import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We find the paragraph in the first column of the footer
    old_p = '<p class="text-lg leading-relaxed max-w-sm !text-white-400">\n  Providing empathetic, personalized care with high success rates for your journey to parenthood. Tracking treatment \ncycle stages and supporting you every step of the way.</p>'
    
    # If the exact multiline string fails, we'll use regex.
    import re
    pattern = re.compile(
        r'<p class="text-lg leading-relaxed max-w-sm !text-white-400">\s*'
        r'Providing empathetic, personalized care with high success rates for your journey to parenthood\. Tracking treatment\s*'
        r'cycle stages and supporting you every step of the way\.</p>',
        re.MULTILINE
    )
    
    new_html = (
        '<p class="text-lg leading-relaxed max-w-sm text-gray-300 mb-6">\n'
        '                          Providing empathetic, personalized care with high success rates for your journey to parenthood. Tracking treatment cycle stages and supporting you every step of the way.\n'
        '                      </p>\n'
        '                      <div class="flex items-start space-x-4 text-gray-300 mb-8">\n'
        '                          <i class="fa-solid fa-location-dot text-accent text-xl mt-1"></i>\n'
        '                          <span class="text-base">123 Fertility Way, Medical District<br>New York, NY 10001</span>\n'
        '                      </div>'
    )
    
    content = pattern.sub(new_html, content)
    
    # Also there is a version that might be slightly different in formatting.
    # Let's try to just do a broad replacement if it failed.
    if '123 Fertility Way' not in content:
        # Fallback regex
        fallback = re.compile(r'<p class="text-lg leading-relaxed max-w-sm !text-white-400">[\s\S]*?every step of the way\.</p>')
        content = fallback.sub(new_html, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated footer with address!")
