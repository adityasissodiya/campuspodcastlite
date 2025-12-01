# Media Streaming Lite – Campus Podcast Platform

> A 10-week, full-stack learning project: build a simple audio-only “campus podcast” platform from scratch.

---

You (the students) will build a small **podcast-style audio streaming web app**:

- Upload audio files
- List available “episodes”
- Stream and seek within audio (via HTTP range requests)
- Optional: user auth + roles, playlists, moderation

This repository is the **skeleton + specification**. 
**All actual implementation work is done by students.** 
I’m only here to track progress and evaluate.

---

## Project Overview

Your goal is to implement a minimal but realistic **audio streaming platform** suitable for a campus podcast:

- Creators upload audio episodes (e.g. talks, lectures, student podcasts).
- Listeners browse available episodes and play them via a web UI.
- The backend supports **partial content / range requests** so users can **seek** in the audio without re-downloading the entire file.
- Advanced features (auth, playlists, moderation) are optional stretch goals, not required for passing the baseline.

The focus is on:

- End-to-end web development (frontend + backend + “middleware” concerns).
- File handling and basic streaming logic.
- Clean project organization and use of Git/GitHub.

---

## Tech Stack

**Recommended baseline stack (you’re free to propose justified alternatives):**

- **Frontend**
  - HTML5, CSS3
  - Vanilla JavaScript (only as needed, no framework required)
  - HTML5 `<audio>` element for playback

- **Backend**
  - **Python 3.x**
  - **Flask** (minimal web framework)
  - Local file system storage for audio uploads (`uploads/` directory)

- **Data / Persistence**
  - **SQLite** for optional:
    - User accounts (auth)
    - Role management (admin/user)
    - Playlists / metadata, if implemented

- **Dev & Tooling**
  - **Git** for version control
  - **GitHub** for repository hosting
  - **GitHub Projects** (Kanban) for task & sprint management
  - Optional: **Docker** for containerization (only if you have time and capacity)
  - Optional: Free hosting platform for deployment (e.g. Render/Railway/etc.)

---

## Core Features (Minimum Scope)

You should aim to deliver at least the following:

1. **Upload Audio**
   - Web form to upload audio files (e.g. `.mp3`).
   - Files are stored on the server (local `uploads/` directory).
   - Basic validation (e.g. reject non-audio, or at least document the limitation).

2. **List Episodes**
   - A homepage that lists all available audio files.
   - Display at least: “title” (or filename) and maybe simple metadata (duration is bonus).

3. **Playback & Streaming**
   - A page with an HTML5 audio player.
   - Users can **play**, **pause**, and **seek** within audio.
   - Backend returns **HTTP 206 Partial Content** with proper `Range` handling, so seeking works properly.

4. **Local Development**
   - The app runs locally (e.g. `flask run`) with clear instructions in this README.
   - No paid services required.

---

## Stretch Goals (Nice to Have, Not Mandatory)

Only do these if the core is solid:

- **User Accounts & Roles**
  - Simple registration/login
  - “Admin” can upload/delete episodes; “User” can only play

- **Playlists**
  - Create and manage playlists of episodes
  - Auto-play next track when the current one ends

- **Moderation**
  - Admin-only approval/hide for uploaded content

- **UI & UX Polish**
  - Better layout, responsive design, basic branding
  - Search/filter for episodes

- **Deployment / Docker**
  - Simple Dockerfile
  - Deployment to a free hosting platform (if feasible)

---

## Getting Started (High-Level)

> These are **guidelines**. You’ll create the actual files and code.

1. **Fork & Clone**
   - Fork this repo to your personal GitHub account.
   - Clone the fork locally.

2. **Set Up Environment**
   - Install Python 3.x
   - Create a virtual environment
   - Install Flask (and other dependencies you decide on)

3. **Bootstrap the App**
   - Create a minimal Flask app (`app.py`) that serves a “Hello, Media Streaming Lite” page.
   - Commit early, commit often.

