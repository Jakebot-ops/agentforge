# AgentForge Dev Pipeline

Two-bot development workflow with automatic failover and retry.

## Bots

### CodeBot
Fast, ship-oriented code engineer.
- Writes clean, minimal code
- Always uses feature branches
- Runs tests before reporting
- Terse, action-focused

**Models:** xai/grok-3 (primary), claude-sonnet-4-5 (fallback)

### OpusBot
Deliberate, thorough architect and reviewer.
- Analysis and recommendations only (no production code)
- Security-focused
- Never rubber-stamps

**Models:** claude-opus-4-5

## Usage

### Direct orchestration
```bash
python -m pipeline.orchestrate codebot "add user auth module"
python -m pipeline.orchestrate opusbot "review auth implementation"
```

### Via AgentForge
```bash
agentforge dispatch codebot "implement feature X"
agentforge dispatch opusbot "review feature X"
```

## Workflow

1. **CodeBot** implements feature on branch
2. **OpusBot** reviews (VERDICT: Ship-ready / Needs fixes / Redesign)
3. **CodeBot** addresses feedback (if any)
4. Human approval → merge

## Failure Handling

- **CodeBot**: Auto-retry on fallback model, then escalate to main agent
- **OpusBot**: Queue review for later (no model downgrade)
- All failures logged to `failure_log.json`

## Integration

Part of AgentForge. Install via:
```bash
agentforge init --install
```

Pipeline is included in the main AgentForge repo (not a separate component).
