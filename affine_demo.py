import numpy as np
import torch
import torch.nn.functional as F


row = np.array(range(5))
img = torch.as_tensor(np.array([row+i for i in range(5)]))
img = torch.reshape(img, (1, 1, *img.shape))
print(img)

mask = torch.ones(2, 2)
mask = F.pad(mask, (0, 3, 0, 3))
mask = torch.reshape(mask, img.shape)
print(mask)

offsets = torch.zeros(2, 1)
offsets.requires_grad = True

print("Optimizing:")
while True:
    theta = torch.hstack([torch.eye(2), offsets])
    theta = torch.reshape(theta, (1, *theta.shape))
    print(theta)

    grid = F.affine_grid(theta, img.shape)
    out_mask = F.grid_sample(mask, grid)
    print(out_mask)

    loss = torch.sum(out_mask * img)
    print("Current loss:", loss.item())

    if abs(loss.item()-(6+7+7+8)) < 0.1:
        break

    loss.backward(retain_graph=True)
    offsets = (offsets + 0.01 * offsets.grad).detach()
    offsets.requires_grad = True

