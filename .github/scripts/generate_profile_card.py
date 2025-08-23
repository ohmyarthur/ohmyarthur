import os

PROFILE_CARD_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'profile-card.svg')

svg_content = '''<svg width="400" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="pastelGradient" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#a8edea" />
      <stop offset="100%" stop-color="#fed6e3" />
    </linearGradient>
  </defs>
  <rect width="400" height="200" rx="20" fill="url(#pastelGradient)" />
  <text x="50%" y="40%" dominant-baseline="middle" text-anchor="middle" font-size="28" font-family="Arial" fill="#444">Arthur</text>
  <text x="50%" y="60%" dominant-baseline="middle" text-anchor="middle" font-size="18" font-family="Arial" fill="#666">19 y/o Open-source Enthusiast</text>
  <text x="50%" y="75%" dominant-baseline="middle" text-anchor="middle" font-size="16" font-family="Arial" fill="#888">Jakarta, Indonesia</text>
</svg>'''

with open(PROFILE_CARD_PATH, 'w') as f:
    f.write(svg_content)

print(f"Profile card generated at {PROFILE_CARD_PATH}")
