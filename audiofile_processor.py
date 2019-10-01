from os import listdir
import os.path as osp

class AudiofileProcessor(object):

	SECONDS = 60
	POMADORO_LENGTH_IN_SECONDS = 25 * SECONDS

	def __init__(self, directory, filter_by_ext, length_calculator):
		self.directory = directory
		self.filter_by_ext = filter_by_ext
		self.length_calculator = length_calculator

	def _get_files(self):
		files = []
		if osp.isdir(self.directory):
			for f in listdir(self.directory):
				if osp.isfile(osp.join(self.directory, f)) and self.filter_by_ext(f):
					files.append(osp.join(self.directory, f))
		return files

	def pomodoro(self):
		files = self._get_files()
		length = 0
		for f in files:
			length += self.length_calculator(f)
		l = round(length)
		print("Pomodoros listened: #{}. Time remained: {}:{}"
			.format(l // self.POMADORO_LENGTH_IN_SECONDS,
				(l % self.POMADORO_LENGTH_IN_SECONDS) // self.SECONDS,
				(l % self.POMADORO_LENGTH_IN_SECONDS) % self.SECONDS))
