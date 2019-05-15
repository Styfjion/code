#include <cstdlib>
#include <iostream>
#include <stdexcept>
using namespace std;

void Swap(int* a1, int* a2)
{
    int temp;
    temp = *a2;
    *a2 = *a1;
    *a1 = temp;
}

int Partition(int data[], int length, int start, int end)
{
    if(data==nullptr||length<=0||start<0||end>=length)
     {
        std::logic_error ex("Invalid Input");
        throw std::exception(ex);
     }  
    int index = rand()%(end-start+1) + start;
    Swap(&data[index],&data[end]);
    int small = start - 1;
    for(index=start;index<end;index++)
    {
        if(data[index]<data[end])
        {
            small++;
            if(small!=index)
                Swap(&data[index],&data[small]);
        }
    }
    small++;
    Swap(&data[small],&data[end]);
    return small;
}

void QuickSort(int data[], int length, int start, int end)
{
    if(start==end)
        return;
    int index = Partition(data,length,start,end);
    if(index>start)
        QuickSort(data,length,start,index-1);
    if(index<end)
        QuickSort(data,length,index+1,end);
}
int main()
{
    int data[] = {0,4,5,7,9,0,3,4};
    QuickSort(data,8,0,7);
    for(int i=0;i<8;i++)
        cout<<data[i]<<" ";
    system("pause");
    return 0;
}