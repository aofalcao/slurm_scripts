import torch
print("Is CUDA available?----->", torch.cuda.is_available())
print()
x = torch.rand(5, 3)
print(x)
