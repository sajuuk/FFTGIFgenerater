# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 20:51:47 2021

@author: 39106
"""

from ctypes import *
class complexNum(Structure):
    _fields_=[('r',c_float),('j',c_float)]
def main():
    FFTdll=CDLL('F:\\DA\\FFTGIFgenerater\\build\\libFFT.dll')
    print(FFTdll)
    FFTdll.init(c_int(8))
    datastore=complexNum*8
    inputdata=datastore()
    outputdata=datastore()
    for i in inputdata:
        i.r=int(input())
        i.j=int(input())
    fft=FFTdll.ffTrans(c_int(8),pointer(inputdata),pointer(outputdata))
    for i in outputdata:
        print("{0}+{1}i".format(i.r,i.j))
if __name__ == "__main__":
    main()