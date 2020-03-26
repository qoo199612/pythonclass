balance = 0
drinks = [
    {'name': '可樂', 'price': 20},
    {'name': '雪碧', 'price': 20},
    {'name': '玉米濃湯', 'price': 25},
    {'name': '巧克力土司夾蛋', 'price': 25},
    {'name': '純粹喝', 'price': 30},
    {'name': '水', 'price': 20}
]


def deposit():
    """
    儲值功能
    :return:nothing
    """
    """
    儲值
    :return: nothing
    """
    global balance   #宣告函式中會用到全域變數balance
    value = eval(input('儲值金額'))
    while value < 1:
        print('====儲值金額需大於零====')
        value = eval(input('儲值金額'))
    balance += value
    print(f'儲值後餘額為 {balance}元')
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