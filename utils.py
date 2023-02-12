from pathlib import Path

import click

ReadableFile = click.Path(exists=True, dir_okay=False, readable=True, path_type=Path)
WriteableFile = click.Path(dir_okay=False, writable=True, path_type=Path)
