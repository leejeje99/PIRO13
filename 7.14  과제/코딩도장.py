# 반복문
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# 중첩루프
# for i in range(5):
#     for j in range(5):
#         print('j:', j, sep='', end='')
    
#     print('i:', i, sep ='')
# 별사각형
# for i in range(5):
#     for j in range(5):
#         print('*', end = '')
#     print()\
# 계단식 한줄에 i개씩
# for i in range(5):
#     for j in range(5):
#         if j<=i:
#             print('*', end='')
#     print()
# height = int(input())
# for i in range(height):
#     for j in reversed(range(height)):
#         if j > i:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     for j in range(height):
#         if j < i:
#             print('*', end='')
#     print()  
            
            
# class Annie:
#     def __init__(self, health, mana, ability_power):
#         self.health = health
#         self.mana = mana
#         self.ability_power = ability_power
#     def tibbers(self):
#         print ('티버: 피해량 '+ str(self.ability_power*0.65+400))
# x = Annie(health=health, mana=mana, ability_power=ability_power)
# x.tibbers()
# class Time:
#     def __init__(self, hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#     @classmethod
#     def from_string(cls, time_string):
#         hour, minute, second = map(int, time_string.split(':'))
#         time = cls(hour, minute, second)
#         return time

#     @staticmethod
#     def is_time_valid(time_string):
#         hour, minute, second = map(int, time_string.split(':'))
#         return hour <= 24 and minute <= 59 and second <= 60

# time_string = input()

# if Time.is_time_valid(time_string):
#     t = Time.from_string(time_string)
#     print(t.hour, t.minute, t.second)
# else:
#     print('잘못된 시간 형식입니다.')
# class Bird(Wing, Animal):
#     def fly(self):
#         print('날다')

# def palindrome(x):
#     for i in range(len(x) // 2):
#         if x[i] == x[-1 - i]:
#             print(x)
#     else:
#        raise NotPalindromeError()
# 38강
# class NotPalindromeError(Exception):
#     def __init__(self):
#         print('희문이 아닙니다')
# def palindrome(x):
#     for i in range(len(x) // 2):
#         if x[i] == x[-1 - i]:
#             print(x)
# import math
# a = float(input())
# print(a*a*math.pi)
# import calcpkg.operation
# import calcpkg.geometry
# n =int(input())
# print(calcpkg.operation.squareroot(n))
# print(calcpkg.geometry.circle_area(n))

