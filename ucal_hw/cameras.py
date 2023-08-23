from sst_base.cameras import StandardProsilicaV33

bpm8 = StandardProsilicaV33("XF:07ID-BI{BPM:8}", name="BPM8")
bpm8.stage_sigs['cam.image_mode'] = 0
bpm8.stats1.kind = 'hinted'

bpm14 = StandardProsilicaV33("XF:07ID-BI{BPM:14}", name="BPM14")
bpm14.stage_sigs['cam.image_mode'] = 0
bpm14.stats1.kind = 'hinted'

