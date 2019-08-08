.. image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. image:: https://badge.fury.io/py/cloud-storage.svg
    :target: https://badge.fury.io/py/cloud-storage

.. image:: https://img.shields.io/travis/Gatsby-Lee/moonqueue.svg
   :target: https://travis-ci.org/Gatsby-Lee/moonqueue


moonqueue
=========

MoonQueue is another Queue Library using Redis as storage.


How to Install
--------------

.. code-block:: bash

    pip install moonqueue


How To Use - Redis
----------

.. code-block:: python

    >>> from mq import RedisQueue
    >>> r = RedisQueue('list:default')


    # push one message. tuple(queue_name, queue_length) will be returned.
    >>> r.push(['apple'])
    ('list:default', 1)
    >>> r.pop()
    ('list:default', (b'apple',))


    # push multiple messages
    >>> r.push(['apple', 'banana'])
    ('list:default', 2)
    >>> r.pop()
    ('list:default', (b'apple',))
    >>> r.pop()
    ('list:default', (b'banana',))


    # Empty exception will raise if queue is empty.
    >>> r.pop()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/home/web/moonqueue/mq/redis_queue.py", line 45, in pop
        raise Empty(excep_msg)
    mq.exceptions.Empty: list:default is empty


    # polling if queues are empty. ( multiple queues can be used. )
    >>> r.push(['apple'])
    ('list:default', 1)
    >>> r.poll_pop()
    (b'list:default', (b'apple',))


    # possible to poll with multiple queues
    >>> r.poll_pop(['list:test1', 'list:test2'])


    # possible to poll with timeout. ( default: indefinite )
    >>> r.poll_pop(['list:test1'], timeout=1)


    # Empty exception will raise if queue is empty within timeout.
    >>> r.poll_pop(['list:test1', 'list:test2'], timeout=1)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/home/web/moonqueue/mq/redis_queue.py", line 69, in poll_pop
        raise Empty(excep_msg)
    mq.exceptions.Empty: ['list:test1', 'list:test2'] is empty
<<<<<<< Updated upstream
=======


CHANGES
=======

0.2.2
-----

* Relesae Date: 2019-04-19
* Add retry decorator
* Add interface class

0.2.1
-----

* Date: 2019-04-10
* Add test cases
* Add travis.yml to use travis CI


0.2.0
-----

* Date: 2019-04-08
* Raise Empty exception if queue is empty.
* Change return format from ``pop`` and ``poll_pop``

0.1.2
-----

* Date: 2019-04-08
* Update README.rst with 'how to install'
* Add CHANGES.rst


0.1.1
-----

* Date: 2019-04-05
* Update README.rst with 'how to install'
* Add CHANGES.rst


0.1
---

* Date: 2019-04-05
* Initial version with supporting RedisQueue, RedisPollQueue
>>>>>>> Stashed changes
