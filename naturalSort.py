import re

def atoi(text):
	return int(text) if text.isdigit() else text

def natural(text):
	return [atoi(c) for c in re.split('(\d+)',text)]

l=["something1","something12","something17","something2","something25","something29"]
l.sort(key=natural)
print l

