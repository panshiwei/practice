import tensorflow as tf
tf.logging.set_verbosity(tf.logging.ERROR)

import numpy as np
celsius_q=np.array([-40,-10,0,8,15,22,38],dtype=float)
fahrenheit_a=np.array([-40,14,32,46,59,72,100],dtype=float)

l0 = tf.keras.layers.Dense(units=1, input_shape=[1])

model = tf.keras.Sequential([l0])

model.compile(loss='mean_squared_error',
              optimizer=tf.keras.optimizers.Adam(0.1))
model.fit(celsius_q,fahrenheit_a,epochs=5000)

history = model.fit(celsius_q, fahrenheit_a, epochs=500, verbose=False)
print("Finished training the model")

import matplotlib.pyplot as plt
plt.xlabel('Epoch Number')
plt.ylabel("Loss Magnitude")
plt.plot(history.history['loss'])
plt.show()
x=int(input())
print(model.predict([x]))

print("These are the layer variables: {}".format(l0.get_weights()))


