#include<iostream>
#include<cstdlib>
using namespace std;
int main()
{
	cout<<"����������N��ֵ"<<endl;
	int n,i,sum=0;
	cin>>n;
	for(i=1;i<=n;i++)
		if(i%2==0)
			sum-=i;
		else
			sum+=i;
	cout<<"ǰ"<<n<<"��ĺ�Ϊ"<<sum<<endl;
	system("pause");
	return 0;
}








