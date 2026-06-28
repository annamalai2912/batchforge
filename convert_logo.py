import os
from PIL import Image

logo_path = r"C:\Users\Xtreme\.gemini\antigravity\brain\dcffd26e-31a3-4447-bc8f-ffdff3fe71ec\batchforge_logo_1782563071614.png"
output_path = r"e:\Batch Scrippting\batchforge.ico"

try:
    img = Image.open(logo_path)
    # Ensure it's square
    w, h = img.size
    if w != h:
        s = max(w, h)
        bg = Image.new('RGBA', (s, s), (255, 255, 255, 0))
        bg.paste(img, ((s - w) // 2, (s - h) // 2))
        img = bg
        
    img.save(output_path, format="ICO", sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])
    print(f"Successfully created {output_path}")
except Exception as e:
    print(f"Error: {e}")
