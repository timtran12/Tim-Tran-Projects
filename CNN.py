#Tim Tran
#1001638285


# importing required libraries
import numpy as np
from keras.datasets import mnist

# defining the Sigmoid Function
def sigmoid (x):
        return 1/(1 + np.exp(-x))

# derivative of Sigmoid Function
def derivatives_sigmoid(x):
        return x * (1 - x)

def neural_network(layers = 4, units_per_layer = 500, rounds = 50):
    # loading dataset
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    
    hidden_layers = layers - 2
    learning_rate = .01

    # selecting a subset of data (200 images)
    x_train = x_train[:200]
    y = y_train[:200]

    X = x_train.T
    X = X/255

    y.resize((200,1))
    y = y.T

    # converting into binary classification
    #Not needed for multi-class
    for i in range(y.shape[1]):
        if y[0][i] >4:
            y[0][i] = 1
        else:
            y[0][i] = 0

    f=np.random.uniform(size=(3,5,5))
    f = f.T

    #print('Filter 1', '\n', f[:,:,0], '\n')
    #print('Filter 2', '\n', f[:,:,1], '\n')
    #print('Filter 3', '\n', f[:,:,2], '\n')

    # Generating patches from images
    new_image = []

    # for number of images
    for k in range(X.shape[2]):
        # sliding in horizontal direction
        for i in range(X.shape[0]-f.shape[0]+1):
            # sliding in vertical direction
            for j in range(X.shape[1]-f.shape[1]+1):
                new_image.append(X[:,:,k][i:i+f.shape[0],j:j+f.shape[1]])
                
    # resizing the generated patches as per number of images
    new_image = np.array(new_image)
    new_image.resize((X.shape[2],int(new_image.shape[0]/X.shape[2]),new_image.shape[1],new_image.shape[2]))

    # number of features in data set
    s_row = X.shape[0] - f.shape[0] + 1
    print(X.shape[0])
    print(f.shape[0])
    print(s_row)
    s_col = X.shape[1] - f.shape[1] + 1
    print(X.shape[0])
    print(f.shape[1])
    print(s_col)
    num_filter = f.shape[2]
    print(num_filter)

    inputlayer_neurons = (s_row)*(s_col)*(num_filter)
    output_neurons = 1

    # initializing weight
    wo=np.random.uniform(size=(inputlayer_neurons,output_neurons))

    for i in range(rounds):

        # generating output of convolution layer
        filter_output = []
        # for each image
        for i in range(len(new_image)):
            # apply each filter
            for k in range(f.shape[2]):
                # do element wise multiplication
                for j in range(new_image.shape[1]):
                    filter_output.append((new_image[i][j]*f[:,:,k]).sum())
                    
        filter_output = np.resize(np.array(filter_output), (len(new_image),f.shape[2],new_image.shape[1]))
        
        if hidden_layers != 0:
            hidden_output = []
            final_output = []
            previous_output = filter_output
            for h in range(hidden_layers):
                for i in range(len(previous_output)):
                    for k in range(f.shape[2]):
                        for j in range(units_per_layer):
                            final_output.append((previous_output[i][k][j]*f[:,:,k]).sum())
                previous_output = final_output
                previous_output = np.resize(np.array(previous_output), (len(new_image),f.shape[2],new_image.shape[1]))
                final_output = []
                            
            hidden_output = previous_output
                
        else:
            hidden_output = filter_output

        # applying activation over convolution output
        filter_output_sigmoid = sigmoid(hidden_output)

        # generating input for fully connected layer
        filter_output_sigmoid = filter_output_sigmoid.reshape((filter_output_sigmoid.shape[0],filter_output_sigmoid.shape[1]*filter_output_sigmoid.shape[2]))

        filter_output_sigmoid = filter_output_sigmoid.T

        # Linear transformation for fully Connected Layer
        output_layer_input= np.dot(wo.T,filter_output_sigmoid)
        output_layer_input = (output_layer_input - np.average(output_layer_input))/np.std(output_layer_input)

        # activation function
        output = sigmoid(output_layer_input)

        error_value = y-output
        error_value = -error_value

        deriv_sigmoid_output=derivatives_sigmoid(output)

        copy_filter_output_sigmoid=filter_output_sigmoid
        sigmoid_dotproduct = np.dot(copy_filter_output_sigmoid,(error_value * deriv_sigmoid_output).T)

        wo = wo - learning_rate*sigmoid_dotproduct
        
        deriv_sigmoid_x2_filter_output = derivatives_sigmoid(filter_output_sigmoid)
        
        weight_transform = wo.T

        filter_output_error = np.dot(weight_transform.T,error_value*deriv_sigmoid_output) * deriv_sigmoid_x2_filter_output
        
        filter_output_error = np.average(filter_output_error, axis=1)
        
        filter_output_error = np.resize(filter_output_error,(X.shape[0]-f.shape[0]+1,X.shape[1]-f.shape[1]+1, f.shape[2]))

        filter_update = []
        for i in range(f.shape[2]):
            for k in range(f.shape[0]):
                for j in range(f.shape[1]):            
                    temp = 0
                    rows = k
                    cols = j
                    e_row = rows + s_row
                    e_col = cols + s_col
                    for l in range(X.shape[2]):
                        temp = temp + (X[rows:e_row,cols:e_col,l]*filter_output_error[:,:,i]).sum()
                    filter_update.append(temp/X.shape[2]) 

        filter_update_array = np.array(filter_update)
        filter_update_array = np.resize(filter_update_array,(f.shape[2],f.shape[0],f.shape[1]))

        for i in range(f.shape[2]):
            f[:,:,i] = f[:,:,i] - learning_rate*filter_update_array[i]
    
    f = open("output.txt", "w")
          
    predicted_classes = []
    for i in range(len(output[0])):
        if(output[0][i] > .5):
            prediction = 1
            predicted_classes.append(prediction)
        else:
            prediction = 0
            predicted_classes.append(prediction)
    
    counter = 0
    accuracies = []
    for i in range(len(y[0])):
        if y[0][i] == predicted_classes[i]:
            counter+=1
            accuracies.append(1)
            
        else:
            accuracies.append(0)
            
    f.write("Tim Tran\n1001638285\n")
    
    for i in range(len(y[0])):
        f.write('ID=%5d, predicted=%3d, true=%3d, accuracy=%4.2f\n' % (i+1, predicted_classes[i], y[0][i], accuracies[i]))
        
    f.write("Classification Accuracy= %6.2f%%" % ((counter/200)*100))
    
    f.close()
    
neural_network()