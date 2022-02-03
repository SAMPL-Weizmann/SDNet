import torch

class AverageMeter(object):
    # Computes and stores the average and current value
    def __init__(self, device):
        self.reset(device)

    def reset(self, device):
        self.val = torch.tensor(0.0).to(device)
        self.avg = torch.tensor(0.0).to(device)
        self.sum = torch.tensor(0.0).to(device)
        self.count = torch.tensor(0.0).to(device)

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count