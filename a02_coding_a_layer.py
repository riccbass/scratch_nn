inputs = [1, 2, 3, 2.5]

weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.25, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5


[]

output = sum([i * w for i, w in zip(inputs, weights)]) + bias

output = [sum([i * w for i, w in zip(inputs, weights1)]) + bias1]
output += [sum([i * w for i, w in zip(inputs, weights2)]) + bias2]
output += [sum([i * w for i, w in zip(inputs, weights3)]) + bias3]


