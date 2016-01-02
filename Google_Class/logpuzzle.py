import os,re,urllib
f=open('animal_code.google.com','r')
text=f.read()
url=re.findall(r' (/edu/languages/google-python-class/images/puzzle/[a-zA-Z.-]+) ',text)
l=[]

for i in set(url):
	l.append("http://code.google.com"+i)
l=sorted(l)

dest="/home/yash/interviewbit/Google_Class/images"
os.mkdir(dest)
for index,i in enumerate(l):
	print "retrieving"
	urllib.urlretrieve(i,"/home/yash/interviewbit/Google_Class/images/img"+str(index)+".jpg")
