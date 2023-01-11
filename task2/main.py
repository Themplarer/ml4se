from torch import argmax, tensor

from task2.transformer import Transformer


def main():
    t = Transformer(10, 6, 1, 100)
    input_seq = tensor([[1., 2, 3, 1, 1, 1, 1, 1, 1, 1],
                        [1., 20, 3, 1, 3, 1, 1, 1, 18, 1]])
    probabilities_vector = t(input_seq, input_seq)
    print(probabilities_vector)
    print(argmax(probabilities_vector, dim=-1))


if __name__ == '__main__':
    main()
