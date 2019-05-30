import glob, os

wav_dir = os.path.join('.','s1_audios')
wav_files = glob.glob(os.path.join(wav_dir, '*.wav'))
 
for wav in wav_files:
	os.rename(wav,(wav[:-10]+'1'+wav[-10:]))
	
align_dir = os.path.join('.','s1_align')
align_files = glob.glob(os.path.join(align_dir, '*.align'))
 
for align in align_files:
	os.rename(align,(align[:-12]+'1'+align[-12:]))
	
	