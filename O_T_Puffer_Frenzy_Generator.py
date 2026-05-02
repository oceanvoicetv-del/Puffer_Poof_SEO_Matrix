import os

# Updated to the official app link provided
APP_URL = "https://play.google.com/store/apps/details?id=com.pufferpoof.app&hl="

KEYWORD_MATRIX = {
    "en": "bubble popping game", "es": "juego de explotar burbujas", "fr": "jeu d'éclatement de bulles", 
    "de": "Seifenblasen-Spiel", "it": "gioco di scoppio delle bolle", "nl": "bellenblaas spel", 
    "pt": "jogo de estourar bolhas", "ru": "игра лопать пузыри", "zh-CN": "泡泡爆破游戏", 
    "ja": "バブルポップゲーム", "ko": "버블 팝 게임", "ar": "لعبة فرقعة الفقاعات", 
    "hi": "बुलबुला फोड़ने वाला खेल", "bn": "বাবল পপিং গেম", "ur": "بلبلے پاپ کرنے والا کھیل", 
    "tr": "balon patlatma oyunu", "vi": "trò chơi bắn bong bóng", "th": "เกมระเบิดฟองสบู่", 
    "id": "game meletuskan gelembung", "ms": "permainan meletupkan buih", "tl": "larong bubble popping", 
    "sw": "mchezo wa maputo", "pl": "gra w pękanie baniek", "uk": "гра лопання бульбашок", 
    "cs": "praskání bublin hra", "el": "παιχνίδι με φούσκες", "sv": "bubbelspel", 
    "fi": "kuplan puhkaisupeli", "da": "boblespil", "no": "boblespill"
}

def generate_frenzy_matrix():
    output_dir = "Puffer_Poof_SEO_Matrix"
    if not os.path.exists(output_dir): os.makedirs(output_dir)

    for lang, keyword in KEYWORD_MATRIX.items():
        html_content = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Puffer Poof: The high-velocity {keyword} frenzy. Master the underwater bubble pop challenge and save the reef.">
    <title>Puffer Poof - {keyword.title()} Frenzy</title>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;700&family=Montserrat:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {{ --primary: #00b4d8; --accent: #ffb703; --glow: 0 0 15px rgba(255, 183, 3, 0.6); }}
        body {{ font-family: 'Montserrat', sans-serif; background: linear-gradient(rgba(1,2,10,0.85), rgba(0,0,0,0.95)), url('https://raw.githubusercontent.com/oceanvoicetv-del/OceanVoice-site/main/images/gallery/many_dolphins.jpg') center/cover fixed; color: #e0e0e0; display: flex; align-items: center; justify-content: center; min-height: 100vh; text-align: center; }}
        .container {{ max-width: 800px; padding: 50px; background: rgba(8, 12, 36, 0.65); border: 1px solid #1a2238; border-radius: 15px; backdrop-filter: blur(8px); }}
        h1 {{ font-family: 'Cormorant Garamond', serif; font-size: 4.5rem; color: var(--accent); text-shadow: var(--glow); margin-bottom: 10px; }}
        h2 {{ color: var(--primary); font-weight: 300; letter-spacing: 3px; margin-bottom: 30px; text-transform: uppercase; }}
        p {{ font-size: 1.15rem; line-height: 1.8; margin-bottom: 20px; }}
        .btn {{ display: inline-block; margin-top: 30px; padding: 16px 45px; color: var(--accent); text-decoration: none; font-weight: 600; text-transform: uppercase; border: 2px solid var(--accent); border-radius: 50px; box-shadow: var(--glow); transition: 0.4s; }}
        .btn:hover {{ background: var(--accent); color: #01020a; transform: translateY(-4px); }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Puffer Poof</h1>
        <h2>The {keyword.title()} Frenzy</h2>
        <p>Dive into the ultimate underwater popping sensation! <strong>Puffer Poof</strong> is a fast-paced <span style="color:#fff;">{keyword}</span> designed for maximum velocity and addictive fun.</p>
        <p>Chain explosive bubble reactions, clear the screen with precision, and climb the global leaderboards. The reef is waiting—are you ready for the frenzy?</p>
        <a href="{APP_URL}{lang}" class="btn">Play on Google Play</a>
    </div>
</body>
</html>"""
        with open(os.path.join(output_dir, f"index_{lang}.html"), "w", encoding="utf-8") as f: f.write(html_content)

if __name__ == "__main__": generate_frenzy_matrix()
