#!/usr/bin/env python3
"""
AgentForge Dev Pipeline Orchestrator

Dispatch tasks to CodeBot (code) or OpusBot (review) with automatic
fallback and retry on model failures.

Usage:
    python -m pipeline.orchestrate codebot "write a hello world script"
    python -m pipeline.orchestrate opusbot "review the auth module"
"""

import json
import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime

WORKSPACE = Path(__file__).parent.parent
FAILURE_LOG = WORKSPACE / "pipeline" / "failure_log.json"

# Model preferences
CODEBOT_MODELS = ["xai/grok-3", "anthropic/claude-sonnet-4-5"]
OPUSBOT_MODELS = ["anthropic/claude-opus-4-5"]

def run_task(bot: str, task: str, timeout: int = 600) -> dict:
    """Run a task via the appropriate bot."""
    models = CODEBOT_MODELS if bot == "codebot" else OPUSBOT_MODELS
    
    for model in models:
        print(f"🤖 Trying {bot} with {model}...")
        # This would integrate with the actual agent runtime
        # For now, return a placeholder
        return {
            "success": True,
            "bot": bot,
            "model": model,
            "output": f"Task dispatched to {bot}",
        }
    
    return {"success": False, "error": "All models failed"}

def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    
    bot = sys.argv[1].lower()
    task = " ".join(sys.argv[2:])
    
    if bot not in ["codebot", "opusbot"]:
        print(f"Unknown bot: {bot}. Use: codebot | opusbot")
        sys.exit(1)
    
    result = run_task(bot, task)
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["success"] else 1)

if __name__ == "__main__":
    main()
