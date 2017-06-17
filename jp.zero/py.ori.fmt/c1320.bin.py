from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "マリアベル",             # 1
        "研究員クレイ",           # 2
        "研究員ダビッド",         # 3
        "ロバーツ主任",           # 4
        "ティオ",                 # 5
        "ギヨーム親方",           # 6
        "SE制御",                 # 7
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
        "Function_5_1DBB",         # 05, 5
        "Function_6_3508",         # 06, 6
        "Function_7_3A85",         # 07, 7
        "Function_8_3FD1",         # 08, 8
        "Function_9_461D",         # 09, 9
        "Function_10_493A",        # 0A, 10
        "Function_11_4B02",        # 0B, 11
        "Function_12_4F15",        # 0C, 12
        "Function_13_6F9A",        # 0D, 13
        "Function_14_6FC7",        # 0E, 14
        "Function_15_7015",        # 0F, 15
        "Function_16_7066",        # 10, 16
        "Function_17_70B7",        # 11, 17
        "Function_18_7108",        # 12, 18
        "Function_19_7153",        # 13, 19
        "Function_20_71C2",        # 14, 20
        "Function_21_721E",        # 15, 21
        "Function_22_7281",        # 16, 22
        "Function_23_72DD",        # 17, 23
        "Function_24_7346",        # 18, 24
        "Function_25_7369",        # 19, 25
        "Function_26_7906",        # 1A, 26
        "Function_27_7BEE",        # 1B, 27
        "Function_28_8966",        # 1C, 28
        "Function_29_897E",        # 1D, 29
        "Function_30_899A",        # 1E, 30
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_END)), "loc_856")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_77F")

    #C0001
    ChrTalk(
        0xFE,
        "導力ネットの復旧なら任せてくれ。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "こう見えても僕らは\x01",
            "導力ネットの管理者だからね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84A")

    label("loc_77F")


    #C0003
    ChrTalk(
        0xFE,
        (
            "第二次テスト用に開発していた\x01",
            "演算システムが役に立ちそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "こいつは複雑化した\x01",
            "大規模ネットワーク用に\x01",
            "最適化されてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "誰が遮断してるのか知らないが……\x01",
            "見てろ、絶対裏をかいてやる！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_84A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1DBA")

    label("loc_856")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A8A")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F3")
    Jump("loc_93D")

    label("loc_8F3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_913")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_93D")

    label("loc_913")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_933")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_93D")

    label("loc_933")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_93D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9D4")

    #C0006
    ChrTalk(
        0xFE,
        (
            "予定より早く完成させて\x01",
            "お嬢様を驚かせてやろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "うん、きっと\x01",
            "褒めてもらえるに違いないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7E")

    label("loc_9D4")


    #C0008
    ChrTalk(
        0xFE,
        (
            "大規模ネットワーク用に\x01",
            "特化したシステムを作っているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "これが完成すれば\x01",
            "第二次テストにも耐えられるはず……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "ようやくお嬢様にも\x01",
            "認めてもらえそうだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_A7E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1DBA")

    label("loc_A8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C29")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B27")
    Jump("loc_B71")

    label("loc_B27")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B47")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B71")

    label("loc_B47")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B67")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B71")

    label("loc_B67")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B71")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0011
    ChrTalk(
        0xFE,
        (
            "主任が手伝ってくれるとは\x01",
            "ありがたいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "主任は導力ネットワークの設計にも\x01",
            "ずっと携わってきた専門家なんだ。\x01",
            "いやあ、心強いな！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1DBA")

    label("loc_C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_E1C")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CC6")
    Jump("loc_D10")

    label("loc_CC6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CE6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D10")

    label("loc_CE6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D06")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D10")

    label("loc_D06")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D10")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D76")

    #C0013
    ChrTalk(
        0xFE,
        (
            "お嬢様の期待に\x01",
            "応えられるよう頑張らないとね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E10")

    label("loc_D76")


    #C0014
    ChrTalk(
        0xFE,
        (
            "導力ネットの運用も\x01",
            "安定してきたからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "そろそろ第二次テストの\x01",
            "準備を進めているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "よーし、待ってろ……\x01",
            "すぐに計画書を纏めてやるぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_E10")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1DBA")

    label("loc_E1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_106A")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EB9")
    Jump("loc_F03")

    label("loc_EB9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ED9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F03")

    label("loc_ED9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EF9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F03")

    label("loc_EF9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F03")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FB0")

    #C0017
    ChrTalk(
        0xFE,
        (
            "ハッカーがあれだけ暴れても\x01",
            "ネットワークはびくともしなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "導力ネットもようやく\x01",
            "安定した運用が出来そうだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_105E")

    label("loc_FB0")


    #C0019
    ChrTalk(
        0xFE,
        (
            "先日のハッカー達のお陰で\x01",
            "ネットワークの負荷データは取れたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "これで導力ネットも\x01",
            "安定した運用が出来そうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "マリアベルお嬢様には\x01",
            "色々叱られちゃったけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_105E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1DBA")

    label("loc_106A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1169")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_115E")

    #C0022
    ChrTalk(
        0xFE,
        (
            "昨日の夕方、どうやらハッカーが\x01",
            "ネット上を走り回っていたらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "その、その過程を追跡していたら\x01",
            "色々見つけちゃってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "べ、別にサボってたわけじゃなくて、\x01",
            "ハッカーのデータを\x01",
            "取っていただけなんだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1161")

    label("loc_115E")

    Call(0, 10)

    label("loc_1161")

    TalkEnd(0xFE)
    Jump("loc_1DBA")

    label("loc_1169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_13BB")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1206")
    Jump("loc_1250")

    label("loc_1206")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1226")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1250")

    label("loc_1226")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1246")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1250")

    label("loc_1246")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1250")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 3)), scpexpr(EXPR_END)), "loc_13AC")

    #C0025
    ChrTalk(
        0xFE,
        (
            "他にも雑多な情報ファイルが\x01",
            "流れていて、その中から見つけたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "どうやらどこかの\x01",
            "ハッカーの仕業みたいだが……\x01",
            "一体何のために……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "…………とりあえず一枚\x01",
            "プリントアウトしておこうかな。\x02",
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
    Jump("loc_13AF")

    label("loc_13AC")

    Call(0, 9)

    label("loc_13AF")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1DBA")

    label("loc_13BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1683")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1458")
    Jump("loc_14A2")

    label("loc_1458")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1478")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14A2")

    label("loc_1478")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1498")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14A2")

    label("loc_1498")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14A2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1552")

    #C0028
    ChrTalk(
        0xFE,
        (
            "導力ネットワークは\x01",
            "実に研究しがいのあるシステムだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "スカウトしてくれたお嬢様に\x01",
            "報いるためにも\x01",
            "頑張らなくちゃね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1677")

    label("loc_1552")


    #C0030
    ChrTalk(
        0xFE,
        (
            "僕は元々大学の\x01",
            "研究機関にいたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "でもある日マリアベルお嬢様が現れてね、\x01",
            "ＩＢＣ技術部にスカウトしてくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "ＩＢＣの導力ネットワーク構想は\x01",
            "世界中の端末を繋いで\x01",
            "一瞬で顧客情報をやりとりできる……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "そんな話を聞かされてさ、\x01",
            "いてもたっても\x01",
            "いられなくなったんだよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1677")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1DBA")

    label("loc_1683")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_18F0")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1720")
    Jump("loc_176A")

    label("loc_1720")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1740")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_176A")

    label("loc_1740")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1760")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_176A")

    label("loc_1760")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_176A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_182E")

    #C0034
    ChrTalk(
        0xFE,
        (
            "最近じゃ導力ネットに参加する企業も\x01",
            "増えてきているからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "端末数が増えた所に\x01",
            "記念祭で怒涛の情報量……\x01",
            "これは何か対策を取らないとな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E4")

    label("loc_182E")


    #C0036
    ChrTalk(
        0xFE,
        (
            "参ったな……記念祭に合わせて\x01",
            "大量の情報が行き来しているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        "うーん、想定外の事態だよ。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "このままじゃネットワーク全体が\x01",
            "不安定になってしまう。\x01",
            "何とかしないとな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_18E4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1DBA")

    label("loc_18F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1B57")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_198D")
    Jump("loc_19D7")

    label("loc_198D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19AD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19D7")

    label("loc_19AD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19CD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19D7")

    label("loc_19CD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19D7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A8C")

    #C0039
    ChrTalk(
        0xFE,
        (
            "エプスタイン財団のロバーツ氏は\x01",
            "導力ネットの開発主任の一人なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "技術顧問として、僕らもよく\x01",
            "知恵をお借りしてるんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B4B")

    label("loc_1A8C")


    #C0041
    ChrTalk(
        0xFE,
        "ふう、これは厄介だよ。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "例のハッカーは\x01",
            "システムの基礎コードを\x01",
            "巧みに利用して侵入したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "これは僕たちだけじゃ荷が重い。\x01",
            "……財団のロバーツ主任に\x01",
            "応援を頼んだ方がいいかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1B4B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1DBA")

    label("loc_1B57")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BEB")
    Jump("loc_1C35")

    label("loc_1BEB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C0B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C35")

    label("loc_1C0B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C2B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C35")

    label("loc_1C2B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C35")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1CE9")

    #C0044
    ChrTalk(
        0xFE,
        (
            "しかもお嬢様の前で\x01",
            "失態が明らかになるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "くそっ、すぐに\x01",
            "原因を突き止めてやる……！\x01",
            "（カタカタカタタタタ……！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB3")

    label("loc_1CE9")


    #C0046
    ChrTalk(
        0xFE,
        (
            "ＩＢＣのターミナルポイントが\x01",
            "外部から不正利用されていたなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "め、面目ない。\x01",
            "こんなこと実用化後に起きたら\x01",
            "許されないことだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "急いで原因を突き止めて\x01",
            "対策を取らないとな……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_1DB3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)

    label("loc_1DBA")

    Return()

    # Function_4_60A end

    def Function_5_1DBB(): pass

    label("Function_5_1DBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_END)), "loc_1E49")
    TalkBegin(0xFE)

    #C0049
    ChrTalk(
        0xFE,
        (
            "フッ、ここのマシンパワーは\x01",
            "こんな時のために存在するんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "俺たちに任せてくれ！\x01",
            "必ず迂回ルートを構築してやるぜ！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_3507")

    label("loc_1E49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_20F3")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1EE6")
    Jump("loc_1F30")

    label("loc_1EE6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F06")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F30")

    label("loc_1F06")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F26")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F30")

    label("loc_1F26")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F30")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1FDA")

    #C0051
    ChrTalk(
        0xFE,
        (
            "クレイの奴と\x01",
            "新システムを組み上げてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "今のシステムは\x01",
            "あちこちバグがあるからなぁ……\x01",
            "見直すとへこむよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E7")

    label("loc_1FDA")


    #C0053
    ChrTalk(
        0xFE,
        (
            "最近気付いたんだが、\x01",
            "不思議な動きをするノードがあるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "ハッキングみたいなんだが\x01",
            "悪さをするでもなく\x01",
            "ただネット上を眺めてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "うーん、これどこの端末だ？\x01",
            "……『マインツ山道』……\x01",
            "……『ローゼンベルク工房』？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "ちっ……また\x01",
            "どっかがバグってるぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_20E7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_3507")

    label("loc_20F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2293")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2190")
    Jump("loc_21DA")

    label("loc_2190")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_21B0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21DA")

    label("loc_21B0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21D0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21DA")

    label("loc_21D0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21DA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0057
    ChrTalk(
        0xFE,
        (
            "今日はマリアベルお嬢様が\x01",
            "妙にぷりぷりしておられるんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        "何かあったのか？\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "地下に篭ってると\x01",
            "世情に疎くなっていけないぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_3507")

    label("loc_2293")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2511")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2330")
    Jump("loc_237A")

    label("loc_2330")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2350")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_237A")

    label("loc_2350")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2370")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_237A")

    label("loc_2370")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_237A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2459")

    #C0060
    ChrTalk(
        0xFE,
        (
            "第二次テストじゃ、\x01",
            "これまで以上に対象を広げて\x01",
            "接続端末数を増やす予定なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "それに耐えうる新システムの開発が\x01",
            "必要になるんだが……\x01",
            "ここまで来たらやるしかねえよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2505")

    label("loc_2459")


    #C0062
    ChrTalk(
        0xFE,
        (
            "お嬢様に第二次テストの打診をしたら\x01",
            "乗り気になってくれたんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "これで根詰めて\x01",
            "改良を重ねてきた甲斐があったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "うっし、早速データ収集だ。\x01",
            "バリバリやるか！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2505")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_3507")

    label("loc_2511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2748")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25AE")
    Jump("loc_25F8")

    label("loc_25AE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_25CE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25F8")

    label("loc_25CE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25EE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25F8")

    label("loc_25EE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25F8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2678")

    #C0065
    ChrTalk(
        0xFE,
        (
            "やっぱ個人情報ってのは難しいよな……\x01",
            "ハッカー対策が必要になるわけだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_273C")

    label("loc_2678")


    #C0066
    ChrTalk(
        0xFE,
        (
            "……導力ネット上に流れていた\x01",
            "不謹慎な情報ファイルは、\x01",
            "全て抹消することになったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        "やっぱ個人情報ってのは難しいよな……\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "お陰でマリアベルお嬢さまにも\x01",
            "こっぴどく叱られちまったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_273C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_3507")

    label("loc_2748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_28BE")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_28B3")

    #C0069
    ChrTalk(
        0xFE,
        (
            "じ、実は導力ネット上で\x01",
            "興味深い……もとい\x01",
            "不謹慎な画像データを見つけたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "や、やっぱり\x01",
            "お嬢様に報告すべきだったか……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "お嬢様が学生の頃の\x01",
            "ナイスバディな水着写真だもんな……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28AE")

    #C0072
    ChrTalk(
        0x101,
        (
            "#0005F（まさか……\x01",
            "  昨日のヨナの仕業か？）\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x103,
        (
            "#0200F（そういえばエサを撒くとか\x01",
            "  言っていましたね。\x01",
            "  その一部かもしれません。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28AE")

    Jump("loc_28B6")

    label("loc_28B3")

    Call(0, 10)

    label("loc_28B6")

    TalkEnd(0xFE)
    Jump("loc_3507")

    label("loc_28BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2A2B")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 3)), scpexpr(EXPR_END)), "loc_2A20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2985")

    #C0074
    ChrTalk(
        0xFE,
        (
            "……おいクレイ、ずるいぞ。\x01",
            "俺の分もプリントアウトしてくれ。\x02",
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
    Jump("loc_2A1B")

    label("loc_2985")


    #C0075
    ChrTalk(
        0xFE,
        (
            "お願いだからお嬢様には\x01",
            "内緒にしておいてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "その、きっと叱られると思うんだ。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x103,
        "#0200F別にいいですけど……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    OP_9E(0xA, 0x0, 0x0, 0xAFC8, 0x0, 0x0)
    SetChrFlags(0xA, 0x10)

    label("loc_2A1B")

    Jump("loc_2A23")

    label("loc_2A20")

    Call(0, 9)

    label("loc_2A23")

    TalkEnd(0xFE)
    Jump("loc_3507")

    label("loc_2A2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2CE1")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AC8")
    Jump("loc_2B12")

    label("loc_2AC8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2AE8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B12")

    label("loc_2AE8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B08")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B12")

    label("loc_2B08")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B12")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2BD8")

    #C0078
    ChrTalk(
        0xFE,
        (
            "実は今朝からハッカーが\x01",
            "活発に動き回ってるみたいなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "よし、追跡してデータを取ってやるか。\x01",
            "ハッカー対策の第一歩は\x01",
            "データ収集だからな！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD5")

    label("loc_2BD8")


    #C0080
    ChrTalk(
        0xFE,
        (
            "導力ネットは\x01",
            "研究段階のシステムだから、\x01",
            "色んなトラブルが起こるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "ハッキング、なんてのも\x01",
            "その１つだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "レマン自治州にも\x01",
            "研究機関同士をつなげた\x01",
            "ネットワークがあるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "ハッキングしようなんて\x01",
            "考える人間はいないからなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2CD5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_3507")

    label("loc_2CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2F53")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D7E")
    Jump("loc_2DC8")

    label("loc_2D7E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D9E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2DC8")

    label("loc_2D9E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2DBE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2DC8")

    label("loc_2DBE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2DC8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2E85")

    #C0084
    ChrTalk(
        0xFE,
        (
            "だが、俺たち管理者が踏ん張らねえと\x01",
            "導力ネットが落ちちまうしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "……そうなったらお嬢様に……\x01",
            "……考えるだけで恐ろしいぜ…………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F47")

    label("loc_2E85")


    #C0086
    ChrTalk(
        0xFE,
        (
            "導力ネットってのは\x01",
            "安定した運用をするだけでも\x01",
            "結構大変なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "……実は昨日も\x01",
            "演算装置が１つ落ちちまってね。\x01",
            "徹夜で復旧作業だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "外は記念祭だってのに\x01",
            "ちょっと空しいよなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2F47")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_3507")

    label("loc_2F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_30B8")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2FC9")

    #C0089
    ChrTalk(
        0xA,
        (
            "早いこと対策を取らないと\x01",
            "またマリアベルお嬢様に叱られるぜ……\x01",
            "い、急がなくちゃな………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B0")

    label("loc_2FC9")


    #C0090
    ChrTalk(
        0xA,
        (
            "うーん、こんな所から\x01",
            "侵入したのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xA,
        (
            "でもこれって\x01",
            "ソースコードを知ってないと\x01",
            "絶対無理じゃないのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x9,
        (
            "ああ、まったくだよ。\x01",
            "どうやって嗅ぎ付けたんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "ハッカーって本当に\x01",
            "システムを熟知しているなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xA, 0x10)

    label("loc_30B0")

    TalkEnd(0xFE)
    Jump("loc_3507")

    label("loc_30B8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_314C")
    Jump("loc_3196")

    label("loc_314C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_316C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3196")

    label("loc_316C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_318C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3196")

    label("loc_318C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3196")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_33B3")

    #C0094
    ChrTalk(
        0xFE,
        (
            "というか……何とかできないと\x01",
            "またマリアベルお嬢様に……\x01",
            "…………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "……いや、何でもないさ。\x01",
            "聞かなかったことにしてくれ。\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32F1")

    #C0096
    ChrTalk(
        0x101,
        "#0005F（き、気になるなぁ……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_33AE")

    label("loc_32F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_333D")

    #C0097
    ChrTalk(
        0x102,
        (
            "#0106F（ベルったら、また\x01",
            "  部下の人をいじめて……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33AE")

    label("loc_333D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_337C")

    #C0098
    ChrTalk(
        0x103,
        "#0200F（……何かされるのでしょうか。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_33AE")

    label("loc_337C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33AE")

    #C0099
    ChrTalk(
        0x104,
        "#0300F（ははは、怖えなぁ……）\x02",
    )

    CloseMessageWindow()

    label("loc_33AE")

    Jump("loc_3500")

    label("loc_33B3")


    #C0100
    ChrTalk(
        0xFE,
        "しかしぶったまげたな……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "あんなトレースの仕方、\x01",
            "初めて見たぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x103,
        (
            "#0203F……魔導杖に付属する\x01",
            "《エイオンシステム》のお陰です。\x01",
            "わたしの能力ではありません。\x02\x03",

            "#0200Fそれより、ここは任せてしまっても？\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "ああ、助かったぜ。\x01",
            "後は俺たちで何とかする。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "まあ任せてくれ。\x01",
            "これでも導力ネットシステムの\x01",
            "研究員なんだからさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3500")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)

    label("loc_3507")

    Return()

    # Function_5_1DBB end

    def Function_6_3508(): pass

    label("Function_6_3508")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x397, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_353F")
    Call(0, 26)
    Return()

    label("loc_353F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_END)), "loc_37AF")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_35DC")
    Jump("loc_3626")

    label("loc_35DC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_35FC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3626")

    label("loc_35FC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_361C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3626")

    label("loc_361C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3626")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_36B7")

    #C0105
    ChrTalk(
        0xFE,
        (
            "導力ネットの方は\x01",
            "僕たちに任せてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "数時間もあれば\x01",
            "何とか復旧してみせるよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A3")

    label("loc_36B7")


    #C0107
    ChrTalk(
        0xFE,
        (
            "導力ネットの方は\x01",
            "僕たちに任せてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "僕の解析では、どうやら\x01",
            "導力ケーブルに妨害波を流し込む装置が\x01",
            "取り付けられているようなんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "ここのスタッフは優秀だからね。\x01",
            "うん、数時間もあれば\x01",
            "何とか復旧できるはずだよ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_37A3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_3A84")

    label("loc_37AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3844")

    #C0110
    ChrTalk(
        0xFE,
        (
            "ふんふふ～ん……♪\x01",
            "（パシャシャ、パシャシャシャ……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        (
            "#0005F（キーボードを打つ指が見えない……\x01",
            "  どうなってるんだ……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A81")

    label("loc_3844")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_38D8")
    Jump("loc_3922")

    label("loc_38D8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_38F8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3922")

    label("loc_38F8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3918")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3922")

    label("loc_3918")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3922")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0112
    ChrTalk(
        0xFE,
        (
            "ちょっとＩＢＣの人に\x01",
            "頼まれてしまってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "導力ネット第二次テストのために\x01",
            "新システムを組んでいる所なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#0000F（財団の主任さん……今日は\x01",
            "  難しい仕事をしてるみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        (
            "#0203F（黙って仕事をしている分には\x01",
            "  相当優秀なはずです。）\x02\x03",

            "#0200F（一応、世界屈指の\x01",
            "  頭脳集団の１人なので。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetScenarioFlags(0x0, 2)

    label("loc_3A81")

    TalkEnd(0xFE)

    label("loc_3A84")

    Return()

    # Function_6_3508 end

    def Function_7_3A85(): pass

    label("Function_7_3A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3D54")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3B87")

    #C0116
    ChrTalk(
        0x8,
        (
            "#2904Fまあ、技術的な問題は\x01",
            "近いうちにクリアできるでしょう。\x02\x03",

            "#2900Fうちの技術スタッフは\x01",
            "定期的に叱ってやれば\x01",
            "優秀な働きをしますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        "#0000Fそ、そうなんですか……\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x102,
        (
            "#0106F（ベルが口にすると\x01",
            "  微妙に女王様なのよね……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D4C")

    label("loc_3B87")


    #C0119
    ChrTalk(
        0x8,
        "#2903Fふむ、中々難しいですわね。\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x102,
        "#0105Fベル、どうかしたの？\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        (
            "#0006Fというか相変わらず\x01",
            "凄い部屋ですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "#2900Fふふ、実は導力ネットワークの\x01",
            "第二次テストを計画していますの。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x103,
        (
            "#0200F第二次テスト……\x01",
            "一般市民を対象とした\x01",
            "導力端末の本格普及ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        (
            "#2903Fええ、もっとも\x01",
            "端末の一般販売などは\x01",
            "まだまだ先の話ですわ。\x02\x03",

            "今考えているのは\x01",
            "より大規模なネットワークの構築……\x02\x03",

            "#2900F色々と壁はありますけど\x01",
            "挑戦しがいのある課題ですわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3D4C")

    TalkEnd(0x8)
    Jump("loc_3FD0")

    label("loc_3D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3EDD")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3ED2")
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0125
    ChrTalk(
        0x102,
        (
            "#0103Fベル、あまり部下の人たちを\x01",
            "いじめるのは……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "#2905Fあら、別にいじめている\x01",
            "わけではありませんわ。\x02\x03",

            "#2904F……そうですわね？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 300)
    TurnDirection(0xA, 0x0, 300)

    #N0127
    NpcTalk(
        0x9,
        "クレイ＆ダビッド",
        "はいっ、もちろんですっ！\x02",
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
    Jump("loc_3ED5")

    label("loc_3ED2")

    Call(0, 10)

    label("loc_3ED5")

    TalkEnd(0x8)
    Jump("loc_3FD0")

    label("loc_3EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EF3")
    Call(0, 25)
    Jump("loc_3FD0")

    label("loc_3EF3")

    TalkBegin(0x8)

    #C0128
    ChrTalk(
        0x8,
        (
            "#2900Fどうやらハッカーは\x01",
            "ジオフロントのＢ区画に\x01",
            "いるようですわね。\x02\x03",

            "#2903Fジオフロントは\x01",
            "市庁舎の管理下ですから\x01",
            "まずは話を通す必要があるでしょう。\x02\x03",

            "#2900Fふふ、事件が無事解決したら\x01",
            "是非顛末を教えてくださいな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_3FD0")

    Return()

    # Function_7_3A85 end

    def Function_8_3FD1(): pass

    label("Function_8_3FD1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4065")
    Jump("loc_40AF")

    label("loc_4065")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4085")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40AF")

    label("loc_4085")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40A5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40AF")

    label("loc_40A5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_40AF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 3)), scpexpr(EXPR_END)), "loc_43A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42CC")

    #C0129
    ChrTalk(
        0xC,
        "#0205Fあ、ロイドさん。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        (
            "#0002Fティオ、さっそく\x01",
            "手伝ってるみたいだな。\x02\x03",

            "ヨナと連絡を取るって言ってたけど、\x01",
            "何とかなりそうなのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xC,
        (
            "#0204Fそうですね……\x02\x03",

            "#0202Fヨナはハッキングのために\x01",
            "あちこちの制御端末に\x01",
            "バックドアを仕掛けています。\x02\x03",

            "そのどれかにアクセスできれば\x01",
            "状況を伝える事ができるかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#0000Fな、なるほど……\x01",
            "外と連絡が取れるって事だな？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xC,
        (
            "#0204Fええ、まだ試している段階ですが。\x02\x03",

            "#0202F……こんな時こそ\x01",
            "日頃の借りを返してもらおうかと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE4, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_439E")

    label("loc_42CC")


    #C0134
    ChrTalk(
        0xC,
        (
            "#0204F……こちらの手伝いは\x01",
            "わたし一人でも十分です。\x02\x03",

            "#0202Fロイドさんは補給を済ませたら\x01",
            "少しでも休んでください。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_439E")

    #C0135
    ChrTalk(
        0x101,
        (
            "#0004Fああ、ありがとう。\x02\x03",

            "#0002Fティオもあんまり\x01",
            "根を詰めないでくれよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_439E")

    Jump("loc_4615")

    label("loc_43A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_458D")

    #C0136
    ChrTalk(
        0x101,
        (
            "#0002Fティオ、導力ネットの\x01",
            "復旧を手伝ってるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xC,
        "#0203Fええ、それもありますが……\x02",
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
            "#0202Fヨナと連絡が取れないものかと。\x02\x03",

            "ヨナはハッキングのために\x01",
            "あちこちの制御端末に\x01",
            "バックドアを仕掛けています。\x02\x03",

            "#0204Fそのどれかにアクセスできれば\x01",
            "状況を伝える事ができるかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        (
            "#0000Fな、なるほど……\x01",
            "外と連絡が取れるって事だな？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xC,
        (
            "#0204Fええ、まだ試している段階ですが。\x02\x03",

            "#0202F……こんな時こそ\x01",
            "日頃の借りを返してもらおうかと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE4, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4615")

    label("loc_458D")


    #C0142
    ChrTalk(
        0xC,
        (
            "#0204Fどこかの制御端末にアクセスできれば\x01",
            "ヨナと連絡が取れるかもしれません。\x02\x03",

            "#0202F……この際なので\x01",
            "ヨナにも協力してもらおうかと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4615")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_3FD1 end

    def Function_9_461D(): pass

    label("Function_9_461D")

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
            "な、なんだ……君たちか……\x01",
            "驚かさないでくれよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x103,
        "#0205Fどうかしたんですか……？\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x9,
        (
            "いや、そのう……\x01",
            "導力ネット上に、気になるデータが\x01",
            "流れていたものだからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xA,
        (
            "ああ、まさか\x01",
            "マリアベルお嬢様が学生時代の\x01",
            "水着写真のデータなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xA,
        "超激レアものだぜ……\x02",
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
        "いや、あ、遊んでるわけじゃないんだぜ？\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        "その、偶然見つけただけで……\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x9,
        (
            "でもこんな情報、\x01",
            "誰が流したんだろうなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        "#0003F（まさか……ヨナの仕業か？）\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x103,
        (
            "#0200F（そういえばエサを撒くとか\x01",
            "  言っていましたね。\x01",
            "  その一部かもしれません。）\x02",
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

    # Function_9_461D end

    def Function_10_493A(): pass

    label("Function_10_493A")

    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0153
    ChrTalk(
        0xA,
        "お嬢様が差し入れを……\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x9,
        "か、感激です！\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x8,
        (
            "#2904Fフフ、記念祭に\x01",
            "部下を労わらないほど\x01",
            "器量が狭くはありませんわ。\x02\x03",

            "#2900Fそれで、導力ネットの方は\x01",
            "どうなのかしら？\x01",
            "何か変わった事は？\x02",
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
        "特にありません！\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xA,
        "ええ、特に何も！\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x8,
        (
            "#2902F……何か隠してますわね。\x01",
            "すぐに吐きなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x9,
        "も、申し訳ありません～！\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xA,
        "すぐにお話しますので……っ！\x02",
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

    # Function_10_493A end

    def Function_11_4B02(): pass

    label("Function_11_4B02")

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

    def lambda_4C17():
        OP_96(0xFE, 0x1016C, 0x2710, 0x5DC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_4C17)

    def lambda_4C31():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_4C31)
    Sleep(800)

    def lambda_4C45():
        OP_96(0xFE, 0x108D8, 0x2710, 0x5B68, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C45)

    def lambda_4C5F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4C5F)
    Sleep(400)

    def lambda_4C73():
        OP_96(0xFE, 0x108D8, 0x2710, 0x6018, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4C73)

    def lambda_4C8D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4C8D)
    Sleep(400)

    def lambda_4CA1():
        OP_96(0xFE, 0x10D24, 0x2710, 0x5B68, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4CA1)

    def lambda_4CBB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4CBB)
    Sleep(400)

    def lambda_4CCF():
        OP_96(0xFE, 0x10D24, 0x2710, 0x6018, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4CCF)

    def lambda_4CE9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4CE9)
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
            "#6P#2904Fここが地下５Ｆ……\x01",
            "メイン端末があるフロアですわ。\x02\x03",

            "#2900F端末室は、階段を降りた先です。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            "#0001F#11P随分、厳重な場所に\x01",
            "設置されているんですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x138,
        (
            "#6P#2903Fいずれここで、顧客の情報を\x01",
            "管理することを考えていますから。\x02\x03",

            "#2901Fハッキング対策が十分でないため\x01",
            "現状では見送られていますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        "#11P#0101Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x103,
        (
            "#11P#0206F確かに、もし流出したら\x01",
            "大変な事になるでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x138,
        (
            "#6P#2904Fええ、それも含めて\x01",
            "まだまだ研究段階ですわ。\x02",
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

    # Function_11_4B02 end

    def Function_12_4F15(): pass

    label("Function_12_4F15")

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
        "#12P#0005Fこ、これは……\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x104,
        (
            "#0306Fなんつーか……\x01",
            "メチャクチャ凄そうな部屋だな。\x02\x03",

            "#0301F最新技術がてんこ盛りに\x01",
            "なっているのだけは分かるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x103,
        (
            "#12P#0204Fエプスタイン財団製の、\x01",
            "最新情報処理システムですね。\x02\x03",

            "#0202Fリベールの高速巡洋艦にも\x01",
            "使われているそうですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x138, 0xB4, 0x1F4)

    #C0172
    ChrTalk(
        0x138,
        (
            "#2904Fあの有名な\x01",
            "《アルセイユ号》ですわね。\x02\x03",

            "#2902Fあれに使われているものと\x01",
            "基本的には同じシステムですが……\x02\x03",

            "莫大なネットワーク情報に対応すべく、\x01",
            "処理容量を数倍に強化していますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x102,
        "#0105F……すごい……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x2)
    Sleep(300)

    #C0174
    ChrTalk(
        0x9,
        "#6Pマリアベルお嬢様……？\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xA,
        "#4Pお疲れさまです！\x02",
    )

    CloseMessageWindow()
    OP_63(0x138, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    BeginChrThread(0x9, 3, 0, 20)
    Sleep(300)
    BeginChrThread(0xA, 3, 0, 22)
    Sleep(2000)
    OP_68(0, 500, 13000, 1000)

    def lambda_5380():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_5380)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    OP_6F(0x1)

    #C0176
    ChrTalk(
        0x138,
        (
            "#11P#2900Fふふ、お疲れさま。\x02\x03",

            "仕事の方は順調かしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x9,
        "#11Pええ、おかげさまで。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xA,
        (
            "#5P例のシミュレーションも\x01",
            "順調に行きそうですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)

    #C0179
    ChrTalk(
        0xA,
        "#5Pえっと、こちらの方々は？\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x138,
        (
            "#11P#2900Fクロスベル警察の方々ですわ。\x02\x03",

            "実は、ここのメイン端末が\x01",
            "外部からハッキングを受けた\x01",
            "可能性があるらしいのです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_5501():
        TurnDirection(0xFE, 0x138, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_5501)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0181
    ChrTalk(
        0x9,
        "#11P#4Sええええっ！？\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xA,
        "#5Pハ、ハッキング！？\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        "#12P#0003Fえっと……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0184
    ChrTalk(
        0x101,
        (
            "#5P#0001Fティオ、彼らに\x01",
            "一通り説明してもらえるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x103,
        "#12P#0200Fはい、それでは……\x02",
    )

    CloseMessageWindow()
    OP_68(0, 500, 13280, 1000)

    def lambda_55E4():
        OP_95(0xFE, -1400, -600, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_55E4)
    Sleep(150)

    def lambda_5601():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5601)
    Sleep(100)

    def lambda_5611():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_5611)
    WaitChrThread(0x103, 1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0186
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティオは専門的な用語を交えながら\x01",
            "研究員たちに事情を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0187
    ChrTalk(
        0x9,
        "#11P外部からのハッキング……\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x9,
        (
            "#11P可能性はあったけど\x01",
            "まさか本当に起こるなんて……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 500)

    #C0189
    ChrTalk(
        0xA,
        "#1Pいや、でもあり得ないぜ！\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xA,
        (
            "#1Pハッキングなんてできる技術者が\x01",
            "そう簡単にいるはずが……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x138,
        (
            "#11P#2904Fもし、ハッキングでなければ\x01",
            "メールを送ったのが貴方たちである\x01",
            "可能性が高くなりますわねぇ。\x02\x03",

            "#2902Fうふふ……\x01",
            "どちらが《銀》なのかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_5812():
        TurnDirection(0xFE, 0x138, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_5812)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0192
    ChrTalk(
        0x9,
        "#11Pそ、そんな滅相もない！\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xA,
        (
            "#5P僕たちが不甲斐ないから\x01",
            "ハッキングされたんだと思います！\x02",
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
        "#12P#0012F（な、何ていうか……）\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x104,
        (
            "#0300F（イリアさんとは違った意味で\x01",
            "  女王様って感じだよな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x138,
        (
            "#11P#2903F特務支援課の端末にメールが\x01",
            "届いたのが、真夜中の３時頃……\x02\x03",

            "#2901Fその時間帯の\x01",
            "ログはどうなっていますの？\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x9,
        "#11Pは、はい。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xA,
        "#5Pすぐに調べます。\x02",
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
        "#6P……あ、ありました！\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x9,
        (
            "#6Pメールの転送システムが\x01",
            "クラッキングされています！\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x102,
        "#0101Fやっぱり……\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x104,
        (
            "#0303Fこれで外部説が\x01",
            "確定したってわけだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xA,
        "#11Pこちらも侵入経路を確認！\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xA,
        (
            "#11Pアクセス元は……駄目だ。\x01",
            "ロストしてしまっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        (
            "#0001Fどこから入り込まれたか\x01",
            "分からないってことですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xA,
        (
            "#11Pああ、巧妙に痕跡を\x01",
            "消されてしまっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xA,
        (
            "#11Pクロスベル市内の何処かなのは\x01",
            "間違いないと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x138,
        "#2901Fふむ……やりますわね。\x02",
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
            "#12P#0200F……端末を一つ、\x01",
            "貸してもらってもいいですか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x2)
    Sleep(300)

    #C0210
    ChrTalk(
        0x9,
        "#6Pえ……\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xA,
        "#4Pだ、だが……\x02",
    )

    CloseMessageWindow()

    def lambda_5D05():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_5D05)
    WaitChrThread(0x138, 1)

    #C0212
    ChrTalk(
        0x138,
        (
            "#11P#2904Fいいですわ。\x02\x03",

            "#2900Fティオさんと言ったかしら。\x01",
            "好きにいじってしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x103,
        "#6P#0204Fはい、それでは……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(0, 800, 18600, 3000)
    MoveCamera(40, 27, 0, 3000)
    SetCameraDistance(18000, 3000)
    SetChrSubChip(0x9, 0x0)

    def lambda_5DBC():

        label("loc_5DBC")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_5DBC")

    QueueWorkItem2(0x138, 2, lambda_5DBC)

    def lambda_5DCE():
        OP_95(0xFE, 0, -600, 14700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5DCE)
    WaitChrThread(0x103, 1)

    def lambda_5DEC():
        OP_95(0xFE, 0, -300, 17300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5DEC)
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
        "#0005Fな……\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x102,
        "#0101Fティオちゃん……！？\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x138,
        "#2905Fこれは……\x02",
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
            "#0201F#30W多次元解析による\x01",
            "リアルタイム制御を試行……\x02\x03",

            "全端末のログを解析、\x01",
            "隠蔽された痕跡の前後における\x01",
            "不審なアクセスを全て精査……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x9,
        "#5Pす、凄い……！？\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xA,
        "#11Pなんだ、この処理速度は！？\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x103,
        (
            "#0203F……サポートをお願いします。\x02\x03",

            "#0202Fクロスベルの全ターミナルに\x01",
            "管理者権限でアクセスをかけます。\x02\x03",

            "不審と思われるログを吐き出すので\x01",
            "チェックをお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x9,
        "#5Pあ、ああ……！\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xA,
        "#11P任せてくれ……！\x02",
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
        "#6P#0008F……エリィ、分かるか？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0224
    ChrTalk(
        0x102,
        (
            "#0106F#11Pう、ううん……\x01",
            "流石に付いていけないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x104,
        (
            "#0309F俺なんか、何をやってんのか\x01",
            "理解すらできてねぇんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x138,
        (
            "#5P#2904Fなるほど、ティオさんは\x01",
            "《魔導杖#6Rオーバルスタッフ#》の使い手ですのね。\x02\x03",

            "#2902F導力魔法をノーウェイトで\x01",
            "発動するための高速展開技術が\x01",
            "使われているそうですが……\x02\x03",

            "それを端末のコントロールに\x01",
            "利用したのかもしれませんわね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6303():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6303)
    Sleep(100)
    OP_93(0x102, 0x0, 0x1F4)

    #C0227
    ChrTalk(
        0x101,
        "#12P#0005Fわ、分かるんですか？\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x102,
        (
            "#0100F#11Pベルは一応、\x01",
            "エプスタイン財団で導力工学を\x01",
            "学んだ経験があるから……\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x138,
        (
            "#2904F#5Pふふ、といっても\x01",
            "かじった程度ですけれど。\x02",
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
        "#5P#2900F終わったみたいですわね。\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x104,
        "#0305Fおっ……\x02",
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
        "#0200F#6P……いかがでした？\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xA,
        "#11Pこちらの持ち分はシロだ。\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xA,
        "#11Pそっちはどうだ？\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)

    #C0235
    ChrTalk(
        0x9,
        "#5Pビンゴ──コイツだ！\x02",
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
            "#5PジオフロントＢ区画、\x01",
            "『第８制御端末』……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x9,
        "#5Pここからアクセスしたらしい！\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x101,
        "#0001Fジオフロント……\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x104,
        (
            "#0301Fあの駅前通りの外れにある\x01",
            "地下区画からかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x103,
        (
            "#0203Fいえ、あの場所は\x01",
            "ジオフロントＡ区画になります。\x02\x03",

            "#0201Fハッキングに使われた端末の所在は\x01",
            "ジオフロントのＢ区画……\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xA,
        (
            "#11Pえっと、市北西部の\x01",
            "地下にあるエリアみたいだね。\x02",
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
            "#0103F#11P市北西部……\x01",
            "住宅街や歓楽街のあたりね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0243
    ChrTalk(
        0x102,
        "#0101F#11Pロイド、どうするの？\x02",
    )

    CloseMessageWindow()

    def lambda_67E2():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_67E2)
    Sleep(150)
    TurnDirection(0x104, 0x101, 500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7522", 0)

    #C0244
    ChrTalk(
        0x101,
        (
            "#6P#0003F──早速、行ってみよう。\x02\x03",

            "#0001Fジオフロントのゲート管理は\x01",
            "たしか市庁舎の管理だったはずだ。\x02\x03",

            "鍵が借りられないか\x01",
            "受付に問い合わせてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x104,
        "#0300Fああ、さっそく行ってみようぜ。\x02",
    )

    CloseMessageWindow()
    OP_93(0x138, 0xB4, 0x1F4)
    Sleep(150)

    #C0246
    ChrTalk(
        0x138,
        (
            "#2904Fふふ……どうやら事件の核心に\x01",
            "迫ってきたみたいですわね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6911():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6911)
    Sleep(50)

    def lambda_6921():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6921)
    Sleep(50)
    OP_93(0x104, 0x0, 0x1F4)

    #C0247
    ChrTalk(
        0x101,
        (
            "#12P#0000Fはい……\x01",
            "色々とお世話になりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        (
            "#0102F#11Pありがとう、ベル。\x01",
            "それに研究員の方々も。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)

    def lambda_69AC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_69AC)
    Sleep(50)
    OP_93(0xA, 0xB4, 0x1F4)

    #C0249
    ChrTalk(
        0x9,
        "#5Pい、いやあ……\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xA,
        (
            "#5P僕らより、そのお嬢さんの\x01",
            "手柄の方が大きいと思うよ。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6A2F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6A2F)
    Sleep(150)

    def lambda_6A3F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6A3F)
    Sleep(50)

    def lambda_6A4F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_6A4F)

    def lambda_6A5C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_6A5C)
    Sleep(50)
    OP_93(0x104, 0x10E, 0x1F4)

    #C0251
    ChrTalk(
        0x101,
        (
            "#12P#0004Fそうだな……\x02\x03",

            "#0002Fお疲れ、ティオ。\x01",
            "おかげで助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x102,
        "#0109F#11Pふふっ、お疲れさま。\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x104,
        (
            "#0302Fさすがティオすけ。\x01",
            "決めてくれるじゃん。\x02",
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
            "#6P#0205Fえと、その……\x01",
            "大したことじゃないです。\x02\x03",

            "#0203Fそれにわたしも一応、\x01",
            "特務支援課の一員ですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x138,
        (
            "#11P#2909Fふふ……\x01",
            "十分、大したものですわ。\x02\x03",

            "#2902Fどうかしら、ティオさん。\x02\x03",

            "エリィ共々わたくしの所に\x01",
            "リクルートするというのは？\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x103,
        "#6P#0205Fえ……？\x02",
    )

    CloseMessageWindow()

    def lambda_6C35():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6C35)
    Sleep(50)

    def lambda_6C45():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6C45)
    Sleep(50)
    OP_93(0x104, 0x0, 0x1F4)

    #C0257
    ChrTalk(
        0x102,
        "#0101F#11Pちょ、ちょっとベル……\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x104,
        (
            "#0302Fはは……\x01",
            "いきなり引き抜きッスか。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#12P#0012Fえっと、それはさすがに\x01",
            "勘弁して欲しいんですけど……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6CF2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_6CF2)
    Sleep(100)
    OP_93(0x9, 0xB4, 0x1F4)

    #C0260
    ChrTalk(
        0x138,
        (
            "#2904Fふふ、冗談ですわ。\x02\x03",

            "#2900F事件が無事解決したら\x01",
            "是非、顛末を教えてください。\x02\x03",

            "それと──\x01",
            "お渡ししたセキュリティカードは\x01",
            "そのまま預けておきますわ。\x02\x03",

            "最上階とこのフロアなら\x01",
            "いつでも来れるようにしますから\x01",
            "何かあったら訪ねてくださいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x102,
        "#0104F#11Pありがとう、ベル。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        "#12P#0000Fそれでは失礼します。\x02",
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

    # Function_12_4F15 end

    def Function_13_6F9A(): pass

    label("Function_13_6F9A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6FC6")
    SetChrSubChip(0x103, 0x0)
    Sleep(70)
    SetChrSubChip(0x103, 0x1)
    Sleep(70)
    SetChrSubChip(0x103, 0x2)
    Sleep(70)
    SetChrSubChip(0x103, 0x1)
    Sleep(70)
    Jump("Function_13_6F9A")

    label("loc_6FC6")

    Return()

    # Function_13_6F9A end

    def Function_14_6FC7(): pass

    label("Function_14_6FC7")


    def lambda_6FCC():
        OP_95(0xFE, 0, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_6FCC)

    def lambda_6FE6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_6FE6)
    WaitChrThread(0x138, 1)

    def lambda_6FFB():
        OP_95(0xFE, 0, -600, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_6FFB)
    WaitChrThread(0x138, 1)
    Return()

    # Function_14_6FC7 end

    def Function_15_7015(): pass

    label("Function_15_7015")

    Sleep(800)

    def lambda_701D():
        OP_95(0xFE, -500, 0, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_701D)

    def lambda_7037():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7037)
    WaitChrThread(0x101, 1)

    def lambda_704C():
        OP_95(0xFE, -500, -600, 11100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_704C)
    WaitChrThread(0x101, 1)
    Return()

    # Function_15_7015 end

    def Function_16_7066(): pass

    label("Function_16_7066")

    Sleep(1300)

    def lambda_706E():
        OP_95(0xFE, 500, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_706E)

    def lambda_7088():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7088)
    WaitChrThread(0x102, 1)

    def lambda_709D():
        OP_95(0xFE, 500, -600, 11100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_709D)
    WaitChrThread(0x102, 1)
    Return()

    # Function_16_7066 end

    def Function_17_70B7(): pass

    label("Function_17_70B7")

    Sleep(1700)

    def lambda_70BF():
        OP_95(0xFE, -500, 0, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_70BF)

    def lambda_70D9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_70D9)
    WaitChrThread(0x103, 1)

    def lambda_70EE():
        OP_95(0xFE, -1100, -600, 10100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_70EE)
    WaitChrThread(0x103, 1)
    Return()

    # Function_17_70B7 end

    def Function_18_7108(): pass

    label("Function_18_7108")

    OP_93(0x103, 0xB4, 0x1F4)

    def lambda_7114():
        OP_95(0xFE, 0, -600, 14700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7114)
    WaitChrThread(0x103, 1)

    def lambda_7132():
        OP_95(0xFE, -1400, -600, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7132)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x5A, 0x1F4)
    Return()

    # Function_18_7108 end

    def Function_19_7153(): pass

    label("Function_19_7153")

    Sleep(2200)

    def lambda_715B():
        OP_95(0xFE, 500, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_715B)

    def lambda_7175():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7175)
    Sleep(1000)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    WaitChrThread(0x104, 1)

    def lambda_71A8():
        OP_95(0xFE, 1100, -600, 10100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_71A8)
    WaitChrThread(0x104, 1)
    Return()

    # Function_19_7153 end

    def Function_20_71C2(): pass

    label("Function_20_71C2")

    Fade(150)
    SetChrPos(0x9, 3500, -380, 21500, 45)
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_0D()

    def lambda_71E6():
        OP_95(0xFE, 3500, -600, 16800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_71E6)
    WaitChrThread(0x9, 1)

    def lambda_7204():
        OP_95(0xFE, 1000, -600, 14300, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7204)
    WaitChrThread(0x9, 1)
    Return()

    # Function_20_71C2 end

    def Function_21_721E(): pass

    label("Function_21_721E")

    OP_93(0x9, 0x2D, 0x1F4)

    def lambda_722A():
        OP_95(0xFE, 3500, -600, 16800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_722A)
    WaitChrThread(0x9, 1)

    def lambda_7248():
        OP_95(0xFE, 3500, -480, 22200, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7248)
    WaitChrThread(0x9, 1)
    Fade(250)
    SetChrPos(0x9, 4700, -380, 22700, 45)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    Return()

    # Function_21_721E end

    def Function_22_7281(): pass

    label("Function_22_7281")

    Fade(150)
    SetChrPos(0xA, -3500, -380, 21700, 315)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    OP_0D()

    def lambda_72A5():
        OP_95(0xFE, -3500, -600, 16800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_72A5)
    WaitChrThread(0xA, 1)

    def lambda_72C3():
        OP_95(0xFE, -1000, -600, 14300, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_72C3)
    WaitChrThread(0xA, 1)
    Return()

    # Function_22_7281 end

    def Function_23_72DD(): pass

    label("Function_23_72DD")

    OP_93(0xA, 0x13B, 0x1F4)

    def lambda_72E9():
        OP_95(0xFE, -3500, -600, 16800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_72E9)
    WaitChrThread(0xA, 1)

    def lambda_7307():
        OP_95(0xFE, -3500, -600, 22200, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7307)
    WaitChrThread(0xA, 1)
    Fade(250)
    SetChrPos(0xA, -4700, -380, 22700, 315)
    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Return()

    # Function_23_72DD end

    def Function_24_7346(): pass

    label("Function_24_7346")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7368")
    Sound(849, 0, 100, 0)
    Sleep(950)
    Sound(850, 0, 100, 0)
    Sleep(1750)
    Jump("Function_24_7346")

    label("loc_7368")

    Return()

    # Function_24_7346 end

    def Function_25_7369(): pass

    label("Function_25_7369")

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
            "#2904F#5Pそうそう、これは\x01",
            "わたくしのカンですけど……\x02\x03",

            "#2902F恐らく、メールを送った人物と\x01",
            "《銀》というのは別人ですわね。\x02\x03",

            "明らかに、専門の技術者……\x01",
            "それもエプスタイン財団の\x01",
            "関係者である可能性が高いですわ。\x02",
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
        "#0011Fええっ！？\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x102,
        "#0105Fそ、そんなこと分かるの！？\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x103,
        (
            "#6P#0203F……そうですね。\x01",
            "わたしもそう思いました。\x02\x03",

            "あれだけのネットワーク技術を\x01",
            "使える人間は限られています。\x02\x03",

            "#0208Fそれにハッキングのクセにしても\x01",
            "どこかで見た事があるような……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7615():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7615)
    Sleep(100)

    def lambda_7625():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7625)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)

    #C0267
    ChrTalk(
        0x101,
        "#0001F#5Pそうなのか……\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x8,
        (
            "#2904F#5Pああ、それともし、\x01",
            "そのハッカーを見つけた場合……\x02\x03",

            "#2902Fそのまま泳がせたいですから、\x01",
            "放置しておいていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_76DC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_76DC)
    Sleep(100)

    def lambda_76EC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_76EC)
    Sleep(50)
    OP_93(0x104, 0x0, 0x1F4)

    #C0269
    ChrTalk(
        0x101,
        "#0005Fえ゛。\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x102,
        "#0105Fど、どうして……？\x02",
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x8,
        (
            "#2909F#5P現時点で、ハッカー行為を\x01",
            "取り締まる法律はありませんから。\x02\x03",

            "それならむしろ、放置した上で\x01",
            "こちらのプロテクト技術の向上に\x01",
            "役立ってもらうことにしますわ。\x02\x03",

            "#2902F銀行機能の導力化を実現するにも\x01",
            "ハッカー対策は不可欠ですから。\x02",
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
        "#0106Fふう……貴女って人は。\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x104,
        (
            "#12P#0302Fいやはや……\x01",
            "大胆というか、豪胆な人だねぇ。\x02",
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

    # Function_25_7369 end

    def Function_26_7906(): pass

    label("Function_26_7906")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_799A")
    Jump("loc_79E4")

    label("loc_799A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_79BA")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_79E4")

    label("loc_79BA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_79DA")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_79E4")

    label("loc_79DA")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_79E4")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    #C0274
    ChrTalk(
        0xB,
        (
            "そういえば……\x01",
            "例の魔導杖の改造の件は\x01",
            "どうなったんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xB,
        (
            "君達のほうで材料を\x01",
            "探してくる手筈だったと\x01",
            "思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x101,
        (
            "#0000Fああ……すみません。\x02\x03",

            "素材は集めていたんですが、\x01",
            "時間が無かったもので……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xB,
        (
            "そうだったのか、\x01",
            "それは残念だな……\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xB,
        (
            "こんな時だし\x01",
            "ティオ君の戦力強化ができるなら\x01",
            "やっておいた方がいいと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xB,
        (
            "こちらも準備だけはしてあるから\x01",
            "もし改造したくなったら\x01",
            "ギヨームに声を掛けてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xB,
        (
            "あいつも商売道具一式\x01",
            "持ってきているはずだからさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x31, 0x1, 0x2)
    SetChrSubChip(0xB, 0x0)
    TalkEnd(0xB)
    Return()

    # Function_26_7906 end

    def Function_27_7BEE(): pass

    label("Function_27_7BEE")

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
            "材料は確認したぜ。\x01",
            "こっちは問題なしだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xB,
        "よし、準備は万全だね。\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)

    #C0283
    ChrTalk(
        0xB,
        (
            "うふふ、楽しみだね～。\x01",
            "新しい魔導杖を颯爽と構える\x01",
            "ティオ君が目に浮かぶようだよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xC,
        (
            "#0200F……主任。\x02\x03",

            "魔導杖がバグって\x01",
            "使い物にならなくなったら\x01",
            "恨みますよ？\x02",
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
            "そ、そんな……\x01",
            "ティオ君に一生嫌われちゃう……\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xB,
        (
            "うわーん……！\x01",
            "僕は、僕は何て酷い事を……！\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#0000F#2P主任さん、まだ何も\x01",
            "起きてませんよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 500)
    Sleep(300)

    #C0288
    ChrTalk(
        0xD,
        "ロバーツよう、正気に戻れ。\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0289
    ChrTalk(
        0xB,
        "ハッ……！？\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0xE1, 0x190)
    OP_93(0xD, 0xE1, 0x1F4)
    Sleep(300)

    #C0290
    ChrTalk(
        0xB,
        (
            "す、すまない。\x01",
            "早速始めるとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xB,
        (
            "ロイド君は少しの間\x01",
            "待っていてくれるかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        (
            "#0000F#2Pええ、それでは\x01",
            "見学させてもらいます。\x02",
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
            "ロイドはそのまま\x01",
            "３０分ほどの時間を過ごした。\x02",
        )
    )

    CloseMessageWindow()

    #A0294
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "詳しくは判らないが、\x01",
            "魔導杖の改造は\x01",
            "手際よく進められているようだった。\x02",
        )
    )

    CloseMessageWindow()

    #A0295
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そして──\x02",
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
        "#0200Fそうですね……\x02",
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
            "#0200F基本プログラムが書き換わったので\x01",
            "やや違和感がありますが、\x01",
            "悪くない感じです。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xB,
        (
            "きっと重心制御だね。\x01",
            "ティオ君ならすぐに慣れると思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xB,
        (
            "他の魔導杖に持ち替えるときは\x01",
            "エイオンシステムを使って\x01",
            "プログラムをコピーして使ってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xB,
        (
            "脱着式のアタッチパーツも\x01",
            "付けるのを忘れないようにね。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xC,
        "#0200F了解です。\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xD,
        (
            "にしても、\x01",
            "やっぱりメインマシンを使うと\x01",
            "作業が早くていいねえ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 400)
    Sleep(300)

    #C0303
    ChrTalk(
        0xD,
        (
            "俺ぁこのままここに\x01",
            "居ついちまいそうだぜ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)
    Sleep(300)

    #C0304
    ChrTalk(
        0xB,
        (
            "うふふ、魔導杖のコアシステムだって\x01",
            "簡単にバックアップできちゃうしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xB,
        (
            "チューンナップだって\x01",
            "とことん試せるんだよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xC,
        (
            "#0200Fあまり主任の手は\x01",
            "借りたくないのですが……\x02\x03",

            "お陰でプログラムも７％ほど\x01",
            "軽量化しましたし。\x01",
            "早く実戦で使ってみたい所です。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8514():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8514)

    def lambda_8521():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8521)
    Sleep(200)

    #C0307
    ChrTalk(
        0xB,
        (
            "あ、ティオ君も\x01",
            "やっぱりそう思うよね～♪\x02",
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
            "#0000Fな、何だか\x01",
            "凄い改造を見てしまった……\x02\x03",

            "えっとティオ、\x01",
            "上手く行ったのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xC, 0x101, 400)

    def lambda_8680():
        OP_95(0xFE, -2500, 0, -380, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_8680)
    Sleep(800)

    def lambda_869D():
        OP_95(0xFE, -1120, 0, 810, 1200, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_869D)
    Sleep(100)
    BeginChrThread(0xD, 1, 0, 29)
    WaitChrThread(0xC, 1)

    #C0309
    ChrTalk(
        0xC,
        (
            "#0200F#2Pええ、改造は一通り終了しました。\x01",
            "性能も期待通りの値を\x01",
            "発揮しているようです。\x02\x03",

            "絶対零度の反エネルギー弾を打ち出す\x01",
            "『アブソリュート・ゼロ』──\x02\x03",

            "乱発は出来ませんが\x01",
            "重要な戦闘では\x01",
            "役に立ってくれそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x101,
        (
            "#0000Fそうか……それは心強いな。\x02\x03",

            "（本音を言うと\x01",
            "  無茶な戦闘には\x01",
            "  巻き込みたくないけど……）\x02\x03",

            "ティオ、こんな時だけど頑張ろう。\x01",
            "頼りにしてるんだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xC,
        (
            "#0200F#2P──ふふ、了解です。\x02\x03",

            "今のわたしには\x01",
            "守りたいものがありますから……\x02\x03",

            "ロイドさん、お互い\x01",
            "全力を尽くしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        "#0000Fああ……！\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_894B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_894B")
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)

    label("loc_894B")

    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_29(0x31, 0x4, 0x10)
    OP_29(0x31, 0x1, 0x3)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_27_7BEE end

    def Function_28_8966(): pass

    label("Function_28_8966")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_897D")
    OP_A0(0xC, 1200, 0x0, 0x4)
    Jump("Function_28_8966")

    label("loc_897D")

    Return()

    # Function_28_8966 end

    def Function_29_897E(): pass

    label("Function_29_897E")

    OP_95(0xFE, -750, 0, -990, 1200, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Return()

    # Function_29_897E end

    def Function_30_899A(): pass

    label("Function_30_899A")

    EventBegin(0x1)

    #C0313
    ChrTalk(
        0x138,
        (
            "#2905Fあら、端末室が\x01",
            "見たかったのではなくて？\x02\x03",

            "#2900Fメイン端末はこの先ですわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x101,
        (
            "#0005Fおっと……すみません。\x01",
            "この階段の下でしたね。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 67810, 10000, 23760, 270)
    EventEnd(0x4)
    Return()

    # Function_30_899A end

    SaveToFile()

Try(main)
