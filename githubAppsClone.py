from os import path
from urllib import urlretrieve
from urlparse import urlparse


import csv 
import sys
 
apps = open('git_apps.csv')
csv_apps = csv.reader(apps)

b = "/archive/master.zip"

text_file = open("Failed_files.txt", "w")


for row in csv_apps:

	app_source = row[9].replace(".git", "")


	app_source = "".join((app_source, b))

	print "App ID: ", row[0]
	print "App Link: ", app_source

	# tgt_path = path.split(urlparse(src_url).path)[-1]
	try:
		urlretrieve(app_source, str(row[1]+".zip"))	
		print "Download completed"
		print "====================================="
	except:
		print "Exception: ", row[0]
		print "====================================="
		text_file.write(row[0]+"," + row[1] + "\n")
		pass

text_file.close()


	

	






