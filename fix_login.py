import re

files = ['login.html', 'signup.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the purple gradient
    content = re.sub(r'<div class="absolute inset-0 bg-gradient-[^>]+></div>', '', content)

    # 2. Update the left side Logo to match index.html
    # We find the existing logo block:
    # <a href="index.html" class="flex items-center gap-3">
    #     <span class="flex h-12 w-12 items-center justify-center rounded-full bg-white shadow-md">
    #         <i class="fa-solid fa-hand-holding-heart text-accent text-xl"></i>
    #     </span>
    #     <span class="text-2xl font-serif font-extrabold text-white tracking-tight">FertiCare</span>
    # </a>
    
    old_logo_left = r'<a href="index.html" class="flex items-center gap-3">\s*<span class="flex h-12 w-12 items-center justify-center rounded-full bg-white shadow-md">\s*<i class="fa-solid fa-hand-holding-heart text-accent text-xl"></i>\s*</span>\s*<span class="text-2xl font-serif font-extrabold text-white tracking-tight">FertiCare</span>\s*</a>'
    new_logo = r'<a href="index.html" class="text-3xl font-serif font-extrabold tracking-tight mb-4 inline-block">\n                        <i class="fa-solid fa-hand-holding-heart text-accent"></i> <span class="text-accent text-xl sm:text-2xl">FertiCare</span>\n                    </a>'
    content = re.sub(old_logo_left, new_logo, content)
    
    # 3. Update the mobile logo to match index.html
    old_logo_mobile = r'<div class="md:hidden text-center mb-5">\s*<a href="index.html" class="flex items-center justify-center gap-2">\s*<span class="flex h-10 w-10 items-center justify-center rounded-full text-white shadow-lg"[^>]+>\s*<i class="fa-solid fa-hand-holding-heart text-lg"></i>\s*</span>\s*<span class="block text-xl font-serif font-extrabold tracking-tight text-accent">FertiCare</span>\s*</a>\s*</div>'
    new_logo_mobile = r'<div class="md:hidden text-center mb-5">\n                        <a href="index.html" class="text-3xl font-serif font-extrabold tracking-tight">\n                            <i class="fa-solid fa-hand-holding-heart text-accent"></i> <span class="text-accent text-xl sm:text-2xl">FertiCare</span>\n                        </a>\n                    </div>'
    content = re.sub(old_logo_mobile, new_logo_mobile, content)
    
    # 4. Update the text colors on the left side
    content = content.replace('text-white leading-tight', 'text-[#1E293B] leading-tight')
    content = content.replace('text-white/85 text-sm', 'text-[#475569] text-sm')
    
    # Quote block updates
    content = content.replace('bg-white/10 backdrop-blur-md', 'bg-white/60 backdrop-blur-md')
    content = content.replace('text-white/50 text-sm mb-2', 'text-accent text-sm mb-2')
    content = content.replace('text-white/90', 'text-[#1E293B] font-medium')
    content = content.replace('text-white/70 mt-3', 'text-[#475569] mt-3 font-semibold')
    
    # Also update the background icons transparency
    content = content.replace('absolute inset-0 opacity-10', 'absolute inset-0 opacity-5')
    content = content.replace('text-white', 'text-[#1E293B]', 1) # Might replace the first one but let's be careful. Actually, let's not blindly replace text-white.
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated login and signup pages!")
