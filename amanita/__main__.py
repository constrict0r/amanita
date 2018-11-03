# -*- coding: utf-8 -*-

"""Main amanita CLI."""

import os
import sys

import click

from amanita import __version__


def version_msg():
    """Return the amanita version, location and Python powering it."""
    python_version = sys.version[:3]
    location = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    message = u'amanita %(version)s from {} (Python {})'
    return message.format(location, python_version)


@click.command(context_settings=dict(help_option_names=[u'-h', u'--help']))
@click.version_option(__version__, u'-V', u'--version', message=version_msg())
def main():
    """amanita cli main rutine"""
    # if args is None:
    #     if len(sys.argv) > 1:
    #         args = sys.argv[1]

    print("This is the main routine.")


if __name__ == "__main__":
    sys.exit(main())
