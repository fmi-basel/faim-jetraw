import argparse
import configparser

from prefect import Flow, Parameter, task, unmapped
from prefect.executors import LocalDaskExecutor

from jetraw_tasks.functions import list_files, prepare_and_compress


def config2kwargs(config):
    return {
        "num_workers": int(config["DEFAULT"]["num_workers"]),
        "input_pattern": config["DEFAULT"]["input_pattern"],
        "dat_file": config["DEFAULT"]["dat_file"],
        "cam_id": config["DEFAULT"]["cam_id"],
        "output_dir": config["DEFAULT"]["output_dir"],
    }


@task()
def list_files_task(pattern):
    return list_files(pattern)


@task()
def prepare_and_compress_task(
    input_path: str, dat_path: str, cam_id: str, output_directory: str
):
    prepare_and_compress(
        input_path=input_path,
        dat_path=dat_path,
        cam_id=cam_id,
        output_directory=output_directory,
    )


with Flow("Compress") as flow:
    num_workers = Parameter("num_workers", 1)
    input_pattern = Parameter("input_pattern", "./*.tif")
    dat_file = Parameter("dat_file", "./data/cam_profile.dat")
    cam_id = Parameter("cam_id", "Camera1 2x2binning")
    output_dir = Parameter("output_dir", "./output")

    files = list_files_task(input_pattern)

    prepare_and_compress_task.map(
        files, unmapped(dat_file), unmapped(cam_id), unmapped(output_dir)
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config")
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.config)

    kwargs = config2kwargs(config)

    flow.executor = LocalDaskExecutor(num_workers=kwargs["num_workers"])

    kwargs.pop("num_workers")

    flow.run(parameters=kwargs)
