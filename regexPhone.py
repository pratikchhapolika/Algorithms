import re
#phonePattern=re.compile(r'(\(?\d{3}\)?)[ -](\d{3})-(\d{4})$')
phonePattern=re.compile(r'((\(\d{3}\))|(\d{3}))[ -](\d{3})-(\d{4})$')
print phonePattern.search('555-555-5555')
print phonePattern.search('(555) 555-5555')
print phonePattern.search('555-555-5555')
