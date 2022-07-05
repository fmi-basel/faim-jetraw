import os
from glob import glob

import dpcore
import jetraw
import tifffile


def list_files(pattern):
    return glob(pattern)


def prepare_and_compress(
    input_path: str, dat_path: str, cam_id: str, output_directory: str
):
    image = tifffile.imread(input_path)
    dpcore.load_parameters(dat_path)
    if len(image.shape) == 2:
        dpcore.prepare_image(image, cam_id)
    elif len(image.shape) == 3:
        for page in range(image.shape[0]):
            dpcore.prepare_image(image[page], cam_id)
    else:
        raise NotImplementedError("More than 3 dimensions not supported")
    jetraw.imwrite(os.path.join(output_directory, os.path.basename(input_path)), image)
