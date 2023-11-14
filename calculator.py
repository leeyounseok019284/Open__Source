def add(a,b):
    return a+b;
def sub(a,b):
    return a-b;
def mul(a,b):
    return a*b;
def div(a,b):
    return a/b;

buho=input("부호 입력");
a=int(input("첫번째 숫자 입력 : "));
b=int(input("두번째 숫자 입력: "))

if(buho=="+"):
    print(a,"+",b,"=",add(a,b));

if(buho=="-"):
    print(a,"-",b"=",sub(a,b));

if(buho=="*"):
    print(a,"*",b,"=",mul(a,b));

if(buho=="/"):
    print(a,"/",b,"=",div(a,b));
