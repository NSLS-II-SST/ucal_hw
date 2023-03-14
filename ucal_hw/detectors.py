#from sst_base.detectors import I400
from sst_base.detectors.scalar import I400SingleCh
from sst_tes.readable_tes import TES


#dm7_i400 = I400("XF:07ID-BI{DM7:I400-1}", name="DM7_I400")
#ucal_i400 = I400("XF:07ID-BI{DM2:I400-1}", name="ucal_I400")
#m5c_i400 = I400("XF07ID-BI{M5C:I400-1}", name="M5C_I400")
tes = TES("tes", address="10.66.48.41", path="/nsls2/data/sst/legacy/ucal/raw/%Y/%m/%2d", port=4000)


def rename_cpt(cpt, name):
    cpt.name = cpt.parent.name + "_" + name


# i400 aliases
"""
i0up = ucal_i400.i1
rename_cpt(i0up, "i0up")
ref = ucal_i400.i2
rename_cpt(ref, "ref")
i1 = m5c_i400.i1
rename_cpt(i1, "i1")
i0 = dm7_i400.i3
rename_cpt(i0, "i0")
sc = ucal_i400.i3
rename_cpt(sc, "sc")
dm7_i400.i1.kind = "omitted"
dm7_i400.i2.kind = "omitted"
dm7_i400.i4.kind = "omitted"

#ucal_i400.i2.kind = "omitted"
ucal_i400.i4.kind = "omitted"
"""
#i0 = I400SingleCh("XF:07ID-BI{DM2:I400-1}:IC1_MON", name="ucal_i400_i0up")
i0 = I400SingleCh("XF:07ID-BI[ADC:1-Ch:7]Volt", name="ucal_i0up")
i0.rescale.set(-1)
i0.mean.name = i0.name
#ref = I400SingleCh("XF:07ID-BI{DM2:I400-1}:IC2_MON", name="ucal_i400_ref")
ref = I400SingleCh("XF:07ID-BI[ADC:1-Ch:5]Volt", name="ucal_ref")
ref.rescale.set(-1)
ref.mean.name = ref.name
#sc = I400SingleCh("XF:07ID-BI{DM2:I400-1}:IC3_MON", name="ucal_i400_sc")
sc = I400SingleCh("XF:07ID-BI[ADC:1-Ch:4]Volt", name="ucal_sc")
sc.rescale.set(-1)
sc.mean.name = sc.name
i0mir = I400SingleCh("XF:07ID-BI{DM7:I400-1}:IC3_MON", name="DM7_i400_i0mirror")
i0mir.mean.name = i0mir.name
#thresholds = {sc.name: 2e-11, i0mir.name: 2e-11, ref.name: 2e-11, i0.name: 2e-11}
thresholds = {sc.name: .1, i0mir.name: 2e-11, ref.name: .1, i0.name: .1}
basic_dets = [ref, i0, sc]
#det_devices = [ucal_i400, dm7_i400]
