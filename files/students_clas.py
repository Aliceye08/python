class Students:
    def __init__(self):
        print('this is the program that gives average and sum')

    def file_Write(self):
        grades = ['100,90\n', '98,76\n', '89,2\n', '97,17\n', '100,90\n', '93,44\n', '97,68\n', '90,98\n', '90,100\n', '91,70\n']
        with open('grades.txt', 'w')as file:
            file.writelines(grades)

    def file_read(self):
        mt = []
        ko = []
        with open('grades.txt', 'r')as file:
            line = None
            while line != '':
                line = file.readline()
                if (line != ''):
                    b = line.split(',')
                    ko.append(int(b[0]))
                    mt.append(int(b[1]))
        return mt,ko

    def sum(self,mt,ko):
        sum = 0
        for i in mt:
            sum += i
        print('수학총합=', sum)
        print('수학평균=', sum / len(mt))

        for j in ko:
            sum += j
        print('국어총합=', sum)
        print('국어평균=', sum/len(ko))

