# news-image-nov-22

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/wenjinqin/news-image-nov-22/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/wenjinqin/news-image-nov-22/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

One page that sums up the world news of **Sunday 22 November 2026**,
drawn entirely with code — no photographs, no stock art. The front page
leads with the collapse of COP31 in Antalya and carries five more of
the day's stories as illustrated panels:

- **COP31 collapses with no deal** — the EU rejects the "Antalya
  Pact" draft with no mention of fossil fuels; the longest climate
  summit ever ends empty-handed.
- **Russian drone hits a flat block near Kyiv** — a drone destroys
  part of a five-storey block in Dymer; 14 missing, nine pulled out.
- **Bahrain counts two hurt in the Iran strike** — Tehran claims it
  hit US Patriot radars; Bahrain says an industrial site was hit,
  one victim in critical condition.
- **Settlers torch cars in four West Bank villages** — a dozen
  vehicles burned overnight near Ramallah; Israel opens an
  investigation.
- **Democrats take 258 House seats** — a North Carolina recount
  hands Chuck Hubbard the 258th seat, the biggest House majority
  since 1992; Democrats also take the Senate.
- **Candy factory fire kills 3, 36 missing** — a blaze sweeps the
  Milkita sweets plant in Banten, Indonesia; rescuers search the
  ruins a day on.

A ticker along the bottom adds the US warning Americans in Bahrain
after the strikes, Delta delaying 1,000+ flights after a Microsoft
outage, and Russia starting to tow its drone-hit ship in the Baltic.

Every story was verified against at least two published sources dated
22 November 2026 (Le Monde, Reuters/Nikkei, NPR, CNN, Al Jazeera;
Reuters, Ukrainska Pravda, Kyiv Post, The New Voice of Ukraine,
Daily Sabah; Arab News/AFP, Al Arabiya, The National, Gulf News;
Reuters, AFP/Arab News, Haaretz, The Times of Israel, Al Jazeera;
Reuters/AP, Al Jazeera, Fox News; CNA/Reuters, AP, Al Jazeera, Fox
News). Stories first reported on an earlier day were deliberately
left out: the Iran strike on Bahrain (21 November), the capture of
"El Chapo Isidro" (21 November), the Kryvyi Rih missile (21 November),
BepiColombo reaching Mercury (21 November), the S&P 500's 3.7% Friday
fall (20 November), and the Trump–Xi–Putin trilateral summit
(19–20 November). The Indonesia fire began on Saturday evening, but
its toll was first reported on Sunday.

`draw22.py` renders `entry.png` (1024 × 1024) with Pillow; `main.ts` is
the contest program — it validates the image against the gate's limits
and copies it to `/output/entry.png` in the grading sandbox.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # writes out/entry.png
python3 draw22.py                                     # regenerates entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=d5a50dzy&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
