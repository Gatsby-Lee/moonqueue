"""
:author: Gatsby Lee
:since: 2019-04-10
"""
import pytest

from moonqueue import RedisQueueSet
from moonqueue.excep import EmptyQueueException


def test_object_creation():
    assert RedisQueueSet('mq.test')


def test_push_to_one_queue():
    qnames = 'mq.test.1'
    r = RedisQueueSet(qnames)
    r.delete_queues()

    msg = 'string msg'
    response = r.push([msg])
    assert response == ((qnames, 1),)
    assert r._redis.scard(qnames) == 1
    assert r._redis.sismember(qnames, 'string msg')


def test_push_to_one_queues_inited_list_qnames():
    qnames = ['mq.test.list.1']
    r = RedisQueueSet(qnames)
    r.delete_queues()

    msg = 'string msg'
    response = r.push([msg])
    assert response == ((qnames[0], 1),)
    assert r._redis.scard(qnames[0]) == 1
    assert r._redis.sismember(qnames[0], 'string msg')


def test_push_to_one_queues_inited_tuple_qnames():
    qnames = ('mq.test.tuple.1',)
    r = RedisQueueSet(qnames)
    r.delete_queues()

    msg = 'string msg'
    response = r.push([msg])
    assert response == ((qnames[0], 1),)
    assert r._redis.scard(qnames[0]) == 1
    assert r._redis.sismember(qnames[0], 'string msg')


def test_push_to_two_queues():
    qnames = ['mq.test.list.2-1', 'mq.test.list.2-2']
    r = RedisQueueSet(qnames)
    r.delete_queues()

    response = r.push(['string msg'])
    assert response == ((qnames[0], 1), (qnames[1], 1))
    assert r._redis.scard(qnames[0]) == 1
    assert r._redis.sismember(qnames[0], 'string msg')
    assert r._redis.scard(qnames[1]) == 1
    assert r._redis.sismember(qnames[1], 'string msg')


def test_pop_when_one_queue():
    qnames = 'mq.test.pop.1'
    r = RedisQueueSet(qnames)
    r.delete_queues()

    msg = 'string msg'
    r.push([msg])

    response = r.pop()
    assert response == (qnames, b'string msg')
    assert r._redis.scard(qnames) == 0


def test_pop_when_two_queues():
    qnames = ['mq.test.pop.1', 'mq.test.pop.2']
    r = RedisQueueSet(qnames)
    r.delete_queues()

    msg = 'string msg'
    r.push([msg])

    response = r.pop()
    assert response == (qnames[0], b'string msg')
    assert r._redis.scard(qnames[0]) == 0
    assert r._redis.scard(qnames[1]) == 1


def test_pop_when_two_queues_but_only_last_queue_has_one():
    qnames = ['mq.test.pop.1', 'mq.test.pop.2']
    r = RedisQueueSet(qnames)
    r.delete_queues()

    msg = 'string msg'
    r.push([msg])
    r._redis.delete(qnames[0])

    assert r._redis.scard(qnames[0]) == 0

    response = r.pop()
    assert response == (qnames[1], b'string msg')
    assert r._redis.scard(qnames[1]) == 0


def test_pop_when_one_queue_but_empty():
    qnames = 'mq.test.pop.empty.1'
    r = RedisQueueSet(qnames)
    r.delete_queues()

    with pytest.raises(EmptyQueueException):
        r.pop()


def test_pop_when_two_queue_but_empty():
    qnames = ['mq.test.pop.empty.1', 'mq.test.pop.empty.2']
    r = RedisQueueSet(qnames)
    r.delete_queues()

    with pytest.raises(EmptyQueueException):
        r.pop()
