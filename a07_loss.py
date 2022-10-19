from math import log


softmax_output = [0.7, 0.1, 0.2]
target_ouput = [1, 0, 0]

loss = -log(softmax_output[0]) * target_ouput[0]