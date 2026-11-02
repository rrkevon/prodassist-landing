# ProdAssist — social posting guide

Use this with [SOCIAL-DRAFTS.md](SOCIAL-DRAFTS.md). Images to attach are in **`social-export/`** (generated from `docs/assets/`).

**Primary link (most posts):** https://rrkevon.github.io/prodassist-landing/  
**Closed testers:** https://rozhawebdesigns.com/technologies/Android-testings-rozha-apps/  
**Long walkthrough:** https://rozhawebdesigns.com/technologies/prodassist/v2/

---

## Suggested order (first week)

| Day | Platform | Goal |
|-----|----------|------|
| 1 | **X** + **Facebook** | Public launch post (landing link) |
| 2 | **Instagram** feed + story | Same message; link in bio or sticker |
| 3 | **LinkedIn** (optional) | Slightly longer “builder” angle |
| 4 | **X** Post B | Closed testers (only if you want more testers) |
| 5 | **YouTube Community** | Short update if you use Community tab |

---

## Post 1 — Launch (copy-paste)

### X

**Image:** `social-export/x-facebook-launch-1200x675.png`

```
ProdAssist — pro manual camera for Android: exposure, zebras, HDMI program out, RTMP, plus a Windows companion so your phone is a webcam in OBS & Zoom.

https://rrkevon.github.io/prodassist-landing/

#ProdAssist #Android #MobileFilmmaking #OBS #ContentCreator
```

*(~240 characters with hashtags; trim hashtags if you prefer a cleaner look.)*

### Facebook

**Image:** same as X

Use the paragraph from [SOCIAL-DRAFTS.md](SOCIAL-DRAFTS.md) Facebook section, or:

```
ProdAssist brings cinema-style controls to Android — ISO, shutter, white balance, zebras, Extra Cam, and program HDMI out.

On Windows, the companion turns your phone into a webcam for meetings and streaming.

Learn more: https://rrkevon.github.io/prodassist-landing/
Walkthrough: https://rozhawebdesigns.com/technologies/prodassist/v2/
```

### Instagram feed

**Image (recommended):** `social-export/instagram-launch-1080x1350.png` — full phone UI, letterboxed (nothing cropped).  
Alternate square: `instagram-launch-1080x1080.png` (same fit, not zoom-crop).

**Do not** reuse `x-facebook-launch-1200x675.png` here unless you tap the **aspect-ratio** control on Instagram’s Crop step (bottom-left, two corners) until the whole image fits — square crop will cut the sides.

**If Crop still looks wrong:** cancel, re-upload the `1080x1350` file above; leave zoom at default.

**Caption:**

```
ProdAssist 📱 Pro manual camera on Android — monitoring, streaming, and a Windows companion for OBS/Zoom as your webcam.

Link in bio → landing page

#ProdAssist #MobileFilmmaking #OBS #Android #ContentCreator #LiveStreaming #Webcam
```

**Bio link:** set to `https://rrkevon.github.io/prodassist-landing/` (Linktree or direct URL).

### Instagram story

**Image:** `social-export/instagram-story-launch-1080x1920.png`

Add **Link sticker** → landing URL. Text overlay optional: “ProdAssist — pro Android camera”.

### LinkedIn

**Image:** `social-export/x-facebook-launch-1200x675.png`

Same body as Facebook; add one line: “Built by Rozha Tech — feedback welcome from creators and live streamers.”

---

## Post 2 — Closed testing (when you want more testers)

### X

```
Joining closed testing for ProdAssist? Sign up with the Gmail on your Play Store account (keep the app installed 14 days):

https://rozhawebdesigns.com/technologies/Android-testings-rozha-apps/
```

### WhatsApp / church / small groups

```
ProdAssist — pro camera for Android + Windows webcam companion. Closed test signup (Play Store Gmail): https://rozhawebdesigns.com/technologies/Android-testings-rozha-apps/
```

---

## Post 3 — Companion angle (optional follow-up)

**Image:** `social-export/x-facebook-companion-1200x675.png`

```
Same phone. Pro camera on the go — and on Windows it shows up as a webcam for OBS, Zoom, and Teams. ProdAssist companion + Android app.

https://rrkevon.github.io/prodassist-landing/
```

---

## Before you publish (30-second checklist)

- [ ] Landing page opens on phone: https://rrkevon.github.io/prodassist-landing/
- [ ] Play Store listing opens (public or opt-in link matches what you say in the post)
- [ ] Image attached matches platform size (use `social-export/`)
- [ ] Instagram: bio link updated if you say “link in bio”

---

## Regenerate images

From repo root:

```powershell
python scripts/export-social-images.py
```

*(Script added alongside this guide.)*
