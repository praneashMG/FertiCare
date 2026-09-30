import re
import os

files = ['index.html', 'home2.html', 'about.html', 'doctors.html']

for file in files:
    if not os.path.exists(file): continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Find the section and the image URL
    section_pattern = r'(<section[^>]*class="relative pt-16 pb-20 lg:pt-24 lg:pb-28 overflow-hidden bg-background"[^>]*>.*?</section>)'
    
    def replace_hero(match):
        section_html = match.group(1)
        
        # Extract image source
        img_match = re.search(r'<img[^>]*src="([^"]+)"', section_html)
        if not img_match:
            return section_html
        img_url = img_match.group(1)
        
        # Remove the image block
        # We will look for: <!-- Responsive HD Hero Image --> ... </div>
        section_html = re.sub(r'<!-- Responsive HD Hero Image -->\s*<div[^>]*>\s*<img[^>]*>\s*</div>', '', section_html)
        
        # Modify section tag to have background image
        section_html = section_html.replace('bg-background', 'bg-cover bg-center')
        section_html = re.sub(r'<section', f'<section style="background-image: url(\'{img_url}\');"', section_html, count=1)
        
        # Add overlay right after section starts
        overlay = '\\n      <div class="absolute inset-0 bg-black bg-opacity-60 z-0"></div>'
        section_html = re.sub(r'(<section[^>]*>)', r'\1' + overlay, section_html, count=1)
        
        # Adjust padding to make it look more like a hero section
        section_html = section_html.replace('pt-16 pb-20 lg:pt-24 lg:pb-28', 'py-32 lg:py-48')
        
        # Update text colors to be white for contrast
        section_html = section_html.replace('text-primary-text', 'text-white')
        section_html = section_html.replace('text-secondary-text', 'text-gray-200')
        section_html = section_html.replace('btn-outline', 'btn-cta-white') # Change outline button to white outline/bg
        
        # Remove mb-14 from CTA buttons container since there's no image below it now
        section_html = section_html.replace('mb-14', 'mb-0')
        
        return section_html
    
    new_content = re.sub(section_pattern, replace_hero, content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Updated hero sections!")
