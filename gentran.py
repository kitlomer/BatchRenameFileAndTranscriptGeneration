import glob, os

align_dir = os.path.join('.','s1_align')
align_files = glob.glob(os.path.join(align_dir, '*.align'))
# fw = open("transin","w") 
# for align in align_files:
	
	# all = open(align).read().split('\n')[1:-2]
	# line =str('')
	# for single in all:
		# line+=single.split(' ')[-1]
		# line+=' '
	# each = os.path.basename(align)[:-6]+'.wav|'+line
	# fw.write(each)
	# fw.write('\n')
	
	
####### =====================combine two wav files=================	
# fw =open("transdoublewav","w")
# for i,align in enumerate(align_files):
	# if i%2==1:
		# doublename=align_files[i-1][-12:-6]+'-'+align_files[i][-12:-6]+'.wav'+'|'
		# all1 = open(align_files[i-1]).read().split('\n')[1:-2]
		# line1 =str('')
		# for single in all1:
			# line1+=single.split(' ')[-1]
			# line1+=' '
		# all2 = open(align_files[i ]).read().split('\n')[1:-2]
		# line2 =str('')
		# for single in all2:
			# line2+=single.split(' ')[-1]
			# line2+=' '
		# fw.write(doublename+line1+line2+'\n')


####### =====================combine three wav files=================	
		
fw =open("transtriwav","w")
for i,align in enumerate(align_files):
	if (i+1)%3==0:
		doublename=align_files[i-2][-12:-6]+'-'+align_files[i-1][-12:-6]+'-'+align_files[i][-12:-6]+'.wav'+'|'
		all1 = open(align_files[i-2]).read().split('\n')[1:-2]
		line1 =str('')
		for single in all1:
			line1+=single.split(' ')[-1]
			line1+=' '
		all2 = open(align_files[i-1]).read().split('\n')[1:-2]
		line2 =str('')
		for single in all2:
			line2+=single.split(' ')[-1]
			line2+=' '
		all3 = open(align_files[i ]).read().split('\n')[1:-2]
		line3 =str('')
		for single in all3:
			line3+=single.split(' ')[-1]
			line3+=' '
		fw.write(doublename+line1+line2+line3+'\n')
		
		
