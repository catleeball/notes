# coding: utf-8

with open('cleaned_text.md', 'r') as f:
    tales = f.read()
    
tales
import re
r = re.compile(r'(\#\s[\d{1-3}].*)')
matches = r.match(tales)
matches
print(matches)
r = re.compile(r'(\#\s[\d{1-3}].*)', re.MULTILINE)
matches = r.match(tales)
type(matches)
matches
r = re.compile(r'\#\s(\d{1-3})(.*)', re.MULTILINE)
matches = r.match(tales)
matches
get_ipython().run_line_magic('pinfo', 're.findall')
re.findall(r'(\#\s[\d{1-3}].*)', tales)
tales_dict = {}
with open('cleaned_text.md', 'r') as f:
    tales = f.readlines()
    
with open('cleaned_text.md', 'r') as f:
    tales = f.read()
    
    
chapter_regex = re.compile(r'^\#\s?(\d{1,3})')
chapter_regex.match('# 1')
chapter_regex.match('# 1 ')
chapter_regex.match('# 10 ')
chapter_regex.match('# 100 ')
tale_list = re.split(chapter_regex, tales)
tale_list
len(tale_list)
split_reg = re.compile(r'^#\s?\d.*')
tale_list = re.split(split_reg, tales)
tale_list
len(tale_list)
chapter_regex = re.compile(r'^\#\s?(\d{1,3})', re.MULTILINE)
tale_list = re.split(chapter_regex, tales)
len(tale_list)
tale_list[0]
tale_list[1]
tale_list[2]
tale_list[3]
tale_list[4]
tale_list[-1]
for t in tale_list:
    if all([lambda c: c is string.whitespace, t]):
        print('.')
        
for t in tale_list:
    if not all([lambda c: c is string.whitespace, t]):
        print('.')
        
        
for t in tale_list:
    if not all([lambda c: c in string.whitespace, t]):
        print('.')
        
for t in tale_list:
    if all([lambda c: c in string.whitespace, t]):
        print('.')
        
filtered_tale_list = list(filter( lambda s: s == '\n' , tale_list ))
filtered_tale_list 
filtered_tale_list = list(filter( lambda s: s != '\n' , tale_list ))
filtered_tale_list
tale_list[0:]
tale_list[1:]
tale_list[1:][0]
tale_list = tale_list[1:]
tale_dict = {}
get_ipython().run_line_magic('pinfo', 'string.count')
get_ipython().set_next_input("'s'.count");get_ipython().run_line_magic('pinfo', 'count')
's'.count()?
's'.count()
's'.count('s')
's'.count(string.digits)
import string
's'.count(string.digits)
all([lambda c: c in string.digits, '123a54'])
[c for c in '1234a567' if c in string.digits]
'123'.isdigit
'123'.isdigit()
'123a'.isdigit()
i = 0
for t in tale_list:
    if t.isdigit():
        i = t
        continue
    tale_dict[i] = t
    
tale_dict
tale_dict[1]
tale_dict['1']
for t in tale_list:
    if t.isdigit():
        i = int(t)
        continue
    tale_dict[i] = t.strip()
    
    
tale_dict = {}
for t in tale_list:
    if t.isdigit():
        i = int(t)
        continue
    tale_dict[i] = t.strip()
    
    
tale_dict
tale_dict[1]
tale_dict[10]
tale_dict[100]
