/*
 * @Author: your name
 * @Date: 2021-06-23 23:18:14
 * @LastEditTime: 2021-06-24 00:19:43
 * @LastEditors: Please set LastEditors
 * @Description: test FFT
 * @FilePath: \FFTGIFgenerater\util\main.cpp
 */
#include"FFT.h"
#include<cstdio>
#include<iostream>
using namespace std;
complexNum a[256];
complexNum b[256];
int n;
void read()
{
    int r,j;
    cin>>n;
    for (int i=0;i<n;i++)
    {
        cin>>r>>j;
        a[i].r=r;
        a[i].j=j;
    }
}
void test()
{
    init(n);
    ffTrans(n,a,b);
    for (int i=0;i<n;i++)
    {
        cout<<b[i].r<<'+'<<b[i].j<<'i'<<endl;
    }
}
int main()
{
    read();
    test();
    return 0;
}