#include<cstdio>
#include<iostream>
#include<cstring>
#include<queue>
using namespace std;
char maze[50][50];
bool vis[10][10];
int n,m;
int sx,sy;
int ex,ey;
int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};
struct node
{
    int x,y,step;
};
void bfs()
{
    node p;
    p.x=sx;p.y=sy;p.step=0;
    queue<node>q;
    q.push(p);
    vis[sx][sy]=1;
    while(!q.empty())
    {    node tmp=q.front();
        q.pop();
        if(tmp.x==ex&&tmp.y==ey)
            {cout<<"最短路为"<<tmp.step<<endl;
                return;}
        for(int i=0;i<4;i++)
        {int xx=tmp.x+dx[i];
        int yy=tmp.y+dy[i];
        if(maze[xx][yy]!='#'&&xx>0&&yy>0&&xx<=n&&yy<=m&&!vis[xx][yy])
        {
            node tp;
            tp.x=xx;
            tp.y=yy;
            tp.step=tmp.step+1;
            vis[xx][yy]=1;
            q.push(tp);
        }

        }
    }
    cout << "不能走到那里！" << endl;
}


int main()
{
    while(~scanf("%d%d",&n,&m)&&n!=0&&m!=0)
    {   memset(vis,0,sizeof(vis));
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
            {
                cin>>maze[i][j];
                if(maze[i][j]=='S')
                    {sx=i;sy=j;}
                if(maze[i][j]=='G')
                    {ex=i;ey=j;}
            }   
        bfs();
    }
}