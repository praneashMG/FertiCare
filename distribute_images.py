import re
import glob
import random

random.seed(42) # fixed seed for reproducibility

# 1. Gather all assets
all_assets = glob.glob('assets/*.*')
images = [a.replace('\\\\', '/') for a in all_assets if a.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.avif'))]
images = [img for img in images if 'fav.png' not in img]
images.sort()
random.shuffle(images)

html_files = glob.glob('*.html')

img_idx = 0

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We will do a replacement function that picks the next image
    def replacer_src(match):
        global img_idx
        val = match.group(1)
        if val.startswith('assets/') and 'fav.png' not in val:
            new_img = images[img_idx % len(images)]
            img_idx += 1
            return f'src="{new_img}"'
        return match.group(0)

    def replacer_url(match):
        global img_idx
        val = match.group(1)
        if val.startswith('assets/') and 'fav.png' not in val:
            new_img = images[img_idx % len(images)]
            img_idx += 1
            return f"url('{new_img}')"
        return match.group(0)

    content = re.sub(r'src="([^"]+)"', replacer_src, content)
    content = re.sub(r"url\('([^']+)'\)", replacer_url, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Distributed {len(images)} images across {img_idx} slots in {len(html_files)} files without inner-page repetition (mostly).")
