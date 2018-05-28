import tensorflow as tf
import numpy as np
from source2.test1 import net

def prepare_label(input_batch, new_size):
    input_batch = tf.image.resize_nearest_neighbor(input_batch, new_size) 
    input_batch = tf.squeeze(input_batch, squeeze_dims=[3]) 
    return input_batch

# raw_output=np.random.randint(0, 255, (1, 3, 3, 3))
# label_batch=np.random.randint(0, 3, (1, 3, 3, 1))

raw_output=np.load("a.npy")
label_batch=np.load("b.npy")

raw_output=tf.cast(tf.convert_to_tensor(raw_output), dtype=tf.float32)

raw_output=net(raw_output)

label_batch=tf.cast(label_batch, dtype=tf.int32)

raw_prediction=tf.reshape(raw_output, [-1, 4])
label_proc=prepare_label(label_batch, tf.stack(raw_output.get_shape()[1:3]))

raw_gt=tf.reshape(label_proc, [-1,])

indicies=tf.squeeze(tf.where(tf.less_equal(raw_gt, 3)), 1)

gt=tf.cast(tf.gather(raw_gt, indicies), tf.int32)

prediction=tf.gather(raw_prediction, indicies)

sparse_loss=tf.nn.sparse_softmax_cross_entropy_with_logits(labels=gt, logits=prediction)

loss_total=tf.reduce_mean(sparse_loss)

train_step=tf.train.AdamOptimizer(0.0001).minimize(loss_total)

saver=tf.train.Saver(var_list=tf.global_variables())

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1,10000):
        sess.run(train_step)
        if(i%100==0):
            print(loss_total.eval())
    saver.save(sess, "./test.ckpt")
    
    
    
    
    
    
    
    
    
    