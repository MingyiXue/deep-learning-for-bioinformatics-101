import torch
import torch.nn as nn

class FCNNModel(nn.Module):
    def __init__(self, ndim, hidden_dims):
        super(FCNNModel, self).__init__()
        total_dims = [ndim] + hidden_dims + [1]
        net = []
        for i in range(len(total_dims)-1):
            net.append(nn.Linear(total_dims[i], total_dims[i+1]))
        self.net = nn.Sequential(*net)

    def forward(self, x):
        out = x
        for idx in range(len(self.net)-1):
            out = self.net[idx](out)
            out = nn.ReLU()(out)
        out = self.net[-1](out)
        return out


class FCNNBtachModel(nn.Module):
    def __init__(self, ndim, hidden_dims):
        super(FCNNBtachModel, self).__init__()
        total_dims = [ndim] + hidden_dims
        net = []
        self.bn = nn.BatchNorm1d(total_dims[0])
        for i in range(len(total_dims)-1):
            net.append(nn.Linear(total_dims[i], total_dims[i+1]))
            net.append(nn.BatchNorm1d(total_dims[i+1]))
        self.fc = nn.Linear(total_dims[-1], 1)
        self.net = nn.Sequential(*net)

    def forward(self, x):
        out = x
        out = self.bn(x)
        layers_in_block = 2
        for idx in range(len(self.net)//layers_in_block):
            out = self.net[layers_in_block*idx](out)
            out = self.net[layers_in_block*idx+1](out)
            out = nn.ReLU()(out)
        out = self.fc(out)
        return out