"""The target command."""


from json import dumps

from .base import Base
import os

class Target(Base):
	"""Write target to .config file"""

	def run(self):

		target = self.options['<path>']

		# parse input







		# check for folder


		print('You want to aim the jagger at:', self.options["<path>"])
		print('bluubb')
