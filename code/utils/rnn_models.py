import torch
import torch.nn as nn

class SMILESModel(nn.Module):
    def __init__(self, mask=True, ratio=0.15):
        super(SMILESModel, self).__init__()
        self.mask = mask
        self.mask_ratio = ratio
        raise NotImplemented
    
    def forward(self, smi_batch, smi_mask=None):
        raise NotImplemented
