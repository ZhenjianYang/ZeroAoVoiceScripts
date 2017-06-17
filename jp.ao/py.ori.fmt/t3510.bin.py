from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t3510.bin",                # FileName
        "t3510",                    # MapName
        "t3510",                    # Location
        0x005C,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x01',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 92, 0, 2, 0, 3],
    )

    BuildStringList((
        "t3510",                  # 0
        "受付嬢マルカナ",         # 1
        "受付トーマス",           # 2
        "リカルド",               # 3
        "観光客",                 # 4
        "観光客",                 # 5
        "観光客",                 # 6
        "市民",                   # 7
        "市民",                   # 8
        "男の子",                 # 9
        "運送員アロン",           # 10
        "ビリー",                 # 11
        "女性士官",               # 12
        "飛空挺",                 # 13
        "警官",                   # 14
        "警官",                   # 15
        "グレイス",               # 16
        "レインズ",               # 17
        "記者ノティシア",         # 18
        "記者",                   # 19
        "記者",                   # 20
        "記者",                   # 21
        "記者",                   # 22
    ))

    AddCharChip((
        "chr/ch10500.itc",                   # 00
        "chr/ch23600.itc",                   # 01
        "chr/ch26000.itc",                   # 02
        "chr/ch28200.itc",                   # 03
        "chr/ch28100.itc",                   # 04
        "chr/ch22000.itc",                   # 05
        "chr/ch22100.itc",                   # 06
        "chr/ch21800.itc",                   # 07
        "chr/ch20200.itc",                   # 08
        "chr/ch20302.itc",                   # 09
        "chr/ch34202.itc",                   # 0A
    ))

    DeclNpc(-10220,  150,     2849,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-8350,   150,     6730,    135,  261,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(6679,    0,       5530,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-11300,  5000,    4760,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-10729,  5000,    5769,    225,  389,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-1039,   5000,    13960,   315,  389,  0x0, 0,   7,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-5679,   0,       -2539,   225,  389,  0x0, 0,   8,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-10319,  5199,    8109,    45,   389,  0x0, 0,   9,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(-8869,   5199,    10039,   225,  389,  0x0, 0,   10,  0,   255, 255, 0,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 18,  0.25999999046325684,   7.989999771118164,     0.0,                   36.0,                  [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   -0.04333333298563957,  -3.994999885559082,    -0.0,                  1.0])

    DeclActor(-8690,   0,       2530,    1000,    -10220,  1600,    2850,    0x007E, 0,  7,  0x0000)
    DeclActor(-7210,   0,       5680,    1000,    -8350,   1600,    6730,    0x007E, 0,  9,  0x0000)
    DeclActor(-7590,   0,       -2440,   1200,    -7590,   1500,    -2440,   0x007C, 0,  17, 0x0000)

    ChipFrameInfo(1136, 0)                                       # 0

    ScpFunction((
        "Function_0_470",          # 00, 0
        "Function_1_520",          # 01, 1
        "Function_2_56D",          # 02, 2
        "Function_3_6EA",          # 03, 3
        "Function_4_75D",          # 04, 4
        "Function_5_A2C",          # 05, 5
        "Function_6_AEF",          # 06, 6
        "Function_7_107F",         # 07, 7
        "Function_8_1083",         # 08, 8
        "Function_9_1586",         # 09, 9
        "Function_10_158A",        # 0A, 10
        "Function_11_1A84",        # 0B, 11
        "Function_12_1B01",        # 0C, 12
        "Function_13_1B97",        # 0D, 13
        "Function_14_1C33",        # 0E, 14
        "Function_15_1CD8",        # 0F, 15
        "Function_16_1D4D",        # 10, 16
        "Function_17_1DBA",        # 11, 17
        "Function_18_1E99",        # 12, 18
        "Function_19_1FE0",        # 13, 19
        "Function_20_21C6",        # 14, 20
        "Function_21_227F",        # 15, 21
        "Function_22_2BF8",        # 16, 22
        "Function_23_2E2E",        # 17, 23
        "Function_24_2F82",        # 18, 24
        "Function_25_30A0",        # 19, 25
        "Function_26_3A93",        # 1A, 26
        "Function_27_3F9F",        # 1B, 27
        "Function_28_47F6",        # 1C, 28
        "Function_29_4992",        # 1D, 29
        "Function_30_4ACE",        # 1E, 30
    ))


    def Function_0_470(): pass

    label("Function_0_470")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_4A8"),
        (1, "loc_4B4"),
        (2, "loc_4C0"),
        (3, "loc_4CC"),
        (4, "loc_4D8"),
        (5, "loc_4E4"),
        (6, "loc_4F0"),
        (SWITCH_DEFAULT, "loc_4FC"),
    )


    label("loc_4A8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4B4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4C0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4CC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4D8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4E4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4FC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_508")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_51F")

    Return()

    # Function_0_470 end

    def Function_1_520(): pass

    label("Function_1_520")

    SetMapObjFlags(0x0, 0x2000000)
    SetMapObjFlags(0x2, 0x2000000)
    SetMapObjFlags(0x5, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_546")
    ClearMapObjFlags(0x5, 0x2000000)
    Jump("loc_555")

    label("loc_546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_555")
    ClearMapObjFlags(0x5, 0x2000000)

    label("loc_555")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56C")
    ClearMapObjFlags(0x0, 0x2000000)

    label("loc_56C")

    Return()

    # Function_1_520 end

    def Function_2_56D(): pass

    label("Function_2_56D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_594")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 6600, 0, -3500, 180)

    label("loc_594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5D5")
    SetChrPos(0x8, 0, 0, -5500, 90)
    SetChrPos(0x9, 1500, 0, -5500, 270)
    SetChrPos(0xA, 340, 0, 6490, 180)
    Jump("loc_6A7")

    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5E3")
    Jump("loc_6A7")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5F1")
    Jump("loc_6A7")

    label("loc_5F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_66E")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xF, 0x9)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x10, 0xA)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_669")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 5480, 0, 5530, 90)
    TurnDirection(0xA, 0x12, 0)

    label("loc_669")

    Jump("loc_6A7")

    label("loc_66E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_67C")
    Jump("loc_6A7")

    label("loc_67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_69E")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x10)
    Jump("loc_6A7")

    label("loc_69E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6A7")

    label("loc_6A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_6BE")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 4)
    Event(0, 19)
    Jump("loc_6E9")

    label("loc_6BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_6D5")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 4)
    Event(0, 21)
    Jump("loc_6E9")

    label("loc_6D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_6E9")
    ClearScenarioFlags(0x22, 2)
    SetMapFlags(0x10000000)
    Event(0, 26)

    label("loc_6E9")

    Return()

    # Function_2_56D end

    def Function_3_6EA(): pass

    label("Function_3_6EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6FE")
    OP_24(0x86)
    ClearScenarioFlags(0x0, 4)
    Jump("loc_71A")

    label("loc_6FE")

    SoundDistance(0x86, 0x16D0, 0x0, 0x259E, 0x1388, 0x30D40, 0x64, 0x0)

    label("loc_71A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_72B")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)

    label("loc_72B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_745")
    ModifyEventFlags(0, 0, 0x80)
    ClearMapObjFlags(0x3, 0x10)
    ClearMapObjFlags(0x4, 0x10)

    label("loc_745")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75C")
    ClearMapObjFlags(0x0, 0x4)

    label("loc_75C")

    Return()

    # Function_3_6EA end

    def Function_4_75D(): pass

    label("Function_4_75D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_795")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_791")
    Call(0, 22)
    Return()

    label("loc_791")

    Call(0, 23)
    Return()

    label("loc_795")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E0")

    #C0001
    ChrTalk(
        0xFE,
        (
            "荷物が間違って届いちまった場所を\x01",
            "順番に巡って、荷物を正しいものと\x01",
            "交換していってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "まずはマインツ、次にウルスラ病院、\x01",
            "最後に住宅街の民家に行くといいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "住宅街の民家の住所は\x01",
            "伝票に書いてるから、最後に行くときに\x01",
            "改めてチェックしてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "面倒で悪いが、よろしく頼んだぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_955")

    label("loc_8E0")


    #C0005
    ChrTalk(
        0xFE,
        (
            "まずはマインツ、次にウルスラ病院、\x01",
            "最後に住宅街の民家に行くといいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "面倒で悪いが、よろしく頼んだぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_955")

    Jump("loc_A28")

    label("loc_95A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E0")

    #C0007
    ChrTalk(
        0xFE,
        "お疲れさん、おかげで助かったぜ。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "さ～て、無事に済んだのをお頭……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "じゃなくて、社長に報告しないとな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_A28")

    label("loc_9E0")


    #C0010
    ChrTalk(
        0xFE,
        "お疲れさん、おかげで助かったぜ。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "また何かあったらよろしくな。\x02",
    )

    CloseMessageWindow()

    label("loc_A28")

    TalkEnd(0xFE)
    Return()

    # Function_4_75D end

    def Function_5_A2C(): pass

    label("Function_5_A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 6)), scpexpr(EXPR_END)), "loc_A6B")
    Call(0, 28)
    Jump("loc_A6E")

    label("loc_A6B")

    Call(0, 27)

    label("loc_A6E")

    Return()

    label("loc_A6F")

    TalkBegin(0x12)

    #C0012
    ChrTalk(
        0xFE,
        (
            "クロスベルがこんな時に\x01",
            "医療物資を騙し取るなんて……\x01",
            "絶対に許せないぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "あんたたち、\x01",
            "何とか犯人を捕まえてくれ！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_5_A2C end

    def Function_6_AEF(): pass

    label("Function_6_AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 6)), scpexpr(EXPR_END)), "loc_B2E")
    Call(0, 28)
    Jump("loc_B31")

    label("loc_B2E")

    Call(0, 27)

    label("loc_B31")

    Return()

    label("loc_B32")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_BBC")

    #C0014
    ChrTalk(
        0xA,
        (
            "さっきここに警官たちが来てな。\x01",
            "発着場で猟兵の痕跡とかを調べてるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xA,
        "悪いが、この先には入らないでくれよな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_107B")

    label("loc_BBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_BCA")
    Jump("loc_107B")

    label("loc_BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BD8")
    Jump("loc_107B")

    label("loc_BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F52")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD6")

    #C0016
    ChrTalk(
        0xFE,
        (
            "あんたたち、医療物資を\x01",
            "よく取り戻してくれたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "さっきウルスラ病院から\x01",
            "荷物が届いたって連絡がきてな、\x01",
            "俺もようやく安心できたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "今後はこんな事がないよう、\x01",
            "もっと気をつけてチェック\x01",
            "していかないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_D78")

    label("loc_CD6")


    #C0019
    ChrTalk(
        0xFE,
        (
            "さっきウルスラ病院から\x01",
            "荷物が届いたって連絡がきてな、\x01",
            "俺もようやく安心できたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "今後はこんな事がないよう、\x01",
            "もっと気をつけてチェック\x01",
            "していかないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D78")

    Jump("loc_F4D")

    label("loc_D7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_ED3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E5A")

    #C0021
    ChrTalk(
        0xFE,
        (
            "……結局、医療物資は\x01",
            "持ち逃げされちまったんだってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "いや、あんたたちのせいじゃないさ。\x01",
            "うっかり騙された俺が全部悪いんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "今後はもっと気をつけて\x01",
            "チェックしていかねえとな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_ECE")

    label("loc_E5A")


    #C0024
    ChrTalk(
        0xFE,
        (
            "……結局、医療物資は\x01",
            "持ち逃げされちまったんだってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "今後はもっと気をつけて\x01",
            "チェックしていかねえとな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ECE")

    Jump("loc_F4D")

    label("loc_ED3")


    #C0026
    ChrTalk(
        0xFE,
        (
            "まさか偽造の書類に騙されるとは……\x01",
            "ちくしょう、俺の責任だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "ウルスラ病院のほうにも\x01",
            "あとで連絡しておかないと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F4D")

    Jump("loc_107B")

    label("loc_F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_107B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1009")

    #C0028
    ChrTalk(
        0xFE,
        (
            "カプア特急便のヤツらも、\x01",
            "空港では馴染み深くなったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "個人経営の運送会社としては、\x01",
            "かなりの業績を上げてるそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        "いや、景気がいい話だねぇ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_107B")

    label("loc_1009")


    #C0031
    ChrTalk(
        0xFE,
        (
            "カプア特急便は、\x01",
            "個人経営の運送会社としては、\x01",
            "かなりの業績を上げてるそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "いや、景気がいい話だねぇ。\x02",
    )

    CloseMessageWindow()

    label("loc_107B")

    TalkEnd(0xFE)
    Return()

    # Function_6_AEF end

    def Function_7_107F(): pass

    label("Function_7_107F")

    Call(0, 8)
    Return()

    # Function_7_107F end

    def Function_8_1083(): pass

    label("Function_8_1083")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_11FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1174")

    #C0033
    ChrTalk(
        0x8,
        (
            "猟兵や街を徘徊していた化物が去って、\x01",
            "ひとまず職場に戻ってみたのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "航空便は一切運行できない状態ですし、\x01",
            "これからどうしたらいいか……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "私たちが日常を取り戻すことなんて\x01",
            "できるのでしょうか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11F8")

    label("loc_1174")


    #C0036
    ChrTalk(
        0x8,
        (
            "航空便は一切運行できない状態ですし、\x01",
            "これからどうしたらいいか……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "私たちが日常を取り戻すことなんて\x01",
            "できるのでしょうか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F8")

    Jump("loc_1582")

    label("loc_11FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_13AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1309")

    #C0038
    ChrTalk(
        0x8,
        (
            "リベールやレミフェリアには、\x01",
            "今回のクロスベル市の復旧に\x01",
            "大きく支援いただいています。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "義援金や物資も集まり、\x01",
            "復興作業も比較的早い段階で\x01",
            "落ち着きを見せたそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "クロスベルのいち住民として、\x01",
            "是非ともお礼申し上げたいものです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13A8")

    label("loc_1309")


    #C0041
    ChrTalk(
        0x8,
        (
            "リベールやレミフェリアには、\x01",
            "今回のクロスベル市の復旧に\x01",
            "大きく支援いただいています。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "クロスベルのいち住民として、\x01",
            "是非ともお礼申し上げたいものです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13A8")

    Jump("loc_1582")

    label("loc_13AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1582")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CE")

    #C0043
    ChrTalk(
        0x8,
        (
            "独立提唱がされてから、\x01",
            "クロスベルの情勢に不安を感じる\x01",
            "お客様もいらっしゃるようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "実際、予定されていたご旅行を\x01",
            "キャンセルされる方も\x01",
            "少数ながら見受けられます。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "無理からぬことかもしれませんが、\x01",
            "クロスベルの住民からすると\x01",
            "少し寂しくもありますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1582")

    label("loc_14CE")


    #C0046
    ChrTalk(
        0x8,
        (
            "独立提唱がされてから、\x01",
            "クロスベルの情勢に不安を感じる\x01",
            "お客様もいらっしゃるようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "無理からぬことかもしれませんが、\x01",
            "クロスベルの住民からすると\x01",
            "少し寂しくもありますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1582")

    TalkEnd(0x8)
    Return()

    # Function_8_1083 end

    def Function_9_1586(): pass

    label("Function_9_1586")

    Call(0, 10)
    Return()

    # Function_9_1586 end

    def Function_10_158A(): pass

    label("Function_10_158A")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_170C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B8")

    #C0048
    ChrTalk(
        0x9,
        (
            "独立宣言が成されてから、\x01",
            "この空港は２大国の侵攻への\x01",
            "迎撃拠点になっていました。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "以前、街を襲撃した猟兵たちが\x01",
            "大統領の私設部隊として\x01",
            "詰めていたそうなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        (
            "……なんと言っていいやら。\x01",
            "大統領の言葉を信じ、独立に賛成した\x01",
            "私たちの心はなんだったんでしょうか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1707")

    label("loc_16B8")


    #C0051
    ChrTalk(
        0x9,
        (
            "大統領の言葉を信じ、独立に賛成した\x01",
            "私たちの心はなんだったんでしょうか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1707")

    Jump("loc_1A80")

    label("loc_170C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_18D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1827")

    #C0052
    ChrTalk(
        0x9,
        (
            "あのクロスベル襲撃事件は、\x01",
            "帝国の陰謀だとまことしやかに\x01",
            "囁かれているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        (
            "確証はありませんが……\x01",
            "火のないところに煙は立たない、\x01",
            "とも言いますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "今までの帝国のやり方を見れば、\x01",
            "真実である可能性は高い……\x01",
            "そう思わざるを得ないのです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18CB")

    label("loc_1827")


    #C0055
    ChrTalk(
        0x9,
        (
            "あのクロスベル襲撃事件は、\x01",
            "帝国の陰謀だとまことしやかに\x01",
            "囁かれているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "確証はありませんが、\x01",
            "真実である可能性は高い……\x01",
            "そう思わざるを得ません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18CB")

    Jump("loc_1A80")

    label("loc_18D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1A80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D5")

    #C0057
    ChrTalk(
        0x9,
        (
            "こちらは出入国届けの受付、\x01",
            "及び手荷物をお預りしています。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x9,
        (
            "外国への荷物の配送でしたら、\x01",
            "丁度来ている『カプア特急便』の方々に\x01",
            "ご依頼してみてはいかがでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "通常の空輸よりも速く荷物が届くと\x01",
            "なかなか好評のようですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A80")

    label("loc_19D5")


    #C0060
    ChrTalk(
        0x9,
        (
            "外国への荷物の配送でしたら、\x01",
            "丁度来ている『カプア特急便』の方々に\x01",
            "ご依頼してみてはいかがでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "通常の空輸よりも速く荷物が届くと\x01",
            "なかなか好評のようですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A80")

    TalkEnd(0x9)
    Return()

    # Function_10_158A end

    def Function_11_1A84(): pass

    label("Function_11_1A84")

    TalkBegin(0xFE)

    #C0062
    ChrTalk(
        0xFE,
        (
            "おお～、ほらほら！\x01",
            "飛行船が飛び立つのが見えるよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "ハニー、君も覗いてごらんよ！\x01",
            "興奮する事間違いなしだから！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1A84 end

    def Function_12_1B01(): pass

    label("Function_12_1B01")

    TalkBegin(0xFE)

    #C0064
    ChrTalk(
        0xFE,
        (
            "はあ、男の子って\x01",
            "いくつになっても子供よねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "でも、あんな大きなものが\x01",
            "空を飛ぶなんてすごい技術よね。\x01",
            "その点は素直に感心しちゃうわ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1B01 end

    def Function_13_1B97(): pass

    label("Function_13_1B97")

    TalkBegin(0xFE)

    #C0066
    ChrTalk(
        0xFE,
        (
            "おや、あの緑色の飛行艇は\x01",
            "客船とはちがうようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "見たところラインフォルト社製の\x01",
            "旧式の高速艇のようだが……\x01",
            "どこぞの貴族の持ち物なのかな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1B97 end

    def Function_14_1C33(): pass

    label("Function_14_1C33")

    TalkBegin(0xFE)

    #C0068
    ChrTalk(
        0xFE,
        (
            "街の復旧も一通り終わったし、\x01",
            "しばらく家族みんなで\x01",
            "外国に行ってようと思うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "ウチの実家がある\x01",
            "レミフェリアあたりなら\x01",
            "きっと安全だろうしな、うん。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1C33 end

    def Function_15_1CD8(): pass

    label("Function_15_1CD8")

    TalkBegin(0xFE)

    #C0070
    ChrTalk(
        0xFE,
        (
            "はあ、突然里帰りする事になって\x01",
            "驚いたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "旦那の言う事も一理あるわよね。\x01",
            "最近何だか物騒だし……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_1CD8 end

    def Function_16_1D4D(): pass

    label("Function_16_1D4D")

    TalkBegin(0xFE)

    #C0072
    ChrTalk(
        0xFE,
        (
            "今から飛行船に乗るんだ～。\x01",
            "えへへ、楽しみだな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "空の上からいっぱい写真を\x01",
            "撮らなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_1D4D end

    def Function_17_1DBA(): pass

    label("Function_17_1DBA")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1E30")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル独立国へようこそ！\x01",
            "ご滞在・ご宿泊は\x01",
            "《ホテル・ミレニアム》へ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E80")

    label("loc_1E30")


    #A0075
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル自治州へようこそ！\x01",
            "ご滞在・ご宿泊は\x01",
            "《ホテル・ミレニアム》へ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E80")

    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_1DBA end

    def Function_18_1E99(): pass

    label("Function_18_1E99")

    EventBegin(0x1)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1F26")

    #C0076
    ChrTalk(
        0xA,
        (
            "さっきここに警官たちが来てな。\x01",
            "発着場で猟兵の痕跡とかを調べてるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xA,
        "悪いが、この先には入らないでくれよな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F91")

    label("loc_1F26")

    TurnDirection(0xA, 0x0, 500)

    #C0078
    ChrTalk(
        0xA,
        (
            "おっと……\x01",
            "そっちは搭乗口の方だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "チケットを持ってないと\x01",
            "入れないから注意してくれよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F91")

    Sleep(50)
    SetChrPos(0x0, 960, 0, 5140, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FD2")
    TurnDirection(0xA, 0x12, 0)
    Jump("loc_1FD9")

    label("loc_1FD2")

    OP_93(0xA, 0xB4, 0x0)

    label("loc_1FD9")

    OP_4C(0xA, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_18_1E99 end

    def Function_19_1FE0(): pass

    label("Function_19_1FE0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06000.itc", 0x1E)
    LoadChrToIndex("apl/ch50314.itc", 0x1F)
    LoadChrToIndex("chr/ch47900.itc", 0x20)
    LoadChrToIndex("chr/ch27400.itc", 0x21)
    LoadChrToIndex("chr/ch27800.itc", 0x22)
    LoadChrToIndex("chr/ch27900.itc", 0x23)
    LoadChrToIndex("chr/ch27600.itc", 0x24)
    LoadEffect(0x0, "event/eva02_00.eff")
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x20)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x21)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x22)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x23)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetMapObjFlags(0x5, 0x1000)
    ClearMapObjFlags(0x5, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x17, -1450, 5000, 13350, 0)
    SetChrPos(0x18, -900, 5000, 13950, 0)
    SetChrPos(0x19, 3000, 5000, 13450, 0)
    SetChrPos(0x1A, 1150, 5000, 13950, 0)
    SetChrPos(0x1B, -3150, 5000, 13350, 45)
    SetChrPos(0x1C, 1550, 5000, 12500, 0)
    SetChrPos(0x1D, 4700, 5000, 13000, 0)
    BeginChrThread(0x18, 3, 0, 20)
    OP_68(1000, 8000, 13250, 0)
    MoveCamera(315, 15, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(37800, 0)
    OP_68(1000, 6000, 13250, 5000)
    SetCameraDistance(35800, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 5)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_1FE0 end

    def Function_20_21C6(): pass

    label("Function_20_21C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_227E")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_21F4")
    Sleep(500)
    Jump("loc_223C")

    label("loc_21F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_220B")
    Sleep(1000)
    Jump("loc_223C")

    label("loc_220B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2222")
    Sleep(1500)
    Jump("loc_223C")

    label("loc_2222")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2239")
    Sleep(2000)
    Jump("loc_223C")

    label("loc_2239")

    Sleep(2500)

    label("loc_223C")

    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 80, 0)
    Jump("Function_20_21C6")

    label("loc_227E")

    Return()

    # Function_20_21C6 end

    def Function_21_227F(): pass

    label("Function_21_227F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11200.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("apl/ch51212.itc", 0x24)
    LoadChrToIndex("chr/ch30000.itc", 0x25)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07100.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x2)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrPos(0x101, 3000, 5000, 11400, 0)
    SetChrPos(0x102, 2700, 5100, 13000, 90)
    SetChrPos(0x104, 4500, 5000, 10600, 0)
    SetChrPos(0x109, 4800, 5100, 12300, 270)
    SetChrPos(0x105, 3300, 5000, 10100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -8300, 5000, 6700, 90)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0x15, 0x25)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -4300, 0, -6800, 45)
    BeginChrThread(0x15, 0, 0, 0)
    SetChrChipByIndex(0x16, 0x25)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -3700, 0, 6600, 180)
    BeginChrThread(0x16, 0, 0, 0)
    ClearChrFlags(0x14, 0x80)
    OP_78(0x5, 0x14)
    OP_49()
    SetChrPos(0x14, -7700, 0, 29900, 270)
    OP_D5(0x14, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    ClearMapObjFlags(0x5, 0x4)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    OP_11(0xE4, 0xA9, 0x9D, 0x32, 0xBE, 0x0)
    OP_68(0, 2000, 0, 0)
    MoveCamera(330, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(30000, 0)
    OP_68(0, 7500, 0, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(4300, 6500, 12000, 0)
    MoveCamera(330, 20, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22000, 0)
    SetCameraDistance(20500, 2000)
    OP_6F(0x79)

    #C0080
    ChrTalk(
        0x109,
        (
            "#6P#10102Fリベール王国の高速巡洋艦、\x01",
            "《アルセイユ号》……\x02\x03",

            "#10109Fはあ……\x01",
            "やっぱり凄い船ですよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        (
            "#00104F#6PＺＣＦの名前を轟かせた\x01",
            "世界最高速の飛行船ね……\x02\x03",

            "#00100Fいまだに自己記録を更新し続けて\x01",
            "他を寄せ付けていないそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x104,
        (
            "#6P#00309Fそんで、リベールの王女様が\x01",
            "乗ってきた旗艦ってわけだ。\x02\x03",

            "#00302Fクローディア姫だったか？\x01",
            "やんごとなき方って感じだよな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0083
    ChrTalk(
        0x101,
        (
            "#00004F#5P正確には『王女』じゃなくて\x01",
            "『王太女』だけどね。\x02\x03",

            "#00000Fつまりはリベール王国の\x01",
            "次期女王陛下ってわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x104,
        (
            "#6P#00305Fは～、なるほどね。\x02\x03",

            "#00301F……まさか呼び出したのが\x01",
            "本人ってワケはないよな？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    #C0085
    ChrTalk(
        0x102,
        (
            "#5P#00106Fう、うーん。\x01",
            "さすがに分からないわね。\x02\x03",

            "#00108Fベルに聞いてみれば\x01",
            "殿下のスケジュールくらいは\x01",
            "分かると思うけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x105, 0x13, 500)

    def lambda_27D0():

        label("loc_27D0")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_27D0")

    QueueWorkItem2(0x105, 2, lambda_27D0)

    #C0086
    ChrTalk(
        0x105,
        (
            "#11P#10302Fフフ……\x01",
            "その必要はないみたいだよ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0087
    ChrTalk(
        0x101,
        "#5P#00005Fえ。\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    ClearChrFlags(0x13, 0x80)

    #N0088
    NpcTalk(
        0x13,
        "凛とした声",
        (
            "──お待たせした。\x01",
            "特務支援課の諸君だな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_28C1():

        label("loc_28C1")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_28C1")

    QueueWorkItem2(0x101, 2, lambda_28C1)
    Sleep(50)

    def lambda_28D6():

        label("loc_28D6")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_28D6")

    QueueWorkItem2(0x104, 2, lambda_28D6)
    Sleep(100)
    SetChrSubChip(0x109, 0x1)
    Sleep(300)
    Fade(500)
    OP_68(-7500, 6100, 7000, 0)
    MoveCamera(336, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)
    OP_68(1800, 6100, 11300, 5500)
    MoveCamera(321, 19, 0, 5500)

    def lambda_2941():
        OP_95(0xFE, -4300, 5000, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2941)
    WaitChrThread(0x13, 1)

    def lambda_295F():
        OP_95(0xFE, 1000, 5000, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_295F)
    WaitChrThread(0x13, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x105, 0x2)
    OP_6F(0x79)

    #C0089
    ChrTalk(
        0x101,
        "#00011Fあ──\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x109,
        "#12P#10101F！！\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        "#00102Fや、やっぱり……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x104,
        (
            "#12P#00305Fおお、さっき\x01",
            "お嬢さん方が騒いでた……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x13,
        (
            "#07105F#5P……？\x02\x03",

            "#07104Fああ、これは失礼。\x01",
            "除幕式でご一緒だったかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(20000, 300)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0094
    AnonymousTalk(
        0x13,
        (
            "──申し遅れた。\x01",
            "リベール王国軍、王室親衛隊、\x01",
            "ユリア・シュバルツ准佐だ。\x02\x03",

            "クローディア殿下の命により\x01",
            "これより諸君を《アルセイユ》へ\x01",
            "案内させていただく。\x02\x03",

            "どうぞ、付いて来てくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetCameraDistance(20500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(500)
    SetScenarioFlags(0x22, 1)
    NewScene("t3520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_227F end

    def Function_22_2BF8(): pass

    label("Function_22_2BF8")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(6860, 1250, -5300, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(36000, 0)
    SetChrPos(0x101, 6000, 0, -4790, 0)
    SetChrPos(0x102, 7200, 0, -4850, 0)
    SetChrPos(0x103, 5430, 0, -5620, 0)
    SetChrPos(0x104, 6910, 0, -5920, 0)
    SetChrPos(0x109, 7600, 0, -6670, 0)
    SetChrPos(0x105, 6280, 0, -6960, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x11, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0095
    ChrTalk(
        0x101,
        (
            "#00000Fすみません、あなたが\x01",
            "カプア特急便の方ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x11,
        (
            "ああ、そうだけど……\x01",
            "あんたらは？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#00000Fクロスベル警察、\x01",
            "特務支援課の者です。\x02\x03",

            "依頼を確認して\x01",
            "伺わせていただきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x11,
        "おお、あんたらが！\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x11,
        (
            "いやあ、ありがてぇ。\x01",
            "すっかり困ってたトコでさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x11,
        (
            "ちっと手間な仕事なんだが、\x01",
            "引き受けてくれるかい？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 24)
    OP_4C(0x11, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6600, 0, -5000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_22_2BF8 end

    def Function_23_2E2E(): pass

    label("Function_23_2E2E")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(6860, 1250, -5300, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(36000, 0)
    SetChrPos(0x101, 6000, 0, -4790, 0)
    SetChrPos(0x102, 7200, 0, -4850, 0)
    SetChrPos(0x103, 5430, 0, -5620, 0)
    SetChrPos(0x104, 6910, 0, -5920, 0)
    SetChrPos(0x109, 7600, 0, -6670, 0)
    SetChrPos(0x105, 6280, 0, -6960, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x11, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0101
    ChrTalk(
        0x11,
        (
            "おっ、もしかして\x01",
            "手が空いたのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x11,
        (
            "ちっと手間な仕事なんだが、\x01",
            "引き受けてくれるかい？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 24)
    OP_4C(0x11, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6600, 0, -5000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_23_2E2E end

    def Function_24_2F82(): pass

    label("Function_24_2F82")

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
            "【引き受ける】\x01",      # 0
            "【やめる】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2FEC"),
        (1, "loc_2FF4"),
        (SWITCH_DEFAULT, "loc_309F"),
    )


    label("loc_2FEC")

    Call(0, 25)
    Jump("loc_309F")

    label("loc_2FF4")


    #C0103
    ChrTalk(
        0x101,
        (
            "#00006Fすみません、今はちょっと\x01",
            "手が空いてなくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x11,
        (
            "ありゃ、そうなのか？\x01",
            "まいったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x11,
        (
            "そんじゃ、手が空いたら\x01",
            "また話しかけてくれよな！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x175, 4)
    Jump("loc_309F")

    label("loc_309F")

    Return()

    # Function_24_2F82 end

    def Function_25_30A0(): pass

    label("Function_25_30A0")


    #C0106
    ChrTalk(
        0x101,
        "#00000Fええ、お任せください。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x104,
        (
            "#00300F依頼は確か、誤配荷物が\x01",
            "どうとかいう話だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x11,
        "ああ、そうなんだ。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x11,
        (
            "俺たち、大陸を飛び回って\x01",
            "色んな場所に荷物を\x01",
            "届けてるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x11,
        (
            "今回、ここに届けた荷物に\x01",
            "手違いがあってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x11,
        (
            "届け先があべこべになってて、\x01",
            "いくつかの荷物が間違った場所に\x01",
            "届いてしまったらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        "#00105Fまぁ……それは大変ですね。\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        (
            "#00206F伝票を間違えるなんてこと\x01",
            "そうそうないと思うんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x11,
        (
            "いやー、ウチの社長が\x01",
            "おっちょこちょいなお人でさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x11,
        (
            "今までも何度か\x01",
            "こういうことがあったんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x11,
        (
            "ひどいときは、伝票の代わりに\x01",
            "知り合いからの手紙を\x01",
            "貼っつけちまったりとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x109,
        (
            "#10109Fあはは……\x01",
            "うっかりしたお方\x01",
            "みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x11,
        (
            "ま、尊敬できるお人だけどな。\x01",
            "行き場のなかった俺たちを\x01",
            "拾ってくれて……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x11,
        (
            "……コホン、すまねえ。\x01",
            "話が逸れちまったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x11,
        (
            "要するに、間違って届けられた\x01",
            "荷物の再配達を頼みたいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x11,
        (
            "自治州に届けた後は、いつも\x01",
            "地元の運送会社に任せてるから\x01",
            "ちっと土地勘がなくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x105,
        (
            "#10304Fなるほど、\x01",
            "事情は分かったよ。\x02\x03",

            "#10302F誤配された荷物の所在は\x01",
            "把握できてるのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x11,
        (
            "ええと、確認したところに\x01",
            "よるとだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x11,
        (
            "マインツの《赤レンガ亭》に\x01",
            "ウルスラ病院宛ての荷物。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x11,
        (
            "で、ウルスラ病院には\x01",
            "市内の住宅街にある民家宛ての\x01",
            "荷物が届いたらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x11,
        (
            "あんたらにはその住所を回って、\x01",
            "誤配した荷物を回収しつつ\x01",
            "本来の荷物を届けて欲しいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x11,
        (
            "……ってことで、\x01",
            "こいつを受け取ってくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0128
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x331),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x331, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0129
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x332),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x332, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0130
    ChrTalk(
        0x101,
        (
            "#00000Fこれが《赤レンガ亭》に\x01",
            "本来届くはずだった\x01",
            "荷物というわけですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x103,
        (
            "#00200Fこっちの伝票は、病院に届いた荷物に\x01",
            "本来貼られているはずのものですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x11,
        "ああ、そういうこと。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x11,
        (
            "まずはその小包を\x01",
            "《赤レンガ亭》とやらに\x01",
            "届けてやってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x11,
        (
            "そこにはウルスラ病院宛ての\x01",
            "荷物が届いてるはずだから\x01",
            "それを受け取って、えーっと……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x11,
        (
            "……なんだか自分で言ってて\x01",
            "分からなくなってきたなあ。\x02",
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
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0136
    ChrTalk(
        0x101,
        (
            "#00003Fと、とにかく……\x01",
            "そうやって順番に荷物を\x01",
            "交換していけばいいんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x11,
        "うん、まあそういうことだな。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x11,
        (
            "面倒で悪いが、\x01",
            "よろしくたのんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#00004Fええ、了解しました。\x02\x03",

            "#00000F……それじゃ、さっそく\x01",
            "マインツの《赤レンガ亭》に\x01",
            "行ってみるとするか。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x104,
        (
            "#00306Fやれやれ、なかなか\x01",
            "骨が折れそうだぜ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0141
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【誤配荷物の再配達】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x175, 5)
    OP_29(0x85, 0x1, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x11, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6600, 0, -5000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_25_30A0 end

    def Function_26_3A93(): pass

    label("Function_26_3A93")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(6860, 2500, -5300, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(36000, 0)
    SetChrPos(0x101, 6000, 0, -4790, 0)
    SetChrPos(0x102, 7200, 0, -4850, 0)
    SetChrPos(0x103, 5430, 0, -5620, 0)
    SetChrPos(0x104, 6910, 0, -5920, 0)
    SetChrPos(0x109, 7600, 0, -6670, 0)
    SetChrPos(0x105, 6280, 0, -6960, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x11, 0xFF)
    OP_68(6860, 1250, -5300, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0142
    ChrTalk(
        0x11,
        (
            "おう、きちんと正しい届け先に\x01",
            "荷物を届けてくれたみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x11,
        (
            "いやー、助かったぜ。\x01",
            "本当にありがとな、支援課サンよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        "#00000Fどういたしまして。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x11,
        "ところで……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    #C0146
    ChrTalk(
        0x11,
        (
            "その姉ちゃん、\x01",
            "なんだか顔色悪くないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x102,
        (
            "#00106F#1Sぶつぶつ……\x01",
            "おばけと話しちゃうなんて……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0148
    ChrTalk(
        0x105,
        "#10309Fフフ、よほどショックだったみたいだね。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x109,
        "#10106F気持ちは分かります……\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x104,
        "#00300Fまあ、そのうち収まるだろ。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#00012Fえ、えーっと……\x01",
            "そういうことなので、\x01",
            "気にしないでください。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0xB4, 0x1F4)
    Sleep(300)

    #C0152
    ChrTalk(
        0x11,
        (
            "そうか？\x01",
            "まあいいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x11,
        (
            "それじゃ、俺はここらで\x01",
            "失礼するぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x11,
        (
            "また何かあったら\x01",
            "よろしく頼むな。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#00000Fええ、いつでもどうぞ。\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x103,
        "#00200Fお待ちしてます。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3EDF")
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0157
    ChrTalk(
        0x101,
        (
            "#00000F……よし、それじゃあ\x01",
            "西クロスベル街道の\x01",
            "脱線現場に急ぐとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EDF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0158
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【誤配荷物の再配達】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x85, 0x1, 0x5)
    OP_29(0x85, 0x1, 0x6)
    OP_29(0x85, 0x4, 0x10)
    SubItemNumber(0x332, 1)
    OP_4C(0x11, 0xFF)
    ClearMapFlags(0x10000000)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3F87")
    EventEnd(0x5)
    NewScene("c0000", 103, 0, 0)
    IdleLoop()
    Jump("loc_3F9E")

    label("loc_3F87")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6600, 0, -5000, 0)
    EventEnd(0x5)

    label("loc_3F9E")

    Return()

    # Function_26_3A93 end

    def Function_27_3F9F(): pass

    label("Function_27_3F9F")

    EventBegin(0x0)
    Fade(500)
    OP_68(5810, 1250, 4500, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32500, 0)
    SetChrPos(0x101, 5480, 0, 4000, 0)
    SetChrPos(0x102, 6680, 0, 4000, 0)
    SetChrPos(0x104, 5480, 0, 2800, 0)
    SetChrPos(0x103, 6580, 0, 2800, 0)
    SetChrPos(0x105, 5480, 0, 1600, 0)
    SetChrPos(0x109, 6680, 0, 1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x12, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_0D()

    #C0159
    ChrTalk(
        0x12,
        "はあ、一体どうすればいいんだ……\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xA,
        (
            "俺がもっとしっかりしておけば\x01",
            "こんなことには……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        (
            "#00005Fあの……\x01",
            "どうかなさったんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_410C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_410C)
    Sleep(10)

    def lambda_411C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_411C)
    WaitChrThread(0xA, 2)
    Sleep(500)

    #C0162
    ChrTalk(
        0x12,
        (
            "おお、あんたたちは特務支援課の……\x01",
            "実は困ったことになっちまってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x12,
        (
            "今日は、ウルスラ病院に\x01",
            "レミフェリアからの医療物資を\x01",
            "届ける予定だったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x12,
        (
            "どうやら、どこのどいつかが\x01",
            "そいつを騙し取っちまったらしいんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0165
    ChrTalk(
        0x102,
        "#00105F医療物資を騙し取った……！？\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xA,
        (
            "ああ……ついさっき、\x01",
            "運送会社の人間だって男が\x01",
            "ここを訪れたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xA,
        (
            "『ライムス運送が来られなくなったから、\x01",
            "  代理で物資の輸送を引き受けた』って、\x01",
            "もっともらしい理由を言ってきてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xA,
        (
            "とても嘘をつくような人には\x01",
            "見えなかったし、つい二つ返事で\x01",
            "荷物を渡しちゃったんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x12,
        (
            "だけどウチも、そんな委任状なんかを\x01",
            "よそに出した覚えがなくってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x12,
        (
            "それで色々と話しているうちに、\x01",
            "荷物を騙し取られた事に気づいたわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x103,
        (
            "#00203Fふむ……要するに、\x01",
            "その委任状が偽物だったわけですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x105,
        (
            "#10301Fしかし、この非常時に\x01",
            "医療物資を騙し取るなんて\x01",
            "相当タチが悪いね。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x109,
        (
            "#10108Fあの襲撃事件の被害者も\x01",
            "沢山入院してるっていうのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x104,
        (
            "#00303Fそういう医療物資なんかは、\x01",
            "裏で捌けば、それなりのミラに\x01",
            "なるだろうからな。\x02\x03",

            "#00301Fミラ目当ての狡猾な\x01",
            "火事場泥棒ってトコだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x102,
        "#00101Fひ、ひどい……\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x12,
        "しかし、困ったな……\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x12,
        (
            "ウルスラ病院では今も\x01",
            "物資の到着を待っているって\x01",
            "言うのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xA,
        (
            "ああ、全て俺の責任だ……\x01",
            "せめてライムス運送さんに\x01",
            "確認をとっておけば……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0xA, 500)

    #C0179
    ChrTalk(
        0x12,
        (
            "いや……あんたは悪くないさ。\x01",
            "悪いのはどう考えても\x01",
            "荷物を騙し取った奴だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x12, 0x101, 500)

    #C0180
    ChrTalk(
        0x12,
        (
            "そうだ……あんたたち、\x01",
            "医療物資を騙し取った犯人を\x01",
            "あんたたちで探せないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x12,
        (
            "ウルスラ病院に入院している\x01",
            "患者さんたちのためにも、\x01",
            "なんとか捕まえて欲しいんだ。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 29)
    OP_4C(0x12, 0xFF)
    OP_4C(0xA, 0xFF)
    TurnDirection(0x12, 0xA, 0)
    TurnDirection(0xA, 0x12, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6080, 0, 4000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_3F9F end

    def Function_28_47F6(): pass

    label("Function_28_47F6")

    EventBegin(0x0)
    Fade(500)
    OP_68(5810, 1250, 4500, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32500, 0)
    SetChrPos(0x101, 5480, 0, 4000, 0)
    SetChrPos(0x102, 6680, 0, 4000, 0)
    SetChrPos(0x104, 5480, 0, 2800, 0)
    SetChrPos(0x103, 6580, 0, 2800, 0)
    SetChrPos(0x105, 5480, 0, 1600, 0)
    SetChrPos(0x109, 6680, 0, 1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x12, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_93(0x12, 0xB4, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    OP_0D()

    #C0182
    ChrTalk(
        0x12,
        (
            "医療物資を騙し取った犯人……\x01",
            "あんたたちで探せないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x12,
        (
            "ウルスラ病院に入院している\x01",
            "患者さんたちのためにも、\x01",
            "なんとか捕まえて欲しいんだ。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 29)
    OP_4C(0x12, 0xFF)
    OP_4C(0xA, 0xFF)
    TurnDirection(0x12, 0xA, 0)
    TurnDirection(0xA, 0x12, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6080, 0, 4000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_47F6 end

    def Function_29_4992(): pass

    label("Function_29_4992")

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
            "引き受ける\x01",      # 0
            "やめる\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_49F4"),
        (1, "loc_49FC"),
        (SWITCH_DEFAULT, "loc_4ACD"),
    )


    label("loc_49F4")

    Call(0, 30)
    Jump("loc_4ACD")

    label("loc_49FC")


    #C0184
    ChrTalk(
        0x101,
        (
            "#00003Fすみません……\x01",
            "今は外せない用事がありまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xA,
        (
            "そ、そうか……\x01",
            "だったら仕方ないな……\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x12,
        (
            "もし、時間が空いたら\x01",
            "また声をかけてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x12,
        (
            "あんたたちだけが頼りだ。\x01",
            "どうかよろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19B, 6)
    Jump("loc_4ACD")

    label("loc_4ACD")

    Return()

    # Function_29_4992 end

    def Function_30_4ACE(): pass

    label("Function_30_4ACE")


    #C0188
    ChrTalk(
        0x101,
        (
            "#00003F……まだ事件発生から時間も\x01",
            "経ってないみたいですし……\x01",
            "急げば間に合うかもしれません。\x02\x03",

            "#00000F一旦俺たちに任せてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xA,
        "おお……恩に着るぜ！\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x102,
        (
            "#00103Fでも、相手はもう仕事を\x01",
            "済ませてしまったみたいだし……\x01",
            "本当に急いだ方がよさそうですね。\x02\x03",

            "#00101F何か、犯人の行き先を示すような\x01",
            "手がかりがありませんでしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x12,
        (
            "そうだな……\x01",
            "こっちは見てないから\x01",
            "なんとも言えないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xA,
        (
            "そういえば……\x01",
            "あの男はラインフォルト社製の\x01",
            "黒い運搬車に乗ってたみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xA,
        (
            "見た感じも身なりのいい帝国人って\x01",
            "感じだったし、もしかすると……\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x104,
        (
            "#00301Fそのまま帝国方面に\x01",
            "高飛びしようとしてる可能性は\x01",
            "高いかも知れねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x109,
        (
            "#10103Fもしかすると、\x01",
            "今頃ベルガード門あたりに\x01",
            "着いている頃かもしれませんね。\x02\x03",

            "#10101F念の為、運搬車の通り道を\x01",
            "聞き込みして追っていった方が\x01",
            "いいとは思いますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x105,
        (
            "#10306Fまあ、悠長にも\x01",
            "してられなさそうだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#00003Fとにかく……\x01",
            "なんとか追いかけてみよう。\x02\x03",

            "#00001Fビリーさんたちはここで\x01",
            "連絡を待っていてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x12,
        "ああ、分かった。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xA,
        "よろしく頼むぜ、あんたたち！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0200
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【医療物資の捜索】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x93, 0x4, 0x2)
    OP_29(0x93, 0x1, 0x0)
    Return()

    # Function_30_4ACE end

    SaveToFile()

Try(main)
