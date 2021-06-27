# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 22:30:46 2021

@author: 39106
"""
from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from ctypes import *
class complexNum(Structure):
    _fields_=[('r',c_float),('j',c_float)]
class draw:
    def __init__(self):
        self.status='idle'
        plt.figure(figsize=(12,8))
        plt.xlim((0,1200))
        plt.ylim((0,800))
        plt.connect('button_release_event',self.onClick)
        plt.connect('motion_notify_event',self.onMove)
    def initFFT(self,n):
        dll=CDLL("../build/libFFT.dll")
        dll.init(c_int(n))
        fft=dll.ffTrans
        return fft
    def getDis(self,x,y):
        dis=np.sqrt((self.nx-x)**2+(self.ny-y)**2)
        return dis
    def createComplexarray(self,n):
        complexArray=complexNum*n
        t=complexArray()
        return t
    def transTocomplex(self,x,y,n):
        complexArray=self.createComplexarray(n)
        #create complex number array
        i=0
        #print('debug in tanrsTocomplex')
        for x1,y1 in zip(x,y):
            complexArray[i].r=x1
            complexArray[i].j=y1
            #print("x1:{0} y1:{1} r:{2} j:{3}".format(x1,y1,complexArray[i].r,complexArray[i].j))
            i=i+1
        return complexArray
    def extendArray(self,inputList):
        n=len(inputList)
        low=0
        high=1
        while n<low or n>high:
            low=high
            high=high*2
        exn=high
        for i in range(n,exn):
            inputList=np.append(inputList,inputList[0])
        #print('debug:in extendArray')
        #print(inputList)
        return inputList
    def animateUpdate(self,num):
        N=len(self.mods)
        dt=1/200
        x=0
        y=0
        linex=[]
        liney=[]
        for i in range(0,N):
            x=x+self.mods[i]*np.cos(self.angles[i])
            y=y+self.mods[i]*np.sin(self.angles[i])
            f=((i+N/2)%N)-N/2
            self.angles[i]=self.angles[i]+2*np.pi*f*dt
            linex.append(x)
            liney.append(y)
            self.circles['pos'][i,0]=x
            self.circles['pos'][i,1]=y
            if i<N-1:
                self.circles['size'][i]=self.mods[i+1]
            self.scats.set_offsets(self.circles['pos'])
            self.scats.set_sizes(self.circles['size']**2*1.25)
            #print("{0},{1}".format(x,y))
        self.tracex.append(x)
        self.tracey.append(y)
        self.trace.set_data(self.tracex,self.tracey)
        self.line.set_data(linex,liney)
        return self.trace,self.line,self.scats
    def createAnimate(self,cList):
        fig=plt.figure(figsize=(12,8))
        ax=fig.add_subplot(autoscale_on=False, xlim=(0, 1200), ylim=(0, 800))
        self.tracex=[]
        self.tracey=[]
        self.mods=[]
        self.angles=[]
        N=len(cList)
        self.circles=np.zeros(N,dtype=[('pos',float,(2,)),
                                  ('size',float,)])
        for c in cList:
            self.mods.append(np.sqrt(c.r**2+c.j**2)/N)
            self.angles.append(np.arctan2(c.j,c.r))
        
        self.trace, =ax.plot(self.tracex,self.tracey,lw=2.5)
        self.line, =ax.plot([],[],lw=1)
        self.scats=ax.scatter(self.circles['pos'][:,0],self.circles['pos'][:,1],s=self.circles['size'],facecolors='none',edgecolors=(0.3,0.2,0.1),lw=0.5)
        self.ani=animation.FuncAnimation(fig,self.animateUpdate,range(0,N),interval=50,blit=True)
        plt.show()
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
                #print(self.xList)
            else:
                self.status='idle'
                self.xList=self.extendArray(self.xList)
                self.yList=self.extendArray(self.yList)
                n=len(self.xList)
                print('sanmples:{0}'.format(n))
                inputArray=self.transTocomplex(self.xList,self.yList,n)
                outputArray=self.createComplexarray(n)
                fft=self.initFFT(n)
                fft(c_int(n),pointer(inputArray),pointer(outputArray))
                self.createAnimate(outputArray)
    def onMove(self,event):
        if self.status=='drawing' and self.getDis(event.x,event.y) > 5:
            self.xList=np.insert(self.xList,-1,event.xdata)
            self.yList=np.insert(self.yList,-1,event.ydata)
            plt.cla()
            plt.xlim((0,1200))
            plt.ylim((0,800))
            plt.plot(self.xList,self.yList,'r')
            plt.draw()
            self.nx=event.xdata
            self.ny=event.ydata
            print('detected move')
            #print(self.xList)
                
        
if __name__ =='__main__':
    d=draw()