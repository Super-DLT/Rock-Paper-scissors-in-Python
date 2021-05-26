#import time
from time import time
# get a random time
def random_time():
 return time() - float(str(time()).split('.')[0])
# generate a random number 
def random_range(min, max):
 return int(random_time() * ((max + 1) - min) + min)
