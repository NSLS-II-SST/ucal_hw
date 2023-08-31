from sst_base.manipulator import Manipulator4AxBase
from sst_base.motors import FlyableMotor, EpicsMotor
from sst_funcs.geometry.linalg import vec
from ophyd import Component as Cpt

# Note, multimesh is in sst_hw
manip_origin = vec(0, 0, 464, 0)


class Manipulator(Manipulator4AxBase):
    x = Cpt(FlyableMotor, "SampX}Mtr", name="x", kind='hinted')
    y = Cpt(FlyableMotor, "SampY}Mtr",  name="y", kind='hinted')
    z = Cpt(FlyableMotor, "SampZ}Mtr",  name="z", kind='hinted')
    r = Cpt(FlyableMotor, "SampTh}Mtr", name="r", kind='hinted')


def ManipulatorBuilder(prefix, *, name):
    return Manipulator(None, prefix, origin=manip_origin, name=name)

"""
manipulator = Manipulator(None, "XF:07ID1-BI{UCAL-Ax:", origin=manip_origin,
                          name="manip")

manipx = manipulator.x
manipy = manipulator.y
manipz = manipulator.z
manipr = manipulator.r

samplex = manipulator.sx
sampley = manipulator.sy
samplez = manipulator.sz
sampler = manipulator.sr
"""
