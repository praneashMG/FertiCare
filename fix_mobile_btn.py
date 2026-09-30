import re

file = 'doctors.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the padding
content = content.replace('p-10 lg:p-14', 'p-6 sm:p-10 lg:p-14')

# Fix the flex container and button
# Old: <div class="flex gap-4">
# New: <div class="flex flex-wrap items-center justify-center gap-3 sm:gap-4">
content = content.replace('<div class="flex gap-4">', '<div class="flex flex-wrap items-center justify-center gap-3 sm:gap-4">')

# Old: <a href="contact.html" class="px-6 py-2 bg-accent text-white font-bold rounded-full hover:shadow-lg transition-all">Book with Dr. Jenkins</a>
# New: <a href="contact.html" class="px-4 sm:px-6 py-2 text-sm sm:text-base bg-accent text-white font-bold rounded-full hover:shadow-lg transition-all whitespace-nowrap">Book with Dr. Jenkins</a>
content = content.replace('px-6 py-2 bg-accent text-white font-bold rounded-full hover:shadow-lg transition-all', 'px-4 sm:px-6 py-2 text-sm sm:text-base bg-accent text-white font-bold rounded-full hover:shadow-lg transition-all whitespace-nowrap')

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed mobile responsiveness for Book with Dr. Jenkins button!")
