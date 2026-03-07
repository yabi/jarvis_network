import json
import logging
import subprocess
import sys

logger = logging.getLogger(__name__)

try:
    import httpx
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "httpx"])
    import httpx


class OllamaClient:
    def __init__(self, host="http://127.0.0.1:11434", model="llama3"):
        self.host = host
        self.model = model

    async def generate(self, prompt, stream=False):
        url = f"{self.host}/api/generate"
        payload = {"model": self.model, "prompt": prompt, "stream": stream}
        try:
            async with httpx.AsyncClient() as client:
                if stream:
                    async with client.stream("POST", url, json=payload) as response:
                        async for line in response.aiter_lines():
                            if line:
                                yield json.loads(line)
                else:
                    resp = await client.post(url, json=payload)
                    yield resp.json()
        except Exception as e:
            logger.error(f"Ollama connection error: {e}")
            yield {"response": "Error connecting to Ollama."}
