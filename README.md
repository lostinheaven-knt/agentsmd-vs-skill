# agentsmd-vs-skill

A focused experiment repo comparing **AGENTS.md doc-index driven exploration** vs **skills-style active retrieval** for documentation QA.

This repo is built around a real(ish) help-doc QA scenario using Genstore help documents.

## What’s inside

- `qa_genstore_demo/`: runnable QA eval harness
  - modes: baseline / agents_md (doc-index) / skills (tool search)
  - supports `--mock` (no API calls)
- `blaze-genstore-help-doc-qa/`: documentation corpus used by the harness

## Key idea

> Prefer **retrieval-led reasoning** over **pre-training-led reasoning**.

Instead of hoping the model decides to call a skill/tool, provide a compact **docs index** (AGENTS.md-style) and let the agent:

1. Explore the index
2. Choose a relevant leaf path
3. Open the referenced doc(s)

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run with mock agent (no API key)
python qa_genstore_demo/qa_genstore.py --mock

# Run with real LLM (DeepSeek OpenAI-compatible)
export DEEPSEEK_API_KEY=...
export DEEPSEEK_BASE_URL=https://api.deepseek.com
python qa_genstore_demo/qa_genstore.py

# Run tests
pytest -q
```

## Configuration

Environment variables (optional):

- `DEEPSEEK_API_KEY`: required for real LLM mode
- `DEEPSEEK_BASE_URL`: defaults to `https://api.deepseek.com`
- `QA_KEEP_LAST_QA_PAIRS`: defaults to `1`

## References

- Vercel blog: **“AGENTS.md outperforms skills in our agent evals”** (Jan 27, 2026)
  - https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals

- This repo’s harness is inspired by the general finding that passive, always-available indices can outperform tool-triggered retrieval.

## License

MIT (see `LICENSE`).
