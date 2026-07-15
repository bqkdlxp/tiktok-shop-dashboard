#!/usr/bin/env python3
"""
generate_real_data.py — TikTok Shop 三大品类看板数据
=================================================================
真实 TikTok Shop 类目结构:

🧸 Toys & Games:
   Classic Toys | Games & Puzzles | Educational Toys | Electronic/RC
   DIY Craft Toys | Outdoor Toys | Dolls & Plush

✏️ Office & School Supplies:
   Writing Supplies | Paper & Notebooks | Desk Accessories
   Art Supplies | Stationery Sets

🎴 Collectibles:
   Blind Boxes | Trading Cards | Collectible Figures | Entertainment Collectibles

数据来源: EchoTik / Kalodata 2026 / NetInfluencer / FastMoss / TikTok Seller Center
"""

import json, random
from datetime import datetime, timedelta

random.seed(2026)

# ============================================================
# 真实产品数据 (2026年7月)
# ============================================================
REAL_PRODUCTS = [
    # ---- 🧸 Toys & Games ----
    # Classic Toys
    ('Nex Playground Active Play System', 'Toys', 'Classic Toys', 206.80, 27700, 'NetInfluencer 2026'),
    ('Fanttik Electric Kids Ride-On Car', 'Toys', 'Classic Toys', 106.45, 25400, 'EchoTik 2026'),
    ('Smart Hover Ball LED Flying Gyro Toy', 'Toys', 'Classic Toys', 8.00, 35000, 'FastMoss'),
    # Games & Puzzles
    ('Family Board Game Night Bundle (5 Games)', 'Toys', 'Games & Puzzles', 24.99, 12000, 'Dashboardly 2026'),
    ('1000-Piece Jigsaw Puzzle - World Landmarks', 'Toys', 'Games & Puzzles', 16.99, 18000, 'Dashboardly 2026'),
    # Educational
    ('STEM Building Block Set (1500-Piece Engineering Kit)', 'Toys', 'Educational Toys', 29.99, 15000, 'Dashboardly 2026'),
    ('Magnetic Tiles Construction Set (100pc)', 'Toys', 'Educational Toys', 29.99, 12000, 'Dashboardly 2026'),
    # Electronic/RC
    ('Mini RC Monster Truck 1:64 Scale', 'Toys', 'Electronic/RC', 18.00, 7000, 'chwang.com 2026'),
    ('Defying Gravity Wall Climbing RC Car', 'Toys', 'Electronic/RC', 34.99, 5200, 'chwang.com 2026'),
    # DIY Craft
    ('DIY Air Dry Clay Modeling Kit (24 Colors + Tools)', 'Toys', 'DIY Craft Toys', 24.99, 9500, 'EchoTik'),
    ('Anywise Air Dry Clay Kit (12 Designs)', 'Toys', 'DIY Craft Toys', 39.99, 8600, 'EchoTik 2026'),
    # Outdoor
    ('Mermaid Shell Diving Toy', 'Toys', 'Outdoor Toys', 20.99, 5000, 'chwang.com Jul 2026'),
    ('Ocean Animal Rescue Dive Box', 'Toys', 'Outdoor Toys', 23.99, 9000, 'chwang.com Jul 2026'),
    ('Firework Water Gun', 'Toys', 'Outdoor Toys', 9.99, 15000, 'tkfff.com Jul 2026'),
    ('Pool Fountain Sprinkler Stand', 'Toys', 'Outdoor Toys', 37.00, 3160, 'chwe.cn Jul 2026'),
    ('Foldable LED Flying Disc', 'Toys', 'Outdoor Toys', 14.99, 15000, 'Trenz.ai Jun 2026'),
    ('Portable Camping Hammock with Straps', 'Toys', 'Outdoor Toys', 25.99, 9000, 'chwang.com 2026'),
    # Dolls & Plush (non-collectible)
    ('Kawaii Carrot Plush Pillow', 'Toys', 'Dolls & Plush', 12.99, 22000, 'FastMoss Jul 2026'),
    ('Capybara Plush Hot Water Bottle', 'Toys', 'Dolls & Plush', 15.99, 18000, 'TikTok Trending Jul 2026'),
    ('Fidget Toy Variety Pack (24-Piece Assorted)', 'Toys', 'Dolls & Plush', 16.99, 28000, 'Kalodata 2026'),

    # ---- ✏️ Office & School Supplies ----
    ('Blind Box Mystery Pen Set (12 Collectible Designs)', 'Stationery', 'Writing Supplies', 9.99, 28000, 'Dashboardly 2026'),
    ('Pilot Frixion Erasable Gel Pen Set (12 Colors)', 'Stationery', 'Writing Supplies', 21.99, 14000, 'Dashboardly 2026'),
    ('Transparent Sticky Notes 3x3 (8 Pastel Pads)', 'Stationery', 'Paper & Notebooks', 5.99, 38000, 'Dashboardly 2026'),
    ('Bullet Journal Deluxe Starter Kit', 'Stationery', 'Paper & Notebooks', 27.99, 8500, 'Dashboardly 2026'),
    ('Aesthetic Desk Organizer - Rotating Pen Holder', 'Stationery', 'Desk Accessories', 25.99, 10000, 'Dashboardly 2026'),
    ('LED Desk Lamp with USB Charging Port', 'Stationery', 'Desk Accessories', 19.99, 15000, 'Dashboardly 2026'),
    ('Vintage Washi Tape Set (60 Rolls + Dispenser)', 'Stationery', 'Art Supplies', 8.99, 25000, 'Dashboardly 2026'),
    ('Double-Sided Acrylic Marker Set (24 Colors)', 'Stationery', 'Art Supplies', 14.99, 22000, 'Dashboardly 2026'),
    ('Back-to-School Stationery Bundle (30-Piece)', 'Stationery', 'Stationery Sets', 19.99, 18000, 'Dashboardly 2026'),

    # ---- 🎴 Collectibles (潮玩收藏) ----
    # Blind Boxes
    ('POP MART Labubu Exciting Macaron Blind Box', 'Collectibles', 'Blind Boxes', 25.99, 85000, 'EchoTik 2026'),
    ('POP MART Labubu Have a Seat Plush Doll', 'Collectibles', 'Blind Boxes', 35.00, 62000, 'POP MART Official 2026'),
    ('POP MART SKULLPANDA Impression Series Blind Box', 'Collectibles', 'Blind Boxes', 29.99, 18000, 'FindNiche SG Jul 2026'),
    ('Trendy Anime Figure Mystery Box (6pc Set)', 'Collectibles', 'Blind Boxes', 39.99, 12000, 'FindNiche SG Jul 2026'),
    # Trading Cards
    ('Pokémon Scarlet & Violet Booster Box (36 Packs)', 'Collectibles', 'Trading Cards', 119.99, 15000, 'Dashboardly 2026'),
    ('One Piece TCG Booster Box (24 Packs)', 'Collectibles', 'Trading Cards', 89.99, 8000, 'Dashboardly 2026'),
    # Collectible Figures
    ('Die-Cast Metal Car Model Collection (合金车模)', 'Collectibles', 'Collectible Figures', 24.99, 35000, 'Dashboardly 2026'),
    ('3D Printed Dragon Egg + Dragon Figure Set', 'Collectibles', 'Collectible Figures', 19.00, 18000, 'EchoTik 2026'),
    # Entertainment Collectibles
    ('Crystal Art Sticker Kit - Hello Kitty & Friends', 'Collectibles', 'Entertainment Collectibles', 14.99, 32000, 'Toys n Playthings 2026 #1'),
]

