"""Tests for our `skele hello` subcommand."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase


class TestFly(TestCase):
	def test_invalid_input_file(self):
		output = popen(['dagger', 'fly', 'noMdFile.txt'], stdout=PIPE).communicate()[0].decode()
		self.assertTrue('No scribbles' in output)

	def test_baddir(self):
		badpath = '../files/baddir/'
		output = popen(['dagger', 'fly', badpath], stdout=PIPE).communicate()[0].decode()
		self.assertTrue('No scribbles' in output)