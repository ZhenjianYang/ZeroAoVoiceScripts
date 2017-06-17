from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t101b.bin",                # FileName
        "t101b",                    # MapName
        "t101b",                    # Location
        0x0045,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 69, 0, 2, 0, 3],
    )

    BuildStringList((
        "t101b",                  # 0
        "艾米",                   # 1
        "泽鲁",                   # 2
        "卡比兰",                 # 3
        "卢古曼",                 # 4
        "蔡特",                   # 5
        "塞茜尔",                 # 6
        "伊莉娅",                 # 7
        "迎宾馆方向",             # 8
        "翠雀酒店方向",           # 9
    ))

    AddCharChip((
        "chr/ch22300.itc",                   # 00
        "chr/ch22200.itc",                   # 01
        "chr/ch33100.itc",                   # 02
        "chr/ch33000.itc",                   # 03
        "chr/ch02708.itc",                   # 04
        "chr/ch07502.itc",                   # 05
    ))

    DeclNpc(-2750,   -2000,   33099,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-2750,   -2000,   31899,   0,    389,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(26860,   -2000,   2200,    270,  385,  0x0, 0,   2,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(-6929,   -1799,   52110,   45,   389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-3170,   -3799,   -13359,  135,  405,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-1919,   -3700,   -12430,  180,  389,  0x0, 0,   5,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    PlaceName(-5.0, 0.0, 81.0, 0x0000, 0x0000, "迎宾馆方向")
    PlaceName(65.0, 0.0, 0.0, 0x0000, 0x0000, "翠雀酒店方向")

    ChipFrameInfo(456, 0)                                        # 0

    ScpFunction((
        "Function_0_1C8",          # 00, 0
        "Function_1_280",          # 01, 1
        "Function_2_2E1",          # 02, 2
        "Function_3_39E",          # 03, 3
        "Function_4_3C6",          # 04, 4
        "Function_5_44B",          # 05, 5
        "Function_6_4FE",          # 06, 6
        "Function_7_5A3",          # 07, 7
        "Function_8_689",          # 08, 8
        "Function_9_725",          # 09, 9
        "Function_10_8A7",         # 0A, 10
        "Function_11_9F2",         # 0B, 11
    ))


    def Function_0_1C8(): pass

    label("Function_0_1C8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_208"),
        (1, "loc_214"),
        (2, "loc_220"),
        (3, "loc_22C"),
        (4, "loc_238"),
        (5, "loc_244"),
        (6, "loc_250"),
        (SWITCH_DEFAULT, "loc_25C"),
    )


    label("loc_208")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_214")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_220")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_22C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_238")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_244")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_250")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_25C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_268")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_27F")

    Return()

    # Function_0_1C8 end

    def Function_1_280(): pass

    label("Function_1_280")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E0")
    OP_95(0xFE, 26860, -2000, 2200, 2000, 0x0)
    OP_95(0xFE, -4019, -1800, 2200, 2000, 0x0)
    OP_95(0xFE, -3510, -1800, -1500, 2000, 0x0)
    OP_95(0xFE, 26860, -2000, -2060, 2000, 0x0)
    Jump("Function_1_280")

    label("loc_2E0")

    Return()

    # Function_1_280 end

    def Function_2_2E1(): pass

    label("Function_2_2E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_2EF")
    Jump("loc_39D")

    label("loc_2EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_2FD")
    Jump("loc_39D")

    label("loc_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_34E")
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32B")
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)

    label("loc_32B")

    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_39D")

    label("loc_34E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_35C")
    Jump("loc_39D")

    label("loc_35C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_36A")
    Jump("loc_39D")

    label("loc_36A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_378")
    Jump("loc_39D")

    label("loc_378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_386")
    Jump("loc_39D")

    label("loc_386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_394")
    Jump("loc_39D")

    label("loc_394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_39D")

    label("loc_39D")

    Return()

    # Function_2_2E1 end

    def Function_3_39E(): pass

    label("Function_3_39E")

    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(126, 1, 80, 0)
    Return()

    # Function_3_39E end

    def Function_4_3C6(): pass

    label("Function_4_3C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DD")
    Call(0, 11)
    Return()

    label("loc_3DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_3EE")
    Jump("loc_447")

    label("loc_3EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_406")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_401")

    label("loc_401")

    Jump("loc_447")

    label("loc_406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_414")
    Jump("loc_447")

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_422")
    Jump("loc_447")

    label("loc_422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_430")
    Jump("loc_447")

    label("loc_430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_43E")
    Jump("loc_447")

    label("loc_43E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_447")

    label("loc_447")

    TalkEnd(0xFE)
    Return()

    # Function_4_3C6 end

    def Function_5_44B(): pass

    label("Function_5_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_462")
    Call(0, 11)
    Return()

    label("loc_462")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_473")
    Jump("loc_4FA")

    label("loc_473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_4AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48B")
    Jump("loc_4A6")

    label("loc_48B")


    #C0001
    ChrTalk(
        0xC,
        "#01200F咕呜呜……嗷。\x02",
    )

    CloseMessageWindow()

    label("loc_4A6")

    Jump("loc_4FA")

    label("loc_4AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_4B9")
    Jump("loc_4FA")

    label("loc_4B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_4C7")
    Jump("loc_4FA")

    label("loc_4C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4D5")
    Jump("loc_4FA")

    label("loc_4D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_4E3")
    Jump("loc_4FA")

    label("loc_4E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_4F1")
    Jump("loc_4FA")

    label("loc_4F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_4FA")

    label("loc_4FA")

    TalkEnd(0xFE)
    Return()

    # Function_5_44B end

    def Function_6_4FE(): pass

    label("Function_6_4FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_588")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51C")
    Call(0, 7)
    Jump("loc_583")

    label("loc_51C")


    #C0002
    ChrTalk(
        0x8,
        (
            "泽鲁啊……\x01",
            "只有在绅士风度这方面算是一流的。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "话、话虽如此，\x01",
            "但他离完美老公\x01",
            "的标准还差得远呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_583")

    Jump("loc_59F")

    label("loc_588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_596")
    Jump("loc_59F")

    label("loc_596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_59F")

    label("loc_59F")

    TalkEnd(0xFE)
    Return()

    # Function_6_4FE end

    def Function_7_5A3(): pass

    label("Function_7_5A3")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0004
    ChrTalk(
        0x8,
        "听好哦，泽鲁。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "记住我白天对你说的话，\x01",
            "你今后一定要努力学习，努力运动。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x9,
        (
            "我、我知道啦，\x01",
            "因为我是艾米的未婚夫嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x9,
        (
            "虽然还不太明白是怎么回事，\x01",
            "但我一定会尽量努力的。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        "…………（脸红）。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_7_5A3 end

    def Function_8_689(): pass

    label("Function_8_689")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_70A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A7")
    Call(0, 7)
    Jump("loc_705")

    label("loc_6A7")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0009
    ChrTalk(
        0x9,
        (
            "那就再见啦，艾米，\x01",
            "晚上的气温很低，\x01",
            "不穿暖些可不行哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        "知、知道啦。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)

    label("loc_705")

    Jump("loc_721")

    label("loc_70A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_718")
    Jump("loc_721")

    label("loc_718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_721")

    label("loc_721")

    TalkEnd(0xFE)
    Return()

    # Function_8_689 end

    def Function_9_725(): pass

    label("Function_9_725")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_87E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80F")

    #C0011
    ChrTalk(
        0xA,
        (
            "最近这段时间，我尽量不在\x01",
            "天黑之后出来走动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xA,
        (
            "在以前的某日，我正在夜幕下散着步，\x01",
            "却突然跳出来好几条黑手党的军犬，\x01",
            "把我吓得要死，直到现在还心有余悸。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xA,
        (
            "如果没有事情要做，\x01",
            "你们最好也早点回家。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_879")

    label("loc_80F")


    #C0014
    ChrTalk(
        0xA,
        (
            "最近这段时间，只要天一黑，\x01",
            "我就马上回家。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xA,
        (
            "……免得再像当时一样，\x01",
            "被突然出现的军犬吓得心惊肉跳。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_879")

    Jump("loc_8A3")

    label("loc_87E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_88C")
    Jump("loc_8A3")

    label("loc_88C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_89A")
    Jump("loc_8A3")

    label("loc_89A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_8A3")

    label("loc_8A3")

    TalkEnd(0xFE)
    Return()

    # Function_9_725 end

    def Function_10_8A7(): pass

    label("Function_10_8A7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_9D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95C")

    #C0016
    ChrTalk(
        0xB,
        (
            "迪塔市长好像要在今晚\x01",
            "来访迎宾馆。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xB,
        (
            "听说自从发表了独立提案之后，\x01",
            "他就一直很忙碌……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xB,
        (
            "为了最终能实现那个提案，\x01",
            "现在准备工作做的怎么样了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_9D2")

    label("loc_95C")


    #C0019
    ChrTalk(
        0xB,
        (
            "听说自从发表了独立提案之后，\x01",
            "迪塔市长就一直很忙碌……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xB,
        (
            "为了最终能实现那个提案，\x01",
            "现在准备工作做的怎么样了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D2")

    Jump("loc_9EE")

    label("loc_9D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_9E5")
    Jump("loc_9EE")

    label("loc_9E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_9EE")

    label("loc_9EE")

    TalkEnd(0xFE)
    Return()

    # Function_10_8A7 end

    def Function_11_9F2(): pass

    label("Function_11_9F2")

    EventBegin(0x0)
    Fade(500)
    LoadChrToIndex("chr/ch05100.itc", 0x1E)
    LoadChrToIndex("chr/ch07500.itc", 0x1F)
    OP_68(-1560, -2000, -14560, 0)
    MoveCamera(351, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20110, 0)
    SetChrPos(0x101, -1020, -3800, -14130, 315)
    SetChrPos(0xEF, 0, -3800, -13600, 315)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xC, 0x8000)
    OP_4B(0xC, 0xFF)
    SetChrSubChip(0xD, 0x1)
    OP_0D()

    #C0021
    ChrTalk(
        0xD,
        "#5P#05902F啊，罗伊德。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xC,
        "#5P#01200F咕呜呜……嗷。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#12P#00000F塞茜尔姐姐、蔡特，\x01",
            "你们在这里啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_B20")

    #C0024
    ChrTalk(
        0x102,
        (
            "#12P#00100F还真是少见的组合呢。\x02\x03",

            "你们怎么还没去\x01",
            "迎宾馆？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C4B")

    label("loc_B20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_B6E")

    #C0025
    ChrTalk(
        0x103,
        (
            "#12P#00200F还真是少见的组合呢。\x02\x03",

            "你们怎么还没有去\x01",
            "迎宾馆？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C4B")

    label("loc_B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_BBC")

    #C0026
    ChrTalk(
        0x104,
        (
            "#12P#00300F这可真是少见的组合啊。\x02\x03",

            "你们怎么还没去\x01",
            "迎宾馆？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C4B")

    label("loc_BBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_C06")

    #C0027
    ChrTalk(
        0x109,
        (
            "#12P#10100F真是少见的组合啊。\x02\x03",

            "你们怎么还没去\x01",
            "迎宾馆？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C4B")

    label("loc_C06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_C4B")

    #C0028
    ChrTalk(
        0x105,
        (
            "#12P#10300F真是少见的组合呢。\x02\x03",

            "你们怎么还没去\x01",
            "迎宾馆？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4B")


    #C0029
    ChrTalk(
        0xD,
        (
            "#5P#05909F嗯，蔡特刚才把我\x01",
            "带到了这里。\x02\x03",

            "#05904F这里离主题公园比较远，\x01",
            "十分安静，很适合乘凉休息。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)

    #C0030
    ChrTalk(
        0x101,
        (
            "#12P#00003F塞茜尔姐姐……\x01",
            "你是不是有什么烦恼呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xD,
        (
            "#5P#05904F……呵呵，没有啦，\x01",
            "也算不上什么烦恼……\x02\x03",

            "#05901F不过也是，\x01",
            "还是应该告诉你们一声呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0032
    ChrTalk(
        0xD,
        (
            "#5P#05903F其实小滴就要\x01",
            "接受手术了。\x02\x03",

            "#05901F是由赛兰德教授负责的\x01",
            "视力恢复手术。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0033
    ChrTalk(
        0x101,
        "#12P#0005F小滴她……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xD,
        (
            "#5P#05908F嗯，小滴至今为止已经\x01",
            "接受过好几次视力恢复\x01",
            "手术了……\x02\x03",

            "#05903F但她的症状同时涉及了\x01",
            "内科、外科与神经科，情况错综复杂，\x01",
            "复明的难度相当大。\x02\x03",

            "#05900F所以这次将会尝试\x01",
            "赛兰德教授经过长期研究\x01",
            "而提出的新手术方案。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_F3B")

    #C0035
    ChrTalk(
        0x102,
        "#12P#00105F新手术方案吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF0")

    label("loc_F3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_F68")

    #C0036
    ChrTalk(
        0x103,
        "#12P#00205F新手术方案……\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF0")

    label("loc_F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_F95")

    #C0037
    ChrTalk(
        0x104,
        "#12P#00305F新手术方案啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF0")

    label("loc_F95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_FC4")

    #C0038
    ChrTalk(
        0x109,
        "#12P#10105F新手术方案……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF0")

    label("loc_FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_FF0")

    #C0039
    ChrTalk(
        0x105,
        "#12P#10305F唔，新手术方案啊。\x02",
    )

    CloseMessageWindow()

    label("loc_FF0")


    #C0040
    ChrTalk(
        0xD,
        (
            "#5P#05903F我也不是很了解具体情况……\x02\x03",

            "#05902F总之，好像是只有对外科手术极具心得的\x01",
            "神经科权威教授才能完成的手术方案。\x02\x03",

            "#05903F手术需要万全的准备工作，\x01",
            "不久之前，医院还特意从雷米菲利亚\x01",
            "订购了最新型的医疗器械。\x02\x03",

            "#05908F……据赛兰德教授说，\x01",
            "即使在这种条件下，手术的\x01",
            "成功率也只有百分之五十。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#12P#00003F在如此完善的条件下，成功率也只有一半吗……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_1182")

    #C0042
    ChrTalk(
        0x102,
        "#12P#00108F……真是让人担心啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_125A")

    label("loc_1182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_11B3")

    #C0043
    ChrTalk(
        0x103,
        "#12P#00208F……真让人担心呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_125A")

    label("loc_11B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_11E8")

    #C0044
    ChrTalk(
        0x104,
        "#12P#00303F……那可真让人担心啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_125A")

    label("loc_11E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_121D")

    #C0045
    ChrTalk(
        0x109,
        "#12P#10108F那可真是让人担心啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_125A")

    label("loc_121D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_125A")

    #C0046
    ChrTalk(
        0x105,
        (
            "#12P#10308F原来如此。\x01",
            "……那还真是让人担心呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_125A")


    #C0047
    ChrTalk(
        0xD,
        (
            "#5P#05903F但相比以往的几次失败手术，\x01",
            "这次毕竟还是拥有\x01",
            "相当高的希望。\x02\x03",

            "#05908F真希望手术\x01",
            "能顺利成功啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#12P#00003F是啊……\x01",
            "支援科经常受到\x01",
            "亚里欧斯先生的照顾。\x02\x03",

            "#00000F我们也来向女神祷告，\x01",
            "祈祷手术能取得成功吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xD,
        (
            "#5P#05909F呵呵，谢谢。\x01",
            "我一定转告给小滴。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 250, -1800, -440, 180)

    #N0050
    NpcTalk(
        0xE,
        "女性的声音",
        (
            "#N啊，塞茜尔，\x01",
            "你还在这里啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-860, -2000, -14160, 3000)
    MoveCamera(344, 18, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(20110, 3000)

    def lambda_1430():

        label("loc_1430")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_1430")

    QueueWorkItem2(0x101, 2, lambda_1430)

    def lambda_1442():

        label("loc_1442")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_1442")

    QueueWorkItem2(0xEF, 2, lambda_1442)

    def lambda_1454():
        OP_95(0xFE, 250, -3800, -12220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1454)
    WaitChrThread(0xE, 1)
    OP_93(0xE, 0x10E, 0x1F4)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0xEF, 0xFF)

    #C0051
    ChrTalk(
        0xD,
        "#5P#05905F伊莉娅，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xE,
        (
            "#01706F还问我怎么了……\x02\x03",

            "#01700F你明明说稍后就来，\x01",
            "结果怎么等都不到，\x01",
            "我只能专程过来接你。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xD,
        (
            "#5P#05902F呵呵，抱歉抱歉，\x01",
            "我马上就过去。\x02\x03",

            "#05904F嗯……和罗伊德聊过一番之后，\x01",
            "我的心情比之前平静多了……\x01",
            "差不多也该走啦。\x02\x03",

            "#05900F你们的工作想必也很辛苦……\x01",
            "我和小滴都会为大家加油的。\x02\x03",

            "#05909F所以无论遇到什么挫折\x01",
            "也不要沮丧哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15EB():
        TurnDirection(0x101, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_15EB)
    Sleep(50)

    def lambda_15FB():
        TurnDirection(0xEF, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_15FB)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)

    #C0054
    ChrTalk(
        0x101,
        "#12P#00000F嗯，谢谢啦，塞茜尔姐姐。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x40)
    SetChrPos(0xD, -1920, -3800, -13130, 180)
    OP_0D()
    Sleep(300)
    OP_93(0xD, 0x5A, 0x1F4)

    def lambda_1670():
        OP_95(0xFE, -580, -3800, -12220, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1670)
    WaitChrThread(0xD, 1)

    #C0055
    ChrTalk(
        0xD,
        "#5P#05900F好啦，我们走吧。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xE,
        (
            "#01705F怎么怎么？你刚才在和警察弟弟他们\x01",
            "谈论很暧昧的话题吗？\x02\x03",

            "#01709F我也要听啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    OP_93(0xEF, 0x0, 0x1F4)

    def lambda_1713():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1713)
    OP_93(0xD, 0x0, 0x1F4)

    def lambda_1727():
        OP_95(0xFE, 250, -1800, -440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1727)

    def lambda_1741():
        OP_95(0xFE, -580, -1800, -440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1741)
    OP_68(-20, -2000, -16100, 5000)
    MoveCamera(344, 18, 0, 5000)
    OP_6E(400, 5000)
    SetCameraDistance(20110, 5000)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)

    def lambda_179B():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_179B)
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_17FA")

    #C0057
    ChrTalk(
        0x102,
        (
            "#12P#00102F呵呵，我们本想鼓励塞茜尔小姐，\x01",
            "结果反被她鼓励了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_193F")

    label("loc_17FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1844")

    #C0058
    ChrTalk(
        0x103,
        (
            "#12P#00202F我们本想鼓励塞茜尔小姐，\x01",
            "结果反被她鼓励了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_193F")

    label("loc_1844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_1896")

    #C0059
    ChrTalk(
        0x104,
        (
            "#12P#00302F哈哈，我们本想鼓励塞茜尔小姐，\x01",
            "结果反被她鼓励了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_193F")

    label("loc_1896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_18E8")

    #C0060
    ChrTalk(
        0x109,
        (
            "#12P#10102F呵呵，我们本想鼓励塞茜尔小姐，\x01",
            "结果反被她鼓励了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_193F")

    label("loc_18E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_193F")

    #C0061
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，我们本想鼓励塞茜尔小姐，\x01",
            "但最后却搞不清是谁在鼓励谁了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_193F")


    #C0062
    ChrTalk(
        0x101,
        (
            "#6P#00004F嗯，这正是塞茜尔姐姐的性格啊。\x02\x03",

            "#00000F……好，我们也\x01",
            "向迎宾馆出发吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xC,
        "#5P#01200F咕呜呜……嗷。\x02",
    )

    CloseMessageWindow()

    def lambda_19B8():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_19B8)
    Sleep(50)

    def lambda_19C8():
        TurnDirection(0xEF, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_19C8)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_1A0A")

    #C0064
    ChrTalk(
        0x102,
        "#12P#00100F我们走啦，蔡特。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AE3")

    label("loc_1A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1A40")

    #C0065
    ChrTalk(
        0x103,
        (
            "#12P#00200F嗯……\x01",
            "我们走了，蔡特。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE3")

    label("loc_1A40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_1A6F")

    #C0066
    ChrTalk(
        0x104,
        "#12P#00300F我们走了，蔡特。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AE3")

    label("loc_1A6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_1AA0")

    #C0067
    ChrTalk(
        0x109,
        "#12P#10100F我们走了哦，蔡特。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AE3")

    label("loc_1AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_1AE3")

    #C0068
    ChrTalk(
        0x105,
        (
            "#12P#10300F呵呵，你在目送我们吗？\x01",
            "稍后再见啦，蔡特。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AE3")

    OP_5A()
    SetScenarioFlags(0x15A, 2)
    ClearChrFlags(0xC, 0x8000)
    OP_4C(0xC, 0xFF)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -1020, -3800, -14130, 0)
    EventEnd(0x5)
    Return()

    # Function_11_9F2 end

    SaveToFile()

Try(main)