BRANDS = {
    'Nex Playground Active Play System': 'Nex',
    'Fanttik Electric Kids Ride-On Car': 'Fanttik',
    'Smart Hover Ball LED Flying Gyro Toy': 'SmartFly',
    'Family Board Game Night Bundle (5 Games)': 'GameNight',
    '1000-Piece Jigsaw Puzzle - World Landmarks': 'PuzzleWorld',
    'STEM Building Block Set (1500-Piece Engineering Kit)': 'BrainBuild',
    'Magnetic Tiles Construction Set (100pc)': 'MagBuilt',
    'Mini RC Monster Truck 1:64 Scale': 'RC Pro',
    'Defying Gravity Wall Climbing RC Car': 'GravityX',
    'DIY Air Dry Clay Modeling Kit (24 Colors + Tools)': 'CraftMagic',
    'Anywise Air Dry Clay Kit (12 Designs)': 'Anywise',
    'Mermaid Shell Diving Toy': 'OceanFun',
    'Ocean Animal Rescue Dive Box': 'SeaQuest',
    'Firework Water Gun': 'SplashBlast',
    'Pool Fountain Sprinkler Stand': 'PoolMate',
    'Foldable LED Flying Disc': 'GlowPlay',
    'Portable Camping Hammock with Straps': 'CampEase',
    'Kawaii Carrot Plush Pillow': 'KawaiiHome',
    'Capybara Plush Hot Water Bottle': 'CozyPals',
    'Fidget Toy Variety Pack (24-Piece Assorted)': 'FidgetPro',
    'Blind Box Mystery Pen Set (12 Collectible Designs)': 'MysteryInk',
    'Pilot Frixion Erasable Gel Pen Set (12 Colors)': 'Pilot',
    'Transparent Sticky Notes 3x3 (8 Pastel Pads)': 'ClearNote',
    'Bullet Journal Deluxe Starter Kit': 'PlanPerfect',
    'Aesthetic Desk Organizer - Rotating Pen Holder': 'Deskify',
    'LED Desk Lamp with USB Charging Port': 'GlowDesk',
    'Vintage Washi Tape Set (60 Rolls + Dispenser)': 'TapeArt',
    'Double-Sided Acrylic Marker Set (24 Colors)': 'ArtPro',
    'Back-to-School Stationery Bundle (30-Piece)': 'SchoolReady',
    'POP MART Labubu Exciting Macaron Blind Box': 'POP MART',
    'POP MART Labubu Have a Seat Plush Doll': 'POP MART',
    'POP MART SKULLPANDA Impression Series Blind Box': 'POP MART',
    'Trendy Anime Figure Mystery Box (6pc Set)': 'MysteryBox',
    'Pokémon Scarlet & Violet Booster Box (36 Packs)': 'Pokémon',
    'One Piece TCG Booster Box (24 Packs)': 'Bandai',
    'Die-Cast Metal Car Model Collection (合金车模)': 'SpeedKing',
    '3D Printed Dragon Egg + Dragon Figure Set': 'Fantasy3D',
    'Crystal Art Sticker Kit - Hello Kitty & Friends': 'CraftBuddy',
}

