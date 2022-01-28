from sst_base.detectors import I400
from sst_tes.readable_tes import TES


dm7_i400 = I400("XF:07ID-BI{DM7:I400-1}", name="DM7_I400")
ucal_i400 = I400("XF:07ID-BI{DM2:I400-1}", name="ucal_I400")
m5c_i400 = I400("XF07ID-BI{M5C:I400-1}", name="M5C_I400")
tes = TES("tes", address="10.66.48.41", path="/home/pcuser/data", port=4000)


def rename_cpt(cpt, name):
    cpt.name = cpt.parent.name + "_" + name


# i400 aliases
ref = ucal_i400.i2
rename_cpt(ref, "ref")
i1 = m5c_i400.i1
rename_cpt(i1, "i1")
i0 = dm7_i400.i2
rename_cpt(i0, "i0")
sc = ucal_i400.i3
rename_cpt(sc, "sc")
dm7_i400.i1.kind = "omitted"
dm7_i400.i3.kind = "omitted"
dm7_i400.i4.kind = "omitted"

ucal_i400.i2.kind = "omitted"
ucal_i400.i4.kind = "omitted"

thresholds = {sc.name: 2e-11, i0.name: 2e-11, ref.name: 2e-11, i1.name: 2e-11}
basic_dets = [ref, i0, sc]
det_devices = [ucal_i400, dm7_i400]
