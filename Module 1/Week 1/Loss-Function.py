import math
import random

def cal_loss_function():
    num_samples = input("Input number of samples (integer number) which are generated: ")
    if num_samples.isnumeric():
        num_samples = int(num_samples)
    else:
        print("number of samples must be an integer number.")
        return
    
    loss_function = input("Input loss name: ")
    predict = [random.uniform(0, 10) for i in range(num_samples)]
    target = [random.uniform(0, 10) for i in range(num_samples)]

    for i in range(num_samples):
        if loss_function == "MAE":
            loss = abs(target[i] - predict[i]) / num_samples
        elif loss_function == "MSE":
            loss = math.pow((target[i] - predict[i]), 2) / num_samples
        elif loss_function == "RMSE":
            loss = math.sqrt(math.pow((target[i] - predict[i]), 2) / num_samples)

        print(f"loss_name: {loss_function}, sample: {i}, target: {target[i]}, predict: {predict[i]}, loss: {loss}")

cal_loss_function()