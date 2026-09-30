import glob

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('assets\\', 'assets/')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed backslashes to forward slashes properly!")
