from bl_base.detectors import I400
from sst_tes.readable_tes import TES


dm7_i400 = I400("XF:07ID-BI{DM7:I400-1}", name="DM7 I400")
ucal_i400 = I400("XF:07ID-BI{DM2:I400-1}", name="ucal I400")
m5c_i400 = I400("XF07ID-BI{M5C:I400-1}", name="M5C I400")
tes = TES("tes", address="10.66.51.41", port="4000")

# i400 aliases
ref = ucal_i400.i1
ref.name = "ref"
i1 = m5c_i400.i1
i1.name = "i1"
i0 = ucal_i400.i2
i0.name = "i0"
sc = ucal_i400.i3
sc.name = "sc"

thresholds = {"sc": 2e-11, "i0": 2e-11, "ref": 2e-11, "i1": 2e-11}
