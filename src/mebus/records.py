"""PredictionRecord — the cognition synapse.

Emitted by Orbi/Urbi agents in WAKE; consumed by the Urbi Dream Layer (ΦΔ) in DREAM.
The unblocking primitive: action → outcome → error → reliability → dream learning.
Carried on MΣBUS as the π of an `m.prediction_record` message.
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Optional

from .protocol import MMessage, Mode


@dataclass
class PredictionRecord:
    record_id: str
    belief_state: dict
    predicted_outcome: dict
    domain: str
    mu_at_time: Mode = Mode.WAKE
    actual_outcome: Optional[dict] = None
    prediction_error: Optional[float] = None     # KL divergence predicted vs actual
    confidence: float = 0.5
    causal_parents: list = field(default_factory=list)

    def to_payload(self) -> dict:
        d = asdict(self)
        d["mu_at_time"] = self.mu_at_time.value
        return d

    def to_message(self, *, destination: str = "urbi", mode: Mode = Mode.WAKE) -> MMessage:
        return MMessage(sigma="m.prediction_record", payload=self.to_payload(),
                        destination=destination, mode=mode).validate()
