# AgentForge — Generalization Gaps for v0.2.0

**Status:** v0.1.0 — functional on BOTASAURUS (Jakebot's dev machine), partially broken on clean installs.

---

## T1 Issues Fixed in This Audit (committed to main)

| # | File | Issue | Fix Applied |
|---|------|-------|-------------|
| 1 | `config.py` | Default `platform` was `"openclaw"` — breaks doctor/status on non-OpenClaw machines | Changed default to `"standalone"` |
| 2 | `config.py` | Default `workspace` was `~/.openclaw/workspace` | Changed to `~/.agentforge` |
| 3 | `config.py` | Default `memory.path` pointed into `~/.openclaw/` | Changed to `~/.agentforge/components/agent-memory-core` |
| 4 | `config.py` | Default `healthkit.path` pointed into `~/.openclaw/` | Changed to `~/.agentforge/components/agent-healthkit` |
| 5 | `runner.py` | Dashboard looked at `config.workspace / "jakebot-dashboard"` (missing `components/`, wrong name) | Fixed to `config.workspace / "components" / "agentforge-dashboard"` |
| 6 | `installer.py` | Referenced `jakebot-dashboard` as repo name and pip package | Renamed to `agentforge-dashboard` throughout |

---

## Remaining Gaps for v0.2.0

### GAP-1 — `agentforge-dashboard` repo doesn't exist (CRITICAL)
- `agentforge install` tries to clone `github.com/JakebotLabs/agentforge-dashboard`
- That repo does not yet exist publicly (it was `jakebot-dashboard`, which is private)
- **Impact:** `agentforge install` fails for all public users
- **Fix:** Publish the dashboard repo as `agentforge-dashboard` OR make the install step skip gracefully when the repo is missing with a clear message

### GAP-2 — `agent-memory-core` and `agent-healthkit` repos are not public (CRITICAL)
- `agentforge install` clones from `github.com/JakebotLabs/agent-memory-core` and `agent-healthkit`
- If these repos are private, clone fails with an auth error (returns a confusing message)
- **Fix:** Make repos public, or add detection + fallback stub installs that work without the full component

### GAP-3 — `agentsforge.dev` install script domain is not live
- README quickstart: `curl -fsSL https://agentsforge.dev/install.sh | bash`
- That domain appears to not be hosting the script yet
- **Impact:** The #1 install path in the README is broken for all new users
- **Fix:** Either deploy the script, or change the primary install method in README to `pip install agentsforge` until the site is live

### GAP-4 — `agentforge start` has no real services to start
- Dashboard, memory, healthkit all return "not installed" on a clean machine
- The start command completes with zero services running and no guidance
- **Impact:** User experience dead-end — "installed" but nothing works
- **Fix:** Add a post-init bootstrapper that creates stub components or links to install docs; `agentforge start` should print actionable next steps when components are missing

### GAP-5 — No `pip install agentsforge` → working state path
- PyPI package is `agentsforge` but the README manual install uses the repo name `agentforge`
- A clean `pip install agentsforge && agentforge init` flow ends with all components "not found"
- Nothing is actually installed (no memory, no healthkit, no dashboard) unless the user also runs `agentforge install` — which then fails due to GAP-1 and GAP-2
- **Fix:** `agentforge init` should self-contain enough to be useful: create the workspace dirs, write a valid config, and show the user exactly what's missing and how to get it

### GAP-6 — OpenClaw adapter: path coupling to Jakebot's env (MINOR)
- `adapters/openclaw.py` hard-codes `~/.openclaw/openclaw.json` for OpenClaw detection
- This is correct for OpenClaw standard install, but should be made into a constant or env-override
- **Fix:** Add `OPENCLAW_HOME` env var support and surface the detected path in `agentforge doctor`

---

## Recommended v0.2.0 Priorities

1. **Publish** `agentforge-dashboard`, `agent-memory-core`, and `agent-healthkit` as public repos
2. **Fix `agentforge init` → usable state** without any cloning (embed a minimal memory stub or link to docs)
3. **Live install script** at `agentsforge.dev/install.sh`
4. **README cleanup:** remove the curl one-liner until the domain is live; promote `pip install agentsforge` as primary

---

## Test Coverage Status

- `tests/test_cli.py` — 6 tests, all passing ✅
- `tests/test_installer.py` — skipped (requires component repos to be cloneable)
- `tests/test_platform.py` — not yet written
- **Missing:** integration test for `agentforge init --platform standalone` on a clean tmpdir
