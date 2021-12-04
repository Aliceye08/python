import os


class Questions:
    def __init__(self):
        print('문제:(2+1)*7...')

    def display(self):
        a = ['1번:20,''2번:21,''3번:22,''4번:23']
        for i in a:
            print('보기:', i)

    def questions_write(self):
        a = ['1번:20', '2번:21', '3번:22', '4번:23']
        fName = 'yoohoo.txt'
        isFileEixts = os.path.isfile(fName)
        if not isFileEixts:
            with open(fName, 'w') as file:
                for i in a:
                    file.write(i + '\n')

    def questions_read(self):
        str = ''
        with open('yoohoo.txt', 'r') as file:
            lines = file.readlines()
            ln = len(lines)
            k = 0
            for i in lines:
                str += i.strip('\n')
                k += 1
                if k < ln:
                    str += ','

        print('보기:', str)

    def answer(self):
        i = 0
        while i == 0:

            try:
                answer = int(input('답:'))
                if answer == 2:
                    print('정답입니다!')
                    break
                elif answer < 5:
                    print('답이 아닙니다.')
                else:
                    print('보기에 없는 답입니다.')
            except:
                print('예외가 발생했습니다.')
