import java.util.Arrays;

public class Heapify
{
    public static void swap(int[] array, int s, int t) 
    {
        int temp = array[s];
        array[s] = array[t];
        array[t] = temp;
    }
    public static void bigHeapify(int[] array,int begin, int end)
    {
        int root = begin;
        while(true)
        {
            int child = root*2+1;
            if(child>=end)
                break;
            if(child+1<=end && array[child+1]>array[child])
                child++;
            if(array[root]<array[child])
            {
                swap(array, root, child);
                root = child;
            }
            else
                break;   
        }
    }
    public static void heapifySort(int[]array)
    {
        int mid = (int)array.length/2 - 1;
        for(int first=mid;first>=0;first--)
            bigHeapify(array, first, array.length-1);
        for(int end = array.length-1;end>0;end--)
        {
            swap(array, 0, end);
            bigHeapify(array, 0, end-1);
        }
    }
    public static void main(String[] args) {
        int arr[] = { 3, 5, 3, 0, 8, 6, 1, 5, 8, 6, 2, 4, 9, 4, 7, 0, 1, 8, 9, 7, 3, 1, 2, 5, 9, 7, 4, 0, 2, 6 };
        heapifySort(arr);
        System.out.println(Arrays.toString(arr));
    }
}