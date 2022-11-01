from torch import nn


class Norm(nn.Module):
    def __init__(self, eps=1e-6):
        super().__init__()
        self.eps = eps

    def forward(self, x):
        mu = x.mean(dim=-1, keepdim=True)
        sigma_squared = (x * (x - mu) ** 2).mean(dim=-1, keepdim=True)
        return (x - mu) / ((sigma_squared + self.eps) ** 0.5)
