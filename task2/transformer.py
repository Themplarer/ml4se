from torch import nn
from torch.nn.functional import softmax

from task2.decoder import Decoder
from task2.encoder import Encoder


class Transformer(nn.Module):
    def __init__(self, d_model, layers_count, heads, vocab_size):
        super().__init__()
        self.encoder = Encoder(d_model, layers_count, heads)
        self.decoder = Decoder(d_model, layers_count, heads)

        self.out = nn.Linear(d_model, vocab_size)

    def forward(self, src, trg):
        encoder_output = self.encoder(src)
        decoder_output = self.decoder(trg, encoder_output)
        return softmax(self.out(decoder_output), dim=-1)
