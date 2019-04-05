moonqueue
=========

Author: Gatsby

Since: 2019-04-04

How To Use
----------

.. code-block:: python

    >>> from mq import RedisQueue
    >>> r = RedisQueue('hello')
    >>> r.push(['world'])
    >>> r.pop()
    ('hello', [b'world'])


Supported Message Storage
------------------------

* Redis

