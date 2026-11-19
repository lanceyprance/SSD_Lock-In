"""Check every md file: relative links/images exist, <details> blocks balanced."""
import re, os, glob, sys
bad = 0
for f in sorted(glob.glob('**/*.md', recursive=True)):
    if f.startswith('tools/'): continue
    s = open(f).read(); d = os.path.dirname(f)
    for m in re.finditer(r'!?\[[^\]]*\]\(([^)\s]+)\)', s):
        href = m.group(1).split('#')[0]
        if not href or re.match(r'^(https?:|mailto:|data:)', href): continue
        if not os.path.exists(os.path.normpath(os.path.join(d, href))):
            print(f'{f}: missing {href}'); bad += 1
    o, c = s.count('<details>'), s.count('</details>')
    if o != c: print(f'{f}: details {o} open vs {c} close'); bad += 1
print('problems:', bad); sys.exit(1 if bad else 0)
