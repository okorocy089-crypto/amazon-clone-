# seed_products.py
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazon.settings')  # Change to your project name
django.setup()

from catalog.models import Category, Product  

PRODUCTS_BY_CATEGORY = {
    'electronics': [
        {'name': 'Sony 65" 4K OLED Smart TV', 'description': 'Stunning OLED display with XR processor, Dolby Vision, and Google TV. Perfect for home theater enthusiasts.', 'price': 1899.99},
        {'name': 'Bose Soundbar 900', 'description': 'Premium Dolby Atmos soundbar with 360° audio and built-in Alexa. Wireless subwoofer ready.', 'price': 899.99},
        {'name': 'Yamaha 5.1 Channel Receiver', 'description': '7.2-channel AV receiver with 8K HDMI, Wi-Fi, Bluetooth, and MusicCast multi-room audio.', 'price': 549.99},
        {'name': 'Sonos Arc Soundbar', 'description': 'Premium smart soundbar with Dolby Atmos, voice control, and 11 high-performance drivers.', 'price': 899.99},
        {'name': 'Shure SM7B Microphone', 'description': 'Legendary dynamic microphone for broadcast, podcasting, and studio recording. Cardioid pattern.', 'price': 399.99},
        {'name': 'Rode NT1-A Condenser Mic', 'description': '1" cardioid condenser microphone with low self-noise, ideal for vocals and acoustic instruments.', 'price': 229.99},
        {'name': 'LG 75" NanoCell TV', 'description': '75-inch 4K NanoCell TV with AI-powered picture quality and Dolby Atmos sound.', 'price': 1499.99},
        {'name': 'Bose QuietComfort 45', 'description': 'Over-ear noise-cancelling headphones with 24-hour battery and crisp, balanced audio.', 'price': 329.99},
        {'name': 'Amazon Echo Studio', 'description': 'Premium smart speaker with 3D audio, Dolby Atmos, and built-in Zigbee smart home hub.', 'price': 199.99},
        {'name': 'Dyson Purifier Cool Tower', 'description': 'Smart air purifier with HEPA filter and cooling fan that removes 99.97% of pollutants.', 'price': 699.99},
    ],
    'mobile': [
        {'name': 'iPhone 15 Pro Max', 'description': '6.7" OLED display, A17 Pro chip, titanium design, 5x telephoto lens, USB-C.', 'price': 1199.99},
        {'name': 'Samsung Galaxy S24 Ultra', 'description': '6.8" Dynamic AMOLED, Snapdragon 8 Gen 3, 200MP camera, S Pen, 5000mAh battery.', 'price': 1299.99},
        {'name': 'Google Pixel 8 Pro', 'description': '6.7" display with Google Tensor G3, 50MP camera, AI-powered features, 7-year updates.', 'price': 999.99},
        {'name': 'Samsung Galaxy Tab S9 Ultra', 'description': '14.6" AMOLED tablet, Snapdragon 8 Gen 2, 12GB RAM, included S Pen.', 'price': 1199.99},
        {'name': 'Apple Watch Ultra 2', 'description': '49mm titanium smartwatch, always-on display, dive-ready, 36-hour battery.', 'price': 799.99},
        {'name': 'OnePlus 12', 'description': '6.82" AMOLED, Snapdragon 8 Gen 3, 50MP Hasselblad camera, 100W charging.', 'price': 799.99},
        {'name': 'Nothing Phone (2)', 'description': '6.7" OLED, Glyph interface, Snapdragon 8+ Gen 1, wireless charging.', 'price': 599.99},
        {'name': 'Samsung Galaxy Watch 6', 'description': '44mm smartwatch with body composition analysis, ECG, and sleep tracking.', 'price': 329.99},
        {'name': 'Spigen MagSafe Battery Pack', 'description': '5000mAh portable charger with MagSafe alignment, auto-charging with pass-through.', 'price': 49.99},
        {'name': 'Anker 20W USB-C Charger', 'description': 'Compact 20W USB-C power adapter with foldable plug, fast-charges most phones.', 'price': 14.99},
    ],
    'computers': [
        {'name': 'Apple MacBook Pro 16"', 'description': 'M3 Pro chip, 16" Liquid Retina XDR, 18GB RAM, 512GB SSD, 22-hour battery.', 'price': 2499.99},
        {'name': 'Dell XPS 15', 'description': '15.6" OLED 4K, Intel Core i9, 32GB RAM, 1TB SSD, RTX 4070.', 'price': 2899.99},
        {'name': 'Razer Blade 16', 'description': '16" 240Hz OLED, Intel i9-13950HX, RTX 4090, 32GB RAM, 1TB SSD.', 'price': 3599.99},
        {'name': 'Logitech MX Master 3S', 'description': 'Wireless mouse with 8K DPI, MagSpeed scroll wheel, USB-C, 70-day battery.', 'price': 99.99},
        {'name': 'Keychron Q1 Pro', 'description': '75% mechanical keyboard, Gateron switches, QMK/VIA support, Bluetooth 5.1.', 'price': 199.99},
        {'name': 'Samsung 990 Pro SSD', 'description': '2TB NVMe M.2 SSD with read speeds up to 7,450 MB/s. Perfect for gaming/creative.', 'price': 159.99},
        {'name': 'LG 27" 4K Monitor', 'description': '27" UltraFine 4K IPS display, USB-C, HDR10, and 99% sRGB coverage.', 'price': 499.99},
        {'name': 'Apple iMac 24"', 'description': '24" 4.5K Retina, M3 chip, 16GB RAM, 512GB SSD, 7-color design.', 'price': 1899.99},
        {'name': 'Corsair Vengeance DDR5', 'description': '32GB (2x16GB) DDR5 5600MHz RAM with RGB lighting and heat spreader.', 'price': 139.99},
        {'name': 'ASUS ROG Strix B650E-F', 'description': 'ATX motherboard for AMD AM5, PCIe 5.0, 16+2 power stages, Wi-Fi 6E.', 'price': 299.99},
    ],
    'gaming': [
        {'name': 'Sony PlayStation 5', 'description': 'PS5 console with Ultra HD Blu-ray, DualSense controller, 1TB SSD, 8K-ready.', 'price': 499.99},
        {'name': 'Xbox Series X', 'description': '1TB SSD, 12 TFLOPS GPU, 4K at 120fps, backward compatible, Game Pass ready.', 'price': 499.99},
        {'name': 'Nintendo Switch OLED', 'description': '7" OLED screen, 64GB storage, docked/TV mode, enhanced audio.', 'price': 349.99},
        {'name': 'ASUS ROG Ally', 'description': 'Handheld gaming PC, AMD Z1 Extreme, 7" 120Hz touchscreen, 512GB SSD.', 'price': 699.99},
        {'name': 'Steam Deck OLED', 'description': '7.4" OLED handheld, 512GB SSD, 90Hz, AMD APU, custom SteamOS.', 'price': 549.99},
        {'name': 'Razer Kishi V2', 'description': 'Mobile game controller for Android, USB-C, low latency, works with cloud gaming.', 'price': 99.99},
        {'name': 'SteelSeries Arctis Nova Pro', 'description': 'Wireless gaming headset with ANC, 36-hour battery, AI noise-cancelling mic.', 'price': 349.99},
        {'name': 'Logitech G Pro Wheel', 'description': 'Direct drive racing wheel with 11Nm torque, magnetic paddles, PC/PS5.', 'price': 999.99},
        {'name': 'Elgato Stream Deck Mk2', 'description': '15-button macro keyboard for streaming, with customizable LCD icons.', 'price': 149.99},
        {'name': 'Corsair HS80 Wireless', 'description': 'Gaming headset with Dolby Atmos, 60-hour battery, and broadcast-quality mic.', 'price': 149.99},
    ],
    'pets': [
        {'name': 'Whistle Go Explore', 'description': 'GPS pet tracker with health monitoring, 20-day battery, activity tracking.', 'price': 129.99},
        {'name': 'Neakasa M1', 'description': 'Cordless pet vacuum/grooming kit with 5 suction levels and 3 grooming heads.', 'price': 149.99},
        {'name': 'Petkit PuraMax 2', 'description': 'Self-cleaning litter box with app control, odor filter, and raking system.', 'price': 399.99},
        {'name': 'Outward Hound Life Jacket', 'description': 'Buoyant pet life vest with top handle, reflective strips, and adjustable straps.', 'price': 45.99},
        {'name': 'Seresto Flea Collar', 'description': '8-month flea and tick prevention collar, water-resistant, odorless.', 'price': 59.99},
        {'name': 'K&H Pet Bed Heater', 'description': 'Thermostatically controlled heated pad, safe for indoor pets, 25W.', 'price': 79.99},
        {'name': 'PetSafe Automatic Feeder', 'description': 'Wi-Fi enabled feeder with portion control, 16-cup capacity, camera included.', 'price': 199.99},
        {'name': 'Burt\'s Bees Dog Shampoo', 'description': 'All-natural dog shampoo with shea butter and honey, 16oz.', 'price': 14.99},
        {'name': 'Trixie Cat Tree', 'description': '3-level scratching post with condo, hammock, and dangling toy.', 'price': 89.99},
        {'name': 'Earthbath Dog Wipes', 'description': '100-count hypoallergenic grooming wipes, unscented, for paws and body.', 'price': 12.99},
    ],
    'cutlery': [
        {'name': 'Wüsthof Classic 8" Chef Knife', 'description': 'Forged stainless steel chef\'s knife with full tang and ergonomic handle.', 'price': 149.99},
        {'name': 'Zwilling Pro 7-Piece Set', 'description': '7-pc knife set, includes chef, bread, paring, utility, and Santoku knives.', 'price': 399.99},
        {'name': 'HexClad 10" Fry Pan', 'description': 'Hybrid nonstick/fry pan, induction-ready, metal utensil safe.', 'price': 125.99},
        {'name': 'Le Creuset Dutch Oven', 'description': '5.5qt enameled cast iron Dutch oven, available in 10+ colors.', 'price': 399.99},
        {'name': 'Victorinox 15-Piece Set', 'description': 'Complete kitchen knife set with 15 pieces, including steel and scissors.', 'price': 199.99},
        {'name': 'Cuisinart Stainless Steel Set', 'description': '12-pc cookware set, induction ready, dishwasher safe, with tempered glass lids.', 'price': 179.99},
        {'name': 'Ooni Koda 12 Gas Pizza Oven', 'description': 'Portable gas pizza oven, 16" pizza capacity, 60-second cook time.', 'price': 349.99},
        {'name': 'KitchenAid Pasta Roller', 'description': '3-in-1 pasta roller attachment for stand mixers, stainless steel.', 'price': 149.99},
        {'name': 'Pyrex Glass Measuring Cups', 'description': '4-piece set: 1-cup, 2-cup, 4-cup, 8-cup with red and black markings.', 'price': 29.99},
        {'name': 'Mora Swedish Knife', 'description': 'Carbon steel fixed-blade knife with birch handle, perfect for prep.', 'price': 19.99},
    ],
    'musical-instruments': [
        {'name': 'Fender Stratocaster', 'description': 'Electric guitar, alder body, maple neck, 3 single-coil pickups, incl. case.', 'price': 899.99},
        {'name': 'Yamaha FG830 Acoustic Guitar', 'description': 'Dreadnought guitar with solid spruce top, rosewood back/sides, warm tone.', 'price': 399.99},
        {'name': 'Casio Privia PX-S1100', 'description': 'Digital piano, 88 keys, 10 tones, Bluetooth audio/MIDI, slim design.', 'price': 899.99},
        {'name': 'Roland TD-17KVX', 'description': 'Electronic drum kit with mesh snare, dual-zone pads, and 50 drum kits.', 'price': 1199.99},
        {'name': 'Gibson Les Paul Studio', 'description': 'Solid-body electric guitar with mahogany body, humbuckers, ebony fretboard.', 'price': 1499.99},
        {'name': 'Yamaha P125 Digital Piano', 'description': '88-key weighted action piano with 24 voices, built-in speakers, USB-MIDI.', 'price': 649.99},
        {'name': 'Shure PGA58 Mic Kit', 'description': 'Dynamic vocal mic with 15\' cable and stand, cardioid pattern.', 'price': 89.99},
        {'name': 'Martin LX1 Little Martin', 'description': '3/4-size acoustic guitar, solid spruce top, mahogany laminate, with gig bag.', 'price': 479.99},
        {'name': 'Sennheiser HD 600', 'description': 'Open-back studio headphones, reference grade, neutral sound, detachable cable.', 'price': 299.99},
        {'name': 'Focusrite Scarlett 2i2', 'description': '2-in/2-out USB audio interface with high-headroom instrument inputs.', 'price': 179.99},
    ],
    'school-accessories': [
        {'name': 'Herschel Classic Backpack', 'description': '18L backpack with classic silhouette, 15" laptop sleeve, internal water bottle pocket.', 'price': 69.99},
        {'name': 'Sharpie Highlighters', 'description': '12-pack of fluorescent highlighters, chisel tip, assorted colors.', 'price': 12.99},
        {'name': 'Apple Pencil (2nd Gen)', 'description': 'Precision stylus for iPad Pro/Air, with magnetic charging, tilt/pressure sensitivity.', 'price': 129.99},
        {'name': 'Moleskine Classic Notebook', 'description': '5x8.25" hardcover journal, acid-free paper, expandable pocket.', 'price': 24.99},
        {'name': 'BIC Round Stic Pens', 'description': '60-pack of ballpoint pens, 0.7mm point, medium blue ink.', 'price': 8.99},
        {'name': 'Bose QC35 II Headphones', 'description': 'Over-ear noise-cancelling headphones for studying, 20-hour battery.', 'price': 299.99},
        {'name': 'Rite in the Rain Notebook', 'description': 'All-weather waterproof notebook, spiral-bound, 3x5", 100 sheets.', 'price': 19.99},
        {'name': 'Five Star 5-Subject Notebook', 'description': '180 sheets, 5 dividers, pocket, carbonless copy sheets for notes.', 'price': 12.99},
        {'name': 'Pilot G2 Gel Pens', 'description': '12-pack of retractable gel pens, 0.7mm, smooth-writing.', 'price': 14.99},
        {'name': 'Xenon 2-Hole Punch', 'description': 'Heavy-duty 2-hole punch for paper, up to 30 sheets, adjustable.', 'price': 29.99},
    ],
    'clothing-fashion': [
        {'name': 'Levi\'s 501 Original Jeans', 'description': 'Classic straight-fit jeans, button fly, 100% cotton, available in all sizes.', 'price': 89.99},
        {'name': 'Champion Reverse Weave Hoodie', 'description': 'Pullover hoodie with oversized front pouch, 12oz fleece, iconic script logo.', 'price': 69.99},
        {'name': 'Nike Air Force 1 \'07', 'description': 'Sneaker with leather upper, Nike Air sole, classic lace-up style.', 'price': 115.99},
        {'name': 'Hanes EcoSmart T-Shirt', 'description': '5-pack of 100% cotton t-shirts, ring-spun fabric, tag-free neck.', 'price': 22.99},
        {'name': 'Lululemon Align Leggings', 'description': 'High-waisted yoga leggings with Nulu fabric, 4-way stretch.', 'price': 98.99},
        {'name': 'Carhartt Work Jacket', 'description': 'Quilted flannel-lined work jacket, 100% cotton duck canvas, sturdy.', 'price': 129.99},
        {'name': 'Tommy Hilfiger Polo', 'description': 'Classic cotton pique polo shirt with embroidered logo, 3-button placket.', 'price': 69.99},
        {'name': 'Vans Old Skool Sneakers', 'description': 'Classic skate shoe with side stripe, canvas/suede upper, padded collar.', 'price': 64.99},
        {'name': 'Fjallraven Kanken Backpack', 'description': 'Water-resistant backpack with seat pad, reflective logo, in 20 colors.', 'price': 79.99},
        {'name': 'Calvin Klein Boxers', 'description': '3-pack of cotton stretch boxer briefs, no-fly design, tag-free waistband.', 'price': 42.99},
    ],
    'wears': [
        {'name': 'New Era 59FIFTY Hat', 'description': 'MLB fitted cap, structured silhouette, wool blend, flat brim.', 'price': 42.99},
        {'name': 'Adidas Ultraboost Light', 'description': 'Running shoe with Light Boost foam, 3D heel cup, continental rubber.', 'price': 169.99},
        {'name': 'Carhartt Beanie', 'description': 'Rib-knit acrylic beanie, soft, warm, with logo patch on front.', 'price': 22.99},
        {'name': 'Birkenquantity Arizona Sandals', 'description': 'Two-strap sandal with cork footbed, leather upper, contoured arch support.', 'price': 99.99},
        {'name': 'CK One Underwear', 'description': 'Microfiber boxer briefs, minimal stitching, flexible fit, 3-pack.', 'price': 36.99},
        {'name': 'Crocs Classic Clog', 'description': 'Lightweight clog with heel strap, ventilation holes, easy to clean.', 'price': 45.99},
        {'name': 'Nike Dri-FIT Socks', 'description': '6-pack of running socks, moisture-wicking, cushioned sole, arch support.', 'price': 28.99},
        {'name': 'Filson Tin Cloth Hat', 'description': 'Waxed tin cloth baseball cap, durable, water-repellent, adjustable.', 'price': 49.99},
        {'name': 'Timberland 6-Inch Boots', 'description': 'Premium leather boot, waterproof, padded collar, 100% recycled lining.', 'price': 198.99},
        {'name': 'Under Armour Tech Boxerjock', 'description': '2-pack of boxer briefs, HeatGear fabric, anti-odor, stretch.', 'price': 34.99},
    ],
    'sports-equipment': [
        {'name': 'Wilson NBA Basketball', 'description': 'Official leather basketball, 29.5" size 7, NBA approved.', 'price': 149.99},
        {'name': 'Babolat Pure Drive Tennis Racquet', 'description': '100sq in racquet, 300g, 16x19 string pattern, power and spin.', 'price': 269.99},
        {'name': 'Callaway Rogue ST Driver', 'description': '460cc driver with jailbreak technology, 9°–12° loft, adjustable.', 'price': 549.99},
        {'name': 'Adidas MLS Soccer Ball', 'description': '32-panel soccer ball, textured surface, FIFA quality approved.', 'price': 39.99},
        {'name': 'Garmin Forerunner 55', 'description': 'GPS running watch, heart rate, pace/distance alerts, up to 14 days.', 'price': 199.99},
        {'name': 'SPRI Resistance Bands Set', 'description': '5-pack of loop bands: X-light to X-heavy, non-slip, reusable.', 'price': 24.99},
        {'name': 'Rawlings Player Series Glove', 'description': '12.5" baseball glove, soft leather, pre-oiled, for youth/adult.', 'price': 59.99},
        {'name': 'Franklin Sports Soccer Goal', 'description': '6x4ft folding goal with 4mm steel, includes stakes, 2pcs.', 'price': 79.99},
        {'name': 'Hex Dumbbell Set', 'description': '50lb single hex dumbbell, chrome handle, rubber-coated.', 'price': 79.99},
        {'name': 'Yoga Mat by Manduka', 'description': '6mm thick mat, high-density, closed-cell, 71"x26", eco-friendly.', 'price': 89.99},
    ],
    'cycling': [
        {'name': 'Trek FX 3 Disc', 'description': 'Hybrid bike, 24-speed, hydraulic disc brakes, lightweight aluminum frame.', 'price': 1249.99},
        {'name': 'Segway Ninebot MAX', 'description': 'Electric scooter, 40mi range, 18.6mph, air-filled tires, foldable.', 'price': 799.99},
        {'name': 'Razor A5 Kick Scooter', 'description': 'Adult kick scooter, 8" wheels, aluminum frame, foldable.', 'price': 79.99},
        {'name': 'Specialized Rockhopper', 'description': 'Mountain bike, 27.5" wheels, 1x drivetrain, 80mm suspension fork.', 'price': 699.99},
        {'name': 'Aventon Level.2 E-Bike', 'description': '500W motor, 60mi range, 28mph, 8-speed, integrated rear rack.', 'price': 1999.99},
        {'name': 'Boosted Rev Scooter', 'description': 'Dual motors, 28mph top speed, 20mi range, regenerative brakes.', 'price': 1599.99},
        {'name': 'Schwinn GTX 3', 'description': 'Hybrid/e-bike, 48V battery, 7-speed, 20" wheels, hydraulic brakes.', 'price': 1299.99},
        {'name': 'Kawasaki KLX230R', 'description': '233cc dirt bike, electric start, 6-speed, off-road, 230lb.', 'price': 4999.99},
        {'name': 'Yamaha MT-03', 'description': '321cc motorcycle, 37hp, 6-speed, 368lb, ABS.', 'price': 4999.99},
        {'name': 'StreetScooter Skateboard', 'description': '36" cruiser board, 7-ply maple, ABEC-5 bearings, 65mm wheels.', 'price': 49.99},
    ],
    'dope-tech': [
        {'name': 'DJI Mavic 3 Pro', 'description': 'Triple-camera drone with 4/3 CMOS, 28x hybrid zoom, 43min flight.', 'price': 2199.99},
        {'name': 'Tesla Cybertruck Grill', 'description': 'Stainless steel modular tech panel (not a grill), with LED/Tesla power.', 'price': 2999.99},
        {'name': 'Anker Eufy X10', 'description': 'Robotic vac/mop with dual cameras, Auto-empty, 6,000Pa suction.', 'price': 499.99},
        {'name': 'Nothing Ear (2)', 'description': 'ANC earbuds with 11.6mm drivers, up to 36hr battery, LHDC codec.', 'price': 149.99},
        {'name': 'TCL NXTWEAR S', 'description': '3D AR glasses, 1080p micro-OLED, 60Hz, virtual 130" screen.', 'price': 399.99},
        {'name': 'Roborock S8 MaxV Ultra', 'description': 'Robot mop/vac with obstacle avoidance, 8,000Pa suction, hot-water mop.', 'price': 1599.99},
        {'name': 'Sony A7R V Camera', 'description': '61MP full-frame mirrorless, AI AF, 8K video, 5-axis IBIS.', 'price': 3899.99},
        {'name': 'HoverAir X1', 'description': 'Self-flying drone, palm-sized, follow-me modes, 16min flight.', 'price': 599.99},
        {'name': 'Plume SuperPod X', 'description': 'Mesh Wi-Fi 6E, 8.5Gbps speed, AI-powered, 1,200m² range.', 'price': 199.99},
        {'name': 'EcoFlow Delta 2', 'description': '1,024Wh portable power station with 15 outlets, solar-ready.', 'price': 1099.99},
    ],
    'toys-games': [
        {'name': 'Lego Star Wars Millennium Falcon', 'description': '1,354-piece building set with 6 minifigures, Han Solo cockpit.', 'price': 159.99},
        {'name': 'Hasbro Monopoly Classic', 'description': 'Family board game with 8 tokens, 32 houses, 12 hotels, banking.', 'price': 19.99},
        {'name': 'Nerf Elite 2.0 Motoblitz', 'description': 'Motorized blaster with 20-dart drum, slam-fire, 3 modes.', 'price': 39.99},
        {'name': 'Ravensburger Disney 1000pc', 'description': 'Jigsaw puzzle with Mickey, Minnie, 24"x30", for ages 10+.', 'price': 19.99},
        {'name': 'Mattel Minecraft Sword', 'description': '2ft foam diamond sword with 3D detailing, harmless for cosplay.', 'price': 29.99},
        {'name': 'Spin Master Ice Cream Maker', 'description': '2.5L electric ice cream maker, 8 recipes, 30-min freeze.', 'price': 99.99},
        {'name': 'Marvel Legends Action Figures', 'description': '6" Dr. Strange figure with 20 points of articulation and accessories.', 'price': 24.99},
        {'name': 'Catan Board Game', 'description': 'Classic settlement/road-building game, 3-4 players, 60min play.', 'price': 49.99},
        {'name': 'Yoto Mini Player', 'description': 'Audio player for kids, screen-free, 1,000+ stories, 6-hour battery.', 'price': 69.99},
        {'name': 'Jenga Classic', 'description': 'Stacking block game, 54 blocks, age 6+, 2+ players.', 'price': 16.99},
    ],
    'cosmetics': [
        {'name': 'Dior Sauvage Eau de Parfum', 'description': 'Men\'s fragrance with bergamot, ambroxan, woody notes, 100ml.', 'price': 149.99},
        {'name': 'Chanel No.5 Parfum', 'description': 'Iconic floral/aldehydic fragrance, 50ml, for women.', 'price': 179.99},
        {'name': 'MAC Lipstick - Ruby Woo', 'description': 'Matte retro-red lipstick with blue undertones, 12hr wear.', 'price': 26.99},
        {'name': 'NARS Light Reflecting Foundation', 'description': '30ml, medium/buildable coverage, SPF 15, radiant finish.', 'price': 49.99},
        {'name': 'Dior J\'adore EDP', 'description': 'Women\'s floral fragrance, 100ml, with ylang-ylang and jasmine.', 'price': 159.99},
        {'name': 'Maybelline Lash Sensational', 'description': 'Mascara with curved brush, 10hr volume, waterproof.', 'price': 12.99},
        {'name': 'The Ordinary Retinol 1%', 'description': '30ml squalane-based retinol serum, reduces fine lines/wrinkles.', 'price': 12.99},
        {'name': 'Aesop Resurrection Hand Balm', 'description': '75ml, citrus/wood scent, 24hr hydration.', 'price': 35.99},
        {'name': 'Clinique Moisturizing Gel', 'description': '125ml gel moisturizer, oil-free, for all skin types.', 'price': 46.99},
        {'name': 'Guerlain Homme EDP', 'description': 'Men\'s fragrance with mint/rum/woods, 75ml, fresh/citrus.', 'price': 109.99},
    ],
    'automotive': [
        {'name': 'Tesla Model 3', 'description': 'Mid-size all-electric sedan, 272mi range, 0-60mph in 5.8s.', 'price': 38990.99},
        {'name': 'Ford F-150 Raptor R', 'description': '5.2L supercharged V8, 700hp, 35" tires, 4x4, towing 8,200lb.', 'price': 79975.99},
        {'name': 'Toyota Corolla LE', 'description': 'Compact sedan, 1.8L 4-cyl, 33mpg, 8" touchscreen, safety sense.', 'price': 22050.99},
        {'name': 'Honda CR-V Hybrid', 'description': '5-passenger SUV, 2.0L hybrid, 40mpg, AWD, heated seats.', 'price': 33800.99},
        {'name': 'Chevrolet Suburban', 'description': '8-passenger SUV, 5.3L V8, 6,000lb towing, 4x4.', 'price': 59800.99},
        {'name': 'Jeep Wrangler 4xe', 'description': 'PHEV SUV, 21mi EV range, 49MPGe, 4x4, removable roof.', 'price': 49995.99},
        {'name': 'Toyota Sienna LE', 'description': '8-passenger minivan, 2.5L hybrid, 36mpg, AWD, 7" infotainment.', 'price': 37185.99},
        {'name': 'Mercedes-Benz Sprinter', 'description': '144" crew van, 3.0L diesel V6, 188hp, 9,000lb towing.', 'price': 49900.99},
        {'name': 'Nissan Z Sports Car', 'description': '3.0L V6 twin-turbo, 400hp, 6-speed manual, RWD.', 'price': 42000.99},
        {'name': 'Rivian R1S', 'description': '7-passenger electric SUV, 316mi range, 7 seats, 0-60 in 3.0s.', 'price': 78000.99},
    ],
}

