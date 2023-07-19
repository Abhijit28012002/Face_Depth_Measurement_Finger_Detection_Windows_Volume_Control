from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

def Volume(length):
    volume = interface.QueryInterface(IAudioEndpointVolume)
    number=10-length
    Division=-6.525
    vol=number*Division
    vol=round(vol,2)

    volume.SetMasterVolumeLevel(vol, None)