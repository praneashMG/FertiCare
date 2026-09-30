import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Inject the hover utility into the style block
    if '.hover\\:text-accent:hover' not in content:
        content = content.replace(
            '.text-accent { color: var(--color-accent); }',
            '.text-accent { color: var(--color-accent); }\n        .hover\\:text-accent:hover { color: var(--color-accent) !important; }'
        )

        # For pages like login.html that don't have .text-accent defined in the style block but use bg-accent
        if '.hover\\:text-accent:hover' not in content:
            content = content.replace(
                '</style>',
                '    .hover\\:text-accent:hover { color: #EC4899 !important; }\n    </style>'
            )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed hover text visibility!")
