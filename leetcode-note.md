## 单调栈
### 代码模板
```
int stack[arraySize];
int stackLen = 0;
for (int i = 0; i < arraySize; i++) {
    if (!stack && array[stack[stackLen - 1]] <= array[i]) {
        stackLen--;
    }  //严格递增栈
    if (stackLen) {
        do something.....
    }
    stack[stackLen++] = i;
}
```

## 并查集
### 代码模板
```
int g_count;

int FindRoot(int root, int *pre)
{
    int son, temp;
    son = root;
    while (root != pre[root]) {
        root = pre[root];
    }
    while (son != root) {
        temp = pre[son];
        pre[son] = root;
        son = temp;
    }
    return root;
}

void Union(int x, int y , int *pre)
{
    int rootX = FindRoot(x, pre);
    int rootY = FindRoot(y, pre);
    if (rootX == rootY) {
        return;
    }
    pre[rootY] = rootX;
    g_count--;
}
```

## 滑动窗口模型
### 代码模板:
```
//for控制右边界前进, while控制左边界前进
int left = 0;
for (int i = 0; i < arraySize; i++) {
    do something...
    while(conditon is true) {
        //求最短，最小XXX时
        ans = min(ans, ...); 
        do someting... reverse
        left++;
    }
    //求最长，最大XXX时
    ans = max(ans, ...);  
}


