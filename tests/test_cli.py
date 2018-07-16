"""Tests for our main jagger CLI module."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase

from jagger import __version__ as VERSION


class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = popen(['jagger', '-h'], stdout=PIPE).communicate()[0].decode()
        self.assertTrue('Usage:' in output)

        output = popen(['jagger', '--help'], stdout=PIPE).communicate()[0].decode()
        self.assertTrue('Usage:' in output)


class TestVersion(TestCase):
    def test_returns_version_information(self):
        output = popen(['jagger', '--version'], stdout=PIPE).communicate()[0].decode()
        self.assertEqual(output.strip(), VERSION)
