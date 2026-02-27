"""Dev pipeline component — CodeBot, OpusBot, and orchestrator."""

from pathlib import Path


def get_pipeline_root(workspace: Path) -> Path:
    """Return the root of the cloned pipeline repo."""
    return Path(workspace) / "components" / "pipeline"


def check_pipeline(workspace: Path) -> dict:
    """Check if the dev pipeline is installed.

    The pipeline is cloned by the installer into workspace/components/pipeline/.
    Inside that clone, the Python package lives at pipeline/orchestrate.py.
    """
    repo_root = get_pipeline_root(workspace)
    orchestrator = repo_root / "pipeline" / "orchestrate.py"

    if orchestrator.exists():
        return {"installed": True, "path": str(repo_root)}
    return {"installed": False, "path": None}


def get_pipeline_status(workspace: Path) -> dict:
    """Get pipeline health status for the status command."""
    check = check_pipeline(workspace)
    if check["installed"]:
        return {
            "healthy": True,
            "status": "Ready",
            "details": "CodeBot + OpusBot available",
        }
    return {
        "healthy": None,  # None = not an error, just not available
        "status": "Pro feature",
        "details": "github.com/sponsors/JakebotLabs",
    }
