import time

class Timer:
    def __init__(self):
        self.start_time = time.time()
        self.stop_time = self.start_time
        self.intermediate_time = self.start_time
        self.switch = False
        self.str_format = "%Hh %Mmin %Ss"
        
    def start(self):
        self.start_time = time.time()
        self.switch = True
        
    def stop(self):
        self.stop_time = time.time()
        self.switch = False

    def start_lap(self):
        if self.switch:
            self.intermediate_time = time.time()
            
    def time(self):
        if self.switch:
            t = time.time() - self.start_time
        else:
            t = self.stop_time - self.start_time
        return time.strftime(self.str_format,time.gmtime(t))
    
    def lap_time(self, output_str=True):
        t = 0
        if self.switch:
            t = time.time() - self.intermediate_time
        if output_str:
            return time.strftime(self.str_format,time.gmtime(t))
        else: return t
