/*
 * @Author: your name
 * @Date: 2021-06-22 20:55:44
 * @LastEditTime: 2021-06-23 09:59:19
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \FFTGIFgenerater\util\FFT.h
 */
#ifndef __FFT__
#define __FFT__
#endif

#include<stdio.h>
#include<stdlib.h>
#include<math.h>
struct complexNum
{
    float r;//real part
    float j;//image part
    friend complexNum operator* (complexNum& a,complexNum& b)
    {
        complexNum temp;
        temp.r=a.r*b.r-a.j*b.j;
        temp.j=a.r*b.j+a.j*b.r;
        return temp;
    }
    void operator=(complexNum& a)
    {
        r=a.r;
        j=a.j;
    }
};
extern "C"
{
    void ffTrans(int n,complexNum* input,complexNum* output);
}
