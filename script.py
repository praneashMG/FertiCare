import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Change title and logo text
content = re.sub(r'<title>.*?</title>', '<title>Home | IVF & Fertility Clinic</title>', content)
content = re.sub(r'<span style="color: #E6B325;">Gemora</span>', '<i class="fa-solid fa-hand-holding-heart text-accent"></i> <span class="text-accent text-xl sm:text-2xl">IVF & Fertility</span>', content)
content = re.sub(r'Gemora', 'IVF & Fertility Clinic', content)

# 2. Change CSS variables and colors
content = re.sub(r'--color-primary-text: #5C4033; \n\s*--color-secondary-text: #5C4033; /\* Neat Rich Brown \*/\n\s*--color-accent: #E6B325; /\* Lawn Green \*/\n\s*--color-accent-light: #5C4033; /\* Rich Brown \*/\n\s*--color-border: #E5E7EB; \n\s*--color-hover: #FFF8E6; \n\s*--color-footer-bg: #5C4033;\n\s*--color-footer-text: #EAEAEA;',
'''--color-primary-text: #1E293B;
            --color-secondary-text: #475569;
            --color-accent: #EC4899; /* Pink 500 */
            --color-accent-light: #3B82F6; /* Blue 500 */
            --color-border: #E2E8F0;
            --color-hover: #FDF2F8;
            --color-footer-bg: #0F172A;
            --color-footer-text: #F1F5F9;''', content)

content = re.sub(r'--color-primary-text: #FFFFFF;\n\s*--color-secondary-text: #D7CCC8;\n\s*--color-accent: #E6B325; \n\s*--color-accent-light: #BCAAA4; \n\s*--color-border: #374151; \n\s*--color-hover: #2B1D16;\n\s*--color-footer-bg: #000000;\n\s*--color-footer-text: #FFFFFF;',
'''--color-primary-text: #F1F5F9;
            --color-secondary-text: #CBD5E1;
            --color-accent: #EC4899; 
            --color-accent-light: #3B82F6; 
            --color-border: #334155; 
            --color-hover: #1E293B;
            --color-footer-bg: #020617;
            --color-footer-text: #F1F5F9;''', content)

content = re.sub(r'background: linear-gradient\(135deg, #E6B325 0%, #5C4033 100%\);', 'background: linear-gradient(135deg, #EC4899 0%, #3B82F6 100%);', content)
content = re.sub(r'color: #E6B325 !important; /\* Elegant Green Heading \*/', 'color: #EC4899 !important;', content)
content = re.sub(r'color: #BCAAA4;', 'color: #3B82F6;', content)
content = re.sub(r'rgba\(230,179,37,0\.3\)', 'rgba(236,72,153,0.3)', content)
content = re.sub(r'rgba\(230,179,37,0\.25\)', 'rgba(236,72,153,0.25)', content)
content = re.sub(r'color: #E6B325;', 'color: var(--color-accent);', content)
content = re.sub(r'border-color: #E6B325;', 'border-color: var(--color-accent);', content)
content = re.sub(r'background: #E6B325;', 'background: var(--color-accent);', content)
content = re.sub(r'style="color:#E6B325"', 'class="text-accent"', content)
content = re.sub(r'bg-\[#E6B325\]', 'bg-accent', content)

# 3. Change Nav
desktop_nav_old = """<a href="about.html" class="nav-link">About Us</a>
<a href="specimens.html" class="nav-link">Specimens</a>
<a href="fossils.html" class="nav-link">Fossils</a>
<a href="minerals.html" class="nav-link">Minerals</a>
<a href="collections.html" class="nav-link">Collections</a>
<a href="contact.html" class="nav-link">Contact</a>"""
desktop_nav_new = """<a href="about.html" class="nav-link">About Us</a>
<a href="treatments.html" class="nav-link">Treatments</a>
<a href="doctors.html" class="nav-link">Doctors</a>
<a href="contact.html" class="nav-link">Contact</a>"""
content = content.replace(desktop_nav_old, desktop_nav_new)

mobile_nav_old = """<a href="about.html" class="block text-primary-text font-semibold text-lg py-2">About Us</a>
<a href="specimens.html" class="block text-primary-text font-semibold text-lg py-2">Specimens</a>
<a href="fossils.html" class="block text-primary-text font-semibold text-lg py-2">Fossils</a>
<a href="minerals.html" class="block text-primary-text font-semibold text-lg py-2">Minerals</a>
<a href="collections.html" class="block text-primary-text font-semibold text-lg py-2">Collections</a>
<a href="contact.html" class="block text-primary-text font-semibold text-lg py-2">Contact</a>"""
mobile_nav_new = """<a href="about.html" class="block text-primary-text font-semibold text-lg py-2">About Us</a>
<a href="treatments.html" class="block text-primary-text font-semibold text-lg py-2">Treatments</a>
<a href="doctors.html" class="block text-primary-text font-semibold text-lg py-2">Doctors</a>
<a href="contact.html" class="block text-primary-text font-semibold text-lg py-2">Contact</a>"""
content = content.replace(mobile_nav_old, mobile_nav_new)

# 4. Footer Changes
content = content.replace('Specimen Categories', 'Treatments')
content = content.replace('Providing authentic fossil and mineral specimens with premium quality and rare geological treasures for collectors and enthusiasts.', 'Providing empathetic, personalized care with high success rates for your journey to parenthood. Tracking treatment cycle stages and supporting you every step of the way.')
footer_links_old = """<ul class="space-y-4">
    <li><a href="specimens.html" class="footer-link">Rare Specimens</a></li>
    <li><a href="fossils.html" class="footer-link">Ancient Fossils</a></li>
    <li><a href="minerals.html" class="footer-link">Crystal Minerals</a></li>
    <li><a href="collections.html" class="footer-link">Curated Collections</a></li>
</ul>"""
footer_links_new = """<ul class="space-y-4">
    <li><a href="treatments.html" class="footer-link">IVF Treatment</a></li>
    <li><a href="treatments.html" class="footer-link">IUI Treatment</a></li>
    <li><a href="doctors.html" class="footer-link">Our Specialists</a></li>
    <li><a href="userdash.html" class="footer-link">Patient Dashboard</a></li>
</ul>"""
content = content.replace(footer_links_old, footer_links_new)

footer_quick_old = """<ul class="space-y-4">
                        <li><a href="partners.html" class="footer-link">Partners</a></li>
                        <li><a href="about.html" class="footer-link">About Us</a></li>
                        <li><a href="specimens.html" class="footer-link">Specimens</a></li>
                        <li><a href="fossils.html" class="footer-link">Fossils</a></li>
                        <li><a href="contact.html" class="footer-link">Contact</a></li>
                    </ul>"""
footer_quick_new = """<ul class="space-y-4">
                        <li><a href="about.html" class="footer-link">About Us</a></li>
                        <li><a href="treatments.html" class="footer-link">Treatments</a></li>
                        <li><a href="doctors.html" class="footer-link">Doctors</a></li>
                        <li><a href="contact.html" class="footer-link">Contact</a></li>
                        <li><a href="login.html" class="footer-link">Patient Login</a></li>
                    </ul>"""
content = content.replace(footer_quick_old, footer_quick_new)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated index.html")
