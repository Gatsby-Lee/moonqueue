"""
:author: Gatsby Lee
:since: 2019-04-04
"""
import logging
import redis

from mq.exceptions import Empty


LOGGER = logging.getLogger(__name__)


class RedisQueue(object):

    def __init__(self, default_qname: str, redis_config: dict = {}):
        self.r = redis.StrictRedis(**redis_config)
        self._default_qname = default_qname

    def push(self, serialized_msgs: list, qname: str = None):
        """
        Push ``serialized_msgs`` onto the head of the list ``qname``

        Args:
            msg: serialized message
            qname: queue name where message is pushed. ( optional )
        Returns:
            tuple(queue_name, queue_length)
        """
        _qname = qname if qname else self._default_qname
        qlenth = self.r.lpush(_qname, *serialized_msgs)
        return (_qname, qlenth)

    def pop(self, qname: str = None) -> tuple:
        """
        Remove and return the last item of the ``qname``

        Args:
            qname: queue name where message is popped. ( optional )
        Returns:
            tuple(qname, (serialized_msg,))
        """
        _qname = qname if qname else self._default_qname
        _msg = self.r.rpop(_qname)
        if _msg is None:
            excep_msg = '%s is empty' % _qname
            raise Empty(excep_msg)
        return (_qname, (_msg,))

    def poll_pop(self, qnames: list = None, timeout: int = 0):
        """
        POP a value off of the first non-empty list
        named in the ``qnames`` list.

        If none of the lists in ``qnames`` has a value to POP, then block
        for ``timeout`` seconds, or until a value gets pushed on to one
        of the lists.

        If timeout is 0, then block indefinitely.

        Args:
            qnames: list of queue names to pop
            timeout: wait
        Returns:
            tuple (qname, serialized_msg)
        """
        _qnames = qnames if qnames else [self._default_qname]
        qname_msg_tuple = self.r.brpop(_qnames, timeout=timeout)
        if qname_msg_tuple is None:
            excep_msg = '%s is empty' % _qnames
            raise Empty(excep_msg)
        return (qname_msg_tuple[0], (qname_msg_tuple[1],))


__all__ = (
    'RedisQueue',
)
