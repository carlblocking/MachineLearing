import tensorflow as tf
import numpy as np
from source2.test1 import net

raw_output2=np.load("a.npy")
label=np.load("b.npy")
label=np.reshape(label , [5, 5])

print(label)

raw_output=tf.cast(tf.convert_to_tensor(raw_output2), dtype=tf.float32)
  
raw_output=net(raw_output)

raw_output=tf.argmax(raw_output, dimension=3)
  
saver=tf.train.Saver()
  
with tf.Session() as sess:
    saver.restore(sess, "./test.ckpt")
    print(raw_output.eval())

