import os
import subprocess
import sys


def test_cli_text():
    # construct path relative to this test file
    base_dir = os.path.dirname(__file__)
    script_path = os.path.normpath(os.path.join(base_dir, os.pardir, "jarvis_core.py"))

    proc = subprocess.run(
        [sys.executable, script_path, "--text", "hello"],
        capture_output=True,
        text=True,
    )
    # for the mock orchestrator the output will be str(dict)
    assert "response_text" in proc.stdout
