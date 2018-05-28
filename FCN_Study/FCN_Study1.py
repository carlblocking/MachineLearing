import tensorflow as tf
import numpy as np

def prepare_label(input_batch, new_size):
    input_batch = tf.image.resize_nearest_neighbor(input_batch, new_size) 
    input_batch = tf.squeeze(input_batch, squeeze_dims=[3]) 
    return input_batch

raw_output=np.random.randint(0, 255, (1, 3, 3, 3))
label_batch=np.random.randint(0, 5, (1, 3, 3, 1))

raw_output=tf.cast(tf.convert_to_tensor(raw_output), dtype=tf.float32)

weights1=tf.Variable(tf.random_normal([3,3,3,4], name="weight1"))
raw_output=tf.nn.conv2d(raw_output, weights1, [1,1,1,1], padding='SAME', name="conv1")

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
    print(tf.stack(raw_output.get_shape()[1:3]).eval())
#     print("raw_output:", raw_prediction.eval())
#     print("label_proc:", label_proc.eval())
#     print("indicies:", indicies.eval())

#     print("gt:", gt.eval())
#     print("prediction:" , prediction.eval())
#     print(sparse_loss.eval())
    for i in range(1,1000):
        sess.run(train_step)
        if(i%100==0):
            print(loss_total.eval())
    saver.save(sess, "./test.ckpt")
        























