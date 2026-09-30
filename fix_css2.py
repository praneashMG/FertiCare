import glob

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '.bg-accent-light {' not in content:
        content = content.replace('.bg-accent { background-color: var(--color-accent); }', '.bg-accent { background-color: var(--color-accent); }\n        .bg-accent-light { background-color: var(--color-accent-light); }')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Added .bg-accent-light to CSS!")
