from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0800.bin",                # FileName
        "c0800",                    # MapName
        "c0800",                    # Location
        0x0003,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 3, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0800",                  # 0
        "ロメオ隊員",             # 1
        "乗客",                   # 2
        "乗客",                   # 3
        "乗客",                   # 4
        "臨検官クワトロ",         # 5
        "老人",                   # 6
        "老婦人",                 # 7
        "乗客",                   # 8
        "乗客",                   # 9
        "乗客",                   # 10
        "乗客",                   # 11
        "乗客",                   # 12
        "乗客",                   # 13
        "乗客",                   # 14
        "駅員",                   # 15
        "駅員",                   # 16
        "乗客",                   # 17
        "列車",                   # 18
        "キャンベル議員",         # 19
        "カーラ",                 # 20
        "マーシャ",               # 21
        "SE制御",                 # 22
    ))

    AddCharChip((
        "chr/ch31200.itc",                   # 00
        "chr/ch20302.itc",                   # 01
        "chr/ch24400.itc",                   # 02
        "chr/ch20802.itc",                   # 03
        "chr/ch28500.itc",                   # 04
    ))

    DeclNpc(-1500,   0,       -18530,  0,    385,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(43000,   100,     -17200,  180,  453,  0x0, 0,   1,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(49700,   0,       -14050,  0,    385,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(15000,   100,     -17200,  180,  453,  0x0, 0,   3,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(7500,    0,       -12500,  270,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 33,  58.0,                  -16.0,                 0.0,                   17.015625,             [0.3333333134651184,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3636363446712494,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -19.333332061767578,   5.81818151473999,      -0.0,                  1.0])

    DeclActor(24500,   0,       0,       2000,    24500,   1500,    0,       0x007C, 0,  34, 0x0000)
    DeclActor(24500,   0,       -16000,  2000,    24500,   1500,    -16000,  0x007C, 0,  34, 0x0000)
    DeclActor(18000,   0,       0,       2000,    17500,   1500,    0,       0x007C, 0,  35, 0x0000)
    DeclActor(18000,   0,       -16000,  2000,    17500,   1500,    -16000,  0x007C, 0,  35, 0x0000)

    ScpFunction((
        "Function_0_498",          # 00, 0
        "Function_1_550",          # 01, 1
        "Function_2_623",          # 02, 2
        "Function_3_6E3",          # 03, 3
        "Function_4_97B",          # 04, 4
        "Function_5_C00",          # 05, 5
        "Function_6_CBE",          # 06, 6
        "Function_7_E99",          # 07, 7
        "Function_8_ED6",          # 08, 8
        "Function_9_FF7",          # 09, 9
        "Function_10_16D0",        # 0A, 10
        "Function_11_188E",        # 0B, 11
        "Function_12_198F",        # 0C, 12
        "Function_13_1C99",        # 0D, 13
        "Function_14_1CC2",        # 0E, 14
        "Function_15_1D37",        # 0F, 15
        "Function_16_2854",        # 10, 16
        "Function_17_28A9",        # 11, 17
        "Function_18_2DE6",        # 12, 18
        "Function_19_2E2A",        # 13, 19
        "Function_20_2EFE",        # 14, 20
        "Function_21_2F5D",        # 15, 21
        "Function_22_2FBC",        # 16, 22
        "Function_23_301B",        # 17, 23
        "Function_24_307A",        # 18, 24
        "Function_25_3514",        # 19, 25
        "Function_26_3556",        # 1A, 26
        "Function_27_35B3",        # 1B, 27
        "Function_28_35CA",        # 1C, 28
        "Function_29_3A5F",        # 1D, 29
        "Function_30_4898",        # 1E, 30
        "Function_31_48C1",        # 1F, 31
        "Function_32_48E2",        # 20, 32
        "Function_33_5356",        # 21, 33
        "Function_34_54A6",        # 22, 34
        "Function_35_54DF",        # 23, 35
        "Function_36_5518",        # 24, 36
        "Function_37_5563",        # 25, 37
    ))


    def Function_0_498(): pass

    label("Function_0_498")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4D8"),
        (1, "loc_4E4"),
        (2, "loc_4F0"),
        (3, "loc_4FC"),
        (4, "loc_508"),
        (5, "loc_514"),
        (6, "loc_520"),
        (SWITCH_DEFAULT, "loc_52C"),
    )


    label("loc_4D8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_4E4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_4F0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_4FC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_508")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_514")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_520")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_52C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_538")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_54F")

    Return()

    # Function_0_498 end

    def Function_1_550(): pass

    label("Function_1_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_564")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 17)
    Jump("loc_5C6")

    label("loc_564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_578")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 8)
    Jump("loc_5C6")

    label("loc_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_58C")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 15)
    Jump("loc_5C6")

    label("loc_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_5A6")
    ClearScenarioFlags(0x5C, 3)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 3)
    Event(0, 28)
    Jump("loc_5C6")

    label("loc_5A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x9)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C6")
    Event(0, 24)

    label("loc_5C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5EB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E1")
    Jump("loc_5E6")

    label("loc_5E1")

    ClearChrFlags(0x8, 0x80)

    label("loc_5E6")

    Jump("loc_622")

    label("loc_5EB")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_610")
    Jump("loc_622")

    label("loc_610")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_622")
    ClearChrFlags(0xC, 0x80)

    label("loc_622")

    Return()

    # Function_1_550 end

    def Function_2_623(): pass

    label("Function_2_623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_635")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_635")

    SetMapObjFlags(0x1, 0x1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_680")
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)

    label("loc_680")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CB")
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6DC")
    OP_24(0x323)
    Jump("loc_6E2")

    label("loc_6DC")

    Sound(803, 1, 100, 0)

    label("loc_6E2")

    Return()

    # Function_2_623 end

    def Function_3_6E3(): pass

    label("Function_3_6E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_79F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_701")
    Jump("loc_79A")

    label("loc_701")


    #C0001
    ChrTalk(
        0xFE,
        (
            "よう、今共和国から\x01",
            "戻ったところかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "俺も、一度でいいから\x01",
            "旅行に行ってみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#0003F（……旅行って感じじゃ\x01",
            "  なかったんだけどな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79A")

    Jump("loc_977")

    label("loc_79F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_896")

    #C0004
    ChrTalk(
        0xFE,
        (
            "この駅からは警備隊への物資を\x01",
            "運搬するための貨物列車が出ていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "ついさっき、ベルガード門の方に\x01",
            "列車を送り出した所なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "警備隊員も、警備だけしてれば\x01",
            "いいってわけじゃないんだから\x01",
            "なかなか大変だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_90A")

    label("loc_896")


    #C0007
    ChrTalk(
        0xFE,
        (
            "さっき門に向かう貨物列車に\x01",
            "荷物を運び入れたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "３番ホームは貨物線専用だから、\x01",
            "入ってくるんじゃないぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90A")

    Jump("loc_977")

    label("loc_90F")


    #C0009
    ChrTalk(
        0xFE,
        (
            "おっと……帝国行き列車の\x01",
            "臨検が済んだみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "俺もそろそろベルガード門に\x01",
            "帰るとするかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_977")

    TalkEnd(0xFE)
    Return()

    # Function_3_6E3 end

    def Function_4_97B(): pass

    label("Function_4_97B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A0F")
    Jump("loc_A59")

    label("loc_A0F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A2F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A59")

    label("loc_A2F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A59")

    label("loc_A4F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A59")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5F")

    #C0011
    ChrTalk(
        0xFE,
        (
            "クロスベル入りする乗客には\x01",
            "臨検なんてしてないのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "あくまで、帝国と共和国に向かう\x01",
            "人達だけをチェックするの。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "そんなだから、\x01",
            "列車を利用した密入国や密輸が\x01",
            "後を絶たないんだってさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_BBC")

    label("loc_B5F")


    #C0014
    ChrTalk(
        0xFE,
        (
            "列車を利用した密入国や密輸が\x01",
            "後を絶たないんだってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        "ま、あたしには関係ないけど。\x02",
    )

    CloseMessageWindow()

    label("loc_BBC")

    Jump("loc_BF8")

    label("loc_BC1")


    #C0016
    ChrTalk(
        0xFE,
        (
            "さてと……休憩終わり。\x01",
            "そろそろ行くとしようかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_4_97B end

    def Function_5_C00(): pass

    label("Function_5_C00")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C62")

    #C0017
    ChrTalk(
        0xFE,
        (
            "帝国まで行く友人を\x01",
            "見送りに来てるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        "……まだ発車しないのかな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CBA")

    label("loc_C62")


    #C0019
    ChrTalk(
        0xFE,
        (
            "うーん……\x01",
            "まだ発車しないのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "いい加減見送りを済ませて\x01",
            "帰りたいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CBA")

    TalkEnd(0xFE)
    Return()

    # Function_5_C00 end

    def Function_6_CBE(): pass

    label("Function_6_CBE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D52")
    Jump("loc_D9C")

    label("loc_D52")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D72")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D9C")

    label("loc_D72")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D92")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D9C")

    label("loc_D92")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D9C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1B")

    #C0021
    ChrTalk(
        0xFE,
        "友人が次の列車で来るのじゃ。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        "１０年ぶりじゃ……懐かしいのう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E91")

    label("loc_E1B")


    #C0023
    ChrTalk(
        0xFE,
        (
            "臨検官殿も出てきたようだし、\x01",
            "そろそろ発車かのう？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "友人が乗ってくる列車が入るのは\x01",
            "この列車が出てからじゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E91")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_CBE end

    def Function_7_E99(): pass

    label("Function_7_E99")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_EAD")
    Jump("loc_ED2")

    label("loc_EAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_EC2")
    Call(0, 10)
    Jump("loc_ED2")

    label("loc_EC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_ED2")
    Call(0, 9)

    label("loc_ED2")

    TalkEnd(0xFE)
    Return()

    # Function_7_E99 end

    def Function_8_ED6(): pass

    label("Function_8_ED6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(452)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    OP_49()
    SetChrPos(0x19, 7000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_68(61500, 2500, -10500, 0)
    MoveCamera(60, 15, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(16000, 0)
    OP_EE(0x0, 0x1)
    OP_68(58500, 2500, -11500, 5000)
    MoveCamera(45, 20, 0, 5000)
    SetCameraDistance(24000, 5000)
    ClearMapObjFlags(0x1, 0x4)
    BeginChrThread(0x19, 3, 0, 18)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(5500, 3300, -8000, 0)
    MoveCamera(48, -15, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(14000, 0)
    OP_68(5500, 2300, -8000, 4000)
    OP_0D()
    WaitChrThread(0x19, 3)
    OP_6F(0x1)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_ED6 end

    def Function_9_FF7(): pass

    label("Function_9_FF7")

    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_68(5270, 1500, -12980, 0)
    MoveCamera(29, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17840, 0)
    SetChrPos(0x101, 5500, 0, -13000, 90)
    SetChrPos(0x102, 5250, 0, -12000, 90)
    SetChrPos(0x103, 4000, 0, -13000, 90)
    SetChrPos(0x104, 3700, 0, -12000, 90)
    OP_93(0xC, 0x10E, 0x0)
    SetChrSubChip(0xC, 0x0)
    OP_0D()

    #C0025
    ChrTalk(
        0xFE,
        (
            "#11P……では早速、\x01",
            "仕事の内容を説明しよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#6P#0000Fはい、よろしくお願いします。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "#11Pこれから君たちには、\x01",
            "１車両ごとに分担して\x01",
            "列車内の臨検を始めてもらう。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "#11P具体的には、乗客の一人一人話しかけて\x01",
            "入国申請書と手荷物をチェックするのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "#11P万が一入国申請書が無かったり、\x01",
            "危険物を持ち込んでいる者がいたら\x01",
            "即刻、拘束してもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#6P#0003Fなるほど……了解しました。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#0303Fんー、まぁ臨検はいいとしても……\x02\x03",

            "#0301F万が一、乗客が席を離れてたら\x01",
            "どうするんスか？\x02\x03",

            "#0306Fいくらなんでも、\x01",
            "素人の俺たちだけじゃ\x01",
            "カバーしきれない気がするが……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "#11Pああ、その辺は抜かりない。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "#11P臨検が開始されて終わるまでは、\x01",
            "乗客は車両を移動することは\x01",
            "できない決まりになっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "#11P時々、どさくさに紛れて\x01",
            "臨検をやり過ごそうとする\x01",
            "小賢しい連中もいるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        "#6P#0200Fさすが、厳重ですね。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#6P#0001Fなるほど……\x01",
            "一通りやり方は分かりました。\x02\x03",

            "#0003Fうーん、でも……\x01",
            "１車両ごとに分担か……\x02\x03",

            "#0000F俺とランディは一人でもいいけど、\x01",
            "エリィとティオは……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1492():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1492)

    def lambda_149F():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_149F)

    def lambda_14AC():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14AC)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0037
    ChrTalk(
        0x102,
        (
            "#5P#0105F今更そんな心配は\x01",
            "いらないでしょう？\x02\x03",

            "#0104F警察官として最低限の体術は\x01",
            "心得ているつもりよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        (
            "#6P#0203F右に同じく。\x02\x03",

            "#0200F万が一不審者が逆上したとしても、\x01",
            "わたしを圧倒できるとは到底思えません。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        (
            "#5P#0309Fハハ、うちの女性陣は\x01",
            "か弱い女ってタマじゃねぇからな。\x02\x03",

            "いい加減学習しろって、ロイド。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0040
    ChrTalk(
        0x101,
        "#12P#0003Fた、確かにそうだな。\x02",
    )

    CloseMessageWindow()

    def lambda_1627():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1627)

    def lambda_1634():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1634)

    def lambda_1641():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1641)

    def lambda_164E():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_164E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0041
    ChrTalk(
        0xC,
        (
            "それでは……\x01",
            "さっそく始めてもらって\x01",
            "構わないな？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x9, 0x1, 0x2)
    Call(0, 11)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16BC")
    Call(0, 12)
    Jump("loc_16CF")

    label("loc_16BC")

    SetChrPos(0x0, 5000, 0, -13500, 90)
    EventEnd(0x5)

    label("loc_16CF")

    Return()

    # Function_9_FF7 end

    def Function_10_16D0(): pass

    label("Function_10_16D0")

    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_68(5270, 1500, -12980, 0)
    MoveCamera(29, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17840, 0)
    SetChrPos(0x101, 5500, 0, -13000, 90)
    SetChrPos(0x102, 5250, 0, -12000, 90)
    SetChrPos(0x103, 4000, 0, -13000, 90)
    SetChrPos(0x104, 3700, 0, -12000, 90)
    OP_93(0xC, 0x10E, 0x0)
    SetChrSubChip(0xC, 0x0)
    OP_0D()

    #C0042
    ChrTalk(
        0xC,
        (
            "#11Pこれから君たちには、\x01",
            "１車両ずつに分担して\x01",
            "臨検を執り行ってもらう。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xC,
        (
            "#11Pやってもらいたいのは、\x01",
            "乗客の手荷物、及び\x01",
            "『入国申請書』の確認だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xC,
        (
            "#11Pそれでは……\x01",
            "さっそく始めてもらって\x01",
            "構わないな？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 11)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_187A")
    Call(0, 12)
    Jump("loc_188D")

    label("loc_187A")

    SetChrPos(0x0, 5000, 0, -13500, 90)
    EventEnd(0x5)

    label("loc_188D")

    Return()

    # Function_10_16D0 end

    def Function_11_188E(): pass

    label("Function_11_188E")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【はい】\x01",        # 0
            "【いいえ】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_198E")

    #C0045
    ChrTalk(
        0x101,
        "#6P#0006Fえっと、まだ心の準備が……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xC,
        (
            "#11P……仕方ないな。\x01",
            "緊張して失敗されても困る。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xC,
        (
            "#11Pただし、発車を\x01",
            "あまり待たせる事は出来ん。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xC,
        "#11Pできるだけ速く戻ってくるのだぞ。\x02",
    )

    CloseMessageWindow()

    label("loc_198E")

    Return()

    # Function_11_188E end

    def Function_12_198F(): pass

    label("Function_12_198F")


    #C0049
    ChrTalk(
        0x101,
        "#6P#0000Fはい、分かりました。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xC,
        (
            "#11P……ウォッホン！\x01",
            "問題はないようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xC,
        (
            "#11Pそれでは、早速\x01",
            "取り掛かってもらうとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xC,
        (
            "#11P私は先頭車両を臨検する。\x01",
            "２両目以降は君たちで分担したまえ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A60():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A60)
    Sleep(300)

    def lambda_1A70():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A70)

    def lambda_1A7D():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A7D)

    def lambda_1A8A():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A8A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0053
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそれじゃ……２両目は俺が。\x02\x03",

            "３両目からは\x01",
            "エリィ、ティオ、ランディの順で\x01",
            "臨検に当たってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        "#5P#0300Fラジャ！\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        "#6P#0200F把握です。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        "#5P#0100Fじゃあ、後ほど。\x02",
    )

    CloseMessageWindow()

    def lambda_1B62():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B62)

    def lambda_1B6F():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B6F)

    def lambda_1B7C():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B7C)

    def lambda_1B89():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B89)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0057
    ChrTalk(
        0xC,
        (
            "#11Pうむ、くれぐれも丁寧な仕事を\x01",
            "心がけるがいい。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 1, 0, 13)
    Sleep(500)
    BeginChrThread(0x101, 1, 0, 14)
    WaitChrThread(0xC, 1)
    WaitChrThread(0x101, 1)

    #C0058
    ChrTalk(
        0x101,
        (
            "#6P#0001Fよぉし……\x01",
            "任務開始だな！\x02",
        )
    )

    CloseMessageWindow()
    Sound(454, 0, 100, 0)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    OP_79(0x1)

    def lambda_1C31():
        OP_97(0x101, 0x12C, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C31)
    BeginChrThread(0x1D, 0, 0, 36)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 1)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    StopBGM(0x7D0)
    WaitBGM()
    EndChrThread(0x1D, 0x0)
    SetScenarioFlags(0x5C, 1)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_198F end

    def Function_13_1C99(): pass

    label("Function_13_1C99")

    OP_97(0xC, 0xFFFFFA24, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    OP_97(0xC, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_13_1C99 end

    def Function_14_1CC2(): pass

    label("Function_14_1CC2")


    def lambda_1CC7():
        OP_97(0x102, 0x3A98, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CC7)
    Sleep(300)
    OP_97(0x103, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)

    def lambda_1CF8():
        OP_97(0x103, 0x3A98, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1CF8)
    Sleep(400)

    def lambda_1D15():
        OP_97(0x104, 0x3A98, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D15)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Return()

    # Function_14_1CC2 end

    def Function_15_1D37(): pass

    label("Function_15_1D37")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_68(5270, 1500, -12980, 0)
    MoveCamera(29, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17840, 0)
    SetChrPos(0x101, 5500, 0, -13000, 90)
    SetChrPos(0x102, 5250, 0, -12000, 90)
    SetChrPos(0x103, 4000, 0, -13000, 90)
    SetChrPos(0x104, 3700, 0, -12000, 90)
    OP_93(0xC, 0x10E, 0x0)
    SetChrSubChip(0xC, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0xB)"), scpexpr(EXPR_END)), "loc_2364")
    OP_2C(0x9, 0x2)

    #C0059
    ChrTalk(
        0xC,
        (
            "#11P……奴は入国申請書に\x01",
            "虚偽申告をしていたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#6P#0005Fき、虚偽申告……？\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        "#6P#0200F嘘の経歴を書いていたわけですか。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xC,
        "#11P奴は共和国の元・詐欺師でな。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xC,
        (
            "#11P旅行好きな奴で、以前も\x01",
            "前科を隠して虚偽申告していたのを\x01",
            "この私が見つけ出したのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xC,
        (
            "#11Pこれで私に捕まるのは二度目……\x01",
            "全く、バカな男だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x104,
        (
            "#5P#0301F元・詐欺師ってことは……\x01",
            "今は何をやってるんスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xC,
        (
            "#11P今は共和国で刑期を終えて\x01",
            "まっとうに暮らしているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xC,
        (
            "#11P奴が起こした詐欺事件も、\x01",
            "規模が小さかったから\x01",
            "大きな罪には問われなかったようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#5P#0103Fだけど“前科”というものは\x01",
            "一生ついてまわる……\x02\x03",

            "#0108F入国申請書に前科があれば\x01",
            "旅行中も行動が制限されるから、\x01",
            "それを嫌ったんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xC,
        (
            "#11P詐欺などしなければ……\x01",
            "などと後悔はあるだろうが、\x01",
            "全ては自業自得だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xC,
        (
            "#11P罪は一生背負っていくしかない。\x01",
            "だから罪は犯してはならないのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        "#6P#0001F……結局、あの男はどうなるんですか？\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xC,
        "#11P奴は今、私の執務室で拘束している。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xC,
        (
            "#11P私が厳重注意を行なったあと、\x01",
            "共和国に送還されることになる。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xC,
        "#11Pまぁ、そこまで大事にもなるまい。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        "#6P#0003Fそうですか……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xC,
        (
            "#11P……ともあれ、つつがなく\x01",
            "全車両の臨検を終えることができた。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xC,
        (
            "#11P多少、定刻から遅れてしまったが……\x01",
            "無事列車を送り出すことができそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xC,
        (
            "#11P礼を言おうじゃないか、\x01",
            "特務支援課……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xC,
        "#11Pまた何かあったらよろしく頼むぞ。\x02",
    )

    CloseMessageWindow()
    OP_29(0x9, 0x1, 0xC)
    Jump("loc_2407")

    label("loc_2364")


    #C0080
    ChrTalk(
        0xC,
        (
            "#11Pつつがなく全車両の臨検を\x01",
            "終えることができた。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xC,
        (
            "#11Pおかげで定刻通りに\x01",
            "列車を送り出すことができそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xC,
        (
            "#11P礼を言おうじゃないか、\x01",
            "特務支援課……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2407")


    #C0083
    ChrTalk(
        0x101,
        (
            "#6P#0000Fいえ、自分たちも\x01",
            "随分勉強になったと思います。\x02\x03",

            "何かありましたら\x01",
            "是非またご連絡ください。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xC,
        "#11Pうむ、ではな。\x02",
    )

    CloseMessageWindow()
    OP_68(5080, 1000, -12450, 5000)
    MoveCamera(26, 13, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(17840, 5000)
    BeginChrThread(0xC, 1, 0, 13)
    BeginChrThread(0x101, 1, 0, 16)
    WaitChrThread(0xC, 1)
    EndChrThread(0x101, 0x1)

    def lambda_24CD():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24CD)

    def lambda_24DA():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_24DA)

    def lambda_24E7():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_24E7)

    def lambda_24F4():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_24F4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0085
    ChrTalk(
        0x101,
        (
            "#12P#0006Fふぅ……なかなか\x01",
            "大変な仕事だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x102,
        (
            "#11P#0100Fええ、ほんとに……\x02\x03",

            "#0106Fでも、私たちの中じゃ\x01",
            "ティオちゃんが一番疲れてるかも。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0087
    ChrTalk(
        0x101,
        "#12P#0005F……どういうことだ？\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x104,
        (
            "#5P#0309F『一日駅長』だか何かと勘違いされて、\x01",
            "乗客に随分と可愛いがられてたらしいぜ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0089
    ChrTalk(
        0x101,
        (
            "#12P#0005Fい、一日駅長って……\x01",
            "大丈夫なのか、ティオ？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x103,
        "#6P#0203F…………………………\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#12P#0005Fしゃ、喋る気力が無いほど\x01",
            "ゲッソリしてるのか……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        (
            "#6P#0206Fい、いえ。\x01",
            "ちょっと気疲れしただけですから\x01",
            "問題ありません。\x02\x03",

            "#0200F……行きましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#12P#0003Fそ、そうだな……\x01",
            "まぁ、無理だけはしないでくれよ。\x02",
        )
    )

    CloseMessageWindow()
    Sound(9, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0094
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【臨検官補佐求ム】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 5000, 0, -13500, 90)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_29(0x9, 0x1, 0xD)
    OP_29(0x9, 0x4, 0x10)
    OP_4C(0xC, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_15_1D37 end

    def Function_16_2854(): pass

    label("Function_16_2854")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28A8")

    def lambda_2864():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2864)

    def lambda_2871():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2871)

    def lambda_287E():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_287E)

    def lambda_288B():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_288B)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    Jump("Function_16_2854")

    label("loc_28A8")

    Return()

    # Function_16_2854 end

    def Function_17_28A9(): pass

    label("Function_17_28A9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(452)
    LoadChrToIndex("chr/ch20800.itc", 0x1E)
    LoadChrToIndex("chr/ch20900.itc", 0x1F)
    LoadChrToIndex("chr/ch20000.itc", 0x20)
    LoadChrToIndex("chr/ch20400.itc", 0x21)
    LoadChrToIndex("chr/ch20700.itc", 0x22)
    LoadChrToIndex("chr/ch28300.itc", 0x23)
    LoadChrToIndex("chr/ch20200.itc", 0x24)
    LoadChrToIndex("chr/ch20500.itc", 0x25)
    LoadChrToIndex("chr/ch28400.itc", 0x26)
    LoadChrToIndex("chr/ch21802.itc", 0x27)
    LoadChrToIndex("apl/ch50003.itc", 0x28)
    OP_68(17500, 3800, -200, 0)
    MoveCamera(58, 1, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(17000, 0)
    OP_EE(0x0, 0x1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 15700, 0, -9700, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xD, 15700, 0, -9700, 180)
    SetChrPos(0xE, 15700, 0, -9700, 180)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 3000, 0, -2600, 90)
    SetChrChipByIndex(0x10, 0x25)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 20000, 0, 2200, 270)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x2)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x1)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 19500, 100, -1300, 180)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -3000, 0, 3300, 90)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 20000, 0, -30000, 270)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 52500, 0, -13300, 45)
    SetChrChipByIndex(0x18, 0x27)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 32800, 100, -14600, 0)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    OP_49()
    SetChrPos(0x19, 7000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_E5()
    ClearChrFlags(0xF, 0x80)

    def lambda_2AFA():
        OP_95(0xFE, 40000, 0, -2600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2AFA)
    ClearChrFlags(0x10, 0x80)

    def lambda_2B19():
        OP_95(0xFE, 8000, 0, 2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2B19)
    ClearChrFlags(0x13, 0x80)
    OP_68(17500, 1800, -200, 10000)
    FadeToBright(2000, 0)
    OP_0D()
    ClearChrFlags(0x14, 0x80)

    def lambda_2B58():
        OP_95(0xFE, 34000, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2B58)
    OP_6F(0x1)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    Fade(1000)
    OP_68(27000, 1500, -15000, 0)
    MoveCamera(54, 5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(28000, 0)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)

    def lambda_2BC9():
        OP_95(0xFE, 12000, 0, -30000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2BC9)
    MoveCamera(60, 5, 0, 8000)
    SetCameraDistance(38000, 8000)
    WaitChrThread(0x16, 1)
    PlaceName2(340, 200, "c_plac00", 0x0, 0)
    Sleep(2000)

    def lambda_2C0F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_2C0F)
    WaitChrThread(0x16, 2)
    Sleep(500)

    def lambda_2C23():
        OP_95(0xFE, 22000, 0, -30000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2C23)
    OP_6F(0x40)
    OP_6F(0x10)
    Sleep(1000)
    Fade(500)
    OP_68(57000, 1500, -8500, 0)
    OP_6E(780, 0)
    SetCameraDistance(21000, 0)
    MoveCamera(53, 2, 0, 0)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_68(10000, 500, -8500, 10000)
    MoveCamera(57, 12, 0, 10000)
    ClearMapObjFlags(0x1, 0x4)
    BeginChrThread(0x19, 3, 0, 18)
    WaitChrThread(0x19, 3)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_68(18400, -900, -4400, 0)
    MoveCamera(54, 10, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(30500, 0)
    SetCameraDistance(33500, 20000)
    Sleep(1000)
    Sound(454, 0, 100, 0)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    OP_79(0x1)
    BeginChrThread(0x11, 3, 0, 21)
    Sleep(500)
    BeginChrThread(0x12, 3, 0, 20)
    Sleep(500)
    BeginChrThread(0xF, 3, 0, 22)
    Sleep(800)
    BeginChrThread(0x14, 3, 0, 20)
    Sleep(2200)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(300)
    BeginChrThread(0x10, 3, 0, 23)
    Sleep(700)
    BeginChrThread(0x15, 3, 0, 23)
    BeginChrThread(0xD, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0xE, 3, 0, 21)
    Sleep(8000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    OP_EE(0x0, 0xA)
    OP_E6()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_28A9 end

    def Function_18_2DE6(): pass

    label("Function_18_2DE6")

    Sound(452, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x3D, 0x168, 0x0, 0x0)
    Sleep(2000)

    def lambda_2E04():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_2E04)
    OP_79(0x1)
    Sound(143, 0, 100, 0)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    Sleep(500)
    Return()

    # Function_18_2DE6 end

    def Function_19_2E2A(): pass

    label("Function_19_2E2A")


    def lambda_2E2F():
        OP_96(0xFE, 0x1B58, 0xFFFFF9F2, 0xFFFFE05C, 0x2260, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2E2F)
    Sleep(2000)

    def lambda_2E4C():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_2E4C)
    Sleep(1000)

    def lambda_2E5C():
        OP_96(0xFE, 0x1B58, 0xFFFFF9F2, 0xFFFFE05C, 0x1E78, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2E5C)
    Sleep(2000)

    def lambda_2E79():
        OP_96(0xFE, 0x1B58, 0xFFFFF9F2, 0xFFFFE05C, 0x1A90, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2E79)
    Sleep(2000)

    def lambda_2E96():
        OP_96(0xFE, 0x1B58, 0xFFFFF9F2, 0xFFFFE05C, 0x16A8, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2E96)
    Sleep(2000)

    def lambda_2EB3():
        OP_96(0xFE, 0x1B58, 0xFFFFF9F2, 0xFFFFE05C, 0x12C0, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2EB3)
    Sleep(1500)

    def lambda_2ED0():
        OP_96(0xFE, 0x1B58, 0xFFFFF9F2, 0xFFFFE05C, 0xED8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2ED0)
    WaitChrThread(0x19, 1)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    Sleep(500)
    Return()

    # Function_19_2E2A end

    def Function_20_2EFE(): pass

    label("Function_20_2EFE")

    SetChrPos(0xFE, 6000, 0, -9700, 180)

    def lambda_2F14():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F14)

    def lambda_2F25():
        OP_95(0xFE, 6000, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F25)
    WaitChrThread(0xFE, 1)

    def lambda_2F43():
        OP_95(0xFE, -5000, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F43)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_20_2EFE end

    def Function_21_2F5D(): pass

    label("Function_21_2F5D")

    SetChrPos(0xFE, 15700, 0, -9700, 180)

    def lambda_2F73():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F73)

    def lambda_2F84():
        OP_95(0xFE, 15700, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F84)
    WaitChrThread(0xFE, 1)

    def lambda_2FA2():
        OP_95(0xFE, -5000, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FA2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_21_2F5D end

    def Function_22_2FBC(): pass

    label("Function_22_2FBC")

    SetChrPos(0xFE, 18700, 0, -9700, 180)

    def lambda_2FD2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FD2)

    def lambda_2FE3():
        OP_95(0xFE, 18700, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FE3)
    WaitChrThread(0xFE, 1)

    def lambda_3001():
        OP_95(0xFE, -5000, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3001)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_2FBC end

    def Function_23_301B(): pass

    label("Function_23_301B")

    SetChrPos(0xFE, 28400, 0, -9700, 180)

    def lambda_3031():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3031)

    def lambda_3042():
        OP_95(0xFE, 28400, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3042)
    WaitChrThread(0xFE, 1)

    def lambda_3060():
        OP_95(0xFE, -5000, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3060)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_301B end

    def Function_24_307A(): pass

    label("Function_24_307A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(453)
    SoundLoad(805)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x0, 0x19)
    OP_49()
    SetChrPos(0x19, 55000, -1550, 8000, 0)
    OP_D3(0x19, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_70(0x0, 0x1E)
    OP_68(-22350, 3240, -810, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -21570, 600, 190, 90)
    SetChrPos(0x102, -21570, 600, -1220, 90)
    SetChrPos(0x103, -22700, 600, -1220, 90)
    SetChrPos(0x104, -22700, 600, 190, 90)
    OP_68(-14120, 2100, 690, 2000)

    def lambda_3152():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3152)

    def lambda_3167():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3167)

    def lambda_317C():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_317C)

    def lambda_3191():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3191)
    StopBGM(0x1388)
    Sound(805, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x3, 1)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("駅員の声")

    #A0095
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "１番線、共和国行き列車、\x01",
            "発車いたします。\x02",
        )
    )

    CloseMessageWindow()

    #A0096
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "お見送りのお客様は\x01",
            "ホーム中ほどまでお下がりください。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_3297():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3297)

    def lambda_32A4():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_32A4)

    def lambda_32B1():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_32B1)

    def lambda_32BE():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_32BE)
    Sleep(300)

    #C0097
    ChrTalk(
        0x104,
        (
            "#5P#0305Fおい……\x01",
            "あれが議員令嬢の乗ってる\x01",
            "列車じゃねえのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#11P#0001Fまだ間に合う……\x01",
            "このまま乗り込もう！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x2, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_3390():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3390)

    def lambda_339D():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_339D)

    def lambda_33AA():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_33AA)

    def lambda_33B7():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_33B7)
    WaitChrThread(0x3, 1)
    BeginChrThread(0x19, 3, 0, 25)
    BeginChrThread(0x101, 3, 0, 26)
    Sleep(150)
    BeginChrThread(0x102, 3, 0, 26)
    Sleep(250)
    BeginChrThread(0x104, 3, 0, 26)
    Sleep(150)
    BeginChrThread(0x103, 3, 0, 26)
    Sleep(2000)
    BeginChrThread(0x1D, 0, 0, 37)
    Sleep(3000)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x104, 3)
    EndChrThread(0x1D, 0x0)
    Sound(454, 0, 100, 0)
    OP_71(0x0, 0x14, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    Sound(143, 0, 100, 0)
    OP_82(0x64, 0x32, 0xBB8, 0x1F4)
    Sleep(800)
    Fade(500)
    OP_68(5700, 1500, 4200, 0)
    MoveCamera(58, 1, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(17000, 0)
    OP_EE(0x0, 0x1)
    OP_0D()
    BeginChrThread(0x19, 1, 0, 27)
    OP_68(61700, 1500, 4200, 9000)
    Sleep(8000)
    BeginChrThread(0x1D, 0, 0, 36)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    EndChrThread(0x1D, 0x0)
    OP_EE(0x0, 0xA)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x325)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 0)
    NewScene("r0040", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_307A end

    def Function_25_3514(): pass

    label("Function_25_3514")

    OP_68(-9530, 2100, -200, 2000)
    OP_6F(0x1)
    OP_68(700, 1500, 4200, 1500)
    MoveCamera(44, 13, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(18000, 1500)
    Return()

    # Function_25_3514 end

    def Function_26_3556(): pass

    label("Function_26_3556")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x1)
    OP_95(0xFE, -1000, 0, 3000, 5000, 0x1)

    def lambda_357E():
        OP_95(0xFE, -1000, 0, 7000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_357E)
    Sleep(400)

    def lambda_359B():
        OP_A7(0xFE, 0x0, 0x0, 0x0, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_359B)
    OP_64(0xFE)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_26_3556 end

    def Function_27_35B3(): pass

    label("Function_27_35B3")

    Sound(453, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x169, 0x294, 0x0, 0x0)
    Return()

    # Function_27_35B3 end

    def Function_28_35CA(): pass

    label("Function_28_35CA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(452)
    LoadChrToIndex("chr/ch20800.itc", 0x1E)
    LoadChrToIndex("chr/ch20900.itc", 0x1F)
    LoadChrToIndex("chr/ch20000.itc", 0x20)
    LoadChrToIndex("chr/ch20400.itc", 0x21)
    LoadChrToIndex("chr/ch20700.itc", 0x22)
    LoadChrToIndex("chr/ch28300.itc", 0x23)
    LoadChrToIndex("chr/ch20200.itc", 0x24)
    LoadChrToIndex("chr/ch20500.itc", 0x25)
    LoadChrToIndex("chr/ch28400.itc", 0x26)
    LoadChrToIndex("chr/ch21802.itc", 0x27)
    LoadChrToIndex("chr/ch27700.itc", 0x28)
    LoadChrToIndex("chr/ch33200.itc", 0x29)
    LoadChrToIndex("chr/ch34500.itc", 0x2A)
    LoadChrToIndex("apl/ch50111.itc", 0x2B)
    SoundLoad(803)
    OP_68(17500, 3800, -200, 0)
    MoveCamera(58, 1, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(17000, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x0, 15700, 0, -9700, 180)
    SetChrPos(0x1, 15700, 0, -9700, 180)
    SetChrPos(0x2, 15700, 0, -9700, 180)
    SetChrPos(0x3, 15700, 0, -9700, 180)
    SetChrPos(0x1B, 15700, 0, -9700, 180)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1B, 0x29)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1A, 0x28)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1C, 0x2A)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x12, 0x2)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -3000, 0, 3300, 90)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 3000, 0, -2600, 90)
    SetChrChipByIndex(0x10, 0x25)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 20000, 0, 2200, 270)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x23)
    SetChrChipByIndex(0x13, 0x1)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 19500, 100, -1300, 180)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 20000, 0, -30000, 270)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 52500, 0, -13300, 45)
    SetChrChipByIndex(0x18, 0x27)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 32800, 100, -14600, 0)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    OP_49()
    SetChrPos(0x19, 7000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetChrName("")

    #A0099
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイド達はアルタイル市で\x01",
            "折り返しの便に乗り換えた。\x02",
        )
    )

    CloseMessageWindow()

    #A0100
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そして更に３０分後……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7103", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 2)
    Sound(803, 2, 100, 0)
    ClearScenarioFlags(0x0, 3)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    Sleep(2500)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_68(61500, 2500, -10500, 0)
    MoveCamera(60, 15, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(16000, 0)
    OP_EE(0x0, 0x1)
    OP_68(58500, 2500, -11500, 5000)
    MoveCamera(45, 20, 0, 5000)
    SetCameraDistance(24000, 5000)
    ClearMapObjFlags(0x1, 0x4)
    BeginChrThread(0x19, 3, 0, 18)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(5500, 3300, -8000, 0)
    MoveCamera(48, -15, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(14000, 0)
    OP_68(5500, 2300, -8000, 4000)
    OP_0D()
    WaitChrThread(0x19, 3)
    OP_6F(0x1)
    Sleep(1000)
    Fade(500)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_68(18400, -900, -4400, 0)
    MoveCamera(54, 10, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(30500, 0)
    SetCameraDistance(33500, 20000)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_3A5B")
    Call(0, 29)
    Jump("loc_3A5E")

    label("loc_3A5B")

    Call(0, 32)

    label("loc_3A5E")

    Return()

    # Function_28_35CA end

    def Function_29_3A5F(): pass

    label("Function_29_3A5F")

    Sound(454, 0, 100, 0)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    OP_79(0x1)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    BeginChrThread(0x11, 3, 0, 21)
    Sleep(500)
    BeginChrThread(0x12, 3, 0, 20)
    Sleep(500)
    BeginChrThread(0xF, 3, 0, 22)
    Sleep(800)
    BeginChrThread(0x14, 3, 0, 20)
    Sleep(2200)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(300)
    BeginChrThread(0x10, 3, 0, 23)
    Sleep(700)
    BeginChrThread(0x15, 3, 0, 23)
    BeginChrThread(0x102, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x1B, 3, 0, 21)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x0, 0x2)
    EndChrThread(0x0, 0x3)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x1, 0x2)
    EndChrThread(0x1, 0x3)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x2, 0x2)
    EndChrThread(0x2, 0x3)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x3, 0x2)
    EndChrThread(0x3, 0x3)
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1B, 0x2)
    EndChrThread(0x1B, 0x3)
    EndChrThread(0xF, 0x1)
    EndChrThread(0xF, 0x2)
    EndChrThread(0xF, 0x3)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x1B, 0x0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrPos(0x101, 4059, 0, -15180, 45)
    SetChrPos(0x102, 4920, 0, -15560, 0)
    SetChrPos(0x103, 3910, 0, -13780, 135)
    SetChrPos(0x104, 4810, 0, -12940, 180)
    SetChrPos(0x1B, 5870, 0, -14030, 270)
    SetChrPos(0xF, 5500, 0, -14560, 270)
    SetChrPos(0x1A, -7130, 600, -15750, 90)
    SetChrPos(0x1C, -9130, 600, -16740, 90)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    OP_68(4760, 1500, -14530, 0)
    MoveCamera(49, 27, 0, 0)
    OP_6E(720, 0)
    SetCameraDistance(12050, 0)
    OP_EE(0x0, 0xA)
    FadeToBright(1000, 0)
    OP_0D()

    #C0101
    ChrTalk(
        0x104,
        "#5P#0306Fふう、ようやく戻ってきたぜ。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x103,
        "#6P#0200F色々と長かったですね。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x1B,
        "#11Pその、ご迷惑をお掛けしましたわ。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x1B,
        (
            "#11P話まで聞いていただいて、\x01",
            "本当にありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x102,
        "#12P#0100Fふふ、気になさらないで下さい。\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        (
            "#6P#0000F相談ならいくらでも乗りますし。\x01",
            "また何かあれば\x01",
            "支援課を頼ってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x1B,
        "#11Pは、はい……\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(200)
    TurnDirection(0x1B, 0x1A, 400)
    Sleep(400)

    #C0108
    ChrTalk(
        0x1B,
        "#11Pあ……\x02",
    )

    CloseMessageWindow()
    OP_68(1960, 1500, -15420, 3000)
    MoveCamera(320, 30, 0, 3000)

    def lambda_3E26():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E26)

    def lambda_3E33():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E33)

    def lambda_3E40():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3E40)

    def lambda_3E4D():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3E4D)

    def lambda_3E5A():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3E5A)

    def lambda_3E6F():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_3E6F)
    Sleep(2500)
    Sleep(800)

    #C0109
    ChrTalk(
        0x1A,
        (
            "#5Pフン、馬鹿娘め。\x01",
            "こんな時に心配を掛けおって。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x1B,
        "#12Pお、お父様こそなんですの！？\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x1B,
        (
            "#12P自分で説得に来るならまだしも、\x01",
            "人をよこすなんて……！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 1, 0, 30)
    OP_96(0x1C, 0xFFFFFCD6, 0x0, 0xFFFFBEB0, 0x3E8, 0x0)
    TurnDirection(0x1C, 0x1B, 400)
    Sleep(300)

    #C0112
    ChrTalk(
        0x1C,
        "#5Pあのお嬢様……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x1C,
        (
            "#5Pす、すみませんでした。\x01",
            "差し出がましい事をして……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1B, 0xE1, 0x190)
    Sleep(300)

    #C0114
    ChrTalk(
        0x1B,
        (
            "#12Pフン、全くですわ！\x01",
            "マーシャにも怒ってますのよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x1C,
        "#5Pす、す、すみません……\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x1B,
        (
            "#12Pでも、その……\x01",
            "感謝してますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x1B,
        "#12Pまた、傍に居てくれます？\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x1C,
        "#5Pは、はい、喜んで。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x1B,
        (
            "#12P……よかった。\x01",
            "これで決心が付きましたわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1A, 400)
    Sleep(300)

    #C0120
    ChrTalk(
        0x1B,
        "#12Pお父様、要求がありますわ。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x1B,
        (
            "#12P今後部屋に入るときは\x01",
            "必ずノックしていただきます！\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x1B,
        (
            "#12Pそれと、今後は私の私生活に\x01",
            "一切口を挟まないでもらいますわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x1B,
        (
            "#12P……でないと私、\x01",
            "今から家出しますわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x1A,
        "#5Pむむむ……\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x1A,
        (
            "#5Pまあいい、しばらく家で\x01",
            "大人しくしておれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x1B,
        (
            "#12P要求を受けるんですの？\x01",
            "受けないんですの！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x101, 0)

    #C0127
    ChrTalk(
        0x1A,
        (
            "#5Pフン、心配せんでも\x01",
            "こんな騒動は二度とゴメンだ！\x01",
            "約束は守ってやる。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(2670, 1500, -15870, 2000)

    def lambda_4254():

        label("loc_4254")

        TurnDirection(0xFE, 0x1A, 400)
        Yield()
        Jump("loc_4254")

    QueueWorkItem2(0x1B, 1, lambda_4254)

    def lambda_4266():

        label("loc_4266")

        TurnDirection(0xFE, 0x1A, 400)
        Yield()
        Jump("loc_4266")

    QueueWorkItem2(0x1C, 1, lambda_4266)

    def lambda_4278():
        OP_95(0xFE, 2040, 0, -14970, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4278)
    Sleep(300)
    OP_96(0x1B, 0x244, 0x0, 0xFFFFC180, 0x3E8, 0x0)
    Sleep(400)

    #C0128
    ChrTalk(
        0x1A,
        "#5P警察の何とか課だったか。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x1A,
        (
            "#5P無事に娘を連れ戻してくれた事、\x01",
            "一応礼を言っておこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x1A,
        (
            "#5Pただし、覚えているだろうが\x01",
            "今回の事は他言無用だぞ。\x01",
            "分かっているな！？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        "#11P#0300Fええ、モチロンっす。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        "#12P#0000Fその点はご安心下さい。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x1A,
        "#5Pなら、よし。\x02",
    )

    CloseMessageWindow()
    OP_95(0x1A, -630, 0, -14820, 2000, 0x0)

    #C0134
    ChrTalk(
        0x1A,
        "#5Pカーラ、帰るぞ！\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x1B,
        "#12Pフン、指図しないでくださいな！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1A, 0, 0, 31)
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1C, 0x1)

    def lambda_441C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_441C)

    def lambda_4429():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_4429)
    Sleep(300)

    #C0136
    ChrTalk(
        0x1B,
        (
            "#5Pエリィさん、皆さん。\x01",
            "……それではまた。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x1C,
        (
            "#5Pみなさん、本当に\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x1C,
        (
            "#5Pあの、また家の方に\x01",
            "お寄りになってください。\x01",
            "お持て成ししますから……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")
    FadeToDark(300, 0, 100)

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "２人は深々と頭を下げた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    BeginChrThread(0x1B, 1, 0, 31)

    def lambda_4526():

        label("loc_4526")

        TurnDirection(0xFE, 0x1B, 400)
        Yield()
        Jump("loc_4526")

    QueueWorkItem2(0x1C, 1, lambda_4526)
    Sleep(1200)
    BeginChrThread(0x1C, 1, 0, 31)
    OP_63(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(2400)

    #C0140
    ChrTalk(
        0x101,
        "#12P#0004Fま、何とか丸く収まったか。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x104,
        (
            "#11P#0300F時間は食ったが、\x01",
            "一つ人助けした気分だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x103,
        (
            "#11P#0200Fまあ、あの様子だと\x01",
            "大丈夫そうです。\x01",
            "良かったのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        (
            "#12P#0104Fそうね……\x01",
            "上手く行く事を祈ってるわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(4580, 1500, -14920, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12550, 0)
    SetChrPos(0x102, 5380, 0, -15280, 270)
    OP_0D()

    def lambda_4680():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4680)

    def lambda_468D():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_468D)

    def lambda_469A():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_469A)

    def lambda_46A7():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_46A7)
    Sleep(300)

    #C0144
    ChrTalk(
        0x102,
        (
            "#11P#0100Fそれじゃあロイド、\x01",
            "そろそろ戻りましょうか。\x02\x03",

            "まだ片付けなくちゃいけない\x01",
            "仕事が残っているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        (
            "#6P#0005Fおっと、そうだった……\x02\x03",

            "#0000Fよし、切り上げるとしようか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0146
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【要人の捜索依頼】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_64(0x1C)
    SetChrPos(0x0, 4780, 0, -14570, 275)
    ClearChrFlags(0x8, 0x80)
    OP_70(0x1, 0x0)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_29(0x2D, 0x4, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_29_3A5F end

    def Function_30_4898(): pass

    label("Function_30_4898")

    OP_96(0xFE, 0xDC0, 0x0, 0xFFFFC89C, 0x7D0, 0x0)
    OP_96(0xFE, 0x244, 0x0, 0xFFFFC39C, 0x7D0, 0x0)
    Return()

    # Function_30_4898 end

    def Function_31_48C1(): pass

    label("Function_31_48C1")

    OP_93(0xFE, 0x10E, 0x190)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_31_48C1 end

    def Function_32_48E2(): pass

    label("Function_32_48E2")

    Sound(454, 0, 100, 0)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    OP_79(0x1)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    BeginChrThread(0x11, 3, 0, 21)
    Sleep(500)
    BeginChrThread(0x12, 3, 0, 20)
    Sleep(500)
    BeginChrThread(0xF, 3, 0, 22)
    Sleep(800)
    BeginChrThread(0x14, 3, 0, 20)
    Sleep(2200)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(300)
    BeginChrThread(0x10, 3, 0, 23)
    Sleep(700)
    BeginChrThread(0x15, 3, 0, 23)
    BeginChrThread(0x102, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 21)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x0, 0x2)
    EndChrThread(0x0, 0x3)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x1, 0x2)
    EndChrThread(0x1, 0x3)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x2, 0x2)
    EndChrThread(0x2, 0x3)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x3, 0x2)
    EndChrThread(0x3, 0x3)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrPos(0x101, 3910, 0, -14550, 90)
    SetChrPos(0x102, 4920, 0, -15560, 0)
    SetChrPos(0x103, 5870, 0, -14030, 270)
    SetChrPos(0x104, 4810, 0, -12940, 180)
    SetChrPos(0x1C, -8130, 600, -16740, 90)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    OP_68(4760, 1500, -14530, 0)
    MoveCamera(49, 27, 0, 0)
    OP_6E(720, 0)
    SetCameraDistance(12050, 0)
    OP_EE(0x0, 0xA)
    FadeToBright(1000, 0)
    OP_0D()

    #C0147
    ChrTalk(
        0x104,
        "#5P#0306Fふう、ようやく戻ってきたぜ。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x103,
        "#11P#0203F色々と長かったですね。\x02",
    )

    CloseMessageWindow()

    #N0149
    NpcTalk(
        0x1C,
        "声",
        "あ、あの皆さん……\x02",
    )

    CloseMessageWindow()
    OP_68(2670, 1500, -15870, 3000)
    MoveCamera(320, 30, 0, 3000)

    def lambda_4B2F():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B2F)

    def lambda_4B3C():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4B3C)

    def lambda_4B49():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4B49)

    def lambda_4B56():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4B56)
    OP_95(0x1C, 130, 0, -15210, 2000, 0x0)
    Sleep(300)

    #C0150
    ChrTalk(
        0x1C,
        (
            "#5Pお嬢様は……\x01",
            "カーラ様のお具合は……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#12P#0006Fすみません、実は\x01",
            "説得に失敗してしまいまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x102,
        (
            "#6P#0106Fカーラさんはあのまま\x01",
            "共和国に行ってしまったんです。\x02\x03",

            "#0108Fごめんなさい、\x01",
            "折角話を聞かせてくれたのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x1C,
        (
            "#5Pい、いえ……\x01",
            "皆さんのせいじゃないです。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x1C,
        (
            "#5P私がちゃんと\x01",
            "お止めできなかったから……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0155
    ChrTalk(
        0x1C,
        (
            "#5Pあ、でも……旦那様には\x01",
            "なんと言えばいいのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x1C,
        (
            "#5Pこのままでは私、\x01",
            "クビになってしまうかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x102,
        (
            "#6P#0103Fキャンベル議員には\x01",
            "私から連絡を入れておくわ。\x02\x03",

            "#0100Fあなたの事も伝えておくから、\x01",
            "心配しないで戻って頂戴。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x1C,
        "#5Pほ、本当ですか……？\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x1C,
        (
            "#5P分かりました、\x01",
            "それではよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x1C,
        (
            "#5Pあ、あの、本当に\x01",
            "お世話になりました……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")
    FadeToDark(300, 0, 100)

    #A0161
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "マーシャは深々と頭を下げた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    BeginChrThread(0x1C, 1, 0, 31)
    Sleep(2400)

    #C0162
    ChrTalk(
        0x104,
        (
            "#12P#0306Fふう……\x01",
            "ま、仕方ねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x103,
        (
            "#12P#0200F連絡先は聞いておきましたし、\x01",
            "警察として最低限の\x01",
            "対応はしたかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそうだな、身の安全は\x01",
            "確認できたわけだし。\x02\x03",

            "後は議員への報告だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x102,
        (
            "#6P#0103F私から連絡を入れるわね。\x01",
            "……マーシャさんが戻る前に\x01",
            "一通り伝えておかないと。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_68(4580, 1500, -14920, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12550, 0)
    OP_0D()

    def lambda_4FDE():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FDE)
    Sleep(20)

    def lambda_4FEE():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4FEE)
    Sleep(12)

    def lambda_4FFE():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4FFE)
    Sleep(80)
    OP_93(0x102, 0xB4, 0x190)
    Sleep(300)
    Fade(300)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    Sleep(600)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2800)
    OP_64(0x102)
    Sleep(300)
    SetChrName("")
    FadeToDark(300, 0, 100)

    #A0166
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィはキャンベル議員を呼び出し、\x01",
            "事のあらましとカーラの連絡先を伝えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    OP_93(0x102, 0x0, 0x190)
    Sleep(200)

    #C0167
    ChrTalk(
        0x101,
        "#6P#0005F議員は何だって？\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x102,
        "#12P#0103F『ご苦労だった』ですって。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x104,
        (
            "#5P#0306Fやれやれ、\x01",
            "張り合いのねえ反応だなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x103,
        "#11P#0203Fまあ予想通りかと。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    Sleep(300)

    #C0171
    ChrTalk(
        0x103,
        (
            "#11P#0200F……ロイドさん、\x01",
            "そろそろ戻りましょうか。\x01",
            "他の仕事も残っている事ですし。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(300)

    #C0172
    ChrTalk(
        0x101,
        (
            "#11P#0005Fおっと、そうだった……\x02\x03",

            "#0000Fよし、切り上げるとしようか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0173
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【要人の捜索依頼】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 4780, 0, -14570, 275)
    OP_70(0x1, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_29(0x2D, 0x4, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_32_48E2 end

    def Function_33_5356(): pass

    label("Function_33_5356")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xC)"), scpexpr(EXPR_END)), "loc_53D2")

    #C0174
    ChrTalk(
        0x101,
        (
            "#0003Fこっちは別のホームへの\x01",
            "連絡路だな。\x02\x03",

            "#0000F仕事も済んだし、寄り道せずに\x01",
            "引き上げるとしよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_548F")

    label("loc_53D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_542D")

    #C0175
    ChrTalk(
        0x101,
        (
            "#0000F臨検も終わったことだし……\x01",
            "共和国行きのホームには\x01",
            "用はないな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_548F")

    label("loc_542D")


    #C0176
    ChrTalk(
        0x101,
        (
            "#0003Fこっちは別のホームへの\x01",
            "連絡路だな。\x02\x03",

            "#0001F列車が行ってしまう前に\x01",
            "仕事を始めないと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_548F")

    Sleep(50)
    SetChrPos(0x0, 54500, 0, -16000, 270)
    EventEnd(0x4)
    Return()

    # Function_33_5356 end

    def Function_34_54A6(): pass

    label("Function_34_54A6")

    TalkBegin(0xFF)
    SetChrName("")

    #A0177
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル自治州周辺の\x01",
            "時刻表がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_34_54A6 end

    def Function_35_54DF(): pass

    label("Function_35_54DF")

    TalkBegin(0xFF)
    SetChrName("")

    #A0178
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル自治州周辺の\x01",
            "路線図がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_35_54DF end

    def Function_36_5518(): pass

    label("Function_36_5518")

    OP_25(0x323, 0x64)
    Sleep(200)
    OP_25(0x323, 0x5A)
    Sleep(200)
    OP_25(0x323, 0x50)
    Sleep(200)
    OP_25(0x323, 0x46)
    Sleep(200)
    OP_25(0x323, 0x3C)
    Sleep(200)
    OP_25(0x323, 0x32)
    Sleep(200)
    OP_25(0x323, 0x28)
    Sleep(200)
    OP_25(0x323, 0x1E)
    Sleep(200)
    OP_25(0x323, 0x14)
    Sleep(200)
    OP_25(0x323, 0xA)
    Sleep(200)
    OP_25(0x323, 0x0)
    Return()

    # Function_36_5518 end

    def Function_37_5563(): pass

    label("Function_37_5563")

    OP_25(0x325, 0x64)
    Sleep(80)
    OP_25(0x325, 0x5A)
    Sleep(80)
    OP_25(0x325, 0x50)
    Sleep(80)
    OP_25(0x325, 0x46)
    Sleep(80)
    OP_25(0x325, 0x3C)
    Sleep(80)
    OP_25(0x325, 0x32)
    Sleep(80)
    OP_25(0x325, 0x28)
    Sleep(80)
    OP_25(0x325, 0x1E)
    Sleep(80)
    OP_25(0x325, 0x14)
    Sleep(80)
    OP_25(0x325, 0xA)
    Sleep(80)
    OP_25(0x325, 0x0)
    Return()

    # Function_37_5563 end

    SaveToFile()

Try(main)
