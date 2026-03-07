import logging
import subprocess
import sys

logger = logging.getLogger(__name__)

try:
    import chromadb
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "chromadb"])
    import chromadb


class MemoryInterface:
    def __init__(self, db_path=None):
        self.db_path = db_path
        self.db = f"Chroma DB at {db_path}" if chromadb else None

    def query_similar(self, text):
        return f"[Mock] Query result for '{text}'"
