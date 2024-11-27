import torch
import time

#this is a sample file for using more than one GPU

# Check if GPUs are available
if not torch.cuda.is_available():
    raise RuntimeError("CUDA-capable GPU not available. Make sure the GPUs are accessible.")

# Print available devices
print(f"Available GPUs: {torch.cuda.device_count()}")
for i in range(torch.cuda.device_count()):
    print(f"Device {i}: {torch.cuda.get_device_name(i)}")

# Define a custom module for matrix multiplication
class MatrixMultiply(torch.nn.Module):
    def forward(self, A, B):
        return torch.matmul(A, B)

# Set up DataParallel for multiple GPUs
device = torch.device("cuda")
model = torch.nn.DataParallel(MatrixMultiply()).to(device)

# Create consistent matrices for all GPUs
matrix_size_A = (8192, 4096)  
matrix_size_B = (4096, 8192)  
A = torch.randn(matrix_size_A, device=device)
B = torch.randn(matrix_size_B, device=device)

# Perform matrix multiplication
num_iterations = 10000  
start_time = time.time()
#This will take some time and will use the available GPUs
for i in range(num_iterations):
    A_broadcast = A.unsqueeze(0).expand(torch.cuda.device_count(), *A.size())
    B_broadcast = B.unsqueeze(0).expand(torch.cuda.device_count(), *B.size())
    C = model(A_broadcast, B_broadcast)
    if i % 10 == 0:
        print(f"Iteration {i} complete")

end_time = time.time()
print(f"Completed {num_iterations} matrix multiplications of size {matrix_size_A} * {matrix_size_B} in {end_time - start_time:.2f} seconds.")
