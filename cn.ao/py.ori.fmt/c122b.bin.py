from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c122b.bin",                # FileName
        "c122b",                    # MapName
        "c122b",                    # Location
        0x0020,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "c122b",                  # 0
        "接待小姐托莉亚",         # 1
        "格蕾丝",                 # 2
        "雷因兹",                 # 3
        "马凯奈",                 # 4
        "总编",                   # 5
        "奥赛尔",                 # 6
        "技师",                   # 7
        "猎兵",                   # 8
        "猎兵",                   # 9
        "bc122b",                 # 10
    ))

    ATBonus("ATBonus_268", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_288", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_28C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_290", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_30C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_310", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_314", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_318", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_31C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_320", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_324", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_328", 0x004A, 3, 6, 45, 3, 3, 30, 0, "bc122b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms41900.dat", "ms41900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_288", "MonsterBattlePostion_308", "ed7544", "ed7453", "ATBonus_268"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch26600.itc",                   # 00
        "chr/ch26602.itc",                   # 01
        "chr/ch06000.itc",                   # 02
        "chr/ch28100.itc",                   # 03
        "chr/ch26700.itc",                   # 04
        "chr/ch20200.itc",                   # 05
        "chr/ch25200.itc",                   # 06
        "chr/ch25202.itc",                   # 07
        "chr/ch26000.itc",                   # 08
    ))

    DeclNpc(5789,    0,       -430,    270,  389,  0x0, 0,   1,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(60619,   0,       11819,   270,  389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(59009,   0,       11810,   90,   389,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(5099,    0,       60020,   0,    389,  0x0, 0,   4,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(65879,   0,       129,     89,   389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(300,     0,       56950,   180,  389,  0x0, 0,   7,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(67139,   0,       -319,    90,   389,  0x0, 0,   8,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   8,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   8,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 24,  -6.369999885559082,    4.800000190734863,     0.0,                   6.25,                  [0.40000003576278687,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   2.5480000972747803,    -2.4000000953674316,   -0.0,                  1.0])

    DeclActor(4100,    0,       -520,    1500,    5500,    1800,    -470,    0x007E, 0,  3,  0x0000)

    ChipFrameInfo(1008, 0)                                       # 0

    ScpFunction((
        "Function_0_3F0",          # 00, 0
        "Function_1_4A0",          # 01, 1
        "Function_2_59C",          # 02, 2
        "Function_3_5EF",          # 03, 3
        "Function_4_821",          # 04, 4
        "Function_5_94E",          # 05, 5
        "Function_6_A4D",          # 06, 6
        "Function_7_D2C",          # 07, 7
        "Function_8_E7C",          # 08, 8
        "Function_9_EED",          # 09, 9
        "Function_10_F74",         # 0A, 10
        "Function_11_1A16",        # 0B, 11
        "Function_12_1A50",        # 0C, 12
        "Function_13_1A9E",        # 0D, 13
        "Function_14_1AD8",        # 0E, 14
        "Function_15_1AFE",        # 0F, 15
        "Function_16_1B42",        # 10, 16
        "Function_17_1B90",        # 11, 17
        "Function_18_1BC0",        # 12, 18
        "Function_19_1BF0",        # 13, 19
        "Function_20_1C0C",        # 14, 20
        "Function_21_1C28",        # 15, 21
        "Function_22_1C44",        # 16, 22
        "Function_23_1C60",        # 17, 23
        "Function_24_1C7C",        # 18, 24
        "Function_25_1F77",        # 19, 25
        "Function_26_1F8C",        # 1A, 26
        "Function_27_1FB5",        # 1B, 27
        "Function_28_1FDE",        # 1C, 28
        "Function_29_29B9",        # 1D, 29
        "Function_30_3671",        # 1E, 30
        "Function_31_36CC",        # 1F, 31
        "Function_32_3774",        # 20, 32
    ))


    def Function_0_3F0(): pass

    label("Function_0_3F0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_428"),
        (1, "loc_434"),
        (2, "loc_440"),
        (3, "loc_44C"),
        (4, "loc_458"),
        (5, "loc_464"),
        (6, "loc_470"),
        (SWITCH_DEFAULT, "loc_47C"),
    )


    label("loc_428")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_434")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_440")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_44C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_458")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_464")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_470")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_47C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_488")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_49F")

    Return()

    # Function_0_3F0 end

    def Function_1_4A0(): pass

    label("Function_1_4A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4AE")
    Jump("loc_55D")

    label("loc_4AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_55D")
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 2)), scpexpr(EXPR_END)), "loc_528")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrChipByIndex(0xD, 0x7)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_514")
    SetChrFlags(0xA, 0x10)

    label("loc_514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_523")
    SetChrFlags(0x9, 0x10)

    label("loc_523")

    Jump("loc_55D")

    label("loc_528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 1)), scpexpr(EXPR_END)), "loc_555")
    SetChrChipByIndex(0x8, 0x0)
    SetChrChipByIndex(0xD, 0x6)
    SetChrPos(0x8, 3450, 20, -20, 270)
    BeginChrThread(0x8, 0, 0, 0)
    Jump("loc_55D")

    label("loc_555")

    SetChrChipByIndex(0x8, 0x0)
    SetChrChipByIndex(0xD, 0x6)

    label("loc_55D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_578")
    Event(0, 10)
    Jump("loc_59B")

    label("loc_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59B")
    Event(0, 28)

    label("loc_59B")

    Return()

    # Function_1_4A0 end

    def Function_2_59C(): pass

    label("Function_2_59C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B2")
    OP_70(0xB, 0xB)

    label("loc_5B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CD")
    OP_66(0x0, 0x1)
    Jump("loc_5D1")

    label("loc_5CD")

    OP_65(0x0, 0x1)

    label("loc_5D1")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EE")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5EE")

    Return()

    # Function_2_59C end

    def Function_3_5EF(): pass

    label("Function_3_5EF")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_600")
    Jump("loc_81D")

    label("loc_600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_81D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 2)), scpexpr(EXPR_END)), "loc_6DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67F")

    #C0001
    ChrTalk(
        0x8,
        (
            "多谢各位\x01",
            "救了我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "如果没有你们前来救援，\x01",
            "说不定我至今仍在\x01",
            "接待室的角落发抖呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_6D7")

    label("loc_67F")


    #C0003
    ChrTalk(
        0x8,
        (
            "如果没有你们前来救援，\x01",
            "说不定我至今仍在\x01",
            "接待室的角落发抖呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        "实在是感激不尽。\x02",
    )

    CloseMessageWindow()

    label("loc_6D7")

    Jump("loc_81D")

    label("loc_6DC")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_72B"),
        (1, "loc_792"),
        (2, "loc_818"),
        (SWITCH_DEFAULT, "loc_81D"),
    )


    label("loc_72B")


    #C0005
    ChrTalk(
        0x8,
        (
            "（这里有急救箱，\x01",
            "  可以给各位做一些应急处理。）\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "（格蕾丝小姐他们……\x01",
            "  就拜托大家了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81D")

    label("loc_792")


    #C0007
    ChrTalk(
        0x8,
        (
            "（明白了，\x01",
            "  请注意不要发出声响哦。）\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_0D()

    #C0008
    ChrTalk(
        0x8,
        (
            "（格蕾丝小姐他们……\x01",
            "  就拜托大家了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81D")

    label("loc_818")

    Jump("loc_81D")

    label("loc_81D")

    TalkEnd(0x8)
    Return()

    # Function_3_5EF end

    def Function_4_821(): pass

    label("Function_4_821")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_832")
    Jump("loc_94A")

    label("loc_832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_94A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E0")

    #C0009
    ChrTalk(
        0xFE,
        (
            "哎呀呀，这次可真是\x01",
            "被卷进大事件了。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "幸好没人受伤……\x01",
            "但格蕾丝总是那么乱来。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "好胜虽然是优点，但她老是那样子，\x01",
            "有多少条命也不够用啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_94A")

    label("loc_8E0")


    #C0012
    ChrTalk(
        0xFE,
        (
            "幸好没人受伤……\x01",
            "但格蕾丝总是那么乱来。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "好胜虽然是优点，但她老是那样子，\x01",
            "有多少条命也不够用啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94A")

    TalkEnd(0xFE)
    Return()

    # Function_4_821 end

    def Function_5_94E(): pass

    label("Function_5_94E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_95F")
    Jump("loc_A49")

    label("loc_95F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_A49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F0")

    #C0014
    ChrTalk(
        0xFE,
        (
            "我来这里送外卖的时候，\x01",
            "那些全身武装的男人\x01",
            "突然就冲了进来。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "外边现在一片混乱，\x01",
            "不知我那个小摊子\x01",
            "是否还好……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_A49")

    label("loc_9F0")


    #C0016
    ChrTalk(
        0xFE,
        (
            "那可是自我在克洛斯贝尔卖面以来，\x01",
            "一直甘苦与共的摊子……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "……真希望它平安无事。\x02",
    )

    CloseMessageWindow()

    label("loc_A49")

    TalkEnd(0xFE)
    Return()

    # Function_5_94E end

    def Function_6_A4D(): pass

    label("Function_6_A4D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A5E")
    Jump("loc_D28")

    label("loc_A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_D28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA1")
    OP_4B(0xA, 0x0)

    #C0018
    ChrTalk(
        0xFE,
        "#02101F雷因兹，你带好相机了吧？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xA,
        "是、是的，已经准备周全了！\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00011F格蕾丝小姐……\x01",
            "你们该不会是打算出去取材吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        (
            "#00101F外面现在十分危险，\x01",
            "你们还是别出去比较好……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 500)

    #C0022
    ChrTalk(
        0xFE,
        (
            "#02103F这叫什么话！我们怎么能\x01",
            "放过这样的重大事件！\x02\x03",

            "#02101F身为一名新闻工作者，\x01",
            "我肩负着自己的使命，必须要把目睹\x01",
            "到的事件真相传达给各位市民！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        "#00206F……看来已经阻止不了她了。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#00006F呼……是啊。\x02\x03",

            "#00001F在如今这种状况下，接下来还不知会\x01",
            "发生什么事，请二位一定要万分小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "#02102F呵呵，我当然明白。\x02\x03",

            "罗伊德，你们也要\x01",
            "多加小心哦！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 3)
    OP_4C(0xA, 0x0)
    Jump("loc_D28")

    label("loc_CA1")


    #C0026
    ChrTalk(
        0xFE,
        (
            "#02103F我们绝对不能\x01",
            "放过这种重大事件！\x02\x03",

            "#02101F身为一名新闻工作者，\x01",
            "我肩负着自己的使命，必须要把目睹\x01",
            "到的事件真相传达给各位市民！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D28")

    TalkEnd(0xFE)
    Return()

    # Function_6_A4D end

    def Function_7_D2C(): pass

    label("Function_7_D2C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D3D")
    Jump("loc_E78")

    label("loc_D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_E78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DFF")
    OP_4B(0x9, 0x0)

    #C0027
    ChrTalk(
        0x9,
        (
            "#02102F雷因兹，要看你的了！\x02\x03",

            "#02109F继续保持你刚才展现出来的过人胆量，\x01",
            "紧紧跟在我身后吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "我、我都说了，刚才那只是\x01",
            "身体下意识地动了起来而已……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xFE, 0x10)
    OP_4C(0x9, 0x0)
    Jump("loc_E78")

    label("loc_DFF")


    #C0029
    ChrTalk(
        0xFE,
        (
            "呼，但也没办法了。\x01",
            "既然身为前辈的搭档，\x01",
            "就不可能回避这些危险……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "事到如今，也只能拼命努力，\x01",
            "争取多拍些照片了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E78")

    TalkEnd(0xFE)
    Return()

    # Function_7_D2C end

    def Function_8_E7C(): pass

    label("Function_8_E7C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E8D")
    Jump("loc_EE9")

    label("loc_E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_EE9")

    #C0031
    ChrTalk(
        0xFE,
        (
            "通讯器没有在事故中被毁，\x01",
            "真是不幸中的大幸。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "必须要赶快叫人来救我们……！\x02",
    )

    CloseMessageWindow()

    label("loc_EE9")

    TalkEnd(0xFE)
    Return()

    # Function_8_E7C end

    def Function_9_EED(): pass

    label("Function_9_EED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_EFE")
    Jump("loc_F70")

    label("loc_EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_F70")

    #C0033
    ChrTalk(
        0xFE,
        (
            "我只是正巧到这里检修通讯器而已，\x01",
            "没想到却遇到了这种可怕的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        "唉，为什么我总是这么倒霉啊。\x02",
    )

    CloseMessageWindow()

    label("loc_F70")

    TalkEnd(0xFE)
    Return()

    # Function_9_EED end

    def Function_10_F74(): pass

    label("Function_10_F74")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 1470, 0, -5130, 0)
    SetChrPos(0x1, 1470, 0, -5130, 0)
    SetChrPos(0x2, 1470, 0, -5130, 0)
    SetChrPos(0x3, 1470, 0, -5130, 0)
    SetChrPos(0x4, 1470, 0, -5130, 0)
    SetChrPos(0x5, 1470, 0, -5130, 0)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 8180, 0, 4000, 225)
    OP_68(1600, 1500, -3250, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(23000, 0)
    OP_68(1800, 1500, -1130, 4000)
    FadeToBright(1000, 0)
    BeginChrThread(0x101, 1, 0, 11)
    Sleep(500)
    BeginChrThread(0x102, 1, 0, 12)
    Sleep(500)
    BeginChrThread(0x104, 1, 0, 13)
    Sleep(500)
    BeginChrThread(0x103, 1, 0, 14)
    Sleep(500)
    BeginChrThread(0x109, 1, 0, 15)
    Sleep(500)
    BeginChrThread(0x105, 1, 0, 16)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    #C0035
    ChrTalk(
        0x101,
        "#00013F#5P这里也太安静了吧……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        (
            "#00108F#11P格蕾丝小姐他们\x01",
            "是不是已经逃往别处了呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    OP_64(0x104)

    #C0037
    ChrTalk(
        0x103,
        (
            "#00201F#12P不，我在这栋建筑中\x01",
            "感知到了多个人类生命反应。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        "#00311F#6P可是，这种感觉是……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 10, -1, -1)
    SetChrName("女性的声音")

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1S各、各位……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(4180, 1500, -890, 2500)
    MoveCamera(36, 20, 0, 2500)

    def lambda_129E():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_129E)
    Sleep(50)

    def lambda_12AE():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_12AE)
    Sleep(50)

    def lambda_12BE():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_12BE)
    Sleep(50)

    def lambda_12CE():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_12CE)
    Sleep(50)

    def lambda_12DE():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_12DE)
    Sleep(50)

    def lambda_12EE():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_12EE)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    SetChrFlags(0x8, 0x40)
    Sleep(1500)
    OP_74(0x0, 0x3)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x8)
    Sound(103, 0, 100, 0)
    Sleep(400)
    OP_96(0x8, 0x1FF4, 0x0, 0x9C4, 0x2BC, 0x0)
    OP_79(0x0)

    #C0040
    ChrTalk(
        0x101,
        "#00005F#6P是接待处的……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        "#11P（嘘……请安静。）\x02",
    )

    CloseMessageWindow()
    OP_68(3440, 1500, -1740, 2500)
    MoveCamera(36, 16, 0, 2500)
    OP_6E(400, 2500)
    SetCameraDistance(20500, 2500)
    OP_74(0x0, 0x3)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x8)

    def lambda_13C3():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13C3)

    def lambda_13D0():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13D0)

    def lambda_13DD():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13DD)

    def lambda_13EA():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13EA)

    def lambda_13F7():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13F7)

    def lambda_1404():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1404)
    BeginChrThread(0x8, 1, 0, 17)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    Sleep(1000)
    Sleep(300)
    Sound(104, 0, 70, 0)
    BeginChrThread(0x101, 1, 0, 18)
    Sleep(50)
    BeginChrThread(0x104, 1, 0, 20)
    Sleep(50)
    BeginChrThread(0x105, 1, 0, 23)
    Sleep(50)
    BeginChrThread(0x102, 1, 0, 19)
    Sleep(60)
    BeginChrThread(0x103, 1, 0, 21)
    Sleep(60)
    BeginChrThread(0x109, 1, 0, 22)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    #C0042
    ChrTalk(
        0x109,
        "#10101F#6P（发、发生什么事了吗？）\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        "#11P（其、其实是这样的……）\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "#11P（就在刚刚，一群持有枪械的人\x01",
            "  突然闯进了这里。）\x02",
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

    #C0045
    ChrTalk(
        0x102,
        "#00105F#6P（什么……！？）\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x104,
        (
            "#00303F#6P（果然如此……）\x02\x03",

            "#00301F（就是正在外面肆虐的那些猎兵吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "#11P（因、因为事情太过突然，\x01",
            "  我也没有搞清具体情况……\x01",
            "  不过，多半没错吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "#11P（他们以枪相胁，\x01",
            "  很快就将社内所有人\x01",
            "  都抓起来了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "#11P（我躲在了办公桌后面，\x01",
            "  才勉强逃过这一劫……）\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x105,
        (
            "#10306F#6P（真是不幸中的大幸啊。）\x02\x03",

            "#10301F（然后呢，那些家伙现在去哪里了？）\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#11P（他们……好像留了两个人\x01",
            "  在楼上监视……）\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "#11P（现在外面这么混乱，\x01",
            "  实在是求救无门……\x01",
            "  到、到底该怎么办啊？）\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00013F#6P（……我大致了解情况了，\x01",
            "  总之，这里就交给我们\x01",
            "  来处理吧。）\x02\x03",

            "（我们一定会把格蕾丝小姐\x01",
            "  他们救出来的。）\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        "#11P（真的吗……真是太感谢你们了！）\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x102,
        (
            "#00103F#6P（既然决定要救人，最好在\x01",
            "  行动之前做好万全准备。）\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x103,
        (
            "#00201F#6P（对手可是职业猎兵，\x01",
            "  战前准备做得\x01",
            "  越全面越好。）\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "#11P（如果有什么事情需要我帮忙，\x01",
            "  请不要客气，尽管来找我吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "#11P（这里有急救箱，\x01",
            "  可以给各位做一些应急处理。）\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#00003F#6P（嗯，多谢啦。）\x02\x03",

            "#00007F（好……我们做好准备之后，\x01",
            "  就直接冲上二楼吧！）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x8, 3450, 20, -20, 270)
    BeginChrThread(0x8, 0, 0, 0)
    ClearChrFlags(0x8, 0x40)
    OP_74(0x0, 0x1E)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 1250, 0, -1520, 225)
    SetScenarioFlags(0x192, 1)
    OP_29(0xAB, 0x1, 0x1)
    ModifyEventFlags(1, 0, 0x80)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_10_F74 end

    def Function_11_1A16(): pass

    label("Function_11_1A16")


    def lambda_1A1B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1A1B)
    OP_95(0xFE, 1610, 0, -520, 2000, 0x0)
    Sleep(250)
    OP_93(0xFE, 0x13B, 0xFA)
    Sleep(250)
    OP_93(0xFE, 0x2D, 0xFA)
    Return()

    # Function_11_1A16 end

    def Function_12_1A50(): pass

    label("Function_12_1A50")


    def lambda_1A55():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1A55)
    OP_95(0xFE, 1000, 0, -2300, 2000, 0x0)
    OP_95(0xFE, 530, 0, -1340, 2000, 0x0)
    Sleep(250)
    OP_93(0xFE, 0x10E, 0x12C)
    Sleep(250)
    OP_93(0xFE, 0x13B, 0x12C)
    Return()

    # Function_12_1A50 end

    def Function_13_1A9E(): pass

    label("Function_13_1A9E")


    def lambda_1AA3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1AA3)
    OP_95(0xFE, 2000, 0, -2300, 2000, 0x0)
    OP_95(0xFE, 2470, 20, -1230, 2000, 0x0)
    Return()

    # Function_13_1A9E end

    def Function_14_1AD8(): pass

    label("Function_14_1AD8")


    def lambda_1ADD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1ADD)
    OP_95(0xFE, 1720, 0, -2230, 2000, 0x0)
    Return()

    # Function_14_1AD8 end

    def Function_15_1AFE(): pass

    label("Function_15_1AFE")


    def lambda_1B03():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1B03)
    OP_95(0xFE, 1000, 0, -3300, 2000, 0x0)
    OP_95(0xFE, 280, 0, -2730, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x12C)
    Return()

    # Function_15_1AFE end

    def Function_16_1B42(): pass

    label("Function_16_1B42")


    def lambda_1B47():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1B47)
    OP_95(0xFE, 1700, 0, -3300, 2000, 0x0)
    OP_95(0xFE, 2270, 0, -3040, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0xC8)
    Sleep(300)
    OP_93(0xFE, 0x2D, 0xC8)
    Return()

    # Function_16_1B42 end

    def Function_17_1B90(): pass

    label("Function_17_1B90")

    OP_95(0xFE, 7020, 0, 960, 2000, 0x0)
    OP_95(0xFE, 5640, 0, 320, 2000, 0x0)
    TurnDirection(0xFE, 0x109, 500)
    Return()

    # Function_17_1B90 end

    def Function_18_1BC0(): pass

    label("Function_18_1BC0")

    OP_95(0xFE, 2029, 0, 180, 2000, 0x0)
    OP_95(0xFE, 3010, 20, 160, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_18_1BC0 end

    def Function_19_1BF0(): pass

    label("Function_19_1BF0")

    OP_95(0xFE, 1750, 0, 230, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_19_1BF0 end

    def Function_20_1C0C(): pass

    label("Function_20_1C0C")

    OP_95(0xFE, 3250, 20, -880, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_20_1C0C end

    def Function_21_1C28(): pass

    label("Function_21_1C28")

    OP_95(0xFE, 2100, 20, -1790, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_21_1C28 end

    def Function_22_1C44(): pass

    label("Function_22_1C44")

    OP_95(0xFE, 2040, 0, -640, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_22_1C44 end

    def Function_23_1C60(): pass

    label("Function_23_1C60")

    OP_95(0xFE, 3080, 20, -2350, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_23_1C60 end

    def Function_24_1C7C(): pass

    label("Function_24_1C7C")

    EventBegin(0x0)
    Fade(500)
    OP_68(-6720, 1520, 2430, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(19500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -6560, 0, 3910, 0)
    SetChrPos(0x104, -5880, 20, 3120, 315)
    SetChrPos(0x102, -7120, 20, 2670, 0)
    SetChrPos(0x109, -5320, 0, 2130, 315)
    SetChrPos(0x103, -6570, 0, 1720, 0)
    SetChrPos(0x105, -5760, 0, 1130, 315)
    OP_0D()

    #C0060
    ChrTalk(
        0x101,
        (
            "#00001F#5P（格蕾丝小姐他们被\x01",
            "  猎兵们关押在楼上……）\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        "#00301F#11P（罗伊德，我们这就冲上去吗？）\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "冲上去\x01",            # 0
            "还没做好准备\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1DDE"),
        (SWITCH_DEFAULT, "loc_1EB1"),
    )


    label("loc_1DDE")


    #C0062
    ChrTalk(
        0x101,
        "#00007F#5P（嗯……各位，上吧！）\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x109,
        "#10107F（是，队长！）\x02",
    )

    CloseMessageWindow()
    OP_68(-7710, 2920, 3910, 1500)
    MoveCamera(45, 21, 0, 1500)
    OP_6E(380, 1500)
    SetCameraDistance(15500, 1500)
    FadeToDark(1000, 0, -1)
    BeginChrThread(0x101, 1, 0, 25)
    Sleep(50)
    BeginChrThread(0x104, 1, 0, 27)
    Sleep(60)
    BeginChrThread(0x102, 1, 0, 26)
    Sleep(50)
    BeginChrThread(0x109, 1, 0, 27)
    Sleep(60)
    BeginChrThread(0x103, 1, 0, 26)
    Sleep(50)
    BeginChrThread(0x105, 1, 0, 27)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x105, 0x1)
    NewScene("c122B", 104, 0, 0)
    IdleLoop()
    Jump("loc_1F76")

    label("loc_1EB1")


    #C0064
    ChrTalk(
        0x104,
        (
            "#00303F#11P（这样啊……）\x02\x03",

            "#00301F（如果救援得太晚，还不知\x01",
            "  那群猎兵会做出什么事来。\x01",
            "  抓紧时间，赶快做好准备吧！）\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#00001F#5P（好的……！）\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -6510, 20, 2640, 180)
    EventEnd(0x5)
    Jump("loc_1F76")

    label("loc_1F76")

    Return()

    # Function_24_1C7C end

    def Function_25_1F77(): pass

    label("Function_25_1F77")

    OP_95(0xFE, -6440, 3730, 7730, 4000, 0x0)
    Return()

    # Function_25_1F77 end

    def Function_26_1F8C(): pass

    label("Function_26_1F8C")

    OP_95(0xFE, -7000, 0, 4000, 4000, 0x0)
    OP_95(0xFE, -7000, 3730, 7730, 4000, 0x0)
    Return()

    # Function_26_1F8C end

    def Function_27_1FB5(): pass

    label("Function_27_1FB5")

    OP_95(0xFE, -5800, 0, 4000, 4000, 0x0)
    OP_95(0xFE, -5800, 3730, 7730, 4000, 0x0)
    Return()

    # Function_27_1FB5 end

    def Function_28_1FDE(): pass

    label("Function_28_1FDE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 30)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xE, 0x40)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xD, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrChipByIndex(0xD, 0x6)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrPos(0xE, 67690, 0, 12730, 225)
    SetChrPos(0xB, 67190, 0, 11890, 225)
    SetChrPos(0xD, 67780, 0, 11680, 180)
    SetChrPos(0xC, 66950, 0, 13050, 225)
    SetChrPos(0xA, 66550, 0, 12150, 270)
    SetChrPos(0x9, 66060, 0, 13000, 270)
    SetChrPos(0xF, 63430, 0, 12700, 90)
    SetChrPos(0x10, 67400, 0, 8550, 0)
    OP_68(61700, 1500, 7460, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(26000, 0)
    OP_70(0xB, 0x0)
    FadeToBright(2000, 0)
    OP_68(65910, 1500, 11380, 4000)
    MoveCamera(45, 20, 0, 4000)
    OP_6E(400, 0)
    SetCameraDistance(19500, 4000)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    #C0066
    ChrTalk(
        0x9,
        (
            "#02101F#11P……我说你们啊，\x01",
            "别再做这种傻事了！\x02\x03",

            "居然在市内发动袭击，\x01",
            "这到底有什么意义呢！？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xF,
        (
            "我们自有目的……\x01",
            "和你们毫无关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x10,
        (
            "放心吧，只要乖乖待着，\x01",
            "我们就不会加害你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x10,
        (
            "不过，如果你们不遵守这条要求……\x01",
            "那就只能强迫你们变乖了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    #C0070
    ChrTalk(
        0xE,
        "#5P呜、呜哇哇……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xD,
        (
            "#5P我、我只是来送个外卖而已，\x01",
            "为什么会遇到这种事啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0072
    ChrTalk(
        0x9,
        (
            "#02104F#11P哼，你们好大的胆子……！\x02\x03",

            "#02102F如果以为这种小小的\x01",
            "威胁就能吓住我，\x01",
            "那可就大错特错了！\x02\x03",

            "要是你们有胆子，\x01",
            "就尽管试试看吧！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x9, 500)
    Sleep(100)

    #C0073
    ChrTalk(
        0xC,
        (
            "#11P格蕾丝，你不要一直\x01",
            "刺激他们……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_96(0xA, 0x10158, 0x0, 0x307A, 0x5DC, 0x0)

    #C0074
    ChrTalk(
        0xA,
        (
            "#11P请、请等一下！\x01",
            "前辈，你就忍忍吧……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0075
    ChrTalk(
        0xA,
        (
            "#11P#4S你、你们两个听好了！\x01",
            "如果敢动她，我绝对不会善罢甘休！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2461():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2461)

    def lambda_246E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_246E)
    Sleep(50)

    def lambda_247E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_247E)

    def lambda_248B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_248B)
    Sleep(50)

    def lambda_249B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_249B)

    def lambda_24A8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_24A8)

    #C0076
    ChrTalk(
        0x9,
        "#02105F#5P雷、雷因兹……！？\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xF,
        (
            "哼，这两个记者倒是挺有胆量嘛……\x01",
            "不过，我可不会受你们的挑衅。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x10,
        (
            "在作战结束之前，\x01",
            "你们就老实点吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xB,
        "#11P作战……你们到底想干什么？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, 54080, 0, 12770, 90)
    SetChrPos(0x104, 53960, 0, 11780, 90)
    SetChrPos(0x102, 52770, 0, 12870, 90)
    SetChrPos(0x103, 52610, 0, 11860, 90)
    SetChrPos(0x109, 51500, 0, 12880, 90)
    SetChrPos(0x105, 51610, 0, 11990, 90)
    SetChrChipByIndex(0x101, 0x21)
    SetChrChipByIndex(0x104, 0x27)
    SetChrChipByIndex(0x102, 0x23)
    SetChrChipByIndex(0x103, 0x25)
    SetChrChipByIndex(0x109, 0x29)
    SetChrChipByIndex(0x105, 0x2B)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(0, 200, -1, -1)
    SetChrName("罗伊德的声音")
    Sound(2090, 255, 100, 0)    #voice#Lloyd

    #A0080
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#4S到此为止了！！#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_2705():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2705)

    def lambda_2712():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2712)
    Sleep(50)

    def lambda_2722():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2722)

    def lambda_272F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_272F)
    OP_68(61890, 1500, 11620, 1800)
    MoveCamera(45, 13, 0, 1800)
    OP_6E(460, 1800)
    SetCameraDistance(19500, 1800)

    def lambda_276A():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_276A)
    Sleep(50)

    def lambda_2782():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2782)
    Sleep(50)

    def lambda_279A():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_279A)
    Sleep(50)

    def lambda_27B2():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_27B2)
    Sleep(50)

    def lambda_27CA():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_27CA)
    Sleep(50)

    def lambda_27E2():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_27E2)
    Sleep(600)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    #C0081
    ChrTalk(
        0xF,
        "#11P你们是……！\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        "#02105F#11P罗伊德！是你们！？\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x10,
        "#5P兰道夫队长！？\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x109,
        "#10107F#5P开始武力压制！！\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        "#00307F#5P好！我们上吧！！\x02",
    )

    CloseMessageWindow()

    def lambda_28B0():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28B0)

    def lambda_28C5():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_28C5)

    def lambda_28DA():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_28DA)

    def lambda_28EF():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_28EF)

    def lambda_2904():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2904)

    def lambda_2919():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2919)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    OP_68(61890, 1500, 11620, 250)
    MoveCamera(45, 15, 0, 250)
    OP_6E(460, 250)
    SetCameraDistance(15300, 250)
    Sleep(250)
    CancelBlur(200)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrChipByIndex(0x101, 0x21)
    SetChrChipByIndex(0x104, 0x27)
    SetChrChipByIndex(0x102, 0x23)
    SetChrChipByIndex(0x103, 0x25)
    SetChrChipByIndex(0x109, 0x29)
    SetChrChipByIndex(0x105, 0x2B)
    Battle("BattleInfo_328", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 29)
    Return()

    # Function_28_1FDE end

    def Function_29_29B9(): pass

    label("Function_29_29B9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 30)
    SetChrChipByIndex(0xF, 0x20)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0xF, 0x3)
    SetChrSubChip(0x10, 0x3)
    SetChrPos(0xF, 63550, 0, 12500, 270)
    SetChrPos(0x10, 64680, 0, 11840, 270)
    SetChrPos(0x101, 61080, 0, 12770, 90)
    SetChrPos(0x104, 60960, 0, 11780, 90)
    SetChrPos(0x102, 59770, 0, 12870, 90)
    SetChrPos(0x103, 59610, 0, 11860, 90)
    SetChrPos(0x109, 58500, 0, 12880, 90)
    SetChrPos(0x105, 58610, 0, 11990, 90)
    SetChrChipByIndex(0x101, 0x21)
    SetChrChipByIndex(0x104, 0x27)
    SetChrChipByIndex(0x102, 0x23)
    SetChrChipByIndex(0x103, 0x25)
    SetChrChipByIndex(0x109, 0x29)
    SetChrChipByIndex(0x105, 0x2B)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0xE, 67690, 0, 12730, 270)
    SetChrPos(0xB, 67190, 0, 11890, 270)
    SetChrPos(0xD, 67780, 0, 11680, 270)
    SetChrPos(0xC, 66950, 0, 13050, 270)
    SetChrPos(0xA, 66300, 0, 12150, 270)
    SetChrPos(0x9, 66060, 0, 13000, 270)
    LoadEffect(0x0, "event\\ev307_00.eff")
    OP_68(62190, 1500, 11630, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(16800, 0)
    FadeToBright(2000, 0)
    SetCameraDistance(16000, 2000)
    OP_0D()
    OP_6F(0x79)

    #C0086
    ChrTalk(
        0xF,
        "#5P唔……！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x10,
        "#11P看来也只能撤退了。\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#00011F#6P什么……！？\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x10, 1, 0, 31)
    Sleep(200)
    BeginChrThread(0xF, 1, 0, 31)
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
    Sleep(300)
    OP_68(65200, 1500, 11630, 2000)
    SetCameraDistance(16300, 2000)
    OP_6F(0x79)
    WaitChrThread(0xF, 1)
    WaitChrThread(0xF, 2)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x10, 2)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xD, 1)
    Sleep(1000)
    OP_68(62930, 1500, 11660, 2000)
    SetCameraDistance(17630, 2000)
    OP_6F(0x79)

    #C0089
    ChrTalk(
        0x104,
        "#00310F#5P啧……逃跑了啊。\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x105,
        (
            "#10306F#5P本来还有很多事情\x01",
            "想问问他们呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    OP_0D()
    OP_68(63150, 1600, 11590, 2000)
    MoveCamera(45, 17, 0, 2000)
    OP_6E(400, 2000)
    SetCameraDistance(17430, 2000)

    def lambda_2D4F():
        OP_9B(0x0, 0xFE, 0x0, 0x6A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D4F)
    Sleep(50)

    def lambda_2D67():
        OP_9B(0x0, 0xFE, 0x0, 0x6A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2D67)
    Sleep(50)

    def lambda_2D7F():
        OP_9B(0x0, 0xFE, 0x0, 0x73A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D7F)
    Sleep(50)

    def lambda_2D97():
        OP_9B(0x0, 0xFE, 0x0, 0x73A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D97)
    Sleep(50)

    def lambda_2DAF():
        OP_9B(0x0, 0xFE, 0x0, 0x73A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2DAF)
    Sleep(50)

    def lambda_2DC7():
        OP_9B(0x0, 0xFE, 0x0, 0x73A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2DC7)
    Sleep(50)

    def lambda_2DDF():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2DDF)
    Sleep(50)

    def lambda_2DF7():
        OP_9B(0x0, 0xFE, 0xFFFB, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2DF7)
    Sleep(50)

    def lambda_2E0F():
        OP_9B(0x0, 0xFE, 0x0, 0x578, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2E0F)
    Sleep(50)

    def lambda_2E27():
        OP_9B(0x0, 0xFE, 0xFFFB, 0x578, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2E27)
    Sleep(50)

    def lambda_2E3F():
        OP_9B(0x0, 0xFE, 0x0, 0x514, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2E3F)
    Sleep(50)

    def lambda_2E57():
        OP_9B(0x0, 0xFE, 0xFFFB, 0x514, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2E57)
    Sleep(50)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xD, 1)

    #C0091
    ChrTalk(
        0x9,
        "#02110F#11P罗伊德，你们没事吧！？\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#00000F#6P格蕾丝小姐，你们呢……？\x01",
            "大家都没受伤吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xB,
        (
            "#11P嗯，托你们的福，\x01",
            "所有人都毫发无伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xC,
        "#11P真是千钧一发啊。\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xC,
        (
            "#11P哎呀呀，格蕾丝，\x01",
            "你未免也太乱来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xE,
        "#11P老实说，刚才真是把我吓出了一身冷汗呢……\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        (
            "#02109F#11P啊哈哈，不由自主地\x01",
            "热血上涌呢。\x02\x03",

            "#02104F身为专业的新闻工作者，\x01",
            "总不能屈服于暴力威胁\x01",
            "之下啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)
    Sleep(100)

    #C0098
    ChrTalk(
        0x9,
        (
            "#02110F……话说回来，\x01",
            "真要对雷因兹刮目相看了！\x02\x03",

            "#02109F真没想到你会在\x01",
            "那种情况下挺身保护我！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 500)

    #C0099
    ChrTalk(
        0xA,
        (
            "#12P啊、啊哈哈，\x01",
            "该怎么说呢，只是一时冲动，\x01",
            "身体就下意识地动起来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xD,
        (
            "#11P哎呀呀……\x01",
            "真是让人敬佩的青年啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x102,
        (
            "#00104F#5P呵呵，不管怎么说，\x01",
            "大家平安无事就再好不过。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x109,
        (
            "#10108F#5P不过……\x01",
            "那些猎兵为何会\x01",
            "盯上通讯社呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x103,
        (
            "#00206F#5P这个问题确实让人在意啊。\x02\x03",

            "#00208F毁掉『黑月』还能理解，\x01",
            "但对他们来说，通讯社应该\x01",
            "并不是什么重要地点啊……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_31E8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_31E8)
    Sleep(50)

    def lambda_31F8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_31F8)
    WaitChrThread(0x9, 1)

    #C0104
    ChrTalk(
        0x9,
        (
            "#02106F#11P啊！多半是为了那个。\x02\x03",

            "#02101F他们的目标大概就是那边的\x01",
            "国际通讯器吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(67640, 1600, -250, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(20820, 0)
    OP_0D()
    Sleep(300)
    SetMessageWindowPos(30, 200, -1, -1)

    #A0105
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013F国际通讯器……就是可以直接\x01",
            "向外国发送导力波的通讯器吗？\x02\x03",

            "#00008F也就是说，这是为了防止共和国\x01",
            "等势力介入……？\x02",
        )
    )

    CloseMessageWindow()

    #A0106
    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10303F唔，确实有\x01",
            "可能呢。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 0, -1, -1)

    #A0107
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02101F嗯，多半没错。\x02\x03",

            "那些家伙闯入港湾区之后，\x01",
            "第一时间就攻向了这里。\x02\x03",

            "#02106F因为来得太过突然，\x01",
            "导致我们措手不及。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(63150, 1600, 11590, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(17430, 0)
    OP_0D()
    Sleep(300)

    #C0108
    ChrTalk(
        0x104,
        (
            "#00303F#6P既然如此……\x01",
            "我们还是尽快出发为好。\x02\x03",

            "#00301F他们已经摧毁了『黑月』，\x01",
            "现在又跑到了ＩＢＣ，\x01",
            "不知有何企图……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#00006F#5P是啊……计划制定得如此周全，\x01",
            "他们的目的恐怕并非金钱这么简单。\x02\x03",

            "#00013F请各位暂时留在室内，\x01",
            "在事态平息下来之前，\x01",
            "一定不要外出。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xC,
        "#11P好、好的……我们会照做的。\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xA,
        "#11P你们打算追上去吗？\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        (
            "#02103F#11P千万要多加小心哦！\x02\x03",

            "#02101F如果你们能将这起事件顺利解决，\x01",
            "我一定会给你们在头版登出专题报道的！\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x102,
        (
            "#00109F#6P啊哈哈……\x01",
            "有这份心意就足够了。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#00007F#5P好，我们这就出发吧！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19820, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_49()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
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
    OP_D7(0x28)
    OP_D7(0x29)
    OP_D7(0x2A)
    OP_D7(0x2B)
    OP_D7(0x2C)
    SetScenarioFlags(0x192, 2)
    OP_2C(0xAB, 0x2)
    OP_29(0xAB, 0x1, 0x2)
    NewScene("c122B", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_29_29B9 end

    def Function_30_3671(): pass

    label("Function_30_3671")

    LoadChrToIndex("chr/ch41950.itc", 0x1E)
    LoadChrToIndex("chr/ch41951.itc", 0x1F)
    LoadChrToIndex("chr/ch41953.itc", 0x20)
    LoadChrToIndex("chr/ch00050.itc", 0x21)
    LoadChrToIndex("chr/ch00051.itc", 0x22)
    LoadChrToIndex("chr/ch00150.itc", 0x23)
    LoadChrToIndex("chr/ch00151.itc", 0x24)
    LoadChrToIndex("chr/ch00250.itc", 0x25)
    LoadChrToIndex("chr/ch00251.itc", 0x26)
    LoadChrToIndex("chr/ch00350.itc", 0x27)
    LoadChrToIndex("chr/ch00351.itc", 0x28)
    LoadChrToIndex("chr/ch02950.itc", 0x29)
    LoadChrToIndex("chr/ch02951.itc", 0x2A)
    LoadChrToIndex("chr/ch03050.itc", 0x2B)
    LoadChrToIndex("chr/ch03051.itc", 0x2C)
    Return()

    # Function_30_3671 end

    def Function_31_36CC(): pass

    label("Function_31_36CC")

    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, 66500, 0, 11400, 5000, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_372F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 32)

    label("loc_372F")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x2)
    SetChrChip(0x0, 0xFE, 0x32, 0xC8)
    Sound(534, 0, 80, 0)
    OP_9C(0xFE, 0x1388, 0x0, 0x0, 0x514, 0xBB8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_31_36CC end

    def Function_32_3774(): pass

    label("Function_32_3774")

    Sleep(150)
    OP_74(0xB, 0xF)
    OP_71(0xB, 0x0, 0xB, 0x0, 0x8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 70000, 0, 12500, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(991, 0, 100, 0)
    Return()

    # Function_32_3774 end

    SaveToFile()

Try(main)
