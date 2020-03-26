"""
x = 2
y = 5
print(x+y)
print(x-y)
print(x*y+x)
print(x**y)
print(y%x)
print(y//x)
print(round(4.9555))

值的計算
"""
"""
我知道我很帥
"""
"""
針對List進行選擇顯示哪個位置的數字
mathscores = [60, 70, 10, 20, 81, 63, 4]

mathscores[2]
print(mathscores[2])
mathscores[1:6]
print(mathscores[1:6])
print(mathscores[-1])
print(mathscores[6])
print(mathscores[-3])
print(mathscores[0:5])
print(mathscores[:6])
print(mathscores[2:])
print(len(mathscores))
print(sum(mathscores))
print(max(mathscores))
print(min(mathscores))
print(sum(mathscores)/len(mathscores))
"""

"""
mathscores2 = []
print(mathscores2)
mathscores2.append(60)
print(mathscores2)
mathscores2.append(80)
print(mathscores2)
mathscores2.append(90)
mathscores2.append(100)
mathscores2.append(20)
mathscores2.append(57)
"""
"""
新增List裡面的數字(只能到最右邊)
"""
"""
mathscores2.insert(1, 30)
print(mathscores2)
"""
"""
在指定位置中新增數字
"""
"""
mathscores2.remove(60)
print(mathscores2)
"""

"""
將數字移除
"""

"""
del mathscores2[1]
print(mathscores2)
"""

"""
刪除指定位置的值
"""

"""
mathscores2[0] = 55
print(mathscores2)
"""

"""
取代某值
"""
"""
mathscores2.pop(1)
print(mathscores2)
"""
"""
把最後一個刪除
"""

"""
print(80 in mathscores2)
print(55 in mathscores2)
"""
"""
尋找List裡面是否有這個數字
"""

# print(mathscores2)

"""
print(mathscores2.count(90))
"""
"""
算裡面幾個90
"""

"""
mathscores2.index(80)
print(mathscores2.index(20))
"""
"""
查數字20在list的位置在哪裡
"""

# list1 = [1, 2, 3, 4, 5]
# print(mathscores2 + list1)
"""
List相加
"""
"""
print(sorted(mathscores2))
print(sorted(mathscores2, reverse=True))
"""
"""
數字排序升冪或降冪
"""
"""
ls = [[1, 2, 3], [4, 5, 6]]
print(ls)
print (ls[0][2])
"""

"""
練習題
"""
"""
rades = [[5, 14, 7], [23, 36, 28], [88, 80, 92]]
print(len(grades[1]))
print(grades[2])
print(len(grades[0]))
print(sum(grades[0])/len(grades[0])) #國文平均
print(sum(grades[1])/len(grades[1])) #英文平均
print(sum(grades[2])/len(grades[2])) #數學平均
grades.append([94, 90, 96]) #新增自然成績
print(grades)
grades[0][1] = 20
print(grades[0])
"""

"""
宣告
"""
"""
tuple1 = (1, 2, 3, 4, 5)  #tuple不能改變值
tuple2 = 1, 2, 3, 4, 5
print(tuple1)
print(tuple2)
tuple3 = () #初始化
print(tuple3)
print(tuple1[3]) #取第三個值
print(tuple1.index(2)) #取得數字索引位置
print(tuple1.count(5)) #計算幾個5
print(tuple1 + tuple2) #相加
print(sorted(tuple1)) #升冪
print(sorted(tuple1, reverse=True)) #降冪
print(20 in tuple1) #20是否有在裡面
print(1 in tuple1) #1是否有在裡面
"""
"""
tuple3 = (88, 42)
x, y = tuple3 #使tuple數值由XY去接收
print(x)
print(y)
"""

"""
#練習題
gradesTuple = ((5, 14, 7), (23, 36, 28), (88, 80, 92))
print(gradesTuple[2])
print(sum(gradesTuple[0])/len(gradesTuple[0]))
print(sum(gradesTuple[1])/len(gradesTuple[1]))
print(sum(gradesTuple[2])/len(gradesTuple[2]))
"""

