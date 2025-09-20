import tensorflow as tf
import mathplotlib.pyplot as plt
(x_train,y_train),(x_test,y_test) = tf.keras.datasets.mnist.load_data()
x_train,x_test = x_train /255.0 , x_test / 255.0
model = tf.keras.models.Sequintal([
    tf.keras.layers.Flatten = (input_shape=(28,28)),
    tf.keras.layers.Dense = (128, activation = 'relu'),
    tf.keras.layers.Dense = (10,activation = 'softmax')
])
model.compile(
    optimizer = 'adam'
    loss = 'sparse_categorical_crosssentry'
    metrics = ['accuracy']
)
model.fit(x_train,y_train,epchos = 5)
test_loss , test_acc = (x_test)
print(f"test:{test_acc}")
pred = model.predict(x_test)
plt.impshow(x_test[0],cmap='binary')
plt.title("Predicted:{pred[0].argmax()}")
plt.show()