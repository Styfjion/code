#include <stdio.h>
#include <string.h>
#include <stdbool.h>
int trace[101][101] = {0};
int direct[2][4] ={{0,0,1,-1},{1,-1,0,0}};

bool dfs(int n, int m, char daze[n][m], int trace[][101], char *p, int x, int y)
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
            if (dfs(n, m, daze, trace, p, nx, ny))
                return true;
            trace[nx][ny] = 0;
            p--;
        }
    }
    return false;
}

int main(int argc, char const *argv[])
{
    int n,m;
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
                if(dfs(n, m, daze, trace, p, i, j)){
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
