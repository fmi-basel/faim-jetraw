import argparse
import configparser

from prefect import Flow


def config2kwargs(config):
    return {"num_workers": config["DEFAULT"]["num_workers"]}


with Flow("Compress") as flow:
    pass

from prefect.executors import LocalDaskExecutor

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
