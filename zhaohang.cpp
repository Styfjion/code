#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int ci[101000];
int buhe[101000];
int main()
{
	int n;
	int lim=100000;
	while(scanf("%d",&n)!=EOF)
	{
		memset(ci,0,sizeof ci);
		memset(buhe,0,sizeof buhe);
		for(int i=0;i<n;i++)
		{
			int num;
			scanf("%d",&num);
			int flag=1;
			int bu=0;
 			while(num)
			{
				if(flag)
				{
					int tt=bu+1;
					int num2=num*2;;
					while(num2<=lim)
					{
						ci[num2]++;
						buhe[num2]+=tt;
 
						num2*=2;
						tt++;
					}
					flag=0;
				}
				ci[num]++;
				buhe[num]+=bu;
				bu++;
				if(num%2==0)
					num/=2;
				else
				{
					flag=1;
					num/=2;
				}
			}
		}
		int minn=999999999;
		for(int i=1;i<=lim;i++)
		{
			if(ci[i]==n)
				minn=min(minn,buhe[i]);
		}
		printf("%d\n",minn);
	}
	return 0;
}