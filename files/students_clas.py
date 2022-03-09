class Students:
    def __init__(self):
        print('this is the program that gives average and sum')

    def file_Write(self,std_name,std_grade):
        with open(std_name+'.txt', 'w')as file:
            file.writelines(std_grade)

    def file_read(self,std_name):
        mt = []
        ko = []
        with open(std_name+'.txt', 'r')as file:
            line = None
            while line != '':
                line = file.readline()
                if (line != ''):
                    b = line.split(',')
                    ko.append(int(b[0]))
                    mt.append(int(b[1]))
        return mt,ko

    def sum(self,mt,ko,std_name):
        sum = 0
        for i in mt:
            sum += i
        print(std_name+'수학총합=', sum)
        print(std_name+'수학평균=', sum / len(mt))

        sum=0
        for j in ko:
            sum += j
        print(std_name+'국어총합=', sum)
        print(std_name+'국어평균=', sum/len(ko))

