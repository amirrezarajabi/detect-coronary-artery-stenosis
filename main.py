import argparse
from ultralytics import YOLO
import os
from tqdm import tqdm

FORMAT = ['bmp', 'dng', 'jpeg', 'jpg', 'mpo', 'png', 'tif', 'tiff', 'webp', 'pfm']

parser = argparse.ArgumentParser()
parser.add_argument(
    "--model", type=str, help="path to yolo model"
)

parser.add_argument(
    "--inp", type=str, help="path to input image/folder"
)

args = parser.parse_args()

if os.path.exists(args.model):
    model = YOLO(args.model)
else:
    raise FileNotFoundError(args.model)



if os.path.exists(args.inp):
    if os.path.isdir(args.inp):
        files = [os.path.join(args.inp, f) for f in os.listdir(args.inp) if os.path.splitext(f)[1][1:] in FORMAT]
    else:
        if os.path.splitext(args.inp)[1][1:] in FORMAT:
            files = [args.inp]
        else:
            raise NotImplementedError(f"This format {os.path.splitext(args.inp)[1]} is not supported. Supported formats are {FORMAT}")
else:
    raise FileNotFoundError(args.model)


for f in tqdm(files):
    model(f, save=True)