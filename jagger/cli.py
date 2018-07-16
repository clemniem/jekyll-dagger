"""
jagger

Usage:
  jagger init
  jagger status
  jagger add <path>
  jagger fly <md-resource>
  jagger -h | --help
  jagger --version

Arguments:
  <path>   needs to be a directory containing .md-Files or a .md-File

Options:
  -h, --help        Show this screen.
  -v, --version     Show version.
  -p, --push        Automatically pushes latest changes.
  -f, --force       Forces a rewrite of all scribbles in file.

Examples:
  jagger scribble.md

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/clemniem/jagger
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import jagger.commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items(): 
        if hasattr(jagger.commands, k) and v:
            module = getattr(jagger.commands, k)
            jagger.commands = getmembers(module, isclass)
            command = [command[1] for command in jagger.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
