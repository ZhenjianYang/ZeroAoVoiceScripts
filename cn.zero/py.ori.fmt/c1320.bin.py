from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1320.bin",                # FileName
        "c1320",                    # MapName
        "c1320",                    # Location
        0x001F,                     # MapIndex
        "ed7522",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 31, 0, 1, 0, 3],
    )

    BuildStringList((
        "c1320",                  # 0
        "玛丽亚贝尔",             # 1
        "研究员库雷",             # 2
        "研究员达比德",           # 3
        "罗伯兹主任",             # 4
        "缇欧",                   # 5
        "基约姆师傅",             # 6
        "SE控制",                 # 7
    ))

    AddCharChip((
        "chr/ch32800.itc",                   # 00
        "chr/ch29400.itc",                   # 01
        "chr/ch05500.itc",                   # 02
        "chr/ch32802.itc",                   # 03
        "chr/ch29402.itc",                   # 04
        "chr/ch29302.itc",                   # 05
        "chr/ch00202.itc",                   # 06
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4699,    -379,    22700,   45,   341,  0x0, 0,   3,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(-4699,   -379,    22700,   315,  341,  0x0, 0,   4,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(0,       0,       18239,   0,    469,  0x0, 0,   5,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(-4699,   -379,    22700,   315,  469,  0x0, 0,   6,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 30,  70.63999938964844,     24.0,                  9.5,                   9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -35.31999969482422,    -8.0,                  -1.9000002145767212,   1.0])

    ScpFunction((
        "Function_0_250",          # 00, 0
        "Function_1_308",          # 01, 1
        "Function_2_554",          # 02, 2
        "Function_3_55B",          # 03, 3
        "Function_4_60A",          # 04, 4
        "Function_5_1C85",         # 05, 5
        "Function_6_32EC",         # 06, 6
        "Function_7_381B",         # 07, 7
        "Function_8_3D59",         # 08, 8
        "Function_9_4341",         # 09, 9
        "Function_10_4634",        # 0A, 10
        "Function_11_47E0",        # 0B, 11
        "Function_12_4BF7",        # 0C, 12
        "Function_13_6A66",        # 0D, 13
        "Function_14_6A93",        # 0E, 14
        "Function_15_6AE1",        # 0F, 15
        "Function_16_6B32",        # 10, 16
        "Function_17_6B83",        # 11, 17
        "Function_18_6BD4",        # 12, 18
        "Function_19_6C1F",        # 13, 19
        "Function_20_6C8E",        # 14, 20
        "Function_21_6CEA",        # 15, 21
        "Function_22_6D4D",        # 16, 22
        "Function_23_6DA9",        # 17, 23
        "Function_24_6E12",        # 18, 24
        "Function_25_6E35",        # 19, 25
        "Function_26_7360",        # 1A, 26
        "Function_27_7602",        # 1B, 27
        "Function_28_8294",        # 1C, 28
        "Function_29_82AC",        # 1D, 29
        "Function_30_82C8",        # 1E, 30
    ))


    def Function_0_250(): pass

    label("Function_0_250")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_290"),
        (1, "loc_29C"),
        (2, "loc_2A8"),
        (3, "loc_2B4"),
        (4, "loc_2C0"),
        (5, "loc_2CC"),
        (6, "loc_2D8"),
        (SWITCH_DEFAULT, "loc_2E4"),
    )


    label("loc_290")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_29C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2A8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2B4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2C0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2CC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2E4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_307")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_307")

    Return()

    # Function_0_250 end

    def Function_1_308(): pass

    label("Function_1_308")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_329")
    ClearScenarioFlags(0x5F, 1)
    Call(0, 2)

    label("loc_329")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_348")
    SetMapFlags(0x10000000)
    Event(0, 12)

    label("loc_348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_357")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 11)

    label("loc_357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37B")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 700, -600, 13500, 0)

    label("loc_37B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_END)), "loc_3DE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 3)), scpexpr(EXPR_END)), "loc_3A1")
    ClearChrFlags(0xC, 0x80)

    label("loc_3A1")

    Jump("loc_3AB")

    label("loc_3A6")

    ClearChrFlags(0xC, 0x80)

    label("loc_3AB")

    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 4070, -480, 20560, 45)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x40)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_544")

    label("loc_3DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3EC")
    Jump("loc_544")

    label("loc_3EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3FF")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_544")

    label("loc_3FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_40D")
    Jump("loc_544")

    label("loc_40D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_41B")
    Jump("loc_544")

    label("loc_41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_496")
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, -1070, 0, -640, 135)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x40)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -1070, 0, -2590, 45)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x40)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 640, 0, -1590, 270)
    SetChrFlags(0x8, 0x10)
    Jump("loc_544")

    label("loc_496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4D2")
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 4070, -480, 20560, 45)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x40)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0x9, 0x10)
    Jump("loc_544")

    label("loc_4D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4E0")
    Jump("loc_544")

    label("loc_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4FF")
    SetChrPos(0xA, 0, 0, 18240, 0)
    Jump("loc_544")

    label("loc_4FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_536")
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 4070, -480, 20560, 45)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x40)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_544")

    label("loc_536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_END)), "loc_544")
    ClearChrFlags(0x8, 0x80)

    label("loc_544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_553")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 27)

    label("loc_553")

    Return()

    # Function_1_308 end

    def Function_2_554(): pass

    label("Function_2_554")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_554 end

    def Function_3_55B(): pass

    label("Function_3_55B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_577")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_589")

    label("loc_577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_END)), "loc_589")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x201), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_589")

    SetMapObjFrame(0xFF, "monita3_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita4_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita5_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita2_add", 0x2, "nomal")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_END)), "loc_5EB")
    OP_10(0x2, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_5F1")

    label("loc_5EB")

    OP_10(0x2, 0x1)
    OP_10(0x3, 0x0)

    label("loc_5F1")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_609")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_609")

    Return()

    # Function_3_55B end

    def Function_4_60A(): pass

    label("Function_4_60A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_END)), "loc_834")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6A7")
    Jump("loc_6F1")

    label("loc_6A7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6C7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F1")

    label("loc_6C7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F1")

    label("loc_6E7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6F1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_777")

    #C0001
    ChrTalk(
        0xFE,
        "导力网络的恢复工作就交给我吧。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "别看我这样，毕竟也是\x01",
            "导力网络的管理者呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_828")

    label("loc_777")


    #C0003
    ChrTalk(
        0xFE,
        (
            "在第二次测试中开发的\x01",
            "演算系统似乎发挥了作用呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "它经过了优化处理，\x01",
            "可以适用于大规模的\x01",
            "导力网络。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "虽然还不知道是被谁切断的……\x01",
            "但你们等着吧，我一定会查清真相！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_828")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1C84")

    label("loc_834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A40")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D1")
    Jump("loc_91B")

    label("loc_8D1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8F1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_91B")

    label("loc_8F1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_911")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_91B")

    label("loc_911")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_91B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9A6")

    #C0006
    ChrTalk(
        0xFE,
        (
            "要尽量在预定时间之前完成，\x01",
            "给大小姐一个惊喜。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "嗯，到时肯定能\x01",
            "得到她的表扬呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A34")

    label("loc_9A6")


    #C0008
    ChrTalk(
        0xFE,
        (
            "我正在制作大规模导力网络\x01",
            "专用的特殊系统。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "只要将它完成，应该就能\x01",
            "顺利进行第二次测试了……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "总算有希望得到\x01",
            "大小姐的认可了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_A34")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1C84")

    label("loc_A40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_BCB")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ADD")
    Jump("loc_B27")

    label("loc_ADD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AFD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B27")

    label("loc_AFD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B27")

    label("loc_B1D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B27")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0011
    ChrTalk(
        0xFE,
        (
            "主任会来帮忙，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "主任在导力网络的设计领域\x01",
            "也是个富有经验的专家啊。\x01",
            "哎，这下就让人心里有底啦！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1C84")

    label("loc_BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_DAC")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C68")
    Jump("loc_CB2")

    label("loc_C68")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C88")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CB2")

    label("loc_C88")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CA8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CB2")

    label("loc_CA8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CB2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D16")

    #C0013
    ChrTalk(
        0xFE,
        (
            "为了不辜负大小姐的期待，\x01",
            "必须要拼命努力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA0")

    label("loc_D16")


    #C0014
    ChrTalk(
        0xFE,
        (
            "导力网络的运行状况\x01",
            "也终于稳定下来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "差不多也该开始\x01",
            "第二次测试的准备工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "好～等着瞧吧……\x01",
            "我马上就把计划书完成！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_DA0")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1C84")

    label("loc_DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_FEC")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E49")
    Jump("loc_E93")

    label("loc_E49")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E69")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E93")

    label("loc_E69")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E89")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E93")

    label("loc_E89")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E93")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F30")

    #C0017
    ChrTalk(
        0xFE,
        (
            "就算黑客进行了如此疯狂的攻击，\x01",
            "导力网络还是没受到丝毫影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "导力网络似乎总算\x01",
            "可以稳定运行了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE0")

    label("loc_F30")


    #C0019
    ChrTalk(
        0xFE,
        (
            "多亏了那些黑客在前些天的攻击，\x01",
            "导力网络中的负荷数据都已经清除掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "这样一来，导力网络似乎\x01",
            "也可以稳定运行了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "不过这期间也被玛丽亚贝尔小姐\x01",
            "训斥过无数次呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_FE0")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1C84")

    label("loc_FEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_10AB")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_10A0")

    #C0022
    ChrTalk(
        0xFE,
        (
            "昨天傍晚时分，好像有黑客\x01",
            "入侵网络呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "我在追踪其形迹的过程中，\x01",
            "发现了不少好玩的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "这、这并不是在偷懒啦，\x01",
            "黑客的资料已经\x01",
            "顺利取得了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A3")

    label("loc_10A0")

    Call(0, 10)

    label("loc_10A3")

    TalkEnd(0xFE)
    Jump("loc_1C84")

    label("loc_10AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_12F5")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1148")
    Jump("loc_1192")

    label("loc_1148")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1168")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1192")

    label("loc_1168")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1188")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1192")

    label("loc_1188")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1192")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 3)), scpexpr(EXPR_END)), "loc_12E6")

    #C0025
    ChrTalk(
        0xFE,
        (
            "但同时也得到了各种不相关的情报文件，\x01",
            "我顺便查看了一下其中的内容而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "看起来，似乎是某个地方\x01",
            "的黑客所为……\x01",
            "究竟是出于什么企图呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "…………总之，先把这些资料\x01",
            "打印出一份吧。\x02",
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
    Jump("loc_12E9")

    label("loc_12E6")

    Call(0, 9)

    label("loc_12E9")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1C84")

    label("loc_12F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_15A5")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1392")
    Jump("loc_13DC")

    label("loc_1392")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13B2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13DC")

    label("loc_13B2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13D2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13DC")

    label("loc_13D2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13DC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1484")

    #C0028
    ChrTalk(
        0xFE,
        (
            "导力网络实在是一个\x01",
            "非常有研究价值的系统。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "就算是为了回报赏识我，\x01",
            "把我招募到这里的大小姐，\x01",
            "也必须要努力啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1599")

    label("loc_1484")


    #C0030
    ChrTalk(
        0xFE,
        (
            "我原来在大学的\x01",
            "研究机关工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "但就在某一天，玛丽亚贝尔小姐突然出现，\x01",
            "把我挖角到了ＩＢＣ的技术部。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ的导力网络构想\x01",
            "是把全世界的终端连接在一起，\x01",
            "从而得以在瞬间查询到顾客的信息……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "听到如此宏伟的构想之后，\x01",
            "我实在是激动万分，\x01",
            "甚至到了坐立不安的程度呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1599")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1C84")

    label("loc_15A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1810")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1642")
    Jump("loc_168C")

    label("loc_1642")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1662")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_168C")

    label("loc_1662")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1682")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_168C")

    label("loc_1682")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_168C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_174E")

    #C0034
    ChrTalk(
        0xFE,
        (
            "最近，加入导力网络计划的企业\x01",
            "开始增多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "随着终端数量的增加，纪念庆典期间的\x01",
            "情报量就如洪水般汹涌而至……\x01",
            "必须要制定些对策才行啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1804")

    label("loc_174E")


    #C0036
    ChrTalk(
        0xFE,
        (
            "真是麻烦啊……随着纪念庆典的召开，\x01",
            "大量情报都汹涌而至了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        "嗯～这真是预料之外的事态啊。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "再这样下去，整个导力网络系统\x01",
            "恐怕都会陷入不稳定的状态。\x01",
            "必须想点办法才行……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1804")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1C84")

    label("loc_1810")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1A4F")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_18AD")
    Jump("loc_18F7")

    label("loc_18AD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_18CD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18F7")

    label("loc_18CD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18ED")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18F7")

    label("loc_18ED")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18F7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1998")

    #C0039
    ChrTalk(
        0xFE,
        (
            "爱普斯泰恩财团的罗伯兹氏\x01",
            "是导力网络的开发主任之一。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "他身为技术顾问，\x01",
            "经常向我们提供一些技术支持呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A43")

    label("loc_1998")


    #C0041
    ChrTalk(
        0xFE,
        "呼，这可真够棘手。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "黑客利用系统的\x01",
            "基础代码，\x01",
            "巧妙的侵入了进来。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "只有我们几个来应对的话，负担实在是太重了。\x01",
            "……是不是应该请财团的\x01",
            "罗伯兹主任前来支援呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1A43")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1C84")

    label("loc_1A4F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1AE3")
    Jump("loc_1B2D")

    label("loc_1AE3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1B03")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B2D")

    label("loc_1B03")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B23")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B2D")

    label("loc_1B23")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B2D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1BC3")

    #C0044
    ChrTalk(
        0xFE,
        (
            "竟然在大小姐的面前\x01",
            "把脸丢得如此彻底……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "可恶，我要立刻\x01",
            "查明原因……！\x01",
            "（狂敲键盘……！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C7D")

    label("loc_1BC3")


    #C0046
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ的终端竟然\x01",
            "会被人从外部盗用……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "真、真是没脸见人了。\x01",
            "如果在导力网络正式投入使用后\x01",
            "还发生这种事，那就真的不可原谅了。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "必须迅速查明原因，\x01",
            "并采取相应对策……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_1C7D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)

    label("loc_1C84")

    Return()

    # Function_4_60A end

    def Function_5_1C85(): pass

    label("Function_5_1C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_END)), "loc_1D03")
    TalkBegin(0xFE)

    #C0049
    ChrTalk(
        0xFE,
        (
            "嘿，这些先进的设备就是\x01",
            "为了应对这种情况而存在的。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "交给我们吧！\x01",
            "我们一定会建立起一条迂回线路的！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_32EB")

    label("loc_1D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1F9F")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DA0")
    Jump("loc_1DEA")

    label("loc_1DA0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1DC0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DEA")

    label("loc_1DC0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DE0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DEA")

    label("loc_1DE0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DEA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1E94")

    #C0051
    ChrTalk(
        0xFE,
        (
            "我在和库雷那家伙\x01",
            "一起创建新系统。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "现在的系统确实存在着\x01",
            "各种各样的漏洞啊……\x01",
            "重新审视一下后，真是觉得很惭愧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F93")

    label("loc_1E94")


    #C0053
    ChrTalk(
        0xFE,
        (
            "最近才注意到，\x01",
            "似乎有个节点的运转十分异常呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "看起来虽然像是黑客行为，\x01",
            "但并没有造成什么破坏与损失，\x01",
            "只是在网络上进行观察而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "嗯～这是哪里的终端？\x01",
            "……『玛因兹山道』……\x01",
            "……『罗赞贝尔克工房』？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "嘁……好像又有\x01",
            "什么地方出现故障了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1F93")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_32EB")

    label("loc_1F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_214F")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_203C")
    Jump("loc_2086")

    label("loc_203C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_205C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2086")

    label("loc_205C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_207C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2086")

    label("loc_207C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2086")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0057
    ChrTalk(
        0xFE,
        (
            "真奇怪，玛丽亚贝尔小姐\x01",
            "今天紧绷着脸，莫名地怒气冲冲……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        "发生什么事了吗？\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "长期在这种地下房间里工作，慢慢就会\x01",
            "变得不通世事，这样可不行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_32EB")

    label("loc_214F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_23BD")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_21EC")
    Jump("loc_2236")

    label("loc_21EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_220C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2236")

    label("loc_220C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_222C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2236")

    label("loc_222C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2236")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2317")

    #C0060
    ChrTalk(
        0xFE,
        (
            "在第二次测试，预定将会\x01",
            "增加连接的导力终端数量，\x01",
            "覆盖比以往更多的对象。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "为了负担如此巨大的数据量，\x01",
            "必须要开发新的系统……\x01",
            "既然都已经走到这一步了，也只能全力以赴啦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23B1")

    label("loc_2317")


    #C0062
    ChrTalk(
        0xFE,
        (
            "大小姐来咨询第二次测试的状况，\x01",
            "然后表现得很感兴趣哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "看来，我拼命努力，不断进行改良强化\x01",
            "还是很值得的。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "好，赶快收集资料，\x01",
            "全力以赴吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_23B1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_32EB")

    label("loc_23BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_25B8")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_245A")
    Jump("loc_24A4")

    label("loc_245A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_247A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24A4")

    label("loc_247A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_249A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24A4")

    label("loc_249A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24A4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2514")

    #C0065
    ChrTalk(
        0xFE,
        (
            "个人情报果然很难处理啊……\x01",
            "有必要增加一些防黑客的对策。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25AC")

    label("loc_2514")


    #C0066
    ChrTalk(
        0xFE,
        (
            "……通过导力网络流传的\x01",
            "不正当的情报文件\x01",
            "已经全部删除了。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        "个人情报果然很难处理啊……\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "因为这个，我还被玛丽亚贝尔小姐\x01",
            "狠狠训斥了一顿呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_25AC")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_32EB")

    label("loc_25B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2722")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2717")

    #C0069
    ChrTalk(
        0xFE,
        (
            "事、事实上，在导力网络上，\x01",
            "发现了一个让我非常感兴趣……\x01",
            "但又不太正当的图片资料。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "果、果然还是应该\x01",
            "向大小姐报告吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "其实是大小姐在学生时代\x01",
            "穿着泳装，身材火爆的照片……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2712")

    #C0072
    ChrTalk(
        0x101,
        (
            "#0005F（难道……\x01",
            "  是约纳昨天干的吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x103,
        (
            "#0200F（说起来，他好像是说过\x01",
            "  要布下诱饵之类的话呢。\x01",
            "  这也许就是其中之一吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2712")

    Jump("loc_271A")

    label("loc_2717")

    Call(0, 10)

    label("loc_271A")

    TalkEnd(0xFE)
    Jump("loc_32EB")

    label("loc_2722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_286D")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 3)), scpexpr(EXPR_END)), "loc_2862")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_27DF")

    #C0074
    ChrTalk(
        0xFE,
        (
            "……喂，库雷，你太狡猾了。\x01",
            "赶快给我也打印一份啊。\x02",
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
    Jump("loc_285D")

    label("loc_27DF")


    #C0075
    ChrTalk(
        0xFE,
        (
            "拜托啦，一定要对\x01",
            "大小姐保密啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "那个，我觉得一定会被骂的。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x103,
        "#0200F我倒是没问题……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    OP_9E(0xA, 0x0, 0x0, 0xAFC8, 0x0, 0x0)
    SetChrFlags(0xA, 0x10)

    label("loc_285D")

    Jump("loc_2865")

    label("loc_2862")

    Call(0, 9)

    label("loc_2865")

    TalkEnd(0xFE)
    Jump("loc_32EB")

    label("loc_286D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2AF7")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_290A")
    Jump("loc_2954")

    label("loc_290A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_292A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2954")

    label("loc_292A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_294A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2954")

    label("loc_294A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2954")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2A0A")

    #C0078
    ChrTalk(
        0xFE,
        (
            "事实上，好像从今天早上开始，\x01",
            "黑客就开始积极展开行动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "好，追踪他们，然后获取数据吧。\x01",
            "反击黑客的第一步\x01",
            "就是收集数据啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AEB")

    label("loc_2A0A")


    #C0080
    ChrTalk(
        0xFE,
        (
            "导力网络是一个\x01",
            "尚处于研究阶段的系统，\x01",
            "所以有可能会出现各种各样的问题呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "像黑客之类的问题\x01",
            "就算是其中之一吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "在列曼自治州，\x01",
            "也有将各个研究机关\x01",
            "紧密相连的导力网络……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "但都没有出现\x01",
            "意图入侵其中的黑客呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2AEB")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_32EB")

    label("loc_2AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2D79")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B94")
    Jump("loc_2BDE")

    label("loc_2B94")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BB4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BDE")

    label("loc_2BB4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BD4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BDE")

    label("loc_2BD4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BDE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2C97")

    #C0084
    ChrTalk(
        0xFE,
        (
            "不过，我们这些管理者如果不全力以赴，\x01",
            "导力网络就会瘫痪的。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "……那样的话，大小姐肯定会……\x01",
            "……光是想想就觉得很恐怖了…………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D6D")

    label("loc_2C97")


    #C0086
    ChrTalk(
        0xFE,
        (
            "导力网络这种东西，\x01",
            "光是想让它稳定运行，\x01",
            "就已经是相当复杂的工程了。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "……其实，昨天也有\x01",
            "一部演算装置瘫痪了呢。\x01",
            "我通宵达旦地进行了恢复工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "外面正在热热闹闹地举办纪念庆典呢，\x01",
            "真是觉得有些空虚啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2D6D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_32EB")

    label("loc_2D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2EB0")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2DEB")

    #C0089
    ChrTalk(
        0xA,
        (
            "不尽快落实对策的话，\x01",
            "就又要被玛丽亚贝尔大小姐斥责了……\x01",
            "必、必须要抓紧时间了………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA8")

    label("loc_2DEB")


    #C0090
    ChrTalk(
        0xA,
        (
            "嗯～是从这种地方\x01",
            "侵入进来的吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xA,
        (
            "可是，这样的话，\x01",
            "如果不知道源代码，\x01",
            "是绝对无法做到的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x9,
        (
            "啊啊，真是的！\x01",
            "这究竟是怎么做到的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "黑客对系统还真是\x01",
            "相当熟悉呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xA, 0x10)

    label("loc_2EA8")

    TalkEnd(0xFE)
    Jump("loc_32EB")

    label("loc_2EB0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F44")
    Jump("loc_2F8E")

    label("loc_2F44")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F64")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F8E")

    label("loc_2F64")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F84")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F8E")

    label("loc_2F84")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F8E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_319F")

    #C0094
    ChrTalk(
        0xFE,
        (
            "话说回来……要是再不赶快采取对策，\x01",
            "又要被玛丽亚贝尔小姐……\x01",
            "…………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "……不，没什么。\x01",
            "就当我什么都没说吧。\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30DF")

    #C0096
    ChrTalk(
        0x101,
        "#0005F（有、有些令人在意呢……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_319A")

    label("loc_30DF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_312B")

    #C0097
    ChrTalk(
        0x102,
        (
            "#0106F（贝尔也真是的，\x01",
            "  平时好像总是欺负部下……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_319A")

    label("loc_312B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3168")

    #C0098
    ChrTalk(
        0x103,
        "#0200F（……会有什么特别的惩罚吗。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_319A")

    label("loc_3168")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_319A")

    #C0099
    ChrTalk(
        0x104,
        "#0300F（哈哈哈，真可怕啊……）\x02",
    )

    CloseMessageWindow()

    label("loc_319A")

    Jump("loc_32E4")

    label("loc_319F")


    #C0100
    ChrTalk(
        0xFE,
        "不过，还真是让人大吃一惊啊……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "那种追踪技术，我还是\x01",
            "第一次见识到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x103,
        (
            "#0203F……这全都是靠魔导杖附带的\x01",
            "『永世系统』才能实现，\x01",
            "并不是我自身的能力。\x02\x03",

            "#0200F那么，接下来交给你们就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "嗯，已经帮了大忙啦，\x01",
            "之后的事情我们会解决的。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "哈，总之就交给我们吧。\x01",
            "再怎么说，我也是\x01",
            "导力网络系统的研究员啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_32E4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)

    label("loc_32EB")

    Return()

    # Function_5_1C85 end

    def Function_6_32EC(): pass

    label("Function_6_32EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x397, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3323")
    Call(0, 26)
    Return()

    label("loc_3323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_END)), "loc_356D")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_33C0")
    Jump("loc_340A")

    label("loc_33C0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_33E0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_340A")

    label("loc_33E0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3400")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_340A")

    label("loc_3400")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_340A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3497")

    #C0105
    ChrTalk(
        0xFE,
        (
            "导力网络方面的问题就\x01",
            "交给我们好啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "只要再等几个小时，\x01",
            "应该就能完成恢复工作了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3561")

    label("loc_3497")


    #C0107
    ChrTalk(
        0xFE,
        (
            "导力网络方面的问题就\x01",
            "交给我们好啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "根据我的解析，问题的原因\x01",
            "似乎在于导力缆线上被人装设了\x01",
            "会散发妨害波流的装置……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "这里的工作人员都是很优秀的。\x01",
            "嗯，再有几个小时，\x01",
            "应该就能成功修复了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3561")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_381A")

    label("loc_356D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_35E8")

    #C0110
    ChrTalk(
        0xFE,
        (
            "哼哼～呵……¤\x01",
            "（狂敲键盘……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        (
            "#0005F（都看不清他敲打键盘的动作……\x01",
            "  究竟是怎么做到的……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3817")

    label("loc_35E8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_367C")
    Jump("loc_36C6")

    label("loc_367C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_369C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36C6")

    label("loc_369C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36BC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36C6")

    label("loc_36BC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_36C6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0112
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ的人来向我\x01",
            "求助了。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "他们为了对导力系统进行第二次测试，\x01",
            "正在创建新系统呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#0000F（财团的主任先生……\x01",
            "  今天好像在负责很困难的工作呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        (
            "#0203F（就安静踏实地处理工作这点来看，\x01",
            "  主任应该算是非常优秀的。）\x02\x03",

            "#0200F（毕竟，他也是世界上为数不多的\x01",
            "  智慧集团中的一员啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetScenarioFlags(0x0, 2)

    label("loc_3817")

    TalkEnd(0xFE)

    label("loc_381A")

    Return()

    # Function_6_32EC end

    def Function_7_381B(): pass

    label("Function_7_381B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3B02")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3917")

    #C0116
    ChrTalk(
        0x8,
        (
            "#2904F嗯，技术方面的问题\x01",
            "应该能在短时间内解决吧。\x02\x03",

            "#2900F我们这里的技术员很优秀，\x01",
            "只要定期去训斥一下，\x01",
            "他们就能出色地完成工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        "#0000F是、是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x102,
        (
            "#0106F（贝尔的这种口气，\x01",
            "  好像有点女王大人的感觉呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AFA")

    label("loc_3917")


    #C0119
    ChrTalk(
        0x8,
        "#2903F嗯，好像真是很困难呢。\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x102,
        "#0105F贝尔，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        (
            "#0006F话说回来，这个房间还是老样子，\x01",
            "看上去很惊人呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "#2900F呵呵，事实上，这里正在进行\x01",
            "导力网络的第二次测试计划。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x103,
        (
            "#0200F第二次测试……其目的是\x01",
            "以普通市民为对象，让导力终端\x01",
            "得到正式普及。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        (
            "#2903F嗯，不过再怎么说，想要让终端\x01",
            "普及到可以在市场上正常贩卖的程度，\x01",
            "还有相当长的路要走呢。\x02\x03",

            "现在要考虑的问题，主要是\x01",
            "建立更大规模的导力网络……\x02\x03",

            "#2900F虽然有着各种各样的阻碍，\x01",
            "但确实是个很有挑战价值的课题呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3AFA")

    TalkEnd(0x8)
    Jump("loc_3D58")

    label("loc_3B02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3C6F")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3C64")
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0125
    ChrTalk(
        0x102,
        (
            "#0103F贝尔，我觉得你还是不要\x01",
            "太欺负你的部下吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "#2905F啊呀，其实这并不算\x01",
            "什么欺负啦。\x02\x03",

            "#2904F……我说的对吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 300)
    TurnDirection(0xA, 0x0, 300)

    #N0127
    NpcTalk(
        0x9,
        "库雷＆达比德",
        "是啊，当然不算！\x02",
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
    OP_9E(0xA, 0x0, 0x0, 0x20F58, 0x0, 0x0)
    OP_9E(0x9, 0x0, 0x0, 0xAFC8, 0x0, 0x0)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Jump("loc_3C67")

    label("loc_3C64")

    Call(0, 10)

    label("loc_3C67")

    TalkEnd(0x8)
    Jump("loc_3D58")

    label("loc_3C6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C85")
    Call(0, 25)
    Jump("loc_3D58")

    label("loc_3C85")

    TalkBegin(0x8)

    #C0128
    ChrTalk(
        0x8,
        (
            "#2900F看起来，黑客似乎\x01",
            "就在地下空间的\x01",
            "Ｂ区域呢。\x02\x03",

            "#2903F地下空间是由市政厅管理的，\x01",
            "所以如果想展开调查，就要先和\x01",
            "他们那边打声招呼。\x02\x03",

            "#2900F呵呵，等到将事件顺利解决之后，\x01",
            "一定要把具体经过全部告诉我啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_3D58")

    Return()

    # Function_7_381B end

    def Function_8_3D59(): pass

    label("Function_8_3D59")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3DED")
    Jump("loc_3E37")

    label("loc_3DED")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3E0D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E37")

    label("loc_3E0D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E2D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E37")

    label("loc_3E2D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E37")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 3)), scpexpr(EXPR_END)), "loc_40EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_402E")

    #C0129
    ChrTalk(
        0xC,
        "#0205F啊，罗伊德前辈。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        (
            "#0002F缇欧，你已经开始\x01",
            "在这里帮忙了啊。\x02\x03",

            "之前说要和约纳取得联络，\x01",
            "有什么进展吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xC,
        (
            "#0204F这个啊……\x02\x03",

            "#0202F约纳为了方便进行黑客行动，\x01",
            "在各处的控制终端上\x01",
            "都开了后门。\x02\x03",

            "如果可以访问到其中一处，\x01",
            "应该就能将现状传达给他了……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#0000F原、原来如此……\x01",
            "也就是说，终于可以和外界取得联络了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xC,
        (
            "#0204F嗯，虽然目前还在尝试阶段。\x02\x03",

            "#0202F……正是在这种时期，\x01",
            "才要让他把平时欠我们的情全部还回来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE4, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40E6")

    label("loc_402E")


    #C0134
    ChrTalk(
        0xC,
        (
            "#0204F……在这边帮忙的\x01",
            "有我一个人就足够了。\x02\x03",

            "#0202F罗伊德前辈如果已经完成了补给工作，\x01",
            "就先去稍微休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40E6")

    #C0135
    ChrTalk(
        0x101,
        (
            "#0004F嗯，谢谢。\x02\x03",

            "#0002F缇欧，你也不要\x01",
            "太过拼命啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_40E6")

    Jump("loc_4339")

    label("loc_40EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42BB")

    #C0136
    ChrTalk(
        0x101,
        (
            "#0002F缇欧，你好像在帮忙\x01",
            "进行导力网络的复原工作啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xC,
        "#0203F嗯，算是，不过……\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        "#0005F？？？\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xC,
        (
            "#0202F还是想先试试能否与约纳取得联络。\x02\x03",

            "约纳为了方便进行黑客行动，\x01",
            "在各处的控制终端上\x01",
            "都开了后门。\x02\x03",

            "如果可以访问到其中一处，\x01",
            "应该就能将现状传达给他了……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        (
            "#0000F原、原来如此……\x01",
            "也就是说，终于可以和外界取得联络了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xC,
        (
            "#0204F嗯，虽然目前还在尝试阶段。\x02\x03",

            "#0202F……正是在这种时期，\x01",
            "才要让他把平时欠我们的情全部还回来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE4, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4339")

    label("loc_42BB")


    #C0142
    ChrTalk(
        0xC,
        (
            "#0204F如果可以成功访问其中一处控制终端，\x01",
            "或许就能同约纳取得联络了。\x02\x03",

            "#0202F……正是因为情况特殊，\x01",
            "所以才要拉约纳来帮忙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4339")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_3D59 end

    def Function_9_4341(): pass

    label("Function_9_4341")

    OP_4B(0xA, 0xFF)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x9, 0x0, 1000)
    TurnDirection(0xA, 0x0, 1000)
    Sleep(1000)
    OP_64(0x9)
    OP_64(0xA)

    #C0143
    ChrTalk(
        0x9,
        (
            "什、什么啊……是你们吗……\x01",
            "不要吓我嘛……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x103,
        "#0205F发生什么事了吗……？\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x9,
        (
            "不，那个……\x01",
            "只是在导力网络上发现了一些\x01",
            "让人在意的数据在流传。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xA,
        (
            "啊啊，竟然是玛丽亚贝尔小姐\x01",
            "在学生时代穿泳装\x01",
            "的照片……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xA,
        "这真是超级稀有的资料啊……\x02",
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

    #C0148
    ChrTalk(
        0xA,
        "啊，那、那个，我并不是在忙中偷闲哦！\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        "那个，只是偶然发现的而已……\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x9,
        (
            "不过，这种照片，\x01",
            "到底是谁传出来的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        "#0003F（难道……是约纳干的吗？）\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x103,
        (
            "#0200F（说起来，他好像是说过\x01",
            "  要布下诱饵之类的话呢。\x01",
            "  这也许就是其中之一吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0xA, 0x0, 0x0, 0xAFC8, 0x0, 0x0)
    OP_9E(0x9, 0x0, 0x0, 0xAFC8, 0x0, 0x0)
    SetScenarioFlags(0xB2, 3)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_4341 end

    def Function_10_4634(): pass

    label("Function_10_4634")

    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0153
    ChrTalk(
        0xA,
        "竟然得到了大小姐的慰劳……\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x9,
        "太、太感激了！\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x8,
        (
            "#2904F呵呵，我可没有那么小气，\x01",
            "总不会让部下在纪念庆典期间\x01",
            "也这么辛苦。\x02\x03",

            "#2900F另外，导力网络那边\x01",
            "的情况怎么样了？\x01",
            "有什么异常吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x9,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xA,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x9,
        "没什么！\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xA,
        "嗯，没什么特别的！\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x8,
        (
            "#2902F……你们好像有所隐瞒啊。\x01",
            "赶快给我说实话。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x9,
        "十、十分抱歉～！\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xA,
        "我马上就坦白……呃！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x8, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_10_4634 end

    def Function_11_47E0(): pass

    label("Function_11_47E0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(69400, 11000, 24000, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 72500, 10000, 23700, 270)
    SetChrPos(0x102, 72500, 10000, 24300, 270)
    SetChrPos(0x103, 72500, 10000, 23700, 270)
    SetChrPos(0x104, 72500, 10000, 24300, 270)
    SetChrPos(0x138, 72500, 10000, 24000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x138, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(160, 0, 100, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    Sleep(500)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    OP_68(67400, 11000, 24000, 3000)
    SetCameraDistance(22500, 3000)

    def lambda_48F5():
        OP_96(0xFE, 0x1016C, 0x2710, 0x5DC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_48F5)

    def lambda_490F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_490F)
    Sleep(800)

    def lambda_4923():
        OP_96(0xFE, 0x108D8, 0x2710, 0x5B68, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4923)

    def lambda_493D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_493D)
    Sleep(400)

    def lambda_4951():
        OP_96(0xFE, 0x108D8, 0x2710, 0x6018, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4951)

    def lambda_496B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_496B)
    Sleep(400)

    def lambda_497F():
        OP_96(0xFE, 0x10D24, 0x2710, 0x5B68, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_497F)

    def lambda_4999():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4999)
    Sleep(400)

    def lambda_49AD():
        OP_96(0xFE, 0x10D24, 0x2710, 0x6018, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_49AD)

    def lambda_49C7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_49C7)
    WaitChrThread(0x138, 1)
    WaitChrThread(0x101, 1)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    OP_93(0x138, 0x5A, 0x1F4)

    #C0163
    ChrTalk(
        0x138,
        (
            "#6P#2904F这里就是地下五层……\x01",
            "设置有主终端的区域。\x02\x03",

            "#2900F下了楼梯就是终端室了。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            "#0001F#11P设置主终端的地方，\x01",
            "戒备真是相当森严呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x138,
        (
            "#6P#2903F这里毕竟是将要管理顾客情报的地方，\x01",
            "总要考虑得周全一点。\x02\x03",

            "#2901F不过对黑客的防范措施并不十分完善，所以目前，\x01",
            "通过导力网络办理银行业务的计划也只能暂缓了。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        "#11P#0101F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x103,
        (
            "#11P#0206F确实，这里的资料一旦外流，\x01",
            "后果会相当严重呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x138,
        (
            "#6P#2904F嗯，这也是原因之一，\x01",
            "所以计划仍然处于研究阶段。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 68000, 10000, 24000, 270)
    SetScenarioFlags(0x82, 6)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_11_47E0 end

    def Function_12_4BF7(): pass

    label("Function_12_4BF7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50218.itc", 0x1E)
    LoadEffect(0x0, "event\\eva06_00.eff")
    SoundLoad(840)
    OP_68(10000, 1100, 0, 0)
    MoveCamera(55, 18, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x101, 10500, 0, -500, 270)
    SetChrPos(0x102, 10500, 0, 500, 270)
    SetChrPos(0x103, 10500, 0, -500, 270)
    SetChrPos(0x104, 10500, 0, 500, 270)
    SetChrPos(0x138, 10500, 0, 0, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x138, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 4700, -380, 22700, 45)
    SetChrFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, -4700, -380, 22700, 315)
    SetMapObjFrame(0xFF, "monita2_add", 0x2, "nomal")
    StopBGM(0x5DC)
    FadeToBright(1000, 0)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7522", 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x1)
    BeginChrThread(0x138, 3, 0, 14)
    BeginChrThread(0x101, 3, 0, 15)
    BeginChrThread(0x102, 3, 0, 16)
    BeginChrThread(0x103, 3, 0, 17)
    BeginChrThread(0x104, 3, 0, 19)
    OP_68(0, 1100, 0, 5000)
    OP_6F(0x1)
    OP_68(0, 1100, 16500, 8000)
    MoveCamera(30, 13, 0, 8000)
    SetCameraDistance(25500, 8000)
    WaitChrThread(0x138, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 500, 12500, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_0D()

    #C0169
    ChrTalk(
        0x101,
        "#12P#0005F这、这是……\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x104,
        (
            "#0306F怎么说呢～……\x01",
            "这房间还真是超级惊人啊。\x02\x03",

            "#0301F虽然早就知道这里是汇聚了\x01",
            "最新技术的地方，可还是……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x103,
        (
            "#12P#0204F这是爱普斯泰恩财团研发的\x01",
            "最新情报处理系统。\x02\x03",

            "#0202F听说利贝尔的高速巡洋舰\x01",
            "使用的就是这个系统……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x138, 0xB4, 0x1F4)

    #C0172
    ChrTalk(
        0x138,
        (
            "#2904F就是那艘非常有名的\x01",
            "『埃尔赛尤号』吧。\x02\x03",

            "#2902F那艘飞艇使用的系统\x01",
            "虽然和这个基本相同，不过……\x02\x03",

            "这个系统为了应对庞大的网络情报，\x01",
            "其处理能力已经强化了好几倍呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x102,
        "#0105F……好厉害……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x2)
    Sleep(300)

    #C0174
    ChrTalk(
        0x9,
        "#6P玛丽亚贝尔小姐……？\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xA,
        "#4P您辛苦了！\x02",
    )

    CloseMessageWindow()
    OP_63(0x138, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    BeginChrThread(0x9, 3, 0, 20)
    Sleep(300)
    BeginChrThread(0xA, 3, 0, 22)
    Sleep(2000)
    OP_68(0, 500, 13000, 1000)

    def lambda_5030():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_5030)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    OP_6F(0x1)

    #C0176
    ChrTalk(
        0x138,
        (
            "#11P#2900F呵呵，你们也辛苦了。\x02\x03",

            "工作还算顺利吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x9,
        "#11P嗯，托您的福。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xA,
        (
            "#5P模拟测试工作\x01",
            "应该可以顺利进展……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)

    #C0179
    ChrTalk(
        0xA,
        "#5P那个……这几位是……？\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x138,
        (
            "#11P#2900F他们是克洛斯贝尔警察局的人哦。\x02\x03",

            "据说，这个主终端有可能\x01",
            "受到了来自外部的\x01",
            "黑客入侵。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_517D():
        TurnDirection(0xFE, 0x138, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_517D)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0181
    ChrTalk(
        0x9,
        "#11P#4S哎哎哎哎！？\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xA,
        "#5P黑、黑客！？\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        "#12P#0003F那个……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0184
    ChrTalk(
        0x101,
        (
            "#5P#0001F缇欧，可以向他们\x01",
            "做个大致说明吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x103,
        "#12P#0200F好的，那么……\x02",
    )

    CloseMessageWindow()
    OP_68(0, 500, 13280, 1000)

    def lambda_524A():
        OP_95(0xFE, -1400, -600, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_524A)
    Sleep(150)

    def lambda_5267():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5267)
    Sleep(100)

    def lambda_5277():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_5277)
    WaitChrThread(0x103, 1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0186
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "缇欧夹杂着各种专门术语，\x01",
            "向研究员们说明了事件的情况。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0187
    ChrTalk(
        0x9,
        "#11P有黑客从外部入侵……\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x9,
        (
            "#11P虽然也存在这种可能性，\x01",
            "但没想到会真的发生……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 500)

    #C0189
    ChrTalk(
        0xA,
        "#1P不，这是不可能的啊！\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xA,
        (
            "#1P作为黑客入侵这里，需要十分高超的技术。\x01",
            "这种人怎么可能轻易出现……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x138,
        (
            "#11P#2904F如果这不是黑客所为，\x01",
            "那么，发送邮件的嫌疑人\x01",
            "就很有可能是你们了哦。\x02\x03",

            "#2902F呵呵……\x01",
            "你们之中，谁才是『银』呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_5458():
        TurnDirection(0xFE, 0x138, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_5458)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0192
    ChrTalk(
        0x9,
        "#11P没、没那回事啊！\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xA,
        (
            "#5P果然还是因为我们太没用，\x01",
            "所以才会让黑客趁虚而入！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0194
    ChrTalk(
        0x101,
        "#12P#0012F（这……该怎么说才好呢……）\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x104,
        (
            "#0300F（和伊莉娅小姐的感觉不同，\x01",
            "  属于另一种类型的女王呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x138,
        (
            "#11P#2903F邮件发送到特别任务支援科的终端，\x01",
            "是在凌晨三点左右……\x02\x03",

            "#2901F请你们调查一下，在那个时间段的\x01",
            "进程记录有什么异常吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x9,
        "#11P好、好的。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xA,
        "#5P马上就开始调查。\x02",
    )

    CloseMessageWindow()
    OP_68(0, 800, 21500, 3500)
    MoveCamera(45, 27, 0, 3500)
    SetCameraDistance(23000, 3500)
    BeginChrThread(0x9, 3, 0, 21)
    Sleep(200)
    BeginChrThread(0xA, 3, 0, 23)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    OP_6F(0x79)
    Sleep(200)
    Sound(849, 0, 100, 0)
    Sleep(1300)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0199
    ChrTalk(
        0x9,
        "#6P……啊，查到了！\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x9,
        (
            "#6P邮件的转发系统\x01",
            "遭到攻击了！\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x102,
        "#0101F果然……\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x104,
        (
            "#0303F这样一来，外部侵入\x01",
            "的推测就得到证实了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xA,
        "#11P我这边也确认到侵入路径了！\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xA,
        (
            "#11P入侵的原地址是……不行，\x01",
            "数据已经丢失了。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        (
            "#0001F也就是说，无法查明是从\x01",
            "什么地方进行入侵的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xA,
        (
            "#11P嗯，对方巧妙地\x01",
            "消除了访问痕迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xA,
        (
            "#11P我想，他肯定就在克洛斯贝尔\x01",
            "市内的某个地方，不过……\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x138,
        "#2901F嗯……干得不错嘛。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 500, 12500, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_0D()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    #C0209
    ChrTalk(
        0x103,
        (
            "#12P#0200F……终端装置，\x01",
            "可以借我用一台吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x2)
    Sleep(300)

    #C0210
    ChrTalk(
        0x9,
        "#6P哎……\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xA,
        "#4P可、可是……\x02",
    )

    CloseMessageWindow()

    def lambda_590D():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_590D)
    WaitChrThread(0x138, 1)

    #C0212
    ChrTalk(
        0x138,
        (
            "#11P#2904F可以。\x02\x03",

            "#2900F你是叫缇欧吧，\x01",
            "请随意使用。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x103,
        "#6P#0204F好的，那么……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(0, 800, 18600, 3000)
    MoveCamera(40, 27, 0, 3000)
    SetCameraDistance(18000, 3000)
    SetChrSubChip(0x9, 0x0)

    def lambda_59A2():

        label("loc_59A2")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_59A2")

    QueueWorkItem2(0x138, 2, lambda_59A2)

    def lambda_59B4():
        OP_95(0xFE, 0, -600, 14700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_59B4)
    WaitChrThread(0x103, 1)

    def lambda_59D2():
        OP_95(0xFE, 0, -300, 17300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_59D2)
    WaitChrThread(0x103, 1)
    Fade(250)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 0, -200, 18600, 0)
    Sound(820, 0, 100, 0)
    OP_0D()
    EndChrThread(0x138, 0x2)
    OP_6F(0x79)
    Sleep(500)
    Sound(1278, 255, 100, 0)    #voice#Tio
    Sleep(1500)
    Sound(1280, 255, 100, 0)    #voice#Tio
    Sleep(2000)
    PlayEffect(0x0, 0x0, 0x103, 0x140, 0, 1250, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(840, 2, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7524", 0)

    #C0214
    ChrTalk(
        0x101,
        "#0005F什么……\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x102,
        "#0101F缇欧……！？\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x138,
        "#2905F这是……\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xE, 1, 0, 24)
    Fade(500)
    OP_68(0, 800, 20500, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(15500, 0)
    SetMapObjFrame(0xFF, "monita2_add", 0x2, "event")
    BeginChrThread(0x103, 3, 0, 13)
    SetCameraDistance(22500, 20000)
    OP_0D()
    Sleep(300)

    #C0217
    ChrTalk(
        0x103,
        (
            "#0201F#30W展开多维解析，\x01",
            "施行实时控制……\x02\x03",

            "解析全部终端的进程记录，\x01",
            "分析所有被隐藏痕迹的前后差异，\x01",
            "对全部可疑地址进行详细检查……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x9,
        "#5P好、好厉害啊……！？\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xA,
        "#11P怎么回事，这种惊人的处理速度！？\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x103,
        (
            "#0203F……辅助工作就拜托二位了。\x02\x03",

            "#0202F我将使用管理者的权限，\x01",
            "访问克洛斯贝尔的全部终端。\x02\x03",

            "然后会把可疑的进程记录全部提取出来，\x01",
            "检查工作就交给你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x9,
        "#5P嗯……！\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xA,
        "#11P交给我们吧……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 500, 14500, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_68(0, 500, 12500, 2500)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_6F(0x1)
    TurnDirection(0x101, 0x102, 500)

    #C0223
    ChrTalk(
        0x101,
        "#6P#0008F……艾莉，你能听懂吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0224
    ChrTalk(
        0x102,
        (
            "#0106F#11P听、听不懂啊……\x01",
            "实在是跟不上他们这种水平啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x104,
        (
            "#0309F我可是连他们现在正在做些什么\x01",
            "都无法理解呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x138,
        (
            "#5P#2904F原来如此，缇欧原来是\x01",
            "『魔导杖』的使用者啊。\x02\x03",

            "#2902F听说有一种无需驱动时间\x01",
            "就可以直接发动导力魔法的\x01",
            "高速展开技术已经开始投入运用……\x02\x03",

            "她现在也许就是利用那个\x01",
            "来对终端进行控制呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5EA7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5EA7)
    Sleep(100)
    OP_93(0x102, 0x0, 0x1F4)

    #C0227
    ChrTalk(
        0x101,
        "#12P#0005F您、您能看明白吗？\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x102,
        (
            "#0100F#11P贝尔她毕竟有过\x01",
            "在爱普斯泰恩财团学习\x01",
            "导力工程学的经验……\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x138,
        (
            "#2904F#5P呵呵，话虽如此，\x01",
            "但也只是皮毛的程度而已。\x02",
        )
    )

    CloseMessageWindow()
    StopEffect(0x0, 0x2)
    SetMapObjFrame(0xFF, "monita2_add", 0x2, "event_stop")
    SetMapObjFrame(0xFF, "monita4_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "monita3_add", 0x1, 0x1)
    Sound(863, 0, 100, 0)
    EndChrThread(0x103, 0x3)
    SetChrSubChip(0x103, 0x0)
    EndChrThread(0xE, 0x1)
    OP_24(0x348)
    Sleep(800)
    OP_63(0x138, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x138, 0x0, 0x1F4)

    #C0230
    ChrTalk(
        0x138,
        "#5P#2900F好像已经结束了呢。\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x104,
        "#0305F噢……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 800, 20500, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(22500, 0)
    OP_0D()
    Sleep(500)

    #C0232
    ChrTalk(
        0x103,
        "#0200F#6P……情况如何？\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xA,
        "#11P我这边没发现异常。\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xA,
        "#11P你那边如何啦？\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)

    #C0235
    ChrTalk(
        0x9,
        "#5P找到了──就是这家伙！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(200)
    SetMapObjFrame(0xFF, "monita5_add", 0x1, 0x1)
    OP_0D()

    #C0236
    ChrTalk(
        0x9,
        (
            "#5P地下空间Ｂ区域\x01",
            "『第８控制终端』……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x9,
        "#5P好像是从这里进行访问的！\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x101,
        "#0001F地下空间……\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x104,
        (
            "#0301F就是位于站前街道角落的\x01",
            "那个地下区域吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x103,
        (
            "#0203F不，那个地方是\x01",
            "地下空间Ａ区域。\x02\x03",

            "#0201F而黑客使用的那个终端\x01",
            "在地下空间的Ｂ区域……\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xA,
        (
            "#11P那个，好像是城市西北部\x01",
            "的地下空间呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    Fade(500)
    OP_68(0, 500, 14500, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 0, -300, 17300, 0)
    BeginChrThread(0x103, 3, 0, 18)
    OP_68(0, 500, 12500, 2500)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    BeginChrThread(0x9, 3, 0, 20)
    BeginChrThread(0xA, 3, 0, 22)

    #C0242
    ChrTalk(
        0x102,
        (
            "#0103F#11P城市西北部……\x01",
            "也就是住宅街和欢乐街那一带啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0243
    ChrTalk(
        0x102,
        "#0101F#11P罗伊德，怎么办？\x02",
    )

    CloseMessageWindow()

    def lambda_6330():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6330)
    Sleep(150)
    TurnDirection(0x104, 0x101, 500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7522", 0)

    #C0244
    ChrTalk(
        0x101,
        (
            "#6P#0003F──赶快过去看看吧。\x02\x03",

            "#0001F地下空间的出入口应该是由\x01",
            "市政厅负责管理的。\x02\x03",

            "至于能不能借到钥匙，\x01",
            "我们就去问问那里的接待员吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x104,
        "#0300F嗯，那我们赶快出发吧。\x02",
    )

    CloseMessageWindow()
    OP_93(0x138, 0xB4, 0x1F4)
    Sleep(150)

    #C0246
    ChrTalk(
        0x138,
        (
            "#2904F呵呵……看起来，好像已经\x01",
            "逐渐迫近事件的核心了呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6441():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6441)
    Sleep(50)

    def lambda_6451():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6451)
    Sleep(50)
    OP_93(0x104, 0x0, 0x1F4)

    #C0247
    ChrTalk(
        0x101,
        (
            "#12P#0000F是啊……\x01",
            "真是多谢各位的帮助了。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        (
            "#0102F#11P谢谢你，贝尔，\x01",
            "还有两位研究员先生。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)

    def lambda_64D2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_64D2)
    Sleep(50)
    OP_93(0xA, 0xB4, 0x1F4)

    #C0249
    ChrTalk(
        0x9,
        "#5P哪、哪里……\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xA,
        (
            "#5P比起我们，还是这位小姑娘\x01",
            "发挥的作用更大呢。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_654B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_654B)
    Sleep(150)

    def lambda_655B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_655B)
    Sleep(50)

    def lambda_656B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_656B)

    def lambda_6578():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_6578)
    Sleep(50)
    OP_93(0x104, 0x10E, 0x1F4)

    #C0251
    ChrTalk(
        0x101,
        (
            "#12P#0004F说得也是啊……\x02\x03",

            "#0002F辛苦你了，缇欧，\x01",
            "多亏有你帮忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x102,
        "#0109F#11P呵呵，辛苦啦。\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x104,
        (
            "#0302F真不愧是阿缇，\x01",
            "立下了大功劳啊，真是可靠。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x103)

    #C0254
    ChrTalk(
        0x103,
        (
            "#6P#0205F嗯，那个……\x01",
            "这没什么了不起的。\x02\x03",

            "#0203F而且，我本来就是\x01",
            "特别任务支援科的一员……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x138,
        (
            "#11P#2909F呵呵……\x01",
            "已经非常了不起了哦。\x02\x03",

            "#2902F怎么样，缇欧。\x02\x03",

            "不如和艾莉一起来我这里\x01",
            "工作吧，意下如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x103,
        "#6P#0205F哎……？\x02",
    )

    CloseMessageWindow()

    def lambda_6725():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6725)
    Sleep(50)

    def lambda_6735():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6735)
    Sleep(50)
    OP_93(0x104, 0x0, 0x1F4)

    #C0257
    ChrTalk(
        0x102,
        "#0101F#11P等、等一下啦，贝尔……\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x104,
        (
            "#0302F哈哈……\x01",
            "怎么突然就开始挖墙角了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#12P#0012F那个，关于这点，希望您还是\x01",
            "放我们一马吧……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_67DC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_67DC)
    Sleep(100)
    OP_93(0x9, 0xB4, 0x1F4)

    #C0260
    ChrTalk(
        0x138,
        (
            "#2904F呵呵，只是开个玩笑啦。\x02\x03",

            "#2900F等到把事件顺利解决之后，\x01",
            "请一定要将具体过程告诉我啊。\x02\x03",

            "还有──\x01",
            "之前给你们的那张认证卡片，\x01",
            "就留在你们那里好了。\x02\x03",

            "最上层的区域随时都\x01",
            "欢迎你们来访，\x01",
            "如果有什么事，就过来看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x102,
        "#0104F#11P谢谢你了，贝尔。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        "#12P#0000F那我们就先告辞了。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "monita3_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita4_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita5_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita2_add", 0x2, "nomal")
    RemoveParty(0x37, 0x0)
    OP_D5(0x1E)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 700, -600, 13500, 0)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x9, 4700, -380, 22700, 45)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x8000)
    OP_4C(0xA, 0xFF)
    SetChrPos(0xA, -4700, -380, 22700, 315)
    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x8000)
    OP_68(0, 1100, 10300, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x0, 0, -600, 10300, 180)
    SetChrPos(0x1, 0, -600, 10300, 180)
    SetChrPos(0x2, 0, -600, 10300, 180)
    SetChrPos(0x3, 0, -600, 10300, 180)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x82, 7)
    OP_29(0x43, 0x1, 0x4)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x20A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7102")
    OP_24(0x348)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_4BF7 end

    def Function_13_6A66(): pass

    label("Function_13_6A66")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A92")
    SetChrSubChip(0x103, 0x0)
    Sleep(70)
    SetChrSubChip(0x103, 0x1)
    Sleep(70)
    SetChrSubChip(0x103, 0x2)
    Sleep(70)
    SetChrSubChip(0x103, 0x1)
    Sleep(70)
    Jump("Function_13_6A66")

    label("loc_6A92")

    Return()

    # Function_13_6A66 end

    def Function_14_6A93(): pass

    label("Function_14_6A93")


    def lambda_6A98():
        OP_95(0xFE, 0, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_6A98)

    def lambda_6AB2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_6AB2)
    WaitChrThread(0x138, 1)

    def lambda_6AC7():
        OP_95(0xFE, 0, -600, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_6AC7)
    WaitChrThread(0x138, 1)
    Return()

    # Function_14_6A93 end

    def Function_15_6AE1(): pass

    label("Function_15_6AE1")

    Sleep(800)

    def lambda_6AE9():
        OP_95(0xFE, -500, 0, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AE9)

    def lambda_6B03():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6B03)
    WaitChrThread(0x101, 1)

    def lambda_6B18():
        OP_95(0xFE, -500, -600, 11100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6B18)
    WaitChrThread(0x101, 1)
    Return()

    # Function_15_6AE1 end

    def Function_16_6B32(): pass

    label("Function_16_6B32")

    Sleep(1300)

    def lambda_6B3A():
        OP_95(0xFE, 500, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B3A)

    def lambda_6B54():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6B54)
    WaitChrThread(0x102, 1)

    def lambda_6B69():
        OP_95(0xFE, 500, -600, 11100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B69)
    WaitChrThread(0x102, 1)
    Return()

    # Function_16_6B32 end

    def Function_17_6B83(): pass

    label("Function_17_6B83")

    Sleep(1700)

    def lambda_6B8B():
        OP_95(0xFE, -500, 0, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6B8B)

    def lambda_6BA5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6BA5)
    WaitChrThread(0x103, 1)

    def lambda_6BBA():
        OP_95(0xFE, -1100, -600, 10100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6BBA)
    WaitChrThread(0x103, 1)
    Return()

    # Function_17_6B83 end

    def Function_18_6BD4(): pass

    label("Function_18_6BD4")

    OP_93(0x103, 0xB4, 0x1F4)

    def lambda_6BE0():
        OP_95(0xFE, 0, -600, 14700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6BE0)
    WaitChrThread(0x103, 1)

    def lambda_6BFE():
        OP_95(0xFE, -1400, -600, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6BFE)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x5A, 0x1F4)
    Return()

    # Function_18_6BD4 end

    def Function_19_6C1F(): pass

    label("Function_19_6C1F")

    Sleep(2200)

    def lambda_6C27():
        OP_95(0xFE, 500, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C27)

    def lambda_6C41():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6C41)
    Sleep(1000)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    WaitChrThread(0x104, 1)

    def lambda_6C74():
        OP_95(0xFE, 1100, -600, 10100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C74)
    WaitChrThread(0x104, 1)
    Return()

    # Function_19_6C1F end

    def Function_20_6C8E(): pass

    label("Function_20_6C8E")

    Fade(150)
    SetChrPos(0x9, 3500, -380, 21500, 45)
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_0D()

    def lambda_6CB2():
        OP_95(0xFE, 3500, -600, 16800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6CB2)
    WaitChrThread(0x9, 1)

    def lambda_6CD0():
        OP_95(0xFE, 1000, -600, 14300, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6CD0)
    WaitChrThread(0x9, 1)
    Return()

    # Function_20_6C8E end

    def Function_21_6CEA(): pass

    label("Function_21_6CEA")

    OP_93(0x9, 0x2D, 0x1F4)

    def lambda_6CF6():
        OP_95(0xFE, 3500, -600, 16800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6CF6)
    WaitChrThread(0x9, 1)

    def lambda_6D14():
        OP_95(0xFE, 3500, -480, 22200, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6D14)
    WaitChrThread(0x9, 1)
    Fade(250)
    SetChrPos(0x9, 4700, -380, 22700, 45)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    Return()

    # Function_21_6CEA end

    def Function_22_6D4D(): pass

    label("Function_22_6D4D")

    Fade(150)
    SetChrPos(0xA, -3500, -380, 21700, 315)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    OP_0D()

    def lambda_6D71():
        OP_95(0xFE, -3500, -600, 16800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6D71)
    WaitChrThread(0xA, 1)

    def lambda_6D8F():
        OP_95(0xFE, -1000, -600, 14300, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6D8F)
    WaitChrThread(0xA, 1)
    Return()

    # Function_22_6D4D end

    def Function_23_6DA9(): pass

    label("Function_23_6DA9")

    OP_93(0xA, 0x13B, 0x1F4)

    def lambda_6DB5():
        OP_95(0xFE, -3500, -600, 16800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6DB5)
    WaitChrThread(0xA, 1)

    def lambda_6DD3():
        OP_95(0xFE, -3500, -600, 22200, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6DD3)
    WaitChrThread(0xA, 1)
    Fade(250)
    SetChrPos(0xA, -4700, -380, 22700, 315)
    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Return()

    # Function_23_6DA9 end

    def Function_24_6E12(): pass

    label("Function_24_6E12")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E34")
    Sound(849, 0, 100, 0)
    Sleep(950)
    Sound(850, 0, 100, 0)
    Sleep(1750)
    Jump("Function_24_6E12")

    label("loc_6E34")

    Return()

    # Function_24_6E12 end

    def Function_25_6E35(): pass

    label("Function_25_6E35")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(1000)
    OP_68(700, 400, 12300, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x8, 700, -600, 13500, 180)
    SetChrPos(0x101, 700, -600, 11700, 0)
    SetChrPos(0x102, 1300, -600, 10600, 0)
    SetChrPos(0x103, -900, -600, 11300, 45)
    SetChrPos(0x104, -200, -600, 10400, 0)
    OP_0D()

    #C0263
    ChrTalk(
        0x8,
        (
            "#2904F#5P对了对了，虽然这只是\x01",
            "我的直觉而已，不过……\x02\x03",

            "#2902F我总觉得，发送邮件并非\x01",
            "那位『银』，而是另有他人呢。\x02\x03",

            "那人很明显是专业技术人员……\x01",
            "而且，很有可能是和爱普斯泰恩\x01",
            "财团有关的人物呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0264
    ChrTalk(
        0x101,
        "#0011F哎！？\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x102,
        "#0105F你、你怎么会知道那些呢！？\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x103,
        (
            "#6P#0203F……有道理呢，\x01",
            "我也是这么想的。\x02\x03",

            "如此精通导力网络技术的人\x01",
            "实在是屈指可数。\x02\x03",

            "#0208F而且，这种入侵手法，\x01",
            "好像曾在什么地方见过呢……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_70A5():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_70A5)
    Sleep(100)

    def lambda_70B5():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_70B5)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)

    #C0267
    ChrTalk(
        0x101,
        "#0001F#5P是吗……\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x8,
        (
            "#2904F#5P嗯，还有，\x01",
            "如果你们找到了那个黑客……\x02\x03",

            "#2902F我希望他今后也可以自由行动，\x01",
            "所以你们能不能放他一马呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7156():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7156)
    Sleep(100)

    def lambda_7166():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7166)
    Sleep(50)
    OP_93(0x104, 0x0, 0x1F4)

    #C0269
    ChrTalk(
        0x101,
        "#0005F哎？\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x102,
        "#0105F为、为什么呢……？\x02",
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x8,
        (
            "#2909F#5P如今尚未制定惩罚\x01",
            "黑客行为的相关法律。\x02\x03",

            "既然如此，放着他别管，\x01",
            "反而能起到一些作用，说不定可以\x01",
            "使我们的安全技术进一步提高呢。\x02\x03",

            "#2902F因为，若想实现银行业务的导力化，\x01",
            "防黑客对策也是必不可少的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0272
    ChrTalk(
        0x102,
        "#0106F呼……你可真是……\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x104,
        (
            "#12P#0302F哎呀呀……\x01",
            "与其说是大胆，不如说是豪气冲天呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 700, -600, 11500, 0)
    SetChrPos(0x8, 700, -600, 13500, 0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x83, 0)
    EventEnd(0x5)
    Return()

    # Function_25_6E35 end

    def Function_26_7360(): pass

    label("Function_26_7360")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_73F4")
    Jump("loc_743E")

    label("loc_73F4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7414")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_743E")

    label("loc_7414")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7434")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_743E")

    label("loc_7434")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_743E")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    #C0274
    ChrTalk(
        0xB,
        (
            "说起来……\x01",
            "那个改造魔导杖的事情\x01",
            "进行得怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xB,
        (
            "改造材料应该是\x01",
            "需要你们自己\x01",
            "来寻找的……\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x101,
        (
            "#0000F啊……对不起。\x02\x03",

            "我们也想收集素材，\x01",
            "但实在是没有时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xB,
        (
            "是吗，\x01",
            "那可真是遗憾啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xB,
        (
            "我本来还在想，在这种时候，\x01",
            "要是能强化一下缇欧的战斗力，\x01",
            "应该会对你们很有帮助的。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xB,
        (
            "我这边已经准备就绪了，\x01",
            "如果以后想要改造的话，\x01",
            "和基约姆说一声就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xB,
        (
            "他应该也随身携带着\x01",
            "他那些谋生工具呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x31, 0x1, 0x2)
    SetChrSubChip(0xB, 0x0)
    TalkEnd(0xB)
    Return()

    # Function_26_7360 end

    def Function_27_7602(): pass

    label("Function_27_7602")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch29300.itc", 0x28)
    LoadChrToIndex("chr/ch26400.itc", 0x29)
    LoadChrToIndex("chr/ch00200.itc", 0x2A)
    OP_68(-200, 1100, 12300, 0)
    MoveCamera(23, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13040, 0)
    SetChrPos(0x101, -70, -600, 12460, 45)
    SetChrPos(0xC, -1120, -600, 12910, 90)
    SetChrPos(0xB, -80, -600, 14300, 225)
    SetChrPos(0xD, 1130, -600, 13670, 225)
    SetChrChipByIndex(0xC, 0x2A)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xD, 0x29)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0281
    ChrTalk(
        0xD,
        (
            "材料已经确认完毕了。\x01",
            "我这边没问题了。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xB,
        "好，已经准备万全了啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)

    #C0283
    ChrTalk(
        0xB,
        (
            "呵呵，真是期待啊～\x01",
            "缇欧手持新型魔导杖的飒爽英姿，\x01",
            "仿佛已经浮现在眼前了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xC,
        (
            "#0200F……主任。\x02\x03",

            "魔导杖要是改造失败，出现故障\x01",
            "导致无法使用的话，\x01",
            "我可是会恨你的哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0xB, 0x13B, 0x1F4)
    Sleep(300)

    #C0285
    ChrTalk(
        0xB,
        (
            "怎、怎么会……\x01",
            "竟然要被缇欧憎恨一生……\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xB,
        (
            "呜哇～……！\x01",
            "我、我为什么要经受如此残酷的事情……！\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#0000F#2P主任先生，现在还没发生\x01",
            "任何情况呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 500)
    Sleep(300)

    #C0288
    ChrTalk(
        0xD,
        "罗伯兹，清醒一点。\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0289
    ChrTalk(
        0xB,
        "哈……！？\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0xE1, 0x190)
    OP_93(0xD, 0xE1, 0x1F4)
    Sleep(300)

    #C0290
    ChrTalk(
        0xB,
        (
            "抱、抱歉，\x01",
            "那就赶快开始吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xB,
        (
            "罗伊德，请你\x01",
            "稍等一下啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        (
            "#0000F#2P嗯，那我就\x01",
            "在一旁参观学习了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(800)
    SetChrName("")

    #A0293
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德就这么\x01",
            "等了三十分钟左右。\x02",
        )
    )

    CloseMessageWindow()

    #A0294
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "虽然对具体过程不甚了解，\x01",
            "但魔导杖的改造工作\x01",
            "似乎进展得非常顺利。\x02",
        )
    )

    CloseMessageWindow()

    #A0295
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "随后──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x101, -4700, 0, -620, 90)
    SetChrPos(0xC, 1960, 0, -560, 270)
    SetChrPos(0xB, 1140, 0, 1320, 180)
    SetChrPos(0xD, 3470, 0, 1260, 225)
    OP_68(1050, 1700, -1130, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(20500, 0)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00257.itc", 0x1F)
    LoadChrToIndex("chr/ch0025A.itc", 0x20)
    LoadEffect(0x0, "battle\\cr002403.eff")
    LoadEffect(0x1, "battle\\cr002401.eff")
    SetChrChipByIndex(0xC, 0x1E)
    BeginChrThread(0xC, 0, 0, 28)
    SetCameraDistance(25500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(3000)
    EndChrThread(0xC, 0x0)
    SetChrChipByIndex(0xC, 0x1F)
    OP_A0(0xC, 1500, 0x0, 0x2)
    Sleep(300)
    OP_A0(0xC, 1500, 0x2, 0x3)
    Sound(279, 0, 100, 0)
    SetChrSubChip(0xC, 0x4)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xC, 0xC0, 200, 700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(363, 0, 100, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xC, 0xC0, 200, 700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(274, 0, 100, 0)
    Sleep(100)
    Fade(300)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    Sleep(2500)
    PlayEffect(0x1, 0xFF, 0xC, 0xC0, 200, 550, 850, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sound(280, 0, 90, 0)
    Sound(323, 0, 90, 0)
    Sleep(4500)
    Fade(300)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    BeginChrThread(0xC, 0, 0, 28)
    OP_0D()
    Sleep(1000)

    #C0296
    ChrTalk(
        0xC,
        "#0200F这个嘛……\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1200)
    Fade(300)
    SetChrChipByIndex(0xC, 0x2A)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    OP_0D()
    TurnDirection(0xC, 0xB, 500)
    Sleep(300)

    #C0297
    ChrTalk(
        0xC,
        (
            "#0200F因为基本程序已经更新了，\x01",
            "所以稍微有点不太适应，\x01",
            "不过感觉并不差。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xB,
        (
            "肯定是重心控制的问题，\x01",
            "我相信缇欧很快就会习惯的。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xB,
        (
            "想换用其它魔导杖的话，\x01",
            "就利用永世系统把\x01",
            "新程序复制过去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xB,
        (
            "另外也不要忘记把可装卸式\x01",
            "的新组件装上去哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xC,
        "#0200F了解。\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xD,
        (
            "话说回来……\x01",
            "使用这里的主装置，工作效率\x01",
            "果然快了很多了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 400)
    Sleep(300)

    #C0303
    ChrTalk(
        0xD,
        (
            "我准备暂时留在\x01",
            "这个地方了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)
    Sleep(300)

    #C0304
    ChrTalk(
        0xB,
        (
            "呵呵，魔导杖的核心系统\x01",
            "已经顺利备份了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xB,
        (
            "接下来我还会尝试\x01",
            "进一步提高它的性能～\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xC,
        (
            "#0200F虽然并不想\x01",
            "太依靠主任……\x02\x03",

            "但多亏了您的帮助，\x01",
            "程序简化了７％左右。\x01",
            "真想赶快在实战中试一试。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7E54():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7E54)

    def lambda_7E61():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7E61)
    Sleep(200)

    #C0307
    ChrTalk(
        0xB,
        (
            "啊，缇欧，\x01",
            "你果然也是这样想的啊～¤\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(70)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(70)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(300)
    Fade(800)
    OP_68(-3750, 1700, -1220, 0)
    MoveCamera(41, 28, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(21140, 0)
    OP_0D()

    #C0308
    ChrTalk(
        0x101,
        (
            "#0000F真、真是见识到了\x01",
            "一次惊人的改造过程呢……\x02\x03",

            "那个……缇欧，\x01",
            "情况还算顺利吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xC, 0x101, 400)

    def lambda_7FBE():
        OP_95(0xFE, -2500, 0, -380, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7FBE)
    Sleep(800)

    def lambda_7FDB():
        OP_95(0xFE, -1120, 0, 810, 1200, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7FDB)
    Sleep(100)
    BeginChrThread(0xD, 1, 0, 29)
    WaitChrThread(0xC, 1)

    #C0309
    ChrTalk(
        0xC,
        (
            "#0200F#2P嗯，改造已经全部结束了。\x01",
            "至于性能方面，似乎也能发挥出\x01",
            "预期的威力。\x02\x03",

            "可以发射绝对零度的反能源弹，其名为\x01",
            "──『绝对零度』。\x02\x03",

            "虽然无法频繁使用，\x01",
            "但在重要的战斗中\x01",
            "应该能发挥些作用。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x101,
        (
            "#0000F是吗……那真是令人信心百倍呢。\x02\x03",

            "（如果要说真心话，\x01",
            "  我是希望你不要参与\x01",
            "  那些太过危险的战斗……）\x02\x03",

            "缇欧，虽然现在情况不容乐观，但还是要努力啊。\x01",
            "因为大家都很依赖你呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xC,
        (
            "#0200F#2P──呵呵，明白。\x02\x03",

            "现在的我，已经有了\x01",
            "想要守护的人……\x02\x03",

            "罗伊德前辈，我们互相加油，\x01",
            "一起全力以赴吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        "#0000F是啊……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    AddCraft(0x2, 0xAE)
    SubItemNumber(0x397, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -750, 0, 630, 180)
    SetChrPos(0xB, 0, 0, 18240, 0)
    SetChrPos(0xC, -4700, -380, 22700, 315)
    SetChrChipByIndex(0xB, 0x5)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x6)
    SetChrSubChip(0xC, 0x0)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8279")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8279")
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)

    label("loc_8279")

    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_29(0x31, 0x4, 0x10)
    OP_29(0x31, 0x1, 0x3)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_27_7602 end

    def Function_28_8294(): pass

    label("Function_28_8294")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_82AB")
    OP_A0(0xC, 1200, 0x0, 0x4)
    Jump("Function_28_8294")

    label("loc_82AB")

    Return()

    # Function_28_8294 end

    def Function_29_82AC(): pass

    label("Function_29_82AC")

    OP_95(0xFE, -750, 0, -990, 1200, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Return()

    # Function_29_82AC end

    def Function_30_82C8(): pass

    label("Function_30_82C8")

    EventBegin(0x1)

    #C0313
    ChrTalk(
        0x138,
        (
            "#2905F啊呀，你们不是\x01",
            "要去终端室吗？\x02\x03",

            "#2900F主终端就在前面呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x101,
        (
            "#0005F啊……不好意思。\x01",
            "是在楼梯下面吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 67810, 10000, 23760, 270)
    EventEnd(0x4)
    Return()

    # Function_30_82C8 end

    SaveToFile()

Try(main)
