"""
:author: Gatsby Lee
:since: 2019-04-10
"""
import pytest

from mq import RedisQueue
from mq.exceptions import Empty


def test_object_creation_with_default_value():
    """
    Test that RedisQueue instance could be created with
    default value argument.
    """
    RedisQueue("mq.test")


def test_push_one():
    """
    Test return value of pushing one message
    """
    default_qname = "mq.test_push_one"
    q = RedisQueue(default_qname)
    _qname, _qlength = q.push(['apple'])
    assert _qname == default_qname
    assert type(_qlength) == int
    assert _qlength == 1


def test_push_unicode_qname():
    """
    Test push
    """
    default_qname = "mq.push_unicode_큐"
    q = RedisQueue(default_qname)
    _qname, _qlength = q.push(['apple'])
    assert _qname == default_qname
    assert type(_qlength) == int
    assert _qlength == 1


def test_push_bytes_qname():
    """
    Test push
    """
    default_qname = "mq.push_bytes_큐".encode()
    q = RedisQueue(default_qname)
    _qname, _qlength = q.push(['apple'])
    assert _qname == default_qname
    assert type(_qlength) == int
    assert _qlength == 1


def test_push_multiple():
    """
    Test push multiple messages
    """
    default_qname = "mq.test_push_multiple"
    q = RedisQueue(default_qname)
    _qname, _qlength = q.push(['apple', 'banana', 'orange'])
    assert _qname == default_qname
    assert _qlength == 3


def test_pop_from_empty_queue():
    """
    Test raised Empty exception.
    """
    default_qname = "mq.test_push_from_empty_queue"
    q = RedisQueue(default_qname)
    with pytest.raises(Empty):
        q.pop()


def test_push_and_pop():
    """
    Test push
    """
    default_qname = "mq.test_push_one"
    msg = 'apple'
    q = RedisQueue(default_qname)
    q.push([msg])
    _qname, _msgs = q.pop()

    # returned msg is bytes type
    assert _qname == default_qname
    assert type(_msgs) is tuple
    assert type(_msgs[0]) is bytes
    assert _msgs == (msg.encode(),)


def test_push_and_pop_unicode_qname():
    """
    Test push
    """
    default_qname = "mq.test_push_and_pop_unicode_qname_큐"
    msg = 'apple'
    q = RedisQueue(default_qname)
    q.push([msg])
    _qname, _msgs = q.pop()

    # returned msg is bytes type
    assert _qname == default_qname
    assert type(_msgs) is tuple
    assert type(_msgs[0]) is bytes
    assert _msgs == (msg.encode(),)


def test_push_and_pop_with_qname_param():
    """
    Test push
    """
    default_qname = "mq.test_push_and_pop_with_qname_param_default"
    msg = 'apple'
    qname_param = 'mq.test_push_and_pop_with_qname_param'
    q = RedisQueue(default_qname)
    q.push([msg], qname=qname_param)
    _qname, _msgs = q.pop(qname=qname_param)

    # returned msg is bytes type
    assert _qname == qname_param
    assert _msgs == (msg.encode(),)


def test_push_and_pollingpop():
    """
    Test push
    """
    default_qname = "mq.test_push_and_pollingpop"
    msg = 'apple'
    q = RedisQueue(default_qname)
    q.push([msg])
    _qname, _msgs = q.poll_pop()

    # returned msg is bytes type
    assert _qname == default_qname.encode()
    assert _msgs == (msg.encode(),)
