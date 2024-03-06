from observee.subject import Subject


class WeatherData(Subject):
    def __init__(self):
        self.temp=0.0
        self.observers=[]

    def add_obervers(self,observer):
        self.observers.append(observer)

    def remove_observer(self,observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def set_measurements(self,temperature):
        self.temp=temperature
        self.notify()