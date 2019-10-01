from audiofile_processor import AudiofileProcessor
import argparse
from mutagen.mp3 import MP3


def main(directory, audiofile_ext):
	if "mp3" == audiofile_ext:
		processor = AudiofileProcessor(directory, lambda f: f.endswith(".mp3"), lambda f: MP3(f).info.length)
		processor.pomodoro()
	else:
		raise NotImplementedError("Audio file format: {} is not supported".format(audiofile_ext))


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", help="directory with audio files", required=True)
	parser.add_argument("-ext", help="extension of audio files", required=True)
	args = parser.parse_args()
	main(args.d, args.ext)
