from bl_base.manipulator import ManipulatorBase
from bl_base.motors import PrettyMotorFMBO
from bl_base.sampleholder import SampleHolder
from ophyd import Component as Cpt

class Manipulator(ManipulatorBase):
    x = Cpt(PrettyMotorFMBO, "PlaceholderX")
    y = Cpt(PrettyMotorFMBO, "PlaceholderY")
    z = Cpt(PrettyMotorFMBO, "PlaceholderZ")
    r = Cpt(PrettyMotorFMBO, "PlaceholderR")

bar = SampleHolder(name="Sample Holder")
# manipulator = Manipulator(bar, "MCS8:PREFIX:PLACEHOLDER:", name="Manipulator")

