class Students:
    def __init__(self):
        print('this is the program that gives average and sum')

    def file_Write(self):
        grades = ['100\n', '98\n', '89\n', '97\n', '100\n', '93\n', '97\n', '90\n', '90\n', '91\n']
        with open('grades.txt', 'w')as file:
            file.writelines(grades)

    def file_read(self):
        a = []
        with open('grades.txt', 'r')as file:
            line = None
            while line != '':
                line = file.readline()
                b = line.strip('\n')
                if (b != ''):
                    a.append(int(b))
        return a

    def sum(self, a):
        sum = 0
        for i in a:
            sum += i
        print('총합=', sum)
        print('평균=', sum / len(a))
