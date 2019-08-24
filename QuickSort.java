import java.util.Arrays;

public class QuickSort
{
    public static void quickSort(int[] array,int first,int end)
    {
        if(first>=end)
            return;
        int midValue = array[first];
        int low = first;
        int high = end;
        while(low<high)
        {
            if(low<high && array[high]>=midValue)
                high--;
            array[low] = array[high];
            if(low<high && array[low]<midValue)
                low++;
            array[high] = array[low];
        }
        array[low] = midValue;
        quickSort(array, first, low-1);
        quickSort(array, low+1, end);   
    }

    public static void main(String[] args) {
        int[] test = {2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12};
        quickSort(test,0,test.length-1);
        System.out.println(Arrays.toString(test));
    }
}

