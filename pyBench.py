import time
import random

disable_timing = False
print_args = False
def timefunc(method):
  ''' runs the function inside a timer and prints details passed to it and time taken \n
    run via\n
    --
    @timefunc \n
    def functionname():\n
    --
    
    must be placed after @staticmethod if used together
  '''
  def wrapper(*args, **kw):
    if disable_timing: return method(*args, **kw)
    s_time = time.time()
    res = method(*args, **kw)
    if print_args:
      print("----- Method:[" + method.__qualname__ + "], ran in", time.time() - s_time, "Seconds," \
          " With args:[", *args, "]")
    else:
      print("----- Method:[" + method.__qualname__ + "], ran in", time.time() - s_time, "Seconds,")
    
    return res
  return wrapper

class timeBlock():
  def __init__(self):
    self.start_time = time.time()
    self.id = str(random.randint(0,10000))
    
  def timing_restart(self):
    self.start_time = time.time()

  def timing_end(self, method_name = ""):
    if method_name == "": method_name=self.id
    print("----- ID:"+self.id+" Method:[" + method_name + "], ran in", time.time() - self.start_time, "Seconds,")

