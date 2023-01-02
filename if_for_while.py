# if 判斷式
# if-->如果 
# 如果if後面的條件為True，便會執行下方縮排之程式，跳過else
# 如果if後面的條件為False，就直接跳到else(或其他非if下轄的程式)
# else-->否則
# 縮排代表該行程式是包含在上面的程式中，為上面的程式後要執行的動作

a=10
b=7
if a>b :  
    print("a大於b")
else:
    print("a不大於b") # 有被包含在else裡面
print("test") # 沒有被包含在if或else裡面

# 多層if判斷
# elif = else if(否則如果)
if b==10:
    print("b的內容是10")
elif b>10:
    print("b大於10")
    print("b小於10")

# if運用在字串比較
c="甲乙丙丁戊己庚辛壬癸子丑寅卯辰巳午未申酉戌亥"
if "乙" in c:
    print("有在裡面喔")
# 後面如果沒有寫elif或else，若條件不成立，則什麼事情都不會發生
if "乙己" in c:
    print("有在裡面喔") 
# 雖然乙、己都有在c裡面，但他們不在一起，因此會判定他們不在c裡面

# if運用在序列
d=["甲子","乙丑","丙寅"]
if "甲子" in d:
    print("有在裡面喔")
# 若要在序列中有沒有某個物件，如果完全符合，才會執行if的指令，如果寫得不完全，不會執行if的指令
if "甲" in d:
    print("有在裡面喔")
if "丁卯" in d:
    print("有在裡面喔")
    
# if加上邏輯運算
if ("甲" in c) and ("甲" in d):
    print("兩個都有在裡面喔")
if ("甲" in c) or ("甲" in d):
    print("兩個之中其中一個有在裡面喔")


# for 迴圈

for i in [0,1,2,3,4,5,6,7,8,9]:
    print(i)
""" 
=>for迴圈的運作方式：
以上方的例子來說，一開始變數i先從0開始，執行print的指令
執行完後，變數i變成1，執行print的指令
以此類推，重複上述動作直到i=9
"""
for i in [1,2,4]:
    print(i)

a=[0,1,2,3,4,5]
for i in a: # 序列也可以獨立在for迴圈外
    print(i) 

# range(開始,結束,公差)
for i in range(4): # range(結束)(開始=0,公差=1) => 可以想成重複幾次
    print(i)
    
for i in range(1,20,3): 
    print(i)
    
b=[1,2,2,3,4,5,5,6,6,7]
len(b)
for i in range(len(b)): # len() 長度
    print(i)

b=[1,2,2,3,4,5,5,6,6,7]
for i in range(len(b)): # len() 長度 
    print(b[i]) # print出b序列中的第i項
    
# 應用：創造累加
c=0
for i in range(10):
    c=c+i
print(c)

# for與if結合
d=[1,2,3,3,4,5,6,7,9,11,14,19]
for i in range(len(d)):
    if d[i]%3==0:
        print(d[i])
        
# 製作斷點
e=[1,2,6,7,9,10,13,16,19,23,24,26]
for i in range(len(e)):
    if e[i]%2==0:
        if e[i]%4==0:
            break; # 斷點，直接停止此迴圈
        else:
            print(e[i])

# 製作繼續
c=[1,2,5,7,9,10,13,16,19,22,23,24,26,29]
for i in range(len(c)):
    if e[i]%2==0:
        if e[i]%4==0:
            continue; # 跳過
        else:
            print(e[i])

# 雙重迴圈
for i in range(1,6):
    for j in range(1,6):
        print("i = "+str(i)+" j = "+str(j))
"""
=>雙重for迴圈的運作方式：
以上方的例子來說，一開始變數i先從1開始，執行「for j in range(1,6):」的指令
變數j從1開始，執行print的指令
執行完後，變數j變成2，執行print的指令
以此類推，重複上述動作直到j=5
當j=5的指令完成時，會回來執行「for i in range(1,6):」的指令
變數i變成2，執行「for j in range(1,6):」的指令
以此類推，重複上述動作直到i=5
"""

# 應用：九九乘法
for i in range(1,10):
    for j in range(1,10):
        print(str(i)+"x"+str(j)+"="+str(i*j))


# while 迴圈
i=0 # 需要有一個容器
while i<10: # 判斷式(當)  while包含迴圈和判斷式
    print(i)
    i=i+1 # 容器需要變化
    # 當i=10時，while會停止執行，因為while=>False
    
# 無窮迴圈
i=0
while i<10: # 因為布林值一直是True，所以不會停止
    print(i)

# 無窮迴圈
while True: # 因為布林值一直是True，所以不會停止
    print("這是一個無窮迴圈")

# while可以做到無窮迴圈，但for不行，for有極限

# while迴圈與if判斷式的結合
i=0
while i<10:
    if i%2==0:
        print(i)
    i=i+1 # 容器需要變化
    
# 製作斷點
i=0
while i<10:
    if i%2==0:
        if i==8:
            break; # 斷點
        print(i)
    i=i+1 # 容器需要變化

# 製作跳過
i=0
while i<10:
    if i%2==0:
        if i==6:
            continue; # 跳過
        print(i)
    i=i+1 # 容器需要變化
        
    
