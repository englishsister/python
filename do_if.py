#if 条件判断
age = 25
if age >= 30:
    print("hah")
elif age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("kid")

"""
input,
input函数返回str类型，必须通过int()将字符串转换为int类型，
否则if条件判断语句出错
"""
birth = int(input("birh:"))
if birth < 2000:
	print("00前")
else:
	print("00后")

"""
练习

小明身高1.75，体重80.5kg。
请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖

BMI公式 = 體重(公斤) / 身高2(公尺2)
"""
height = float(input("您的身高:"))
weight = float(input("您的体重:"))
BIM = weight/(height*height)
if BIM < 18.5:
	print("您的体重过轻")
elif BIM <= 25:
	print("您的体重正常")
elif BIM <= 28:
	print("您的体重过重")
elif BIM <= 32:
	print("您的体重肥胖")
else :
	print("您的体重严重肥胖")
