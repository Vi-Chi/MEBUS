# MΣBUS Adapters & Translation — "transport anything"

> MΣBUS = **Membrane(Sigma + EBUS)**. It is not merely a message bus — it is a **universal
> transport / transformer / gateway / translator**. The same core inside; a context-specific
> membrane surface outside. This doc describes the surface.

## The two halves

| Half | Answers | Provides |
|------|---------|----------|
| **Sigma** | *What does this mean? who produced it? can I trust it? how do I translate it?* | identity, semantics, provenance, trust, uncertainty, capability, **translation** |
| **EBUS** | *Where does this go? who handles it? what job does it create? how do we replay it?* | event transport, subscriptions, queues, dispatch, replay, outcome routing |

The **M** is the **Membrane**: the selective interface that adapts to anything outside while the
core stays invariant.

## Carrying anything: the `ext.*` class

The σ signature has a payload class. Alongside `cm.*` (coordination) and `m.*` (cognition), the
**`ext.*`** class is the universal carrier: any foreign payload — NMEA, Signal K, JSON/API, GUI
state, SDR events, model responses, files, raw bytes — crosses the bus **intact**, tagged with its
source in `κ.provenance`, until a translator gives it a typed form.

```python
from mebus import wrap_external
m = wrap_external("nmea", {"sentence": "$GPGGA,..."})   # → σ = "ext.nmea", carried verbatim
```

`ext.*` is data, not action — so it flows even in DREAM (Ω₈ only gates the action layer).

## Translating into typed form: Adapters

An **Adapter** is a bidirectional translator between an external format and an `MMessage`:

```python
class Adapter(ABC):
    name: str
    def ingest(self, external, *, mode=WAKE) -> MMessage: ...   # outside  → bus
    def emit(self, msg: MMessage) -> Any: ...                   # bus      → outside
```

Reference adapters (`src/mebus/adapter.py`):

| Adapter | `ingest` → σ | Role |
|---------|-------------|------|
| `JSONAdapter` | `ext.json` | simplest universal JSON/dict gateway |
| `SignalKAdapter` | `m.state` (domain `maritime.nav`) | translate a Signal K delta into typed maritime cognition |

An `AdapterRegistry` holds the membrane's installed translators. Deployment-specific membranes
(maritime / embedded / industrial) are just adapter sets.

```python
from mebus import AdapterRegistry, JSONAdapter, SignalKAdapter
reg = AdapterRegistry(); reg.register(JSONAdapter()); reg.register(SignalKAdapter())
msg = reg.ingest("signalk", {"path": "navigation.position", "value": {"lat": 52.0}})
```

## Gateway pattern (bridging worlds)

Because adapters translate both directions, MΣBUS is a **gateway**: ingest from transport/format A,
re-`emit` to transport/format B. This is how Orbi (outward/world) and Urbi (inward/cognition) speak
across protocol boundaries, and how external AI providers (Nemotron/OpenAI/Claude/Grok) enter as
`ext.*` / `cm.inform` with `external_model` provenance — evidence, never sensory truth.

## Future adapters (roadmap)

NMEA 0183/2000, MQTT, NATS, MCP tool calls, A2A, SDR/SigMF events, GUI/UI-automation state,
files/logs, vector/embedding state. Each is an `Adapter`; none changes the core.
