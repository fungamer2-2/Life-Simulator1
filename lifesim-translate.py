import os

#Extracts lifesim.py files for translation

print("Finding translations...")
FOLDER = os.getcwd()

skip_dirs = [".git", ".github", "__pycache__"]
candidates = []
for path, dirs, files in os.walk(FOLDER, topdown=True):
	for d in skip_dirs:
		if d in dirs:
			dirs.remove(d)
			#print("Skipping " + d)
	for file in files:
		if file.endswith(".py") and file != "pygettext.py":
			candidates.append((path+ "/" + file).removeprefix(FOLDER + "/"))

os.chdir(FOLDER)

names = []
for name in candidates:
	f = open(FOLDER + "/" + name, "r")
	contents = f.read()
	if "_(\"" in contents or "_('":
		names.append(name)
		
all = " ".join(map(lambda s: "\"" + s + "\"", names))
print("Extracting strings...")

os.system("python pygettext.py -d lifesim " + all)
print("Sucessfully extracted all strings")
