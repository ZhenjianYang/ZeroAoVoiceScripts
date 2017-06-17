from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c018b.bin",                # FileName
        "c018b",                    # MapName
        "c018b",                    # Location
        0x0005,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "c018b",                  # 0
        "游客",                   # 1
        "游客",                   # 2
        "市民",                   # 3
        "市民",                   # 4
    ))

    AddCharChip((
        "chr/ch33100.itc",                   # 00
        "chr/ch33200.itc",                   # 01
        "chr/ch24500.itc",                   # 02
        "chr/ch22100.itc",                   # 03
    ))

    DeclNpc(-6880,   -200,    4840,    0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-5969,   -200,    5070,    0,    389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-14199,  -200,    6070,    0,    389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-13100,  -200,    5980,    0,    389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)

    ChipFrameInfo(304, 0)                                        # 0

    ScpFunction((
        "Function_0_130",          # 00, 0
        "Function_1_1E0",          # 01, 1
        "Function_2_209",          # 02, 2
        "Function_3_20A",          # 03, 3
        "Function_4_246",          # 04, 4
        "Function_5_26D",          # 05, 5
        "Function_6_2C4",          # 06, 6
    ))


    def Function_0_130(): pass

    label("Function_0_130")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_168"),
        (1, "loc_174"),
        (2, "loc_180"),
        (3, "loc_18C"),
        (4, "loc_198"),
        (5, "loc_1A4"),
        (6, "loc_1B0"),
        (SWITCH_DEFAULT, "loc_1BC"),
    )


    label("loc_168")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_174")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_180")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_18C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_198")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_1A4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_1B0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_1BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_1C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_1DF")

    Return()

    # Function_0_130 end

    def Function_1_1E0(): pass

    label("Function_1_1E0")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Return()

    # Function_1_1E0 end

    def Function_2_209(): pass

    label("Function_2_209")

    Return()

    # Function_2_209 end

    def Function_3_20A(): pass

    label("Function_3_20A")

    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        (
            "这就是夜晚的兰花塔吗……\x01",
            "简直让人震撼到失语呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_20A end

    def Function_4_246(): pass

    label("Function_4_246")

    TalkBegin(0xFE)

    #C0002
    ChrTalk(
        0xFE,
        "呵呵，的确是很美的夜景呢。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_246 end

    def Function_5_26D(): pass

    label("Function_5_26D")

    TalkBegin(0xFE)

    #C0003
    ChrTalk(
        0xFE,
        (
            "虽然夜景确实\x01",
            "十分漂亮……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "但在这种时候，\x01",
            "还是想和喜欢的人一起观赏啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_26D end

    def Function_6_2C4(): pass

    label("Function_6_2C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D")

    #C0005
    ChrTalk(
        0xFE,
        (
            "嗯，好想要个男朋友啊……\x01",
            "……不对！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    TurnDirection(0xB, 0xA, 500)
    Sleep(300)

    #C0006
    ChrTalk(
        0xFE,
        (
            "我正在努力\x01",
            "不去想这种事。\x01",
            "不要说多余的话啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xB)
    OP_93(0xB, 0x0, 0x1F4)
    SetScenarioFlags(0x0, 0)
    Jump("loc_3E5")

    label("loc_35D")


    #C0007
    ChrTalk(
        0xFE,
        (
            "兰花塔好漂亮，\x01",
            "兰花塔好漂亮……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_3E5")

    TalkEnd(0xFE)
    Return()

    # Function_6_2C4 end

    SaveToFile()

Try(main)
