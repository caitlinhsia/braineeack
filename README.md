# Synapse Arcade

An adaptive brain-training game that runs in the browser. Seventeen rooms, each tracking its own difficulty (1–10) and tuning itself so you succeed about 75% of the time.

| Wing | Room | What you learn |
| --- | --- | --- |
| Explorers | **World Kitchen**: guess where a dish comes from on a world map (plus a 60-second Blitz) | Geography, food history |
| Explorers | **Time & Thread**: guess where and when an outfit was worn | History, geography |
| Explorers | **Landmark Hunt**: pin 32 illustrated world landmarks on the map | Geography, history |
| Explorers | **Atlas Detective**: an unlabeled map: find countries, name highlighted ones by shape, pick capitals (64 countries) | Map reading, capitals |
| Explorers | **Postcard Trip**: postcards arrive from your next stop; read the clues, pick the city and fly 8 legs around the world, tracking kilometres (28 cities) | Geography, distance |
| Explorers | **Mystery Guest**: a silhouette from history; reveal clues and guess who it is (43 figures) | History |
| Explorers | **Flag Maker**: rebuild 59 countries' flags across 10 layouts (stripes, crosses, saltires, triangles, discs) | Flags, symbolism |
| Explorers | **Then & Now**: slot 80 events, from farming to the Webb telescope, into a growing timeline | History |
| Studios | **Test Kitchen**: run a kitchen: tickets with a dish photo, real knife work, a live stove where food browns, sizzles and burns, flipping, stirring, salting pasta water, tasting and seasoning, plating to the photo, coins, upgrades and a daily dish. Classic mode: cook for customers who taste and react ("too salty!") until you get it right | Flavor balance, food science, food origins |
| Studios | **Atelier**: run a styling studio. Dress a live model from a wardrobe rack to a client's mood board, choose fabrics, dye each piece on a color wheel that names the harmony, accessorize, then walk the runway for three judges. Coins, upgrades and a daily look. Classic design mode kept | Color theory, proportion, dress codes |
| Studios | **Hair Salon**: run your own salon with live, moving hair. Every strand gets wet, foams, tangles, frizzes, curls, shines, takes heat damage and holds product; straight, wavy, curly and coily hair each behave differently. The appointment runs in phases (Wash → Cut → Color → Dry → Style), with a front and back view. Clients bring a photo to match, with a live match score, coins, tips, pro upgrades and a daily challenge. Wash at a real shampoo bowl (recline, neck towel, water temperature, shampoo choice, scalp massager, conditioner and masks) and section hair with clips. 12 hair types (1A–4C) in fine, medium or thick density, and 20+ products and tools (leave-in, oil, dry shampoo, sea-salt spray, edge control, thinning shears, clippers, round brush…) that visibly coat the hair. Clients have varied faces and hair with highlights, balayage, grown-out roots, greys and split ends; dye colors exactly the zone you paint (roots, lengths or ends). The classic mode keeps the full step-by-step appointment: recline the client into the shampoo bowl, pick the right shampoo, wash (water temperature, pumps, scalp massage, rinse, conditioner timer, towel), detangle from the ends up, blow-dry with heat settings, products for curl pattern (1A–4C) and porosity, a cut in six clippable sections (crown, middle, nape, sides, bangs), color, and styling (12 styles including pigtails, side and fishtail braids, crown braid, cornrows and locs), with a client comfort meter | Hair care, proportion, color theory |
| Studios | **Makeup Studio**: run a makeup studio with real layered painting on a canvas. Clients bring a photo and real skin needs (shine, redness, dark circles, spots, dry patches): prep, color-correct, match foundation shade and undertone, sculpt, paint eyes with close-up zoom and lips, blend and set, scored pixel by pixel against their photo, with coins, upgrades and a daily challenge. Classic and theme modes still paint 17 products onto varied faces (9 skin tones, eye, nose, lip and brow shapes, freckles, vitiligo, mature skin, headscarves, piercings) with brush size, intensity, softness, finish and a blending tool, for 15 occasions or 17 themes | Color theory, skin undertones, makeup history |
| Studios | **Sewing Room**: run a tailoring studio: measure varied bodies with a tape, choose fabric within budget, lay out, pin and cut the pattern with shears, drive a pedal-powered machine along the seam guide with backstitching, fit and alter on the client, press, hem and close, then walk the runway against their sketch, with coins, upgrades and a daily challenge. Classic mode: take a commission, design it (12 materials, prints, bodice, sleeves, skirt, layers), set up the machine, lay out and sew 30 garments (from tote bags to corsets, ballgowns and waistcoats), then hands-on finishing (boning, grommets, lacing, zippers, embroidery, hem pinning, drawstrings, buttons, pleats, gathering, pressing) and trims | Materials, construction, spatial planning |
| Studios | **Floorplan Lab**: run a home-design firm. Families bring a wish list and a budget: draw rooms, add doors (wide ones for wheelchairs) and windows, furnish with real-size furniture and clearances, pick floors and paint, follow the sun, see it as a 3D dollhouse, then watch them move in. Classic plan mode kept | Spatial reasoning, area, building basics |
| Studios | **Gift Detective**: scroll a person's feed and pin clues, DM their friends, shop on a budget, wrap it by hand, write the card and watch them unbox it. Holiday rush mode shares one budget across three gifts. Classic blog shopping kept | Reading comprehension, inference, empathy, budgeting |
| Studios | **Peacemaker**: mediate a live argument between animated characters whose body language shifts with their mood. Reply before the timer runs out, pick a tone (calm, warm, firm) and words, rescue walkouts and reach one of three endings. Classic scenes kept | Conflict resolution, psychology |
| Brain gym | **Deep Dive**: two versions. Classic: name as many as you can; rare answers sink you deeper. Rare Pick: one answer per category, so pick the rarest you dare | Knowledge breadth, recall |
| Brain gym | **Science Lab**: find organs and bones, mix light versus ink, sink or float, line up the planets | Biology, color science |
| Brain gym | Echo Grid, Quick Sums, Unscramble, Switchboard | Memory, mental math, vocabulary, logic |

There's also a daily **World Tour** event (the same five map rounds for every player, with a shareable score) and a **Daily Mix** of eight interleaved questions.

Double-click any word in the app for a definition (built-in glossary, with a dictionary lookup as a fallback). Map rounds show country names as you zoom.

## Project layout

- `src/game.html` is the source: the whole game (HTML, CSS, JavaScript and map data) in one file.
- `scripts/build.py` wraps it into a full web page at `index.html`, which Vercel serves. Run `python3 scripts/build.py` after editing the source, and commit both files.
- Progress is saved in the browser's `localStorage`, so it stays on that device.

## Run locally

Open `index.html` in a browser, or serve the folder:

```bash
npx serve .
```

## Deploy to Vercel

1. Go to <https://vercel.com/new> and sign in with GitHub.
2. Import the `braineeack` repository.
3. Leave **Framework Preset** as **Other**, and leave the build command and output directory empty.
4. Click **Deploy**.

Every push to `main` then redeploys automatically.

## Credits

Map data: [Natural Earth](https://www.naturalearthdata.com/) (public domain), via [world-atlas](https://github.com/topojson/world-atlas) (ISC), pre-projected into SVG paths. Fonts from Google Fonts.
