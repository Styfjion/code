
public class Solution {
    public int MoreThanHalfNum_Solution(int [] array) {
        if(array == null || array.length == 0 )
            return 0;
        int target = array[0];
        int times = 1;
        for (int i=1;i<array.length;i++)
            if(times == 0)
            {
                target = array[i];
                times = 1;
            }
            else if(target == array[i])
                times++;
            else
                times--;
        int count = 0;
        for(int unit:array)
            if(unit==target)
                count++;
        if(count*2<=array.length)
            target = 0;
        return target;
    }

}