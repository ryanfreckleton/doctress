"""doctress - A RestructuredText based literate programming and documentation tool."""

__version__ = '0.1.0'
__author__ = 'Ryan Freckleton <ryan.freckleton@gmail.com>'
__all__ = []

import sys

import click

import docutils
from docutils.parsers.rst import directives
from docutils.writers.html4css1 import Writer

import pycon
import html5

@click.command()
@click.argument('input', type=click.File('rb'))
@click.argument('outfile', type=click.File('wb'), default=sys.stdout)
def cli(input, outfile):
    directives.register_directive('pycon', pycon.PyconDirective)
    writer = html5.Writer()
    output = docutils.core.publish_string(input.read(), writer=writer)
    outfile.write(output)
