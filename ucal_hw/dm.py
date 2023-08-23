from ophyd import EpicsMotor
from bluesky.plan_stubs import mv

dm8 = EpicsMotor('XF:07ID2-BI{Diag:08-Ax:Y}Mtr', name='DM8')
dm7 = EpicsMotor('XF:07ID2-BI{Diag:07-Ax:Y}Mtr', name='DM7')

def dm8_out():
    yield from mv(dm8, 150)

def dm8_in_nexafs():
    yield from mv(dm8, 0)
    
def dm8_in_lariat2():
    yield from mv(dm8, 0)

def dm7_out():
    yield from mv(dm7, 85)
    
def dm7_in():
    yield from mv(dm7, 0)
