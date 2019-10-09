'''
    从数据库中登录,
'''

from mysqlpython import Mysqlpython
#sha1加密算法
from hashlib import sha1

uname = input('请输入用户名：')
pwd = input('请输入密码：')

#用sha1给pwd加密
s1 = sha1()   #创建sha1加密对象
s1.update(pwd.encode('utf8'))  #指定编码，转换为utf8格式，此时为10进制的密码
pwd2 = s1.hexdigest()   #返回16进制加密的结果

#连接数据库并执行相关操作
sqlh = Mysqlpython('stu')
select = 'select password from user where username=%s;'
result = sqlh.select_all(select,[uname])
# print(result)


if len(result) == 0:
    print('用户名不存在')

elif result[0][0] == pwd2:
    print('登录成功')

else:
    print("密码错误,请重新输入")

