import re
import glob

html_files = glob.glob('*.html')
images = ['assets/a2.jpg', 'assets/a4.webp', 'assets/a5.avif', 'assets/cc.jpeg', 'assets/r1.jpg', 'assets/r2.jpg', 'assets/r3.jpg', 'assets/r4.jpg']
doctor_images = ['assets/d1.jpg', 'assets/d2.jpg', 'assets/d3.jpg', 'assets/d4.jpg']

img_idx = 0
doc_idx = 0

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def replacer(match):
        global img_idx, doc_idx
        # Check surrounding text for doctor context roughly
        if 'doctor' in file.lower() or 'Dr.' in content:
             # Just use doctor images for everything in doctors.html or if it looks like a doctor
             pass
             
        url = match.group(0)
        return url

    # Replace unsplash in bg images
    def bg_repl(match):
        global img_idx, doc_idx
        if file == 'doctors.html' and doc_idx < len(doctor_images):
            res = doctor_images[doc_idx]
            doc_idx += 1
            return res
        res = images[img_idx % len(images)]
        img_idx += 1
        return res
        
    content = re.sub(r'https://images\.unsplash\.com/[^\'"\s)]+', bg_repl, content)

    # Let's add an image to index.html 'Why Choose Us' section
    if file == 'index.html':
        # Find 'Why Choose Us?'
        if '<!-- Feature 1 -->' in content and 'assets/add1.jpg' not in content:
            addition = '<img src="assets/l1.jpeg" class="w-full h-48 object-cover rounded-xl mb-4">'
            content = content.replace('<!-- Feature 1 -->\\n                    <div class="p-8', '<!-- Feature 1 -->\\n                    <div class="p-8">\\n                        ' + addition + '\\n                    </div>\\n                    <div class="p-8')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Replaced Unsplash images with local assets!")
