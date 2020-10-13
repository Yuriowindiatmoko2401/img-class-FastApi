import os, sys, re, natsort


def main():
	
	ls = [this for this in os.listdir(os.getcwd() + '/' + str(sys.argv[1]))]

	ls = natsort.natsorted(ls,reverse=False)

	with open(os.getcwd() + '/' + str(sys.argv[2]), 'w') as f:
	    for item in ls:
	        f.write("%s\n" % item)


if __name__ == '__main__':
	main()