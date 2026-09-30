import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update grid container
    content = content.replace('grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-6 gap-8 pb-16 border-b border-gray-800', 'grid grid-cols-1 md:grid-cols-2 xl:grid-cols-6 gap-8 lg:gap-12 pb-16 border-b border-gray-800')

    # Update the first column col-span
    content = content.replace('<div class="lg:col-span-2">', '<div class="md:col-span-2 xl:col-span-2">')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed tablet responsiveness for footer!")
