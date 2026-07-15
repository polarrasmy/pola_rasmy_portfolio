# RASMY Studio Project State

Last baseline: 2026-07-15

## Purpose

Standalone service landing page for cinematic AI ad films. `rasmy.co` remains the separate portfolio and authority site for film director Pola Rasmy.

## Current architecture

- Static, dependency-free `index.html`.
- Hosted by GitHub Pages from `main` at <https://polarrasmy.github.io/rasmy-studio/>.
- No application backend or lead-storage endpoint.
- Booking handoff uses the owner's public Calendly; email is the fallback.

## Verified baseline

- GitHub Pages build and deployment succeeded before this change.
- The public page returned HTTP 200 over HTTPS.
- The repository had one source commit, no README, no package scripts or automated quality tests, and no branch protection.

## Current priority

Make conversion honest and functional: never simulate a successful email submission. Keep booking CTAs linked to the canonical Calendly URL with studio-specific UTM parameters.

## Remaining risks

- Showreel is still a visual placeholder rather than playable work.
- Client and credit claims have no linked proof or case studies on this page.
- Social sharing metadata, canonical URL, favicon, and structured data are absent.
- Accessibility and responsive behavior have no automated regression checks.

## Next recommended task

Replace the showreel placeholder with one owner-approved, captioned reel or case-study link, then verify playback, keyboard access, reduced-motion behavior, and mobile layout.
