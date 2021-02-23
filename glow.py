import pymem
import pymem.process

dwEntityList = (0x4D4B144)
dwGlowObjectManager = (0x5292F18)
m_iGlowIndex = (0xA428)
m_iTeamNum = (0xF4)
m_EntLoopDist = (0x10)


def main():
    print("Glow has launched.")
    try:
        pm = pymem.Pymem("csgo.exe")
        if pm:
            client = pymem.process.module_from_name(pm.process_handle, "client_panorama.dll").lpBaseOfDll
            while True:
                glow_manager = pm.read_int(client + dwGlowObjectManager)
                for i in range(1, 64):  # Entities 1-64 are reserved for players.
                    entity = pm.read_int(client + dwEntityList + i * m_EntLoopDist)
                    if entity:
                        entity_team_id = pm.read_int(entity + m_iTeamNum)
                        entity_glow = pm.read_int(entity + m_iGlowIndex)
                        if entity_team_id == 2:  # Terrorist
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(1))  # R 
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))   # G
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # B
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))   # Alpha
                            pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)     # Enable glow
                        elif entity_team_id == 3:  # Counter-terrorist
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x4,  float(0))   # R
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8,  float(0))   # G
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC,  float(1))   # B
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))   # Alpha
                            pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)     # Enable glow
    except:
        pass

if __name__ == '__main__':
    main()
