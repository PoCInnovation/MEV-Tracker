import numpy as np
import torch

import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as F


class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(4, 1)
        self.data = []
        self.model = torch.nn.Sequential(
            torch.nn.Linear(4, 1),
            torch.nn.Flatten(0, 1),
            torch.nn.Sigmoid()
        )

    def forward(self, X):
        y_pred = self.model(X)
        return y_pred


test = torch.randn(1, 4)

print(test)

nnmodel = Model()
optimizer = optim.Adam(nnmodel.parameters(), lr=0.01)


def load_model():
    nnmodel.load_state_dict(torch.load("model.pth"))


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


np_data = np.loadtxt("new_dataset.csv", dtype=np.float32, delimiter=",", skiprows=1)
np_data_test = np.loadtxt("new_data_not_labelised.csv", dtype=np.float32, delimiter=",", skiprows=1)
pytorch_data = torch.from_numpy(np_data)
pytorch_data_test = torch.from_numpy(np_data_test)

mev_dataset = []
for line in pytorch_data:
    mev_dataset.append(line)

mev_dataset_test = []
for line in pytorch_data_test:
    mev_dataset_test.append(line)

def test(data_test):
    test_size = len(data_test)
    correct = 0

    for data in data_test:
        data = data.view((-1, 4))
        prediction = nnmodel.forward(data)
        # print(prediction, data[0][2])
        correct_predictions = prediction.eq(target.view_as(prediction)).sum().item()
        # print()
        correct += correct_predictions
    accuracy = correct / test_size
    print(f"accuracy: on test: {accuracy * 100}%")


it = 0
loss = nn.BCEWithLogitsLoss()
for data in mev_dataset:

    data = data.view((-1, 4))
    target = torch.tensor([data[0][3]])
    data = nnmodel.forward(data)
    output = loss(data, target)
    output.backward()
    optimizer.step()
    optimizer.zero_grad()

    it += 1

    if not it % 100:
        test(mev_dataset)

    # if it > 5000:
        # break

    torch.save(nnmodel.state_dict(), "model.pth")

#   ajouter données [X]
#   ajouter programme avec goeth pour recuperer les blocs de flashbot [X]

#   ajouter layers []