"""
#沒有順序是亂數
family = {'dad' : ' Homer',
          'mom' : 'Marge',
          'son' : 'Bart',
          'daughter' : 'Lisa'}
print(family['dad'])            #取值打Key
print(family.get('dad'))        #較安全的取值法較安全不會噴錯
print('dad' in family)          #看是否有這個名字
print(family.items())           #取全部的值且是tuple型態(這個較常使用)
print(family)                   #取全部的值且是tuple型態
print(family.values())          #取後面的值
print(family.keys())            #取前面的值
"""

""""
family = {}           #初始化
family['cousin'] = 'Max'  #新增一個值
print(family)
family.update({'uncle':'Martin',
               'aunt':'May'})         #新增多個值
print(family)

#del family['cousin'] #刪除
print(family)
print(family.pop("cousin"))  #移出並回傳
"""
"""
#練習題
gradesDict = {'chinese': [5, 14, 7],
              'english':[23, 36, 28],
              'math': [88, 80, 92] }
print(gradesDict)
print(gradesDict['math'])
print(sum(gradesDict['math'])/len(gradesDict['math']))
gradesDict['science'] = [94, 90, 96]
gradesDict.update({'science'}) #沒寫完
"""

"""
#SET操作

fruits = {'apple',
          'banana',
          'guava',
          'guava'}
fruits1 = {'strawberry',
           'papaya',
           'banana'}
# print(fruits|fruits1)  #聯集
# print(fruits&fruits1)  #交集
# print(fruits-fruits1)  #差集

fruits.add('watermelon') #新增
print(fruits)
fruits.remove('apple')  #刪除但容易噴錯
print(fruits)
fruits.discard('apple') #刪除較安全
print(fruits)
fruits.clear()          #刪除全部元素
print(fruits)
sorted(fruits)          #排序
print(sorted(fruits))
"""

"""
# 練習題
allStudents = {'John',
               'Eva',
               'Jill',
               'Eric',
               'Andy',
               'Albert',
               'Polina',
               'Kristin',
               'Angela'}
danceClub = {'Andy',
             'Eric',
             'Albert',
             'Polina',
             'Kristin'}
guitarClub = {'John',
              'Eva',
              'Jill',
              'Eric',
              'Andy'}

print(danceClub & guitarClub)
print(guitarClub - danceClub)
print(allStudents - danceClub - guitarClub)

"""

# 3/16課程

# 開根號
# 1.
"""
x = 4** 0.5
print(x)
# 2.
import math
x = math.sqrt(9)
print(x)
"""


# 練習題
"""
x = 10 #圓的直徑
print((x/2)*(x/2)*3.14) #圓的面積
pi = 3.14
print((x/2)**2*pi)
list = [10, 30, 40, 90, 100, 61]
print(round(sum(list)/len(list)))
"""


# 邏輯運算
"""
10==10 #還沒打完
"""

#條件控制
""""
score = 52
if score >= 60:
    print('及格了')
elif 55 <= score < 60:
    print('教授拜託調分')
elif 50 <= score < 55:
    print('寂寞邊界')
else:
    print('被當了')
"""

#巢式迴圈
"""
score = 70
if score >= 60:
    print('及格了')

    if score >= 90:
        print('阿不就好棒棒') #可以往下問下去
    else:
        print('及格就很屌了') #不是90分的
elif 55 <= score < 60 :
    print('求我啊') 
else:
    print('沒救了')
"""

#迴圈
#print用法
"""
print("good morning")
print("Hello")
print("good", "nice", "wonderful") #中間一個空格
print("nice\ngood\nwonderful")  #換行

print("123", end="") #想要將123與456相接，使用end來連接
print("456")
"""
"""
x = 42
print(f"value of x is {x}") #抓x的值
mathScorers = [60, 70, 10, 20, 81, 63, 4]
print(mathScorers[2])
firstItem = f"first item in mathScores is {mathScorers[2]}" #印出List的值
print(firstItem)
print(f"the mathScores has {len(mathScorers)}") #印出有幾個數字
"""