CATEGORY_NAME_MAP = {
    'electronics': 'Electronics',
    'mobile': 'Mobile',
    'computers': 'Computers',
    'gaming': 'Gaming',
    'pets': 'Pets',
    'cutlery': 'Cutlery',
    'musical-instruments': 'Musical Instruments',
    'school-accessories': 'School Stuff',
    'clothing-fashion': 'Clothing & Fashion',
    'wears': 'Wears',
    'sports-equipment': 'Sports',
    'cycling': 'Cycling',
    'automotive': 'Automotive',
    'dope-tech': 'Dope Tech',
    'toys-games': 'Toys & Games',
    'cosmetics': 'Cosmetics',
}
def list_categories():
    print("Categories currently in your database:")
    for cat in Category.objects.all():
        print(f"  - {cat.name!r}")

def seed_products():
    """Add products to existing categories (skip if product already exists)"""
    created_count = 0
    skipped_count = 0
    missing_categories = []
    
    print("🌱 Starting product seed...")
    print("=" * 50)
    
    for category_key, products in PRODUCTS_BY_CATEGORY.items():
        real_name = CATEGORY_NAME_MAP.get(category_key)
        if not real_name:
            print(f"\n[SKIP] No mapping set for '{category_key}' in CATEGORY_NAME_MAP")
            missing_categories.append(category_key)
            continue
 
        try:
            category = Category.objects.get(name__iexact=real_name)
        except Category.DoesNotExist:
            print(f"\n[MISSING] Category '{real_name}' (mapped from '{category_key}') not found")
            missing_categories.append(category_key)
            continue
 
        print(f"\nCategory: {category.name}")
 
        for product_data in products:
            if Product.objects.filter(name=product_data['name']).exists():
                print(f"  skipped (exists): {product_data['name']}")
                skipped_count += 1
            else:
                Product.objects.create(
                    name=product_data['name'],
                    description=product_data['description'],
                    price=product_data['price'],
                    category=category,
                    quantity=50,
                )
                print(f"  created: {product_data['name']}")
                created_count += 1
 
    print("\n" + "=" * 50)
    print("Seed complete!")
    print(f"  Created: {created_count}")
    print(f"  Skipped (already existed): {skipped_count}")
    print(f"  Total products in DB now: {Product.objects.count()}")
 
    if missing_categories:
        print(f"\n  Unmapped/missing categories: {', '.join(missing_categories)}")
        print("  Run with --list-categories to see your real category names,")
        print("  then fill in CATEGORY_NAME_MAP at the top of this file.")
 
 
if __name__ == '__main__':
    import sys
    if '--list-categories' in sys.argv:
        list_categories()
    else:
        seed_products()