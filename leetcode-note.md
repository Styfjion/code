## 单调栈
### 代码模板
```C
int stack[arraySize];
int stackLen = 0;
for (int i = arraySize - 1; i > _1_; i--) {
    if (stackLen && array[stack[stackLen - 1]] <= array[i]) {
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
```C
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
```C
//for控制右边界前进, while控制左边界前进
int left = 0;
for (int i = 0; i < arraySize; i++) {
    do something...
    //有时会出现
    if (contiditon is false) {
        continue
    }
    while(conditon is true) {
        ans = min(ans, ...); 
        or ans = max(ans, ...)
        do someting... reverse
        left++;
    }
    ans = max(ans, ...);
    or ans = min(ans, ...);  
}
```


## 前缀和模型
### 代码模板:
```C
HashMap *map, *node;
map = NULL;
int preSum = 0;
for (int i = 0; i < arraySize; i++) {
    node = NULL;
    preSum += array[i];
    HASH_FIND_INT(map, &preSum, node);
    if (node != NULL) {
        node->count++;
    } else {
        node = malloc(sizeof(HashMap));
        node->number = preSum;
        node->count = 1;
    }
}
```

## 差分模型
### 代码模板
```C
int endTime = 0;
for (int i = 0; i <intervalsSize; i++) {
    endTime = MAX(intervals[i][1], endTime);
}

int time[endTime + 1];
memset(time, 0, sizeof(time));
for (int i = 0; i < intervalsSize; i++) {
    time[intervals[i][0]] += intervals[i][2];    //上车
    time[intervals[i][1]] -= intervals[i][2];    //下车
}
int timeProc = 0;
int maxNum = 0;
for (int i = 0; i <= endTime; i++) {
    timeProc += time[i];                 //前进             
    do something

}
```

## 字符串拼接与截取
### 代码
```C
//从source中去掉第i位
char target = [strlen(s)];
memset_s(target, sizeof(target), 0, sizeof(target));
strncat_s(target, sizeof(target), source, i);
strcat_s(target, sizeof(target), source + i + 1);

//截取字符串
char reviews[] = "java python cpp";
char *nextToken = NULL;
char *token = NULL;
char *seps = " ";
token = strtok_s(reviews, seps, &nextToken);

while (token != NULL) {
    printf("%s\r\n", token);       
    token = strtok_s(NULL, seps, &nextToken);
```
### BFS
### 代码模板
```C
typedef struct {
    int data; or char data[MAX];
    int pathLen;
} Unit;

//BFS函数中的操作
Unit queue[totalDataSize];
int queueHead = 0;
int queueTail = 0;
queue[queueTail].data = beginData;
queue[queueTail].pathLen = 1;
bool visited[totalDataSize];
memset(visited, 0, sizeof(visited));
while (queueHead < queueTail) {
    Unit *top = &queue[queueHead++];
    if (condition is true) {
        return true;
    }
    for (int i = 0; i < conditionSize; i++) {
        if (!visited[i] and conditionSize[i] is true) {
            visited[i] = true;
            queue[queueTail].data = conditionSize[i];
            queue[queueTail].pathLen = top->pathLen + 1;
        }
    }
}
return false;
```
## 拓扑排序
### 代码模板
```C++
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites)
    {
        vector<pair<int, vector<int>>> courses(numCourses, {0, {}});

        for (auto &pre : prerequisites) {
            // 添加后续依赖
            courses[pre[1]].second.push_back(pre[0]);
            // 增加入度
            courses[pre[0]].first++;
        }
        queue<int> courseQueue;
        
        for(int i = 0; i < numCourses; i++) {
            if (courses[i].first == 0) {
                // 收集入度为0，即没有依赖的节点
                courseQueue.push(i);
            }
        }

        vector<int> rslt;
        while (!courseQueue.empty()) {
            int topCourseIdx = courseQueue.front();
            rslt.push_back(topCourseIdx);
            courseQueue.pop();
            for (int afterCourseIdx : courses[topCourseIdx].second) {
                if (--courses[afterCourseIdx].first == 0) {
                    // 后续课程入度为0时，添加到队列
                    courseQueue.push(afterCourseIdx);
                }
            }
        }

        if (rslt.size() == numCourses) {
            return rslt;
        } else {
            return {};
        }
    }
};
```
### 字典树
### 代码

```C
typedef struct Trie {
    bool isEnd;
    struct Trie *next[MAX];
} Trie;

Trie *TrieInit()
{
    Trie *root = malloc(sizeof(Trie));
    memset(root, 0, sizeof(Trie));
    return root;
}

void InsertTire(Trie *node, char *word)
{
    for (int i = 0; word[i] != '\0'; i++) {
        char ch = word[i];
        if (!node->next[ch - 'a']) {
            node->next[ch - 'a'] = TrieInit();
        }
        node = node->next[ch - 'a'];
        node->isEnd = false;
    }
    node->isEnd = true;
}

bool TrieStartsWith(Trie* node, char * prefix) {
    for (int i = 0; prefix[i] != '\0'; i++) {
        char ch = prefix[i];
        if (node->next[ch - 'a'] == NULL) {
            return false;
        }
        node = node->next[ch - 'a'];
    }
    return true;
}
```
### 最大最小问题 二分法
### 代码模板
```C
bool CheckValid(int *array, int arraySize, int limit, int mid)
{
    int cnt = 1;
    for （int i= 0; i < arraySize; i++） {
        if (/* 不满足边界条件 */) {  //最大值中的最小 >mid 最小值中的最大， <mid
            cnt++;
        }
    }
    return /* cnt和limit比较 */
}

int FindMaxMin(int *array, int arraySize, int limit)
{
    int left, right, mid;
    /* 确定左右边界 */
    while (left <= right) {
        mid = (left + right) / 2;
        if (CheckValid(array, arraySize, limit, mid)) {
            rslt = mid /* 求最小值时,已满足当前条件时，区间应该左移*/ 
            right = mid - 1;
        } else {
            // if (CheckValid(array, arraySize, limit, mid))
            //     rslt = mid /* 求最大值时，已满足当前条件时，区间应该右移 */
            left = mid + 1;
        }
    }
    return rslt;
}
```







