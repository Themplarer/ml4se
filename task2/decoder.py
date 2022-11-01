from functools import reduce

from torch import nn

from task2.decoderlayer import DecoderLayer
from task2.norm import Norm
from task2.positionalencoder import PositionalEncoder
from task2.utils import generate_deep_copies, generate_triangular_mask


class Decoder(nn.Module):
    def __init__(self, d_model, layers_count, heads):
        super().__init__()
        self.pe = PositionalEncoder(d_model)
        self.layers = generate_deep_copies(DecoderLayer(d_model, heads),
                                           layers_count)
        self.norm = Norm(d_model)
        self.mask = generate_triangular_mask((1, 1))

    def forward(self, x, encoder_outputs):
        x = self.pe(x)
        x = reduce(lambda acc, layer: layer(acc, encoder_outputs, self.mask),
                   self.layers, x)
        return self.norm(x)
