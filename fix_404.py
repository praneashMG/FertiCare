import re

file = '404.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the 404 illustration
old_illustration = r'<!-- 404 Illustration -->\s*<div class="mb-8 relative">\s*<div class="text-\[120px\] sm:text-\[160px\] font-black leading-none text-accent/20 select-none">404</div>\s*<div class="absolute inset-0 flex items-center justify-center">\s*<i class="fa-solid fa-hand-holding-heart text-6xl sm:text-7xl text-accent error-illustration"></i>\s*</div>\s*</div>'
new_illustration = r'''<!-- 404 Illustration -->
            <div class="mb-10 flex items-center justify-center gap-2 sm:gap-4 text-accent select-none">
                <span class="text-[120px] sm:text-[160px] font-black leading-none drop-shadow-md">4</span>
                <div class="w-24 h-24 sm:w-32 sm:h-32 rounded-full bg-accent/10 flex items-center justify-center shadow-inner border border-accent/20">
                    <i class="fa-solid fa-hand-holding-heart text-[70px] sm:text-[90px] error-illustration"></i>
                </div>
                <span class="text-[120px] sm:text-[160px] font-black leading-none drop-shadow-md">4</span>
            </div>'''
content = re.sub(old_illustration, new_illustration, content)

# Fix the quick links at the bottom
old_links = r'<!-- Quick links -->\s*<div class="mt-16 pt-8 border-t border-border flex flex-wrap justify-center gap-x-6 gap-y-3 text-secondary-text text-sm">[\s\S]*?</div>'
new_links = r'''<!-- Quick links -->
            <div class="mt-16 flex flex-wrap justify-center gap-4 border-t border-border pt-8">
                <a href="treatments.html" class="px-5 py-2.5 rounded-full border border-border text-secondary-text hover:text-accent hover:border-accent hover:bg-accent/5 transition flex items-center gap-2 text-sm font-medium shadow-sm"><i class="fa-solid fa-stethoscope"></i> Our Treatments</a>
                <a href="doctors.html" class="px-5 py-2.5 rounded-full border border-border text-secondary-text hover:text-accent hover:border-accent hover:bg-accent/5 transition flex items-center gap-2 text-sm font-medium shadow-sm"><i class="fa-solid fa-user-doctor"></i> Our Specialists</a>
                <a href="about.html" class="px-5 py-2.5 rounded-full border border-border text-secondary-text hover:text-accent hover:border-accent hover:bg-accent/5 transition flex items-center gap-2 text-sm font-medium shadow-sm"><i class="fa-solid fa-circle-info"></i> About Us</a>
            </div>'''
content = re.sub(old_links, new_links, content)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Redesigned 404 page!")
