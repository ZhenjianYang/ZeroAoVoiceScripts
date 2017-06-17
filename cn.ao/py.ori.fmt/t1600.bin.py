from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1600.bin",                # FileName
        "t1600",                    # MapName
        "t1600",                    # Location
        0x004D,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 77, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1600",                  # 0
        "巴乔",                   # 1
        "滴",                     # 2
        "赛兰德教授",             # 3
        "勤杂工戴森",             # 4
        "希伦护士",               # 5
        "梅菲尔护士",             # 6
        "亚里欧斯",               # 7
        "赛尔盖",                 # 8
        "乌尔斯拉间道",           # 9
    ))

    AddCharChip((
        "chr/ch20400.itc",                   # 00
        "chr/ch05400.itc",                   # 01
        "chr/ch44800.itc",                   # 02
        "chr/ch20200.itc",                   # 03
        "chr/ch29900.itc",                   # 04
        "chr/ch29800.itc",                   # 05
        "chr/ch05300.itc",                   # 06
    ))

    DeclNpc(-21979,  6000,    18520,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-3589,   7000,    11229,   225,  389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4039,    7000,    2160,    270,  389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(3430,    7000,    -9159,   180,  389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-26559,  6000,    14199,   0,    389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-26559,  6000,    14199,   0,    389,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 29,  -13.5,                 20.0,                  5.5,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   6.75,                  -10.0,                 -1.100000023841858,    1.0])

    DeclActor(17500,   7000,    -3000,   2000,    18000,   8000,    -3000,   0x007C, 0,  22, 0x0000)

    PlaceName(-69.0, 0.0, -8.0, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(-23.0, 0.0, 18.0, 0x0000, 0x0052, "")
    PlaceName(-57.900001525878906, 0.0, 4.199999809265137, 0x0000, 0x0055, "")

    ChipFrameInfo(712, 0)                                        # 0

    ScpFunction((
        "Function_0_2C8",          # 00, 0
        "Function_1_380",          # 01, 1
        "Function_2_512",          # 02, 2
        "Function_3_5DE",          # 03, 3
        "Function_4_698",          # 04, 4
        "Function_5_8FF",          # 05, 5
        "Function_6_BF2",          # 06, 6
        "Function_7_F12",          # 07, 7
        "Function_8_1461",         # 08, 8
        "Function_9_15EB",         # 09, 9
        "Function_10_16FF",        # 0A, 10
        "Function_11_1988",        # 0B, 11
        "Function_12_1F40",        # 0C, 12
        "Function_13_2837",        # 0D, 13
        "Function_14_285D",        # 0E, 14
        "Function_15_2883",        # 0F, 15
        "Function_16_28A9",        # 10, 16
        "Function_17_28CF",        # 11, 17
        "Function_18_28F5",        # 12, 18
        "Function_19_291B",        # 13, 19
        "Function_20_2941",        # 14, 20
        "Function_21_2967",        # 15, 21
        "Function_22_298D",        # 16, 22
        "Function_23_2ADF",        # 17, 23
        "Function_24_2EF8",        # 18, 24
        "Function_25_2F43",        # 19, 25
        "Function_26_2F8E",        # 1A, 26
        "Function_27_2FD9",        # 1B, 27
        "Function_28_3024",        # 1C, 28
        "Function_29_306F",        # 1D, 29
    ))


    def Function_0_2C8(): pass

    label("Function_0_2C8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_308"),
        (1, "loc_314"),
        (2, "loc_320"),
        (3, "loc_32C"),
        (4, "loc_338"),
        (5, "loc_344"),
        (6, "loc_350"),
        (SWITCH_DEFAULT, "loc_35C"),
    )


    label("loc_308")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_314")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_320")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_32C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_338")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_344")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_350")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_35C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_368")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_37F")

    Return()

    # Function_0_2C8 end

    def Function_1_380(): pass

    label("Function_1_380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3A4")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 8450, 7000, -13870, 135)
    Jump("loc_4EE")

    label("loc_3A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3C8")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 13730, 7000, -3100, 90)
    Jump("loc_4EE")

    label("loc_3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_411")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -26060, 6000, 14200, 0)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -27060, 6000, 14200, 0)
    SetChrFlags(0xD, 0x10)
    Jump("loc_4EE")

    label("loc_411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_424")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4EE")

    label("loc_424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_446")
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_441")
    SetChrFlags(0x9, 0x10)

    label("loc_441")

    Jump("loc_4EE")

    label("loc_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_454")
    Jump("loc_4EE")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_46C")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_4EE")

    label("loc_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_47F")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4EE")

    label("loc_47F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4CD")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -22110, 6000, 16760, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -20450, 6000, 17030, 315)
    SetChrFlags(0xD, 0x10)
    Jump("loc_4EE")

    label("loc_4CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4E0")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4EE")

    label("loc_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4EE")
    ClearChrFlags(0xB, 0x80)

    label("loc_4EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_502")
    ClearScenarioFlags(0x22, 0)
    Event(0, 23)
    Jump("loc_511")

    label("loc_502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_511")
    ClearScenarioFlags(0x22, 1)
    Event(0, 12)

    label("loc_511")

    Return()

    # Function_1_380 end

    def Function_2_512(): pass

    label("Function_2_512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_524")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A8")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x6E, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_5BF")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_5BF")

    label("loc_5BF")

    ClearMapObjFlags(0x5, 0x10)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DD")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5DD")

    Return()

    # Function_2_512 end

    def Function_3_5DE(): pass

    label("Function_3_5DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_694")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FC")
    Call(0, 8)
    Jump("loc_694")

    label("loc_5FC")


    #C0001
    ChrTalk(
        0x8,
        (
            "做个护士，\x01",
            "说不定也不错啊，\x01",
            "应该也会有男护士吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "虽然知道姐姐不可靠，\x01",
            "但还是来这里找姐姐谈心了，\x01",
            "没想到竟突然觉得未来的道路一下变得光明了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_694")

    TalkEnd(0xFE)
    Return()

    # Function_3_5DE end

    def Function_4_698(): pass

    label("Function_4_698")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AD")
    Call(0, 11)
    Jump("loc_8FB")

    label("loc_6AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A7")
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0003
    ChrTalk(
        0x9,
        (
            "#11200F对了，各位。\x02\x03",

            "琪雅三天前\x01",
            "来过医院……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#00005F哦……说起来，\x01",
            "当时好像是来\x01",
            "探望你的吧？\x02\x03",

            "#00000F那个……\x01",
            "琪雅怎么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x9,
        (
            "#11208F没什么……\x01",
            "只是觉得她的\x01",
            "样子有点奇怪。\x02\x03",

            "#11203F似乎有什么烦恼……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x103,
        "#00205F琪雅她……？\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#00303F在我们面前，\x01",
            "她从来没有显露过\x01",
            "那种样子呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x109,
        (
            "#10108F……琪雅大概\x01",
            "也对克洛斯贝尔的状况\x01",
            "感到不安吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        (
            "#00103F是啊……\x01",
            "也许是为了不让我们担心，\x01",
            "她刻意隐藏了自己的心情。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x105,
        (
            "#10302F不管怎么说，\x01",
            "还是留意一下为好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18E, 6)
    Jump("loc_8FB")

    label("loc_8A7")


    #C0011
    ChrTalk(
        0x9,
        (
            "#11200F我想大家现在一定都很辛苦，\x01",
            "请继续加油吧。\x02\x03",

            "我也会在这里为你们鼓劲的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FB")

    TalkEnd(0xFE)
    Return()

    # Function_4_698 end

    def Function_5_8FF(): pass

    label("Function_5_8FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_910")
    Jump("loc_BEE")

    label("loc_910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_AA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0F")

    #C0012
    ChrTalk(
        0xA,
        (
            "所有内科医师和实习医生\x01",
            "都在思索如何应对\x01",
            "药品种类不足的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xA,
        (
            "虽说目前的条件并不完善，\x01",
            "但在任何时期都要尽最大努力，\x01",
            "这是身为医生的义务。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xA,
        (
            "我在此向女神发誓，\x01",
            "赌上自己药物学·神经科教授\x01",
            "的荣耀与威信，一定要想出对策。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_AA3")

    label("loc_A0F")


    #C0015
    ChrTalk(
        0xA,
        (
            "所有内科医师和实习医生\x01",
            "都在思索如何应对\x01",
            "药品种类不足的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xA,
        (
            "我在此向女神发誓，\x01",
            "赌上自己药物学·神经科教授\x01",
            "的荣耀与威信，一定要想出对策。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA3")

    Jump("loc_BEE")

    label("loc_AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_AB6")
    Jump("loc_BEE")

    label("loc_AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_AC4")
    Jump("loc_BEE")

    label("loc_AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B73")

    #C0017
    ChrTalk(
        0xA,
        (
            "……让小滴恢复\x01",
            "视力的可能性\x01",
            "恐怕相当低。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xA,
        (
            "……但是，只要患者还在坚持，\x01",
            "我就绝不会放弃。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xA,
        (
            "赌上赛兰德之名……\x01",
            "终有一天我要亲手把她治好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_BEE")

    label("loc_B73")


    #C0020
    ChrTalk(
        0xA,
        (
            "如果滴的视力恢复手术\x01",
            "顺利成功，一定能为情况\x01",
            "类似的患者们带来希望。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xA,
        (
            "赌上赛兰德之名……\x01",
            "终有一天我要亲手把她治好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BEE")

    TalkEnd(0xFE)
    Return()

    # Function_5_8FF end

    def Function_6_BF2(): pass

    label("Function_6_BF2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C59")

    #C0022
    ChrTalk(
        0xB,
        (
            "那棵巨大的树好惊人啊……\x01",
            "站在这里都能看到。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xB,
        (
            "……克洛斯贝尔\x01",
            "究竟会怎么样呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0E")

    label("loc_C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_C67")
    Jump("loc_F0E")

    label("loc_C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_DC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D46")

    #C0024
    ChrTalk(
        0xB,
        (
            "最近在研究楼中举行讲义时，\x01",
            "基本已经没办法做实验了。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xB,
        (
            "这主要是受到\x01",
            "不能去郊外采集标本，\x01",
            "也不能从雷米菲利亚订购医疗物资的影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xB,
        (
            "如果再这样下去，实习医生们的\x01",
            "学习环境恐怕会越来越恶劣。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_DBC")

    label("loc_D46")


    #C0027
    ChrTalk(
        0xB,
        (
            "最近在研究楼中举行讲义时，\x01",
            "基本已经没办法做实验了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xB,
        (
            "如果再这样下去，实习医生们的\x01",
            "学习环境恐怕会越来越恶劣。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DBC")

    Jump("loc_F0E")

    label("loc_DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_DCF")
    Jump("loc_F0E")

    label("loc_DCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9A")

    #C0029
    ChrTalk(
        0xB,
        (
            "由于我在这里工作，\x01",
            "在午餐时间总能听到实习医生们\x01",
            "讨论一些传闻……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xB,
        (
            "最近这段时间，他们聊的\x01",
            "几乎都是有关赛兰德教授。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xB,
        (
            "我是无缘和教授接触……\x01",
            "她究竟是个什么样的人呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_F0E")

    label("loc_E9A")


    #C0032
    ChrTalk(
        0xB,
        (
            "最近这段时间，实习医生们\x01",
            "总是谈论有关赛兰德教授的传闻呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xB,
        (
            "我是无缘和教授接触……\x01",
            "她究竟是个什么样的人呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F0E")

    TalkEnd(0xFE)
    Return()

    # Function_6_BF2 end

    def Function_7_F12(): pass

    label("Function_7_F12")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F23")
    Jump("loc_145D")

    label("loc_F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_F31")
    Jump("loc_145D")

    label("loc_F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_F76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4C")
    Call(0, 9)
    Jump("loc_F71")

    label("loc_F4C")


    #C0034
    ChrTalk(
        0xC,
        (
            "嘿嘿嘿，梅菲尔小姐\x01",
            "果然可靠啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F71")

    Jump("loc_145D")

    label("loc_F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_110B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_108A")

    #C0035
    ChrTalk(
        0xC,
        (
            "今天的晾床单方法\x01",
            "是我昨天想出来的\x01",
            "必杀技『叠放晾置法』。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xC,
        (
            "只要把床单两张两张地\x01",
            "叠挂在一起，\x01",
            "就可以同时晾干两倍的床单啦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xC,
        (
            "这样一来，就可以把\x01",
            "今天休假的梅菲尔小姐\x01",
            "的那份工作也轻松完成啦！！\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xC,
        (
            "……哎哎，可是……\x01",
            "好像根本没干啊……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1106")

    label("loc_108A")


    #C0039
    ChrTalk(
        0xC,
        (
            "呜呜，原来我的\x01",
            "必杀技『叠放晾置法』\x01",
            "不能把床单晾干……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xC,
        (
            "梅菲尔小姐今天休息，\x01",
            "我本来还想努力完成\x01",
            "两人份的工作呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1106")

    Jump("loc_145D")

    label("loc_110B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1119")
    Jump("loc_145D")

    label("loc_1119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1127")
    Jump("loc_145D")

    label("loc_1127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1135")
    Jump("loc_145D")

    label("loc_1135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1282")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1202")

    #C0041
    ChrTalk(
        0xC,
        (
            "不久前，米海尔出院时，\x01",
            "我把自己的手帕递给了\x01",
            "哭泣的梅菲尔小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xC,
        (
            "她接过之后，突然止住了泪水，\x01",
            "然后目不转睛地瞪着我。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xC,
        (
            "唔～到底是怎么回事呢？\x01",
            "之后她也没把手帕还我……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_127D")

    label("loc_1202")


    #C0044
    ChrTalk(
        0xC,
        (
            "梅菲尔小姐拿走了我的手帕，\x01",
            "到底想干什么呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xC,
        (
            "那手帕是我之前在宿舍里捡到的，\x01",
            "手感很好，款式也很漂亮，\x01",
            "我很喜欢呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_127D")

    Jump("loc_145D")

    label("loc_1282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1353")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129D")
    Call(0, 8)
    Jump("loc_134E")

    label("loc_129D")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0046
    ChrTalk(
        0xC,
        (
            "啊，对了！\x01",
            "干脆先试试护士服吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    #C0047
    ChrTalk(
        0xC,
        (
            "来，梅菲尔小姐，\x01",
            "脱下来借我用用吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xD,
        "才、才不借呢！\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "（唔、唔……\x01",
            "  她还是老样子呢……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x8, 0)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0x8, 0xFF)

    label("loc_134E")

    Jump("loc_145D")

    label("loc_1353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1454")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F8")

    #C0050
    ChrTalk(
        0xC,
        (
            "呵呵，今天的天气真好，\x01",
            "床单应该很快就能晾干呢¤\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xC,
        (
            "……呼～这温暖\x01",
            "的天气……\x01",
            "让人很想睡啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xC,
        (
            "再借用一张床单，\x01",
            "稍微睡一会好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_144F")

    label("loc_13F8")


    #C0053
    ChrTalk(
        0xC,
        (
            "在这里晒太阳\x01",
            "很舒服呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xC,
        (
            "我觉得梅菲尔小姐\x01",
            "今天应该不会来……\x01",
            "嗯，小睡一会吧☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_144F")

    Jump("loc_145D")

    label("loc_1454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_145D")

    label("loc_145D")

    TalkEnd(0xFE)
    Return()

    # Function_7_F12 end

    def Function_8_1461(): pass

    label("Function_8_1461")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0055
    ChrTalk(
        0x8,
        (
            "我在实习医生的选拔考试中落榜了……\x01",
            "在家里都觉得好丢脸。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "希伦姐姐，\x01",
            "我今后到底该怎么办呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xD,
        (
            "（巴乔……\x01",
            "  竟然来找希伦谈心，\x01",
            "  应该是相当苦恼吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xC,
        "嗯，这个嘛……\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xC,
        (
            "那就像姐姐一样，\x01",
            "当个护士如何呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_64(0xD)

    #C0060
    ChrTalk(
        0xD,
        (
            "希、希伦竟然能说出\x01",
            "这么像样的意见啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "原来如此，男护士吗……\x01",
            "以前倒是从没想过呢！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 6)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_8_1461 end

    def Function_9_15EB(): pass

    label("Function_9_15EB")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0062
    ChrTalk(
        0xD,
        (
            "希伦，你可真是……\x01",
            "竟然把床单叠在一起晾晒，\x01",
            "这不是更不容易晾干了吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xD,
        (
            "真是的，\x01",
            "你做这份工作\x01",
            "都多少年了！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xC,
        (
            "嗯……我是和梅菲尔小姐一起\x01",
            "入职的，一年、两年……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xD,
        (
            "唉！这种无关紧要的问题\x01",
            "不用那么认真回答啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xD,
        "好了！赶快重新晾床单！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_9_15EB end

    def Function_10_16FF(): pass

    label("Function_10_16FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1710")
    Jump("loc_1984")

    label("loc_1710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_171E")
    Jump("loc_1984")

    label("loc_171E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_179D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1739")
    Call(0, 9)
    Jump("loc_1798")

    label("loc_1739")


    #C0067
    ChrTalk(
        0xD,
        (
            "希伦可真是的……\x01",
            "连个床单都不能\x01",
            "一个人晾好。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xD,
        (
            "如果我不照看着她，\x01",
            "她什么都做不好呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1798")

    Jump("loc_1984")

    label("loc_179D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_17AB")
    Jump("loc_1984")

    label("loc_17AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_17B9")
    Jump("loc_1984")

    label("loc_17B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_17C7")
    Jump("loc_1984")

    label("loc_17C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_18F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1884")

    #C0069
    ChrTalk(
        0xD,
        (
            "不知希伦今天做了什么，\x01",
            "把护士长给惹火了。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xD,
        (
            "她平时总是犯错误，\x01",
            "偶尔训斥她一下\x01",
            "也是很有必要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xD,
        (
            "……算啦，等到差不多的时候，\x01",
            "我就去帮她说几句好话吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_18F0")

    label("loc_1884")


    #C0072
    ChrTalk(
        0xD,
        (
            "不知希伦今天做了什么，\x01",
            "把护士长给惹火了。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xD,
        (
            "算啦，我稍后去帮她说几句好话吧。\x01",
            "……我总是在纵容她呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18F0")

    Jump("loc_1984")

    label("loc_18F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1903")
    Jump("loc_1984")

    label("loc_1903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_196D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_191E")
    Call(0, 8)
    Jump("loc_1968")

    label("loc_191E")


    #C0074
    ChrTalk(
        0xD,
        (
            "希伦偶尔也会说出些\x01",
            "正经话啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xD,
        (
            "……明天会不会\x01",
            "从天上射下激光呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1968")

    Jump("loc_1984")

    label("loc_196D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_197B")
    Jump("loc_1984")

    label("loc_197B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1984")

    label("loc_1984")

    TalkEnd(0xFE)
    Return()

    # Function_10_16FF end

    def Function_11_1988(): pass

    label("Function_11_1988")

    EventBegin(0x0)
    Fade(500)
    OP_68(-3510, 8300, 11470, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x104, -1400, 7000, 11230, 270)
    SetChrPos(0x102, -1990, 7000, 12030, 225)
    SetChrPos(0x101, -2790, 7000, 12830, 225)
    SetChrPos(0x103, -3590, 7000, 13630, 180)
    SetChrPos(0x109, -2590, 7000, 14030, 180)
    SetChrPos(0x105, -3400, 7000, 14840, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    OP_0D()

    #C0076
    ChrTalk(
        0x101,
        (
            "#5P#00000F小滴，\x01",
            "你在这里啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 500)

    #C0077
    ChrTalk(
        0x9,
        (
            "#12P#11205F啊……\x01",
            "是支援科的各位？\x02\x03",

            "#11200F你们今天是来\x01",
            "探视的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x109,
        (
            "#5P#10108F嗯，芙兰受伤住院了，我们刚才探望了她。\x02\x03",

            "#10100F之后还探望了警察局的警督\x01",
            "和伊莉娅小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "#12P#11208F是吗……\x01",
            "我已经听塞茜尔小姐\x01",
            "说了芙兰小姐的事情……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    #C0080
    ChrTalk(
        0x9,
        (
            "#12P#11203F发生在市里的\x01",
            "袭击事件相当严重吧。\x02\x03",

            "#11208F塞茜尔小姐她们，\x01",
            "还有医生们一直都很忙碌……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#5P#00003F嗯……\x01",
            "好像确实都很忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x102,
        (
            "#11P#00100F对了，小滴，\x01",
            "亚里欧斯先生\x01",
            "最近来探望过你吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            "#12P#11208F没有，自袭击事件之后，\x01",
            "爸爸一次都没有来过……\x02\x03",

            "#11200F不过倒是用通讯器联络过，\x01",
            "他好像也非常繁忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        (
            "#5P#00200F是吗……\x01",
            "你很寂寞吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        (
            "#12P#11200F……不，我没关系的。\x02\x03",

            "#11203F那么多人不幸牺牲，\x01",
            "还有很多人受伤……\x02\x03",

            "我不能在这种时候\x01",
            "任性撒娇。\x02\x03",

            "#11208F……我很想为芙兰小姐\x01",
            "和其他患者做些什么，\x01",
            "好鼓舞他们振作起来……\x02\x03",

            "#11203F……但我的眼睛看不见，\x01",
            "唯一能做的也只有让自己坚强起来了……\x01",
            "真是很不甘心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        "#11P#00300F……不，这就足够了。\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#00000F你这种坚强的精神\x01",
            "一定能为大家带来\x01",
            "直面逆境的勇气。\x02\x03",

            "#00004F……我们也必须要努力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x105,
        "#5P#10302F呵呵……是啊。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "#12P#11200F那个……\x01",
            "我想大家现在一定都很辛苦，\x01",
            "请继续加油吧。\x02\x03",

            "#11203F我会在这里为你们鼓劲的……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    ClearChrFlags(0x9, 0x10)
    OP_93(0x9, 0x5A, 0x0)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x18E, 5)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -2790, 7000, 12830, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_11_1988 end

    def Function_12_1F40(): pass

    label("Function_12_1F40")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02400.itc", 0x1E)
    LoadChrToIndex("chr/ch02500.itc", 0x1F)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -1900, 7000, 14600, 180)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -1300, 7000, 15610, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -3100, 7000, 14600, 180)
    OP_68(-3510, 8400, 11470, 0)
    MoveCamera(44, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16160, 0)
    SetChrPos(0x104, -2100, 7000, 16800, 180)
    SetChrPos(0x102, -1900, 7000, 17810, 180)
    SetChrPos(0x101, -2310, 7000, 18610, 180)
    SetChrPos(0x103, -1700, 7000, 19600, 180)
    SetChrPos(0x109, -1910, 7000, 20600, 180)
    SetChrPos(0x105, -2120, 7000, 21590, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    BeginChrThread(0x9, 3, 0, 13)
    BeginChrThread(0xE, 3, 0, 14)
    BeginChrThread(0xF, 3, 0, 15)
    BeginChrThread(0x104, 3, 0, 16)
    BeginChrThread(0x102, 3, 0, 17)
    BeginChrThread(0x101, 3, 0, 18)
    BeginChrThread(0x103, 3, 0, 19)
    BeginChrThread(0x109, 3, 0, 20)
    BeginChrThread(0x105, 3, 0, 21)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x9, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)

    #C0090
    ChrTalk(
        0xE,
        "#01400F滴，小心脚下。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "#6P#11202F嗯，谢谢爸爸。\x02\x03",

            "#11204F呵呵，好凉爽的风……\x01",
            "而且阳光温暖明媚，\x01",
            "让人心情舒畅……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#00002F哈哈，那就好。\x02\x03",

            "#00003F……对了，你刚才说，\x01",
            "能感觉到周围的\x01",
            "光芒了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    #C0093
    ChrTalk(
        0x9,
        (
            "#12P#11200F嗯，不过也不是\x01",
            "非常清晰的感觉。\x02\x03",

            "#11203F只是觉得一片纯白色的\x01",
            "雾气迎面而来，\x01",
            "让我感到光明。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x102,
        "#00108F是吗……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x104,
        (
            "#00303F虽说感觉到了光芒，\x01",
            "但终究还是不能\x01",
            "看到东西啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xE,
        "#01403F…………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    #C0097
    ChrTalk(
        0x9,
        (
            "#6P#11202F……那、那个，\x01",
            "各位，请不必\x01",
            "那么消沉。\x02\x03",

            "#11209F其实，这次手术的结果\x01",
            "让我非常开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x105,
        "#5P#10305F哎……是吗？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "#6P#11203F……没能彻底痊愈，\x01",
            "我一开始的确\x01",
            "有些沮丧。\x02\x03",

            "#11208F总觉得肯定\x01",
            "不可能治好了……\x01",
            "所以产生了放弃的想法。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x103,
        "#00208F滴……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "#6P#11202F不过，仔细想想，\x01",
            "『治疗取得进展』这种情况\x01",
            "还是第一次出现呢。\x02\x03",

            "#11204F所以，虽然治疗进度缓慢，\x01",
            "但我的眼睛一定会变好的……\x01",
            "我现在已经这样想了。\x02\x03",

            "#11200F为了一直在照料我的爸爸、\x01",
            "医院中的各位，\x01",
            "还有琪雅……\x02\x03",

            "#11209F我一定不会放弃，\x01",
            "今后还要继续接受治疗。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x109,
        "#5P#10102F小滴……\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        "#00004F……你真的很坚强呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    #C0104
    ChrTalk(
        0x9,
        (
            "#6P#11205F那、那个……对不起，\x01",
            "我好像把自己说得很了不起似的。\x02\x03",

            "#11203F其实治疗费\x01",
            "全都是爸爸出的，\x01",
            "我一直都在给他增添负担……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xE,
        (
            "#01403F……只要你不放弃，\x01",
            "我永远都会像现在这样照料你。\x02\x03",

            "#01402F不要想一些多余的事情，\x01",
            "集中精神接受治疗吧。\x02\x03",

            "#01404F纱绫肯定也是这样期望的。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        (
            "#6P#11203F爸爸……嗯，是啊。\x02\x03",

            "#11202F就算是为了已在女神\x01",
            "身边的妈妈……\x01",
            "我也一定会继续努力的。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xF,
        (
            "#01004F呵呵，亚里欧斯，\x01",
            "她真不愧是你的孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x104,
        (
            "#00309F哈哈，确实。内心坚毅\x01",
            "这个特点真是一模一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xE,
        (
            "#01404F……这大概是她母亲\x01",
            "纱绫的遗传吧。\x02\x03",

            "#01400F外出时间快要结束了。\x01",
            "滴，我们回病房吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        "#6P#11205F啊……嗯，知道了。\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        "#00000F那我们就一起回去吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    #A0112
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德等人又在滴的病房\x01",
            "开心畅谈了一段时间。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 0)
    NewScene("t1550", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1F40 end

    def Function_13_2837(): pass

    label("Function_13_2837")


    def lambda_283C():
        OP_95(0xFE, -3590, 7000, 11230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_283C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_13_2837 end

    def Function_14_285D(): pass

    label("Function_14_285D")


    def lambda_2862():
        OP_95(0xFE, -2590, 7000, 11020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2862)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_14_285D end

    def Function_15_2883(): pass

    label("Function_15_2883")


    def lambda_2888():
        OP_95(0xFE, -1500, 7000, 10030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2888)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_15_2883 end

    def Function_16_28A9(): pass

    label("Function_16_28A9")


    def lambda_28AE():
        OP_95(0xFE, -1400, 7000, 11230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28AE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_16_28A9 end

    def Function_17_28CF(): pass

    label("Function_17_28CF")


    def lambda_28D4():
        OP_95(0xFE, -1990, 7000, 12030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28D4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_17_28CF end

    def Function_18_28F5(): pass

    label("Function_18_28F5")


    def lambda_28FA():
        OP_95(0xFE, -2790, 7000, 12830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28FA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_18_28F5 end

    def Function_19_291B(): pass

    label("Function_19_291B")


    def lambda_2920():
        OP_95(0xFE, -3590, 7000, 13630, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2920)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_19_291B end

    def Function_20_2941(): pass

    label("Function_20_2941")


    def lambda_2946():
        OP_95(0xFE, -2590, 7000, 14030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2946)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_20_2941 end

    def Function_21_2967(): pass

    label("Function_21_2967")


    def lambda_296C():
        OP_95(0xFE, -3400, 7000, 14840, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_296C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_21_2967 end

    def Function_22_298D(): pass

    label("Function_22_298D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A93")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0113
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K要去哪里？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【４Ｆ 药物学·神经科研究室】\x01",      # 0
            "【放弃】\x01",                           # 1
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
        (0, "loc_2A3E"),
        (1, "loc_2A87"),
        (SWITCH_DEFAULT, "loc_2A8E"),
    )


    label("loc_2A3E")

    FadeToDark(1000, 0, -1)
    OP_71(0x5, 0x0, 0x5, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x5)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A79")
    SetScenarioFlags(0x22, 0)
    NewScene("t1650", 100, 0, 0)
    IdleLoop()
    Jump("loc_2A82")

    label("loc_2A79")

    NewScene("t1650", 101, 0, 0)
    IdleLoop()

    label("loc_2A82")

    Jump("loc_2A8E")

    label("loc_2A87")

    EventEnd(0x3)
    Jump("loc_2A8E")

    label("loc_2A8E")

    Jump("loc_2ADE")

    label("loc_2A93")

    EventBegin(0x2)
    ClearMapFlags(0x20)

    #C0114
    ChrTalk(
        0x101,
        (
            "#00000F这是研究楼，\x01",
            "我们没什么特别的事情，\x01",
            "还是不要进去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EventEnd(0x3)

    label("loc_2ADE")

    Return()

    # Function_22_298D end

    def Function_23_2ADF(): pass

    label("Function_23_2ADF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(14750, 9400, -3400, 0)
    MoveCamera(47, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15860, 0)
    SetChrPos(0x101, 18740, 7000, -3160, 270)
    SetChrPos(0x102, 18740, 7000, -3160, 270)
    SetChrPos(0x109, 18740, 7000, -3160, 270)
    SetChrPos(0x105, 18740, 7000, -3160, 270)
    SetChrPos(0x104, 18740, 7000, -3160, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(14750, 8000, -3400, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(500)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x5, 0x10)
    OP_71(0x5, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x5)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 24)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 25)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 27)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 26)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 28)
    WaitChrThread(0x105, 3)
    Sound(107, 0, 100, 0)
    OP_71(0x5, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x5)
    SetMapObjFlags(0x5, 0x10)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    #C0115
    ChrTalk(
        0x104,
        (
            "#00301F……了解到了不少情报，\x01",
            "但谜团好像又增多了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x109,
        "#12P#10106F真让人着急啊……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x102,
        (
            "#00108F嗯，约亚西姆医生已经身亡，\x01",
            "我们如今的线索实在太少了……\x02\x03",

            "#00103F如果能把教团数据库中的情报\x01",
            "解析出来，说不定还能取得一些进展……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x105,
        (
            "#11P#10300F好啦，就把这些事情\x01",
            "当作今后的课题吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#6P#00001F嗯……我们要牢记在心，\x01",
            "多加注意。\x02\x03",

            "#00003F总之，我们已经\x01",
            "完成了这次的委托。\x02\x03",

            "#00000F回去之前，先去和\x01",
            "塞茜尔姐姐打声招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x104,
        "#00309F好啊，我们走吧！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0121
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【新教授的委托】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x70, 0x1, 0x6)
    OP_29(0x70, 0x1, 0x7)
    OP_29(0x70, 0x4, 0x10)
    OP_29(0xA3, 0x1, 0x5)
    OP_66(0x0, 0x1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 15500, 7000, -3000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapObjFlags(0x5, 0x10)
    EventEnd(0x5)
    Return()

    # Function_23_2ADF end

    def Function_24_2EF8(): pass

    label("Function_24_2EF8")


    def lambda_2EFD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2EFD)

    def lambda_2F0E():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F0E)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 13000, 7000, -3000, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_24_2EF8 end

    def Function_25_2F43(): pass

    label("Function_25_2F43")


    def lambda_2F48():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2F48)

    def lambda_2F59():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2F59)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 14160, 7000, -2240, 2000, 0x0)
    OP_93(0x102, 0xB4, 0x1F4)
    Return()

    # Function_25_2F43 end

    def Function_26_2F8E(): pass

    label("Function_26_2F8E")


    def lambda_2F93():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2F93)

    def lambda_2FA4():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2FA4)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 15890, 7000, -3980, 2000, 0x0)
    OP_93(0x104, 0x10E, 0x1F4)
    Return()

    # Function_26_2F8E end

    def Function_27_2FD9(): pass

    label("Function_27_2FD9")


    def lambda_2FDE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2FDE)

    def lambda_2FEF():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2FEF)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 14180, 7000, -4310, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_27_2FD9 end

    def Function_28_3024(): pass

    label("Function_28_3024")


    def lambda_3029():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3029)

    def lambda_303A():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_303A)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 15840, 7000, -2650, 2000, 0x0)
    OP_93(0x105, 0x10E, 0x1F4)
    Return()

    # Function_28_3024 end

    def Function_29_306F(): pass

    label("Function_29_306F")

    EventBegin(0x1)

    #C0122
    ChrTalk(
        0x101,
        (
            "#00000F哦，我们还没去接待处预约，\x01",
            "不能直接进入病房楼。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -16059, 6000, 19210, 270)
    EventEnd(0x4)
    Return()

    # Function_29_306F end

    SaveToFile()

Try(main)
