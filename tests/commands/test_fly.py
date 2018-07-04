"""Tests for our `jagger fly` subcommand."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase


class TestFly(TestCase):
	def test_invalid_input_file(self):
		output = popen(['jagger', 'fly', 'noMdFile.txt'], stdout=PIPE).communicate()[0].decode()
		self.assertTrue('No scribbles' in output)

	def test_baddir(self):
		badpath = '../files/baddir/'
		output = popen(['jagger', 'fly', badpath], stdout=PIPE).communicate()[0].decode()
		self.assertTrue('No scribbles' in output)