import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。
并将P对1000000007取模的结果输出。 即输出P%1000000007
*/
public class Solution {
    public int InversePairs(int [] array) {
        if(array == null || array.length == 0)
            return 0;
        int count = 0;
        int i = 0;
        List<Integer> data = new ArrayList<>();
        for (int unit:array)
            data.add(unit);
        Arrays.sort(array);
        while (i<array.length)
        {
            int index = data.indexOf(array[i]);
            count += index;
            data.remove(index);
            i++;
        }
        return count;
    }
    public static void main(String[] args) {
        
    }
}