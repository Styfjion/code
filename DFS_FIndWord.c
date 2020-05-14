#include <stdio.h>
#include <string.h>
#include <stdbool.h>
int trace[101][101] = {0};
int direct[2][4] ={{0,0,1,-1},{1,-1,0,0}};
int n,m;

bool dfs(char daze[n][m], char *p, int x, int y)
{
    if(*p == daze[x][y] && *(p+1) == '\0')
        return true;
    for(int i=0; i<4; i++) {
        int nx,ny;
        nx = x + direct[0][i];
        ny = y + direct[1][i];
        if(nx>=0 && nx <n && ny >= 0 && ny < m && *(p+1) == daze[nx][ny] && trace[nx][ny] == 0)
        {
            trace[nx][ny] = 1;
            p++;
            if (dfs(daze, p, nx, ny))
                return true;
            trace[nx][ny] = 0;
            p--;
        }
    }
    return false;
}

int main()
{
    scanf("%d %d", &n, &m);

    char daze[n][m];
    char word[101];
    scanf("%s", word);
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            scanf(" %c", &daze[i][j]);

    bool token = false;
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
        {
            if(daze[i][j] == word[0])
            {
                for(int k=0;k<n;k++)
                    memset(trace[k],0,m*sizeof(int));
                char *p = word;
                if(dfs(daze,p, i, j)){
                    token = true;
                    break;
                }
            }
        }
    if(token)
        printf("YES");
    else
        printf("NO");
    return 0;
}
