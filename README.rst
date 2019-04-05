moonqueue
=========

Author: Gatsby

Since: 2019-04-04


How to Install
--------------

.. code-block:: bash

    pip install moonqueue


How To Use
----------

.. code-block:: python

    >>> from mq import RedisQueue
    >>> r = RedisQueue('hello')
    >>> r.push(['apple'])
    >>> r.pop()
    ('hello', [b'apple'])

    # Multiple message can be pushed
    >>> r.push(['apple', 'banana'])
    >>> r.pop()
    ('hello', [b'apple'])
    >>> r.pop()
    ('hello', [b'banana'])


Supported Message Storage
------------------------

* Redis

