while True:
    win={
        '石头':'剪刀',
        '剪刀':'布',
        '布':'石头'
    }
    player=input('请输入剪刀,石头,布:')
    import random
    import time
    computer=random.choice(['石头','剪刀','布'])
    print('电脑出的是:')
    time.sleep(1)
    print(computer)
    if player==computer:
        print('平局')
    elif win[player]==computer:
        print('你赢了!')
    else:
        print('你输了')
    again=input('是否继续玩游戏?(y/n)')
    if again==('n'):
        print('游戏结束')
        break
