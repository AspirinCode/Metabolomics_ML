import os
import argparse

# Default is to run on the Windows_EE EC2 instance for the Alm lab
# Script assumes that msconvert.exe is in the system path, for Administrator on Windows_ee instance it is

#NOTE IT REQUIRES THAT THE PATH TO THE DATA NOT HAVE ANY SPACES!!!!

parser = argparse.ArgumentParser()
parser.add_argument('input_dir', help='path to directory or directory tree containing\
	files to convert')
# parser.add_argument('--msconvert', help='path to the msconvert exe',
# 	default=r'C:\\Program\ Files\\ProteoWizard\\ProteoWizard\ 3.0.18226.9d6a5e0de\\msconvert.exe')
args = parser.parse_args()
# msconvert = args.msconvert
input_dir = args.input_dir

parserable_files = ('.d', '.D', '.RAW', '.raw', '.wiff')
constant_convert_cmd = 'msconvert --mzML --filter "peakPicking true 1-" '

for directory, sub_dir_list, file_list in os.walk(input_dir):
	for file_dir in sub_dir_list:
		if file_dir.endswith(parserable_files):
			# print(constant_convert_cmd + '-o "' + directory + '\\" "' + directory + '\\' + file_dir + '"')
			os.system(constant_convert_cmd + '-o ' + directory + '\\ ' + directory + '\\' + file_dir)
	for file in file_list:
		if file.endswith(parserable_files):
			print(file, ' ACTUAL FILE')
			if file.endswith('.wiff'):
				try:
					assert file + '.scan' in file_list
				except:
					print('passing {} since no .wiff.scan file found'.format(file))
					continue
			# print(constant_convert_cmd + '-o "' + directory + '\\" "' + directory + '\\' + file + '"')
			os.system(constant_convert_cmd +'-o ' + directory + '\\ ' + directory + '\\' + file)








