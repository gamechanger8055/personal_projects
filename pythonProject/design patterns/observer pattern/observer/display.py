from observer.observer import Observer


class Display(Observer):
    def __init__(self):
        self.temperature=0.0


    def update(self):
        if self.temperature==0.0:
            self.temperature+=30
        self.message()

    def message(self):
        print("current condition: {}".format(self.temperature))

