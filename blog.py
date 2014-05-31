import os
import time
if os.name == "nt":
	postdir = os.path.realpath(__file__)[:-7] + "posts\\"
else:
	postdir = os.path.realpath(__file__)[:-7] + "posts/"

	
date = (time.strftime("%d/%m/%Y %H:%M:%S"))

filename = raw_input("File name? ")
title = raw_input("Page Title? ")
content = raw_input("Page content? ")
author = raw_input("Author? ")

# Open a file
fo = open(postdir + filename, "wb")
fo.write("<html><head><title=" + title + "></head><body><h1>" + title + " - " + date +"</h1><h3><a href='index.html'>Back to Blog</a></h3>" + content + "<br><br>" + "-" + author);

# Close opend file
fo.close()


with open('index.html') as f:
    lines = f.read().splitlines()
lines.insert(8, "<a href='" + postdir + filename + "'>" + title + " - " + date + "</a><br>")
point = 0
while point < len(lines):
	lines[point] = lines[point] + "\n"
	point = point + 1

with open('index.html', 'w') as file:
    file.writelines( lines )