import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agent import Agent

def test_summarizer_basic():
    agent = Agent()
    text = "The quick brown fox jumps over the lazy dog. This sentence is often used to test typing or display fonts because it contains every letter of the English alphabet."
    summary = agent.summarize(text)
    # Check for key concepts, not exact phrases
    assert "alphabet" in summary.lower()
    assert ("sentence" in summary.lower() or "typing" in summary.lower() or "font" in summary.lower())

# Add more tests as needed for edge cases, empty input, etc.
