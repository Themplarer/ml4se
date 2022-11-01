from torch import nn

from task2.feedforward import FeedForward
from task2.multiheadattention import MultiHeadAttention
from task2.norm import Norm


class DecoderLayer(nn.Module):
    def __init__(self, d_model, heads):
        super().__init__()
        self.norm_1 = Norm(d_model)
        self.norm_2 = Norm(d_model)
        self.norm_3 = Norm(d_model)

        self.attention_1 = MultiHeadAttention(heads, d_model)
        self.attention_2 = MultiHeadAttention(heads, d_model)
        self.feed_forward = FeedForward(d_model)

    def forward(self, x, encoder_output, mask):
        x = self.norm_1(x + self.attention_1(x, x, x, mask))
        x = self.norm_2(x + self.attention_2(x, encoder_output, encoder_output))
        x = self.norm_3(x + self.feed_forward(x))
        return x
