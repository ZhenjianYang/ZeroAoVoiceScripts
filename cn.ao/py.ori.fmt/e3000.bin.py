from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e3000.bin",                # FileName
        "e3000",                    # MapName
        "e3000",                    # Location
        0x00A1,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 161, 0, 1, 0, 2],
    )

    BuildStringList((
        "e3000",                  # 0
        "缇欧",                   # 1
        "蔡特",                   # 2
        "瓦吉",                   # 3
        "琪雅",                   # 4
        "游客",                   # 5
        "游客",                   # 6
        "玛丽亚贝尔",             # 7
    ))

    AddCharChip((
        "chr/ch00200.itc",                   # 00
        "chr/ch02707.itc",                   # 01
        "chr/ch03002.itc",                   # 02
        "chr/ch08200.itc",                   # 03
        "chr/ch24502.itc",                   # 04
        "chr/ch21302.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
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

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    404,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    388,  0x0, 0,   2,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(2210,    4250,    899,     180,  453,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(1029,    4250,    899,     180,  453,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(580, 0)                                        # 0

    ScpFunction((
        "Function_0_244",          # 00, 0
        "Function_1_2F4",          # 01, 1
        "Function_2_408",          # 02, 2
        "Function_3_475",          # 03, 3
        "Function_4_97A",          # 04, 4
        "Function_5_B88",          # 05, 5
        "Function_6_BA6",          # 06, 6
        "Function_7_E30",          # 07, 7
        "Function_8_F1F",          # 08, 8
        "Function_9_F8A",          # 09, 9
        "Function_10_231B",        # 0A, 10
        "Function_11_233B",        # 0B, 11
        "Function_12_235B",        # 0C, 12
        "Function_13_2AC7",        # 0D, 13
        "Function_14_2C5E",        # 0E, 14
        "Function_15_37AA",        # 0F, 15
        "Function_16_37C1",        # 10, 16
        "Function_17_3845",        # 11, 17
        "Function_18_386B",        # 12, 18
        "Function_19_3882",        # 13, 19
        "Function_20_38A8",        # 14, 20
        "Function_21_38D5",        # 15, 21
        "Function_22_38E7",        # 16, 22
        "Function_23_38F2",        # 17, 23
        "Function_24_3911",        # 18, 24
        "Function_25_3930",        # 19, 25
        "Function_26_3A43",        # 1A, 26
        "Function_27_482D",        # 1B, 27
        "Function_28_4853",        # 1C, 28
    ))


    def Function_0_244(): pass

    label("Function_0_244")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_27C"),
        (1, "loc_288"),
        (2, "loc_294"),
        (3, "loc_2A0"),
        (4, "loc_2AC"),
        (5, "loc_2B8"),
        (6, "loc_2C4"),
        (SWITCH_DEFAULT, "loc_2D0"),
    )


    label("loc_27C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_288")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_294")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2A0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2AC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2B8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2F3")

    Return()

    # Function_0_244 end

    def Function_1_2F4(): pass

    label("Function_1_2F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38A")
    SetChrPos(0x8, -500, 4100, 11000, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, 1000, 4100, 11000, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, -2250, 4250, -2100, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x10)
    SetChrSubChip(0xD, 0x1)

    label("loc_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AE")
    SetChrPos(0xB, 3000, 4100, -8000, 180)
    ClearChrFlags(0xB, 0x80)

    label("loc_3AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3C8")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 9)
    Jump("loc_3EE")

    label("loc_3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_3DF")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 1)
    Event(0, 25)
    Jump("loc_3EE")

    label("loc_3DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_3EE")
    ClearScenarioFlags(0x22, 2)
    Event(0, 26)

    label("loc_3EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_407")
    Event(0, 13)

    label("loc_407")

    Return()

    # Function_1_2F4 end

    def Function_2_408(): pass

    label("Function_2_408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_422")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_43A")

    label("loc_422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 0)), scpexpr(EXPR_END)), "loc_43A")
    SetScenarioFlags(0x0, 1)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x25, 0)

    label("loc_43A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_44E")
    OP_24(0x1DF)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_454")

    label("loc_44E")

    Sound(479, 1, 100, 0)

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_474")
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_474")

    Return()

    # Function_2_408 end

    def Function_3_475(): pass

    label("Function_3_475")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_486")
    Jump("loc_976")

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_494")
    Jump("loc_976")

    label("loc_494")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4A4")
    Jump("loc_976")

    label("loc_4A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_4B2")
    Jump("loc_976")

    label("loc_4B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_4C0")
    Jump("loc_976")

    label("loc_4C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4CE")
    Jump("loc_976")

    label("loc_4CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_4DC")
    Jump("loc_976")

    label("loc_4DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_4EA")
    Jump("loc_976")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_976")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90F")

    #C0001
    ChrTalk(
        0x8,
        (
            "#00204F咳，总之……\x01",
            "今天就尽情享受\x01",
            "久违的休假吧。\x02\x03",

            "#00200F我们上次来这里是为了\x01",
            "调查『竞拍会』，\x01",
            "几乎没有娱乐时间呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#00004F确实，\x01",
            "这还是第一次\x01",
            "为了游玩来米修拉姆呢。\x02\x03",

            "#00009F哈哈，缇欧\x01",
            "最关心的自然还是\x01",
            "主题公园吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "#00204F当然。\x02\x03",

            "『米修拉姆奇幻乐园』\x01",
            "（MICHLLAM WONDER LAND）……\x02\x03",

            "——简称Ｍ·Ｗ·Ｌ。\x02\x03",

            "#00202F真期待和咪西的见面。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_820")
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0004
    ChrTalk(
        0x101,
        (
            "#00004F……说起来，你还记得\x01",
            "当时那个『约定』吗？\x02\x03",

            "#00002F将教团事件解决之后，\x01",
            "找时间一起来主题公园\x01",
            "游玩的约定……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "#00204F……当然记得。\x02\x03",

            "『首先是支援科全体成员一起来玩……\x01",
            "  然后是罗伊德前辈和我两个人来。』\x02\x03",

            "#00200F从某种意义上说，\x01",
            "这次的招待总算使计划\x01",
            "顺利进入第一阶段了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，不太理解\x01",
            "你这种表达方式呢……\x02\x03",

            "#00000F总之，近期我们一定要\x01",
            "单独再来玩一次哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "#00209F呵呵……\x01",
            "嗯，我很期待。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_907")

    label("loc_820")


    #C0008
    ChrTalk(
        0x101,
        (
            "#00004F缇欧对咪西的了解\x01",
            "非常详细吧？\x02\x03",

            "#00002F能不能多告诉我一些\x01",
            "有关主题公园的信息？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#00204F……好的。\x02\x03",

            "#00202F那么，就把咪西诞生的秘密，\x01",
            "还有家族构成等信息\x01",
            "详细说给罗伊德前辈听吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#00006F不不，倒也不用那么夸张。\x02",
    )

    CloseMessageWindow()

    label("loc_907")

    SetScenarioFlags(0x15A, 0)
    Jump("loc_976")

    label("loc_90F")


    #C0011
    ChrTalk(
        0x8,
        (
            "#00202F到了主题公园之后，\x01",
            "我会好好给你讲一讲\x01",
            "有关咪西的事情。\x02\x03",

            "#00204F现在还是先去\x01",
            "和大家聊聊吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_976")

    TalkEnd(0xFE)
    Return()

    # Function_3_475 end

    def Function_4_97A(): pass

    label("Function_4_97A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_98B")
    Jump("loc_B84")

    label("loc_98B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_999")
    Jump("loc_B84")

    label("loc_999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_9A7")
    Jump("loc_B84")

    label("loc_9A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_9B5")
    Jump("loc_B84")

    label("loc_9B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_9C3")
    Jump("loc_B84")

    label("loc_9C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_9D1")
    Jump("loc_B84")

    label("loc_9D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_9DF")
    Jump("loc_B84")

    label("loc_9DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_B84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B33")
    OP_4B(0x8, 0xFF)

    #C0012
    ChrTalk(
        0x9,
        "#01203F咕呜呜……嗷。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    #C0013
    ChrTalk(
        0x8,
        (
            "#00204F它说『哎呀呀，真是个\x01",
            "不成熟的队长』。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00012F哈哈，被蔡特这样一说，\x01",
            "还真是很没面子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "#00211F它还说，\x01",
            "『你太迟钝了』、\x01",
            "『学机灵些吧』。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 500)

    #C0016
    ChrTalk(
        0x101,
        (
            "#00006F……其中好像掺杂了\x01",
            "你的主观想法吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        "#00203F哪有的事。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)
    SetScenarioFlags(0x0, 4)
    OP_4C(0x8, 0xFF)
    Jump("loc_B84")

    label("loc_B33")


    #C0018
    ChrTalk(
        0x9,
        "#01203F……咕呜呜呜……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#00002F（蔡特好像也很\x01",
            "  期待去米修拉姆呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B84")

    TalkEnd(0xFE)
    Return()

    # Function_4_97A end

    def Function_5_B88(): pass

    label("Function_5_B88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B9F")
    Call(0, 14)
    Return()

    label("loc_B9F")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_5_B88 end

    def Function_6_BA6(): pass

    label("Function_6_BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BBD")
    Call(0, 12)
    Return()

    label("loc_BBD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_BCE")
    Jump("loc_E2C")

    label("loc_BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_BDC")
    Jump("loc_E2C")

    label("loc_BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_BEA")
    Jump("loc_E2C")

    label("loc_BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_BF8")
    Jump("loc_E2C")

    label("loc_BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_C06")
    Jump("loc_E2C")

    label("loc_C06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_C14")
    Jump("loc_E2C")

    label("loc_C14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_C22")
    Jump("loc_E2C")

    label("loc_C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_E2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3A")
    Jump("loc_E2C")

    label("loc_C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D8E")

    #C0020
    ChrTalk(
        0xA,
        (
            "#10304F呼，除了男公关的工作之外，\x01",
            "真是好久没去米修拉姆玩过了，\x01",
            "今天可要好好放松一下。\x02\x03",

            "#10300F等到有空时，我准备\x01",
            "去西餐厅喝一杯，\x01",
            "你要不要一起去？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#00003F……那个，我早就想说了，\x01",
            "未成年人是不可以饮酒的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xA,
        (
            "#10309F呵呵，不要这么死板嘛，\x01",
            "出来玩的时候就要尽兴一些。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#00006F这并不是什么\x01",
            "死板不死板的问题。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_E2C")

    label("loc_D8E")


    #C0024
    ChrTalk(
        0xA,
        (
            "#10309F不要这么死板嘛，\x01",
            "出来玩的时候就要尽兴一些。\x02\x03",

            "#10302F不然的话，\x01",
            "我就传授给你一些征服女孩子\x01",
            "的男公关基本技巧如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#00006F不、不要收买别人……\x02",
    )

    CloseMessageWindow()

    label("loc_E2C")

    TalkEnd(0xFE)
    Return()

    # Function_6_BA6 end

    def Function_7_E30(): pass

    label("Function_7_E30")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_F1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB7")

    #C0026
    ChrTalk(
        0xC,
        (
            "市里的人都在讨论\x01",
            "什么独立。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xC,
        (
            "我们是从外国来的，\x01",
            "并不是很理解……\x01",
            "但听起来似乎是很重要的问题呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_F1B")

    label("loc_EB7")


    #C0028
    ChrTalk(
        0xC,
        (
            "市里的人都在讨论的\x01",
            "独立到底是什么意思呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xC,
        (
            "我不是很理解……\x01",
            "但听起来似乎是很重要的问题呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1B")

    TalkEnd(0xFE)
    Return()

    # Function_7_E30 end

    def Function_8_F1F(): pass

    label("Function_8_F1F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_F86")

    #C0030
    ChrTalk(
        0xD,
        (
            "嘿，先不说这些了，你看，\x01",
            "前面座位上的那个男孩是不是很可爱？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xD,
        "不然过去和他搭讪吧？\x02",
    )

    CloseMessageWindow()

    label("loc_F86")

    TalkEnd(0xFE)
    Return()

    # Function_8_F1F end

    def Function_9_F8A(): pass

    label("Function_9_F8A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_32(0xFF, 0xFE, 0x0)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x4, 0xFF)
    LoadChrToIndex("apl/ch51300.itc", 0x1E)
    LoadChrToIndex("apl/ch51301.itc", 0x1F)
    SoundLoad(479)
    SoundLoad(2674)
    SoundLoad(2675)
    SoundLoad(2676)
    SoundLoad(4108)
    SoundLoad(3054)
    SoundLoad(3060)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis245.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis091.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00201.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01200.itp")
    SetChrPos(0x101, -750, 4100, 12500, 0)
    ClearChrFlags(0x9, 0x80)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 1000, 4100, 11000, 0)
    BeginChrThread(0x9, 3, 0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -2250, 4250, -2100, 180)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 4100, 5000, 0)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x10)
    SetChrSubChip(0xD, 0x1)
    Sleep(1000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0032
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30W通商会议结束后，经过两周──\x01",
            "克洛斯贝尔被一股静静的热烈气氛所笼罩。\x02\x03",

            "其它自治州──\x01",
            "列曼、奥雷德、诺桑普里亚\x01",
            "均得到了亚尔特利亚法典国的认可，\x01",
            "拥有与国家同等的主权。\x02\x03",

            "而克洛斯贝尔自治州\x01",
            "作为帝国与共和国之间的缓冲地带，\x01",
            "始终都只有自治权而已。\x02\x03",

            "（此外，自治州还要以『委任统治费』\x01",
            "  的名义，将税收的１０％\x01",
            "  缴纳给帝国和共和国。）\x02\x03",

            "克洛斯贝尔作为贸易·金融中心，一直在繁荣发展，\x01",
            "而政治根基却与之形成强烈反比，显得极其脆弱。\x02\x03",

            "其结果就是外国势力的干涉日益强烈，\x01",
            "黑手党等组织也越发猖獗。\x02\x03",

            "为了打破这种扭曲的状况，\x01",
            "迪塔市长大胆提出了\x01",
            "『独立为主权国家』的倡导，\x01",
            "众多市民对此也深有共鸣……\x02\x03",

            "但也有很多人担心两大国的反应，\x01",
            "自治州内，到处都在进行着\x01",
            "有关『独立利弊』问题的讨论。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    PlayBGM("ed7515", 0)
    OP_68(0, 4100, -15000, 0)
    MoveCamera(340, 6, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(45000, 0)
    OP_68(0, 4100, 45000, 12000)
    Sound(479, 2, 20, 0)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(200)
    FadeToBright(2000, 0)
    Sleep(10500)
    OP_0D()
    Fade(1000)
    OP_68(-750, 5100, 12500, 0)
    MoveCamera(225, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    SetCameraDistance(21000, 2000)
    OP_6F(0x79)
    OP_0D()

    #C0033
    ChrTalk(
        0x101,
        "#00008F#5P#30W……………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(800)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    #C0034
    ChrTalk(
        0x101,
        (
            "#00006F#5P#30W…………呼……………\x02\x03",

            "#00008F还是不行啊，虽然自那之后，\x01",
            "已经过去快半个月了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(3052, 255, 80, 0)    #voice#Zeit

    #C0035
    ChrTalk(
        0x9,
        "#01200F#6P#30W嗷？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x7)
    Sleep(100)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    TurnDirection(0x101, 0x9, 500)
    Sleep(300)

    #C0036
    ChrTalk(
        0x101,
        (
            "#00012F#11P#30W抱歉，我又在叹气了。\x02\x03",

            "#00008F……蔡特，告诉我。\x02\x03",

            "身为队长，在这种时候\x01",
            "究竟应该做些什么呢？\x02\x03",

            "兰迪自不用说，\x01",
            "艾莉和诺艾尔似乎也\x01",
            "一直心事重重……\x02\x03",

            "#00006F……好像连琪雅\x01",
            "都很担忧呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0037
    AnonymousTalk(
        0x9,
        (
            "#3054V#30W嗷。\x02\x03",

            "#3060V#40W咕呜呜呜呜呜……嗷。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xBF4)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)

    #C0038
    ChrTalk(
        0x101,
        (
            "#00005F#11P#30W那个……\x01",
            "你在说什么呢？\x02\x03",

            "#00012F哈哈，抱歉啊，\x01",
            "我向你发问，却听不懂……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x8, 0x8)
    OP_C9(0x0, 0x80000000)

    #N0039
    NpcTalk(
        0xA,
        "少女的声音",
        (
            "#2674V#5P#N#30W#35A『在这种时候，\x01",
            "  不要从理论的角度来思考。』\x02\x03",

            "#2675V#25A『只要遵照自己的想法\x01",
            "  行动就可以了。』\x02\x03",

            "#4108V#N#15A──它是这样说的。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_68(-350, 5100, 11350, 2500)
    OP_9B(0x0, 0x8, 0x0, 0x1194, 0x7D0, 0x0)
    OP_6F(0x79)

    #C0040
    ChrTalk(
        0x101,
        "#00005F#12P缇欧……\x02",
    )

    CloseMessageWindow()
    OP_68(-1350, 5100, 12250, 2500)
    MoveCamera(210, 23, 0, 2500)
    SetCameraDistance(19330, 2500)

    def lambda_18DB():

        label("loc_18DB")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_18DB")

    QueueWorkItem2(0x101, 2, lambda_18DB)
    OP_96(0x8, 0xFFFFF894, 0x1004, 0x2F76, 0x7D0, 0x0)
    EndChrThread(0x101, 0x2)
    OP_6F(0x79)
    SetCameraDistance(18360, 20000)
    Sound(2676, 255, 80, 0)    #voice#Tio
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0041
    AnonymousTalk(
        0x8,
        (
            "#30W……好凉爽的风。\x02\x03",

            "难得有次休假，天气这么晴朗，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    #C0042
    ChrTalk(
        0x101,
        (
            "#00004F#5P是啊……\x02\x03",

            "#00000F在接到玛丽亚贝尔小姐的邀请时，\x01",
            "我还在想到底会是什么事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#00202F#5P呵呵，以为是陷阱之类的吗？\x02\x03",

            "她好像直到现在\x01",
            "都有些敌视你呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#00012F#5P哈哈，确实闪现过这个想法呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0045
    ChrTalk(
        0x101,
        (
            "#00006F#5P……抱歉啊，缇欧。\x02\x03",

            "#00008F你刚刚回来，就让你\x01",
            "看到了我这么没用的样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "#00206F#5P……这也难怪啊。\x02\x03",

            "#00208F毕竟有那么多人\x01",
            "死在自己的面前……\x02\x03",

            "#00200F一般来说，肯定会受很大刺激的。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#00003F#5P不，既然我选择了搜查官的道路，\x01",
            "就应该有相应的觉悟。\x02\x03",

            "#00001F……之前也经历过约亚西姆那件事，\x01",
            "本以为自己已经习惯了，结果还是……\x02\x03",

            "#00006F无论是作为搜查官，还是作为队长，\x01",
            "我的觉悟好像都还远远不够呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        "#00203F#5P#40W呼……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    #C0049
    ChrTalk(
        0x8,
        (
            "#00200F#11P能否习惯这种事情，\x01",
            "与觉悟并没有很大关系。\x02\x03",

            "不然的话，我应该早就\x01",
            "彻底习惯那种场面了。\x02\x03",

            "#00203F毕竟我对『死亡』的熟悉程度\x01",
            "应该是仅次于兰迪前辈的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 500)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(1000)
    SetCameraDistance(18360, 0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)

    #C0050
    ChrTalk(
        0x101,
        "#00008F#6P……是吗………\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#00206F#11P但我并不认为\x01",
            "自己比罗伊德前辈\x01",
            "更适合当搜查官……\x02\x03",

            "当然，我也没有\x01",
            "成为队长的觉悟。\x02\x03",

            "#00201F我想，大家对罗伊德前辈的期待\x01",
            "并不是那方面的觉悟。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#00005F#6P缇欧……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0053
    ChrTalk(
        0x101,
        (
            "#00006F#6P……是啊，\x01",
            "也许正如你所说。\x02\x03",

            "#00008F我将遭受到的刺激误认为是\x01",
            "自己的觉悟不足，才导致止步不前。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "#00204F#11P既然如此，那就赶快迈开脚步吧。\x02\x03",

            "#00202F难得有这种全员一起休假的机会……\x02\x03",

            "努力让大家玩得开心\x01",
            "也是队长的职责吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#00002F#6P嗯，说的没错。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(18060, 1000)
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_6F(0x79)
    Fade(250)
    BeginChrThread(0x101, 3, 0, 10)
    BeginChrThread(0x8, 3, 0, 11)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x8, 3)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7565", 0)

    #C0056
    ChrTalk(
        0x8,
        "#00205F#11P……！？\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#00009F#6P谢啦，缇欧。\x02\x03",

            "#00000F我现在就去找大家\x01",
            "随便聊聊。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "#00206F#11P啊……嗯……\x01",
            "这就好。\x02\x03",

            "#00208F#30W……可是……那个……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0059
    ChrTalk(
        0x101,
        "#00011F#6P哦哦，抱歉抱歉。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_A1(0x101, 0x4E2, 0x2, 0x1, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_9B(0x1, 0x101, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
    OP_0D()
    #Sound(2274, 255, 60, 0)    #voice#Tio

    #C0060
    ChrTalk(
        0x8,
        "#00205F#11P#40W……啊………\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#00012F#6P哈哈，我并不是把你当成小孩子，\x01",
            "只是想表达一下谢意……\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x8, 0x5DC, 0x3, 0x7, 0x8, 0x9)

    #C0062
    ChrTalk(
        0x8,
        (
            "#00206F#11P没关系，我并不介意。\x02\x03",

            "#00208F#30W不如说……反倒想再……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#00005F#6P哎？\x02",
    )

    CloseMessageWindow()
    OP_A1(0x8, 0x5DC, 0x2, 0xA, 0xB)
    Sleep(150)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0064
    ChrTalk(
        0x8,
        "#00201F#11P唔……没什么！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x8, 0x5DC, 0x2, 0xC, 0xD)

    #C0065
    ChrTalk(
        0x8,
        (
            "#00203F#11P赶快去找\x01",
            "大家聊聊吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#00000F#6P啊……哦……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    #Sound(3053, 255, 60, 0)    #voice#Zeit

    #C0067
    ChrTalk(
        0x9,
        "#01203F#6P#30W咕呜呜呜呜……（唉呀呀）\x02",
    )

    CloseMessageWindow()
    OP_24(0xBED)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x8, -500, 4100, 11000, 90)
    ClearChrFlags(0x8, 0x8000)
    OP_4C(0x8, 0xFF)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 1000, 4100, 11000, 180)
    ClearChrFlags(0x9, 0x8000)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -2250, 4250, -2100, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0x0, 0, 4100, 8000, 180)
    SetScenarioFlags(0x144, 0)
    OP_29(0xA5, 0x4, 0x2)
    OP_29(0xA5, 0x1, 0x0)
    ClearChrFlags(0xA, 0x8)
    OP_25(0x1DF, 0x64)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_9_F8A end

    def Function_10_231B(): pass

    label("Function_10_231B")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1E)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0x3E8, 0x7, 0x2, 0x3, 0x4, 0x5, 0x4, 0x3, 0x2)
    Return()

    # Function_10_231B end

    def Function_11_233B(): pass

    label("Function_11_233B")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1F)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0x3E8, 0x7, 0x2, 0x3, 0x4, 0x5, 0x4, 0x3, 0x2)
    Return()

    # Function_11_233B end

    def Function_12_235B(): pass

    label("Function_12_235B")

    EventBegin(0x0)
    Fade(500)
    OP_68(-2250, 5100, -2100, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16450, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10301.itp")
    SetChrPos(0x101, -1050, 4100, -2900, 315)
    SetChrSubChip(0xA, 0x1)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    #Sound(2911, 255, 100, 0)    #voice#Lazy

    #A0068
    AnonymousTalk(
        0xA,
        (
            "#30W哟，罗伊德。\x02\x03",

            "被人鼓励了一番之后，\x01",
            "你好像恢复精神了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xB5F)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0069
    ChrTalk(
        0x101,
        (
            "#00012F#6P哈哈，算是吧。\x02\x03",

            "#00000F……瓦吉，你好像\x01",
            "完全没受影响啊。\x02\x03",

            "还是和平时\x01",
            "一样沉静。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xA,
        (
            "#10304F#5P呵，这正是我的优点嘛。\x02\x03",

            "#10308F而且我以前也\x01",
            "并不是没见过那种\x01",
            "非正常的死亡。\x02\x03",

            "#10303F不过，那是在来到克洛斯贝尔之前的事情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        (
            "#00008F#6P是吗……\x02\x03",

            "#00005F……哎，这好像还是第一次\x01",
            "听你谈起自己的往事呢。\x02\x03",

            "#00000F以前只在无意中听说过你不是\x01",
            "出身于克洛斯贝尔的……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xA,
        (
            "#10309F#5P呵呵，这些都是商业机密啦。\x02\x03",

            "#10300F不过可以告诉你……\x01",
            "我曾在贫民窟中生活过。\x02\x03",

            "那是一片远比旧城区更加\x01",
            "穷困萧条的垃圾场。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6F), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2701")

    #C0073
    ChrTalk(
        0x101,
        (
            "#00006F#6P……是吗……\x02\x03",

            "#00008F说起来，听说彩虹剧团的修利\x01",
            "也出身于边境地区的贫民窟……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2761")

    label("loc_2701")


    #C0074
    ChrTalk(
        0x101,
        (
            "#00006F#6P……是吗……\x02\x03",

            "#00008F说起来，听说彩虹剧团的那个新人\x01",
            "也出身于边境地区的贫民窟……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2761")


    #C0075
    ChrTalk(
        0xA,
        (
            "#10305F#5P哦，那个诺桑普里亚的孩子啊。\x02\x03",

            "#10306F那个地方相当贫困……\x01",
            "要靠在外从事猎兵行业的\x01",
            "亲人寄钱回去，才能勉强糊口。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#00003F#6P嗯，我也听说过相关的传闻……\x02\x03",

            "#00005F……哎，听你的口气，\x01",
            "简直就像去过那里一样啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xA,
        (
            "#10304F#5P呵呵，是吗～\x02\x03",

            "#10308F#30W………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#00005F#6P？？\x02\x03",

            "#00003F虽然你故意装出一副轻松的口气，\x01",
            "但总觉得好像有点没精神的样子……\x02\x03",

            "#00001F……是不是有什么事呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "#10304F#5P我倒没有。\x02\x03",

            "#10300F不过，剑蛇帮那边\x01",
            "好像发生了不少事。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        (
            "#00001F#6P剑蛇帮……\x01",
            "瓦鲁多他们吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xA,
        (
            "#10304F#5P以那样的形式分别之后，\x01",
            "终究还是有些挂怀。\x02\x03",

            "#10302F就算是我这以神秘气质而著称的\x01",
            "冷俊美少年也不能免俗啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#00006F#6P哪有这样夸奖自己的……\x02\x03",

            "#00008F……不过，我也有些\x01",
            "担心瓦鲁多的情况。\x02\x03",

            "#00000F等以后有空时，\x01",
            "不妨过去看看他们好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xA,
        (
            "#10304F#5P呵呵，你要是愿意代劳，\x01",
            "那可真是再好不过了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -1050, 4100, -3100, 180)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0xD, 0x1)
    SetScenarioFlags(0x144, 1)
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_235B end

    def Function_13_2AC7(): pass

    label("Function_13_2AC7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 2640, 4100, 4150, 180)
    SetChrPos(0xB, 3000, 4100, -8000, 180)
    ClearChrFlags(0xB, 0x80)
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x5)
    OP_68(2700, 5100, 3350, 0)
    MoveCamera(52, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18200, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(17700, 2000)
    Sleep(500)
    Sound(100, 0, 100, 0)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x8)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_6F(0x79)
    OP_68(3000, 5100, -8000, 3000)
    SetCameraDistance(18000, 3000)
    OP_6F(0x79)
    Sleep(1500)
    Fade(500)
    OP_68(2700, 5100, 3350, 0)
    MoveCamera(52, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_0D()

    #C0084
    ChrTalk(
        0x101,
        (
            "#00002F#5P（琪雅……\x01",
            "  原来在这种地方啊。）\x02\x03",

            "#00006F（……看来我们的确让她\x01",
            "  有些担心了呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x101, 2640, 4100, 4150, 180)
    SetMapObjFlags(0x0, 0x10)
    SetScenarioFlags(0x144, 4)
    EventEnd(0x5)
    Return()

    # Function_13_2AC7 end

    def Function_14_2C5E(): pass

    label("Function_14_2C5E")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_64(0xB)
    LoadChrToIndex("chr/ch02710.itc", 0x1E)
    LoadChrToIndex("chr/ch02702.itc", 0x1F)
    LoadChrToIndex("apl/ch51302.itc", 0x20)
    LoadChrToIndex("apl/ch51355.itc", 0x21)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01103.itp")
    SoundLoad(3611)
    SoundLoad(3612)
    OP_4B(0xB, 0xFF)
    SetChrPos(0x101, 3000, 4100, -6800, 180)
    SetChrPos(0x102, 0, 4100, 2000, 180)
    SetChrPos(0x103, 3550, 4100, 0, 180)
    SetChrPos(0x104, 3550, 4100, 4000, 180)
    SetChrPos(0x109, 0, 4100, 3200, 180)
    SetChrPos(0x105, 0, 4100, 4400, 180)
    SetChrPos(0x9, 0, 4100, 0, 180)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x1)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0x8, 0x8)
    OP_68(3000, 5100, -7400, 0)
    MoveCamera(135, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(17500, 2000)
    OP_6F(0x79)
    OP_0D()

    #C0085
    ChrTalk(
        0xB,
        "#01108F#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        "#00002F#6P琪雅，你在这里啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0xB, 0x0, 0x1F4)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #A0087
    AnonymousTalk(
        0xB,
        (
            "#3611V#40W啊……罗伊德……\x02\x03",

            "#3612V#30W嘿嘿嘿……\x01",
            "好像快到了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE1C)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0088
    ChrTalk(
        0x101,
        (
            "#00004F#6P嗯，马上就到了。\x02\x03",

            "#00000F到时可要在那里的\x01",
            "主题公园玩个够哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xB,
        (
            "#01102F#11P嗯！\x02\x03",

            "#01122F……嘿嘿嘿…………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0090
    ChrTalk(
        0x101,
        (
            "#00006F#6P……抱歉，琪雅。\x02\x03",

            "#00008F最近好像让你\x01",
            "感到很寂寞吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xB,
        (
            "#01121F#11P……没有啊，\x01",
            "我完全没事的。\x02\x03",

            "#01106F虽然不知道发生了什么……\x01",
            "但还是可以感觉到\x01",
            "大家都很消沉……\x02\x03",

            "#01108F我很想给大家鼓劲，\x01",
            "让大家恢复精神……\x02\x03",

            "但最后却什么都做不到……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(17200, 750)
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_6F(0x79)
    Fade(250)
    BeginChrThread(0x101, 3, 0, 23)
    BeginChrThread(0xB, 3, 0, 24)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xB, 3)
    OP_0D()

    #C0092
    ChrTalk(
        0xB,
        "#01105F#11P啊……\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#00004F#6P你做得已经非常好啦。\x02\x03",

            "#00002F琪雅只要陪伴在我们身边……\x02\x03",

            "就能给我们带来\x01",
            "无穷的力量与活力。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xB,
        (
            "#01105F#11P真的吗……？\x02\x03",

            "#01108F……真的是这样么……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        "#00005F#6P……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0x101, 0x514, 0x2, 0x2, 0x1)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_9B(0x1, 0x101, 0x0, 0xFFFFFF06, 0x1F4, 0x0)

    #C0096
    ChrTalk(
        0xB,
        (
            "#01109F#11P……嘿嘿嘿，\x01",
            "有点不明白呢。\x02\x03",

            "#01105F啊，不过大家好像\x01",
            "都恢复一些精神了。\x02\x03",

            "#01104F嘿嘿嘿，\x01",
            "罗伊德果然很棒。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#00012F#6P不不，那并不是\x01",
            "因为我啦……\x02\x03",

            "#00002F总之，难得来玩一次，\x01",
            "一定要和大家一起尽兴享受啊。\x02\x03",

            "琪雅也很期待\x01",
            "主题公园吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xB, 0x4B0, 0x4, 0x8, 0x9, 0x8, 0x3)

    #C0098
    ChrTalk(
        0xB,
        "#01109F#11P嗯！\x02",
    )

    CloseMessageWindow()
    OP_A1(0xB, 0x4B0, 0x6, 0xB, 0xC, 0xD, 0xE, 0xD, 0xC)

    #C0099
    ChrTalk(
        0xB,
        (
            "#01110F#11P我想去坐摩天轮！\x02\x03",

            "然后还要和缇欧\x01",
            "一起去『踢咪西』～！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        (
            "#00011F#6P『踢咪西』……\x01",
            "好像是在小孩子间很流行的游戏吧？\x02\x03",

            "#00012F唔……不过缇欧好像\x01",
            "稍微有点超龄了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0101
    ChrTalk(
        0x103,
        (
            "#00211F#6P#N不要随便议论女性的年龄，\x01",
            "这可是基本礼仪哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0xB, 0x5DC, 0x2, 0xC, 0xF)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x2)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(3000, 4800, -5400, 0)
    OP_68(3000, 4800, -7400, 6000)
    MoveCamera(150, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20350, 0)
    ClearChrFlags(0x9, 0x800)
    BeginChrThread(0x101, 3, 0, 21)
    BeginChrThread(0xB, 3, 0, 22)
    BeginChrThread(0x103, 3, 0, 15)
    BeginChrThread(0x9, 3, 0, 16)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 17)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 18)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 19)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 20)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0x102, 3)

    #C0102
    ChrTalk(
        0x101,
        "#00005F#5P缇欧，还有大家……\x02",
    )

    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)
    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xB,
        "#01105F#11P哎，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        "#01200F#11P嗷。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x102,
        (
            "#00109F#12P呵呵，大家都不由自主地\x01",
            "聚集到这里了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x105,
        (
            "#10302F#12P而且差不多\x01",
            "也快到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        "#00002F#5P啊，是吗？\x02",
    )

    CloseMessageWindow()

    def lambda_3595():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3595)
    Sleep(50)

    def lambda_35A5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_35A5)
    Sleep(50)

    def lambda_35B5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_35B5)
    Sleep(50)

    def lambda_35C5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_35C5)
    Sleep(50)

    def lambda_35D5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_35D5)
    Sleep(50)

    def lambda_35E5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_35E5)
    Sleep(50)

    def lambda_35F5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_35F5)
    Sleep(50)
    SetChrFlags(0x9, 0x20)

    def lambda_360A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_360A)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0x9, 2)
    Sleep(200)
    Fade(500)
    OP_68(3000, 4800, -7400, 0)
    MoveCamera(159, 0, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(47500, 0)
    OP_93(0x101, 0xE1, 0x0)
    OP_93(0x102, 0xE1, 0x0)
    OP_93(0x103, 0xE1, 0x0)
    OP_93(0x104, 0xE1, 0x0)
    OP_93(0x109, 0xE1, 0x0)
    OP_93(0x105, 0xE1, 0x0)
    OP_93(0xB, 0xE1, 0x0)
    OP_93(0x9, 0xE1, 0x0)
    OP_68(0, 7800, -25000, 6000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    #Sound(3029, 255, 100, 0)    #voice#KeA
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0108
    ChrTalk(
        0xB,
        "#01109F#6P#N#4S哇～啊……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xBD9)

    #C0109
    ChrTalk(
        0x102,
        "#00102F#6P#N好漂亮啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0110
    ChrTalk(
        0x109,
        "#10109F#6P#N今天是大晴天，最适合游玩了！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0111
    ChrTalk(
        0x104,
        (
            "#00309F#6P#N好，让我们拿出\x01",
            "最大热情吧～！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(479, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_68(0, 7800, -26000, 2000)
    OP_6F(0x79)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_2C5E end

    def Function_15_37AA(): pass

    label("Function_15_37AA")

    OP_9B(0x0, 0xFE, 0x0, 0x15E0, 0x898, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_15_37AA end

    def Function_16_37C1(): pass

    label("Function_16_37C1")

    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x898, 0x1)
    SetChrFlags(0xFE, 0x800)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x898, 0x1)
    ClearChrFlags(0xFE, 0x800)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x898, 0x1)
    SetChrFlags(0xFE, 0x800)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x898, 0x1)
    ClearChrFlags(0xFE, 0x800)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x898, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x7D0, 0x898, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 1, 0, 0)
    TurnDirection(0xFE, 0xB, 500)
    Return()

    # Function_16_37C1 end

    def Function_17_3845(): pass

    label("Function_17_3845")

    OP_9B(0x0, 0xFE, 0x0, 0x1D4C, 0x898, 0x1)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x7D0, 0x898, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_17_3845 end

    def Function_18_386B(): pass

    label("Function_18_386B")

    OP_9B(0x0, 0xFE, 0x0, 0x2008, 0x898, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_18_386B end

    def Function_19_3882(): pass

    label("Function_19_3882")

    OP_9B(0x0, 0xFE, 0x0, 0x21FC, 0x898, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x320, 0x898, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_19_3882 end

    def Function_20_38A8(): pass

    label("Function_20_38A8")

    OP_9B(0x0, 0xFE, 0x0, 0x238C, 0x898, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x640, 0x898, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    TurnDirection(0xFE, 0xB, 500)
    Return()

    # Function_20_38A8 end

    def Function_21_38D5(): pass

    label("Function_21_38D5")

    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_21_38D5 end

    def Function_22_38E7(): pass

    label("Function_22_38E7")

    Sleep(1000)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_22_38E7 end

    def Function_23_38F2(): pass

    label("Function_23_38F2")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x20)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    OP_A1(0xFE, 0x3E8, 0x6, 0x4, 0x5, 0x6, 0x5, 0x4, 0x3)
    Return()

    # Function_23_38F2 end

    def Function_24_3911(): pass

    label("Function_24_3911")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x21)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    OP_A1(0xFE, 0x3E8, 0x6, 0x4, 0x5, 0x6, 0x5, 0x4, 0x3)
    Return()

    # Function_24_3911 end

    def Function_25_3930(): pass

    label("Function_25_3930")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0x101, 2500, 4100, -8000, 180)
    SetChrPos(0xB, 3500, 4100, -8000, 180)
    OP_68(0, 5100, -18500, 0)
    MoveCamera(35, 3, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(25000, 0)
    OP_68(0, 2100, 18000, 15000)
    MoveCamera(40, 30, 0, 15000)
    SetCameraDistance(25000, 15000)
    FadeToBright(1000, 0)
    Sound(479, 2, 10, 0)
    Sleep(100)
    OP_25(0x1DF, 0x14)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x64)
    OP_0D()
    Sleep(8000)
    StopSound(479, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("e0510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_3930 end

    def Function_26_3A43(): pass

    label("Function_26_3A43")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    LoadChrToIndex("chr/ch05500.itc", 0x1E)
    SoundLoad(3802)
    SoundLoad(3775)
    SoundLoad(3776)
    SoundLoad(3777)
    SoundLoad(3778)
    SoundLoad(3779)
    SoundLoad(3619)
    SoundLoad(3620)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis407.itp")
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0x101, 2500, 4100, -8000, 180)
    SetChrPos(0xB, 3500, 4100, -8000, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 0, 4100, 1000, 180)
    SetChrFlags(0xE, 0x8)
    ClearMapObjFlags(0x0, 0x10)
    OP_68(3160, 5100, -6140, 0)
    MoveCamera(145, 29, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20900, 0)
    FadeToBright(1000, 0)
    OP_68(3160, 5100, -8140, 3000)
    Sleep(2500)
    OP_63(0xB, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    #C0112
    ChrTalk(
        0xB,
        "#01104F#3619V#5P#30W#15A啦啦啦¤\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    TurnDirection(0x101, 0xB, 500)
    Sleep(150)

    #C0113
    ChrTalk(
        0x101,
        (
            "#00012F#12P哈哈……\x01",
            "琪雅，你的心情不错啊。\x02\x03",

            "#00002F虽然发生了不少事情……\x01",
            "不过玩得还算开心吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    #C0114
    ChrTalk(
        0xB,
        (
            "#01109F#5P嗯！\x02\x03",

            "#01110F以后还想和大家\x01",
            "一起出去玩！\x02\x03",

            "下次就去阿尔摩利卡村吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#00002F#12P哈哈，这提议不错啊。\x02\x03",

            "#00004F（……从她昨天的样子来看，\x01",
            "  还以为会有什么事……）\x02\x03",

            "（不过她现在已经完全恢复精神了，\x01",
            "  应该不必太担心吧？）\x02\x03",

            "#00008F（现在更需要担心的，\x01",
            "  恐怕还是『结社』的动向……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0116
    ChrTalk(
        0xB,
        (
            "#01105F#5P嗯？\x01",
            "罗伊德，怎么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#00012F#12P啊，没什么。\x02\x03",

            "#00008F……对了，琪雅。\x01",
            "昨天夜里，你真的没有\x01",
            "见到过奇怪的人吗？\x02\x03",

            "#00001F比如说，穿着粉色衣服的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xB,
        (
            "#01112F#5P嗯……\x01",
            "没有印象呢。\x02\x03",

            "#01106F不过我好像梦游了，\x01",
            "所以也不是很确定。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#00000F#12P是吗……\x01",
            "嗯，那就算啦。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_3ED8")
    OP_C9(0x0, 0x80000000)

    #N0120
    NpcTalk(
        0xE,
        "玛丽亚贝尔的声音",
        "#3802V#2P#30W啊，原来你们在这里啊。\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Jump("loc_3F02")

    label("loc_3ED8")


    #N0121
    NpcTalk(
        0xE,
        "女孩的声音",
        "#2P啊，原来你们在这里啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3F02")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(2000, 5100, -7500, 4000)
    MoveCamera(147, 22, 0, 4000)

    def lambda_3F4A():

        label("loc_3F4A")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_3F4A")

    QueueWorkItem2(0x101, 2, lambda_3F4A)

    def lambda_3F5C():

        label("loc_3F5C")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_3F5C")

    QueueWorkItem2(0xB, 2, lambda_3F5C)
    BeginChrThread(0xE, 3, 0, 27)
    WaitChrThread(0xE, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0xB, 0x2)
    OP_6F(0x79)

    #C0122
    ChrTalk(
        0xB,
        "#01110F#5P啊，是贝尔。\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#00002F#5P玛丽亚贝尔小姐，\x01",
            "这次真是麻烦你了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_40B3")

    #C0124
    ChrTalk(
        0xE,
        (
            "#02902F#12P呵呵，没什么。\x01",
            "各位倒是辛苦了。\x02\x03",

            "#02906F话说回来，是叫『结社』吧？\x01",
            "竟然还存在那种肆意妄为的家伙。\x02\x03",

            "#02903F当时偷走我人偶的那个家伙\x01",
            "也是他们的一员！\x02\x03",

            "#02910F今后必须要彻底\x01",
            "整改保安部的警备体制……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4159")

    label("loc_40B3")


    #C0125
    ChrTalk(
        0xE,
        (
            "#02902F#12P呵呵，麻烦的人\x01",
            "应该是你们才对吧？\x02\x03",

            "#02906F话说回来，是叫『结社』吧？\x01",
            "竟然还存在那种肆意妄为的家伙。\x02\x03",

            "#02901F今后必须要彻底\x01",
            "整改保安部的警备体制……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4159")


    #C0126
    ChrTalk(
        0x101,
        (
            "#00012F#5P是、是啊……\x02\x03",

            "#00008F（但那些家伙恐怕不是\x01",
            "  民间警备员可以应付的……）\x02\x03",

            "#00013F（……还是要靠我们\x01",
            "  多加注意啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xE,
        (
            "#02904F#12P好啦，先不说这些了。\x02\x03",

            "#02900F罗伊德警官、琪雅……\x02\x03",

            "我突然有个想法，\x01",
            "大家要不要拍张纪念合影呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0128
    ChrTalk(
        0x101,
        "#00002F#5P啊，好啊！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)
    Sleep(100)

    #C0129
    ChrTalk(
        0xB,
        (
            "#01105F#5P那个……纪念合影？\x01",
            "就是上次那种大家一起拍的照片吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 500)
    Sleep(100)

    #C0130
    ChrTalk(
        0x101,
        (
            "#00004F#11P嗯，可以把与大家在一起\x01",
            "的珍贵回忆留存在照片上。\x02\x03",

            "#00000F以后只要看看照片，随时都可以\x01",
            "回想起我们这次的假期。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0131
    ChrTalk(
        0xB,
        "#01107F#4S#5P嗯！我要照！\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xE,
        (
            "#02909F#12P那就这么定啦。\x02\x03",

            "#02905F既然如此……\x01",
            "甲板应该比船舱内更适合拍照吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)

    #C0133
    ChrTalk(
        0x101,
        (
            "#00009F#5P是啊，难得有\x01",
            "这么好的天气。\x02\x03",

            "#00002F我去把大家叫来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xE,
        (
            "#02904F#12P嗯，拜托啦。\x02\x03",

            "#02902F顺便再和船内的\x01",
            "导游小姐说一声吧。\x02\x03",

            "她应该会马上过来\x01",
            "帮我们拍照的。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        "#00000F#5P知道了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x19, 0x1F4)
    OP_68(3000, 5100, 0, 5000)
    MoveCamera(30, 25, 0, 5000)
    OP_6E(400, 5000)
    SetCameraDistance(22000, 5000)
    BeginChrThread(0x101, 3, 0, 28)

    def lambda_4509():

        label("loc_4509")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4509")

    QueueWorkItem2(0xB, 2, lambda_4509)

    def lambda_451B():
        OP_93(0xFE, 0xA, 0x12C)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_451B)
    Sleep(1500)
    SetMessageWindowPos(250, 180, -1, -1)
    OP_C9(0x0, 0x80000000)

    #C0136
    ChrTalk(
        0xB,
        "#01105F#3620V#30W#10A#11P#N啊──\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    WaitChrThread(0x101, 3)
    EndChrThread(0xB, 0x2)
    EndChrThread(0xE, 0x2)
    OP_6F(0x79)
    StopBGM(0x1770)

    #C0137
    ChrTalk(
        0xB,
        "#01112F#40W#12P#N…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0138
    ChrTalk(
        0xE,
        (
            "#02913F#3775V#12P#30W#N呵呵……\x02\x03",

            "#3776V不想让重要的人们\x01",
            "过度担心。\x02\x03",

            "#02902F#3777V当个好女孩很辛苦吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xEC1)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()

    #C0139
    ChrTalk(
        0xB,
        "#01105F#12P#N！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    TurnDirection(0xB, 0xE, 0)
    OP_68(2000, 5100, -7500, 0)
    MoveCamera(300, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetCameraDistance(22000, 1500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    TurnDirection(0xE, 0xB, 350)
    OP_6F(0x79)
    CancelBlur(0)
    SetCameraDistance(21000, 20000)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #C0140
    ChrTalk(
        0xE,
        (
            "#02913F#3778V#5P#40W#30A你好像有什么烦恼吧？\x02\x03",

            "#02912F#3779V#35A如果愿意，\x01",
            "我说不定可以帮上你的忙哦。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_24(0xEC3)
    OP_C9(0x1, 0x80000000)
    StopSound(479, 3000, 80)
    FadeToDark(2000, 0, -1)
    SetCameraDistance(20700, 2000)
    OP_6F(0x79)
    OP_0D()
    WaitBGM()
    Sleep(2500)
    OP_29(0xA5, 0x1, 0xD)
    OP_29(0xA5, 0x4, 0x10)
    OP_32(0xFF, 0xFE, 0x0)
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E5(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_E0(0x1F, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C9(0x0, 0x10)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x25, 0)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x99), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x25, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x1, 0x10)
    OP_E5(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("e4600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_26_3A43 end

    def Function_27_482D(): pass

    label("Function_27_482D")

    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x5DC, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xB, 0)
    Return()

    # Function_27_482D end

    def Function_28_4853(): pass

    label("Function_28_4853")

    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFE7, 0x1F40, 0x7D0, 0x1)
    OP_96(0xFE, 0xA50, 0x1004, 0x11C6, 0x7D0, 0x0)
    Sound(100, 0, 100, 0)
    OP_70(0x0, 0x5)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x0)

    def lambda_48A3():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_48A3)
    Sleep(300)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0xFE, 1)
    Sound(100, 0, 100, 0)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x0)
    SetChrPos(0x101, 0, 0, 0, 0)
    Return()

    # Function_28_4853 end

    SaveToFile()

Try(main)
