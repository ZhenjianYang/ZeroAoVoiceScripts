from ScenarioHelper import *

def main():
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
        "奇幻乐园工作人员",       # 1
        "奇幻乐园工作人员",       # 2
        "游客",                   # 3
        "游客",                   # 4
        "梅尔斯",                 # 5
        "柯洛娜",                 # 6
        "利玛",                   # 7
        "翠雀酒店方向",           # 8
        "主题公园方向",           # 9
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

    PlaceName(10.0, 0.0, -68.0, 0x0000, 0x0000, "翠雀酒店方向")
    PlaceName(-5.0, 0.0, 20.0, 0x0000, 0x0000, "主题公园方向")

    ChipFrameInfo(644, 0)                                        # 0

    ScpFunction((
        "Function_0_284",          # 00, 0
        "Function_1_33C",          # 01, 1
        "Function_2_44B",          # 02, 2
        "Function_3_515",          # 03, 3
        "Function_4_6D0",          # 04, 4
        "Function_5_78A",          # 05, 5
        "Function_6_7E4",          # 06, 6
        "Function_7_846",          # 07, 7
        "Function_8_904",          # 08, 8
        "Function_9_9A2",          # 09, 9
        "Function_10_A3B",         # 0A, 10
        "Function_11_B10",         # 0B, 11
        "Function_12_1234",        # 0C, 12
        "Function_13_130C",        # 0D, 13
        "Function_14_147D",        # 0E, 14
        "Function_15_14F1",        # 0F, 15
        "Function_16_1551",        # 10, 16
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_6B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65C")

    #C0001
    ChrTalk(
        0x8,
        (
            "主题公园内正在\x01",
            "举办晚间活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "咪西它们正在公园内巡游，\x01",
            "游行活动正值高潮。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_614")

    #C0003
    ChrTalk(
        0x103,
        "#00203F……老实说，我很想进去看看。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#00002F哈哈，这次不行啦，\x01",
            "等下次有机会再来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x103,
        "#00202F呵呵……那就说好了哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_654")

    label("loc_614")


    #C0006
    ChrTalk(
        0x101,
        (
            "#00003F（嗯～缇欧要是听到的话，\x01",
            "  肯定会很想去看看吧……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_654")

    SetScenarioFlags(0x0, 0)
    Jump("loc_6B0")

    label("loc_65C")


    #C0007
    ChrTalk(
        0x8,
        (
            "主题公园内正在\x01",
            "举办晚间活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "咪西它们正在公园内巡游，\x01",
            "游行活动正值高潮。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B0")

    Jump("loc_6CC")

    label("loc_6B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_6C3")
    Jump("loc_6CC")

    label("loc_6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_6CC")

    label("loc_6CC")

    TalkEnd(0xFE)
    Return()

    # Function_3_515 end

    def Function_4_6D0(): pass

    label("Function_4_6D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_76F")

    #C0009
    ChrTalk(
        0x9,
        (
            "米修拉姆著名的烟花表演，\x01",
            "每天会燃放\x01",
            "一百发左右。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x9,
        (
            "在主题公园内自不必说，就算在酒店里，\x01",
            "或是在夜间航行的飞船上，\x01",
            "也能清楚地观赏到哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_786")

    label("loc_76F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_77D")
    Jump("loc_786")

    label("loc_77D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_786")

    label("loc_786")

    TalkEnd(0xFE)
    Return()

    # Function_4_6D0 end

    def Function_5_78A(): pass

    label("Function_5_78A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_7C9")

    #C0011
    ChrTalk(
        0xA,
        "（……现、现在或许是个牵手的好机会……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E0")

    label("loc_7C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_7D7")
    Jump("loc_7E0")

    label("loc_7D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_7E0")

    label("loc_7E0")

    TalkEnd(0xFE)
    Return()

    # Function_5_78A end

    def Function_6_7E4(): pass

    label("Function_6_7E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_82B")

    #C0012
    ChrTalk(
        0xB,
        "哇～放了好多烟花哦……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xB,
        "……呵呵，真漂亮……\x02",
    )

    CloseMessageWindow()
    Jump("loc_842")

    label("loc_82B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_839")
    Jump("loc_842")

    label("loc_839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_842")

    label("loc_842")

    TalkEnd(0xFE)
    Return()

    # Function_6_7E4 end

    def Function_7_846(): pass

    label("Function_7_846")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_8CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_864")
    Call(0, 8)
    Jump("loc_8C8")

    label("loc_864")


    #C0014
    ChrTalk(
        0xC,
        (
            "利玛玩得这么高兴，\x01",
            "来这一趟也值得了。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xC,
        (
            "其实我本来还想在酒店住一晚，\x01",
            "可惜实在预约不到房间。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C8")

    Jump("loc_900")

    label("loc_8CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_8DB")
    Jump("loc_900")

    label("loc_8DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_8E9")
    Jump("loc_900")

    label("loc_8E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_8F7")
    Jump("loc_900")

    label("loc_8F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_900")

    label("loc_900")

    TalkEnd(0xFE)
    Return()

    # Function_7_846 end

    def Function_8_904(): pass

    label("Function_8_904")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0016
    ChrTalk(
        0xC,
        (
            "呼～今天还真是\x01",
            "玩了一整天啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xC,
        "利玛，玩得开心吗？\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xE,
        (
            "嗯，非常开心～！！\x01",
            "谢谢爸爸～！！\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xD,
        "呵呵，辛苦你了。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 1)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_8_904 end

    def Function_9_9A2(): pass

    label("Function_9_9A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C0")
    Call(0, 8)
    Jump("loc_9FF")

    label("loc_9C0")


    #C0020
    ChrTalk(
        0xD,
        "呵呵，辛苦你了。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xD,
        (
            "回去以后，我会给你做\x01",
            "很多好吃的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FF")

    Jump("loc_A37")

    label("loc_A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_A12")
    Jump("loc_A37")

    label("loc_A12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A20")
    Jump("loc_A37")

    label("loc_A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A2E")
    Jump("loc_A37")

    label("loc_A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_A37")

    label("loc_A37")

    TalkEnd(0xFE)
    Return()

    # Function_9_9A2 end

    def Function_10_A3B(): pass

    label("Function_10_A3B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_AD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A59")
    Call(0, 8)
    Jump("loc_AD4")

    label("loc_A59")


    #C0022
    ChrTalk(
        0xE,
        (
            "我在镜子城堡的最高处\x01",
            "许了这样一个心愿——\x01",
            "要和爸爸妈妈永远在一起～！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xE,
        (
            "今天还坐了摩天轮和过山车，\x01",
            "玩得真开心呀～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD4")

    Jump("loc_B0C")

    label("loc_AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_AE7")
    Jump("loc_B0C")

    label("loc_AE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_AF5")
    Jump("loc_B0C")

    label("loc_AF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_B03")
    Jump("loc_B0C")

    label("loc_B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_B0C")

    label("loc_B0C")

    TalkEnd(0xFE)
    Return()

    # Function_10_A3B end

    def Function_11_B10(): pass

    label("Function_11_B10")

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

    def lambda_BE3():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BE3)
    Sleep(50)

    def lambda_BFB():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BFB)
    Sleep(50)

    def lambda_C13():
        OP_9B(0x0, 0x103, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_C13)
    Sleep(50)

    def lambda_C2B():
        OP_9B(0x0, 0x104, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C2B)
    Sleep(50)

    def lambda_C43():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C43)
    Sleep(50)

    def lambda_C5B():
        OP_9B(0x0, 0x109, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C5B)
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
        "#00107F#6P这、这是……！？\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#00013F#6P垂幕变了！？\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x104,
        "#00301F#6P喂喂，这是……\x02",
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

    def lambda_E23():
        OP_9B(0x0, 0x101, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E23)
    Sleep(50)

    def lambda_E3B():
        OP_9B(0x0, 0x102, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_E3B)
    Sleep(50)

    def lambda_E53():
        OP_9B(0x0, 0x103, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_E53)
    Sleep(50)

    def lambda_E6B():
        OP_9B(0x0, 0x104, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E6B)
    Sleep(50)

    def lambda_E83():
        OP_9B(0x0, 0x105, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E83)
    Sleep(50)

    def lambda_E9B():
        OP_9B(0x0, 0x109, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E9B)
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
        "#10108F#6P什、什么时候变的……？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x105,
        (
            "#10308F#6P唔，这似乎不是夜间限定的\x01",
            "特别节目啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x103,
        (
            "#00206F#6P……我可没听说过\x01",
            "会有这种安排。\x02\x03",

            "#00201F而且……\x01",
            "也不可能把咪西换成\x01",
            "别的吉祥物吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#00006F#6P……是啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0031
    ChrTalk(
        0x101,
        "#00005F#6P那是──\x02",
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
        "#00105F『小丑奇幻乐园』……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 160, -1, -1)

    #A0033
    AnonymousTalk(
        0x104,
        (
            "#00306F连名字都被\x01",
            "改掉了啊……\x02",
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
            "#10113F我、我难道\x01",
            "是在做梦吗……\x02",
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
            "#10306F……就算真的是梦，\x01",
            "也是一场噩梦呢。\x02",
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
            "#00003F#5P琪雅应该\x01",
            "就在前面。\x02\x03",

            "#00013F既然如此……\x01",
            "我们也只能冲进去了！\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x102,
        "#00101F#6P嗯……！\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        "#00301F#6P只能进去了……！\x02",
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

    # Function_11_B10 end

    def Function_12_1234(): pass

    label("Function_12_1234")

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
        "#6P#00002F啊…………\x02",
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

    # Function_12_1234 end

    def Function_13_130C(): pass

    label("Function_13_130C")

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
            "#12P#00004F……好，那我们这就\x01",
            "去迎宾馆吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_13D5")

    #C0042
    ChrTalk(
        0x102,
        "#00102F嗯，好的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1456")

    label("loc_13D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_13F6")

    #C0043
    ChrTalk(
        0x103,
        "#00202F好的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1456")

    label("loc_13F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_1415")

    #C0044
    ChrTalk(
        0x104,
        "#00309F好。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1456")

    label("loc_1415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_1434")

    #C0045
    ChrTalk(
        0x109,
        "#10109F好！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1456")

    label("loc_1434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_1456")

    #C0046
    ChrTalk(
        0x105,
        "#10304F呵呵，走吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1456")

    OP_5A()
    ClearMapFlags(0x10000000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, -57250, 0)
    EventEnd(0x5)
    Return()

    # Function_13_130C end

    def Function_14_147D(): pass

    label("Function_14_147D")

    EventBegin(0x1)

    #C0047
    ChrTalk(
        0x101,
        (
            "#00000F虽说晚上的\x01",
            "主题公园好像也很有趣，\x01",
            "但我们还是下次再来吧。\x02\x03",

            "现在要赶快前往迎宾馆。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 4400, -1250, 180)
    EventEnd(0x4)
    Return()

    # Function_14_147D end

    def Function_15_14F1(): pass

    label("Function_15_14F1")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里画着\x01",
            "主题公园的平面图。\x02\x03",

            "广阔的区域内\x01",
            "似乎遍布着\x01",
            "各种各样的游乐设施。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_15_14F1 end

    def Function_16_1551(): pass

    label("Function_16_1551")

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
            "   ～致各位来园宾客～\x01\x01",
            "本主题公园内\x01",
            "严禁喧闹生事，\x01",
            "或携带危险物品入园。\x01\x01",
            "此外，儿童必须\x01",
            "由监护人陪同入园，\x01",
            "敬请配合。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_16_1551 end

    SaveToFile()

Try(main)
