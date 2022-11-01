import torch
from torch import nn


class PositionalEncoder(nn.Module):
    def __init__(self, d_model, max_len=80):
        super().__init__()
        self.d_model = d_model

        a = torch.arange(0, max_len).reshape(-1, 1)
        b = torch.arange(0, d_model)

        self.pe = a / 10000 ** (2 * b / d_model)
        for i in range(0, d_model, 2):
            self.pe[:, i] = torch.sin(self.pe[:, i])
            self.pe[:, i + 1] = torch.cos(self.pe[:, i + 1])

    def forward(self, x):
        return x + self.pe[:x.size(0)]
