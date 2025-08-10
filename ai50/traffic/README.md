model1: [loss: 3.5037 - accuracy: 0.0556 - 1s/epoch - 4ms/step]
filters = 32
kernel = (3, 3)
pool_size = (2,2)
hidden_layer = 128 neurons
dropout = 0.5

model2: [loss: 0.5779 - accuracy: 0.8282 - 1s/epoch - 4ms/step]
filters = 32
kernel = (6, 6)
pool_size = (4,4)
hidden_layer = 128 neurons
dropout = 0.5

model3: [loss: 0.4367 - accuracy: 0.8911 - 1s/epoch - 4ms/step]
filters = 32
kernel = (6, 6)
pool_size = (4,4)
hidden_layer_1 = 128 neurons
hidden_layer_2 = 256 neurons
dropout = 0.5

model4: [loss: 0.2098 - accuracy: 0.9608 - 4s/epoch - 12ms/step]
layer_1_filters = 32
layer_2_filers = 64
kernel = (6, 6)
pool_size = (4,4)
hidden_layer_1 = 128 neurons
hidden_layer_2 = 256 neurons
dropout = 0.5

model5: [loss: 0.1249 - accuracy: 0.9711 - 4s/epoch - 12ms/step]
layer_1_filters = 32
layer_2_filers = 64
kernel = (6, 6)
pool_size_layer_1 = (4,4)
pool_size_layer_2 = (2,2)
hidden_layer_1 = 128 neurons
hidden_layer_2 = 256 neurons
dropout = 0.5

model6: [loss: 0.0697 - accuracy: 0.9843 - 4s/epoch - 12ms/step]
layer_1_filters = 32
layer_2_filers = 64
kernel = (6, 6)
pool_size_layer_1 = (4,4)
pool_size_layer_2 = (2,2)
hidden_layer_1 = 128 neurons
hidden_layer_2 = 256 neurons
dropout = 0.4

Summary:
    I started with a very simple model(model1) similar to the model in handwritting.py. The model was very inaccurate. In the model_2 i changed the size of the kernel and pool_size by doubling there dimensions. As a result, the model accuracy jumped significantly to about 80% accurate. Next, in model_3 i added one more hidden layer with 256 neurons while using the same dropout of 50%. This model also did well compared to prior models as the accuracy was about 90%. In model_4, i further added another layer of convolution with 64 neurons while keeping the kernel size same. Consequently, accuracy jumped to about 95%. Beside this, in model_5 i added one more pooling layer with pooling matrix of (2, 2) and accuracy increased to about 97%. Finally, i reduced the dropout from 0.5 to 0.4 and that resulted into an accuracy of about 98%.

    As i was making changes through these models, i realized adding more than 2 hidden layers didn't make any noticable contribution to accuracy. Also, more convolution layers and bigger kernel size or pooling sizes didn't show improvement to accuracy. 