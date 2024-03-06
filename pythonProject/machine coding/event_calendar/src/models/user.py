class User:
    def __init__(self,name,start_time,end_time):
        self.name=name
        self.start=start_time
        self.end=end_time
        self.is_available=True
        self.events=[]

