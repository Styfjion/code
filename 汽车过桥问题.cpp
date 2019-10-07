#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int fun(int N,int W,int w[],int t[])
{
    int res = 0,i=0;
    vector<int> curt;
    vector<int> curw;
    while (i<N)
    {
        if(curt.empty())
        {
            curt.push_back(t[i]);
            curw.push_back(w[i]);
            i++;
        }
        else
        {
            int sumW = 0;
            for(int unit:curw)
                sumW+=unit;
            if(sumW+w[i]<=W)
            {
                curt.push_back(t[i]);
                curw.push_back(w[i]);
                i++;
                continue;
            }
            int tmin;
            tmin = *(min_element(curt.begin(),curt.end()));
            res += tmin;
            vector<int>::iterator it_t = curt.begin();
            vector<int>::iterator it_w = curw.begin();
            for(;it_t<curt.end();)
            {
                *it_t -= tmin;
                if(!*it_t)
                {
                    curt.erase(it_t);
                    curw.erase(it_w);
                }
                else
                {
                    it_t++;
                    it_w++;
                }
            }
        }
        
    }
    int tmax;
    tmax = *(max_element(curt.begin(),curt.end()));
    res += tmax;
    return res;
}

int main(int argc, char const *argv[])
{
    int N,W;
    cin>>N>>W;
    int *w = new int[N];
    int *t = new int[N];
    for(int i=0;i<N;i++)
        cin>>w[i];
    for(int i=0;i<N;i++)
        cin>>t[i];
    int res;
    res = fun(N,W,w,t);
    cout<<res<<endl;
    delete w;
    delete t;
    return 0;
}

