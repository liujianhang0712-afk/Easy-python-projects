def start_game():
    print('你醒来在一个陌生的房间')
    room()
def room():
    print('\n你在房间里,可以做以下选择:')
    print('1.环顾房间')
    print('2.回想自己是谁')
    print('3.什么也不做')

    choice=input('请输入数字:')
    if choice=='1':
        table()
    elif choice=='2':
        memory()
    elif choice=='3':
        nothing()
    else:
        print('输入无效')
        room()
def table():
    print('\n桌上有一把\n钥匙')
    print('\n1.yes\n2.no')
    key=input('\n是否拿起钥匙?')
    if key=='1':
        key1()
    else:
        room()
def memory():
    print('\n你什么也没想起来......')
    room()
def nothing():
    print('\n什么也没有发生......')
    room()
def key1():
    print('\n1.使用钥匙\n2.不使用钥匙')
    choice2=input('\n请问是否使用钥匙?')
    if choice2=='1':
        print('你成功打开门\n恭喜你通过游戏')
    else:
        room()
start_game()    
    

