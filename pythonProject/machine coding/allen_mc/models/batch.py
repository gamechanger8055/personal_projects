class Batch:
    def __init__(self, admin, capacity, stream, timing):
        self.admin = admin
        self.capacity = capacity
        self.stream = stream
        self.timing = timing
        self.students = []
