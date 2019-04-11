"""
:author: Gatsby Lee
:since: 2019-04-05
"""

from mq.redis_queue import RedisQueue
from mq.exceptions import Empty
__VERSION__ = '0.2.2'


__all__ = (
    'RedisQueue',
    'Empty',
)
