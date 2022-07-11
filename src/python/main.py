import numpy as np
import torch
import csv



import torch as tor
import torch.nn as nn
import torch.nn.functional as F
class model(nn.Module):
    def __init__(self):
      super(model, self).__init__()
      self.fc1 = nn.Linear(2, 1)

test = torch.randn(1, 2)

print(test)

nnmodel = model()

output = nnmodel.fc1(test)

print(output)




# file = open("blocks.json")

# jsondata = json.loads(file.read())

# i = 0
# print("gas_used, gas_price")
# for block in jsondata["blocks"]:
#   for transaction in block["transactions"]:
#     i += 1
#     # print(transaction)
#     print(transaction["gas_used"], transaction["gas_price"], sep=",")




np_data = np.loadtxt("gas_data.csv", dtype=np.float32, delimiter=",", skiprows=1)
print(np_data)
pytorch_data = torch.from_numpy(np_data)
print(pytorch_data)




mev_dataset = []

for line in pytorch_data:
  mev_dataset.append((line, 1))


weights = torch.randn(1, 2)
print(weights)


def test(weights, data_test):
    test_size = len(data_test.dataset)
    correct = 0

    for (data, target) in data_test:
        # print(batch_idx, data.shape, target.shape)
        data = data.view((1, 2))
        # print(batch_idx, data.shape, target.shape)

        activations = torch.matmul(data, weights)
        softmax = F.softmax(activations, dim=1)
        prediction = softmax.argmax(dim=1, keepdim=True)
        correct_predictions = prediction.eq(target.view_as(prediction)).sum().item()
        correct += correct_predictions
    accuracy = correct / test_size
    print(f"accuracy: on test: {accuracy*100}%")


it = 0
for img_number, (data, target) in enumerate(mev_dataset):

    if weights.grad is not None:
        weights.grad.zero_()
    data = data.view(1, 2)

    print("data = ", data)
    print("weights = ", weights.view(2, 1))
    activations = torch.matmul(data, weights.view(2, 1))
    print('activations =', activations)
    log_softmax = F.log_softmax(activations, dim=1)
    print("log_softmax =", log_softmax[0])
    print('size = ', log_softmax.size())
    print('size = ', log_softmax.size())
    print('target = ', torch.tensor([target]))

    loss = F.nll_loss(log_softmax[0], torch.tensor([target]))
    print("\r",loss.item(), end=' ')

    loss.backward()

    with torch.no_grad():
        weights -= 0.1*weights.grad
    it += 1

    # if not it % 100:
    #     test(weights, test_dataset)

    if it > 5000:
        break
