from abc import ABC, abstractmethod


class BasicWorker(ABC):
    @abstractmethod
    def work(self):
        pass


class Worker(BasicWorker):

    def work(self):
        print("I'm working!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, BasicWorker):
            return f'`worker` must be of type {BasicWorker}'
        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


class SuperWorker(BasicWorker):

    def work(self):
        print("I work very hard!!!")


worker = Worker()

manager = Manager()

manager.set_worker(worker)

manager.manage()

super_worker = SuperWorker()

try:

    manager.set_worker(super_worker)

    manager.manage()

except AssertionError:

    print("manager fails to support super_worker....")
