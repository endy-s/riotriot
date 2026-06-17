# Gera o stage plot técnico (top-down) em SVG -> assets/stageplot.svg
# Layout: upstage (fundo) em cima, downstage (frente) embaixo
# Esq -> Dir: Guit Base | Baixo | [Bateria fundo / Vocal frente] | Guit Solo
# (sem riser, sem DI de baixo, sem monitores numerados — canais batem com a input list)

W, H = 1000, 760
STAGE_X, STAGE_Y, STAGE_W, STAGE_H = 40, 70, 920, 600

INK="#1a1a1a"; ORANGE="#ff5b29"; LILAC="#d9a8ff"; CREAM="#ece6d8"; GREY="#bbb"

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Arial, sans-serif">')
# fundo
svg.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{CREAM}"/>')

# moldura do palco
svg.append(f'<rect x="{STAGE_X}" y="{STAGE_Y}" width="{STAGE_W}" height="{STAGE_H}" '
           f'fill="#fff" stroke="{INK}" stroke-width="4" rx="6"/>')

# labels upstage/downstage
svg.append(f'<text x="{W/2}" y="{STAGE_Y-22}" text-anchor="middle" font-size="17" font-weight="bold" fill="#888" letter-spacing="3">UPSTAGE  /  FUNDO DO PALCO</text>')
svg.append(f'<text x="{W/2}" y="{STAGE_Y+STAGE_H+38}" text-anchor="middle" font-size="17" font-weight="bold" fill="#888" letter-spacing="3">DOWNSTAGE  /  FRENTE  •  PLATEIA</text>')

# ---- helpers ----
def amp(x, y, label, num):
    # cabinet de amplificador (retângulo com grade)
    w,h=84,58
    s=[f'<g>']
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{LILAC}" stroke="{INK}" stroke-width="2.5" rx="4"/>')
    for i in range(1,4):
        s.append(f'<line x1="{x+10}" y1="{y+h*i/4}" x2="{x+w-10}" y2="{y+h*i/4}" stroke="{INK}" stroke-width="1" opacity="0.4"/>')
    s.append(f'<text x="{x+w/2}" y="{y+h+15}" text-anchor="middle" font-size="12" font-weight="bold" fill="{INK}">{label}</text>')
    s.append(numbadge(x+w-8, y-8, num))
    s.append('</g>')
    return "".join(s)

def numbadge(cx, cy, num):
    return (f'<circle cx="{cx}" cy="{cy}" r="13" fill="{ORANGE}" stroke="#fff" stroke-width="2"/>'
            f'<text x="{cx}" y="{cy+4.5}" text-anchor="middle" font-size="13" font-weight="bold" fill="#fff">{num}</text>')

def micstand(cx, cy, label="", num=None):
    # pedestal de mic visto de cima: círculo + haste
    s=[f'<g>']
    s.append(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy+26}" stroke="{INK}" stroke-width="3"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="11" fill="#fff" stroke="{INK}" stroke-width="3"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{INK}"/>')
    if label:
        s.append(f'<text x="{cx}" y="{cy+44}" text-anchor="middle" font-size="11" font-weight="bold" fill="{INK}">{label}</text>')
    if num is not None:
        s.append(numbadge(cx+16, cy-14, num))
    s.append('</g>')
    return "".join(s)

def musician(cx, cy, name, sub=""):
    # ponto do músico (círculo cinza com nome)
    s=[f'<g>']
    s.append(f'<circle cx="{cx}" cy="{cy}" r="30" fill="{INK}"/>')
    s.append(f'<text x="{cx}" y="{cy+4}" text-anchor="middle" font-size="12" font-weight="bold" fill="#fff">{name}</text>')
    if sub:
        s.append(f'<text x="{cx}" y="{cy+47}" text-anchor="middle" font-size="11" fill="#555">{sub}</text>')
    s.append('</g>')
    return "".join(s)

