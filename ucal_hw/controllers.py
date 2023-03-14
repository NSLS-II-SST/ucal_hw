from sst_tes.adr import EPICS_ADR

adr = EPICS_ADR('XF:07ID-ES{UCAL:ADR}', name="adr")

#adr.rpc.timeout = 10000 # hack to fix adr_gui freeze when measuring alt temp
