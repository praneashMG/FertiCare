import re
import glob

# 1. Gather all assets
all_assets = glob.glob('assets/*.*')
images = [a.replace('\\\\', '/') for a in all_assets if a.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.avif'))]
images = [img for img in images if 'fav.png' not in img] # ignore favicon

# 2. Gather all image slots across HTML files
html_files = glob.glob('*.html')

slots = []
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # find all src="..."
    src_matches = re.finditer(r'src="([^"]+)"', content)
    for match in src_matches:
        val = match.group(1)
        if val.startswith('assets/') and 'fav.png' not in val:
            slots.append({'file': file, 'type': 'src', 'original': val})
            
    # find all url('...')
    url_matches = re.finditer(r"url\('([^']+)'\)", content)
    for match in url_matches:
        val = match.group(1)
        if val.startswith('assets/') and 'fav.png' not in val:
            slots.append({'file': file, 'type': 'url', 'original': val})

print(f"Total images available: {len(images)}")
print(f"Total image slots to fill: {len(slots)}")
