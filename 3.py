import datetime

today=datetime.date.today()
week = today.weekday()
print(week)
oneday=datetime.timedelta(days=2)
yesterday=today-oneday
week = yesterday.weekday()
print(week)
yesterday = yesterday.strftime('%Y年%m月%d日')



# 输出/home/yxj touch ~/MyCrontab1 && nano ~/MyCrontab1  /home/yxj/PycharmProjects/test/
# print(getYesterday())
# def f():
#     a=1
#     b=[1,2,3,4,5,6,7,8,9,['w','q']]
#     print(len(b))
#     print(b[9][0])
#     if 10 not in b:
#         print("true")
#     c=3
#     return a,b,c;
# if __name__ == '__main__':
#     x,y,z=f()
#     t=f()
#     print(t)
#     print(x,y,z)