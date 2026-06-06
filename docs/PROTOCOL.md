# MΣBUS Protocol — v0.1 (canonical)

> **MΣBUS = Membrane(Sigma + EBUS).** A universal **transport / transformer / gateway / translator**
> between **Orbi** (outward) and **Urbi** (inward) — not merely a message bus. Environment-agnostic
> core; context-specific membrane adapters. Supersedes ΣBUS / SigmaΣBUS. License: GPL-3.0-or-later.
>
> - **Sigma** = semantics, identity, provenance, trust, uncertainty, capability, **translation**.
> - **EBUS** = event/job transport: subscriptions, queues, dispatch, replay, outcome routing.
> - **M (Membrane)** = the selective surface that adapts to anything outside; same core inside.

This spec **reconciles three earlier message definitions** into one:
1. the MΣBUS repo frame `M := (v, σ, π, δ, κ, τ, μ)` (the outer envelope — canonical here);
2. the ΣBUS-CM Semantic Envelope + AID (rich coordination/trust/provenance detail — lives in `κ` and `cm.*`);
3. the geometric M-tuple (cognition/state — lives in `m.*`).

---

## 1. The seven fields

`M := (v, σ, π, δ, κ, τ, μ)`

| Field | Name | Type | Meaning |
|------|------|------|---------|
| v | version | int | Protocol schema version (currently `1`). |
| σ | signature | str | Payload schema / message-type id, dotted `class.name`. Drives routing **and** payload dispatch. |
| π | payload | object | Message content. Schema determined by σ. |
| δ | destination | str | Target module / agent / path. |
| κ | context | object | Metadata — trust, provenance, expiry (the **ΣBUS-CM Semantic Envelope**: trust_score, provenance, t_expires, anomaly_score). |
| τ | timestamp | int | Monotonic **nanoseconds**. Ordering, not wall-clock. |
| μ | mode | enum | System mode: `WAKE` \| `LIMINAL` \| `DREAM`. |

---

## 2. Signature classes (σ) — one wire, four payload families

σ is `class.name`; the class selects the payload family:

| Class | Purpose | Examples |
|-------|---------|----------|
| `cm.*` | **Coordination** speech-acts (agent↔agent) | `cm.announce` `cm.heartbeat` `cm.query` `cm.inform` `cm.request` `cm.confirm` `cm.fail` `cm.propose` `cm.agree` `cm.refuse` `cm.retract` `cm.delegate` `cm.resume` `cm.alert` `cm.withdraw` |
| `m.*` | **Cognition** state/geometry | `m.state` `m.prediction_record` `m.belief` `m.action` |
| `ext.*` | **Universal carrier** — ANY foreign payload, verbatim | `ext.nmea` `ext.signalk` `ext.json` `ext.sdr` `ext.gui` `ext.model` |
| `sys.*` | **Bus / system** control | `sys.mode` `sys.health` |

`cm.*` carries ΣBUS-CM bodies (envelope in `κ`). `m.prediction_record` is the **cognition synapse**
(emitted WAKE, consumed by the Urbi Dream Layer ΦΔ). `ext.*` is how MΣBUS **transports anything** —
see `docs/ADAPTERS.md` for the translation/gateway layer.

---

## 3. Invariant Ω₈ — mode-gated routing

`μ` is not a passive tag; it **gates the bus**:

| μ | Sensory (in) | Action (out) | Notes |
|---|--------------|--------------|-------|
| **WAKE** | open | open | Full traffic, all σ classes. |
| **LIMINAL** | reduced | held / advisory | Delivered but flagged advisory; T₁-fast instinct watchdog. |
| **DREAM** | gated (monitor) | **SUPPRESSED** | **Ω₈: action-layer messages MUST NOT be delivered.** |

**Ω₈ (hard invariant):** when `μ = DREAM`, any σ in the **action layer** is suppressed (audited, not
delivered). Action layer = `cm.request, cm.confirm, cm.fail, cm.propose, cm.agree, cm.refuse,
cm.retract, cm.delegate, cm.resume, m.action`, and any `cmd.*` path. Cognition (`m.*`), information
(`cm.inform`, `cm.alert`) and carried data (`ext.*`) still flow so consolidation can proceed.

---

## 4. Context (κ) — trust, provenance, freshness

`κ` carries the ΣBUS-CM Semantic Envelope: `trust_score` (0–1), `anomaly_score`, `cross_validated`,
`provenance` (derivation chain), `t_expires` (ns). **Effective trust:**
`clamp(base − age_decay(Δτ) − anomaly·0.5 + (0.1 if cross_validated), 0, 1)`; below `0.1` → discard.
External AI providers enter with `external_model` provenance — evidence, never sensory truth.

---

## 5. Transport, runtime & the Autopoiesis substrate

Transport-agnostic. Reference bindings: **NATS JetStream** (primary/persistent/federated), **ZeroMQ**
(intra-platform low-latency), **MQTT** (IoT/maritime), **serial/HF** (bandwidth-constrained).

**Division of labour:** MΣBUS owns the *protocol + translation* — the seven-field envelope, σ
dispatch, Ω₈, schemas, adapters. The reference implementation (`src/mebus`) is **Python**. The
**high-performance Rust transport runtime is provided by the Autopoiesis substrate** (which also
hosts the ICP economic canisters; `sigma-bus-rust` migrates there). **MΣBUS defines and translates;
Autopoiesis runs it fast.**

---

## 6. Conformance (reference levels, from ΣBUS-CM)

- **L1 Minimal** — envelope + validation + `cm.announce/withdraw/heartbeat/query/inform`.
- **L2 Standard** — + action/negotiation/alert + Ω₈ + conversation state.
- **L3 Gateway** — + delegate/resume + federation + store-and-forward + multi-format adapters.

v0.1 implements the envelope, validation, **Ω₈**, the **adapter/translation layer**, and the
PredictionRecord synapse.

---

## 7. Status

v0.1 foundation: Python reference + adapter/translation layer + 16 passing tests. Next: more adapters
(NMEA/MQTT/MCP/SDR), the `cm.*` payload schemas from the ΣBUS-CM spec, and wiring to the
Autopoiesis-hosted Rust transport runtime.
