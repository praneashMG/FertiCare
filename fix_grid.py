import glob

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('grid-cols-1 md:grid-cols-3', 'grid-cols-1 md:grid-cols-2 lg:grid-cols-3')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated grid layouts for better iPad responsiveness!")
