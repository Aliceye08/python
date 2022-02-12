import files.grestest_common_factor_class as gcf

myCls = gcf.gcf()
input_num=2
m = myCls.input(input_num)

h1 = myCls.divisor(m[0])
h2 = myCls.divisor(m[1])
print(m[0], '의 약수:', h1)
print(m[1], '의 약수:', h2)
cmd_result = myCls.common_variables(h1, h2)

print('공통약수:', cmd_result)
print('최대공약수:', max(cmd_result))
