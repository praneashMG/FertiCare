import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The current structure:
# <nav ... flex items-center justify-between ...>
#     <a ...logo...>...</a>
#     <div class="hidden xl:flex items-center space-x-6">
#         <div class="flex space-x-6 ...">...links...</div>
#         <div class="w-px h-6 ..."></div>
#         <div class="flex items-center space-x-4">...buttons...</div>
#     </div>
#     <div class="xl:hidden ...">...</div>
# </nav>

# We want to change it to:
# <nav ... flex items-center justify-between ...>
#     <a ...logo...>...</a>
#     <div class="hidden xl:flex flex-1 justify-center">
#         <div class="flex space-x-6 ...">...links...</div>
#     </div>
#     <div class="hidden xl:flex items-center space-x-4">...buttons...</div>
#     <div class="xl:hidden ...">...</div>
# </nav>

# Let's do string replacements.

old_part1 = '<div class="hidden xl:flex items-center space-x-6">\\n                <div class="flex space-x-6 rtl:space-x-reverse rtl:ml-6 text-primary-text font-medium">'
new_part1 = '<div class="hidden xl:flex flex-1 justify-center">\\n                <div class="flex space-x-6 rtl:space-x-reverse text-primary-text font-medium">'
content = content.replace(old_part1, new_part1)

old_part2 = '</div>\\n\\n                <div class="w-px h-6 bg-border mx-3"></div>\\n                \\n                <div class="flex items-center space-x-4">'
new_part2 = '</div>\\n            </div>\\n\\n            <div class="hidden xl:flex items-center space-x-4">'
content = content.replace(old_part2, new_part2)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated header layout for centered nav items.')
