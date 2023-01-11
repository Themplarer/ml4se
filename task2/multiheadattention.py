import math

import torch
from torch import nn
from torch.nn.functional import softmax


def attention(q, k, v, d_model, mask):
    with torch.no_grad():
        scores = q @ (k.transpose(-2, -1) / math.sqrt(d_model))

        if mask is not None:
            scores = scores.masked_fill(mask == float('-inf'), float('-inf'))

        return softmax(scores, dim=-1) @ v


class MultiHeadAttention(nn.Module):
    def __init__(self, h, d_model):
        super().__init__()
        self.d_model = d_model
        self.h = h

        self.q_linear = nn.Linear(d_model, d_model)
        self.v_linear = nn.Linear(d_model, d_model)
        self.k_linear = nn.Linear(d_model, d_model)

    def forward(self, q, k, v, mask=None):
        q = self.q_linear(q)
        k = self.k_linear(k)
        v = self.v_linear(v)

        return attention(q, k, v, self.d_model, mask)
