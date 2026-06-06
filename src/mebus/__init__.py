"""MΣBUS — Membrane Sigma Bus (reference implementation, v0.1).

MΣBUS = Membrane(Sigma + EBUS): a universal transport / transformer / gateway / translator.
Sigma = semantics, identity, provenance, trust, translation. EBUS = event/job transport.
M := (v, σ, π, δ, κ, τ, μ) — see docs/PROTOCOL.md.
"""
from .protocol import (
    PROTOCOL_VERSION, Mode, MMessage, MembraneBus, is_action_layer,
    MebusError, SchemaVersionError, InvalidModeError, DreamActionSuppressed,
    MessageValidationError, monotonic_tau,
)
from .adapter import Adapter, AdapterRegistry, JSONAdapter, SignalKAdapter, wrap_external
from .records import PredictionRecord

__all__ = [
    "PROTOCOL_VERSION", "Mode", "MMessage", "MembraneBus", "is_action_layer",
    "MebusError", "SchemaVersionError", "InvalidModeError", "DreamActionSuppressed",
    "MessageValidationError", "monotonic_tau",
    "Adapter", "AdapterRegistry", "JSONAdapter", "SignalKAdapter", "wrap_external",
    "PredictionRecord",
]
__version__ = "0.1.0"
