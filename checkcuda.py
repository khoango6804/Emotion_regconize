
import torch

def check_cuda():
    if torch.cuda.is_available():
        print("CUDA is available.")
        print(f"Device name: {torch.cuda.get_device_name(0)}")
        print(f"CUDA capability: {torch.cuda.get_device_capability(0)}")
    else:
        print("CUDA is not available.")

check_cuda()
