from numpy import exp, array, random, dot
training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
training_set_outputs = array([[0, 1, 1, 0]]).T
random.seed(1)
# random start weights [-1, 1]
synaptic_weights = 2 * random.random((3, 1)) - 1
# train 
for iteration in xrange(10000): 
    # 1 / (1 + exp(0-(inp1*wgh1 + inp2*wgh2 + inp3*wgh3))) - synaptic
    output = 1 / (1 + exp(0-(dot(training_set_inputs, synaptic_weights))))
    # Error weigh formula: error * input * output * (1 - output)
    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
#think
print 1 / (1 + exp(0-(dot(array([1, 0, 0]), synaptic_weights))))
