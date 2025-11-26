#!/usr/bin/env python3
"""Convenience script to run benchmarks."""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from benchmark.benchmark import main

if __name__ == "__main__":
    main()
