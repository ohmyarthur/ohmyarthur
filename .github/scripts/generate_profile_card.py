import os

# Path ke file SVG (relatif dari lokasi file ini)
PROFILE_CARD_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    'profile-card.svg'
)

# SVG sederhana, fokus ke teks & layout
svg_content = f'''<svg width="420" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#a8edea" />
      <stop offset="100%" stop-color="#fed6e3" />
    </linearGradient>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600&display=swap');
      .name {{ font-family: 'Montserrat', sans-serif; font-size: 28px; fill: #333; }}
      .subtitle {{ font-family: 'Montserrat', sans-serif; font-size: 16px; fill: #555; }}
    </style>
  </defs>

  <!-- background -->
  <rect width="100%" height="100%" rx="16" fill="url(#bg)" />

  <!-- content -->
  <text x="50%" y="40%" text-anchor="middle" class="name">Arthur</text>
  <text x="50%" y="58%" text-anchor="middle" class="subtitle">19 y/o Open-source Enthusiast</text>
  <text x="50%" y="74%" text-anchor="middle" class="subtitle">Jakarta, Indonesia</text>
</svg>'''

with open(PROFILE_CARD_PATH, 'w', encoding='utf-8') as f:
    f.write(svg_content)

print(f"Profile card saved to {PROFILE_CARD_PATH}")
