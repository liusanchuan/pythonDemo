__author__ = 'Administrator'
# from __future__ import print_function,division

from scipy.io import loadmat as load
import matplotlib.pyplot as plt
import numpy as np
def reformat(samples,labels):
    new =np.transpose(samples,(3,0,1,2))
    labels =np.array([x[0] for x in labels])
    one_hot_lables=[]
    for num in labels:
        one_hot=[0.0]*10
        if num==10:
            one_hot[0]=1.0
        else:
            one_hot[num]=1.0
        one_hot_lables.append(one_hot)
    labels =np.array(one_hot_lables).astype(np.float32)
    return new,labels

def inspect(dataset,labels,i):
    #显示图片看看
    if dataset.shape[3]==i:
        shape=dataset.shape
        dataset=dataset.reshape(shape[0],shape[1],shape[2])
    print(labels[i])
    plt.imshow(dataset[i])
    plt.show()
def distribution(labels, name):
    # 查看一下每个label的分布，再画个统计图
    # keys:
    # 0
    # 1
    # 2
    # ...
    # 9
    count = {}
    for label in labels:
        key = 0 if label[0] == 10 else label[0]
        if key in count:
            count[key] += 1
        else:
            count[key] = 1
    x = []
    y = []
    for k, v in count.items():
        # print(k, v)
        x.append(k)
        y.append(v)
    y_pos = np.arange(len(x))
    plt.bar(y_pos, y, align='center', alpha=0.5)
    plt.xticks(y_pos, x)
    plt.ylabel('Count')
    plt.title(name + ' Label Distribution')
    plt.show()

def normalize(samples):
    ###
    # @samples:numpy array
    # #将图片从0~255现行映射到-1.0~1.0
    # #并且灰度化：从三色通道-》三色通道 省内存+加快训练速度
    # (R+G+B)/3
    #
    a=np.add.reduce(samples,keepdims=True,axis=3)
    a=a/3
    return a/128-1


train =load('train_32x32.mat')
train_samples=train['X']
train_lables=train['y']

# print('Train Sample',train['X'])
print('Train Sample',train['y'].shape)

_train_sample,_train_lables=reformat(train_samples,train_lables)

# inspect(_train_sample,_train_lables,1000)
distribution(train_lables,"Train_lable")
# _train_sample=normalize(_train_sample)
# inspect(_train_sample,_train_lables,1000)
