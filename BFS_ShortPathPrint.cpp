/*
Description
定义一个二维数组：


int maze[5][5] = {

	0, 1, 0, 0, 0,

	0, 1, 0, 1, 0,

	0, 0, 0, 0, 0,

	0, 1, 1, 1, 0,

	0, 0, 0, 1, 0,

};


它表示一个迷宫，其中的1表示墙壁，0表示可以走的路，只能横着走或竖着走，不能斜着走，要求编程序找出从左上角到右下角的最短路线。

Input
一个5 × 5的二维数组，表示一个迷宫。数据保证有唯一解。

Output
左上角到右下角的最短路径，格式如样例所示。

Sample Input

0 1 0 0 0
0 1 0 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0

Sample Output

(0, 0)
(1, 0)
(2, 0)
(2, 1)
(2, 2)
(2, 3)
(2, 4)
(3, 4)
(4, 4)
*/
#include<iostream>
#include<queue>
#include<cstring>
#include<cstdio>
using namespace std;

bool maze[5][5];
int go[4][2] = {0,1,0,-1,1,0,-1,0};
struct node
{
    int x,y;
    int prex,prey;
}path[5][5],temp;

void bfs()
{
    queue<node> Q;
    node temp;
    int nx,ny;
    path[0][0].x=path[0][0].y=0;
    Q.push(path[0][0]);
    while(!Q.empty())
    {
        temp = Q.front();
        Q.pop();
        if(temp.x==4&&temp.y==4)
            return;
        for(int i=0;i<4;i++)
        {
            nx = temp.x + go[i][0];
            ny = temp.y + go[i][1];
            if(nx>=0&&nx<5&&ny>=0&&ny<5&&!maze[nx][ny])
            {
                path[nx][ny].x = nx;
                path[nx][ny].y = ny;
                path[nx][ny].prex = temp.x;
                path[nx][ny].prey = temp.y;
                maze[nx][ny] = 1;
                Q.push(path[nx][ny]);
            }
        }
    }
}

void print_path(int x,int y)
{
    if(x==0&&y==0)
    {
        cout<<"("<<path[0][0].x<<", "<<path[0][0].y<<")"<<endl;
        return ;
    }
    int px = path[x][y].prex;
    int py = path[x][y].prey;
    print_path(px,py);
    cout<<"("<<path[x][y].x<<", "<<path[x][y].y<<")"<<endl;
}
int main()
{
    for(int i=0;i<5;i++)
        for(int j=0;j<5;j++)
            scanf("%d",&maze[i][j]);
    bfs();
    print_path(4,4);
    return 0;
}