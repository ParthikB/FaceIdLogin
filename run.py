import click
import os
# import warnings
# warnings.filterwarnings("ignore")

# Defining a function to Erase the database.
def reset():
	PATH = os.path.join(os.curdir, 'data')
	os.chdir(PATH)
	for file in os.listdir():
		os.remove(file)


@click.command()
@click.argument('mode')

def main(mode):

	# Records a New Profile
	if   mode == 'record':
		import __record_faces__
	
	# Trains the Machine Learning Algo.
	elif mode == 'train':
		import __train_face_model__
	
	# Tests the Output
	elif mode == 'test':
		import __test__
	
	# Erases the Database
	elif mode == 'reset':
		import __reset__


if __name__ == '__main__':
	main()