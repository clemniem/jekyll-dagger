"""Tests for our `skele hello` subcommand."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase


# class TestHello(TestCase):
#     def test_returns_multiple_lines(self):
#         output = popen(['jagger', 'hello'], stdout=PIPE).communicate()[0].decode()
#         lines = output.split('\n')
#         self.assertTrue(len(lines) != 1)
#
#     def test_returns_hello_world(self):
#         output = popen(['jagger', 'hello'], stdout=PIPE).communicate()[0].decode()
#         self.assertTrue('Hell, world!' in output)
