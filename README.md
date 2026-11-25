# Wednesday 25 November 2026 — The World in One Day

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/rz7mong/makefun-news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/rz7mong/makefun-news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-page newspaper front page summing up Wednesday 25 November
2026's world news — 34 stories, every one dated that day, drawn
entirely in code. Entry for the make.fun bounty
[news-image-20261125](https://make.fun/bounty/news-image-20261125)
($100, 50 places).

## The page

- **1024×1024 PNG**, cream paper, serif masthead, navy/red/gold palette.
- **THE DAY IN NUMBERS** — a six-number stats row: 30 hostages held
  in Cartagena · 1st Pakistani in orbit · −2.6% Nikkei at
  Wednesday's close · 9 Champions League ties tonight · 26 miners
  trapped in Bogor · 168 Tai Po dead, a year on.
- **Region bar** — 4 regions: ASIA-PACIFIC 20 · AMERICAS 8 ·
  EUROPE 4 · MIDEAST 2 = 34 stories.
- **THE DAY IN UTC** — timeline strip: 00:18 Shenzhou launch ·
  03:48 docking · 06:00 Nikkei close · 17:45 UCL · 20:00 UCL night ·
  22:00 NBA · WED Cartagena · WED Solomons.
- **3 lead stories**, each with a large code-drawn illustration:
  1. **All Cartagena hostages freed after 15-hour siege** —
     forces stormed an Éxito supermarket, every hostage freed, one
     captor killed, four detained (Reuters, AFP — REPORTED).
  2. **Shenzhou-24 lifts off with Pakistan's first astronaut** —
     launched 08:18, Muhammad Zeeshan Ali, first Pakistani in orbit
     and first foreigner aboard Tiangong (Reuters, Nature —
     REPORTED).
  3. **Solomons signs Australia pact, bars China bases** — security
     treaty with Australia, "no foreign military base" pledge,
     Canberra named primary security partner (AP, CNN — REPORTED).
- **12 small stories**, each with a small code-drawn illustration:
  Nikkei slides as AI rally reverses (Reuters) · Seoul protests to
  Moscow over jets (Yonhap, AP) · Champions League: 9 ties tonight
  (UEFA) · Tai Po fire: a year on, answers sought (Reuters, HRW) ·
  Rescuers hunt for 26 miners in Bogor (Reuters) · NBA: 9 games
  tonight, Cup night (NBA) · Spain's snap vote: housing on top
  (Reuters) · Oil down 21% in November, Brent $87.49 (Yahoo
  Finance) · Japan services prices jump 4.2% (RTTNews) ·
  Argentina enters technical recession (AFP) · Houthis claim Ras
  Tanura refinery hit (Reuters — CLAIM) · Australia inflation jumps
  to 4.9% (ABS).
- **WHERE IT HAPPENED** — a REAL world map (Natural Earth 110m
  land, filled, no borders) with 15 numbered pins matching the
  story numbers, spread apart so the Europe cluster stays readable.
- **ALSO ON WEDNESDAY 25 NOVEMBER — 19 MORE STORIES** — numbered
  16–34: Cartagena details (30 held at first; 10 released; 1
  captor killed, 4 detained; gang sought $2m ransom) · Shenzhou
  details (launch 08:18; docked ~3.5 hours later; Ali stays 5–10
  days; Tang's 3rd Tiangong trip) · Solomons details (AU$740m over
  10 years; China pact lapses early 2027; treaty needs
  ratification) · SoftBank −13%, Advantest −13%; Kospi −5.05% to
  4,753 · Nvidia −7% on Tuesday · F-15K scrambled, 4 Russian jets;
  3rd KADIZ entry in a week · Sabah v Barcelona 17:45 UTC; PSG v
  Roma 20:00 UTC · Residents return Thu to mark a year.
- **DATE CHECK** — other days' news, deliberately left out and
  labelled with its real day: Senegal AFCON title back (Tue) ·
  Ulleung jet alert (Tue) · Nikkei +3.9% (Tue) · Venezuela debt
  $237.5bn (Tue) · Democrats reach 259 seats (Tue) · Chen Jining
  probe (Tue) · DR Congo plane down (Sun) · Iran flogs singer
  (Mon) · Zambia treason charge (Mon) · Pentagon faults Canada
  (Mon).
- **Footer** — full source list plus a certainty legend: REPORTED =
  carried by the day's wires · CLAIM = one side's account ·
  FORECAST = still to happen when drawn · "Illustrations and map
  drawn in code".

## Date discipline

Every main story is a Wednesday 25 November 2026 event, checked
against a second independent source. Two stories were caught and
swapped out before submitting because their events were actually
Monday 23 November — the Zambia treason indictment and the Pentagon
fact sheet faulting Canada — and both now sit in the DATE CHECK box
instead. Five items that first came from a single dated briefing
were each cross-checked: Brent $87.49 and the −21% monthly move,
Nvidia −7% on Tuesday, and Argentina's technical recession were
confirmed and re-cited to their real sources; the two wrong-dated
items were replaced with Wednesday stories (the Houthi claim on the
Ras Tanura refinery, Reuters + Maritime Executive; Australia's
4.9% CPI, ABS + WSJ + FXStreet). No invented quotes, no
unverifiable claims: every number on the page comes from a named
source, and the Houthi claim is tagged CLAIM because the damage is
unverified.

## Why every picture is drawn in code

The final top 5 of the 22 November edition of this daily bounty all
used illustrations drawn in code — no photos, no AI-generated
images — and said so in their footers. Our photo-first 22 Nov entry
and our photo-plus-AI-illustration 23 Nov entry both missed the
paid places. The 24 Nov code-drawn entry jumped from 2642/7302 in
round 1 to 389/9063 in round 2. This entry follows the same
approach, with one correction from that experiment: the lead panels
are drawn big, dense and dramatic (a night rescue with a
helicopter searchlight, a large rocket launch, a treaty scene with
two national flags), because small, diagram-like lead art was the
weak point of the 24 Nov page. Small panels are each one bold
symbol on a flat background — a falling bar chart, a stadium, a
mine shaft, a refinery, a price tag — checked at display size so
none of them reads as noise.

## Files

- `main.py` — entry point: copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR` (default `/output`). It does not run the
  generator and uses no network.
- `gen_image.py` — the generator: layout, all 34 stories, the
  stats/region/timeline blocks, the real map (Natural Earth 110m
  land polygons, simplified, embedded as `LAND_POLYS`), the ALSO
  list, the DATE CHECK box and the footer. Pure Pillow, fixed
  inputs, no randomness, no network — deterministic.
- `draw_panels.py` — every illustration, drawn with PIL geometric
  primitives only: 3 lead panels (317×148) and 12 small panels
  (156×40). No photos, no AI image generation, no gradients, no
  text inside the illustrations.
- `entry.png` — the finished page, 1024×1024, 189,315 bytes,
  SHA256
  `9a08b42a40ac2d20fbee1a0e8fa61fedc8e4ec049d37924a61576fa6db4a4a56`.

## Run it

```sh
python3 gen_image.py        # writes entry.png (1024x1024, 34 stories)
```

Requires Python 3 with Pillow and the DejaVu fonts
(`/usr/share/fonts/truetype/dejavu/`). Running it twice produces
byte-identical output. The harness runs `main.py`, which only
copies the pre-built `entry.png` to the output directory.

## Sources

Reuters, AFP, AP, CNN, Yonhap, UEFA, NBA, HRW, Nature, RTTNews,
CCTV, WSJ, JBizmNews, Yahoo Finance, Motley Fool, ABS.
