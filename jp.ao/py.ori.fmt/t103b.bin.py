from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t103b.bin",                # FileName
        "t103b",                    # MapName
        "t103b",                    # Location
        0x0041,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 65, 0, 1, 0, 2],
    )

    BuildStringList((
        "t103b",                  # 0
        "ＭＷＬスタッフ",         # 1
        "ＭＷＬスタッフ",         # 2
        "観光客",                 # 3
        "観光客",                 # 4
        "メルスン",               # 5
        "コロナ",                 # 6
        "リマ",                   # 7
        "ホテル・デルフィニア方面",# 8
        "テーマパーク方面",       # 9
    ))

    AddCharChip((
        "chr/ch44500.itc",                   # 00
        "chr/ch32300.itc",                   # 01
        "chr/ch32400.itc",                   # 02
        "chr/ch26200.itc",                   # 03
        "chr/ch22700.itc",                   # 04
        "chr/ch20700.itc",                   # 05
    ))

    DeclNpc(-4000,   4400,    0,       180,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(4750,    4400,    0,       180,  389,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4329,    2599,    -23489,  0,    389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(5329,    2599,    -23489,  0,    389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-13270,  4000,    -4579,   135,  261,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-11810,  4000,    -4820,   270,  261,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-13079,  4000,    -6130,   0,    261,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)

    DeclEvent(0x0000, 0, 14,  0.0,                   2.5,                   3.4000000953674316,    100.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.0,                  -1.25,                 -0.6800000071525574,   1.0])

    DeclActor(-14170,  4000,    -6040,   1200,    -14170,  5500,    -6040,   0x007C, 0,  15, 0x0000)
    DeclActor(-6650,   4000,    1550,    1200,    -6650,   5500,    1550,    0x007C, 0,  16, 0x0000)

    PlaceName(10.0, 0.0, -68.0, 0x0000, 0x0000, "ホテル・デルフィニア方面")
    PlaceName(-5.0, 0.0, 20.0, 0x0000, 0x0000, "テーマパーク方面")

    ChipFrameInfo(644, 0)                                        # 0

    ScpFunction((
        "Function_0_284",          # 00, 0
        "Function_1_33C",          # 01, 1
        "Function_2_44B",          # 02, 2
        "Function_3_515",          # 03, 3
        "Function_4_714",          # 04, 4
        "Function_5_7E2",          # 05, 5
        "Function_6_838",          # 06, 6
        "Function_7_8A2",          # 07, 7
        "Function_8_984",          # 08, 8
        "Function_9_A44",          # 09, 9
        "Function_10_AF3",         # 0A, 10
        "Function_11_BEC",         # 0B, 11
        "Function_12_13B0",        # 0C, 12
        "Function_13_1488",        # 0D, 13
        "Function_14_1627",        # 0E, 14
        "Function_15_16A7",        # 0F, 15
        "Function_16_1727",        # 10, 16
    ))


    def Function_0_284(): pass

    label("Function_0_284")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2C4"),
        (1, "loc_2D0"),
        (2, "loc_2DC"),
        (3, "loc_2E8"),
        (4, "loc_2F4"),
        (5, "loc_300"),
        (6, "loc_30C"),
        (SWITCH_DEFAULT, "loc_318"),
    )


    label("loc_2C4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_2D0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_2DC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_2E8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_2F4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_300")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_30C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_318")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_324")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_33B")

    Return()

    # Function_0_284 end

    def Function_1_33C(): pass

    label("Function_1_33C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_359")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Jump("loc_400")

    label("loc_359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_367")
    Jump("loc_400")

    label("loc_367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_3B1")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    Jump("loc_400")

    label("loc_3B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_3BF")
    Jump("loc_400")

    label("loc_3BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_3CD")
    Jump("loc_400")

    label("loc_3CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_3DB")
    Jump("loc_400")

    label("loc_3DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_3E9")
    Jump("loc_400")

    label("loc_3E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_3F7")
    Jump("loc_400")

    label("loc_3F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_400")

    label("loc_400")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_414")
    ClearScenarioFlags(0x22, 0)
    SetMapFlags(0x10000000)
    Event(0, 13)

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42F")
    SetMapFlags(0x10000000)
    Event(0, 11)
    Jump("loc_44A")

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44A")
    SetMapFlags(0x10000000)
    Event(0, 12)

    label("loc_44A")

    Return()

    # Function_1_33C end

    def Function_2_44B(): pass

    label("Function_2_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47C")
    SetMapObjFrame(0xFF, "board0a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "board0b", 0x0, 0x1)
    Jump("loc_49A")

    label("loc_47C")

    SetMapObjFrame(0xFF, "board1a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "board1b", 0x0, 0x1)

    label("loc_49A")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B2")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_4B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CB")
    OP_24(0x335)
    OP_24(0x1BC)
    Jump("loc_4F8")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EC")
    Sound(821, 1, 40, 0)
    OP_24(0x1BC)
    Jump("loc_4F8")

    label("loc_4EC")

    Sound(821, 1, 40, 0)
    Sound(444, 1, 100, 0)

    label("loc_4F8")

    SoundDistance(0x7B, 0xFFFFFFBA, 0x109A, 0xFFFFD9E0, 0x2710, 0x186A0, 0x50, 0x0)
    Return()

    # Function_2_44B end

    def Function_3_515(): pass

    label("Function_3_515")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_6F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_680")

    #C0001
    ChrTalk(
        0x8,
        (
            "ただいま、テーマパーク内では\x01",
            "夜の部が開催中です。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "みっしぃたちが園内を回る\x01",
            "ナイトパレードも大盛況ですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_636")

    #C0003
    ChrTalk(
        0x103,
        "#00203F……正直、見たかったです。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#00002Fはは、まあ今回は仕方ないよ。\x01",
            "次の機会にな。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x103,
        "#00202Fふふっ……絶対ですよ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_678")

    label("loc_636")


    #C0006
    ChrTalk(
        0x101,
        (
            "#00003F（う～ん、ティオが聞いたら\x01",
            "  見たがるだろうなあ……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_678")

    SetScenarioFlags(0x0, 0)
    Jump("loc_6F4")

    label("loc_680")


    #C0007
    ChrTalk(
        0x8,
        (
            "ただいま、テーマパーク内では\x01",
            "夜の部が開催中です。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "みっしぃたちが園内を回る\x01",
            "ナイトパレードも大盛況ですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F4")

    Jump("loc_710")

    label("loc_6F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_707")
    Jump("loc_710")

    label("loc_707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_710")

    label("loc_710")

    TalkEnd(0xFE)
    Return()

    # Function_3_515 end

    def Function_4_714(): pass

    label("Function_4_714")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_7C7")

    #C0009
    ChrTalk(
        0x9,
        (
            "ミシュラム名物の花火は、\x01",
            "毎日１００発ほどの\x01",
            "打ち上げを行っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x9,
        (
            "テーマパークはもちろん、\x01",
            "ホテルや夜間航行中の飛行船からも\x01",
            "見えると評判なのですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DE")

    label("loc_7C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_7D5")
    Jump("loc_7DE")

    label("loc_7D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_7DE")

    label("loc_7DE")

    TalkEnd(0xFE)
    Return()

    # Function_4_714 end

    def Function_5_7E2(): pass

    label("Function_5_7E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_81D")

    #C0011
    ChrTalk(
        0xA,
        "（……い、今なら手を握れるかも……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_834")

    label("loc_81D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_82B")
    Jump("loc_834")

    label("loc_82B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_834")

    label("loc_834")

    TalkEnd(0xFE)
    Return()

    # Function_5_7E2 end

    def Function_6_838(): pass

    label("Function_6_838")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_887")

    #C0012
    ChrTalk(
        0xB,
        "わあ、花火が沢山上がってる……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xB,
        "……ふふ、綺麗ね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_89E")

    label("loc_887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_895")
    Jump("loc_89E")

    label("loc_895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_89E")

    label("loc_89E")

    TalkEnd(0xFE)
    Return()

    # Function_6_838 end

    def Function_7_8A2(): pass

    label("Function_7_8A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_94D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C0")
    Call(0, 8)
    Jump("loc_948")

    label("loc_8C0")


    #C0014
    ChrTalk(
        0xC,
        (
            "本当ならホテルに宿泊したかったけど、\x01",
            "どうしても予約が取れなくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xC,
        (
            "まあ、リマは楽しんでくれたようだし\x01",
            "来た甲斐があったかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_948")

    Jump("loc_980")

    label("loc_94D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_95B")
    Jump("loc_980")

    label("loc_95B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_969")
    Jump("loc_980")

    label("loc_969")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_977")
    Jump("loc_980")

    label("loc_977")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_980")

    label("loc_980")

    TalkEnd(0xFE)
    Return()

    # Function_7_8A2 end

    def Function_8_984(): pass

    label("Function_8_984")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0016
    ChrTalk(
        0xC,
        (
            "ふう、今日は本当に\x01",
            "一日中遊んでしまったなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xC,
        "リマ、楽しかったかい？\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xE,
        (
            "うん、楽しかったよー！！\x01",
            "パパありがと～！！\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xD,
        "ふふ、おつかれさま。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 1)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_8_984 end

    def Function_9_A44(): pass

    label("Function_9_A44")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_ABC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A62")
    Call(0, 8)
    Jump("loc_AB7")

    label("loc_A62")


    #C0020
    ChrTalk(
        0xD,
        "ふふ、おつかれさま。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xD,
        (
            "帰ったら、美味しいご飯を\x01",
            "沢山つくってあげますからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB7")

    Jump("loc_AEF")

    label("loc_ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_ACA")
    Jump("loc_AEF")

    label("loc_ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_AD8")
    Jump("loc_AEF")

    label("loc_AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_AE6")
    Jump("loc_AEF")

    label("loc_AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_AEF")

    label("loc_AEF")

    TalkEnd(0xFE)
    Return()

    # Function_9_A44 end

    def Function_10_AF3(): pass

    label("Function_10_AF3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_BB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B11")
    Call(0, 8)
    Jump("loc_BB0")

    label("loc_B11")


    #C0022
    ChrTalk(
        0xE,
        (
            "カガミのお城のてっぺんで、\x01",
            "パパとママといつまでも一緒に\x01",
            "いられるようにお願いしたのー！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xE,
        (
            "観覧車やホラーコースターにも\x01",
            "乗れたし、本当に楽しかったなー！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB0")

    Jump("loc_BE8")

    label("loc_BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_BC3")
    Jump("loc_BE8")

    label("loc_BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_BD1")
    Jump("loc_BE8")

    label("loc_BD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_BDF")
    Jump("loc_BE8")

    label("loc_BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_BE8")

    label("loc_BE8")

    TalkEnd(0xFE)
    Return()

    # Function_10_AF3 end

    def Function_11_BEC(): pass

    label("Function_11_BEC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 0, 0, -61000, 0)
    SetChrPos(0x102, -700, 0, -61700, 0)
    SetChrPos(0x103, 600, 0, -62100, 0)
    SetChrPos(0x104, 100, 0, -63000, 0)
    SetChrPos(0x105, 1000, 0, -63500, 0)
    SetChrPos(0x109, -950, 0, -63100, 0)
    OP_68(0, 4500, -53000, 0)
    MoveCamera(314, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(28000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1500, -53000, 5000)

    def lambda_CBF():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CBF)
    Sleep(50)

    def lambda_CD7():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CD7)
    Sleep(50)

    def lambda_CEF():
        OP_9B(0x0, 0x103, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CEF)
    Sleep(50)

    def lambda_D07():
        OP_9B(0x0, 0x104, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D07)
    Sleep(50)

    def lambda_D1F():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_D1F)
    Sleep(50)

    def lambda_D37():
        OP_9B(0x0, 0x109, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D37)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
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
    OP_6F(0x79)

    #C0024
    ChrTalk(
        0x102,
        "#00107F#6Pこ、これって……！？\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#00013F#6P垂れ幕が変わってる！？\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x104,
        "#00301F#6Pおいおい、コイツは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(-4000, 1000, -38000, 0)
    OP_68(-4000, 1000, -33000, 5500)
    MoveCamera(315, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(33000, 0)
    SetCameraDistance(26000, 5500)
    SetChrPos(0x101, -3500, 0, -42000, 0)
    SetChrPos(0x102, -4100, 0, -42900, 0)
    SetChrPos(0x103, -2900, 0, -43100, 0)
    SetChrPos(0x104, -3400, 0, -44200, 0)
    SetChrPos(0x105, -2000, 0, -44500, 0)
    SetChrPos(0x109, -4900, 0, -44100, 0)

    def lambda_F15():
        OP_9B(0x0, 0x101, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F15)
    Sleep(50)

    def lambda_F2D():
        OP_9B(0x0, 0x102, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F2D)
    Sleep(50)

    def lambda_F45():
        OP_9B(0x0, 0x103, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F45)
    Sleep(50)

    def lambda_F5D():
        OP_9B(0x0, 0x104, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F5D)
    Sleep(50)

    def lambda_F75():
        OP_9B(0x0, 0x105, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F75)
    Sleep(50)

    def lambda_F8D():
        OP_9B(0x0, 0x109, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F8D)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_6F(0x79)
    OP_0D()

    #C0027
    ChrTalk(
        0x109,
        "#10108F#6Pい、いつのまにこんな……？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x105,
        (
            "#10308F#6Pふむ、夜限定の趣向#4Rイベント#とも\x01",
            "思えないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x103,
        (
            "#00206F#6P……そんな話は\x01",
            "聞いた事がありません。\x02\x03",

            "#00201Fそれに……\x01",
            "みっしぃを他のキャラに\x01",
            "変えるなんてあり得ないです。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#00006F#6P……だろうな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0031
    ChrTalk(
        0x101,
        "#00005F#6Pあれは──\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 4500, -7000, 0)
    MoveCamera(0, 35, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26000, 0)
    OP_68(0, 9500, 0, 7000)
    MoveCamera(0, 18, 0, 7000)
    OP_6E(600, 7000)
    SetCameraDistance(20000, 7000)
    OP_6F(0x79)
    OP_0D()
    SetMessageWindowPos(50, 160, -1, -1)

    #A0032
    AnonymousTalk(
        0x102,
        "#00105F『道化師#6Rフール#のワンダーランド』……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 160, -1, -1)

    #A0033
    AnonymousTalk(
        0x104,
        (
            "#00306F完全に名前が\x01",
            "書き換わってんじゃねーか……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(280, 160, -1, -1)

    #A0034
    AnonymousTalk(
        0x109,
        (
            "#10113Fゆ、夢でも\x01",
            "見てるんでしょうか……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 160, -1, -1)

    #A0035
    AnonymousTalk(
        0x105,
        (
            "#10306F……夢は夢でも\x01",
            "悪夢の類いみたいだけどね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 160, -1, -1)

    #A0036
    AnonymousTalk(
        0x101,
        "#00008F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-3580, 1000, -32790, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24640, 0)
    OP_0D()
    Sleep(300)

    #C0037
    ChrTalk(
        0x101,
        (
            "#00003F#5P──どうやらキーアは\x01",
            "この先にいるみたいだ。\x02\x03",

            "#00013Fだったら……\x01",
            "とにかく中に入るしかない！\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x102,
        "#00101F#6Pええ……！\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        "#00301F#6P行くしかねえな……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -2890, 0, -32110, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x146, 1)
    OP_29(0xA5, 0x1, 0xA)
    EventEnd(0x5)
    Return()

    # Function_11_BEC end

    def Function_12_13B0(): pass

    label("Function_12_13B0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(780, 1600, -58060, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 600, 0, -57250, 0)
    SetChrPos(0xEF, -600, 0, -57250, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0040
    ChrTalk(
        0x101,
        "#6P#00002Fあ…………\x02",
    )

    CloseMessageWindow()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x201), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopSound(821, 500, 100)
    Sleep(500)
    SetScenarioFlags(0x15B, 2)
    SetScenarioFlags(0x22, 0)
    NewScene("e3110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_13B0 end

    def Function_13_1488(): pass

    label("Function_13_1488")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(780, 1600, -58060, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 600, 0, -57250, 0)
    SetChrPos(0xEF, -600, 0, -57250, 0)
    FadeToBright(1000, 0)
    OP_0D()
    TurnDirection(0x101, 0xEF, 500)

    #C0041
    ChrTalk(
        0x101,
        (
            "#12P#00004F……よし、それじゃあ\x01",
            "そろそろ迎賓館に行くとしようか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_156F")

    #C0042
    ChrTalk(
        0x102,
        "#00102Fええ、分かったわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1600")

    label("loc_156F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1594")

    #C0043
    ChrTalk(
        0x103,
        "#00202F了解です。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1600")

    label("loc_1594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_15B5")

    #C0044
    ChrTalk(
        0x104,
        "#00309Fおう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1600")

    label("loc_15B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_15DA")

    #C0045
    ChrTalk(
        0x109,
        "#10109F了解です！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1600")

    label("loc_15DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_1600")

    #C0046
    ChrTalk(
        0x105,
        "#10304Fフフ、そうだね。\x02",
    )

    CloseMessageWindow()

    label("loc_1600")

    OP_5A()
    ClearMapFlags(0x10000000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, -57250, 0)
    EventEnd(0x5)
    Return()

    # Function_13_1488 end

    def Function_14_1627(): pass

    label("Function_14_1627")

    EventBegin(0x1)

    #C0047
    ChrTalk(
        0x101,
        (
            "#00000F夜のテーマパークも\x01",
            "楽しそうだけど、\x01",
            "それはまた次の機会だな。\x02\x03",

            "早いところ、迎賓館に向かおう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 4400, -1250, 180)
    EventEnd(0x4)
    Return()

    # Function_14_1627 end

    def Function_15_16A7(): pass

    label("Function_15_16A7")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "テーマパークの\x01",
            "見取り図が描かれている。\x02\x03",

            "広大な敷地に\x01",
            "さまざまなアミューズメント施設が\x01",
            "並んでいるようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_15_16A7 end

    def Function_16_1727(): pass

    label("Function_16_1727")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0049
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "   ～こ来園のみなさまへ～\x01\x01",
            "当テーマパーク内での\x01",
            "暴走行為や危険物の持ち込みは\x01",
            "固くお断り申し上げます。\x01\x01",
            "また、お子様には必ず\x01",
            "保護者の方が同伴なさるよう\x01",
            "お願い申し上げます。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_16_1727 end

    SaveToFile()

Try(main)
