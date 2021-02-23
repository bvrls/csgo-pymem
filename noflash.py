import keyboard
import pymem
import pymem.process
import time
import sys

dwLocalPlayer = (0xD36B94)
m_flFlashMaxAlpha = (0xA40C)

mask = sys.argv[1] #0-255

def main():
    pm = pymem.Pymem('csgo.exe')
    if pm:
        client = pymem.process.module_from_name(pm.process_handle, 'client_panorama.dll').lpBaseOfDll 
        localplayer = pm.read_int(client + dwLocalPlayer)
        if localplayer:
            flash_value = localplayer + m_flFlashMaxAlpha
            if flash_value:
                pm.write_float(flash_value, float(mask))
                
if __name__ == '__main__':
    main()
