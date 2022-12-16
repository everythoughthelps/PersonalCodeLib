import os
import time
import csv
import numpy as np
import torch
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim
from PIL import Image
from torchvision.transforms import ToPILImage, ToTensor
cudnn.benchmark = True

import models
from metrics import AverageMeter, Result
import utils

args = utils.parse_command()
print(args)
os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu # Set the GPU.


def main():
    global args, best_result, output_directory, train_csv, test_csv

    # Data loading code
    print("=> creating data loaders...")
    valdir = os.path.join('..','..', 'data', args.data, 'val')

    if args.data == 'nyudepthv2':
        from dataloaders.nyu_dataset import NYUDataset
        val_dataset = NYUDataset(valdir, split='val', modality=args.modality)
    elif args.data == 'nyu_real':
        from dataloaders.patch_dataset import PatchDataset
        val_dataset = PatchDataset(args.root)

    else:
        raise RuntimeError('Dataset not found.')

    # set batch size to be 1 for validation
    val_loader = torch.utils.data.DataLoader(val_dataset,
        batch_size=1, shuffle=False, num_workers=args.workers, pin_memory=True)
    print("=> data loaders created.")

    # evaluation mode
    if args.evaluate:
        assert os.path.isfile(args.evaluate), \
        "=> no model found at '{}'".format(args.evaluate)
        print("=> loading model '{}'".format(args.evaluate))
        checkpoint = torch.load(args.evaluate)
        if type(checkpoint) is dict:
            args.start_epoch = checkpoint['epoch']
            best_result = checkpoint['best_result']
            model = checkpoint['model']
            print("=> loaded best model (epoch {})".format(checkpoint['epoch']))
        else:
            model = checkpoint
            args.start_epoch = 0
        output_directory = os.path.dirname(args.evaluate)
        validate(val_loader, model, args.start_epoch, write_to_file=False)
        return


def validate(val_loader, model, epoch, write_to_file=True):
    average_meter = AverageMeter()
    model.eval() # switch to evaluate mode
    end = time.time()
    for i, sample in enumerate(val_loader):
        input = sample
        input, name = sample['image'], sample['image_name'][0]
        input = input.float().cuda()
        # torch.cuda.synchronize()
        data_time = time.time() - end

        # compute output
        end = time.time()
        with torch.no_grad():
            pred = model(input)
        # torch.cuda.synchronize()
        pred = pred.squeeze().float().cpu()
        pred_np = np.uint8(np.array(pred)*25.5)
        pred_depth = Image.fromarray(pred_np)
        #pred_depth = ToPILImage()(pred)
        pred_depth.save(name)
        gpu_time = time.time() - end


        # measure accuracy and record loss
        end = time.time()

        # save 8 images for visualization



if __name__ == '__main__':
    main()
