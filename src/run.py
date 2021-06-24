# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 20:51:47 2021

@author: 39106
"""

from ctypes import *
def main():
    FFTdll=CDLL('F:\\DA\\FFTGIFgenerater\\src\\FFT.dll')
    print(FFTdll)
if __name__ == "__main__":
    main()