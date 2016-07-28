# -*- coding: utf-8 -*-
from __future__ import print_function
from Queue import Queue
from threading import Thread, Lock

PRINT_LOCK = Lock()


def printf(*args, **kwargs):
    with PRINT_LOCK:
        print(*args, **kwargs)


class Worker(Thread):
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kwargs = self.tasks.get()
            try:
                func(*args, **kwargs)
            except Exception, e:
                printf(e)
            self.tasks.task_done()


class Threadpool:
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for count in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kwargs):
        self.tasks.put((func, args, kwargs))

    def wait_completion(self):
        self.tasks.join()
