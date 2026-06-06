import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from mebus import (
    MMessage, Mode, MembraneBus, AdapterRegistry, JSONAdapter,
    SignalKAdapter, wrap_external, PredictionRecord,
)


class TestAdapters(unittest.TestCase):
    def test_wrap_external_anything(self):
        m = wrap_external("nmea", {"sentence": "$GPGGA,..."})
        self.assertEqual(m.sigma, "ext.nmea")
        self.assertEqual(m.sigma_class, "ext")
        self.assertIn("nmea", m.context["provenance"])
        m.validate()

    def test_json_adapter_roundtrip(self):
        a = JSONAdapter()
        m = a.ingest('{"k": 1}')
        self.assertEqual(m.sigma, "ext.json")
        self.assertEqual(m.payload, {"k": 1})
        self.assertEqual(a.emit(m), '{"k": 1}')

    def test_signalk_translation(self):
        a = SignalKAdapter()
        m = a.ingest({"path": "navigation.position", "value": {"lat": 52.0}, "source": "gps0"})
        self.assertEqual(m.sigma, "m.state")
        self.assertEqual(m.context["domain"], "maritime.nav")
        self.assertEqual(a.emit(m)["path"], "navigation.position")

    def test_registry(self):
        r = AdapterRegistry()
        r.register(JSONAdapter())
        r.register(SignalKAdapter())
        self.assertEqual(r.ingest("json", {"a": 2}).payload, {"a": 2})


class TestPredictionRecord(unittest.TestCase):
    def test_to_message_routes(self):
        bus = MembraneBus()
        got = []
        bus.subscribe("m.prediction_record", lambda m: got.append(m))
        pr = PredictionRecord(record_id="r1", belief_state={"region": "A"},
                              predicted_outcome={"v": 1}, domain="maritime.nav", confidence=0.8)
        self.assertTrue(bus.publish(pr.to_message()))
        self.assertEqual(got[0].payload["domain"], "maritime.nav")
        self.assertEqual(got[0].payload["mu_at_time"], "WAKE")

    def test_ext_passes_in_dream(self):
        bus = MembraneBus()
        got = []
        bus.subscribe("ext.nmea", lambda m: got.append(m))
        self.assertTrue(bus.publish(wrap_external("nmea", {"s": 1}, mode=Mode.DREAM)))


if __name__ == "__main__":
    unittest.main()
