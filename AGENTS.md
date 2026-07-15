# Agent Guide

## Scope

This repository is the standalone conversion landing page for **RASMY Studio**, a productized cinematic AI ad-film service. It is separate from `rasmy.co`, Pola Rasmy's director portfolio and authority site.

## Guardrails

- Keep the site dependency-free and deployable as static GitHub Pages HTML.
- Preserve the existing visual direction unless a task explicitly requests design work.
- Never show a successful lead state unless data was actually delivered to a real endpoint.
- Treat prices, credits, client names, and portfolio claims as owner-approved content; do not alter them without explicit approval.
- Do not add secrets, API keys, customer data, or analytics identifiers to the repository.
- Keep external booking links canonical and tagged with `utm_source=rasmy-studio`.

## Validation

Before publishing, verify:

1. HTML links and anchors resolve as intended.
2. Booking and email CTAs work with keyboard focus.
3. The page has no horizontal overflow at 390px or desktop width.
4. GitHub Pages build succeeds and the deployed page returns HTTP 200.
