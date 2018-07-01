"""
dagger

Usage:
  dagger init
  dagger add
  dagger fly <path>
  dagger -h | --help
  dagger --version

Arguments:
  <path>   needs to be a directory containing .md-Files or a .md-File

Options:
  -h, --help        Show this screen.
  -v, --version     Show version.
  -p, --push        Automatically pushes latest changes.
  -f, --force       Forces a rewrite of all scribbles in file.

Examples:
  dagger scribble.md

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/clemniem/jekyll-dagger
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import dagger.commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items(): 
        if hasattr(dagger.commands, k) and v:
            module = getattr(dagger.commands, k)
            dagger.commands = getmembers(module, isclass)
            command = [command[1] for command in dagger.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
