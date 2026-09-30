import glob

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '.bg-accent {' not in content:
        content = content.replace('.bg-background { background-color: var(--color-background); }', '.bg-background { background-color: var(--color-background); }\n        .bg-accent { background-color: var(--color-accent); }')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Added .bg-accent to CSS!")
