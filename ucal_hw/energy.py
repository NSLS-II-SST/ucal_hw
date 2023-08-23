#from sst_hw.energy import EnPos
from sst_hw.new_energy import NewEnPos
from ucal_hw.manipulator import manipulator
import bluesky.plan_stubs as bps
from sst_hw.shutters import psh4


#en = EnPos("", rotation_motor=manipulator.r, name="en")
en = NewEnPos("", rotation_motor=manipulator.r, name="en")
en.scanlock.set(1)


def base_grating_to_250():
    mono_en = en.monoen
    type = mono_en.gratingx.readback.get()
    if '250l/mm' in type:
        print("the grating is already at 250 l/mm")
        return 0  # the grating is already here
    print("Moving the grating to 250 l/mm.  This will take a minute...")
    yield from psh4.close()
    yield from bps.abs_set(mono_en.gratingx, 2, wait=True)
    #yield from bps.sleep(60)
    #yield from bps.mv(mirror2.user_offset, 0.04) #0.0315)
    #yield from bps.mv(grating.user_offset, -0.0874)#-0.0959)
    yield from bps.mv(en.m3offset,7.91)
    yield from bps.mv(mono_en.cff, 1.52)
    yield from bps.mv(en, 270)
    yield from psh4.open()
    print("the grating is now at 250 l/mm signifigant higher order")
    return 1


def base_grating_to_1200():
    mono_en = en.monoen
    type = mono_en.gratingx.readback.get()
    if '1200' in type:
        print("the grating is already at 1200 l/mm")
        return 0  # the grating is already here
    print("Moving the grating to 1200 l/mm.  This will take a minute...")
    yield from psh4.close()
    yield from bps.abs_set(mono_en.gratingx, 9, wait=True)
    #yield from bps.sleep(60)
    #yield from bps.mv(mirror2.user_offset, 0.2044) #0.1962) #0.2052) # 0.1745)  # 8.1264)
    #yield from bps.mv(grating.user_offset, 0.0769) #0.0687) # 0.0777) # 0.047)  # 7.2964)  # 7.2948)#7.2956
    yield from bps.mv(mono_en.cff, 2.05)
    yield from bps.mv(en.m3offset,7.91)
    yield from bps.mv(en, 270)
    yield from psh4.open()
    print("the grating is now at 1200 l/mm")
    return 1
