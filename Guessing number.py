import random
answer=random.randint(1,1000)
while True:
     guess=int(input('请输入数字:'))
     if guess<answer:
         print('太小了')
     elif guess==answer:
         print('恭喜你,答对了')
         break
     else:
         print('太大了')
         