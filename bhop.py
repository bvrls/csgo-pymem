import keyboard
import pymem
import pymem.process
import time

dwLocalPlayer = (0xD36B94)
m_fFlags = (0x104)
dwForceJump = (0x51F4DC0)

def main():
    print("Bhop has launched.")
    try:
        pm = pymem.Pymem('csgo.exe')
        if pm:
            client = pymem.process.module_from_name(pm.process_handle, 'client_panorama.dll').lpBaseOfDll
            while True:
                time.sleep(0.015) # 0.015625
                player = pm.read_int(client + dwLocalPlayer)
                if player:
                    Flags = pm.read_int(player + m_fFlags) #257 ground, 256 air
                    Jump = pm.read_int(client + dwForceJump) #5 !jumping, 4 jumping
                    if Flags == 257:
                        pm.write_int(client + dwForceJump, 5)
                        time.sleep(0.015)
                        pm.write_int(client + dwForceJump, 4)
    except:
        pass
        print("a")
           
if __name__ == '__main__':
    main()
