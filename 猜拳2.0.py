import random
import time
player=input('请输入石头,剪刀或布:')
computer=random.choice(['石头','剪刀','布'])
print('你出了:',player)
print('电脑出了:.....')
time.sleep(1)
print(computer)
if player==computer:
    print('平局')
elif (
    player=='石头' and computer=='剪刀'
    ) or(
    player=='剪刀' and computer=='布'
    ) or(
    player=='布' and computer=='石头'
    ):
    print('你赢了')
else:
    print('你输了')
