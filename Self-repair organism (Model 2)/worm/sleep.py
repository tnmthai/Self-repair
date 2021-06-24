import time
import sys


def sleep():
    for remaining in range(10, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("Regeneration in {:2d} seconds.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    
    sys.stdout.write("\rComplete!                                        \n")   