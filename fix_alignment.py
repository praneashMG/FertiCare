import re

file = 'home2.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the h3 tags in the grid
content = content.replace('<h3 class="text-xl font-bold text-primary-text mb-2">', '<h3 class="text-xl font-bold text-primary-text mb-2 min-h-[3.5rem] flex items-center text-center">')

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated home2.html h3 heights!")
