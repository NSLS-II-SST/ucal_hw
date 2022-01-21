from sst_base.manipulator import Manipulator4AxBase, Manipulator1AxBase
from sst_base.motors import PrettyMotorFMBO
from sst_funcs.geometry.linalg import vec
from ophyd import Component as Cpt


manip_origin = vec(0, 0, 531)


class Manipulator(Manipulator4AxBase):
    x = Cpt(PrettyMotorFMBO, "SampX}Mtr", name="Manipulator X", kind='hinted')
    y = Cpt(PrettyMotorFMBO, "SampY}Mtr",  name="Manipulator Y", kind='hinted')
    z = Cpt(PrettyMotorFMBO, "SampZ}Mtr",  name="Manipulator Z", kind='hinted')
    r = Cpt(PrettyMotorFMBO, "SampTh}Mtr", name="Manipulator R", kind='hinted')


# Check actual PV name


manipulator = Manipulator(None, "XF:07ID1-BI{UCAL-Ax:", origin=manip_origin,
                          name="Manipulator")
