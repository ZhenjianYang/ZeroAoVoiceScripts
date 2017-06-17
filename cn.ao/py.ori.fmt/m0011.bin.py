from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m0011.bin",                # FileName
        "m0011",                    # MapName
        "m0011",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "m0011",                  # 0
        "SE控制",                 # 1
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(192, 0)                                        # 0

    ScpFunction((
        "Function_0_C0",           # 00, 0
        "Function_1_D0",           # 01, 1
        "Function_2_D1",           # 02, 2
        "Function_3_184",          # 03, 3
    ))


    def Function_0_C0(): pass

    label("Function_0_C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_CF")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_CF")

    Return()

    # Function_0_C0 end

    def Function_1_D0(): pass

    label("Function_1_D0")

    Return()

    # Function_1_D0 end

    def Function_2_D1(): pass

    label("Function_2_D1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(931)
    SoundLoad(825)
    SoundLoad(148)
    OP_68(0, 1500, 90000, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(25000, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_70(0x2, 0x14)
    ClearMapObjFlags(0x15, 0x4)
    OP_75(0x15, 0x2, 0x1B58)
    OP_7D(0x7D, 0xFF, 0xCD, 0x0, 0x2328)
    OP_68(0, 1500, 110000, 9000)
    MoveCamera(40, 10, 15, 9000)
    SetCameraDistance(23000, 9000)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x8, 1, 0, 3)
    Sleep(7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("m0101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_D1 end

    def Function_3_184(): pass

    label("Function_3_184")

    Sound(931, 2, 10, 0)
    Sound(825, 2, 10, 0)
    Sound(148, 2, 100, 0)
    Sleep(400)
    Sound(930, 0, 100, 0)
    OP_25(0x3A3, 0x14)
    OP_25(0x339, 0x14)
    Sleep(400)
    OP_25(0x3A3, 0x1E)
    OP_25(0x339, 0x1E)
    Sleep(400)
    OP_25(0x3A3, 0x28)
    OP_25(0x339, 0x28)
    Sleep(400)
    OP_25(0x3A3, 0x32)
    OP_25(0x339, 0x32)
    Sleep(400)
    OP_25(0x3A3, 0x3C)
    OP_25(0x339, 0x3C)
    Sleep(400)
    OP_25(0x3A3, 0x46)
    OP_25(0x339, 0x46)
    Sleep(400)
    OP_25(0x3A3, 0x50)
    OP_25(0x339, 0x50)
    Sleep(400)
    OP_25(0x339, 0x5A)
    Sleep(400)
    OP_25(0x339, 0x64)
    Sleep(3400)
    StopSound(931, 1000, 80)
    StopSound(825, 1000, 100)
    Return()

    # Function_3_184 end

    SaveToFile()

Try(main)
