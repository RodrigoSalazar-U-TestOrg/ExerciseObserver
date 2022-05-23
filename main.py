from abc import ABC, abstractmethod


class Subject(ABC):

    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class Observer(ABC):

    @abstractmethod
    def update(self, subject):
        pass


class WeatherStation(Subject):

    def __init__(self, humidity=0, temperature=0, pressure=0):
        self.observers = []
        self.humidity = humidity
        self.temperature = temperature
        self.pressure = pressure

    def set_humidity(self, humidity):
        self.humidity = humidity
        self.notify_observers()

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify_observers()

    def set_pressure(self, pressure):
        self.pressure = pressure
        self.notify_observers()

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for obs in self.observers:
            obs.update(self)


class CurrentObserver(Observer):
    def __init__(self):
        self.current = 0

    def update(self, subject):
        self.current = subject.temperature * subject.pressure

    def __str__(self):
        return str(self.current)


class StatisticsObserver(Observer):
    def __init__(self):
        self.statistics = "No Statistics"

    def update(self, subject):
        self.statistics = "H:{} T:{} P:{}".format(subject.humidity, subject.temperature, subject.pressure)

    def __str__(self):
        return self.statistics


class ForecastObserver(Observer):
    def __init__(self):
        self.forecast = "No Forecast"

    def update(self, subject):
        self.forecast = "Rain" if (subject.humidity * subject.pressure >= 1) else "Clear"

    def __str__(self):
        return self.forecast


class DisplayDevice:
    def __init__(self):
        self.obs_current = CurrentObserver()
        self.obs_statistics = StatisticsObserver()
        self.obs_forecast = ForecastObserver()

    def subscribe_observers(self, subject):
        subject.add_observer(self.obs_current)
        subject.add_observer(self.obs_statistics)
        subject.add_observer(self.obs_forecast)

    def __str__(self):
        return "CURRENT: {} \nSTATISTICS:{} \nFORECAST: {}".format(self.obs_current,
                                                                   self.obs_statistics,
                                                                   self.obs_forecast)


if __name__ == '__main__':
    d = DisplayDevice()
    ws = WeatherStation()
    d.subscribe_observers(ws)
    ws.set_temperature(25)
    ws.set_humidity(0.8)
    ws.set_pressure(1.5)
    print(d)


