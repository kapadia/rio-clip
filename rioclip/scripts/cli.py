

import click
import rasterio
from rasterio.rio.cli import cli

from rioclip import clip as rioclip
from rioclip import __version__ as rioclip_version


@cli.command(short_help="Clip a dataset to the bounds of another dataset.")
@click.argument('srcpath', type=click.Path(resolve_path=True), required=True, metavar='SRC')
@click.argument('tarpath', type=click.Path(resolve_path=True), required=True, metavar='TAR')
@click.argument('dstpath', type=click.Path(resolve_path=False), required=True, metavar='DST')
@click.version_option(version=rioclip_version, message='%(version)s')
@click.pass_context
def clip(ctx, srcpath, tarpath, dstpath):

    verbosity = (ctx.obj and ctx.obj.get('verbosity')) or 1
    rioclip(srcpath, tarpath, dstpath)