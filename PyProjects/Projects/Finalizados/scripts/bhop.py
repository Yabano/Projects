import pymem
import win32api
import time

LOCAL_PLAYER = 14592396
FORCE_JUMP = 86752472
HEALTH = 256
FLAGS = 260


def bhop() -> None:
    global client
    pm = pymem.Pymem("csgo.exe")

    for module in list(pm.list_modules()):
        if module.name == "client.dll":
            client = module.lpBaseOfDll

    while True:
        time.sleep(0.01)

        if not win32api.GetAsyncKeyState(0x20):
            continue

        local_player: int = pm.read_uint(client + LOCAL_PLAYER)

        if not local_player:
            continue

        if not pm.read_int(local_player + HEALTH):
            continue

        if pm.read_uint(local_player + FLAGS) & 1 << 0:
            pm.write_uint(client + FORCE_JUMP, 6)
            time.sleep(0.01)
            pm.write_uint(client + FORCE_JUMP, 4)


if __name__ == "__main__":
    bhop()
