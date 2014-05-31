filename = raw_input("File name? ")
title = raw_input("Page Title? ")
content = raw_input("Page content? ")
author = raw_input("Author? ")


# Open a file
fo = open(filename, "wb")
fo.write("<html><head><title=" + title + "></head><body><h1>" + title +"</h1>" + content + "<br><br>" + "-" + author);

# Close opend file
fo.close()