#1
letters="python"
print("첫번째 문자 : "+letters[0])
print("세번째 문자 : "+letters[2],end='\n\n')

#2
string="PYTHON"
for i in range(len(string)):
    print(string[len(string)-i-1],end='')
print(end='\n\n')

#3
url="http://sharebook.kr"
fine=input("찾을 문자를 입력해주세요 : ")
index = url.rfind(fine)
print(index)
for i in range(len(fine)):
    print(url[index+i],end='')
print()

#4
file_name="보고서.xlsx"
if file_name.endswith('xlsx'):
    print('xlsx로 끝나는 파일 이름입니다.',end='\n\n')

#5
file_name="2020_보고서.xlsx"
if file_name.startswith('2020'):
    print('2020으로 시작하는 파일 이름입니다.',end='\n\n')


#6
score=int(input("점수를 입력하세요 : "))
if(score>80) : print("A")
if(score>60 and score<81) : print("B")
if(score>40 and score<61) : print("C")
if(score>20 and score<41) : print("D")
if(score<21) : print("E")
print()

#7
cook=["피자","김밥","만두","양념치킨","족발","김치만두","쫄면","소시지","라면","팥빙수","김치전"]
print(len(cook),end='\n\n')

#8
warn_investment_list=["Microsoft","Google","Naver","Kakao","SAMSUNG","LG"]
a=input("투자 종목명을 입력해주세요 : ")
for i in warn_investment_list:
    if(a.find(i)!=-1):
        exsit=1
    else:
        exsit=0

if(exsit==1):
    print("투자 경고 종목입니다.",end='\n\n')
else:
    print("투자 경고 종목이 아닙니다.",end='\n\n')

#9
num_list=[100,200,300]
for i in num_list:
    print(i+10)
print()

#10
list=["SK하이닉스","삼성전자","LG전자"]
for i in list:
    print(len(i))