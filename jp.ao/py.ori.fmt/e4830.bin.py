from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4830.bin",                # FileName
        "e4830",                    # MapName
        "e4830",                    # Location
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
        "e4830",                  # 0
        "SE制御",                 # 1
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(200, 0)                                        # 0

    ScpFunction((
        "Function_0_C8",           # 00, 0
        "Function_1_D8",           # 01, 1
        "Function_2_DD",           # 02, 2
        "Function_3_1F8",          # 03, 3
        "Function_4_223",          # 04, 4
        "Function_5_233",          # 05, 5
    ))


    def Function_0_C8(): pass

    label("Function_0_C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_D7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_D7")

    Return()

    # Function_0_C8 end

    def Function_1_D8(): pass

    label("Function_1_D8")

    OP_F0(0x1, 0x7D0)
    Return()

    # Function_1_D8 end

    def Function_2_DD(): pass

    label("Function_2_DD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(941)
    SoundLoad(933)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_68(1560, 0, -336640, 0)
    MoveCamera(212, 11, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(12000, 0)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    OP_70(0x1, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    OP_70(0x0, 0x0)
    Sound(941, 2, 100, 0)
    Sound(933, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x8, 1, 0, 4)
    OP_71(0x0, 0x0, 0x3C, 0x0, 0x0)
    OP_79(0x0)
    Fade(250)
    OP_68(8390, -2270, -24170, 0)
    MoveCamera(330, -9, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(20500, 0)
    BeginChrThread(0x8, 1, 0, 5)
    ClearMapObjFlags(0x1, 0x4)
    OP_71(0x1, 0x0, 0x257, 0x0, 0x20)
    BeginChrThread(0x0, 3, 0, 3)
    Sleep(18000)
    StopSound(941, 1000, 100)
    StopSound(933, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x0, 0x3)
    SetScenarioFlags(0x23, 2)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_DD end

    def Function_3_1F8(): pass

    label("Function_3_1F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_222")
    MoveCamera(343, -4, 0, 10000)
    OP_6F(0x79)
    MoveCamera(330, -9, 0, 10000)
    OP_6F(0x79)
    Jump("Function_3_1F8")

    label("loc_222")

    Return()

    # Function_3_1F8 end

    def Function_4_223(): pass

    label("Function_4_223")

    Sound(940, 0, 100, 0)
    Sleep(1000)
    Sound(255, 0, 100, 0)
    Return()

    # Function_4_223 end

    def Function_5_233(): pass

    label("Function_5_233")

    Sleep(900)
    Sound(251, 0, 50, 0)
    Sound(259, 0, 70, 0)
    Sleep(4200)
    Sound(251, 0, 50, 0)
    Sound(259, 0, 70, 0)
    Sleep(600)
    Sound(251, 0, 50, 0)
    Sound(259, 0, 70, 0)
    Sleep(550)
    Sound(251, 0, 50, 0)
    Sound(259, 0, 70, 0)
    Sleep(2950)
    Sound(251, 0, 50, 0)
    Sound(259, 0, 70, 0)
    Sleep(500)
    Sound(251, 0, 50, 0)
    Sound(259, 0, 70, 0)
    Sleep(2200)
    Sound(251, 0, 50, 0)
    Sound(259, 0, 70, 0)
    Sleep(900)
    Sound(251, 0, 50, 0)
    Sound(259, 0, 70, 0)
    Sleep(1300)
    Sound(251, 0, 50, 0)
    Sound(259, 0, 70, 0)
    Sleep(2000)
    Sound(251, 0, 50, 0)
    Sound(259, 0, 70, 0)
    Sleep(1500)
    Sound(251, 0, 50, 0)
    Sound(259, 0, 70, 0)
    Return()

    # Function_5_233 end

    SaveToFile()

Try(main)
