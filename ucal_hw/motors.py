from bl_base.motors import PrettyMotorFMBO

tesz = PrettyMotorFMBO("XF:07ID1-BI{UCAL-Ax:DetX}Mtr", name = "TES z")
samplex = PrettyMotorFMBO("XF:07ID1-BI{UCAL-Ax:SampX}Mtr", name="Sample X")
sampley = PrettyMotorFMBO("XF:07ID1-BI{UCAL-Ax:SampY}Mtr", name="Sample Y")
samplez = PrettyMotorFMBO("XF:07ID1-BI{UCAL-Ax:SampZ}Mtr", name="Sample Z")
sampler = PrettyMotorFMBO("XF:07ID1-BI{UCAL-Ax:SampTh}Mtr", name="Sample R")

#meshz = PrettyMotorFMBO("XF:07ID1-BI{I0Up-Ax:MMesh}Mtr")


