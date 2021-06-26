# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 22:30:46 2021

@author: 39106
"""
from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import numpy as np
from ctypes import *
class complexNum(Structure):
    _fields_=[('r',c_float),('j',c_float)]
class draw:
    def __init__(self):
        self.status='idle'
        plt.figure(figsize=(6,4))
        plt.xlim((0,600))
        plt.ylim((0,400))
        plt.connect('button_release_event',self.onClick)
        plt.connect('motion_notify_event',self.onMove)
    def getDis(self,x,y):
        dis=np.sqrt((self.nx-x)**2+(self.ny-y)**2)
        return dis
    def transTocomplex(x,y):
        for x1,y1 in zip(x,y):
            
    def onClick(self,event):
        if event.button is MouseButton.LEFT:
            if self.status=='idle':
                self.xList=np.empty([0,1])
                self.yList=np.empty([0,1])
                self.nx=event.xdata
                self.ny=event.ydata
                self.xList=np.append(self.xList,[event.xdata,event.xdata])
                self.yList=np.append(self.yList,[event.ydata,event.ydata])
                self.status='drawing'
                plt.plot(self.xList,self.yList,'r')
                print('drawing')
                print(self.xList)
            else:
                self.status='idle'
                
    def onMove(self,event):
        if self.status=='drawing' and self.getDis(event.x,event.y) > 10:
            self.xList=np.insert(self.xList,-1,event.xdata)
            self.yList=np.insert(self.yList,-1,event.ydata)
            plt.cla()
            plt.xlim((0,600))
            plt.ylim((0,400))
            plt.plot(self.xList,self.yList,'r')
            plt.draw()
            self.nx=event.xdata
            self.ny=event.ydata
            print('detected move')
            print(self.xList)
                
        
if __name__ =='__main__':
    d=draw()