from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0140.bin",                # FileName
        "c0140",                    # MapName
        "c0140",                    # Location
        0x0006,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 6, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0140",                  # 0
        "查珂",                   # 1
        "温蒂",                   # 2
        "菲尔纳德",               # 3
        "米泽特",                 # 4
        "巴吉利奥",               # 5
        "哈斯",                   # 6
        "市民",                   # 7
        "游客",                   # 8
        "游客",                   # 9
        "雷因兹",                 # 10
    ))

    AddCharChip((
        "chr/ch26100.itc",                   # 00
        "chr/ch27800.itc",                   # 01
        "chr/ch25700.itc",                   # 02
        "chr/ch21000.itc",                   # 03
        "chr/ch20800.itc",                   # 04
        "chr/ch21900.itc",                   # 05
        "chr/ch24500.itc",                   # 06
        "chr/ch32300.itc",                   # 07
        "chr/ch32200.itc",                   # 08
        "chr/ch28100.itc",                   # 09
        "chr/ch26000.itc",                   # 0A
    ))

    DeclNpc(9270,    0,       2650,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(9329,    0,       -1350,   270,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-1519,   0,       14659,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-4480,   0,       7440,    0,    261,  0x0, 0,   5,   0,   0,   1,   0,   14,  255,  0)
    DeclNpc(2299,    0,       6420,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-1519,   0,       14659,   180,  389,  0x0, 0,   10,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(11319,   4000,    8640,    90,   385,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(11470,   4000,    -1720,   90,   385,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(11300,   4000,    -2170,   90,   385,  0x0, 0,   8,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-4679,   0,       -1820,   90,   389,  0x0, 0,   9,   0,   0,   0,   0,   20,  255,  0)

    DeclActor(8130,    0,       3080,    1000,    9270,    1500,    2650,    0x007E, 0,  4,  0x0000)
    DeclActor(8310,    0,       -1360,   1000,    9330,    1500,    -1350,   0x007E, 0,  8,  0x0000)

    ChipFrameInfo(652, 0)                                        # 0

    ScpFunction((
        "Function_0_28C",          # 00, 0
        "Function_1_344",          # 01, 1
        "Function_2_495",          # 02, 2
        "Function_3_677",          # 03, 3
        "Function_4_6C3",          # 04, 4
        "Function_5_9BA",          # 05, 5
        "Function_6_247F",         # 06, 6
        "Function_7_2C14",         # 07, 7
        "Function_8_3511",         # 08, 8
        "Function_9_351B",         # 09, 9
        "Function_10_392A",        # 0A, 10
        "Function_11_4FAB",        # 0B, 11
        "Function_12_5ADF",        # 0C, 12
        "Function_13_5CBC",        # 0D, 13
        "Function_14_6A64",        # 0E, 14
        "Function_15_7305",        # 0F, 15
        "Function_16_7CC6",        # 10, 16
        "Function_17_7DD4",        # 11, 17
        "Function_18_8172",        # 12, 18
        "Function_19_8395",        # 13, 19
        "Function_20_84A4",        # 14, 20
        "Function_21_858C",        # 15, 21
        "Function_22_90B7",        # 16, 22
        "Function_23_987F",        # 17, 23
        "Function_24_AAE1",        # 18, 24
        "Function_25_B44A",        # 19, 25
        "Function_26_B96E",        # 1A, 26
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

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_494")
    OP_95(0xFE, -4480, 0, 9380, 2000, 0x0)
    OP_95(0xFE, -1380, 0, 11120, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 9480, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 9480, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 6900, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 5230, 0, 1000, 2000, 0x0)
    OP_95(0xFE, 3800, 0, 930, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -1350, 0, 930, 2000, 0x0)
    OP_95(0xFE, -1310, 0, -1230, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -1310, 0, 2990, 2000, 0x0)
    OP_95(0xFE, -4480, 0, 4640, 2000, 0x0)
    OP_95(0xFE, -4480, 0, 7440, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    Jump("Function_1_344")

    label("loc_494")

    Return()

    # Function_1_344 end

    def Function_2_495(): pass

    label("Function_2_495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4B9")
    SetChrPos(0xC, 7140, 0, 3340, 90)
    SetChrFlags(0xA, 0x80)
    Jump("loc_649")

    label("loc_4B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4E7")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xA, 7390, 0, -250, 270)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_649")

    label("loc_4E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4F5")
    Jump("loc_649")

    label("loc_4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_503")
    Jump("loc_649")

    label("loc_503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_516")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_649")

    label("loc_516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_529")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_649")

    label("loc_529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_53C")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_649")

    label("loc_53C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_54F")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_649")

    label("loc_54F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_562")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_649")

    label("loc_562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_575")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_649")

    label("loc_575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_588")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_649")

    label("loc_588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5AC")
    SetChrPos(0xC, -3640, 0, 5020, 45)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_649")

    label("loc_5AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E4")
    SetChrPos(0xC, -3640, 0, 5020, 45)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DF")
    SetChrFlags(0x11, 0x10)

    label("loc_5DF")

    Jump("loc_649")

    label("loc_5E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_619")
    SetChrPos(0xC, 11470, 4000, 8119, 90)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 2040, 0, 12670, 0)
    Jump("loc_649")

    label("loc_619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_649")
    SetChrPos(0xC, -3640, 0, 5020, 45)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 11470, 4000, 8119, 90)

    label("loc_649")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_676")
    SetMapFlags(0x10000000)
    Event(0, 24)

    label("loc_676")

    Return()

    # Function_2_495 end

    def Function_3_677(): pass

    label("Function_3_677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68A")
    OP_1B(0x0, 0x0, 0x1A)

    label("loc_68A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6AB")
    Sound(128, 1, 50, 0)

    label("loc_6AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C2")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)

    label("loc_6C2")

    Return()

    # Function_3_677 end

    def Function_4_6C3(): pass

    label("Function_4_6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E3")
    SetScenarioFlags(0x0, 0)
    TalkBegin(0x8)
    Call(0, 12)
    TalkEnd(0x8)
    Return()

    label("loc_6E3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C9")

    #C0001
    ChrTalk(
        0x8,
        (
            "欢迎光临☆\x01",
            "这边是销售柜台。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "啊，各位是温蒂前辈的\x01",
            "朋友吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "呵呵，有新的艾尼格玛\x01",
            "外壳到货啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "只要购买过一次，\x01",
            "以后就可以随时来我们这里\x01",
            "免费更换外壳了～\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "请不必客气，\x01",
            "有需要时就尽管吩咐我吧～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 4)

    label("loc_7C9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B6")
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_891")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",                        # 0
            "购买·更换艾尼格玛外壳\x01",      # 1
            "购买核心回路\x01",                # 2
            "购买导力车部件\x01",              # 3
            "放弃\x01",                        # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_88C")

    Jump("loc_90A")

    label("loc_891")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",                        # 0
            "购买·更换艾尼格玛外壳\x01",      # 1
            "购买核心回路\x01",                # 2
            "放弃\x01",                        # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_90A")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_90A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_90A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92B")
    Call(0, 7)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9B1")

    label("loc_92B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94F")
    OP_60(0x0)
    Call(0, 5)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9B1")

    label("loc_94F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_973")
    OP_60(0x0)
    Call(0, 6)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9B1")

    label("loc_973")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B1")
    OP_60(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_995")
    OP_AF(0xC0)
    Jump("loc_9A7")

    label("loc_995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_9A5")
    OP_AF(0xBF)
    Jump("loc_9A7")

    label("loc_9A5")

    OP_AF(0xBE)

    label("loc_9A7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9B1")

    Jump("loc_7D3")

    label("loc_9B6")

    TalkEnd(0x8)
    Return()

    # Function_4_6C3 end

    def Function_5_9BA(): pass

    label("Function_5_9BA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_247E")
    MenuCmd(0, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0006
    ChrTalk(
        0x8,
        "要更换成哪款呢～？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ADC")
    MenuCmd(1, 0, "ＣＰＤ（罗伊德）　　　使用中")
    Jump("loc_AFA")

    label("loc_ADC")

    MenuCmd(1, 0, "ＣＰＤ（罗伊德）　　　更换")

    label("loc_AFA")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_END)), "loc_B3C")
    MenuCmd(1, 0, "蓝色警官　　　　　　　使用中")
    Jump("loc_B8A")

    label("loc_B3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_END)), "loc_B68")
    MenuCmd(1, 0, "蓝色警官　　　　　　　更换")
    Jump("loc_B8A")

    label("loc_B68")

    MenuCmd(1, 0, "蓝色警官　　　　　　　1000米拉")

    label("loc_B8A")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_END)), "loc_BC2")
    MenuCmd(1, 0, "啸天狼　　　　　　　　使用中")
    Jump("loc_C10")

    label("loc_BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_END)), "loc_BEE")
    MenuCmd(1, 0, "啸天狼　　　　　　　　更换")
    Jump("loc_C10")

    label("loc_BEE")

    MenuCmd(1, 0, "啸天狼　　　　　　　　1000米拉")

    label("loc_C10")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_CBF")

    label("loc_CA1")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CBF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D03")
    MenuCmd(1, 0, "ＣＰＤ（艾莉）　　　　使用中")
    Jump("loc_D21")

    label("loc_D03")

    MenuCmd(1, 0, "ＣＰＤ（艾莉）　　　　更换")

    label("loc_D21")

    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_END)), "loc_D63")
    MenuCmd(1, 0, "和平绿　　　　　　　　使用中")
    Jump("loc_DB1")

    label("loc_D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_END)), "loc_D8F")
    MenuCmd(1, 0, "和平绿　　　　　　　　更换")
    Jump("loc_DB1")

    label("loc_D8F")

    MenuCmd(1, 0, "和平绿　　　　　　　　1000米拉")

    label("loc_DB1")

    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_END)), "loc_DE9")
    MenuCmd(1, 0, "报春鸟　　　　　　　　使用中")
    Jump("loc_E37")

    label("loc_DE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_END)), "loc_E15")
    MenuCmd(1, 0, "报春鸟　　　　　　　　更换")
    Jump("loc_E37")

    label("loc_E15")

    MenuCmd(1, 0, "报春鸟　　　　　　　　1000米拉")

    label("loc_E37")

    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_EC8")

    label("loc_EAA")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EC8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1095")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F0C")
    MenuCmd(1, 0, "ＣＰＤ（缇欧）　　　　使用中")
    Jump("loc_F2A")

    label("loc_F0C")

    MenuCmd(1, 0, "ＣＰＤ（缇欧）　　　　更换")

    label("loc_F2A")

    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_END)), "loc_F6C")
    MenuCmd(1, 0, "黑猫　　　　　　　　　使用中")
    Jump("loc_FBA")

    label("loc_F6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_END)), "loc_F98")
    MenuCmd(1, 0, "黑猫　　　　　　　　　更换")
    Jump("loc_FBA")

    label("loc_F98")

    MenuCmd(1, 0, "黑猫　　　　　　　　　1000米拉")

    label("loc_FBA")

    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_END)), "loc_FF2")
    MenuCmd(1, 0, "影丸　　　　　　　　　使用中")
    Jump("loc_1040")

    label("loc_FF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_END)), "loc_101E")
    MenuCmd(1, 0, "影丸　　　　　　　　　更换")
    Jump("loc_1040")

    label("loc_101E")

    MenuCmd(1, 0, "影丸　　　　　　　　　1000米拉")

    label("loc_1040")

    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_10B3")

    label("loc_1095")

    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1262")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F7")
    MenuCmd(1, 0, "ＣＰＤ（兰迪）　　　　使用中")
    Jump("loc_1115")

    label("loc_10F7")

    MenuCmd(1, 0, "ＣＰＤ（兰迪）　　　　更换")

    label("loc_1115")

    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_END)), "loc_1157")
    MenuCmd(1, 0, "危险橙　　　　　　　　使用中")
    Jump("loc_11A5")

    label("loc_1157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_END)), "loc_1183")
    MenuCmd(1, 0, "危险橙　　　　　　　　更换")
    Jump("loc_11A5")

    label("loc_1183")

    MenuCmd(1, 0, "危险橙　　　　　　　　1000米拉")

    label("loc_11A5")

    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_END)), "loc_11DD")
    MenuCmd(1, 0, "午夜香吻　　　　　　　使用中")
    Jump("loc_122B")

    label("loc_11DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_END)), "loc_1209")
    MenuCmd(1, 0, "午夜香吻　　　　　　　更换")
    Jump("loc_122B")

    label("loc_1209")

    MenuCmd(1, 0, "午夜香吻　　　　　　　1000米拉")

    label("loc_122B")

    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1280")

    label("loc_1262")

    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1280")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1386")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12BF")
    MenuCmd(1, 0, "ＣＧＦ（诺艾尔）　　　使用中")
    Jump("loc_12DD")

    label("loc_12BF")

    MenuCmd(1, 0, "ＣＧＦ（诺艾尔）　　　更换")

    label("loc_12DD")

    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_END)), "loc_1315")
    MenuCmd(1, 0, "自由之路　　　　　　　使用中")
    Jump("loc_1363")

    label("loc_1315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_END)), "loc_1341")
    MenuCmd(1, 0, "自由之路　　　　　　　更换")
    Jump("loc_1363")

    label("loc_1341")

    MenuCmd(1, 0, "自由之路　　　　　　　1000米拉")

    label("loc_1363")

    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_139A")

    label("loc_1386")

    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_139A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_148C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D9")
    MenuCmd(1, 0, "纯白信条　　　　　　　使用中")
    Jump("loc_13F7")

    label("loc_13D9")

    MenuCmd(1, 0, "纯白信条　　　　　　　更换")

    label("loc_13F7")

    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_END)), "loc_142F")
    MenuCmd(1, 0, "纹章盟约　　　　　　　使用中")
    Jump("loc_147D")

    label("loc_142F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_END)), "loc_145B")
    MenuCmd(1, 0, "纹章盟约　　　　　　　更换")
    Jump("loc_147D")

    label("loc_145B")

    MenuCmd(1, 0, "纹章盟约　　　　　　　1000米拉")

    label("loc_147D")

    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_14A0")

    label("loc_148C")

    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14A0")

    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14D1")
    Sleep(1)
    Return()

    label("loc_14D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_150F")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_18AC")

    label("loc_150F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_154D")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis350.itp")
    Jump("loc_18AC")

    label("loc_154D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_158B")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis351.itp")
    Jump("loc_18AC")

    label("loc_158B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C9")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_18AC")

    label("loc_15C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1607")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis352.itp")
    Jump("loc_18AC")

    label("loc_1607")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1645")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis353.itp")
    Jump("loc_18AC")

    label("loc_1645")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1683")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_18AC")

    label("loc_1683")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C1")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis354.itp")
    Jump("loc_18AC")

    label("loc_16C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16FF")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis355.itp")
    Jump("loc_18AC")

    label("loc_16FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_173D")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_18AC")

    label("loc_173D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_177B")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis356.itp")
    Jump("loc_18AC")

    label("loc_177B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B9")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis357.itp")
    Jump("loc_18AC")

    label("loc_17B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F7")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis392.itp")
    Jump("loc_18AC")

    label("loc_17F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1835")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis359.itp")
    Jump("loc_18AC")

    label("loc_1835")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1873")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis393.itp")
    Jump("loc_18AC")

    label("loc_1873")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18AC")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis358.itp")

    label("loc_18AC")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1957")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个外壳是罗伊德专用的。\x01",
            "更换后，显示在[ORBMENT]菜单里的\x01",
            "战术导力器外壳即会改变。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAB")

    label("loc_1957")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_19D2")

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个外壳是艾莉专用的。\x01",
            "更换后，显示在[ORBMENT]菜单里的\x01",
            "战术导力器外壳即会改变。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAB")

    label("loc_19D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A4D")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个外壳是缇欧专用的。\x01",
            "更换后，显示在[ORBMENT]菜单里的\x01",
            "战术导力器外壳即会改变。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAB")

    label("loc_1A4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1AC8")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个外壳是兰迪专用的。\x01",
            "更换后，显示在[ORBMENT]菜单里的\x01",
            "战术导力器外壳即会改变。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAB")

    label("loc_1AC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B3D")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个外壳是诺艾尔专用的。\x01",
            "更换后，显示在[ORBMENT]菜单里的\x01",
            "战术导力器外壳即会改变。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAB")

    label("loc_1B3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BAB")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个外壳是瓦吉专用的。\x01",
            "更换后，显示在[ORBMENT]菜单里的\x01",
            "战术导力器外壳即会改变。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BAB")


    #A0013
    AnonymousTalk(
        0x8,
        "好的，要这个吗～？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【更换外壳】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x3)
    OP_60(0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2461")
    ClearScenarioFlags(0x1, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C5C")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1DE2")

    label("loc_1C5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C75")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1DE2")

    label("loc_1C75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C8E")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1DE2")

    label("loc_1C8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CAD")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1DE2")

    label("loc_1CAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CC6")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1DE2")

    label("loc_1CC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CDF")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1DE2")

    label("loc_1CDF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CFE")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1DE2")

    label("loc_1CFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D17")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1DE2")

    label("loc_1D17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D30")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1DE2")

    label("loc_1D30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D4F")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1DE2")

    label("loc_1D4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D68")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1DE2")

    label("loc_1D68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D81")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1DE2")

    label("loc_1D81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D9B")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1DE2")

    label("loc_1D9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DB4")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1DE2")

    label("loc_1DB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DCE")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1DE2")

    label("loc_1DCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DE2")
    SetScenarioFlags(0x1, 1)

    label("loc_1DE2")

    ClearScenarioFlags(0x1, 2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DFA")
    SetScenarioFlags(0x1, 2)
    Jump("loc_1F58")

    label("loc_1DFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E13")
    SetScenarioFlags(0x1, 2)
    Jump("loc_1F58")

    label("loc_1E13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E2C")
    SetScenarioFlags(0x1, 2)
    Jump("loc_1F58")

    label("loc_1E2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E41")
    SetScenarioFlags(0x1, 2)
    Jump("loc_1F58")

    label("loc_1E41")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E5A")
    SetScenarioFlags(0x1, 2)
    Jump("loc_1F58")

    label("loc_1E5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E73")
    SetScenarioFlags(0x1, 2)
    Jump("loc_1F58")

    label("loc_1E73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E88")
    SetScenarioFlags(0x1, 2)
    Jump("loc_1F58")

    label("loc_1E88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EA1")
    SetScenarioFlags(0x1, 2)
    Jump("loc_1F58")

    label("loc_1EA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EBA")
    SetScenarioFlags(0x1, 2)
    Jump("loc_1F58")

    label("loc_1EBA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ECF")
    SetScenarioFlags(0x1, 2)
    Jump("loc_1F58")

    label("loc_1ECF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EE8")
    SetScenarioFlags(0x1, 2)
    Jump("loc_1F58")

    label("loc_1EE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F01")
    SetScenarioFlags(0x1, 2)
    Jump("loc_1F58")

    label("loc_1F01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F16")
    SetScenarioFlags(0x1, 2)
    Jump("loc_1F58")

    label("loc_1F16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F2F")
    SetScenarioFlags(0x1, 2)
    Jump("loc_1F58")

    label("loc_1F2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F44")
    SetScenarioFlags(0x1, 2)
    Jump("loc_1F58")

    label("loc_1F44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F58")
    SetScenarioFlags(0x1, 2)

    label("loc_1F58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1F99")

    #C0014
    ChrTalk(
        0x8,
        (
            "哎～您已经换上了这种外壳啊，\x01",
            "请选择其它的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2452")

    label("loc_1F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FE6")

    #C0015
    ChrTalk(
        0x8,
        (
            "咦～您的米拉好像不够呢。\x01",
            "这样是没办法更换的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2452")

    label("loc_1FE6")


    #C0016
    ChrTalk(
        0x8,
        (
            "明白啦，\x01",
            "请稍等一下哦～⊥\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(71, 0, 100, 0)
    Sleep(800)
    FadeToBright(1000, 0)
    OP_0D()

    #C0017
    ChrTalk(
        0x8,
        "好了，让您久等啦。\x02",
    )

    CloseMessageWindow()
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_20DB")

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "更换了罗伊德的艾尼格玛外壳。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_209E")
    ClearScenarioFlags(0xF0, 5)
    ClearScenarioFlags(0x2E, 0)
    Jump("loc_20D6")

    label("loc_209E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B8")
    SetScenarioFlags(0x2C, 0)

    label("loc_20B8")

    ClearScenarioFlags(0x2E, 0)
    SetScenarioFlags(0xF0, 5)
    Jump("loc_20D6")

    label("loc_20C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20D0")
    SetScenarioFlags(0x2C, 1)

    label("loc_20D0")

    SetScenarioFlags(0x2E, 0)
    ClearScenarioFlags(0xF0, 5)

    label("loc_20D6")

    Jump("loc_23A8")

    label("loc_20DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2183")

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "更换了艾莉的艾尼格玛外壳。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2134")
    ClearScenarioFlags(0x2E, 1)
    ClearScenarioFlags(0xF0, 6)
    Jump("loc_217E")

    label("loc_2134")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2162")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2157")
    SetScenarioFlags(0x2C, 2)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2157")

    ClearScenarioFlags(0x2E, 1)
    SetScenarioFlags(0xF0, 6)
    Jump("loc_217E")

    label("loc_2162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2178")
    SetScenarioFlags(0x2C, 3)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2178")

    SetScenarioFlags(0x2E, 1)
    ClearScenarioFlags(0xF0, 6)

    label("loc_217E")

    Jump("loc_23A8")

    label("loc_2183")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_222B")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "更换了缇欧的艾尼格玛外壳。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21DC")
    ClearScenarioFlags(0x2E, 2)
    ClearScenarioFlags(0xF0, 7)
    Jump("loc_2226")

    label("loc_21DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_220A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21FF")
    SetScenarioFlags(0x2C, 4)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_21FF")

    ClearScenarioFlags(0x2E, 2)
    SetScenarioFlags(0xF0, 7)
    Jump("loc_2226")

    label("loc_220A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2220")
    SetScenarioFlags(0x2C, 5)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2220")

    SetScenarioFlags(0x2E, 2)
    ClearScenarioFlags(0xF0, 7)

    label("loc_2226")

    Jump("loc_23A8")

    label("loc_222B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_22D3")

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "更换了兰迪的艾尼格玛外壳。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2284")
    ClearScenarioFlags(0x2E, 3)
    ClearScenarioFlags(0xF1, 0)
    Jump("loc_22CE")

    label("loc_2284")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A7")
    SetScenarioFlags(0x2C, 6)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_22A7")

    ClearScenarioFlags(0x2E, 3)
    SetScenarioFlags(0xF1, 0)
    Jump("loc_22CE")

    label("loc_22B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22C8")
    SetScenarioFlags(0x2C, 7)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_22C8")

    SetScenarioFlags(0x2E, 3)
    ClearScenarioFlags(0xF1, 0)

    label("loc_22CE")

    Jump("loc_23A8")

    label("loc_22D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2341")

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "更换了诺艾尔的艾尼格玛外壳。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2323")
    ClearScenarioFlags(0x2F, 0)
    Jump("loc_233C")

    label("loc_2323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2339")
    SetScenarioFlags(0x2D, 1)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2339")

    SetScenarioFlags(0x2F, 0)

    label("loc_233C")

    Jump("loc_23A8")

    label("loc_2341")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23A8")

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "更换了瓦吉的艾尼格玛外壳。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_238F")
    ClearScenarioFlags(0x2E, 4)
    Jump("loc_23A8")

    label("loc_238F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23A5")
    SetScenarioFlags(0x2D, 0)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_23A5")

    SetScenarioFlags(0x2E, 4)

    label("loc_23A8")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_241F")
    OP_E0(0x16, 0x0)

    label("loc_241F")


    #C0024
    ChrTalk(
        0x8,
        (
            "呵呵，期待您的\x01",
            "下次光临～\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2452")
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_2452")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_246B")

    label("loc_2461")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_246B")

    OP_CC(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_9C4")

    label("loc_247E")

    Return()

    # Function_5_9BA end

    def Function_6_247F(): pass

    label("Function_6_247F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2489")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C13")
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('白金', 0x4)"), scpexpr(EXPR_END)), "loc_24C9")
    MenuCmd(1, 0, "白金　　　　　　已购买")
    MenuCmd(3, 0, 0x0)
    Jump("loc_24E5")

    label("loc_24C9")

    MenuCmd(1, 0, "白金　　　　　　1000米拉")

    label("loc_24E5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('幻象', 0x4)"), scpexpr(EXPR_END)), "loc_2513")
    MenuCmd(1, 0, "幻象　　　　　　已购买")
    MenuCmd(3, 0, 0x1)
    Jump("loc_252F")

    label("loc_2513")

    MenuCmd(1, 0, "幻象　　　　　　5000米拉")

    label("loc_252F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_25D3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('神佑', 0x4)"), scpexpr(EXPR_END)), "loc_256B")
    MenuCmd(1, 0, "神佑　　　　　　已购买")
    MenuCmd(3, 0, 0x2)
    Jump("loc_2588")

    label("loc_256B")

    MenuCmd(1, 0, "神佑　　 　　　 20000米拉")

    label("loc_2588")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('王权', 0x4)"), scpexpr(EXPR_END)), "loc_25B6")
    MenuCmd(1, 0, "王权　　　　　　已购买")
    MenuCmd(3, 0, 0x3)
    Jump("loc_25D3")

    label("loc_25B6")

    MenuCmd(1, 0, "王权　　　　　  50000米拉")

    label("loc_25D3")

    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2610")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2610")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2610")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_262D")
    Sleep(1)
    Return()

    label("loc_262D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_266D")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis378.itp")
    Jump("loc_2728")

    label("loc_266D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26AD")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis379.itp")
    Jump("loc_2728")

    label("loc_26AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26ED")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis380.itp")
    Jump("loc_2728")

    label("loc_26ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2728")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis381.itp")

    label("loc_2728")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27B3")

    #A0025
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "空属性的核心回路。\x01",
            "※HP/ADF强化型·在消灭敌人时可回复镶嵌者的HP\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D1")

    label("loc_27B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2810")

    #A0026
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "幻属性的核心回路。\x01",
            "※EP/ATS强化型·在消灭敌人时可回复镶嵌者的EP\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D1")

    label("loc_2810")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2874")

    #A0027
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "地属性的核心回路。\x01",
            "※DEF/ADF强化型·满足特定条件时产生「完全防御」效果\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D1")

    label("loc_2874")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28D1")

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "水属性的核心回路。\x01",
            "※STR/ATS强化型·镶嵌者每次攻击都有几率获得耀晶片\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28D1")


    #A0029
    AnonymousTalk(
        0x8,
        "好的，要这个吗～？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【购买】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x3)
    OP_60(0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BF6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x4E20), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_29E7")

    #C0030
    ChrTalk(
        0x8,
        (
            "咦～您的米拉好像不够呢。\x01",
            "这样是没办法购买的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BE7")

    label("loc_29E7")


    #C0031
    ChrTalk(
        0x8,
        (
            "明白啦，\x01",
            "请稍等一下哦～⊥\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(71, 0, 100, 0)
    Sleep(800)
    FadeToBright(1000, 0)
    OP_0D()

    #C0032
    ChrTalk(
        0x8,
        "好了，让您久等啦。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AA0")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0033
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xE0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('白金', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2BC7")

    label("loc_2AA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B04")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0034
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xE1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('幻象', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2BC7")

    label("loc_2B04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B68")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0035
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xE5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('神佑', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x4E20), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2BC7")

    label("loc_2B68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BC7")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xE6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('王权', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_2BC7")


    #C0037
    ChrTalk(
        0x8,
        (
            "呵呵，期待您的\x01",
            "下次光临～\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2BE7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C00")

    label("loc_2BF6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C00")

    OP_CC(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_2489")

    label("loc_2C13")

    Return()

    # Function_6_247F end

    def Function_7_2C14(): pass

    label("Function_7_2C14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C94")

    #C0038
    ChrTalk(
        0x8,
        (
            "爸爸总是会来盯着我看，\x01",
            "感觉身上都快被他的眼光穿出个洞来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "不过，爸爸这么担心我，\x01",
            "还是很让人开心的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3510")

    label("loc_2C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2D4A")

    #C0040
    ChrTalk(
        0x8,
        (
            "戒严令颁布的时候，\x01",
            "店长让我赶快\x01",
            "回家……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "但温蒂前辈为了应对特殊情况，\x01",
            "主动留了下来，\x01",
            "所以我也没有走。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "虽然感觉有点\x01",
            "对不起爸爸，\x01",
            "不过他一定会理解我的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3510")

    label("loc_2D4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2DAE")

    #C0043
    ChrTalk(
        0x8,
        (
            "迪塔总统的演讲……\x01",
            "非常震撼人心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "我在听的时候，\x01",
            "都不由自主地屏住了呼吸。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3510")

    label("loc_2DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2E42")

    #C0045
    ChrTalk(
        0x8,
        (
            "在最近这一周，无论是上班还是回家，\x01",
            "我都会和爸爸一起走。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "在这种时候才想到和爸爸在一起，\x01",
            "未免有些过于现实，但总算可以安心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3510")

    label("loc_2E42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2E8F")

    #C0047
    ChrTalk(
        0x8,
        "真是很担心玛因兹的人啊。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "为什么会发生\x01",
            "这种事情呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3510")

    label("loc_2E8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2F83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F2C")

    #C0049
    ChrTalk(
        0x8,
        (
            "听说爸爸昨天竟然\x01",
            "偷偷参加了\x01",
            "我们店里的面试。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "他并不具备\x01",
            "技师所需的技能，\x01",
            "自然没有被录用……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        "呜呜，总觉得很丢脸呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2F7E")

    label("loc_2F2C")


    #C0052
    ChrTalk(
        0x8,
        (
            "听说爸爸偷偷参加了\x01",
            "我们店里的面试。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "呜呜，好丢脸，\x01",
            "真想找个地洞钻进去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F7E")

    Jump("loc_3510")

    label("loc_2F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2FB4")

    #C0054
    ChrTalk(
        0x8,
        (
            "列车竟然脱轨了，\x01",
            "好可怕啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3510")

    label("loc_2FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_301B")

    #C0055
    ChrTalk(
        0x8,
        "总觉得爸爸一副坐立不安的样子。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "虽然不清楚是怎么回事……\x01",
            "但总有种很不好的预感。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3510")

    label("loc_301B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3066")

    #C0057
    ChrTalk(
        0x8,
        (
            "我也知道爸爸\x01",
            "是在担心我……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        "但他的做法也太过火了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3510")

    label("loc_3066")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_309D")

    #C0059
    ChrTalk(
        0x8,
        (
            "居然对顾客说教……\x01",
            "实在是难以置信。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3510")

    label("loc_309D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_310C")

    #C0060
    ChrTalk(
        0x8,
        (
            "好啦，已经快到\x01",
            "关店时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "爸爸还是像以前一样，\x01",
            "躲在店里偷看我……\x01",
            "真希望他早点回去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3510")

    label("loc_310C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_318D")

    #C0062
    ChrTalk(
        0x8,
        (
            "我一直在用的那台\x01",
            "导力相机展示品\x01",
            "被温蒂前辈拿走了～\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "本来还想用它拍些\x01",
            "科洛蒂娅公主和阿尔伯特大公的照片呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3510")

    label("loc_318D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3319")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3217")

    #C0064
    ChrTalk(
        0x8,
        "各位，欢迎光临☆\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "本店开始销售\x01",
            "导力车部件\x01",
            "和车辆喷漆套装了。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "如果方便的话，请一定要\x01",
            "考虑购买哦～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 1)
    Jump("loc_3314")

    label("loc_3217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32B6")

    #C0067
    ChrTalk(
        0x8,
        (
            "话说回来，爸爸每天都要来，\x01",
            "还真是不嫌烦啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "不管怎么说他，他都坚持要来，\x01",
            "我最近已经不再管了……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "不过，太纵容他\x01",
            "似乎也不好呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3314")

    label("loc_32B6")


    #C0070
    ChrTalk(
        0x8,
        (
            "不管怎么说爸爸，他都坚持要来，\x01",
            "我最近已经不再管了……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "不过，太纵容他\x01",
            "似乎也不好呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3314")

    Jump("loc_3510")

    label("loc_3319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3494")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_341C")

    #C0072
    ChrTalk(
        0x8,
        (
            "最近这段时间，\x01",
            "店长对温蒂前辈的态度\x01",
            "有了很明显的变化。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "以前都是呼来喝去的，\x01",
            "但最近却突然变得很有礼貌……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "另外，在提到前辈的时候，\x01",
            "他还会很自然地\x01",
            "流露出敬重之情。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            "前辈一开始也觉得很不自在，\x01",
            "但现在已经完全习惯了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_348F")

    label("loc_341C")


    #C0076
    ChrTalk(
        0x8,
        (
            "最近这段时间，\x01",
            "店长对温蒂前辈的态度\x01",
            "有了很明显的变化。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "前辈一开始也觉得很不自在，\x01",
            "但现在已经完全习惯了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_348F")

    Jump("loc_3510")

    label("loc_3494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3510")

    #C0078
    ChrTalk(
        0x8,
        (
            "本柜台不仅提供贩卖、更换\x01",
            "艾尼格玛外壳的服务，\x01",
            "同时也销售核心回路。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "请不必客气，\x01",
            "有需要时就尽管吩咐我吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3510")

    Return()

    # Function_7_2C14 end

    def Function_8_3511(): pass

    label("Function_8_3511")

    OP_C9(0x1, 0x80)
    Call(0, 9)
    Return()

    # Function_8_3511 end

    def Function_9_351B(): pass

    label("Function_9_351B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3549")
    Call(0, 25)
    Return()

    label("loc_3549")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3707")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_369C")
    TalkBegin(0x9)

    #C0080
    ChrTalk(
        0x9,
        "哟，罗伊德。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "发生什么事了？\x01",
            "你怎么带着那么可爱的小朋友？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#00000F哦，我们正在带\x01",
            "熟人的孩子\x01",
            "在市里游览。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        "呵呵，是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "也就是说，这孩子\x01",
            "应该没来过这里吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x1A2, 500)
    Sleep(300)

    #C0085
    ChrTalk(
        0x9,
        (
            "小朋友，这家店\x01",
            "挺少见吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "你慢慢逛，\x01",
            "尽情享受一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x1A2,
        "好、好的……（享受？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DD, 0)
    TalkEnd(0x9)
    Jump("loc_3701")

    label("loc_369C")

    TalkBegin(0x9)

    #C0088
    ChrTalk(
        0x9,
        (
            "在市里游览吗？\x01",
            "好像很有趣呢，真羡慕。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "呵呵，话说回来，\x01",
            "你们还真是\x01",
            "什么工作都要做啊～\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_3701")

    Return()

    label("loc_3707")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3731")
    Call(0, 21)
    Return()

    label("loc_3731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37EB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BF(0x0, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_BF(0x1, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BF(0x4, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BF(0x8, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3788")
    Call(0, 22)
    Jump("loc_37E5")

    label("loc_3788")

    TalkBegin(0x9)

    #C0090
    ChrTalk(
        0x9,
        (
            "你们先给所有人的导力器\x01",
            "都镶嵌好核心回路吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        "其余的话，等到镶嵌完毕之后再说。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_37E5")

    Return()

    label("loc_37EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_380C")
    Call(0, 23)
    Return()

    label("loc_380C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_382C")
    SetScenarioFlags(0x0, 1)
    TalkBegin(0x9)
    Call(0, 12)
    TalkEnd(0x9)
    Return()

    label("loc_382C")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3839")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3926")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",            # 0
            "改造·合成\x01",      # 1
            "提问\x01",            # 2
            "放弃\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3894")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3894")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38B5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 10)
    Jump("loc_3921")

    label("loc_38B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3905")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_38D4")
    OP_AF(0xD)
    Jump("loc_38F6")

    label("loc_38D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_38E4")
    OP_AF(0xC)
    Jump("loc_38F6")

    label("loc_38E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_38F4")
    OP_AF(0xB)
    Jump("loc_38F6")

    label("loc_38F4")

    OP_AF(0xA)

    label("loc_38F6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3921")

    label("loc_3905")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3921")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 11)

    label("loc_3921")

    Jump("loc_3839")

    label("loc_3926")

    TalkEnd(0x9)
    Return()

    # Function_9_351B end

    def Function_10_392A(): pass

    label("Function_10_392A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B98")

    #C0092
    ChrTalk(
        0x9,
        (
            "罗伊德，还有各位，\x01",
            "拘捕总统的行动\x01",
            "真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "今后的情况\x01",
            "大概也会很艰难，\x01",
            "但我们都要加油啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#00004F嗯。\x02\x03",

            "#00000F不管发生什么事，也要在这里\x01",
            "做好自己的工作哦，温蒂。\x02\x03",

            "我们今后应该还会有\x01",
            "很多导力器方面的事情\x01",
            "需要你帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        "呵呵，明白了。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "对了，虽然这不是什么\x01",
            "贵重之物，\x01",
            "但请你们拿去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0097
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了３个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＥＰ填充剂Ⅲ', 3)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0098
    ChrTalk(
        0x101,
        (
            "#00000F谢谢，温蒂，\x01",
            "这些东西很有用啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        "呵呵，不客气。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "总之，如果你们\x01",
            "要去危险的地方，\x01",
            "一定要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "等事态平息下来以后，\x01",
            "我们叫上奥斯卡，\x01",
            "三个人一起去吃饭吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        "#00002F嗯，一定。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BB, 6)
    Jump("loc_3C0C")

    label("loc_3B98")


    #C0103
    ChrTalk(
        0x9,
        (
            "今后的情况大概\x01",
            "也会很艰难，\x01",
            "但我们都要加油啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "等事态平息下来以后，\x01",
            "我们叫上奥斯卡，\x01",
            "三个人一起去吃饭吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C0C")

    Jump("loc_4FAA")

    label("loc_3C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3CB1")

    #C0105
    ChrTalk(
        0x9,
        (
            "虽然已经听说你们平安无事了……\x01",
            "但亲眼见到之后，\x01",
            "才算彻底松了口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        (
            "如果有导力器方面的事情，\x01",
            "随时都可以和我说。\x01",
            "我一定会全力协助你们的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FAA")

    label("loc_3CB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3DFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D6F")

    #C0107
    ChrTalk(
        0x9,
        (
            "没想到事态会发展得\x01",
            "如此突然……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        "总之，看来今后的形势很严峻呢。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        (
            "罗伊德，如果有导力器方面的事情\x01",
            "需要帮忙，随时都可以来找我哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        "#00000F嗯，谢了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3DF6")

    label("loc_3D6F")


    #C0111
    ChrTalk(
        0x9,
        (
            "没想到事态会发展得\x01",
            "如此突然……\x01",
            "总之，看来今后的形势很严峻呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        (
            "罗伊德，如果有导力器方面的事情\x01",
            "需要帮忙，随时都可以来找我哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DF6")

    Jump("loc_4FAA")

    label("loc_3DFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_40BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E8E")

    #C0113
    ChrTalk(
        0x9,
        (
            "城市重建工作已经基本告一段落了，\x01",
            "但旧城区那边的进度\x01",
            "却还差得远呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "工作结束后，今天也\x01",
            "去基约姆师傅那里看看好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40B6")

    label("loc_3E8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F38")

    #C0115
    ChrTalk(
        0x9,
        (
            "选秀活动啊……\x01",
            "什么事情都应该经历一下嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "既然儿时好友专程来拜托，\x01",
            "我就答应好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "在活动开始之前，\x01",
            "我还要继续工作，\x01",
            "到时候再和我联系吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40B6")

    label("loc_3F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4050")

    #C0118
    ChrTalk(
        0x9,
        (
            "罗伊德，你们辛苦啦。\x01",
            "我也刚从活动会场\x01",
            "回来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "……话说回来，\x01",
            "那个叫洛依的主持人\x01",
            "可真是没礼貌啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x9,
        (
            "他竟然那样介绍，\x01",
            "说得我好像总用\x01",
            "扳手揍客人一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        "罗伊德，你也觉得他很过分吧？\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#00012F唔……嗯，是啊。\x01",
            "（其实好像没法完全否定他的话吧……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_40B6")

    label("loc_4050")


    #C0123
    ChrTalk(
        0x9,
        (
            "不过，选秀活动倒是很有意思，\x01",
            "多谢你们邀请我。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        (
            "既然已经回来了，\x01",
            "就要赶快重新投入到工作之中。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40B6")

    Jump("loc_4FAA")

    label("loc_40BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_41C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_416E")

    #C0125
    ChrTalk(
        0x9,
        (
            "玛因兹好像\x01",
            "出了大事呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x9,
        (
            "罗伊德，如果你们要去调查，\x01",
            "一定得多加小心哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        (
            "要是想调整艾尼格玛Ⅱ，\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        "#00000F嗯，谢啦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_41C0")

    label("loc_416E")


    #C0129
    ChrTalk(
        0x9,
        (
            "玛因兹好像\x01",
            "出了大事呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "罗伊德，如果你们要去调查，\x01",
            "一定得多加小心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41C0")

    Jump("loc_4FAA")

    label("loc_41C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_424C")

    #C0131
    ChrTalk(
        0x9,
        (
            "查珂的爸爸那爱操心的毛病\x01",
            "似乎已经无药可救了。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x9,
        (
            "虽然他做的并不是什么坏事，\x01",
            "但也希望他能\x01",
            "多考虑一下查珂的感受呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FAA")

    label("loc_424C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4294")

    #C0133
    ChrTalk(
        0x9,
        "听说导力列车脱轨了。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x9,
        "是不是机械出现了故障……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4FAA")

    label("loc_4294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_446B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43CF")

    #C0135
    ChrTalk(
        0x9,
        (
            "店长竟然说，为了表达对技师的敬意，\x01",
            "要把店内的装潢改造得土气一些，\x01",
            "以便让人找回旧工房的感觉……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "难得店里的经营状况很不错，\x01",
            "回头客也越来越多，如果突然改造成那样，\x01",
            "只会让客人们觉得莫名其妙吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x9,
        (
            "店长对技师的看法有了如此转变，\x01",
            "我自然感到很开心，\x01",
            "但还是希望他能用其它方式来表现。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4466")

    label("loc_43CF")


    #C0138
    ChrTalk(
        0x9,
        (
            "如今突然改变店里的装潢风格，\x01",
            "也只会让客人觉得莫名其妙吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x9,
        (
            "店长对技师的看法有了如此转变，\x01",
            "我自然感到很开心，\x01",
            "但还是希望他能用其它方式来表现。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4466")

    Jump("loc_4FAA")

    label("loc_446B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4609")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4565")

    #C0140
    ChrTalk(
        0x9,
        (
            "独立啊……初次听说的时候，\x01",
            "实在是吃了一惊，但认真听过之后，\x01",
            "便觉得市长的主张很有道理。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x9,
        (
            "要是再继续沉默下去，\x01",
            "两大国的军队就要在\x01",
            "边境大门驻留了……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x9,
        (
            "如果我们渴望得到真正的和平，\x01",
            "现在也许正是应该奋起疾呼的时候。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4604")

    label("loc_4565")


    #C0143
    ChrTalk(
        0x9,
        (
            "独立啊……初次听说的时候，\x01",
            "实在是吃了一惊，但认真听过之后，\x01",
            "便觉得市长的主张很有道理。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x9,
        (
            "如果我们渴望得到真正的和平，\x01",
            "现在也许正是应该奋起疾呼的时候。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4604")

    Jump("loc_4FAA")

    label("loc_4609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_466D")

    #C0145
    ChrTalk(
        0x9,
        (
            "唔～查珂的爸爸\x01",
            "可真厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x9,
        (
            "反正我觉得是那个在营业时间\x01",
            "搭讪店员的家伙不对。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FAA")

    label("loc_466D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_47F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_479B")

    #C0147
    ChrTalk(
        0x9,
        (
            "啊，罗伊德，是你们啊。\x01",
            "竟然在这种时候来，真是少见。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        (
            "#00000F嗯，我们刚刚接到了\x01",
            "一件紧急调查任务。\x02\x03",

            "是不是马上要关店了啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        (
            "没有啦，我们一般都会\x01",
            "到八点才关门呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#00000F是吗，那就好。\x01",
            "等我们有需要时，还要拜托你来调整哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x9,
        (
            "嗯，知道啦。\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_47F2")

    label("loc_479B")


    #C0152
    ChrTalk(
        0x9,
        (
            "只要是艾尼格玛Ⅱ方面的事情，\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        "我一定会迅速帮你们调整完美。\x02",
    )

    CloseMessageWindow()

    label("loc_47F2")

    Jump("loc_4FAA")

    label("loc_47F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4BAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B33")

    #C0154
    ChrTalk(
        0x9,
        (
            "呵呵呵，『埃尔赛尤号』。\x01",
            "虽然隔得有点远，\x01",
            "但还是顺利拍到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x9,
        (
            "我这就把照片显像出来，\x01",
            "你们要是有兴趣看，就留下等等吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0156
    ChrTalk(
        0x101,
        (
            "#00005F哎，既然如此，\x01",
            "那就给我们看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0157
    ChrTalk(
        0x102,
        "#00106F啊，这是……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x104,
        "#00306F真的是『埃尔赛尤号』吗？\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x109,
        (
            "#10112F只能勉强看到轮廓，\x01",
            "很难辨别呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x9,
        "哎～你们再看仔细些嘛。\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x9,
        (
            "这边是船首，这边是船尾，\x01",
            "明明拍得很清楚，非常容易辨别啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，听你这么一说，\x01",
            "好像确实如此呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        (
            "#00006F这就是所谓的机械爱好者吗……\x01",
            "温蒂着眼的地方总是与众不同。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x9,
        (
            "哎～是吗？\x01",
            "但我觉得这很普通啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x101,
        (
            "#00000F哈哈哈……\x01",
            "（她绝对不普通，\x01",
            "  至少这一点我可以确定。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 4)
    Jump("loc_4BA9")

    label("loc_4B33")


    #C0166
    ChrTalk(
        0x9,
        (
            "虽然隔得有点远，不过还是把\x01",
            "『埃尔赛尤号』完美拍下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x9,
        (
            "呵呵呵，要不要把这张照片\x01",
            "放大之后贴在房间的墙上呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BA9")

    Jump("loc_4FAA")

    label("loc_4BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4DF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D71")

    #C0168
    ChrTalk(
        0x9,
        (
            "通商会议啊……\x01",
            "利贝尔的代表一定会乘\x01",
            "那艘『埃尔赛尤号』来吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        (
            "#00000F『埃尔赛尤号』……\x01",
            "哦，是利贝尔王国的高速巡洋舰吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x9,
        (
            "没错，它集蔡斯中央工房的精华技术于一身，\x01",
            "简直可以称之为飞船中的\x01",
            "最高杰作！\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x9,
        (
            "如果到时它从上空飞过，\x01",
            "就算停下工作，我也要给它拍照！\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#00006F可以理解你的心情……\x01",
            "但还是要适可而止哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x9,
        "才不。（干脆）\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        "#00011F呃……\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x104,
        (
            "#00309F哈哈，不愧是心直口快的温蒂小姐，\x01",
            "回答得好干脆啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 3)
    Jump("loc_4DED")

    label("loc_4D71")


    #C0176
    ChrTalk(
        0x9,
        (
            "通商会议啊……利贝尔的代表一定会乘\x01",
            "那艘『埃尔赛尤号』来吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x9,
        (
            "如果到时它从上空飞过，\x01",
            "就算停下工作，我也要给它拍照！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DED")

    Jump("loc_4FAA")

    label("loc_4DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4E71")

    #C0178
    ChrTalk(
        0x9,
        (
            "店长比我想象中\x01",
            "还爱学习呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x9,
        (
            "大概因为他原来是设计师吧？\x01",
            "该怎么说呢，那种类似于求知欲的\x01",
            "想法相当强烈呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FAA")

    label("loc_4E71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4FAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 7)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F3A")

    #C0180
    ChrTalk(
        0x9,
        (
            "总之，你们就在镶嵌着\x01",
            "核心回路的状态下去战斗吧，\x01",
            "只要战斗一次就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x9,
        (
            "战斗结束之后，\x01",
            "别忘了来我这里报告。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x9,
        (
            "否则的话，这次的讲习\x01",
            "就不算正式结束哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FAA")

    label("loc_4F3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4FAA")

    #C0183
    ChrTalk(
        0x9,
        (
            "呵呵，大家今后\x01",
            "也要多加疼爱\x01",
            "核心回路哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x9,
        (
            "你们对核心回路\x01",
            "倾注的爱越多，\x01",
            "得到的回报就越大。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FAA")

    Return()

    # Function_10_392A end

    def Function_11_4FAB(): pass

    label("Function_11_4FAB")


    #C0185
    ChrTalk(
        0x9,
        (
            "ＯＫ。\x01",
            "想问哪方面的问题呢？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4FD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AD1")
    FadeToDark(300, 0, 100)

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "关于战术导力器\x01",        # 0
            "关于回路\x01",              # 1
            "关于结晶孔的开封\x01",      # 2
            "关于结晶孔的强化\x01",      # 3
            "关于导力魔法\x01",          # 4
            "关于艾尼格玛Ⅱ\x01",        # 5
            "关于核心回路\x01",          # 6
            "放弃\x01",                  # 7
        )
    )

    MenuEnd(0x3)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_508A")
    FadeToBright(300, 0)
    OP_5A()

    label("loc_508A")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_50BE"),
        (1, "loc_523F"),
        (2, "loc_5364"),
        (3, "loc_545A"),
        (4, "loc_55A5"),
        (5, "loc_571D"),
        (6, "loc_58A9"),
        (SWITCH_DEFAULT, "loc_5ABD"),
    )


    label("loc_50BE")


    #C0186
    ChrTalk(
        0x9,
        (
            "所谓的『战术导力器』，\x01",
            "是一种专门用于个人战斗的\x01",
            "便携式小型导力器。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x9,
        (
            "它不仅能强化使用者的能力，\x01",
            "还可以用来发动导力魔法。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x9,
        (
            "一般情况下，我们就把它\x01",
            "简称为『导力器』啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x9,
        (
            "为了配合每个人的具体情况与使用习惯，\x01",
            "我们会对导力器进行完美的微调，\x01",
            "所以其构造会因人而异。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x9,
        (
            "像限定属性的结晶孔啦，连接结晶孔的\x01",
            "结晶链形状啦，都会有所不同。\x01",
            "各位可以自行比较一下每个人的导力器。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ACC")

    label("loc_523F")


    #C0191
    ChrTalk(
        0x9,
        (
            "所谓回路，就是将耀晶片进行精炼后\x01",
            "所制造出的战术导力器专用的『结晶回路』。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x9,
        (
            "如果携带着足够数量的耀晶片，\x01",
            "就可以在我们这里合成回路。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x9,
        (
            "每种回路都有各自的特性效果，\x01",
            "同一条结晶链上的回路属性值达到一定数值后，\x01",
            "就可以使用特定的导力魔法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x9,
        "如果你们攒够了耀晶片，可以多试试哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5ACC")

    label("loc_5364")


    #C0195
    ChrTalk(
        0x9,
        (
            "导力器的结晶孔\x01",
            "在最初时几乎都是未开封的状态。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x9,
        (
            "所以，如果想镶嵌回路，\x01",
            "首先需要开封结晶孔。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x9,
        (
            "多开封一些结晶孔，\x01",
            "不仅可以镶嵌更多的回路，\x01",
            "同时也能提升最大ＥＰ值。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x9,
        (
            "虽然在开封时需要使用一些耀晶片，\x01",
            "但早点开封绝对是有益无害的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ACC")

    label("loc_545A")


    #C0199
    ChrTalk(
        0x9,
        (
            "在回路之中，还存在着\x01",
            "一部分『高级回路』。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x9,
        (
            "这些回路的性能极强，\x01",
            "因此无法镶嵌在普通的结晶孔内。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x9,
        (
            "如果想镶嵌高级回路，\x01",
            "就需要强化结晶孔本身。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x9,
        (
            "和开封相同，强化结晶孔也需要消耗耀晶片，\x01",
            "不过这也会使最大ＥＰ值提升。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x9,
        (
            "虽然没必要急着强化结晶孔，\x01",
            "但如果想增加导力器的性能，\x01",
            "强化结晶孔可以算是一个不可缺少的要素。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ACC")

    label("loc_55A5")


    #C0204
    ChrTalk(
        0x9,
        (
            "利用战术导力器发动的魔法\x01",
            "统称为导力魔法。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x9,
        "我们一般都将它简称为『魔法』。\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x9,
        (
            "而可发动的魔法，是由\x01",
            "『每条结晶链上所镶嵌的回路属性总值』\x01",
            "所决定的。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x9,
        (
            "也就是说，结晶链上镶嵌回路\x01",
            "的属性值越高，\x01",
            "可以使用的魔法就越多。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x9,
        (
            "顺便一说，如果想发动一些\x01",
            "非常强力的魔法，属性值的组合\x01",
            "也是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x9,
        (
            "至于这方面的详细情报，\x01",
            "你们可以查看调查手册中\x01",
            "收录的魔法一览表。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ACC")

    label("loc_571D")


    #C0210
    ChrTalk(
        0x9,
        (
            "继承了艾尼格玛的通讯功能，\x01",
            "并进行了大胆改造的后继机型——\x01",
            "即『艾尼格玛Ⅱ』。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x9,
        (
            "和上一代机型相比，艾尼格玛Ⅱ\x01",
            "唯一的大改变就是可以镶嵌一种\x01",
            "名为『核心回路』的特殊回路。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x9,
        (
            "虽然并没有太大变化……\x01",
            "但这次的版本升级\x01",
            "使基础构造发生了改变。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x9,
        (
            "所以，由于兼容性方面的问题，\x01",
            "旧型号艾尼格玛所使用的回路\x01",
            "全都不能镶嵌在艾尼格玛Ⅱ上。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x9,
        (
            "也就是说，如想使用艾尼格玛Ⅱ，\x01",
            "必须装载新规格的回路。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ACC")

    label("loc_58A9")


    #C0215
    ChrTalk(
        0x9,
        (
            "所谓的核心回路，\x01",
            "就是镶嵌在艾尼格玛Ⅱ\x01",
            "中心的特殊结晶回路。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x9,
        (
            "核心回路与以往那些回路的决定性差异，\x01",
            "就在于自身拥有『成长』的特性。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x9,
        (
            "只要将核心回路镶嵌在导力器中，\x01",
            "核心回路就会随着战斗的累积而提升等级，\x01",
            "并发挥出更加强力的效果。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x9,
        (
            "强化使用者的能力、\x01",
            "回路的特殊效果，以及属性值……\x01",
            "主要的成长要素就是这三点。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x9,
        (
            "无论是哪种核心回路，\x01",
            "只要能将其提升到最高等级，\x01",
            "就会进化为非常强大的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x9,
        (
            "想把核心回路提升到最高等级，\x01",
            "恐怕需要消耗相当长的时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x9,
        (
            "不要三心二意，坚持使用自己\x01",
            "最喜欢的核心回路应该是最佳方案。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ACC")

    label("loc_5ABD")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5ACC")

    label("loc_5ACC")

    Jump("loc_4FD6")

    label("loc_5AD1")

    Sleep(150)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_4FAB end

    def Function_12_5ADF(): pass

    label("Function_12_5ADF")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    def lambda_5AF0():
        TurnDirection(0x8, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5AF0)

    def lambda_5AFD():
        TurnDirection(0x9, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5AFD)
    TurnDirection(0xA, 0x0, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5B49")

    #C0222
    ChrTalk(
        0x8,
        "啊，你们是……\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x9,
        (
            "罗伊德……\x01",
            "你没事啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BAA")

    label("loc_5B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5B72")

    #C0224
    ChrTalk(
        0x9,
        (
            "罗伊德……\x01",
            "你没事啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BAA")

    label("loc_5B72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5BAA")

    #C0225
    ChrTalk(
        0xA,
        "啊，你们是……\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x9,
        (
            "罗伊德……\x01",
            "你没事啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BAA")


    #C0227
    ChrTalk(
        0x101,
        "#00000F嗯，还好。\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x9,
        (
            "我已经听你们的警察同事\x01",
            "说了事情的大致状况。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x9,
        (
            "你们应该能设法改善\x01",
            "目前这种情况吧？\x01",
            "全都拜托大家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x8,
        (
            "那个……我们店也会\x01",
            "尽力为大家提供支援的～\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xA,
        (
            "各位行动的时候\x01",
            "一定要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        "#00000F嗯，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0x9, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    SetScenarioFlags(0x1BB, 5)
    Return()

    # Function_12_5ADF end

    def Function_13_5CBC(): pass

    label("Function_13_5CBC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5CCD")
    Jump("loc_6A60")

    label("loc_5CCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5D4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CEB")
    SetScenarioFlags(0x0, 3)
    Call(0, 12)
    Jump("loc_5D47")

    label("loc_5CEB")


    #C0233
    ChrTalk(
        0xFE,
        (
            "话说回来，目前这种情况……\x01",
            "真是已经混乱到了极点。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔今后\x01",
            "到底会怎么样呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D47")

    Jump("loc_6A60")

    label("loc_5D4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5E7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E08")

    #C0235
    ChrTalk(
        0xFE,
        (
            "『克洛斯贝尔独立国』……\x01",
            "这样一来，就彻底\x01",
            "与两大国为敌了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "……我们店今后也没法销售\x01",
            "莱恩福尔特公司和\x01",
            "乌尔努公司的产品了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        "唉，一想到这里就头疼。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E76")

    label("loc_5E08")


    #C0238
    ChrTalk(
        0xFE,
        (
            "竟然下了这么大的决心，\x01",
            "不惜停止经济活动也要坚持独立……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "早知道事情会变成这样，\x01",
            "我就不赞成独立了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E76")

    Jump("loc_6A60")

    label("loc_5E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5EF7")

    #C0240
    ChrTalk(
        0xFE,
        (
            "调查独立意向的居民投票活动\x01",
            "再过三天就要到来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "到时候，大家轮流值班看店，\x01",
            "我们全体店员都会去投票。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A60")

    label("loc_5EF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5FDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F8C")

    #C0242
    ChrTalk(
        0xFE,
        (
            "唔，占领事件吗，\x01",
            "事态真是相当严重啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "据说有可能是帝国\x01",
            "在暗中穿针引线……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        "无论如何，希望事情能早日解决。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5FD9")

    label("loc_5F8C")


    #C0245
    ChrTalk(
        0xFE,
        (
            "据说有可能是帝国\x01",
            "在暗中穿针引线……\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        "无论如何，希望事情能早日解决。\x02",
    )

    CloseMessageWindow()

    label("loc_5FD9")

    Jump("loc_6A60")

    label("loc_5FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6101")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_608D")

    #C0247
    ChrTalk(
        0xFE,
        (
            "昨天，查珂的父亲\x01",
            "参加了我们店的面试。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "他说因为担心女儿，\x01",
            "所以想在这里工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "但很遗憾，他并不符合\x01",
            "我们的录用标准，\x01",
            "只好婉言谢绝了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_60FC")

    label("loc_608D")


    #C0250
    ChrTalk(
        0xFE,
        (
            "查珂的父亲因为担心女儿，\x01",
            "所以想在这里工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "但很遗憾，他并不符合\x01",
            "我们的录用标准，\x01",
            "只好婉言谢绝了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60FC")

    Jump("loc_6A60")

    label("loc_6101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_614C")

    #C0252
    ChrTalk(
        0xFE,
        (
            "我听客人说，\x01",
            "列车脱轨了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        "希望大家都平安无事……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A60")

    label("loc_614C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6260")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6205")

    #C0254
    ChrTalk(
        0xFE,
        (
            "我本想把店内的装潢改得土气一些，\x01",
            "为此还特意去征求\x01",
            "温蒂和查珂的意见……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "但还没等我把话说完，\x01",
            "就被她们驳回了。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "唔～本来还以为\x01",
            "是个不错的想法呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_625B")

    label("loc_6205")


    #C0257
    ChrTalk(
        0xFE,
        (
            "唔～本来还以为\x01",
            "是个不错的想法呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "哎呀呀，既然她们那么反对，\x01",
            "那就没办法了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_625B")

    Jump("loc_6A60")

    label("loc_6260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_63DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_633E")

    #C0259
    ChrTalk(
        0xFE,
        (
            "基约姆先生曾在这家店里工作，\x01",
            "我们在经营方针上存在严重的意见冲突，\x01",
            "最后就分路而行了……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "如今回想起来，总觉得\x01",
            "有些对不住他呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "直到最近我才明白，\x01",
            "在这个行业中，\x01",
            "技师永远是最重要的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_63D6")

    label("loc_633E")


    #C0262
    ChrTalk(
        0xFE,
        (
            "说起来，温蒂以前说过，\x01",
            "她更喜欢旧工房的\x01",
            "那种气氛……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "对了，既然如此，\x01",
            "不如把店里的内部装潢改造一下，\x01",
            "改成过去的『原点』工房那种土气的式样吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63D6")

    Jump("loc_6A60")

    label("loc_63DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6477")

    #C0264
    ChrTalk(
        0xFE,
        "正式会议就要在今天召开了。\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "这是一次重要的国际会议，它将会决定\x01",
            "克洛斯贝尔，乃至整个大陆的经济发展趋势……\x01",
            "真是不得不关注会议内容啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A60")

    label("loc_6477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_64DC")

    #C0266
    ChrTalk(
        0xFE,
        "晚上好，欢迎光临『原点』。\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "我们再过一段时间才会关店，\x01",
            "请不必着急，慢慢看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A60")

    label("loc_64DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_663E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65C8")

    #C0268
    ChrTalk(
        0xFE,
        (
            "呼，温蒂真是\x01",
            "让人头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "竟然丢下工作不管，\x01",
            "还把店里的导力相机拿出去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "……如果是以前的我，\x01",
            "肯定会这样唠叨个没完。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "但仔细想想，她的行为\x01",
            "并没对业务造成太大干扰，\x01",
            "这点小事也不必计较了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6639")

    label("loc_65C8")


    #C0272
    ChrTalk(
        0xFE,
        (
            "而且她用展示相机拍照，\x01",
            "还能给它的机能起到宣传作用，\x01",
            "反而是件好事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "嗯，待会我也去看看\x01",
            "她拍的照片吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6639")

    Jump("loc_6A60")

    label("loc_663E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_67B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6713")

    #C0274
    ChrTalk(
        0xFE,
        "客人，有什么能为您服务的吗？\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "如果您想挑选导力吸尘器，\x01",
            "我向您推荐乌尔努公司\x01",
            "生产的最新款。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "它有三个特性各异的可拆卸吸头配件，\x01",
            "可以清洁一切环境，\x01",
            "是一款非常方便的优质产品。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_67AB")

    label("loc_6713")


    #C0277
    ChrTalk(
        0xFE,
        (
            "如果您想挑选导力吸尘器，\x01",
            "我向您推荐乌尔努公司\x01",
            "生产的最新款。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "它有三个特性各异的可拆卸吸头配件，\x01",
            "可以清洁一切环境，\x01",
            "是一款非常方便的优质产品。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67AB")

    Jump("loc_6A60")

    label("loc_67B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_693E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68D3")

    #C0279
    ChrTalk(
        0xFE,
        (
            "很惭愧，我以前\x01",
            "对导力器几乎\x01",
            "没有任何了解。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "但随着本店的经营渐渐步入正轨，\x01",
            "我才意识到这样下去是不行的。\x01",
            "虽然有些晚，但我已经开始学习了……\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "哎呀，导力技师真是了不起啊，\x01",
            "比如我们店的温蒂。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xFE,
        (
            "我也尝试学习了技术知识，\x01",
            "但实在是太复杂了，我完全搞不懂。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6939")

    label("loc_68D3")


    #C0283
    ChrTalk(
        0xFE,
        (
            "哎呀，导力技师真是了不起啊，\x01",
            "比如我们店的温蒂。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        (
            "像我光是学习一些\x01",
            "浅显的知识就已经很吃力了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6939")

    Jump("loc_6A60")

    label("loc_693E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6A60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69ED")

    #C0285
    ChrTalk(
        0xFE,
        (
            "欢迎光临\x01",
            "导力商店『原点』。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "本店不仅销售最尖端的导力制品，\x01",
            "还提供细致周到的\x01",
            "区域性售后服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xFE,
        (
            "如果您有什么问题想要咨询，\x01",
            "请尽管提出。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6A60")

    label("loc_69ED")


    #C0288
    ChrTalk(
        0xFE,
        (
            "本店不仅销售最尖端的导力制品，\x01",
            "还提供细致周到的\x01",
            "区域性售后服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        (
            "如果您有什么问题想要咨询，\x01",
            "请尽管提出。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A60")

    TalkEnd(0xFE)
    Return()

    # Function_13_5CBC end

    def Function_14_6A64(): pass

    label("Function_14_6A64")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6AF7")

    #C0290
    ChrTalk(
        0xFE,
        (
            "说实话，我根本没有购物的心情……\x01",
            "但待在家里也平静不下来，所以就来这里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "唉……真希望事态早日平息，\x01",
            "恢复平常的生活啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7301")

    label("loc_6AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6B05")
    Jump("loc_7301")

    label("loc_6B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6B82")

    #C0292
    ChrTalk(
        0xFE,
        (
            "迪塔总统的演说\x01",
            "真是震撼。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "虽然今后恐怕要面对各种困难，\x01",
            "但我已经坚定了决心，\x01",
            "一定会和大家一起努力的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7301")

    label("loc_6B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6C1D")

    #C0294
    ChrTalk(
        0xFE,
        (
            "虽然我平时不太关注政治，\x01",
            "但独立问题自然另当别论。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        (
            "通过最近的这些事件，\x01",
            "我考虑了很多，得出的结论就是，\x01",
            "克洛斯贝尔果然还是应该独立。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7301")

    label("loc_6C1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6C72")

    #C0296
    ChrTalk(
        0xFE,
        "居然会发生占领事件，真可怕啊……\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "要是我也能帮上忙\x01",
            "就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7301")

    label("loc_6C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6D7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D05")

    #C0298
    ChrTalk(
        0xFE,
        (
            "听说独立之后，就不用\x01",
            "向两大国交纳税金了。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "那样一来，克洛斯贝尔的经济\x01",
            "就能进一步发展啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        "这可是很重要的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6D78")

    label("loc_6D05")


    #C0301
    ChrTalk(
        0xFE,
        (
            "听说独立之后，就不用\x01",
            "向两大国交纳税金了。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "那样一来，克洛斯贝尔的经济\x01",
            "就能进一步发展啦。\x01",
            "这可是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D78")

    Jump("loc_7301")

    label("loc_6D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6DA7")

    #C0303
    ChrTalk(
        0xFE,
        "哎呀，外面怎么这么吵？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7301")

    label("loc_6DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6EDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E65")

    #C0304
    ChrTalk(
        0xFE,
        (
            "莱恩福尔特公司生产的产品\x01",
            "大多都以大容量和\x01",
            "高输出为卖点。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "而乌尔努公司的大部分产品则以\x01",
            "功能丰富、价格适中为特点。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xFE,
        "呵呵呵，这也正是两个国家的特色吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6ED9")

    label("loc_6E65")


    #C0307
    ChrTalk(
        0xFE,
        (
            "莱恩福尔特公司重视大容量\x01",
            "和高输出，乌尔努公司则更\x01",
            "重视便利性和经济性。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xFE,
        "呵呵呵，这也正是两个国家的特色吧。\x02",
    )

    CloseMessageWindow()

    label("loc_6ED9")

    Jump("loc_7301")

    label("loc_6EDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6F6C")

    #C0309
    ChrTalk(
        0xFE,
        (
            "我最近刚刚知道，\x01",
            "原来最不容易坏的是\x01",
            "蔡斯中央工房的产品呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xFE,
        (
            "虽然他们的产品价格往往比\x01",
            "其它公司的高，\x01",
            "但似乎物有所值啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7301")

    label("loc_6F6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6FDC")

    #C0311
    ChrTalk(
        0xFE,
        (
            "不同品牌的产品，即使看上去相差无几，\x01",
            "具体特点也会各不相同。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "呵呵呵，我也渐渐\x01",
            "明白了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7301")

    label("loc_6FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_709D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_704E")

    #C0313
    ChrTalk(
        0xFE,
        "哎呀，已经这么晚了啊。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xFE,
        (
            "呵呵呵，我得赶快回家，\x01",
            "用我那性能超群的导力炉做饭呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7098")

    label("loc_704E")


    #C0315
    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "导力炉确实非常方便呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        (
            "虽然价格很贵，\x01",
            "但真是买对了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7098")

    Jump("loc_7301")

    label("loc_709D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7196")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_713B")

    #C0317
    ChrTalk(
        0xFE,
        (
            "通商会议？\x01",
            "唔～老实说，那和我没什么\x01",
            "直接关系，所以没有兴趣呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "好啦，别说那个了，看看这个。\x01",
            "你不觉得这个新产品很可爱吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7191")

    label("loc_713B")


    #C0319
    ChrTalk(
        0xFE,
        (
            "要是把装在这里的螺丝\x01",
            "当作眼睛的话，\x01",
            "看，就像张脸一样吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        "呵呵呵，真可爱啊～\x02",
    )

    CloseMessageWindow()

    label("loc_7191")

    Jump("loc_7301")

    label("loc_7196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_722D")

    #C0321
    ChrTalk(
        0xFE,
        (
            "在最近这几个月，这里的店长\x01",
            "突然变成了万事通。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        (
            "有时候根本没问，他就主动介绍起来，\x01",
            "让人觉得有点烦……\x01",
            "不过可以感觉到他的热情呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7301")

    label("loc_722D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7290")

    #C0323
    ChrTalk(
        0xFE,
        "越来越懂得导力产品的魅力了～\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        (
            "本来并没打算买东西，\x01",
            "但不由自主地就想进来看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7301")

    label("loc_7290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7301")

    #C0325
    ChrTalk(
        0xFE,
        (
            "哎呀呀，上次买的吸尘器\x01",
            "这么快就出新一代产品了。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        (
            "真是的～要是早点告诉我的话，\x01",
            "当时就先不买了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7301")

    TalkEnd(0xFE)
    Return()

    # Function_14_6A64 end

    def Function_15_7305(): pass

    label("Function_15_7305")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7364")

    #C0327
    ChrTalk(
        0xFE,
        (
            "哦哦，查珂……\x01",
            "真的是我的女儿查珂啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        (
            "爸爸一直都\x01",
            "非常非常担心你……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CC2")

    label("loc_7364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7372")
    Jump("loc_7CC2")

    label("loc_7372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_740C")

    #C0329
    ChrTalk(
        0xFE,
        (
            "虽然号称『国防军』，\x01",
            "但真的有能力保护我们吗……\x01",
            "老实说，我很不安。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "……不过，没关系的。\x01",
            "不管发生什么事，\x01",
            "我也一定会保护好查珂的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CC2")

    label("loc_740C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7493")

    #C0331
    ChrTalk(
        0xFE,
        (
            "因为得到了查珂的允许，\x01",
            "所以今天早上我也陪她一起来上班。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        (
            "查珂，不管要付出\x01",
            "什么样的代价，\x01",
            "爸爸也一定会保护你的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CC2")

    label("loc_7493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7515")

    #C0333
    ChrTalk(
        0xFE,
        (
            "矿山镇居然被\x01",
            "武装集团占领了……\x01",
            "真、真是局势动荡啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "总、总之，\x01",
            "今天不管查珂说什么，\x01",
            "我也要跟她一起回家。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CC2")

    label("loc_7515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7592")

    #C0335
    ChrTalk(
        0xFE,
        (
            "唔～店长真是个\x01",
            "不好说话的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        (
            "不过也无所谓。\x01",
            "既然如此，只要像以前一样，\x01",
            "以客人的身份来这里就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CC2")

    label("loc_7592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_75DC")

    #C0337
    ChrTalk(
        0xFE,
        (
            "脱轨事故吗……\x01",
            "虽然过去也偶尔会发生，\x01",
            "但还真是少见呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CC2")

    label("loc_75DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7618")

    #C0338
    ChrTalk(
        0xFE,
        (
            "我今天参加了\x01",
            "这家店的面试。\x01",
            "（紧张）……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CC2")

    label("loc_7618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7728")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76EB")

    #C0339
    ChrTalk(
        0xFE,
        (
            "不管女儿怎么说，\x01",
            "我就是非常担心她。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "唔，干脆在这里\x01",
            "应聘一份技师工作吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xFE,
        (
            "不过，我的专业技能\x01",
            "是设计。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "虽然会点简单的维修，但更复杂的就……\x01",
            "不知道店长会不会雇用我。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7723")

    label("loc_76EB")


    #C0343
    ChrTalk(
        0xFE,
        (
            "唔～我的专业技能\x01",
            "是设计。\x01",
            "不知道店长会不会雇用我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7723")

    Jump("loc_7CC2")

    label("loc_7728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_77A7")

    #C0344
    ChrTalk(
        0xFE,
        (
            "昨天，有个人趁着\x01",
            "工作要结束的时候接近查珂，\x01",
            "我忍不住提醒了他一句……\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        (
            "结果这件事让查珂\x01",
            "发了很大的火呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CC2")

    label("loc_77A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_78D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7871")

    #C0346
    ChrTalk(
        0xFE,
        (
            "虽然还没到关店时间，\x01",
            "但也就是转眼间的事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "走夜路是很危险的，\x01",
            "我真想陪查珂一起回家……\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "但如果关心得那么过火，\x01",
            "肯定会被查珂讨厌的。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xFE,
        "唔，到底该怎么办呢……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_78D2")

    label("loc_7871")


    #C0350
    ChrTalk(
        0xFE,
        (
            "要是偷偷摸摸地跟在她后面，\x01",
            "我也许会被误认成可疑人物吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        "今天也老老实实地回去好了……\x02",
    )

    CloseMessageWindow()

    label("loc_78D2")

    Jump("loc_7CC2")

    label("loc_78D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_796D")

    #C0352
    ChrTalk(
        0xFE,
        (
            "查珂那个前辈是叫温蒂吧？\x01",
            "她一听到飞艇引擎的声音，\x01",
            "就急匆匆地从店里冲出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "然后过了好一会\x01",
            "都没有回来，\x01",
            "这到底是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CC2")

    label("loc_796D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_79DC")

    #C0354
    ChrTalk(
        0xFE,
        (
            "嗯，虽然都说看自己的孩子怎么都好，\x01",
            "但查珂确实就像是一朵鲜花。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        "真担心那些害虫接近她啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7CC2")

    label("loc_79DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7B71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AFF")

    #C0356
    ChrTalk(
        0xFE,
        (
            "对于导力产品的外观设计，\x01",
            "各个制造商都会有\x01",
            "各自不同的特色……\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "单就没有多余的装饰和累赘，\x01",
            "具有功能美这一点来说，\x01",
            "蔡斯中央工房和爱普斯泰恩的产品可谓出类拔萃呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        (
            "顺带一提，莱恩福尔特公司的产品\x01",
            "大多数都很华丽，而乌尔努公司的\x01",
            "大部分产品则倾向于大众风格。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7B6C")

    label("loc_7AFF")


    #C0359
    ChrTalk(
        0xFE,
        (
            "我认为导力制品\x01",
            "并不需要任何多余的装饰。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        (
            "一想到要为那些没用的装饰\x01",
            "而花费更多的米拉，\x01",
            "我就非常生气。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B6C")

    Jump("loc_7CC2")

    label("loc_7B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7CC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C54")

    #C0361
    ChrTalk(
        0xFE,
        (
            "我直到去年都还在\x01",
            "从事导力产品设计师\x01",
            "这个工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "不过，女儿现在已经工作，\x01",
            "家计也有了着落，\x01",
            "所以我就干脆退休了。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xFE,
        (
            "虽然对工作还有一些留恋，\x01",
            "但如今可以用更多的时间来陪伴家人，\x01",
            "这让我很开心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7CC2")

    label("loc_7C54")


    #C0364
    ChrTalk(
        0xFE,
        (
            "我今天也是来\x01",
            "查看女儿查珂的\x01",
            "工作情况的……\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        (
            "嗯，她似乎一直都\x01",
            "非常努力。\x01",
            "我这个当爸爸的真是很感慨呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CC2")

    TalkEnd(0xFE)
    Return()

    # Function_15_7305 end

    def Function_16_7CC6(): pass

    label("Function_16_7CC6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7D60")

    #C0366
    ChrTalk(
        0xFE,
        (
            "不管是导力车，还是导力终端，\x01",
            "都是平民难以企及的商品呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "虽然价格在慢慢降低……\x01",
            "但不知最终能否下降到\x01",
            "一般家庭都能承受的程度呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DD0")

    label("loc_7D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7DD0")

    #C0368
    ChrTalk(
        0xFE,
        (
            "哇，这就是传说中的\x01",
            "笔记本型导力终端啊。\x01",
            "价格是……\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        (
            "………唔，好长一串零。\x01",
            "终究还是买不起呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DD0")

    TalkEnd(0xFE)
    Return()

    # Function_16_7CC6 end

    def Function_17_7DD4(): pass

    label("Function_17_7DD4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7E92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E57")

    #C0370
    ChrTalk(
        0xFE,
        (
            "我实在是忘不掉查珂，\x01",
            "所以又来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        "……不过，她老爸还在啊。\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        "唉，只能死心而归了吗……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7E8D")

    label("loc_7E57")


    #C0373
    ChrTalk(
        0xFE,
        "……查珂的老爸还在呢。\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        "唉，只能死心而归了。\x02",
    )

    CloseMessageWindow()

    label("loc_7E8D")

    Jump("loc_816E")

    label("loc_7E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_7F4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F03")

    #C0375
    ChrTalk(
        0xFE,
        (
            "马上就要到关店时间了。\x01",
            "虽然店里还有\x01",
            "不少客人……\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        "…………要不要试着搭话呢？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7F49")

    label("loc_7F03")


    #C0377
    ChrTalk(
        0xFE,
        (
            "鼓起勇气，\x01",
            "向查珂搭话……\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        (
            "呼，还是冷静下来，\x01",
            "再考虑一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F49")

    Jump("loc_816E")

    label("loc_7F4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_806C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8028")

    #C0379
    ChrTalk(
        0xFE,
        (
            "虽然我并没打算买东西……\x01",
            "但因为想见销售柜台的那个女孩，\x01",
            "所以又到店里来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xFE,
        (
            "对了，我特意看了看\x01",
            "她的名牌，原来她的名字\x01",
            "叫查珂。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "真是个可爱的名字呢，\x01",
            "跟她那天真烂漫的外表很相配！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8067")

    label("loc_8028")


    #C0382
    ChrTalk(
        0xFE,
        "揭幕式和我无关！\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        (
            "我只要能看到那个女孩的笑脸\x01",
            "就够了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8067")

    Jump("loc_816E")

    label("loc_806C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_816E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_811A")

    #C0384
    ChrTalk(
        0xFE,
        "唔～这家店真棒呢。\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "我指的并不是导力器之类的东西，\x01",
            "而是这里的店员很可爱。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "呵呵，那位技师很不错，\x01",
            "销售柜台的女孩\x01",
            "更是我最喜欢的类型⊥\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_816E")

    label("loc_811A")


    #C0387
    ChrTalk(
        0xFE,
        (
            "唔～这还真是\x01",
            "旅途中的意外惊喜啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xFE,
        (
            "要是拜托她让我拍张照，\x01",
            "她会不会答应呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_816E")

    TalkEnd(0xFE)
    Return()

    # Function_17_7DD4 end

    def Function_18_8172(): pass

    label("Function_18_8172")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_81D9")

    #C0389
    ChrTalk(
        0xFE,
        (
            "唔，好像发生了\x01",
            "什么不太平的事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        (
            "要不要取消旅行的行程安排，\x01",
            "尽快回去呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8391")

    label("loc_81D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8255")

    #C0391
    ChrTalk(
        0xFE,
        (
            "听说昨天发生了事故的\x01",
            "导力列车已经在今天早上\x01",
            "完全修复了。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        (
            "嗯，看来负责处理\x01",
            "事故的警备队\x01",
            "相当优秀呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8391")

    label("loc_8255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_829D")

    #C0393
    ChrTalk(
        0xFE,
        (
            "唔，刚才的声音\x01",
            "应该是警笛吧。\x01",
            "真不想听到这个声音……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8391")

    label("loc_829D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_831E")

    #C0394
    ChrTalk(
        0xFE,
        (
            "哎呀呀，\x01",
            "导力产品可真是美妙的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        (
            "就算是同样功能的产品，\x01",
            "不同品牌的外形也各不相同，\x01",
            "真是很有意思呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8391")

    label("loc_831E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8391")

    #C0396
    ChrTalk(
        0xFE,
        (
            "唔，这家店的商品很齐全，\x01",
            "各国厂商的导力产品都有呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xFE,
        (
            "不愧是大陆数一数二的贸易中心\x01",
            "克洛斯贝尔啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8391")

    TalkEnd(0xFE)
    Return()

    # Function_18_8172 end

    def Function_19_8395(): pass

    label("Function_19_8395")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_844B")

    #C0398
    ChrTalk(
        0xFE,
        "这种情况到底是怎么回事呢……\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xFE,
        (
            "总之，如果回到家之后\x01",
            "连顿像样的饭都没有的话，\x01",
            "那还不如留在这里……\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "……唉，也没什么事情可做，\x01",
            "就来调整一下充气机吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_84A0")

    label("loc_844B")


    #C0401
    ChrTalk(
        0xFE,
        "这种情况到底是怎么回事呢……\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xFE,
        (
            "反正也没什么事情可做，\x01",
            "就来调整一下充气机吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84A0")

    TalkEnd(0xFE)
    Return()

    # Function_19_8395 end

    def Function_20_84A4(): pass

    label("Function_20_84A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_851F")

    #C0403
    ChrTalk(
        0xFE,
        "感光回路、感光回路……\x02",
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        (
            "哦，最新款的容量增加了。\x01",
            "这样的话，只要有两、三个应该就够了吧？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 6)
    Jump("loc_8588")

    label("loc_851F")


    #C0405
    ChrTalk(
        0xFE,
        (
            "为了明天的揭幕式，\x01",
            "我正在采购备用的\x01",
            "感光回路。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "如果在关键时刻把感光回路用完了，\x01",
            "可就太糟糕了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8588")

    TalkEnd(0xFE)
    Return()

    # Function_20_84A4 end

    def Function_21_858C(): pass

    label("Function_21_858C")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x9, 0xFF)
    OP_68(6960, 1500, -2230, 0)
    MoveCamera(51, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 6850, 0, -790, 90)
    SetChrPos(0x102, 6820, 0, -2020, 90)
    SetChrPos(0x109, 5740, 0, -580, 90)
    SetChrPos(0x105, 5730, 0, -2460, 90)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0407
    ChrTalk(
        0x9,
        "#11P罗伊德，等你好久啦。\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x9,
        (
            "#11P大家也来了啊……\x01",
            "啊，有一半是生面孔呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x101,
        (
            "#6P#00000F嗯，我们这个阵容\x01",
            "刚开始工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x109,
        (
            "#6P#10100F初次见面，\x01",
            "我叫诺艾尔·希卡。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x105,
        (
            "#6P#10304F我是瓦吉·赫米斯菲亚，你好。\x02\x03",

            "#10300F说起来，你好像是\x01",
            "罗伊德的儿时好友吧？\x02\x03",

            "如果可以，下次一定要\x01",
            "给我讲讲罗伊德\x01",
            "小时候的趣事哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0412
    ChrTalk(
        0x9,
        (
            "#11P呵呵，好啊～！\x01",
            "你是想抓住罗伊德的把柄吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0413
    ChrTalk(
        0x101,
        (
            "#6P#00006F你、你们在说什么啊……\x02\x03",

            "#00000F好了，\x01",
            "我们赶快进入正题吧。\x02\x03",

            "你不是要给我们上一堂\x01",
            "艾尼格玛Ⅱ的讲习课吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x9,
        "#11P啊，对啊，都给忘了。\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x9,
        "#11P咳，那就马上开始吧……\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x9,
        (
            "#11P既然你们已经开始\x01",
            "使用艾尼格玛Ⅱ了，\x01",
            "所以我想你们应该知道……\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x9,
        (
            "#11P爱普斯泰恩财团这次\x01",
            "推出的新版本产品，\x01",
            "与旧版产品的唯一且最大的不同点……\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x9,
        (
            "#11P就是中心部分的\x01",
            "结晶孔构造。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x9,
        (
            "#11P镶嵌在中心的\x01",
            "特殊回路名为\x01",
            "『核心回路』。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x101,
        (
            "#6P#00000F哦，就是这个刻有花纹的\x01",
            "回路吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x9,
        "#11P没错，就是那个球状回路。\x02",
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x9,
        (
            "#11P这个核心回路与以往的回路\x01",
            "有一个决定性的不同点，\x01",
            "那就是它能够『成长』。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x9,
        (
            "#11P把它镶嵌在导力器中，并在此状态下\x01",
            "不断进行战斗，就可以让它得到磨练，\x01",
            "从而实现阶段性的强化。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x109,
        (
            "#6P#10100F该怎么说呢……\x01",
            "有点神秘的感觉啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x102,
        (
            "#6P#00100F是啊，简直就像\x01",
            "拥有生命一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x105,
        (
            "#6P#10302F呵呵，\x01",
            "那么你接下来要给我们\x01",
            "讲解它的原理等内容吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x9,
        (
            "#11P啊，不是的。\x01",
            "很遗憾，我并不是研究者，\x01",
            "所以并不了解那些。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x9,
        (
            "#11P严格来说，与其称之为成长，\x01",
            "倒不如说是把它\x01",
            "隐藏的力量引发出来……\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x9,
        (
            "#11P先不说这些了，\x01",
            "我想让各位学习的是\x01",
            "艾尼格玛Ⅱ的使用方法。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x9,
        "#11P不管怎么说，理论终究不如实践。\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x9,
        (
            "#11P请大家把这些\x01",
            "收下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0432
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "艾莉把",
            scpstr(SCPSTR_CODE_ITEM, 0xDE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('妖精', 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0433
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "瓦吉把",
            scpstr(SCPSTR_CODE_ITEM, 0xDF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('利爪', 1)

    #C0434
    ChrTalk(
        0x102,
        "#6P#00105F这就是核心回路……\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x105,
        (
            "#6P#10303F嗯，与普通的回路相比，\x01",
            "感觉确实完全不同呢。\x02\x03",

            "#10300F不过，真的可以收下吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x9,
        (
            "#11P是的，没什么可不可以的，\x01",
            "这本来就是警察总部\x01",
            "发放给各位的物品。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x9,
        (
            "#11P另外，核心回路\x01",
            "不仅无法在普通的工房内合成，\x01",
            "而且也无法量产。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x9,
        (
            "#11P我们店里的少量存货\x01",
            "都是从财团调来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x9,
        (
            "#11P基本来说，每种核心回路\x01",
            "只有一个可供出售，\x01",
            "因此请各位一定要倍加珍惜。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x109,
        (
            "#6P#10100F原来如此……\x01",
            "这是那么稀有的东西啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x101,
        (
            "#6P#00005F温蒂，我已经懂了，\x01",
            "但说到实践，到底要做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x9,
        (
            "#11P这个嘛，在此之前，\x01",
            "请你们先给所有人的导力器\x01",
            "镶嵌好核心回路吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x9,
        (
            "#11P怎么分配都无所谓，\x01",
            "四人全都镶嵌完毕之后，\x01",
            "和我说一声就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x9,
        (
            "#11P对了，核心回路虽然\x01",
            "也有自身的属性，\x01",
            "但结晶孔是没有限制的。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x9,
        (
            "#11P也就是说，所有的核心回路\x01",
            "都可以镶嵌在任何人的导力器中。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x102,
        "#6P#00100F原来如此，这还真是方便呢。\x02",
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x105,
        (
            "#6P#10300F呵呵，那我们\x01",
            "就赶快镶嵌吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0448
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【关于艾尼格玛Ⅱ的讲习】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 6620, 0, -1810, 90)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x132, 6)
    OP_29(0x65, 0x1, 0x0)
    OP_1B(0x0, 0x0, 0x1A)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_21_858C end

    def Function_22_90B7(): pass

    label("Function_22_90B7")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x9, 0xFF)
    OP_68(6960, 1500, -2230, 0)
    MoveCamera(51, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 6850, 0, -790, 90)
    SetChrPos(0x102, 6820, 0, -2020, 90)
    SetChrPos(0x109, 5740, 0, -580, 90)
    SetChrPos(0x105, 5730, 0, -2460, 90)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_0D()

    #C0449
    ChrTalk(
        0x9,
        (
            "#11P好，看来你们\x01",
            "都已镶嵌好\x01",
            "核心回路了。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x101,
        "#6P#00000F然后呢，接下来该怎么做？\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x9,
        (
            "#11P呵呵，简单得很。\x01",
            "接下来，我想让你们实际确认\x01",
            "一下核心回路的效果。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x102,
        (
            "#6P#00105F那是指……\x01",
            "通过战斗来确认吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x9,
        "#11P没错，就是这个意思。\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x9,
        (
            "#11P虽然罗伊德和诺艾尔小姐\x01",
            "已经体验过了，\x01",
            "但还是麻烦你们再辛苦一下啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x109,
        "#6P#10100F明白。\x02",
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x101,
        (
            "#6P#00005F那有没有什么条件？\x01",
            "比如战斗的地点、次数之类的。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x9,
        (
            "#11P不，没有呢。\x01",
            "地点和对手完全交给你们来决定。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x9,
        (
            "#11P战斗的次数也只需一次即可，\x01",
            "但不能逃跑，要认真战斗到最后哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x105,
        "#6P#10300F呵呵，那当然。\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x102,
        "#6P#00100F罗伊德，地点怎么决定呢？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_93FC")

    #C0461
    ChrTalk(
        0x101,
        (
            "#6P#00003F这个嘛，我们暂时\x01",
            "没有到市外的计划……\x02\x03",

            "#00000F就去和伊梅尔达馆\x01",
            "中的魔兽战斗吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_945A")

    label("loc_93FC")


    #C0462
    ChrTalk(
        0x101,
        (
            "#6P#00003F说起来，伊梅尔达馆中\x01",
            "还有通缉魔兽呢。\x02\x03",

            "#00000F去消灭它的时候，\x01",
            "可以顺便一试。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_945A")


    #C0463
    ChrTalk(
        0x109,
        (
            "#6P#10100F确实，这样也就\x01",
            "省事多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x9,
        (
            "#11P呵呵，看来你们\x01",
            "已经决定好地点了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x9,
        (
            "#11P那就把这个回路\x01",
            "也拿去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0466
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x74),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('精神１', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0467
    ChrTalk(
        0x101,
        "#6P#00005F这是……\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x9,
        "#11P嗯，这也是警察总部发放的物品。\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x9,
        (
            "#11P只要把这个回路镶嵌在普通结晶孔里，\x01",
            "就可以使用艾尼格玛Ⅱ\x01",
            "专用的新魔法『情报解析』了。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x9,
        (
            "#11P掌控情报的人\x01",
            "就可以掌握整个战局。\x01",
            "请一定要在战斗中灵活使用。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x101,
        (
            "#6P#00000F嗯，我明白了。\x02\x03",

            "#00003F（缇欧不在……\x01",
            "  暂时要靠魔法来收集\x01",
            "  魔兽的情报了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x9,
        (
            "#11P好，\x01",
            "一路小心啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x9,
        (
            "#11P如果想改造导力器\x01",
            "或合成回路，\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0474
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※与温蒂对话，\x01",
            "　选择『改造·合成』，\x01",
            "　即可合成新回路，或对战术\x01",
            "　导力器的结晶孔进行开封·强化。\x02\x03",

            "※合成新回路之后，只要镶嵌在导力器内，\x01",
            "　就可以使用各种各样的魔法了。\x02\x03",

            "※通过开封·强化结晶孔，\x01",
            "　能够增加可镶嵌的回路数量，\x01",
            "　同时还能增加最大ＥＰ。\x02\x03",

            "※另外，要想使用这些功能，\x01",
            "  需要花费被称为『耀晶片』的七耀石碎片。\x01",
            "  （耀晶片主要通过打倒魔兽获得。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x132, 7)
    OP_29(0x65, 0x1, 0x1)
    OP_1B(0x0, 0xFF, 0xFFFF)
    SetChrPos(0x0, 6620, 0, -1810, 90)
    OP_69(0xFF, 0x0)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_22_90B7 end

    def Function_23_987F(): pass

    label("Function_23_987F")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x9, 0xFF)
    OP_68(6960, 1500, -2230, 0)
    MoveCamera(51, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 6850, 0, -790, 90)
    SetChrPos(0x102, 6820, 0, -2020, 90)
    SetChrPos(0x109, 5740, 0, -580, 90)
    SetChrPos(0x105, 5730, 0, -2460, 90)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_0D()

    #C0475
    ChrTalk(
        0x9,
        (
            "#11P啊，辛苦了。\x01",
            "看来你们已经在\x01",
            "战斗中应用过了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x9,
        (
            "#11P艾莉小姐，瓦吉先生，\x01",
            "实际使用核心回路的\x01",
            "感受如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x102,
        "#6P#00100F嗯，该怎么说呢，真是吃了一惊。\x02",
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x105,
        (
            "#6P#10304F是啊，区区一枚回路，\x01",
            "竟能发挥出\x01",
            "那么惊人的效果。\x02\x03",

            "#10300F老实说，完全没想到会这么厉害。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B18")

    #C0479
    ChrTalk(
        0x9,
        "#11P呵呵，反响不错呢～\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x9,
        (
            "#11P对了，让它成长到最终阶段后，\x01",
            "将可以使用某种特殊功能……\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x9,
        (
            "#11P不过，这个就让你们\x01",
            "到时候亲身体会吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x109,
        (
            "#6P#10105F哎～还有\x01",
            "隐藏惊喜吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x101,
        (
            "#6P#00009F哈哈，真期待啊。\x02\x03",

            "#00000F那么，讲习至此\x01",
            "就算是结束了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BC4")

    label("loc_9B18")


    #C0484
    ChrTalk(
        0x9,
        "#11P呵呵，反响不错呢～\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x9,
        (
            "#11P真想转告给爱普斯泰恩\x01",
            "财团的开发人员。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x101,
        (
            "#6P#00009F哈哈，他们要是听到夸奖，\x01",
            "一定会很开心吧。\x02\x03",

            "#00000F那么，讲习至此\x01",
            "就算是结束了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BC4")


    #C0487
    ChrTalk(
        0x9,
        (
            "#11P嗯，我会把讲习结果\x01",
            "报告给警察总部。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x9,
        (
            "#11P最后，如果还有什么\x01",
            "关于导力器的问题，\x01",
            "我都可以回答。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x9,
        "#11P还有什么想问的问题吗？\x02",
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x101,
        "#6P#00000F这个嘛……\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9C73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A7D8")

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "关于战术导力器\x01",        # 0
            "关于回路\x01",              # 1
            "关于结晶孔的开封\x01",      # 2
            "关于结晶孔的强化\x01",      # 3
            "关于导力魔法\x01",          # 4
            "关于艾尼格玛Ⅱ\x01",        # 5
            "关于核心回路\x01",          # 6
            "放弃\x01",                  # 7
        )
    )

    MenuEnd(0x3)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_9D2D"),
        (1, "loc_9ECA"),
        (2, "loc_9FFF"),
        (3, "loc_A105"),
        (4, "loc_A264"),
        (5, "loc_A3F4"),
        (6, "loc_A594"),
        (SWITCH_DEFAULT, "loc_A7C4"),
    )


    label("loc_9D2D")


    #C0491
    ChrTalk(
        0x9,
        (
            "#11P#11P所谓的『战术导力器』，\x01",
            "是一种专门用于个人战斗的\x01",
            "便携式小型导力器。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x9,
        (
            "#11P#11P它不仅能强化使用者的能力，\x01",
            "还可以用来发动导力魔法。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x9,
        (
            "#11P一般情况下，我们就把它\x01",
            "简称为『导力器』啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x9,
        (
            "#11P为了配合每个人的具体情况与使用习惯，\x01",
            "我们会对导力器进行完美的微调，\x01",
            "所以其构造会因人而异。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x9,
        (
            "#11P像限定属性的结晶孔啦，连接结晶孔的\x01",
            "结晶链形状啦，都会有所不同。\x01",
            "各位可以自行比较一下每个人的导力器。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7D3")

    label("loc_9ECA")


    #C0496
    ChrTalk(
        0x9,
        (
            "#11P所谓回路，就是将耀晶片进行精炼后\x01",
            "所制造出的战术导力器专用的『结晶回路』。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x9,
        (
            "#11P如果携带着足够数量的耀晶片，\x01",
            "就可以在我们这里合成回路。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x9,
        (
            "#11P每种回路都有各自的特性效果，\x01",
            "同一条结晶链上的回路属性值达到一定数值后，\x01",
            "就可以使用特定的导力魔法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x9,
        "#11P如果你们攒够了耀晶片，可以多试试哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A7D3")

    label("loc_9FFF")


    #C0500
    ChrTalk(
        0x9,
        (
            "#11P导力器的结晶孔\x01",
            "在最初时几乎都是未开封的状态。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x9,
        (
            "#11P所以，如果想镶嵌回路，\x01",
            "首先需要开封结晶孔。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x9,
        (
            "#11P多开封一些结晶孔，\x01",
            "不仅可以镶嵌更多的回路，\x01",
            "同时也能提升最大ＥＰ值。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x9,
        (
            "#11P虽然在开封时需要使用一些耀晶片，\x01",
            "但早点开封绝对是有益无害的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7D3")

    label("loc_A105")


    #C0504
    ChrTalk(
        0x9,
        (
            "#11P在回路之中，还存在着\x01",
            "一部分『高级回路』。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x9,
        (
            "#11P这些回路的性能极强，\x01",
            "因此无法镶嵌在普通的结晶孔内。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x9,
        (
            "#11P如果想镶嵌高级回路，\x01",
            "就需要强化结晶孔本身。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x9,
        (
            "#11P和开封相同，强化结晶孔也需要消耗耀晶片，\x01",
            "不过这也会使最大ＥＰ值提升。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x9,
        (
            "#11P虽然没必要急着强化结晶孔，\x01",
            "但如果想增加导力器的性能，\x01",
            "强化结晶孔可以算是一个不可缺少的要素。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7D3")

    label("loc_A264")


    #C0509
    ChrTalk(
        0x9,
        (
            "#11P利用战术导力器发动的魔法\x01",
            "统称为导力魔法。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x9,
        "#11P我们一般都将它简称为『魔法』。\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x9,
        (
            "#11P而可发动的魔法，是由\x01",
            "『每条结晶链上所镶嵌的回路属性总值』\x01",
            "所决定的。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x9,
        (
            "#11P也就是说，结晶链上镶嵌回路\x01",
            "的属性值越高，\x01",
            "可以使用的魔法就越多。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x9,
        (
            "#11P顺便一说，如果想发动一些\x01",
            "非常强力的魔法，属性值的组合\x01",
            "也是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x9,
        (
            "#11P至于这方面的详细情报，\x01",
            "你们可以查看调查手册中\x01",
            "收录的魔法一览表。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7D3")

    label("loc_A3F4")


    #C0515
    ChrTalk(
        0x9,
        (
            "#11P继承了艾尼格玛的通讯功能，\x01",
            "并进行了大胆改造的后继机型——\x01",
            "即『艾尼格玛Ⅱ』。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x9,
        (
            "#11P和上一代机型相比，艾尼格玛Ⅱ\x01",
            "唯一的大改变就是可以镶嵌一种\x01",
            "名为『核心回路』的特殊回路。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x9,
        (
            "#11P虽然并没有太大变化……\x01",
            "但这次的版本升级\x01",
            "使基础构造发生了改变。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x9,
        (
            "#11P所以，由于兼容性方面的问题，\x01",
            "旧型号艾尼格玛所使用的回路\x01",
            "全都不能镶嵌在艾尼格玛Ⅱ上。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x9,
        (
            "#11P也就是说，如想使用艾尼格玛Ⅱ，\x01",
            "必须装载新规格的回路。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7D3")

    label("loc_A594")


    #C0520
    ChrTalk(
        0x9,
        (
            "#11P所谓的核心回路，\x01",
            "就是镶嵌在艾尼格玛Ⅱ\x01",
            "中心的特殊结晶回路。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x9,
        (
            "#11P核心回路与以往那些回路的决定性差异，\x01",
            "就在于自身拥有『成长』的特性。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x9,
        (
            "#11P只要将核心回路镶嵌在导力器中，\x01",
            "核心回路就会随着战斗的累积而提升等级，\x01",
            "并发挥出更加强力的效果。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x9,
        (
            "#11P强化使用者的能力、\x01",
            "回路的特殊效果，以及属性值……\x01",
            "主要的成长要素就是这三点。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x9,
        (
            "#11P无论是哪种核心回路，\x01",
            "只要能将其提升到最高等级，\x01",
            "就会进化为非常强大的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x9,
        (
            "#11P想把核心回路提升到最高等级，\x01",
            "恐怕需要消耗相当长的时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x9,
        (
            "#11P不要三心二意，坚持使用自己\x01",
            "最喜欢的核心回路应该是最佳方案。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7D3")

    label("loc_A7C4")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A7D3")

    label("loc_A7D3")

    Jump("loc_9C73")

    label("loc_A7D8")


    #C0527
    ChrTalk(
        0x101,
        (
            "#6P#00004F……没有别的问题了。\x02\x03",

            "#00000F谢谢，温蒂，\x01",
            "我们今天真是学到了不少。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x9,
        "#11P呵呵，那就好。\x02",
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x9,
        (
            "#11P还有这个，\x01",
            "用于艾尼格玛Ⅱ的新型回路。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x9,
        (
            "#11P这是我为了庆祝你们重新开始工作，\x01",
            "送给特别任务支援科的礼物。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0531
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('鹰目', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0532
    ChrTalk(
        0x101,
        (
            "#6P#00002F谢了，温蒂，\x01",
            "我们一定会多加利用的。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x102,
        "#6P#00102F真是谢谢了。\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x9,
        "#11P呵呵，不客气。\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x9,
        (
            "#11P总之，要是还有\x01",
            "什么不清楚的事情，\x01",
            "随时都可以来问我。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x9,
        (
            "#11P旁边的柜台\x01",
            "今后也会开放\x01",
            "各种各样的新服务……\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x9,
        (
            "#11P今后就请\x01",
            "各位多多关照\x01",
            "导力商店『原点』了。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x105,
        "#6P#10302F呵呵，彼此彼此。\x02",
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x109,
        (
            "#6P#10102F今天真是\x01",
            "多谢了。\x02",
        )
    )

    CloseMessageWindow()
    Sound(9, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0540
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【关于艾尼格玛Ⅱ的讲习】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_29(0x65, 0x1, 0x3)
    OP_29(0x65, 0x4, 0x10)
    OP_29(0xA1, 0x1, 0x2)
    SetChrPos(0x0, 6620, 0, -1810, 90)
    OP_69(0xFF, 0x0)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_23_987F end

    def Function_24_AAE1(): pass

    label("Function_24_AAE1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-6460, 1500, 2290, 0)
    MoveCamera(62, 32, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24150, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_AC5B")
    SetChrPos(0x1A2, -7900, 0, 2940, 90)
    SetChrPos(0x102, -7900, 0, 2090, 90)
    SetChrPos(0x101, -7900, 0, 3210, 90)
    SetChrPos(0x104, -7900, 0, 1790, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(100, 0, 100, 0)
    OP_0D()

    def lambda_ABAC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_ABAC)

    def lambda_ABBD():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_ABBD)

    def lambda_ABD2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_ABD2)

    def lambda_ABE3():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ABE3)
    OP_68(-4830, 1500, 1680, 3000)
    Sleep(700)

    def lambda_AC0C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AC0C)

    def lambda_AC1D():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AC1D)
    Sleep(100)

    def lambda_AC35():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AC35)

    def lambda_AC46():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AC46)
    Jump("loc_AED6")

    label("loc_AC5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_AD9B")
    SetChrPos(0x1A2, -7900, 0, 2940, 90)
    SetChrPos(0x102, -7900, 0, 2090, 90)
    SetChrPos(0x101, -7900, 0, 3210, 90)
    SetChrPos(0x109, -7900, 0, 1790, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(100, 0, 100, 0)
    OP_0D()

    def lambda_ACEC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_ACEC)

    def lambda_ACFD():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_ACFD)

    def lambda_AD12():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AD12)

    def lambda_AD23():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AD23)
    OP_68(-4830, 1500, 1680, 3000)
    Sleep(700)

    def lambda_AD4C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AD4C)

    def lambda_AD5D():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD5D)
    Sleep(100)

    def lambda_AD75():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AD75)

    def lambda_AD86():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AD86)
    Jump("loc_AED6")

    label("loc_AD9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_AED6")
    SetChrPos(0x1A2, -7900, 0, 2940, 90)
    SetChrPos(0x102, -7900, 0, 2090, 90)
    SetChrPos(0x101, -7900, 0, 3210, 90)
    SetChrPos(0x105, -7900, 0, 1790, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(100, 0, 100, 0)
    OP_0D()

    def lambda_AE2C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_AE2C)

    def lambda_AE3D():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_AE3D)

    def lambda_AE52():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AE52)

    def lambda_AE63():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AE63)
    OP_68(-4830, 1500, 1680, 3000)
    Sleep(700)

    def lambda_AE8C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AE8C)

    def lambda_AE9D():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AE9D)
    Sleep(100)

    def lambda_AEB5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_AEB5)

    def lambda_AEC6():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AEC6)

    label("loc_AED6")

    OP_6F(0x1)
    WaitChrThread(0x101, 1)

    #C0541
    ChrTalk(
        0x1A2,
        (
            "这里就是\x01",
            "很多杂志都报道过的\x01",
            "导力商店啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x1A2,
        (
            "无论是室内装潢，还是摆放的商品，\x01",
            "全都有种最尖端的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x1A2,
        (
            "就算是共和国，恐怕也没有\x01",
            "这么大规模的店……\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，能够像这样\x01",
            "汇集各国的产品，\x01",
            "恐怕也只有克洛斯贝尔了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x101,
        (
            "#00000F说到最尖端，\x01",
            "这里连导力网络终端\x01",
            "都有哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0546
    ChrTalk(
        0x1A2,
        "导力……网络？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_B043")

    def lambda_B026():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B026)
    Sleep(50)

    def lambda_B036():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B036)
    Jump("loc_B094")

    label("loc_B043")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_B06E")

    def lambda_B051():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B051)
    Sleep(50)

    def lambda_B061():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B061)
    Jump("loc_B094")

    label("loc_B06E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_B094")

    def lambda_B07C():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B07C)
    Sleep(50)

    def lambda_B08C():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B08C)

    label("loc_B094")


    #C0547
    ChrTalk(
        0x101,
        (
            "#6P#00000F嗯，简单来说，就是将以往的\x01",
            "通讯器进一步发展而诞生的技术。\x02\x03",

            "#00004F这项计划是以一个\x01",
            "名为爱普斯泰恩财团的组织\x01",
            "为中心而推进的……\x02\x03",

            "#00000F使用终端的时候，不光是声音，\x01",
            "连文字和图像等信息\x01",
            "都可以互相传送。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x1A2,
        (
            "哎、哎……\x01",
            "这样都可以啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_93(0x1A2, 0x5A, 0x1F4)
    OP_64(0x1A2)

    #C0549
    ChrTalk(
        0x1A2,
        (
            "哼、哼……我才\x01",
            "没有吃惊呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x1A2,
        (
            "不要因为显摆了些许知识\x01",
            "就得意忘形啊！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_B2B9")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0551
    ChrTalk(
        0x101,
        (
            "#6P#00006F这……我并没有\x01",
            "得意忘形……\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x104,
        "#12P#00300F哈，真是个不坦率的小鬼啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B41E")

    label("loc_B2B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_B373")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0553
    ChrTalk(
        0x101,
        (
            "#6P#00006F这……我并没有\x01",
            "得意忘形……\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x109,
        (
            "#12P#10100F该说是不坦率吗，\x01",
            "他好像相当不服气呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B41E")

    label("loc_B373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_B41E")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0555
    ChrTalk(
        0x101,
        (
            "#6P#00006F这……我并没有\x01",
            "得意忘形……\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x105,
        (
            "#12P#10300F呵呵，他好像\x01",
            "非常不服气呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B41E")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x154, 5)
    OP_29(0x73, 0x1, 0xA)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -4800, 0, 2530, 90)
    EventEnd(0x5)
    Return()

    # Function_24_AAE1 end

    def Function_25_B44A(): pass

    label("Function_25_B44A")

    EventBegin(0x0)
    Fade(500)
    OP_68(7160, 1500, -1600, 0)
    MoveCamera(45, 29, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 6940, 0, -1330, 90)
    SetChrPos(0x102, 6850, 0, -320, 90)
    SetChrPos(0x103, 6730, 0, -2450, 90)
    SetChrPos(0x104, 5780, 0, -1390, 90)
    SetChrPos(0x105, 5400, 0, -2610, 90)
    SetChrPos(0x109, 5680, 0, -160, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    OP_0D()

    #C0557
    ChrTalk(
        0x9,
        "咦，罗伊德，有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x105,
        (
            "#10300F（选秀活动中的『技师』……\x01",
            "  让她来担当应该很不错吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x101,
        (
            "#00003F（唔……她应该对这种事情\x01",
            "  没什么兴趣……\x01",
            "  但都已经来了，还是问问看吧。）\x02\x03",

            "#00000F……温蒂，打扰你一下。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0560
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

    #C0561
    ChrTalk(
        0x9,
        "职业女性选秀……？那是什么？\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x9,
        (
            "是新型导力器的\x01",
            "零件还是什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0563
    ChrTalk(
        0x104,
        (
            "#00306F不、不不不，\x01",
            "完全不是啦，温蒂小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x103,
        (
            "#00203F毕竟是纯粹的技师……\x01",
            "不通世事也不奇怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x9,
        (
            "啊哈哈，开个玩笑啦，\x01",
            "这种事情我还是懂的。\x01",
            "简单来说，就是美少女选拔赛吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x9,
        (
            "嗯，听起来好像很有趣……\x01",
            "我可以参加哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x102,
        "#00105F真、真的吗？\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x109,
        (
            "#10102F呵呵，有点意外呢，\x01",
            "没想到你能同意。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x9,
        "什么事情都应该经历一下嘛。\x02",
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x9,
        (
            "既然儿时好友专程来拜托，\x01",
            "我就答应好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x9,
        (
            "在活动开始之前，\x01",
            "我还要继续工作，\x01",
            "到时候再和我联系吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x101,
        (
            "#00000F嗯，我知道了。\x01",
            "谢啦，温蒂。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B93B")

    #C0573
    ChrTalk(
        0x101,
        (
            "#00000F好，我们总算\x01",
            "把参选者找齐了。\x02\x03",

            "这就去市民会馆，\x01",
            "向洛依先生他们报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x5)

    label("loc_B93B")

    SetScenarioFlags(0x199, 5)
    OP_4C(0x9, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 7330, 0, -1350, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_25_B44A end

    def Function_26_B96E(): pass

    label("Function_26_B96E")

    EventBegin(0x1)

    #C0574
    ChrTalk(
        0x101,
        (
            "#00000F哦，现在可不能\x01",
            "从店里出去啊。\x02\x03",

            "镶嵌好核心回路之后，\x01",
            "就和温蒂说一声吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -4250, 0, 2230, 90)
    EventEnd(0x4)
    Return()

    # Function_26_B96E end

    SaveToFile()

Try(main)
