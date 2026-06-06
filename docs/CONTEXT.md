# Vi-Chi Cognitive Architecture — Context Capsule

> **Paste-ready primer.** Drop this into any model (Gemini / ChatGPT / Grok / Claude) to bootstrap the
> full project state in one paste. Single source of truth: the GitHub repos below.

## What this is

A sovereign, offline-first maritime AI ecosystem for the **Wibo 835 / Project Vento-Vivere** sailboat.

| Module | Was | Role | Yin/Yang | Repo |
|--------|-----|------|----------|------|
| **Urbi** | Cognitive Matrix | inward: memory, dream (ΦΔ), self-audit, coherence | Yin | `Vi-Chi/Urbi` |
| **Orbi** | Omni-AI | outward: orchestration, execution, world I/O | Yang | `Vi-Chi/Orbi` |
| **MΣBUS** (`MEBUS`) | ΣBUS | universal transport/transformer/gateway/translator; **Membrane(Sigma + EBUS)** | the Tao | `Vi-Chi/MEBUS` |
| **Autopoiesis** | — | self-maintaining **polyglot substrate / floor**: watchdog, recovery, + the high-performance runtime (bus hot-path, ICP canisters, GPU networks) | independent | `Vi-Chi/autopoiesis` |

Naming: *Urbi et Orbi* (inward/outward) + Vi's father's two cats. M = Membrane.

## Core design principles

- **Geometric, not linguistic** — internal state is geometry (GSS, ℝ²⁰⁴⁸ manifold); language only at the human membrane.
- **Causal time, not clock** — ordering is a monotonic/causal tick (τ).
- **Tri-state epistemics `[+]/[−]/[=]`** — `=` holds genuine uncertainty. *Model indecision ≠ epistemic uncertainty.*
- **3-6-9 out-of-loop audit (ΦΩ)** · **Dream Layer (ΦΔ)** sub-engines ΦΔ-REC/REP/GEO/COH/CTN · **Tri-state mode (ΦΨ)** WAKE→LIMINAL→DREAM.
- **Provenance mandatory; external models are providers, not oracles.**

## MΣBUS in one screen

`M := (v, σ, π, δ, κ, τ, μ)`. **MΣBUS = Membrane(Sigma + EBUS)** — Sigma = semantics/translation, EBUS = event transport. σ classes: `cm.*` coordination · `m.*` cognition · `ext.*` universal carrier (transport ANYTHING via adapters) · `sys.*` control. **Invariant Ω₈:** action suppressed when μ=DREAM. Adapters translate NMEA/SignalK/JSON/SDR/GUI/model output ↔ typed messages.

## Repos & build bases (private, owner Vi-Chi)

- Scaffolds (GPLv3): `Urbi` `Orbi` `MEBUS` `autopoiesis`.
- Migrate in: `sigmabus` (ΣBUS spec → MEBUS; `sigma-bus-rust/` runtime → **Autopoiesis**) · `cognitive_matrix` (Python v2.1) → Urbi · `omni-ai` → Orbi · `project-autopoiesis` (Motoko/ICP) → Autopoiesis.

## Resolved decisions

GPLv3 everywhere · ΦΔ = REC/REP/GEO/COH/CTN · build MEBUS first · **Languages:** Urbi/Orbi/MΣBUS = Python; **Autopoiesis = polyglot substrate** — Motoko-preferred (open architecture) + Rust (canisters, GPU networks) + future platforms; it hosts the MΣBUS transport hot-path · **GitHub is the source of truth** (a Drive-synced working copy corrupts `.git`; keep git trees off Drive).

## Current status

MΣBUS v0.1 (`Vi-Chi/MEBUS`): protocol spec, schemas, Python reference with Ω₈ + **adapter/translation layer** (transport anything) + PredictionRecord, 16 passing tests.
