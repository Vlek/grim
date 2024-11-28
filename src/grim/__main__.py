from dataconf import load

from grim import GrimConfig
from grim.client import GrimApp


def main():
    config: GrimConfig = load("./config.yaml", GrimConfig)

    app = GrimApp(config)

    app.run()
