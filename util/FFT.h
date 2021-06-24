/*
 * @Author: your name
 * @Date: 2021-06-22 20:55:44
 * @LastEditTime: 2021-06-24 00:17:43
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \FFTGIFgenerater\util\FFT.h
 */
#pragma once

#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define PI 3.14159265358979323846
struct complexNum
{
    float r;//real part
    float j;//image part
    friend complexNum operator* (const complexNum& a,const complexNum& b)
    {
        complexNum temp(0,0);
        temp.r=a.r*b.r-a.j*b.j;
        temp.j=a.r*b.j+a.j*b.r;
        return temp;
    }
    friend complexNum operator+ (const complexNum& a,const complexNum& b)
    {
        complexNum temp(0,0);
        temp.r=a.r+b.r;
        temp.j=a.j+b.j;
        return temp;
    }
    friend complexNum operator- (const complexNum& a,const complexNum& b)
    {
        complexNum temp(0,0);
        temp.r=a.r-b.r;
        temp.j=a.j-b.j;
        return temp;
    }
    void operator=(const complexNum& a)
    {
        r=a.r;
        j=a.j;
    }
    complexNum(float rr,float jj)
    {
        r=rr;j=jj;
    }
    complexNum()
    {
        
    }
};
extern "C"
{
    void init(int n);
    complexNum getTwiddlefactor(int n,int k);
    void ffTrans(int n,complexNum* input,complexNum* output);
}