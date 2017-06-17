from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t102b.bin",                # FileName
        "t102b",                    # MapName
        "t102b",                    # Location
        0x0095,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 149, 0, 2, 0, 3],
    )

    BuildStringList((
        "t102b",                  # 0
        "芙兰",                   # 1
        "塞茜尔",                 # 2
        "伊莉娅",                 # 3
        "莉夏",                   # 4
        "修利",                   # 5
        "蔡特",                   # 6
        "艾丽洁",                 # 7
        "游客",                   # 8
        "游客",                   # 9
        "游客",                   # 10
        "SE控制",                 # 11
    ))

    AddCharChip((
        "chr/ch02702.itc",                   # 00
        "chr/ch08500.itc",                   # 01
        "chr/ch05200.itc",                   # 02
        "chr/ch05100.itc",                   # 03
        "chr/ch07500.itc",                   # 04
        "chr/ch10000.itc",                   # 05
        "chr/ch33200.itc",                   # 06
        "chr/ch21600.itc",                   # 07
        "chr/ch20100.itc",                   # 08
        "chr/ch32300.itc",                   # 09
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

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-24909,  0,       5570,    90,   389,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(98589,   0,       20659,   225,  389,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(97339,   0,       19579,   45,   389,  0x0, 0,   8,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       500,     0,    385,  0x0, 0,   9,   0,   0,   1,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(27760,   0,       9640,    1200,    27760,   1500,    9640,    0x007C, 0,  22, 0x0000)
    DeclActor(96820,   0,       -30,     1200,    96820,   1500,    -30,     0x007C, 0,  23, 0x0000)

    ChipFrameInfo(748, 0)                                        # 0

    ScpFunction((
        "Function_0_2EC",          # 00, 0
        "Function_1_3A4",          # 01, 1
        "Function_2_3CF",          # 02, 2
        "Function_3_513",          # 03, 3
        "Function_4_55F",          # 04, 4
        "Function_5_6EB",          # 05, 5
        "Function_6_9AF",          # 06, 6
        "Function_7_B38",          # 07, 7
        "Function_8_CD0",          # 08, 8
        "Function_9_DDB",          # 09, 9
        "Function_10_EF0",         # 0A, 10
        "Function_11_F85",         # 0B, 11
        "Function_12_1002",        # 0C, 12
        "Function_13_107F",        # 0D, 13
        "Function_14_1183",        # 0E, 14
        "Function_15_1BCB",        # 0F, 15
        "Function_16_1BE7",        # 10, 16
        "Function_17_1C72",        # 11, 17
        "Function_18_1C8E",        # 12, 18
        "Function_19_1D0A",        # 13, 19
        "Function_20_1D38",        # 14, 20
        "Function_21_1D8A",        # 15, 21
        "Function_22_1F0F",        # 16, 22
        "Function_23_1F72",        # 17, 23
        "Function_24_1FA4",        # 18, 24
    ))


    def Function_0_2EC(): pass

    label("Function_0_2EC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_32C"),
        (1, "loc_338"),
        (2, "loc_344"),
        (3, "loc_350"),
        (4, "loc_35C"),
        (5, "loc_368"),
        (6, "loc_374"),
        (SWITCH_DEFAULT, "loc_380"),
    )


    label("loc_32C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_338")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_344")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_350")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_35C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_368")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_374")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_380")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_38C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_3A3")

    Return()

    # Function_0_2EC end

    def Function_1_3A4(): pass

    label("Function_1_3A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CE")
    OP_94(0xFE, 0xFFFFF542, 0x60E, 0xABE, 0xFFFFFE3E, 0x3E8)
    Sleep(300)
    Jump("Function_1_3A4")

    label("loc_3CE")

    Return()

    # Function_1_3A4 end

    def Function_2_3CF(): pass

    label("Function_2_3CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_461")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 101660, 0, 21040, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 102720, 0, 19670, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 98850, 0, 20700, 270)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 97500, 0, 21100, 135)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 97890, 0, 19530, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 101520, 0, 18870, 0)
    Jump("loc_4EA")

    label("loc_461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_46F")
    Jump("loc_4EA")

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_49B")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_4EA")

    label("loc_49B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_4A9")
    Jump("loc_4EA")

    label("loc_4A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_4B7")
    Jump("loc_4EA")

    label("loc_4B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4C5")
    Jump("loc_4EA")

    label("loc_4C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_4D3")
    Jump("loc_4EA")

    label("loc_4D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_4E1")
    Jump("loc_4EA")

    label("loc_4E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_4EA")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_4FE")
    ClearScenarioFlags(0x22, 0)
    Event(0, 14)
    Jump("loc_512")

    label("loc_4FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_512")
    ClearScenarioFlags(0x22, 1)
    SetMapFlags(0x10000000)
    Event(0, 20)

    label("loc_512")

    Return()

    # Function_2_3CF end

    def Function_3_513(): pass

    label("Function_3_513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52A")
    OP_7D(0xAA, 0xAA, 0xFF, 0x0, 0x0)

    label("loc_52A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53D")
    OP_1B(0x6, 0x0, 0x15)

    label("loc_53D")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55E")
    ClearMapObjFlags(0x5, 0x10)
    OP_1B(0x8, 0x0, 0x18)
    OP_66(0x1, 0x1)

    label("loc_55E")

    Return()

    # Function_3_513 end

    def Function_4_55F(): pass

    label("Function_4_55F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_688")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60D")

    #C0001
    ChrTalk(
        0x8,
        (
            "#06406F小琪雅\x01",
            "一个人进\x01",
            "主题公园了吗……\x02\x03",

            "#06401F总、总之，如果遇到什么情况，\x01",
            "请立刻和我联络哦。\x02\x03",

            "如果情势需要，\x01",
            "我会请求警察总部提供支援！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_683")

    label("loc_60D")


    #C0002
    ChrTalk(
        0x8,
        (
            "#06406F小琪雅……在如此深夜里\x01",
            "一个人乱跑，不会有事吧……\x02\x03",

            "#06401F总、总之，如果遇到什么情况，\x01",
            "请立刻和我联络哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_683")

    Jump("loc_6E7")

    label("loc_688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_696")
    Jump("loc_6E7")

    label("loc_696")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_6A4")
    Jump("loc_6E7")

    label("loc_6A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_6B4")
    Jump("loc_6E7")

    label("loc_6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_6C2")
    Jump("loc_6E7")

    label("loc_6C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_6D0")
    Jump("loc_6E7")

    label("loc_6D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_6DE")
    Jump("loc_6E7")

    label("loc_6DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_6E7")

    label("loc_6E7")

    TalkEnd(0xFE)
    Return()

    # Function_4_55F end

    def Function_5_6EB(): pass

    label("Function_5_6EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_95C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_701")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_957")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "请求治疗\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_876")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_806")

    #C0003
    ChrTalk(
        0x9,
        (
            "#05900F如果遇到什么问题，\x01",
            "请立刻和我说。\x02\x03",

            "#05903F我带着急救箱，\x01",
            "处理一般的伤势\x01",
            "还是没有问题的。\x02\x03",

            "#05901F罗伊德，还有大家，\x01",
            "请一定要多加小心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_871")

    label("loc_806")


    #C0004
    ChrTalk(
        0x9,
        (
            "#05903F我带着急救箱，\x01",
            "处理一般的伤势\x01",
            "还是没有问题的。\x02\x03",

            "#05901F罗伊德，还有大家，\x01",
            "请一定要多加小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_871")

    Jump("loc_952")

    label("loc_876")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0005
    ChrTalk(
        0x9,
        (
            "#05900F需要治疗吗？\x01",
            "知道啦，交给我吧。\x02",
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
    FadeToBright(1000, 0)
    OP_0D()

    #C0006
    ChrTalk(
        0x9,
        (
            "#05900F嗯，这样就没问题了。\x01",
            "……一定要多加小心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_952")

    label("loc_92B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93F")
    Jump("loc_952")

    label("loc_93F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_952")
    TalkEnd(0x9)
    Return()

    label("loc_952")

    Jump("loc_701")

    label("loc_957")

    Jump("loc_9AB")

    label("loc_95C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_96A")
    Jump("loc_9AB")

    label("loc_96A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_978")
    Jump("loc_9AB")

    label("loc_978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_986")
    Jump("loc_9AB")

    label("loc_986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_994")
    Jump("loc_9AB")

    label("loc_994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_9A2")
    Jump("loc_9AB")

    label("loc_9A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_9AB")

    label("loc_9AB")

    TalkEnd(0xFE)
    Return()

    # Function_5_6EB end

    def Function_6_9AF(): pass

    label("Function_6_9AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_AE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A78")

    #C0007
    ChrTalk(
        0xA,
        (
            "#01700F我们如果跟过去，也许会成为累赘，\x01",
            "还是在这里等你们吧。\x02\x03",

            "#01703F看到蔡特的样子，\x01",
            "总有种不好的预感……\x02\x03",

            "#01702F警察弟弟，\x01",
            "赶快找到那孩子吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        "#00001F是……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_AE0")

    label("loc_A78")


    #C0009
    ChrTalk(
        0xA,
        (
            "#01703F我们如果跟过去，也许会成为累赘，\x01",
            "还是在这里等你们吧。\x02\x03",

            "#01701F警察弟弟，\x01",
            "赶快找到那孩子吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE0")

    Jump("loc_B34")

    label("loc_AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_AF3")
    Jump("loc_B34")

    label("loc_AF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_B01")
    Jump("loc_B34")

    label("loc_B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_B0F")
    Jump("loc_B34")

    label("loc_B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_B1D")
    Jump("loc_B34")

    label("loc_B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_B2B")
    Jump("loc_B34")

    label("loc_B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_B34")

    label("loc_B34")

    TalkEnd(0xFE)
    Return()

    # Function_6_9AF end

    def Function_7_B38(): pass

    label("Function_7_B38")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_C6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C0F")

    #C0010
    ChrTalk(
        0xB,
        "#01803F（……这股气息，莫非是……）\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        "#00005F……莉夏？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xB,
        (
            "#01808F……不，没什么。\x02\x03",

            "#01803F不过，任何情况都有可能发生。\x01",
            "大家务必做好\x01",
            "充分的准备。\x02\x03",

            "#01801F各位，一定要小心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_C69")

    label("loc_C0F")


    #C0013
    ChrTalk(
        0xB,
        (
            "#01803F任何情况都有可能发生。\x01",
            "大家务必做好\x01",
            "充分的准备。\x02\x03",

            "#01801F各位，一定要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C69")

    Jump("loc_CCC")

    label("loc_C6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_C7C")
    Jump("loc_CCC")

    label("loc_C7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_C8A")
    Jump("loc_CCC")

    label("loc_C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_CA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA2")
    Jump("loc_CA2")

    label("loc_CA2")

    Jump("loc_CCC")

    label("loc_CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_CB5")
    Jump("loc_CCC")

    label("loc_CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_CC3")
    Jump("loc_CCC")

    label("loc_CC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_CCC")

    label("loc_CCC")

    TalkEnd(0xFE)
    Return()

    # Function_7_B38 end

    def Function_8_CD0(): pass

    label("Function_8_CD0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_D88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4F")

    #C0014
    ChrTalk(
        0xC,
        (
            "#04206F那个小鬼头，如果是梦游乱跑，\x01",
            "未免也太夸张了吧？\x02\x03",

            "#04201F她到底跑到什么地方去了……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_D83")

    label("loc_D4F")


    #C0015
    ChrTalk(
        0xC,
        (
            "#04201F那个小鬼头，\x01",
            "到底跑到什么地方去了……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D83")

    Jump("loc_DD7")

    label("loc_D88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_D96")
    Jump("loc_DD7")

    label("loc_D96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_DA4")
    Jump("loc_DD7")

    label("loc_DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_DB2")
    Jump("loc_DD7")

    label("loc_DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_DC0")
    Jump("loc_DD7")

    label("loc_DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_DCE")
    Jump("loc_DD7")

    label("loc_DCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_DD7")

    label("loc_DD7")

    TalkEnd(0xFE)
    Return()

    # Function_8_CD0 end

    def Function_9_DDB(): pass

    label("Function_9_DDB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_E8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6D")

    #C0016
    ChrTalk(
        0xD,
        "#01201F……咕呜呜呜……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        (
            "#00201F……蔡特似乎保持着\x01",
            "相当高的警戒。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#00001F嗯……我们也要时刻保持警惕。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_E8A")

    label("loc_E6D")


    #C0019
    ChrTalk(
        0xD,
        "#01201F……咕呜呜呜……\x02",
    )

    CloseMessageWindow()

    label("loc_E8A")

    Jump("loc_EEC")

    label("loc_E8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_E9D")
    Jump("loc_EEC")

    label("loc_E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_EAB")
    Jump("loc_EEC")

    label("loc_EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_EB9")
    Jump("loc_EEC")

    label("loc_EB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_EC7")
    Jump("loc_EEC")

    label("loc_EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_ED5")
    Jump("loc_EEC")

    label("loc_ED5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_EE3")
    Jump("loc_EEC")

    label("loc_EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_EEC")

    label("loc_EEC")

    TalkEnd(0xFE)
    Return()

    # Function_9_DDB end

    def Function_10_EF0(): pass

    label("Function_10_EF0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_F5C")

    #C0020
    ChrTalk(
        0xE,
        (
            "我今天也在珠宝店\x01",
            "买了很多首饰呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xE,
        (
            "呵呵呵……\x01",
            "缓解压力的最佳手段\x01",
            "果然还是购物啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F81")

    label("loc_F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_F6A")
    Jump("loc_F81")

    label("loc_F6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_F78")
    Jump("loc_F81")

    label("loc_F78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_F81")

    label("loc_F81")

    TalkEnd(0xFE)
    Return()

    # Function_10_EF0 end

    def Function_11_F85(): pass

    label("Function_11_F85")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_FD9")

    #C0022
    ChrTalk(
        0xF,
        (
            "哦，主题公园里\x01",
            "好像正在放烟花呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xF,
        "老婆子，我们去看看吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_FFE")

    label("loc_FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_FE7")
    Jump("loc_FFE")

    label("loc_FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_FF5")
    Jump("loc_FFE")

    label("loc_FF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_FFE")

    label("loc_FFE")

    TalkEnd(0xFE)
    Return()

    # Function_11_F85 end

    def Function_12_1002(): pass

    label("Function_12_1002")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1056")

    #C0024
    ChrTalk(
        0x10,
        (
            "嗯，那是一定\x01",
            "要去看的。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x10,
        "呵呵，肯定能留下很美好的回忆呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_107B")

    label("loc_1056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1064")
    Jump("loc_107B")

    label("loc_1064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1072")
    Jump("loc_107B")

    label("loc_1072")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_107B")

    label("loc_107B")

    TalkEnd(0xFE)
    Return()

    # Function_12_1002 end

    def Function_13_107F(): pass

    label("Function_13_107F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_115A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FA")

    #C0026
    ChrTalk(
        0x11,
        (
            "彩、彩虹剧团的\x01",
            "伊莉娅刚刚\x01",
            "从这里过去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x11,
        (
            "我、我应该没看错。\x01",
            "她竟然会来米修拉姆……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1155")

    label("loc_10FA")


    #C0028
    ChrTalk(
        0x11,
        (
            "伊莉娅·普拉提耶\x01",
            "刚刚从这里\x01",
            "经过。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x11,
        (
            "……啊啊！真是的！\x01",
            "当时要是和她握个手就好了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1155")

    Jump("loc_117F")

    label("loc_115A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1168")
    Jump("loc_117F")

    label("loc_1168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1176")
    Jump("loc_117F")

    label("loc_1176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_117F")

    label("loc_117F")

    TalkEnd(0xFE)
    Return()

    # Function_13_107F end

    def Function_14_1183(): pass

    label("Function_14_1183")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02751.itc", 0x1E)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x20)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xD, 0, 0, 15)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 0, 0, 0, 0)
    SetChrPos(0x102, 0, 0, 0, 0)
    SetChrPos(0x103, 0, 0, 0, 0)
    SetChrPos(0x104, 0, 0, 0, 0)
    SetChrPos(0x109, 0, 0, 0, 0)
    SetChrPos(0x105, 0, 0, 0, 0)
    SetChrPos(0x8, 0, 0, 0, 0)
    SetChrPos(0xB, 0, 0, 0, 0)
    SetChrPos(0xA, 0, 0, 0, 0)
    SetChrPos(0x9, 0, 0, 0, 0)
    SetChrPos(0xC, 0, 0, 0, 0)
    SetChrPos(0xD, 0, 0, 0, 0)
    OP_68(95850, 100, -10550, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    OP_68(95200, 1200, -9050, 6000)
    MoveCamera(330, 10, 0, 6000)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    OP_52(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    BeginChrThread(0x12, 1, 0, 18)
    BeginChrThread(0xD, 3, 0, 16)
    Sleep(2000)
    BeginChrThread(0x101, 3, 0, 16)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 16)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 16)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 16)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 16)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 16)
    OP_0D()
    Sleep(800)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xD, 0x3)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    EndChrThread(0xD, 0x2)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_52(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xD, 100000, 0, 7000, 0)
    SetChrPos(0x101, 100000, 0, 7000, 0)
    SetChrPos(0x102, 99500, 0, 6000, 0)
    SetChrPos(0x103, 100500, 0, 6000, 0)
    SetChrPos(0x104, 100000, 0, 5000, 0)
    SetChrPos(0x109, 101000, 0, 4500, 0)
    SetChrPos(0x105, 99000, 0, 4500, 0)
    SetChrPos(0x8, 99000, 0, 7000, 0)
    SetChrPos(0xA, 100000, 0, 7000, 0)
    SetChrPos(0x9, 101000, 0, 7000, 0)
    SetChrPos(0xB, 100500, 0, 6000, 0)
    SetChrPos(0xC, 99500, 0, 6000, 0)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(100000, 1000, 22000, 0)
    OP_68(100110, 1000, 18460, 8000)
    MoveCamera(315, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    FadeToBright(1000, 0)
    BeginChrThread(0x12, 1, 0, 19)
    BeginChrThread(0xD, 3, 0, 17)
    Sleep(2000)

    def lambda_16C8():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16C8)
    Sleep(50)

    def lambda_16E0():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16E0)
    Sleep(50)

    def lambda_16F8():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_16F8)
    Sleep(50)

    def lambda_1710():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1710)
    Sleep(50)

    def lambda_1728():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1728)
    Sleep(50)

    def lambda_1740():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1740)
    Sleep(2000)

    def lambda_1758():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1758)
    Sleep(200)

    def lambda_1770():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1770)
    Sleep(200)

    def lambda_1788():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1788)
    Sleep(200)

    def lambda_17A0():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_17A0)
    Sleep(200)

    def lambda_17B8():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_17B8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xD, 3)
    OP_6F(0x79)
    OP_0D()

    #C0030
    ChrTalk(
        0xD,
        (
            "#01203F#5P……咕呜呜呜………\x02\x03",

            "#01201F咕呜呜……嗷。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x103,
        (
            "#00201F#6P『在那边，\x01",
            "  要小心。』\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xA,
        (
            "#01705F#6P呼……\x01",
            "还好你懂得它的意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        "#00108F#6P不、不过，『要小心』是指……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(100)

    #C0034
    ChrTalk(
        0x101,
        (
            "#00006F#11P……没时间想这些了，\x01",
            "我们赶快过去吧。\x02\x03",

            "#00003F芙兰、塞茜尔姐姐，\x01",
            "还有彩虹剧团的三位……\x02\x03",

            "#00001F请你们在这里\x01",
            "等着我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xC,
        "#04207F#6P可、可是……！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        (
            "#01703F#6P……嗯，这也没办法。\x01",
            "我们也许会成为累赘的。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x9,
        (
            "#05901F#6P不过，万一遇到什么情况，\x01",
            "一定要立刻呼叫我们。\x02\x03",

            "我带着\x01",
            "急救箱呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#00002F#11P嗯，知道了。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xB,
        (
            "#01803F#6P……各位，\x01",
            "一定要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "#06401F#6P如果遇到紧急情况，\x01",
            "请用艾尼格玛联络～！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0xD, 0x0)
    SetChrSubChip(0xD, 0x0)
    OP_49()
    OP_D7(0x1E)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xD, 0x40)
    SetChrPos(0x8, 97000, 0, 20000, 90)
    SetChrPos(0x9, 97000, 0, 19000, 90)
    SetChrPos(0xA, 97000, 0, 18000, 90)
    SetChrPos(0xB, 97000, 0, 17000, 90)
    SetChrPos(0xC, 97000, 0, 16000, 90)
    SetChrPos(0xD, 97000, 0, 15000, 90)
    SetChrPos(0x0, 99620, 0, 22780, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0xD, 101660, 0, 21040, 0)
    SetChrPos(0x8, 102720, 0, 19670, 0)
    SetChrPos(0xB, 98850, 0, 20700, 270)
    SetChrPos(0xA, 97500, 0, 21100, 135)
    SetChrPos(0x9, 97890, 0, 19530, 0)
    SetChrPos(0xC, 101520, 0, 18870, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    BeginChrThread(0xD, 0, 0, 0)
    SetScenarioFlags(0x146, 0)
    OP_29(0xA5, 0x1, 0x9)
    OP_32(0xFF, 0xFF, 0x0)
    OP_1B(0x8, 0x0, 0x18)
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x5, 0x10)
    EventEnd(0x5)
    Return()

    # Function_14_1183 end

    def Function_15_1BCB(): pass

    label("Function_15_1BCB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1BE6")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_15_1BCB")

    label("loc_1BE6")

    Return()

    # Function_15_1BCB end

    def Function_16_1BE7(): pass

    label("Function_16_1BE7")

    SetChrPos(0xFE, 92740, 1900, -9330, 0)

    def lambda_1BFD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1BFD)
    OP_95(0xFE, 92800, 1300, -11030, 4000, 0x1)
    OP_95(0xFE, 94740, 200, -13790, 4000, 0x1)
    OP_95(0xFE, 98460, 100, -13380, 4000, 0x1)
    OP_95(0xFE, 100000, 0, -8700, 4000, 0x1)
    OP_95(0xFE, 100000, 0, 10000, 4000, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_16_1BE7 end

    def Function_17_1C72(): pass

    label("Function_17_1C72")

    OP_9B(0x1, 0xFE, 0xA, 0x32C8, 0xFA0, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_17_1C72 end

    def Function_18_1C8E(): pass

    label("Function_18_1C8E")

    Sound(845, 0, 20, 0)
    Sleep(450)
    Sound(845, 0, 25, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Sleep(450)
    Sound(845, 0, 25, 0)
    Sleep(450)
    Sound(845, 0, 20, 0)
    Sleep(450)
    Sound(845, 0, 15, 0)
    Sleep(450)
    Sound(845, 0, 10, 0)
    Sleep(450)
    Sound(845, 0, 5, 0)
    Return()

    # Function_18_1C8E end

    def Function_19_1D0A(): pass

    label("Function_19_1D0A")

    Sleep(1550)
    Sound(845, 0, 20, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Return()

    # Function_19_1D0A end

    def Function_20_1D38(): pass

    label("Function_20_1D38")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-17890, 1600, 9710, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17250, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -18950, 0, 10980, 180)
    EventEnd(0x5)
    Return()

    # Function_20_1D38 end

    def Function_21_1D8A(): pass

    label("Function_21_1D8A")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1EF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EBB")

    #C0041
    ChrTalk(
        0x101,
        (
            "#00003F湖水浴场在晚间\x01",
            "好像不营业。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_1DF7")

    #C0042
    ChrTalk(
        0x102,
        (
            "#00100F嗯，还是不要\x01",
            "过去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB3")

    label("loc_1DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1E25")

    #C0043
    ChrTalk(
        0x103,
        (
            "#00200F还是不要\x01",
            "过去为好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB3")

    label("loc_1E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_1E4E")

    #C0044
    ChrTalk(
        0x104,
        "#00300F还是别过去了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EB3")

    label("loc_1E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_1E80")

    #C0045
    ChrTalk(
        0x109,
        (
            "#10100F看来还是\x01",
            "别过去为好啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB3")

    label("loc_1E80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_1EB3")

    #C0046
    ChrTalk(
        0x105,
        (
            "#10300F嗯，看来还是\x01",
            "不要过去为好呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EB3")

    SetScenarioFlags(0x1, 1)
    Jump("loc_1EF8")

    label("loc_1EBB")


    #C0047
    ChrTalk(
        0x101,
        (
            "#00003F湖水浴场在晚间\x01",
            "好像不营业。\x01",
            "……还是不要过去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EF8")

    Sleep(50)
    SetChrPos(0x0, 28500, 0, 8080, 270)
    EventEnd(0x4)
    Return()

    # Function_21_1D8A end

    def Function_22_1F0F(): pass

    label("Function_22_1F0F")

    EventBegin(0x2)
    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "湖水浴场的营业时间已结束，\x01",
            "期待您再度光临。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_22_1F0F end

    def Function_23_1F72(): pass

    label("Function_23_1F72")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0049
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上了锁。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_23_1F72 end

    def Function_24_1FA4(): pass

    label("Function_24_1FA4")

    EventBegin(0x1)

    #C0050
    ChrTalk(
        0x101,
        (
            "#00001F已经是深夜了，\x01",
            "我们赶快前往主题公园吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 100200, 0, -4830, 0)
    EventEnd(0x4)
    Return()

    # Function_24_1FA4 end

    SaveToFile()

Try(main)
