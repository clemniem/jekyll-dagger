"""Tests for our `jagger target` subcommand."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase

class TestTarget(TestCase):
    def test_invalid_input_file(self):
        output = popen(['jagger', 'target', 'noMdFile.txt'], stdout=PIPE).communicate()[0].decode()
        self.assertTrue('Invalid path: Please target to a valid .md-file or directory containing .md-files' in output)


