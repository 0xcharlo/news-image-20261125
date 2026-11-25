# News Image — 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/0xcharlo/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/0xcharlo/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image that sums up the world's news of Wednesday 25 November 2026,
entered in the make.fun [`news-image-20261125`](https://make.fun/bounty/news-image-20261125) bounty. Play on make.fun with referral code `7n8phv37`.

## What it shows

- **Lead:** CIA and ODNI hit by a hack of their unclassified
  open-source-intelligence network — no classified data affected,
  attacker unknown, breach resolved.
- **Grid:** Houthi strike hits Riyadh's tallest tower, 11 wounded;
  Huawei convicted on 10 of 12 counts; NATO sends AWACS to Poland;
  WHO evacuates Ebola staff in Congo.
- **Also today:** Ukraine says it struck a Russian ship in the Gulf of
  Finland; Sarkozy corruption case ordered to trial in France; IRGC
  claims more tankers hit mines in Hormuz — unverified.

Every headline was checked against Reuters, AP, NYT and CNN reporting
from 24–25 November 2026.

## How it is made

`render_frontpage.py` draws the front page from scratch with Pillow —
masthead, lead story with a drawn globe illustration, four-story grid,
also-today strip and footer. No stock photos or external images are used.

`main.py` is the competition entry point: it copies `news.png` to
`/output/entry.png` using only the standard library.

## Run it

```sh
python3 render_frontpage.py   # writes news.png (1024x1024)
python3 main.py               # writes /output/entry.png
```

## Verification

The rendered page is 1024x1024 pixels and well under the 1 MiB limit.
It was checked at full size and scaled to 300 pixels wide: headlines stay
legible, nothing overlaps, and no text is garbled.
