import sys

def minWindow(s, t):
	s_map = {}
	t_map = {}

	for i in t:
		if i in t_map:
			t_map[i]+=1
		else:
			t_map[i] = 1

	start = 0
	end = 0
	min_length = sys.maxsize
	lettercnt = 0
	result = ""

	while end<len(s):
		if s[end] in t_map:
			if s[end] in s_map:
				s[end]+=1
			else:
				s[end] = 1
			if s_map[s[end]] <= t_map[s[end]]:
				lettercnt+=1

		if lettercnt==len(t):
			while (not s[start] in t_map) or (s_map[s[start]] > t_map[s[start]]):
				pass

			if end-start+1 < min:
				min_length = end-start+1
				result = s[start:end+1]
	
		end+=1

	return result

print minWindow("ADOBECODEBANC", "ABC")