#迴圈
"""
for i in range(0, 10):
    print(i)
for i in range(10):
    print(i)
for i in range(0, 10, 2):  #開始值結束值間隔
    print(i)
    
mathScorers = [60, 70, 10, 20, 81, 63, 4]
for i in range(len(mathScorers)):   #印出每個值
    print(i , mathScorers[i])
"""
"""
mathScorers = [60, 70, 10, 20, 81, 63, 4]
for i in mathScorers:    #for...in 直接加list名稱
    print(i)
"""
"""
family = {'dad' : ' Homer',
          'mom' : 'Marge',
          'son' : 'Bart',
          'daughter' : 'Lisa'}
for member in family.items():    #完全顯示非常完整
    print(member)
for member in family:
    print(member)    #只有Keyword
for key, value in family.items():
    print(f"my {key} is {value}")  #可以迴圈把my跟is輪迴所有數據
"""

#練習題
"""
mathScores = [60, 70,10, 20, 81, 63, 4]
for score in mathScores:
    print("myscore", (score**0.5*10))
"""

#進階
"""
for i in range(10):
    print(i)
[print(i) for i in range(10)]   #上下答案相同[動作for變數in範圍]

import math
mathScores = [60, 70,10, 20, 81, 63, 4]
for item in mathScores:
    print(math.sqrt(item)*10)
[print(math.sqrt(item)*10) for item in mathScores]  #上下答案相同，兩行變一行
"""

#while  #不斷迴圈一直執行
"""
count = 0
while count <10:
    print(count)
    count += 1

else:
    print('loop end')
"""

#break 跳出迴圈
"""
mathScores = [60, 70,10, 20, 81, 63, 4]

for score in mathScores:
    if score >80:
        break                    #遇到80以上就停止迴圈
    print(score)

for score in mathScores:
    if score >80:
        continue                 #遇到80以上繼續跑
    print(score)
"""

#補充
"""
import random
i = random.randint(1, 3)

rows = eval(input('How many rows:'))
print(type(rows))
"""

#練習題 99乘法表
"""
#1
for i in range(1,10):
    for j in range(1,10):
        print(f"{i}*{j}=",i*j)
"""
#2
"""
count = 0
while count <= 50:
    print("你好")
    count += 1

else:
    print("我說完了")
"""
"""  #要再認真看
#3
keyin = input("輸入一個數值: ")
keyin2 = int(keyin)
for a in range(1,keyin2,2):    #開始值，結束值，間隔
    print(a)
    
#第二種方式
num = eval(input('Enter a number:'))
for i in range(1, num+1):
    if i % 2 == 1:
       print(i)
"""
#4
"""
import randan

rows = eval(input('輸入一個rows值:'))
columns = eval(input('輸入一個column值:'))
for i in randan(rows):
    ls.append([])
    for j in range(columns):
        num = randan.randint(1, 100)
        ls[i].append(num)
for x in range(rows):
    for y in range(columns):
        num = randan.randint(1, 100)
        ls[i].append(num)
for rows ls
    for value in rows:
        print(f'{value}', end="")
    print()
"""


"""       
#8
import randan

rows = 3
columns = 3

        
i = random.randint(0, 100)
j = random.randint(0, 100)

[print()]
"""

#販賣機練習題1
"""
flag = True
balance = 0
drinks = [
    {'name': '可樂', 'price': 20},
    {'name': '雪碧', 'price': 20},
    {'name': '玉米濃湯', 'price': 25},
    {'name': '巧克力土司夾蛋', 'price': 25},
    {'name': '純粹喝', 'price': 30},
    {'name': '水', 'price': 20}
]

while flag:
    print('\n======================================================')
    select = eval(input('1. 儲值\n2. 購物\n3. 查詢餘額\n4. 離開\n請選擇:'))


    if select == 1:  #儲值
        value = eval(input('儲值金額'))
        while value < 1:        #若儲值小於0，需重新輸入
            print('====儲值金額需大於零====')
            value = eval(input('儲值金額'))
        balance += value
        print(f'儲值後餘額為{balance}元')
    elif select == 2:  #購買
        print('\n請選擇商品')   #印出品項
        for i in range(0, len(drinks)):
            print(f'({i+1})\t{drinks[i]["name"]} \t {drinks[i]["price"]}元')  #將商品印出並且前面印出索引值
        choose = eval(input('你想喝甚麼?'))  #打一個input

        while choose < 1 or choose > 6:   #如果輸入值超出1~6 那將印出提醒
            print('====請輸入1-6之間====')
            choose = eval(input('幹!都不要喝，要喝就輸入正確的號碼'))

        buy_drink = drinks[choose-1]     #如果金額小於飲料價錢，將印出提醒
        if balance < buy_drink['price']:
            print('====餘額不足====')
            print('販賣機：你耍我?')
        else:
            print(f'已購買{buy_drink["name"]} {buy_drink["price"]}元')
            balance -= buy_drink['price']
            print(f'購買後餘額為{balance}元')
    elif select == 3: #查詢餘額
        print(f'目前餘額為{balance}元')
    elif select == 4:  # 離開
        print('bye')
        flag = 0
        break

    else:  # 重新輸入
        print('====請輸入1-4之間====')
        continue
"""


