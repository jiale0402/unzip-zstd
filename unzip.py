import zstandard
import pathlib

def decompress_zstandard_to_folder(input_file, destination_dir):
    input_file = pathlib.Path(input_file)
    with open(input_file, 'rb') as compressed:
        decomp = zstandard.ZstdDecompressor()
        output_path = pathlib.Path(destination_dir) / input_file.stem
        with open(output_path, 'wb') as destination:
            decomp.copy_stream(compressed, destination)
            
import os
file_path = '...'
files = os.listdir(file_path)
wd = os.getcwd()
data_files =  []
for file in files: 
    if file.endswith('zst'):
        data_files.append(wd+file)

for f in data_files:
    decompress_zstandard_to_folder(f,'some destination')