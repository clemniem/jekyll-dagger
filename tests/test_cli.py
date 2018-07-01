"""Tests for our main skele CLI module."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase

from dagger import __version__ as VERSION


class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = popen(['dagger', '-h'], stdout=PIPE).communicate()[0].decode()
        self.assertTrue('Usage:' in output)

        output = popen(['dagger', '--help'], stdout=PIPE).communicate()[0].decode()
        self.assertTrue('Usage:' in output)


class TestVersion(TestCase):
    def test_returns_version_information(self):
        output = popen(['dagger', '--version'], stdout=PIPE).communicate()[0].decode()
        self.assertEqual(output.strip(), VERSION)
