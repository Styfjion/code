#include <iostream>
#include <algorithm>
#include <cstdlib>
using namespace std;

void heapify_build(int data[],int start,int end)
{
    int root = start;
    while(true)
    {
        int child = root*2 + 1;
        if(child > end)
            return;
        if (child+1 <= end && data[child] < data[child+1])
            child++;
        if (data[child]>data[root])
        {
            swap(data[child],data[root]);
            root = child;
        }
        else
            return;
    }
}

void heapify_sort(int data[],int length)
{
    int start = length/2 - 1;
    for(int i=start;i>=0;i--)
        heapify_build(data,i,length-1);
    for(int j=length-1;j>0;j--)
    {
        swap(data[j],data[0]);
        heapify_build(data,0,j-1);
    }
}

int main(int argc, char const *argv[])
{
    int arr[] = { 3, 5, 3, 0, 8, 6, 1, 5, 8, 6, 2, 4, 9, 4, 7, 0, 1, 8, 9, 7, 3, 1, 2, 5, 9, 7, 4, 0, 2, 6 };
    int length = (int)sizeof(arr)/sizeof(arr[0]);
    heapify_sort(arr,length);
    for(int i=0;i<length;i++)
        cout<<arr[i]<<" ";
    system("pause");
    return 0;
}
