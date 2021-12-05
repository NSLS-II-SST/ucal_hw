from bl_base.detectors import I400
from sst_tes.readable_tes import TES

i400 = I400("XF:07ID-BI{DM2:I400-1}", name="ucal I400-1")
i400 = I400("XF:07ID-BI{DM7:I400-1}", name="DM7 I400")
tes = TES("tes", address="10.66.51.41", port="4000")

# i400 aliases
ref = i400.i1
ref.name = "ref"
# m4drain = i400.i2
# m4drain.name = "m4drain"
sc = i400.i3
sc.name = "sc"

thresholds = {"sc": 2e-11}
