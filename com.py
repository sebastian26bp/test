# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:42:13 2023

@author: Sebastian Barroso
"""

import sys
  
  
print("This is the name of the program:",
       sys.argv[0])
print("Number of elements including the name of the program:",
       len(sys.argv))
print("Number of elements excluding the name of the program:",
      (len(sys.argv)-1))
print("Argument List:",
       str(sys.argv))