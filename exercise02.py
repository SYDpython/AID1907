'''
实心金字塔
  *
 ***
*****
'''
str_row = input('请输入行数:')
try:
    row = int(str_row)
    if row <= 0:
        print('请输入正整数')
    else:
        for i in range(row):
            for j in range(row-i-1):
                print(' ',end='')
            for k in range(2*i+1):
                print('*',end='')
            print()
except Exception as e:
    print(e)
    print('请输入正确的正整数')
