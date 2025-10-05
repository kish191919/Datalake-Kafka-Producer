


BROKER_LIST = 'kafka01:9092,kafka02:9092,kafka03:9092'

class BicycleProducer():
    def __init__(self, topic):
        self.topic = top