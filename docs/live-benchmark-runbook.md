# Live Benchmark Runbook

Use this runbook after `.env.adr` exists and the referenced 1Password item has
real provider keys. The live runner skips missing providers by default and keeps
the benchmark category and prompt count small to stay within the `$1` per-call
budget.

## Preflight

```bash
python -m awesome_deep_research.audit
python -m awesome_deep_research.op_env --env-file .env.adr --scope commercial
python -m awesome_deep_research.op_env --op-scaffold --scope commercial
op run --env-file .env.adr -- python -m awesome_deep_research.op_env --live --scope commercial
```

If `op run` reports that `awesome-deep-researchers` is not a vault in this
account, run the 1Password setup in `docs/api-key-signup-checklist.md` before
retrying. That error means the live provider benchmark has not reached API-key
validation yet.

If `--op-scaffold` passes but `--live` reports keys as `not set`, paste real API
keys into the existing `api-keys` fields. The vault and field labels are already
correct in that state.

## Run Low-Cost Live Smoke

```bash
op run --env-file .env.adr -- python benchmark/live_smoke.py -v
```

The default live skills are:

- `you-research` with `research_effort=lite`
- `gemini-deep-research` in grounded Interactions API mode
- `tavily-search` with the benchmark's default bounded query command
- `jina-ai` for low-cost retrieval/reader coverage

Results are written to `benchmark/results/live-smoke/` and successful outputs
are automatically normalized to OKF under `benchmark/results/live-smoke/okf/`.

## Strict Mode

To fail if any requested provider key is missing:

```bash
op run --env-file .env.adr -- python benchmark/live_smoke.py \
  --skills you-research gemini-deep-research perplexity-sonar \
  --fail-missing-env \
  -v
```

## Interpreting Results

For each run, inspect:

- `q1_metrics.json` for duration, estimated or actual cost, and `okf_valid`.
- `q1_output.txt` for raw provider output.
- `okf/<skill>/<category>/...` for the normalized OKF bundle.

If a provider exceeds `$1`, the benchmark marks the run failed unless
`--allow-over-budget` is used on the lower-level benchmark runner.
