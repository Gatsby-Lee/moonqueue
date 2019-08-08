.. image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. image:: https://badge.fury.io/py/moonqueue.svg
    :target: https://badge.fury.io/py/moonqueue

.. image:: https://img.shields.io/travis/Gatsby-Lee/moonqueue.svg
   :target: https://travis-ci.org/Gatsby-Lee/moonqueue


moonqueue
=========

MoonQueue is another Queue Library using Redis as storage.


How to Install
--------------

.. code-block:: bash

    pip install moonqueue


How To Use
----------

RedisQueueList - One Queue
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> from moonqueue import RedisQueueList
    >>> r = RedisQueueList('list:myqueue')

    # push one message
    >>> r.push(['apple'])
    (('list:myqueue', 1),)
    >>> r.pop()
    ('list:myqueue', b'apple')

    # push multiple messages
    >>> r.push(['apple', 'banana'])
    (('list:myqueue', 2),)
    >>> r.pop()
    ('list:myqueue', b'apple')
    >>> r.pop()
    ('list:myqueue', b'banana')
    >>> r.pop()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/home/web/moonqueue/moonqueue/redis_queue_list.py", line 52, in pop
        raise EmptyQueueException(excep_msg)
    moonqueue.excep.EmptyQueueException: list:myqueue is empty


RedisQueueList - Two Queues
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> from moonqueue import RedisQueueList
    >>> r = RedisQueueList(['list:myqueue1', 'list:myqueue2'])
    >>> r.get_queues()
    ['list:myqueue1', 'list:myqueue2']

    # push one message - it will be pused to all queues
    >>> r.push(['apple'])
    (('list:myqueue1', 1), ('list:myqueue2', 1))

    # pop from queues
    >>> r.pop()
    ('list:myqueue1', b'apple')
    >>> r.pop()
    ('list:myqueue2', b'apple')
    >>> r.pop()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/home/web/moonqueue/moonqueue/redis_queue_list.py", line 52, in pop
        raise EmptyQueueException(excep_msg)
    moonqueue.excep.EmptyQueueException: ['list:myqueue1', 'list:myqueue2'] is empty
