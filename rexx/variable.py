__author__ = 'Administrator'

import tensorflow as tf
import numpy as np
def fun():
    state=tf.Variable(0,name='counter')
    print(state.name)

    one =tf.constant(1)
    new_value=tf.add(state,one)
    update=tf.assign(state,new_value)
    init=tf.initialize_all_variables()

    with tf.Session() as sess:
        sess.run(init)
        for _ in range(3):
            sess.run(update)
            print(sess.run(state))
def variableDemo():
    state=tf.Variable(0,name="counter")

    one =tf.constant(1)
    new_value =tf.add(state,one)
    update=tf.assign(state,new_value)
    init_op=tf.initialize_all_variables()
    with tf.Session() as sess:
        sess.run(init_op)
        print(sess.run(state))
        for _ in range(3):
            sess.run(update)
            print(sess.run(state))

def multiDemo():
    input1=tf.constant(3)
    input2=tf.constant(5)
    input3=tf.constant(2)
    sum1=tf.add(input2,input3)
    multi=tf.mul(sum1,input1)
    with tf.Session() as sess:
        # init=tf.initialize_all_variables()
        # sess.run(init)
        print(sess.run([multi,sum1]))
def use_Feed_demo():
    input1=tf.placeholder(tf.float32)
    input2=tf.placeholder(tf.float32)
    mult=tf.add(input1,input2)
    with tf.Session() as sess:
        print(sess.run([mult],feed_dict={input1:[7.],input2:[3.]}))

def add_layer(inputs,in_size,out_size,activation_function=None):    # 输入值、输入的大小、输出的大小和激励函数
    Weights=tf.Variable(tf.random_normal([in_size,out_size]))
    biases=tf.Variable(tf.zeros([1,out_size])+0.1)
    Wx_plus_b=tf.matmul(inputs,Weights)+biases
    if activation_function is None:
        outputs=Wx_plus_b
    else:
        outputs=activation_function(Wx_plus_b)
    return outputs

variableDemo()
multiDemo()
use_Feed_demo()
add_layer(1,)



