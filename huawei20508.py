import itertools

if __name__ == "__main__":
    n,k = map(int,input().strip().split())
    result = list(itertools.combinations(list(range(n+k-1)),k-1))
    result = result[::-1]
    print(len(result))
    for unit in result:
        for i in range(n+k-1):
            if i in unit:
                print('|',end='')
            else:
                print('*',end='')
            if i == n+k-2:
                print('')
    
            
