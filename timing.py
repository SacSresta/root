from utils import time_utc
import datetime as dt


class Timing():
    def __init__(self, last_candle):
        self.last_candle = last_candle
        if last_candle is None:
            self.last_candle = time_utc() - dt.timedelta(minutes=10)
        self.ready = False

    def __repr__(self):
        return str(vars(self))
    

if __name__ =="__main__":
    timing_instance = Timing(None)  # Creating an instance of Timing class
    print(timing_instance.last_candle)
    print(time_utc())
    print(dt.timedelta(minutes=10))
