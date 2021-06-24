# -*- coding: utf-8 -*-
"""
Created on Sat Apr 06 21:53:15 2019

@author: trann5
"""

import time
import sys

def sleep():
    s = '.'
    sys.stdout.write( 'Repairing' )
    for remaining in range(10, 0, -1):
            sys.stdout.write( s )
            sys.stdout.flush()
            time.sleep(0.5)