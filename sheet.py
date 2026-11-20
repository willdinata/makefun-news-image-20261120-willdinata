import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageOps

from stories import REGION_COLOURS, MAINS, BRIEFS, NUMBERS

# Output path anchored to script directory
OUT_PATH = os.path.join(os.path.dirname(__file__), 'entry.png')

WIDTH, HEIGHT = 1024, 1024

def get_font(name, size):
    paths = [
        f"/usr/share/fonts/truetype/noto/{name}",
        f"/usr/share/fonts/truetype/dejavu/{name.replace('NotoSans', 'DejaVuSans').replace('NotoSerif', 'DejaVuSerif')}"
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def draw_icon(draw, name, box, color):
    x, y, w, h = box
    cx, cy = x + w / 2, y + h / 2
    r = min(w, h) / 2 - 1.5
    
    if name == "burst":
        # Starburst / explosion lines
        for i in range(8):
            angle = i * (3.14159 / 4)
            import math
            x1 = cx + math.cos(angle) * (r * 0.3)
            y1 = cy + math.sin(angle) * (r * 0.3)
            x2 = cx + math.cos(angle) * r
            y2 = cy + math.sin(angle) * r
            draw.line([(x1, y1), (x2, y2)], fill=color, width=1)
        draw.ellipse([cx-2, cy-2, cx+2, cy+2], fill=color)
        
    elif name == "cyclone":
        # Spiral arcs
        for r_step in [r * 0.3, r * 0.6, r * 0.9]:
            draw.arc([cx-r_step, cy-r_step, cx+r_step, cy+r_step], start=0, end=270, fill=color, width=1)
            
    elif name == "chart":
        # Bar chart / graph axes
        bx, by, bw, bh = x + 2, y + 2, w - 4, h - 4
        draw.line([(bx, by + bh), (bx + bw, by + bh)], fill=color, width=1)
        draw.line([(bx, by), (bx, by + bh)], fill=color, width=1)
        bar_w = bw / 4
        bars = [0.4, 0.7, 0.9, 0.6]
        for i, val in enumerate(bars):
            bh_i = bh * val
            bx_i = bx + 2 + i * (bar_w + 0.5)
            draw.rectangle([bx_i, by + bh - bh_i, bx_i + bar_w - 0.5, by + bh], fill=color)
            
    elif name == "sign":
        # Placard / sign on post
        draw.rectangle([cx - r*0.7, cy - r*0.8, cx + r*0.7, cy + r*0.1], outline=color, width=1)
        draw.line([(cx, cy + r*0.1), (cx, cy + r*0.9)], fill=color, width=1)
        draw.line([(cx - r*0.4, cy + r*0.9), (cx + r*0.4, cy + r*0.9)], fill=color, width=1)
        
    elif name == "chip":
        # Microchip square with pins
        sz = r * 1.1
        draw.rectangle([cx - sz/2, cy - sz/2, cx + sz/2, cy + sz/2], outline=color, width=1)
        pin_len = 2
        for i in [-0.5, 0, 0.5]:
            py = cy + i * (sz * 0.6)
            draw.line([(cx - sz/2 - pin_len, py), (cx - sz/2, py)], fill=color, width=1)
            draw.line([(cx + sz/2, py), (cx + sz/2 + pin_len, py)], fill=color, width=1)
            px = cx + i * (sz * 0.6)
            draw.line([(px, cy - sz/2 - pin_len), (px, cy - sz/2)], fill=color, width=1)
            draw.line([(px, cy + sz/2), (px, cy + sz/2 + pin_len)], fill=color, width=1)
            
    elif name == "shield":
        # Shield outline
        sx, sy, sw, sh = x + 2, y + 2, w - 4, h - 4
        points = [
            (sx, sy),
            (sx + sw, sy),
            (sx + sw, sy + sh * 0.5),
            (sx + sw / 2, sy + sh),
            (sx, sy + sh * 0.5)
        ]
        draw.polygon(points, outline=color)
        
    elif name == "boat":
        # Hull and sail
        bx, by = x + 2, y + h * 0.65
        bw = w - 4
        draw.arc([bx, by - 4, bx + bw, by + 8], start=0, end=180, fill=color, width=1)
        draw.line([(cx, by), (cx, y + 2)], fill=color, width=1)
        draw.polygon([(cx, y + 2), (cx, y + h * 0.55), (cx + bw * 0.35, y + h * 0.4)], fill=color)
        
    elif name == "ballot":
        # Ballot box with slot
        bx, by, bw, bh = x + 2, y + 2, w - 4, h - 4
        draw.rectangle([bx, by + bh*0.3, bx + bw, by + bh], outline=color, width=1)
        draw.line([(bx + bw*0.3, by + bh*0.3), (bx + bw*0.7, by + bh*0.3)], fill=color, width=1)
        draw.rectangle([bx + bw*0.35, by, bx + bw*0.65, by + bh*0.4], outline=color, fill=(255,255,255), width=1)
        
    elif name == "flag":
        # Flag on pole
        draw.line([(x + 3, y + 2), (x + 3, y + h - 2)], fill=color, width=1)
        draw.polygon([(x + 3, y + 2), (x + w - 2, y + h * 0.3), (x + 3, y + h * 0.6)], fill=color)
        
    elif name == "leaf":
        # Leaf with stem and vein
        sx, sy = x + 2, y + 2
        sw, sh = w - 4, h - 4
        draw.arc([sx, sy, sx + sw, sy + sh], start=30, end=210, fill=color, width=1)
        draw.arc([sx, sy, sx + sw, sy + sh], start=210, end=30, fill=color, width=1)
        draw.line([(sx + sw*0.2, sy + sh*0.8), (sx + sw*0.8, sy + sh*0.2)], fill=color, width=1)
        
    elif name == "globe":
        # Globe circle with meridians
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=1)
        draw.arc([cx - r, cy - r, cx + r, cy + r], start=-60, end=60, fill=color, width=1)
        draw.arc([cx - r, cy - r, cx + r, cy + r], start=120, end=240, fill=color, width=1)
        draw.line([(cx, cy - r), (cx, cy + r)], fill=color, width=1)
        draw.line([(cx - r, cy), (cx + r, cy)], fill=color, width=1)
        
    elif name == "coin":
        # Coin with inner ring
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=1)
        draw.ellipse([cx - r*0.6, cy - r*0.6, cx + r*0.6, cy + r*0.6], outline=color, width=1)
        
    else:
        draw.rectangle([cx - r/2, cy - r/2, cx + r/2, cy + r/2], outline=color, width=1)

