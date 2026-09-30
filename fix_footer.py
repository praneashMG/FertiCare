import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_footer_logo = '<h1 class="text-3xl font-serif font-black text-accent">IVF & Fertility Clinic</h1>'
new_footer_logo = '<a href="index.html" class="text-3xl font-serif font-extrabold tracking-tight block mb-4">\\n                        <i class="fa-solid fa-hand-holding-heart text-accent"></i> <span class="text-accent text-xl sm:text-2xl">IVF & Fertility</span>\\n                    </a>'

content = content.replace(old_footer_logo, new_footer_logo)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated footer logo")
