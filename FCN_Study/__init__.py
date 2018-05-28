import numpy as np 
import matplotlib.pyplot as plt
import tensorflow as tf

def prepare_label(image_data, new_size):
    image=tf.image.resize_nearest_neighbor(image_data, new_size)
    input_batch=tf.squeeze(image, squeeze_dims=[3])
    return input_batch

raw_output=np.random.randint(0, 3, [4,4])
print("raw_output:", raw_output)
raw_output=tf.cast(raw_output, dtype=tf.float32)
raw_prediction=tf.reshape(raw_output, [-1,4])

label_raw_data=np.random.randint(0, 3, [1,4,4,1])
print("label_raw_data:", label_raw_data)
label_data=tf.cast(label_raw_data, dtype=tf.int32)
label_data=tf.squeeze(label_data, squeeze_dims=[3])

label_data2=tf.reshape(label_data, [-1,])

indices=tf.squeeze(tf.where(tf.less_equal(label_data2, 3)), 1)

gt=tf.cast(tf.gather(label_data2, indices), tf.int32)

prediction=tf.gather(raw_prediction, indices)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print("raw_prediction:", raw_prediction.eval())
    print("label_data:", label_data.eval())
    print("label_data2:", label_data2.eval())
    print("indices:", indices.eval())
    
    print("gt:", gt.eval())
    print("prediction:", prediction.eval())

    
