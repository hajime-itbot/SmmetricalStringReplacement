Word=input("対称性のあるアルファベットの文字列を入力") #対称性になりうるアルファベット文字列
Word=list(Word) #アルファベット文字列を配列化
Count_Word=len(Word) #アルファベット文字列数
Alphabet="abcdefghijklmnopqrstuvwxyz" 
Alphabet=list(Alphabet) #各アルファベットの配列

NumOfAlphabet=[0]*(len(Alphabet)) #アルファベット文字列にどのアルファベットがどれだけ含まれているかを数値化

for i in Word: #NumOfAlphabetの作成
    for j in range(len(Alphabet)) :
        if i==Alphabet[j] :
            NumOfAlphabet[j]+=1
            break

Aranged_Word=[] #修正後のアルファベット配列

#アルファベット文字列数が偶数の場合と奇数の場合で考える

if (Count_Word % 2) == 0 : 
    for i in range(int(Count_Word/2)) : #偶数の場合、Count_word/2までの文字列が線対称であることを利用
        for j in range(len(NumOfAlphabet)) :
            if (NumOfAlphabet[j] >= 2) :
                NumOfAlphabet[j]-=2
                Aranged_Word.append(Alphabet[j])
                break
    
    for i in range(int(Count_Word/2)-1,-1,-1) : #線対称性から配列を完成させる。
        Aranged_Word.append(Aranged_Word[i])

else : 
    odd=0 #何番目のアルファベットが奇数個であるか判定
    for i in range(len(NumOfAlphabet)) :
        if(NumOfAlphabet[i] % 2) != 0 :
            odd=i
    
    for i in range(odd-1): #奇数の場合、odd番目の文字を中心として線対称になることを利用
        for j in range(len(NumOfAlphabet)) :
            NumOfAlphabet[j]-=2
            Aranged_Word.append(Alphabet[j])
            break
    
    Aranged_Word.append(Alphabet[odd])
    for i in range((odd-2),-1,-1) : #線対称性から配列を完成させる。
        Aranged_Word.append(Aranged_Word[i])

print(Aranged_Word)
    














        

