# ASTK Testing Repository

A minimal setup for testing AI agents with the **ASTK (Agent Sprint TestKit)** package.

## What's This?

This repository contains a simple AI agent (`simple_agent.py`) and the necessary setup to benchmark it using [ASTK](https://pypi.org/project/agent-sprint-testkit/) - a comprehensive AI agent testing framework.

## Files

- **`simple_agent.py`** - Universal AI agent that handles various question types
- **`requirements.txt`** - ASTK package dependency
- **`astk_env/`** - Virtual environment with ASTK installed
- **`benchmark_results/`** - ASTK test results

## Usage

```bash
# Activate virtual environment
source astk_env/bin/activate

# Run ASTK benchmark
python3 astk_env/lib/python3.13/site-packages/scripts/simple_benchmark.py simple_agent.py
```

## Test Results

ASTK tests the agent across 12 sophisticated scenarios including:

- 🧠 Reasoning & Problem-Solving
- 🎨 Creativity & Innovation
- ⚡ Performance Optimization
- ⚖️ Ethics & Compliance
- 🔗 System Integration
- And more...

Results include success rates, complexity scores, and performance breakdowns by category and difficulty level.

## Note

The ASTK CLI (`astk benchmark`) has a bug in v0.1.2, so we run the benchmark script directly. The core functionality works perfectly.
