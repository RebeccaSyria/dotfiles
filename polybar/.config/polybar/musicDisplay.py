import subprocess 
import os
with open(os.devnull, 'w') as devnull:
	status = subprocess.run(["playerctl","status"], stdout=devnull, stderr=devnull)
if status.returncode == 0:
	artist = subprocess.check_output(["playerctl","metadata", "artist"])
	title = subprocess.check_output(["playerctl","metadata","title"])
	print(title.decode("utf-8") + " - " + artist.decode("utf-8"))
else:
	print(" ")
