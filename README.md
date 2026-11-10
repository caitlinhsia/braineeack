# Synapse Arcade

An adaptive brain-training game that runs in the browser. Seventeen rooms, each tracking its own difficulty (1–10) and tuning itself so you succeed about 75% of the time.

| Wing | Room | What you learn |
| --- | --- | --- |
| Explorers | **World Kitchen**: guess where a dish comes from on a world map | Geography, food history |
| Explorers | **Time & Thread**: guess where and when an outfit was worn | History, geography |
| Explorers | **Landmark Hunt**: pin illustrated world landmarks on the map | Geography, history |
| Explorers | **Flag Maker**: rebuild a country's flag (layout and colors) | Flags, symbolism |
| Explorers | **Then & Now**: slot events into a growing timeline | History |
| Studios | **Test Kitchen**: cook for customers who taste and react ("too salty!") until you get it right | Flavor balance, food science, food origins |
| Studios | **Atelier**: design a dress to a client brief | Color theory, proportion, dress codes |
| Studios | **Hair Salon**: cuts, bangs and toners for each face shape and color problem | Face shapes, color correction |
| Studios | **Makeup Studio**: paint 13 products onto a face for clients' occasions, or face the judges in theme challenges | Color theory, skin undertones, makeup history |
| Studios | **Sewing Room**: pick from 11 patterns, lay out the pieces, then sew by tracing each seam | Spatial planning, fine motor control |
| Studios | **Floorplan Lab**: draw a home that meets a client's rules | Spatial reasoning, area, building basics |
| Studios | **Peacemaker**: mediate a heated argument | Conflict resolution, psychology |
| Brain gym | **Science Lab**: find organs and bones; mix light versus ink | Biology, color science |
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
