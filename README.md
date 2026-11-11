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
| Studios | **Test Kitchen**: cook for customers who taste and react ("too salty!") until you get it right | Flavor balance, food science, food origins |
| Studios | **Atelier**: design a dress and accessorize it (shoes, bag, jewelry, layers) to a client brief | Color theory, proportion, dress codes |
| Studios | **Hair Salon**: a full appointment: recline the client into the shampoo bowl, pick the right shampoo, wash (water temperature, pumps, scalp massage, rinse, conditioner timer, towel), detangle from the ends up, blow-dry with heat settings, products for curl pattern (1A–4C) and porosity, a cut in six clippable sections (crown, middle, nape, sides, bangs), color, and styling (12 styles including pigtails, side and fishtail braids, crown braid, cornrows and locs), with a client comfort meter | Hair care, proportion, color theory |
| Studios | **Makeup Studio**: paint 17 products onto varied faces (9 skin tones, eye, nose, lip and brow shapes, freckles, vitiligo, mature skin, headscarves, piercings) with brush size, intensity, softness, finish and a blending tool, for 15 occasions or 17 themes | Color theory, skin undertones, makeup history |
| Studios | **Sewing Room**: take a commission, design it (12 materials, prints, bodice, sleeves, skirt, layers), set up the machine, lay out and sew 30 garments (from tote bags to corsets, ballgowns and waistcoats), then hands-on finishing (boning, grommets, lacing, zippers, embroidery, hem pinning, drawstrings, buttons, pleats, gathering, pressing) and trims | Materials, construction, spatial planning |
| Studios | **Floorplan Lab**: draw a home that meets a client's rules, then add doors, windows and furniture (reachability, daylight, kitchen work triangle) | Spatial reasoning, area, building basics |
| Studios | **Gift Detective**: read a person's blog, infer what they need, love and must avoid, then shop an online store of 60 products within budget (shipping included), for 18 people | Reading comprehension, inference, empathy, budgeting |
| Studios | **Peacemaker**: mediate 14 heated arguments, from group chats to noisy neighbors | Conflict resolution, psychology |
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
