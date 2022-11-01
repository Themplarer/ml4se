from functools import reduce
from torch import nn

from task2.encoderlayer import EncoderLayer
from task2.norm import Norm
from task2.positionalencoder import PositionalEncoder
from task2.utils import generate_deep_copies


class Encoder(nn.Module):
    def __init__(self, d_model, layers_count, heads):
        super().__init__()
        self.pe = PositionalEncoder(d_model)
        self.layers = generate_deep_copies(EncoderLayer(d_model, heads),
                                           layers_count)
        self.norm = Norm(d_model)

    def forward(self, x):
        x = self.pe(x)
        x = reduce(lambda acc, layer: layer(acc), self.layers, x)
        return self.norm(x)