def wrap_text(text, font, max_width, draw):
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        test_line = " ".join(current_line + [word])
        w = draw.textlength(test_line, font=font)
        if w <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
                current_line = [word]
            else:
                lines.append(word)
                current_line = []
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def draw_pill(draw, x, y, label, icon_name, region_color, font, icon_box_size=14, pad_left=4, gap=6, pad_right=7):
    text_w = draw.textlength(label, font=font)
    text_x = x + pad_left + icon_box_size + gap
    pill_w = text_x - x + text_w + pad_right
    pill_h = 22
    
    try:
        draw.rounded_rectangle([x, y, x + pill_w, y + pill_h], radius=4, fill=region_color)
    except AttributeError:
        draw.rectangle([x, y, x + pill_w, y + pill_h], fill=region_color)
        
    icon_box = (x + pad_left, y + (pill_h - icon_box_size) // 2, icon_box_size, icon_box_size)
    draw_icon(draw, icon_name, icon_box, (255, 255, 255))
    
    text_y = y + (pill_h - 12) // 2 - 1
    draw.text((text_x, text_y), label, fill=(255, 255, 255), font=font)
    
    return x + pill_w

def main():
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#FAF8F5")
    draw = ImageDraw.Draw(img)
    
    # Fonts
    font_serif_lg = get_font("NotoSerif-Bold.ttf", 46)
    font_serif_md = get_font("NotoSerif-Bold.ttf", 24)
    font_sans_bold = get_font("NotoSans-Bold.ttf", 12)
    font_sans_bold_14 = get_font("NotoSans-Bold.ttf", 14)
    font_sans_reg_10 = get_font("NotoSans-Regular.ttf", 10)
    
    # ----------------------------------------------------
    # 1. MASTHEAD (Budget: ~92px)
    # ----------------------------------------------------
    title_text = "THE MERIDIAN"
    title_w = draw.textlength(title_text, font=font_serif_lg)
    draw.text(((WIDTH - title_w) / 2, 8), title_text, fill="#1A1A1A", font=font_serif_lg)
    
    draw.line([(40, 64), (WIDTH - 40, 64)], fill="#1A1A1A", width=2)
    draw.line([(40, 68), (WIDTH - 40, 68)], fill="#1A1A1A", width=1)
    
    strapline_y = 72
    draw.text((40, strapline_y), "THE WORLD IN ONE DAY", fill="#1A1A1A", font=font_sans_bold)
    date_text = "FRIDAY 20 NOVEMBER 2026"
    date_w = draw.textlength(date_text, font=font_sans_bold)
    draw.text(((WIDTH - date_w) / 2, strapline_y), date_text, fill="#1A1A1A", font=font_sans_bold)
    right_strap = "ONE DAY · ONE PAGE"
    right_w = draw.textlength(right_strap, font=font_sans_bold)
    draw.text((WIDTH - 40 - right_w, strapline_y), right_strap, fill="#1A1A1A", font=font_sans_bold)
    
    draw.line([(40, 91), (WIDTH - 40, 91)], fill="#1A1A1A", width=1)
    
    # ----------------------------------------------------
    # 2. BREAKING NEWS STRIP (Budget: ~36px, y: 92 to 128)
    # ----------------------------------------------------
    draw.rectangle([40, 92, WIDTH - 40, 128], fill="#C8102E")
    breaking_text = "BREAKING — RUSSIA FIRES 110+ MISSILES AND 400 DRONES AT UKRAINE HOURS AFTER THE SHENZHEN PEACE SUMMIT."
    break_font = get_font("NotoSans-Bold.ttf", 13)
    bw_len = draw.textlength(breaking_text, font=break_font)
    draw.text(((WIDTH - bw_len) / 2, 102), breaking_text, fill="#FFFFFF", font=break_font)
    
    # ----------------------------------------------------
    # 3. LEAD PANEL (Budget: ~130px, y: 130 to 260)
    # ----------------------------------------------------
    lead_y = 130
    lead_h = 130
    draw.rectangle([40, lead_y, WIDTH - 40, lead_y + lead_h], outline="#D3D0C7", fill="#F4F1EA", width=1)
    
    art_x, art_y, art_w, art_h = 50, lead_y + 10, 160, lead_h - 20
    for dy in range(int(art_h)):
        r_c = int(15 + (30 - 15) * (dy / art_h))
        g_c = int(23 + (41 - 23) * (dy / art_h))
        b_c = int(42 + (59 - 42) * (dy / art_h))
        draw.line([(art_x, art_y + dy), (art_x + art_w, art_y + dy)], fill=(r_c, g_c, b_c))
    
    silhouette_pts = [
        (art_x, art_y + art_h),
        (art_x, art_y + art_h - 20),
        (art_x + 20, art_y + art_h - 20),
        (art_x + 20, art_y + art_h - 40),
        (art_x + 45, art_y + art_h - 40),
        (art_x + 45, art_y + art_h - 25),
        (art_x + 70, art_y + art_h - 25),
        (art_x + 70, art_y + art_h - 55),
        (art_x + 95, art_y + art_h - 55),
        (art_x + 95, art_y + art_h - 30),
        (art_x + art_w, art_y + art_h - 30),
        (art_x + art_w, art_y + art_h)
    ]
    draw.polygon(silhouette_pts, fill="#0A0F1D")
    
    s1 = MAINS[0]
    reg_color = REGION_COLOURS.get("EUROPE", (20, 50, 90))
    pill_end_x = draw_pill(draw, 220, lead_y + 12, s1["label"], s1["icon"], reg_color, font_sans_bold, icon_box_size=14, pad_left=4, gap=6, pad_right=7)
    
    draw.ellipse([pill_end_x + 12, lead_y + 12, pill_end_x + 34, lead_y + 34], fill="#1A1A1A")
    draw.text((pill_end_x + 17, lead_y + 14), str(s1["n"]), fill="#FFFFFF", font=font_sans_bold)
    
    head_font = get_font("NotoSans-Bold.ttf", 18)
    head_lines = wrap_text(s1["head"], head_font, WIDTH - 220 - 70, draw)
    hy = lead_y + 42
    for line in head_lines[:2]:
        draw.text((220, hy), line, fill="#1A1A1A", font=head_font)
        hy += 22
        
    desc_font = get_font("NotoSans-Regular.ttf", 12)
    desc_lines = wrap_text(s1["desc"], desc_font, WIDTH - 220 - 60, draw)
    dy = hy + 4
    for line in desc_lines[:3]:
        draw.text((220, dy), line, fill="#333333", font=desc_font)
        dy += 16
        
    # ----------------------------------------------------
    # 4. GRID OF 12 TILES (Budget: ~300px, y: 265 to 565)
    # ----------------------------------------------------
    grid_y = 265
    row_h = 100
    col_w = (WIDTH - 80 - 3 * 12) / 4
    
    story_idx = 1
    for row in range(3):
        for col in range(4):
            if story_idx >= len(MAINS): break
            s = MAINS[story_idx]
            story_idx += 1
            tx = 40 + col * (col_w + 12)
            ty = grid_y + row * row_h
            draw.rectangle([tx, ty, tx + col_w, ty + row_h - 6], outline="#D3D0C7", fill="#FAF8F5", width=1)
            
            reg_c = REGION_COLOURS.get(s["label"].split("·")[0].strip(), (60, 70, 80))
            draw.ellipse([tx + 6, ty + 6, tx + 20, ty + 20], fill="#1A1A1A")
            draw.text((tx + 9, ty + 7), str(s["n"]), fill="#FFFFFF", font=get_font("NotoSans-Bold.ttf", 10))
            draw_pill(draw, tx + 24, ty + 5, s["label"], s["icon"], reg_c, get_font("NotoSans-Bold.ttf", 10), icon_box_size=14, pad_left=4, gap=6, pad_right=7)
            
            t_head_size = 11
            while True:
                t_head_font = get_font("NotoSans-Bold.ttf", t_head_size)
                head_lines = wrap_text(s["head"], t_head_font, col_w - 12, draw)
                if len(head_lines) <= 2 or t_head_size <= 9: break
                t_head_size -= 1
            
            thy = ty + 28
            for line in head_lines[:2]:
                draw.text((tx + 6, thy), line, fill="#1A1A1A", font=t_head_font)
                thy += t_head_size + 2
                
            t_desc_size = 10
            while True:
                t_desc_font = get_font("NotoSans-Regular.ttf", t_desc_size)
                desc_lines = wrap_text(s["desc"], t_desc_font, col_w - 12, draw)
                if len(desc_lines) <= 3 or t_desc_size <= 9: break
                t_desc_size -= 1
            
            if len(desc_lines) > 3:
                desc_lines = desc_lines[:3]
                line3 = desc_lines[2]
                while draw.textlength(line3 + "…", font=t_desc_font) > (col_w - 12) and len(line3) > 0:
                    line3 = line3.rsplit(' ', 1)[0] if ' ' in line3 else line3[:-1]
                desc_lines[2] = line3.rstrip() + "…"
            
            tdy = thy + 2
            for line in desc_lines[:3]:
                if tdy + t_desc_size < ty + row_h - 8:
                    draw.text((tx + 6, tdy), line, fill="#444444", font=t_desc_font)
                    tdy += t_desc_size + 2

    # ----------------------------------------------------
    # 5. MAP BAND (Budget: ~100px, y: 570 to 670)
    # ----------------------------------------------------
    map_y = 570
    map_h = 100
    draw.rectangle([40, map_y, WIDTH - 40, map_y + map_h], outline="#D3D0C7", fill="#F4F1EA", width=1)
    draw.text((55, map_y + 4), "WHERE IT HAPPENED", fill="#1A1A1A", font=get_font("NotoSerif-Bold.ttf", 20))
    
    mx_start, my_start, mw, mh = 45, map_y + 16, WIDTH - 90, 72
    WORLD_MAP = [
        "...............................................................................................",
        "...#####...###........................................###############..........................",
        "..#######.#####.....................................###################........................",
        "..#########....###................................#####################........................",
        "...#######..#######.............................#########################......................",
        "....#####.#########.............................##########################.....................",
        ".....###.###########.............................########################......................",
        "      #.###########..............................########################......................",
        "        #########.................................#####################........................",
        "         #######....................................###################........................",
        "          #####.......................................###############..........................",
        "            ##.........###.............................###########.............................",
        "                         #######.............................#######...............................",
        "                       #########..................................................................-",
        "                      ###########......................########....................................",
        "                      ###########....................############..................................",
        "                       #########...................##############..................................",
        "                        #######...................###############..................................",
        "                         #####....................###############..................................",
        "                          ###......................#############..................................",
        "                                                   #############..................................",
        "                                                    ###########....................................",
        "                                                     #########..................#####..............",
        "                                                       #####...................#######.............",
        "                                                                                #####..............",
        "...............................................................................................",
    ]
    num_rows = len(WORLD_MAP)
    num_cols = max(len(r) for r in WORLD_MAP)
    for r, r_str in enumerate(WORLD_MAP):
        for c, ch in enumerate(r_str):
            if ch == '#':
                dot_x = mx_start + (c / (num_cols - 1)) * mw
                dot_y = my_start + (r / (num_rows - 1)) * mh
                draw.ellipse([dot_x - 1.5, dot_y - 1.5, dot_x + 1.5, dot_y + 1.5], fill="#B0ACA1")
    
    for s in MAINS:
        px = mx_start + ((s["lon"] + 180) / 360) * mw
        py = my_start + ((90 - s["lat"]) / 180) * mh
        reg_c = REGION_COLOURS.get(s["label"].split("·")[0].strip(), (200, 30, 30))
        draw.ellipse([px - 5, py - 5, px + 5, py + 5], fill=reg_c, outline="#FFFFFF", width=1)
        draw.text((px - 3, py - 5), str(s["n"]), fill="#FFFFFF", font=font_sans_reg_10)

    # ----------------------------------------------------
    # 6. NUMBERS BAND (Budget: ~54px, y: 675 to 729)
    # ----------------------------------------------------
    num_y = 675
    num_h = 54
    draw.rectangle([40, num_y, WIDTH - 40, num_y + num_h], outline="#D3D0C7", fill="#FAF8F5", width=1)
    draw.text((55, num_y + 4), "THE DAY IN NUMBERS", fill="#1A1A1A", font=font_sans_bold)
    
    cell_w_num = (WIDTH - 80) / 6
    for i, (val, caption) in enumerate(NUMBERS):
        cx = 40 + i * cell_w_num
        if i > 0: draw.line([(cx, num_y + 20), (cx, num_y + num_h - 4)], fill="#D3D0C7", width=1)
        val_font = get_font("NotoSans-Bold.ttf", 16)
        vw = draw.textlength(val, font=val_font)
        draw.text((cx + (cell_w_num - vw) / 2, num_y + 20), val, fill="#C8102E", font=val_font)
        cap_font = get_font("NotoSans-Regular.ttf", 8)
        cap_lines = wrap_text(caption, cap_font, cell_w_num - 10, draw)
        cy_text = num_y + 38
        for line in cap_lines[:1]:
            lw = draw.textlength(line, font=cap_font)
            draw.text((cx + (cell_w_num - lw) / 2, cy_text), line, fill="#333333", font=cap_font)

    # ----------------------------------------------------
    # 7. BRIEFS SECTION (Budget: ~243px, y: 735 to 978)
    # ----------------------------------------------------
    briefs_y = 735
    briefs_h = 243
    draw.rectangle([40, briefs_y, WIDTH - 40, briefs_y + briefs_h], outline="#D3D0C7", fill="#F4F1EA", width=1)
    draw.text((55, briefs_y + 6), "WORLD BRIEFS", fill="#1A1A1A", font=font_serif_md)
    
    col_width = (WIDTH - 100) / 2
    row_pitch = 21
    brief_font = get_font("NotoSans-Regular.ttf", 10)
    
    for i, b in enumerate(BRIEFS):
        col = i // 10
        row = i % 10
        bx = 50 + col * (col_width + 10)
        by = briefs_y + 32 + row * row_pitch
        
        draw.text((bx, by + 4), f"{b['n']}.", fill="#1A1A1A", font=get_font("NotoSans-Bold.ttf", 10))
        reg_c = REGION_COLOURS.get(b["label"].split("·")[0].strip(), (60, 70, 80))
        icon_name = b["label"].split("·")[0].strip()[:3].lower()
        if icon_name not in ["bur","cyc","cha","sig","chi","shi","boa","bal","fla","lea","glo","coi"]: icon_name = "flag"
        pill_end = draw_pill(draw, bx + 22, by, b["label"], icon_name, reg_c, font_sans_reg_10, icon_box_size=14, pad_left=4, gap=6, pad_right=7)
        
        max_w = col_width - (pill_end - bx) - 10
        h_lines = wrap_text(b["head"], brief_font, max_w, draw)
        hy = by + 2
        for line in h_lines[:2]:
            draw.text((pill_end + 6, hy), line, fill="#1A1A1A", font=brief_font)
            hy += 11
            
    # ----------------------------------------------------
    # 8. FOOTER (Budget: ~23px, y: 982 to 1008)
    # ----------------------------------------------------
    footer_y = 998
    draw.line([(40, footer_y), (WIDTH - 40, footer_y)], fill="#1A1A1A", width=1)
    sources_text = "Sources: Reuters · AP · BBC · CNN · France 24 · The Hindu · IMD · Sensor Tower — page drawn by an AI agent."
    src_font = get_font("NotoSans-Regular.ttf", 9)
    sw = draw.textlength(sources_text, font=src_font)
    draw.text(((WIDTH - sw) / 2, footer_y + 5), sources_text, fill="#555555", font=src_font)
    
    img.save(OUT_PATH, "PNG", optimize=True)
    size_bytes = os.path.getsize(OUT_PATH)
    print(f"Saved {OUT_PATH} successfully!")
    print(f"Dimensions: {img.size[0]}x{img.size[1]} px")
    print(f"File size: {size_bytes} bytes")    
    if size_bytes > 1024 * 1024:
        print("Warning: PNG exceeds 1 MiB. Quantising...")
        img_q = img.quantize(colors=256)
        img_q.save(OUT_PATH, "PNG", optimize=True)
        size_bytes = os.path.getsize(OUT_PATH)
        print(f"Quantised file size: {size_bytes} bytes ({size_bytes / 1024 / 1024:.2f} MiB)")

if __name__ == "__main__":
    main()
