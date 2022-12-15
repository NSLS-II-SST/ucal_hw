from sst_tes.adr import ADR

adr = ADR(name="adr", address="10.66.48.41", port=5020, client='zmqreq')
adr.rpc.timeout = 10000 # hack to fix adr_gui freeze when measuring alt temp
