import os
import glob


def deleteFile(filename):

    if os.path.exists(filename) and not os.path.isdir(filename) and not os.path.islink(filename):

        os.remove(filename)
      

def main():

	workdir = os.getcwd()

	ls_labels = os.listdir(workdir + '/raw_data/all_labels')
	
	ls_labels.remove('.gitkeep')

	ls_labels.remove('.DS_Store')

	# renaming files inside label_folders
	for label in ls_labels:

		os.system("python helper_utils/randomfilerenamer.py 'raw_data/all_labels/{label}'".format(label=label))

	# read all files inside label_folders n write to .txt
	for label in ls_labels:

		os.system("python helper_utils/read_file.py 'raw_data/all_labels/{label}' 'raw_data/txt_file/{label}.txt'".format(label=label))

	# mapping all files from .txt file to labels:[files] json
	for label in ls_labels:		

		os.system("python helper_utils/mapping.py 'raw_data/txt_file/{label}.txt' '{label}' 'raw_data/json_file/{label}.json'".format(label=label))

	# merge all img files into one data folders
	for label in ls_labels:
		
		os.system("cp '{workdir}/raw_data/all_labels/{label}/'* data/".format(workdir=workdir,label=label))

	# create labels file csv
	os.system("python helper_utils/merge_to_csv.py")


if __name__ == '__main__':
	main()













