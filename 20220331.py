#1
price_list=[32100,32150,32000,32500]
for i in range(4):
    print(i,end=' ')
    print(price_list[i])
print()

#2
for i in range(3):
    print(i*10+100,end=' ')
    print(price_list[i+1])
print()

#3
for i in range(13):
    print(2002+i*4)
print()

#4
for i in range(10):
    print(round(i*0.1,1))
print()

#5
ticker="btc_krw"
print(ticker.upper(),end='\n\n')

#6
file_name="보고서.xlsx"
if file_name.endswith('xlsx'):
    print('xlsx로 끝나는 파일 이름입니다.',end='\n\n')

#7
a = "hello world"
x = a.split()
print(x,end='\n\n')

#8
date ="2020-05-01"
d = date.split('-')
print(d,end='\n\n')

#9
stock = "5,969,782,550"
replace1 = int(stock.replace(",",""))
print(replace1,end='\n\n')

#10
a = "hello world"
x = a.split()
print(x,end='\n\n')

#11
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:],end='\n\n')

#12
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[1:10:2],end='\n\n')

#13
list = [3, 100, 23, 44]
for i in list:
    if(i%3 == 0):
        print(i)