from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0210.bin",                # FileName
        "c0210",                    # MapName
        "c0210",                    # Location
        0x000B,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 11, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0210",                  # 0
        "奥斯卡",                 # 1
        "摩尔吉",                 # 2
        "贝奈特",                 # 3
        "卡缇莉娜",               # 4
        "琪露露",                 # 5
        "塔利兹",                 # 6
        "爱尔莎",                 # 7
        "小桃",                   # 8
        "皮特",                   # 9
    ))

    AddCharChip((
        "chr/ch07000.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch34300.itc",                   # 02
        "chr/ch24500.itc",                   # 03
        "chr/ch20500.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch24800.itc",                   # 06
        "chr/ch10400.itc",                   # 07
        "chr/ch20700.itc",                   # 08
        "chr/ch22200.itc",                   # 09
    ))

    DeclNpc(56290,   0,       2019,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(119120,  0,       -660,    275,  261,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(51279,   1000,    12869,   90,   261,  0x0, 0,   2,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(58540,   0,       -2329,   0,    261,  0x0, 0,   3,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(57799,   0,       -2200,   0,    389,  0x0, 0,   4,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(200,     0,       8500,    180,  261,  0x0, 0,   6,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(3089,    0,       4199,    90,   261,  0x0, 0,   7,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(3089,    0,       4199,    90,   261,  0x0, 0,   8,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(2589,    0,       1830,    90,   389,  0x0, 0,   9,   0,   0,   0,   0,   25,  255,  0)

    DeclActor(54900,   0,       1720,    1000,    56290,   1500,    2020,    0x007E, 0,  5,  0x0000)
    DeclActor(300,     0,       6960,    1000,    200,     1500,    8500,    0x007E, 0,  20, 0x0000)
    DeclActor(-72380,  0,       8250,    1200,    -72380,  2450,    8250,    0x007C, 0,  4,  0x0000)

    ChipFrameInfo(668, 0)                                        # 0

    ScpFunction((
        "Function_0_29C",          # 00, 0
        "Function_1_34C",          # 01, 1
        "Function_2_377",          # 02, 2
        "Function_3_662",          # 03, 3
        "Function_4_6BF",          # 04, 4
        "Function_5_768",          # 05, 5
        "Function_6_782",          # 06, 6
        "Function_7_8D9",          # 07, 7
        "Function_8_1D0C",         # 08, 8
        "Function_9_1FEC",         # 09, 9
        "Function_10_20A2",        # 0A, 10
        "Function_11_215D",        # 0B, 11
        "Function_12_220F",        # 0C, 12
        "Function_13_2FF5",        # 0D, 13
        "Function_14_30D9",        # 0E, 14
        "Function_15_335E",        # 0F, 15
        "Function_16_3FC7",        # 10, 16
        "Function_17_418C",        # 11, 17
        "Function_18_4AD1",        # 12, 18
        "Function_19_4B63",        # 13, 19
        "Function_20_4BE4",        # 14, 20
        "Function_21_4BE8",        # 15, 21
        "Function_22_589B",        # 16, 22
        "Function_23_5EBD",        # 17, 23
        "Function_24_5F69",        # 18, 24
        "Function_25_6275",        # 19, 25
        "Function_26_6858",        # 1A, 26
        "Function_27_7A87",        # 1B, 27
        "Function_28_7EF9",        # 1C, 28
        "Function_29_8DB3",        # 1D, 29
    ))


    def Function_0_29C(): pass

    label("Function_0_29C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_2D4"),
        (1, "loc_2E0"),
        (2, "loc_2EC"),
        (3, "loc_2F8"),
        (4, "loc_304"),
        (5, "loc_310"),
        (6, "loc_31C"),
        (SWITCH_DEFAULT, "loc_328"),
    )


    label("loc_2D4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_2E0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_2EC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_2F8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_304")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_310")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_31C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_328")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_334")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_34B")

    Return()

    # Function_0_29C end

    def Function_1_34C(): pass

    label("Function_1_34C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_376")
    OP_94(0xFE, 0xFFFFF308, 0x438, 0x7ED, 0x10B8, 0x3E8)
    Sleep(300)
    Jump("Function_1_34C")

    label("loc_376")

    Return()

    # Function_1_34C end

    def Function_2_377(): pass

    label("Function_2_377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_39B")
    SetChrPos(0xE, -65370, 0, 2009, 90)
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_39B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3E6")
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xA, 123090, 0, 580, 90)
    SetChrPos(0xE, -68850, 0, -980, 0)
    SetChrPos(0xF, -68700, 0, 340, 180)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_652")

    label("loc_3E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_405")
    SetChrPos(0xE, -65370, 0, 2009, 90)
    Jump("loc_652")

    label("loc_405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_440")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xA, 56290, 0, 2020, 270)
    SetChrPos(0xE, -65370, 0, 2009, 90)
    BeginChrThread(0xF, 0, 0, 1)
    Jump("loc_652")

    label("loc_440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_45D")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_45D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4A8")
    SetChrPos(0xA, 51280, 1000, 12870, 180)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xE, -65370, 0, 2009, 90)
    SetChrPos(0xF, 51240, 1000, 11020, 0)
    SetChrFlags(0xF, 0x10)
    Jump("loc_652")

    label("loc_4A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4C5")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_4C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_522")
    SetChrPos(0x9, 51280, 1000, 12870, 90)
    SetChrPos(0xA, 119120, 0, -660, 275)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_513")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_513")

    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_535")
    SetChrFlags(0xE, 0x80)
    Jump("loc_652")

    label("loc_535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_548")
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_58C")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xE, -68850, 0, -980, 0)
    SetChrFlags(0xE, 0x10)
    SetChrPos(0xF, -68700, 0, 340, 180)
    SetChrFlags(0xF, 0x10)
    Jump("loc_652")

    label("loc_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5A4")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_5A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E3")
    SetChrPos(0x9, 51280, 1000, 12870, 90)
    SetChrPos(0xA, 119120, 0, -660, 275)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_63F")
    SetChrPos(0xE, -65370, 0, 2009, 90)
    SetChrPos(0xA, 52620, 0, 4250, 90)
    SetChrPos(0xF, 53630, 0, 4250, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_63A")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xF, 0x10)

    label("loc_63A")

    Jump("loc_652")

    label("loc_63F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_652")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)

    label("loc_652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_661")
    ClearScenarioFlags(0x22, 0)
    Event(0, 27)

    label("loc_661")

    Return()

    # Function_2_377 end

    def Function_3_662(): pass

    label("Function_3_662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_695")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BE")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)

    label("loc_6BE")

    Return()

    # Function_3_662 end

    def Function_4_6BF(): pass

    label("Function_4_6BF")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "放置着『点心王国　第一卷』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_764")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_764")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『混合冰激凌』\x07\x00",
            "的做法已经记下来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_764")

    TalkEnd(0xFF)
    Return()

    # Function_4_6BF end

    def Function_5_768(): pass

    label("Function_5_768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_77E")
    Call(0, 13)
    Jump("loc_781")

    label("loc_77E")

    Call(0, 6)

    label("loc_781")

    Return()

    # Function_5_768 end

    def Function_6_782(): pass

    label("Function_6_782")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7B9")
    Call(0, 28)
    Return()

    label("loc_7B9")

    Jump("loc_7E3")

    label("loc_7BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E3")
    Call(0, 26)
    Return()

    label("loc_7E3")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D5")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_840")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_840")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_85F")
    OP_AF(0xCC)
    Jump("loc_891")

    label("loc_85F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_86F")
    OP_AF(0xCB)
    Jump("loc_891")

    label("loc_86F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_87F")
    OP_AF(0xCA)
    Jump("loc_891")

    label("loc_87F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_88F")
    OP_AF(0xC9)
    Jump("loc_891")

    label("loc_88F")

    OP_AF(0xC8)

    label("loc_891")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D0")

    label("loc_8A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B4")
    Jump("loc_8D0")

    label("loc_8B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)

    label("loc_8D0")

    Jump("loc_7F0")

    label("loc_8D5")

    TalkEnd(0x8)
    Return()

    # Function_6_782 end

    def Function_7_8D9(): pass

    label("Function_7_8D9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F4")
    Call(0, 8)
    Jump("loc_1D0B")

    label("loc_8F4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_90F")
    Call(0, 9)
    Jump("loc_1D0B")

    label("loc_90F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92A")
    Call(0, 10)
    Jump("loc_1D0B")

    label("loc_92A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_945")
    Call(0, 11)
    Jump("loc_1D0B")

    label("loc_945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_9D6")

    #C0003
    ChrTalk(
        0x8,
        (
            "那个『鲜嫩猪排三明治』只是试做品，\x01",
            "并没在店里出售。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "我本想推荐贝奈特\x01",
            "做的面包，可她却……\x01",
            "哎，女人的心思真是难以理解啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D0B")

    label("loc_9D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5F")

    #C0005
    ChrTalk(
        0x8,
        "哦，来了啊！\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "我这次特意为你们\x01",
            "制作了新品面包。\x01",
            "来，拿去吧！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x214),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('最终旅途', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0008
    ChrTalk(
        0x101,
        "#00002F哎，这面包闻起来好香。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        "#00109F嗯，好像非常美味呢¤\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "哈哈，对吧。\x01",
            "这是我最近的最佳作品。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "你们大概需要面对很多\x01",
            "艰难的挑战吧，吃掉这个，\x01",
            "然后努力解决掉这异常的事态吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00000F嗯……\x01",
            "谢了，奥斯卡。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 4)
    Jump("loc_C9A")

    label("loc_B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C10")

    #C0013
    ChrTalk(
        0x8,
        (
            "在这种时候，\x01",
            "我希望更多的人\x01",
            "来品尝我做的面包。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "我所能做到的事，\x01",
            "只有做出好吃的面包……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "只要能使食客的\x01",
            "不安心情稍有减轻，\x01",
            "就是最令我开心的事了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C9A")

    label("loc_C10")


    #C0016
    ChrTalk(
        0x8,
        (
            "不管在什么时候，\x01",
            "不断制作美味的面包\x01",
            "都是我们最重要的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "对我来说，只要能使食客的\x01",
            "不安心情稍有减轻，\x01",
            "就是最开心不过的事情了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9A")

    Jump("loc_1D0B")

    label("loc_C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_E7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1F")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0018
    ChrTalk(
        0x8,
        "这不是……罗伊德吗！？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#00000F奥斯卡……\x01",
            "太好了，看来你平安无事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "哦哦，我们当然不要紧……\x01",
            "你们也都没什么事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "对了，罗伊德，\x01",
            "你不是被指名通缉了……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#00006F啊……嗯嗯……\x01",
            "说来话长。\x02\x03",

            "#00000F总之，奥斯卡，\x01",
            "你们暂时一定不要\x01",
            "出去。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "嗯……\x01",
            "虽然不知道是怎么回事，\x01",
            "但我知道了。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "罗伊德，\x01",
            "你们也要小心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 3)
    Jump("loc_E77")

    label("loc_E1F")


    #C0025
    ChrTalk(
        0x8,
        (
            "虽然不知道是怎么回事，\x01",
            "但你们平安无事，我就放心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "罗伊德，\x01",
            "你们也要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E77")

    Jump("loc_1D0B")

    label("loc_E7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_FE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5A")

    #C0027
    ChrTalk(
        0x8,
        (
            "受到铁路货运停止的影响，\x01",
            "我们储备的面包材料\x01",
            "都快用光了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "不过毕竟还有阿尔摩利卡村，\x01",
            "就算不能从外国进口食材，\x01",
            "也总能想办法解决。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "总之，无论发生什么状况，\x01",
            "我都会继续制作美味的面包。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FDB")

    label("loc_F5A")


    #C0030
    ChrTalk(
        0x8,
        (
            "毕竟还有阿尔摩利卡村，\x01",
            "就算不能从外国进口食材，\x01",
            "也总能想办法解决。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "总之，无论发生什么状况，\x01",
            "我都会继续制作美味的面包。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FDB")

    Jump("loc_1D0B")

    label("loc_FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_FEE")
    Jump("loc_1D0B")

    label("loc_FEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_10EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_109A")

    #C0032
    ChrTalk(
        0x8,
        (
            "从今天一大早开始，\x01",
            "来店的客人们就都在议论纷纷。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "据说在昨天夜晚，\x01",
            "矿山那边发生枪战了。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "真是可怕啊……\x01",
            "但愿别再出现更严重的状况了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10E5")

    label("loc_109A")


    #C0035
    ChrTalk(
        0x8,
        (
            "矿山那边发生枪战了，\x01",
            "真是可怕啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        "但愿别再出现更严重的状况了。\x02",
    )

    CloseMessageWindow()

    label("loc_10E5")

    Jump("loc_1D0B")

    label("loc_10EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_11F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A5")

    #C0037
    ChrTalk(
        0x8,
        (
            "贝奈特对人\x01",
            "很好哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "我向她请教做面包的方法时，\x01",
            "她虽然总是牢骚不断，\x01",
            "但每次都会认真指导我。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "从表面上也许看不出，\x01",
            "但她本质上其实是个很温柔的人呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11F4")

    label("loc_11A5")


    #C0040
    ChrTalk(
        0x8,
        (
            "你们也买点\x01",
            "面包如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "在这种下雨天，\x01",
            "正适合吃些刚刚出炉\x01",
            "的松软面包。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F4")

    Jump("loc_1D0B")

    label("loc_11F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_13B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A4")

    #C0042
    ChrTalk(
        0x8,
        (
            "贝奈特在厨房\x01",
            "专心致志地和面，\x01",
            "结果把手腕都累疼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "正好有湿毛巾，\x01",
            "我就帮她敷上了……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "太过拼命也是不好的，\x01",
            "我以后可得仔细看好她。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1311")

    label("loc_12A4")


    #C0045
    ChrTalk(
        0x8,
        (
            "呼，不过这种拼命的精神\x01",
            "也是贝奈特的\x01",
            "优点之一啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "我以后可得仔细看好她，\x01",
            "免得她太过拼命，累坏身体。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1311")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13AE")

    #C0047
    ChrTalk(
        0x101,
        (
            "#00008F（在这里似乎可以进行\x01",
            "  美食向导的取材……）\x02\x03",

            "#00003F（但现在不是做这种事的时候，\x01",
            "  以后别忘了再过来一趟。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13AE")

    Jump("loc_1D0B")

    label("loc_13B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_14E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1468")

    #C0048
    ChrTalk(
        0x8,
        (
            "贝奈特制作的新品面包\x01",
            "卖得很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "不过，我夸赞她的时候，\x01",
            "她却只是板着面孔，说些\x01",
            "『我可不能输给你』之类的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "唔……难道她\x01",
            "很讨厌我吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14E1")

    label("loc_1468")


    #C0051
    ChrTalk(
        0x8,
        (
            "如果我以前说过什么不妥的话，\x01",
            "必须要好好向她道歉才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "因为我今后也想和贝奈特\x01",
            "齐心协力，一起制作\x01",
            "美味的面包啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E1")

    Jump("loc_1D0B")

    label("loc_14E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_15C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1564")

    #C0053
    ChrTalk(
        0x8,
        (
            "我试吃了贝奈特\x01",
            "制作的新品面包，\x01",
            "真是美味无比。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "哎呀，真不亏是贝奈特。\x01",
            "我可不能输给她啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15BD")

    label("loc_1564")


    #C0055
    ChrTalk(
        0x8,
        (
            "贝奈特最近\x01",
            "已经可以做出\x01",
            "很美味的面包了。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "不愧是师傅的女儿，\x01",
            "我可不能输给她啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15BD")

    Jump("loc_1D0B")

    label("loc_15C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1672")

    #C0057
    ChrTalk(
        0x8,
        (
            "从一大早开始，\x01",
            "就涌来了很多记者。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "在平时，早上的客人\x01",
            "主要都是上班族\x01",
            "和商界人士……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "嘿嘿，能让忙碌的人\x01",
            "轻松食用，\x01",
            "也是面包的魅力之一。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16E8")

    label("loc_1672")


    #C0060
    ChrTalk(
        0x8,
        (
            "能让忙碌的人\x01",
            "轻松食用，\x01",
            "也是面包的魅力之一。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "希望今天早上的那些记者\x01",
            "吃了我们的面包之后，\x01",
            "一整天都充满干劲。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E8")

    Jump("loc_1D0B")

    label("loc_16ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1898")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_182F")

    #C0062
    ChrTalk(
        0x8,
        (
            "都这么晚了，\x01",
            "你们还在外面走动，\x01",
            "实在是少见啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "其实都已经过了\x01",
            "关店时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "不过算啦，既然是你们，凡事都好商量。\x01",
            "请不必客气，随便挑选吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#00000F谢啦，奥斯卡，\x01",
            "那我们就来挑一些……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x10A,
        "#00603F…………………………\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#00006F（如、如果要买面包，\x01",
            "  动作还是迅速一些为好啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1893")

    label("loc_182F")


    #C0068
    ChrTalk(
        0x8,
        (
            "其实都已经过了\x01",
            "关店时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "不过算啦，既然是你们，凡事都好商量。\x01",
            "请不必客气，随便挑选吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1893")

    Jump("loc_1D0B")

    label("loc_1898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A07")

    #C0070
    ChrTalk(
        0x8,
        (
            "不久前，有个女孩子\x01",
            "给了我一封信，\x01",
            "上面说『我是你的支持者』。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "唔……\x01",
            "我又不是彩虹剧团\x01",
            "的演员……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "难道是认错人了吗？\x01",
            "等她下次再来的时候，\x01",
            "我可得把信还给人家。\x02",
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

    #C0073
    ChrTalk(
        0x101,
        (
            "#00006F我、我认为还是\x01",
            "别还为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "嗯？是吗，\x01",
            "真搞不懂啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A77")

    label("loc_1A07")


    #C0075
    ChrTalk(
        0x8,
        (
            "说起来……\x01",
            "在我收到信的时候，\x01",
            "贝奈特的样子很奇怪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "而且还向我追问\x01",
            "信上的内容……\x01",
            "她真的那么想看吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A77")

    Jump("loc_1D0B")

    label("loc_1A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1BCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B5A")

    #C0077
    ChrTalk(
        0x8,
        (
            "最近这段时间，贝奈特做的面包\x01",
            "比以前更加美味了。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "过了关店时间之后，\x01",
            "她也一直待在厨房继续练习，\x01",
            "每天都是如此。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "唔，再这么下去可不行啊。\x01",
            "为了不输给贝奈特，\x01",
            "我也必须要更加努力地练习。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BC7")

    label("loc_1B5A")


    #C0080
    ChrTalk(
        0x8,
        (
            "为了不输给贝奈特，\x01",
            "我也必须要更加努力地练习。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "对了，难得两个人都有热情，\x01",
            "不如向她提议\x01",
            "一起练习吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC7")

    Jump("loc_1D0B")

    label("loc_1BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1C87")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C82")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C48")

    #C0082
    ChrTalk(
        0x8,
        (
            "梅琳是东街的\x01",
            "摩尔斯老爷爷\x01",
            "的孙女。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "不好意思，\x01",
            "后面的事情就交给你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C81")

    label("loc_1C48")


    #C0084
    ChrTalk(
        0x8,
        "多亏你们，真是帮大忙了。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "你们果然\x01",
            "值得信赖啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C81")

    Return()

    label("loc_1C82")

    Jump("loc_1D0B")

    label("loc_1C87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1D0B")

    #C0086
    ChrTalk(
        0x8,
        (
            "我最近尝试制作了很多新面包，\x01",
            "品种比以前更加丰富了。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "店里还会时常提供试吃，\x01",
            "如果尝过之后觉得不错，\x01",
            "就多买一些吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D0B")

    Return()

    # Function_7_8D9 end

    def Function_8_1D0C(): pass

    label("Function_8_1D0C")


    #C0088
    ChrTalk(
        0x8,
        "哦哦，这不是罗伊德吗！\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#00000F呀，奥斯卡，好久不见。\x01",
            "最近工作怎么样？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "哦，日复一日，没什么变化，\x01",
            "就是一直在烤面包啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "话说回来，\x01",
            "都有好久没看见你了，\x01",
            "你去什么地方了？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "莫非去米修拉姆\x01",
            "长住了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0093
    ChrTalk(
        0x101,
        (
            "#00006F喂……\x01",
            "这显然不可能吧？\x02\x03",

            "#00001F而且我走之前不是\x01",
            "和你说得很清楚吗？\x01",
            "『为了研修，暂时离开支援科』。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "哎，有这回事吗？\x01",
            "我完全不记得了。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "算啦，\x01",
            "作为重逢的纪念，\x01",
            "把这个收下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0096
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x210),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('赏月面包', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0097
    ChrTalk(
        0x102,
        (
            "#00105F这是……\x01",
            "每月固定推出的新品吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x105,
        "#10300F嘿，闻起来好香。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x109,
        "#10109F看起来好像很好吃！\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "嗯，刚刚出炉的，\x01",
            "一定很美味。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "嘿嘿，如果喜欢，\x01",
            "就再买几个好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#00000F谢啦，奥斯卡。\x01",
            "就让我尝尝看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 0)
    Return()

    # Function_8_1D0C end

    def Function_9_1FEC(): pass

    label("Function_9_1FEC")


    #C0103
    ChrTalk(
        0x8,
        "哦，来得正好！\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "今天也有新品面包推出哦，\x01",
            "拿去尝尝吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0105
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x211),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('奶油菠萝包', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0106
    ChrTalk(
        0x101,
        (
            "#00000F谢啦，奥斯卡。\x01",
            "就让我尝尝看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 1)
    Return()

    # Function_9_1FEC end

    def Function_10_20A2(): pass

    label("Function_10_20A2")


    #C0107
    ChrTalk(
        0x8,
        "哦，来得正好！\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "这次的新品\x01",
            "是贝奈特做的面包，\x01",
            "拿去尝尝吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0109
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x212),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('贝奈特绝品', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0110
    ChrTalk(
        0x101,
        (
            "#00000F谢啦，奥斯卡。\x01",
            "就让我尝尝看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 2)
    Return()

    # Function_10_20A2 end

    def Function_11_215D(): pass

    label("Function_11_215D")


    #C0111
    ChrTalk(
        0x8,
        "哦，来得正好！\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x8,
        (
            "今天也有新品推出哦，\x01",
            "拿去尝尝吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0113
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x213),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('极厚猪排三明治', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0114
    ChrTalk(
        0x101,
        (
            "#00000F谢啦，奥斯卡。\x01",
            "就让我尝尝看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 3)
    Return()

    # Function_11_215D end

    def Function_12_220F(): pass

    label("Function_12_220F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_23B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2306")

    #C0115
    ChrTalk(
        0xFE,
        (
            "使用政府配发的小麦粉，\x01",
            "根本就做不出\x01",
            "美味的面包……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "不过现在的交通状况已经恢复，\x01",
            "可以订购到阿尔摩利卡村出产的新鲜面粉了。\x01",
            "总算是恢复正常啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "希望奥斯卡和贝奈特\x01",
            "也能比以前更加努力，制作出更美味的面包啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23B3")

    label("loc_2306")


    #C0118
    ChrTalk(
        0xFE,
        (
            "现在的交通状况已经恢复，\x01",
            "可以订购到阿尔摩利卡村出产的新鲜面粉了。\x01",
            "这样一来，总算能做出美味的面包啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "希望奥斯卡和贝奈特\x01",
            "也能比以前更加努力，制作出更美味的面包啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B3")

    Jump("loc_2FF1")

    label("loc_23B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2432")

    #C0120
    ChrTalk(
        0xFE,
        (
            "由于戒严令的缘故，\x01",
            "都没有客人来了，\x01",
            "所以我就想安静地研究新品面包……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        "不过，这蓝雾究竟是什么情况？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FF1")

    label("loc_2432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2581")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24F2")

    #C0122
    ChrTalk(
        0xFE,
        (
            "现在已经不能再向两大国\x01",
            "订购食材了，\x01",
            "真是有些头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "说到底，\x01",
            "制作面包所需要的原料\x01",
            "几乎都是从外国进口的。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "暂时也只能光靠克洛斯贝尔\x01",
            "产的原料撑一撑了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_257C")

    label("loc_24F2")


    #C0125
    ChrTalk(
        0xFE,
        (
            "唔，不过……\x01",
            "『所用原料１００％为克洛斯贝尔出产』，\x01",
            "这似乎也可以当作一种卖点吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "……算啦，我也知道\x01",
            "现实可没有说的\x01",
            "这么轻松啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_257C")

    Jump("loc_2FF1")

    label("loc_2581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_269A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_262E")

    #C0127
    ChrTalk(
        0xFE,
        (
            "为了城市复兴，\x01",
            "我们开始打折促销……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "但奥斯卡今天不在，\x01",
            "真是对不住女性客人……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "算啦，难得只有\x01",
            "我们父女两个人看店，\x01",
            "还是努力加油吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2695")

    label("loc_262E")


    #C0130
    ChrTalk(
        0xFE,
        (
            "奥斯卡今天不在，\x01",
            "真是对不住女性客人……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "算啦，难得只有\x01",
            "我们父女两个人看店，\x01",
            "还是努力加油吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2695")

    Jump("loc_2FF1")

    label("loc_269A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_26FC")

    #C0132
    ChrTalk(
        0xFE,
        (
            "喂喂，听说矿山镇\x01",
            "被人占领了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "这究竟是什么人干的？\x01",
            "实在是不可饶恕啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FF1")

    label("loc_26FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2839")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27B3")

    #C0134
    ChrTalk(
        0xFE,
        (
            "在这种下雨天，\x01",
            "来面包店的客人\x01",
            "本该减少……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "但我们店却有很多\x01",
            "在下雨天也坚持光顾的常客。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "嘿嘿，真是感谢他们啊。\x01",
            "这也是因为我们长年经营的缘故。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2834")

    label("loc_27B3")


    #C0137
    ChrTalk(
        0xFE,
        (
            "我们店有很多\x01",
            "在下雨天也坚持光顾的常客。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "嘿嘿，真是感谢他们啊。\x01",
            "为了表达对他们的感谢之情，\x01",
            "下次就举办个打折促销活动吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2834")

    Jump("loc_2FF1")

    label("loc_2839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2870")

    #C0139
    ChrTalk(
        0xFE,
        (
            "大街上好像很乱啊……\x01",
            "出什么事了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FF1")

    label("loc_2870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_28EF")

    #C0140
    ChrTalk(
        0xFE,
        (
            "贝奈特那家伙，\x01",
            "在受到别人的表扬时\x01",
            "也要反唇相讥。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "这是为了掩饰害羞吗……\x01",
            "哎呀呀，真是让人伤脑筋的性格。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FF1")

    label("loc_28EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2A00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2993")

    #C0142
    ChrTalk(
        0xFE,
        (
            "奥斯卡那小子，\x01",
            "入我门下已经\x01",
            "有一段时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "贝奈特也渐渐开始\x01",
            "在意奥斯卡了……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "不然就让奥斯卡这小子\x01",
            "做我的女婿好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_29FB")

    label("loc_2993")


    #C0145
    ChrTalk(
        0xFE,
        (
            "不然就让\x01",
            "奥斯卡这小子\x01",
            "做我的女婿好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "嘿嘿，要是能有个\x01",
            "继承我家业的女婿，\x01",
            "可真是求之不得啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29FB")

    Jump("loc_2FF1")

    label("loc_2A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A7F")

    #C0147
    ChrTalk(
        0xFE,
        (
            "今天早上，有一大群要去通商会议\x01",
            "现场采访的记者光临本店。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "要是早知道能卖得那么好，\x01",
            "多烤一些面包\x01",
            "就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FF1")

    label("loc_2A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2B06")

    #C0149
    ChrTalk(
        0xFE,
        (
            "好，差不多也该开始\x01",
            "整理收拾一下了。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "面包店的准备工作\x01",
            "从凌晨三点就开始了。\x01",
            "为了准备明天的工作，必须得早点休息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FF1")

    label("loc_2B06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2C45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BCE")

    #C0151
    ChrTalk(
        0xFE,
        (
            "奥斯卡好像时常收到\x01",
            "崇拜者送来的\x01",
            "慕名信。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "自从之前他上了杂志之后，\x01",
            "就常遇到这种事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "拜他所赐，店里的生意也越来越好了。\x01",
            "必须要好好珍惜\x01",
            "奥斯卡的那些崇拜者啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C40")

    label("loc_2BCE")


    #C0154
    ChrTalk(
        0xFE,
        (
            "为了店里的生意，\x01",
            "也必须要好好珍惜\x01",
            "奥斯卡的那些崇拜者啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "但美中不足的是，\x01",
            "贝奈特好像\x01",
            "很反感这种现象呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C40")

    Jump("loc_2FF1")

    label("loc_2C45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2D5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CE5")

    #C0156
    ChrTalk(
        0xFE,
        (
            "哎呀呀，贝奈特把我\x01",
            "从厨房里轰出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "最近这段时间，她对制作面包\x01",
            "的热情简直就是鬼气逼人。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "算了，积极向上\x01",
            "总是件好事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D5A")

    label("loc_2CE5")


    #C0159
    ChrTalk(
        0xFE,
        (
            "其实，她一直自言自语的\x01",
            "小声嘟囔抱怨\x01",
            "有点好笑。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "不过，如果这能激发她的动力，\x01",
            "从某种意义上来说也没什么问题。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D5A")

    Jump("loc_2FF1")

    label("loc_2D5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2E99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DC5")

    #C0161
    ChrTalk(
        0xFE,
        (
            "哦，你们……\x01",
            "是为工作而来的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "详细情况你们去问\x01",
            "奥斯卡或贝奈特吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E94")

    label("loc_2DC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E40")

    #C0163
    ChrTalk(
        0xFE,
        (
            "我还得赶快揉出足够的面团，\x01",
            "不然就来不及烤制\x01",
            "下午的面包了。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "不好意思，找伞\x01",
            "的事情就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E94")

    label("loc_2E40")


    #C0165
    ChrTalk(
        0xFE,
        (
            "你们已经找到伞了啊？\x01",
            "嘿嘿，谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "好，这样我就又可以\x01",
            "安心地制作面包了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E94")

    Jump("loc_2FF1")

    label("loc_2E99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2FF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F66")

    #C0167
    ChrTalk(
        0xFE,
        (
            "最近这段时间，新品面包\x01",
            "基本都交给奥斯卡和贝奈特来研制。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "他们两人在竞争中\x01",
            "不断成长，\x01",
            "现在已经可以做出很不错的面包了。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "再过一阵子，把店交给\x01",
            "他们来管理应该也没问题。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2FF1")

    label("loc_2F66")


    #C0170
    ChrTalk(
        0xFE,
        (
            "特别是我女儿贝奈特，对我来说，\x01",
            "她的成长实在是个让人欣喜的误算。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "看来奥斯卡的存在\x01",
            "对她产生了很大的影响。\x01",
            "有个好对手真是很重要呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FF1")

    TalkEnd(0xFE)
    Return()

    # Function_12_220F end

    def Function_13_2FF5(): pass

    label("Function_13_2FF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3023")
    Call(0, 29)
    Return()

    label("loc_3023")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3030")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30D5")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3080")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3080")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30A0")
    OP_AF(0xCB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30D0")

    label("loc_30A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30B4")
    Jump("loc_30D0")

    label("loc_30B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30D0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)

    label("loc_30D0")

    Jump("loc_3030")

    label("loc_30D5")

    TalkEnd(0xA)
    Return()

    # Function_13_2FF5 end

    def Function_14_30D9(): pass

    label("Function_14_30D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3170")

    #C0172
    ChrTalk(
        0xA,
        (
            "抱歉，参加职业女性选秀这种活动\x01",
            "实在是不符合我的性格……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xA,
        (
            "我已经帮忙制作了\x01",
            "慈善宴会中的料理，\x01",
            "至于职业女性选秀，还是容我拒绝吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_335D")

    label("loc_3170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3232")

    #C0174
    ChrTalk(
        0xA,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xA,
        (
            "我们推出了新品面包，\x01",
            "如果有兴趣，就请尝一尝吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0176
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x213),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('极厚猪排三明治', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0177
    ChrTalk(
        0x101,
        (
            "#00000F谢谢，\x01",
            "就让我尝尝看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 3)
    Jump("loc_335D")

    label("loc_3232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32F9")

    #C0178
    ChrTalk(
        0xA,
        (
            "奥斯卡去\x01",
            "慈善宴会的会场\x01",
            "帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xA,
        (
            "虽然也可以由我过去帮忙，\x01",
            "呼，不过还是笑容灿烂、英俊帅气\x01",
            "的奥斯卡更能鼓舞大家………………\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xA,
        (
            "……呃，我、我刚才什么都没说！\x01",
            "赶快忘掉吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_335D")

    label("loc_32F9")


    #C0181
    ChrTalk(
        0xA,
        (
            "哼、哼……\x01",
            "我还要留下来\x01",
            "看店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xA,
        (
            "所以才会把慈善宴会\x01",
            "那边的任务交给奥斯卡。\x01",
            "……仅此而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_335D")

    Return()

    # Function_14_30D9 end

    def Function_15_335E(): pass

    label("Function_15_335E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_33D2")

    #C0183
    ChrTalk(
        0xFE,
        (
            "可恶的奥斯卡……\x01",
            "竟然自作主张，把我做的\x01",
            "面包推荐给杂志刊登。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "……哼，莫非是想\x01",
            "讽刺我吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FC3")

    label("loc_33D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_350D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34A3")

    #C0185
    ChrTalk(
        0xFE,
        (
            "为了不输给奥斯卡，\x01",
            "我也必须要制作很多\x01",
            "能给大家带来幸福的新品面包。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "可是……\x01",
            "我做的面包还是\x01",
            "比不上奥斯卡做的。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "既然如此，就去听听\x01",
            "奥斯卡的建议吧。\x01",
            "……虽然有些不甘心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3508")

    label("loc_34A3")


    #C0188
    ChrTalk(
        0xFE,
        (
            "我做的面包还是\x01",
            "比不上奥斯卡做的。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "既然如此，就去听听\x01",
            "奥斯卡的建议吧。\x01",
            "……虽然有些不甘心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3508")

    Jump("loc_3FC3")

    label("loc_350D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3600")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_359E")

    #C0190
    ChrTalk(
        0xFE,
        "门窗已经关好了……\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "……那些怪物到底是什么东西？\x01",
            "它们好像并不会袭击\x01",
            "我们这些市民。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        "但还是觉得好可怕……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_35FB")

    label("loc_359E")


    #C0193
    ChrTalk(
        0xFE,
        "外面那些怪物实在是让人觉得很不安……\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "就算它们不会袭击市民，\x01",
            "也还是不能让人放心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35FB")

    Jump("loc_3FC3")

    label("loc_3600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_372A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36C5")

    #C0195
    ChrTalk(
        0xFE,
        (
            "在这种状况下，奥斯卡和爸爸\x01",
            "却都意外地积极乐观呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "……真的不要紧吗？\x01",
            "就算是亚里欧斯先生，\x01",
            "终究也不可能力敌两大国啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "……算了，我再怎么担心\x01",
            "也是没用的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3725")

    label("loc_36C5")


    #C0198
    ChrTalk(
        0xFE,
        (
            "就算是亚里欧斯先生，\x01",
            "终究也不可能力敌两大国啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "……算了，我再怎么担心\x01",
            "也是没用的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3725")

    Jump("loc_3FC3")

    label("loc_372A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_373F")
    TalkEnd(0xFE)
    Call(0, 13)
    Return()

    label("loc_373F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3820")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37D1")

    #C0200
    ChrTalk(
        0xFE,
        (
            "……对了，如果在下一款新品中\x01",
            "加入那种香草……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    #C0201
    ChrTalk(
        0xFE,
        (
            "哇，抱歉！\x01",
            "一不小心想入神了。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x0, 2)
    Jump("loc_381B")

    label("loc_37D1")


    #C0202
    ChrTalk(
        0xFE,
        (
            "我正在构思\x01",
            "下一款新品面包的做法。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "嗯～那种香草应该\x01",
            "还有储备……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_381B")

    Jump("loc_3FC3")

    label("loc_3820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3831")
    Call(0, 16)
    Jump("loc_3FC3")

    label("loc_3831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3903")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38B0")

    #C0204
    ChrTalk(
        0xFE,
        "……唔，可恶的奥斯卡……\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "如果以为敷个毛巾\x01",
            "就能跟我和解，\x01",
            "那可就大错特错了！\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        "……哼。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38FE")

    label("loc_38B0")


    #C0207
    ChrTalk(
        0xFE,
        "可恶的奥斯卡……\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "如果以为敷个毛巾\x01",
            "就能跟我和解，\x01",
            "那可就大错特错了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38FE")

    Jump("loc_3FC3")

    label("loc_3903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3A1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39B3")

    #C0209
    ChrTalk(
        0xFE,
        (
            "唔唔唔，可恶的奥斯卡……\x01",
            "竟敢那么从容……！\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "……不过，看他品尝时的表情，\x01",
            "似乎是真的觉得很美味……\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "……不、不对！\x01",
            "我完全没有觉得开心！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A16")

    label("loc_39B3")


    #C0212
    ChrTalk(
        0xFE,
        (
            "邪·念·退·散……！\x01",
            "（拼命揉面……）\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "奥斯卡……\x01",
            "我下次一定～～～～\x01",
            "要让你输得痛哭流涕！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A16")

    Jump("loc_3FC3")

    label("loc_3A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3B31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AD8")

    #C0214
    ChrTalk(
        0xFE,
        (
            "我难得做出了胜过\x01",
            "奥斯卡的面包，\x01",
            "可他却表现得那么开心……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "这不是我期待的结果啊！\x01",
            "我想看到的是\x01",
            "奥斯卡心有不甘的表情……！\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        "呜呜呜，可恶的奥斯卡……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B2C")

    label("loc_3AD8")


    #C0217
    ChrTalk(
        0xFE,
        (
            "可恶的奥斯卡……\x01",
            "吃了我做的面包之后，\x01",
            "为何会那么开心呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        "真是不甘心啊！\x02",
    )

    CloseMessageWindow()

    label("loc_3B2C")

    Jump("loc_3FC3")

    label("loc_3B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3C25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BC0")

    #C0219
    ChrTalk(
        0xFE,
        (
            "把我做的面包和\x01",
            "奥斯卡做的面包摆放在一起，\x01",
            "客人基本都会选购奥斯卡做的。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        "呜呜，我的问题到底出在哪里呢……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C20")

    label("loc_3BC0")


    #C0221
    ChrTalk(
        0xFE,
        (
            "可恶，既然如此，\x01",
            "也只有继续努力了。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "一定要做出超越\x01",
            "『贝奈特特制面包』的顶级面包……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C20")

    Jump("loc_3FC3")

    label("loc_3C25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3C8D")

    #C0223
    ChrTalk(
        0xFE,
        (
            "我做的面包……\x01",
            "销售额竟然输给了\x01",
            "奥斯卡做的面包……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        "唔唔唔，明天一定要……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FC3")

    label("loc_3C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3DB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D3A")

    #C0225
    ChrTalk(
        0xFE,
        (
            "不久之前，奥斯卡\x01",
            "收到了一封奇怪的信。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "莫非是暗恋者给他的\x01",
            "情书吗……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "只不过是做面包的技术\x01",
            "比我稍好些而已，\x01",
            "竟然就如此得意忘形！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3DAC")

    label("loc_3D3A")


    #C0228
    ChrTalk(
        0xFE,
        (
            "竟然给奥斯卡\x01",
            "寄情书，\x01",
            "究竟是谁……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "……啊、那个……不对。\x01",
            "可恶的奥斯卡！\x01",
            "竟、竟敢收下那种东西……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DAC")

    Jump("loc_3FC3")

    label("loc_3DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3DF9")

    #C0230
    ChrTalk(
        0xFE,
        "（用力揉面）\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "哼……\x01",
            "我绝对不会输给\x01",
            "奥斯卡……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FC3")

    label("loc_3DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3EBB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E8A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E59")

    #C0232
    ChrTalk(
        0xA,
        (
            "雨伞的事情就交给你们啦。\x01",
            "这个孩子就由我来照顾。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E86")

    label("loc_3E59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E6E")
    Call(0, 16)
    SetScenarioFlags(0x1, 0)
    Jump("loc_3E86")

    label("loc_3E6E")


    #C0233
    ChrTalk(
        0xA,
        "呼，真是麻烦啊……\x02",
    )

    CloseMessageWindow()

    label("loc_3E86")

    TalkEnd(0xFE)
    Return()

    label("loc_3E8A")


    #C0234
    ChrTalk(
        0xA,
        "好了，别哭啦。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xA,
        "一定会帮你找到的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FC3")

    label("loc_3EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3FC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F63")

    #C0236
    ChrTalk(
        0xFE,
        (
            "欢迎光临，\x01",
            "这边有刚烤好的面包哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "……但几乎都是奥斯卡做的，\x01",
            "真是太不甘心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "可恶的奥斯卡，有朝一日，\x01",
            "我绝对会超越他的……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3FC3")

    label("loc_3F63")


    #C0239
    ChrTalk(
        0xFE,
        (
            "可恶的奥斯卡，但我现在实力不足，\x01",
            "生气也没用……\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "不过等着瞧吧，\x01",
            "我一定会超越他的……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FC3")

    TalkEnd(0xFE)
    Return()

    # Function_15_335E end

    def Function_16_3FC7(): pass

    label("Function_16_3FC7")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_409D")

    #C0241
    ChrTalk(
        0xA,
        (
            "好，我这就\x01",
            "把你送回\x01",
            "塔利兹先生那里。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xA,
        (
            "……这次没有\x01",
            "忘了什么东西吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xF,
        "啊……\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xF,
        (
            "之前买的面包\x01",
            "都已经凉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xF,
        "……呜呜。\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xA,
        (
            "啊，好啦好啦，\x01",
            "我给你换成刚出炉的，别再哭了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4183")

    label("loc_409D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4147")

    #C0247
    ChrTalk(
        0xA,
        "今天又来帮家里买东西吗？\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xA,
        (
            "可别再\x01",
            "把伞弄丢了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xF,
        (
            "嗯、嗯，不会了。\x01",
            "我已经把住址写在\x01",
            "名字的旁边了……\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xA,
        (
            "嗯～原来如此，\x01",
            "这样就可以放心了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4183")

    label("loc_4147")


    #C0251
    ChrTalk(
        0xA,
        (
            "呵呵，你的字写得\x01",
            "很漂亮呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xF,
        (
            "是、是吗？\x01",
            "嘿嘿嘿……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4183")

    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_16_3FC7 end

    def Function_17_418C(): pass

    label("Function_17_418C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4266")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4213")

    #C0253
    ChrTalk(
        0xFE,
        (
            "这里的面包真是\x01",
            "很合我的口味呢，吃了以后，\x01",
            "就觉得稍微开心些了。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "我要多买一些，带回去\x01",
            "给家人吃。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4261")

    label("loc_4213")


    #C0255
    ChrTalk(
        0xFE,
        (
            "说起来，琪露露说她\x01",
            "又要去旅行了……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "不要紧吗？\x01",
            "市外现在还很危险……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4261")

    Jump("loc_4ACD")

    label("loc_4266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4274")
    Jump("loc_4ACD")

    label("loc_4274")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_431A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42E8")

    #C0257
    ChrTalk(
        0xFE,
        (
            "琪露露好像\x01",
            "已经回家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "还不知今后的局势\x01",
            "会怎样发展，\x01",
            "确实应该和家人在一起……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4315")

    label("loc_42E8")


    #C0259
    ChrTalk(
        0xFE,
        (
            "我今天也不要四处乱逛了，\x01",
            "早点回家吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4315")

    Jump("loc_4ACD")

    label("loc_431A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4384")

    #C0260
    ChrTalk(
        0xFE,
        (
            "今天有支持城市复兴的促销活动，\x01",
            "部分面包半价销售。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "难得的好机会，\x01",
            "我就多买一些吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ACD")

    label("loc_4384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_43DA")

    #C0262
    ChrTalk(
        0xFE,
        (
            "妈妈让我今天\x01",
            "早点回家。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "毕竟发生了那样的事件，\x01",
            "这也难怪啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ACD")

    label("loc_43DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4454")

    #C0264
    ChrTalk(
        0xFE,
        (
            "说起来……\x01",
            "明天不就是彩虹剧团\x01",
            "的公演日吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "嗯，真想去看啊。\x01",
            "那个传说中的新人……\x01",
            "演技究竟如何呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ACD")

    label("loc_4454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4462")
    Jump("loc_4ACD")

    label("loc_4462")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_44EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_447D")
    Call(0, 18)
    Jump("loc_44E5")

    label("loc_447D")


    #C0266
    ChrTalk(
        0xFE,
        (
            "……哎？厨房里面好像\x01",
            "传出了贝奈特小姐的声音……？\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "呵呵，新品面包很受欢迎，\x01",
            "她似乎干劲十足呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44E5")

    Jump("loc_4ACD")

    label("loc_44EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_462F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45D8")

    #C0268
    ChrTalk(
        0xFE,
        (
            "嗯嗯，这次的新品面包\x01",
            "是贝奈特小姐做的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "松软可口的长条面包中\x01",
            "夹着草莓和鲜奶油，\x01",
            "看起来就美味无比……！\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "和装点繁多，材料丰富的\x01",
            "前款面包形成鲜明对照，\x01",
            "是款很可爱的面包呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        "嗯，一定得吃吃看！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_462A")

    label("loc_45D8")


    #C0272
    ChrTalk(
        0xFE,
        (
            "这次的新品面包\x01",
            "是贝奈特小姐做的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "看起来好可爱……\x01",
            "嗯，一定得吃吃看！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_462A")

    Jump("loc_4ACD")

    label("loc_462F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4669")

    #C0274
    ChrTalk(
        0xFE,
        (
            "啊啊，我最爱吃的\x01",
            "早餐包已经\x01",
            "卖光了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ACD")

    label("loc_4669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4677")
    Jump("loc_4ACD")

    label("loc_4677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4778")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4727")

    #C0275
    ChrTalk(
        0xFE,
        (
            "说起来，听说琪露露在不久前\x01",
            "结束了旅行，回到市里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "真是的，既然都回来了，\x01",
            "也不和我联系一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        (
            "难得她回来一次，\x01",
            "还想和她一起喝个茶呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4773")

    label("loc_4727")


    #C0278
    ChrTalk(
        0xFE,
        (
            "琪露露总是\x01",
            "在家里待不住。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "难得她回来一次，\x01",
            "还想和她一起喝个茶呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4773")

    Jump("loc_4ACD")

    label("loc_4778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4889")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_483B")

    #C0280
    ChrTalk(
        0xFE,
        (
            "啊，这次的新品面包……\x01",
            "看起来好像很好吃啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "柔软的蜜瓜面包里\x01",
            "充满鲜美的\x01",
            "牛奶蛋黄酱……\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xFE,
        (
            "虽然吃这种东西可能会发胖……\x01",
            "嗯，但不管那么多了，还是买来尝尝吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4884")

    label("loc_483B")


    #C0283
    ChrTalk(
        0xFE,
        (
            "看起来这么美味的新品面包，\x01",
            "实在是不能不吃啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        "买几个回去好了。\x02",
    )

    CloseMessageWindow()

    label("loc_4884")

    Jump("loc_4ACD")

    label("loc_4889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_49C6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4976")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4924")

    #C0285
    ChrTalk(
        0xFE,
        (
            "这么一说……\x01",
            "好像确实来过\x01",
            "一对兄妹呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "那个女孩和这个叫小桃的\x01",
            "孩子年龄相仿，\x01",
            "不小心拿错伞也不奇怪……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4972")

    label("loc_4924")


    #C0287
    ChrTalk(
        0xFE,
        (
            "呵呵，能把伞找到，\x01",
            "真是太好啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "好，买完面包之后，\x01",
            "我也赶快回家吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4972")

    TalkEnd(0xFE)
    Return()

    label("loc_4976")


    #C0289
    ChrTalk(
        0xFE,
        (
            "那个哭泣的孩子就是\x01",
            "旁边那家商店店主的女儿吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        "发生什么事了吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4ACD")

    label("loc_49C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4ACD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A60")

    #C0291
    ChrTalk(
        0xFE,
        "这次的新品面包……\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        (
            "是如同满月一般的\x01",
            "煎蛋夹心面包……\x01",
            "啊啊～好像很好吃呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "呵呵，买个新品面包，\x01",
            "喝杯茶再回去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4ACD")

    label("loc_4A60")


    #C0294
    ChrTalk(
        0xFE,
        (
            "自从发现了这家店之后，\x01",
            "看看有没有新品面包\x01",
            "是我每天必做的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        (
            "呵呵，买个新品面包，\x01",
            "喝杯茶再回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4ACD")

    TalkEnd(0xFE)
    Return()

    # Function_17_418C end

    def Function_18_4AD1(): pass

    label("Function_18_4AD1")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0296
    ChrTalk(
        0xB,
        "琪露露喜欢哪种面包呢？\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xB,
        (
            "我推荐这款\x01",
            "新品面包哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xC,
        (
            "……那就要\x01",
            "这个吧。\x01",
            "看起来很可爱。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xB,
        "对吧对吧～\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_18_4AD1 end

    def Function_19_4B63(): pass

    label("Function_19_4B63")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4B74")
    Jump("loc_4BE0")

    label("loc_4B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4BE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B8F")
    Call(0, 18)
    Jump("loc_4BE0")

    label("loc_4B8F")


    #C0300
    ChrTalk(
        0xFE,
        (
            "在外出旅行之前，\x01",
            "我总会来这里买食物。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xFE,
        "话说回来，这个面包真的好可爱……\x02",
    )

    CloseMessageWindow()

    label("loc_4BE0")

    TalkEnd(0xFE)
    Return()

    # Function_19_4B63 end

    def Function_20_4BE4(): pass

    label("Function_20_4BE4")

    Call(0, 21)
    Return()

    # Function_20_4BE4 end

    def Function_21_4BE8(): pass

    label("Function_21_4BE8")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4BF5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5897")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C45")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4C45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4C64")
    OP_AF(0x31)
    Jump("loc_4CE6")

    label("loc_4C64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4C74")
    OP_AF(0x30)
    Jump("loc_4CE6")

    label("loc_4C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4C84")
    OP_AF(0x2F)
    Jump("loc_4CE6")

    label("loc_4C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4C94")
    OP_AF(0x2E)
    Jump("loc_4CE6")

    label("loc_4C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4CA4")
    OP_AF(0x2D)
    Jump("loc_4CE6")

    label("loc_4CA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4CB4")
    OP_AF(0x2C)
    Jump("loc_4CE6")

    label("loc_4CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_4CC4")
    OP_AF(0x2B)
    Jump("loc_4CE6")

    label("loc_4CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4CD4")
    OP_AF(0x2A)
    Jump("loc_4CE6")

    label("loc_4CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4CE4")
    OP_AF(0x29)
    Jump("loc_4CE6")

    label("loc_4CE4")

    OP_AF(0x28)

    label("loc_4CE6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5892")

    label("loc_4CF5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D09")
    Jump("loc_5892")

    label("loc_4D09")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5892")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4E6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE5")

    #C0302
    ChrTalk(
        0xD,
        (
            "贸易渠道仍然没有恢复，\x01",
            "所以现在还无法订购到\x01",
            "充足的商品……\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xD,
        (
            "但至少克洛斯贝尔恢复原状了，\x01",
            "总算可以稍微安心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xD,
        (
            "为了让家人能够安心生活，\x01",
            "我一定要继续努力。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4E6A")

    label("loc_4DE5")


    #C0305
    ChrTalk(
        0xD,
        (
            "虽然贸易仍然无法正常进行……\x01",
            "但至少克洛斯贝尔恢复原状了，\x01",
            "总算可以稍微安心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xD,
        (
            "为了让家人能够安心生活，\x01",
            "我一定要继续努力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E6A")

    Jump("loc_5892")

    label("loc_4E6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4F04")

    #C0307
    ChrTalk(
        0xD,
        (
            "到、到底是怎么回事？\x01",
            "那如同中世纪铠甲一样的怪物是……\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xD,
        (
            "在、在这种时候，\x01",
            "你们竟然还到店里来……\x01",
            "如果想买什么东西，就和我说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5892")

    label("loc_4F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5001")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FAB")

    #C0309
    ChrTalk(
        0xD,
        (
            "听了迪塔先生的演说之后，\x01",
            "我觉得独立确实是唯一的出路。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xD,
        (
            "虽然不知道未来\x01",
            "还要面对怎样的危险……\x01",
            "但我无论如何都会\x01",
            "保护好小桃和爱尔莎。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4FFC")

    label("loc_4FAB")


    #C0311
    ChrTalk(
        0xD,
        (
            "虽然不知道未来\x01",
            "还要面对怎样的危险……\x01",
            "但我无论如何都会\x01",
            "保护好小桃和爱尔莎。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FFC")

    Jump("loc_5892")

    label("loc_5001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5070")

    #C0312
    ChrTalk(
        0xD,
        (
            "欢迎光临\x01",
            "塔利兹商店。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xD,
        (
            "我们以生活必需品为主，\x01",
            "展开了大减价活动，\x01",
            "如果需要，就来看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5892")

    label("loc_5070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_516B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_510F")

    #C0314
    ChrTalk(
        0xD,
        (
            "玛因兹那起事件……\x01",
            "据说是帝国\x01",
            "在暗中策动的。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xD,
        (
            "竟然将无辜的\x01",
            "普通人卷入其中……\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xD,
        (
            "如果传闻真的属实，\x01",
            "我绝对不会原谅帝国。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5166")

    label("loc_510F")


    #C0317
    ChrTalk(
        0xD,
        (
            "说不定他们的\x01",
            "下一个目标\x01",
            "就是市区了。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xD,
        (
            "如果传闻真的属实，\x01",
            "我绝对不会原谅帝国。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5166")

    Jump("loc_5892")

    label("loc_516B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5201")

    #C0319
    ChrTalk(
        0xD,
        (
            "昨天那起脱轨事故\x01",
            "使不少人负伤，\x01",
            "但铁路总算是恢复运行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xD,
        (
            "采购的物品经常需要\x01",
            "利用铁路运输，\x01",
            "铁路恢复运行，大家也就可以安心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5892")

    label("loc_5201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_530B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52B6")

    #C0321
    ChrTalk(
        0xD,
        (
            "听到急救车的声音之后，\x01",
            "我慌慌忙忙地跑到了店外……\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xD,
        (
            "呼……\x01",
            "发现不是小桃受伤，\x01",
            "稍微松了口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xD,
        (
            "不过，竟然出动那么多辆车……\x01",
            "到底发生什么事了？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5306")

    label("loc_52B6")


    #C0324
    ChrTalk(
        0xD,
        (
            "有好几辆\x01",
            "急救车通过……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xD,
        (
            "必须得提醒在街上玩的孩子们，\x01",
            "让他们小心车辆。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5306")

    Jump("loc_5892")

    label("loc_530B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_536F")

    #C0326
    ChrTalk(
        0xD,
        (
            "小桃他们正在\x01",
            "外面一起玩呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xD,
        (
            "最近的交通流量比较大，\x01",
            "希望他们小心过往的车辆。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5892")

    label("loc_536F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_547D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5420")

    #C0328
    ChrTalk(
        0xD,
        (
            "我认为克洛斯贝尔脱离\x01",
            "帝国和共和国，成为独立国家\x01",
            "是一件好事。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xD,
        (
            "但一旦真的独立，\x01",
            "恐怕就要与\x01",
            "两大国为敌了……\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xD,
        "唔，真是个让人头疼的问题啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5478")

    label("loc_5420")


    #C0331
    ChrTalk(
        0xD,
        (
            "我认为克洛斯贝尔独立\x01",
            "是件好事……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xD,
        (
            "但如果与帝国和共和国为敌，\x01",
            "实在是很可怕……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5478")

    Jump("loc_5892")

    label("loc_547D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_54F9")

    #C0333
    ChrTalk(
        0xD,
        (
            "下期的克洛斯贝尔时代周刊肯定\x01",
            "会刊登大量有关通商会议的文章吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xD,
        (
            "销量应该会很不错，\x01",
            "我就多进一些货吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5892")

    label("loc_54F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_554C")

    #C0335
    ChrTalk(
        0xD,
        (
            "欢迎，\x01",
            "有什么需要吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xD,
        (
            "距离关店还有\x01",
            "一段时间，\x01",
            "请慢慢看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5892")

    label("loc_554C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_565E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55EE")

    #C0337
    ChrTalk(
        0xD,
        (
            "今天是兰花塔的\x01",
            "揭幕日呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xD,
        (
            "哎呀，我都想过要暂时关店\x01",
            "去好好观赏揭幕式呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xD,
        (
            "呵呵，巨大的建筑物和座驾\x01",
            "是男孩子永远的梦想啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5659")

    label("loc_55EE")


    #C0340
    ChrTalk(
        0xD,
        (
            "兰花塔那样的\x01",
            "巨大建筑物和座驾\x01",
            "是男孩子永远的梦想啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xD,
        (
            "无论到了什么年龄，\x01",
            "也都会因它们而心跳加速。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5659")

    Jump("loc_5892")

    label("loc_565E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5782")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_571C")

    #C0342
    ChrTalk(
        0xD,
        (
            "最近在市里经常能\x01",
            "看到警察。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xD,
        (
            "各国的首脑好像都要\x01",
            "来参加通商会议，\x01",
            "这也是为了做好警备工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xD,
        (
            "我可不希望小桃\x01",
            "被卷进什么事件，\x01",
            "希望他们一定要认真尽职。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_577D")

    label("loc_571C")


    #C0345
    ChrTalk(
        0xD,
        (
            "警察好像加强了\x01",
            "市内警戒力度。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xD,
        (
            "我可不希望小桃\x01",
            "被卷进什么事件，\x01",
            "希望他们一定要认真尽职。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_577D")

    Jump("loc_5892")

    label("loc_5782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5833")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5809")

    #C0347
    ChrTalk(
        0xD,
        (
            "小桃帮我去面包店\x01",
            "买面包了。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xD,
        (
            "不过……\x01",
            "都这么久了怎么还没回来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xD,
        (
            "是忘记\x01",
            "要买哪种\x01",
            "面包了吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_582E")

    label("loc_5809")


    #C0350
    ChrTalk(
        0xD,
        (
            "小桃好慢啊，\x01",
            "是发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_582E")

    Jump("loc_5892")

    label("loc_5833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5892")

    #C0351
    ChrTalk(
        0xD,
        (
            "呀，欢迎，\x01",
            "欢迎光临『塔利兹商店』。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xD,
        (
            "我们这里日用品应有尽有，\x01",
            "请随意看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5892")

    Jump("loc_4BF5")

    label("loc_5897")

    TalkEnd(0xD)
    Return()

    # Function_21_4BE8 end

    def Function_22_589B(): pass

    label("Function_22_589B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_59E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5963")

    #C0353
    ChrTalk(
        0xFE,
        (
            "小桃说要为市里的大家做些什么，\x01",
            "和朋友们一起\x01",
            "跑出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xFE,
        (
            "小桃还是第一次那么强烈地\x01",
            "坚持自己的主张呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "虽然很担心，不想让她去外边玩……\x01",
            "但我还是尊重她的想法。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_59DC")

    label("loc_5963")


    #C0356
    ChrTalk(
        0xFE,
        (
            "小桃说要为市里的大家做些什么，\x01",
            "和朋友们一起\x01",
            "跑出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "虽然很担心，不想让她去外边玩……\x01",
            "但我还是尊重她的想法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59DC")

    Jump("loc_5EB9")

    label("loc_59E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5A3B")

    #C0358
    ChrTalk(
        0xFE,
        (
            "城市里居然出现了\x01",
            "那种东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        (
            "这就是总统颁布\x01",
            "戒严令的原因吗……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EB9")

    label("loc_5A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5B76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AFC")

    #C0360
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔今后的形势\x01",
            "可能会越来越不安定……\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xFE,
        (
            "虽然有些对不起小桃……\x01",
            "但短时间内还是\x01",
            "不能再让她去外面玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "只要她离开我的视线范围，\x01",
            "我就会担心得要命……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5B71")

    label("loc_5AFC")


    #C0363
    ChrTalk(
        0xFE,
        (
            "虽然有些对不起小桃……\x01",
            "但短时间内还是\x01",
            "不能再让她去外面玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "只要她离开我的视线范围，\x01",
            "我就会担心得要命……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B71")

    Jump("loc_5EB9")

    label("loc_5B76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5BF4")

    #C0365
    ChrTalk(
        0xFE,
        (
            "……实在是不敢\x01",
            "让小桃去外面玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "自那次事件之后，已经过去了一周，\x01",
            "我也希望能尽快忘记那些事，但还是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EB9")

    label("loc_5BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5C02")
    Jump("loc_5EB9")

    label("loc_5C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5C55")

    #C0367
    ChrTalk(
        0xFE,
        (
            "我让小桃去买配炖牛肉\x01",
            "吃的面包了。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        "希望她今天能快去快回……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5EB9")

    label("loc_5C55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5C63")
    Jump("loc_5EB9")

    label("loc_5C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5C71")
    Jump("loc_5EB9")

    label("loc_5C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5C7F")
    Jump("loc_5EB9")

    label("loc_5C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5D5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D21")

    #C0369
    ChrTalk(
        0xFE,
        (
            "小桃今天也和隆他们\x01",
            "一起去玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "这孩子过于内向，我原来一直很发愁，\x01",
            "但她最近似乎改变了不少。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        (
            "呵呵，真要感谢\x01",
            "隆和亨利啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5D55")

    label("loc_5D21")


    #C0372
    ChrTalk(
        0xFE,
        (
            "嗯，小桃今天大概\x01",
            "也会玩到肚子饿了\x01",
            "才会回来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D55")

    Jump("loc_5EB9")

    label("loc_5D5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5DA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D7A")
    Call(0, 23)
    ClearChrFlags(0xE, 0x10)
    Jump("loc_5D9F")

    label("loc_5D7A")


    #C0373
    ChrTalk(
        0xFE,
        (
            "呵呵，小桃她一定\x01",
            "玩得很开心吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D9F")

    Jump("loc_5EB9")

    label("loc_5DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5DB2")
    Jump("loc_5EB9")

    label("loc_5DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5DC0")
    Jump("loc_5EB9")

    label("loc_5DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5EB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E4B")

    #C0374
    ChrTalk(
        0xFE,
        (
            "小桃这孩子，\x01",
            "外面下着雨，她却开开心心地\x01",
            "出去帮家里买东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        (
            "呵呵，大概是\x01",
            "很想用用爸爸\x01",
            "买给她的雨伞吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5EAB")

    label("loc_5E4B")


    #C0376
    ChrTalk(
        0xFE,
        (
            "小桃的雨伞是\x01",
            "她爸爸买给她的。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "这孩子很喜欢粉色，\x01",
            "所以她好像非常中意那把粉色的雨伞呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EAB")

    Jump("loc_5EB9")

    label("loc_5EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5EB9")

    label("loc_5EB9")

    TalkEnd(0xFE)
    Return()

    # Function_22_589B end

    def Function_23_5EBD(): pass

    label("Function_23_5EBD")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0378
    ChrTalk(
        0xF,
        (
            "……对了，对了，\x01",
            "隆想擅自闯进\x01",
            "兰花塔。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xF,
        (
            "结果连我和亨利\x01",
            "都被警察骂了……\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xE,
        (
            "哎呀呀……\x01",
            "小桃运气真不好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xF,
        (
            "不过……\x01",
            "真是很开心呢……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 7)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_23_5EBD end

    def Function_24_5F69(): pass

    label("Function_24_5F69")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5F7A")
    Jump("loc_6271")

    label("loc_5F7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5FBE")

    #C0382
    ChrTalk(
        0xFE,
        "呜呜，外面好可怕……\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        "隆和亨利他们没事吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6271")

    label("loc_5FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_600A")

    #C0384
    ChrTalk(
        0xFE,
        (
            "爸爸和妈妈\x01",
            "好像都很不安……\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "我也开始觉得\x01",
            "害怕了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6271")

    label("loc_600A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_606D")

    #C0386
    ChrTalk(
        0xFE,
        (
            "最近，我每次想\x01",
            "出去玩的时候，\x01",
            "都会被妈妈阻止……\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        (
            "好想和隆他们\x01",
            "一起玩啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6271")

    label("loc_606D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_607B")
    Jump("loc_6271")

    label("loc_607B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_608C")
    Call(0, 16)
    Jump("loc_6271")

    label("loc_608C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_609A")
    Jump("loc_6271")

    label("loc_609A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_60A8")
    Jump("loc_6271")

    label("loc_60A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6101")

    #C0388
    ChrTalk(
        0xFE,
        "我今天要在店里帮忙……\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "也不能一天到晚总是玩。\x01",
            "必须要努力帮忙……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6271")

    label("loc_6101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_610F")
    Jump("loc_6271")

    label("loc_610F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_6195")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_612A")
    Call(0, 23)
    Jump("loc_6190")

    label("loc_612A")


    #C0390
    ChrTalk(
        0xFE,
        (
            "隆真是很有趣啊。\x01",
            "他把所有责任\x01",
            "都推给亨利了……\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        (
            "但谎话马上就被戳破，\x01",
            "被骂得更凶了。\x01",
            "嘻嘻……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6190")

    Jump("loc_6271")

    label("loc_6195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_61A3")
    Jump("loc_6271")

    label("loc_61A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_61B1")
    Jump("loc_6271")

    label("loc_61B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6268")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6251")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6217")

    #C0392
    ChrTalk(
        0xF,
        "那把伞很重要……\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xF,
        (
            "（抽泣）……\x01",
            "拜托了，大哥哥……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_624D")

    label("loc_6217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_622C")
    Call(0, 16)
    SetScenarioFlags(0x1, 0)
    Jump("loc_624D")

    label("loc_622C")


    #C0394
    ChrTalk(
        0xF,
        (
            "嘿嘿嘿，\x01",
            "大姐姐好温柔呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_624D")

    TalkEnd(0xFE)
    Return()

    label("loc_6251")


    #C0395
    ChrTalk(
        0xF,
        "（抽泣）……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6271")

    label("loc_6268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6271")

    label("loc_6271")

    TalkEnd(0xFE)
    Return()

    # Function_24_5F69 end

    def Function_25_6275(): pass

    label("Function_25_6275")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6815")

    #C0396
    ChrTalk(
        0xFE,
        "啊，是特别任务支援科的各位……！\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x101,
        (
            "#00005F你不是伊安律师的\x01",
            "助手皮特吗？\x02\x03",

            "#00001F就你一个人啊……\x01",
            "律师在做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "看到这种状况之后，\x01",
            "伊安律师\x01",
            "去兰花塔抗议了。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xFE,
        (
            "他把我托付在这里，\x01",
            "之后就一直都没有联络了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_66EA")

    #C0400
    ChrTalk(
        0x102,
        "#00106F伊安律师……真让人担心啊。\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x103,
        (
            "#00208F如果去了兰花塔，\x01",
            "说不定会被总统\x01",
            "拘捕吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x104,
        "#00301F我们还是抓紧时间为好啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0403
    ChrTalk(
        0x101,
        (
            "#00003F……皮特。\x02\x03",

            "#00001F伊安律师\x01",
            "还说过什么吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0404
    ChrTalk(
        0xFE,
        "这个嘛……\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        (
            "他确实说了一些\x01",
            "奇怪的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "他让我等状况平息下来之后，\x01",
            "回事务所\x01",
            "整理一下他的办公桌。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x101,
        "#00005F整理办公桌……？\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "嗯，一开始我还以为他走得太急，\x01",
            "所以来不及整理……\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xFE,
        (
            "可仔细一想，虽然伊安律师一直\x01",
            "都让我负责扫除和整理文件，但他经常提醒我，\x01",
            "说唯独桌子是绝对不能碰的。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "由于工作性质的缘故，他有不少东西，\x01",
            "连我这个当助手的都不能随便看，\x01",
            "一直都就那样放在原处……\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x102,
        (
            "#00108F伊安律师……\x01",
            "嗯，这确实令人在意呢……\x02\x03",

            "#00106F在这种时候竟然\x01",
            "拜托别人整理通常不能碰的办公桌，\x01",
            "真是难以理解啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x101,
        (
            "#00003F………………………………\x02\x03",

            "#00000F皮特，\x01",
            "你继续留在这里避难，\x01",
            "伊安律师就交给我们吧。\x02\x03",

            "如果我们了解到什么情况，\x01",
            "一定会立刻联络你的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67E8")

    label("loc_66EA")


    #C0413
    ChrTalk(
        0x102,
        "#00106F伊安律师……真让人担心啊。\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x103,
        (
            "#00208F如果去了兰花塔，\x01",
            "说不定会被总统\x01",
            "拘捕吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x104,
        "#00301F我们还是抓紧时间为好啊。\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x101,
        (
            "#00003F嗯……\x02\x03",

            "#00000F皮特，\x01",
            "你继续留在这里避难，\x01",
            "伊安律师就交给我们吧。\x02\x03",

            "如果我们了解到什么情况，\x01",
            "一定会立刻联络你的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67E8")


    #C0417
    ChrTalk(
        0xFE,
        (
            "知、知道了……\x01",
            "那就拜托大家了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 5)
    Jump("loc_6854")

    label("loc_6815")


    #C0418
    ChrTalk(
        0xFE,
        (
            "各位，伊安律师\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xFE,
        "希望律师他平安无事……\x02",
    )

    CloseMessageWindow()

    label("loc_6854")

    TalkEnd(0xFE)
    Return()

    # Function_25_6275 end

    def Function_26_6858(): pass

    label("Function_26_6858")

    EventBegin(0x0)
    Fade(500)
    OP_68(53840, 1200, 2280, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28210, 0)
    SetChrPos(0x101, 53550, 0, 2200, 90)
    SetChrPos(0x102, 53350, 0, 1200, 90)
    SetChrPos(0x109, 52400, 0, 2200, 90)
    SetChrPos(0x105, 52200, 0, 1200, 90)
    TurnDirection(0x8, 0x101, 0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 0)), scpexpr(EXPR_END)), "loc_6993")

    #C0420
    ChrTalk(
        0x101,
        (
            "#6P#00000F哟，奥斯卡，\x01",
            "我们接到了这里发出的委托。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x8,
        (
            "#11P哦，罗伊德！\x01",
            "我就知道你会来。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x102,
        (
            "#6P#00100F虽然有些仓促，\x01",
            "不过可以请你立即\x01",
            "说明事情的详情吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B97")

    label("loc_6993")


    #C0423
    ChrTalk(
        0x101,
        (
            "#6P#00000F哟，奥斯卡，好久不见，\x01",
            "我们是接到委托而来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x8,
        (
            "#11P哦哦！这不是罗伊德吗！\x01",
            "我就知道你会来。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x8,
        (
            "#11P话说回来，\x01",
            "都有好久没看见你了，\x01",
            "你去什么地方了？\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x8,
        (
            "#11P莫非去米修拉姆\x01",
            "长住了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0427
    ChrTalk(
        0x101,
        (
            "#6P#00006F喂……\x01",
            "这显然不可能吧？\x02\x03",

            "#00001F而且我走之前不是\x01",
            "和你说得很清楚吗？\x01",
            "『为了研修，暂时离开支援科』。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x8,
        (
            "#11P哎，有这回事吗？\x01",
            "我完全不记得了。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x8,
        (
            "#11P……好像越扯越远了，\x01",
            "还是赶快说说这次的委托吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x102,
        (
            "#6P#00100F那么……虽然有些仓促，\x01",
            "不过请你说明一下事情的详情吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 0)

    label("loc_6B97")


    #C0431
    ChrTalk(
        0x8,
        (
            "#11P嗯，这次的委托\x01",
            "和那边的小桃有关。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x8,
        (
            "#11P她是塔利兹商店店主的孩子，\x01",
            "今天在雨中打着伞，\x01",
            "出来帮家里买东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x8,
        "#11P可是……\x02",
    )

    CloseMessageWindow()
    OP_68(53460, 1500, 2390, 2000)

    def lambda_6C34():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_6C34)
    Sleep(10)

    def lambda_6C44():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_6C44)
    Sleep(10)

    def lambda_6C54():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6C54)
    Sleep(10)

    def lambda_6C64():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6C64)
    Sleep(10)

    def lambda_6C74():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6C74)
    Sleep(10)

    def lambda_6C84():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6C84)
    WaitChrThread(0x105, 2)
    OP_6F(0x1)

    #C0434
    ChrTalk(
        0xF,
        "……呜、呜……\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xF,
        (
            "我、我最重要的\x01",
            "粉色雨伞不知\x01",
            "丢到什么地方了……\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x8,
        "#11P……事情就是这样啦。\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x101,
        (
            "#12P#00005F原来如此……\x02\x03",

            "#00001F在店内和店外找过了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xA,
        (
            "我和奥斯卡已经\x01",
            "仔细找过一遍了。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xA,
        (
            "结果……\x01",
            "只找到了这个。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0440
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "贝奈特取出了一把粉色雨伞。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0441
    ChrTalk(
        0x109,
        (
            "#12P#10105F哎……？\x01",
            "这把粉色的雨伞……\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x105,
        (
            "#12P#10305F这不就是那个女孩\x01",
            "的雨伞吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0xA,
        (
            "我本来也是这么想的……\x01",
            "不过，你们看这里。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0444
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "贝奈特将伞柄部分\x01",
            "指给罗伊德等人看。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0445
    ChrTalk(
        0x102,
        (
            "#12P#00100F上面写着字……\x01",
            "『梅琳』。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x101,
        (
            "#12P#00003F原来如此……\x02\x03",

            "#00000F也就是说，\x01",
            "有人拿错了\x01",
            "伞啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x8,
        "#11P嗯，看来是这样。\x02",
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x8,
        (
            "#11P今天因为下雨，客人很少，\x01",
            "我还记得来过店里\x01",
            "的几组客人……\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x8,
        (
            "#11P不过我并不知道\x01",
            "名叫『梅琳』的人\x01",
            "是谁。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x8,
        (
            "#11P希望你们能帮忙找到\x01",
            "这把伞的主人，\x01",
            "把拿错的雨伞取回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x8,
        "#11P怎么样？可以吗？\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0452
    ChrTalk(
        0x101,
        (
            "#6P#00000F嗯，知道了，\x01",
            "交给我们吧。\x02\x03",

            "一定会把伞找到的。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x8,
        "#11P哦！罗伊德真是可靠啊！\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x102,
        (
            "#12P#00103F唔，\x01",
            "关于『梅琳』这个名字……\x01",
            "要是能有多一些的线索就好了。\x02\x03",

            "#00100F罗伊德，你有什么头绪吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_70EB():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_70EB)
    Sleep(50)

    def lambda_70FB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_70FB)
    Sleep(50)

    def lambda_710B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_710B)
    Sleep(300)

    #C0455
    ChrTalk(
        0x109,
        (
            "#6P#10100F对啊，比如有没有\x01",
            "和这个人\x01",
            "说过话呢？\x02\x03",

            "#10106F哪怕能确认这个人\x01",
            "所在的街区也好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x101,
        (
            "#11P#00003F嗯，这个嘛……\x01",
            "（我好像在哪里听过这个名字，\x01",
            "  但又不是很确定……）\x02\x03",

            "#00000F那个叫『梅琳』的孩子，记得是……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "中央广场的居民\x01",      # 0
            "西街的居民\x01",          # 1
            "住宅街的居民\x01",        # 2
            "东街的居民\x01",          # 3
            "港湾区的居民\x01",        # 4
            "行政区的居民\x01",        # 5
            "欢乐街的居民\x01",        # 6
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7406")
    OP_2C(0x6B, 0x1)

    #C0457
    ChrTalk(
        0x101,
        (
            "#11P#00000F……是住在东街的\x01",
            "那个女孩吧？\x02\x03",

            "我记得是工商协会会长\x01",
            "摩尔斯先生的孙女。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x102,
        (
            "#11P#12P#00105F啊，这么一说……！\x01",
            "我们好像和她说过几次话呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x105,
        (
            "#6P#10304F那孩子还有个\x01",
            "名叫洛依的哥哥。\x02\x03",

            "#10300F也就是说，他们兄妹\x01",
            "一起来这里买过东西？\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x8,
        (
            "#11P……哦哦！没错没错！\x01",
            "的确有一对兄妹来过。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x8,
        (
            "#11P原来是摩尔斯老爷爷的孙子和孙女啊，\x01",
            "怪不得我觉得眼熟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77C5")

    label("loc_7406")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7434"),
        (1, "loc_746B"),
        (2, "loc_749E"),
        (4, "loc_74D3"),
        (5, "loc_7508"),
        (6, "loc_753D"),
        (SWITCH_DEFAULT, "loc_7572"),
    )


    label("loc_7434")


    #C0462
    ChrTalk(
        0x101,
        (
            "#11P#00000F……是住在中央广场的\x01",
            "那个女孩吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7572")

    label("loc_746B")


    #C0463
    ChrTalk(
        0x101,
        (
            "#11P#00000F……是住在西街的\x01",
            "那个女孩吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7572")

    label("loc_749E")


    #C0464
    ChrTalk(
        0x101,
        (
            "#11P#00000F……是住在住宅街的\x01",
            "那个女孩吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7572")

    label("loc_74D3")


    #C0465
    ChrTalk(
        0x101,
        (
            "#11P#00000F……是住在港湾区的\x01",
            "那个女孩吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7572")

    label("loc_7508")


    #C0466
    ChrTalk(
        0x101,
        (
            "#11P#00000F……是住在行政区的\x01",
            "那个女孩吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7572")

    label("loc_753D")


    #C0467
    ChrTalk(
        0x101,
        (
            "#11P#00000F……是住在欢乐街的\x01",
            "那个女孩吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7572")

    label("loc_7572")


    #C0468
    ChrTalk(
        0x105,
        "#6P#10304F不是的。\x02",
    )

    CloseMessageWindow()

    def lambda_758F():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_758F)
    Sleep(50)

    def lambda_759F():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_759F)
    Sleep(300)

    #C0469
    ChrTalk(
        0x101,
        "#11P#00005F哎？\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x105,
        (
            "#6P#10300F『梅琳』是住在\x01",
            "东街的工商协会会长\x01",
            "摩尔斯先生的孙女。\x02\x03",

            "#10304F她还有个名叫洛依的哥哥，\x01",
            "多半是兄妹二人\x01",
            "一起来这里买过东西吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x8,
        (
            "#11P……哦哦！没错没错！\x01",
            "的确有一对兄妹来过。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x101,
        (
            "#11P#00005F是吗……\x01",
            "原来是摩尔斯先生的孙女啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x102,
        (
            "#12P#00100F这么一说，\x01",
            "我们好像和她说过几次话呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x109,
        "#6P#10100F瓦吉，你知道的还真多啊。\x02",
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x105,
        (
            "#6P#10302F呵呵，做男公关兼职的时候，\x01",
            "会得到各种各样的情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x109,
        (
            "#6P#10106F原、原来如此……\x01",
            "呃，但实在是没法赞赏你呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x101,
        (
            "#11P#00009F好啦好啦，总之，\x01",
            "你可真是帮大忙了，瓦吉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77C5")


    #C0478
    ChrTalk(
        0x8,
        (
            "#11P好，那就把\x01",
            "梅琳的雨伞\x01",
            "交给你们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xA,
        "嗯，就是这把。\x02",
    )

    CloseMessageWindow()

    def lambda_780A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_780A)
    Sleep(50)

    def lambda_781A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_781A)
    Sleep(50)

    def lambda_782A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_782A)
    Sleep(50)

    def lambda_783A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_783A)
    Sleep(50)

    def lambda_784A():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_784A)
    WaitChrThread(0xA, 2)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0480
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x325),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('梅琳的伞', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_9B(0x1, 0xA, 0xB4, 0x3E8, 0x5DC, 0x0)

    #C0481
    ChrTalk(
        0x8,
        (
            "#11P请将这把雨伞\x01",
            "还给梅琳，\x01",
            "并取回小桃的雨伞。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x8,
        "#11P拜托你啦，罗伊德。\x02",
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0xF,
        (
            "呜、呜……\x01",
            "大哥哥，拜托你了……\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x101,
        "#12P#00000F嗯，交给我吧。\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x102,
        (
            "#12P#00100F那好，\x01",
            "我们就先去摩尔斯\x01",
            "会长家拜访吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7987():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7987)
    Sleep(50)

    def lambda_7997():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7997)
    Sleep(50)

    def lambda_79A7():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_79A7)

    #C0486
    ChrTalk(
        0x101,
        (
            "#5P#00000F记得是位于东街边缘\x01",
            "的那座住宅。\x02\x03",

            "先过去\x01",
            "看看吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0487
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找遗失的雨伞】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 52100, 0, -200, 270)
    TurnDirection(0xA, 0xF, 0)
    TurnDirection(0xF, 0xA, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x132, 3)
    OP_29(0x6B, 0x1, 0x0)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xF, 0x10)
    EventEnd(0x5)
    Return()

    # Function_26_6858 end

    def Function_27_7A87(): pass

    label("Function_27_7A87")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(53840, 1200, 2280, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28210, 0)
    SetChrPos(0x101, 53550, 0, 2200, 90)
    SetChrPos(0x102, 53350, 0, 1200, 90)
    SetChrPos(0x109, 52400, 0, 2200, 90)
    SetChrPos(0x105, 52200, 0, 1200, 90)
    OP_93(0xA, 0xB4, 0x0)
    OP_93(0xF, 0xB4, 0x0)
    TurnDirection(0x8, 0x101, 0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0xA, 0xFF)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    #C0488
    ChrTalk(
        0x8,
        (
            "#11P哦！罗伊德！\x01",
            "情况如何了？\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x101,
        "#6P#00000F嗯，顺利取回啦。\x02",
    )

    CloseMessageWindow()

    def lambda_7B7B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7B7B)
    Sleep(10)

    def lambda_7B8B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7B8B)
    Sleep(10)

    def lambda_7B9B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7B9B)
    Sleep(10)

    def lambda_7BAB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7BAB)
    WaitChrThread(0x105, 2)
    Sleep(500)

    #C0490
    ChrTalk(
        0x101,
        (
            "#12P#00000F来，小桃，\x01",
            "拿好吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x101, 0x0, 0x3E8, 0x5DC, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0491
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#16I小桃的伞\x07\x00",
            "交出去了。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('梅琳的伞', 1)
    OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x5DC, 0x0)

    #C0492
    ChrTalk(
        0xF,
        (
            "呜……\x01",
            "啊……是我的伞……\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0xF,
        (
            "这是爸爸特意买给我\x01",
            "的很重要的雨伞……\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xF,
        (
            "谢、谢谢……\x01",
            "真是太谢谢了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x109,
        (
            "#12P#10105F哦哦，原来是爸爸买的啊。\x02\x03",

            "#10100F呵呵，能顺利找回来，\x01",
            "真是太好啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0xF,
        "嗯……！\x02",
    )

    CloseMessageWindow()

    def lambda_7D29():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7D29)
    Sleep(50)

    def lambda_7D39():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7D39)
    Sleep(50)

    def lambda_7D49():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7D49)
    Sleep(50)

    def lambda_7D59():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7D59)
    Sleep(300)

    #C0497
    ChrTalk(
        0x105,
        (
            "#6P#10304F好啦，这样就算是\x01",
            "告一段落了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x8,
        "#11P多亏有你们，真是帮大忙了。\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x8,
        (
            "#11P你们果然\x01",
            "值得信赖啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0xA,
        (
            "如果以后再有什么事，\x01",
            "还要请你们帮忙哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x102,
        (
            "#6P#00100F嗯，随时恭候\x01",
            "各位的委托。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x101,
        "#6P#00000F那我们就先告辞了，奥斯卡。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0503
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找遗失的雨伞】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 52100, 0, -200, 270)
    TurnDirection(0xA, 0xF, 0)
    TurnDirection(0xF, 0xA, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_29(0x6B, 0x1, 0x5)
    OP_29(0x6B, 0x1, 0x6)
    OP_29(0x6B, 0x4, 0x10)
    OP_29(0xA1, 0x1, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xF, 0x10)
    OP_C9(0x1, 0x1000)
    EventEnd(0x5)
    Return()

    # Function_27_7A87 end

    def Function_28_7EF9(): pass

    label("Function_28_7EF9")

    EventBegin(0x0)
    Fade(500)
    OP_68(52330, 2200, -660, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(23210, 0)
    SetChrPos(0x101, 53850, 0, 1490, 90)
    SetChrPos(0x102, 53850, 0, 500, 90)
    SetChrPos(0x103, 52650, 0, 1490, 90)
    SetChrPos(0x109, 52650, 0, 500, 90)
    SetChrPos(0x104, 51450, 0, 1490, 90)
    SetChrPos(0x105, 51450, 0, 500, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x8, 0x10E, 0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80A8")

    #C0504
    ChrTalk(
        0x8,
        "哦，罗伊德，你来了啊。\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x8,
        (
            "这次的新品\x01",
            "是贝奈特做的面包，\x01",
            "拿去尝尝吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0506
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x212),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('贝奈特绝品', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0507
    ChrTalk(
        0x101,
        (
            "#00000F谢啦，奥斯卡。\x01",
            "就让我尝尝看吧。\x02\x03",

            "不过我们今天是为了工作而来的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8108")

    label("loc_80A8")


    #C0508
    ChrTalk(
        0x8,
        (
            "哦，罗伊德，你来了啊。\x01",
            "是来我们这里买面包的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x101,
        "#00000F那个，今天是为了工作而来的……\x02",
    )

    CloseMessageWindow()

    label("loc_8108")

    SetChrName("")

    #A0510
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将『美食向导』取材一事的\x01",
            "情况做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0511
    ChrTalk(
        0x8,
        (
            "哦哦，说起来，\x01",
            "确实听通讯社的人说过那件事。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x8,
        (
            "唔，我们这里的面包都很不错，\x01",
            "每一种都值得推荐……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81FC")

    #C0513
    ChrTalk(
        0x8,
        (
            "如果硬要选择的话，\x01",
            "那就还是推荐刚才给你们的\x01",
            "『贝奈特绝品』吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 2)
    Jump("loc_8241")

    label("loc_81FC")


    #C0514
    ChrTalk(
        0x8,
        (
            "如果硬要选择的话，那就还是推荐\x01",
            "以前给过你们的『贝奈特绝品』吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8241")


    #C0515
    ChrTalk(
        0x102,
        "#00105F哎，这样啊。\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x8,
        (
            "嗯，在贝奈特的作品之中，\x01",
            "这款面包实在是非常不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x8,
        (
            "它绝对是『摩尔吉』面包店\x01",
            "目前最美味的──\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("贝奈特的声音")

    #A0518
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "等、等一下！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_82FC():

        label("loc_82FC")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_82FC")

    QueueWorkItem2(0x109, 0, lambda_82FC)

    def lambda_830E():

        label("loc_830E")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_830E")

    QueueWorkItem2(0x102, 0, lambda_830E)

    def lambda_8320():

        label("loc_8320")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_8320")

    QueueWorkItem2(0x104, 0, lambda_8320)

    def lambda_8332():

        label("loc_8332")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_8332")

    QueueWorkItem2(0x101, 0, lambda_8332)

    def lambda_8344():

        label("loc_8344")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_8344")

    QueueWorkItem2(0x105, 0, lambda_8344)

    def lambda_8356():

        label("loc_8356")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_8356")

    QueueWorkItem2(0x103, 0, lambda_8356)

    def lambda_8368():

        label("loc_8368")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_8368")

    QueueWorkItem2(0x8, 1, lambda_8368)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8403")
    OP_68(55480, 1510, 1690, 1500)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_83B6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_83B6)
    SetChrPos(0xA, 60080, 10, 4000, 135)
    OP_95(0xA, 59190, 10, 2000, 3000, 0x0)
    OP_95(0xA, 57580, 10, 2090, 3000, 0x0)
    OP_64(0xA)
    Jump("loc_8484")

    label("loc_8403")

    OP_68(52700, 1510, 1930, 1500)
    MoveCamera(45, 22, 0, 1500)
    OP_6E(340, 1500)
    SetCameraDistance(23210, 1500)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetChrPos(0xA, 52110, 1000, 10270, 315)
    ClearChrFlags(0xA, 0x4)
    OP_95(0xA, 52470, 0, 4720, 3000, 0x0)
    OP_95(0xA, 53600, 0, 4100, 3000, 0x0)
    OP_64(0xA)

    label("loc_8484")

    EndChrThread(0x101, 0x0)
    EndChrThread(0x102, 0x0)
    EndChrThread(0x103, 0x0)
    EndChrThread(0x104, 0x0)
    EndChrThread(0x109, 0x0)
    EndChrThread(0x105, 0x0)
    EndChrThread(0x8, 0x1)

    #C0519
    ChrTalk(
        0x8,
        (
            "哦，贝奈特，\x01",
            "我正要将你的面包——\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0xA,
        (
            "不、不要自作主张！\x01",
            "在我眼里，那款面包\x01",
            "只是未完成品而已！\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xA,
        (
            "在做出胜过你的\x01",
            "面包之前，\x01",
            "才不要参加什么美食向导……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x8,
        (
            "哈哈，介绍一下有什么不好嘛，\x01",
            "这款面包明明很美味啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xA,
        "……唔……！！\x02",
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0xA,
        (
            "总、总之……\x01",
            "要是你敢擅自推荐，\x01",
            "我一定不会饶过你！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8639")
    OP_95(0xA, 59190, 10, 2000, 3000, 0x0)
    OP_95(0xA, 60330, 0, 3200, 3000, 0x0)

    def lambda_8603():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_8603)
    OP_95(0xA, 60080, 10, 4000, 2000, 0x0)
    SetChrPos(0xA, 119120, 0, -660, 275)
    Jump("loc_86AA")

    label("loc_8639")

    OP_95(0xA, 52470, 0, 4720, 3000, 0x0)
    OP_95(0xA, 52110, 1000, 10270, 3000, 0x0)
    OP_95(0xA, 51750, 1000, 10270, 3000, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8694")
    SetChrPos(0xA, 51280, 1000, 12870, 180)
    Jump("loc_86A5")

    label("loc_8694")

    SetChrPos(0xA, 51280, 1000, 12870, 90)

    label("loc_86A5")

    ClearChrFlags(0xA, 0x4)

    label("loc_86AA")

    OP_68(53180, 2200, 190, 1500)
    MoveCamera(45, 22, 0, 1500)
    OP_6E(340, 1500)
    SetCameraDistance(23210, 1500)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)

    #C0525
    ChrTalk(
        0x8,
        (
            "哎，搞什么啊，贝奈特那家伙，\x01",
            "我都和她说过面包很美味了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_87AD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_87AD)
    Sleep(50)

    def lambda_87BD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_87BD)
    Sleep(50)

    def lambda_87CD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_87CD)
    Sleep(50)

    def lambda_87DD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_87DD)
    Sleep(50)

    def lambda_87ED():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_87ED)
    Sleep(50)

    def lambda_87FD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_87FD)
    Sleep(300)

    #C0526
    ChrTalk(
        0x105,
        "#10304F呵呵，我看正是因为如此，她才会介意的。\x02",
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x104,
        "#00309F哈哈，你也很会察言观色啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0528
    ChrTalk(
        0x101,
        (
            "#00006F总、总之……\x01",
            "贝奈特小姐似乎很抵触，\x01",
            "还是给我们介绍些别的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x8,
        "唔，真没办法啊。\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x8,
        (
            "那就请大家品尝\x01",
            "我正在试做的\x01",
            "『鲜嫩猪排三明治』吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0531
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人品尝了『鲜嫩猪排三明治』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0532
    ChrTalk(
        0x109,
        (
            "#10100F（咀嚼）……\x01",
            "呼，口感非常松软……\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x101,
        (
            "#00000F嗯，肉饼也\x01",
            "鲜嫩多汁……\x01",
            "真好吃啊，奥斯卡。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x8,
        "哈哈，谢谢夸奖。\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x8,
        (
            "不过，那只是试制品。\x01",
            "要想作为正式商品销售，\x01",
            "还需要继续改良呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x103,
        (
            "#00205F这样啊……\x02\x03",

            "#00203F既然如此，\x01",
            "我们似乎不该\x01",
            "介绍它吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x8,
        (
            "由你们决定好了，\x01",
            "等到完成之后，\x01",
            "我还会再送给大家品尝的。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x102,
        "#00100F嗯，非常期待。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AC3")
    SetScenarioFlags(0x1, 2)

    label("loc_8AC3")

    SetScenarioFlags(0x172, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_8AF7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_8B14")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_8B27")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_8B3A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_8B57")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_8B6A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_8B87")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_8B9A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_8BB7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_8BCA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_8BE7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BE7")

    OP_29(0x80, 0x1, 0x6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8CBC")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0539
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在六家饮食店完成了取材！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8CB3")

    #A0540
    AnonymousTalk(
        0x101,
        (
            "#00003F现在就可以去向\x01",
            "格蕾丝小姐报告了……\x02\x03",

            "#00000F不过，还没有把六个人\x01",
            "喜欢的美食全部找到。\x01",
            "不如再努努力吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_8CB3")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_8CBC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D7F")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0541
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "找到了特别任务支援科\x01",
            "全体成员各自喜欢的美食。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0542
    AnonymousTalk(
        0x101,
        (
            "#00000F这样一来，已经找到\x01",
            "所有人喜欢的美食了啊。\x02\x03",

            "取材工作已经足够了，\x01",
            "马上去通讯社报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_8D7F")

    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 53850, 0, 1490, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_7EF9 end

    def Function_29_8DB3(): pass

    label("Function_29_8DB3")

    TalkBegin(0xA)

    #C0543
    ChrTalk(
        0xA,
        (
            "呼……\x01",
            "还是做不出可以胜过\x01",
            "奥斯卡的新品面包啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xA,
        (
            "不行，绝对不能放弃，\x01",
            "无论失败多少次，也要继续挑战……！\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x101,
        (
            "#00003F（要不要邀请她来担当\x01",
            "  职业女性选秀活动中的『技师』呢……？）\x02\x03",

            "#00000F那个，不好意思，\x01",
            "有件事情想和你商量……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0546
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人邀请对方参加\x01",
            "慈善宴会中的职业女性选秀活动。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0547
    ChrTalk(
        0xA,
        "……啊！？职业女性选秀！？\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xA,
        (
            "容、容我拒绝吧。\x01",
            "参加那种活动太不符合我的性格……\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xA,
        (
            "我已经帮忙制作了\x01",
            "慈善宴会中的料理，\x01",
            "至于职业女性选秀，还是容我拒绝吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x101,
        (
            "#00003F是、是吗……\x01",
            "那就没办法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x102,
        "#00100F还是去问问其他人吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 6)
    SetScenarioFlags(0x1, 3)
    TalkEnd(0xA)
    Return()

    # Function_29_8DB3 end

    SaveToFile()

Try(main)
