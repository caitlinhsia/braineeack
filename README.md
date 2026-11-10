# Synapse Arcade

An adaptive brain-training game that runs in the browser. Ten rooms, each tracking its own difficulty (1–10) and tuning itself so you succeed about 75% of the time.

| Wing | Room | What you learn |
| --- | --- | --- |
| Explorers | **World Kitchen**: guess where a dish comes from on a world map | Geography, food history |
| Explorers | **Time & Thread**: guess where and when an outfit was worn | History, geography |
| Studios | **Atelier**: design a dress to a client brief | Color theory, proportion, dress codes |
| Studios | **Sewing Room**: lay out pattern pieces, then order the construction steps | Spatial planning, sequencing |
| Studios | **Floorplan Lab**: draw a home that meets a client's rules | Spatial reasoning, area, building basics |
| Studios | **Peacemaker**: mediate a heated argument | Conflict resolution, psychology |
| Core | Echo Grid, Quick Sums, Unscramble, Switchboard | Memory, mental math, vocabulary, logic |

There's also a **Daily Mix**: eight interleaved questions from eight rooms.

## Project layout

- `index.html` is the whole game: HTML, CSS, JavaScript and map data in one file. It has no build step and no dependencies.
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
