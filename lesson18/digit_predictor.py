# import tensorflow as tf
# from tensorflow.keras import layers, models
# import matplotlib.pyplot as plt 
# #load mnist dataset 
# (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# #normalizing the data
# x_train, x_test = x_train / 255.0, x_test / 255.0 
# #building the model 
# model.compile(
#     optimizer = 'adam', #adam = adaptive moment estimation (algorithm)
#     loss = 'sparse_categorical_crossentropy' ,
#     metrics = ['accuracy'] #tracks the accuracy  
# )
# #train the model 
# model.fit (x_train, y_train, epochs = 5)
# #evaluate the model
# test_loss, test_acc = model.evaluate(x_test, y_test)
# print (f"test accuracy : {test_acc}")
# #make predictions
# predictions = model.predict(x_test)
# #display a sample prediction
# plt.imshow(x_test[0], cmap = plt.cm.binary)
# plt.title(f"Predicted : {predictions[0].argmax()}") 
# plt.show()
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize the data
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build the model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Flatten the 28x28 image
    layers.Dense(128, activation='relu'),  # Fully connected layer
    layers.Dense(10, activation='softmax')  # Output layer for 10 classes
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}")

# Make predictions
predictions = model.predict(x_test)

# Display a sample prediction
plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.title(f"Predicted: {predictions[0].argmax()}")
plt.show()
