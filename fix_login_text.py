file = 'login.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the dark text color for Welcome Back
content = content.replace('dark:text-[#1E293B]', 'dark:text-white')

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed dark mode text in login.html!")
