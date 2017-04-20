import numpy as np
from flask import Flask

app=Flask(__name__)
@app.route('/')
def helloWord():
	return "hello Word"
if __name__=='__main__':
	app.run('0.0.0.0',12345)
# a=np.array([[3,3,3],[2,2,2]])
# print(a.shape)
# print(a.ndim)
# print(a.size)
# print(a.dtype)
# def printl(E=np.array()){
# 	print(E)
# 	print(E.shape)
# 	print(E.size)
# }
b=np.arange(27,dtype=float).reshape(3,3,3)
print(b)
print(b.shape)
print(b.size)
print("____________")
student=np.dtype({'names':['name', 'age', 'weight'], 'formats':['S32', 'i','f']}, align = True)
c=np.arange([("zhangsna",12,22.5),("lisi",17,20)],dtype=student)
print(c)
print(c.dtype)
