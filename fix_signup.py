import re

file = 'signup.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Update the mobile logo
old_logo = re.compile(r'<div class="md:hidden text-center mb-8 mt-4">\s*<a href="index.html" class="flex items-center justify-center gap-2">\s*<span class="flex h-12 w-12 items-center justify-center rounded-full text-\[#1E293B\] shadow-lg"\s*style="background: linear-gradient\(135deg, #EC4899, #3B82F6\);">\s*<i class="fa-solid fa-hand-holding-heart text-xl"></i>\s*</span>\s*<span class="block text-2xl font-serif font-extrabold tracking-tight text-accent">FertiCare</span>\s*</a>\s*</div>')
new_logo = r'<div class="md:hidden text-center mb-6 mt-4">\n                        <a href="index.html" class="text-3xl font-serif font-extrabold tracking-tight">\n                            <i class="fa-solid fa-hand-holding-heart text-accent"></i> <span class="text-accent text-xl sm:text-2xl">FertiCare</span>\n                        </a>\n                    </div>'
content = old_logo.sub(new_logo, content)

# Also ensure left side logo is correct if it was missed
old_logo_left = re.compile(r'<a href="index.html" class="flex items-center gap-3">\s*<span class="flex h-12 w-12 items-center justify-center rounded-full bg-white shadow-md">\s*<i class="fa-solid fa-hand-holding-heart text-accent text-xl"></i>\s*</span>\s*<span class="text-2xl font-serif font-extrabold text-[#1E293B] tracking-tight">FertiCare</span>\s*</a>')
new_logo_left = r'<a href="index.html" class="text-3xl font-serif font-extrabold tracking-tight mb-4 inline-block">\n                        <i class="fa-solid fa-hand-holding-heart text-accent"></i> <span class="text-accent text-xl sm:text-2xl">FertiCare</span>\n                    </a>'
content = old_logo_left.sub(new_logo_left, content)

# Adjust padding for better spacing on 360px
content = content.replace('p-2 sm:p-4 lg:p-6', 'p-5 sm:p-8 lg:p-12')

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated signup page mobile logo and spacing!")
