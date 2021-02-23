import keyboard
import pymem
import pymem.process
import time

dwEntityList = (0x4D4B144)
dwLocalPlayer = (0xD36B94)
m_iTeamNum = (0xF4)
m_bSpotted = (0x93D)
m_EntLoopDist = (0x10)

def main():
    pm = pymem.Pymem('csgo.exe')
    if pm:
        client = pymem.process.module_from_name(pm.process_handle, 'client_panorama.dll').lpBaseOfDll
        while True:
            time.sleep(1)
            if pm.read_int(client + dwLocalPlayer):
                localplayer = pm.read_int(client + dwLocalPlayer)
                localplayer_team = pm.read_int(localplayer + m_iTeamNum)
                for i in range(1, 64):
                    if pm.read_int(client + dwEntityList + i * m_EntLoopDist):
                        entity = pm.read_int(client + dwEntityList + i * m_EntLoopDist)
                        entity_team = pm.read_int(entity + m_iTeamNum)
                        if entity_team != localplayer_team:
                            pm.write_int(entity + m_bSpotted, 1)
if __name__ == '__main__':
    main()
    
