from torch import nn

from task2.feedforward import FeedForward
from task2.multiheadattention import MultiHeadAttention
from task2.norm import Norm


class EncoderLayer(nn.Module):
    def __init__(self, d_model, h):
        super().__init__()
        self.norm_1 = Norm(d_model)
        self.norm_2 = Norm(d_model)
        self.attention = MultiHeadAttention(h, d_model)
        self.feed_forward = FeedForward(d_model)

    def forward(self, x):
        x = self.norm_1(x + self.attention(x, x, x))
        x = self.norm_2(x + self.feed_forward(x))
        return x
