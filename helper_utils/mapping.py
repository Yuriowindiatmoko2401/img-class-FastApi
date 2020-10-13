import random, sys, os, json


def main():
	
	workdir = os.getcwd()

	data_name = []
	file1 = open(workdir + '/' + str(sys.argv[1]), 'r')
	Lines = file1.readlines()

	for line in Lines:
		data_name.append(line.replace('\n',''))

	name_folder = str(sys.argv[2])

	mapped = {name_folder:data_name}

	with open(workdir + '/' + str(sys.argv[3]), 'w') as fp:
	    json.dump(mapped, fp)


if __name__ == '__main__':
	main()
