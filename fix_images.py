import re
import os

def update_file(filename, replacements):
    if not os.path.exists(filename): return
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    for old, new in replacements:
        content = content.replace(old, new)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# Update index.html
update_file('index.html', [
    ("url('assets/a5.avif')", "url('assets/bb.webp')"),  # background hero
    ('src="assets/cc.jpeg" alt="Advanced Fertility Laboratory"', 'src="assets/vr.jpg" alt="Advanced Fertility Laboratory"'),
])

# Update home2.html
update_file('home2.html', [
    ("url('assets/r1.jpg')", "url('assets/gfd.jpg')"),  # background hero
    ('src="assets/r2.jpg" alt="Medical professional reviewing fertility ultrasound results"', 'src="assets/ggg.jpg" alt="Medical professional reviewing fertility ultrasound results"')
])

# Update about.html
update_file('about.html', [
    ("url('assets/a2.jpg')", "url('assets/tt.jpg')"),  # background hero
    ('src="assets/a5.avif" alt="Advanced Embryology Lab"', 'src="assets/vr.jpg" alt="Advanced Embryology Lab"'),
    ('src="assets/cc.jpeg" alt="Private Consultation Room"', 'src="assets/m.jpg" alt="Private Consultation Room"')
])

# Update doctors.html
update_file('doctors.html', [
    ("url('assets/d1.jpg')", "url('assets/m.jpg')")  # background hero
])

# Update treatments.html
update_file('treatments.html', [
    ('src="assets/a4.webp" alt="Doctor explaining fertility treatment options to a patient"', 'src="assets/ggg.jpg" alt="Doctor explaining fertility treatment options to a patient"'),
    ('src="assets/a5.avif" alt="ICSI Procedure under microscope"', 'src="assets/vr.jpg" alt="ICSI Procedure under microscope"')
])

print("Images replaced successfully!")
