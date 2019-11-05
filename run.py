import click
import os
# import warnings
# warnings.filterwarnings("ignore")


@click.command()
@click.argument('mode')

def main(mode):
	if mode == 'train':
		import train_face_model
	elif mode == 'test':
		import main
	elif mode == 'record':
		import record_faces
	elif mode == 'reset':
		reset()

def reset():
	PATH = os.path.join(os.curdir, 'data')
	os.chdir(PATH)
	for file in os.listdir():
		os.remove(file)


if __name__ == '__main__':
	main()