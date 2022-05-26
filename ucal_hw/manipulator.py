from sst_base.manipulator import Manipulator4AxBase
from sst_base.motors import EpicsMotor
from sst_funcs.geometry.linalg import vec
from ophyd import Component as Cpt

# Note, multimesh is in sst_hw
manip_origin = vec(0, 0, 464, 0)


class Manipulator(Manipulator4AxBase):
    x = Cpt(EpicsMotor, "SampX}Mtr", name="x", kind='hinted')
    y = Cpt(EpicsMotor, "SampY}Mtr",  name="y", kind='hinted')
    z = Cpt(EpicsMotor, "SampZ}Mtr",  name="z", kind='hinted')
    r = Cpt(EpicsMotor, "SampTh}Mtr", name="r", kind='hinted')


manipulator = Manipulator(None, "XF:07ID1-BI{UCAL-Ax:", origin=manip_origin,
                          name="Manipulator")

manipx = manipulator.x
manipx.name = "manipx"
manipy = manipulator.y
manipy.name = "manipy"
manipz = manipulator.z
manipz.name = "manipz"
manipr = manipulator.r
manipr.name = "manipr"

samplex = manipulator.sx
samplex.name = "samplex"
sampley = manipulator.sy
sampley.name = "sampley"
samplez = manipulator.sz
samplez.name = "samplez"
sampler = manipulator.sr
sampler.name = "sampler"
