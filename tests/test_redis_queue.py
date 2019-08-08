"""
:author: Gatsby Lee
:since: 2019-04-10
"""
import pytest

from moonqueue import RedisQueue


def test_object_creation_string_qnames():
    qnames = 'mq.test'
    r = RedisQueue(qnames)
    assert r._qnames == qnames
    assert r._is_multiq is False


def test_object_creation_list_qnames():
    qnames = ['mq.test']
    r = RedisQueue(qnames)
    assert r._qnames == 'mq.test'
    assert r._is_multiq is False

    qnames = ['mq.test', 'mq.test1']
    r = RedisQueue(qnames)
    assert r._qnames == qnames
    assert r._is_multiq is True


def test_object_creation_tuple_qnames():
    qnames = ('mq.test',)
    r = RedisQueue(qnames)
    assert r._qnames == 'mq.test'
    assert r._is_multiq is False

    qnames = ('mq.test', 'mq.test1')
    r = RedisQueue(qnames)
    assert r._qnames == qnames
    assert r._is_multiq is True


def test_object_creation_empty_qnames():
    with pytest.raises(ValueError):
        RedisQueue([])

    with pytest.raises(ValueError):
        RedisQueue(())

    with pytest.raises(ValueError):
        RedisQueue('')
