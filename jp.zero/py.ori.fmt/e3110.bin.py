from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e3110.bin",                # FileName
        "e3110",                    # MapName
        "e3110",                    # Location
        0x0000,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e3110",                  # 0
    ))

    ScpFunction((
        "Function_0_A0",           # 00, 0
        "Function_1_B0",           # 01, 1
        "Function_2_B1",           # 02, 2
    ))


    def Function_0_A0(): pass

    label("Function_0_A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_AF")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)

    label("loc_AF")

    Return()

    # Function_0_A0 end

    def Function_1_B0(): pass

    label("Function_1_B0")

    Return()

    # Function_1_B0 end

    def Function_2_B1(): pass

    label("Function_2_B1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event\\ev304_00.eff")
    LoadEffect(0x1, "event\\ev304_01.eff")
    LoadEffect(0x2, "event\\ev304_02.eff")
    LoadEffect(0x3, "event\\ev304_03.eff")
    LoadEffect(0x4, "event\\ev304_04.eff")
    LoadEffect(0x5, "event\\ev304_05.eff")
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x151, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 15700, 0, 0)
    MoveCamera(312, -21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(80350, 0)
    FadeToBright(500, 0)
    SetCameraDistance(90850, 9000)
    Sleep(300)
    Sound(916, 0, 100, 0)
    Sleep(700)
    PlayEffect(0x5, 0x0, 0xFF, 0x0, 0, 20000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    PlayEffect(0x1, 0x1, 0xFF, 0x0, -5000, 15000, -7000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x0, 0x2, 0xFF, 0x0, 10000, 12000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sound(917, 0, 100, 0)
    Sleep(900)
    PlayEffect(0x3, 0x3, 0xFF, 0x0, 10000, 12000, 7000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x2, 0x5, 0xFF, 0x0, -5000, 15000, -7000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    PlayEffect(0x4, 0x4, 0xFF, 0x0, 0, 18000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("t105B", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_2_B1 end

    SaveToFile()

Try(main)
