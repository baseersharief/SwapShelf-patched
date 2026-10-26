# Hosting SwapShelf (public URL for the writeup)

The assignment needs a URL your classmates and instructor can reach. The repo is Docker-ready,
so any container host works. Below is the fastest free path (Render), plus two alternatives.
Pick one, deploy, then paste the resulting URL into the writeup (§Hosted app) and your submission.

## Option A — Render (free, ~5 minutes, recommended)

1. Push this repo to a GitHub repo of your own (public or private):
   ```
   git init && git add . && git commit -m "SwapShelf patched"
   git branch -M main
   git remote add origin https://github.com/baseersharief/swapshelf.git
   git push -u origin main
   ```
2. Go to https://render.com, sign in with GitHub, click **New → Web Service**, and pick the repo.
3. Render detects `render.yaml` (Docker). Accept the defaults and click **Create**. It builds the
   Dockerfile, runs `migrate` + `seed`, and starts gunicorn.
4. In ~2–3 min you get a URL like `https://swapshelf.onrender.com`. That's your hosted URL.

Notes: the free instance sleeps after ~15 min idle and cold-starts on the next hit (fine for a
demo). The SQLite file is ephemeral on the free plan, so it reseeds the demo accounts on each
restart — exactly what you want for grading.

## Option B — Railway (free trial)

1. Push to GitHub (as above).
2. https://railway.app → **New Project → Deploy from GitHub repo** → pick the repo.
3. Railway builds the Dockerfile automatically and injects `PORT` (the Dockerfile already honors it).
4. Under the service → **Settings → Networking → Generate Domain** to get a public URL.

## Option C — Any machine with Docker

```
docker compose up --build        # serves on http://<host>:3000
```
If you run this on a VM with a public IP (AWS EC2, a droplet, UD lab box), open port 3000 and
share `http://<public-ip>:3000`.

## After deploying — verify it's the patched version

Sign in as `alex` / `campus123`, open `/profile/`, and confirm there is **no** "Show my name on the
department board" checkbox. `/desk/` should stay locked for `alex`. That proves the fix shipped.

To create a legitimate department-board (staff) account on the live site, open a shell on the host
and run `python manage.py createsuperuser`, then tick **Staff status** for that user in `/admin/`.
