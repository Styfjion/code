#include<iostream>
#include<cstdlib>
using namespace std;
int main()
{
	cout<<"请输入项数N的值"<<endl;
	int n,i,sum=0;
	cin>>n;
	for(i=1;i<=n;i++)
		if(i%2==0)
			sum-=i;
		else
			sum+=i;
	cout<<"前"<<n<<"项的和为"<<sum<<endl;
	system("pause");
	return 0;
}