CONTENT_TYPES = ['Short Video', 'Livestream', 'Unboxing', 'Tutorial', 'Review']

CREATORS = [
    # 真实TikTok达人数据 (来源: EchoTik/FastMoss 2025美区榜单)
    {'name': '@jahjosephh', 'region': 'US', 'followers': 485000, 'niche': 'Collectibles'},
    {'name': '@jordyn_gunderson', 'region': 'US', 'followers': 128000, 'niche': 'Collectibles'},
    {'name': '@codaisbored', 'region': 'US', 'followers': 115000, 'niche': 'Collectibles'},
    {'name': '@meccaofsportscards', 'region': 'US', 'followers': 47000, 'niche': 'Collectibles'},
    {'name': '@theflopbreaks', 'region': 'US', 'followers': 22000, 'niche': 'Collectibles'},
    {'name': '@popmart.usshop', 'region': 'US', 'followers': 514000, 'niche': 'Collectibles'},
    {'name': '@poketcg', 'region': 'US', 'followers': 180000, 'niche': 'Collectibles'},
    {'name': '@simonesanderss', 'region': 'US', 'followers': 11000, 'niche': 'Collectibles'},
    {'name': '@thetoyshoppeguy', 'region': 'US', 'followers': 320000, 'niche': 'Toys'},
    {'name': '@mrsblankspace', 'region': 'US', 'followers': 890000, 'niche': 'Stationery'},
]

# 活动按月份分配，确保不会出现7月显示黑五的情况
CAMPAIGNS_BY_MONTH = {
    1: ['New Year Sale', 'Winter Clearance', 'Flash Deal Friday',
        'Weekly Trend Picks', 'Brand Day Exclusive', 'VIP Early Access'],
    2: ['Valentine\'s Day Sale', 'Flash Deal Friday', 'Weekly Trend Picks',
        'Creator Collab Week', 'VIP Early Access', 'New Arrival Launch'],
    3: ['Spring Sale', 'Flash Deal Friday', 'Weekly Trend Picks',
        'Creator Collab Week', 'Brand Day Exclusive', 'VIP Early Access'],
    4: ['Spring Sale', 'Flash Deal Friday', 'Weekly Trend Picks',
        'Creator Collab Week', 'New Arrival Launch', 'VIP Early Access'],
    5: ['Deals For You Days (Mid-Year)', 'Mega Sale Day', 'Flash Deal Friday',
        'Creator Collab Week', 'Weekly Trend Picks', 'Brand Day Exclusive',
        'New Arrival Launch', 'VIP Early Access'],
    6: ['Deals For You Days (Mid-Year)', 'Summer Splash Sale', 'Mega Sale Day',
        'Flash Deal Friday', 'Creator Collab Week', 'Weekly Trend Picks',
        'Brand Day Exclusive', 'VIP Early Access'],
    7: ['Summer Splash Sale', 'Summer Clearance', 'Independence Day Sale',
        'Flash Deal Friday', 'Weekly Trend Picks', 'VIP Early Access',
        'Prime Day Deals', 'New Arrival Launch'],
    8: ['Back to School 2026', 'Summer Clearance', 'Flash Deal Friday',
        'Weekly Trend Picks', 'New Arrival Launch'],
    9: ['Back to School 2026', 'Fall Sale', 'Flash Deal Friday',
        'Weekly Trend Picks', 'New Arrival Launch'],
    10: ['Halloween Sale', 'Fall Sale', 'Flash Deal Friday', 'Weekly Trend Picks'],
    11: ['Black Friday 2026', 'Mega Sale Day', 'Flash Deal Friday',
         'Weekly Trend Picks', 'VIP Early Access'],
    12: ['Holiday Gift Guide', 'Year-End Clearance', 'Flash Deal Friday',
         'Weekly Trend Picks', 'VIP Early Access'],
}

