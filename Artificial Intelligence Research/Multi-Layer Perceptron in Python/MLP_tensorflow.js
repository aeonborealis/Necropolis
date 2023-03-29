// Define the MLP class
class MLP {
  constructor(inputSize, hiddenSize, outputSize) {
    this.inputSize = inputSize;
    this.hiddenSize = hiddenSize;
    this.outputSize = outputSize;

    // Initialize weights and biases randomly
    this.weights1 = tf.randomNormal([inputSize, hiddenSize]);
    this.bias1 = tf.randomNormal([hiddenSize]);
    this.weights2 = tf.randomNormal([hiddenSize, outputSize]);
    this.bias2 = tf.randomNormal([outputSize]);
  }

  // Define the forward pass method
  predict(x) {
    // Convert input to tensor
    const input = tf.tensor2d(x, [1, this.inputSize]);

    // Compute first layer activations
    const hidden = input.matMul(this.weights1).add(this.bias1).sigmoid();

    // Compute output layer activations
    const output = hidden.matMul(this.weights2).add(this.bias2).sigmoid();

    // Convert output to array and return
    return output.dataSync();
  }
}

// Test the MLP
const mlp = new MLP(2, 3, 1);
console.log(mlp.predict([0, 1])); // Example output: [0.7818524832725525]
