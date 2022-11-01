import copy

import torch


def generate_deep_copies(param, copies):
    return [copy.deepcopy(param) for _ in range(copies)]


def generate_triangular_mask(size):
    mask = (torch.triu(torch.ones(size[::-1]))).transpose(0, 1)
    return mask\
        .masked_fill(mask == 0, float('-inf'))\
        .masked_fill(mask == 1, float(0.0))
