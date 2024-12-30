import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights and biases
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Randomly initialize weights and biases
        self.W1 = np.random.randn(self.input_size, self.hidden_size)
        self.b1 = np.zeros((1, self.hidden_size))
        self.W2 = np.random.randn(self.hidden_size, self.output_size)
        self.b2 = np.zeros((1, self.output_size))
        
    def sigmoid(self, x):
        """Sigmoid activation function"""
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        """Derivative of the sigmoid function"""
        return x * (1 - x)

    def forward(self, X):
        """Forward pass"""
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.sigmoid(self.z2)
        return self.a2
    
    def backward(self, X, y, learning_rate=0.1):
        """Backward pass (Backpropagation)"""
        m = X.shape[0]
        
        # Calculate error for output layer
        error_output = self.a2 - y
        dZ2 = error_output * self.sigmoid_derivative(self.a2)
        
        # Calculate error for hidden layer
        error_hidden = dZ2.dot(self.W2.T)
        dZ1 = error_hidden * self.sigmoid_derivative(self.a1)
        
        # Update weights and biases using gradient descent
        self.W2 -= learning_rate * self.a1.T.dot(dZ2) / m
        self.b2 -= learning_rate * np.sum(dZ2, axis=0, keepdims=True) / m
        self.W1 -= learning_rate * X.T.dot(dZ1) / m
        self.b1 -= learning_rate * np.sum(dZ1, axis=0, keepdims=True) / m
        
    def train(self, X, y, epochs=1000, learning_rate=0.1):
        """Train the neural network"""
        for epoch in range(epochs):
            self.forward(X)  # Forward pass
            self.backward(X, y, learning_rate)  # Backward pass
            if epoch % 100 == 0:
                loss = np.mean((self.a2 - y) ** 2)
                print(f'Epoch {epoch}, Loss: {loss}')
    
    def predict(self, X):
        """Predict using the trained neural network"""
        return np.round(self.forward(X))  # Return binary prediction (0 or 1)

# Example usage
if __name__ == "__main__":
    # Simple dataset: XOR Problem
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Input
    y = np.array([[0], [1], [1], [0]])  # Output (XOR result)

    # Create the neural network with 2 input nodes, 2 hidden nodes, and 1 output node
    nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)

    # Train the network
    nn.train(X, y, epochs=1000, learning_rate=0.1)

    # Predict for the input data
    predictions = nn.predict(X)
    print(f"Predictions:\n{predictions}")
