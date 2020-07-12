# 13강 
# money = int(input())
# coupon = input()
# if coupon == 'Cash3000':
#     money -= 3000
# elif coupon == 'Cash5000':
#     money -= 5000
# print(money)
# --------------------------------------------------------
#16강
# korean, english, math, science = map(int, input().split())
# if korean > 100 or korean < 0 or english > 100 or english < 0 or math > 100 or math < 0 or science > 100 or science < 0:
#     print('잘못된 점수')
# elif (korean+english+math+science)/4>=80:
#     print('합격')
# else:
#     print('불합격')
# --------------------------------------------------------
#17강
# money = int(input())
# while 0<= money and 1350<=money:
#     money-=1350
#     print(money)
# --------------------------------------------------------
#18강
# start, stop = map(int, input().split())

# i = start

# while True:
#     if i%10 ==3:
#         i += 1
#         continue
#     if i>200:
#         break
# --------------------------------------------------------
#19강
# a = int(input())
# for i in range(a):        # 0부터 4까지 5번 반복. 세로 방향
#     for j in range(a*2):    # 0부터 4까지 5번 반복. 가로 방향
#         if j <= i:                # 세로 방향 변수 i만큼
#             print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
#     print('*')
# --------------------------------------------------------
#21강
# import turtle as t
# t.Shape('turtle')
# --------------------------------------------------------
# 22강
# --------------------------------------------------------
# 23
# a, b = map(int, input().split())
# c = [2 ** i for i in range(a, b + 1)]
# c.pop(1)
# c.pop(-2)
# print(c)
# --------------------------------------------------------
# 24-1 틀림
# paragraph = input()
# words=list(paragraph.split(''))
# for i in words:
#     count=0
#     i.strip(',.')
#     if i == 'the':
#         count+=1
# print(count)
    

# 24-2
# money = map(input().split(';'))
# money2= list(money).sort(reverse=True)
# for i in money2(format{0:>9}):
#     print(i)

# --------------------------------------------------------
# 25 틀림
# del x['delta']
# {key: value for keys, values in x if value != 30}
# --------------------------------------------------------
# 26 
# num1, num2 = map(int, input().split())
# a = {i for i in range(1, num1 + 1) if num1 % i == 0}
# b = {i for i in range(1, num2 + 1) if num2 % i == 0}
# with open('words.txt', 'r') as file:
# --------------------------------------------------------
# 27 틀림
# file = open('word.txt','r')
# s =file.read()
# slist = list(s.split())
# for i in slist:
#     if 'c' in i:
#         i.strip('.,')
#         print(i)
# --------------------------------------------------------
# 28
# with open('words.txt','r') as file:
#     words = list(file.readlines())
#     for word in words:
#         word = word.strip('\n')
#         if word == word[::-1]:
#             print(word)
# --------------------------------------------------------
# 29강
# def calc(x, y):
#     return(x+y, x-y, x*y, x/y)
# --------------------------------------------------------
# 30강
# def get_min_max_score(*args):
#     return min(args), max(args)
# def get_average(**kwargs):
#     return sum(kwargs.values())/len(kwargs)
# --------------------------------------------------------
# 31강
# def fib(n):
#     if n<=1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)

# --------------------------------------------------------
# 32강
# list(map(lambda x: int(x.split('.')[0]+'.'+x.split('.')[1])(file.split())


    

    







    

    

        
        


   


    
