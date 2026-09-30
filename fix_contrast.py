import re

files = ['login.html', 'signup.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add light overlay behind the text
    # The structure is:
    # <div class="hidden md:flex md:w-5/12 relative p-8 flex-col justify-between bg-cover bg-center" style="background-image: url(...)">
    #     <div class="absolute inset-0 opacity-5">...
    
    # We can inject a white overlay right after the background style.
    
    if '<div class="absolute inset-0 bg-white/70 backdrop-blur-[2px]"></div>' not in content:
        content = re.sub(
            r'(<div class="hidden md:flex md:w-5/12 relative p-8 flex-col justify-between bg-cover bg-center"[^>]+>)',
            r'\1\n                <div class="absolute inset-0 bg-white/70 backdrop-blur-[2px]"></div>',
            content
        )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added overlay to login and signup pages!")
