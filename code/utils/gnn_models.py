import torch
import torch.nn as nn
from torch_geometric.nn.pool import global_mean_pool

class SchNet(nn.Module):
    def __init__(self, hidden_dims):
        super(SchNet, self).__init__()
        raise NotImplemented
    
    def forward(self, graph_batch):
        raise NotImplemented
