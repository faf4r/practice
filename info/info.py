name = input('请输入您的姓名：')
age = input('请输入您的年龄：')
sex = input('请输入您的性别：')
job = input('请输入您的职业：')

msg = '''--------------Info of %s--------------
Name : %s
Age : %d
Sex : %s
Job : %s

----------------- end ----------------'''%(name, name, int(age), sex, job)

info = '我叫%s，我今年%d岁，我是%s生，职业是%s，已经完成了大学的85%%。'%(name, int(age), sex, job)

print(msg)
print(info)
