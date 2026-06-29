player=input('请输入石头,剪刀,布:')
import random
import time
computer=random.choice(['石头','布','剪刀'])
print('你出了:',player)
print('电脑出了:')
time.sleep(1)
print(computer)
if player=='石头' and computer=='布':
    print('你输了')
elif player=='石头' and computer=='石头':
    print('平局')
elif player=='石头' and computer=='剪刀':
    print('你赢了')
elif player=='布' and computer=='布':
    print('平局')
elif player=='布' and computer=='石头':
    print('你赢了')
elif player=='布' and computer=='剪刀':
    print('你输了')
elif player=='剪刀' and computer=='布':
    print('你赢了')
elif player=='剪刀' and computer=='石头':
    print('你输了')
elif player=='剪刀' and computer=='剪刀':
    print('平局')
