import files.students_clas as sc

myCls = sc.Students()
yesol_grades = ['90,98\n', '90,100\n']
seonghwan_grades = ['89,2\n', '97,17\n']
names = ['yesol', 'seonghwan']

grades = [yesol_grades, seonghwan_grades]
k = 0
for name in names:
    myCls.file_Write(name, grades[k])
    list = myCls.file_read(name)
    myCls.sum(list[0], list[1], name)
    k = k + 1

students = {
    "name": ["yesol", "seonghwan"],
    "grade": ['90,98', '90,100', '89,2', '97,17']
}
for student in students:
    print('studen=', students[student])
