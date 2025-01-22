import torch

# Check available GPUs
num_gpus = torch.cuda.device_count()
print(f"Number of GPUs available: {num_gpus}")

for i in range(num_gpus):
    print(f"GPU {i}: {torch.cuda.get_device_name(i)}")

# Set device (use cuda:0 or cuda:1 based on nvidia-smi results)
device = torch.device("cuda:1" if torch.cuda.is_available() and num_gpus > 1 else "cuda:0")
print(f"Using device: {device}")

# Test Tensor on GPU
try:
    x = torch.tensor([1.0, 2.0, 3.0]).to(device)
    print("Tensor successfully moved to:", device)
except RuntimeError as e:
    print(f"Error: {e}")
