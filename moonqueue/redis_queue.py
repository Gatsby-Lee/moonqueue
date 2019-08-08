"""
:author: Gatsby Lee
:since: 2019-04-04
"""
from moonqueue import Redis

POSSIBLE_TYPES = (list, tuple, str)


class RedisQueue(object):

    def __init__(self, qnames, redis_kwargs=None):
        """
        Init RedisListQueue

        Args:
            qnames (tuple|str)
            redis_kwargs (dict)
        """
        self._validate_qnames(qnames)

        self.numq = len(qnames)
        qnames_type = type(qnames)
        self._is_multiq = False
        if self.numq and qnames_type is str:
            self._qnames = qnames
        elif self.numq and qnames_type in (list, tuple):
            self._qnames = qnames if self.numq > 1 else qnames[0]
            self._is_multiq = True if self.numq > 1 else False

        if redis_kwargs:
            self._redis = Redis(**redis_kwargs)
        else:
            self._redis = Redis()

    def _validate_qnames(self, qnames, possible_types=POSSIBLE_TYPES):
        numq = len(qnames)
        qnames_type = type(qnames)
        if numq == 0 or qnames_type not in possible_types:
            raise ValueError('qnames must be either non-empty ``tuple(list) of str`` or ``str``')
        elif qnames_type is (tuple, list):
            for _qname in qnames:
                self._validate_qnames(_qname, [str])

    def get_queues(self):
        return self._qnames

    def delete_queues(self):
        if self._is_multiq:
            pipeline = self._redis.pipeline()
            for _qname in self._qnames:
                pipeline.delete(_qname)
            pipeline.execute()
        else:
            self._redis.delete(self._qnames)

    def push(self, serialized_msgs):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError
