from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1040.bin",                # FileName
        "t1040",                    # MapName
        "t1040",                    # Location
        0x0043,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 67, 0, 2, 0, 3],
    )

    BuildStringList((
        "t1040",                  # 0
        "リュート",               # 1
        "メーシェ",               # 2
        "婦人",                   # 3
        "観光客",                 # 4
        "観光客",                 # 5
        "観光客",                 # 6
        "観光客",                 # 7
        "観光客",                 # 8
        "観光客",                 # 9
        "観光客",                 # 10
        "ワジ",                   # 11
        "マーガレット夫人",       # 12
        "ウィノナ",               # 13
        "ドローナ",               # 14
        "観光客",                 # 15
        "エリィ",                 # 16
        "フラン",                 # 17
        "セシル",                 # 18
        "イリア",                 # 19
        "リーシャ",               # 20
    ))

    AddCharChip((
        "chr/ch25000.itc",                   # 00
        "chr/ch34500.itc",                   # 01
        "chr/ch33202.itc",                   # 02
        "chr/ch24002.itc",                   # 03
        "chr/ch21702.itc",                   # 04
        "chr/ch21802.itc",                   # 05
        "chr/ch21902.itc",                   # 06
        "chr/ch33102.itc",                   # 07
        "chr/ch44202.itc",                   # 08
        "chr/ch34402.itc",                   # 09
        "chr/ch27900.itc",                   # 0A
        "chr/ch26600.itc",                   # 0B
        "chr/ch33300.itc",                   # 0C
        "chr/ch03002.itc",                   # 0D
        "chr/ch00100.itc",                   # 0E
        "chr/ch08500.itc",                   # 0F
        "chr/ch07500.itc",                   # 10
        "chr/ch05100.itc",                   # 11
        "chr/ch05200.itc",                   # 12
        "chr/ch44002.itc",                   # 13
    ))

    DeclNpc(-104069, 0,       2980,    90,   261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-101099, 0,       5880,    90,   257,  0x0, 0,   1,   0,   0,   1,   0,   8,   255,  0)
    DeclNpc(-101819, 119,     -879,    270,  453,  0x0, 0,   2,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-104800, 119,     8930,    45,   453,  0x0, 0,   3,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-103000, 119,     10930,   225,  453,  0x0, 0,   4,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-97959,  119,     19090,   45,   453,  0x0, 0,   5,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-97959,  119,     19090,   45,   453,  0x0, 0,   6,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(-104800, 119,     8930,    45,   453,  0x0, 0,   7,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   8,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(-96120,  119,     20889,   225,  453,  0x0, 0,   9,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(-101790, 119,     1120,    270,  453,  0x0, 0,   13,  0,   255, 255, 0,   4,   255,  0)
    DeclNpc(-101790, 119,     -910,    270,  453,  0x0, 0,   19,  0,   255, 255, 0,   29,  255,  0)
    DeclNpc(-1860,   0,       10640,   180,  261,  0x0, 0,   10,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-6250,   0,       6099,    180,  261,  0x0, 0,   11,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(-8189,   0,       7510,    0,    389,  0x0, 0,   12,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(-4050,   0,       4530,    270,  389,  0x0, 0,   14,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-8170,   0,       7940,    270,  389,  0x0, 0,   15,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(4300,    0,       5079,    90,   389,  0x0, 0,   16,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   17,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   18,  0,   0,   0,   0,   17,  255,  0)

    DeclActor(-1770,   0,       8810,    1000,    -1860,   1500,    10640,   0x007E, 0,  24, 0x0000)
    DeclActor(-101650, 0,       2470,    1000,    -104070, 1500,    2980,    0x007E, 0,  6,  0x0000)

    ChipFrameInfo(980, 0)                                        # 0

    ScpFunction((
        "Function_0_3D4",          # 00, 0
        "Function_1_48C",          # 01, 1
        "Function_2_515",          # 02, 2
        "Function_3_74D",          # 03, 3
        "Function_4_7AC",          # 04, 4
        "Function_5_8C7",          # 05, 5
        "Function_6_A32",          # 06, 6
        "Function_7_A36",          # 07, 7
        "Function_8_E44",          # 08, 8
        "Function_9_104B",         # 09, 9
        "Function_10_1221",        # 0A, 10
        "Function_11_12AE",        # 0B, 11
        "Function_12_1339",        # 0C, 12
        "Function_13_13B2",        # 0D, 13
        "Function_14_143D",        # 0E, 14
        "Function_15_14C4",        # 0F, 15
        "Function_16_15C5",        # 10, 16
        "Function_17_164C",        # 11, 17
        "Function_18_16C2",        # 12, 18
        "Function_19_18E1",        # 13, 19
        "Function_20_19CF",        # 14, 20
        "Function_21_1BA9",        # 15, 21
        "Function_22_2129",        # 16, 22
        "Function_23_232C",        # 17, 23
        "Function_24_2ABE",        # 18, 24
        "Function_25_2AC2",        # 19, 25
        "Function_26_2DBB",        # 1A, 26
        "Function_27_2F9F",        # 1B, 27
        "Function_28_3043",        # 1C, 28
        "Function_29_30E9",        # 1D, 29
    ))


    def Function_0_3D4(): pass

    label("Function_0_3D4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_414"),
        (1, "loc_420"),
        (2, "loc_42C"),
        (3, "loc_438"),
        (4, "loc_444"),
        (5, "loc_450"),
        (6, "loc_45C"),
        (SWITCH_DEFAULT, "loc_468"),
    )


    label("loc_414")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_420")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_42C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_438")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_444")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_450")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_45C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_468")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_474")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_48B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_48B")

    Return()

    # Function_0_3D4 end

    def Function_1_48C(): pass

    label("Function_1_48C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_514")
    OP_95(0xFE, -98090, 0, 5880, 2000, 0x0)
    OP_95(0xFE, -98090, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 5880, 2000, 0x0)
    Jump("Function_1_48C")

    label("loc_514")

    Return()

    # Function_1_48C end

    def Function_2_515(): pass

    label("Function_2_515")

    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x10, 0x8)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    SetChrChipByIndex(0x12, 0xD)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrChipByIndex(0x13, 0x13)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_5CD")
    Jump("loc_74C")

    label("loc_5CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_5DB")
    Jump("loc_74C")

    label("loc_5DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_664")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x15, 1590, 0, 8900, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61F")
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1050, 0, 2180, 0)
    Jump("loc_655")

    label("loc_61F")

    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -1530, 0, 2530, 90)
    SetChrFlags(0x1B, 0x10)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -540, 0, 2530, 270)
    SetChrFlags(0x1A, 0x10)

    label("loc_655")

    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_74C")

    label("loc_664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_6F4")
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrSubChip(0xA, 0x2)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -103000, 120, 10930, 225)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x15, -1530, 0, 2530, 90)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -540, 0, 2530, 270)
    SetChrFlags(0x1A, 0x10)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_74C")

    label("loc_6F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_74C")
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x10, -96120, 120, 20890, 225)
    SetChrPos(0x15, -8189, 0, 8640, 180)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x10)

    label("loc_74C")

    Return()

    # Function_2_515 end

    def Function_3_74D(): pass

    label("Function_3_74D")

    SetMapObjFrame(0xFF, "t1040_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1040_sky_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "t1040_sky01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1040_sky01_y", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7AB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7AB")

    Return()

    # Function_3_74D end

    def Function_4_7AC(): pass

    label("Function_4_7AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_7BD")
    Jump("loc_8C3")

    label("loc_7BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_7CB")
    Jump("loc_8C3")

    label("loc_7CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_7D9")
    Jump("loc_8C3")

    label("loc_7D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_7E7")
    Jump("loc_8C3")

    label("loc_7E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_89E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_802")
    Call(0, 5)
    Jump("loc_899")

    label("loc_802")


    #C0001
    ChrTalk(
        0x12,
        (
            "#10304Fフフ、見ての通りクラブの\x01",
            "常連さんに捕まっちゃってね。\x02\x03",

            "#10300Fまあ、集合には遅れないように\x01",
            "早めに切り上げるつもりだから、\x01",
            "安心していいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_899")

    Jump("loc_8C3")

    label("loc_89E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_8AC")
    Jump("loc_8C3")

    label("loc_8AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_8BA")
    Jump("loc_8C3")

    label("loc_8BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_8C3")

    label("loc_8C3")

    TalkEnd(0xFE)
    Return()

    # Function_4_7AC end

    def Function_5_8C7(): pass

    label("Function_5_8C7")


    #C0002
    ChrTalk(
        0xA,
        (
            "ふふ、それにしても奇遇ねえ。\x01",
            "ワジ君がこっちに来てくれるなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xA,
        (
            "すぐに連絡くれれば、\x01",
            "いくらでも付き合ってあげるのに～。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x12,
        (
            "#10304Fフフ、今日は友人たちと来ていてさ。\x02\x03",

            "#10302F悪いけど、この後約束があるから\x01",
            "早めに切り上げさせてもらうよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xA,
        "あン、そんな素っ気無いところもステキ㈱\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#00006F（ホ、ホストって\x01",
            "  こんなのでいいのか……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0xA, 0x10)
    Return()

    # Function_5_8C7 end

    def Function_6_A32(): pass

    label("Function_6_A32")

    Call(0, 7)
    Return()

    # Function_6_A32 end

    def Function_7_A36(): pass

    label("Function_7_A36")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A43")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E40")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AA1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_AA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC1")
    OP_AF(0x66)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E3B")

    label("loc_AC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD5")
    Jump("loc_E3B")

    label("loc_AD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_AFC")
    Jump("loc_E3B")

    label("loc_AFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_CBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C14")

    #C0007
    ChrTalk(
        0x8,
        (
            "当レストランの\x01",
            "『フォルトゥナ』という名前には、\x01",
            "“幸福”という意味がございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "まさに幸福な食事を楽しめるよう、\x01",
            "お客様には最大限のサービスを\x01",
            "させていただいております。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "何かお気づきの点がございましたら、\x01",
            "ご遠慮なくお申し付け下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CB5")

    label("loc_C14")


    #C0010
    ChrTalk(
        0x8,
        (
            "幸福な食事を楽しめるよう、\x01",
            "お客様には最大限のサービスを\x01",
            "させていただいております。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "何かお気づきの点がございましたら、\x01",
            "ご遠慮なくお申し付け下さいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB5")

    Jump("loc_E3B")

    label("loc_CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_E3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9E")

    #C0012
    ChrTalk(
        0x8,
        "レストラン《フォルトゥナ》へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "当店では、最高の食材を用いた\x01",
            "最高の料理を、最高のロケーションで\x01",
            "お召し上がりいただけます。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "どうか、優雅で幸福な一時を\x01",
            "楽しんでいただけますよう……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E3B")

    label("loc_D9E")


    #C0015
    ChrTalk(
        0x8,
        (
            "当店では、最高の食材を用いた\x01",
            "最高の料理を、最高のロケーションで\x01",
            "お召し上がりいただけます。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "どうか、優雅で幸福な一時を\x01",
            "楽しんでいただけますよう……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3B")

    Jump("loc_A43")

    label("loc_E40")

    TalkEnd(0x8)
    Return()

    # Function_7_A36 end

    def Function_8_E44(): pass

    label("Function_8_E44")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_E55")
    Jump("loc_1047")

    label("loc_E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_EF2")

    #C0017
    ChrTalk(
        0xFE,
        (
            "テーマパークに最近、\x01",
            "新しいアトラクションが\x01",
            "設置されたらしいのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "噂じゃコワ～イやつらしいけど、\x01",
            "どんなアトラクションなのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1047")

    label("loc_EF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1047")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FD8")

    #C0019
    ChrTalk(
        0xFE,
        (
            "この間オープンしたレイクビーチは、\x01",
            "老若男女を問わず大人気らしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "まだまだ暑い日が続くし、\x01",
            "ミシュラムを訪れるお客さんも、\x01",
            "例年に比べて増えているみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "うーん、私も一度行ってみたいな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1047")

    label("loc_FD8")


    #C0022
    ChrTalk(
        0xFE,
        (
            "この間オープンしたレイクビーチは、\x01",
            "老若男女を問わず大人気らしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "うーん、私も一度行ってみたいな。\x02",
    )

    CloseMessageWindow()

    label("loc_1047")

    TalkEnd(0xFE)
    Return()

    # Function_8_E44 end

    def Function_9_104B(): pass

    label("Function_9_104B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_105C")
    Jump("loc_121D")

    label("loc_105C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1187")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1111")

    #C0024
    ChrTalk(
        0xFE,
        "あーあ、ワジ君が行ってしまったわ。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "かといって、家に帰っても\x01",
            "つまらない旦那の世話を\x01",
            "しなきゃいけないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        "しばらく１人で飲んでようかしら。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1182")

    label("loc_1111")


    #C0027
    ChrTalk(
        0xFE,
        "あーあ、ワジ君が行ってしまったわ。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "家で旦那の世話をするのもなんだし、\x01",
            "しばらく１人で飲んでようかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1182")

    Jump("loc_121D")

    label("loc_1187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1214")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AA")
    Call(0, 5)
    TalkEnd(0xFE)
    SetChrSubChip(0xA, 0x2)
    Return()

    label("loc_11AA")


    #C0029
    ChrTalk(
        0xFE,
        (
            "ワジ君ってホストなのに、\x01",
            "たまに素っ気無いのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        "……まあ、そこが素敵なんだけど㈱\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0xA, 0x2)
    Return()

    label("loc_1214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_121D")

    label("loc_121D")

    TalkEnd(0xFE)
    Return()

    # Function_9_104B end

    def Function_10_1221(): pass

    label("Function_10_1221")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1232")
    Jump("loc_12AA")

    label("loc_1232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1240")
    Jump("loc_12AA")

    label("loc_1240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_12AA")

    #C0031
    ChrTalk(
        0xFE,
        "ちょいと遅めの朝ごはんじゃ。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "ほっほっほ、モーニングにしては\x01",
            "豪華すぎるかもしれんがな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12AA")

    TalkEnd(0xFE)
    Return()

    # Function_10_1221 end

    def Function_11_12AE(): pass

    label("Function_11_12AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_12BF")
    Jump("loc_1335")

    label("loc_12BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_12CD")
    Jump("loc_1335")

    label("loc_12CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1335")

    #C0033
    ChrTalk(
        0xFE,
        "ううん、何を食べようかしら。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "まだまだ暑いし、どうせなら\x01",
            "涼しくなれるものがいいわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1335")

    TalkEnd(0xFE)
    Return()

    # Function_11_12AE end

    def Function_12_1339(): pass

    label("Function_12_1339")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_134A")
    Jump("loc_13AE")

    label("loc_134A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1358")
    Jump("loc_13AE")

    label("loc_1358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_13AE")

    #C0035
    ChrTalk(
        0xFE,
        "（カチャカチャ……）\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "うまいなあ、もぐもぐ……\x01",
            "くっちゃくっちゃ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13AE")

    TalkEnd(0xFE)
    Return()

    # Function_12_1339 end

    def Function_13_13B2(): pass

    label("Function_13_13B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_13C3")
    Jump("loc_1439")

    label("loc_13C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1430")

    #C0037
    ChrTalk(
        0xFE,
        (
            "そうね、貸切になってたのは\x01",
            "午前中だけみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        "ご飯を食べたら行ってみましょうか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1439")

    label("loc_1430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1439")

    label("loc_1439")

    TalkEnd(0xFE)
    Return()

    # Function_13_13B2 end

    def Function_14_143D(): pass

    label("Function_14_143D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_144E")
    Jump("loc_14C0")

    label("loc_144E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_14B7")

    #C0039
    ChrTalk(
        0xFE,
        (
            "ハハ、どうだい。\x01",
            "僕の選んだ店はなかなかだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "心行くまでこの味を楽しみたまえ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14C0")

    label("loc_14B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_14C0")

    label("loc_14C0")

    TalkEnd(0xFE)
    Return()

    # Function_14_143D end

    def Function_15_14C4(): pass

    label("Function_15_14C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_14D5")
    Jump("loc_15C1")

    label("loc_14D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_154B")

    #C0041
    ChrTalk(
        0xFE,
        (
            "（料理の味は\x01",
            "  かなりいいんだけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "（うーん、一緒に来る相手を\x01",
            "  間違えたわね、こりゃ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C1")

    label("loc_154B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_15C1")

    #C0043
    ChrTalk(
        0xFE,
        "ちょっと、ちょっとお父さんってば。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "こういう店はテーブルマナーに\x01",
            "うるさいんだから、気をつけてよね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C1")

    TalkEnd(0xFE)
    Return()

    # Function_15_14C4 end

    def Function_16_15C5(): pass

    label("Function_16_15C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_15D6")
    Jump("loc_1648")

    label("loc_15D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_163F")

    #C0045
    ChrTalk(
        0xFE,
        "あたし、暑くなってきちゃった。\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "ねえお母さん、昼からは\x01",
            "レイクビーチに行こうよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1648")

    label("loc_163F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1648")

    label("loc_1648")

    TalkEnd(0xFE)
    Return()

    # Function_16_15C5 end

    def Function_17_164C(): pass

    label("Function_17_164C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_165D")
    Jump("loc_16BE")

    label("loc_165D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_166B")
    Jump("loc_16BE")

    label("loc_166B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1679")
    Jump("loc_16BE")

    label("loc_1679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1699")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1691")
    Jump("loc_1694")

    label("loc_1691")

    Call(0, 20)

    label("loc_1694")

    Jump("loc_16BE")

    label("loc_1699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_16A7")
    Jump("loc_16BE")

    label("loc_16A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_16B5")
    Jump("loc_16BE")

    label("loc_16B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_16BE")

    label("loc_16BE")

    TalkEnd(0xFE)
    Return()

    # Function_17_164C end

    def Function_18_16C2(): pass

    label("Function_18_16C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_16D3")
    Jump("loc_18DD")

    label("loc_16D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_16E1")
    Jump("loc_18DD")

    label("loc_16E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_16EF")
    Jump("loc_18DD")

    label("loc_16EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1821")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1819")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1797")

    #C0047
    ChrTalk(
        0x1A,
        (
            "#01703Fうーん、この店の服は\x01",
            "あたしにはイマイチねー。\x02\x03",

            "#01702Fもっとこう、情熱的で\x01",
            "エキゾチックなのがあれば\x01",
            "よかったんだけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_1814")

    label("loc_1797")


    #C0048
    ChrTalk(
        0x1A,
        (
            "#01705Fそれにしても、\x01",
            "リーシャってば遅いわね。\x02\x03",

            "#01706F早く来ないと、\x01",
            "服を選んであげる時間が\x01",
            "なくなっちゃうじゃないの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1814")

    Jump("loc_181C")

    label("loc_1819")

    Call(0, 20)

    label("loc_181C")

    Jump("loc_18DD")

    label("loc_1821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_18C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_183C")
    Call(0, 19)
    Jump("loc_18C1")

    label("loc_183C")


    #C0049
    ChrTalk(
        0x1A,
        (
            "#01705Fあれ、そういえばリーシャは\x01",
            "まだ来ないのかしら？\x02\x03",

            "#01706Fあの子にも、\x01",
            "もうちょっとセクシーな服を\x01",
            "着せてあげたいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C1")

    Jump("loc_18DD")

    label("loc_18C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_18D4")
    Jump("loc_18DD")

    label("loc_18D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_18DD")

    label("loc_18DD")

    TalkEnd(0xFE)
    Return()

    # Function_18_16C2 end

    def Function_19_18E1(): pass

    label("Function_19_18E1")

    OP_4B(0x1A, 0xFF)
    OP_4B(0x15, 0xFF)

    #C0050
    ChrTalk(
        0x15,
        (
            "そうですねぇ、それでしたら\x01",
            "こちらのドレスなんかどうでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x1A,
        (
            "#01703Fふーむ、そうねえ……\x01",
            "もうちょっと派手めの方が\x01",
            "私的には好みなんだけど。\x02\x03",

            "#01702Fあ、帽子とかも見せてもらえる？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x15,
        "はい、こちらへどうぞ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    ClearChrFlags(0x1A, 0x10)
    OP_4C(0x1A, 0xFF)
    Return()

    # Function_19_18E1 end

    def Function_20_19CF(): pass

    label("Function_20_19CF")

    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B13")

    #C0053
    ChrTalk(
        0x1A,
        (
            "#01700Fさっき見つけた服なんだけど、\x01",
            "胸元がスパーンと空いててセクシーでしょ。\x02\x03",

            "#01709Fどう？　リーシャ。\x01",
            "買ってあげるから着てみない？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x1B,
        (
            "#01805Fえ、ええ！？\x01",
            "これを着るんですか！？\x02\x03",

            "#01809Fさ、さすがに\x01",
            "恥ずかしいって言うか……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x1A,
        (
            "#01709F大丈夫大丈夫、あんたなら\x01",
            "絶対魅力的に着こなせるって！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_1BA0")

    label("loc_1B13")


    #C0056
    ChrTalk(
        0x1A,
        (
            "#01709Fいいからいいから、\x01",
            "一度騙されたと思って\x01",
            "試着してみなさいって。\x02\x03",

            "#01701Fてゆーか、あたしが見たいし！\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x1B,
        "#01806Fひ、ひ～ん……！\x02",
    )

    CloseMessageWindow()

    label("loc_1BA0")

    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    Return()

    # Function_20_19CF end

    def Function_21_1BA9(): pass

    label("Function_21_1BA9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1BBA")
    Jump("loc_2125")

    label("loc_1BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1BC8")
    Jump("loc_2125")

    label("loc_1BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1BD6")
    Jump("loc_2125")

    label("loc_1BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1ED3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E0B")

    #C0058
    ChrTalk(
        0x19,
        (
            "#05900Fさっきエリィさんから聞いたけど、\x01",
            "ロイドってこのブティックで\x01",
            "スーツを買ったんですって？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#00005Fああ、ちょっと前だけど……\x01",
            "それがどうかしたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x19,
        (
            "#05906Fうう、結婚式のためのスーツは\x01",
            "お姉ちゃんが見繕ってあげる\x01",
            "つもりだったのに……！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x153,
        (
            "#01105Fえ、ロイドって\x01",
            "やっぱり結婚するのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#00012Fい、いやいや、しないし！\x02\x03",

            "#00006Fそもそもあれは捜査のために\x01",
            "見繕ったものだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x19,
        (
            "#05905Fまあ、そうだったの？\x01",
            "それはそれで残念だけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0064
    ChrTalk(
        0x101,
        (
            "#00006F（セシル姉……\x01",
            "  何か俺の反応を楽しんでないか？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_1ECE")

    label("loc_1E0B")


    #C0065
    ChrTalk(
        0x19,
        (
            "#05902Fふふ、結婚式をするときは、\x01",
            "絶対に私を呼ぶのよ。\x02\x03",

            "#05901F式場のセッティングから\x01",
            "新婚旅行の場所決めまで、\x01",
            "お姉ちゃんがやってあげるから！\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#00006Fスーツの話から\x01",
            "飛躍しすぎだって……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ECE")

    Jump("loc_2125")

    label("loc_1ED3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_210E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_208C")

    #C0067
    ChrTalk(
        0x19,
        "#05903F………………………………\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#00005Fセシル姉、どうかしたの？\x02",
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0069
    ChrTalk(
        0x19,
        (
            "#05902F……ああ、ロイド。\x02\x03",

            "#05909Fうん、テーマパークに\x01",
            "行くのなんて初めてだから、\x01",
            "どんな所なのかなあって。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00004Fああ、俺も初めてなんだよな。\x02\x03",

            "#00000F前に行ったことがある\x01",
            "ランディやノエルから聞く限りじゃ、\x01",
            "期待してていいんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x19,
        (
            "#05909Fふふ、そうね。\x01",
            "せっかくだから色々と\x01",
            "案内してもらわないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_2109")

    label("loc_208C")


    #C0072
    ChrTalk(
        0x19,
        (
            "#05904Fうん、今日は\x01",
            "とことん楽しまないとね。\x02\x03",

            "#05902F私も初めてだし、\x01",
            "ランディ君やノエルさんに\x01",
            "案内してもらおうかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2109")

    Jump("loc_2125")

    label("loc_210E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_211C")
    Jump("loc_2125")

    label("loc_211C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2125")

    label("loc_2125")

    TalkEnd(0xFE)
    Return()

    # Function_21_1BA9 end

    def Function_22_2129(): pass

    label("Function_22_2129")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_213A")
    Jump("loc_2328")

    label("loc_213A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2148")
    Jump("loc_2328")

    label("loc_2148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_2156")
    Jump("loc_2328")

    label("loc_2156")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_2166")
    Jump("loc_2328")

    label("loc_2166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_2174")
    Jump("loc_2328")

    label("loc_2174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2311")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B2")

    #C0073
    ChrTalk(
        0x18,
        (
            "#06405Fあ、ロイドさん！\x01",
            "ちょっと見て下さいよ～。\x02\x03",

            "#06409Fどうですかこの服、\x01",
            "私に似合いそうですかね～？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        "#00000Fうん、なかなかいいんじゃないか？\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x18,
        (
            "#06402Fおおっ、ロイドさんのお墨付きですね！\x01",
            "それじゃあこれは買うとして……\x02\x03",

            "#06409Fふふ、お姉ちゃんの服も\x01",
            "勝手に選んじゃおうかな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_230C")

    label("loc_22B2")


    #C0076
    ChrTalk(
        0x18,
        (
            "#06409F良さそうな服がいっぱいですよ～！\x02\x03",

            "#06406Fお姉ちゃんも来ればよかったのになあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_230C")

    Jump("loc_2328")

    label("loc_2311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_231F")
    Jump("loc_2328")

    label("loc_231F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2328")

    label("loc_2328")

    TalkEnd(0xFE)
    Return()

    # Function_22_2129 end

    def Function_23_232C(): pass

    label("Function_23_232C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_233D")
    Jump("loc_2ABA")

    label("loc_233D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_234B")
    Jump("loc_2ABA")

    label("loc_234B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_2359")
    Jump("loc_2ABA")

    label("loc_2359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_25D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_253F")

    #C0077
    ChrTalk(
        0x17,
        (
            "#00113Fはあ、少し覚悟してたけど\x01",
            "まさかあんな目に合うなんて……\x02\x03",

            "#00111F……ねえ、ロイド。\x01",
            "本当に見てない#8R㈲　㈲　㈲　㈲#のよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#00012Fあ、ああ。\x01",
            "大丈夫だ、見てないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x17,
        (
            "#00106Fふう、それならいいんだけど。\x02\x03",

            "#00112F……もし見ていたんだったら、\x01",
            "責任とってもらいますから。\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0080
    ChrTalk(
        0x101,
        "#00011F#4Sえ゛！？#3S\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x17,
        (
            "#00104F……なんてね、冗談よ。\x02\x03",

            "#00109Fふふ、あなたって本当に\x01",
            "からかいがいがあるわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#00006Fか、勘弁してくれよ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_25CB")

    label("loc_253F")


    #C0083
    ChrTalk(
        0x17,
        (
            "#00113Fま、まああんな目に合うのは\x01",
            "ある程度覚悟はしていたし……\x02\x03",

            "#00102Fひとまず魔獣を撃退できてよかった、\x01",
            "ってことにしておきましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25CB")

    Jump("loc_2ABA")

    label("loc_25D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_27B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_273E")

    #C0084
    ChrTalk(
        0x17,
        (
            "#00105Fあ、キーアちゃん。\x02\x03",

            "#00102Fねえ、どうかしらこのドレス。\x01",
            "キーアちゃんにぴったりだと\x01",
            "思うんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x153,
        "#01110Fわー、キレーかもー！\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#00003Fド、ドレスかあ……\x01",
            "着るタイミングがあるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x17,
        (
            "#00109Fふふ、無くてもいいじゃない。\x02\x03",

            "#00104Fキーアちゃんには色々な服を\x01",
            "試してもらわないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#00012F（うーん、楽しそうだ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_27AE")

    label("loc_273E")


    #C0089
    ChrTalk(
        0x17,
        (
            "#00102Fふふ、私はもう少し\x01",
            "ここを見ていることにするわ。\x02\x03",

            "#00109Fキーアちゃんの服を\x01",
            "色々と探してみないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27AE")

    Jump("loc_2ABA")

    label("loc_27B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2A95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29E8")

    #C0090
    ChrTalk(
        0x17,
        (
            "#00103Fやっぱり、このブティックは\x01",
            "質がいい物が揃っているみたいね。\x02\x03",

            "#00100Fこのドレスのシルクもそうだし、\x01",
            "あっちにあるバリアハートの毛皮も\x01",
            "とても優しい手触りで……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#00005Fバリアハートって……\x01",
            "確か帝国東部にある\x01",
            "都市の名前だったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x17,
        (
            "#00100Fええ、あそこは\x01",
            "良質な毛皮の産地として有名なの。\x02\x03",

            "#00104F社交パーティに出席すると、\x01",
            "身につけてるご婦人を\x01",
            "お見かけすることも多いわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#00000Fへえ、さすがに詳しいな。\x02\x03",

            "#00003Fこのシーズン、さすがに毛皮は\x01",
            "暑苦しいと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x17,
        (
            "#00111F……身も蓋もない事を\x01",
            "言ってくれるわねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2A90")

    label("loc_29E8")


    #C0095
    ChrTalk(
        0x17,
        (
            "#00104F社交の場において、\x01",
            "身につけているものというのは\x01",
            "一種のステイタスなのよね。\x02\x03",

            "#00100F個人的には、作りがよければ\x01",
            "ブランド品に拘る必要なんて\x01",
            "ないとは思うけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A90")

    Jump("loc_2ABA")

    label("loc_2A95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_2AA3")
    Jump("loc_2ABA")

    label("loc_2AA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2AB1")
    Jump("loc_2ABA")

    label("loc_2AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_2ABA")

    label("loc_2ABA")

    TalkEnd(0xFE)
    Return()

    # Function_23_232C end

    def Function_24_2ABE(): pass

    label("Function_24_2ABE")

    Call(0, 25)
    Return()

    # Function_24_2ABE end

    def Function_25_2AC2(): pass

    label("Function_25_2AC2")

    TalkBegin(0x14)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2ACF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DB7")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B2D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2B2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B4D")
    OP_AF(0x69)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2DB2")

    label("loc_2B4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B61")
    Jump("loc_2DB2")

    label("loc_2B61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DB2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2B88")
    Jump("loc_2DB2")

    label("loc_2B88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_2C6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C18")

    #C0096
    ChrTalk(
        0x14,
        (
            "ふう、ドローナったら\x01",
            "浮かれてしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x14,
        (
            "気持ちは分かりますけど、\x01",
            "お客様の前では\x01",
            "控えて欲しいものですわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2C66")

    label("loc_2C18")


    #C0098
    ChrTalk(
        0x14,
        (
            "ふう、ドローナったら。\x01",
            "お客様の前で浮かれるのは\x01",
            "控えて欲しいものですわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C66")

    Jump("loc_2DB2")

    label("loc_2C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2CE3")

    #C0099
    ChrTalk(
        0x14,
        (
            "女性のお客様が\x01",
            "多数いらっしゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x14,
        (
            "ふふ、お美しい方々ばかりで\x01",
            "ため息がでてしまいますわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB2")

    label("loc_2CE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2DB2")

    #C0101
    ChrTalk(
        0x14,
        (
            "レイクビーチのオープンにあわせて、\x01",
            "ブティック《コルセリカ》では\x01",
            "水着の取り扱いも始めましたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x14,
        (
            "大陸沿岸部から輸入した\x01",
            "流行の水着も取り揃えていますので、\x01",
            "是非是非ご覧になって下さいませね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DB2")

    Jump("loc_2ACF")

    label("loc_2DB7")

    TalkEnd(0x14)
    Return()

    # Function_25_2AC2 end

    def Function_26_2DBB(): pass

    label("Function_26_2DBB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2DCC")
    Jump("loc_2F9B")

    label("loc_2DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_2EB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E4A")

    #C0103
    ChrTalk(
        0xFE,
        (
            "あのイリア・プラティエに\x01",
            "直筆のサインを頂いてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        "ああ、一生の宝物にしますわ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2EAF")

    label("loc_2E4A")


    #C0105
    ChrTalk(
        0xFE,
        (
            "まさかあのイリアに、\x01",
            "こんな所でお目にかかれるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        "このサイン、一生の宝物にしますわ！\x02",
    )

    CloseMessageWindow()

    label("loc_2EAF")

    Jump("loc_2F9B")

    label("loc_2EB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2F1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ECF")
    Call(0, 19)
    Jump("loc_2F15")

    label("loc_2ECF")


    #C0107
    ChrTalk(
        0xFE,
        (
            "（……あれ？\x01",
            "  そういえばこのお客様、\x01",
            "  どこかで見たような……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F15")

    Jump("loc_2F9B")

    label("loc_2F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2F9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F35")
    Call(0, 27)
    Jump("loc_2F9B")

    label("loc_2F35")


    #C0108
    ChrTalk(
        0xFE,
        "うふふ、大変お似合いですよ。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "お客様のエレガントさを\x01",
            "最大限に引き出しているかと\x01",
            "存じますわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F9B")

    TalkEnd(0xFE)
    Return()

    # Function_26_2DBB end

    def Function_27_2F9F(): pass

    label("Function_27_2F9F")

    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    #C0110
    ChrTalk(
        0x15,
        (
            "そうですね、コーディネートで\x01",
            "こちらのリボンをつけると\x01",
            "よりエレガントになるかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x16,
        "……こうかしら？\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x15,
        "うふふ、大変お似合いですわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    Return()

    # Function_27_2F9F end

    def Function_28_3043(): pass

    label("Function_28_3043")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_3054")
    Jump("loc_30E5")

    label("loc_3054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_3062")
    Jump("loc_30E5")

    label("loc_3062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_30E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_307D")
    Call(0, 27)
    Jump("loc_30E5")

    label("loc_307D")


    #C0113
    ChrTalk(
        0xFE,
        (
            "ふふ、あなた\x01",
            "なかなか分かってますわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "それじゃあこのコーディネートを\x01",
            "一通りくださるかしら？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30E5")

    TalkEnd(0xFE)
    Return()

    # Function_28_3043 end

    def Function_29_30E9(): pass

    label("Function_29_30E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B0")

    #C0115
    ChrTalk(
        0xFE,
        (
            "保養地ミシュラム……\x01",
            "初めてきたけれど最高ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "ここで暮らせば、\x01",
            "あの冴えない夫との暮らしとも\x01",
            "おさらばできそう。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "ご飯を食べたら、さっそく\x01",
            "別荘地を見に行かなくちゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_322F")

    label("loc_31B0")


    #C0118
    ChrTalk(
        0xFE,
        (
            "ここで暮らせば、\x01",
            "あの冴えない夫との暮らしとも\x01",
            "おさらばできそう。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "ご飯を食べたら、さっそく\x01",
            "別荘地を見に行かなくちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_322F")

    TalkEnd(0xFE)
    Return()

    # Function_29_30E9 end

    SaveToFile()

Try(main)
