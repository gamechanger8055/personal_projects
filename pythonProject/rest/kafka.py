import threading
import queue

class MessageBroker:
    def __init__(self):
        self.message_queue=queue.Queue()
        self.topics={}

    def create_topic(self,topic):
        if topic not in self.topics:
            self.topics[topic]=[]

    def publish_message(self,topic,message):
        if topic in self.topics:
            self.message_queue.put((topic,message))

    def subscribe_message(self,topic,subscriber):
        if topic in self.topics:
            self.topics[topic].append(subscriber)

    def start_delivery_thread(self):
        delivery_thread = threading.Thread(target=self._deliver_messages)
        delivery_thread.daemon = True
        delivery_thread.start()

    def _deliver_messages(self):
        while True:
            topic, message = self.message_queue.get()
            if topic in self.topics:
                for subscriber in self.topics[topic]:
                    subscriber.receive_message(message)
            self.message_queue.task_done()

class Publisher:
    def __init__(self, message_broker):
        self.message_broker = message_broker

    def publish(self, topic, message):
        self.message_broker.publish_message(topic, message)

class Subscriber:
    def __init__(self,name, message_broker):
        self.name=name
        self.message_broker=message_broker

    def subscribe(self,topic):
        self.message_broker.subscribe_message(topic,self)

    def receive_message(self, message):
        print(f"{self.name} received message: {message}")


if __name__ == "__main__":
    message_broker = MessageBroker()
    message_broker.create_topic("topic1")

    publisher = Publisher(message_broker)
    subscriber1 = Subscriber("Subscriber1", message_broker)
    subscriber2 = Subscriber("Subscriber2", message_broker)

    subscriber1.subscribe("topic1")
    subscriber2.subscribe("topic1")

    message_broker.start_delivery_thread()

    publisher.publish("topic1", "Message 1")
    publisher.publish("topic1", "Message 2")

    message_broker.message_queue.join()

