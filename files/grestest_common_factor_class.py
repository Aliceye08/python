
class gcf:
    def __init__(self):
        print('이 프로그램은 각 수의 약수와 두수의 최대공배수를 구하는 프로그램입니다.')
    def input(self,input_number):
        value=[]
        for i in range(0,input_number):
           tmp=int(input(str(i+1)+'번째수:'))
           value.append(tmp)
        return value

    def divisor(self,value):
        h=[]
        for i in range(1,value+1):
         if value%i==0:
            # print('첫번째 수의 약수:',i)
            h.append(i)

        return h

    def common_variables(self,h1,h2):
        rvalue=[]
        for i in h1:
            for j in h2:
                if i == j:
                    rvalue.append(i)

        return rvalue






