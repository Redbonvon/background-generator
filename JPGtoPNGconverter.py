import sys 
import os
from PIL import Image

pdf_folder = (sys.argv[1])

png_folder = (sys.argv[2])


if not os.path.exists(png_folder):
	os.makedirs(png_folder)


for image in os.listdir(pdf_folder):
	img = Image.open(f'{pdf_folder}{image}')
	clean_name = os.path.splitext(image)[0]
	img.save(f'{png_folder}{clean_name}.png', 'png')

	print('Your pain and suffering is over!!') 