from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "受付カイル",             # 1
        "ドリス",                 # 2
        "アーロン",               # 3
        "レティシア支配人",       # 4
        "ガンツ",                 # 5
        "ビクセン町長",           # 6
        "ロバーツ主任",           # 7
        "トロント",               # 8
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
        "Function_8_1A04",         # 08, 8
        "Function_9_1A08",         # 09, 9
        "Function_10_2738",        # 0A, 10
        "Function_11_31B5",        # 0B, 11
        "Function_12_3C6C",        # 0C, 12
        "Function_13_45AA",        # 0D, 13
        "Function_14_4A29",        # 0E, 14
        "Function_15_4A59",        # 0F, 15
        "Function_16_4B94",        # 10, 16
        "Function_17_4F07",        # 11, 17
        "Function_18_71D1",        # 12, 18
        "Function_19_721B",        # 13, 19
        "Function_20_7237",        # 14, 20
        "Function_21_7253",        # 15, 21
        "Function_22_726F",        # 16, 22
        "Function_23_728B",        # 17, 23
        "Function_24_72A7",        # 18, 24
        "Function_25_7B37",        # 19, 25
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E8")

    #C0001
    ChrTalk(
        0xB,
        "《ホテル・ミレニアム》へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xB,
        (
            "うふふ、当ホテルでは\x01",
            "様々なサービスをご用意しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xB,
        (
            "歓楽の都クロスベルでの\x01",
            "極上の一日を約束致しますわ。\x02",
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
            "ホテルや宿酒場に宿泊すると\x01",
            "ＣＰを回復する事ができます。\x02",
        )
    )

    CloseMessageWindow()

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "通常の宿酒場ではＣＰ１００、\x01",
            "高級ホテルではＣＰ２００が回復します。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E5")
    SetScenarioFlags(0x0, 0)

    label("loc_8E5")

    SetScenarioFlags(0x4B, 4)

    label("loc_8E8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A00")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",        # 0
            "休憩をする\x01",      # 1
            "やめる\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_94E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_94E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96E")
    OP_AF(0x3C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19FB")

    label("loc_96E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_982")
    Jump("loc_19FB")

    label("loc_982")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19FB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A20")

    #C0006
    ChrTalk(
        0xB,
        (
            "噂で聞きましたが、ガンツ様だけでなく\x01",
            "街の人間も何人か失踪しているとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xB,
        "何かが起こっているのでしょうか……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_19FB")

    label("loc_A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AAF")

    #C0008
    ChrTalk(
        0xB,
        (
            "こういった場合の対応は\x01",
            "ホテル側としても難しいところです。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xB,
        (
            "ガンツ様がお怪我など\x01",
            "していなければよいのですけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B6A")

    label("loc_AAF")


    #C0010
    ChrTalk(
        0xB,
        (
            "今朝早く、ガンツ様は\x01",
            "一人で出て行かれてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xB,
        (
            "泥酔してらしたと伺っていたので\x01",
            "アーロンさんが\x01",
            "声をお掛けしたのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xB,
        (
            "お怪我などしていなければ\x01",
            "よいのですけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_B6A")

    Jump("loc_19FB")

    label("loc_B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_E33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_D71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BFB")

    #C0013
    ChrTalk(
        0xB,
        (
            "ふふ、ガンツさんは\x01",
            "よほど酔ってしまわれたのですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xB,
        (
            "あとでお部屋の方に\x01",
            "水を持って行かせましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D6C")

    label("loc_BFB")


    #C0015
    ChrTalk(
        0xB,
        (
            "あの……ガンツ様は\x01",
            "一体どうなされたのでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        (
            "よろしければ、\x01",
            "ウルスラ病院に連絡して\x01",
            "救急車に来て頂きますけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#0003F（ガンツさんは心配だけど、\x01",
            "  大事にする訳にはいかない……）\x02\x03",

            "#0012Fえ、えっと……\x01",
            "ちょっと酔っぱらって\x01",
            "しまったみたいです。\x02\x03",

            "#0000F付き添いの方も一緒ですし\x01",
            "多分大丈夫だと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xB,
        (
            "あら、そうでしたか。\x01",
            "安心いたしましたわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_D6C")

    Jump("loc_E2E")

    label("loc_D71")


    #C0019
    ChrTalk(
        0xB,
        (
            "宿泊なさっていたガンツ様……\x01",
            "今日も気分よく出かけて行かれましたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xB,
        (
            "マインツの方から迎えの方が来ると\x01",
            "伺っていたのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xB,
        (
            "お部屋でお待ちにならなくて\x01",
            "よかったのでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E2E")

    Jump("loc_19FB")

    label("loc_E33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_F33")

    #C0022
    ChrTalk(
        0xB,
        (
            "２ヶ月前に整備が整った\x01",
            "導力ネットの予約システムが\x01",
            "ようやく軌道に乗りだしましたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xB,
        "あとはネットワークの拡大を待つのみ……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xB,
        (
            "こちらは時間がかかるでしょうが、\x01",
            "先んじてシステムを導入した当ホテルなら\x01",
            "適宜対応していけることでしょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FB")

    label("loc_F33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_FAD")

    #C0025
    ChrTalk(
        0xB,
        "いらっしゃいませ。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xB,
        (
            "今年で創業６０周年の当ホテル、\x01",
            "誠心誠意をもって\x01",
            "お客様に尽くさせて頂きますわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FB")

    label("loc_FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1276")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10E9")

    #C0027
    ChrTalk(
        0xB,
        "お、お客様……！？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xB,
        (
            "ペットのお持込みは\x01",
            "ご遠慮いただきたいのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        "#0006Fすみません、ウチの警察犬でして。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x103,
        (
            "#0203Fちょっとした捜査中です。\x01",
            "どうかお気になさらず。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xB,
        "そ、そうでしたか。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xB,
        (
            "失礼いたしました。\x01",
            "どうぞ、ご自由に見ていらしてください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x95, 5)
    TalkEnd(0xB)
    Return()

    label("loc_10E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_117B")

    #C0033
    ChrTalk(
        0xB,
        (
            "サービスの本質は困っている人に\x01",
            "手を差し伸べること……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xB,
        (
            "当ホテルもリベール王国ホテルの\x01",
            "サービス精神を見習いたいものですわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1271")

    label("loc_117B")


    #C0035
    ChrTalk(
        0xB,
        (
            "以前、リベール王国の方で\x01",
            "ボースという街が竜に襲われる\x01",
            "大事件があったそうですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xB,
        (
            "その時は、街のホテルが先陣を切って\x01",
            "被災者の宿の確保にあたったとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xB,
        (
            "まさに究極のサービス精神……\x01",
            "当ホテル・ミレニアムも\x01",
            "かくありたいものですわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1271")

    Jump("loc_19FB")

    label("loc_1276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1304")

    #C0038
    ChrTalk(
        0xB,
        (
            "カジノを目当てに観光にいらっしゃる\x01",
            "お客様も多数いらっしゃいますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xB,
        (
            "まさに歓楽の都クロスベル\x01",
            "ならではの客層ですわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FB")

    label("loc_1304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1384")

    #C0040
    ChrTalk(
        0xB,
        (
            "本日もご予約のお客様で\x01",
            "当ホテルはほぼ満室でございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xB,
        (
            "お部屋をご所望なら\x01",
            "お早めにお願いいたしますわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FB")

    label("loc_1384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1440")

    #C0042
    ChrTalk(
        0xB,
        (
            "導力ネットはクロスベル市内と\x01",
            "ミシュラム、後はウルスラ病院にしか\x01",
            "通っていないのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xB,
        (
            "当ホテルに引かれた導力ネットも、\x01",
            "当面はビジネスでの\x01",
            "利用が多くなるでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FB")

    label("loc_1440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_14D4")

    #C0044
    ChrTalk(
        0xB,
        (
            "本日はエプスタイン財団の方に\x01",
            "導力ネットを引きにきてもらいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xB,
        (
            "これでホテルのサービスを\x01",
            "より充実させる事ができますわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FB")

    label("loc_14D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1604")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_156D")

    #C0046
    ChrTalk(
        0xB,
        (
            "近日中に導力ネットワークを通じた\x01",
            "ご予約サービスを開始いたしますの。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xB,
        (
            "サービスの開始まで\x01",
            "もうしばらくお待ちくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15FF")

    label("loc_156D")


    #C0048
    ChrTalk(
        0xB,
        (
            "当ホテルでは、近日中に\x01",
            "導力ネットワークを通じての\x01",
            "ご予約が可能になる予定ですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xB,
        (
            "サービスの開始まで\x01",
            "もうしばらくお待ちくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_15FF")

    Jump("loc_19FB")

    label("loc_1604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_16F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_165F")

    #C0050
    ChrTalk(
        0xB,
        (
            "例のサービスが始まれば\x01",
            "水を開けることも\x01",
            "出来るのですけれど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16F1")

    label("loc_165F")


    #C0051
    ChrTalk(
        0xB,
        (
            "お陰様で当ホテルは\x01",
            "この歓楽街でもトップレベルの\x01",
            "売り上げを誇っておりますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xB,
        (
            "しかしライバルも多いのです。\x01",
            "決して気が抜けませんわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_16F1")

    Jump("loc_19FB")

    label("loc_16F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1866")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1790")

    #C0053
    ChrTalk(
        0xB,
        (
            "クロスベルは再来月に\x01",
            "創立記念祭と劇団アルカンシェルの\x01",
            "新作公演を控えております。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xB,
        (
            "きっとこの時期は\x01",
            "大変混雑いたしますわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1861")

    label("loc_1790")


    #C0055
    ChrTalk(
        0xB,
        (
            "クロスベルは再来月に\x01",
            "大きなイベントを控えてございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xB,
        (
            "自治州の創立記念祭……\x01",
            "そして劇団アルカンシェルの\x01",
            "新作公演もありますわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xB,
        (
            "大変混雑が予想されますので\x01",
            "ご予約は早めにお願い致しますわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1861")

    Jump("loc_19FB")

    label("loc_1866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_18D6")

    #C0058
    ChrTalk(
        0xB,
        (
            "当ホテルでは\x01",
            "コンシェルジェサービスも\x01",
            "行っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xB,
        "ご活用いただけると嬉しいですわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19FB")

    label("loc_18D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1958")

    #C0060
    ChrTalk(
        0xB,
        (
            "ガイド、エステ、サロン、\x01",
            "各種ブッキングサービス……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xB,
        (
            "歓楽の都クロスベルでの\x01",
            "極上の一日をお約束致しますわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FB")

    label("loc_1958")


    #C0062
    ChrTalk(
        0xB,
        "《ホテル・ミレニアム》へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xB,
        (
            "うふふ、当ホテルでは\x01",
            "様々なサービスをご用意しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xB,
        (
            "歓楽の都クロスベルでの\x01",
            "極上の一日を約束致しますわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_19FB")

    Jump("loc_8F2")

    label("loc_1A00")

    TalkEnd(0xB)
    Return()

    # Function_7_770 end

    def Function_8_1A04(): pass

    label("Function_8_1A04")

    Call(0, 9)
    Return()

    # Function_8_1A04 end

    def Function_9_1A08(): pass

    label("Function_9_1A08")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B50")

    #C0065
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "《ホテル・ミレニアム》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "お部屋のご予約なら\x01",
            "当フロントをご利用ください。\x02",
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
            "ホテルや宿酒場に宿泊すると\x01",
            "ＣＰを回復する事ができます。\x02",
        )
    )

    CloseMessageWindow()

    #A0068
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "通常の宿酒場ではＣＰ１００、\x01",
            "高級ホテルではＣＰ２００が回復します。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B4D")
    SetScenarioFlags(0x0, 1)

    label("loc_1B4D")

    SetScenarioFlags(0x4B, 4)

    label("loc_1B50")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2734")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",        # 0
            "休憩をする\x01",      # 1
            "やめる\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BB6")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1BB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BD6")
    OP_AF(0x3C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_272F")

    label("loc_1BD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BEA")
    Jump("loc_272F")

    label("loc_1BEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_272F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1C82")

    #C0069
    ChrTalk(
        0x8,
        "このような夕暮れ時までお疲れ様です。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "お部屋をご利用でしょうか？\x01",
            "チェックインは常時受け付けていますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_272F")

    label("loc_1C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1D30")

    #C0071
    ChrTalk(
        0x8,
        (
            "ビジネスマンの方などが\x01",
            "先程チェックアウトを\x01",
            "済まされたところです。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "チェックインは午後からですが……\x01",
            "休憩とあらばお部屋をご用意させて\x01",
            "いただきますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_272F")

    label("loc_1D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1DDF")

    #C0073
    ChrTalk(
        0x8,
        (
            "ガンツ様はデラックスルームに\x01",
            "長期滞在契約で宿泊されてます。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "なかなかわがままの多い方ですが……\x01",
            "プロとして誠意をもって\x01",
            "対応させていただいておりますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_272F")

    label("loc_1DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1E98")

    #C0075
    ChrTalk(
        0x8,
        (
            "当店はカジノ帰りのお客様も\x01",
            "多数いらっしゃいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "ホステスをはべらせて\x01",
            "帰ってくるお客様もいまして……\x01",
            "いやはや、うらやま……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        "……コホン、なんでもないです。\x02",
    )

    CloseMessageWindow()
    Jump("loc_272F")

    label("loc_1E98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1F56")

    #C0078
    ChrTalk(
        0x8,
        (
            "記念祭の期間中は\x01",
            "大変忙しかったですが、\x01",
            "やりがいはありました。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "やはりクロスベルの活気は\x01",
            "他の国とは一味違いますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "こちらのホテルに勤めて\x01",
            "良かったと思いますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_272F")

    label("loc_1F56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_200F")

    #C0081
    ChrTalk(
        0x8,
        (
            "当ホテルは、隅々まで手が行き届く\x01",
            "献身的なサービスを信条としております。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "レティシア支配人が\x01",
            "百貨店タイムズの支配人から学んだ、\x01",
            "客商売で最も大切なことなのですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_272F")

    label("loc_200F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2091")

    #C0083
    ChrTalk(
        0x8,
        (
            "当ホテルのお部屋には\x01",
            "内線用の通信器が備え付けてあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "御用がありましたら\x01",
            "フロントまでご連絡ください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_272F")

    label("loc_2091")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_20FA")

    #C0085
    ChrTalk(
        0x8,
        (
            "そろそろ団体客の皆さんが\x01",
            "戻ってくる頃ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x8,
        "受け入れの準備をしておかなければ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_272F")

    label("loc_20FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2193")

    #C0087
    ChrTalk(
        0x8,
        (
            "当ホテルは３台の\x01",
            "導力車を所有しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        (
            "駅や空港までの\x01",
            "送迎サービスも行っておりますので\x01",
            "ご利用の際は声をお掛けくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_272F")

    label("loc_2193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2247")

    #C0089
    ChrTalk(
        0x8,
        (
            "導力ネットワークは\x01",
            "クロスベルにとってまだまだ\x01",
            "未知数の代物だといえます。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "それをいち早く取り入れる事は\x01",
            "必ず将来の為になる……\x01",
            "支配人の策はそこにあるのです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_272F")

    label("loc_2247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_23A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_22DB")

    #C0091
    ChrTalk(
        0x8,
        (
            "導力ネットワークを\x01",
            "使用した予約サービスは\x01",
            "支配人の肝いりなのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "サービス開始の暁には\x01",
            "どうぞご利用くださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_239C")

    label("loc_22DB")


    #C0093
    ChrTalk(
        0x8,
        (
            "導力ネットワークを\x01",
            "使用した予約サービスは\x01",
            "支配人の肝いりなのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "市内のどこからでも利用できる\x01",
            "非常に便利なサービスですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "運用が始まった暁には\x01",
            "ぜひご利用くださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_239C")

    Jump("loc_272F")

    label("loc_23A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_24BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2428")

    #C0096
    ChrTalk(
        0x8,
        (
            "クロスベル市には観光業を\x01",
            "優遇する法律があるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        (
            "観光に携わる者として\x01",
            "大変光栄なことでございます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B9")

    label("loc_2428")


    #C0098
    ChrTalk(
        0x8,
        (
            "クロスベル市には\x01",
            "観光業振興のための\x01",
            "様々な優遇策があるのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "観光業は商業と並ぶ\x01",
            "市の主要産業……\x01",
            "大変光栄なことでございますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_24B9")

    Jump("loc_272F")

    label("loc_24BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2563")

    #C0100
    ChrTalk(
        0x8,
        (
            "お早うございます。\x01",
            "本日もご利用ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "丁度チェックアウトのお客様も\x01",
            "お出掛けになられた所です。\x01",
            "お部屋にも空きがございますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_272F")

    label("loc_2563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2657")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_25BB")

    #C0102
    ChrTalk(
        0x8,
        (
            "やりがいのある職場を与えて頂き\x01",
            "支配人には感謝しております。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2652")

    label("loc_25BB")


    #C0103
    ChrTalk(
        0x8,
        (
            "私は帝国のホテルにおりましたが、\x01",
            "現支配人に声を掛けて頂いたのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "ふふ、当ホテルはお客様の数も多く\x01",
            "やりがいのある職場と思っております。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2652")

    Jump("loc_272F")

    label("loc_2657")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_26BC")

    #C0105
    ChrTalk(
        0x8,
        "現在、空き部屋もございます。\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "お部屋のご予約なら\x01",
            "当フロントをご利用ください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_272F")

    label("loc_26BC")


    #C0107
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "《ホテル・ミレニアム》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "お部屋のご予約なら\x01",
            "当フロントをご利用ください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_272F")

    Jump("loc_1B5A")

    label("loc_2734")

    TalkEnd(0x8)
    Return()

    # Function_9_1A08 end

    def Function_10_2738(): pass

    label("Function_10_2738")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_27DA")

    #C0109
    ChrTalk(
        0xA,
        (
            "ビクセン様がガンツ様を\x01",
            "随分心配して待っているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        (
            "ふむ……あのままでは体を壊します。\x01",
            "ルームサービスの案内でも\x01",
            "してきましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B1")

    label("loc_27DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_287C")

    #C0111
    ChrTalk(
        0xA,
        (
            "ううむ……\x01",
            "ガンツ様はどうも\x01",
            "様子がおかしかったようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xA,
        (
            "心、ここに在らずといいますか……\x01",
            "どうも二日酔いのそれには\x01",
            "見えなかったのですが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B1")

    label("loc_287C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_297D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_28F9")

    #C0113
    ChrTalk(
        0xA,
        (
            "ようやく導力ネットワークでの\x01",
            "予約件数を纏められました。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "……はて。\x01",
            "なにかあったのですかな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2978")

    label("loc_28F9")


    #C0115
    ChrTalk(
        0xA,
        (
            "さて、今日の導力ネットの予約を\x01",
            "チェックしなくては。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        (
            "あの複雑な機械も、\x01",
            "一度操作を覚えると\x01",
            "なかなか楽しいものですな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2978")

    Jump("loc_31B1")

    label("loc_297D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2A56")

    #C0117
    ChrTalk(
        0xFE,
        (
            "近頃、デラックスルームを\x01",
            "借り切ってらっしゃる\x01",
            "お客様がいるのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "非常に気前のよい方で、\x01",
            "私どもも最高のおもてなしを\x01",
            "させて頂いております。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "ふふ、どうか皆様も\x01",
            "廊下はお静かに願いますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B1")

    label("loc_2A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2ADD")

    #C0120
    ChrTalk(
        0xA,
        (
            "近頃、歓楽街をうろつく\x01",
            "ルバーチェ商会の者たちを\x01",
            "見かけませんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "ふむ……記念祭の間に\x01",
            "何かあったのでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B1")

    label("loc_2ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2BAB")

    #C0122
    ChrTalk(
        0xA,
        (
            "劇団アルカンシェルは、\x01",
            "私が使用人頭になった年に\x01",
            "創設されたのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xA,
        "かれこれ２０年になるでしょうか。\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        (
            "ふふ、アルカンシェルの\x01",
            "今日びの人気にはどうしても\x01",
            "嬉しくなってしまいますな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B1")

    label("loc_2BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2C3C")

    #C0125
    ChrTalk(
        0xA,
        (
            "いやはや、難しい操作は\x01",
            "専門の方にほとんど\x01",
            "やっていただきましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xA,
        (
            "しかしまぁ、機械の保全くらいは\x01",
            "私でも出来そうですな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B1")

    label("loc_2C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2CB6")

    #C0127
    ChrTalk(
        0xA,
        (
            "さてと、そろそろ厨房の\x01",
            "確認してまいりますか。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xA,
        (
            "本日は団体客の方が多く、\x01",
            "給仕に手間取りそうですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B1")

    label("loc_2CB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2CD6")

    #C0129
    ChrTalk(
        0xA,
        "ふむふむ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_31B1")

    label("loc_2CD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2DCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2D41")

    #C0130
    ChrTalk(
        0xA,
        (
            "わたくしも歳ですかな。\x01",
            "オンライン予約システムというものは\x01",
            "よくわかりませんよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DC9")

    label("loc_2D41")


    #C0131
    ChrTalk(
        0xA,
        (
            "支配人が進めておられる\x01",
            "オンライン予約システム、でしたか……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        (
            "大変結構なのですが、\x01",
            "わたくしには詳しい事は\x01",
            "とんと判りません。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2DC9")

    Jump("loc_31B1")

    label("loc_2DCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2E8B")

    #C0133
    ChrTalk(
        0xA,
        (
            "この最上階のお部屋はすべて\x01",
            "デラックスルームとなっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        (
            "少々宿泊代金は張ってしまうのですが、\x01",
            "通常の部屋とは比べ物にならない\x01",
            "極上のサービスを提供いたしますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B1")

    label("loc_2E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2F3D")

    #C0135
    ChrTalk(
        0xA,
        (
            "現在のスタッフは、一昨年に\x01",
            "レティシア様が支配人になられてから\x01",
            "集められた者たちなのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xA,
        (
            "ふふ……\x01",
            "個性的なスタッフもいますが\x01",
            "非常に優秀な者ばかりですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B1")

    label("loc_2F3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_30C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2FD4")

    #C0137
    ChrTalk(
        0xA,
        (
            "不戦条約が締結された一昨年以降、\x01",
            "お客様が随分と増えました。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xA,
        (
            "やはり周辺諸国の動向には\x01",
            "気を配っておかねばなりませんな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30C0")

    label("loc_2FD4")


    #C0139
    ChrTalk(
        0xA,
        (
            "当ホテルのお客様は\x01",
            "大半が外国からの観光の方……\x01",
            "周辺諸国の動向には気を配りますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xA,
        (
            "例えば……昨年は\x01",
            "エレボニア・カルバード・リベール間で\x01",
            "不戦条約が締結されました。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        (
            "人の行き来が激しくなり\x01",
            "お客様がどっと増えたのですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_30C0")

    Jump("loc_31B1")

    label("loc_30C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_313F")

    #C0142
    ChrTalk(
        0xA,
        (
            "そろそろ観光客の方々が\x01",
            "チェックインを始められる頃……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            "万全の体制で\x01",
            "お迎えしなければいけませんな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B1")

    label("loc_313F")


    #C0144
    ChrTalk(
        0xA,
        (
            "当ホテルは本年で\x01",
            "開業６０周年となります。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xA,
        (
            "近年はツアー企画なども運営し\x01",
            "ますますご好評頂いておりますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31B1")

    TalkEnd(0xFE)
    Return()

    # Function_10_2738 end

    def Function_11_31B5(): pass

    label("Function_11_31B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3273")

    #C0146
    ChrTalk(
        0x9,
        (
            "ガンツ様、カジノのほうにも\x01",
            "行ってないみたいなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x9,
        (
            "もう夕方……ですね。\x01",
            "さすがに警察に届けた方が……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x9,
        (
            "……えっ、皆様が警察なんですか？\x01",
            "し、失礼しました……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C68")

    label("loc_3273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_335E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_32BB")

    #C0149
    ChrTalk(
        0x9,
        (
            "はぁ……自分の配慮のなさが\x01",
            "いやになります。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3359")

    label("loc_32BB")


    #C0150
    ChrTalk(
        0x9,
        (
            "昨日はガンツ様、\x01",
            "とても静かでした……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x9,
        (
            "ううん、悪いものでも\x01",
            "食べてしまったのでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x9,
        (
            "……ふ、不謹慎でしたかね。\x01",
            "失踪してしまったのに……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3359")

    Jump("loc_3C68")

    label("loc_335E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_34CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_33FE")

    #C0153
    ChrTalk(
        0x9,
        (
            "ガンツ様から頂いたチップ……\x01",
            "額が大きいものですから\x01",
            "市庁舎のほうに寄付してきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x9,
        (
            "……ちょ、ちょっと\x01",
            "勿体無かったかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34CA")

    label("loc_33FE")


    #C0155
    ChrTalk(
        0x9,
        (
            "ガンツ様から額の大きい\x01",
            "チップを頂いてしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x9,
        (
            "手元においておくのが怖いので、\x01",
            "市庁舎のほうに寄付してきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x9,
        (
            "……何に使われるか分かりませんけど、\x01",
            "私の手元にあるよりはいいですよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_34CA")

    Jump("loc_3C68")

    label("loc_34CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3580")

    #C0158
    ChrTalk(
        0x9,
        (
            "最上階に宿泊しているお客様……\x01",
            "少し騒がしくて苦情が来てるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x9,
        (
            "でも、ホテル側としては\x01",
            "どちらも大事なお客様ですから\x01",
            "一方的には言及できないんですよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C68")

    label("loc_3580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_35C9")

    #C0160
    ChrTalk(
        0x9,
        (
            "おはようございます。\x01",
            "……ご家族さまで宿泊でしょうか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C68")

    label("loc_35C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3767")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_363E")
    TurnDirection(0x9, 0x11C, 0)

    #C0161
    ChrTalk(
        0x9,
        (
            "こ、こっちへ来ないで下さい！\x01",
            "わたし犬は苦手なんです……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F0")

    label("loc_363E")

    TurnDirection(0x9, 0x11C, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0162
    ChrTalk(
        0x9,
        "い、犬……！？\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x9,
        (
            "こ、こっちへ来ないで下さい！\x01",
            "わたし犬は苦手なんです……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        "#0012Fはは、それはすみません。\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x11C,
        "#1203Fグルルル……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_36F0")

    TalkEnd(0x9)
    Return()

    label("loc_36F4")


    #C0166
    ChrTalk(
        0x9,
        (
            "外出の際は、\x01",
            "フロントに鍵をお預けください。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x9,
        (
            "お出かけの間にきちんと\x01",
            "ベッドメイクさせていただきます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C68")

    label("loc_3767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_37DF")

    #C0168
    ChrTalk(
        0x9,
        (
            "お部屋にあるお飲み物などは\x01",
            "宿泊料金のうちに入っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x9,
        (
            "どうぞご自由に\x01",
            "お取り下さいませね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C68")

    label("loc_37DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_385E")

    #C0170
    ChrTalk(
        0x9,
        (
            "部屋と廊下の掃除も\x01",
            "一通り終わりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x9,
        (
            "デラックスルームは\x01",
            "整備するところが多くて\x01",
            "やっぱり大変ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C68")

    label("loc_385E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_397D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_38C2")

    #C0172
    ChrTalk(
        0x9,
        (
            "あとでアーロンさんに叱られないように、\x01",
            "念入りに掃除をしておかなくちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3978")

    label("loc_38C2")


    #C0173
    ChrTalk(
        0x9,
        "お掃除はこんなところかしら……\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x9,
        (
            "あとでアーロンさんに叱られないように、\x01",
            "念入りにやっておかなくちゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x9,
        (
            "アーロンさんは\x01",
            "怒っているときもあの調子なので\x01",
            "逆に怖いんですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3978")

    Jump("loc_3C68")

    label("loc_397D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_39BE")

    #C0176
    ChrTalk(
        0x9,
        (
            "最上階は廊下も部屋も広くて\x01",
            "お掃除が大変です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C68")

    label("loc_39BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3A9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3A1B")

    #C0177
    ChrTalk(
        0x9,
        (
            "アルカンシェルの公演を\x01",
            "観にいらっしゃるお客様が\x01",
            "増えそうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A98")

    label("loc_3A1B")


    #C0178
    ChrTalk(
        0x9,
        (
            "アルカンシェルの新作公演、\x01",
            "ついに発表されるそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x9,
        (
            "またお客様が増えそうです。\x01",
            "気を引き締めておかなくちゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3A98")

    Jump("loc_3C68")

    label("loc_3A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3B0F")

    #C0180
    ChrTalk(
        0x9,
        (
            "そろそろ観光ツアーのお客様が\x01",
            "お戻りになられるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x9,
        (
            "お出迎えの準備を\x01",
            "しておかなくちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C68")

    label("loc_3B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3B98")

    #C0182
    ChrTalk(
        0x9,
        (
            "お早うございます。\x01",
            "《ホテル・ミレニアム》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x9,
        (
            "お出かけの際は\x01",
            "お忘れ物などないよう\x01",
            "お気をつけ下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C68")

    label("loc_3B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3C06")

    #C0184
    ChrTalk(
        0x9,
        (
            "今年は例年になく\x01",
            "お客様が多いようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x9,
        (
            "お部屋もすぐに\x01",
            "満室になってしまうんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C68")

    label("loc_3C06")


    #C0186
    ChrTalk(
        0x9,
        (
            "おはようございます。\x01",
            "宿泊客の方でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x9,
        (
            "よろしければお荷物を\x01",
            "部屋までお運びします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C68")

    TalkEnd(0xFE)
    Return()

    # Function_11_31B5 end

    def Function_12_3C6C(): pass

    label("Function_12_3C6C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F37")
    TurnDirection(0xFE, 0x0, 0)

    #C0188
    ChrTalk(
        0x101,
        (
            "#0005Fあ、あなたは確か\x01",
            "ティオの上司の……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x102,
        (
            "#0100Fエプスタイン財団の方が\x01",
            "どうしてホテルに……？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "ああ、このホテルに\x01",
            "導力ネットを引くことになったから\x01",
            "監督に来ているんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "企業やホテルなんかは、\x01",
            "申請を出せば導力ネットの試験運用に\x01",
            "参加が出来るんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x104,
        (
            "#0300Fなるほど、それで……\x02\x03",

            "#0301F……でも導力ネットってのは\x01",
            "随分と簡単に引ける物なんスね？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x103,
        (
            "#0203Fまあ業種や用途などの\x01",
            "一定の審査はありますが……\x02\x03",

            "#0200F端末装置の費用も\x01",
            "ＩＢＣが全額負担してくれますし、\x01",
            "試験環境としては恵まれているかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "そうなんだよねぇ。\x01",
            "お陰でやりたかったテストが沢山できて\x01",
            "本当にＩＢＣ様様だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "ははは、まあ\x01",
            "まだ端末を使える人が少ないから\x01",
            "指導するのも大変なんだけどね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xA, 0)
    SetScenarioFlags(0x92, 6)
    Jump("loc_45A6")

    label("loc_3F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4230")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 6)), scpexpr(EXPR_END)), "loc_3FAD")

    #C0196
    ChrTalk(
        0xFE,
        "さて、ここの端末の設定も完了したよ。\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "まあ僕は専門家だから\x01",
            "お茶の子さいさいだけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_422B")

    label("loc_3FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_403D")

    #C0198
    ChrTalk(
        0xFE,
        (
            "あどけないティオ君に\x01",
            "邪念なんてある訳がないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "うんうん、やっぱり僕の気のせいだ。\x01",
            "支援課のみんな、ティオ君を頼んだよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_422B")

    label("loc_403D")


    #C0200
    ChrTalk(
        0xFE,
        "さて、ここの端末の設定も完了したよ。\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "まあ僕は専門家だから\x01",
            "お茶の子さいさいだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x103,
        (
            "#0203Fこんな人間ですが、主任は\x01",
            "『導力ネットワーク構想』の\x01",
            "開発主任の一人なんですよね。\x02\x03",

            "#0200Fクロスベルの導力ネットは\x01",
            "一応、主任の功績だとか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 500)

    #C0203
    ChrTalk(
        0xFE,
        (
            "そ、そうだけど……\x01",
            "あのティオ君、何かトゲがない？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x103,
        (
            "#0211F……そうですか？\x01",
            "いつも通りですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "そ…………そうだよね！\x01",
            "ハハ、やっぱり僕の気のせいかぁ～。\x02",
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

    label("loc_422B")

    Jump("loc_45A6")

    label("loc_4230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_42E7")

    #C0206
    ChrTalk(
        0xFE,
        (
            "それではまた明日\x01",
            "設定にお伺いしますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "ああ……まだ端末は起動しないように。\x01",
            "初期化作業が必要ですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x103,
        (
            "#0200F（仕事しているときは\x01",
            "  普通なのに……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A6")

    label("loc_42E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_45A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_43AC")
    TurnDirection(0xFE, 0x103, 0)

    #C0209
    ChrTalk(
        0xFE,
        (
            "……ティオ君、\x01",
            "端末が壊れたら僕に言ってね！\x01",
            "すぐに直すから！！\x02",
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
    Jump("loc_45A6")

    label("loc_43AC")


    #C0210
    ChrTalk(
        0xFE,
        (
            "ちなみに端末装置をまともに買うと\x01",
            "１５０万ミラはするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "まだまだ一般市民には\x01",
            "手が届かないんだろうなぁ。\x02",
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
            "#0003F支援課の端末、\x01",
            "いつもぞんざいに扱ってたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x103,
        (
            "#0200Fまあ、物理的な故障は\x01",
            "大した問題ではありません。\x01",
            "気にしなくてもいいかと。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 500)

    #C0214
    ChrTalk(
        0xFE,
        (
            "……ティオ君、\x01",
            "端末が壊れたら僕に言ってね！\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "すぐに直すから！\x01",
            "全力で直すから！！\x02",
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
            "#0200Fいえ……多分\x01",
            "自分で直せるのでいいです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_45A6")

    TalkEnd(0xFE)
    Return()

    # Function_12_3C6C end

    def Function_13_45AA(): pass

    label("Function_13_45AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x337, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x338, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x339, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45E9")
    TurnDirection(0x0, 0xF, 0)
    Call(0, 25)
    Return()

    label("loc_45E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4611")
    TurnDirection(0x0, 0xF, 0)
    Call(0, 24)
    Return()

    label("loc_4611")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4845")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_477D")

    #C0217
    ChrTalk(
        0xFE,
        "これでようやく国に帰れるよ～。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        "みんな、ありがと～！\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x101,
        (
            "#0006Fトロントさん、とりあえず\x01",
            "新しいカバンを買ってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "え、う、うん。\x01",
            "そうだね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        "あはは、ありがと～！\x02",
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
        "#0200F（……どこまでも陽気な人です。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4840")

    label("loc_477D")


    #C0223
    ChrTalk(
        0xFE,
        (
            "お財布よし、お土産よし、\x01",
            "チケットよし！\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "あ、でも入れるカバンがないや。\x01",
            "あはははは～！\x02",
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

    label("loc_4840")

    Jump("loc_4A25")

    label("loc_4845")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_49BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4950")

    #C0225
    ChrTalk(
        0xFE,
        (
            "クロスベルを観光するのが\x01",
            "夢だったからさー。\x01",
            "つい夢中になっちゃったんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "はあ、もう探すのは疲れたよ～。\x01",
            "クロスベル市、広すぎだよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "……あ、でも僕って\x01",
            "今日で帰国する予定なんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        "警察の人、急ぎで頼むよ～っ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_49B9")

    label("loc_4950")


    #C0229
    ChrTalk(
        0xFE,
        (
            "はあ、僕は疲れちゃったよ～。\x01",
            "クロスベル市、広すぎだよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        "警察の人、とにかく急ぎで頼むよ～っ！\x02",
    )

    CloseMessageWindow()

    label("loc_49B9")

    Jump("loc_4A25")

    label("loc_49BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_49CF")
    Jump("loc_4A25")

    label("loc_49CF")


    #C0231
    ChrTalk(
        0xFE,
        (
            "はあぁ～……\x01",
            "もう歩くのやだよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "困ったな～……\x01",
            "諦めて帰っちゃおうかな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A25")

    TalkEnd(0xFE)
    Return()

    # Function_13_45AA end

    def Function_14_4A29(): pass

    label("Function_14_4A29")

    EventBegin(0x2)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0233
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "鍵が掛かっているようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_14_4A29 end

    def Function_15_4A59(): pass

    label("Function_15_4A59")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B34")

    #C0234
    ChrTalk(
        0xC,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        "#0001Fすっかり気を失っているみたいだ。\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x104,
        "#0301Fこいつも薬の副作用ってとこかねぇ。\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x102,
        "#0108Fまだ断定は出来ないけど……\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x103,
        "#0208F………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4B90")

    label("loc_4B34")


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
            "ガンツは気を失っている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    label("loc_4B90")

    TalkEnd(0xC)
    Return()

    # Function_15_4A59 end

    def Function_16_4B94(): pass

    label("Function_16_4B94")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4C19")

    #C0241
    ChrTalk(
        0xFE,
        "ガンツはまだ戻らないようだ……\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "おお、女神よ……\x01",
            "マインツの大切な若者をどうか、\x01",
            "どうか無事に帰したまえ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F03")

    label("loc_4C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4D20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CAB")

    #C0243
    ChrTalk(
        0xFE,
        "おお、君たちか……\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "まったく……ガンツめ、\x01",
            "よく心配をかけてくれるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        "一体どこに行ってしまったんだ……？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4D1B")

    label("loc_4CAB")


    #C0246
    ChrTalk(
        0xFE,
        (
            "ガンツ……\x01",
            "一体どこに行ってしまったんだ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "忙しいところすまないが、\x01",
            "彼の事も気にかけてやってくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D1B")

    Jump("loc_4F03")

    label("loc_4D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4F03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E64")

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
            "……すまない、\x01",
            "やはりショックは隠しきれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        "#0008F町長……\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "……ガンツは決して薬物などに\x01",
            "安易に手を出すような若者ではない。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "その薬が本当に、\x01",
            "そういった物なのかは知らないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "もしそうだとしたら、\x01",
            "ガンツにそれを渡した人物を\x01",
            "私は許す事はできんよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4F03")

    label("loc_4E64")


    #C0254
    ChrTalk(
        0xFE,
        "……ガンツは任せてくれたまえ。\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "もし目を覚ましたら\x01",
            "改めて事情を聞いてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "……その薬が何物でもない\x01",
            "普通の医薬品であることを\x01",
            "願うばかりだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F03")

    TalkEnd(0xD)
    Return()

    # Function_16_4B94 end

    def Function_17_4F07(): pass

    label("Function_17_4F07")

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
            "#5Pおお女神よ……\x01",
            "一体どうしてこんな事に……\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xD,
        (
            "#5Pだらしないが気のいい、\x01",
            "誰からも好かれる男だったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x102,
        "#0108F#12P町長さん……\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x104,
        (
            "#12P#0306Fしかしまあ、とんでもない\x01",
            "暴れっぷりだったよな……\x02\x03",

            "#0301Fまさか俺とロイドの２人がかりで\x01",
            "取り押さえる羽目になるとは\x01",
            "思わなかったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x101,
        (
            "#6P#0006Fああ……\x01",
            "正直、物凄い力だった。\x02",
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
            "#2103F#11Pねえ……\x01",
            "これは率直な印象なんだけど。\x02\x03",

            "#2101Fその人、何か危ない\x01",
            "クスリでもやってるんじゃない？\x02",
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

    def lambda_52BA():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_52BA)

    def lambda_52C7():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_52C7)
    Sleep(50)

    def lambda_52D7():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_52D7)

    def lambda_52E4():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_52E4)
    Sleep(50)
    TurnDirection(0x104, 0x13D, 500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0264
    ChrTalk(
        0xD,
        "#5P#4Sな……！？\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x102,
        "#6P#0105Fそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x104,
        "#6P#0305Fマジかよ……！？\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x13D,
        (
            "#2100F#11Pあら、ロイド君とティオちゃんは\x01",
            "あたしと同意見かしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x103,
        "#0208F#6P#N………それは……………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0269
    ChrTalk(
        0x101,
        (
            "#0006F#6P……あまり滅多なことを\x01",
            "言うつもりはないんですが……\x02\x03",

            "#0001F可能性はあるかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xD,
        (
            "#5Pば、馬鹿な……\x01",
            "薬物なんてあり得るものか！\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xD,
        (
            "#5Pただの普通の鉱員だぞ！？\x01",
            "そんな物に手を出すはずが──\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13D, 0xD, 500)

    #C0272
    ChrTalk(
        0x13D,
        (
            "#2100F#11Pでも、こちらに来てから\x01",
            "半月近く経ってるんでしょう？\x02\x03",

            "相当ミラも儲けていたはずだし、\x01",
            "そこに付け込まれた可能性は\x01",
            "無いとは言い切れないのでは？\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xD,
        "#5Pい、いい加減にしたまえ！\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xD,
        (
            "#5P君はクロスベルタイムズの\x01",
            "記者という話だったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xD,
        (
            "#5P憶測で記事を書いたりしたら\x01",
            "厳重に抗議させてもらうぞ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x13D,
        (
            "#2106F#11Pあー、別に記事に\x01",
            "するつもりは無いんですが。\x02",
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
            "#12P#0003F──ビクセン町長。\x02\x03",

            "#0001F念のため、ガンツさんの私物を\x01",
            "確かめても構いませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_56FB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_56FB)
    Sleep(100)

    def lambda_570B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_570B)

    def lambda_5718():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5718)

    def lambda_5725():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5725)
    Sleep(50)
    TurnDirection(0x13D, 0x101, 500)

    #C0278
    ChrTalk(
        0xD,
        "#5Pロイド君、君まで！？\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        (
            "#12P#0006F決め付けるつもりはありませんが\x01",
            "色々と符合する事も多いんです。\x02\x03",

            "#0008Fあの暴れ方、凄まじい力、\x01",
            "そして変わってしまった性格……\x02\x03",

            "#0013F過去、幾つかあった薬物事件と\x01",
            "似たような反応が見られるんです。\x02\x03",

            "それに、比べ物にならないくらい\x01",
            "ギャンブルの腕が上がったのも……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x104,
        (
            "#0303F#11P……クスリのせいで知覚が異常に\x01",
            "過敏になったせいかもしれねぇな。\x02\x03",

            "#0301Fそれで相手の心理を読み取ったり、\x01",
            "カンが働いてたのかもしれねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x103,
        (
            "#12P#0206F…………そうですね。\x02\x03",

            "#0200F多分、わたしが賭け事をすれば、\x01",
            "他の人よりも有利になるはずです。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)
    Sleep(300)

    #C0282
    ChrTalk(
        0x102,
        "#0105F#5Pティオちゃん……\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x104,
        (
            "#0306F#11P……悪ぃ。\x01",
            "んなつもりじゃ無かったが。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x103,
        (
            "#12P#0204Fいえ、気にしてません。\x02\x03",

            "#0201F──町長さん。\x01",
            "ガンツさんの名誉のことを\x01",
            "気にするのは分かります。\x02\x03",

            "でも、もし本当に\x01",
            "何らかの薬物だった場合……\x02\x03",

            "このまま放置しておいたら\x01",
            "どんな危険があるか分かりません。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_5ABB():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5ABB)
    Sleep(50)

    def lambda_5ACB():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5ACB)

    #C0285
    ChrTalk(
        0xD,
        "#5Pそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x13D,
        (
            "#11P#2106F中毒症状に後遺症……\x01",
            "まあ、色々と考えられそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#12P#0006Fええ、薬物による被害で\x01",
            "一番怖いのはそこだと思います。\x02",
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
            "#5P判った……\x01",
            "思慮が足りなかったようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xD,
        "#5Pロイド君、お願いする。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        "#12P#0003F……はい。\x02",
    )

    CloseMessageWindow()

    def lambda_5BF4():

        label("loc_5BF4")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_5BF4")

    QueueWorkItem2(0x13D, 2, lambda_5BF4)

    def lambda_5C06():

        label("loc_5C06")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_5C06")

    QueueWorkItem2(0x102, 2, lambda_5C06)

    def lambda_5C18():

        label("loc_5C18")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_5C18")

    QueueWorkItem2(0x103, 2, lambda_5C18)

    def lambda_5C2A():

        label("loc_5C2A")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_5C2A")

    QueueWorkItem2(0x104, 2, lambda_5C2A)

    def lambda_5C3C():

        label("loc_5C3C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_5C3C")

    QueueWorkItem2(0xD, 2, lambda_5C3C)
    OP_68(162700, 1000, 4930, 1200)

    def lambda_5C5F():
        OP_96(0xFE, 0x27B8C, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C5F)
    Sleep(300)

    def lambda_5C7C():
        OP_96(0xFE, 0x278D0, 0x0, 0xC80, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5C7C)
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
            "ロイドはガンツを起こさないよう、\x01",
            "注意して懐などを探って行った。\x07\x00\x02",
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
        "#6P#0013F（………これは…………）\x02",
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x32B, 1)

    #A0294
    AnonymousTalk(
        0x102,
        "#0105Fそ、それは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0295
    AnonymousTalk(
        0xD,
        "おお、女神よ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0296
    AnonymousTalk(
        0x13D,
        "#2101Fまさか本当にあったなんて……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0297
    AnonymousTalk(
        0x104,
        (
            "#0301F綺麗な色をしてやがるが……\x01",
            "いったい、どんなクスリなんだ？\x02",
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
            "#0006F#5P──まだこの薬が\x01",
            "原因と決まったわけじゃない。\x02\x03",

            "ひょっとしたら\x01",
            "何か持病の薬かもしれないし。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 500)

    #C0300
    ChrTalk(
        0x101,
        "#11P#0001F町長、ガンツさんに持病は？\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xD,
        (
            "#6P……知る限り無かったはずだ。\x01",
            "もちろん断言は出来ないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x101,
        (
            "#11P#0003F判りました。\x02\x03",

            "#0001F……この薬はいったん、\x01",
            "こちらで預からせて頂いても？\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xD,
        "#6Pああ……よろしくお願いする。\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xD,
        (
            "#6Pだが、どうか……！\x01",
            "どうか事を大きくするのは……！\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x101,
        (
            "#11P#0004Fええ、ガンツさんの名誉には\x01",
            "配慮させていただきます。\x02\x03",

            "#0001Fガンツさん自身については\x01",
            "そちらにお任せしても……？\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xD,
        "#6Pああ……任せてくれたまえ。\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xD,
        (
            "#6Pもし目を覚ましたら\x01",
            "改めて話を聞いてみるつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x101,
        "#11P#0000Fええ、よろしくお願いします。\x02",
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
            "#6P#2106F──ふう、それにしても\x01",
            "クロスベルで薬物疑惑とはねぇ。\x02\x03",

            "珍しいこともあるもんだわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0310
    ChrTalk(
        0x104,
        (
            "#11P#0305Fそうなんスか？\x02\x03",

            "#0301Fてっきりマフィアあたりが\x01",
            "色々扱ってると思ってたんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x13D,
        (
            "#6P#2104Fところがどっこい、\x01",
            "クロスベルで違法薬物ってのは\x01",
            "あんまり出回ることはないのよ。\x02\x03",

            "#2100F何しろ他の犯罪とは違って、\x01",
            "周辺諸国にも広がりかねない\x01",
            "影響力のある犯罪だからね。\x02\x03",

            "帝国や共和国からの圧力もあって\x01",
            "捜査一課の手で違法薬物は\x01",
            "厳重に取り締まられてるらしいの。\x02\x03",

            "#2104Fそしてルバーチェなんかも\x01",
            "その辺の空気は読んでるわけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x102,
        "#11P#0105Fそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        (
            "#11P#0003Fそのあたりの事情は俺も\x01",
            "警察学校で教えてもらいました。\x02\x03",

            "#0008Fでも、この錠剤は……\x02",
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
            "#0101F蒼色の錠剤……\x01",
            "見た目は綺麗な感じだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0315
    AnonymousTalk(
        0x104,
        (
            "#0301Fなんつーか……\x01",
            "やたらと怪しげな感じだな。\x02",
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
        "#6P#0005Fティオ、何か心当たりが？\x02",
    )

    CloseMessageWindow()

    def lambda_6633():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6633)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)

    #C0318
    ChrTalk(
        0x103,
        (
            "#0206F#11Pいえ……すみません。\x01",
            "ただの気のせいだと思います。\x02\x03",

            "#0201Fでも、その錠剤……\x01",
            "一体どうするつもりなんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        (
            "#6P#0006Fそうだな……\x02\x03",

            "俺たちだけで決めるのは\x01",
            "ちょっと大事#4Rおおごと#すぎるかもしれない。\x02\x03",

            "#0001Fいったん戻って課長に相談しよう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_674C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_674C)
    Sleep(100)
    TurnDirection(0x104, 0x101, 500)

    #C0320
    ChrTalk(
        0x102,
        (
            "#5P#0103Fええ、それがいいと思うわ。\x02\x03",

            "#0101F《黒月》の襲撃事件についても\x01",
            "報告した方がいいでしょうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#5P#0306Fマフィア同士の抗争に加えて\x01",
            "クスリ絡みの事件の可能性か……\x02\x03",

            "#0301Fったく、とんでもなく\x01",
            "忙しくなりそうな気がしてきたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x13D,
        "#6P#2102Fふふっ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_68B6():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_68B6)
    Sleep(50)

    def lambda_68C6():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_68C6)
    Sleep(50)

    def lambda_68D6():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_68D6)
    Sleep(50)
    TurnDirection(0x104, 0x13D, 500)

    #C0323
    ChrTalk(
        0x13D,
        (
            "#6P#2109Fいや～、あなたたちと\x01",
            "知り合って４ヶ月になるけど……\x02\x03",

            "ずいぶん成長したな～って、\x01",
            "お姉さん感慨に浸っちゃうなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x101,
        "#11P#0005Fグレイスさん……？\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x102,
        (
            "#11P#0105Fい、いきなり\x01",
            "どうしたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x103,
        "#0211F#11P誉めても何も出ませんが……\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x13D,
        (
            "#6P#2104Fいやいや、マジな話、\x01",
            "あなた達には期待してるのよ。\x02\x03",

            "#2100Fロイド君のお兄さん……\x01",
            "ガイ・バニングスと同じくらいね。\x02",
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
            "#11P#0011Fそ、そういえば……\x01",
            "前にも言ってましたけど。\x02\x03",

            "グレイスさんは兄貴と\x01",
            "知り合いだったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x13D,
        (
            "#6P#2104Fあたしが新米記者だった頃、\x01",
            "色々とお世話になったのよね～。\x02\x03",

            "#2106F結局、ガイさんの事件については\x01",
            "迷宮入りになっちゃったけど……\x02\x03",

            "#2102Fそれでも、彼の遺志を継ぐ部署が\x01",
            "警察に出来て凄く嬉しかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x101,
        "#11P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x102,
        (
            "#11P#0105Fロイドのお兄さんの遺志を\x01",
            "受け継ぐ部署……？\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x13D,
        (
            "#6P#2104Fおっと、これ以上喋ると\x01",
            "課長さんに怒られちゃうかな。\x02\x03",

            "#2100Fあたしも取材があるし、\x01",
            "今日の所はこれで失礼するわね。\x02\x03",

            "#2105Fあ、クスリの件については\x01",
            "勝手に記事にしないから安心して。\x02\x03",

            "#2109Fそれじゃあ、バハハーイ！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x13D, 0x5A, 0x1F4)
    OP_68(76000, 0, 6900, 2000)

    def lambda_6D55():
        OP_98(0xFE, 0x1F40, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13D, 1, lambda_6D55)

    def lambda_6D6F():

        label("loc_6D6F")

        TurnDirection(0xFE, 0x13D, 500)
        Yield()
        Jump("loc_6D6F")

    QueueWorkItem2(0x101, 2, lambda_6D6F)

    def lambda_6D81():

        label("loc_6D81")

        TurnDirection(0xFE, 0x13D, 500)
        Yield()
        Jump("loc_6D81")

    QueueWorkItem2(0x102, 2, lambda_6D81)

    def lambda_6D93():

        label("loc_6D93")

        TurnDirection(0xFE, 0x13D, 500)
        Yield()
        Jump("loc_6D93")

    QueueWorkItem2(0x103, 2, lambda_6D93)

    def lambda_6DA5():

        label("loc_6DA5")

        TurnDirection(0xFE, 0x13D, 500)
        Yield()
        Jump("loc_6DA5")

    QueueWorkItem2(0x104, 2, lambda_6DA5)
    Sleep(1500)

    def lambda_6DBA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13D, 2, lambda_6DBA)
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
            "#5P#0306Fったく、思わせぶりなことを\x01",
            "言うだけ言って行きやがったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x102,
        (
            "#5P#0106Fはぁ……ただでさえ\x01",
            "考えることが山ほどあるのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x103,
        "#0206F#5P……ですね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0337
    ChrTalk(
        0x103,
        (
            "#0200F#11Pロイドさん……\x01",
            "ガイさんの話、気になります？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(150)

    #C0338
    ChrTalk(
        0x101,
        "#6P#0005Fああ、いや……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0339
    ChrTalk(
        0x101,
        (
            "#6P#0006F──確かに気になるけど\x01",
            "どう考えても今は後回しだ。\x02\x03",

            "#0008F黒月の襲撃、ルバーチェの状況、\x01",
            "そしてこの蒼い錠剤……\x02\x03",

            "#0000F一通り課長に報告した上で\x01",
            "どうするか検討してみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x103,
        "#0202F#11P……はい。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x102,
        "#5P#0100Fええ、分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x104,
        (
            "#5P#0300Fよし、それじゃあとっとと\x01",
            "支援課に戻るとしようぜ！\x02",
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

    # Function_17_4F07 end

    def Function_18_71D1(): pass

    label("Function_18_71D1")


    #C0343
    ChrTalk(
        0x11C,
        "#1200F……ウォンウォン！\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        (
            "#0003F……こっちじゃ\x01",
            "無いみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_18_71D1 end

    def Function_19_721B(): pass

    label("Function_19_721B")

    EventBegin(0x1)
    Call(0, 18)
    Sleep(50)
    SetChrPos(0x0, 56000, 0, 11250, 180)
    EventEnd(0x4)
    Return()

    # Function_19_721B end

    def Function_20_7237(): pass

    label("Function_20_7237")

    EventBegin(0x1)
    Call(0, 18)
    Sleep(50)
    SetChrPos(0x0, 68000, 0, 11250, 180)
    EventEnd(0x4)
    Return()

    # Function_20_7237 end

    def Function_21_7253(): pass

    label("Function_21_7253")

    EventBegin(0x1)
    Call(0, 18)
    Sleep(50)
    SetChrPos(0x0, 1000, 0, 66250, 180)
    EventEnd(0x4)
    Return()

    # Function_21_7253 end

    def Function_22_726F(): pass

    label("Function_22_726F")

    EventBegin(0x1)
    Call(0, 18)
    Sleep(50)
    SetChrPos(0x0, 7250, 0, 60000, 270)
    EventEnd(0x4)
    Return()

    # Function_22_726F end

    def Function_23_728B(): pass

    label("Function_23_728B")

    EventBegin(0x1)
    Call(0, 18)
    Sleep(50)
    SetChrPos(0x0, 1000, 0, 53750, 0)
    EventEnd(0x4)
    Return()

    # Function_23_728B end

    def Function_24_72A7(): pass

    label("Function_24_72A7")

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
            "#11Pはあぁ～……\x01",
            "もう歩くのやだよ～。\x02",
        )
    )

    CloseMessageWindow()

    #N0346
    NpcTalk(
        0xF,
        "青年",
        "#11P諦めて帰っちゃおうかな～。\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        (
            "#12P#0000Fあの、すいません。\x01",
            "依頼を出された\x01",
            "トロントさんですか？\x02",
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
        "#11Pおっ、警察の人？\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xF,
        (
            "#11Pおお～、まさか\x01",
            "来てくれるとは思わなかったよ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x101,
        "#12P#0012Fははは、どうも……\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x102,
        (
            "#5P#0100Fえっと、落し物を\x01",
            "されたということですが、\x01",
            "お話を聞かせて頂けますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xF,
        (
            "#11Pそれがね、聞くも涙、\x01",
            "語るも涙なわけで……\x02",
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
            "#11P僕は買い物大好きなわけで、\x01",
            "クロスベルのあちこちを\x01",
            "見て回ってたわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xF,
        (
            "#11Pでも……ふと気付いたら\x01",
            "カバンに穴が開いててさ。\x01",
            "ポロポロこぼしてたわけ！\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xF,
        (
            "#11P僕も必死に探し回ったんだけど\x01",
            "いくつかはどうしても\x01",
            "見つからないんだよねぇ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x104,
        (
            "#0306Fなるほどなぁ……\x02\x03",

            "#0301Fだが昨日の今日じゃ\x01",
            "路上に落ちたまんまってのは\x01",
            "考えにくいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x103,
        (
            "#12P#0200F付近のどなたかが\x01",
            "拾ってくれているかもしれませんね。\x02\x03",

            "ショッピングで\x01",
            "立ち寄った場所を伺っても？\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xF,
        "#11Pうん、まずは当然百貨店さ！\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xF,
        (
            "#11P最新のブランド物が揃っててさ～、\x01",
            "じっくり堪能させてもらったよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xF,
        (
            "#11Pそれから東通りの市場を\x01",
            "ながめて回って……\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xF,
        (
            "#11P港湾区にある公園に来た辺りで\x01",
            "カバンの破れに気付いたんだよね～。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1800)

    #C0362
    ChrTalk(
        0xF,
        (
            "#11P……はあ、どうしても\x01",
            "見つからないんだよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xF,
        (
            "#11Pお財布と土産物と……\x01",
            "あともう１つ、何だったかなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xF,
        (
            "#11P絶対に３つ、\x01",
            "足りないと思うんだけどなぁ……\x02",
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
            "#12P#0003F……最後の１つは\x01",
            "思い出せないわけですね。\x02\x03",

            "#0001F分かりました、ともかくこちらで\x01",
            "周辺を捜索してみましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x102,
        (
            "#5P#0103F中央広場の百貨店に\x01",
            "東通り、港湾区……\x02\x03",

            "#0100Fどこも商店の多い地区だし\x01",
            "お店の人を中心に\x01",
            "聞いて回るのが良さそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xF,
        "#11Pよろしく頼んだよ～っ！\x02",
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
            "クエスト【紛失物の捜索願い】\x07\x00",
            "を開始した！\x02",
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

    # Function_24_72A7 end

    def Function_25_7B37(): pass

    label("Function_25_7B37")

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
            "#12P#0000Fトロントさん、確か\x01",
            "落し物は３つでしたよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x102,
        (
            "#5P#0100F全て見つけてきました。\x02\x03",

            "……はいどうぞ。\x01",
            "もう落とさないでくださいね。\x02",
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
            "を渡した。\x02",
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
            "を渡した。\x02",
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
            "を渡した。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    OP_5A()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x337, 1)
    SubItemNumber(0x338, 1)
    SubItemNumber(0x339, 1)
    OP_96(0x102, 0x1BEA4, 0x0, 0xE83A, 0x3E8, 0x0)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0374
    ChrTalk(
        0xF,
        "#11Pおお、確かに僕の持ち物だ！\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xF,
        (
            "#11Pいやあ良かったぁ～。\x01",
            "もう諦めて国に帰ろうかと\x01",
            "思ってたんだよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x103,
        (
            "#12P#0200Fお財布もチケットも無くては\x01",
            "帰れないのでは……？\x02",
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
            "#11Pうっ……そ、それもそうだね。\x01",
            "あはは、気付かなかったよ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xF,
        (
            "#11Pでも本当にありがとうね～。\x01",
            "念のために警察に\x01",
            "連絡してはみたものの……\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xF,
        (
            "#11Pクロスベルの警察って\x01",
            "対応が悪いって聞いてたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xF,
        (
            "#11Pまさか対応してもらえるとは\x01",
            "思ってなかったよ～。\x02",
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
        "#12P#0012Fそ、そうですか……\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x104,
        (
            "#0306F何となく特務支援課って場所の\x01",
            "意義が判ってきた気がするなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x102,
        (
            "#5P#0100Fまあいいじゃない、\x01",
            "１人の人を助けたわけだし。\x02\x03",

            "これで依頼達成よね。\x02",
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
            "クエスト【紛失物の捜索願い】\x07\x00",
            "を達成した！\x02",
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

    # Function_25_7B37 end

    SaveToFile()

Try(main)
