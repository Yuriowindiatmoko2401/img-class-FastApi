import os, sys, re, natsort

ls = [this for this in os.listdir(os.getcwd() + '/' + str(sys.argv[1]))]

# ls = ls.sort(key=lambda f: int(re.sub('\D', '', f)))
ls = natsort.natsorted(ls,reverse=False)

with open(os.getcwd() + '/' + str(sys.argv[2]), 'w') as f:
    for item in ls:
        f.write("%s\n" % item)