4. **GitHub Project Board**
   - Create a **GitHub Projects** board for your fork.
   - Columns: `Backlog`, `In Progress`, `Review`, `Done` (or similar).
   - Translate requirements into issues + cards.

5. **Iterate Feature-by-Feature**
   - Implement core features in increments:
     1. Static UI + `<audio>` tag
     2. Flask routes & templates
     3. File upload
     4. Listing uploaded files
     5. Streaming with range requests
     6. Optional extras (auth, playlists, etc.)

---

## Student Checklist

Use this as a **personal progress checklist**. You’re expected to drive all implementation.

### Week 1–2: Foundations

- [ ] I can run Python and `pip` on my machine.
- [ ] I have a GitHub account and have **forked** this repo.
- [ ] I cloned my fork locally and can push commits.
- [ ] I created a **GitHub Project** board for this project.
- [ ] I created a minimal HTML page with a title and text.
- [ ] I added an HTML5 `<audio>` element that can play a **local sample file** (manually placed).

### Week 3: Backend Skeleton

- [ ] I created a minimal **Flask** app that serves my HTML page on `http://localhost:5000/`.
- [ ] I understand (at least at a high level) what a **route** is (`@app.route('/')`).
- [ ] I can start/stop the server and see log output in the terminal.

### Week 4: File Upload

- [ ] I added an **Upload** page with an HTML form and file input.
- [ ] I use `enctype="multipart/form-data"` on the form.
- [ ] My Flask backend accepts the uploaded file and saves it to an `uploads/` directory.
- [ ] I can see my uploaded file in the filesystem after submitting the form.

### Week 5: Listing & Playing Uploaded Files

- [ ] The home page shows a **list of uploaded audio files**.
- [ ] I use a **template** (e.g. Jinja) to loop over files and render them.
- [ ] Clicking a file or button on the page plays that audio via the `<audio>` player.
- [ ] The entire flow works: upload → see on list → click → play.

### Week 6: Streaming & Seeking

- [ ] I know what an HTTP `Range` request is (at least conceptually).
- [ ] My audio route inspects the `Range` header and returns `206 Partial Content` when appropriate.
- [ ] The browser audio player can **seek** (scrub) within longer audio files without breaking.
- [ ] I tested seeking with a larger audio file (not a tiny 5-second clip).

### Week 7–8: Advanced (Optional)

- [ ] I implemented **user login / logout** (optional).
- [ ] I distinguish at least two roles (e.g. admin vs standard user) (optional).
- [ ] I implemented **playlists** or another meaningful feature beyond the core spec (optional).
- [ ] I updated my UI and README to reflect extra features (optional).

### Week 9: Stabilization

- [ ] I ran through a **manual test plan** (upload, list, play, seek, error cases).
- [ ] I fixed obvious bugs and handled simple edge cases (duplicates, missing files, etc.).
- [ ] My UI is reasonably clean and usable (no completely broken layouts).
- [ ] My code is in version control and pushed to GitHub.

### Week 10: Presentation & (Optional) Deployment

- [ ] I can demo my app end-to-end in a short presentation.
- [ ] My README explains:
  - How to install dependencies
  - How to run the app locally
  - What features are implemented
- [ ] (Optional) I can run my app in a Docker container or on a free hosting platform.
- [ ] I can explain what I learned and what I would do next with more time.

---

## Progress & Reporting

- You are responsible for:
  - Breaking down tasks into GitHub issues.
  - Keeping your Project board up to date.
  - Committing regularly with meaningful messages.
  - Documenting decisions and limitations in the README.

- I will:
  - Review your repository, board, and running app.
  - Track your progress against the **Student Checklist** and course timeline.
  - Evaluate the final state and your explanation of the work.

---

## How to Use This README

- Treat this file as:
  - The **specification** of what you’re expected to build.
  - A **contract** for minimum and stretch goals.
  - A **living document**: you should update it as your implementation deviates, improves, or adds new features.

If you’re not checking items off the checklist week by week, you’re off track.
 
If you are checking them off and your app actually runs, you’re doing the work you’re supposed to be doing.
