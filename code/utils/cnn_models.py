import torch
import torch.nn as nn

class ResNetBlock(nn.Module):
    def __init__(self, in_channel, hidden_channel, 
                 kernel_size, activation, batchnorm, residual):
        super(ResNetBlock, self).__init__()
        if batchnorm:
            self.conv = nn.Sequential(
                nn.Conv2d(in_channel, hidden_channel, 
                    kernel_size=kernel_size, padding="same"),
                nn.BatchNorm2d(hidden_channel)
            )
        else:
            self.conv = nn.Conv2d(in_channel, hidden_channel, 
                            kernel_size=kernel_size, padding="same")

        self.act1 = getattr(nn.modules.activation, activation)()

        if batchnorm:
            self.bottleneck = nn.Sequential(
                nn.Conv2d(hidden_channel, hidden_channel,\
                    kernel_size=kernel_size, padding="same"),
                nn.BatchNorm2d(hidden_channel)
            )
        else:
            self.bottleneck = nn.Conv2d(hidden_channel, hidden_channel, 
                                kernel_size=kernel_size, padding="same")

        self.downsample = None
        self.residual = residual
        if self.residual and (in_channel!=hidden_channel):
            if batchnorm:
                self.downsample = nn.Sequential(
                    nn.Conv2d(in_channel, hidden_channel, \
                        kernel_size=1, padding="same"),
                    nn.BatchNorm2d(hidden_channel)
                )
            else:
                self.downsample = nn.Conv2d(in_channel, hidden_channel, \
                                        kernel_size=1, padding="same")
    
    def forward(self, x):
        out = self.conv(x)
        out = self.act1(out)
        out = self.bottleneck(out)
        if self.residual:
            if self.downsample:
                out += self.downsample(x)
            else:
                out += x
        return out


class CNNModel(nn.Module):
    def __init__(self, in_channel, hidden_channels, kernel_size=(3, 3),\
        dropout=0.3, activation="ReLU", batchnorm=True, residual=True):
        super(CNNModel, self).__init__()
        total_channels = [in_channel] + hidden_channels
        self.bn = nn.BatchNorm2d(in_channel)
        self.cnn = nn.Sequential()
        for i in range(len(total_channels)-1):
            self.cnn.append(
                ResNetBlock(total_channels[i], total_channels[i+1], 
                    kernel_size=kernel_size, activation=activation,
                    batchnorm=batchnorm, residual=residual
                )
            )
            self.cnn.append(getattr(nn.modules.activation, activation)())

        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(total_channels[-1], 1)
        
    
    def forward(self, x):
        out = self.bn(x)
        out = self.cnn(out)
        b, c, h, w = out.shape
        out = nn.AvgPool2d((h, w))(out)
        out = out.view(out.size(0), -1)
        out = self.dropout(out)
        out = self.fc(out)
        return out