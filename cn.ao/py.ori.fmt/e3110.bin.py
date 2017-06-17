from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e3110.bin",                # FileName
        "e3110",                    # MapName
        "e3110",                    # Location
        0x0000,                     # MapIndex
        "ed7515",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e3110",                  # 0
        "清纯的少女",             # 1
        "白隼",                   # 2
        "女性士官",               # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(248, 0)                                        # 0

    ScpFunction((
        "Function_0_F8",           # 00, 0
        "Function_1_108",          # 01, 1
        "Function_2_109",          # 02, 2
        "Function_3_3FA",          # 03, 3
    ))


    def Function_0_F8(): pass

    label("Function_0_F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_107")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_107")

    Return()

    # Function_0_F8 end

    def Function_1_108(): pass

    label("Function_1_108")

    Return()

    # Function_1_108 end

    def Function_2_109(): pass

    label("Function_2_109")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(447)
    SoundLoad(448)
    LoadEffect(0x0, "event\\ev304_00.eff")
    LoadEffect(0x1, "event\\ev304_01.eff")
    LoadEffect(0x2, "event\\ev304_02.eff")
    LoadEffect(0x3, "event\\ev304_03.eff")
    LoadEffect(0x4, "event\\ev304_04.eff")
    LoadEffect(0x5, "event\\ev304_05.eff")
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 15700, 0, 0)
    MoveCamera(312, -21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(80350, 0)
    FadeToBright(500, 0)
    SetCameraDistance(90850, 9000)
    BeginChrThread(0x101, 3, 0, 3)
    Sleep(8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_24D")
    SetMessageWindowPos(40, 230, -1, -1)

    #A0001
    AnonymousTalk(
        0x102,
        (
            "#00102F好漂亮……\x02\x03",

            "米修拉姆好像\x01",
            "每晚都会燃放烟花呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3A9")

    label("loc_24D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_2A0")
    SetMessageWindowPos(40, 230, -1, -1)

    #A0002
    AnonymousTalk(
        0x103,
        (
            "#00202F……真漂亮。\x02\x03",

            "米修拉姆好像\x01",
            "每晚都会燃放烟花呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A9")

    label("loc_2A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_2FA")
    SetMessageWindowPos(40, 230, -1, -1)

    #A0003
    AnonymousTalk(
        0x104,
        (
            "#00309F哈哈，放烟花了啊。\x02\x03",

            "米修拉姆好像\x01",
            "每天晚上都会放呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3A9")

    label("loc_2FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_356")
    SetMessageWindowPos(40, 230, -1, -1)

    #A0004
    AnonymousTalk(
        0x109,
        (
            "#10102F呵呵，真漂亮啊。\x02\x03",

            "米修拉姆好像\x01",
            "每天晚上都会放烟花呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3A9")

    label("loc_356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_3A9")
    SetMessageWindowPos(40, 230, -1, -1)

    #A0005
    AnonymousTalk(
        0x105,
        (
            "#10302F呵呵，很精彩嘛。\x02\x03",

            "这是米修拉姆每天\x01",
            "必有的演出哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3A9")

    SetMessageWindowPos(280, 230, -1, -1)

    #A0006
    AnonymousTalk(
        0x101,
        (
            "#00002F哈哈，我们正好\x01",
            "赶上啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t103B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_109 end

    def Function_3_3FA(): pass

    label("Function_3_3FA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_57B")
    Sleep(300)
    Sound(447, 0, 100, 0)
    Sleep(700)
    PlayEffect(0x5, 0x0, 0xFF, 0x0, 0, 20000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    PlayEffect(0x1, 0x1, 0xFF, 0x0, -5000, 15000, -7000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x0, 0x2, 0xFF, 0x0, 10000, 12000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sound(448, 0, 100, 0)
    Sleep(900)
    PlayEffect(0x3, 0x3, 0xFF, 0x0, 10000, 12000, 7000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x2, 0x5, 0xFF, 0x0, -5000, 15000, -7000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    PlayEffect(0x4, 0x4, 0xFF, 0x0, 0, 18000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("Function_3_3FA")

    label("loc_57B")

    Return()

    # Function_3_3FA end

    SaveToFile()

Try(main)
