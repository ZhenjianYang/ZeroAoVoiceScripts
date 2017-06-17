from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0470.bin",                # FileName
        "c0470",                    # MapName
        "c0470",                    # Location
        0x0025,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 37, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0470",                  # 0
        "ドレイク・オーナー",     # 1
        "チェリー",               # 2
        "ガレッティ",             # 3
        "エリンデ",               # 4
        "レイタロッサ",           # 5
        "リッケ爺さん",           # 6
        "観光客",                 # 7
        "観光客",                 # 8
        "観光客",                 # 9
        "レクター",               # 10
        "ビクセン町長",           # 11
        "ガンツ",                 # 12
        "レクター",               # 13
    ))

    AddCharChip((
        "chr/ch20002.itc",                   # 00
        "chr/ch21200.itc",                   # 01
        "chr/ch25800.itc",                   # 02
        "chr/ch25900.itc",                   # 03
        "chr/ch27000.itc",                   # 04
        "chr/ch27100.itc",                   # 05
        "chr/ch32300.itc",                   # 06
        "chr/ch32302.itc",                   # 07
        "chr/ch33302.itc",                   # 08
        "chr/ch07402.itc",                   # 09
    ))

    DeclNpc(-899,    4000,    21299,   180,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(6199,    -1000,   8000,    270,  261,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       -1000,   13649,   180,  261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-6500,   -1000,   6000,    90,   261,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(1350,    -949,    11500,   0,    341,  0x0, 0,   8,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(6699,    4269,    15750,   90,   261,  0x0, 0,   0,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(0,       -1000,   5349,    225,  389,  0x0, 0,   1,   0,   0,   1,   0,   15,  255,  0)
    DeclNpc(0,       -1000,   5349,    225,  389,  0x0, 0,   6,   0,   0,   1,   0,   16,  255,  0)
    DeclNpc(3299,    -949,    12590,   315,  469,  0x0, 0,   7,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(1820,    4000,    18850,   0,    469,  0x0, 0,   9,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-900,    4000,    20000,   2000,    -900,    5500,    21300,   0x007E, 0,  5,  0x0000)
    DeclActor(5240,    -1000,   8000,    1200,    6200,    500,     8000,    0x007E, 0,  7,  0x0000)
    DeclActor(-920,    -1000,   12050,   1700,    0,       500,     13650,   0x007E, 0,  9,  0x0000)
    DeclActor(-4500,   -1000,   6000,    1500,    -6500,   500,     6000,    0x007E, 0,  11, 0x0000)
    DeclActor(7530,    4000,    17960,   1800,    7530,    5500,    17960,   0x007C, 0,  20, 0x0000)
    DeclActor(7530,    4000,    15750,   1800,    7530,    5500,    15750,   0x007C, 0,  20, 0x0000)
    DeclActor(7530,    4000,    13410,   1800,    7530,    5500,    13410,   0x007C, 0,  20, 0x0000)
    DeclActor(7530,    4000,    10460,   1800,    7530,    5500,    10460,   0x007C, 0,  20, 0x0000)
    DeclActor(7530,    4000,    8300,    1800,    7530,    5500,    8300,    0x007C, 0,  20, 0x0000)

    ScpFunction((
        "Function_0_3E4",          # 00, 0
        "Function_1_49C",          # 01, 1
        "Function_2_4C7",          # 02, 2
        "Function_3_61B",          # 03, 3
        "Function_4_713",          # 04, 4
        "Function_5_7D0",          # 05, 5
        "Function_6_7D4",          # 06, 6
        "Function_7_25EC",         # 07, 7
        "Function_8_25F0",         # 08, 8
        "Function_9_3A70",         # 09, 9
        "Function_10_3A74",        # 0A, 10
        "Function_11_4923",        # 0B, 11
        "Function_12_4927",        # 0C, 12
        "Function_13_5732",        # 0D, 13
        "Function_14_69DF",        # 0E, 14
        "Function_15_7C4D",        # 0F, 15
        "Function_16_7E4D",        # 10, 16
        "Function_17_8124",        # 11, 17
        "Function_18_817A",        # 12, 18
        "Function_19_8755",        # 13, 19
        "Function_20_8ABD",        # 14, 20
        "Function_21_8B4F",        # 15, 21
        "Function_22_8DDF",        # 16, 22
        "Function_23_96C8",        # 17, 23
        "Function_24_AD6E",        # 18, 24
        "Function_25_ADC9",        # 19, 25
        "Function_26_AE24",        # 1A, 26
        "Function_27_AE4A",        # 1B, 27
        "Function_28_AE70",        # 1C, 28
        "Function_29_B209",        # 1D, 29
    ))


    def Function_0_3E4(): pass

    label("Function_0_3E4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_424"),
        (1, "loc_430"),
        (2, "loc_43C"),
        (3, "loc_448"),
        (4, "loc_454"),
        (5, "loc_460"),
        (6, "loc_46C"),
        (SWITCH_DEFAULT, "loc_478"),
    )


    label("loc_424")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_430")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_43C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_448")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_454")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_460")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_46C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_478")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_484")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_49B")

    Return()

    # Function_0_3E4 end

    def Function_1_49C(): pass

    label("Function_1_49C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C6")
    OP_94(0xFE, 0x744, 0x1BD0, 0xFFFFF704, 0xB2C, 0x3E8)
    Sleep(300)
    Jump("Function_1_49C")

    label("loc_4C6")

    Return()

    # Function_1_49C end

    def Function_2_4C7(): pass

    label("Function_2_4C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E2")
    SetMapFlags(0x10000000)
    Event(0, 23)
    Jump("loc_4F4")

    label("loc_4E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F4")
    Event(0, 19)

    label("loc_4F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_508")
    ClearScenarioFlags(0x5C, 0)
    SetMapFlags(0x10000000)
    Event(0, 21)

    label("loc_508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_527")
    SetChrPos(0xD, 50, 4050, 18950, 0)
    Jump("loc_61A")

    label("loc_527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_535")
    Jump("loc_61A")

    label("loc_535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_55B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_551")
    ClearChrFlags(0x11, 0x80)
    Jump("loc_556")

    label("loc_551")

    SetChrFlags(0x8, 0x80)

    label("loc_556")

    Jump("loc_61A")

    label("loc_55B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_587")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_61A")

    label("loc_587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_595")
    Jump("loc_61A")

    label("loc_595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5C1")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_61A")

    label("loc_5C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5D4")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_61A")

    label("loc_5D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_5EF")
    ClearChrFlags(0x10, 0x80)
    SetChrSubChip(0x10, 0x1)
    SetChrSubChip(0xC, 0x2)
    Jump("loc_61A")

    label("loc_5EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_602")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_61A")

    label("loc_602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_615")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_61A")

    label("loc_615")

    ClearChrFlags(0xE, 0x80)

    label("loc_61A")

    Return()

    # Function_2_4C7 end

    def Function_3_61B(): pass

    label("Function_3_61B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_634")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_63A")

    label("loc_634")

    OP_10(0x0, 0x1)
    OP_10(0x3, 0x0)

    label("loc_63A")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -6000, -1000, 16000, 5000, 5000, 0)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67B")
    OP_1B(0x0, 0x0, 0x1D)

    label("loc_67B")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_691")
    OP_66(0x5, 0x1)
    Jump("loc_712")

    label("loc_691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_69F")
    Jump("loc_712")

    label("loc_69F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_6AD")
    Jump("loc_712")

    label("loc_6AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_6C4")
    Jump("loc_6C8")

    label("loc_6C4")

    OP_65(0x0, 0x1)

    label("loc_6C8")

    Jump("loc_712")

    label("loc_6CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_6EB")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jump("loc_712")

    label("loc_6EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6F9")
    Jump("loc_712")

    label("loc_6F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_712")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)

    label("loc_712")

    Return()

    # Function_3_61B end

    def Function_4_713(): pass

    label("Function_4_713")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_724")
    Jump("loc_7CC")

    label("loc_724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_732")
    Jump("loc_7CC")

    label("loc_732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_740")
    Jump("loc_7CC")

    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_74E")
    Jump("loc_7CC")

    label("loc_74E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_75C")
    Jump("loc_7CC")

    label("loc_75C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_76A")
    Jump("loc_7CC")

    label("loc_76A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_778")
    Jump("loc_7CC")

    label("loc_778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_786")
    Jump("loc_7CC")

    label("loc_786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_794")
    Jump("loc_7CC")

    label("loc_794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7A2")
    Jump("loc_7CC")

    label("loc_7A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7B0")
    Jump("loc_7CC")

    label("loc_7B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7BE")
    Jump("loc_7CC")

    label("loc_7BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7CC")
    Jump("loc_7CC")

    label("loc_7CC")

    TalkEnd(0xFE)
    Return()

    # Function_4_713 end

    def Function_5_7D0(): pass

    label("Function_5_7D0")

    Call(0, 6)
    Return()

    # Function_5_7D0 end

    def Function_6_7D4(): pass

    label("Function_6_7D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7EA")
    Call(0, 22)
    Jump("loc_25EB")

    label("loc_7EA")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8A2")

    #C0001
    ChrTalk(
        0x8,
        (
            "やはりガンツさんは\x01",
            "お見えにならないようですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "ふむ……当店としても\x01",
            "残念なことでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "昨日のことは水に流して\x01",
            "また楽しんで頂けると良いのですが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E8")

    label("loc_8A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_C83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 6)), scpexpr(EXPR_END)), "loc_B01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_93F")

    #C0004
    ChrTalk(
        0x8,
        (
            "レクター様なら昨晩\x01",
            "帝国に呼び戻されたと\x01",
            "愚痴っておられましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "皆様には健闘を祈る、と\x01",
            "言い残されておられました。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFC")

    label("loc_93F")


    #C0006
    ChrTalk(
        0x8,
        (
            "そういえば……\x01",
            "レクター様も今日は\x01",
            "いらっしゃっていませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "昨晩のお話では\x01",
            "帝国に戻るとか何とか。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        (
            "#0005Fえっ……\x01",
            "もう帰国したんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "ええ、何でも\x01",
            "どうしても外せないけど面倒臭い\x01",
            "用事ができてしまったとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#0003Fそう、ですか……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x102,
        (
            "#0101Fあの人なら何か\x01",
            "知ってそうだったのにね。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x103,
        (
            "#0206Fまあ、知っていても\x01",
            "素直に話してくれるタイプには\x01",
            "見えませんでしたが。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF6")

    #C0013
    ChrTalk(
        0x10A,
        "#0605F（……誰の話だ………？）\x02",
    )

    CloseMessageWindow()

    label("loc_AF6")

    SetScenarioFlags(0xD0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_AFC")

    Jump("loc_C7E")

    label("loc_B01")


    #C0014
    ChrTalk(
        0x8,
        (
            "ガンツさんなら\x01",
            "今日はいらっしゃっていませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "昨日の一件もありますからな。\x01",
            "顔を出しづらいのかもしれませんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#0001Fいえ、そうじゃないんですが……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0017
    ChrTalk(
        0x104,
        (
            "#0303Fちょいと事情があってな。\x02\x03",

            "#0300Fオーナー、もし\x01",
            "あの兄さんが顔を出したら\x01",
            "支援課に連絡を入れてくれ。\x02\x03",

            "ちょいとヤボ用があんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "ああ、構わんが……\x01",
            "何か事件絡みのようだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCE, 6)

    label("loc_C7E")

    Jump("loc_25E8")

    label("loc_C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_F0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 5)), scpexpr(EXPR_END)), "loc_D46")

    #C0019
    ChrTalk(
        0x8,
        (
            "ガンツさんが暴れた件、\x01",
            "スタッフには口を噤むよう\x01",
            "言っておきましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "多少の噂は広まるでしょうが……\x01",
            "まあ話題の多い歓楽街の事です。\x01",
            "次第に忘れられていくでしょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F08")

    label("loc_D46")


    #C0021
    ChrTalk(
        0x8,
        (
            "先ほどはありがとうございました。\x01",
            "礼を言わせて頂きますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        (
            "#0306F運が良かったぜ。\x01",
            "あのままじゃどうなってた事か……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#0003Fああ、あの怪力では\x01",
            "傷害沙汰でも\x01",
            "済まなかったかもしれない……\x02\x03",

            "#0001Fオーナーさんも、できれば今日の事は\x01",
            "しばらく伏せておいて頂けますか？\x02\x03",

            "まだ事実関係を\x01",
            "確認している所なので……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "ええ、こちらとしても\x01",
            "好ましくない話ではありますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "多少の噂は広まるでしょうが\x01",
            "スタッフには口を噤むよう\x01",
            "言っておきますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCE, 5)

    label("loc_F08")

    Jump("loc_25E8")

    label("loc_F0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_FCE")

    #C0026
    ChrTalk(
        0x8,
        (
            "ガンツさんならウチの常連ですよ。\x01",
            "間違えるはずはありませんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "ホテル・ミレニアムの\x01",
            "最上階デラックスルームに\x01",
            "ご滞在なさってる筈ですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "ご用ならお会いになられては？\x02",
    )

    CloseMessageWindow()
    Jump("loc_25E8")

    label("loc_FCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_12AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10C2")

    #C0029
    ChrTalk(
        0x8,
        (
            "ランディ、顔を出すのはいいが\x01",
            "あまり調子に乗るなよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "ギャンブルなんてのは、\x01",
            "いつか必ずしっぺ返しを\x01",
            "食らうもんだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#0306Fへいへい、分かってるっつーの。\x01",
            "（……オーナー、少し\x01",
            "  ピリピリしてやがんなぁ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A9")

    label("loc_10C2")


    #C0032
    ChrTalk(
        0x104,
        (
            "#0300Fようオーナー、\x01",
            "久々に遊びに来てやったぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "……ランディ、またお前か。\x01",
            "しっしっ、来なくていいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "お前が近頃控えてるお陰で\x01",
            "ウチの売り上げも……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        "………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0036
    ChrTalk(
        0x104,
        "#0305Fどうかしたのか？\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "……いいや？\x01",
            "大したことじゃないさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "ま、遊ぶなら\x01",
            "程ほどにしておけってこった。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "ギャンブルなんてのは、\x01",
            "いつか必ずしっぺ返しを\x01",
            "食らうもんだからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_12A9")

    Jump("loc_25E8")

    label("loc_12AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_17D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1330")

    #C0040
    ChrTalk(
        0x8,
        (
            "皆さんも、ルバーチェ商会なんぞに\x01",
            "首を突っ込むモンじゃありませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        "お気をつけになってください。\x02",
    )

    CloseMessageWindow()
    Jump("loc_17D0")

    label("loc_1330")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_153D")
    TurnDirection(0x8, 0x104, 0)

    #C0042
    ChrTalk(
        0x8,
        (
            "ランディ、ルバーチェ商会の\x01",
            "シマに顔を出してたんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "フン、また危ない話に\x01",
            "首を突っ込みやがったな。\x01",
            "連中は止めとけと言ってるだろうが。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#0306Fあー、あれは成り行きだっての。\x01",
            "まあトラブったっつーか。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "フン……警備隊だの警察だの、\x01",
            "お前は危ない職場ばかり選びやがるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "ランディ、今からでも\x01",
            "落ち着いた仕事を探せよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#0000F（はは……オーナーさんは\x01",
            "  随分詳しいみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#0300F（……このカジノには\x01",
            "  クロスベルに流れてきたばっかの頃から\x01",
            "  入り浸ってるからなぁ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17CD")

    label("loc_153D")


    #C0049
    ChrTalk(
        0x8,
        (
            "皆さん、ランディと共に\x01",
            "ルバーチェ商会のシマに\x01",
            "顔を出したとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "気を付けなさってくださいよ。\x01",
            "連中に関わるとろくな事がない。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "ランディにもキツく言ってやって下さい。\x01",
            "あいつ……警備隊だの警察だの\x01",
            "危険のある職場ばかり選ぶんですからねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#0000Fはは、ご心配をかけたみたいで……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16BC")

    #C0053
    ChrTalk(
        0x102,
        (
            "#0100Fオーナーさんはランディさんについて\x01",
            "お詳しいみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1713")

    label("loc_16BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1713")

    #C0054
    ChrTalk(
        0x103,
        (
            "#0200Fというかオーナーさん、\x01",
            "ランディさんについて詳しいんですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1713")


    #C0055
    ChrTalk(
        0x8,
        "ええ、まあ……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "ランディがクロスベルに\x01",
            "流れてきたばかりの頃、\x01",
            "ウチに入り浸ってましたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "あいつの事情まで知りませんが……\x01",
            "まあ、どこか放っておけない所が\x01",
            "ありましてねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17CD")

    SetScenarioFlags(0x0, 0)

    label("loc_17D0")

    Jump("loc_25E8")

    label("loc_17D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_195C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_185E")

    #C0058
    ChrTalk(
        0x8,
        (
            "導力ネットとやらの中で\x01",
            "商売をする『情報屋』がいるとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "フフ、近頃はどうして\x01",
            "ハイカラになりましたな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1957")

    label("loc_185E")


    #C0060
    ChrTalk(
        0x8,
        (
            "聞くところによると、\x01",
            "導力ネットの中で商売をする\x01",
            "『情報屋』がいるそうですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "一般的な情報集めから\x01",
            "非合法なものまで\x01",
            "一手に引き受けるそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "フフ、昔はヤクザの\x01",
            "下請け仕事だったものですが……\x01",
            "近頃はどうしてハイカラになりましたな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1957")

    Jump("loc_25E8")

    label("loc_195C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1B22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A08")

    #C0063
    ChrTalk(
        0x8,
        (
            "そもそも市長は自治州創立直後の\x01",
            "激動の時代を生きてきたお方……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "この１５年間\x01",
            "クロスベルが平和でいられたのも\x01",
            "あの方の手腕ならではでしょうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1D")

    label("loc_1A08")


    #C0065
    ChrTalk(
        0x8,
        (
            "ヘンリー・マクダエルといえば\x01",
            "この１５年間、市長職を務めている\x01",
            "中立派の政治家ですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "この１５年の間、\x01",
            "クロスベルにも色々ありましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "あの方の舵取りのお陰で\x01",
            "何とか乗り越えてきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "チンケなカジノ屋が\x01",
            "言うのもなんですが、\x01",
            "あれはたいしたお人ですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1B1D")

    Jump("loc_25E8")

    label("loc_1B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1CA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B9E")

    #C0069
    ChrTalk(
        0x8,
        (
            "……ランディ、休憩スペース#12R  こ    こ  #は\x01",
            "割といつも空いている。\x01",
            "気が向いたら飲みに来いや。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CA1")

    label("loc_1B9E")


    #C0070
    ChrTalk(
        0x8,
        (
            "なんだランディ、\x01",
            "気が抜けた顔をしてるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#0300Fはは、そうか？\x02\x03",

            "#0306Fまあ仕事で色々あんだよ。\x01",
            "聞かせるほどの話じゃねえが。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        "ふん、そうか……\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "実は今日は\x01",
            "いいボトルが入っているんだ。\x01",
            "気が向いたら飲みにでも来い。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x104,
        "#0300Fおう、またな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1CA1")

    Jump("loc_25E8")

    label("loc_1CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1EDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D31")

    #C0075
    ChrTalk(
        0x8,
        (
            "ルバーチェといえば\x01",
            "クロスベル暗黒街を仕切る元締め……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "皆さんも、くれぐれも\x01",
            "無茶はなさらないでくださいよ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED6")

    label("loc_1D31")

    TurnDirection(0x8, 0x104, 0)

    #C0077
    ChrTalk(
        0x8,
        (
            "ランディ、ルバーチェについて\x01",
            "嗅ぎ回ってるんだって？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0078
    ChrTalk(
        0x104,
        "#0306Fうっ……なぜそれを……！？\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "ま、やめときな。\x01",
            "駆け出し警官が\x01",
            "手を出せる相手じゃねえよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "クロスベル……特に\x01",
            "この歓楽街で店やってる連中なら\x01",
            "みんな判ってることさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "ウチも連中と揉めねえよう\x01",
            "みかじめ料を払ってるくらいだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x102,
        "#0108F………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1ED6")

    Jump("loc_25E8")

    label("loc_1EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2022")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F64")

    #C0083
    ChrTalk(
        0x8,
        (
            "記念祭にアルカンシェルの新作……\x01",
            "盛り上がるのも道理ですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "わたくしどもも\x01",
            "来月が楽しみでございますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_201D")

    label("loc_1F64")


    #C0085
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "当カジノハウスへようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x8,
        (
            "記念祭も近いせいか\x01",
            "大盛況でございますな。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "先日はアルカンシェルの\x01",
            "新作チケットが発売されたとか……\x01",
            "大した賑わいでしたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_201D")

    Jump("loc_25E8")

    label("loc_2022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2152")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_20A3")

    #C0088
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "カジノハウス《バルカ》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "本日も楽しんで\x01",
            "いただけると嬉しいですな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_214D")

    label("loc_20A3")


    #C0090
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "カジノハウス《バルカ》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "お疲れになられた方は\x01",
            "こちらの休憩スペースをご利用ください。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "リキュール程度なら\x01",
            "お出しできますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_214D")

    Jump("loc_25E8")

    label("loc_2152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2333")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_21CF")

    #C0093
    ChrTalk(
        0x8,
        (
            "今宵はＶＩＰの方から\x01",
            "ご予約が入っているのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "政府高官と同伴の方……\x01",
            "つまりは接待ですな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232E")

    label("loc_21CF")


    #C0095
    ChrTalk(
        0x8,
        (
            "今宵はＶＩＰの方から\x01",
            "ご予約が入っておりましてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "政府高官と同伴の方ですな。\x01",
            "特別席でおもてなすとしましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x104,
        (
            "#0306Fは～、またかよ。\x01",
            "最近接待連中が多いんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 500)
    Sleep(300)

    #C0098
    ChrTalk(
        0x8,
        (
            "客が増えてんだ、\x01",
            "これでいいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "ランディ、お前は間違っても\x01",
            "顔を出すなよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x104,
        (
            "#0306Fへいへい、野郎の相手なんざ\x01",
            "こっちから願い下げだっての。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_232E")

    Jump("loc_25E8")

    label("loc_2333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_END)), "loc_23E4")

    #C0101
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "カジノハウス《バルカ》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "アホ面のランディ以外なら\x01",
            "いつでも歓迎いたしますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x104,
        (
            "#0306Fおいおい。\x01",
            "俺も客だぞ、狸オヤジ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E8")

    label("loc_23E4")

    TurnDirection(0x8, 0x101, 0)

    #C0104
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "カジノハウス《バルカ》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "ルーレットでもいかがですかな。\x01",
            "丁度席が空いておりますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x104,
        (
            "#0301Fおい狸オヤジ、\x01",
            "なんで俺に声掛けねえんだよ～。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 500)
    Sleep(300)

    #C0107
    ChrTalk(
        0x8,
        (
            "……ランディ、\x01",
            "お前は来なくていいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "しっしっ、たまには他のお客様にも\x01",
            "サービスして差し上げろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x104,
        (
            "#0301Fうわひっでぇ、また俺が\x01",
            "大勝ちする事を警戒してやがるな？\x02\x03",

            "#0300Fはっ、覚えてろよ。\x01",
            "今夜絶対来てやるからな！\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        "しっしっ、黙ってろよ若造！\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        (
            "#0100F（常連……なのかしら。\x01",
            "  変わった関係ねえ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 0)

    label("loc_25E8")

    TalkEnd(0x8)

    label("loc_25EB")

    Return()

    # Function_6_7D4 end

    def Function_7_25EC(): pass

    label("Function_7_25EC")

    Call(0, 8)
    Return()

    # Function_7_25EC end

    def Function_8_25F0(): pass

    label("Function_8_25F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2615")
    Call(0, 28)
    Return()

    label("loc_2615")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2622")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A6C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",        # 0
            "交換をする\x01",      # 1
            "やめる\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_267E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_267E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26E4")
    SetScenarioFlags(0x6D, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_26A0")
    OP_AF(0x41)
    Jump("loc_26D5")

    label("loc_26A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_26B0")
    OP_AF(0x40)
    Jump("loc_26D5")

    label("loc_26B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_26C0")
    OP_AF(0x3F)
    Jump("loc_26D5")

    label("loc_26C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_26D3")
    OP_AF(0x3E)
    Jump("loc_26D5")

    label("loc_26D3")

    OP_AF(0x3D)

    label("loc_26D5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A67")

    label("loc_26E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26F8")
    Jump("loc_3A67")

    label("loc_26F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A67")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_27DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2748")

    #C0112
    ChrTalk(
        0x9,
        "みんなも頑張って稼いでね㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_27D7")

    label("loc_2748")


    #C0113
    ChrTalk(
        0x9,
        "ようこそ《バルカ》へ～！\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "うふふ、昨日の一件で\x01",
            "うちのカジノも\x01",
            "有名になっちゃったみたいなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        "お客さんが多くって嬉しいかも～☆\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_27D7")

    Jump("loc_3A67")

    label("loc_27DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_28EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2858")

    #C0116
    ChrTalk(
        0x9,
        (
            "レクターさん、オーナーとも\x01",
            "気が合っちゃってるみたいよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        "もうすっかり常連さんってカンジ㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_28E5")

    label("loc_2858")


    #C0118
    ChrTalk(
        0x9,
        "うふっ、ようこそ《バルカ》へ～！\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "昨日は遅くまで\x01",
            "レクターさんと飲んじゃったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x9,
        (
            "うふ、ヘンな人だけど\x01",
            "お話が面白いのよね～☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_28E5")

    Jump("loc_3A67")

    label("loc_28EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_299D")

    #C0121
    ChrTalk(
        0x9,
        (
            "あのガンツさんを負かしたヒト、\x01",
            "オーナーと飲んでるわよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x9,
        (
            "最後の大勝負で\x01",
            "ファイブ・オブ・ア・カインド\x01",
            "なんてやるぅ！\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        "きっとよっぽどの勝負師なのね～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A67")

    label("loc_299D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2BBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2A45")

    #C0124
    ChrTalk(
        0x9,
        (
            "ガンツさん、お客さんと\x01",
            "大勝負をしてるらしいわよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x9,
        (
            "ガレッティさんやエリンデさんじゃ\x01",
            "歯が立たないって所に\x01",
            "名乗り出たヒトがいたのよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BB7")

    label("loc_2A45")


    #C0126
    ChrTalk(
        0x9,
        (
            "あ、ランディさん～。\x01",
            "オーナーなら特別室に\x01",
            "入っちゃってるわよ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        (
            "朝からガンツさんの勝負に\x01",
            "立ち会ってるところなの～。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x104,
        (
            "#0305F特別室……あの\x01",
            "ＶＩＰしか使えねえ勝負部屋かよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x9,
        (
            "そうなの、お客さんの１人と\x01",
            "大勝負してるらしいわよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "前までは冴えない\x01",
            "週末ギャンブラーだったのにぃ、\x01",
            "ホント今はＶＩＰ待遇なのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x103,
        "#0201F………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2BB7")

    Jump("loc_3A67")

    label("loc_2BBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_2CBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2C2A")

    #C0132
    ChrTalk(
        0x9,
        (
            "ガンツさん、最近\x01",
            "アタリが来ちゃってるのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        "なんだか前とは別人みた～い。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CB7")

    label("loc_2C2A")


    #C0134
    ChrTalk(
        0x9,
        (
            "でもガンツさん、\x01",
            "最近様子が変かも～。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x9,
        (
            "スッゴク偉そうになったし～\x01",
            "バカみたいに当てまくるし～。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        "なんだか前とは別人みた～い。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2CB7")

    Jump("loc_3A67")

    label("loc_2CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_END)), "loc_2D36")

    #C0137
    ChrTalk(
        0x9,
        "ガンツさんのこと……？\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        (
            "それならオーナーに\x01",
            "聞くといいと思うわよ。\x01",
            "よく休憩スペースで話してるもの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A67")

    label("loc_2D36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2F75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2DCC")

    #C0139
    ChrTalk(
        0x9,
        (
            "でも……あの人が\x01",
            "あんなに大勝ちするなんて～\x01",
            "ちょっと信じられないかも～。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x9,
        (
            "最近すっごい派手に\x01",
            "遊んじゃってるのよね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F70")

    label("loc_2DCC")


    #C0141
    ChrTalk(
        0x9,
        (
            "最近奥の特別室を\x01",
            "１人で使うお客さんがいるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x9,
        (
            "すっごい派手に遊ぶ\x01",
            "お客さんでね～……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x9,
        (
            "昨日なんてガレッティさん相手に\x01",
            "ストレートフラッシュ決めちゃって、\x01",
            "みんなで拍手しちゃった～☆\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x104,
        (
            "#0305Fな、なにぃ！？\x01",
            "俺以外にそんな目立つ事を\x01",
            "する奴がいるとは……\x02\x03",

            "#0301F許せねえな！\x01",
            "俺と勝負させろ！\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        "#0006Fランディ、食いつかないでくれ。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x109,
        (
            "#0506Fランディ先輩……\x01",
            "カジノ遊びが得意というのは\x01",
            "本当みたいですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2F70")

    Jump("loc_3A67")

    label("loc_2F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_310A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2FDB")

    #C0147
    ChrTalk(
        0x9,
        (
            "ここは景品やコインの\x01",
            "交換カウンターよ㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x9,
        "ばんばん遊んで交換してね～☆\x02",
    )

    CloseMessageWindow()
    Jump("loc_3105")

    label("loc_2FDB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3093")

    #C0149
    ChrTalk(
        0x9,
        (
            "あ、ランディさんだー。\x01",
            "最近見なかったじゃな～い。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x9,
        (
            "まあいいかも～。\x01",
            "今日はバッチリ楽しんで行ってね～☆\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        (
            "#0300Fはは、今日は\x01",
            "用事があるんで少しだけな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3102")

    label("loc_3093")


    #C0152
    ChrTalk(
        0x9,
        (
            "あれ、今日は\x01",
            "ランディさんと一緒じゃないの～？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        (
            "まあいいかも～。\x01",
            "みんなもバッチリ\x01",
            "楽しんで行ってね～☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3102")

    SetScenarioFlags(0x0, 1)

    label("loc_3105")

    Jump("loc_3A67")

    label("loc_310A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_32AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_315C")

    #C0154
    ChrTalk(
        0x9,
        (
            "警察って結構いい所なのね～。\x01",
            "ちょっと羨ましいかも～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32A7")

    label("loc_315C")


    #C0155
    ChrTalk(
        0x9,
        (
            "あらランディさん、\x01",
            "まっ昼間からカジノ遊び？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x9,
        (
            "いけないんだー。\x01",
            "警察のカチョーさんに\x01",
            "言いつけちゃうぞ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x104,
        (
            "#0300F課長は……\x01",
            "別に怒らねえよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        "#0003Fうーん、放任主義だからな……\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x103,
        "#0200Fむしろ遊びに来そうな気も。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        (
            "#0106F真面目な所は\x01",
            "ちゃんとあるのだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x9,
        (
            "そうなんだー。\x01",
            "何だかいいカチョーさんね☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_32A7")

    Jump("loc_3A67")

    label("loc_32AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3446")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3316")

    #C0162
    ChrTalk(
        0x9,
        (
            "オーナーって普段から\x01",
            "ちょっと貫禄があるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x9,
        "そう言われると納得よね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3441")

    label("loc_3316")


    #C0164
    ChrTalk(
        0x9,
        (
            "オーナーって昔は\x01",
            "歓楽街でヤクザやってたらしいわよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x9,
        (
            "でも最後にはルバーチェに\x01",
            "潰されちゃったらしいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x9,
        (
            "うふ、今でも\x01",
            "胸に銃創が残ってるんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x104,
        (
            "#0305Fへえ、あのタヌキ親父……\x01",
            "そんな過去があったのかよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x9,
        (
            "うふふ、ヒミツよ☆\x01",
            "あまり言いふらすなって\x01",
            "口止めされてるんだから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3441")

    Jump("loc_3A67")

    label("loc_3446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_34AF")

    #C0169
    ChrTalk(
        0x9,
        "ようこそ《バルカ》へ～！\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x9,
        (
            "クロスベルの夜はこれからよ㈱\x01",
            "たっぷり遊んで行ってね～☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A67")

    label("loc_34AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_353F")

    #C0171
    ChrTalk(
        0x9,
        (
            "アルカンシェルの公演、\x01",
            "もう来月なのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x9,
        (
            "ウチはご近所だから\x01",
            "沢山お客さんが流れてくるはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x9,
        "うふ、楽しみね～㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A67")

    label("loc_353F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_36FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_35C4")

    #C0174
    ChrTalk(
        0x9,
        (
            "ランディさん、最近\x01",
            "カンテツしなくなっちゃったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x9,
        (
            "チェリーつまんなーい。\x01",
            "もっと遊びにきてよね～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F5")

    label("loc_35C4")


    #C0176
    ChrTalk(
        0x9,
        "ようこそ《バルカ》へ☆\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x9,
        (
            "ランディさんじゃない、\x01",
            "最近遊びに来てくれないわね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x104,
        (
            "#0300F悪いなチェリーちゃん、\x01",
            "仕事が忙しくてなぁ。\x01",
            "週に３日しかこれねえんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x9,
        (
            "ぶーぶー、\x01",
            "そんなのつまんなーい！\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#0006F週に３日って\x01",
            "多いと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x103,
        (
            "#0200Fランディさんの\x01",
            "カジノ癖は治りませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_36F5")

    Jump("loc_3A67")

    label("loc_36FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_37F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3769")

    #C0182
    ChrTalk(
        0x9,
        (
            "表の通りで\x01",
            "何か事件があったらしいわよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x9,
        (
            "ま、お店にいれば\x01",
            "関係ないけどね～☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37EE")

    label("loc_3769")


    #C0184
    ChrTalk(
        0x9,
        "さっき警察の人が顔を見せてたの。\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x9,
        (
            "昨晩表の通りで\x01",
            "何か事件があったらしいわよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x9,
        (
            "ま、お店にいれば\x01",
            "関係ないけどね～☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_37EE")

    Jump("loc_3A67")

    label("loc_37F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3914")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3851")

    #C0187
    ChrTalk(
        0x9,
        (
            "オーナーってもう\x01",
            "賭け事しないのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x9,
        "ちょっと残念かも～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_390F")

    label("loc_3851")


    #C0189
    ChrTalk(
        0x9,
        (
            "ガレッティさんもエリンデさんも\x01",
            "とっても賭け事強いのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x9,
        (
            "本気でやったら\x01",
            "まず負けないんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x9,
        (
            "うふふ、でもオーナーの腕は\x01",
            "それ以上って噂なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x9,
        "一度見てみたいかもね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_390F")

    Jump("loc_3A67")

    label("loc_3914")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3971")

    #C0193
    ChrTalk(
        0x9,
        (
            "ここは景品やコインの\x01",
            "交換カウンターよ㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x9,
        "ばんばん遊んで交換してね～☆\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A67")

    label("loc_3971")


    #C0195
    ChrTalk(
        0x9,
        "ようこそ《バルカ》へ～！\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x9,
        "あ、ランディさんだ～。\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x9,
        (
            "うふふ、いつもみたいに\x01",
            "たっぷり遊んで行ってね～☆\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x104,
        (
            "#0309Fおう、チェリーちゃん\x01",
            "任せとけっての！\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#0106F（いつもこうやって\x01",
            "  遊んでるのね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        "#0006F（やれやれだな……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3A67")

    Jump("loc_2622")

    label("loc_3A6C")

    TalkEnd(0x9)
    Return()

    # Function_8_25F0 end

    def Function_9_3A70(): pass

    label("Function_9_3A70")

    Call(0, 10)
    Return()

    # Function_9_3A70 end

    def Function_10_3A74(): pass

    label("Function_10_3A74")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_491F")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                    # 0
            "ポーカーで遊ぶ\x01",              # 1
            "ブラックジャックで遊ぶ\x01",      # 2
            "やめる\x01",                      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AF8")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3AF8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B48")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_3B48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B98")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_3B98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BAC")
    Jump("loc_491A")

    label("loc_3BAC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_491A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3C70")

    #C0201
    ChrTalk(
        0xA,
        (
            "ガンツ様は本日は\x01",
            "いらっしゃっておりません。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xA,
        (
            "ふむ……今までは\x01",
            "遅くとも夕方には来られたのですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xA,
        (
            "やはり昨日の一件が\x01",
            "こたえられたのでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_491A")

    label("loc_3C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3CE0")

    #C0204
    ChrTalk(
        0xA,
        (
            "カジノは昨日の話で\x01",
            "持ちきりでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xA,
        (
            "あれほどの名勝負は\x01",
            "久し振りでございますから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_491A")

    label("loc_3CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_3DA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3D26")

    #C0206
    ChrTalk(
        0xA,
        (
            "ガンツ様のお具合は\x01",
            "大丈夫なのでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D9E")

    label("loc_3D26")


    #C0207
    ChrTalk(
        0xA,
        (
            "ガンツ様の具合が\x01",
            "心配でございますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xA,
        (
            "確かに勝負で\x01",
            "いざこざもありましたが、\x01",
            "当店の常連様でございますから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3D9E")

    Jump("loc_491A")

    label("loc_3DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3EE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3E19")

    #C0209
    ChrTalk(
        0xA,
        (
            "……本日もガンツ様の\x01",
            "大勝ちということになりそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xA,
        "お相手の方にはお気の毒ですが。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EE2")

    label("loc_3E19")


    #C0211
    ChrTalk(
        0xA,
        (
            "……先ほど特別室の様子を\x01",
            "見てきましたが……\x01",
            "やはり思わしくありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xA,
        (
            "ガンツ様のお相手の方、\x01",
            "負け続きのようでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xA,
        (
            "もっとも５ゲームに１回ほどは\x01",
            "引き分けているようですが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3EE2")

    Jump("loc_491A")

    label("loc_3EE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_400A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3F47")

    #C0214
    ChrTalk(
        0xA,
        (
            "以前はフルハウスが精々だった方が\x01",
            "はて、どうしてあれほどのツキを……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4005")

    label("loc_3F47")


    #C0215
    ChrTalk(
        0xA,
        (
            "ガンツ様はカード勝負となると\x01",
            "素晴らしい手ばかりお引きになります。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xA,
        (
            "絶対にイカサマは無いと\x01",
            "言い切れるのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xA,
        (
            "どうしてあれほど運がよいのか、\x01",
            "はてどうしても判らぬのです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4005")

    Jump("loc_491A")

    label("loc_400A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_END)), "loc_40AA")

    #C0218
    ChrTalk(
        0xA,
        "……ガンツ様？\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xA,
        (
            "ええ、以前はよく週末に\x01",
            "いらっしゃっていたお客様ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xA,
        (
            "オーナーに聞いていただければ\x01",
            "詳しい事は分かると思いますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_491A")

    label("loc_40AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4191")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4132")

    #C0221
    ChrTalk(
        0xA,
        (
            "やれやれ、わたくしの腕も\x01",
            "鈍ったという事でしょうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xA,
        "……失礼、私事#4Rわたくしごと#でございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_418C")

    label("loc_4132")


    #C0223
    ChrTalk(
        0xA,
        (
            "これほど負けが込んだのは\x01",
            "久方ぶり……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xA,
        (
            "わたくしの腕も\x01",
            "鈍ったという事でしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_418C")

    Jump("loc_491A")

    label("loc_4191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4220")

    #C0225
    ChrTalk(
        0xA,
        (
            "今年の記念祭は\x01",
            "当カジノも過去最高の\x01",
            "売り上げでございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xA,
        (
            "皆様には楽しんでいただけたようで\x01",
            "大変嬉しゅうございます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_491A")

    label("loc_4220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4370")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_42B2")

    #C0227
    ChrTalk(
        0xA,
        (
            "アルカンシェルのプレ公演前後は\x01",
            "歓楽街も繁盛いたします。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xA,
        (
            "これも大スター、\x01",
            "イリア・プラティエ様の\x01",
            "お陰でしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_436B")

    label("loc_42B2")


    #C0229
    ChrTalk(
        0xA,
        (
            "そういえばアルカンシェルの\x01",
            "プレ公演も近いようでございますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xA,
        (
            "プレ公演に合わせいらっしゃる方々は\x01",
            "各国の富豪や有力者の方ばかり……\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xA,
        "カジノも盛り上がりそうでございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_436B")

    Jump("loc_491A")

    label("loc_4370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4473")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_43D4")

    #C0232
    ChrTalk(
        0xA,
        "いかがですか、皆様も一勝負。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xA,
        (
            "本日の運勢が\x01",
            "占えるかもしれませんよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_446E")

    label("loc_43D4")


    #C0234
    ChrTalk(
        0xA,
        (
            "運命の巡り合わせとは\x01",
            "数奇なもの……\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xA,
        (
            "時として予想を覆す結果を\x01",
            "もたらしてくれるものです。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xA,
        (
            "だからこそ人は\x01",
            "運命にすがるのでございましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_446E")

    Jump("loc_491A")

    label("loc_4473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_44C7")

    #C0237
    ChrTalk(
        0xA,
        "おや、日暮れでございますか……\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xA,
        "カジノも本番でございますね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_491A")

    label("loc_44C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4609")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4559")

    #C0239
    ChrTalk(
        0xA,
        (
            "ＶＩＰルームは本日も\x01",
            "予約済みとなっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xA,
        (
            "日が落ちれば、また大勢の\x01",
            "地位ある方々が\x01",
            "いらっしゃる事でしょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4604")

    label("loc_4559")


    #C0241
    ChrTalk(
        0xA,
        (
            "本日の特別室は\x01",
            "すでに予約済みとなっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xA,
        (
            "やはり自治州議会が\x01",
            "近いせいでしょうかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xA,
        (
            "近頃議員や高官、\x01",
            "社長や重役の方々が\x01",
            "連日楽しんでいかれますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4604")

    Jump("loc_491A")

    label("loc_4609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4734")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4692")

    #C0244
    ChrTalk(
        0xA,
        (
            "フフ、わたくしに\x01",
            "イカサマは通用いたしませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xA,
        (
            "負けは負けでございます。\x01",
            "素直に認めていただかなければ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_472F")

    label("loc_4692")


    #C0246
    ChrTalk(
        0xA,
        (
            "先日、負けそうになったお客様が\x01",
            "イカサマをなさろうとしまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xA,
        "ハア、いけませんね。\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xA,
        (
            "負けは負けでございます。\x01",
            "素直に認めていただかなければ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_472F")

    Jump("loc_491A")

    label("loc_4734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4860")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_47B1")

    #C0249
    ChrTalk(
        0xA,
        (
            "当カジノにはＶＩＰ様専用の\x01",
            "特別室がございますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xA,
        (
            "一般の皆様には\x01",
            "ご遠慮いただいております。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_485B")

    label("loc_47B1")


    #C0251
    ChrTalk(
        0xA,
        (
            "当カジノにはＶＩＰ様専用の\x01",
            "特別室がございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xA,
        (
            "フフ、ＶＩＰ様と申しましても\x01",
            "大貴族や議員の方々の事でして。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xA,
        (
            "相応のお部屋が\x01",
            "必要になるわけでございます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_485B")

    Jump("loc_491A")

    label("loc_4860")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_48CD")

    #C0254
    ChrTalk(
        0xA,
        (
            "レイタロッサ様は、週に一度\x01",
            "共和国からいらっしゃる常連さまです。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xA,
        "フフ、お強いですよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_491A")

    label("loc_48CD")


    #C0256
    ChrTalk(
        0xA,
        "こちらはカード台でございます。\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xA,
        (
            "ブラックジャックでも\x01",
            "いかがですか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_491A")

    Jump("loc_3A81")

    label("loc_491F")

    TalkEnd(0xA)
    Return()

    # Function_10_3A74 end

    def Function_11_4923(): pass

    label("Function_11_4923")

    Call(0, 12)
    Return()

    # Function_11_4923 end

    def Function_12_4927(): pass

    label("Function_12_4927")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4934")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_572E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",              # 0
            "ルーレットで遊ぶ\x01",      # 1
            "やめる\x01",                # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4996")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4996")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49E6")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_49E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49FA")
    Jump("loc_5729")

    label("loc_49FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5729")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4B25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4A9A")

    #C0258
    ChrTalk(
        0xB,
        (
            "いらっしゃいませ。\x01",
            "カジノハウス《バルカ》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xB,
        (
            "本日もじっくり楽しんで\x01",
            "いかれると嬉しいですわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B20")

    label("loc_4A9A")


    #C0260
    ChrTalk(
        0xB,
        (
            "自治州議会も\x01",
            "終わったそうですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xB,
        (
            "夜にはさらに\x01",
            "お客様が増えそうですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xB,
        (
            "うふふ、カジノにとっては\x01",
            "稼ぎ時ですわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4B20")

    Jump("loc_5729")

    label("loc_4B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4C2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4BB3")

    #C0263
    ChrTalk(
        0xB,
        (
            "昨日の名勝負のお陰で\x01",
            "気前のいい店と思われてしまった\x01",
            "ようですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xB,
        (
            "うふふ、カジノと\x01",
            "しましては好都合ですわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C28")

    label("loc_4BB3")


    #C0265
    ChrTalk(
        0xB,
        (
            "あら……今日はお客様が\x01",
            "随分と多い気が致しますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xB,
        (
            "うふふ、昨日の名勝負の噂が\x01",
            "広まってしまったのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4C28")

    Jump("loc_5729")

    label("loc_4C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_4D0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4C8C")

    #C0267
    ChrTalk(
        0xB,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xB,
        "あのお客様、油断なりませんわね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D06")

    label("loc_4C8C")


    #C0269
    ChrTalk(
        0xB,
        (
            "あのお客様……\x01",
            "不思議な打ち方をなさいますわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xB,
        (
            "もしや……\x01",
            "負けてばかりいられたのは\x01",
            "全て演技だったのでは……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4D06")

    Jump("loc_5729")

    label("loc_4D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4D7B")

    #C0271
    ChrTalk(
        0xB,
        (
            "ふう、あのお客様の腕では\x01",
            "無謀ですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xB,
        (
            "ほどほどで引き上げられると\x01",
            "よろしいのですけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5729")

    label("loc_4D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_4DF1")

    #C0273
    ChrTalk(
        0xB,
        (
            "ガンツさんのツキとカンは\x01",
            "異常ですわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xB,
        (
            "わたくしもあそこまで\x01",
            "負けが続いたのは初めてですわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5729")

    label("loc_4DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_END)), "loc_4F4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4E74")

    #C0275
    ChrTalk(
        0xB,
        (
            "ガンツさんは確かに\x01",
            "当店の常連客ですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xB,
        (
            "……詳しい話はオーナーから\x01",
            "お聞きになるとよいと思います。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F4A")

    label("loc_4E74")


    #C0277
    ChrTalk(
        0xB,
        "あら、ガンツさん……ですか？\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xB,
        (
            "ええ確かに\x01",
            "当店の常連の方ですわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xB,
        (
            "ついこの前までは、負けてばかりの\x01",
            "週末ギャンブラーでしたけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xB,
        (
            "……詳しい話はオーナーから\x01",
            "お聞きになるとよいと思いますわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4F4A")

    Jump("loc_5729")

    label("loc_4F4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5046")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4FB9")

    #C0281
    ChrTalk(
        0xB,
        "勝負は時の運、と申します。\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xB,
        (
            "わたくしどもでも\x01",
            "負けるときはございますわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5041")

    label("loc_4FB9")


    #C0283
    ChrTalk(
        0xB,
        (
            "ふう、あのお客様には\x01",
            "やられましたわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xB,
        (
            "……これは失礼、\x01",
            "何でもございませんわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xB,
        (
            "いかがですか、\x01",
            "一勝負試されてみては？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5041")

    Jump("loc_5729")

    label("loc_5046")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_517C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_50CF")

    #C0286
    ChrTalk(
        0xB,
        (
            "うふふ、カジノハウスと\x01",
            "しましては喜ばしいですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xB,
        (
            "今後ともカジノハウス\x01",
            "《バルカ》をご贔屓下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5177")

    label("loc_50CF")


    #C0288
    ChrTalk(
        0xB,
        (
            "うふふ、記念祭は\x01",
            "大いに盛り上がりましたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xB,
        (
            "まだまだ続けて滞在なさっている\x01",
            "観光の方も多いようですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xB,
        (
            "歓楽街ももうしばらくは\x01",
            "盛況が続きそうですわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5177")

    Jump("loc_5729")

    label("loc_517C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_51FC")

    #C0291
    ChrTalk(
        0xB,
        (
            "皆様も熱くなりすぎないように\x01",
            "お気をつけ下さいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xB,
        (
            "ふふ、いつの間にか\x01",
            "借金塗れになってしまいますわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5729")

    label("loc_51FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_527D")

    #C0293
    ChrTalk(
        0xB,
        (
            "うふふ……\x01",
            "わたくしこう見えましても\x01",
            "本物の勝負師ですのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xB,
        (
            "そう簡単に負かせられると\x01",
            "お思いにならないで。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5729")

    label("loc_527D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_52E9")

    #C0295
    ChrTalk(
        0xB,
        "あら、もうこんな時間ですのね。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xB,
        (
            "カジノに居ると\x01",
            "夕の鐘が聞こえないので\x01",
            "難儀しますわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5729")

    label("loc_52E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5348")

    #C0297
    ChrTalk(
        0xB,
        "あら、オーナーに御用ですか？\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xB,
        (
            "２階のカウンター席を\x01",
            "お訪ねくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5729")

    label("loc_5348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5428")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5394")

    #C0299
    ChrTalk(
        0xB,
        (
            "ふふ、今年の記念祭は\x01",
            "どんな祭りになるのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5423")

    label("loc_5394")


    #C0300
    ChrTalk(
        0xB,
        "来月の記念祭は楽しみですわね。\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xB,
        (
            "この歓楽街もいつも以上に\x01",
            "華やかになることでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xB,
        (
            "わたくしどもにとっても\x01",
            "書き入れ時ですわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5423")

    Jump("loc_5729")

    label("loc_5428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_558F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_54B9")

    #C0303
    ChrTalk(
        0xB,
        (
            "大勝ちを続けられた強運な方も\x01",
            "ＶＩＰルームに入る事が出来ますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xB,
        (
            "お客様も狙ってみるのも\x01",
            "いいかもしれませんわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_558A")

    label("loc_54B9")


    #C0305
    ChrTalk(
        0xB,
        (
            "昨晩のＶＩＰルームは\x01",
            "大いに盛り上がっていたようですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xB,
        (
            "あの特別室に入れるのは\x01",
            "大口のお客様か、よほど大勝なされた\x01",
            "ギャンブラーの方のみ。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xB,
        (
            "ふふ、お客様も狙ってみるのも\x01",
            "いいかもしれませんわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_558A")

    Jump("loc_5729")

    label("loc_558F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_562B")

    #C0308
    ChrTalk(
        0xB,
        (
            "人生の甘い罠、それは\x01",
            "何かを悟ってしまったような気分ですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xB,
        (
            "足元にはぽっかり穴が空いてるもの。\x01",
            "うふふ、お客様もお気をつけなさって。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5729")

    label("loc_562B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5681")

    #C0310
    ChrTalk(
        0xB,
        (
            "ルーレットでもいかが？\x01",
            "本日はいい当たりが\x01",
            "来るかもしれませんわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5729")

    label("loc_5681")


    #C0311
    ChrTalk(
        0xB,
        (
            "いらっしゃいませ。\x01",
            "カジノハウス《バルカ》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xB,
        (
            "ふふ、お客様\x01",
            "中々いい眼をお持ちですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xB,
        (
            "ルーレットでもいかが？\x01",
            "当たりが来るかもしれませんわよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5729")

    Jump("loc_4934")

    label("loc_572E")

    TalkEnd(0xB)
    Return()

    # Function_12_4927 end

    def Function_13_5732(): pass

    label("Function_13_5732")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_57C6")
    Jump("loc_5810")

    label("loc_57C6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_57E6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5810")

    label("loc_57E6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5806")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5810")

    label("loc_5806")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5810")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5890")

    #C0314
    ChrTalk(
        0xC,
        (
            "ふう、なんだか最近\x01",
            "遊ぶ気になれないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xC,
        "そろそろ国に帰ろうかしら。\x02",
    )

    CloseMessageWindow()
    Jump("loc_69D7")

    label("loc_5890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5913")

    #C0316
    ChrTalk(
        0xC,
        (
            "レクターに昨日の勝負について\x01",
            "問い詰めてやったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xC,
        "でも、はぐらかされちゃったわ。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xC,
        "何だかムカつくわ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_69D7")

    label("loc_5913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_5ADE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5998")

    #C0319
    ChrTalk(
        0xC,
        (
            "あのレクターって男、\x01",
            "腕は大した事ないはずだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xC,
        (
            "あの余裕ありげな態度が\x01",
            "何か引っかかるのよね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AD9")

    label("loc_5998")


    #C0321
    ChrTalk(
        0xC,
        (
            "あのレクターって男、\x01",
            "昨日も来ていたけれど\x01",
            "腕は大した事ないはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xC,
        (
            "私がコテンパンに\x01",
            "負かしてあげたくらいだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        "#0005Fえ……でもあの最後の手は？\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x104,
        (
            "#0301F確かに、ストレートフラッシュに\x01",
            "ファイブカードで勝つなんざ\x01",
            "狙ってできることじゃねえが……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xC,
        (
            "……偶然、なのかしらね。\x01",
            "本当の所は判らないけれど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5AD9")

    Jump("loc_69D7")

    label("loc_5ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5B44")

    #C0326
    ChrTalk(
        0xC,
        (
            "ガンツに挑むなんて\x01",
            "馬鹿な客もいたものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xC,
        (
            "私があれほど\x01",
            "忠告してあげたのに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69D7")

    label("loc_5B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_END)), "loc_5C37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5BBA")

    #C0328
    ChrTalk(
        0xC,
        "私も一度勝負してみたのだけど。\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xC,
        (
            "とても冴えないギャンブラー\x01",
            "って感じじゃなかったわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C32")

    label("loc_5BBA")


    #C0330
    ChrTalk(
        0xC,
        (
            "あのガンツっていう男、\x01",
            "元は冴えないギャンブラー\x01",
            "だったそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xC,
        (
            "本当かしら。\x01",
            "とても想像できないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5C32")

    Jump("loc_69D7")

    label("loc_5C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5D5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5CAD")

    #C0332
    ChrTalk(
        0xC,
        (
            "うふふ、聞いた話だと\x01",
            "派手に勝ち続けてる客がいるそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xC,
        "私もちょっと興味があるわね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D5A")

    label("loc_5CAD")


    #C0334
    ChrTalk(
        0xC,
        (
            "久し振りにクロスベルに来てみたら\x01",
            "……何だか面白い事になってるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xC,
        (
            "ここのディーラーさん、\x01",
            "負けが続いてるそうじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xC,
        "うふふ、相手は何者なのかしら。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5D5A")

    Jump("loc_69D7")

    label("loc_5D5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5E59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5DCB")

    #C0337
    ChrTalk(
        0xC,
        "私もそろそろ潮時かしら……\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xC,
        (
            "たっぷり遊んだし\x01",
            "一度帰国させてもらうとするわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E54")

    label("loc_5DCB")


    #C0339
    ChrTalk(
        0xC,
        (
            "ふう、暇潰しに\x01",
            "ドレイク・オーナーに\x01",
            "相手してもらったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xC,
        "確かにオーナーは強いわね。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xC,
        "うふふ、久し振りに負けちゃったわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5E54")

    Jump("loc_69D7")

    label("loc_5E59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5F76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5EC7")

    #C0342
    ChrTalk(
        0xC,
        "あの男、また負かしちゃったのよ。\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xC,
        (
            "うふふ……少しこっぴどく\x01",
            "やりすぎたかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F71")

    label("loc_5EC7")

    OP_4B(0xA, 0xFF)
    SetChrSubChip(0xC, 0x0)

    #C0344
    ChrTalk(
        0xA,
        (
            "さすがレイタロッサ様、\x01",
            "相変わらずお強いですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xA,
        (
            "こちらのグラスは\x01",
            "わたくしからの心付けでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xC,
        (
            "あらありがとう。\x01",
            "うふふ、気がきくわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    OP_4C(0xA, 0xFF)

    label("loc_5F71")

    Jump("loc_69D7")

    label("loc_5F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_60F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6002")

    #C0347
    ChrTalk(
        0xC,
        (
            "ＩＢＣって資産総額が\x01",
            "世界一らしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xC,
        (
            "さすが天下のＩＢＣ……\x01",
            "ミラだけなら\x01",
            "帝国や共和国にも負けないわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60F4")

    label("loc_6002")


    #C0349
    ChrTalk(
        0xC,
        (
            "ＩＢＣって資産総額を\x01",
            "合わせると世界一らしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xC,
        (
            "クロスベルはミラが集まる土地だし\x01",
            "歴史のある国際銀行だもの。\x01",
            "当然といえば当然でしょうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xC,
        (
            "うふふ、あのラインフォルト社や\x01",
            "ヴェルヌ社よりも金持ちだなんて\x01",
            "やっぱり驚きよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_60F4")

    Jump("loc_69D7")

    label("loc_60F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_6136")
    SetChrSubChip(0xC, 0x2)

    #C0352
    ChrTalk(
        0xC,
        (
            "やれやれ……\x01",
            "口ほどでもないわね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_6136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6262")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_61B1")

    #C0353
    ChrTalk(
        0xC,
        (
            "クロスベル警備隊の司令さんは\x01",
            "随分と遊び人だそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xC,
        (
            "うふふ、部下の人たちも\x01",
            "カワイソウね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_625D")

    label("loc_61B1")


    #C0355
    ChrTalk(
        0xC,
        (
            "クロスベル警備隊って\x01",
            "精鋭部隊なんですってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xC,
        (
            "でも、あそこの司令さんは\x01",
            "遊び人だって聞いているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xC,
        (
            "うふふ……きっと部下の人たちは\x01",
            "苦労してるんでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_625D")

    Jump("loc_69D7")

    label("loc_6262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6460")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_62C1")

    #C0358
    ChrTalk(
        0xC,
        "お父様ったら手回しが良すぎよ。\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xC,
        "ふう……何だか面白くないわね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_645B")

    label("loc_62C1")


    #C0360
    ChrTalk(
        0xC,
        (
            "今月はアルカンシェルの\x01",
            "チケット狙いで来たんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x104,
        (
            "#0304Fフッ、今の時期\x01",
            "そういう観光客は多いよな。\x02\x03",

            "#0300Fまあ手に入らなくても\x01",
            "落ち込まねえことさ。\x02\x03",

            "再来月でよければ\x01",
            "この俺がエスコートして……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xC,
        (
            "お父様が手配していて\x01",
            "あっさり手に入ってしまったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xC,
        "ふう、面白みがないわね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0364
    ChrTalk(
        0x104,
        (
            "#0306Fがーん……\x01",
            "予定と違うじゃねえか……\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x103,
        "#0200Fランディさん、ドンマイです。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_645B")

    Jump("loc_69D7")

    label("loc_6460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_655A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_64C6")

    #C0366
    ChrTalk(
        0xC,
        (
            "クロスベルにいると\x01",
            "身も心も蕩けちゃいそうよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xC,
        "うふふ、悪くないわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6555")

    label("loc_64C6")


    #C0368
    ChrTalk(
        0xC,
        (
            "クロスベルにいると\x01",
            "身も心も蕩けちゃいそうよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xC,
        (
            "甘い喧騒を聞いていると\x01",
            "頭の芯がじーんとしてきちゃうの。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xC,
        "うふふ、悪くないわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6555")

    Jump("loc_69D7")

    label("loc_655A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6698")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_65F1")

    #C0371
    ChrTalk(
        0xC,
        (
            "ドレイク・オーナーって\x01",
            "名うての賭博師だったらしいわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xC,
        (
            "それもヤクザ絡みの人だったとか。\x01",
            "うふ、ちょっと興味あるわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6693")

    label("loc_65F1")


    #C0373
    ChrTalk(
        0xC,
        (
            "そろそろカード台も\x01",
            "飽きてきちゃったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xC,
        (
            "ドレイク・オーナーに\x01",
            "直接相手してもらえないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xC,
        (
            "あの人、若い頃は\x01",
            "名うての賭博師だったらしいわよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6693")

    Jump("loc_69D7")

    label("loc_6698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 1)), scpexpr(EXPR_END)), "loc_677F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_66D8")

    #C0376
    ChrTalk(
        0xC,
        (
            "うふふ……\x01",
            "私、強いヒトって好きよ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_677A")

    label("loc_66D8")


    #C0377
    ChrTalk(
        0xC,
        (
            "うふふ……\x01",
            "私、強いヒトって好きよ㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x104,
        (
            "#0309F（ヒューヒュー！\x01",
            "  やっぱカジノはいいねぇ！）\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x101,
        (
            "#0006F（えっとランディ、\x01",
            "  あまり浮かれないでくれ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_677A")

    Jump("loc_69D7")

    label("loc_677F")

    SetChrSubChip(0xC, 0x0)
    OP_52(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x104, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6817")
    Jump("loc_6861")

    label("loc_6817")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6837")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6861")

    label("loc_6837")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6857")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6861")

    label("loc_6857")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6861")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    #C0380
    ChrTalk(
        0xC,
        "……あら、アナタがランディ？\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xC,
        (
            "うふふ、噂は聞いてるわ。\x01",
            "貴方賭け事に強いんですってね？\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x104,
        (
            "#0309Fヒュー！\x01",
            "こんな美人に声を掛けて\x01",
            "もらえるなんて光栄だねえ。\x02\x03",

            "#0300Fどうだい、俺と一つ\x01",
            "人生を掛けて勝負してみないか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x102,
        (
            "#0111F……あの、そういう話は\x01",
            "休日にやってもらえるかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x101,
        (
            "#0006F少なくとも\x01",
            "今日はやめておいてくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 1)

    label("loc_69D7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_5732 end

    def Function_14_69DF(): pass

    label("Function_14_69DF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6A73")
    Jump("loc_6ABD")

    label("loc_6A73")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6A93")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6ABD")

    label("loc_6A93")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6AB3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6ABD")

    label("loc_6AB3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6ABD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6BFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6B41")

    #C0385
    ChrTalk(
        0xD,
        "気持ちの切り替えが大切なんじゃ。\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xD,
        "カジノで長く遊ぶ秘訣じゃよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6BF6")

    label("loc_6B41")


    #C0387
    ChrTalk(
        0xD,
        (
            "ううっ……今日は\x01",
            "結局大負けしてしもうた。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xD,
        (
            "ええい、仕方がないわい。\x01",
            "こんな日は婆さんに\x01",
            "土産でも買って帰るとするかの。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xD,
        (
            "カジノ遊びは気持ちの\x01",
            "切り替えが大切なんじゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6BF6")

    Jump("loc_7C45")

    label("loc_6BFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6C8D")

    #C0390
    ChrTalk(
        0xD,
        "むう、あのレクターという男……\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xD,
        (
            "ワシの横で３万メダルも\x01",
            "出していきおったわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xD,
        (
            "腹立たしいのう……\x01",
            "負けてられんわい……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C45")

    label("loc_6C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_6CF1")

    #C0393
    ChrTalk(
        0xD,
        (
            "下で騒いでおったが……\x01",
            "何かあったのかの？\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xD,
        (
            "どうも近頃\x01",
            "騒がしい話が多いのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C45")

    label("loc_6CF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6DC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6D4B")

    #C0395
    ChrTalk(
        0xD,
        (
            "ガンツは近頃\x01",
            "妙に勢いづいておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xD,
        "誰も勝てんじゃろうて。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6DBE")

    label("loc_6D4B")


    #C0397
    ChrTalk(
        0xD,
        (
            "何でも特別室で\x01",
            "大勝負をやっとるそうじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xD,
        (
            "観光客があのガンツ相手に、か。\x01",
            "……まあ無理じゃろうなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6DBE")

    Jump("loc_7C45")

    label("loc_6DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_END)), "loc_6E3D")

    #C0399
    ChrTalk(
        0xD,
        (
            "うむむ、いい所なのに\x01",
            "日が暮れてしもうたわい……\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xD,
        (
            "嫌じゃ、帰りたくない。\x01",
            "今が丁度ノリノリなんじゃ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C45")

    label("loc_6E3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6F72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6ECD")

    #C0401
    ChrTalk(
        0xD,
        (
            "噂ではマフィア同士の\x01",
            "抗争をやっておるそうじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xD,
        (
            "おんしらもごたごたに\x01",
            "巻き込まれんように\x01",
            "気を付けるんじゃぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F6D")

    label("loc_6ECD")


    #C0403
    ChrTalk(
        0xD,
        (
            "近頃、ルバーチェの連中が\x01",
            "不審な動きをしておるそうじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xD,
        (
            "おんしらも\x01",
            "気をつけておくんじゃぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xD,
        (
            "連中に絡まれては\x01",
            "警察官とてただでは済まんからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6F6D")

    Jump("loc_7C45")

    label("loc_6F72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_713A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6FDF")

    #C0406
    ChrTalk(
        0xD,
        (
            "婆さんはいつもいつも\x01",
            "うるさくてのう……\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xD,
        (
            "歳のわりに\x01",
            "元気なのはいいんじゃが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7135")

    label("loc_6FDF")


    #C0408
    ChrTalk(
        0xD,
        (
            "婆さんはカジノ通いを\x01",
            "やめろとうるさくてのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xD,
        (
            "今朝も取っ組み合いの\x01",
            "喧嘩をしてから\x01",
            "ご出勤したんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xD,
        (
            "ふう、朝から\x01",
            "ええ汗をかいてしもうたわい。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7132")

    #C0411
    ChrTalk(
        0x104,
        (
            "#0300Fはは、爺さんも\x01",
            "相変わらずみてえだな……\x02\x03",

            "ちっとは孝行してやんなよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xD,
        (
            "ほっほ、ランディの言う通りじゃな。\x01",
            "今日は景品の一つでも\x01",
            "持ち帰ってやるとするか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7132")

    SetScenarioFlags(0x0, 5)

    label("loc_7135")

    Jump("loc_7C45")

    label("loc_713A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_72C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_71CD")

    #C0413
    ChrTalk(
        0xD,
        (
            "ワシらがこうして暮らしているのも\x01",
            "ジオフロント施設のお陰なんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xD,
        (
            "もっとも、市の管理には\x01",
            "問題も多いと聞くがのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72BF")

    label("loc_71CD")


    #C0415
    ChrTalk(
        0xD,
        (
            "クロスベルのジオフロントは\x01",
            "２０年ほど前に計画されたんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xD,
        (
            "都市人口が増えるにつれ\x01",
            "インフラ施設が足りなくなり\x01",
            "必要に迫られて造られたんじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xD,
        (
            "今でも拡張を繰り返しておってな\x01",
            "クロスベル市の地下中に\x01",
            "巡らされておるらしいのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_72BF")

    Jump("loc_7C45")

    label("loc_72C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_742C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_734C")

    #C0418
    ChrTalk(
        0xD,
        (
            "婆さんめ……\x01",
            "近頃手が込んできたのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xD,
        (
            "じゃがこの程度のことで\x01",
            "ワシがカジノを捨てるものか。\x01",
            "ほっほっほ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7427")

    label("loc_734C")


    #C0420
    ChrTalk(
        0xD,
        (
            "やれやれ、婆さんの目を\x01",
            "くらますのも楽じゃないワイ。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xD,
        (
            "今朝は裏口から\x01",
            "出ようとしたんじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xD,
        (
            "通りに出たところで\x01",
            "ばったり婆さんと会ってしまってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xD,
        (
            "ふう、慌てて走ったが\x01",
            "危なく捕まる所じゃったわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7427")

    Jump("loc_7C45")

    label("loc_742C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_7501")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7489")

    #C0424
    ChrTalk(
        0xD,
        (
            "ワシも昔は\x01",
            "夜遊びして歩いたもんじゃが、\x01",
            "さすがにこの歳ではの～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74FC")

    label("loc_7489")


    #C0425
    ChrTalk(
        0xD,
        (
            "おっと、そろそろ帰らんと\x01",
            "また婆さんにどやされるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xD,
        (
            "さすがにこの歳になって\x01",
            "夜遊びはキビシイからの～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_74FC")

    Jump("loc_7C45")

    label("loc_7501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_765A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_759B")

    #C0427
    ChrTalk(
        0xD,
        (
            "歓楽街の喧騒は昔から\x01",
            "何一つ変わっておらんわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xD,
        (
            "……ついでにちーっとばかり\x01",
            "治安が悪い所もな。\x01",
            "素人は気を付けることじゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7655")

    label("loc_759B")


    #C0429
    ChrTalk(
        0xD,
        (
            "クロスベルがいかに変わろうとも\x01",
            "歓楽街だけは無くならんじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xD,
        (
            "バーに賭博場、溢れる観光客に\x01",
            "群がるギャルたち㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xD,
        (
            "姿かたちは変化しようとも\x01",
            "昔から何一つ変わっておらんよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7655")

    Jump("loc_7C45")

    label("loc_765A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7799")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_76B6")

    #C0432
    ChrTalk(
        0xD,
        (
            "昨日は大負けしてしまったんじゃ。\x01",
            "何とか取り返してやらんとのー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7794")

    label("loc_76B6")


    #C0433
    ChrTalk(
        0xD,
        "おお、今日は調子がいいわい。\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xD,
        (
            "さーて、昨日の負けを\x01",
            "取り返してやるかの！\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x104,
        (
            "#0300F久々に来てみりゃあ\x01",
            "相変わらずだな、爺さん。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xD,
        "ほっほ、ランディか。\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xD,
        (
            "そりゃあそうじゃよ。\x01",
            "スロットはワシの日課じゃもの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7794")

    Jump("loc_7C45")

    label("loc_7799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_78B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7810")

    #C0438
    ChrTalk(
        0xD,
        (
            "ワシはカジノだけが\x01",
            "生き甲斐なんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xD,
        (
            "嫌じゃ嫌じゃ、ワシから\x01",
            "カジノを奪わんでくれい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78AB")

    label("loc_7810")


    #C0440
    ChrTalk(
        0xD,
        (
            "婆さんめ、今朝は\x01",
            "玄関先で待ち伏せしておったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xD,
        "眉を吊り上げて一喝しおってな。\x02",
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xD,
        (
            "危なく連れ戻される所じゃった。\x01",
            "ふう、まさに間一髪じゃよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_78AB")

    Jump("loc_7C45")

    label("loc_78B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7A64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7954")

    #C0443
    ChrTalk(
        0xD,
        (
            "歓楽街で遊び歩いて５０年……\x01",
            "わしはこの辺りが出来た頃からの\x01",
            "超常連さんなんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xD,
        (
            "ランディよ、お主なんぞ\x01",
            "まだまだヒヨッコじゃわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A5F")

    label("loc_7954")


    #C0445
    ChrTalk(
        0xD,
        (
            "わしはこの歓楽街で遊び歩いて\x01",
            "５０年になるんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xD,
        (
            "ランディよ、お主なんぞ\x01",
            "まだまだヒヨッコじゃわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x104,
        (
            "#0300Fうーん、確かに……\x01",
            "俺はせいぜい\x01",
            "１年半ってトコだからな……\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x103,
        (
            "#0200F……ランディさん、\x01",
            "そんな低レベルなところで\x01",
            "張り合わなくてもいいのでは？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7A5F")

    Jump("loc_7C45")

    label("loc_7A64")

    SetChrSubChip(0xD, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7ACB")

    #C0449
    ChrTalk(
        0xD,
        (
            "今いい所なんじゃ、\x01",
            "話しかけるんじゃないわい！\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xD,
        "……おおっ、来た来たぁ～！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C45")

    label("loc_7ACB")


    #C0451
    ChrTalk(
        0x104,
        (
            "#0300Fよう、リッケ爺さん。\x01",
            "今日の調子はどうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xD,
        "あん？　その声はランディか？\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xD,
        (
            "今いい所なんじゃ、\x01",
            "話しかけるんじゃないわい！\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x104,
        (
            "#0300Fははっ、相変わらず\x01",
            "調子いいみてえだな～。\x02\x03",

            "でもあんま遊びすぎると\x01",
            "また婆さんに\x01",
            "怒られるんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0xD,
        (
            "むほほ、それはそれじゃて！\x01",
            "むほほほほ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x101,
        (
            "#0000F（ランディのカジノ友達って\x01",
            "  調子のこういう人ばかりなのかな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7C45")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_69DF end

    def Function_15_7C4D(): pass

    label("Function_15_7C4D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7D0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_7CA2")

    #C0457
    ChrTalk(
        0xE,
        (
            "畜生、あのカウンターの女……\x01",
            "まさに魔性の女だぜ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D05")

    label("loc_7CA2")


    #C0458
    ChrTalk(
        0xE,
        (
            "あのう……\x01",
            "ミラを貸してくれませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0xE,
        (
            "帰りの鉄道代を\x01",
            "巻き上げられちゃったんですよー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_7D05")

    Jump("loc_7E49")

    label("loc_7D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7D5D")

    #C0460
    ChrTalk(
        0xE,
        "ううっ、くそ……\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xE,
        (
            "次こそ……次こそ\x01",
            "あの女を負かしてやるぜ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E49")

    label("loc_7D5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_7DB4")

    #C0462
    ChrTalk(
        0xE,
        (
            "ああいうタイプの女は\x01",
            "気に食わねえんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xE,
        "ハッ、泣かしてやるぜ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E49")

    label("loc_7DB4")


    #C0464
    ChrTalk(
        0xE,
        "ああ畜生、また負けちまったよ。\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xE,
        (
            "あのカウンター席の女、\x01",
            "ありゃあ相当やりこんでるな……\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0xE,
        (
            "いや、今度こそ……\x01",
            "次こそ絶対負かしてやるぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_7E49")

    TalkEnd(0xFE)
    Return()

    # Function_15_7C4D end

    def Function_16_7E4D(): pass

    label("Function_16_7E4D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7F1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_7EAD")

    #C0467
    ChrTalk(
        0xF,
        "７戦６敗など……有り得ん……\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xF,
        "ああ、勝負師としての自信が……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F19")

    label("loc_7EAD")


    #C0469
    ChrTalk(
        0xF,
        (
            "だ、だめだ……\x01",
            "カード台の女に\x01",
            "全て持っていかれた……\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xF,
        (
            "俺は一度国に戻り\x01",
            "やり直すことにするぞ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_7F19")

    Jump("loc_8120")

    label("loc_7F1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8001")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_7F9B")

    #C0471
    ChrTalk(
        0xF,
        (
            "諸国でカジノ巡りしてきた\x01",
            "俺が言うのだ、間違いは無い。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xF,
        (
            "クロスベルの勝負師は\x01",
            "相当強いぞ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FFC")

    label("loc_7F9B")


    #C0473
    ChrTalk(
        0xF,
        (
            "く、くそう……今度は\x01",
            "ルーレットを試してみたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xF,
        (
            "強い……！\x01",
            "この店の連中は強いぞ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_7FFC")

    Jump("loc_8120")

    label("loc_8001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_8089")

    #C0475
    ChrTalk(
        0xF,
        (
            "あのカード台の女、\x01",
            "中々やるな……\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xF,
        (
            "だが、俺は勝負師だ。\x01",
            "女だろうが容赦はせん。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0xF,
        "次は全力でやらせてもらうぞ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8120")

    label("loc_8089")


    #C0478
    ChrTalk(
        0xF,
        (
            "俺は諸国を回って\x01",
            "カジノで修行をしてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xF,
        (
            "フ……今年はこのクロスベルで\x01",
            "勝負させてもらおうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0xF,
        (
            "より一層強い\x01",
            "勝負師になるためにな……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8120")

    TalkEnd(0xFE)
    Return()

    # Function_16_7E4D end

    def Function_17_8124(): pass

    label("Function_17_8124")

    TalkBegin(0xFE)

    #C0481
    ChrTalk(
        0x10,
        "ま、待て、何だそれは……\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x10,
        (
            "ストレートフラッシュ！？\x01",
            "在り得ないだろ！！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_8124 end

    def Function_18_817A(): pass

    label("Function_18_817A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_820E")
    Jump("loc_8258")

    label("loc_820E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_822E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8258")

    label("loc_822E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_824E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8258")

    label("loc_824E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8258")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 3)), scpexpr(EXPR_END)), "loc_8350")

    #C0483
    ChrTalk(
        0x11,
        (
            "#3504Fさーて、ミッションはクリアしたが、\x01",
            "このまま帰るってのもツマランなぁ。\x02\x03",

            "#3510F……ま、ここからは\x01",
            "個人的に動かせてもらうとするか。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x101,
        (
            "#0013F（ミッション……\x01",
            "  いったい何のことだ……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_874D")

    label("loc_8350")


    #C0485
    ChrTalk(
        0x11,
        (
            "#3505Fよー、お疲れ～。\x01",
            "あの男の様子はどうよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x101,
        (
            "#0003Fそれは……申し訳ないですが\x01",
            "直接はお答えしかねます。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x102,
        (
            "#0106Fとりあえずは\x01",
            "落ち着いたみたいですから……\x02\x03",

            "#0100F後で謝罪を要求するくらいは\x01",
            "できるかと思いますけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x11,
        (
            "#3509Fハハハ、なんだそりゃ。\x02\x03",

            "#3500Fそういうつもりで\x01",
            "負かしたんじゃないんだがなァ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0489
    ChrTalk(
        0x101,
        (
            "#0011Fまさか……\x01",
            "あの最後の手は狙って……？\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x104,
        (
            "#0303Fいやいや、あり得ないぜ。\x01",
            "どう見ても幸運な偶然だっつーの。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x11,
        (
            "#3509Fおう、偶然偶然。\x01",
            "きっと日頃の善行のお陰だなァ～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0492
    ChrTalk(
        0x101,
        (
            "#0008F（……まさか……\x01",
            "  本当に狙ってやったのか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x104,
        (
            "#0301F（判らん、俺も\x01",
            "  自信がなくなってきた……）\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x103,
        (
            "#0211F（……この人なら可能性は\x01",
            "  ゼロではないかと……）\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x11,
        (
            "#3504Fま……俺は少し\x01",
            "手を貸してやっただけだしな。\x02\x03",

            "あいつは遅かれ早かれ\x01",
            "ああなっていた。\x01",
            "予定より早かったっつーだけのことさ。\x02\x03",

            "#3502Fクック……というわけで\x01",
            "後の面倒はよろしく～。\x01",
            "くれぐれも目を離さねえようにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x101,
        "#0001Fはい、それはもちろん……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD1, 3)

    label("loc_874D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_18_817A end

    def Function_19_8755(): pass

    label("Function_19_8755")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1200, 500, 10850, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 0, 0, -6250, 0)
    SetChrPos(0x102, -1000, 0, -5500, 0)
    SetChrPos(0x103, 1000, 0, -4500, 0)
    SetChrPos(0x104, 0, 0, -3900, 0)
    OP_68(-1360, 500, 6970, 3000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    Fade(500)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xD, 0x8000)
    OP_68(6530, 5500, 10270, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20800, 0)
    OP_68(-1050, 5500, 21040, 5000)
    MoveCamera(41, 24, 0, 5000)
    SetCameraDistance(20800, 5000)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 1500, -5000, 0)
    MoveCamera(49, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    OP_0D()
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xD, 0x8000)

    #C0497
    ChrTalk(
        0x104,
        "#0309Fよーし、今日も遊ぶかぁ！\x02",
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x103,
        (
            "#11P#0200Fランディさんは事あるごとに\x01",
            "カジノに立ち寄ろうとしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x102,
        (
            "#6P#0106F見回りのはずが意気揚々と\x01",
            "遊び始めるのよねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x101,
        (
            "#12P#0003F情報収集の意味もあるし\x01",
            "全く遊ぶなとは言わないけど……\x02\x03",

            "#0000F……ランディ、節度を保ってな。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(828, 0, 100, 0)
    SetChrName("")

    #A0501
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※カジノに置いてある遊具で遊ぶためには、\x01",
            "  受付に話しかけて手持ちのミラを\x01",
            "  メダルに交換してもらう必要があります。\x02\x03",

            "※メダルはミラに換金できませんが、\x01",
            "  集めると豪華な景品と交換することができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    FadeToBright(300, 0)
    SetChrPos(0x0, 0, 0, -5000, 0)
    SetScenarioFlags(0x6D, 5)
    EventEnd(0x5)
    Return()

    # Function_19_8755 end

    def Function_20_8ABD(): pass

    label("Function_20_8ABD")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "スロットで遊ぶ\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B4B")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_8B4B")

    TalkEnd(0xFF)
    Return()

    # Function_20_8ABD end

    def Function_21_8B4F(): pass

    label("Function_21_8B4F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, -500, 14500, 0)
    MoveCamera(30, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -100, 0, -5300, 0)
    SetChrPos(0x102, 1100, 0, -4900, 330)
    SetChrPos(0x103, -1100, 0, -4900, 30)
    SetChrPos(0x104, 0, 0, -3700, 0)
    OP_68(0, 500, 7500, 6000)
    SetCameraDistance(25000, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 1000, -2700, 0)
    MoveCamera(30, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)

    def lambda_8C2B():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF574, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8C2B)
    WaitChrThread(0x104, 1)
    OP_0D()

    #C0502
    ChrTalk(
        0x104,
        "#0302F#11Pそろそろカジノも夜の部か。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0503
    ChrTalk(
        0x104,
        (
            "#0309F#5Pそんじゃあ適当に遊びながら\x01",
            "例の鉱員の聞き込みでもするか！\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x101,
        "#12P#0006Fいや、駄目だって。\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x103,
        (
            "#12P#0211F潜入捜査でもないのに\x01",
            "遊ぶ必要は全く無いかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x102,
        (
            "#0103F#12Pとにかく従業員の人や\x01",
            "お客さんに聞いてみましょう。\x02\x03",

            "#0100Fガンツさんの消息について\x01",
            "何か掴めるかもしれないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x104,
        "#0306F#5Pへいへい、了解。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, -4700, 0)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xC1, 5)
    OP_C7(0x0, 0x1000)
    EventEnd(0x5)
    Return()

    # Function_21_8B4F end

    def Function_22_8DDF(): pass

    label("Function_22_8DDF")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(1000)
    OP_68(-900, 5000, 20000, 0)
    MoveCamera(53, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -1100, 4000, 17400, 0)
    SetChrPos(0x102, 200, 4000, 17800, 0)
    SetChrPos(0x103, -2000, 4000, 17800, 0)
    SetChrPos(0x104, -900, 4000, 18700, 0)
    SetChrPos(0x8, -900, 4000, 21300, 180)
    OP_0D()

    #C0508
    ChrTalk(
        0x8,
        "#5Pおや、これは皆さん。\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x8,
        (
            "#5Pランディと一緒に\x01",
            "遊びに来られたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x101,
        "#12P#0001Fいえ、実は……\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x104,
        (
            "#0300F#11Pちょいとオーナーに\x01",
            "聞きたい事があるんだけどよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0512
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "行方不明になっている\x01",
            "ガンツ鉱員について訊ねてみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0513
    ChrTalk(
        0x8,
        (
            "#5P行方不明？\x01",
            "ハハ、そんな馬鹿な。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x8,
        (
            "#5P今日だってウチに遊びに来て\x01",
            "荒稼ぎして行かれましたが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0515
    ChrTalk(
        0x101,
        "#12P#0005Fほ、本当ですか？\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x102,
        "#0105F#12Pしかも荒稼ぎって……\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x104,
        (
            "#0301F#11Pおいおい、オーナー。\x01",
            "人違いじゃねえだろうな？\x02\x03",

            "俺たちが捜してんのは\x01",
            "マインツの鉱員をやってる\x01",
            "ツキもカンもねぇ野郎だぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x8,
        "#5Pああ、勿論その方のことさ。\x02",
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x8,
        (
            "#5P２週間前になるか……\x01",
            "久々に顔を見せたかと思ったら\x01",
            "別人のように強くなっててな。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x8,
        (
            "#5Pおかげでウチのディーラーは負け続き。\x01",
            "５０万ミラくらい持っていかれてるよ。\x02",
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

    #C0521
    ChrTalk(
        0x101,
        "#12P#0011Fご、５０万ミラ！？\x02",
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x103,
        "#12P#0205Fかなりの大金ですね……\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x104,
        (
            "#0306F#11Pおいおい、マジかよ……\x02\x03",

            "#0301Fなんかイカサマをやってるとか\x01",
            "そんなんじゃねえんだよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x8,
        (
            "#5P私たちもプロだ。\x01",
            "イカサマがあれば気付くさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x8,
        (
            "#5Pとにかく異常にカンが冴えてる上に\x01",
            "あり得ないほどのツキの良さでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x8,
        (
            "#5P一体、彼に何があったのか\x01",
            "こちらも知りたいくらいなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x104,
        "#0303F#11Pむう……\x02",
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x102,
        (
            "#0106F#12P町長さんから聞いた話と\x01",
            "随分違っているみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x101,
        (
            "#12P#0003Fあの、オーナー。\x02\x03",

            "#0001Fガンツさんは鉱山町には\x01",
            "ずっと帰っていないそうですが……\x02\x03",

            "滞在場所はご存知ありませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x8,
        "#5Pああ、それなら……\x02",
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x8,
        (
            "#5Pすぐ近くにあるホテルに\x01",
            "毎日泊まっておられますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x8,
        (
            "#5Pそれも確か、最上階にある\x01",
            "デラックスルームだった筈です。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0533
    ChrTalk(
        0x101,
        (
            "#12P#0005Fあの高級ホテルの\x01",
            "デラックスルームですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x104,
        (
            "#0306F#11Pおいおい……\x01",
            "どんなお大尽#4Rだいじん#だっつーの。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0535
    ChrTalk(
        0x103,
        (
            "#6P#0202Fでも、意外とすぐに\x01",
            "消息が判明しましたね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    #C0536
    ChrTalk(
        0x102,
        (
            "#0100F#11Pええ……\x01",
            "早速、訪ねてみましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x8, -900, 4000, 21300, 180)
    SetChrPos(0x0, -900, 4000, 17500, 180)
    OP_4C(0x8, 0xFF)
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    SetScenarioFlags(0xC1, 6)
    OP_29(0x4A, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_22_8DDF end

    def Function_23_96C8(): pass

    label("Function_23_96C8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07400.itc", 0x1E)
    LoadChrToIndex("chr/ch07402.itc", 0x1F)
    LoadChrToIndex("chr/ch37600.itc", 0x20)
    LoadChrToIndex("chr/ch37602.itc", 0x21)
    LoadChrToIndex("chr/ch23200.itc", 0x22)
    OP_68(0, 0, 3000, 0)
    MoveCamera(55, 25, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, -700, 0, -5800, 0)
    SetChrPos(0x102, 700, 0, -5800, 0)
    SetChrPos(0x103, -700, 0, -6900, 0)
    SetChrPos(0x104, 700, 0, -6900, 0)
    SetChrPos(0x13D, 0, 0, -8000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 102200, 100, 5000, 270)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 97800, 100, 5000, 90)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x12, 0x22)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 0, -1000, 3000, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 101300, 0, 1600, 315)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    ClearMapFlags(0x10000000)
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis085.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis086.itp")
    SetCameraDistance(26500, 3000)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_98D0():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_98D0)

    def lambda_98EA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_98EA)
    Sleep(50)

    def lambda_98FE():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_98FE)

    def lambda_9918():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9918)
    Sleep(50)

    def lambda_992C():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_992C)

    def lambda_9946():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9946)
    Sleep(50)

    def lambda_995A():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_995A)

    def lambda_9974():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9974)
    Sleep(50)

    def lambda_9988():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13D, 1, lambda_9988)

    def lambda_99A2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13D, 2, lambda_99A2)
    Sleep(1300)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x12, 0xB4, 0x1F4)

    #C0537
    ChrTalk(
        0x12,
        "おお、来てくれたか！\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x12,
        (
            "ありがたい！\x01",
            "いつ喧嘩が始まるものかと……！\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x101,
        (
            "#0013Fそれで、ガンツさんと\x01",
            "相手のお客さんは！？\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x12,
        "ああ……\x02",
    )

    CloseMessageWindow()

    def lambda_9A66():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_9A66)
    OP_68(-3000, 0, 20200, 2500)
    MoveCamera(33, 15, 0, 2500)
    OP_6F(0x41)

    #C0541
    ChrTalk(
        0x12,
        (
            "あちらの奥にある特別室で\x01",
            "一対一の勝負をしているんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x12,
        (
            "早くしないとガンツが相手に\x01",
            "暴力を振るうかもしれない……！\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x101,
        "#0011Fへ……\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x102,
        (
            "#0105Fガンツさんが相手の\x01",
            "逆恨みを買ったんじゃ……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x9C4)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    OP_68(100200, 1000, 2000, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 99900, 0, -7000, 0)
    SetChrPos(0x102, 99900, 0, -7000, 0)
    SetChrPos(0x103, 99900, 0, -7000, 0)
    SetChrPos(0x104, 99900, 0, -7000, 0)
    SetChrPos(0x13D, 99900, 0, -7000, 0)
    SetChrPos(0x12, 99900, 0, -7000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(100570, 1000, 5280, 4000)
    Sleep(10)
    PlayBGM("ed7518", 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0545
    ChrTalk(
        0x13,
        "#5Pおーし、コイツでどうだ！\x02",
    )

    CloseMessageWindow()
    Sound(90, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    SetChrName("")

    #A0546
    AnonymousTalk(
        0x13,
        (
            "ダイヤの９、１０、Ｊ、Ｑ、Ｋの\x01",
            "ストレートフラッシュ！\x02\x03",

            "これ以上の手はねえだろうが！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0547
    AnonymousTalk(
        0x14,
        (
            "#3507Fぐはっ、マジかよ！\x02\x03",

            "#3506Fまさか最後の大勝負で\x01",
            "そんな手で来るとはなァ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_63(0x13, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0548
    ChrTalk(
        0x13,
        (
            "#5Pハッ！\x01",
            "これが俺様の実力なんだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x13,
        (
            "#5P……セコイ手で何度も\x01",
            "引き分けに持ち込みやがったが\x01",
            "これでケリを付けてやる……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0550
    ChrTalk(
        0x13,
        "#5P#4Sとっとと手を晒#2Rさら#して往生しろや！\x02",
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0551
    ChrTalk(
        0x14,
        (
            "#11P#3505Fん、なに言ってんだ？\x02\x03",

            "#3510F負けたなんてオレは\x01",
            "一言も言ってないだろうが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0552
    ChrTalk(
        0x13,
        "#5Pフ、フカシこいてんじゃねえ！\x02",
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x13,
        (
            "#5P俺の手に勝てるとしたら\x01",
            "ロイヤルストレートフラッシュしか\x01",
            "残ってねぇんだぞ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x13,
        "#5Pそんなモンがそうそう出るはずが──\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x14,
        "#11P#3504F残念──ハズレだ。\x02",
    )

    CloseMessageWindow()
    Sound(90, 0, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)
    SetChrName("")

    #A0556
    AnonymousTalk(
        0x13,
        "……………………え゛。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0557
    AnonymousTalk(
        0x8,
        (
            "ファイブ・オブ・ア・カインド……\x01",
            "しかもＡ#2Rエース#のファイブカードですか！！\x02\x03",

            "いやはや、まさかこの場面で\x01",
            "お目にかかれるとは……！！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0558
    AnonymousTalk(
        0x14,
        (
            "#3504Fロイヤルストレートフラッシュを\x01",
            "上回るかはルール次第だが……\x02\x03",

            "#3500Fどっちにしてもアンタの手#10Rストレートフラッシュ#よりは\x01",
            "上なのは間違いないだろ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)

    #C0559
    ChrTalk(
        0x13,
        "#5P#60Wふ、ふ、ふ、ふ……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)

    def lambda_A15A():
        OP_9D(0xFE, 0x18060, 0x0, 0x1388, 0x64, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_A15A)
    WaitChrThread(0x8, 1)
    Sound(819, 0, 100, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)

    #C0560
    ChrTalk(
        0x13,
        "#5P#4Sふざけんな！　イカサマだ！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x8, 500)

    #C0561
    ChrTalk(
        0x13,
        (
            "#5Pおいオーナー！\x01",
            "てめぇグルしてやがったな！？\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x8,
        (
            "#11Pと、とんでもない！\x01",
            "女神に誓ってありませんとも！\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x8,
        (
            "#11Pそれと私が見る限り……\x01",
            "レクター様がイカサマを使っていた\x01",
            "形跡もありませんでした！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x0, 0x64, 0xBB8, 0x12C)

    #C0564
    ChrTalk(
        0x13,
        (
            "#5Pるせえっ！！\x01",
            "そんなのが信じられるかあッ！！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(101140, 1000, 4800, 1000)

    def lambda_A2DF():

        label("loc_A2DF")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_A2DF")

    QueueWorkItem2(0x8, 2, lambda_A2DF)

    def lambda_A2F1():
        OP_95(0xFE, 98400, 0, 2100, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_A2F1)
    WaitChrThread(0x13, 1)

    def lambda_A30F():
        OP_95(0xFE, 100800, 0, 1600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_A30F)
    Sleep(50)
    SetChrSubChip(0x14, 0x1)
    WaitChrThread(0x13, 1)
    EndChrThread(0x8, 0x2)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x4)
    Sound(804, 0, 100, 0)

    def lambda_A348():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A348)

    def lambda_A361():
        OP_96(0xFE, 0x18BB4, 0xC8, 0x640, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A361)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    ClearChrFlags(0x8, 0x20)

    #C0565
    ChrTalk(
        0x13,
        (
            "#5P俺は最高のツキとカンを\x01",
            "手に入れたんだああッ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x13,
        (
            "#5Pこんなふざけた野郎に\x01",
            "負けるはずがないだろうがあッ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x8,
        "お、お客様……\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x14,
        (
            "#5P#3505Fおいおい、落ち着けよ～。\x02\x03",

            "#3504F──ま、勝負は時の運。\x02\x03",

            "#3501Fアンタの運もここまで\x01",
            "だったってことサ！（キリッ）\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x13,
        "#5P#40W……………………………………\x02",
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    Sound(819, 0, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    def lambda_A4D6():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A4D6)

    def lambda_A4EF():
        OP_9D(0xFE, 0x19960, 0x0, 0x640, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A4EF)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)

    #C0570
    ChrTalk(
        0x8,
        "#1Pゲホゲホッ……\x02",
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x13,
        (
            "#5P#40Wあり得ねぇ……\x01",
            "俺が負けるはずねえんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x13,
        (
            "#5P#40Wアレを使った俺が\x01",
            "ギャンブルで負けるはずが……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(100200, 1000, -1500, 2000)
    SetCameraDistance(23500, 2000)
    Sound(103, 0, 100, 0)

    def lambda_A5BB():
        OP_96(0xFE, 0x18894, 0x0, 0xFFFFF63C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A5BB)

    def lambda_A5D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A5D5)
    Sleep(200)

    def lambda_A5E9():
        OP_96(0xFE, 0x18380, 0x0, 0xFFFFF510, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A5E9)

    def lambda_A603():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_A603)
    Sleep(450)
    BeginChrThread(0x104, 3, 0, 25)
    Sleep(450)
    BeginChrThread(0x103, 3, 0, 24)
    Sleep(450)

    def lambda_A629():
        OP_96(0xFE, 0x1863C, 0x0, 0xFFFFEFFC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A629)

    def lambda_A643():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A643)
    Sleep(200)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(200)

    def lambda_A68D():
        OP_96(0xFE, 0x1863C, 0x0, 0xFFFFEAE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13D, 1, lambda_A68D)

    def lambda_A6A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13D, 2, lambda_A6A7)
    Sleep(800)
    OP_6F(0x11)

    #C0573
    ChrTalk(
        0x12,
        "#6Pガンツ……！？\x02",
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x101,
        "#0013F#12Pいけない……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x13, 0x0, 0x2BC)
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0575
    ChrTalk(
        0x13,
        "#11P#4S負けるはずがねえんだよおお！！\x02",
    )

    CloseMessageWindow()
    OP_68(101350, 1000, 3170, 1500)
    MoveCamera(45, 19, 0, 1500)
    BeginChrThread(0x101, 3, 0, 26)
    Sleep(50)
    BeginChrThread(0x12, 3, 0, 27)
    Sleep(300)

    def lambda_A766():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A766)
    Sleep(50)

    def lambda_A783():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A783)
    Sleep(50)

    def lambda_A7A0():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A7A0)
    Sleep(50)

    def lambda_A7BD():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13D, 1, lambda_A7BD)

    def lambda_A7D7():
        OP_96(0xFE, 0x18A88, 0x0, 0xA28, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_A7D7)
    WaitChrThread(0x13, 1)
    Sound(804, 0, 100, 0)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x103, 1)

    def lambda_A807():
        TurnDirection(0xFE, 0x13, 700)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A807)
    OP_6F(0x41)
    Sleep(300)
    Sound(819, 0, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    def lambda_A830():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_A830)

    #C0576
    ChrTalk(
        0x13,
        (
            "#4S#11Pおおおおっ！\x01",
            "離せ、離しやがれえええっ！！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 2)

    #C0577
    ChrTalk(
        0x101,
        (
            "#0007Fお、落ち着いてください！\x02\x03",

            "#0010F（って、何だこの力は……！？）\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x12,
        (
            "#6Pガンツ！\x01",
            "どうか落ち着きなさい！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0579
    ChrTalk(
        0x14,
        (
            "#5P#3505Fおお、アンタらか～。\x02\x03",

            "#3509Fどうよ、元気してた？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0580
    ChrTalk(
        0x102,
        (
            "#12P#0106Fふう……\x01",
            "呑気に挨拶されても。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x103,
        (
            "#6P#0211F#N……相変わらず\x01",
            "色々と怪しすぎです。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0582
    ChrTalk(
        0x13D,
        (
            "#12P#2102Fへえ、面白い子ねぇ。\x01",
            "あなたたちの知り合いなの？\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x104,
        (
            "#0306Fいや、知り合いっつーほど\x01",
            "知ってるわけじゃねえが──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0584
    ChrTalk(
        0x104,
        (
            "#0305Fって、ストレートフラッシュと\x01",
            "ファイブカードだと！？\x02\x03",

            "#0307Fオイオイオイ！？\x01",
            "なんつー勝負してんだよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x14,
        (
            "#5P#3510Fいや～、危なかったぜェ。\x02\x03",

            "#3504F負けたら身ぐるみ剥がされる\x01",
            "寸前だったんだけどよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x102,
        "#12P#0111Fよ、よく分からないけど……\x02",
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x103,
        (
            "#6P#0206F何とか傷害沙汰だけは\x01",
            "回避できたみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(804, 0, 100, 0)
    Sound(819, 0, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    def lambda_ABFA():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_ABFA)

    #C0588
    ChrTalk(
        0x13,
        "#11P#5S離せ、離しやがれえええっ！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(804, 0, 100, 0)
    Sound(819, 0, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0589
    ChrTalk(
        0x13,
        (
            "#11P#4S俺は……俺は絶対に\x01",
            "負けるはずがないんだああああ！！！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrName("")

    #A0590
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ガンツ鉱員は\x01",
            "あらん限りの力で暴れ喚いてから\x01",
            "不意にぐったりと気絶してしまった。\x02\x03",

            "ロイドたちはホテルの部屋まで\x01",
            "気絶した彼を運ぶことにした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0450", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_96C8 end

    def Function_24_AD6E(): pass

    label("Function_24_AD6E")


    def lambda_AD73():
        OP_96(0xFE, 0x1863C, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AD73)

    def lambda_AD8D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AD8D)
    WaitChrThread(0x103, 1)

    def lambda_ADA2():
        OP_95(0xFE, 98700, 0, -4100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ADA2)
    WaitChrThread(0x103, 1)

    def lambda_ADC0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_ADC0)
    Return()

    # Function_24_AD6E end

    def Function_25_ADC9(): pass

    label("Function_25_ADC9")


    def lambda_ADCE():
        OP_96(0xFE, 0x1863C, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ADCE)

    def lambda_ADE8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_ADE8)
    WaitChrThread(0x104, 1)

    def lambda_ADFD():
        OP_95(0xFE, 101100, 0, -4100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ADFD)
    WaitChrThread(0x104, 1)

    def lambda_AE1B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AE1B)
    Return()

    # Function_25_ADC9 end

    def Function_26_AE24(): pass

    label("Function_26_AE24")


    def lambda_AE29():
        OP_95(0xFE, 101600, 0, 2600, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AE29)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x13, 700)
    Return()

    # Function_26_AE24 end

    def Function_27_AE4A(): pass

    label("Function_27_AE4A")


    def lambda_AE4F():
        OP_95(0xFE, 100400, 0, 2600, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_AE4F)
    WaitChrThread(0x12, 1)
    TurnDirection(0x12, 0x13, 700)
    Return()

    # Function_27_AE4A end

    def Function_28_AE70(): pass

    label("Function_28_AE70")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    Fade(500)
    OP_68(4030, -100, 7770, 0)
    MoveCamera(49, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21440, 0)
    SetChrPos(0x101, 2140, -1000, 8000, 90)
    SetChrPos(0x102, 3160, -1000, 6510, 90)
    SetChrPos(0x103, 1840, -1000, 6510, 90)
    SetChrPos(0x104, 3560, -1000, 8000, 90)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    OP_0D()

    #C0591
    ChrTalk(
        0x9,
        "#11Pようこそ《バルカ》へ～！\x02",
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x9,
        (
            "#11Pあ、ランディさんだ。\x01",
            "いらっしゃ～い！\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x104,
        (
            "#6P#0300Fようチェリーちゃん、\x01",
            "ちょっと聞きてえんだが。\x02\x03",

            "確かここの景品に\x01",
            "《みっしぃ》のぬいぐるみって\x01",
            "あったよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x9,
        "#11Pうんうん、一番安い景品よ☆\x02",
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x9,
        (
            "#11P結構人気あるから\x01",
            "無くなりがちだけど～、\x01",
            "今日は並べておこっかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x9,
        (
            "#11Pでもランディさんって\x01",
            "あんなのにも興味あったんだ～。\x01",
            "カ・ワ・イ・イ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x104,
        "#6P#0309Fなははは、そうか～？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    def lambda_B0AE():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B0AE)

    def lambda_B0BB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B0BB)
    Sleep(500)

    #C0598
    ChrTalk(
        0x104,
        "#5P#0300Fどうだ、本当の話だったろ？\x02",
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x102,
        "#11P#0100Fそうみたいね。\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x103,
        (
            "#12P#0203F……ロイドさん、\x01",
            "困っている人もいることですし。\x02\x03",

            "#0201Fとにかく一度\x01",
            "試してみましょう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 300)
    Sleep(300)

    #C0601
    ChrTalk(
        0x101,
        (
            "#5P#0000Fああ……そうだな。\x02\x03",

            "#0003F（気のせいか……ティオの\x01",
            "  目の輝きが増したような……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 2820, -1000, 7050, 90)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetScenarioFlags(0x70, 3)
    OP_29(0xC, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_28_AE70 end

    def Function_29_B209(): pass

    label("Function_29_B209")

    EventBegin(0x1)
    Sleep(50)

    #C0602
    ChrTalk(
        0x101,
        (
            "#0001Fカジノまで来たんだ、\x01",
            "ガンツさんの情報を集めてみよう。\x02\x03",

            "従業員や客の誰かが\x01",
            "消息を知っているかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 0, -5000, 0)
    EventEnd(0x4)
    Return()

    # Function_29_B209 end

    SaveToFile()

Try(main)
