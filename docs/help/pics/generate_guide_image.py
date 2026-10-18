import math
from PIL import Image, ImageDraw, ImageFont

def generate_perfect_guide_image():
    # キャンバスサイズ: 920 x 500
    canvas_w, canvas_h = 920, 500
    canvas = Image.new('RGB', (canvas_w, canvas_h), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)
    
    # 清潔感のある微細スレート背景 + 境界線
    draw.rectangle([(0, 0), (canvas_w - 1, canvas_h - 1)], fill=(248, 250, 252), outline=(226, 232, 240), width=2)
    
    font_bold = 'C:/Windows/Fonts/meiryob.ttc'
    font_reg = 'C:/Windows/Fonts/meiryo.ttc'
    
    # フォントサイズを倍増！（超大型・高視認性）
    f_step_num = ImageFont.truetype(font_bold, 24)
    f_step_text = ImageFont.truetype(font_bold, 25)
    f_arrow = ImageFont.truetype(font_bold, 24)
    f_badge = ImageFont.truetype(font_bold, 16)
    f_folder = ImageFont.truetype(font_bold, 16)
    f_note = ImageFont.truetype(font_bold, 13)
    
    # ----------------------------------------------------
    # 1. 上部ミニマル案内ヘッダー (y: 10〜65)
    # ----------------------------------------------------
    draw.rounded_rectangle([(12, 10), (canvas_w - 12, 65)], radius=10, fill=(241, 245, 249), outline=(203, 213, 225), width=1)
    
    # ステップ1 (特大丸バッジ 直径38px)
    draw.ellipse([(22, 18), (60, 56)], fill=(37, 99, 235))
    draw.text((33, 20), '1', font=f_step_num, fill=(255, 255, 255))
    draw.text((70, 20), '解凍したフォルダ', font=f_step_text, fill=(30, 41, 59))
    
    # 矢印
    draw.text((300, 19), '➜', font=f_arrow, fill=(148, 163, 184))
    
    # ステップ2 (特大丸バッジ 直径38px)
    draw.ellipse([(345, 18), (383, 56)], fill=(16, 185, 129))
    draw.text((356, 20), '2', font=f_step_num, fill=(255, 255, 255))
    draw.text((393, 20), '上の細い黄色「検索対象」枠へドロップ！', font=f_step_text, fill=(15, 23, 42))
    
    # ----------------------------------------------------
    # 2. ツール画面クローズアップ (01_basic.png)
    # 下約2cmカット (y=0〜475), 右約2cmカット (x=0〜815)
    # ----------------------------------------------------
    im = Image.open('docs/help/pics/01_basic.png')
    app_c = im.crop((0, 0, 815, 475))
    
    app_dest_x = 195
    app_dest_y = 72
    target_app_h = canvas_h - app_dest_y - 10 # 418
    scale = target_app_h / app_c.height # 418 / 475 = 0.880
    target_app_w = int(app_c.width * scale) # 815 * 0.880 = 717
    
    app_resized = app_c.resize((target_app_w, target_app_h), Image.Resampling.LANCZOS)
    canvas.paste(app_resized, (app_dest_x, app_dest_y))
    draw.rectangle([(app_dest_x, app_dest_y), (app_dest_x + target_app_w - 1, app_dest_y + target_app_h - 1)], outline=(203, 213, 225), width=2)
    
    # ----------------------------------------------------
    # 3. 「上の細い方の黄色（検索対象）」のピンポイント赤枠ハイライト
    # ----------------------------------------------------
    hl_x1 = int(app_dest_x + 73 * scale)
    hl_y1 = int(app_dest_y + 65 * scale)
    hl_x2 = int(app_dest_x + 810 * scale)
    hl_y2 = int(app_dest_y + 108 * scale)
    
    # 太い赤枠（太さ4px）
    draw.rounded_rectangle([(hl_x1 - 3, hl_y1 - 3), (hl_x2 + 3, hl_y2 + 3)], radius=6, outline=(239, 68, 68), width=4)
    
    # 「★ ここへドロップ！」吹き出しバッジ
    badge_w = 175
    badge_h = 32
    badge_x = int(app_dest_x + 500 * scale)
    badge_y = hl_y1 + (hl_y2 - hl_y1 - badge_h) // 2
    draw.rounded_rectangle([(badge_x, badge_y), (badge_x + badge_w, badge_y + badge_h)], radius=16, fill=(239, 68, 68))
    draw.text((badge_x + 14, badge_y + 4), '★ ここへドロップ！', font=f_badge, fill=(255, 255, 255))
    
    # ----------------------------------------------------
    # 4. 左側：解凍フォルダアイコン
    # ----------------------------------------------------
    fld_x, fld_y = 18, 160
    # フォルダ本体
    draw.rounded_rectangle([(fld_x, fld_y - 14), (fld_x + 55, fld_y + 15)], radius=6, fill=(217, 119, 6))
    draw.rounded_rectangle([(fld_x, fld_y), (fld_x + 145, fld_y + 110)], radius=10, fill=(245, 158, 11), outline=(217, 119, 6), width=3)
    # Excel書類
    draw.rounded_rectangle([(fld_x + 30, fld_y - 8), (fld_x + 115, fld_y + 50)], radius=5, fill=(255, 255, 255), outline=(16, 185, 129), width=2)
    draw.text((fld_x + 44, fld_y + 8), 'Excel', font=ImageFont.truetype(font_bold, 17), fill=(5, 150, 105))
    # フォルダ前カバー
    draw.polygon([(fld_x, fld_y + 34), (fld_x + 145, fld_y + 34), (fld_x + 130, fld_y + 110), (fld_x - 5, fld_y + 110)], fill=(251, 191, 36))
    
    # テキスト
    draw.text((fld_x + 14, fld_y + 120), '解凍したフォルダ', font=f_folder, fill=(180, 83, 9))
    draw.text((fld_x + 14, fld_y + 145), '(200ファイルなど)', font=f_note, fill=(100, 116, 139))
    
    # ----------------------------------------------------
    # 5. ドロップ曲線矢印
    # ----------------------------------------------------
    start_pt = (fld_x + 145, fld_y + 35)
    end_pt = (badge_x - 15, hl_y1 + (hl_y2 - hl_y1) // 2)
    
    points = []
    for t in [i / 40.0 for i in range(41)]:
        cp_x = (start_pt[0] + end_pt[0]) // 2 - 25
        cp_y = min(start_pt[1], end_pt[1]) - 45
        x = (1 - t) ** 2 * start_pt[0] + 2 * (1 - t) * t * cp_x + t ** 2 * end_pt[0]
        y = (1 - t) ** 2 * start_pt[1] + 2 * (1 - t) * t * cp_y + t ** 2 * end_pt[1]
        points.append((x, y))
        
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill=(37, 99, 235), width=6)
        
    tip = points[-1]
    prev = points[-4]
    dx = tip[0] - prev[0]
    dy = tip[1] - prev[1]
    angle = math.atan2(dy, dx)
    arrow_len = 22
    arrow_angle = math.pi / 6
    p1 = (tip[0] - arrow_len * math.cos(angle - arrow_angle), tip[1] - arrow_len * math.sin(angle - arrow_angle))
    p2 = (tip[0] - arrow_len * math.cos(angle + arrow_angle), tip[1] - arrow_len * math.sin(angle + arrow_angle))
    draw.polygon([tip, p1, p2], fill=(37, 99, 235))
    
    # マウスカーソル
    cur_x, cur_y = int(tip[0] + 6), int(tip[1] + 2)
    draw.polygon([(cur_x, cur_y), (cur_x, cur_y + 24), (cur_x + 8, cur_y + 18), (cur_x + 15, cur_y + 30), (cur_x + 20, cur_y + 27), (cur_x + 14, cur_y + 15), (cur_x + 22, cur_y + 15)], fill=(255, 255, 255), outline=(15, 23, 42))
    
    # 保存
    canvas.save('docs/help/pics/drag_drop_flow.jpg', 'JPEG', quality=95)
    print('drag_drop_flow.jpg regenerated with 2x bigger text')

if __name__ == '__main__':
    generate_perfect_guide_image()
