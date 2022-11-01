from torch import nn
from torch.nn.functional import relu


class FeedForward(nn.Module):
    def __init__(self, d_model, d_ff=2048):
        super().__init__()
        self.inner_linear = nn.Linear(d_model, d_ff)
        self.outer_linear = nn.Linear(d_ff, d_model)

    def forward(self, x):
        return self.outer_linear(relu(self.inner_linear(x)))
