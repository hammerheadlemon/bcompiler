"""
Copyright (c) 2019 Matthew Lemon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy,  modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the  Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE. """
import logging
from functools import partial

import click
import colorlog
from engine.adapters import cli as engine_cli
from engine.config import Config as engine_config

logger = colorlog.getLogger("bcompiler")
logger.setLevel(logging.INFO)

# we want to pass echo func down to bcompiler-engine
output_funcs = dict(
    click_echo_green=partial(click.secho, nl=False, fg="green"),
    click_echo_yellow=partial(click.secho, nl=False, fg="yellow"),
    click_echo_red=partial(click.secho, nl=False, fg="red"),
    click_echo_white=partial(click.secho, nl=False, fg="white"),
)


class Config:
    def __init__(self):
        self.verbose = False


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option("--verbose", is_flag=True)
@pass_config
def cli(config, verbose):
    """
    bcompiler is a tool for moving data to and from spreadsheets. See web site, etc.
    """
    config.verbose = verbose


@cli.group("import")
def _import():
    """
    Import something (a batch of populated templates, a datamap, etc).
    """


@_import.command()
@click.option(
    "--to-master",
    "-m",
    is_flag=True,
    default=False,
    help="Create master.xlsx immediately",
)
def templates(to_master):
    engine_config.initialise()
    click.secho("Hello from bcompiler 2.0!", fg="yellow")
    if to_master:
        engine_cli.import_and_create_master(echo_funcs=output_funcs)
    else:
        click.secho("Not implemented yet. Try --to-master/-m flag")