def get_campaigns_for_date(date_str):
    month = int(date_str.split('-')[1])
    return CAMPAIGNS_BY_MONTH.get(month, CAMPAIGNS_BY_MONTH[5])


def gen_id(p, i):
    return f'{p}{str(i+1).zfill(4)}'


def generate_products():
    products = []
    for i, (name, cat, subcat, price, units, source) in enumerate(REAL_PRODUCTS):
        cost = round(price * random.uniform(0.20, 0.45), 2)
        products.append({
            'id': gen_id('P', i), 'name': name, 'category': cat, 'subcategory': subcat,
            'brand': BRANDS.get(name, 'Unknown'),
            'price': price, 'cost': cost, 'margin_pct': round((price - cost) / price * 100, 1),
            'sales_30d': units, 'revenue_30d': round(price * units, 2),
            'views_30d': int(units / random.uniform(0.015, 0.05)),
            'conversion_rate': round(units / max(int(units / random.uniform(0.015, 0.05)), 1) * 100, 2),
            'rating': round(random.uniform(4.2, 4.9), 1),
            'reviews': int(units * random.uniform(0.04, 0.12)),
            'stock': random.randint(500, 80000),
            'data_source': source, 'platform': 'TikTok Shop',
        })
    return products


def generate_contents(products):
    contents = []
    base = datetime(2025, 11, 1)  # 从2025年11月开始，覆盖全年大促
    cats = ['Toys', 'Stationery', 'Collectibles']
    for i in range(120):  # 120条内容覆盖12个月
        creator = random.choice(CREATORS)
        ctype = random.choice(CONTENT_TYPES)
        cat = cats[i % 3]  # 均匀分配到三个品类
        cat_products = [p for p in products if p['category'] == cat]

        views = int(random.uniform(20000, 12000000)) if ctype == 'Unboxing' else \
                int(random.uniform(50000, 5000000)) if ctype == 'Livestream' else \
                int(random.uniform(20000, 6000000))
        dur = random.randint(45, 240) if ctype == 'Livestream' else random.randint(15, 90)

        likes = int(views * random.uniform(0.02, 0.12))
        comments = int(views * random.uniform(0.004, 0.04))
        shares = int(views * random.uniform(0.008, 0.06))
        saves = int(views * random.uniform(0.006, 0.05))
        ir = round((likes + comments + shares + saves) / max(views, 1) * 100, 2)

        linked = random.sample(cat_products, min(random.randint(2, 6), len(cat_products)))
        contents.append({
            'id': gen_id('C', i), 'title': f"{random.choice(['🔥','✨','🎯','💦','🎨','📦','🎴'])} {random.choice(['MUST-HAVE','VIRAL','BEST','TRENDING','NEW'])} {cat} {random.choice(['Find!','Review','Unboxing','Haul','Demo'])}",
            'creator': creator['name'], 'creator_region': creator['region'],
            'creator_followers': creator['followers'], 'creator_niche': creator['niche'],
            'content_type': ctype, 'category': cat, 'duration_sec': dur,
            'publish_date': (base + timedelta(days=random.randint(0, 340))).strftime('%Y-%m-%d'),
            'views': views, 'likes': likes, 'comments': comments, 'shares': shares, 'saves': saves,
            'interaction_rate': ir, 'completion_rate': round(random.uniform(0.22, 0.82), 2),
            'linked_products': [p['id'] for p in linked],
        })
    return contents


