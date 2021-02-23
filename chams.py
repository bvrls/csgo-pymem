import keyboard
import pymem
import pymem.process
import time

dwLocalPlayer = (0xD36B94)
dwEntityList = (0x4D4B144)
m_iTeamNum = (0xF4)
m_EntLoopDist = (0x10)
m_clrRender = (0x70)

def main():
    print("Chams has launched.")
    pm = pymem.Pymem('csgo.exe')
    if pm:
        client = pymem.process.module_from_name(pm.process_handle, 'client_panorama.dll').lpBaseOfDll
        for i in range (1, 32):
            entity = pm.read_int(client + dwEntityList + (i) * m_EntLoopDist)
            if entity:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                if entity_team_id == 2: #Terrorist
                    pm.write_int(entity + m_clrRender + 0x0, 255);   #Red
                    pm.write_int(entity + m_clrRender + 0x1, 0);     #Green
                    pm.write_int(entity + m_clrRender + 0x2, 0);     #Blue
                    pm.write_int(entity + m_clrRender + 0x3, 255);   #Alpha
                elif entity_team_id == 3: #Counter Terrorist
                    pm.write_int(entity + m_clrRender + 0x0, 0);     #Red
                    pm.write_int(entity + m_clrRender + 0x1, 0);     #Green
                    pm.write_int(entity + m_clrRender + 0x2, 255);   #Blue
                    pm.write_int(entity + m_clrRender + 0x3, 255);   #Alpha
                        
if __name__ == '__main__':
    main()
    