#販賣機改為函式寫法
"""
flag = True
balance = 0
drinks = [
    {'name': '可樂', 'price': 20},
    {'name': '雪碧', 'price': 20},
    {'name': '玉米濃湯', 'price': 25},
    {'name': '巧克力土司夾蛋', 'price': 25},
    {'name': '純粹喝', 'price': 30},
    {'name': '水', 'price': 20}
]
"""

#儲值的函式撰寫
"""
def deposit():
    
    # 儲值
    # :return: nothing
    
    global balance   #宣告函式中會用到全域變數balance
    value = eval(input('儲值金額'))
    while value < 1:
        print('====儲值金額需大於零====')
        value = eval(input('儲值金額'))
    balance += value
    print(f'儲值後餘額為 {balance}元')
"""


#購買的函式撰寫
"""
def buy():
    global balance, drinks   #宣告這兩個東西是全域使用的
    print('\n請選擇商品')  # 印出品項
    for i in range(0, len(drinks)):
        print(f'({i + 1})\t{drinks[i]["name"]} \t {drinks[i]["price"]}元')  # 將商品印出並且前面印出索引值
    choose = eval(input('你想喝甚麼?'))  # 打一個input

    while choose < 1 or choose > 6:  # 如果輸入值超出1~6 那將印出提醒
        print('====請輸入1-6之間====')
        choose = eval(input('幹!都不要喝，要喝就輸入正確的號碼'))

    buy_drink = drinks[choose - 1]  # 如果金額小於飲料價錢，將印出提醒
    while balance < buy_drink['price']:
        print('====餘額不足，需要儲值嗎?====')
        print('販賣機：你耍我?')
        want_deposit = input('y/n?')
        if want_deposit == 'y':
            deposit()
        elif want_deposit == 'n':
            break
        else:
            print('====請重新輸入====')
    else:
        print(f'已購買{buy_drink["name"]} {buy_drink["price"]}元')
        balance -= buy_drink['price']
        print(f'購買後餘額為{balance}元')

while flag:
    print('\n======================================================')
    select = eval(input('1. 儲值\n2. 購物\n3. 查詢餘額\n4. 離開\n請選擇:'))


    if select == 1:  #儲值
        deposit()
    elif select == 2:  #購買
        buy()   #按Ctrl 按buy可以找到她的程式
    elif select == 3: #查詢餘額
        print(f'目前餘額為{balance}元')
    elif select == 4:  # 離開
        print('bye')
        flag = 0
        break

    else:  # 重新輸入
        print('====請輸入1-4之間====')
        continue

"""

#傳入參數
"""
weight = 50
weight1 = 80

def add(w1, w2):
    result = w1 + w2
    return result
x = add(weight, weight1)
print(x)

def add(w1, w2=20):
    result = w1 + w2
    result1 = w1 / w2
    return result, result1
x = add(weight)
print(x)

x1, x2 = add(weight, weight1)
print(x1, x2)

y1, y2 = add(w2=weight, w1=weight1)
print(y1, y2)
"""

#模組寫販賣機
"""
import vending_machine as machine

flag = True
while flag:
    print('\n======================================================')
    select = eval(input('1. 儲值\n2. 購物\n3. 查詢餘額\n4. 離開\n請選擇:'))


    if select == 1:  #儲值
        machine.deposit()
    elif select == 2:  #購買
        machine.buy()
    elif select == 3: #查詢餘額
        print(f'目前餘額為{machine.balance}元')
    elif select == 4:  # 離開
        print('bye')
        flag = 0
        break

    else:  # 重新輸入
        print('====請輸入1-4之間====')
        continue
"""


