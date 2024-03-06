import heapq
import threading

class TaskScheduler:
    def __init__(self, num_workers):
        self.num_workers=num_workers
        self.task_queue=[]
        self.workers=[]
        self.worker_count=0

    def enqueue_task(self,task:Task):
        self.task_queue.append(task)

    def execute(self, handler):
        handler()
        self.worker_count-=1

    def handle(self):
        while self.task_queue:
            if self.worker_count<self.num_workers:
                current_task = self.task_queue.pop(0)
                worker_thread = threading.Thread(target=self.execute(current_task.handle()))
                worker_thread.start()
                self.worker_count+=1






    # def start_workers(self):
    #     for i in range(self.num_workers):
    #         worker_thread=threading.Thread(target=self.handle())
    #         worker_thread.start()
    #         self.workers.append(worker_thread)



