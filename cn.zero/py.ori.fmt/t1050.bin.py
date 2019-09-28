from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t1050.bin",                # FileName
        "t1050",                    # MapName
        "t1050",                    # Location
        0x0043,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 67, 0, 4, 0, 5],
    )

    BuildStringList((
        "t1050",                  # 0
        "哈加经理",               # 1
        "洛琪",                   # 2
        "茜特拉丝",               # 3
        "游客",                   # 4
        "游客",                   # 5
        "瓦吉",                   # 6
        "托马",                   # 7
        "阿尔维娜",               # 8
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch25600.itc",                   # 01
        "chr/ch25700.itc",                   # 02
        "chr/ch20400.itc",                   # 03
        "chr/ch20500.itc",                   # 04
        "chr/ch20200.itc",                   # 05
        "chr/ch20300.itc",                   # 06
        "chr/ch08000.itc",                   # 07
    ))

    DeclNpc(-479,    0,       10050,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-100709, 0,       8859,    270,  257,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-101819, 0,       8859,    90,   257,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(8970,    0,       6630,    225,  385,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(8250,    0,       5920,    45,   385,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   7,   0,   0,   3,   255, 255, 255,  0)
    DeclNpc(96220,   0,       121949,  270,  261,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(103230,  0,       124330,  0,    261,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)

    DeclActor(-20,     0,       8270,    1500,    -480,    1500,    10050,   0x007E, 0,  7,  0x0000)
    DeclActor(5500,    0,       13500,   1200,    5500,    1500,    13500,   0x007C, 0,  28, 0x0000)
    DeclActor(-99830,  0,       13590,   1200,    -99830,  1500,    13590,   0x007C, 0,  29, 0x0000)
    DeclActor(-96600,  0,       120560,  1500,    -96600,  1000,    120560,  0x007C, 0,  6,  0x0000)

    ScpFunction((
        "Function_0_29C",          # 00, 0
        "Function_1_354",          # 01, 1
        "Function_2_3B5",          # 02, 2
        "Function_3_416",          # 03, 3
        "Function_4_495",          # 04, 4
        "Function_5_549",          # 05, 5
        "Function_6_583",          # 06, 6
        "Function_7_622",          # 07, 7
        "Function_8_626",          # 08, 8
        "Function_9_8D2",          # 09, 9
        "Function_10_AD4",         # 0A, 10
        "Function_11_C1B",         # 0B, 11
        "Function_12_CD3",         # 0C, 12
        "Function_13_1146",        # 0D, 13
        "Function_14_137F",        # 0E, 14
        "Function_15_13FE",        # 0F, 15
        "Function_16_1429",        # 10, 16
        "Function_17_1C0B",        # 11, 17
        "Function_18_1C20",        # 12, 18
        "Function_19_1CA3",        # 13, 19
        "Function_20_335A",        # 14, 20
        "Function_21_339F",        # 15, 21
        "Function_22_3402",        # 16, 22
        "Function_23_3465",        # 17, 23
        "Function_24_34AA",        # 18, 24
        "Function_25_34EF",        # 19, 25
        "Function_26_3E13",        # 1A, 26
        "Function_27_4CF2",        # 1B, 27
        "Function_28_52D3",        # 1C, 28
        "Function_29_534C",        # 1D, 29
    ))


    def Function_0_29C(): pass

    label("Function_0_29C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2DC"),
        (1, "loc_2E8"),
        (2, "loc_2F4"),
        (3, "loc_300"),
        (4, "loc_30C"),
        (5, "loc_318"),
        (6, "loc_324"),
        (SWITCH_DEFAULT, "loc_330"),
    )


    label("loc_2DC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_2E8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_2F4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_300")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_30C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_318")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_324")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_330")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_33C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_353")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_353")

    Return()

    # Function_0_29C end

    def Function_1_354(): pass

    label("Function_1_354")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B4")
    OP_95(0xFE, -106030, 0, 8260, 2000, 0x0)
    OP_95(0xFE, -106030, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 8260, 2000, 0x0)
    Jump("Function_1_354")

    label("loc_3B4")

    Return()

    # Function_1_354 end

    def Function_2_3B5(): pass

    label("Function_2_3B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_415")
    OP_95(0xFE, 106130, 0, 11580, 2000, 0x0)
    OP_95(0xFE, 106130, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 11580, 2000, 0x0)
    Jump("Function_2_3B5")

    label("loc_415")

    Return()

    # Function_2_3B5 end

    def Function_3_416(): pass

    label("Function_3_416")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_494")
    SetScenarioFlags(0xAA, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_70(0x2, 0xA)
    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -100040, 0, 13630, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(890, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)

    label("loc_494")

    Return()

    # Function_3_416 end

    def Function_4_495(): pass

    label("Function_4_495")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AF")
    Event(0, 19)

    label("loc_4AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_4BD")
    Jump("loc_548")

    label("loc_4BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_4CB")
    Jump("loc_548")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_4D9")
    Jump("loc_548")

    label("loc_4D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4E7")
    Jump("loc_548")

    label("loc_4E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_4F5")
    Jump("loc_548")

    label("loc_4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_531")
    SetChrPos(0x9, -93960, 0, 8260, 0)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, 94190, 0, 11580, 0)
    BeginChrThread(0xA, 0, 0, 2)
    Jump("loc_548")

    label("loc_531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_53F")
    Jump("loc_548")

    label("loc_53F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_548")

    label("loc_548")

    Return()

    # Function_4_495 end

    def Function_5_549(): pass

    label("Function_5_549")

    OP_65(0x2, 0x1)
    SetMapObjFlags(0x2, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56B")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_56B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_582")
    EndChrThread(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)

    label("loc_582")

    Return()

    # Function_5_549 end

    def Function_6_583(): pass

    label("Function_6_583")

    OP_F2(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_604")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_604")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_620")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_620")

    Return()

    # Function_6_583 end

    def Function_7_622(): pass

    label("Function_7_622")

    Call(0, 8)
    Return()

    # Function_7_622 end

    def Function_8_626(): pass

    label("Function_8_626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_63C")
    Call(0, 16)
    Jump("loc_8D1")

    label("loc_63C")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_64D")
    Jump("loc_8CE")

    label("loc_64D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_65B")
    Jump("loc_8CE")

    label("loc_65B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_669")
    Jump("loc_8CE")

    label("loc_669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_677")
    Jump("loc_8CE")

    label("loc_677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_685")
    Jump("loc_8CE")

    label("loc_685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_77B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_734")
    TurnDirection(0x8, 0x151, 0)

    #C0001
    ChrTalk(
        0x8,
        "瓦吉先生，您要出门吗？\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "那么，在此期间，\x01",
            "我来为您\x01",
            "整理床铺吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x151,
        (
            "#5700F是啊，大概会出去一段时间……\x01",
            "那就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        "明白了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_776")

    label("loc_734")


    #C0005
    ChrTalk(
        0x8,
        (
            "那么，\x01",
            "在您外出期间，我会帮您\x01",
            "整理好床铺的。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        "请您慢走。\x02",
    )

    CloseMessageWindow()

    label("loc_776")

    Jump("loc_8CE")

    label("loc_77B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_END)), "loc_7DC")

    #C0007
    ChrTalk(
        0x8,
        "客人是瓦吉先生的朋友吗？\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "从左边那扇门进去，\x01",
            "右手边就是瓦吉先生的房间了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CE")

    label("loc_7DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_8C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86B")

    #C0009
    ChrTalk(
        0x8,
        (
            "欢迎，\x01",
            "欢迎光临翠雀酒店。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "今天在本店住宿的\x01",
            "客人实在不少。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "在本店住宿的客人们\x01",
            "似乎都出门\x01",
            "观光游玩了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8C0")

    label("loc_86B")


    #C0012
    ChrTalk(
        0x8,
        (
            "今天在本店住宿的\x01",
            "客人实在不少。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "在本店住宿的客人们\x01",
            "似乎都出门\x01",
            "观光游玩了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C0")

    Jump("loc_8CE")

    label("loc_8C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_8CE")

    label("loc_8CE")

    TalkEnd(0x8)

    label("loc_8D1")

    Return()

    # Function_8_626 end

    def Function_9_8D2(): pass

    label("Function_9_8D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_8E3")
    Jump("loc_AD0")

    label("loc_8E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_8F1")
    Jump("loc_AD0")

    label("loc_8F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_8FF")
    Jump("loc_AD0")

    label("loc_8FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_90D")
    Jump("loc_AD0")

    label("loc_90D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_91B")
    Jump("loc_AD0")

    label("loc_91B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_A09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D1")
    TurnDirection(0xFE, 0x151, 0)

    #C0014
    ChrTalk(
        0xFE,
        (
            "啊，客人…………\x01",
            "………………\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x151,
        "#5705F……嗯？找我有事吗？\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "（啊啊……果然\x01",
            "  长得好漂亮啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x151,
        "#5702F……呵呵，真是个奇怪的女孩。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_A04")

    label("loc_9D1")


    #C0018
    ChrTalk(
        0xFE,
        "啊……您要出门吗？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "路上请小心，\x01",
            "呵呵……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A04")

    Jump("loc_AD0")

    label("loc_A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_END)), "loc_A59")
    TurnDirection(0xFE, 0xA, 0)
    OP_4B(0xA, 0xFF)

    #C0020
    ChrTalk(
        0xFE,
        (
            "呀～怎么办！\x01",
            "看到脸了！\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xA,
        "好啦，你冷静点。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_AD0")

    label("loc_A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_AC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A74")
    Call(0, 11)
    Jump("loc_AC2")

    label("loc_A74")


    #C0022
    ChrTalk(
        0xFE,
        (
            "那位办理完登记入住手续之后\x01",
            "就马上外出的客人……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "长得真是\x01",
            "好可爱哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC2")

    Jump("loc_AD0")

    label("loc_AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_AD0")

    label("loc_AD0")

    TalkEnd(0xFE)
    Return()

    # Function_9_8D2 end

    def Function_10_AD4(): pass

    label("Function_10_AD4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_AE5")
    Jump("loc_C17")

    label("loc_AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_AF3")
    Jump("loc_C17")

    label("loc_AF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_B01")
    Jump("loc_C17")

    label("loc_B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_B0F")
    Jump("loc_C17")

    label("loc_B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_B1D")
    Jump("loc_C17")

    label("loc_B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_B78")

    #C0024
    ChrTalk(
        0xFE,
        (
            "要是有什么问题，\x01",
            "请不要客气，尽管告诉我。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        "我会诚心诚意为您服务的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C17")

    label("loc_B78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_END)), "loc_BB7")

    #C0026
    ChrTalk(
        0xFE,
        (
            "这孩子真是的，\x01",
            "在客人面前也太不成体统了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C17")

    label("loc_BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_C0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD2")
    Call(0, 11)
    Jump("loc_C09")

    label("loc_BD2")


    #C0027
    ChrTalk(
        0xFE,
        (
            "我说你啊，要是有时间闲聊，\x01",
            "还不赶快去打扫下走廊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C09")

    Jump("loc_C17")

    label("loc_C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_C17")

    label("loc_C17")

    TalkEnd(0xFE)
    Return()

    # Function_10_AD4 end

    def Function_11_C1B(): pass

    label("Function_11_C1B")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)

    #C0028
    ChrTalk(
        0x9,
        (
            "那个，你看见了吗？\x01",
            "刚才的客人……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x9,
        (
            "虽然长得超级可爱，\x01",
            "不过是男孩子吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xA,
        (
            "你又～来了……\x01",
            "别说这种话了，\x01",
            "赶快打扫完吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        "啊～好在意……\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_11_C1B end

    def Function_12_CD3(): pass

    label("Function_12_CD3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D82")

    #C0032
    ChrTalk(
        0xFE,
        (
            "这样应该就能\x01",
            "实行我那在烟花下求婚\x01",
            "的计划了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "谢谢，真不知道\x01",
            "该怎么感谢你们才好。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "好吧……为了晚上能顺利求婚，\x01",
            "要开始做心理准备了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F89")

    label("loc_D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_EEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E80")

    #C0035
    ChrTalk(
        0xFE,
        (
            "好、好的……接下来\x01",
            "就要准备去主题公园了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "虽说已经定好了计划，\x01",
            "但是真的能求婚成功吗。\x01",
            "我开始紧张起来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "不、不行……难得你们\x01",
            "帮我找到了戒指。\x01",
            "我可不能打退堂鼓啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "总而言之，\x01",
            "多重复几次\x01",
            "脑内模拟训练吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_EE9")

    label("loc_E80")


    #C0039
    ChrTalk(
        0xFE,
        (
            "请和我结婚吧！\x01",
            "……嗯。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "我们结婚吧！\x01",
            "……这个也不错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "跟我结婚吧混账！\x01",
            "……这个不行吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EE9")

    Jump("loc_F89")

    label("loc_EEE")


    #C0042
    ChrTalk(
        0xFE,
        (
            "好吧……为了晚上能顺利求婚，\x01",
            "要开始做心理准备了。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "我觉得，阿尔维娜是否会\x01",
            "接受我的求婚……\x01",
            "也就决定了我的生死……！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#0006F这话也太夸张了……\x02",
    )

    CloseMessageWindow()

    label("loc_F89")

    Jump("loc_1142")

    label("loc_F8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_FA3")
    Call(0, 27)
    Jump("loc_1142")

    label("loc_FA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_101D")

    #C0045
    ChrTalk(
        0xFE,
        (
            "总、总而言之，你们！\x01",
            "能不能去高级住宅区\x01",
            "那边帮我看看！？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "戒指说不定\x01",
            "还在那个长椅\x01",
            "附近呢……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1142")

    label("loc_101D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_103B")
    Call(0, 26)
    Jump("loc_1142")

    label("loc_103B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1059")
    Call(0, 26)
    Jump("loc_1142")

    label("loc_1059")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1077")
    Call(0, 26)
    Jump("loc_1142")

    label("loc_1077")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_113F")

    #C0047
    ChrTalk(
        0xFE,
        (
            "我完全不记得\x01",
            "将戒指丢在哪里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "不过可以确定的是……\x01",
            "我和阿尔维娜来到这边以后，\x01",
            "基本上到处都逛了一遍。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "总、总而言之……\x01",
            "要是你们捡到了类似的东西，\x01",
            "就都拿来给我看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1142")

    label("loc_113F")

    Call(0, 25)

    label("loc_1142")

    TalkEnd(0xFE)
    Return()

    # Function_12_CD3 end

    def Function_13_1146(): pass

    label("Function_13_1146")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1275")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1196")

    #C0050
    ChrTalk(
        0xFE,
        "托马好像很开心呢。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "是不是有什么\x01",
            "好事呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1270")

    label("loc_1196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_120A")

    #C0052
    ChrTalk(
        0xFE,
        (
            "托马好像打算\x01",
            "在主题公园做什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "呵呵，他有什么心事，都马上会显露在脸上，\x01",
            "真是太容易看穿了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1270")

    label("loc_120A")


    #C0054
    ChrTalk(
        0xFE,
        (
            "别人经常问我，\x01",
            "为什么会和托马\x01",
            "交往……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "你们不觉得托马\x01",
            "看起来就很搞笑吗？\x01",
            "那就是他的魅力啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1270")

    Jump("loc_137B")

    label("loc_1275")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_12FA")

    #C0056
    ChrTalk(
        0xFE,
        (
            "托马真是的……\x01",
            "今天一会消沉沮丧，一会又大喊大叫的，\x01",
            "好像不太对劲呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "哎，算了。\x01",
            "反正他自己也说没什么事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_137B")

    label("loc_12FA")


    #C0058
    ChrTalk(
        0xFE,
        (
            "今晚我要和托马两个人\x01",
            "去夜晚的主题公园。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "听说到时候会放很多烟花，\x01",
            "可以度过一个非常浪漫的\x01",
            "夜晚呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        "呵呵，好期待哦。\x02",
    )

    CloseMessageWindow()

    label("loc_137B")

    TalkEnd(0xFE)
    Return()

    # Function_13_1146 end

    def Function_14_137F(): pass

    label("Function_14_137F")

    TalkBegin(0xFE)

    #C0061
    ChrTalk(
        0xFE,
        (
            "太阳也西沉了，\x01",
            "今天就和我太太回来休息了。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "在房间里一边欣赏主题公园的烟花，\x01",
            "一边品尝葡萄酒，也别有一番风致吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_137F end

    def Function_15_13FE(): pass

    label("Function_15_13FE")

    TalkBegin(0xFE)

    #C0063
    ChrTalk(
        0xFE,
        (
            "事先\x01",
            "预约了酒店，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_13FE end

    def Function_16_1429(): pass

    label("Function_16_1429")

    EventBegin(0x0)
    Fade(1000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, -16950, 0, 11920, 45)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xD, 0x8000)
    OP_68(-240, 1100, 7180, 0)
    MoveCamera(327, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16470, 0)
    SetChrPos(0x101, -500, 0, 6400, 0)
    SetChrPos(0x102, 500, 0, 6400, 0)
    SetChrPos(0x103, 500, 0, 5000, 0)
    SetChrPos(0x104, -500, 0, 5000, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05700.itp")
    OP_0D()

    #C0064
    ChrTalk(
        0x8,
        (
            "#11P欢迎，\x01",
            "欢迎光临翠雀酒店。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "#11P莫非……\x01",
            "各位想在本酒店住宿吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        (
            "#0100F#6P嗯，是的，\x01",
            "不过现在都已经住满了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        "#11P是的，非常抱歉。\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "#11P其实就在不久前，\x01",
            "刚好有位客人取消了预订的房间，\x01",
            "但是那个房间马上就又被预约了。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        "#0106F#6P是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x103,
        "#0206F#6P……真可惜。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#0306F#6P没办法，\x01",
            "去西餐厅那边吧。\x02\x03",

            "#0300F至少可以坐下谈话吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1670():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1670)
    Sleep(50)

    def lambda_1680():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1680)
    Sleep(300)

    #C0072
    ChrTalk(
        0x101,
        "#0006F#11P是啊……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    #Sound(1437, 255, 100, 0)    #voice#Lazy
    Sleep(700)

    #N0073
    NpcTalk(
        0xD,
        "冷静的声音",
        (
            "#4P#24A呵呵……\x01",
            "你们好像有烦恼啊。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-1880, 1100, 6720, 5100)
    MoveCamera(307, 16, 0, 5100)

    def lambda_174E():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_174E)

    def lambda_175B():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_175B)
    Sleep(50)

    def lambda_176B():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_176B)

    def lambda_1778():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1778)
    Sleep(50)

    def lambda_1788():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1788)
    ClearMapObjFlags(0x5, 0x10)
    OP_70(0x5, 0xA)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0xD, 3, 0, 17)
    OP_71(0x5, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x5)
    SetMapObjFlags(0x5, 0x10)
    WaitChrThread(0xD, 3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x8, 1)
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

    #C0074
    ChrTalk(
        0x101,
        "#0005F#12P哎……？\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        "#0105F#12P瓦、瓦吉……？\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        "#2P啊，瓦吉先生……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    #Sound(1435, 255, 100, 0)    #voice#Lazy
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(700)

    #A0077
    AnonymousTalk(
        0xD,
        (
            "你们似乎正因为订不到房间\x01",
            "而发愁吧……\x02\x03",

            "是不是需要一个\x01",
            "可以安静谈话的地方呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0078
    ChrTalk(
        0x101,
        (
            "#0000F#12P啊，是的，\x01",
            "是这样没错……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xD,
        (
            "#5704F#5P#N那就好说了。\x02\x03",

            "把我的房间借给你们吧。\x02",
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

    #C0080
    ChrTalk(
        0x101,
        "#0011F#12P哎！？\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x104,
        "#0305F#6P喂喂，真突然啊。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xD,
        "#5702F#5P#N呵呵，这边走。\x02",
    )

    CloseMessageWindow()
    OP_68(-3940, 1200, 6960, 5000)
    BeginChrThread(0xD, 3, 0, 18)
    WaitChrThread(0xD, 3)
    OP_6F(0x1)
    OP_68(-1350, 1100, 6510, 1200)

    def lambda_1AA3():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AA3)

    def lambda_1AB0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1AB0)
    Sleep(100)

    def lambda_1AC0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1AC0)

    def lambda_1ACD():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1ACD)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0083
    ChrTalk(
        0x102,
        "#0101F#12P怎、怎么办……？\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        (
            "#0211F#6P他的穿着打扮\x01",
            "明显很可疑……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        (
            "#0301F#6P我说，不良团伙的\x01",
            "首领为什么会在\x01",
            "这种地方啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#0006F#5P好、好啦，\x01",
            "反正也不是不了解的陌生人……\x02\x03",

            "#0000F总之，跟去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 40, 0, 6580, 270)
    SetChrPos(0x8, -480, 0, 10050, 180)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 0, 0, 0, 0)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0xA4, 5)
    OP_29(0x47, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_16_1429 end

    def Function_17_1C0B(): pass

    label("Function_17_1C0B")

    OP_95(0xFE, -4000, 0, 8400, 3000, 0x0)
    Return()

    # Function_17_1C0B end

    def Function_18_1C20(): pass

    label("Function_18_1C20")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_96(0xFE, 0xFFFFC037, 0x0, 0x2EEA, 0x9C4, 0x0)
    ClearMapObjFlags(0x5, 0x10)
    OP_71(0x5, 0x0, 0xA, 0x0, 0x0)
    Sound(121, 0, 100, 0)
    OP_79(0x5)

    def lambda_1C5B():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1C5B)
    Sleep(200)

    def lambda_1C73():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1C73)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_71(0x5, 0xA, 0x0, 0x0, 0x0)
    Sound(890, 0, 100, 0)
    OP_79(0x5)
    SetMapObjFlags(0x5, 0x10)
    Return()

    # Function_18_1C20 end

    def Function_19_1CA3(): pass

    label("Function_19_1CA3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50353.itc", 0x1E)
    OP_68(-99800, 1100, 124250, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    OP_4B(0xD, 0xFF)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x2)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xD, -102200, 150, 124000, 90)
    SetChrPos(0x101, -101400, 0, 121700, 0)
    SetChrPos(0x102, -100300, 0, 121700, 315)
    SetChrPos(0x103, -100300, 0, 120400, 315)
    SetChrPos(0x104, -101400, 0, 120400, 0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis063.itp")
    FadeToBright(1000, 0)
    OP_68(-101070, 1100, 122980, 3000)
    OP_6F(0x1)
    OP_0D()

    #C0087
    ChrTalk(
        0xD,
        (
            "#5709F#11P呵呵，话说回来，\x01",
            "你们也很有雅兴嘛。\x02\x03",

            "#5702F在纪念庆典的最终日，\x01",
            "竟然请假来米修拉姆挥霍。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#0012F#6P啊～……\x01",
            "嗯，算是养精蓄锐吧。\x02\x03",

            "#0001F话说回来，瓦吉，\x01",
            "你这身打扮是……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xD,
        (
            "#5704F#11P呵呵，很适合我吧？\x02\x03",

            "#5700F这个算是我\x01",
            "副业的制服啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#0005F#6P副、副业……？\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        "#0101F#6P那到底是什么工作呢……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xD,
        (
            "#5703F#11P在冰冷的上流阶级世界中\x01",
            "有着许多迷失了爱的、\x01",
            "美丽而寂寞的贵妇人们……\x02\x03",

            "#5702F为她们营造短暂的梦境，\x01",
            "就是我的工作。\x02",
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

    #C0093
    ChrTalk(
        0x101,
        "#0011F#6P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x102,
        "#0105F#6P这、这莫非就是……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x103,
        "#0211F#6P所谓的『男公关』吗？\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x104,
        (
            "#0307F#6P喂喂！\x01",
            "你竟然做这种令人羡慕──\x01",
            "不对，是不知廉耻的工作！\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xD,
        (
            "#5702F#11P呵呵，我可不是\x01",
            "因为缺钱才干这行的。\x02\x03",

            "只是一直被她们纠缠不休，\x01",
            "无奈之下才稍作奉陪的。\x02\x03",

            "#5709F嗯，可以算是发善心吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#0006F#6P这是什么借口……\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#0306F#6P也就是说，还有不少\x01",
            "太太喜欢这种\x01",
            "冷冰冰的家伙啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        (
            "#0103F#6P唉……\x01",
            "说实话，我可是不敢苟同。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x103,
        (
            "#0200F#6P这么说，瓦吉先生\x01",
            "是因为男公关的工作而来这里的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xD,
        (
            "#5702F#11P嗯，其实也就是所谓的\x01",
            "护花使者吧。\x02\x03",

            "我要陪同\x01",
            "某位夫人出席一个\x01",
            "有点隐情的宴会。\x02",
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

    #C0103
    ChrTalk(
        0x101,
        "#0005F#6P哎……\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x102,
        "#0101F#6P这……\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    #Sound(1436, 255, 90, 0)    #voice#Lazy
    Sleep(1000)

    #C0105
    ChrTalk(
        0xD,
        "#5704F#11P呵呵……原来如此啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0106
    ChrTalk(
        0x101,
        (
            "#0012F#6P原来如此是指……\x01",
            "嗯，你在说什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xD,
        (
            "#5702F#11P『黑之竞拍会』……\x02\x03",

            "#5702F你们多半是得知了这个名字，\x01",
            "才过来调查的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        "#0001F#6P唔……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x104,
        (
            "#0306F#6P唉……\x01",
            "目的好像暴露了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x102,
        (
            "#0101F#6P如此说来，你说要出席的\x01",
            "那个有点隐情的宴会也就是……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xD,
        (
            "#5700F#11P嗯，就是那个竞拍会。\x02\x03",

            "#5704F去年也陪别的夫人\x01",
            "去过，所以今年是第二次去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        "#0006F#6P是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        (
            "#0206F#6P没想到了解那个竞拍会\x01",
            "的人就近在身边呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xD,
        (
            "#5705F#11P不过，你们是打算\x01",
            "揭发那个竞拍会吗？\x02\x03",

            "我觉得，那实在是有点勉强。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#0006F#6P不……虽然不甘心，\x01",
            "不过我们原本就没打算去揭发它。\x02\x03",

            "#0008F只是想了解一下。\x02\x03",

            "象征着克洛斯贝尔扭曲现状的，\x01",
            "豪华绚烂的地下社交宴会……\x02\x03",

            "#0013F我们需要跨越的『壁障』\x01",
            "究竟高到何种程度。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        "#0105F#6P罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xD,
        (
            "#5702F#11P呵呵……原来如此啊。\x02\x03",

            "#5704F你们的志气我很欣赏，\x01",
            "不过，想参加『竞拍会』的话，\x01",
            "没有邀请卡可是进不去的哦。\x02\x03",

            "他们每年都会在卡片上设计不同的蔷薇标志，\x01",
            "而且上面还附带通行号码，\x01",
            "要伪造恐怕很难……\x02\x03",

            "#5702F我觉得，应该是没办法混进去的。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#0000F#6P关于这点不必担心……\x01",
            "其实，我们有邀请卡的。\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)

    #A0119
    AnonymousTalk(
        0xD,
        (
            "#5705F哎……\x02\x03",

            "#5709F如果问你们是怎么得到的，\x01",
            "是不是就有点不识趣了？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0120
    AnonymousTalk(
        0x101,
        "#0004F嗯，稍微有点内情。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    #C0121
    ChrTalk(
        0x102,
        (
            "#0108F#6P说到这张邀请卡……\x01",
            "在拿着它入场时，会不会被检查身份呢？\x02\x03",

            "#0101F比如仅限会员，或是只有登记过的人\x01",
            "才能进去什么的……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xD,
        (
            "#5705F#11P不，我想应该不会。\x02\x03",

            "#5704F这场活动也有地下社交的含义在内，\x01",
            "所以好像很欢迎新来的客人。\x02\x03",

            "#5702F再加上拍卖品中还有赃物，\x01",
            "所以很多有权人士也会\x01",
            "想要隐藏身份。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x104,
        (
            "#0300F#6P唔，这样的话，\x01",
            "说不定能顺利混进去。\x02\x03",

            "#0305F话说回来，一张邀请卡\x01",
            "可以让几个人进去呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xD,
        (
            "#5703F#11P关于这点，好像并没有硬性规定……\x01",
            "不过基本都是两人一组去的。\x02\x03",

            "#5700F四人一组进去的话，\x01",
            "未免也太显眼了，我可不推荐呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x103,
        "#0201F#6P原来如此……\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        (
            "#0106F#6P……这么一说，\x01",
            "的确有道理呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xD,
        (
            "#5704F#11P而且，那终究是场宴会，\x01",
            "最好还是穿正装参加吧。\x02\x03",

            "#5702F不过，穿成我这样，\x01",
            "故意引人注目也是一种选择。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        "#0006F#6P那还是免了吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    #C0129
    ChrTalk(
        0x101,
        (
            "#0001F#5P──那个，艾莉。\x02\x03",

            "有没有可以弄到\x01",
            "宴会正装的地方呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(150)

    #C0130
    ChrTalk(
        0x102,
        (
            "#0102F#12P要换正装的话，楼下的精品店\x01",
            "应该正合适。\x02\x03",

            "我以前来的时候也去过，\x01",
            "衣服钱就先由我垫付吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        "#0011F#5P不，这个就……\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x102,
        (
            "#0104F#12P这点小事就不必客气了。\x02\x03",

            "#0100F现在更重要的问题是\x01",
            "决定潜入的成员吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        (
            "#0006F#5P嗯……是啊。\x02\x03",

            "#0008F用抽签或猜拳\x01",
            "来决定好像也不太合适……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x104,
        (
            "#0306F#6P喂喂，说什么呢。\x02\x03",

            "#0300F至少你肯定要去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        "#0005F#5P哎……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(500)

    #C0136
    ChrTalk(
        0x103,
        (
            "#0204F#6P对于这次的事情，最介怀的\x01",
            "就是罗伊德前辈……\x02\x03",

            "#0202F而且你是我们的队长，\x01",
            "你去是理所当然的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        "#0005F#5P可、可是……\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x102,
        (
            "#0103F#12P真是的，你就坦率地\x01",
            "接受吧。\x02\x03",

            "#0102F你也很想亲眼看看吧？\x01",
            "克洛斯贝尔那『扭曲』的实态。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0139
    ChrTalk(
        0x101,
        (
            "#0004F#5P──好吧，\x01",
            "那我就接受了。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xD,
        (
            "#5704F#11P呵呵，那你再决定一个\x01",
            "同行的人选就好了。\x02\x03",

            "#5702F如果一个人参加的话，\x01",
            "反而会更加显眼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#0006F#5P是啊……嗯～\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x102,
        (
            "#0103F#12P是选我、缇欧，还是兰迪。\x02\x03",

            "#0100F选择的时候，或许也应该\x01",
            "考虑到有黑手党在场的情况呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x103,
        (
            "#0204F#6P剩下的两人就在会场外\x01",
            "待命，以防紧急状况发生。\x02\x03",

            "#0202F任务分配应该就是这样吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x104,
        (
            "#0302F#6P嗯，不管怎么分工，\x01",
            "现在还是先去楼下的精品店看看吧。\x02\x03",

            "在换上正装之前\x01",
            "决定好带谁去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        (
            "#0000F#5P……嗯，\x01",
            "就这么办吧。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17500, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetChrChipByIndex(0xD, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    AddParty(0x50, 0xFF, 0xFF)
    OP_68(-100000, 1250, 12500, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18600, 0)
    SetChrPos(0x101, -100030, 0, 14990, 180)
    SetChrPos(0x102, -100030, 0, 14990, 180)
    SetChrPos(0x103, -100030, 0, 14990, 180)
    SetChrPos(0x104, -100030, 0, 14990, 180)
    SetChrPos(0x151, -100030, 0, 14990, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x151, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    SetCameraDistance(17600, 2500)
    OP_6F(0x10)
    OP_0D()
    Sound(121, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x2)
    OP_68(-100000, 1250, 10500, 4000)
    BeginChrThread(0x101, 3, 0, 20)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 22)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 23)
    Sleep(1000)
    BeginChrThread(0x151, 3, 0, 24)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x151, 3)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sleep(100)
    Sound(890, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    OP_6F(0x1)
    TurnDirection(0x101, 0x151, 400)

    #C0146
    ChrTalk(
        0x101,
        (
            "#0011F#6P──等一下。\x02\x03",

            "#0001F为什么连瓦吉\x01",
            "也要跟来？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3183():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3183)
    Sleep(100)

    def lambda_3193():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3193)

    def lambda_31A0():
        TurnDirection(0xFE, 0x151, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_31A0)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0147
    ChrTalk(
        0x151,
        (
            "#5709F#11P呵呵，机会难得，\x01",
            "我可以给你们提供一些\x01",
            "搭配服装的诀窍嘛。\x02\x03",

            "#5702F还可以教你们如何混过\x01",
            "黑手党的盘查哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        (
            "#0006F#6P嗯～……\x01",
            "好吧，既然是这样的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x103,
        (
            "#0211F#6P但你明显只是\x01",
            "为了满足自己的兴趣而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x104,
        "#0302F#5P好啦，就姑且听听他能说出些什么吧。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x102,
        (
            "#0100F#5P那么，我们现在就去\x01",
            "楼下的精品店吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -99720, 0, 10000, 90)
    SetScenarioFlags(0xA4, 6)
    OP_29(0x47, 0x1, 0x5)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, -93960, 0, 8260, 0)
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 94190, 0, 11580, 0)
    BeginChrThread(0xA, 0, 0, 2)
    EventEnd(0x5)
    Return()

    # Function_19_1CA3 end

    def Function_20_335A(): pass

    label("Function_20_335A")


    def lambda_335F():
        OP_95(0xFE, -100000, 0, 9000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_335F)

    def lambda_3379():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3379)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_3392():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3392)
    WaitChrThread(0x101, 1)
    Return()

    # Function_20_335A end

    def Function_21_339F(): pass

    label("Function_21_339F")


    def lambda_33A4():
        OP_95(0xFE, -100000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33A4)

    def lambda_33BE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_33BE)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_33D7():
        OP_95(0xFE, -101200, 0, 10800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33D7)
    WaitChrThread(0xFE, 1)

    def lambda_33F5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33F5)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_21_339F end

    def Function_22_3402(): pass

    label("Function_22_3402")


    def lambda_3407():
        OP_95(0xFE, -100000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3407)

    def lambda_3421():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3421)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_343A():
        OP_95(0xFE, -98800, 0, 10200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_343A)
    WaitChrThread(0xFE, 1)

    def lambda_3458():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3458)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_3402 end

    def Function_23_3465(): pass

    label("Function_23_3465")


    def lambda_346A():
        OP_95(0xFE, -100000, 0, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_346A)

    def lambda_3484():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3484)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_349D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_349D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_3465 end

    def Function_24_34AA(): pass

    label("Function_24_34AA")


    def lambda_34AF():
        OP_95(0xFE, -98610, 0, 11590, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34AF)

    def lambda_34C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_34C9)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_34E2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34E2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_34AA end

    def Function_25_34EF(): pass

    label("Function_25_34EF")

    EventBegin(0x0)
    Fade(500)
    OP_68(97820, 900, 122220, 0)
    MoveCamera(313, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20810, 0)
    SetChrPos(0x101, 98200, 0, 121000, 270)
    SetChrPos(0x102, 98200, 0, 122200, 270)
    SetChrPos(0x103, 99400, 0, 121000, 270)
    SetChrPos(0x104, 99400, 0, 122200, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_3582")
    SetChrPos(0x151, 100600, 0, 121600, 270)

    label("loc_3582")

    OP_4B(0xE, 0xFF)
    OP_93(0xE, 0x10E, 0x0)
    SetChrSubChip(0xE, 0x0)
    OP_4B(0xF, 0xFF)
    SetChrSubChip(0xF, 0x0)
    OP_0D()

    #C0152
    ChrTalk(
        0xE,
        (
            "#5P为什么啊……\x01",
            "我到底做了什么啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xE, 0x5A, 0x1F4)

    #C0153
    ChrTalk(
        0xE,
        (
            "#5P你们……\x01",
            "在米修拉姆疗养地\x01",
            "有没有捡到什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xE,
        (
            "#5P怎么说呢，那个……\x01",
            "比如说，类似订婚戒指的指环什么的。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        (
            "#12P#0005F不，什么也没捡到过……\x02\x03",

            "#0001F……您把订婚戒指\x01",
            "弄丢了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xE,
        "#5P#5S哇～声音太大啦！\x02",
    )

    CloseMessageWindow()
    OP_68(99540, 1200, 123070, 2000)
    OP_6F(0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xF, 0x10E, 0x1F4)

    #C0157
    ChrTalk(
        0xF,
        (
            "#12P托马？你怎么了，\x01",
            "突然叫得那么大声。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)

    #C0158
    ChrTalk(
        0xE,
        (
            "#5P呃……啊，不……\x01",
            "没、没什么啦，\x01",
            "阿尔维娜。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xF,
        (
            "#12P……是吗？\x01",
            "呵呵，托马好奇怪啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x1F4)
    OP_68(97820, 900, 122220, 2000)
    OP_6F(0x1)

    #C0160
    ChrTalk(
        0xE,
        (
            "#5P……差、差点就被\x01",
            "阿尔维娜发现啦。\x01",
            "你可真是的……！\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        (
            "#12P#0006F哦、哦……对不起。\x01",
            "（刚才那是我的错吗……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xE,
        (
            "#5P总而言之……\x01",
            "作为道歉，你要帮我的忙。\x01",
            "帮我找戒指。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x104,
        (
            "#12P#0303F喂喂……\x01",
            "为了什么道歉啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x103,
        (
            "#12P#0203F我觉得完全没有这个义务。\x01",
            "无视他就好，我们走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xE,
        (
            "#5P失、失礼了，是我用词不当。\x01",
            "求你们了，帮帮我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xE,
        (
            "#5P你们知道在今晚的\x01",
            "主题公园夜场会燃放烟花吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xE,
        (
            "#5P那枚戒指，我无论如何\x01",
            "也想在那种绝佳的\x01",
            "气氛中交给女朋友啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_39F0")

    #C0168
    ChrTalk(
        0x151,
        "#5700F#12P呵呵，还挺浪漫呢。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x102,
        (
            "#12P#0102F嗯，是呀。\x02\x03",

            "#0100F虽然我们也\x01",
            "没多少空闲时间……\x01",
            "不过就帮您留意一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A4E")

    label("loc_39F0")


    #C0170
    ChrTalk(
        0x102,
        (
            "#12P#0102F呵呵……真不错呢。\x02\x03",

            "#0100F虽然我们也\x01",
            "没多少空闲时间……\x01",
            "不过就帮您留意一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A4E")


    #C0171
    ChrTalk(
        0xE,
        "#5P哦哦……真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        "#12P#0011F……艾、艾莉？\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x102,
        (
            "#12P#0104F呵呵，没关系嘛。\x02\x03",

            "这是他为了女朋友\x01",
            "拼命想出来的\x01",
            "求婚方案啊。\x02\x03",

            "#0100F如果不能顺利实施，\x01",
            "他的女朋友也很可怜嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_3BBA")

    #C0174
    ChrTalk(
        0x101,
        (
            "#12P#0006F话虽如此，\x01",
            "但终究不能让瓦吉这个民间人士\x01",
            "跟我们一起到处跑……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x151,
        (
            "#5704F#12P我可是完全不介意哦。\x02\x03",

            "#5700F嗯，只要别忘记\x01",
            "自己来此的首要目的\x01",
            "就没问题了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BEC")

    label("loc_3BBA")


    #C0176
    ChrTalk(
        0x101,
        (
            "#12P#0003F嗯，是啊～……\x01",
            "的确是有点\x01",
            "可怜……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BEC")


    #C0177
    ChrTalk(
        0x102,
        (
            "#12P#0100F呵呵，那就这么定了。\x02\x03",

            "#0105F那么……关于丢失的地点，\x01",
            "你有没有头绪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xE,
        (
            "#5P很遗憾，没有。\x01",
            "我完全没有印象了。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xE,
        (
            "#5P非要说的话……\x01",
            "我和阿尔维娜来到这边以后，\x01",
            "基本上到处都逛了一遍。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xE,
        "#5P不过在宝石店吃了闭门羹呢。\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x103,
        (
            "#12P#0203F……这提示\x01",
            "也太粗略了点。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xE,
        (
            "#5P总、总而言之……\x01",
            "要是你们捡到了类似的东西，\x01",
            "就都拿来给我看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xE,
        (
            "#5P到了晚上，\x01",
            "我们就要进主题公园了。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xE,
        "#5P知道了吗，拜托了哦！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0185
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【订婚戒指在何处】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_93(0xE, 0x10E, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    SetChrPos(0x0, 97960, 0, 122140, 270)
    OP_29(0x24, 0x4, 0x2)
    OP_29(0x24, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_25_34EF end

    def Function_26_3E13(): pass

    label("Function_26_3E13")

    EventBegin(0x0)
    Fade(500)
    OP_68(97820, 900, 122220, 0)
    MoveCamera(313, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20810, 0)
    SetChrPos(0x101, 98200, 0, 121000, 270)
    SetChrPos(0x102, 98200, 0, 122200, 270)
    SetChrPos(0x103, 99400, 0, 121000, 270)
    SetChrPos(0x104, 99400, 0, 122200, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_3EA6")
    SetChrPos(0x151, 100600, 0, 121600, 270)

    label("loc_3EA6")

    OP_4B(0xE, 0xFF)
    OP_93(0xE, 0x5A, 0x0)
    SetChrSubChip(0xE, 0x0)
    OP_4B(0xF, 0xFF)
    SetChrSubChip(0xF, 0x0)
    OP_0D()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0186
    ChrTalk(
        0xE,
        (
            "#5P难不成……\x01",
            "你们帮我\x01",
            "找到戒指了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        (
            "#12P#0000F嗯，这是在米修拉姆地区内\x01",
            "捡到的。\x02\x03",

            "请确认一下\x01",
            "是不是您的东西。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F98")
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0188
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x34C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_3F98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FCB")
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0189
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x34D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_3FCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FFE")
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0190
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x34E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_3FFE")

    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0191
    ChrTalk(
        0xE,
        "#5P唔，我看看……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40C9")

    #C0192
    ChrTalk(
        0xE,
        "#5P……这枚金戒指……\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xE,
        (
            "#5P……不对，\x01",
            "不是这个戒指啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xE,
        (
            "#5P虽然外观设计相似，\x01",
            "但是色泽完全不对。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x24, 0x1, 0x2)

    label("loc_40C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4157")

    #C0195
    ChrTalk(
        0xE,
        "#5P……这枚珍珠戒指……\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xE,
        (
            "#5P……不对，\x01",
            "不是这个啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xE,
        (
            "#5P虽然的确很漂亮……\x01",
            "但是和我买的\x01",
            "一点也不像。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x24, 0x1, 0x4)

    label("loc_4157")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41DE")

    #C0198
    ChrTalk(
        0xE,
        "#5P……这枚白金戒指……\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xE,
        (
            "#5P……不对，\x01",
            "不是这个啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xE,
        (
            "#5P这么俗气的东西，\x01",
            "怎么能送给女朋友呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x24, 0x1, 0x6)

    label("loc_41DE")

    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0201
    ChrTalk(
        0x101,
        "#12P#0006F是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xE,
        (
            "#5P这个戒指还给你，\x01",
            "随你怎么处置吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0203
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "托马把交给他的戒指还了回来。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C69")
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xE)

    #C0204
    ChrTalk(
        0xE,
        (
            "#5P……明明都找到了\x01",
            "这么多戒指，\x01",
            "竟然没有我的戒指……\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xE,
        (
            "#5P唉……\x01",
            "到底丢在\x01",
            "哪里了呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x102,
        (
            "#12P#0100F那个……\x01",
            "请不要泄气。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_4480")

    #C0207
    ChrTalk(
        0x151,
        (
            "#5706F#12P不过……还能\x01",
            "到哪里去找呢？\x02\x03",

            "#5702F说不定都已经\x01",
            "被别人捡走了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        "#6P#0011F瓦、瓦吉……！\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xE,
        "#5P……果、果然是这样吗……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xE)

    #C0210
    ChrTalk(
        0x104,
        "#12P#0306F喂喂，他消沉了哦。\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x151,
        (
            "#5709F#12P啊哈哈，\x01",
            "开个小玩笑嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4586")

    label("loc_4480")


    #C0212
    ChrTalk(
        0x104,
        (
            "#12P#0306F话说，都已经找了这么多地方，\x01",
            "却还是没找到，该不会是已经\x01",
            "被别人捡走了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x101,
        "#6P#0011F兰、兰迪……！\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xE,
        "#5P……果、果然是这样吗……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xE)

    #C0215
    ChrTalk(
        0x103,
        (
            "#12P#0203F……完全\x01",
            "消沉下去了呢，\x01",
            "都怪兰迪前辈。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x104,
        "#12P#0306F怎、怎么怪我啊……\x02",
    )

    CloseMessageWindow()

    label("loc_4586")

    OP_68(99540, 1200, 123070, 2000)
    OP_6F(0x1)
    OP_93(0xF, 0x10E, 0x1F4)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(99270, 1200, 122850, 2000)
    OP_95(0xF, 102010, 0, 123530, 2000, 0x0)
    TurnDirection(0xF, 0xE, 500)
    OP_6F(0x1)

    #C0217
    ChrTalk(
        0xF,
        (
            "#12P……托马？怎么了，\x01",
            "你好像很没精神啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4617():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4617)
    Sleep(100)

    def lambda_4627():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4627)
    Sleep(50)

    def lambda_4637():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4637)
    Sleep(100)

    def lambda_4647():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4647)
    Sleep(50)

    def lambda_4657():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4657)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_4678")

    def lambda_4670():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4670)

    label("loc_4678")


    #C0218
    ChrTalk(
        0xE,
        (
            "#5P哎！？\x01",
            "不，呃，那个……\x01",
            "什么事也没有，嗯。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xF,
        (
            "#12P……是吗？\x01",
            "你看起来可不像没事啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xF,
        (
            "#12P那个，托马，\x01",
            "如果你不舒服的话，\x01",
            "要不要去高级住宅区那边透透气？\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xF,
        (
            "#12P上午散步的时候，\x01",
            "我们不是一起在\x01",
            "湖畔的长椅上休息了一下嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xE,
        "#5P嗯，是啊……\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xE,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xE)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0224
    ChrTalk(
        0xE,
        "#5P#5S啊……啊啊啊啊啊啊啊啊啊！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_485D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_485D)
    Sleep(100)

    def lambda_486D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_486D)
    Sleep(50)

    def lambda_487D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_487D)
    Sleep(100)

    def lambda_488D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_488D)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_48AE")

    def lambda_48A6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_48A6)

    label("loc_48AE")


    #C0225
    ChrTalk(
        0x101,
        "#12P#0005F托、托马先生？\x02",
    )

    CloseMessageWindow()

    def lambda_48D1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_48D1)

    #C0226
    ChrTalk(
        0xE,
        (
            "#5P想起来了，我想起来了！\x01",
            "一定是那个时候！\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xE,
        (
            "#5P和阿尔维娜一起\x01",
            "坐在长椅上的时候……\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xE,
        (
            "#5P我曾经把手伸进口袋，\x01",
            "确认了一下那个的存在啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xE,
        (
            "#5P之后回到酒店，\x01",
            "再掏口袋的时候，\x01",
            "就已经不见了……\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xE,
        (
            "#5P如果真是弄丢了，\x01",
            "也只可能是在那个时候，\x01",
            "丢在那个地方了！！\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x101,
        "#12P#0005F真、真的吗？\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x103,
        (
            "#12P#0200F突然就给出了\x01",
            "很重要的线索呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xF,
        (
            "#12P……那个，托马，\x01",
            "你从刚才起，一直在说什么呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4A6E():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4A6E)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)

    #C0234
    ChrTalk(
        0xE,
        (
            "#5P不、不，真的\x01",
            "没什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xE,
        (
            "#5P好啦，阿尔维娜，\x01",
            "你就好好欣赏一下\x01",
            "米修拉姆的美丽街景吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xF,
        (
            "#12P……是吗？\x01",
            "真奇怪呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(97670, 1200, 121980, 2000)
    OP_95(0xF, 103230, 0, 124330, 2000, 0x0)
    OP_93(0xF, 0x0, 0x1F4)
    OP_6F(0x1)

    #C0237
    ChrTalk(
        0xE,
        "#5P好、好险……\x02",
    )

    CloseMessageWindow()

    def lambda_4B56():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4B56)

    #C0238
    ChrTalk(
        0xE,
        (
            "#5P总、总而言之，你们几位！\x01",
            "能不能再去高级住宅区\x01",
            "那边帮我看看！？\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xE,
        (
            "#5P戒指说不定\x01",
            "还在那个长椅\x01",
            "附近呢……！\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x102,
        (
            "#12P#0100F是啊……\x01",
            "罗伊德，过去确认\x01",
            "一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x101,
        "#12P#0000F说得也是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_4C5E")

    #C0242
    ChrTalk(
        0x151,
        (
            "#5709F#12P哈哈，和你们在一起，\x01",
            "真是不会无聊啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C5E")

    OP_29(0x24, 0x1, 0x7)
    Jump("loc_4CCF")

    label("loc_4C69")


    #C0243
    ChrTalk(
        0xE,
        (
            "#5P唉……\x01",
            "到底丢在\x01",
            "哪里了呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xE,
        (
            "#5P总而言之……\x01",
            "要是你们捡到了类似的戒指，\x01",
            "就再拿来给我看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CCF")

    OP_93(0xE, 0x10E, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    SetChrPos(0x0, 97960, 0, 122140, 270)
    EventEnd(0x5)
    Return()

    # Function_26_3E13 end

    def Function_27_4CF2(): pass

    label("Function_27_4CF2")

    EventBegin(0x0)
    Fade(500)
    OP_68(97820, 900, 122220, 0)
    MoveCamera(313, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20810, 0)
    SetChrPos(0x101, 98200, 0, 121000, 270)
    SetChrPos(0x102, 98200, 0, 122200, 270)
    SetChrPos(0x103, 99400, 0, 121000, 270)
    SetChrPos(0x104, 99400, 0, 122200, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_4D85")
    SetChrPos(0x151, 100600, 0, 121600, 270)

    label("loc_4D85")

    OP_4B(0xE, 0xFF)
    OP_93(0xE, 0x5A, 0x0)
    SetChrSubChip(0xE, 0x0)
    OP_4B(0xF, 0xFF)
    SetChrSubChip(0xF, 0x0)
    OP_0D()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0245
    ChrTalk(
        0xE,
        "#5P啊！是你们……！\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xE,
        (
            "#5P难不成……\x01",
            "终于帮我\x01",
            "找到戒指了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        (
            "#12P#0000F嗯，找到了类似的东西，\x01",
            "请您确认一下。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0248
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x34F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('点唱机', 1)

    #C0249
    ChrTalk(
        0xE,
        "#5P唔，我看看……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xE)

    #C0250
    ChrTalk(
        0xE,
        "#5P……就、就是这个……\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xE,
        "#5P就是这个戒指啊，没错！\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xE,
        (
            "#5P银耀石材质的戒指上刻着\x01",
            "我和阿尔维娜的名字……\x01",
            "的确是我的，没错啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        (
            "#12P#0012F是、是吗，\x01",
            "那可太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x104,
        (
            "#12P#0306F哎呀哎呀，\x01",
            "我还在担心，你如果又说不是，\x01",
            "可该怎么办呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_5003")

    #C0255
    ChrTalk(
        0x151,
        (
            "#5702F#12P呵呵，那样的话，\x01",
            "再到别处去找不就好了嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x103,
        "#12P#0206F这玩笑开过头了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_501B")

    label("loc_5003")


    #C0257
    ChrTalk(
        0x103,
        "#12P#0206F真是的。\x02",
    )

    CloseMessageWindow()

    label("loc_501B")


    #C0258
    ChrTalk(
        0x102,
        (
            "#12P#0100F呵呵，太好了呢，\x01",
            "顺利找到了戒指。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xE,
        "#5P嗯，谢谢你们……！\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xE,
        (
            "#5P在进入主题公园之前\x01",
            "能够找到，真是太好了！\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xE,
        (
            "#5P这样应该就能\x01",
            "实行我那烟花下的\x01",
            "求婚计划了。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xE,
        (
            "#5P谢谢，真不知道\x01",
            "该怎么感谢你们才好。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xE,
        (
            "#5P对了，不嫌弃的话，\x01",
            "能不能收下这个？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0264
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x9A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('封技之刃', 1)

    #C0265
    ChrTalk(
        0x101,
        (
            "#12P#0005F哎……这、这样好吗？\x01",
            "将这么好的东西送给我们……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xE,
        (
            "#5P嗯，请不必客气，\x01",
            "这是我对你们的一片感激之情。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xE,
        (
            "#5P好……为了晚上能顺利求婚，\x01",
            "要开始做心理准备了。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xE,
        (
            "#5P如果以后还有机会见面的话，\x01",
            "还请多多关照啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0269
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【订婚戒指在何处】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_93(0xE, 0x10E, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    SetChrPos(0x0, 97960, 0, 122140, 270)
    OP_29(0x24, 0x1, 0xA)
    OP_29(0x24, 0x4, 0x10)
    SetScenarioFlags(0x0, 3)
    EventEnd(0x5)
    Return()

    # Function_27_4CF2 end

    def Function_28_52D3(): pass

    label("Function_28_52D3")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0270
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "    ～楼梯间～\x01",
            "现在三楼的ＶＩＰ层\x01",
            "已被包场，\x01",
            "无关人士请勿入内。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_28_52D3 end

    def Function_29_534C(): pass

    label("Function_29_534C")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0271
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门似乎上了锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_29_534C end

    SaveToFile()

Try(main)
