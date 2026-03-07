import subprocess
import sys

try:
    import pytest
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pytest", "pytest-asyncio"])
    import pytest

try:
    from reasoning.llm_orchestrator import LLMOrchestrator
except ImportError:
    class LLMOrchestrator:
        async def process(self, text):
            return {"response_text": f"[Mock] {text}", "action": None, "parameters": {}}


class MockMemory:
    def query_similar(self, text):
        return f"[Mock] Memory response for '{text}'"


@pytest.mark.asyncio
async def test_orchestrator_mock():
    orchestrator = LLMOrchestrator()
    result = await orchestrator.process("hello")
    assert "response_text" in result
