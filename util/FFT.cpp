/*
 * @Author: sajuuk
 * @Date: 2021-06-22 20:55:44
 * @LastEditTime: 2021-06-23 10:46:44
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \FFTGIFgenerater\util\FFT.cpp
 */
#include "FFT.h"
/**
 * @description: 
 * @param {int} n, the primitive Nth root of unity
 * @param {int} k, power
 * @return {complexNum} the twiddle factor
 */
complexNum getTwiddlefactor(int n,int k)
{
    
}
/**
 * @description: Fast fourier transform
 * @param {int} n,number of samples
 * @param {float*} pointer of input array, 
 * @return {*}
 */
void ffTrans(int n,complexNum* input,complexNum* output)
{
    if(n==1) 
    {
        (*output)=(*input);
        return;
    }
    complexNum* xEven=(complexNum*)malloc(sizeof(complexNum)*(n/2));
    complexNum* xOdd=(complexNum*)malloc(sizeof(complexNum)*(n/2));
    for (int i=0;i<n;i++)
    {
        if (i%2) //i is odd
        {
            xOdd[i/2]=input[i];
        }
        else
        {
            xEven[i/2-1]=input[i];
        }
    }
    complexNum* a=(complexNum*)malloc(sizeof(complexNum)*(n/2));
    complexNum* b=(complexNum*)malloc(sizeof(complexNum)*(n/2));
    ffTrans(n/2,xEven,a);
    ffTrans(n/2,xOdd,b);
    for (int i=0;i<n/2;i++)
    {

    }
}