import numpy as np
import torch
import csv


import torch.optim as optim
import torch as tor
import torch.nn as nn
import torch.nn.functional as F


class model(nn.Module):
    def __init__(self, X):
        super(model, self).__init__()
        self.fc1 = nn.Linear(3, 1)
        self.data = []
        self.model = torch.nn.Sequential(
            torch.nn.Linear(3, 1),
            torch.nn.Flatten(0, 1)
        )
        self.Y = torch.sin(X)


    def forward(self, X):
        y_pred = self.model(X)
        return y_pred


test = torch.randn(1, 3)

print(test)

nnmodel = model(torch.linspace(0, 2038602856570, steps=2))
optimizer = optim.Adam(nnmodel.parameters(), lr=0.01)

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




np_data = np.loadtxt("new_gas_data.csv", dtype=np.float32, delimiter=",", skiprows=1)
print(np_data)
pytorch_data = torch.from_numpy(np_data)
print(pytorch_data)

mev_dataset = []

for line in pytorch_data:
    mev_dataset.append(line)


weights = torch.randn(3, 1, requires_grad=True)
print(weights)


def test(weights, data_test):
    test_size = len(data_test.dataset)
    correct = 0

    for (data, target) in data_test:
        # print(batch_idx, data.shape, target.shape)
        data = data.view((1, 3))
        # print(batch_idx, data.shape, target.shape)

        activations = torch.matmul(data, weights)
        softmax = F.softmax(activations, dim=1)
        prediction = softmax.argmax(dim=1, keepdim=True)
        correct_predictions = prediction.eq(target.view_as(prediction)).sum().item()
        correct += correct_predictions
    accuracy = correct / test_size
    print(f"accuracy: on test: {accuracy*100}%")


it = 0
loss = nn.CrossEntropyLoss()
for data in mev_dataset:

    if weights.grad is not None:
        weights.grad.zero_()
        optimizer.zero_grad()

    data = data.view((-1, 3))
    target = data[0][2]
    data = nnmodel.forward(data)



    # target = torch.empty(1, dtype=torch.long).random_(5)
    print("target = ", target)
    # data = data[:-1]
    print("data = ", data)
    output = loss(data, torch.tensor(0.2).long())
    output.backward()
    optimizer.step()

    it += 1

    # if not it % 100:
    #     test(weights, test_dataset)

    if it > 5000:
        break
