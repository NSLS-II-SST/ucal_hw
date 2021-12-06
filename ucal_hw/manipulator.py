from bl_base.manipulator import Manipulator4AxBase
from bl_base.motors import PrettyMotorFMBO
from bl_base.sampleholder import SampleHolder
from bl_funcs.geometry.linalg import vec
from ophyd import Component as Cpt


manip_origin = vec(0, 0, 531)

class Manipulator(Manipulator4AxBase):
    x = Cpt(PrettyMotorFMBO, "SampX}Mtr", name="Manipulator X")
    y = Cpt(PrettyMotorFMBO, "SampY}Mtr",  name="Manipulator Y")
    z = Cpt(PrettyMotorFMBO, "SampZ}Mtr",  name="Manipulator Z")
    r = Cpt(PrettyMotorFMBO, "SampTh}Mtr", name="Manipulator R")

manipulator = Manipulator(None, "XF:07ID1-BI{UCAL-Ax:", origin=manip_origin, name="Manipulator")

