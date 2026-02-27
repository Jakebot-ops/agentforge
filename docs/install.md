# Installation

## Requirements

- **Python 3.10+** — [Download](https://python.org/downloads/)
- **git** — [Download](https://git-scm.com/downloads)
- **pip** and **venv** modules (usually included with Python)

## One Command Install

```bash
curl -fsSL https://agentsforge.dev/install.sh | bash
```

This will:
1. Check Python 3.10+ and git are available
2. Clone AgentForge to `~/.agentforge`
3. Create an isolated Python environment
4. Install the `agentforge` command to `~/.local/bin`
5. Run diagnostics to verify everything works

### Install Options

```bash
# Include Agent Mailbox for multi-agent coordination
curl -fsSL https://agentsforge.dev/install.sh | bash -s -- --mailbox

# Force upgrade existing installation
curl -fsSL https://agentsforge.dev/install.sh | bash -s -- --upgrade

# Custom install location
AGENTFORGE_HOME=/opt/agentforge curl -fsSL https://agentsforge.dev/install.sh | bash
```

## npm Package (Node.js Projects)

For Node.js/TypeScript projects, use the HealthKit npm package:

```bash
npm install @agentsforge/healthkit
```

```javascript
import { HealthKit } from '@agentsforge/healthkit';

const health = new HealthKit();
await health.check();
```

## pip Package (Python Projects)

```bash
pip install agentforge
```

Then initialize and start:

```bash
agentforge init      # Configure platform and components
agentforge start     # Launch services
agentforge status    # Check what's running
agentforge doctor    # Diagnose issues
```

## Agent Mailbox (Multi-Agent Coordination)

For multi-agent systems, install the Agent Mailbox:

```bash
git clone https://github.com/JakebotLabs/agent-mailbox.git ~/.openclaw/mailbox
cd ~/.openclaw/mailbox
python mailbox.py --agent <your-agent-id> onboard
```

Or include it during install:

```bash
curl -fsSL https://agentsforge.dev/install.sh | bash -s -- --mailbox
```

## Platform Detection

The installer automatically detects your agent platform:

| Platform | Detection | Behavior |
|----------|-----------|----------|
| **OpenClaw** | `openclaw` command + `~/.openclaw/openclaw.json` | Uses existing workspace paths |
| **LangChain** | `import langchain` succeeds | Configures LangChain integration |
| **Standalone** | Default | Full isolation in `~/.agentforge` |

## Manual Installation

If the one-liner doesn't work for your environment:

```bash
# Clone the repo
git clone https://github.com/JakebotLabs/agentforge.git
cd agentforge

# Create venv and install
python3 -m venv venv
source venv/bin/activate
pip install -e .

# Verify
agentforge --version
agentforge doctor
```

## Troubleshooting

### "Python 3.10+ required"

```bash
# Ubuntu/Debian
sudo apt-get install python3.12 python3.12-venv python3-pip

# macOS
brew install python@3.12

# Windows
# Download from https://python.org/downloads/
```

### "agentforge command not found"

The command is installed to `~/.local/bin`. Either:

```bash
# Add to current session
export PATH="$HOME/.local/bin:$PATH"

# Or open a new terminal
```

### "Permission denied"

Don't run with `sudo`. The installer uses `~/.local/bin` which doesn't require root.

## Uninstall

```bash
rm -rf ~/.agentforge
rm ~/.local/bin/agentforge
```

---

**Need help?** Open an issue at [github.com/JakebotLabs/agentforge](https://github.com/JakebotLabs/agentforge/issues)
