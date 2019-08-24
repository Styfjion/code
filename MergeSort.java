import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
public class MergeSort
{
    public List<Integer> mergeSort(List<Integer> array)
    {
        if(array.size()<=1)
            return array;
        int mid = (int)(array.size())/2;
        List<Integer> left = this.mergeSort(array.subList(0, mid));
        List<Integer> right = this.mergeSort(array.subList(mid, array.size()));
        return this.Merge(left, right);
    }

    public List<Integer> Merge(List<Integer>left, List<Integer>right)
    {
        int i=0;
        int j=0;
        List<Integer> result = new ArrayList<>();
        while(i<left.size()&&j<right.size())
        {
            if((int)left.get(i)<=(int)right.get(j))
            {
                result.add(left.get(i));
                i++;
            }
            else
            {
                result.add(right.get(j));
                j++;
            }
        }
        if(i<left.size())
            result.addAll(left.subList(i, left.size()));
        if(j<right.size())
            result.addAll(right.subList(j, right.size()));
        return result;
    }

    public static void main(String[] args) {
        int[] input = {1, 2, 3, 4, 5, 6, 7, 90, 21, 23, 45};
        List<Integer> inputList = new ArrayList<>();
        for (int unit:input)
            inputList.add(unit);
        MergeSort sol = new MergeSort();
        System.out.println(sol.mergeSort(inputList));
    }
}