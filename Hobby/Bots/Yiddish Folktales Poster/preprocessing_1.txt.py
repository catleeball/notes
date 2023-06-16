# coding: utf-8

with open('Yiddish_Folktales.md') as f:
    mdtext = f.read()
    
with open('Yiddish_Folktales.md') as f:
    mdlines = f.readlines()
    
    
mdlines[-1]
mdlines[-2]
tales = {}
mdlines[618]
mdlines[619]
mdlines[617]
mdlines[616]
lines = []
for line in mdlines:
    if not line.contains('\xa0'):
        lines.append(line)
        continue
    newline = []
    for char lin line:
        if char == '\xa0''
for line in mdlines:
    if not line.contains('\xa0'):
        lines.append(line)
        continue
    newline = []
    for char lin line:
        if char == '\xa0'':
            continue
for line in mdlines:
    if not line.contains('\xa0'):
        lines.append(line)
        continue
    newline = []
    for char lin line:
        if char == '\xa0':
            continue
for line in mdlines:
    if not line.contains('\xa0'):
        lines.append(line)
        continue
    newline = []
    for char lin line:
        if char == '\xa0':
            continue
for line in mdlines:
    if not line.contains('\xa0'):
        lines.append(line)
        continue
    newline = []
    for char in line:
        if char == '\xa0':
            continue
        newline.append(char)
    newline = ''.join(newline)
    lines.append(newline)
    
for line in mdlines:
    if '\xa0' not in line:
        lines.append(line)
        continue
    newline = []
    for char in line:
        if char == '\xa0':
            continue
        newline.append(char)
    newline = ''.join(newline)
    lines.append(newline)
    
lines
lines_ = []
# Delete all headers containing no letters or numbers
for line in lines:
    if not line.startswith('#'):
        lines_.append(line)
        continue
    hashmark, chars = line.split('#', maxsplit=1)
    if any(lambda c: c in string.digits or c in string.ascii_letters , chars):
      lines_.append(line)
      continue
      
# Delete all headers containing no letters or numbers
for line in lines:
    if not line.startswith('#'):
        lines_.append(line)
        continue
    hashmark, chars = line.split('#', maxsplit=1)
    if any([lambda c: c in string.digits or c in string.ascii_letters , chars]):
      lines_.append(line)
      continue
      
lines_
lines_[0]
lines_[1]
lines_[615]
lines_[616]
lines_[617]
lines_[618]
lines_[644]
lines_[643:][-1]
lines_[644:][-1]
lines_[645:][-1]
nointro = lines_[643:]
nointro[0]
nointro[1]
import re
reg = re.compile(r'\**?(\d)\**')
reg.match('# **1**')
print(reg.match('# **1**'))
reg = re.compile(r'\**(\d)\**')
print(reg.match('# **1**'))
reg = re.compile(r'\**\d\**')
print(reg.match('# **1**'))
reg = re.compile(r'\**(\d)\**')
reg.group()
match = reg.match("# **1** ")
match
regmatch = reg.match("# **1** ")
regmatch.group()
print(regmatch)
r = re.compile(r'\**(\d)\**')
r
r = re.compile('[a-z]+')
r.match('abc')
r = re.compile(r'\#[\#\s]*\**(\d)\**')
r.match('')
print(r.match(''))
print(r.match('# **1**'))
cleaned = []
matches = r.match('# **1**')
matches.group()
matches.groups()
r = re.compile(r'\#[\#\s]*\**(\d{1,3})\**')
matches = r.match('# **1**')
matches.group
matches.group()
matches.groups()
matches = r.match('# **10**')
matches.groups()
matches = r.match('# **100**')
matches.groups()
cleaned = []
for line in nointro:
    if line.startswith('#'):
        cleaned.append(line)
    matches = r.match(line)
    if not matches:
        continue
    num = matches.groups()[0]
    cleaned.append(f'# {num}')
    
cleaned
for line in nointro:
    if not line.startswith('#'):
        cleaned.append(line)
    matches = r.match(line)
    if not matches:
        continue
    num = matches.groups()[0]
    cleaned.append(f'# {num}')
    
cleaned = []
for line in nointro:
    if not line.startswith('#'):
        cleaned.append(line)
    matches = r.match(line)
    if not matches:
        continue
    num = matches.groups()[0]
    cleaned.append(f'# {num}')
    
cleaned
cleaned[0]
cleaned[1]
with open('cleaned_text.md', 'w') as f:
    contents = ''.join(cleaned)
    f.write(contents)
    
