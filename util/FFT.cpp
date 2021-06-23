/*
 * @Author: sajuuk
 * @Date: 2021-06-22 20:55:44
 * @LastEditTime: 2021-06-23 16:35:46
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \FFTGIFgenerater\util\FFT.cpp
 */
#include "FFT.h"
/**
 * @description: initialize the twiddle factor list and store the number of samples
 * @param {int} N number of samples
 * @return {*}
 */
void init(int n)
{
    N = n;
    twiddleFactor = (complexNum*)malloc(sizeof(complexNum) * n);
    complexNum temp=complexNum(1,0);
    complexNum f=complexNum(cos(2*PI/n),-sin(2*PI/n));
    for (int i = 0; i < n; i++)
    {
        twiddleFactor[i]=temp;
        temp=temp*f;
    }
}
/**
 * @description: get the twiddle factor w(n,k)
 * @param {int} n, the primitive Nth root of unity
 * @param {int} k, power
 * @return {complexNum} the twiddle factor
 */
complexNum getTwiddlefactor(int n, int k)
{
    int t=N/n;
    return twiddleFactor[k*t];//normalize the twiddle factor and query the factor list
}
/**
 * @description: Fast fourier transform
 * @param {int} n,number of samples
 * @param {float*} pointer of input array, 
 * @return {*}
 */
void ffTrans(int n, complexNum* input, complexNum* output)
{
    if (n == 1)
    {
        (*output) = (*input);
        return;
    }
    complexNum* xEven = (complexNum*)malloc(sizeof(complexNum) * (n / 2));
    complexNum* xOdd = (complexNum*)malloc(sizeof(complexNum) * (n / 2));
    for (int i = 0; i < n; i++)
    {
        if (i % 2) //i is odd
        {
            xOdd[i / 2] = input[i];
        }
        else
        {
            xEven[i / 2] = input[i];
        }
    }
    complexNum* a = (complexNum *)malloc(sizeof(complexNum) * (n / 2));
    complexNum* b = (complexNum *)malloc(sizeof(complexNum) * (n / 2));
    ffTrans(n / 2, xEven, a);
    ffTrans(n / 2, xOdd, b);
    free(xEven);
    free(xOdd);
    for (int i = 0; i < n / 2; i++)
    {
        b[i]=getTwiddlefactor(n,i)*b[i];
        output[i]=a[i]+b[i];
        output[i+n/2]=a[i]-b[i];
    }
    free(a);
    free(b);
}