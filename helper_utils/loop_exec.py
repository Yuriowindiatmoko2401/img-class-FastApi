import os

def main():
	workdir = os.getcwd()

	data_folder = open(workdir + '/' + "list_sku.txt", 'r')
	Lines = data_folder.readlines()

	ls_sku = []

	for line in Lines:
		ls_sku.append(line.replace('\n',''))

	for sku in ls_sku:

		# os.system("python read_file.py '{sku}' '{sku}.txt'".format(sku=sku))
		
		# os.system("python mapping.py '{sku}.txt' '{sku}' '{sku}.json'".format(sku=sku))

		os.system("cp '{sku}'/* data/".format(sku=sku))

if __name__ == '__main__':
	main()
