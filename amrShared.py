#Contains a bunch of functions that are used across all the scripts.
#==================================================
def writeValueToRom(romname: bytes, address: int, value: int, bytes: int):
	romname.seek(address)
	romname.write(value.to_bytes(bytes,'big'))

def readValueToRom(romname: bytes, address: int, bytes: int) -> bytes:
	romname.seek(address)
	return (romname.read(bytes))
#==================================================