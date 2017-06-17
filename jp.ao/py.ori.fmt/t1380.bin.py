from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1380.bin",                # FileName
        "t1380",                    # MapName
        "t1380",                    # Location
        0x00BA,                     # MapIndex
        "ed7304",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 186, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1380",                  # 0
        "エリィ",                 # 1
        "ティオ",                 # 2
        "ノエル",                 # 3
        "ワジ",                   # 4
        "フラン",                 # 5
        "リーシャ",               # 6
        "みっしぃ",               # 7
        "見習い",                 # 8
        "観光客",                 # 9
        "観光客",                 # 10
        "観光客",                 # 11
        "観光客",                 # 12
        "観光客",                 # 13
        "ダミー",                 # 14
        "占い師",                 # 15
        "ツァイト",               # 16
        "みーしぇ",               # 17
    ))

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch00200.itc",                   # 01
        "chr/ch02900.itc",                   # 02
        "chr/ch03000.itc",                   # 03
        "chr/ch08500.itc",                   # 04
        "chr/ch05200.itc",                   # 05
        "chr/ch10200.itc",                   # 06
        "chr/ch20500.itc",                   # 07
        "chr/ch22802.itc",                   # 08
        "chr/ch22102.itc",                   # 09
        "chr/ch21102.itc",                   # 0A
        "chr/ch24502.itc",                   # 0B
        "chr/ch34302.itc",                   # 0C
        "chr/ch45400.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(-959,    0,       -3099,   0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-1549,   0,       -2500,   45,   389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-500,    0,       -250,    90,   389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(1500,    0,       -2349,   90,   389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(500,     0,       -250,    270,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       -250,    0,    389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(1700,    0,       5940,    180,  389,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       6500,    180,  389,  0x0, 0,   7,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4800,    100,     4400,    270,  389,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4800,    100,     3599,    270,  389,  0x0, 0,   9,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-4800,   100,     4000,    90,   389,  0x0, 0,   10,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-4800,   100,     -500,    90,   389,  0x0, 0,   11,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-4800,   100,     -1500,   90,   389,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-6500,   0,       2609,    180,  389,  0x0, 0,   13,  0,   0,   0,   255, 255, 255,  0)

    DeclEvent(0x0040, 0, 38,  0.0,                   8.0,                   -1.0,                  4.0,                   [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -0.0,                  -2.0,                  0.25,                  1.0])

    DeclActor(-5050,   0,       2700,    1000,    -6500,   1500,    2610,    0x007E, 0,  36, 0x0000)
    DeclActor(-1870,   0,       5380,    1200,    -1870,   1500,    5380,    0x007C, 0,  37, 0x0000)

    ChipFrameInfo(1068, 0)                                       # 0

    ScpFunction((
        "Function_0_42C",          # 00, 0
        "Function_1_4E4",          # 01, 1
        "Function_2_561",          # 02, 2
        "Function_3_58B",          # 03, 3
        "Function_4_6FD",          # 04, 4
        "Function_5_8E9",          # 05, 5
        "Function_6_990",          # 06, 6
        "Function_7_B06",          # 07, 7
        "Function_8_BBE",          # 08, 8
        "Function_9_D17",          # 09, 9
        "Function_10_DF7",         # 0A, 10
        "Function_11_EE8",         # 0B, 11
        "Function_12_100F",        # 0C, 12
        "Function_13_10ED",        # 0D, 13
        "Function_14_1226",        # 0E, 14
        "Function_15_1276",        # 0F, 15
        "Function_16_12D6",        # 10, 16
        "Function_17_1373",        # 11, 17
        "Function_18_1527",        # 12, 18
        "Function_19_1EE5",        # 13, 19
        "Function_20_2EAA",        # 14, 20
        "Function_21_2F5E",        # 15, 21
        "Function_22_3DD9",        # 16, 22
        "Function_23_3E1E",        # 17, 23
        "Function_24_3E68",        # 18, 24
        "Function_25_3E78",        # 19, 25
        "Function_26_4E08",        # 1A, 26
        "Function_27_5D03",        # 1B, 27
        "Function_28_6C92",        # 1C, 28
        "Function_29_7ADF",        # 1D, 29
        "Function_30_865F",        # 1E, 30
        "Function_31_9528",        # 1F, 31
        "Function_32_A2BB",        # 20, 32
        "Function_33_B0F1",        # 21, 33
        "Function_34_C01A",        # 22, 34
        "Function_35_CF17",        # 23, 35
        "Function_36_DE28",        # 24, 36
        "Function_37_E69C",        # 25, 37
        "Function_38_E700",        # 26, 38
    ))


    def Function_0_42C(): pass

    label("Function_0_42C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_46C"),
        (1, "loc_478"),
        (2, "loc_484"),
        (3, "loc_490"),
        (4, "loc_49C"),
        (5, "loc_4A8"),
        (6, "loc_4B4"),
        (SWITCH_DEFAULT, "loc_4C0"),
    )


    label("loc_46C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_478")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_484")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_490")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_49C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4A8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4E3")

    Return()

    # Function_0_42C end

    def Function_1_4E4(): pass

    label("Function_1_4E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_4F2")
    Jump("loc_560")

    label("loc_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_500")
    Jump("loc_560")

    label("loc_500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_50E")
    Jump("loc_560")

    label("loc_50E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_51F")
    Call(0, 17)
    Jump("loc_560")

    label("loc_51F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_52D")
    Jump("loc_560")

    label("loc_52D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_53B")
    Jump("loc_560")

    label("loc_53B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_549")
    Jump("loc_560")

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_557")
    Jump("loc_560")

    label("loc_557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_560")

    label("loc_560")

    Return()

    # Function_1_4E4 end

    def Function_2_561(): pass

    label("Function_2_561")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58A")
    OP_66(0x0, 0x1)

    label("loc_58A")

    Return()

    # Function_2_561 end

    def Function_3_58B(): pass

    label("Function_3_58B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A4")
    Jump("loc_6F9")

    label("loc_5A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BA")
    Jump("loc_6F9")

    label("loc_5BA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D0")
    Jump("loc_6F9")

    label("loc_5D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E6")
    Jump("loc_6F9")

    label("loc_5E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_681")

    #C0001
    ChrTalk(
        0x8,
        (
            "#00100Fうーん、最後のチケットは\x01",
            "どこで使おうかしらね。\x02\x03",

            "#00104F出来たら思い出に残るような\x01",
            "ところがいいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6F9")

    label("loc_681")


    #C0002
    ChrTalk(
        0x8,
        (
            "#00100F出来たら最後のチケットは\x01",
            "思い出に残るようなところで\x01",
            "使いたいのだけど……\x02\x03",

            "#00104Fうーん、どこがいいかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F9")

    TalkEnd(0xFE)
    Return()

    # Function_3_58B end

    def Function_4_6FD(): pass

    label("Function_4_6FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_716")
    Jump("loc_8E5")

    label("loc_716")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72C")
    Jump("loc_8E5")

    label("loc_72C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_829")

    #C0003
    ChrTalk(
        0x9,
        (
            "#00200Fさっきからみっしぃを\x01",
            "追跡してみてるんですが……\x02\x03",

            "メインのアトラクションに限らず、\x01",
            "実に色々な所を巡回しています。\x02\x03",

            "#00204Fファンに少しでも多く会えるように\x01",
            "頑張っているわけですね。\x01",
            "……さすがはみっしぃです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8B9")

    label("loc_829")


    #C0004
    ChrTalk(
        0x9,
        (
            "#00200Fそれにしても、みっしぃの妹\x01",
            "『みーしぇ』はいまだに見かけません。\x02\x03",

            "#00204Fもしかして、出てくる時間帯が\x01",
            "限られているのでしょうか……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B9")

    Jump("loc_8E5")

    label("loc_8BE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D4")
    Jump("loc_8E5")

    label("loc_8D4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E5")

    label("loc_8E5")

    TalkEnd(0xFE)
    Return()

    # Function_4_6FD end

    def Function_5_8E9(): pass

    label("Function_5_8E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_939")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90F")
    Call(0, 16)
    Jump("loc_934")

    label("loc_90F")


    #C0005
    ChrTalk(
        0xA,
        "#10106Fも、もうフランったら……\x02",
    )

    CloseMessageWindow()

    label("loc_934")

    Jump("loc_98C")

    label("loc_939")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94F")
    Jump("loc_98C")

    label("loc_94F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_965")
    Jump("loc_98C")

    label("loc_965")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97B")
    Jump("loc_98C")

    label("loc_97B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98C")

    label("loc_98C")

    TalkEnd(0xFE)
    Return()

    # Function_5_8E9 end

    def Function_6_990(): pass

    label("Function_6_990")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A9")
    Jump("loc_B02")

    label("loc_9A9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BF")
    Jump("loc_B02")

    label("loc_9BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D5")
    Jump("loc_B02")

    label("loc_9D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA4")

    #C0006
    ChrTalk(
        0xB,
        (
            "#10300Fフフ、ここのソファは\x01",
            "なかなかモノがいいね。\x02\x03",

            "#10304F次に回る場所を決めるまで、\x01",
            "勝手に休ませてもらおうかな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0007
    ChrTalk(
        0x101,
        "#00006Fおいおい……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_AEC")

    label("loc_AA4")


    #C0008
    ChrTalk(
        0xB,
        (
            "#10304Fフフ、次に回る場所を決めるまで\x01",
            "勝手に休ませてもらおうかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AEC")

    Jump("loc_B02")

    label("loc_AF1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B02")

    label("loc_B02")

    TalkEnd(0xFE)
    Return()

    # Function_6_990 end

    def Function_7_B06(): pass

    label("Function_7_B06")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2C")
    Call(0, 16)
    Jump("loc_B62")

    label("loc_B2C")


    #C0009
    ChrTalk(
        0xC,
        (
            "#06409Fお姉ちゃんの恋愛運、\x01",
            "占ってもらおうよ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B62")

    Jump("loc_BBA")

    label("loc_B67")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7D")
    Jump("loc_BBA")

    label("loc_B7D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B93")
    Jump("loc_BBA")

    label("loc_B93")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA9")
    Jump("loc_BBA")

    label("loc_BA9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBA")

    label("loc_BBA")

    TalkEnd(0xFE)
    Return()

    # Function_7_B06 end

    def Function_8_BBE(): pass

    label("Function_8_BBE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD7")
    Jump("loc_D13")

    label("loc_BD7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C54")

    #C0010
    ChrTalk(
        0xD,
        (
            "#01805F（東方系の占術師……）\x02\x03",

            "#01803F（心当たりがないわけじゃ\x01",
            "  ないけど……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xD, 0x10)
    Jump("loc_CD1")

    label("loc_C54")


    #C0011
    ChrTalk(
        0xD,
        (
            "#01805Fあっ……ロイドさん。\x01",
            "い、いつからそこに？\x02\x03",

            "#01809Fあはは……\x01",
            "すごい順番待ちだなあと\x01",
            "改めて感心しちゃってました。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD1")

    Jump("loc_D13")

    label("loc_CD6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEC")
    Jump("loc_D13")

    label("loc_CEC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D02")
    Jump("loc_D13")

    label("loc_D02")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D13")

    label("loc_D13")

    TalkEnd(0xFE)
    Return()

    # Function_8_BBE end

    def Function_9_D17(): pass

    label("Function_9_D17")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D30")
    Jump("loc_DF3")

    label("loc_D30")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D46")
    Jump("loc_DF3")

    label("loc_D46")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCC")

    #C0012
    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "ここの占い師のお姉さん、\x01",
            "すっごく上手なんだ～。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みししっ、色んな事を\x01",
            "占ってもらうといいヨ～。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF3")

    label("loc_DCC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE2")
    Jump("loc_DF3")

    label("loc_DE2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF3")

    label("loc_DF3")

    TalkEnd(0xFE)
    Return()

    # Function_9_D17 end

    def Function_10_DF7(): pass

    label("Function_10_DF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE4")
    TalkBegin(0xFE)

    #C0014
    ChrTalk(
        0xFE,
        "《占いの館》へようこそっ！\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "ここでは、凄腕占い師の先生に\x01",
            "色々と占ってもらえちゃいますっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#00003F（みーしぇとかくれんぼ中だし……\x01",
            "　今アトラクションで遊ぶのは\x01",
            "　やめておくとしよう。）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_EE7")

    label("loc_EE4")

    Call(0, 18)

    label("loc_EE7")

    Return()

    # Function_10_DF7 end

    def Function_11_EE8(): pass

    label("Function_11_EE8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F7D")

    #C0017
    ChrTalk(
        0x10,
        (
            "見渡すと、やっぱり\x01",
            "女の子のお客さんが多いな～……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x10,
        (
            "彼女と一緒だからよかったけど、\x01",
            "１人だったら居心地悪いだろうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_100B")

    label("loc_F7D")


    #C0019
    ChrTalk(
        0x10,
        (
            "相性占いでいい結果が出て、\x01",
            "彼女の機嫌が相当良くなったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x10,
        (
            "もし微妙な結果が出てたらと思うと……\x01",
            "気まずいなんてものじゃないだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100B")

    TalkEnd(0xFE)
    Return()

    # Function_11_EE8 end

    def Function_12_100F(): pass

    label("Function_12_100F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1069")

    #C0021
    ChrTalk(
        0x11,
        (
            "うふふ、何を占ってもらおうかな。\x01",
            "やっぱり彼との相性かしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E9")

    label("loc_1069")


    #C0022
    ChrTalk(
        0x11,
        (
            "占ってもらったら、\x01",
            "私たちは運命の糸で\x01",
            "結ばれてるんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x11,
        (
            "うふふふふ……\x01",
            "彼を選んだ私の目に\x01",
            "間違いはなかったわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E9")

    TalkEnd(0xFE)
    Return()

    # Function_12_100F end

    def Function_13_10ED(): pass

    label("Function_13_10ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_116E")

    #C0024
    ChrTalk(
        0x12,
        (
            "旦那にナイショで、\x01",
            "失くした結婚指輪の場所を\x01",
            "占ってもらいにきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x12,
        "早く順番が来ないかしら……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1222")

    label("loc_116E")


    #C0026
    ChrTalk(
        0x12,
        (
            "落としたと思っていた結婚指輪、\x01",
            "場所を占ってもらったら……\x01",
            "なんとポケットに入ってたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x12,
        (
            "灯台下暗しって本当なのね……\x01",
            "見つかってよかったけど\x01",
            "なんだか情けなくなっちゃった。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1222")

    TalkEnd(0xFE)
    Return()

    # Function_13_10ED end

    def Function_14_1226(): pass

    label("Function_14_1226")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1272")

    #C0028
    ChrTalk(
        0x13,
        (
            "素敵な出会いの暗示が\x01",
            "出てくれたら嬉しいな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1272")

    label("loc_1272")

    TalkEnd(0xFE)
    Return()

    # Function_14_1226 end

    def Function_15_1276(): pass

    label("Function_15_1276")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12D2")

    #C0029
    ChrTalk(
        0x14,
        (
            "オトコなんてどうでもいいし、\x01",
            "あたしは金運を占ってもらおっと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D2")

    label("loc_12D2")

    TalkEnd(0xFE)
    Return()

    # Function_15_1276 end

    def Function_16_12D6(): pass

    label("Function_16_12D6")

    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0030
    ChrTalk(
        0xC,
        (
            "#06400Fお姉ちゃん、ほらほら～。\x01",
            "早く並ぼうよ～。\x02\x03",

            "#06409Fそして、お姉ちゃんの\x01",
            "恋愛運を占ってもらうの！\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xA,
        "#10111Fい、いいってば！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_16_12D6 end

    def Function_17_1373(): pass

    label("Function_17_1373")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13BF")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_13BF")

    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x8)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0xA)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0xB)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0xC)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1461")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    Jump("loc_1526")

    label("loc_1461")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148B")
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1486")
    SetChrFlags(0xD, 0x10)

    label("loc_1486")

    Jump("loc_1526")

    label("loc_148B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AB")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_1526")

    label("loc_14AB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1506")
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14E6")
    SetChrFlags(0xB, 0x80)

    label("loc_14E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1501")
    ClearChrFlags(0x18, 0x80)

    label("loc_1501")

    Jump("loc_1526")

    label("loc_1506")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1526")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_1526")

    Return()

    # Function_17_1373 end

    def Function_18_1527(): pass

    label("Function_18_1527")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 1000, 5750, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    OP_4B(0xF, 0xFF)
    SetChrPos(0x101, 0, 0, 5000, 0)
    OP_0D()

    #C0032
    ChrTalk(
        0xF,
        "《占いの館》へようこそっ！\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xF,
        (
            "ここでは、凄腕占い師の先生に\x01",
            "色々と占ってもらえちゃいますっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xF,
        (
            "２名様までお入りになれますが、\x01",
            "どうされますか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        "#00004F#6P（……誰を誘おうかな？）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 5, -1, -1)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K誰を誘う？\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "エリィ")
    MenuCmd(1, 0, "ティオ")
    MenuCmd(1, 0, "ランディ")
    MenuCmd(1, 0, "ノエル")
    MenuCmd(1, 0, "ワジ")
    MenuCmd(1, 0, "キーア")
    MenuCmd(1, 0, "フラン")
    MenuCmd(1, 0, "セシル")
    MenuCmd(1, 0, "イリア")
    MenuCmd(1, 0, "リーシャ")
    MenuCmd(1, 0, "シュリ")
    MenuCmd(1, 0, "やめる")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_16FB")
    MenuCmd(3, 0, 0x0)

    label("loc_16FB")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_170D")
    MenuCmd(3, 0, 0x1)

    label("loc_170D")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_171F")
    MenuCmd(3, 0, 0x2)

    label("loc_171F")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1731")
    MenuCmd(3, 0, 0x3)

    label("loc_1731")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1743")
    MenuCmd(3, 0, 0x4)

    label("loc_1743")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1755")
    MenuCmd(3, 0, 0x5)

    label("loc_1755")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1767")
    MenuCmd(3, 0, 0x6)

    label("loc_1767")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1779")
    MenuCmd(3, 0, 0x7)

    label("loc_1779")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_178B")
    MenuCmd(3, 0, 0x8)

    label("loc_178B")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_179D")
    MenuCmd(3, 0, 0x9)

    label("loc_179D")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_17AF")
    MenuCmd(3, 0, 0xA)

    label("loc_17AF")

    MenuCmd(2, 0, -1, 55, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E84")
    OP_D2(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1835"),
        (1, "loc_1875"),
        (2, "loc_18B5"),
        (3, "loc_18F7"),
        (4, "loc_1937"),
        (5, "loc_1975"),
        (6, "loc_19B5"),
        (7, "loc_19F5"),
        (8, "loc_1A37"),
        (9, "loc_1A7B"),
        (10, "loc_1ABD"),
        (SWITCH_DEFAULT, "loc_1AFD"),
    )


    label("loc_1835")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0037
    ChrTalk(
        0x101,
        "#00000F#6P（よし……エリィを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_1875")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0038
    ChrTalk(
        0x101,
        "#00000F#6P（よし……ティオを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_18B5")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0039
    ChrTalk(
        0x101,
        "#00000F#6P（よし……ランディを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_18F7")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0040
    ChrTalk(
        0x101,
        "#00000F#6P（よし……ノエルを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_1937")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0041
    ChrTalk(
        0x101,
        "#00000F#6P（よし……ワジを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_1975")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0042
    ChrTalk(
        0x101,
        "#00000F#6P（よし……キーアを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_19B5")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0043
    ChrTalk(
        0x101,
        "#00000F#6P（よし……フランを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_19F5")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0044
    ChrTalk(
        0x101,
        "#00000F#6P（よし……セシル姉を誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_1A37")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0045
    ChrTalk(
        0x101,
        "#00000F#6P（よし……イリアさんを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_1A7B")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0046
    ChrTalk(
        0x101,
        "#00000F#6P（よし……リーシャを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_1ABD")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0047
    ChrTalk(
        0x101,
        "#00000F#6P（よし……シュリを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_1AFD")

    FadeToDark(500, 0, -1)
    OP_0D()
    LoadEffect(0x0, "event/ev13000.eff")
    LoadChrToIndex("chr/ch14202.itc", 0x1E)
    LoadChrToIndex("chr/ch00002.itc", 0x1F)
    LoadChrToIndex("chr/ch00300.itc", 0x21)
    LoadChrToIndex("chr/ch08200.itc", 0x22)
    LoadChrToIndex("chr/ch07500.itc", 0x23)
    LoadChrToIndex("chr/ch05100.itc", 0x24)
    LoadChrToIndex("chr/ch10100.itc", 0x25)
    LoadChrToIndex("chr/ch02710.itc", 0x26)
    LoadChrToIndex("chr/ch02702.itc", 0x27)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrPos(0x16, 0, 50, 104800, 180)
    ClearChrFlags(0x15, 0x80)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1BC1"),
        (1, "loc_1BD0"),
        (2, "loc_1BDF"),
        (3, "loc_1BEE"),
        (4, "loc_1BFD"),
        (5, "loc_1C0C"),
        (6, "loc_1C1B"),
        (7, "loc_1C2A"),
        (8, "loc_1C39"),
        (9, "loc_1C48"),
        (10, "loc_1C57"),
        (SWITCH_DEFAULT, "loc_1C66"),
    )


    label("loc_1BC1")

    LoadChrToIndex("chr/ch00102.itc", 0x20)
    SetChrChipByIndex(0x15, 0x0)
    Jump("loc_1C66")

    label("loc_1BD0")

    LoadChrToIndex("chr/ch00202.itc", 0x20)
    SetChrChipByIndex(0x15, 0x1)
    Jump("loc_1C66")

    label("loc_1BDF")

    LoadChrToIndex("chr/ch00302.itc", 0x20)
    SetChrChipByIndex(0x15, 0x21)
    Jump("loc_1C66")

    label("loc_1BEE")

    LoadChrToIndex("chr/ch02902.itc", 0x20)
    SetChrChipByIndex(0x15, 0x2)
    Jump("loc_1C66")

    label("loc_1BFD")

    LoadChrToIndex("chr/ch03002.itc", 0x20)
    SetChrChipByIndex(0x15, 0x3)
    Jump("loc_1C66")

    label("loc_1C0C")

    LoadChrToIndex("chr/ch08202.itc", 0x20)
    SetChrChipByIndex(0x15, 0x22)
    Jump("loc_1C66")

    label("loc_1C1B")

    LoadChrToIndex("chr/ch08502.itc", 0x20)
    SetChrChipByIndex(0x15, 0x4)
    Jump("loc_1C66")

    label("loc_1C2A")

    LoadChrToIndex("chr/ch07502.itc", 0x20)
    SetChrChipByIndex(0x15, 0x23)
    Jump("loc_1C66")

    label("loc_1C39")

    LoadChrToIndex("chr/ch05102.itc", 0x20)
    SetChrChipByIndex(0x15, 0x24)
    Jump("loc_1C66")

    label("loc_1C48")

    LoadChrToIndex("chr/ch05202.itc", 0x20)
    SetChrChipByIndex(0x15, 0x5)
    Jump("loc_1C66")

    label("loc_1C57")

    LoadChrToIndex("chr/ch10102.itc", 0x20)
    SetChrChipByIndex(0x15, 0x25)
    Jump("loc_1C66")

    label("loc_1C66")

    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x101, -500, 0, 5000, 0)
    SetChrPos(0x15, 500, 0, 5000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0048
    ChrTalk(
        0xF,
        "チケットをお預かりしますねっ！\x02",
    )

    CloseMessageWindow()
    SubItemNumber(0x35D, 1)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0049
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "スタッフにチケットを１枚渡した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0050
    ChrTalk(
        0xF,
        "それでは、お入りくださいませ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 19)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x15, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_1DB9"),
        (1, "loc_1DC7"),
        (2, "loc_1DD5"),
        (3, "loc_1DE3"),
        (4, "loc_1DF1"),
        (5, "loc_1DFF"),
        (6, "loc_1E0D"),
        (7, "loc_1E1B"),
        (8, "loc_1E29"),
        (9, "loc_1E37"),
        (10, "loc_1E45"),
        (SWITCH_DEFAULT, "loc_1E53"),
    )


    label("loc_1DB9")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1DC7")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1DD5")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1DE3")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1DF1")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1DFF")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1E0D")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1E1B")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1E29")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1E37")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1E45")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1E53")

    OP_D2(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E7F")
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()

    label("loc_1E7F")

    Jump("loc_1ECD")

    label("loc_1E84")


    #C0051
    ChrTalk(
        0xF,
        "あら、おやめになりますか？\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xF,
        "またのお越しをおまちしてますっ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1ECD")

    OP_4C(0xF, 0xFF)
    SetChrPos(0x0, 0, 0, 4000, 180)
    EventEnd(0x5)
    Return()

    # Function_18_1527 end

    def Function_19_1EE5(): pass

    label("Function_19_1EE5")

    SoundLoad(852)
    SetChrPos(0x101, -500, 0, 93000, 0)
    SetChrPos(0x15, 500, 0, 93000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 900, 97500, 0)
    MoveCamera(0, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    FadeToBright(1000, 0)
    OP_68(0, 900, 100000, 3000)
    Sleep(500)

    def lambda_1F70():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F70)

    def lambda_1F81():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1F81)

    def lambda_1F92():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F92)
    Sleep(0)

    def lambda_1FAA():
        OP_9B(0x0, 0x15, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1FAA)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x15, 0)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x15, 2)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2939")

    #C0053
    ChrTalk(
        0x16,
        "#5Pふふ、いらっしゃい。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x16,
        "#5Pさあ、こちらの椅子にお座りなさい。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#00000F#6Pは、はい。\x02",
    )

    CloseMessageWindow()
    Call(0, 20)

    #C0056
    ChrTalk(
        0x101,
        (
            "#00003F#6P（話に聞いてた通り、\x01",
            "  エキゾチックで神秘的な人だな……）\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_20DD"),
        (1, "loc_2133"),
        (2, "loc_2196"),
        (3, "loc_21FB"),
        (4, "loc_2260"),
        (5, "loc_22FE"),
        (6, "loc_2352"),
        (7, "loc_23AE"),
        (8, "loc_2404"),
        (9, "loc_245C"),
        (10, "loc_24BC"),
        (SWITCH_DEFAULT, "loc_251B"),
    )


    label("loc_20DD")


    #N0057
    NpcTalk(
        0x15,
        "エリィ",
        (
            "#00100F#12P（ええ、それに顔は隠れてるけど\x01",
            "  とても美人の方みたい。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_2133")


    #N0058
    NpcTalk(
        0x15,
        "ティオ",
        (
            "#00200F#12P（ええ、それに……\x01",
            "  顔は隠れてますけど\x01",
            "  かなり美人の方みたいです。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_2196")


    #N0059
    NpcTalk(
        0x15,
        "ランディ",
        (
            "#00300F#12P（ああ、それに……\x01",
            "  顔は隠れてるがかなり美人の\x01",
            "  お姉さんみてえだ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_21FB")


    #N0060
    NpcTalk(
        0x15,
        "ノエル",
        (
            "#10100F#12P（ええ、それに……\x01",
            "  顔を隠してますけど、\x01",
            "  とても美人な方みたいです。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_2260")


    #N0061
    NpcTalk(
        0x15,
        "ワジ",
        "#10305F#12P（…………へえ…………）\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        "#00005F#6P（……ワジ？）\x02",
    )

    CloseMessageWindow()

    #N0063
    NpcTalk(
        0x15,
        "ワジ",
        (
            "#10304F#12P（フフ、あんまり美人なんで\x01",
            "  ちょっと驚いちゃってね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_22FE")


    #N0064
    NpcTalk(
        0x15,
        "キーア",
        (
            "#01100F#12P（うん、それに顔が隠れてるけど\x01",
            "  美人のヒトみたいー。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_2352")


    #N0065
    NpcTalk(
        0x15,
        "フラン",
        (
            "#06400F#12P（ええ、それに顔は隠れてますけど\x01",
            "  すっごい美人みたいです～。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_23AE")


    #N0066
    NpcTalk(
        0x15,
        "セシル",
        (
            "#05900F#12P（ええ、それに顔は隠れてるけど\x01",
            "  とても美しい人みたい。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_2404")


    #N0067
    NpcTalk(
        0x15,
        "イリア",
        (
            "#01700F#12P（ええ、それに顔は隠れてるけど\x01",
            "  なかなかの美人みたいね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_245C")


    #N0068
    NpcTalk(
        0x15,
        "リーシャ",
        (
            "#01802F#12P（ええ……顔は隠れていますが、\x01",
            "  とても美しい人みたいですし……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_24BC")


    #N0069
    NpcTalk(
        0x15,
        "シュリ",
        (
            "#14000F#12P（ああ、それに……\x01",
            "  顔は隠してるけど、\x01",
            "  すっごい美人みたいだ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_251B")


    #C0070
    ChrTalk(
        0x16,
        (
            "#5Pふふ、どうしたのかしら。\x01",
            "人の顔をジロジロと見て。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x16,
        (
            "#5P順番待ちの人もいるから\x01",
            "すぐにとりかかりたいのだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#00012F#6Pあ、すみません。\x01",
            "えっと、よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x16,
        "#5Pふふ、ではその前に……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x16,
        (
            "#5Pまずはあなた達の\x01",
            "血液型を教えてもらえるかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_269B"),
        (1, "loc_26CA"),
        (2, "loc_26F9"),
        (3, "loc_2726"),
        (4, "loc_2751"),
        (5, "loc_2778"),
        (6, "loc_279F"),
        (7, "loc_27CC"),
        (8, "loc_27FB"),
        (9, "loc_2839"),
        (10, "loc_286A"),
        (SWITCH_DEFAULT, "loc_2893"),
    )


    label("loc_269B")


    #N0075
    NpcTalk(
        0x15,
        "エリィ",
        "#00105F#12P血液型……ですか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_26CA")


    #N0076
    NpcTalk(
        0x15,
        "ティオ",
        "#00205F#12P血液型……ですか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_26F9")


    #N0077
    NpcTalk(
        0x15,
        "ランディ",
        "#00305F#12P血液型ッスか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_2726")


    #N0078
    NpcTalk(
        0x15,
        "ノエル",
        "#10105F#12P血液型ですか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_2751")


    #N0079
    NpcTalk(
        0x15,
        "ワジ",
        "#10305F#12P血液型かい？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_2778")


    #N0080
    NpcTalk(
        0x15,
        "キーア",
        "#01105F#12P血液型ー？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_279F")


    #N0081
    NpcTalk(
        0x15,
        "フラン",
        "#06405F#12P血液型ですか～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_27CC")


    #N0082
    NpcTalk(
        0x15,
        "セシル",
        "#05905F#12P血液型……ですか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_27FB")


    #N0083
    NpcTalk(
        0x15,
        "イリア",
        (
            "#01705F#12P血液型……\x01",
            "何かに必要なのかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_2839")


    #N0084
    NpcTalk(
        0x15,
        "リーシャ",
        "#01805F#12P血液型……ですか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_286A")


    #N0085
    NpcTalk(
        0x15,
        "シュリ",
        "#14005F#12P血液型……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_2893")


    #C0086
    ChrTalk(
        0x16,
        (
            "#5Pええ、正確に占うために\x01",
            "必要になるものなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x16,
        (
            "#5Pもちろん、無理にとは\x01",
            "言わないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#00000F#6Pいえ、それくらいなら。\x01",
            "……俺の血液型はＯ型です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A72")

    label("loc_2939")


    #C0089
    ChrTalk(
        0x16,
        "#5Pあら、貴方はさっきの……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x16,
        (
            "#5Pふふ、いらっしゃい。\x01",
            "こちらの椅子にどうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        "#00000F#6Pはい。\x02",
    )

    CloseMessageWindow()
    Call(0, 20)

    #C0092
    ChrTalk(
        0x16,
        (
            "#5Pまた来てくれたようで\x01",
            "嬉しい限りだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x16,
        (
            "#5Pそれではさっそくだけど、\x01",
            "あなた達の血液型を\x01",
            "教えてもらえるかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x16,
        (
            "#5P……そちらの貴方は、\x01",
            "確かＯ型だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        "#00000F#6Pええ、そうです。\x02",
    )

    CloseMessageWindow()

    label("loc_2A72")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2ABD"),
        (1, "loc_2AF6"),
        (2, "loc_2B2D"),
        (3, "loc_2B5A"),
        (4, "loc_2B8B"),
        (5, "loc_2BC6"),
        (6, "loc_2C45"),
        (7, "loc_2CA2"),
        (8, "loc_2CD5"),
        (9, "loc_2D02"),
        (10, "loc_2D5B"),
        (SWITCH_DEFAULT, "loc_2D97"),
    )


    label("loc_2ABD")


    #N0096
    NpcTalk(
        0x15,
        "エリィ",
        "#00100F#12Pえっと、私の方はＡ型ですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2AF6")


    #N0097
    NpcTalk(
        0x15,
        "ティオ",
        "#00200F#12Pわたしの方はＡＢ型ですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2B2D")


    #N0098
    NpcTalk(
        0x15,
        "ランディ",
        "#00300F#12P俺はＢ型ッス。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2B5A")


    #N0099
    NpcTalk(
        0x15,
        "ノエル",
        "#10100F#12PあたしはＡ型ですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2B8B")


    #N0100
    NpcTalk(
        0x15,
        "ワジ",
        "#10300F#12Pフフ、確かＡＢ型だったと思うよ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2BC6")


    #N0101
    NpcTalk(
        0x15,
        "キーア",
        (
            "#01109F#12Pえっと、キーアは\x01",
            "たしかＢ型だよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#00000F#6Pああ、以前ウルスラ病院で\x01",
            "検査した事があったな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2C45")


    #N0103
    NpcTalk(
        0x15,
        "フラン",
        "#06409F#12Pあ、わたしもＯ型なんですよー！\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        "#00009F#6Pはは、お揃いだな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2CA2")


    #N0105
    NpcTalk(
        0x15,
        "セシル",
        "#05900F#12Pえっと、私はＡ型です。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2CD5")


    #N0106
    NpcTalk(
        0x15,
        "イリア",
        "#01700F#12PあたしはＢ型よ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2D02")


    #N0107
    NpcTalk(
        0x15,
        "リーシャ",
        "#01802F#12Pあ……私もＯ型ですよ。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        "#00009F#6Pはは、奇遇だったな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2D5B")


    #N0109
    NpcTalk(
        0x15,
        "シュリ",
        (
            "#14000F#12Pえっと……\x01",
            "多分、オレはＡかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2D97")


    #C0110
    ChrTalk(
        0x16,
        "#5Pふふ……どうも。\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x16,
        "#5Pでは、今回は何を占うのかしら？\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        "#00000F#6Pえっと、それじゃあ……\x02",
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2E48"),
        (1, "loc_2E50"),
        (2, "loc_2E58"),
        (3, "loc_2E60"),
        (4, "loc_2E68"),
        (5, "loc_2E70"),
        (6, "loc_2E78"),
        (7, "loc_2E80"),
        (8, "loc_2E88"),
        (9, "loc_2E90"),
        (10, "loc_2E98"),
        (SWITCH_DEFAULT, "loc_2EA0"),
    )


    label("loc_2E48")

    Call(0, 25)
    Jump("loc_2EA0")

    label("loc_2E50")

    Call(0, 26)
    Jump("loc_2EA0")

    label("loc_2E58")

    Call(0, 27)
    Jump("loc_2EA0")

    label("loc_2E60")

    Call(0, 28)
    Jump("loc_2EA0")

    label("loc_2E68")

    Call(0, 29)
    Jump("loc_2EA0")

    label("loc_2E70")

    Call(0, 30)
    Jump("loc_2EA0")

    label("loc_2E78")

    Call(0, 31)
    Jump("loc_2EA0")

    label("loc_2E80")

    Call(0, 32)
    Jump("loc_2EA0")

    label("loc_2E88")

    Call(0, 33)
    Jump("loc_2EA0")

    label("loc_2E90")

    Call(0, 34)
    Jump("loc_2EA0")

    label("loc_2E98")

    Call(0, 35)
    Jump("loc_2EA0")

    label("loc_2EA0")

    OP_24(0x354)
    Call(0, 17)
    Call(0, 21)
    Return()

    # Function_19_1EE5 end

    def Function_20_2EAA(): pass

    label("Function_20_2EAA")

    OP_68(0, 900, 103500, 3000)
    SetCameraDistance(15000, 3000)

    def lambda_2EC9():
        OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2EC9)

    def lambda_2EDE():
        OP_9B(0x0, 0xFE, 0xA, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2EDE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x15, 1)

    def lambda_2EFB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2EFB)

    def lambda_2F08():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2F08)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x15, 2)
    OP_6F(0x79)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -630, 50, 101950, 0)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 630, 50, 101950, 0)
    OP_0D()
    Return()

    # Function_20_2EAA end

    def Function_21_2F5E(): pass

    label("Function_21_2F5E")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2FB1"),
        (1, "loc_2FBA"),
        (2, "loc_2FC3"),
        (3, "loc_2FCC"),
        (4, "loc_2FD5"),
        (5, "loc_2FDE"),
        (6, "loc_2FE7"),
        (7, "loc_2FF0"),
        (8, "loc_2FF9"),
        (9, "loc_3002"),
        (10, "loc_300B"),
        (SWITCH_DEFAULT, "loc_3014"),
    )


    label("loc_2FB1")

    SetChrChipByIndex(0x15, 0x0)
    Jump("loc_3014")

    label("loc_2FBA")

    SetChrChipByIndex(0x15, 0x1)
    Jump("loc_3014")

    label("loc_2FC3")

    SetChrChipByIndex(0x15, 0x21)
    Jump("loc_3014")

    label("loc_2FCC")

    SetChrChipByIndex(0x15, 0x2)
    Jump("loc_3014")

    label("loc_2FD5")

    SetChrChipByIndex(0x15, 0x3)
    Jump("loc_3014")

    label("loc_2FDE")

    SetChrChipByIndex(0x15, 0x22)
    Jump("loc_3014")

    label("loc_2FE7")

    SetChrChipByIndex(0x15, 0x4)
    Jump("loc_3014")

    label("loc_2FF0")

    SetChrChipByIndex(0x15, 0x23)
    Jump("loc_3014")

    label("loc_2FF9")

    SetChrChipByIndex(0x15, 0x24)
    Jump("loc_3014")

    label("loc_3002")

    SetChrChipByIndex(0x15, 0x5)
    Jump("loc_3014")

    label("loc_300B")

    SetChrChipByIndex(0x15, 0x25)
    Jump("loc_3014")

    label("loc_3014")

    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -600, 0, 5000, 90)
    SetChrPos(0x15, 600, 0, 5000, 270)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3068")
    SetChrPos(0x17, 1700, 0, 4040, 270)

    label("loc_3068")

    OP_68(0, 1500, 5750, 0)
    OP_68(0, 1000, 5750, 3000)
    MoveCamera(0, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_30FE"),
        (1, "loc_321B"),
        (2, "loc_333B"),
        (3, "loc_346E"),
        (4, "loc_358A"),
        (5, "loc_3695"),
        (6, "loc_3810"),
        (7, "loc_393F"),
        (8, "loc_3A4D"),
        (9, "loc_3B75"),
        (10, "loc_3CBF"),
        (SWITCH_DEFAULT, "loc_3DD8"),
    )


    label("loc_30FE")


    #N0113
    NpcTalk(
        0x15,
        "エリィ",
        (
            "#00100F#11Pはあ……なんだかとても\x01",
            "神秘的な時間だったわね。\x02\x03",

            "#00104Fあの占い師さんの雰囲気に\x01",
            "正直あてられそうだったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#00003F#5Pああ……\x01",
            "只者じゃなさそうだよな。\x02\x03",

            "#00000F……さてと、それじゃあ\x01",
            "俺は一旦ここで。\x02",
        )
    )

    CloseMessageWindow()

    #N0115
    NpcTalk(
        0x15,
        "エリィ",
        "#00100F#11Pええ、また後でね。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DD8")

    label("loc_321B")


    #N0116
    NpcTalk(
        0x15,
        "ティオ",
        (
            "#00202Fあの占い師さんの占いには\x01",
            "かなりのオーラを感じました。\x02\x03",

            "#00204Fやはり噂の占い師だけあって\x01",
            "只者ではなさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#00004F確かに……\x01",
            "なんだか凄そうな人だったな。\x02\x03",

            "#00000F……さてと、それじゃあ\x01",
            "俺は一旦ここで。\x02",
        )
    )

    CloseMessageWindow()

    #N0118
    NpcTalk(
        0x15,
        "ティオ",
        "#00200Fええ、それではまた。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DD8")

    label("loc_333B")


    #N0119
    NpcTalk(
        0x15,
        "ランディ",
        (
            "#00309F……はあ、にしても\x01",
            "ステキなお姉様だったなあ。\x02\x03",

            "#00304Fあのミステリアスな雰囲気が\x01",
            "たまんねえっつうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        (
            "#00009Fはは……確かにな。\x01",
            "占いにしてはものすごく\x01",
            "筋が通っていたみたいだし。\x02\x03",

            "#00000F……さてと、それじゃあ\x01",
            "俺は一旦ここで。\x02",
        )
    )

    CloseMessageWindow()

    #N0121
    NpcTalk(
        0x15,
        "ランディ",
        "#00300Fああ、そんじゃな。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DD8")

    label("loc_346E")


    #N0122
    NpcTalk(
        0x15,
        "ノエル",
        (
            "#10100F……ふう、なんだか凄く\x01",
            "神秘的な時間を過ごしましたね。\x02\x03",

            "#10104F占いも説得力がありましたし、\x01",
            "なんだか不思議な気持ちです。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#00004Fああ……\x01",
            "なかなか興味深かったな。\x02\x03",

            "#00000F……さてと、それじゃあ\x01",
            "俺は一旦ここで。\x02",
        )
    )

    CloseMessageWindow()

    #N0124
    NpcTalk(
        0x15,
        "ノエル",
        "#10100Fええ、ではまた！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DD8")

    label("loc_358A")


    #N0125
    NpcTalk(
        0x15,
        "ワジ",
        (
            "#10300Fフフ、なかなか興味深い\x01",
            "お姉さんだったよ。\x02\x03",

            "#10304Fもう少し色々と\x01",
            "話してみたかったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        (
            "#00009Fはは、確かにな。\x01",
            "なんだか世界観が\x01",
            "広がりそうだし。\x02\x03",

            "#00000F……さてと、それじゃあ\x01",
            "俺は一旦ここで。\x02",
        )
    )

    CloseMessageWindow()

    #N0127
    NpcTalk(
        0x15,
        "ワジ",
        "#10300Fああ、また後でね。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DD8")

    label("loc_3695")


    #N0128
    NpcTalk(
        0x15,
        "キーア",
        (
            "#01109F占いって、すっごく面白かったねー。\x02\x03",

            "#01111Fどうしてあんな色々と分かるのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#00009Fうーん、分からないけど……\x01",
            "きっと相当な修行を\x01",
            "積んだんじゃないかな。\x02\x03",

            "#00000F……さてと、それじゃあ\x01",
            "俺は一旦ここで。\x02",
        )
    )

    CloseMessageWindow()

    #N0130
    NpcTalk(
        0x15,
        "キーア",
        "#01100Fうん、またねー！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3801")

    #C0131
    ChrTalk(
        0x17,
        "#01200F……ウォン。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    EndChrThread(0x17, 0x0)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    OP_93(0x17, 0xB4, 0x1F4)

    def lambda_37DF():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_37DF)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x15, 3)
    SetChrFlags(0x17, 0x80)
    Jump("loc_380B")

    label("loc_3801")

    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)

    label("loc_380B")

    Jump("loc_3DD8")

    label("loc_3810")


    #N0132
    NpcTalk(
        0x15,
        "フラン",
        (
            "#06402Fはー、なんだか\x01",
            "神秘的なお姉さんでしたね～。\x02\x03",

            "#06409Fお姉ちゃんみたいな\x01",
            "かっこいい女性もいいけど、\x01",
            "あんな人も憧れますよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        (
            "#00002Fはは……クロスベルには\x01",
            "なかなかいないタイプだしな。\x02\x03",

            "#00000F……さてと、それじゃあ\x01",
            "俺は一旦ここで。\x02",
        )
    )

    CloseMessageWindow()

    #N0134
    NpcTalk(
        0x15,
        "フラン",
        "#06400Fはい、また～！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DD8")

    label("loc_393F")


    #N0135
    NpcTalk(
        0x15,
        "セシル",
        (
            "#05909Fふふ……なんだか\x01",
            "不思議な人だったわね。\x02\x03",

            "#05904F色々と過去がありそう\x01",
            "だったけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        (
            "#00003Fああ……どういう経緯で\x01",
            "クロスベルに来たんだろうな。\x02\x03",

            "#00000F……さてと、それじゃあ\x01",
            "俺は一旦ここで。\x02",
        )
    )

    CloseMessageWindow()

    #N0137
    NpcTalk(
        0x15,
        "セシル",
        "#05900Fええ、また後でね。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DD8")

    label("loc_3A4D")


    #N0138
    NpcTalk(
        0x15,
        "イリア",
        (
            "#01702Fいやー、世の中には\x01",
            "色々とスゴイ人がいるもんね。\x02\x03",

            "#01703F初めて会うのに、何から何まで\x01",
            "見透かされてそうな感じだったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#00003Fええ、確かに……\x01",
            "只者じゃなさそうでしたね。\x02\x03",

            "#00000F……さてと、それじゃあ\x01",
            "俺は一旦ここで。\x02",
        )
    )

    CloseMessageWindow()

    #N0140
    NpcTalk(
        0x15,
        "イリア",
        "#01700Fうん、また後でね～。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DD8")

    label("loc_3B75")


    #N0141
    NpcTalk(
        0x15,
        "リーシャ",
        (
            "#01803F（あの高等な占術……\x01",
            "  もしかして、あの女性は……）\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        "#00005Fリーシャ、どうしたんだ？\x02",
    )

    CloseMessageWindow()

    #N0143
    NpcTalk(
        0x15,
        "リーシャ",
        (
            "#01805Fあ、いえ。\x02\x03",

            "#01802Fふふ、不思議な体験が出来て\x01",
            "とても楽しかったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        (
            "#00009Fはは、俺もだよ。\x02\x03",

            "#00000F……さてと、それじゃあ\x01",
            "俺は一旦ここで。\x02",
        )
    )

    CloseMessageWindow()

    #N0145
    NpcTalk(
        0x15,
        "リーシャ",
        "#01803Fはい、また後で。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DD8")

    label("loc_3CBF")


    #N0146
    NpcTalk(
        0x15,
        "シュリ",
        (
            "#14000F……なんだか凄い占い師だったな。\x02\x03",

            "#14006F占いなんてあんまり信じてなかったけど、\x01",
            "今回ばかりはそうも言えないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#00004Fああ……\x01",
            "確かに凄い占いだったよな。\x02\x03",

            "#00000F……さてと、それじゃあ\x01",
            "俺は一旦ここで。\x02",
        )
    )

    CloseMessageWindow()

    #N0148
    NpcTalk(
        0x15,
        "シュリ",
        "#14000F……ん、そんじゃな。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DD8")

    label("loc_3DD8")

    Return()

    # Function_21_2F5E end

    def Function_22_3DD9(): pass

    label("Function_22_3DD9")


    def lambda_3DDE():

        label("loc_3DDE")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_3DDE")

    QueueWorkItem2(0x101, 2, lambda_3DDE)
    OP_93(0x15, 0xB4, 0x1F4)

    def lambda_3DF7():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3DF7)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x15, 1)
    EndChrThread(0x101, 0x2)
    Return()

    # Function_22_3DD9 end

    def Function_23_3E1E(): pass

    label("Function_23_3E1E")

    Fade(500)
    Sound(895, 0, 50, 0)
    Sound(852, 2, 70, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 900, 103300, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Return()

    # Function_23_3E1E end

    def Function_24_3E68(): pass

    label("Function_24_3E68")

    Fade(500)
    StopSound(852, 1000, 40)
    StopEffect(0x0, 0x2)
    OP_0D()
    Return()

    # Function_24_3E68 end

    def Function_25_3E78(): pass

    label("Function_25_3E78")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0149
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K何を占う？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "２人の相性を占う\x01",      # 0
            "エリィに任せる\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4737")

    #C0150
    ChrTalk(
        0x101,
        (
            "#00000F#6P俺たちの相性を\x01",
            "占ってもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x16,
        "#5Pええ、お安い御用よ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0152
    NpcTalk(
        0x15,
        "エリィ",
        "#00112F#12Pロ、ロイド……！？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0153
    ChrTalk(
        0x101,
        (
            "#00009F#6Pいや、折角２人で来たんだし\x01",
            "こういう機会もなかなかないしさ。\x02\x03",

            "#00000Fお試し程度にやってみないか？\x02",
        )
    )

    CloseMessageWindow()

    #N0154
    NpcTalk(
        0x15,
        "エリィ",
        "#00106F#12Pお、お試し程度ってあなたねえ……\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        (
            "#00005F#6Pえっと……なにかマズかったか？\x02\x03",

            "#00003Fそんなに嫌ならやめておくけど……\x02",
        )
    )

    CloseMessageWindow()

    #N0156
    NpcTalk(
        0x15,
        "エリィ",
        (
            "#00105F#12Pイ、イヤってわけじゃ……\x02\x03",

            "#00113Fもう、あなたって人はどうしてこう……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0157
    NpcTalk(
        0x15,
        "エリィ",
        (
            "#00111F#12P……はあ、なんでもないわ。\x02\x03",

            "#00100Fすみません、相性占いを\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0158
    ChrTalk(
        0x16,
        "#5Pふふ、それでは…………\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0160
    NpcTalk(
        0x15,
        "エリィ",
        "#00101F#12P（ゴクリ……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0161
    ChrTalk(
        0x16,
        (
            "#5Pまっすぐな目をした青年と\x01",
            "勤勉で包容力に溢れる才女……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x16,
        (
            "#5P同じ目的を持つ仲間として\x01",
            "共に数々の苦難を乗り越え、\x01",
            "固い絆で結ばれている……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_4388")
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0163
    ChrTalk(
        0x16,
        (
            "#5Pあら……しかも以前、\x01",
            "何らかの極限状態に陥ったことで\x01",
            "それは大きく進展したようね。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x16,
        (
            "#5Pまだ決定的ではないけど、\x01",
            "このまま想いを育めば、\x01",
            "いずれは深い仲になれるはずよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4413")

    label("loc_4388")


    #C0165
    ChrTalk(
        0x16,
        (
            "#5P生まれは違えど、\x01",
            "互いの長所を認めて\x01",
            "補い合える関係……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x16,
        (
            "#5Pこのまま想いを育めば、\x01",
            "いずれは深い仲に\x01",
            "なれるかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4413")

    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0167
    ChrTalk(
        0x16,
        "#5P……私に見えたのはこんな所かしら。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #N0168
    NpcTalk(
        0x15,
        "エリィ",
        "#00112F#12Pふ、深い仲って……！？\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x16,
        (
            "#5Pふふ、さて……\x01",
            "それを言ってしまうのは\x01",
            "野暮というものでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x16,
        (
            "#5Pただ、鍵を握るのは\x01",
            "貴方の今後の行動と選択……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        "#00005F#6Pお、俺ですか？\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x16,
        (
            "#5P少なくとも、相手の気持ちを\x01",
            "察する努力は心がけることね。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x16,
        (
            "#5P貴方には、無意識のうちに\x01",
            "周囲を魅了してしまう魔性──\x01",
            "その暗示が見られるから。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0174
    ChrTalk(
        0x101,
        "#00012F#6Pま、魔性って……\x02",
    )

    CloseMessageWindow()

    #N0175
    NpcTalk(
        0x15,
        "エリィ",
        "#00106F#12P（かなり当たってる気がする……）\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x16,
        (
            "#5Pただ、占いはあくまで\x01",
            "占いであって予言ではない……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x16,
        (
            "#5P『運命』とは因果律の元に\x01",
            "常に移ろいゆくものだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x16,
        (
            "#5P今後のあなた達の行動次第で\x01",
            "いくらでも変わりうる……\x01",
            "それを覚えておきなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#00000F#6Pは、はい。\x01",
            "肝に銘じさせていただきます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DFC")

    label("loc_4737")

    SetChrSubChip(0x101, 0x2)

    #C0180
    ChrTalk(
        0x101,
        (
            "#00000F#6Pエリィ、\x01",
            "何か占いたい事はないか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0181
    NpcTalk(
        0x15,
        "エリィ",
        (
            "#00105F#12Pあら、私が決めていいの？\x02\x03",

            "#00103Fうーん、そうねえ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0182
    NpcTalk(
        0x15,
        "エリィ",
        (
            "#00100F#12Pそれなら……\x01",
            "クロスベル自治州の今後を\x01",
            "占ってもらってはどうかしら？\x02\x03",

            "#00103F独立提唱が為されたことで\x01",
            "どうなっていくか……\x01",
            "気になると思わない？\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        "#00003F#6Pああ、確かにな。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0184
    ChrTalk(
        0x101,
        (
            "#00000F#6P……それじゃあ、\x01",
            "お願いしてもいいですか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #C0185
    ChrTalk(
        0x16,
        "#5Pふふ、お安い御用よ。\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0187
    NpcTalk(
        0x15,
        "エリィ",
        "#00101F#12P（ゴクリ……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0188
    ChrTalk(
        0x16,
        (
            "#5P……近いうちに、あなた達は\x01",
            "とても大きな因果に巻き込まれる……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x16,
        (
            "#5P今までに見たこともないような\x01",
            "巨大な《壁》と相対する絶望……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x16,
        "#5Pそれを味わう事になる。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0191
    ChrTalk(
        0x101,
        "#00005F#6Pえ……！？\x02",
    )

    CloseMessageWindow()

    #N0192
    NpcTalk(
        0x15,
        "エリィ",
        "#00105F#12Pそ、それって……？\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x16,
        "#5P……それが何かは分からない。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x16,
        (
            "#5Pだけれどその足音は、\x01",
            "着実にあなた達に近づいている……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0195
    ChrTalk(
        0x16,
        "#5P……私に見えたのはここまでよ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x15)

    #N0196
    NpcTalk(
        0x15,
        "エリィ",
        "#00103F#12P……い、今のは一体……？\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#00003F#6P巨大な《壁》……\x01",
            "それに相対する絶望……\x02\x03",

            "#00008Fまさか、市長の\x01",
            "独立提唱の関係で何かが……？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x16,
        "#5P……詳しくは分からないわ。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x16,
        (
            "#5P私の占いはあくまで、出た暗示を\x01",
            "私なりに読み解くまでのものだから。\x02",
        )
    )

    CloseMessageWindow()

    #N0200
    NpcTalk(
        0x15,
        "エリィ",
        (
            "#00106F#12Pうーん、気になるけど……\x01",
            "今は気にかけておくしかないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x16,
        (
            "#5Pどうやら、余計な心配を\x01",
            "煽ってしまったようね。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x16,
        (
            "#5Pただ、占いはあくまで\x01",
            "占いであって予言ではない……\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x16,
        (
            "#5P『運命』とは因果律の元に\x01",
            "常に移ろいゆくものだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x16,
        (
            "#5P今後のあなた達の行動次第で\x01",
            "いくらでも変わりうる……\x01",
            "それを覚えておきなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        "#00000F#6P……はい、肝に銘じさせていただきます。\x02",
    )

    CloseMessageWindow()

    label("loc_4DFC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_25_3E78 end

    def Function_26_4E08(): pass

    label("Function_26_4E08")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0206
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K何を占う？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "２人の相性を占う\x01",      # 0
            "ティオに任せる\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5687")

    #C0207
    ChrTalk(
        0x101,
        (
            "#00000F#6P俺たちの相性を\x01",
            "占ってもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x16,
        "#5Pええ、お安い御用よ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0209
    ChrTalk(
        0x101,
        (
            "#00000F#6P……ってことだけど、どうかな？\x01",
            "折角来たんだし、試しにさ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0210
    NpcTalk(
        0x15,
        "ティオ",
        (
            "#00203F#12P……ふむ、面白そうですね。\x02\x03",

            "#00200Fどんな結果が出るにしろ、\x01",
            "わたしも今後の身の振り方を\x01",
            "考える事ができそうですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x101,
        "#00006F#6P……よく意味が分かんないんだが。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #N0212
    NpcTalk(
        0x15,
        "ティオ",
        (
            "#00203F#12Pいえ、別に分からなくて結構です。\x02\x03",

            "#00200Fそれでは、占いをお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0213
    ChrTalk(
        0x16,
        "#5Pふふ、それじゃあ…………\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0215
    NpcTalk(
        0x15,
        "ティオ",
        (
            "#00205F#12P（……不思議なオーラを知覚……\x01",
            "  これは一体……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0216
    ChrTalk(
        0x16,
        (
            "#5Pまっすぐな目をした青年と\x01",
            "卓越した能力を秘める少女……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x16,
        (
            "#5P年齢は離れてるけど、\x01",
            "ごく対等な仲間同士として\x01",
            "互いを信頼し合っている……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_5297")
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0218
    ChrTalk(
        0x16,
        (
            "#5Pあら……しかも以前、\x01",
            "何らかの極限状態に陥ったことで\x01",
            "それは大きく進展したようね。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x16,
        (
            "#5P色々と壁はあると思うけど、\x01",
            "深い仲になる可能性はかなり高い\x01",
            "という暗示が出ているわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5326")

    label("loc_5297")


    #C0220
    ChrTalk(
        0x16,
        (
            "#5P生まれは違えど、\x01",
            "互いの長所を認めて\x01",
            "補い合える関係……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x16,
        (
            "#5P色々と壁はあると思うけど、\x01",
            "深い仲になる可能性は\x01",
            "充分にあるでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5326")

    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0222
    ChrTalk(
        0x16,
        "#5P……私に見えたのはこんな所かしら。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)

    #N0223
    NpcTalk(
        0x15,
        "ティオ",
        "#00204F#12Pふむ……面白い結果が出ましたね。\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#00012F#6Pあの、俺はよく意味が……\x02\x03",

            "#00000F『色々な壁』っていうのは\x01",
            "その、一体何のことを……？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x16,
        (
            "#5Pふふ、言ってしまえば\x01",
            "社会的な禁忌や他人の視線……\x01",
            "そんなところね。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x16,
        (
            "#5Pそれを乗り越える覚悟が\x01",
            "貴方にあるなら、あるいは……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#00005F#6Pえっと……？\x01",
            "覚悟も何も……\x02\x03",

            "#00003Fティオと親交を深めるのに、\x01",
            "別に他人の視線なんか\x01",
            "気にならないですし……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0228
    NpcTalk(
        0x15,
        "ティオ",
        "#00211F#12P……何気に爆弾発言ですね。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        "#00005F#6Pへっ……\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x16,
        "#5Pふふ、なかなか面白い人ね。\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x16,
        (
            "#5Pその性格が将来、\x01",
            "多くの災いを招かないことを\x01",
            "女神に祈るばかりだけれど。\x02",
        )
    )

    CloseMessageWindow()

    #N0232
    NpcTalk(
        0x15,
        "ティオ",
        "#00206F#12Pええ、全くその通りです。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0233
    ChrTalk(
        0x101,
        (
            "#00006F#6Pあ、あの……\x01",
            "俺を置いてけぼりにして\x01",
            "話をしないでくれないかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CF7")

    label("loc_5687")

    SetChrSubChip(0x101, 0x2)

    #C0234
    ChrTalk(
        0x101,
        (
            "#00000F#6Pティオ、\x01",
            "何か占いたいことはないか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0235
    NpcTalk(
        0x15,
        "ティオ",
        (
            "#00205F#12Pわたしが決めてもいいんですか？\x02\x03",

            "#00203F……そうですね……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0236
    NpcTalk(
        0x15,
        "ティオ",
        (
            "#00200F#12Pわたしとみっしぃとの相性、\x01",
            "というのを占ってもらえませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0237
    ChrTalk(
        0x101,
        "#00005F#6Pみ、みっしぃとの相性……？\x02",
    )

    CloseMessageWindow()

    #N0238
    NpcTalk(
        0x15,
        "ティオ",
        (
            "#00202F#12Pええ、今後もみっしぃと\x01",
            "触れ合って生きていけるか……\x01",
            "是非占っていただきたいです。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0239
    ChrTalk(
        0x16,
        (
            "#5Pふむ、なかなかユニークね。\x01",
            "……いいでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0241
    NpcTalk(
        0x15,
        "ティオ",
        (
            "#00205F#12P（……不思議なオーラを知覚……\x01",
            "  これは一体……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0242
    ChrTalk(
        0x16,
        (
            "#5P……あなたとみっしぃの相性は……\x01",
            "どうやらかなりいいようね。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x16,
        (
            "#5Pあなたが愛する限り、\x01",
            "みっしぃは必ず応えてくれるはず。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x16,
        (
            "#5Pこの先も、数々のみっしぃグッズや\x01",
            "テーマパークでのふれあいが待っている……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0245
    ChrTalk(
        0x16,
        "#5P……私に見えたのはこんな所かしら。\x02",
    )

    CloseMessageWindow()

    #N0246
    NpcTalk(
        0x15,
        "ティオ",
        "#00202F#12Pふふ、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0247
    ChrTalk(
        0x101,
        (
            "#00012F#6Pま、まあ、よかったな。\x01",
            "みっしぃは必ず応えてくれるってさ。\x02",
        )
    )

    CloseMessageWindow()

    #N0248
    NpcTalk(
        0x15,
        "ティオ",
        (
            "#00204F#12Pええ、ファンとして\x01",
            "これ以上のことはありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x16,
        "#5Pああ、それともう一つ。\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x16,
        (
            "#5P近いうちに、あなたの\x01",
            "みっしぃへの想いを試す、\x01",
            "大きな試練が訪れる……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x16,
        (
            "#5Pそんな暗示も出ているわ。\x01",
            "……せいぜい気をつけることね。\x02",
        )
    )

    CloseMessageWindow()

    #N0252
    NpcTalk(
        0x15,
        "ティオ",
        (
            "#00200F#12P……望む所です。\x02\x03",

            "#00201Fどんな試練が訪れようと、\x01",
            "このみっしぃへの愛を\x01",
            "揺るがすことなどできない……\x02\x03",

            "#00204Fそれを証明してみせましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x16,
        "#5Pふふ、応援しているわ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0254
    ChrTalk(
        0x101,
        (
            "#00006F#6P（ダ、ダメだ。\x01",
            "  つっこみ所が多すぎて\x01",
            "  処理しきれないっ……！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CF7")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_26_4E08 end

    def Function_27_5D03(): pass

    label("Function_27_5D03")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0255
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K何を占う？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "２人の相性を占う\x01",      # 0
            "ランディに任せる\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6566")

    #C0256
    ChrTalk(
        0x101,
        (
            "#00000F#6P俺たちの相性を\x01",
            "占ってもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x16,
        "#5Pええ、お安い御用よ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x15, 0x1)

    #N0258
    NpcTalk(
        0x15,
        "ランディ",
        (
            "#00306F#12Pお前なあ……そういうのは、\x01",
            "気になってる子とでもしろよ。\x02\x03",

            "#00301F野郎同士の相性を調べて\x01",
            "何が楽しいんだっつーの。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0259
    ChrTalk(
        0x101,
        (
            "#00009F#6Pはは、まあいいじゃないか。\x02\x03",

            "#00000Fそれに相性って言っても、\x01",
            "男友達との相性とかもあるだろ？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #N0260
    NpcTalk(
        0x15,
        "ランディ",
        (
            "#00306F#12Pんー……まあいいんだけどよ。\x02\x03",

            "#00300Fそんじゃお姉さん、よろしく頼むッス。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0261
    ChrTalk(
        0x16,
        "#5Pふふ、分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0263
    NpcTalk(
        0x15,
        "ランディ",
        "#00305F#12P（おおっ……本格的じゃねえか。）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0264
    ChrTalk(
        0x16,
        (
            "#5Pまっすぐな目をした青年と\x01",
            "情熱を内に秘めた青年……\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x16,
        (
            "#5P求心力として常に先頭に立ち、\x01",
            "その快活さを以って仲間を励まし\x01",
            "導いてきた心強い仲間……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_6191")
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0266
    ChrTalk(
        0x16,
        (
            "#5Pあら……しかも以前、\x01",
            "何らかの極限状態に陥ったことで\x01",
            "それは大きく深まったみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x16,
        (
            "#5Pこれから互いの理解を深め、\x01",
            "高めあっていくことで\x01",
            "更に固い絆が結ばれるでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_6226")

    label("loc_6191")


    #C0268
    ChrTalk(
        0x16,
        (
            "#5P生まれは違えど、\x01",
            "互いの長所を認めて\x01",
            "補い合える関係……\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x16,
        (
            "#5Pこれから互いの理解を深め、\x01",
            "高めあっていくことで\x01",
            "固い絆が結ばれるでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6226")

    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0270
    ChrTalk(
        0x16,
        "#5P……私に見えたのはこんな所かしら。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #N0271
    NpcTalk(
        0x15,
        "ランディ",
        (
            "#00305F#12Pおおっ……なんだか\x01",
            "よさげな結果じゃねーか。\x02\x03",

            "#00304Fお嬢、ティオすけ、\x01",
            "そしてノエル……悪いな。\x02\x03",

            "#00302Fどうやらロイドは\x01",
            "俺様のモノになっちまいそうだ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0272
    ChrTalk(
        0x101,
        (
            "#00006F#6P……不穏な事を\x01",
            "口走るのはやめてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x16,
        (
            "#5Pそうね、そこまでの仲になるという\x01",
            "暗示は今の所出ていなかったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0274
    ChrTalk(
        0x16,
        (
            "#5Pただ、運命というものは\x01",
            "あなた達が強く望むなら\x01",
            "変わっていくもの……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x16,
        (
            "#5P今後一切そういうことが\x01",
            "ありえないかと問われると、\x01",
            "私も否定することはできないわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0276
    ChrTalk(
        0x101,
        (
            "#00012F#6Pあ、あの、出来れば\x01",
            "否定して欲しいんですけど。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0277
    NpcTalk(
        0x15,
        "ランディ",
        (
            "#00309F#12Pはは、照れるな照れるな。\x02\x03",

            "#00304Fお前が望むなら、\x01",
            "俺も頼れるアニキとして──\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0278
    ChrTalk(
        0x101,
        (
            "#00011F#6P照れとかじゃないからっ！！\x02\x03",

            "#00006Fはあ、ほんと勘弁してくれ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C86")

    label("loc_6566")

    SetChrSubChip(0x101, 0x2)

    #C0279
    ChrTalk(
        0x101,
        (
            "#00000F#6Pランディ、\x01",
            "何か占いたいことはないか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0280
    NpcTalk(
        0x15,
        "ランディ",
        (
            "#00305F#12Pん、俺が決めていいのか？\x02\x03",

            "#00303Fそうだなあ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0281
    NpcTalk(
        0x15,
        "ランディ",
        (
            "#00309F#12Pんー、だったら……\x01",
            "今後の俺のナンパ運でも\x01",
            "占ってもらえるッスか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0282
    ChrTalk(
        0x101,
        "#00006F#6Pそ、それでいいのか……？\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x16,
        (
            "#5P要するに、あなたが声をかけて\x01",
            "見知らぬ女性が誘いに乗る可能性……\x01",
            "ということでいいかしら？\x02",
        )
    )

    CloseMessageWindow()

    #N0284
    NpcTalk(
        0x15,
        "ランディ",
        "#00309F#12Pそれでよろしくお願いするッス！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0285
    ChrTalk(
        0x16,
        "#5Pふふ、お安い御用よ。\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0287
    NpcTalk(
        0x15,
        "ランディ",
        "#00305F#12P（おおっ……本格的じゃねえか。）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0288
    ChrTalk(
        0x16,
        (
            "#5P……貴方のナンパとやら……\x01",
            "成功の可能性はおおよそ、\x01",
            "五分五分と言った所ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x16,
        (
            "#5P持ち前の明るさと端正な顔立ちを\x01",
            "魅力に感じる女性は多いようだけど……\x01",
            "やはり警戒されることも多いはず。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x16,
        (
            "#5Pちなみに成功したとしても\x01",
            "貴方の場合、真実の愛に至る割合は\x01",
            "ほぼゼロと言っていいでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0291
    NpcTalk(
        0x15,
        "ランディ",
        "#00306F#12P#4Sガーン！！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0292
    ChrTalk(
        0x16,
        "#5P……私に見えたのはこんな所かしら。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0293
    NpcTalk(
        0x15,
        "ランディ",
        (
            "#00306F#12Pロ、ロイド……\x01",
            "俺はもうダメだ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0294
    ChrTalk(
        0x101,
        (
            "#00012F#6Pま、まあまあ……\x01",
            "そう気を落とすなよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x16,
        (
            "#5Pふふ、そうね。\x01",
            "アドバイスをするなら……\x01",
            "身近な所にある愛を逃さないこと。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x16,
        (
            "#5Pとても身近に、貴方のことを\x01",
            "大事に想っている異性がいる……\x01",
            "そんな暗示も出ていたわ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    #N0297
    NpcTalk(
        0x15,
        "ランディ",
        "#00305F#12Pマ、マジッスか！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)

    #C0298
    ChrTalk(
        0x101,
        (
            "#00000F#6Pそれってもしかして……\x01",
            "警備隊のミレ──\x02",
        )
    )

    CloseMessageWindow()

    #N0299
    NpcTalk(
        0x15,
        "ランディ",
        (
            "#00303F#12P──よっしゃ！　そうと決まれば……\x02\x03",

            "#00309F俺を大事に想っているっつう\x01",
            "カワイコちゃんが見つかるまで、\x01",
            "とことんナンパに励むしかねえな！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)

    #C0300
    ChrTalk(
        0x101,
        "#00006F#6Pな、なんでそうなるんだよ……\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x16,
        (
            "#5P（……気づかないフリ、かしら。\x01",
            "  ふふ、私には関係ないけれど。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C86")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_27_5D03 end

    def Function_28_6C92(): pass

    label("Function_28_6C92")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0302
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K何を占う？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "２人の相性を占う\x01",      # 0
            "ノエルに任せる\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_747D")

    #C0303
    ChrTalk(
        0x101,
        (
            "#00000F#6P俺たちの相性を\x01",
            "占ってもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x16,
        "#5Pええ、お安い御用よ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x15, 0x1)

    #N0305
    NpcTalk(
        0x15,
        "ノエル",
        "#10105F#12Pロ、ロイドさんっ！？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0306
    ChrTalk(
        0x101,
        (
            "#00009F#6Pはは、まあ折角だから\x01",
            "試しにどうかと思ってさ。\x02\x03",

            "#00000F迷惑だったらやめとくけど……\x02",
        )
    )

    CloseMessageWindow()

    #N0307
    NpcTalk(
        0x15,
        "ノエル",
        (
            "#10111F#12Pい、いえ！！\x01",
            "迷惑とかそういうのじゃ\x01",
            "ないんですけど……\x02\x03",

            "#10116F（というか、これも天然で\x01",
            "  言ってるんでしょうか……）\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x101,
        "#00005F#6Pえっと、どうした？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #N0309
    NpcTalk(
        0x15,
        "ノエル",
        (
            "#10106F#12Pな、何でもありません。\x02\x03",

            "#10100F……えっとそれじゃあ、\x01",
            "占いの方をお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0310
    ChrTalk(
        0x16,
        "#5Pふふ、承りましょう。\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0312
    NpcTalk(
        0x15,
        "ノエル",
        "#10105F#12P（わっ……何かの術……？）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0313
    ChrTalk(
        0x16,
        (
            "#5Pまっすぐな目をした青年と\x01",
            "実直なる意志を瞳に秘めた娘……\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x16,
        (
            "#5P所属は違えど、何かを守るという\x01",
            "同じ目的において協力しあう中で、\x01",
            "強い信頼を築いてきた関係……\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x16,
        (
            "#5Pどちらかが一歩踏み出して\x01",
            "深い部分に立ち入れば、\x01",
            "より親密になっていけるはずよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0316
    ChrTalk(
        0x16,
        "#5P……私に見えたのはこんな所かしら。\x02",
    )

    CloseMessageWindow()

    #N0317
    NpcTalk(
        0x15,
        "ノエル",
        (
            "#10105F#12P一歩踏み出す……ですか。\x01",
            "結構苦手な部分ではあるんですよね。\x02\x03",

            "#10106Fどうも一線を引いちゃうというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x16,
        (
            "#5Pふふ、見たところ\x01",
            "貴女は慎重なタイプのようだし\x01",
            "仕方ないとは思うけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x16,
        (
            "#5P多少は積極的にならないと\x01",
            "手に入るものですら\x01",
            "逃してしまうのではなくて？\x02",
        )
    )

    CloseMessageWindow()

    #N0320
    NpcTalk(
        0x15,
        "ノエル",
        (
            "#10103F#12Pた、確かにそのフシは\x01",
            "あるかもしれませんけど……\x02\x03",

            "#10101F……でも、そうですね。\x01",
            "あたしもいざという時は\x01",
            "勇気を出してみるしかっ……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0321
    ChrTalk(
        0x101,
        (
            "#00012F#6Pえ、えっと、ノエル？\x01",
            "ちょっと真剣になりすぎじゃ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0322
    NpcTalk(
        0x15,
        "ノエル",
        (
            "#10105F#12Pはっ……\x02\x03",

            "#10106F……そ、そうですよね。\x01",
            "どうせお試しですし……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #N0323
    NpcTalk(
        0x15,
        "ノエル",
        (
            "#10105F#12P……っていや！\x01",
            "別に残念に思ってるとか、\x01",
            "そういうんじゃなくて……！\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x101,
        (
            "#00006F#6Pわ、分かってるから\x01",
            "ちょっと落ち着いてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x16,
        "#5P（ふふ、意外といいコンビに見えるけど。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AD3")

    label("loc_747D")

    SetChrSubChip(0x101, 0x2)

    #C0326
    ChrTalk(
        0x101,
        (
            "#00000F#6Pノエル、\x01",
            "何か占いたいことはないか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0327
    NpcTalk(
        0x15,
        "ノエル",
        (
            "#10105F#12Pあたしが決めていいんですか？\x02\x03",

            "#10103Fうーん、そうですねー……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0328
    NpcTalk(
        0x15,
        "ノエル",
        (
            "#10100F#12Pそれじゃあ、\x01",
            "今後の警備隊の行く末……\x01",
            "なんてどうでしょうか。\x02\x03",

            "#10104F私もいずれ警備隊に戻りますし、\x01",
            "そうなった時の心構えを\x01",
            "しておきたいというか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0329
    ChrTalk(
        0x101,
        (
            "#00002F#6Pああ、いいんじゃないか？\x02\x03",

            "#00000Fえっと、それじゃあ\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x16,
        "#5Pええ、お安い御用よ。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0332
    NpcTalk(
        0x15,
        "ノエル",
        "#10105F#12P（わっ……何かの術……？）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0333
    ChrTalk(
        0x16,
        "#5P……これは、変革の暗示ね。\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x16,
        (
            "#5Pそう遠くないうちに、\x01",
            "貴女の所属する組織は\x01",
            "なんらかの変化を遂げる……\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x16,
        (
            "#5Pその時、貴女は何か大きな決断を\x01",
            "迫られる事になるでしょう……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0336
    ChrTalk(
        0x16,
        "#5P……私に見えたのはこんな所かしら。\x02",
    )

    CloseMessageWindow()

    #N0337
    NpcTalk(
        0x15,
        "ノエル",
        (
            "#10103F#12P変革……それに決断ですか。\x02\x03",

            "#10101Fあの、それって一体どういう……？\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x16,
        (
            "#5P残念だけれど、現時点では\x01",
            "それははっきりとは見えないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x16,
        (
            "#5P良くも悪くも、今後の動向次第\x01",
            "と言ったところでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x101,
        (
            "#00003F#6Pうーん、確かに今の時点だと\x01",
            "どうとでも言えてしまいそうだ。\x02\x03",

            "#00000F独立提唱の結果次第で、\x01",
            "警備隊のありかたというのも\x01",
            "変わってきそうだしな。\x02",
        )
    )

    CloseMessageWindow()

    #N0341
    NpcTalk(
        0x15,
        "ノエル",
        (
            "#10100F#12P警備隊にとってそれが\x01",
            "進化か、あるいは衰退か……\x02\x03",

            "#10103F願わくば、それが進化で\x01",
            "あって欲しいものですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x16,
        "#5P私の方から言えるのは一つ……\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x16,
        (
            "#5P後にも先にも、\x01",
            "後悔しない決断をすることね。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x16,
        (
            "#5P占いはあくまでただの占い……\x01",
            "貴女の決意のあり方一つで、\x01",
            "いくらでも未来は変わるのだから。\x02",
        )
    )

    CloseMessageWindow()

    #N0345
    NpcTalk(
        0x15,
        "ノエル",
        (
            "#10100F#12Pええ、そうですね……\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AD3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_28_6C92 end

    def Function_29_7ADF(): pass

    label("Function_29_7ADF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0346
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K何を占う？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "２人の相性を占う\x01",      # 0
            "ワジに任せる\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8179")

    #C0347
    ChrTalk(
        0x101,
        (
            "#00000F#6P俺たちの相性を\x01",
            "占ってもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x16,
        "#5Pええ、お安い御用よ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0349
    NpcTalk(
        0x15,
        "ワジ",
        (
            "#10302F#12Pフフ、珍しいじゃないか。\x01",
            "君のほうからアプローチを\x01",
            "かけてくれるなんてさ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0350
    ChrTalk(
        0x101,
        (
            "#00003F#6Pい、いや、\x01",
            "そういうんじゃないんだが。\x02\x03",

            "#00000F折角こういうところに来たんだし、\x01",
            "試しにどうかと思ってさ。\x02",
        )
    )

    CloseMessageWindow()

    #N0351
    NpcTalk(
        0x15,
        "ワジ",
        "#10309F#12Pフフ、照れなくてもいいのに。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0352
    ChrTalk(
        0x101,
        "#00006F#6P……と、とにかく、お願いします。\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x16,
        "#5Pふふ、いいでしょう。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #C0354
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x16)

    #C0355
    ChrTalk(
        0x16,
        "#5P（……なるほど……）\x02",
    )

    CloseMessageWindow()

    #N0356
    NpcTalk(
        0x15,
        "ワジ",
        (
            "#10309F#12Pフフ、どうかしたのかな？\x01",
            "占い師のお姉さん。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x16,
        "#5P……ふふ、何でもないわ。\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        "#00005F#6P……？\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x16,
        (
            "#5Pまっすぐな目をした青年と\x01",
            "軽妙に世を渡り歩く少年……\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x16,
        (
            "#5P正反対の性格でありながら\x01",
            "互いの優秀な点を認め合うことで、\x01",
            "確かな信頼を築いている……\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x16,
        (
            "#5P信頼が深まり、過去も現在も\x01",
            "含めて許容し合えるようになれば、\x01",
            "固い絆が結ばれるでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0362
    ChrTalk(
        0x16,
        "#5P……私に見えたのはこんな所かしら。\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        (
            "#00005F#6P過去も現在も含めて……\x02\x03",

            "#00003F……確かにワジからは、\x01",
            "あまり昔の話を聞いたことが\x01",
            "なかったかな。\x02",
        )
    )

    CloseMessageWindow()

    #N0364
    NpcTalk(
        0x15,
        "ワジ",
        (
            "#10309F#12Pフフ、やだなあ。\x01",
            "これでもなにもかもを\x01",
            "包み隠さず話してるんだけど。\x02\x03",

            "#10304Fそれに、多少の秘密があるほうが\x01",
            "色々と燃えると思わない？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0365
    ChrTalk(
        0x101,
        (
            "#00006F#6Pやっぱり何か秘密に\x01",
            "してるんじゃないか……\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x16,
        "#5Pふふ、まあ根気強く付き合うことね。\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x16,
        (
            "#5Pこの手のタイプは、\x01",
            "なかなか本音を見せないから。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0368
    NpcTalk(
        0x15,
        "ワジ",
        (
            "#10304F#12Pフフ、だってさ。\x02\x03",

            "#10309F是非とも根気強くアプローチを\x01",
            "かけてくれると、僕も嬉しいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0369
    ChrTalk(
        0x101,
        "#00006F#6Pやれやれ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8653")

    label("loc_8179")

    SetChrSubChip(0x101, 0x2)

    #C0370
    ChrTalk(
        0x101,
        (
            "#00000F#6Pワジ、\x01",
            "何か占いたいことはないか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0371
    NpcTalk(
        0x15,
        "ワジ",
        (
            "#10305F#12Pおや、僕が決めていいのかい？\x02\x03",

            "#10304Fそうだね……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0372
    NpcTalk(
        0x15,
        "ワジ",
        (
            "#10300F#12Pだったら……\x01",
            "こういうのはどうかな？\x02\x03",

            "#10304Fこの地で、僕の望むものが\x01",
            "手に入るかどうか……\x01",
            "それを占って欲しいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x101,
        "#00005F#6Pワジが望むもの……？\x02",
    )

    CloseMessageWindow()

    #N0374
    NpcTalk(
        0x15,
        "ワジ",
        (
            "#10304F#12Pフフ、それは秘密さ。\x02\x03",

            "#10300Fどうだい、お姉さん。\x01",
            "そういった占いは可能かな？\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x16,
        (
            "#5Pふふ、面白いわ。\x01",
            "……やってみましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0376
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x16)

    #C0377
    ChrTalk(
        0x16,
        "#5P（……なるほど……）\x02",
    )

    CloseMessageWindow()

    #N0378
    NpcTalk(
        0x15,
        "ワジ",
        (
            "#10309F#12Pフフ、どうかしたのかな？\x01",
            "占い師のお姉さん。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x16,
        "#5P……ふふ、何でもないわ。\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x101,
        "#00005F#6P……？\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x16,
        "#5Pあなたが探し求める物……\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x16,
        (
            "#5Pそれはすぐ近くにあるけれど、\x01",
            "今は決して手が届くことはない。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x16,
        (
            "#5P今はただ時を待つべし……\x01",
            "そういう暗示が出ているわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0384
    ChrTalk(
        0x16,
        "#5P……私に見えたのはこんな所かしら。\x02",
    )

    CloseMessageWindow()

    #N0385
    NpcTalk(
        0x15,
        "ワジ",
        (
            "#10304F#12P……なるほどね。\x01",
            "それだけ分かれば十分だよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)

    #C0386
    ChrTalk(
        0x101,
        (
            "#00006F#6P何が何だか、\x01",
            "全然分からないんだが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0387
    NpcTalk(
        0x15,
        "ワジ",
        (
            "#10300F#12Pフフ、今はそれでいいじゃない。\x02\x03",

            "#10304Fそれに、多少の秘密があるほうが\x01",
            "色々と燃えると思わない？\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x101,
        "#00006F#6Pはあ、まったく……\x02",
    )

    CloseMessageWindow()

    label("loc_8653")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_29_7ADF end

    def Function_30_865F(): pass

    label("Function_30_865F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0389
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K何を占う？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "２人の相性を占う\x01",      # 0
            "キーアに任せる\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CF0")

    #C0390
    ChrTalk(
        0x101,
        (
            "#00000F#6P俺たちの相性を\x01",
            "占ってもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x16,
        "#5Pええ、お安い御用よ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0392
    NpcTalk(
        0x15,
        "キーア",
        (
            "#01110F#12Pロイドー、『相性』って\x01",
            "お似合いかどうかってことだよね？\x02\x03",

            "#01109Fキーア、ロイドと\x01",
            "お似合いだといいなー。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0393
    ChrTalk(
        0x101,
        (
            "#00009F#6Pはは、そうだな。\x01",
            "俺もそうだと嬉しいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0394
    ChrTalk(
        0x101,
        (
            "#00000F#6P……えっとそれじゃあ、\x01",
            "占いをお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x16,
        "#5Pふふ、分かったわ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #C0396
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0397
    NpcTalk(
        0x15,
        "キーア",
        "#01110F#12P（わあっ、なんだかキレー……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0398
    ChrTalk(
        0x16,
        (
            "#5Pまっすぐな目をした青年と\x01",
            "その笑顔にて光をもたらす少女……\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x16,
        (
            "#5P彼女の存在が貴方達に勇気を与え、\x01",
            "貴方達は彼女を護るという\x01",
            "強固な意志を以って絆を結ぶ……\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x16,
        (
            "#5P貴方達が彼女を護る限り、\x01",
            "決して絆は解ける事はないでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0401
    ChrTalk(
        0x16,
        "#5P……私に見えたのはこんな所かしら。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)

    #N0402
    NpcTalk(
        0x15,
        "キーア",
        (
            "#01106F#12P……キーア、\x01",
            "ちょっとガッカリかも。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0403
    ChrTalk(
        0x101,
        (
            "#00005F#6Pえ、どうしてだ？\x01",
            "いい結果が出たじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #N0404
    NpcTalk(
        0x15,
        "キーア",
        (
            "#01108F#12Pんー……そーだけど、\x01",
            "ちょっとちがうっていうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0405
    ChrTalk(
        0x16,
        (
            "#5P……ふふ、お嬢ちゃん。\x01",
            "この占いが全てではないのだから、\x01",
            "嘆く必要など何もないわ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0406
    ChrTalk(
        0x16,
        (
            "#5Pそれに、今は雛と親鳥のような\x01",
            "関係だったとしても……\x01",
            "雛はいずれ大きくなる。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x16,
        (
            "#5Pそして……親鳥は気づくのよ。\x01",
            "自分の子供が羽ばたけるように\x01",
            "なっているということをね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0408
    NpcTalk(
        0x15,
        "キーア",
        (
            "#01105F#12P……そっかー。\x01",
            "うん、そうだよね。\x02\x03",

            "#01109Fよーし、キーア……\x01",
            "はやくオトナになる！\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x101,
        (
            "#00004F#6Pうーん、よく分からないけど……\x01",
            "元気が出たならよかったかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9415")

    label("loc_8CF0")

    SetChrSubChip(0x101, 0x2)

    #C0410
    ChrTalk(
        0x101,
        (
            "#00000F#6Pキーア、\x01",
            "何か占ってみたいことはないか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0411
    NpcTalk(
        0x15,
        "キーア",
        (
            "#01105F#12Pキーアが決めていいのー？\x02\x03",

            "#01111Fん～、それじゃあ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0412
    NpcTalk(
        0x15,
        "キーア",
        (
            "#01110F#12Pあ、そうだっ！\x01",
            "キーア、ツァイトと\x01",
            "相性を占ってみたいかもー！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0413
    ChrTalk(
        0x16,
        "#5Pツァイト……？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0414
    ChrTalk(
        0x101,
        (
            "#00012F#6Pえ、えーっと……\x01",
            "俺たちの職場で一緒に暮らしてる、\x01",
            "動物……なんですけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0415
    ChrTalk(
        0x16,
        "#5Pふふ、なるほど……\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x16,
        (
            "#5Pいいわ、お嬢ちゃん。\x01",
            "そのツァイトとやらを\x01",
            "連れてきなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x16,
        (
            "#5Pすぐにでも占って\x01",
            "差し上げましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x101,
        "#00011F#6Pええっ！？\x02",
    )

    CloseMessageWindow()

    #N0419
    NpcTalk(
        0x15,
        "キーア",
        (
            "#01110F#12Pホントー！？\x02\x03",

            "#01109Fそれじゃ、連れて来るねー！！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 1500, 0, 101500, 270)
    OP_0D()
    OP_93(0x15, 0xB4, 0x1F4)
    OP_63(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)

    def lambda_8FD1():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8FD1)
    WaitChrThread(0x15, 1)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0420
    ChrTalk(
        0x101,
        (
            "#00012F#6Pす、すみません。\x01",
            "なんだかヘンなことに……\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x16,
        (
            "#5Pふふ、いいわ。\x01",
            "なんだか面白そうだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x101,
        "#00006F#6P（この人も結構変わってるなあ……）\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 630, 50, 101950, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x17, 0x27)
    SetChrSubChip(0x17, 0x0)
    BeginChrThread(0x17, 0, 0, 0)
    SetChrPos(0x17, 2000, 0, 101000, 315)
    FadeToBright(1000, 0)
    OP_0D()

    #C0423
    ChrTalk(
        0x17,
        "#01200F#12Pグルル……ウォン。\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x16,
        "#5Pふふ、それでは…………\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0426
    NpcTalk(
        0x15,
        "キーア",
        "#01110F#12P（わあっ、なんだかキレー……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0427
    ChrTalk(
        0x16,
        (
            "#5Pその笑顔にて光をもたらす少女と、\x01",
            "仲間達を見守りし誇り高き狼……\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x16,
        (
            "#5Pあなた達には気持ちを通じ合わせ、\x01",
            "互いを尊重しあえる絆が見える……\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x16,
        (
            "#5P今後何があろうとも、\x01",
            "狼は貴女を強く見守り続けるでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0430
    ChrTalk(
        0x16,
        "#5P……私に見えたのはこんな所かしら。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x2)

    #N0431
    NpcTalk(
        0x15,
        "キーア",
        (
            "#01100F#12Pツァイト、これからも\x01",
            "一緒にいられそうだねー！\x02\x03",

            "#01109Fえへへ、ツァイトも嬉しいー？\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x17,
        "#01203F#12Pグルル……ウォン。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0433
    ChrTalk(
        0x101,
        (
            "#00012F#6Pはは……ありがとうございます。\x01",
            "無茶なお願いをしてしまったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x16,
        (
            "#5Pふふ、珍しい占いができて\x01",
            "私もいい経験をさせてもらったわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9415")

    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0435
    ChrTalk(
        0x16,
        (
            "#5P（それに……\x01",
            "  興味深い暗示も見ることができた。）\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x16,
        (
            "#5P（これからどうなるかは女神のみぞ知る、\x01",
            "  といった所かしら。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0437
    ChrTalk(
        0x101,
        "#00005F#6P占い師さん……？\x02",
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x16,
        (
            "#5Pふふ……なんでもないわ。\x01",
            "またのお越しを……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_30_865F end

    def Function_31_9528(): pass

    label("Function_31_9528")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0439
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K何を占う？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "２人の相性を占う\x01",      # 0
            "フランに任せる\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BEE")

    #C0440
    ChrTalk(
        0x101,
        (
            "#00000F#6P俺たちの相性を\x01",
            "占ってもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x16,
        "#5Pええ、お安い御用よ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0442
    NpcTalk(
        0x15,
        "フラン",
        (
            "#06405F#12Pおおっ、ロイドさん！\x01",
            "わたしとの相性、\x01",
            "気になっちゃいますか～！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0443
    ChrTalk(
        0x101,
        (
            "#00002F#6Pはは、まあ折角の機会だし\x01",
            "試しにやってみようと\x01",
            "思ったんだけど……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #N0444
    NpcTalk(
        0x15,
        "フラン",
        (
            "#06409F#12Pふふっ、そうですね！\x01",
            "占い師さん、よろしく\x01",
            "お願いします～！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0445
    ChrTalk(
        0x16,
        "#5Pふふ、分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0447
    NpcTalk(
        0x15,
        "フラン",
        (
            "#06405F#12P（わあ～……\x01",
            "  な、なんだかスゴイです～。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0448
    ChrTalk(
        0x16,
        (
            "#5Pまっすぐな目をした青年と\x01",
            "彼らを陰から支える少女……\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x16,
        (
            "#5P何度も共に仕事をする度に\x01",
            "強固な信頼関係が形成され、\x01",
            "絆が結ばれていった……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0450
    ChrTalk(
        0x16,
        (
            "#5Pあら、だけど……\x01",
            "彼女には想い人がいるようね。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x16,
        (
            "#5Pその気持ちが変わらない以上、\x01",
            "そういった関係になることは\x01",
            "まずないでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0452
    ChrTalk(
        0x16,
        "#5P……私に見えたのはこんな所かしら。\x02",
    )

    CloseMessageWindow()

    #N0453
    NpcTalk(
        0x15,
        "フラン",
        (
            "#06409F#12Pおお～……ドンピシャですよ！\x01",
            "さすが、噂に聞く凄腕ですね～！\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x16,
        "#5Pふふ、どういたしまして。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0455
    ChrTalk(
        0x101,
        (
            "#00009F#6Pはは、何となく\x01",
            "想像はついてたけど。\x02\x03",

            "#00000Fえっと、フラン。\x01",
            "参考までに聞いておくけど、\x01",
            "君の想い人っていうのは……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0456
    NpcTalk(
        0x15,
        "フラン",
        "#06409F#12P#4Sモチロン、お姉ちゃんです！！\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x101,
        (
            "#00004F#6Pう～ん、想像通りだな。\x02\x03",

            "#00000Fやっぱりフランに\x01",
            "そういう話が出るのは\x01",
            "まだまだ先っぽいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x16,
        "#5Pふふ、でも逆に考えれば……\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x16,
        (
            "#5P彼女の姉以上の存在になれれば\x01",
            "可能性があるのではなくて？\x02",
        )
    )

    CloseMessageWindow()

    #N0460
    NpcTalk(
        0x15,
        "フラン",
        (
            "#06409F#12Pそうですよ～、\x01",
            "がんばってくださいロイドさん！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0461
    ChrTalk(
        0x101,
        (
            "#00012F#6Pいや、がんばってくださいと\x01",
            "いわれても……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2AF")

    label("loc_9BEE")

    SetChrSubChip(0x101, 0x2)

    #C0462
    ChrTalk(
        0x101,
        (
            "#00000F#6Pフラン、\x01",
            "何か占いたいことはないか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0463
    NpcTalk(
        0x15,
        "フラン",
        (
            "#06405F#12Pあ、わたしに決めさせて\x01",
            "もらえるんですか～？\x02\x03",

            "#06404Fう～ん、そうですね～……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0464
    NpcTalk(
        0x15,
        "フラン",
        (
            "#06405F#12Pああっ、そういえば……！\x02\x03",

            "#06401F占い師さん、バンバンの場所を\x01",
            "見つけ出してくれませんか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x16,
        "#5Pバンバン……？\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x101,
        (
            "#00000F#6Pそれって、フランの大事にしてる\x01",
            "ぬいぐるみじゃなかったっけ……？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0467
    NpcTalk(
        0x15,
        "フラン",
        (
            "#06400F#12Pええ、実は今回のミシュラムにも\x01",
            "連れてこようと思ってたんですけど……\x02\x03",

            "#06406F前日にお母さんが部屋の掃除をした時に\x01",
            "どこかに行っちゃったらしくって、\x01",
            "結局連れて来れなかったんです～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)

    #C0468
    ChrTalk(
        0x101,
        (
            "#00006F#6Pな、なるほど……\x02\x03",

            "#00000Fえっと、お願いできますか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #C0469
    ChrTalk(
        0x16,
        "#5Pふふ、お安い御用よ。\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0471
    NpcTalk(
        0x15,
        "フラン",
        (
            "#06405F#12P（わあ～……\x01",
            "  な、なんだかスゴイです～。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0472
    ChrTalk(
        0x16,
        (
            "#5P失くなったぬいぐるみは……\x01",
            "クマのぬいぐるみかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0473
    NpcTalk(
        0x15,
        "フラン",
        (
            "#06405F#12Pそ、そうです！！\x01",
            "分かるんですか～！？\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x16,
        "#5Pふふ、特徴的だからすぐに分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x16,
        (
            "#5Pあなたのぬいぐるみは、今……\x01",
            "ベッドの下の陰に転がり込んでいる……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #N0476
    NpcTalk(
        0x15,
        "フラン",
        (
            "#06403F#12Pベ、ベッドの下ですか？\x01",
            "おかしいなあ、そこはわたしも\x01",
            "探したんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x16,
        (
            "#5Pおそらく、すぐに思い当たる場所だから\x01",
            "逆に見逃してしまったのでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x16,
        "#5Pよく探せば、必ず見つかるはずよ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #N0479
    NpcTalk(
        0x15,
        "フラン",
        "#06409F#12Pはいっ、ありがとうございます！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0480
    ChrTalk(
        0x101,
        "#00000F#6Pはは、よかったなフラン。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0481
    NpcTalk(
        0x15,
        "フラン",
        (
            "#06406F#12Pええ、ほんとですよ～！\x01",
            "バンバンがいないと、\x01",
            "本当、寂しくなっちゃって。\x02\x03",

            "#06409F明日帰ったら探してみますね～！\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x16,
        "#5Pふふ、お役に立ててなによりだわ。\x02",
    )

    CloseMessageWindow()

    label("loc_A2AF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_31_9528 end

    def Function_32_A2BB(): pass

    label("Function_32_A2BB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0483
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K何を占う？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "２人の相性を占う\x01",      # 0
            "セシルに任せる\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9D9")

    #C0484
    ChrTalk(
        0x101,
        (
            "#00000F#6P俺たちの相性を\x01",
            "占ってもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x16,
        "#5Pええ、お安い御用よ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0486
    NpcTalk(
        0x15,
        "セシル",
        (
            "#05900F#12Pまあ、ロイド……\x02\x03",

            "#05909Fふふ、そんなこと\x01",
            "わざわざ占わなくても、\x01",
            "きっと相性バッチリなのに。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0487
    ChrTalk(
        0x101,
        (
            "#00009F#6Pはは、まあ折角の機会だし\x01",
            "試しにやってみようよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0488
    ChrTalk(
        0x101,
        (
            "#00000F#6P……というわけで、\x01",
            "よろしくおねがいします。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x16,
        "#5Pええ、分かったわ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #C0490
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0491
    NpcTalk(
        0x15,
        "セシル",
        (
            "#05905F#12P（あら……\x01",
            "  なんだか本当に凄そうね。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0492
    ChrTalk(
        0x16,
        (
            "#5Pまっすぐな目をした青年と\x01",
            "慈愛の精神に溢れる女性……\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x16,
        (
            "#5P幼い頃より想いは育まれ、\x01",
            "そこには無二の絆が存在する……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0494
    ChrTalk(
        0x16,
        (
            "#5P……だけど、女性の方には\x01",
            "確かな想いが残っているわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x16,
        (
            "#5P失われた想い人に対する、\x01",
            "強い想いが……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0496
    ChrTalk(
        0x16,
        "#5P……私に見えたのはこんな所かしら。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x15)

    #N0497
    NpcTalk(
        0x15,
        "セシル",
        (
            "#05904F#12P……ふふ、こんなにぴたりと\x01",
            "当てられちゃうなんて。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0498
    ChrTalk(
        0x101,
        (
            "#00006F#6P……ごめん、セシル姉。\x01",
            "こんなこと占ってもらっちゃってさ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0499
    NpcTalk(
        0x15,
        "セシル",
        (
            "#05900F#12Pあら、謝る事なんてないわ。\x01",
            "ロイドと相性がいいみたいなのは\x01",
            "素直に嬉しいし……\x02\x03",

            "#05904Fそれに、ガイさんのことを\x01",
            "忘れずにいられたことを\x01",
            "改めて確認できてよかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x16,
        (
            "#5P……愛する者への想いは、\x01",
            "どんな事があろうと\x01",
            "永遠に生き続けるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x16,
        (
            "#5Pそして、それがあるからこそ\x01",
            "今のあなた達がある……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    #N0502
    NpcTalk(
        0x15,
        "セシル",
        (
            "#05905F#12P……占い師さん、もしかして\x01",
            "あなたも大切な人を……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0503
    ChrTalk(
        0x16,
        "#5P……喋りすぎたようね。\x02",
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x16,
        (
            "#5P私のような一介の占い師ごときが\x01",
            "口を出すことじゃなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x101,
        (
            "#00004F#6Pいえ、ありがたい言葉です。\x01",
            "肝に銘じさせてもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x16,
        "#5Pふふ……どういたしまして。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0E5")

    label("loc_A9D9")

    SetChrSubChip(0x101, 0x2)

    #C0507
    ChrTalk(
        0x101,
        (
            "#00000F#6Pセシル姉、\x01",
            "何か占いたいことはないか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0508
    NpcTalk(
        0x15,
        "セシル",
        (
            "#05905F#12Pえ、私が決めていいのかしら？\x02\x03",

            "#05904Fふふ、そうね……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0509
    NpcTalk(
        0x15,
        "セシル",
        (
            "#05909F#12Pそれじゃあ……ロイドが将来、\x01",
            "どんなお嫁さんをもらうか\x01",
            "占ってもらっちゃおうかしら。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0510
    ChrTalk(
        0x101,
        "#00011F#6P#4Sえ゛。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0511
    ChrTalk(
        0x101,
        (
            "#00011F#6Pちょ、ちょっとセシル姉……？\x01",
            "さすがに恥ずかしすぎるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #N0512
    NpcTalk(
        0x15,
        "セシル",
        (
            "#05909F#12Pあら、いいじゃない。\x01",
            "お姉ちゃんが知りたいんだから。\x02\x03",

            "#05900Fふふ、よろしくおねがいしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x16,
        "#5Pふふ、お安い御用よ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0514
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0515
    NpcTalk(
        0x15,
        "セシル",
        (
            "#05900F#12P（あら……\x01",
            "  なんだか本当に凄そうね。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0516
    ChrTalk(
        0x16,
        (
            "#5Pまっすぐな目をした青年に、\x01",
            "添い遂げる女性、それは……\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x16,
        (
            "#5P………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x15, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #N0518
    NpcTalk(
        0x15,
        "セシル",
        (
            "#05905F#12Pあら……\x01",
            "どうしてしまったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x16,
        (
            "#5P申し訳ないけれど……\x01",
            "現時点では何もいえないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x101,
        "#00005F#6Pへ……\x02",
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x16,
        (
            "#5P今までに何度か同じような占いを\x01",
            "頼まれた事はあるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x16,
        (
            "#5P可能性となる女性の数が多くて、\x01",
            "絞り込めないことがたまにあった。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x16,
        "#5P貴方の場合はまさにそれね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #N0524
    NpcTalk(
        0x15,
        "セシル",
        (
            "#05909F#12Pうーん……そうですか。\x01",
            "さすがに私も計算外だったわね。\x02\x03",

            "#05908Fロイドは私の自慢の弟だし、\x01",
            "女の子が放っておくわけないとは\x01",
            "思っていたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x101,
        (
            "#00006F#6P（な、なんだか俺が\x01",
            "  もの凄い節操ナシみたいに\x01",
            "  言われてる気がする……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0526
    NpcTalk(
        0x15,
        "セシル",
        (
            "#05903F#12P……その、ロイド？\x01",
            "お姉ちゃん、ちょっと心配に\x01",
            "なってきたんだけど……\x02\x03",

            "#05901Fいつか女の子を\x01",
            "悲しませるような事を、\x01",
            "してしまわないようにね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0527
    ChrTalk(
        0x101,
        "#00012F#6Pし、しないからっ！\x02",
    )

    CloseMessageWindow()

    label("loc_B0E5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_32_A2BB end

    def Function_33_B0F1(): pass

    label("Function_33_B0F1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0528
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K何を占う？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "２人の相性を占う\x01",      # 0
            "イリアに任せる\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B68C")

    #C0529
    ChrTalk(
        0x101,
        (
            "#00000F#6P俺たちの相性を\x01",
            "占ってもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x16,
        "#5Pええ、お安い御用よ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0531
    ChrTalk(
        0x101,
        (
            "#00009F#6P……って勝手に\x01",
            "決めちゃいましたけど、\x01",
            "大丈夫でしたかね？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0532
    NpcTalk(
        0x15,
        "イリア",
        (
            "#01709F#12Pあはは、面白そうじゃない。\x01",
            "やってもらいましょ☆\x02\x03",

            "#01704Fフフ、セシルには悪いけど、\x01",
            "いい結果が出たら弟君は\x01",
            "あたしがもらっちゃおっかな～。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)

    #C0533
    ChrTalk(
        0x101,
        (
            "#00012F#6P……ま、まあ、\x01",
            "とりあえず試しってことで。\x02\x03",

            "#00000Fそれじゃあ、お願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x16,
        "#5Pええ、分かったわ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #C0535
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0536
    NpcTalk(
        0x15,
        "イリア",
        "#01705F#12P（へえ……本格的じゃない。）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0537
    ChrTalk(
        0x16,
        (
            "#5Pまっすぐな目をした青年と\x01",
            "舞台に情熱を燃やす舞姫……\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x16,
        (
            "#5P彼女の目指すものへの一途な想いは\x01",
            "他者を惹きつけ、魅了する……\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x16,
        (
            "#5P支える者に徹するならば、\x01",
            "より深い関係になれる可能性は\x01",
            "充分にあるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x16,
        (
            "#5Pだけど……\x01",
            "彼女の大事なものはあくまで舞台。\x01",
            "それ以上になることは難しいはずよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0541
    ChrTalk(
        0x16,
        "#5P……私に見えたのはこんな所かしら。\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x101,
        (
            "#00000F#6Pはは、結局イリアさんは\x01",
            "ステージが一番ってことですね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #N0543
    NpcTalk(
        0x15,
        "イリア",
        (
            "#01700F#12Pフフ、そういうことみたい。\x02\x03",

            "#01709Fそれにしても、占い師さん。\x01",
            "正直ここまでの占いを\x01",
            "見せてくれるとは思わなかったわ。\x02\x03",

            "#01700F一朝一夕で身につく技術じゃ\x01",
            "ないと思うんだけど……\x01",
            "どこで練習してきたわけ？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Jump("loc_BEC3")

    label("loc_B68C")

    SetChrSubChip(0x101, 0x2)

    #C0544
    ChrTalk(
        0x101,
        (
            "#00000F#6Pイリアさん、\x01",
            "何か占いたいことはありますか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0545
    NpcTalk(
        0x15,
        "イリア",
        (
            "#01705F#12Pあら、私が決めていいワケ？\x02\x03",

            "#01703Fうーん、そうねえ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0546
    NpcTalk(
        0x15,
        "イリア",
        (
            "#01709F#12Pじゃ、リーシャとシュリが\x01",
            "将来あたしを追い抜けるかどうか！\x01",
            "……ってのはどうかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x101,
        "#00005F#6Pあの２人が……\x02",
    )

    CloseMessageWindow()

    #N0548
    NpcTalk(
        0x15,
        "イリア",
        (
            "#01704F#12Pまあ、正直こんなこと\x01",
            "占うようなことじゃ\x01",
            "ないかもしれないけど……\x02\x03",

            "#01702Fあたしの目が間違ってないって\x01",
            "改めて確認する意味でもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x16,
        (
            "#5Pあなたのお弟子さんの将来……\x01",
            "それを占えばいいのね？\x02",
        )
    )

    CloseMessageWindow()

    #N0550
    NpcTalk(
        0x15,
        "イリア",
        (
            "#01700F#12Pええ、そんなところかしら。\x01",
            "占ってもらえる？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0551
    ChrTalk(
        0x16,
        "#5Pふふ、お安い御用よ。\x02",
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0553
    NpcTalk(
        0x15,
        "イリア",
        "#01705F#12P（へえ……本格的じゃない。）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0554
    ChrTalk(
        0x16,
        (
            "#5P舞台に情熱を燃やす舞姫が見出した\x01",
            "２人の若き踊り手……\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x16,
        (
            "#5P底知れぬ才を秘めているけど、\x01",
            "彼女たちはそれぞれに\x01",
            "悩みを抱えているようね。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x16,
        (
            "#5Pそれをどう乗り越えるか……\x01",
            "未来への鍵はそこにある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0557
    ChrTalk(
        0x16,
        "#5P……私に見えたのはこんな所かしら。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)

    #N0558
    NpcTalk(
        0x15,
        "イリア",
        "#01703F#12Pリーシャとシュリの悩み、か……\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x101,
        "#00005F#6Pイリアさん、心当たりが？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #N0560
    NpcTalk(
        0x15,
        "イリア",
        (
            "#01703F#12Pあの子たちがそれぞれ、\x01",
            "何かの悩みを抱えているのは\x01",
            "気づいてたけど……\x02\x03",

            "#01700F正直、内容までは\x01",
            "詳しく聞いたことはないわね。\x02\x03",

            "#01704F……でもまあ、誰しも悩みくらい\x01",
            "多かれ少なかれ持ってるものでしょ。\x02\x03",

            "乗り越えられるかも人それぞれ……\x01",
            "あたしの口出す事じゃないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x101,
        (
            "#00000F#6Pはは、手厳しいというか……\x01",
            "ある意味イリアさんらしいですね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0562
    NpcTalk(
        0x15,
        "イリア",
        (
            "#01700F#12Pフフ、まああたしは\x01",
            "あの子達が乗り越えられるって\x01",
            "信じているけどね。\x02\x03",

            "#01703Fきっと、それを乗り越えたときが\x01",
            "あたしの最高のライバルが\x01",
            "生まれる瞬間なんだわ。\x02\x03",

            "#01709Fく～っ、なんだか\x01",
            "ドキドキしてきたわね！\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x16,
        (
            "#5P貴女のその前向きさ……\x01",
            "一種の才といったものでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x16,
        "#5Pふふ、少し羨ましく感じるわ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #N0565
    NpcTalk(
        0x15,
        "イリア",
        (
            "#01702F#12Pフフ、どういたしまして。\x02\x03",

            "#01709Fそれにしても、占い師さん。\x01",
            "正直ここまでの占いを\x01",
            "見せてくれるとは思わなかったわ。\x02\x03",

            "#01700F一朝一夕で身につく技術じゃ\x01",
            "ないと思うんだけど……\x01",
            "どこで練習してきたわけ？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    label("loc_BEC3")


    #C0566
    ChrTalk(
        0x16,
        (
            "#5P……昔、ある旅の一座に入って\x01",
            "色々な芸を披露していてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x16,
        (
            "#5Pその応用で出来るようになった、\x01",
            "とだけ言っておこうかしら。\x02",
        )
    )

    CloseMessageWindow()

    #N0568
    NpcTalk(
        0x15,
        "イリア",
        (
            "#01705F#12P一座……\x01",
            "いわゆるサーカスってやつね。\x02\x03",

            "#01709Fうーん、あなたが\x01",
            "活躍してるところを\x01",
            "一度見てみたかったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x101,
        "#00000F#6Pはは、本当ですね。\x02",
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x16,
        "#5P……ふふ、どういたしまして。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_33_B0F1 end

    def Function_34_C01A(): pass

    label("Function_34_C01A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0571
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K何を占う？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "２人の相性を占う\x01",      # 0
            "リーシャに任せる\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C81E")

    #C0572
    ChrTalk(
        0x101,
        (
            "#00000F#6P俺たちの相性を\x01",
            "占ってもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x16,
        "#5Pええ、お安い御用よ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #N0574
    NpcTalk(
        0x15,
        "リーシャ",
        "#01805F#12Pロ、ロイドさん……？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0575
    ChrTalk(
        0x101,
        (
            "#00009F#6Pはは、折角こういうところに\x01",
            "来たことだし、試しにと思ってさ。\x02\x03",

            "#00000F迷惑だったらやめとくけど……\x02",
        )
    )

    CloseMessageWindow()

    #N0576
    NpcTalk(
        0x15,
        "リーシャ",
        (
            "#01804F#12P……ふふ、いえ。\x02\x03",

            "#01802Fそうですね、せっかくですし\x01",
            "お願いしてみましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x16,
        "#5Pふふ、それでは……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    #C0578
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0579
    NpcTalk(
        0x15,
        "リーシャ",
        "#01801F#12P（……これは……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0580
    ChrTalk(
        0x16,
        (
            "#5Pまっすぐな目をした青年と\x01",
            "憂いを帯びた瞳の少女……\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x16,
        (
            "#5P以前、ある事件に関わったことで\x01",
            "２人には確かな信頼が芽生えている……\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x16,
        (
            "#5Pこの想いを育めば、\x01",
            "より深い関係になれる可能性は\x01",
            "充分にあるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x16,
        (
            "#5Pただし……そのためには、\x01",
            "彼女の心にかかる闇を、\x01",
            "取り払う必要がある……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0584
    ChrTalk(
        0x16,
        "#5P……私に見えたのはこんな所かしら。\x02",
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x101,
        "#00005F#6Pリーシャの心にかかる闇……？\x02",
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x16,
        "#5Pさて……私には分からないわね。\x02",
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x16,
        (
            "#5Pこの水晶玉にそういう暗示を\x01",
            "読み取ったというだけのことだから。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0588
    NpcTalk(
        0x15,
        "リーシャ",
        (
            "#01802F#12P……えっと、その。\x01",
            "多分、今度のリニューアル公演の\x01",
            "心配なんじゃないかと思います。\x02\x03",

            "#01809Fシュリちゃんの晴れ舞台で\x01",
            "ちゃんと踊れるか……\x01",
            "最近少し不安でしたから。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0589
    ChrTalk(
        0x101,
        (
            "#00000F#6Pああ、そういうことか。\x02\x03",

            "#00003Fでも、リーシャは随分前から\x01",
            "一所懸命練習しているようだし、\x01",
            "きっと大丈夫だよ。\x02\x03",

            "#00009F前に観せてもらった公演では\x01",
            "俺も感動したし……\x01",
            "心配する事なんかないさ。\x02",
        )
    )

    CloseMessageWindow()

    #N0590
    NpcTalk(
        0x15,
        "リーシャ",
        "#01805F#12P…………………………\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x16,
        "#5P……ふふ、手が早いわね。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    #C0592
    ChrTalk(
        0x16,
        (
            "#5Pアドバイスを早速実践してくれるのは\x01",
            "占い師冥利に尽きるというものだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0593
    ChrTalk(
        0x101,
        "#00005F#6Pえっ……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0594
    ChrTalk(
        0x101,
        (
            "#00011F#6Pち、違うからな、リーシャ！\x02\x03",

            "決してそういう下心が\x01",
            "あったわけじゃ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0595
    NpcTalk(
        0x15,
        "リーシャ",
        (
            "#01809F#12P……ふふっ、分かってますから。\x02\x03",

            "#01802Fありがとうございます、ロイドさん。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF0B")

    label("loc_C81E")

    SetChrSubChip(0x101, 0x2)

    #C0596
    ChrTalk(
        0x101,
        (
            "#00000F#6Pリーシャ、\x01",
            "何か占いたいことはないか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0597
    NpcTalk(
        0x15,
        "リーシャ",
        (
            "#01805F#12Pえっと、私が決めても\x01",
            "いいんですか？\x02\x03",

            "#01803Fそ、そうですね……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0598
    NpcTalk(
        0x15,
        "リーシャ",
        (
            "#01803F#12Pこの間、仔猫探しの件で会った\x01",
            "シャーリィさんですけど……\x02\x03",

            "#01801F彼女とまた会うご縁があるのか、\x01",
            "ちょっと占っていただけませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0599
    ChrTalk(
        0x101,
        "#00005F#6Pリーシャ……？\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x16,
        "#5Pええ、そのくらいならお安い御用よ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0601
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0602
    NpcTalk(
        0x15,
        "リーシャ",
        "#01801F#12P（……これは……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0603
    ChrTalk(
        0x16,
        "#5P貴女とシャーリィという名の娘……\x02",
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x16,
        (
            "#5P再びクロスベルでまみえるという\x01",
            "暗示が出ているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x16,
        (
            "#5Pそれがいつ、どんな状況かは\x01",
            "分からないけれど……\x01",
            "その時は必ずやってくるでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0606
    ChrTalk(
        0x16,
        "#5P……私に見えたのはこんな所かしら。\x02",
    )

    CloseMessageWindow()

    #N0607
    NpcTalk(
        0x15,
        "リーシャ",
        (
            "#01802F#12P……なるほど、\x01",
            "ありがとうございました。\x02\x03",

            "#01803F（《血染めの#8Rブラッディ#シャーリィ》……\x01",
            "  やっぱり気をつけておかなくちゃ。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0608
    ChrTalk(
        0x101,
        (
            "#00000F#6Pへえ、なんだか意外だな。\x02\x03",

            "マリーの事件の時に\x01",
            "ちょっと関わったくらいだけど、\x01",
            "そんなに気になってたのか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0609
    NpcTalk(
        0x15,
        "リーシャ",
        (
            "#01802F#12Pあ、いえ……\x01",
            "他に占ってもらいたいことが\x01",
            "思いつきませんでしたから。\x02\x03",

            "#01804Fそれに、とっても可愛らしい子でしたし\x01",
            "機会があるならお話したいなって。\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x101,
        (
            "#00002F#6Pう、うーん……\x01",
            "あれで相当危ない子なんだが。\x02\x03",

            "#00006Fエリィの件を考えると\x01",
            "別の意味でも危険そうだし……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #N0611
    NpcTalk(
        0x15,
        "リーシャ",
        "#01805F#12P……エリィさんの件？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0612
    ChrTalk(
        0x101,
        (
            "#00012F#6Pあ、ああいや。\x01",
            "なんでもないから。\x02\x03",

            "#00003F（ちょ、ちょっとすごい光景を\x01",
            "  想像してしまった……）\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x16,
        "#5P……ふふ、お嬢さん。\x02",
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0x16,
        (
            "#5Pよろしければこちらの彼が\x01",
            "何を考えていたか、\x01",
            "占って差し上げましょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    #C0615
    ChrTalk(
        0x101,
        "#00012F#6Pか、勘弁してくださいっ！\x02",
    )

    CloseMessageWindow()

    label("loc_CF0B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_34_C01A end

    def Function_35_CF17(): pass

    label("Function_35_CF17")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0616
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K何を占う？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "２人の相性を占う\x01",      # 0
            "シュリに任せる\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5E4")

    #C0617
    ChrTalk(
        0x101,
        (
            "#00000F#6P俺たちの相性を\x01",
            "占ってもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x16,
        "#5Pええ、お安い御用よ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #N0619
    NpcTalk(
        0x15,
        "シュリ",
        (
            "#14011F#12Pお、おいっ……\x01",
            "何考えてんだ、アンタ！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0620
    ChrTalk(
        0x101,
        (
            "#00005F#6Pえっ……\x01",
            "そ、そんな慌てるほどのことか？\x02\x03",

            "#00009F君と２人でいるなんて珍しいし、\x01",
            "この機に親睦を深められるか、\x01",
            "占ってもらおうと思ったんだが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #N0621
    NpcTalk(
        0x15,
        "シュリ",
        (
            "#14006F#12P（……ンなこと、\x01",
            "  面と向かって言うか、普通！？）\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x16,
        (
            "#5Pふふ、どうするのかしら。\x01",
            "私は何でもいいのだけれど。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #N0623
    NpcTalk(
        0x15,
        "シュリ",
        (
            "#14000F#12P……あーもう、いいよそれで。\x01",
            "勝手に占っちゃってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x16,
        "#5Pええ、それでは………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0625
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0626
    NpcTalk(
        0x15,
        "シュリ",
        "#14005F#12P（……な、なんだ……？）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0627
    ChrTalk(
        0x16,
        (
            "#5Pまっすぐな目をした青年と\x01",
            "輝く可能性を秘めた少女……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D338")

    #C0628
    ChrTalk(
        0x16,
        (
            "#5P出会いは最悪だったけれど、\x01",
            "貴女は、彼の優しさに\x01",
            "気づいているようね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D376")

    label("loc_D338")


    #C0629
    ChrTalk(
        0x16,
        (
            "#5P貴女は、彼から溢れてくる\x01",
            "優しさに気づいているようね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D376")


    #C0630
    ChrTalk(
        0x16,
        (
            "#5P時が経ち、貴女に\x01",
            "素直な心が芽生えたなら、\x01",
            "兄妹のような仲にもなれる……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0631
    ChrTalk(
        0x16,
        "#5P……私に見えたのはこんな所かしら。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #N0632
    NpcTalk(
        0x15,
        "シュリ",
        (
            "#14011F#12Pな、なななななっ……\x01",
            "なんだよ、この占いはっ！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0633
    ChrTalk(
        0x101,
        (
            "#00000F#6Pはは、確かに\x01",
            "ちょっと照れるかもな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0634
    NpcTalk(
        0x15,
        "シュリ",
        (
            "#14006F#12P『ちょっと照れる』、\x01",
            "なんてもんじゃねーっつの！\x02\x03",

            "#14012Fなんでアンタなんかと\x01",
            "兄妹みたいな仲になんて……！\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x16,
        (
            "#5Pふふ……今でも充分に\x01",
            "仲が良いみたいだけど。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #N0636
    NpcTalk(
        0x15,
        "シュリ",
        "#14011F#12Pよ、よくないってば！\x02",
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x101,
        "#00012F#6P（はは、ほんと素直じゃないよな。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_DE1C")

    label("loc_D5E4")

    SetChrSubChip(0x101, 0x2)

    #C0638
    ChrTalk(
        0x101,
        (
            "#00000F#6Pシュリ、\x01",
            "何か占いたいことはないか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0639
    NpcTalk(
        0x15,
        "シュリ",
        (
            "#14005F#12Pえ、オレが決めてもいいのか？\x02\x03",

            "#14003Fうーん……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0640
    NpcTalk(
        0x15,
        "シュリ",
        (
            "#14003F#12Pそれじゃあ、聞くけどさ……\x02\x03",

            "#14000Fオレが今後、アルカンシェルで\x01",
            "ちゃんとやっていけるか……\x01",
            "それを占ってくれるか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0641
    ChrTalk(
        0x101,
        "#00005F#6Pシュリ……？\x02",
    )

    CloseMessageWindow()

    #N0642
    NpcTalk(
        0x15,
        "シュリ",
        (
            "#14008F#12P……だってさ、\x01",
            "もしこれでいい結果が出るなら……\x02\x03",

            "#14008Fきっともう、あんなスラムなんかに\x01",
            "戻ることなんてないだろ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0643
    ChrTalk(
        0x101,
        "#00005F#6Pあ……\x02",
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x16,
        "#5P……いいでしょう、占ってあげるわ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0645
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0646
    NpcTalk(
        0x15,
        "シュリ",
        "#14005F#12P（……な、なんだ……？）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0647
    ChrTalk(
        0x16,
        (
            "#5P……貴女の行く道は、\x01",
            "実に様々な方向に枝分かれ\x01",
            "しているようね。\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0x16,
        (
            "#5P夢をこのまま追い続けられるか、\x01",
            "あるいは挫折して元いた場所に\x01",
            "戻ってしまうのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x16,
        (
            "#5P運命は未だにそれを\x01",
            "決定づけてはいないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0x16,
        (
            "#5P現時点では、私の口からは\x01",
            "絶対に大丈夫だとはいえないわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0651
    ChrTalk(
        0x16,
        "#5P……私に見えたのはこんな所よ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)

    #N0652
    NpcTalk(
        0x15,
        "シュリ",
        (
            "#14003F#12P……そっか……\x02\x03",

            "#14008Fここで『絶対にやってける』って\x01",
            "言ってもらえたなら、\x01",
            "少しは安心できたんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x101,
        "#00008F#6Pシュリ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0654
    ChrTalk(
        0x16,
        (
            "#5P……私の知り合いにも、\x01",
            "スラム出身の子がいたわ。\x02",
        )
    )

    CloseMessageWindow()

    #N0655
    NpcTalk(
        0x15,
        "シュリ",
        "#14005F#12Pえ……\x02",
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0x16,
        (
            "#5P会ってすぐの頃、\x01",
            "その子は何もかもに絶望した\x01",
            "表情をしていたけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0x16,
        (
            "#5P長い間一緒に生活しているうちに、\x01",
            "明るくて強い子になった。\x02",
        )
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x16,
        (
            "#5Pそして、立派な指導者に出会って、\x01",
            "今では一流の遊撃士として活躍している。\x02",
        )
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0x16,
        (
            "#5P彼女を成長させたのは……\x01",
            "間違いなく『人との出会い』だった。\x02",
        )
    )

    CloseMessageWindow()

    #N0660
    NpcTalk(
        0x15,
        "シュリ",
        "#14005F#12Pあ……\x02",
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x16,
        (
            "#5P先ほどの暗示では、\x01",
            "貴女は既に尊敬できる人物に\x01",
            "出会っているのではなくて？\x02",
        )
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x16,
        (
            "#5Pならば、あとは貴女次第……\x01",
            "私はそう思うのだけれど。\x02",
        )
    )

    CloseMessageWindow()

    #N0663
    NpcTalk(
        0x15,
        "シュリ",
        (
            "#14000F#12P……オレ次第……か。\x02\x03",

            "#14003F……そうだな。\x01",
            "オレはその遊撃士さんみたいに\x01",
            "強くあれるかは分からないけど……\x02\x03",

            "#14002Fとにかく、今は頑張ってみるよ。\x01",
            "……ありがとうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x16,
        "#5Pふふ……どういたしまして。\x02",
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x101,
        "#00002F#6P（はは……やっぱり誘ってよかったかな。）\x02",
    )

    CloseMessageWindow()

    label("loc_DE1C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_35_CF17 end

    def Function_36_DE28(): pass

    label("Function_36_DE28")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-7780, -1100, 4820, 0)
    MoveCamera(306, 31, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18050, 0)
    SetChrPos(0x101, -3580, 0, 2100, 270)
    SetChrPos(0xEF, -3200, 0, 3370, 270)
    OP_4B(0x18, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0666
    ChrTalk(
        0x101,
        "#00000Fあっ、見つけた！\x02",
    )

    CloseMessageWindow()
    OP_9C(0x18, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    OP_93(0x18, 0x5A, 0x1F4)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0667
    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "きゃっ、見つかっちゃった☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-5450, -1100, 5050, 0)
    MoveCamera(306, 31, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18050, 0)
    SetChrPos(0x18, -3530, 0, 2710, 90)
    SetChrPos(0x101, -1850, 0, 2040, 270)
    SetChrPos(0xEF, -1850, 0, 3400, 270)
    FadeToBright(1000, 0)
    OP_0D()

    #C0668
    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "みししっ、\x01",
            "おにーさんもラッキーね。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "あたしの隠れてるところを、\x01",
            "２回も連続で発見するなんて、\x01",
            "相当運がいいと見たわ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x101,
        "#00012Fそ、そうか……？\x02",
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "みししっ、でもこれは\x01",
            "ほんの小手調べなんだから。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "そう何回もまぐれは\x01",
            "続かないんだからネッ☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E099():

        label("loc_E099")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_E099")

    QueueWorkItem2(0x101, 1, lambda_E099)

    def lambda_E0AB():

        label("loc_E0AB")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_E0AB")

    QueueWorkItem2(0xEF, 1, lambda_E0AB)
    SetChrFlags(0x18, 0x1000)
    OP_95(0x18, -3310, 0, 340, 5000, 0x0)
    OP_95(0x18, -240, 0, -2920, 5000, 0x0)

    def lambda_E0EA():
        OP_95(0xFE, -80, 0, -8710, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_E0EA)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    OP_68(310, 1200, -870, 0)
    MoveCamera(323, 28, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14850, 0)
    SetChrPos(0x101, -780, 0, 180, 180)
    SetChrPos(0xEF, 850, 0, 160, 180)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_E1CE")

    #C0673
    ChrTalk(
        0x102,
        (
            "#00105F……行ってしまったわね。\x02\x03",

            "#00104F思った以上に\x01",
            "パレバレだったけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E555")

    label("loc_E1CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_E22B")

    #C0674
    ChrTalk(
        0x103,
        (
            "#00205F……行ってしまいました。\x02\x03",

            "#00204F思った以上に\x01",
            "パレバレでしたが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E555")

    label("loc_E22B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_E284")

    #C0675
    ChrTalk(
        0x104,
        (
            "#00305F……行っちまったな。\x02\x03",

            "#00304F思った以上に\x01",
            "パレバレだったが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E555")

    label("loc_E284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_E2E5")

    #C0676
    ChrTalk(
        0x109,
        (
            "#10105F……行ってしまいましたね。\x02\x03",

            "#10104F思った以上に\x01",
            "パレバレでしたけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E555")

    label("loc_E2E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_E342")

    #C0677
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、行っちゃったね。\x02\x03",

            "#10302F思った以上に\x01",
            "パレバレだったけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E555")

    label("loc_E342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_E390")

    #C0678
    ChrTalk(
        0x153,
        (
            "#01105F行っちゃったー。\x02\x03",

            "#01102Fなんだかパレバレだったね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E555")

    label("loc_E390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_E3F1")

    #C0679
    ChrTalk(
        0x156,
        (
            "#06405F……行っちゃいましたね～。\x02\x03",

            "#06404F思った以上に\x01",
            "パレバレでしたけど～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E555")

    label("loc_E3F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_E44A")

    #C0680
    ChrTalk(
        0x14C,
        (
            "#05905F行っちゃったわね。\x02\x03",

            "#05904F思った以上に\x01",
            "パレバレだったけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E555")

    label("loc_E44A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_E4A7")

    #C0681
    ChrTalk(
        0x134,
        (
            "#01705F行っちゃったみたいね。\x02\x03",

            "#01706F思った以上に\x01",
            "パレバレだったけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E555")

    label("loc_E4A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_E508")

    #C0682
    ChrTalk(
        0x135,
        (
            "#01805F……行ってしまいましたね。\x02\x03",

            "#01803F思った以上に\x01",
            "パレバレでしたけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E555")

    label("loc_E508")


    #C0683
    ChrTalk(
        0x166,
        (
            "#14005F……行っちまったな。\x02\x03",

            "#14006F思った以上に\x01",
            "パレバレだったけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_E5E8")

    #C0684
    ChrTalk(
        0x101,
        (
            "#00003Fう、うーん。\x01",
            "かくれんぼは好きなだけで\x01",
            "得意じゃないのかも……\x02\x03",

            "#00000Fとにかく、この調子で\x01",
            "どんどん見つけていきましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E667")

    label("loc_E5E8")


    #C0685
    ChrTalk(
        0x101,
        (
            "#00003Fう、うーん。\x01",
            "かくれんぼは好きなだけで\x01",
            "得意じゃないのかも……\x02\x03",

            "#00000Fとにかく、この調子で\x01",
            "どんどん見つけていこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E667")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x7F, 0x1, 0xB)
    SetScenarioFlags(0x1C9, 3)
    OP_65(0x0, 0x1)
    SetChrFlags(0x18, 0x80)
    SetChrPos(0x0, 130, 0, -70, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_36_DE28 end

    def Function_37_E69C(): pass

    label("Function_37_E69C")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0686
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　 ～占いの館～ 　　\x01",
            "恋愛運に財政運、その他\x01",
            "あなたの運命見通します\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_37_E69C end

    def Function_38_E700(): pass

    label("Function_38_E700")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E812")
    EventBegin(0x1)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xF, 0x0, 0)

    #C0687
    ChrTalk(
        0xF,
        "《占いの館》へようこそっ！\x02",
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0xF,
        (
            "ここでは、凄腕占い師の先生に\x01",
            "色々と占ってもらえちゃいますっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x101,
        (
            "#00000F（みーしぇとかくれんぼ中だし……\x01",
            "　今アトラクションで遊ぶのは\x01",
            "　やめておくとしよう。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -70, 0, 4080, 180)
    OP_4C(0xF, 0xFF)
    OP_93(0xF, 0xB4, 0x0)
    EventEnd(0x4)
    Jump("loc_E815")

    label("loc_E812")

    Call(0, 18)

    label("loc_E815")

    Return()

    # Function_38_E700 end

    SaveToFile()

Try(main)
