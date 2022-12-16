import numpy as np
import torch
import torch.nn.functional as F

def perspective_grid(theta, size, aligh_corners = None):
    n, c, h, w = size

    dx = torch.linspace(-1, 1, w)
    dy = torch.linspace(-1, 1, h)
    x, y = torch.meshgrid(dx,dy)
    coords = torch.stack((y,x), dim=-1)  # [dy*dx*2]
    homo_pos = torch.ones(h, w, 1)
    homo_coords = torch.cat((coords, homo_pos), dim=2)
    homo_coords = homo_coords.unsqueeze(0).expand(n, *homo_coords.shape)
    homo_coords = homo_coords.view(n, h*w, 3).cuda()

    new_homo_coords = homo_coords.bmm(theta.transpose(1,2))
    new_coords = new_homo_coords[:,:,:2] / new_homo_coords[:,:,2].unsqueeze(-1)
    new_coords = new_coords.view(n,h,w,2)

    return new_coords

if __name__ == '__main__':
    row = np.array(range(5))
    img = torch.as_tensor(np.array([row + i for i in range(5)]))
    img = torch.reshape(img, (1, 1, *img.shape))
    print(img)

    patch = torch.ones(2, 2)
    patch = F.pad(patch, (0, 3, 0, 3))
    patch = torch.reshape(patch, img.shape).cuda()
    print(patch)

    #offsets = torch.zeros(2, 1)
    offsets = torch.tensor([[-0.5],[-0.5]])
    offsets.requires_grad = True
    print('offsets', offsets)

    perspective_coefficient = torch.zeros(1, 2)
    perspective_coefficient.requires_grad = True
    last_row = torch.hstack((perspective_coefficient, torch.eye(1)))
    print(perspective_coefficient)

    theta = torch.hstack([torch.eye(2), offsets])
    theta = torch.vstack((theta, last_row))
    theta = torch.reshape(theta, (1, *theta.shape)).cuda()
    print(theta)

    grid = perspective_grid(theta, img.shape)
    out = torch.nn.functional.grid_sample(patch, grid, align_corners=True)
    print(out)