import os
import shutil

folder = os.path.join(os.path.expanduser("~"), "Downloads")

file_types = {	
	"Images": [".png", ".jpeg", ".jpg", ".pdn", ".psd"],
	"Archives": [".zip", ".7z"],
	"Sounds": [".mp3", ".wav", ".m4a"],
	"Executables": [".exe"],
	"Document Files": [".pdf", ".docx"],
	"Videos": [".mov", ".mp4"],
	"Gifs": [".gif"]
}

for categories in file_types:
	os.makedirs(os.path.join(folder, categories), exist_ok=True)

for file in os.listdir(folder):

	source = os.path.join(folder, file)

	if os.path.isdir(source):
		continue

	for groups, extensions in file_types.items():

		if any(file.lower().endswith(ext) for ext in extensions ):
			destination = os.path.join(folder, groups, file)

			shutil.move(source, destination)

			print("Moved:", file)
			break
