from pathlib import Path
import subprocess
import sys
import json
import time

# Assumes Multi-Agent-Auto-Coder is a sibling of jarvis_network
AUTOCODER_ROOT = Path(__file__).resolve().parents[1] / "Multi-Agent-Auto-Coder"
TASKS_DIR = AUTOCODER_ROOT / "tasks"    


def build_website_from_prompt(prompt: str) -> str:
    """
    Runs the Multi-Agent-Auto-Coder to build a website from a natural language prompt.
    Returns either a deployment URL or an error message.
    """
    if not prompt or not prompt.strip():
        return "The autocoder needs a non-empty website prompt."
    if not AUTOCODER_ROOT.exists():
        return f"I couldn't find the Autocoder project at {AUTOCODER_ROOT}."
    main_path = AUTOCODER_ROOT / "main.py"
    if not main_path.exists():
        return f"Autocoder entrypoint not found at {main_path}."


    TASKS_DIR.mkdir(parents=True, exist_ok=True)

    task = {
        "type": "build_website",
        "original_prompt": prompt.strip(),
        "created_at": time.time(),
    }
    task_file = TASKS_DIR / f"jarvis_task_{int(time.time())}.json"
    try:
        task_file.write_text(json.dumps(task, indent=2), encoding="utf-8")
    except OSError as exc:
        return f"Failed to write task file at {task_file}: {exc}"

    try:
        result = subprocess.run(
            [sys.executable, "main.py", "--task-file", str(task_file)],
            cwd=str(AUTOCODER_ROOT),
            capture_output=True,
            text=True,
            timeout=1800,
        )
    except subprocess.TimeoutExpired:
        return "The autocoder timed out after 30 minutes while building the website."
    except Exception as e:
        return f"The autocoder encountered an error while starting: {e}"

    if result.returncode != 0:
        stderr = (result.stderr or "").strip()
        stdout = (result.stdout or "").strip()
        details = stderr or stdout or "No output captured."
        return f"The autocoder exited with an error:\n{details}"

    for line in result.stdout.splitlines():
        stripped = line.strip()
        if stripped.startswith("DEPLOY_URL:"):
            url = stripped.split("DEPLOY_URL:", 1)[1].strip()
            if url:
                return url

    return (
        "The autocoder finished, but it did not return a deployment URL. "
        "You may need to check the Multi-Agent-Auto-Coder logs or README for deployment details."
    )
