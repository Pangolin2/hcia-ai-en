import numpy as np
import matplotlib.pyplot as plt


def generate_gradient(X, theta, y):
    sample_count = X.shape[0]
    # Calculate the gradient based on the matrix 1/m sum(((h(x^i)-y^i)) x_j^i)
    return (1. / sample_count) * X.T.dot(X.dot(theta) - y)


def get_training_data(file_path):
    orig_data = np.loadtxt(file_path, skiprows=1) # Ignore the title in the first row of the dataset.
    cols = orig_data.shape[1]
    return (orig_data, orig_data[:, :cols - 1], orig_data[:, cols - 1:])


# Initialize the theta array.
def init_theta(feature_count):
    return np.ones(feature_count).reshape(feature_count, 1)


def gradient_descending(X, y, theta, alpha):
    Jthetas = [] # Record the change trend of the cost function J(theta) to confirm the gradient descent is correct.
    # Calculate the loss function, which is equal to the square of the difference between the actual
    # value and the predicted value: (y^i-h(x^i))^2
    Jtheta = (X.dot(theta) - y).T.dot(X.dot(theta) - y)
    index = 0
    gradient = generate_gradient(X, theta, y) # Calculate the gradient.
    while not np.all(np.absolute(gradient) <= 1e-5): # End the calculation when the gradient is less than 0.00001.
        theta = theta - alpha * gradient
        gradient = generate_gradient(X, theta, y) # Calculate the new gradient.
        # Calculate the loss function, which is equal to the square of the difference between the actual
        # value and the predicted value: (y^i-h(x^i))^2
        Jtheta = (X.dot(theta) - y).T.dot(X.dot(theta) - y)
        if (index + 1) % 10 == 0:
            Jthetas.append((index, Jtheta[0])) # Record the result every 10 calculations.
        index += 1
    return theta, Jthetas


# Plot the loss function change curve.
def showJTheta(diff_value):
    p_x = []
    p_y = []
    for (index, sum) in diff_value:
        p_x.append(index)
        p_y.append(sum)
    plt.plot(p_x, p_y, color='b')
    plt.xlabel('steps')
    plt.ylabel('loss funtion')
    plt.title('step - loss function curve')
    plt.show()


# Plot the actual data points and the fitted curve.
def showlinercurve(theta, sample_training_set):
    x, y = sample_training_set[:, 1], sample_training_set[:, 2]
    z = theta[0] + theta[1] * x
    plt.scatter(x, y, color='b', marker='x', label="sample data")
    plt.plot(x, z, 'r', color="r", label="regression curve")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('liner regression curve')
    plt.legend()
    plt.show()


# Read the dataset.
training_data_include_y, training_x, y = get_training_data("./ML/02/lr2_data.txt")
# Obtain the numbers of samples and features, respectively.
sample_count, feature_count = training_x.shape
# Define the learning step alpha.
alpha = 0.01
# Initialize theta.
theta = init_theta(feature_count)
# Obtain the final parameter theta and cost.
result_theta, Jthetas = gradient_descending(training_x, y, theta, alpha)
# Display the parameter.
print("w:{}".format(result_theta[0][0]), "b:{}".format(result_theta[1][0]))
showJTheta(Jthetas)
showlinercurve(result_theta, training_data_include_y)
