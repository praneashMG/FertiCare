import re
import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update grid cols to 6 if we keep 5 logical columns
    # <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-12 pb-16 border-b border-gray-800">
    content = content.replace('lg:grid-cols-5 gap-12', 'lg:grid-cols-6 gap-8')

    # 2. Remove the address block from the first column
    # <div class="flex items-start space-x-4 text-gray-300 mb-8">\n                            <i class="fa-solid fa-location-dot text-accent text-xl mt-1"></i>\n                          <span class="text-base">123 Fertility Way, Medical District<br>New York, NY 10001</span>\n                        </div>
    address_regex = re.compile(
        r'<div class="flex items-start space-x-4 text-gray-300 mb-8">\s*<i class="fa-solid fa-location-dot text-accent text-xl mt-1"></i>\s*<span class="text-base">123 Fertility Way, Medical District<br>New York, NY 10001</span>\s*</div>',
        re.MULTILINE
    )
    content = address_regex.sub('', content)

    # 3. Inject the new "Get in Touch" column between Treatments and Quick Links
    # The Treatments closing tag:
    # </ul>\n                </div>\n                <div>\n                    <h4 class="footer-heading font-bold text-xl mb-6">Quick Links</h4>
    
    get_in_touch_html = (
        '</ul>\n'
        '                </div>\n'
        '                <div>\n'
        '                    <h4 class="footer-heading font-bold text-xl mb-6">Get in Touch</h4>\n'
        '                    <ul class="space-y-6">\n'
        '                        <li class="flex items-start gap-4">\n'
        '                            <div class="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center shrink-0">\n'
        '                                <i class="fas fa-map-marker-alt text-accent-light"></i>\n'
        '                            </div>\n'
        '                            <span class="text-gray-300 text-sm mt-1">123 Fertility Way<br>New York, NY 10001</span>\n'
        '                        </li>\n'
        '                        <li class="flex items-center gap-4">\n'
        '                            <div class="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center shrink-0">\n'
        '                                <i class="fas fa-phone-alt text-accent-light"></i>\n'
        '                            </div>\n'
        '                            <span class="text-gray-300 text-sm">+1 (800) 555-0199</span>\n'
        '                        </li>\n'
        '                        <li class="flex items-center gap-4">\n'
        '                            <div class="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center shrink-0">\n'
        '                                <i class="fas fa-envelope text-accent-light"></i>\n'
        '                            </div>\n'
        '                            <span class="text-gray-300 text-sm">contact@ferticare.com</span>\n'
        '                        </li>\n'
        '                    </ul>\n'
        '                </div>\n'
        '                <div>\n'
        '                    <h4 class="footer-heading font-bold text-xl mb-6">Quick Links</h4>'
    )
    
    insertion_regex = re.compile(
        r'</ul>\s*</div>\s*<div>\s*<h4 class="footer-heading font-bold text-xl mb-6">Quick Links</h4>',
        re.MULTILINE
    )
    content = insertion_regex.sub(get_in_touch_html, content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added Get in Touch column!")
