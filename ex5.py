height = input("请输入身高（单位：米）：")
weight = input("请输入体重（单位：千克）：")
bmi = float(weight)/(float(height)*float(height))
print("您的BMI指数（体重身高比）为：%.2f" % bmi)
if bmi<18.5:
    print("您的体重过轻")
elif bmi < 25:
    print("您的体重正常")
elif bmi < 28:
    print("您的体重过重")
elif bmi < 32:
    print("您的体重肥胖")
else:
    print("您的体重严重肥胖")