def drumkit(cx, cy, num):
    # bateria vista de cima (sem riser)
    s=[f'<g>']
    # kick (centro)
    s.append(f'<circle cx="{cx}" cy="{cy+22}" r="26" fill="{GREY}" stroke="{INK}" stroke-width="2.5"/>')
    s.append(f'<text x="{cx}" y="{cy+26}" text-anchor="middle" font-size="10" font-weight="bold">KICK</text>')
    # snare
    s.append(f'<circle cx="{cx-34}" cy="{cy-2}" r="15" fill="#ddd" stroke="{INK}" stroke-width="2"/>')
    s.append(f'<text x="{cx-34}" y="{cy+2}" text-anchor="middle" font-size="8" font-weight="bold">SN</text>')
    # toms
    s.append(f'<circle cx="{cx-8}" cy="{cy-30}" r="13" fill="#ddd" stroke="{INK}" stroke-width="2"/>')
    s.append(f'<circle cx="{cx+22}" cy="{cy-26}" r="13" fill="#ddd" stroke="{INK}" stroke-width="2"/>')
    # cymbals
    s.append(f'<circle cx="{cx-52}" cy="{cy-34}" r="17" fill="none" stroke="{INK}" stroke-width="1.5"/>')
    s.append(f'<circle cx="{cx+50}" cy="{cy-30}" r="19" fill="none" stroke="{INK}" stroke-width="1.5"/>')
    # hi-hat
    s.append(f'<circle cx="{cx-58}" cy="{cy+8}" r="12" fill="none" stroke="{INK}" stroke-width="1.5"/>')
    s.append(f'<text x="{cx}" y="{cy+62}" text-anchor="middle" font-size="12" font-weight="bold" fill="{INK}">BATERIA</text>')
    s.append(numbadge(cx+88, cy-40, num))
    s.append('</g>')
    return "".join(s)

# ===== posicionamento por colunas =====
# 4 zonas em x
cx1 = STAGE_X + 130   # guit base
cx2 = STAGE_X + 330   # baixo
cx3 = STAGE_X + 535   # bateria/vocal
cx4 = STAGE_X + 790   # guit solo

# y de profundidade
y_back  = STAGE_Y + 70    # amps / mesa
y_mid   = STAGE_Y + 250   # músicos
y_front = STAGE_Y + 430   # mics

content=[]

# --- amps no fundo ---
content.append(amp(cx1-42, y_back, "Guitarra base", 4))
content.append(amp(cx4-42, y_back, "Guitarra solo", 6))
content.append(amp(cx2-42, y_back, "Baixo", 5))

# bateria (coluna 3, fundo)
content.append(drumkit(cx3, y_back+30, 7))

# --- músicos linha do meio ---
content.append(musician(cx1, y_mid, "GUIT.", "base + back vocal"))
content.append(musician(cx2, y_mid, "BAIXO", "+ back vocal"))
content.append(musician(cx4, y_mid, "GUIT.", "solo"))
# vocal fica mais à frente (coluna 3)
content.append(musician(cx3, y_mid+120, "VOCAL", "à frente do palco"))

# --- mics frente ---
# mic compartilhado entre base e baixo (entre cx1 e cx2)
content.append(micstand((cx1+cx2)//2, y_front, "Mic compartilhado (base+baixo)", 2))
content.append(micstand(cx3, y_front+30, "Mic vocal", 1))
content.append(micstand(cx4, y_front, "Mic guit. solo", 3))

svg.extend(content)

# PA na frente, fora do palco
pa_y = STAGE_Y+STAGE_H+8
svg.append(f'<polygon points="{STAGE_X+60},{pa_y} {STAGE_X+120},{pa_y} {STAGE_X+108},{pa_y+30} {STAGE_X+72},{pa_y+30}" fill="{ORANGE}" stroke="{INK}" stroke-width="2"/>')
svg.append(f'<text x="{STAGE_X+90}" y="{pa_y+20}" text-anchor="middle" font-size="11" font-weight="bold" fill="#fff">PA</text>')
svg.append(f'<polygon points="{STAGE_X+STAGE_W-120},{pa_y} {STAGE_X+STAGE_W-60},{pa_y} {STAGE_X+STAGE_W-72},{pa_y+30} {STAGE_X+STAGE_W-108},{pa_y+30}" fill="{ORANGE}" stroke="{INK}" stroke-width="2"/>')
svg.append(f'<text x="{STAGE_X+STAGE_W-90}" y="{pa_y+20}" text-anchor="middle" font-size="11" font-weight="bold" fill="#fff">PA</text>')

# power indicators (raio) nos cantos do fundo
for px in [STAGE_X+20, STAGE_X+STAGE_W-20]:
    py=STAGE_Y+18
    svg.append(f'<text x="{px}" y="{py+6}" text-anchor="middle" font-size="20" fill="{ORANGE}">⚡</text>')
svg.append(f'<text x="{STAGE_X+20}" y="{STAGE_Y+44}" text-anchor="middle" font-size="9" fill="#888">POWER</text>')
svg.append(f'<text x="{STAGE_X+STAGE_W-20}" y="{STAGE_Y+44}" text-anchor="middle" font-size="9" fill="#888">POWER</text>')

svg.append('</svg>')

open('assets/stageplot.svg','w').write("\n".join(svg))
print("svg ok")
