import zipfile

# ZIP filename
zip_filename = "Anezone_assets.zip"

# Assets structure with sample content
assets_files = {
    "assets/logo/anezone_logo.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="200" height="50">
  <rect width="200" height="50" fill="#FFD600"/>
  <text x="100" y="30" font-size="20" text-anchor="middle" fill="#000">Anezone</text>
</svg>""",
    "assets/css/style.css": """body {
    font-family: Arial, sans-serif;
    background: #f5f5f5;
    text-align: center;
    padding: 20px;
}
img { max-width: 200px; margin: 10px; }
a { display: inline-block; margin: 10px; padding: 10px 20px; background: #000; color: #fff; text-decoration: none; }"""
}

# Add placeholder product images
for i in range(1,6):
    assets_files[f"assets/images/product{i}.png"] = ""  # empty placeholder

# Create ZIP
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file_path, content in assets_files.items():
        zipf.writestr(file_path, content)

print(f"✅ ZIP তৈরি হয়েছে: {zip_filename}")