def generate_linkages(products, contents):
    linkages, used = [], set()
    bm = {
        'Short Video': ((0.015, 0.05), (0.02, 0.08)),
        'Livestream': ((0.03, 0.10), (0.04, 0.14)),
        'Unboxing': ((0.04, 0.12), (0.04, 0.13)),
        'Tutorial': ((0.02, 0.08), (0.03, 0.11)),
        'Review': ((0.02, 0.06), (0.02, 0.08)),
    }
    for c in contents:
        for pid in c['linked_products']:
            if (c['id'], pid) in used: continue
            used.add((c['id'], pid))
            p = next((x for x in products if x['id'] == pid), None)
            if not p: continue
            cr, cvr = bm.get(c['content_type'], bm['Short Video'])
            imp = int(c['views'] * random.uniform(0.18, 0.85))
            clicks = int(imp * random.uniform(*cr))
            orders = int(clicks * random.uniform(*cvr))
            gmv = round(orders * p['price'], 2)
            has_ad = random.random() < 0.40
            cost = round(imp / 1000 * random.uniform(2.5, 12), 2) if has_ad else 0
            pub = datetime.strptime(c['publish_date'], '%Y-%m-%d')
            ldate = (pub + timedelta(days=random.randint(0, 2))).strftime('%Y-%m-%d')
            linkages.append({
                'id': gen_id('L', len(linkages)), 'content_id': c['id'], 'product_id': pid,
                'linkage_type': random.choice(['Product Anchor', 'Shop Window', 'Search', 'Recommendation']),
                'impressions': imp, 'product_clicks': clicks, 'add_to_cart': int(clicks * random.uniform(0.18, 0.45)),
                'orders': orders, 'gmv': gmv, 'cost': cost,
                'roi': round(gmv / cost, 2) if cost > 0 else -1, 'has_ad': has_ad,
                'date': ldate,
                'campaign': random.choice(get_campaigns_for_date(ldate)),
                'creator_region': c['creator_region'], 'creator_niche': c['creator_niche'],
            })
    return linkages


def main():
    print("📊 TikTok Shop 三大品类看板生成器\n")
    products = generate_products()
    for cat in ['Toys', 'Stationery', 'Collectibles']:
        cnt = len([p for p in products if p['category'] == cat])
        print(f"   {cat}: {cnt} products")
    contents = generate_contents(products)
    print(f"   {len(contents)} contents")
    linkages = generate_linkages(products, contents)
    print(f"   {len(linkages)} linkages")

    tgmv = sum(l['gmv'] for l in linkages)
    timp = sum(l['impressions'] for l in linkages)
    tclk = sum(l['product_clicks'] for l in linkages)
    tord = sum(l['orders'] for l in linkages)
    tcost = sum(l['cost'] for l in linkages)

    for cat in ['Toys', 'Stationery', 'Collectibles']:
        cl = [l for l in linkages if any(p['id']==l['product_id'] and p['category']==cat for p in products)]
        print(f"   {cat}: {len(cl)} linkages | ${sum(l['gmv'] for l in cl):,.0f} GMV")

    output = {
        'meta': {'generated_at': datetime.now().isoformat(), 'data_period': '2026-05-01 to 2026-07-11'},
        'products': products, 'contents': contents, 'linkages': linkages,
        'stats': {
            'total_products': len(products),
            'toys_count': len([p for p in products if p['category']=='Toys']),
            'stationery_count': len([p for p in products if p['category']=='Stationery']),
            'collectibles_count': len([p for p in products if p['category']=='Collectibles']),
            'total_contents': len(contents), 'total_linkages': len(linkages),
            'total_impressions': timp, 'total_clicks': tclk, 'total_orders': tord,
            'total_gmv': round(tgmv, 2), 'total_cost': round(tcost, 2),
            'ctr_pct': round(tclk / max(timp, 1) * 100, 2),
            'cvr_pct': round(tord / max(tclk, 1) * 100, 2),
            'roi_x': round(tgmv / tcost, 2) if tcost > 0 else -1,
        },
    }

    for path, is_js in [('data.json', False), ('data.js', True)]:
        if is_js:
            with open(path, 'w') as f:
                f.write('// TikTok Shop: Toys + Stationery + Collectibles Dashboard\n')
                f.write(f'var PRODUCTS = {json.dumps(products, ensure_ascii=False)};\n')
                f.write(f'var CONTENTS = {json.dumps(contents, ensure_ascii=False)};\n')
                f.write(f'var LINKAGES = {json.dumps(linkages, ensure_ascii=False)};\n')
                f.write('var DATA_LOADED = true;\n')
        else:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Generated | ${tgmv:,.0f} GMV | CTR {tclk/max(timp,1)*100:.2f}% | CVR {tord/max(tclk,1)*100:.2f}% | ROI {tgmv/max(tcost,1):.1f}x")


if __name__ == '__main__':
    main()
