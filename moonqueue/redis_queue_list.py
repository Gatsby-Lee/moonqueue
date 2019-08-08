"""
:author: Gatsby Lee
:since: 2019-04-04
"""
from moonqueue import RedisQueue
from moonqueue.excep import EmptyQueueException


class RedisQueueList(RedisQueue):

    def push(self, serialized_msgs):
        """
        Push ``serialized_msgs``

        Args:
            serialized_msgs (list): serialized message
        Returns:
            tuple(tuple(queue_name, queue_length), .. )
        """
        assert isinstance(serialized_msgs, list), 'serialized_msgs must be list type.'

        ret_val = None
        if self._is_multiq:
            pipeline = self._redis.pipeline()
            for _qname in self._qnames:
                pipeline.lpush(_qname, *serialized_msgs)
            res = pipeline.execute()
            ret_val = tuple([(q, qsize) for q, qsize in zip(self._qnames, res)])
        else:
            qlenth = self._redis.lpush(self._qnames, *serialized_msgs)
            ret_val = ((self._qnames, qlenth),)
        return ret_val

    def pop(self):
        """
        Remove and return item in ``queue``

        Returns:
            tuple(qname, serialized_msg)
        """
        if self._is_multiq:
            for _qname in self._qnames:
                _serialized_msg = self._redis.rpop(_qname)
                if _serialized_msg is not None:
                    return (_qname, _serialized_msg)
        else:
            _serialized_msg = self._redis.rpop(self._qnames)
            if _serialized_msg is not None:
                return (self._qnames, _serialized_msg)

        excep_msg = '%s is empty' % self._qnames
        raise EmptyQueueException(excep_msg)
