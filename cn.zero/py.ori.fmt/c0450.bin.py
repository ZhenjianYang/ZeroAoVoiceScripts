from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0450.bin",                # FileName
        "c0450",                    # MapName
        "c0450",                    # Location
        0x0024,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 36, 0, 4, 0, 5],
    )

    BuildStringList((
        "c0450",                  # 0
        "接待员凯尔",             # 1
        "德莉丝",                 # 2
        "亚伦",                   # 3
        "雷缇希亚经理",           # 4
        "冈兹",                   # 5
        "比克森镇长",             # 6
        "罗伯兹主任",             # 7
        "特伦特",                 # 8
    ))

    AddCharChip((
        "chr/ch22000.itc",                   # 00
        "chr/ch25700.itc",                   # 01
        "chr/ch27500.itc",                   # 02
        "chr/ch27900.itc",                   # 03
        "apl/ch50409.itc",                   # 04
        "chr/ch23200.itc",                   # 05
        "chr/ch29300.itc",                   # 06
        "chr/ch24400.itc",                   # 07
    ))

    DeclNpc(65440,   0,       59970,   270,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4090,    9,       59900,   225,  261,  0x0, 0,   1,   0,   0,   2,   0,   11,  255,  0)
    DeclNpc(50740,   0,       9750,    90,   261,  0x0, 0,   2,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(-3990,   0,       7000,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(162000,  649,     5900,    90,   406,  0x0, 0,   4,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(162000,  0,       4500,    0,    389,  0x0, 0,   5,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(3549,    0,       4360,    45,   389,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(114809,  0,       61029,   180,  389,  0x0, 0,   7,   0,   0,   0,   0,   13,  255,  0)

    DeclActor(-3500,   0,       7000,    1500,    -3990,   1500,    7000,    0x007E, 0,  6,  0x0000)
    DeclActor(64300,   0,       59970,   1500,    65440,   1500,    59970,   0x007E, 0,  8,  0x0000)
    DeclActor(68130,   10,      11650,   1200,    68130,   1500,    11650,   0x007C, 0,  14, 0x0000)
    DeclActor(162620,  0,       6480,    1200,    161500,  1500,    5570,    0x007E, 0,  15, 0x0000)

    ScpFunction((
        "Function_0_28C",          # 00, 0
        "Function_1_344",          # 01, 1
        "Function_2_3A5",          # 02, 2
        "Function_3_3D0",          # 03, 3
        "Function_4_3FB",          # 04, 4
        "Function_5_64E",          # 05, 5
        "Function_6_76C",          # 06, 6
        "Function_7_770",          # 07, 7
        "Function_8_1628",         # 08, 8
        "Function_9_162C",         # 09, 9
        "Function_10_20DC",        # 0A, 10
        "Function_11_29A3",        # 0B, 11
        "Function_12_3240",        # 0C, 12
        "Function_13_3AB6",        # 0D, 13
        "Function_14_3EEB",        # 0E, 14
        "Function_15_3F11",        # 0F, 15
        "Function_16_4026",        # 10, 16
        "Function_17_4333",        # 11, 17
        "Function_18_63A1",        # 12, 18
        "Function_19_63DF",        # 13, 19
        "Function_20_63FB",        # 14, 20
        "Function_21_6417",        # 15, 21
        "Function_22_6433",        # 16, 22
        "Function_23_644F",        # 17, 23
        "Function_24_646B",        # 18, 24
        "Function_25_6C2D",        # 19, 25
    ))


    def Function_0_28C(): pass

    label("Function_0_28C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2CC"),
        (1, "loc_2D8"),
        (2, "loc_2E4"),
        (3, "loc_2F0"),
        (4, "loc_2FC"),
        (5, "loc_308"),
        (6, "loc_314"),
        (SWITCH_DEFAULT, "loc_320"),
    )


    label("loc_2CC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_2D8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_2E4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_2F0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_2FC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_308")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_314")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_320")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_32C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_343")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_343")

    Return()

    # Function_0_28C end

    def Function_1_344(): pass

    label("Function_1_344")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A4")
    OP_95(0xFE, 72280, 0, 9750, 1000, 0x0)
    OP_95(0xFE, 72280, 0, 5580, 1000, 0x0)
    OP_95(0xFE, 50740, 0, 5580, 1000, 0x0)
    OP_95(0xFE, 50740, 0, 9750, 1000, 0x0)
    Jump("Function_1_344")

    label("loc_3A4")

    Return()

    # Function_1_344 end

    def Function_2_3A5(): pass

    label("Function_2_3A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CF")
    OP_94(0xFE, 0x604, 0xD714, 0x17C0, 0xFB9A, 0x3E8)
    Sleep(300)
    Jump("Function_2_3A5")

    label("loc_3CF")

    Return()

    # Function_2_3A5 end

    def Function_3_3D0(): pass

    label("Function_3_3D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FA")
    OP_94(0xFE, 0xFAD1, 0x141E, 0x11B66, 0x2652, 0x3E8)
    Sleep(300)
    Jump("Function_3_3D0")

    label("loc_3FA")

    Return()

    # Function_3_3D0 end

    def Function_4_3FB(): pass

    label("Function_4_3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_40A")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 17)

    label("loc_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_428")
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    BeginChrThread(0xD, 0, 0, 0)
    Jump("loc_64D")

    label("loc_428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_446")
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    BeginChrThread(0xD, 0, 0, 0)
    Jump("loc_64D")

    label("loc_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_48E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_489")
    SetChrPos(0xA, -2009, 0, 9290, 270)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    BeginChrThread(0xD, 0, 0, 0)

    label("loc_489")

    Jump("loc_64D")

    label("loc_48E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_4B0")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_64D")

    label("loc_4B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4BE")
    Jump("loc_64D")

    label("loc_4BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4E0")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_64D")

    label("loc_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4EE")
    Jump("loc_64D")

    label("loc_4EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_553")
    SetChrPos(0xA, 4550, 0, 5360, 225)
    BeginChrThread(0xA, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_524")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_54E")

    label("loc_524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_537")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_54E")

    label("loc_537")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_549")
    Jump("loc_54E")

    label("loc_549")

    ClearChrFlags(0xE, 0x80)

    label("loc_54E")

    Jump("loc_64D")

    label("loc_553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_561")
    Jump("loc_64D")

    label("loc_561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5AC")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    SetChrPos(0xA, 4550, 0, 5360, 225)
    SetChrPos(0x9, 68150, 0, 7780, 225)
    SetChrFlags(0xA, 0x10)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0x9, 0, 0, 3)
    Jump("loc_64D")

    label("loc_5AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5ED")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xA, 4550, 0, 5360, 225)
    SetChrPos(0x9, 68150, 0, 7780, 225)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0x9, 0, 0, 3)
    Jump("loc_64D")

    label("loc_5ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5FB")
    Jump("loc_64D")

    label("loc_5FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_620")
    SetChrPos(0x9, 114570, 0, 61510, 270)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_64D")

    label("loc_620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_62E")
    Jump("loc_64D")

    label("loc_62E")

    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64D")
    SetChrFlags(0xF, 0x10)
    OP_93(0xF, 0x0, 0x0)

    label("loc_64D")

    Return()

    # Function_4_3FB end

    def Function_5_64E(): pass

    label("Function_5_64E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D0")

    label("loc_66A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_686")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D0")

    label("loc_686")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A2")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D0")

    label("loc_6A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BE")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D0")

    label("loc_6BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_6D0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D0")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F3")
    SetMapObjFrame(0xFF, "futon", 0x0, 0x1)
    OP_66(0x3, 0x1)

    label("loc_6F3")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70F")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_70F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_71D")
    Jump("loc_76B")

    label("loc_71D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_76B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_737")
    Jump("loc_76B")

    label("loc_737")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_745")
    Jump("loc_76B")

    label("loc_745")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_76B")
    OP_1B(0x3, 0x0, 0x13)
    OP_1B(0x4, 0x0, 0x14)
    OP_1B(0xB, 0x0, 0x15)
    OP_1B(0xD, 0x0, 0x16)
    OP_1B(0xF, 0x0, 0x17)

    label("loc_76B")

    Return()

    # Function_5_64E end

    def Function_6_76C(): pass

    label("Function_6_76C")

    Call(0, 7)
    Return()

    # Function_6_76C end

    def Function_7_770(): pass

    label("Function_7_770")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AA")

    #C0001
    ChrTalk(
        0xB,
        "欢迎光临『千禧酒店』。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xB,
        (
            "呵呵，本酒店\x01",
            "为您提供多种多样的服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xB,
        (
            "可以让您在欢乐之都克洛斯贝尔\x01",
            "享受完美的一天。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(828, 0, 100, 0)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在酒店或酒馆里休息\x01",
            "可以回复ＣＰ。\x02",
        )
    )

    CloseMessageWindow()

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在普通酒馆里可以回复ＣＰ１００，\x01",
            "在高级酒店里可以回复ＣＰ２００。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A7")
    SetScenarioFlags(0x0, 0)

    label("loc_8A7")

    SetScenarioFlags(0x4B, 4)

    label("loc_8AA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1624")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_904")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_904")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_924")
    OP_AF(0x3C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_161F")

    label("loc_924")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_938")
    Jump("loc_161F")

    label("loc_938")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_161F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9C0")

    #C0006
    ChrTalk(
        0xB,
        (
            "我听传闻说，好像不止是冈兹先生，\x01",
            "市里还有好几个人也失踪了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xB,
        "到底发生了什么事呢……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_161F")

    label("loc_9C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_AAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A25")

    #C0008
    ChrTalk(
        0xB,
        (
            "就算是酒店方面，\x01",
            "也很难应对这种情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xB,
        (
            "希望冈兹先生\x01",
            "没发生什么意外。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAA")

    label("loc_A25")


    #C0010
    ChrTalk(
        0xB,
        (
            "冈兹先生今天一大早\x01",
            "就独自出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xB,
        (
            "因为听说他喝得酩酊大醉，\x01",
            "亚伦先生\x01",
            "还跟他搭话了……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xB,
        (
            "希望冈兹先生\x01",
            "没发生什么意外。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_AAA")

    Jump("loc_161F")

    label("loc_AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_CBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_C39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B13")

    #C0013
    ChrTalk(
        0xB,
        (
            "呵呵，冈兹先生\x01",
            "醉得很厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xB,
        (
            "稍后让人\x01",
            "送水到他的房间吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C34")

    label("loc_B13")


    #C0015
    ChrTalk(
        0xB,
        (
            "那个……冈兹先生\x01",
            "到底发生了什么事？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        (
            "要不然，就和\x01",
            "乌尔斯拉医院联系一下，\x01",
            "让他们派急救车来吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#0003F（虽然很担心冈兹先生，\x01",
            "  但现在不应该把重心放在这里……）\x02\x03",

            "#0012F那、那个……\x01",
            "他好像只是有点\x01",
            "喝醉了。\x02\x03",

            "#0000F现在有人陪同，\x01",
            "应该没问题的。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xB,
        (
            "啊，是吗？\x01",
            "那我就放心了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_C34")

    Jump("loc_CBA")

    label("loc_C39")


    #C0019
    ChrTalk(
        0xB,
        (
            "住在这里的冈兹先生……\x01",
            "今天也心情不错地出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xB,
        (
            "听说从玛因兹那边来了\x01",
            "接他的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xB,
        (
            "不在房间里等着，\x01",
            "真的不要紧吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CBA")

    Jump("loc_161F")

    label("loc_CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_D7F")

    #C0022
    ChrTalk(
        0xB,
        (
            "两个月前整顿好的\x01",
            "导力网络预约系统，\x01",
            "总算走上了正轨啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xB,
        "接下来，只要等着网络扩大就好了……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xB,
        (
            "也许要花些时间，\x01",
            "不过本酒店已经提前架设好了系统，\x01",
            "应该可以做出妥善应对。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_161F")

    label("loc_D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_DEB")

    #C0025
    ChrTalk(
        0xB,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xB,
        (
            "本酒店今年已经创业六十周年了，\x01",
            "今后也会一如既往，诚心诚意地\x01",
            "为客人服务。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_161F")

    label("loc_DEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1036")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EDD")

    #C0027
    ChrTalk(
        0xB,
        "客、客人……！？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xB,
        (
            "本酒店不允许\x01",
            "带宠物进来……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        "#0006F抱歉，这是我们的警犬。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x103,
        (
            "#0203F需要带它进行一次调查，\x01",
            "请不要放在心上。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xB,
        "是、是这样吗？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xB,
        (
            "那真是失礼了，\x01",
            "请随意调查吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x95, 5)
    TalkEnd(0xB)
    Return()

    label("loc_EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F4D")

    #C0033
    ChrTalk(
        0xB,
        (
            "服务业的本质是向需要帮助的人\x01",
            "伸出援手……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xB,
        (
            "本酒店也以利贝尔王国酒店\x01",
            "的服务精神为榜样呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1031")

    label("loc_F4D")


    #C0035
    ChrTalk(
        0xB,
        (
            "之前，利贝尔王国曾发生过一场大事件，\x01",
            "名为柏斯的都市\x01",
            "遭到了巨龙的袭击。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xB,
        (
            "在那个时候，城内的酒店业人士首先站了出来，\x01",
            "为受灾者提供了住宿保障。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xB,
        (
            "真是服务精神的极致体现啊……\x01",
            "本千禧酒店也想\x01",
            "以此为榜样，不断超越自我。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1031")

    Jump("loc_161F")

    label("loc_1036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_10B4")

    #C0038
    ChrTalk(
        0xB,
        (
            "有许多客人是为了体验在巴鲁卡等店\x01",
            "游玩的乐趣而前来观光的。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xB,
        (
            "正可谓是欢乐之都克洛斯贝尔\x01",
            "特有的客户层啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_161F")

    label("loc_10B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1116")

    #C0040
    ChrTalk(
        0xB,
        (
            "今天也是一样，几乎所有的\x01",
            "客房都被预定出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xB,
        (
            "如果您想定房，\x01",
            "还请尽快啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_161F")

    label("loc_1116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_11A2")

    #C0042
    ChrTalk(
        0xB,
        (
            "导力网络只覆盖在\x01",
            "克洛斯贝尔市内、米修拉姆，\x01",
            "还有乌尔斯拉医院这些地区。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xB,
        (
            "本酒店引入的导力网络，\x01",
            "目前多用于\x01",
            "商业活动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_161F")

    label("loc_11A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1216")

    #C0044
    ChrTalk(
        0xB,
        (
            "今天让爱普斯泰恩财团的人\x01",
            "过来安装了导力网络。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xB,
        (
            "这样一来，本酒店\x01",
            "就可以提供更加完善的服务了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_161F")

    label("loc_1216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_12DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_127D")

    #C0046
    ChrTalk(
        0xB,
        (
            "近期就可以开始利用\x01",
            "导力网络进行预约服务了。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xB,
        (
            "请耐心等待\x01",
            "服务正式开通。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D7")

    label("loc_127D")


    #C0048
    ChrTalk(
        0xB,
        (
            "本酒店近期就可以开始\x01",
            "利用导力网络\x01",
            "进行预约服务了。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xB,
        (
            "请耐心等待\x01",
            "服务正式开通。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_12D7")

    Jump("loc_161F")

    label("loc_12DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_13AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1333")

    #C0050
    ChrTalk(
        0xB,
        (
            "网络预约服务开通以后，\x01",
            "我们便会大幅度\x01",
            "领先于同类行业了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A7")

    label("loc_1333")


    #C0051
    ChrTalk(
        0xB,
        (
            "承蒙各位的关照，\x01",
            "本酒店在欢乐街中获得了\x01",
            "属一属二的营业额。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xB,
        (
            "不过竞争对手也不少，\x01",
            "所以绝对不能放松警惕。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_13A7")

    Jump("loc_161F")

    label("loc_13AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_14CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_142E")

    #C0053
    ChrTalk(
        0xB,
        (
            "克洛斯贝尔在下下个月\x01",
            "会举行创立纪念庆典，\x01",
            "还会上演彩虹剧团的新剧。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xB,
        (
            "到那个时候，\x01",
            "人肯定会特别多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C5")

    label("loc_142E")


    #C0055
    ChrTalk(
        0xB,
        (
            "克洛斯贝尔在下下个月\x01",
            "有许多大型活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xB,
        (
            "比如自治州的创立纪念庆典……\x01",
            "还有彩虹剧团的\x01",
            "新剧公演。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xB,
        (
            "届时应该会十分拥挤，\x01",
            "还请尽早预约房间。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_14C5")

    Jump("loc_161F")

    label("loc_14CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1526")

    #C0058
    ChrTalk(
        0xB,
        (
            "本酒店\x01",
            "为您提供\x01",
            "各项代理服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xB,
        "我们非常乐意为您服务，还请随意吩咐。\x02",
    )

    CloseMessageWindow()
    Jump("loc_161F")

    label("loc_1526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_15A2")

    #C0060
    ChrTalk(
        0xB,
        (
            "本酒店负责导游、美容、沙龙\x01",
            "以及各类门票的预约服务……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xB,
        (
            "可以让您在欢乐之都克洛斯贝尔\x01",
            "享受完美的一天。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_161F")

    label("loc_15A2")


    #C0062
    ChrTalk(
        0xB,
        "欢迎光临『千禧酒店』。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xB,
        (
            "呵呵，本酒店\x01",
            "为您提供多种多样的服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xB,
        (
            "可以让您在欢乐之都克洛斯贝尔\x01",
            "享受完美的一天。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_161F")

    Jump("loc_8B4")

    label("loc_1624")

    TalkEnd(0xB)
    Return()

    # Function_7_770 end

    def Function_8_1628(): pass

    label("Function_8_1628")

    Call(0, 9)
    Return()

    # Function_8_1628 end

    def Function_9_162C(): pass

    label("Function_9_162C")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_173E")

    #C0065
    ChrTalk(
        0x8,
        (
            "欢迎。\x01",
            "欢迎光临『千禧酒店』。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "如果需要预约房间，\x01",
            "请在本服务台办理手续。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(828, 0, 100, 0)
    SetChrName("")

    #A0067
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在酒店或酒馆里休息\x01",
            "可以回复ＣＰ。\x02",
        )
    )

    CloseMessageWindow()

    #A0068
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在普通酒馆里可以回复ＣＰ１００，\x01",
            "在高级酒店里可以回复ＣＰ２００。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_173B")
    SetScenarioFlags(0x0, 1)

    label("loc_173B")

    SetScenarioFlags(0x4B, 4)

    label("loc_173E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1748")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20D8")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1798")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1798")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B8")
    OP_AF(0x3C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20D3")

    label("loc_17B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17CC")
    Jump("loc_20D3")

    label("loc_17CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20D3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1846")

    #C0069
    ChrTalk(
        0x8,
        "工作到这么晚，真是辛苦各位了，\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "需要定房吗？\x01",
            "本酒店随时可以办理入住手续。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D3")

    label("loc_1846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_18E2")

    #C0071
    ChrTalk(
        0x8,
        (
            "有些商务人士\x01",
            "刚刚办理完\x01",
            "退房手续。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "要到下午之后，才能办理正式入住手续……\x01",
            "不过，如果您需要稍作休息的话，\x01",
            "我们这就可以为您准备房间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D3")

    label("loc_18E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1973")

    #C0073
    ChrTalk(
        0x8,
        (
            "冈兹先生办理了长期租住手续，\x01",
            "是本酒店豪华套间的长期客户。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "虽然这位客人过于任性，\x01",
            "但我们会以专业的态度和\x01",
            "诚意来为他服务。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D3")

    label("loc_1973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1A00")

    #C0075
    ChrTalk(
        0x8,
        (
            "本店住着许多从\x01",
            "巴鲁卡回来的客人。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "有些客人还让\x01",
            "女公关回房间服侍……\x01",
            "哎呀，真是令人羡……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        "……不，我什么也没说。\x02",
    )

    CloseMessageWindow()
    Jump("loc_20D3")

    label("loc_1A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1AA2")

    #C0078
    ChrTalk(
        0x8,
        (
            "在纪念庆典期间，\x01",
            "虽然十分繁忙，\x01",
            "但是也有忙碌的价值。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "果然，克洛斯贝尔的活力\x01",
            "跟其它国家就是不同啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "能在这里的酒店工作，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D3")

    label("loc_1AA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1B31")

    #C0081
    ChrTalk(
        0x8,
        (
            "本酒店贯彻着\x01",
            "无微不至的奉献式服务理念。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "这是雷缇希亚经理\x01",
            "从时代百货店的经理身上学到的，\x01",
            "在服务业中，这是最重要的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D3")

    label("loc_1B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1B97")

    #C0083
    ChrTalk(
        0x8,
        (
            "本酒店的每个房间里\x01",
            "都有内线用的通讯器。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "如果有什么事情的话，\x01",
            "请与服务台联系。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D3")

    label("loc_1B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1BE4")

    #C0085
    ChrTalk(
        0x8,
        (
            "差不多该到团体客人\x01",
            "回店的时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x8,
        "得准备好迎接他们。\x02",
    )

    CloseMessageWindow()
    Jump("loc_20D3")

    label("loc_1BE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1C4F")

    #C0087
    ChrTalk(
        0x8,
        (
            "本酒店拥有\x01",
            "三部导力车。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        (
            "提供接送客人\x01",
            "往返于车站和空港的服务，\x01",
            "有需要时请尽管提出。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D3")

    label("loc_1C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1CDF")

    #C0089
    ChrTalk(
        0x8,
        (
            "导力网络这种东西，\x01",
            "对于克洛斯贝尔来说，\x01",
            "还是一个未知事物。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "如果能早日安装起来，\x01",
            "肯定对将来有帮助……\x01",
            "这是经理的策略呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D3")

    label("loc_1CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1DEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1D51")

    #C0091
    ChrTalk(
        0x8,
        (
            "使用导力网络进行\x01",
            "预约服务，\x01",
            "是经理关注的重心。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "服务正式开始以后，\x01",
            "请您尽情利用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DEA")

    label("loc_1D51")


    #C0093
    ChrTalk(
        0x8,
        (
            "使用导力网络进行\x01",
            "预约服务，\x01",
            "是经理关注的重心。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "在市内的任何一个角落都可以\x01",
            "使用这种服务，十分便利。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "服务正式开始运营以后，\x01",
            "请尽情利用。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1DEA")

    Jump("loc_20D3")

    label("loc_1DEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1EFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1E68")

    #C0096
    ChrTalk(
        0x8,
        (
            "克洛斯贝尔市的法律对\x01",
            "观光产业有优待政策。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        (
            "作为参与到观光产业中的一员，\x01",
            "我感到十分光荣。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_1E68")


    #C0098
    ChrTalk(
        0x8,
        (
            "克洛斯贝尔市\x01",
            "为了发展旅游业，\x01",
            "制定了许多优惠政策。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "观光业与商业\x01",
            "都是本市的主要产业……\x01",
            "能参与主要产业，真是一件非常光荣的事情。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1EF5")

    Jump("loc_20D3")

    label("loc_1EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1F63")

    #C0100
    ChrTalk(
        0x8,
        (
            "早上好。\x01",
            "感谢您今日再度光临。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "正巧有刚刚退房的\x01",
            "客人离店，\x01",
            "所以空出了一间房间呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D3")

    label("loc_1F63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_202B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1FA5")

    #C0102
    ChrTalk(
        0x8,
        (
            "感谢经理给了我一个\x01",
            "如此有意义的工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2026")

    label("loc_1FA5")


    #C0103
    ChrTalk(
        0x8,
        (
            "我原本在帝国的酒店里工作，\x01",
            "后来就被现在的老板招揽了过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "呵呵，本酒店的客人数量很多，\x01",
            "这是一个十分有挑战性的工作。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2026")

    Jump("loc_20D3")

    label("loc_202B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_207C")

    #C0105
    ChrTalk(
        0x8,
        "现在有空房。\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "如果想预约客房的话，\x01",
            "请在本服务台办理手续。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D3")

    label("loc_207C")


    #C0107
    ChrTalk(
        0x8,
        (
            "欢迎。\x01",
            "欢迎光临『千禧酒店』。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "如果想预约客房的话，\x01",
            "请在本服务台办理手续。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_20D3")

    Jump("loc_1748")

    label("loc_20D8")

    TalkEnd(0x8)
    Return()

    # Function_9_162C end

    def Function_10_20DC(): pass

    label("Function_10_20DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2164")

    #C0109
    ChrTalk(
        0xA,
        (
            "比克森先生好像\x01",
            "非常担心冈兹先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        (
            "嗯……太过操心的话，会劳损身体的。\x01",
            "不然就去给他介绍一下\x01",
            "客房服务的内容吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_299F")

    label("loc_2164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_21E4")

    #C0111
    ChrTalk(
        0xA,
        (
            "嗯嗯……\x01",
            "冈兹先生之前的样子\x01",
            "似乎很奇怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xA,
        (
            "好像魂不附体一样……\x01",
            "虽说是大醉了两天，\x01",
            "但也不该是那种样子啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_299F")

    label("loc_21E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_22CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_224B")

    #C0113
    ChrTalk(
        0xA,
        (
            "总算把导力网络上的\x01",
            "预约数统计出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "……那么，\x01",
            "就来看看具体内容吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C6")

    label("loc_224B")


    #C0115
    ChrTalk(
        0xA,
        (
            "好了，得确认一下\x01",
            "今天导力网络上的预约数了。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        (
            "那种机械虽然看起来很复杂，\x01",
            "但只要学会了操作方法，\x01",
            "以后就非常轻松了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C6")

    Jump("loc_299F")

    label("loc_22CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_236A")

    #C0117
    ChrTalk(
        0xFE,
        (
            "最近有位客人\x01",
            "包下了一间\x01",
            "豪华套间呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "那是个非常豪爽的客人，\x01",
            "我们为他提供了\x01",
            "最高级别的服务呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "呵呵，希望各位\x01",
            "在走廊里保持安静哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_299F")

    label("loc_236A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_23DB")

    #C0120
    ChrTalk(
        0xA,
        (
            "最近好像没有看到\x01",
            "鲁巴彻商会的人\x01",
            "在欢乐街闲晃呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "嗯……在纪念庆典期间，\x01",
            "发生了什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_299F")

    label("loc_23DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2489")

    #C0122
    ChrTalk(
        0xA,
        (
            "彩虹剧团创立于\x01",
            "我升为服务员领班的\x01",
            "那一年。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xA,
        "这么算起来的话，也过去二十年了啊。\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        (
            "呵呵，看到彩虹剧团\x01",
            "拥有了如今这么高的人气，\x01",
            "我也由衷地感到高兴呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_299F")

    label("loc_2489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2504")

    #C0125
    ChrTalk(
        0xA,
        (
            "哎呀呀，比较复杂的操作\x01",
            "几乎都是由\x01",
            "专业人士来进行的。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xA,
        (
            "不过，如果只是保养机器的话，\x01",
            "我应该也能做到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_299F")

    label("loc_2504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_256C")

    #C0127
    ChrTalk(
        0xA,
        (
            "好了，该去查看一下\x01",
            "厨房的情况了。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xA,
        (
            "今天有很多团体客人，\x01",
            "上菜时也许会花一点时间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_299F")

    label("loc_256C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2588")

    #C0129
    ChrTalk(
        0xA,
        "嗯嗯……\x02",
    )

    CloseMessageWindow()
    Jump("loc_299F")

    label("loc_2588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2652")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_25DD")

    #C0130
    ChrTalk(
        0xA,
        (
            "我也上了年纪了。\x01",
            "网络预约系统那种东西，\x01",
            "实在是搞不懂啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_264D")

    label("loc_25DD")


    #C0131
    ChrTalk(
        0xA,
        (
            "经理推荐的\x01",
            "网上预约系统吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        (
            "好像是个很方便的东西，\x01",
            "但具体的使用方法和原理，\x01",
            "我可是一点都搞不懂。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_264D")

    Jump("loc_299F")

    label("loc_2652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_26D1")

    #C0133
    ChrTalk(
        0xA,
        (
            "最顶层的房间\x01",
            "全都是豪华套间。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        (
            "虽然房价要贵了一点，\x01",
            "但我们提供的可是一般房间\x01",
            "完全无法相比的最高等服务。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_299F")

    label("loc_26D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2769")

    #C0135
    ChrTalk(
        0xA,
        (
            "现有的这些工作人员都是\x01",
            "雷缇希亚在前年当上经理之后，\x01",
            "一手提拔的。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xA,
        (
            "呵呵……\x01",
            "虽然也有一些个性很强的服务员，\x01",
            "但大家都是十分优秀的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_299F")

    label("loc_2769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_28D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_27E2")

    #C0137
    ChrTalk(
        0xA,
        (
            "在前年结成互不侵犯条约以后，\x01",
            "客人增加了好多。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xA,
        (
            "果然还是必须得在意\x01",
            "周边诸国的政治动向啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D2")

    label("loc_27E2")


    #C0139
    ChrTalk(
        0xA,
        (
            "住在本酒店的客人\x01",
            "大多都是来自国外的游客……\x01",
            "我也一直在意着周边诸国的政治动向啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xA,
        (
            "比如……就在去年，\x01",
            "埃雷波尼亚、卡尔瓦德、利贝尔\x01",
            "这三国之间缔结了互不侵犯条约。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        (
            "自那之后，来往于三国间的客流量激增，\x01",
            "本店的客人也增加了很多。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_28D2")

    Jump("loc_299F")

    label("loc_28D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2939")

    #C0142
    ChrTalk(
        0xA,
        (
            "差不多到了游客\x01",
            "登记入住的时间了……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            "必须做好万全的准备，\x01",
            "认真迎接他们啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_299F")

    label("loc_2939")


    #C0144
    ChrTalk(
        0xA,
        (
            "本酒店今年已经\x01",
            "迎来了开业六十周年。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xA,
        (
            "最近我们还增加了团体旅游项目，\x01",
            "越来越受到客人的好评呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_299F")

    TalkEnd(0xFE)
    Return()

    # Function_10_20DC end

    def Function_11_29A3(): pass

    label("Function_11_29A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2A3F")

    #C0146
    ChrTalk(
        0x9,
        (
            "冈兹先生似乎\x01",
            "也没有去『巴鲁卡』。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x9,
        (
            "已经到……傍晚了呢，\x01",
            "还是通知警察比较好吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x9,
        (
            "……哎，各位就是警察吗？\x01",
            "真、真是失礼了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323C")

    label("loc_2A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2B1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2A8D")

    #C0149
    ChrTalk(
        0x9,
        (
            "呼……我竟然没有注意到客人的动向，\x01",
            "真是不好意思。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B17")

    label("loc_2A8D")


    #C0150
    ChrTalk(
        0x9,
        (
            "冈兹先生昨天\x01",
            "十分安静……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x9,
        (
            "嗯，是不是吃了\x01",
            "什么不好的东西呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x9,
        (
            "……呼，客人都已经失踪了，\x01",
            "我这样乱说好像有些不负责任啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2B17")

    Jump("loc_323C")

    label("loc_2B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2C45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2B96")

    #C0153
    ChrTalk(
        0x9,
        (
            "冈兹先生给的小费……\x01",
            "因为数额比较大，\x01",
            "所以我捐给市政厅了。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x9,
        (
            "……稍、稍微有点\x01",
            "浪费了吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C40")

    label("loc_2B96")


    #C0155
    ChrTalk(
        0x9,
        (
            "我从冈兹先生那里收到了\x01",
            "一笔很大金额的小费……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x9,
        (
            "因为放在手里挺害怕的，\x01",
            "所以干脆就捐给市政厅了。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x9,
        (
            "……虽然不知道政府会拿它来做什么，\x01",
            "但肯定比我拿着要好吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2C40")

    Jump("loc_323C")

    label("loc_2C45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2CE0")

    #C0158
    ChrTalk(
        0x9,
        (
            "住在最顶层的客人……\x01",
            "稍微有些吵闹，总有人来抱怨。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x9,
        (
            "但是从酒店角度来看，\x01",
            "双方都是重要的客人，站在我们的\x01",
            "立场上，也不能去多说什么啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323C")

    label("loc_2CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2D15")

    #C0160
    ChrTalk(
        0x9,
        (
            "早上好。\x01",
            "……一家人一起来住宿吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323C")

    label("loc_2D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2E67")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2D72")
    TurnDirection(0x9, 0x11C, 0)

    #C0161
    ChrTalk(
        0x9,
        (
            "请不、不要过来！\x01",
            "我有点怕狗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E0A")

    label("loc_2D72")

    TurnDirection(0x9, 0x11C, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0162
    ChrTalk(
        0x9,
        "狗、狗……！？\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x9,
        (
            "请不、不要过来！\x01",
            "我有点怕狗……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        "#0012F哈哈，那真是抱歉了。\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x11C,
        "#1203F呜噜噜噜噜……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2E0A")

    TalkEnd(0x9)
    Return()

    label("loc_2E0E")


    #C0166
    ChrTalk(
        0x9,
        (
            "出门的时候，\x01",
            "请把钥匙寄存在服务台。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x9,
        (
            "您外出的时候，\x01",
            "我们会为您整理床铺的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323C")

    label("loc_2E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2EB7")

    #C0168
    ChrTalk(
        0x9,
        (
            "放在房间里的饮料\x01",
            "都已经算在房费里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x9,
        (
            "您可以自由\x01",
            "取用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323C")

    label("loc_2EB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2F16")

    #C0170
    ChrTalk(
        0x9,
        (
            "打扫了一遍\x01",
            "房间和走廊。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x9,
        (
            "豪华套间里\x01",
            "需要整理的东西很多，\x01",
            "还是很辛苦的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323C")

    label("loc_2F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2FFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2F5E")

    #C0172
    ChrTalk(
        0x9,
        (
            "为了之后不被亚伦先生责骂，\x01",
            "得仔细打扫干净。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FFA")

    label("loc_2F5E")


    #C0173
    ChrTalk(
        0x9,
        "这样就算打扫完了吧……\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x9,
        (
            "为了之后不被亚伦先生责骂，\x01",
            "得仔细打扫干净。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x9,
        (
            "亚伦先生即使是在\x01",
            "生气的时候，也是那样一副表情，\x01",
            "反而让人觉得很可怕啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2FFA")

    Jump("loc_323C")

    label("loc_2FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_304C")

    #C0176
    ChrTalk(
        0x9,
        (
            "在最顶层，无论是走廊还是房间都很宽敞，\x01",
            "打扫起来很是辛苦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323C")

    label("loc_304C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_30EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_308F")

    #C0177
    ChrTalk(
        0x9,
        (
            "来看彩虹剧团\x01",
            "演出的客人\x01",
            "似乎又增加了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30E6")

    label("loc_308F")


    #C0178
    ChrTalk(
        0x9,
        (
            "彩虹剧团的新剧\x01",
            "终于要正式公演了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x9,
        (
            "这下，客人又要增加了。\x01",
            "得提起精神来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_30E6")

    Jump("loc_323C")

    label("loc_30EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_313D")

    #C0180
    ChrTalk(
        0x9,
        (
            "参加观光旅游团的客人\x01",
            "差不多快回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x9,
        (
            "得做好\x01",
            "迎接的准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323C")

    label("loc_313D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3196")

    #C0182
    ChrTalk(
        0x9,
        (
            "早上好。\x01",
            "欢迎光临『千禧酒店』。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x9,
        (
            "出门的时候\x01",
            "请注意\x01",
            "不要忘记东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323C")

    label("loc_3196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_31EA")

    #C0184
    ChrTalk(
        0x9,
        (
            "今年的客人比以往\x01",
            "任何一年都要多。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x9,
        (
            "房间很快\x01",
            "就全部订出去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323C")

    label("loc_31EA")


    #C0186
    ChrTalk(
        0x9,
        (
            "早上好。\x01",
            "请问您是来住宿的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x9,
        (
            "如果需要的话，\x01",
            "我可以帮您把行李拿到房间。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_323C")

    TalkEnd(0xFE)
    Return()

    # Function_11_29A3 end

    def Function_12_3240(): pass

    label("Function_12_3240")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34AD")
    TurnDirection(0xFE, 0x0, 0)

    #C0188
    ChrTalk(
        0x101,
        (
            "#0005F啊，您好像是\x01",
            "缇欧的上司……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x102,
        (
            "#0100F爱普斯泰恩财团的人\x01",
            "为什么要来酒店呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "哦，因为这家酒店要\x01",
            "搭建导力网络，\x01",
            "我是来监管的。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "企业或是酒店\x01",
            "只要提出申请，\x01",
            "就可以参加导力网络的试运营呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x104,
        (
            "#0300F原来如此……\x02\x03",

            "#0301F……不过，导力网络这种东西，\x01",
            "难道这么容易就能搭建吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x103,
        (
            "#0203F嗯，根据行业与用途的不同，\x01",
            "也需要经过一定的审查……\x02\x03",

            "#0200F不过，终端的装置费用\x01",
            "由ＩＢＣ全额支付，\x01",
            "应该算是十分优厚的试验条件了。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "是啊。\x01",
            "托它的福，我得以完成了许多一直想进行的测试，\x01",
            "真是太感谢伟大的ＩＢＣ了。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "哈哈哈，总之，\x01",
            "会操作终端的人还很少，\x01",
            "进行指导也很花时间的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xA, 0)
    SetScenarioFlags(0x92, 6)
    Jump("loc_3AB2")

    label("loc_34AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3768")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 6)), scpexpr(EXPR_END)), "loc_3517")

    #C0196
    ChrTalk(
        0xFE,
        "好了，这里的终端已经设置好了。\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "因为我是专家，\x01",
            "所以这种事情只是小意思啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3763")

    label("loc_3517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_358F")

    #C0198
    ChrTalk(
        0xFE,
        (
            "天真无邪的缇欧是不可能\x01",
            "有特殊目的的。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "嗯嗯，果然只是我的错觉。\x01",
            "支援科的各位，缇欧就拜托你们了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3763")

    label("loc_358F")


    #C0200
    ChrTalk(
        0xFE,
        "好了，这里的终端已经设置好了。\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "因为我是专家，\x01",
            "所以这种事情只是小意思啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x103,
        (
            "#0203F这个人虽然看上去很不可靠，\x01",
            "但却是『导力网络构想』\x01",
            "的开发主任之一呢。\x02\x03",

            "#0200F据说克洛斯贝尔的导力网络\x01",
            "进展得这么快，也都是主任的功劳。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 500)

    #C0203
    ChrTalk(
        0xFE,
        (
            "话、话是这样说啦……\x01",
            "那个，缇欧，你怎么变得和善多了？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x103,
        (
            "#0211F……有吗？\x01",
            "我觉得和平时一样啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "说…………说得也是啊！\x01",
            "哈哈，果然只是我的错觉～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 4)

    label("loc_3763")

    Jump("loc_3AB2")

    label("loc_3768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3803")

    #C0206
    ChrTalk(
        0xFE,
        (
            "那么，明天我会再来\x01",
            "进行设置。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "啊啊……现在请不要启动终端，\x01",
            "因为还需要进行初始化作业呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x103,
        (
            "#0200F（工作的时候\x01",
            "  明明很正常……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AB2")

    label("loc_3803")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3AB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_38CC")
    TurnDirection(0xFE, 0x103, 0)

    #C0209
    ChrTalk(
        0xFE,
        (
            "……缇欧，\x01",
            "如果终端损坏的话，就和我说一声吧！\x01",
            "马上就能把它修好！！\x02",
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
    Jump("loc_3AB2")

    label("loc_38CC")


    #C0210
    ChrTalk(
        0xFE,
        (
            "顺便一说，购买这么一套终端装置，\x01",
            "大概要花费一百五十万米拉。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "对普通市民来说，\x01",
            "仍然还是很遥远的东西啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0212
    ChrTalk(
        0x101,
        (
            "#0003F支援科的终端，\x01",
            "大家平时用得都很随便呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x103,
        (
            "#0200F没关系，物理性的故障\x01",
            "不会构成什么问题。\x01",
            "不必太过在意。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 500)

    #C0214
    ChrTalk(
        0xFE,
        (
            "……缇欧，\x01",
            "如果终端损坏的话，就和我说一声吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "马上就能把它修好！！\x01",
            "我一定会全力维修的！！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0216
    ChrTalk(
        0x103,
        (
            "#0200F不用了……我应该可以\x01",
            "自己修理的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_3AB2")

    TalkEnd(0xFE)
    Return()

    # Function_12_3240 end

    def Function_13_3AB6(): pass

    label("Function_13_3AB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('罗赞贝尔克人偶·Ｍ', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('罗赞贝尔克人偶·Ｓ', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('波波碰！β版', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AF5")
    TurnDirection(0x0, 0xF, 0)
    Call(0, 25)
    Return()

    label("loc_3AF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B1D")
    TurnDirection(0x0, 0xF, 0)
    Call(0, 24)
    Return()

    label("loc_3B1D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3D3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C73")

    #C0217
    ChrTalk(
        0xFE,
        "这样一来，总算能回国了～\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        "太感谢各位了～！\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x101,
        (
            "#0006F特伦特先生，不管怎么说，\x01",
            "还是请您先买个新背包吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "哎，嗯嗯。\x01",
            "说得对啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        "啊哈哈，谢谢啦～！\x02",
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

    #C0222
    ChrTalk(
        0x103,
        "#0200F（……这个人无论何时都这么开朗。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3D3A")

    label("loc_3C73")


    #C0223
    ChrTalk(
        0xFE,
        (
            "钱包没问题，土特产没问题，\x01",
            "车票也没问题！\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "啊，但是没有能放这些东西的包啊，\x01",
            "啊哈哈哈哈～！\x02",
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

    label("loc_3D3A")

    Jump("loc_3EE7")

    label("loc_3D3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_3E84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E20")

    #C0225
    ChrTalk(
        0xFE,
        (
            "来克洛斯贝尔观光\x01",
            "一直都是我的梦想。\x01",
            "一不小心就太投入了。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "呼，已经累得不想再找了～\x01",
            "克洛斯贝尔市实在是太大了。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "……啊，但是我预定\x01",
            "要在今天回国呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        "警察先生，请快点帮帮我吧～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3E7F")

    label("loc_3E20")


    #C0229
    ChrTalk(
        0xFE,
        (
            "唉，我已经很累了啊～\x01",
            "克洛斯贝尔市实在是太大了。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        "警察先生，总之，拜托你们快一点吧～！\x02",
    )

    CloseMessageWindow()

    label("loc_3E7F")

    Jump("loc_3EE7")

    label("loc_3E84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3E95")
    Jump("loc_3EE7")

    label("loc_3E95")


    #C0231
    ChrTalk(
        0xFE,
        (
            "呼～……\x01",
            "已经不想再走了～\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "真麻烦啊～……\x01",
            "不然就放弃这些，直接回去算了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EE7")

    TalkEnd(0xFE)
    Return()

    # Function_13_3AB6 end

    def Function_14_3EEB(): pass

    label("Function_14_3EEB")

    EventBegin(0x2)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0233
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门似乎上了锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_14_3EEB end

    def Function_15_3F11(): pass

    label("Function_15_3F11")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FCE")

    #C0234
    ChrTalk(
        0xC,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        "#0001F好像已经完全失去了知觉。\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x104,
        "#0301F这也是药的副作用吧。\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x102,
        "#0108F现在还无法判断……\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x103,
        "#0208F………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4022")

    label("loc_3FCE")


    #C0239
    ChrTalk(
        0xC,
        "……………………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0240
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "冈兹失去了知觉。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    label("loc_4022")

    TalkEnd(0xC)
    Return()

    # Function_15_3F11 end

    def Function_16_4026(): pass

    label("Function_16_4026")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_408F")

    #C0241
    ChrTalk(
        0xFE,
        "冈兹还是没有回来……\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "哦哦，女神啊……\x01",
            "请一定让玛因兹重要的\x01",
            "年轻人平安归来……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_432F")

    label("loc_408F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4182")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_410D")

    #C0243
    ChrTalk(
        0xFE,
        "哦哦，是你们啊……\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "真是的……冈兹那家伙，\x01",
            "真会给人添麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        "他到底跑到哪里去了……？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_417D")

    label("loc_410D")


    #C0246
    ChrTalk(
        0xFE,
        (
            "冈兹……\x01",
            "到底跑去哪里了……？\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "在你们百忙之中还麻烦你们，很不好意思。\x01",
            "不过，还请多注意一下他的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_417D")

    Jump("loc_432F")

    label("loc_4182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_432F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_429C")

    #C0248
    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "……抱歉，果然还是\x01",
            "无法掩盖我心中所受的打击啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        "#0008F镇长……\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "……冈兹绝不是那种\x01",
            "会染指违禁药物的年轻人。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "现在还不清楚那个药物\x01",
            "是不是那种东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "如果真的是违禁品的话，\x01",
            "我绝对不会原谅\x01",
            "把它交给冈兹的那个人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_432F")

    label("loc_429C")


    #C0254
    ChrTalk(
        0xFE,
        "……冈兹就交给我吧。\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "等他醒来以后，\x01",
            "我会再向他询问事情的经过。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "……我衷心期望那种药\x01",
            "并不是什么不好的东西，\x01",
            "只是普通的医用药物而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_432F")

    TalkEnd(0xD)
    Return()

    # Function_16_4026 end

    def Function_17_4333(): pass

    label("Function_17_4333")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(163000, 1000, 7200, 0)
    MoveCamera(307, 27, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 164300, 0, 3900, 270)
    SetChrPos(0x102, 164300, 0, 5000, 270)
    SetChrPos(0x103, 165200, 0, 3600, 270)
    SetChrPos(0x104, 165200, 0, 5300, 270)
    SetChrPos(0x13D, 164300, 0, 7600, 225)
    SetChrPos(0xC, 162000, 650, 5900, 90)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xD, 162000, 0, 4500, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetMapObjFrame(0xFF, "futon", 0x0, 0x1)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis087.itp")
    OP_68(163000, 1000, 5200, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0257
    ChrTalk(
        0xD,
        (
            "#5P哦哦，女神啊……\x01",
            "到底为什么会发生这种事呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xD,
        (
            "#5P这个男人虽然邋遢，但开朗爽快，\x01",
            "是个人缘非常好的男人啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x102,
        "#0108F#12P镇长先生……\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x104,
        (
            "#12P#0306F不过，他那个时候\x01",
            "还真是乱闹了一阵，场面非常惊人呢……\x02\x03",

            "#0301F真没想到，\x01",
            "竟然要由我和罗伊德两人\x01",
            "合力才能把他按住。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x101,
        (
            "#6P#0006F是啊……\x01",
            "老实说，他的力量确实很惊人。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x103,
        "#12P#0201F#N……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x13D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x13D)
    TurnDirection(0x13D, 0x101, 500)
    Sleep(300)

    #C0263
    ChrTalk(
        0x13D,
        (
            "#2103F#11P那个……\x01",
            "当然，这也只是我的第一感觉而已。\x02\x03",

            "#2101F这个人，会不会\x01",
            "沾染上了什么危险的药物呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_46DC():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_46DC)

    def lambda_46E9():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_46E9)
    Sleep(50)

    def lambda_46F9():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_46F9)

    def lambda_4706():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4706)
    Sleep(50)
    TurnDirection(0x104, 0x13D, 500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0264
    ChrTalk(
        0xD,
        "#5P#4S什么……！？\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x102,
        "#6P#0105F您、您的意思是说……\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x104,
        "#6P#0305F真的吗……！？\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x13D,
        (
            "#2100F#11P哎呀，罗伊德和小缇欧\x01",
            "和我的意见相同吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x103,
        "#0208F#6P#N………那个……………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0269
    ChrTalk(
        0x101,
        (
            "#0006F#6P……我不想说太多\x01",
            "没有根据的话……\x02\x03",

            "#0001F不过，这种可能性确实存在。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xD,
        (
            "#5P不、不可能……\x01",
            "他怎么可能会沾染违禁药物呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xD,
        (
            "#5P他只是个普通的矿工啊！\x01",
            "不可能沾染到那种东西──\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13D, 0xD, 500)

    #C0272
    ChrTalk(
        0x13D,
        (
            "#2100F#11P但是，他来这边\x01",
            "已经快半个月了吧？\x02\x03",

            "肯定赚了相当多的米拉，\x01",
            "在别人的引诱下而沾染违禁药物……\x01",
            "这种可能性也并不是完全没有吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xD,
        "#5P不、不要越说越过分了！\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xD,
        (
            "#5P你好像是克洛斯贝尔时代周刊\x01",
            "的记者吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xD,
        (
            "#5P要是你光凭主观臆断将此事写成报道，\x01",
            "我一定会进行强烈抗议的！\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x13D,
        (
            "#2106F#11P啊……我并没打算\x01",
            "要把这件事写成报道呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Fade(500)
    OP_68(163000, 1000, 4700, 0)
    MoveCamera(330, 19, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0xC, 162000, 600, 5900, 90)
    SetChrSubChip(0xC, 0x1)
    OP_0D()
    TurnDirection(0x101, 0xD, 500)

    #C0277
    ChrTalk(
        0x101,
        (
            "#12P#0003F──比克森镇长。\x02\x03",

            "#0001F以防万一，可以让我们检查一下\x01",
            "冈兹先生随身携带的个人物品吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_4AE1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_4AE1)
    Sleep(100)

    def lambda_4AF1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4AF1)

    def lambda_4AFE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4AFE)

    def lambda_4B0B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4B0B)
    Sleep(50)
    TurnDirection(0x13D, 0x101, 500)

    #C0278
    ChrTalk(
        0xD,
        "#5P罗伊德，连你也那么想吗！？\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        (
            "#12P#0006F虽然我们不打算就此武断地下定结论，\x01",
            "但是目前有很多事实都十分符合刚才的推断。\x02\x03",

            "#0008F那种大闹的方式、惊人的力量，\x01",
            "还有完全变化的性格……\x02\x03",

            "#0013F与过去发生的几起违禁药物事件\x01",
            "所造成的结果十分相似。\x02\x03",

            "另外，他在『巴鲁卡』那超乎寻常的\x01",
            "惊人技巧也很可疑……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x104,
        (
            "#0303F#11P……有可能是因为药物的缘故，\x01",
            "使感知能力变得异常敏锐。\x02\x03",

            "#0301F然后借此来揣测对手的心理活动，\x01",
            "从而赢得比赛……\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x103,
        (
            "#12P#0206F…………是啊。\x02\x03",

            "#0200F如果我参与赌博的话，\x01",
            "大概也会比其他人更加有利吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)
    Sleep(300)

    #C0282
    ChrTalk(
        0x102,
        "#0105F#5P缇欧……\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x104,
        (
            "#0306F#11P……抱歉，\x01",
            "我不是这个意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x103,
        (
            "#12P#0204F不，我并没有在意。\x02\x03",

            "#0201F──镇长先生，\x01",
            "我知道您很在意\x01",
            "冈兹先生的名誉。\x02\x03",

            "但是，假如这真的与\x01",
            "某种违禁药物有关……\x02\x03",

            "如果我们就这么放着不管的话，\x01",
            "不知还会发生什么危险呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_4E3F():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4E3F)
    Sleep(50)

    def lambda_4E4F():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4E4F)

    #C0285
    ChrTalk(
        0xD,
        "#5P这、这个……\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x13D,
        (
            "#11P#2106F中毒症状、后遗症……\x01",
            "总之，能想到的情况实在不少呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#12P#0006F是啊，在违禁药物造成的危害中，\x01",
            "那些才是最可怕的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)

    #C0288
    ChrTalk(
        0xD,
        (
            "#5P我明白了……\x01",
            "看来是我考虑不周啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xD,
        "#5P罗伊德，拜托你了。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        "#12P#0003F……好。\x02",
    )

    CloseMessageWindow()

    def lambda_4F6A():

        label("loc_4F6A")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4F6A")

    QueueWorkItem2(0x13D, 2, lambda_4F6A)

    def lambda_4F7C():

        label("loc_4F7C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4F7C")

    QueueWorkItem2(0x102, 2, lambda_4F7C)

    def lambda_4F8E():

        label("loc_4F8E")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4F8E")

    QueueWorkItem2(0x103, 2, lambda_4F8E)

    def lambda_4FA0():

        label("loc_4FA0")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4FA0")

    QueueWorkItem2(0x104, 2, lambda_4FA0)

    def lambda_4FB2():

        label("loc_4FB2")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4FB2")

    QueueWorkItem2(0xD, 2, lambda_4FB2)
    OP_68(162700, 1000, 4930, 1200)

    def lambda_4FD5():
        OP_96(0xFE, 0x27B8C, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FD5)
    Sleep(300)

    def lambda_4FF2():
        OP_96(0xFE, 0x278D0, 0x0, 0xC80, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4FF2)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x14A, 0x1F4)
    WaitChrThread(0xD, 1)
    EndChrThread(0x13D, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0xD, 0x2)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0291
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德为了不把冈兹惊醒，\x01",
            "小心地把手探入到了他的怀中。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(2000)
    OP_64(0x101)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0292
    ChrTalk(
        0x101,
        "#6P#0013F（………这是…………）\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0293
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('纯白之石', 1)

    #A0294
    AnonymousTalk(
        0x102,
        "#0105F这、这是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0295
    AnonymousTalk(
        0xD,
        "啊啊，女神啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0296
    AnonymousTalk(
        0x13D,
        "#2101F竟然还真有……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0297
    AnonymousTalk(
        0x104,
        (
            "#0301F颜色还真漂亮啊……\x01",
            "这到底是什么药？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0298
    AnonymousTalk(
        0x103,
        "#0201F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0299
    ChrTalk(
        0x101,
        (
            "#0006F#5P──目前还不能确定\x01",
            "这些药物就是造成问题的原因。\x02\x03",

            "毕竟也有可能只是用来\x01",
            "治疗他本身患有的某种疾病。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 500)

    #C0300
    ChrTalk(
        0x101,
        "#11P#0001F镇长，冈兹先生有什么顽症吗？\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xD,
        (
            "#6P……据我所知，应该是没有的。\x01",
            "虽然无法断言……\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x101,
        (
            "#11P#0003F我知道了。\x02\x03",

            "#0001F……这个药，\x01",
            "可以先交给我们保管吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xD,
        "#6P嗯……那就拜托你们了。\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xD,
        (
            "#6P但是、但是……！\x01",
            "请尽量别把事情闹大啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x101,
        (
            "#11P#0004F好的，我们处理时，\x01",
            "会尽量考虑到冈兹先生的名誉。\x02\x03",

            "#0001F至于冈兹先生，\x01",
            "可以暂时交给您来照顾吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xD,
        "#6P可以……请交给我吧。\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xD,
        (
            "#6P等他醒来以后，\x01",
            "我会再问问他的。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x101,
        "#11P#0000F好的，那就麻烦您了。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(24000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(500)
    OP_68(68000, 1000, 9700, 0)
    MoveCamera(310, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 73600, 0, 7400, 180)
    SetChrPos(0x102, 72400, 0, 7400, 180)
    SetChrPos(0x103, 73700, 0, 8600, 180)
    SetChrPos(0x104, 72300, 0, 8600, 180)
    SetChrPos(0x13D, 73000, 0, 5500, 0)
    OP_68(72710, 1000, 7410, 4000)
    SetCameraDistance(22500, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x11)

    #C0309
    ChrTalk(
        0x13D,
        (
            "#6P#2106F──呼，真没想到，在克洛斯贝尔\x01",
            "竟然还会出现疑似违禁药物的案例。\x02\x03",

            "这可真是罕见啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0310
    ChrTalk(
        0x104,
        (
            "#11P#0305F罕见吗？\x02\x03",

            "#0301F我还以为那些黑手党\x01",
            "会经常从事违禁药物交易呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x13D,
        (
            "#6P#2104F但事实却很出乎意料，\x01",
            "在克洛斯贝尔，很少有违禁药物\x01",
            "方面的犯罪。\x02\x03",

            "#2100F因为与其它犯罪不同，\x01",
            "这种犯罪很容易扩展到其它国家，\x01",
            "是一种影响力十分广泛的犯罪形式。\x02\x03",

            "帝国和共和国都在施加压力，\x01",
            "搜查一科也一直都在极其严厉地\x01",
            "打击着违禁药物方面的犯罪。\x02\x03",

            "#2104F而鲁巴彻的那些家伙也看出了\x01",
            "一些端倪，不会触及这个敏感的区域。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x102,
        "#11P#0105F原来如此啊……\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        (
            "#11P#0003F这些事情，\x01",
            "我在警察学校中也曾学过。\x02\x03",

            "#0008F话说回来，这种药片……\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    #A0314
    AnonymousTalk(
        0x102,
        (
            "#0101F蓝色的药片……\x01",
            "外表看起来很美。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0315
    AnonymousTalk(
        0x104,
        (
            "#0301F但是，该怎么说呢……\x01",
            "总有种特别可疑的感觉啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0316
    AnonymousTalk(
        0x103,
        "#0208F#40W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x103, 500)

    #C0317
    ChrTalk(
        0x101,
        "#6P#0005F缇欧，你有什么想法吗？\x02",
    )

    CloseMessageWindow()

    def lambda_58E7():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_58E7)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)

    #C0318
    ChrTalk(
        0x103,
        (
            "#0206F#11P没有……很抱歉，\x01",
            "好像只是我的错觉而已。\x02\x03",

            "#0201F那么，这个药片……\x01",
            "到底要怎么处理呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        (
            "#6P#0006F是啊……\x02\x03",

            "光凭我们，似乎也很难在\x01",
            "这种重大事件中做决定。\x02\x03",

            "#0001F还是先回去一趟，和科长谈谈吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_59CE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_59CE)
    Sleep(100)
    TurnDirection(0x104, 0x101, 500)

    #C0320
    ChrTalk(
        0x102,
        (
            "#5P#0103F嗯，我也这么认为。\x02\x03",

            "#0101F顺便也报告一下\x01",
            "『黑月』受袭的事件吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#5P#0306F黑手党之间的对抗，\x01",
            "再加上很可能与违禁药物有关的事件……\x02\x03",

            "#0301F真是的，总有种强烈的预感，\x01",
            "也许我们很快就会忙成一团了。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x13D,
        "#6P#2102F呵呵……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5B1A():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5B1A)
    Sleep(50)

    def lambda_5B2A():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5B2A)
    Sleep(50)

    def lambda_5B3A():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5B3A)
    Sleep(50)
    TurnDirection(0x104, 0x13D, 500)

    #C0323
    ChrTalk(
        0x13D,
        (
            "#6P#2109F哎呀～虽然从和你们初识算起\x01",
            "只过去了四个月……\x02\x03",

            "但还真是成长了不少呢～\x01",
            "姐姐我不禁感慨万分啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x101,
        "#11P#0005F格蕾丝小姐……？\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x102,
        (
            "#11P#0105F突、突然之间，\x01",
            "在说些什么啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x103,
        "#0211F#11P夸我们也没有什么好处哦……\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x13D,
        (
            "#6P#2104F不不，我说的是心里话，\x01",
            "我对你们抱有很高的期待呢。\x02\x03",

            "#2100F大概和对罗伊德的哥哥……\x01",
            "盖伊·班宁斯的期待度差不多吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0328
    ChrTalk(
        0x101,
        (
            "#11P#0011F说、说起来……\x01",
            "您以前好像也提到过这件事。\x02\x03",

            "格蕾丝小姐\x01",
            "和我大哥认识吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x13D,
        (
            "#6P#2104F在我还是个新记者的时候，\x01",
            "曾受过你哥哥的很多关照呢～\x02\x03",

            "#2106F虽然盖伊先生遇害的事件\x01",
            "最后还是陷入了迷局……\x02\x03",

            "#2102F不过警察局能成立一个\x01",
            "继承他遗志的部门，我感到很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x101,
        "#11P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x102,
        (
            "#11P#0105F继承了罗伊德哥哥\x01",
            "遗志的部门……？\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x13D,
        (
            "#6P#2104F哎呀呀，要是再说下去的话，\x01",
            "科长先生就该对我发怒了吧。\x02\x03",

            "#2100F好啦，我还要去采访呢，\x01",
            "今天就聊到这里吧，先走一步啦。\x02\x03",

            "#2105F啊，对了，我不会擅自写药物方面\x01",
            "的报道，你们放心吧。\x02\x03",

            "#2109F那我走啦，Ｂｙｅｂｙｅ！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x13D, 0x5A, 0x1F4)
    OP_68(76000, 0, 6900, 2000)

    def lambda_5F65():
        OP_98(0xFE, 0x1F40, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13D, 1, lambda_5F65)

    def lambda_5F7F():

        label("loc_5F7F")

        TurnDirection(0xFE, 0x13D, 500)
        Yield()
        Jump("loc_5F7F")

    QueueWorkItem2(0x101, 2, lambda_5F7F)

    def lambda_5F91():

        label("loc_5F91")

        TurnDirection(0xFE, 0x13D, 500)
        Yield()
        Jump("loc_5F91")

    QueueWorkItem2(0x102, 2, lambda_5F91)

    def lambda_5FA3():

        label("loc_5FA3")

        TurnDirection(0xFE, 0x13D, 500)
        Yield()
        Jump("loc_5FA3")

    QueueWorkItem2(0x103, 2, lambda_5FA3)

    def lambda_5FB5():

        label("loc_5FB5")

        TurnDirection(0xFE, 0x13D, 500)
        Yield()
        Jump("loc_5FB5")

    QueueWorkItem2(0x104, 2, lambda_5FB5)
    Sleep(1500)

    def lambda_5FCA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13D, 2, lambda_5FCA)
    WaitChrThread(0x13D, 1)
    WaitChrThread(0x13D, 2)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    OP_6F(0x1)
    Sleep(500)
    OP_68(73000, 1000, 8000, 2500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_6F(0x1)

    #C0333
    ChrTalk(
        0x101,
        "#5P#0008F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x104,
        (
            "#5P#0306F真是的，尽说些吊人胃口的话，\x01",
            "然后又擅自走掉。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x102,
        (
            "#5P#0106F呼……要做的事情\x01",
            "本来就已经堆积如山了。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x103,
        "#0206F#5P……是啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0337
    ChrTalk(
        0x103,
        (
            "#0200F#11P罗伊德前辈……\x01",
            "你很在意盖伊先生的事情吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(150)

    #C0338
    ChrTalk(
        0x101,
        "#6P#0005F嗯，那个……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0339
    ChrTalk(
        0x101,
        (
            "#6P#0006F──虽然的确有些在意，\x01",
            "但现在不是想这些事的时候。\x02\x03",

            "#0008F黑月受袭，鲁巴彻的状况，\x01",
            "还有这个蓝色药片……\x02\x03",

            "#0000F先把这些情况向科长报告，\x01",
            "然后再考虑下一步怎么走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x103,
        "#0202F#11P……好的。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x102,
        "#5P#0100F嗯，明白了。\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x104,
        (
            "#5P#0300F好，那就赶快\x01",
            "回支援科吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    OP_CA(0x1, 0xFF, 0x0)
    OP_68(73000, 1500, 9000, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 74120, 0, 6470, 90)
    SetChrPos(0x1, 74120, 0, 6470, 90)
    SetChrPos(0x2, 74120, 0, 6470, 90)
    SetChrPos(0x3, 74120, 0, 6470, 90)
    RemoveParty(0x3C, 0x0)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 162000, 650, 5900, 90)
    SetChrPos(0xD, 162000, 0, 4500, 0)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, -2009, 0, 9290, 270)
    BeginChrThread(0xA, 0, 0, 0)
    SetScenarioFlags(0xC2, 7)
    OP_C7(0x1, 0x1000)
    OP_29(0x4A, 0x1, 0x9)
    OP_66(0x3, 0x1)
    BeginChrThread(0xD, 0, 0, 0)
    EventEnd(0x5)
    Return()

    # Function_17_4333 end

    def Function_18_63A1(): pass

    label("Function_18_63A1")


    #C0343
    ChrTalk(
        0x11C,
        "#1200F……嗷呜嗷呜～！\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        (
            "#0003F……似乎不在\x01",
            "这边呢。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_18_63A1 end

    def Function_19_63DF(): pass

    label("Function_19_63DF")

    EventBegin(0x1)
    Call(0, 18)
    Sleep(50)
    SetChrPos(0x0, 56000, 0, 11250, 180)
    EventEnd(0x4)
    Return()

    # Function_19_63DF end

    def Function_20_63FB(): pass

    label("Function_20_63FB")

    EventBegin(0x1)
    Call(0, 18)
    Sleep(50)
    SetChrPos(0x0, 68000, 0, 11250, 180)
    EventEnd(0x4)
    Return()

    # Function_20_63FB end

    def Function_21_6417(): pass

    label("Function_21_6417")

    EventBegin(0x1)
    Call(0, 18)
    Sleep(50)
    SetChrPos(0x0, 1000, 0, 66250, 180)
    EventEnd(0x4)
    Return()

    # Function_21_6417 end

    def Function_22_6433(): pass

    label("Function_22_6433")

    EventBegin(0x1)
    Call(0, 18)
    Sleep(50)
    SetChrPos(0x0, 7250, 0, 60000, 270)
    EventEnd(0x4)
    Return()

    # Function_22_6433 end

    def Function_23_644F(): pass

    label("Function_23_644F")

    EventBegin(0x1)
    Call(0, 18)
    Sleep(50)
    SetChrPos(0x0, 1000, 0, 53750, 0)
    EventEnd(0x4)
    Return()

    # Function_23_644F end

    def Function_24_646B(): pass

    label("Function_24_646B")

    EventBegin(0x0)
    OP_4B(0xF, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(115550, 1400, 59480, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, 115750, 0, 59450, 0)
    SetChrPos(0x103, 115750, 0, 58030, 0)
    SetChrPos(0x102, 114340, 0, 59450, 0)
    SetChrPos(0x104, 114340, 0, 58030, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0345
    NpcTalk(
        0xF,
        "青年",
        (
            "#11P呼～……\x01",
            "已经不想再走下去了～\x02",
        )
    )

    CloseMessageWindow()

    #N0346
    NpcTalk(
        0xF,
        "青年",
        "#11P干脆放弃，直接回去算了。\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        (
            "#12P#0000F那个，打扰一下，\x01",
            "您是向我们提出委托的\x01",
            "特伦特先生吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_93(0xF, 0xB4, 0x1F4)
    Sleep(300)

    #C0348
    ChrTalk(
        0xF,
        "#11P噢！你们是警察吗？\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xF,
        (
            "#11P哦哦～没想到\x01",
            "你们真的会来啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x101,
        "#12P#0012F哈哈哈，您好……\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x102,
        (
            "#5P#0100F听说您\x01",
            "丢失了东西，\x01",
            "能将详细情况告诉我们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xF,
        (
            "#11P说起那个，\x01",
            "还真是让人欲哭无泪啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(10)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(20)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0353
    ChrTalk(
        0xF,
        (
            "#11P我最喜欢购物了，\x01",
            "所以在克洛斯贝尔\x01",
            "到处乱逛了很长时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xF,
        (
            "#11P然后……突然发现我的背包\x01",
            "破了一个洞。\x01",
            "但那时，里面的东西都已经掉了！\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xF,
        (
            "#11P我拼命找了很久，\x01",
            "但是，还是有一些东西\x01",
            "怎么也找不到～\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x104,
        (
            "#0306F原来如此……\x02\x03",

            "#0301F不过，事情都已经过了一天，\x01",
            "那些东西恐怕不会\x01",
            "还原封不动地摆在地上吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x103,
        (
            "#12P#0200F有可能是被附近的人\x01",
            "捡起来，然后暂时保管了。\x02\x03",

            "请问您购物时\x01",
            "都去过哪些地方呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xF,
        "#11P嗯，最先去的当然是百货店了！\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xF,
        (
            "#11P那里卖的都是最新的名牌货～\x01",
            "我在那里逛了好久呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xF,
        (
            "#11P之后就在东街的市场里\x01",
            "转了转……\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xF,
        (
            "#11P走到港湾区的公园附近时，\x01",
            "我才注意到背包破了个洞～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1800)

    #C0362
    ChrTalk(
        0xF,
        (
            "#11P……唉，然后，怎么找\x01",
            "也找不到了～\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xF,
        (
            "#11P钱包和土特产……\x01",
            "还有一样东西，是什么来着……\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xF,
        (
            "#11P我觉得肯定是\x01",
            "少了三样，但是……\x02",
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

    #C0365
    ChrTalk(
        0x101,
        (
            "#12P#0003F……也就是说，\x01",
            "您想不起来最后一样是什么了吧。\x02\x03",

            "#0001F我知道了，总之，\x01",
            "我们先去那些地方找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x102,
        (
            "#5P#0103F中央广场的百货店、\x01",
            "东街、港湾区……\x02\x03",

            "#0100F这些地方都是商业繁荣的地区，\x01",
            "以店员为中心来调查，\x01",
            "应该会比较有效率吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xF,
        "#11P那就拜托你们啦～！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0368
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找遗失物品的委托】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(115090, 1500, 58830, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 115090, 0, 58830, 0)
    SetChrPos(0x1, 115090, 0, 58830, 0)
    SetChrPos(0x2, 115090, 0, 58830, 0)
    SetChrPos(0x3, 115090, 0, 58830, 0)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x10)
    OP_29(0x2, 0x1, 0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_24_646B end

    def Function_25_6C2D(): pass

    label("Function_25_6C2D")

    EventBegin(0x0)
    OP_4B(0xF, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(115550, 1400, 59480, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, 115750, 0, 59450, 0)
    SetChrPos(0x103, 115750, 0, 58030, 0)
    SetChrPos(0x102, 114340, 0, 59450, 0)
    SetChrPos(0x104, 114340, 0, 58030, 0)
    OP_93(0xF, 0xB4, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0369
    ChrTalk(
        0x101,
        (
            "#12P#0000F特伦特先生，\x01",
            "您的确是丢了三样东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x102,
        (
            "#5P#0100F已经全部都找到了。\x02\x03",

            "……请收下吧，\x01",
            "要注意别再丢失了哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x102, 114480, 0, 60290, 1000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0371
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x337),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    OP_5A()

    #A0372
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x338),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    OP_5A()

    #A0373
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x339),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    OP_5A()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('罗赞贝尔克人偶·Ｍ', 1)
    SubItemNumber('罗赞贝尔克人偶·Ｓ', 1)
    SubItemNumber('波波碰！β版', 1)
    OP_96(0x102, 0x1BEA4, 0x0, 0xE83A, 0x3E8, 0x0)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0374
    ChrTalk(
        0xF,
        "#11P哦哦，的确是我的东西！\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xF,
        (
            "#11P哎呀，真是太好了～\x01",
            "我本来还在想，干脆就这样放弃，\x01",
            "直接回国算了～\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x103,
        (
            "#12P#0200F但没有钱包和车票的话，\x01",
            "想回也回不去吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0377
    ChrTalk(
        0xF,
        (
            "#11P呜……说、说得也是啊。\x01",
            "啊哈哈，我都没注意到呢～！\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xF,
        (
            "#11P不过，真是太感谢你们了～\x01",
            "虽然在一筹莫展的时候，\x01",
            "选择了试着联络警察，但其实没报什么希望……\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xF,
        (
            "#11P而且我听说克洛斯贝尔的警察\x01",
            "能力很差，态度也很恶劣。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xF,
        (
            "#11P没想到还真的会\x01",
            "帮我找回来啊～\x02",
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
    Sleep(1200)

    #C0381
    ChrTalk(
        0x101,
        "#12P#0012F是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x104,
        (
            "#0306F我好像突然明白特别任务支援科\x01",
            "这个部门存在的意义了。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x102,
        (
            "#5P#0100F这不是挺好的吗，\x01",
            "我们毕竟帮助了一个人。\x02\x03",

            "这样就算是完成任务了吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0384
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找遗失物品的委托】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(115090, 1500, 58830, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 115090, 0, 58830, 0)
    SetChrPos(0x1, 115090, 0, 58830, 0)
    SetChrPos(0x2, 115090, 0, 58830, 0)
    SetChrPos(0x3, 115090, 0, 58830, 0)
    OP_4C(0xF, 0xFF)
    OP_29(0x2, 0x2, 0x1F)
    OP_29(0x2, 0x1, 0x5)
    OP_29(0x2, 0x4, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_25_6C2D end

    SaveToFile()

Try(main)
