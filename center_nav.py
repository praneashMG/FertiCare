import re
import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1: Ensure nav has 'relative' class if it doesn't already
    # The nav tag looks like: <nav class="container mx-auto px-4 sm:px-6 lg:px-8 py-3 flex items-center justify-between h-[70px]">
    content = re.sub(r'(<nav class="[^"]*justify-between)[^"]*(")', r'\1 relative\2', content)

    # Step 2: Separate the giant wrapper into two separate flex containers
    # The wrapper is: <div class="hidden xl:flex items-center space-x-6">
    # Inside it is: <div class="flex space-x-6 rtl:space-x-reverse rtl:ml-6 text-primary-text font-medium">
    # We want to change the wrapper for the nav items to be absolute centered
    
    pattern = re.compile(
        r'<div class="hidden xl:flex items-center space-x-6">\s*'
        r'<div class="flex space-x-6 rtl:space-x-reverse rtl:ml-6 text-primary-text font-medium">',
        re.MULTILINE
    )
    
    replacement = (
        '<div class="hidden xl:flex absolute left-1/2 transform -translate-x-1/2">\n'
        '                <div class="flex space-x-6 rtl:space-x-reverse text-primary-text font-medium">'
    )
    content = pattern.sub(replacement, content)
    
    # Step 3: Find the separator and split the container for the buttons
    # The separator is: </div>\s*<div class="w-px h-6 bg-border mx-3"></div>\s*<div class="flex items-center space-x-4">
    # We replace it with: </div>\n            </div>\n            <div class="hidden xl:flex items-center space-x-4">
    
    pattern2 = re.compile(
        r'</div>\s*<div class="w-px h-6 bg-border mx-3"></div>\s*<div class="flex items-center space-x-4">',
        re.MULTILINE
    )
    replacement2 = (
        '</div>\n'
        '            </div>\n\n'
        '            <div class="hidden xl:flex items-center space-x-4">'
    )
    content = pattern2.sub(replacement2, content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated nav centering in all files!")
