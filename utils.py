from sounddevice import query_devices,DeviceList
def GetDeviceNumber():
    devices = query_devices()
    input = 0
    output=0
    assert isinstance(devices, DeviceList)
    for device in devices:
        assert isinstance(device, dict)
        if device['name'] == 'CABLE Input (VB-Audio Virtual Cable)' and device['hostapi'] == 1:
            output = device['index']
        if device['name'] == 'CABLE Output (VB-Audio Virtual Cable)' and device['hostapi'] == 1:
            input = device['index']
    return (input,output)

if __name__ == "__main__":
    GetDeviceNumber()