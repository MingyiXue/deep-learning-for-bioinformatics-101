import torch
import torch.nn as nn
from torch_geometric.nn.conv import RGATConv, RGCNConv, GCNConv, GATConv
from torch_geometric.nn.pool import global_mean_pool

# class CFilter(nn.Module):
#     def __init__(self, dims):
#         super(CFilter, self).__init__()
#         raise NotImplemented

# class SchNet(nn.Module):
#     def __init__(self, hidden_dims):
#         super(SchNet, self).__init__()
#         raise NotImplemented
    
#     def forward(self, graph_batch):
#         raise NotImplemented


class GCNModel(nn.Module):
    def __init__(self, ndim, hidden_dims, type):
        super(GCNModel, self).__init__()
        total_dims = [ndim] + hidden_dims
        net = []
        self.bn = nn.BatchNorm1d(total_dims[0])
        for i in range(len(total_dims)-1):
            net.extend([
                GCNConv(total_dims[i], total_dims[i+1], add_self_loops=True),
                nn.ELU(),
            ])
        self.net = nn.Sequential(*net)
        self.fc = nn.Linear(total_dims[-1], 1)
        self.type = type
        

    def forward(self, data):
        batch = data.batch
        out = data.x
        if self.type == "float":
            out = out.float()
        elif self.type == "double":
            out = out.double()
        else:
            raise TypeError(f"{self.type} not supported")
        out = self.bn(out)
        edge_index = data.edge_index.long()
        
        for idx in range(len(self.net)//2):
            out = self.net[2*idx](out, edge_index)
            out = self.net[2*idx+1](out)
        out = global_mean_pool(out, batch)
        out = self.fc(out)
        return out