class Snake:
    def __init__(self,start,end):
        self.start=start
        self.end=end

    def move_to_end(self):
        print(f"(climbs a ladder from {self.start} to {self.end})")
        return self.end