import glob, os

align_dir = os.path.join('.','s1_align')
align_files = glob.glob(os.path.join(align_dir, '*.align'))
fw = open("transin","w") 
for align in align_files:
	
	all = open(align).read().split('\n')[1:-2]
	line =str('')
	for single in all:
		line+=single.split(' ')[-1]
		line+=' '
	each = os.path.basename(align)[:-6]+'.wav|'+line
	fw.write(each)
	fw.write('\n')