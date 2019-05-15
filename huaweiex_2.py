if __name__ == "__main__":
    while True:
        try:
            ch = str(input())
            if len(ch) == 1:
                print(ch)
            i = 0
            while i<len(ch) and ch[i]:
                if ch.count(ch[i]) > 1:
                    ch = ch[:i+1]+ch[i+1:].replace(ch[i],'')
                i+=1
            print(ch)
        except:
            break
