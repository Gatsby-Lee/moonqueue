"""
:author: Gatsby Lee
:since: 2019-04-04
"""
import logging
import redis


LOGGER = logging.getLogger(__name__)


class RedisQueue(object):

    def __init__(self, default_qname: str, redis_config: dict = {}):
        self.r = redis.StrictRedis(**redis_config)
        self._default_qname = default_qname

    def push(self, serialized_msgs: list, qname: str = None):
        """
        Push msg into Queue

        Args:
            msg: serialized message
            qname: queue name where message is pushed. ( optional )
        """
        _qname = qname if qname else self._default_qname
        self.r.lpush(_qname, *serialized_msgs)

    def pop(self, qname: str = None) -> tuple:
        """
        Args:
            qname: queue name where message is popped. ( optional )
        Returns:
            tuple (qname, [serialized_msg])
        """
        _qname = qname if qname else self._default_qname
        _msg = self.r.rpop(_qname)
        return (_qname, [_msg])

class RedisPollQueue(object):

    def __init__(self, default_qname: list, redis_config: dict):
        self.r = redis.StrictRedis(**redis_config)
        self._default_qname = default_qname

    def push(self, serialized_msgs: list, qname: str = None):
        """
        Push msg into Queue

        Args:
            msg: serialized message
            qname: queue name where message is pushed. ( optional )
        """
        _qname = qname if qname else self._default_qname
        self.r.lpush(_qname, *serialized_msgs)

    def pop(self, qnames: list, waittime_second=0):
        """
        Args:
            qnames: list of queue names to poll to pop
            waittime_second: wait
        Returns:
            tuple (qname, serialized_msg)
        """
        _qname = qname if qname else self._default_qname
        return self.r.brpop(_qname, timeout=waittime_second)


__all__ = (
    'RedisQueue',
    'RedisPollQueue',
)
