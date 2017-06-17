from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c047c.bin",                # FileName
        "c047c",                    # MapName
        "c047c",                    # Location
        0x0025,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 37, 0, 1, 0, 2],
    )

    BuildStringList((
        "c047c",                  # 0
        "多雷克老板",             # 1
        "切莉",                   # 2
        "加雷提",                 # 3
        "艾琳迪",                 # 4
        "雷特罗莎",               # 5
        "利凯爷爷",               # 6
        "矿工冈兹",               # 7
        "矿工玛尔罗",             # 8
        "游客",                   # 9
        "游客",                   # 10
        "游客",                   # 11
        "游客",                   # 12
        "帝国贵族",               # 13
        "游客",                   # 14
        "菲莉亚",                 # 15
        "兰",                     # 16
        "艾达",                   # 17
    ))

    AddCharChip((
        "chr/ch20002.itc",                   # 00
        "chr/ch20400.itc",                   # 01
        "chr/ch20402.itc",                   # 02
        "chr/ch34300.itc",                   # 03
        "chr/ch23600.itc",                   # 04
        "chr/ch25800.itc",                   # 05
        "chr/ch25900.itc",                   # 06
        "chr/ch26902.itc",                   # 07
        "chr/ch27000.itc",                   # 08
        "chr/ch27100.itc",                   # 09
        "chr/ch33100.itc",                   # 0A
        "chr/ch33302.itc",                   # 0B
        "chr/ch30702.itc",                   # 0C
        "chr/ch26200.itc",                   # 0D
    ))

    DeclNpc(-899,    4000,    21299,   180,  261,  0x0, 0,   5,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(6199,    -1000,   8000,    270,  261,  0x0, 0,   9,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       -1000,   13649,   180,  261,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-6500,   -1000,   6000,    90,   261,  0x0, 0,   8,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(1350,    -949,    11500,   0,    261,  0x0, 0,   11,  0,   255, 255, 0,   13,  255,  0)
    DeclNpc(6699,    4269,    15750,   90,   261,  0x0, 0,   0,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(6699,    4250,    17979,   90,   277,  0x0, 0,   12,  0,   255, 255, 0,   15,  255,  0)
    DeclNpc(6510,    4000,    18979,   135,  261,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(0,       -1000,   4219,    360,  405,  0x0, 0,   1,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-3019,   -1000,   3390,    315,  277,  0x0, 0,   3,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-4519,   -1000,   9789,    225,  261,  0x0, 0,   4,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(50,      4000,    18950,   0,    261,  0x0, 0,   7,   0,   255, 255, 0,   23,  255,  0)
    DeclNpc(-4570,   -1000,   13279,   0,    405,  0x0, 0,   10,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-3400,   -949,    4409,    270,  261,  0x0, 0,   2,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-900,    4000,    20000,   2000,    -900,    5500,    21300,   0x007E, 0,  3,  0x0000)
    DeclActor(5240,    -1000,   8000,    1200,    6200,    500,     8000,    0x007E, 0,  7,  0x0000)
    DeclActor(-920,    -1000,   12050,   1700,    0,       500,     13650,   0x007E, 0,  9,  0x0000)
    DeclActor(-4500,   -1000,   6000,    1500,    -6500,   500,     6000,    0x007E, 0,  11, 0x0000)
    DeclActor(7530,    4000,    17960,   1800,    7530,    5500,    17960,   0x007C, 0,  26, 0x0000)
    DeclActor(7530,    4000,    15750,   1800,    7530,    5500,    15750,   0x007C, 0,  26, 0x0000)
    DeclActor(7530,    4000,    13410,   1800,    7530,    5500,    13410,   0x007C, 0,  26, 0x0000)
    DeclActor(7530,    4000,    10460,   1800,    7530,    5500,    10460,   0x007C, 0,  26, 0x0000)
    DeclActor(7530,    4000,    8300,    1800,    7530,    5500,    8300,    0x007C, 0,  26, 0x0000)

    ScpFunction((
        "Function_0_460",          # 00, 0
        "Function_1_518",          # 01, 1
        "Function_2_5AF",          # 02, 2
        "Function_3_5EE",          # 03, 3
        "Function_4_5F2",          # 04, 4
        "Function_5_B61",          # 05, 5
        "Function_6_C54",          # 06, 6
        "Function_7_CF0",          # 07, 7
        "Function_8_CF4",          # 08, 8
        "Function_9_1197",         # 09, 9
        "Function_10_119B",        # 0A, 10
        "Function_11_15EA",        # 0B, 11
        "Function_12_15EE",        # 0C, 12
        "Function_13_18F8",        # 0D, 13
        "Function_14_1D9B",        # 0E, 14
        "Function_15_21F9",        # 0F, 15
        "Function_16_265C",        # 10, 16
        "Function_17_28D3",        # 11, 17
        "Function_18_2AEB",        # 12, 18
        "Function_19_2AF5",        # 13, 19
        "Function_20_2B5F",        # 14, 20
        "Function_21_2D65",        # 15, 21
        "Function_22_2E47",        # 16, 22
        "Function_23_30AF",        # 17, 23
        "Function_24_33A6",        # 18, 24
        "Function_25_341E",        # 19, 25
        "Function_26_34B1",        # 1A, 26
        "Function_27_353B",        # 1B, 27
        "Function_28_35CE",        # 1C, 28
    ))


    def Function_0_460(): pass

    label("Function_0_460")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4A0"),
        (1, "loc_4AC"),
        (2, "loc_4B8"),
        (3, "loc_4C4"),
        (4, "loc_4D0"),
        (5, "loc_4DC"),
        (6, "loc_4E8"),
        (SWITCH_DEFAULT, "loc_4F4"),
    )


    label("loc_4A0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4AC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4B8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4C4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4D0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4DC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_500")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_517")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_517")

    Return()

    # Function_0_460 end

    def Function_1_518(): pass

    label("Function_1_518")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_527")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 28)

    label("loc_527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_550")
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x8, -4570, -1000, 14750, 180)
    SetChrFlags(0x8, 0x10)
    Jump("loc_5AE")

    label("loc_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_55E")
    Jump("loc_5AE")

    label("loc_55E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_571")
    SetChrFlags(0x8, 0x10)
    Jump("loc_5AE")

    label("loc_571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_58E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_589")
    SetChrFlags(0x8, 0x10)

    label("loc_589")

    Jump("loc_5AE")

    label("loc_58E")

    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x15, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x11, 1000, -1000, 3500, 315)

    label("loc_5AE")

    Return()

    # Function_1_518 end

    def Function_2_5AF(): pass

    label("Function_2_5AF")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -6000, -1000, 16000, 5000, 5000, 0)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5ED")
    OP_65(0x0, 0x1)

    label("loc_5ED")

    Return()

    # Function_2_5AF end

    def Function_3_5EE(): pass

    label("Function_3_5EE")

    Call(0, 4)
    Return()

    # Function_3_5EE end

    def Function_4_5F2(): pass

    label("Function_4_5F2")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_651")
    OP_4B(0x14, 0xFF)

    #C0001
    ChrTalk(
        0x8,
        (
            "这不是伯爵吗，\x01",
            "真是久疏问候了。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "快请进，请到\x01",
            "里面的特别室。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    Jump("loc_B5D")

    label("loc_651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_69C")

    #C0003
    ChrTalk(
        0x8,
        (
            "欢迎光临。\x01",
            "欢迎光临『巴鲁卡』。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        "祝您今天玩得愉快。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B5D")

    label("loc_69C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_85F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 1)), scpexpr(EXPR_END)), "loc_754")

    #C0005
    ChrTalk(
        0x8,
        (
            "外面似乎十分拥挤，\x01",
            "真担心会不会\x01",
            "有孩子走失呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "唔……如果不在欢乐街的话，\x01",
            "就有可能是追着游行队伍，\x01",
            "跑到中央广场了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "没能帮上什么忙，\x01",
            "实在抱歉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85A")

    label("loc_754")


    #C0008
    ChrTalk(
        0x8,
        (
            "外面似乎\x01",
            "相当拥挤。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "真担心会不会\x01",
            "有孩子走失呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，其实……\x01",
            "我正是在寻找走失的孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "哟，是这样吗，\x01",
            "那可真是失礼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "唔，在二楼\x01",
            "没见过小孩子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "一楼的话，\x01",
            "问问切莉比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "如果切莉没看见，\x01",
            "那应该就是没来过本店吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB2, 1)

    label("loc_85A")

    Jump("loc_B5D")

    label("loc_85F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_8F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8B0")

    #C0015
    ChrTalk(
        0x8,
        (
            "外面似乎\x01",
            "相当拥挤。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "真担心会不会\x01",
            "有孩子走失呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F0")

    label("loc_8B0")


    #C0017
    ChrTalk(
        0x8,
        (
            "欢迎光临。\x01",
            "欢迎光临『巴鲁卡』。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        "祝您今天玩得愉快。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_8F0")

    Jump("loc_B5D")

    label("loc_8F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_94A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_942")

    #C0019
    ChrTalk(
        0x8,
        (
            "……小姑娘，\x01",
            "你该回家了。\x01",
            "你应该还没满二十岁吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_945")

    label("loc_942")

    Call(0, 5)

    label("loc_945")

    Jump("loc_B5D")

    label("loc_94A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9CC")

    #C0020
    ChrTalk(
        0x8,
        (
            "……哎呀呀，\x01",
            "兰迪，你能代我一下吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        "#0303F才不干，你自己负责啦～\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        "……你小子，闹什么别扭啊～\x02",
    )

    CloseMessageWindow()
    Jump("loc_9CF")

    label("loc_9CC")

    Call(0, 6)

    label("loc_9CF")

    Jump("loc_B5D")

    label("loc_9D4")

    TurnDirection(0x8, 0x104, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A51")

    #C0023
    ChrTalk(
        0x8,
        (
            "虽然客人很多，\x01",
            "可是也没有出什么乱子啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "兰迪，不要那么担心。\x01",
            "如果有什么事的话，我会联络你的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5D")

    label("loc_A51")


    #C0025
    ChrTalk(
        0x8,
        "……兰迪吗。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "昨天才大玩了一场，\x01",
            "今天怎么又来了？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#0300F没有啦，今天是来工作的。\x02\x03",

            "『巴鲁卡』看来还是\x01",
            "一如既往地生意兴隆啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "嗯，没出什么乱子啦。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "如果有什么事的话，\x01",
            "我会联络你的。\x01",
            "不要那么担心啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        (
            "#0300F哈哈，明白，\x01",
            "我会再来看看情况的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_B5D")

    TalkEnd(0x8)
    Return()

    # Function_4_5F2 end

    def Function_5_B61(): pass

    label("Function_5_B61")

    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x13, 0x0)

    #C0031
    ChrTalk(
        0x8,
        (
            "……小姑娘，你差不多\x01",
            "该回家了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "我可是很忙的。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x13,
        "哎～不要啦～！\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x13,
        (
            "今天没关系吧，\x01",
            "毕竟是庆典嘛～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C15")

    #C0035
    ChrTalk(
        0x104,
        (
            "#0303F（老板难得\x01",
            "  在犯愁呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C4C")

    label("loc_C15")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C4C")

    #C0036
    ChrTalk(
        0x101,
        (
            "#0003F（老板还挺\x01",
            "  受欢迎呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4C")

    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_5_B61 end

    def Function_6_C54(): pass

    label("Function_6_C54")

    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x13, 0x0)

    #C0037
    ChrTalk(
        0x13,
        "老板老板，你多大了？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x13,
        "听说你以前是黑社会的，是真的吗～？\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "客人，您喝醉了。\x01",
            "差不多也该适可而止了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x13,
        "……不要啦～⊥⊥\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_6_C54 end

    def Function_7_CF0(): pass

    label("Function_7_CF0")

    Call(0, 8)
    Return()

    # Function_7_CF0 end

    def Function_8_CF4(): pass

    label("Function_8_CF4")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1193")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "交换\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D51")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_D51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D71")
    OP_AF(0x40)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_118E")

    label("loc_D71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D85")
    Jump("loc_118E")

    label("loc_D85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_DF1")

    #C0041
    ChrTalk(
        0x9,
        (
            "纪念庆典期间大放血，\x01",
            "只到今天为止哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x9,
        "请大家加油玩哦～☆\x02",
    )

    CloseMessageWindow()
    Jump("loc_118E")

    label("loc_DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_E47")

    #C0043
    ChrTalk(
        0x9,
        (
            "游行结束之后，\x01",
            "大家好像都回来了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "各位～加油\x01",
            "挥霍米拉哦～☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_118E")

    label("loc_E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_FD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 3)), scpexpr(EXPR_END)), "loc_EBC")

    #C0045
    ChrTalk(
        0x9,
        (
            "好可爱的男孩子啊～\x01",
            "不过，好像没来过『巴鲁卡』。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            "因为所有客人\x01",
            "我都会仔细观察的嘛～☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FD3")

    label("loc_EBC")


    #C0047
    ChrTalk(
        0x101,
        (
            "#0001F（嗯，这个人\x01",
            "  可能知道些什么吧……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0049
    ChrTalk(
        0x9,
        "哎～是走失的孩子吗～？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        "我想他应该没来过『巴鲁卡』～\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "在我们这种店里，\x01",
            "小孩子会很显眼呢☆\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，说得也是呢……\x01",
            "谢谢您了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAA, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)

    label("loc_FD3")

    Jump("loc_118E")

    label("loc_FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_102E")

    #C0053
    ChrTalk(
        0x9,
        (
            "游行结束之后，\x01",
            "大家好像都回来了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "各位～加油\x01",
            "挥霍米拉哦～☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_118E")

    label("loc_102E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_10B0")

    #C0055
    ChrTalk(
        0x9,
        (
            "别看老板那样，\x01",
            "其实他相当受欢迎呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        "呼，没办法吧～\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "他散发出来的一点点危险气息，\x01",
            "最能撩动少女心呢～⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_118E")

    label("loc_10B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1129")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_10E8")

    #C0058
    ChrTalk(
        0x9,
        (
            "冈兹先生\x01",
            "又来挥霍米拉了～☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1124")

    label("loc_10E8")


    #C0059
    ChrTalk(
        0x9,
        "冈兹先生又来玩了～\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "呵呵，他又来\x01",
            "贡献米拉了吗☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1124")

    Jump("loc_118E")

    label("loc_1129")


    #C0061
    ChrTalk(
        0x9,
        "欢迎光临『巴鲁卡』～！\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "为了配合纪念庆典，\x01",
            "我们准备了豪华奖品呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        "请务必挑战一下哦～☆\x02",
    )

    CloseMessageWindow()

    label("loc_118E")

    Jump("loc_D01")

    label("loc_1193")

    TalkEnd(0x9)
    Return()

    # Function_8_CF4 end

    def Function_9_1197(): pass

    label("Function_9_1197")

    Call(0, 10)
    Return()

    # Function_9_1197 end

    def Function_10_119B(): pass

    label("Function_10_119B")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15E6")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",            # 0
            "玩扑克\x01",          # 1
            "玩二十一点\x01",      # 2
            "放弃\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1205")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1205")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1255")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_1255")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12A5")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_12A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12B9")
    Jump("loc_15E1")

    label("loc_12B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15E1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_13A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1337")

    #C0064
    ChrTalk(
        0xA,
        (
            "老板亲自来做\x01",
            "伯爵的对手呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xA,
        (
            "呵呵，因为是会花大钱来玩的\x01",
            "重要客人嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A2")

    label("loc_1337")


    #C0066
    ChrTalk(
        0xA,
        (
            "每年一到了这个时期，\x01",
            "伯爵就会经常来这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xA,
        (
            "他是特别室的常客之一……\x01",
            "会花大钱来玩，十分豪爽哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_13A2")

    Jump("loc_15E1")

    label("loc_13A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1421")

    #C0068
    ChrTalk(
        0xA,
        (
            "各人有各人的\x01",
            "器量。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xA,
        "呵呵，各位也请多加留意。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xA,
        (
            "若是进行超越自己器量的比赛，\x01",
            "结果是显而易见的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E1")

    label("loc_1421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1530")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1499")

    #C0071
    ChrTalk(
        0xA,
        (
            "玩的时候，常常会\x01",
            "忍不住头脑发热。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xA,
        (
            "虽说适逢纪念庆典，\x01",
            "但过分沉迷于玩乐\x01",
            "也不是件好事呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_152B")

    label("loc_1499")


    #C0073
    ChrTalk(
        0xA,
        (
            "遵守礼节，\x01",
            "这是游戏的基本原则。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xA,
        (
            "就算是庆典，\x01",
            "过分沉迷于玩乐\x01",
            "也不是件好事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xA,
        (
            "比平时稍微增加\x01",
            "一点点代币……\x01",
            "这样的度应该刚刚好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_152B")

    Jump("loc_15E1")

    label("loc_1530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1593")

    #C0076
    ChrTalk(
        0xA,
        (
            "每个游客\x01",
            "都几乎必来的地方……\x01",
            "就是这条欢乐街。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xA,
        (
            "呼……\x01",
            "今天也是客人爆满啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E1")

    label("loc_1593")


    #C0078
    ChrTalk(
        0xA,
        (
            "欢迎光临，\x01",
            "这里是扑克台。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "作为纪念庆典的回忆，\x01",
            "各位要不要来玩一局？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15E1")

    Jump("loc_11A8")

    label("loc_15E6")

    TalkEnd(0xA)
    Return()

    # Function_10_119B end

    def Function_11_15EA(): pass

    label("Function_11_15EA")

    Call(0, 12)
    Return()

    # Function_11_15EA end

    def Function_12_15EE(): pass

    label("Function_12_15EE")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18F4")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",        # 0
            "玩轮盘\x01",      # 1
            "放弃\x01",        # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_164D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_164D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_169D")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_169D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16B1")
    Jump("loc_18EF")

    label("loc_16B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18EF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_17A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_174B")

    #C0080
    ChrTalk(
        0xB,
        (
            "纪念庆典也到了最终日，\x01",
            "说不定会有什么好事发生呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xB,
        (
            "……呵呵，虽然没什么根据。\x01",
            "要不要玩一把试试？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17A4")

    label("loc_174B")


    #C0082
    ChrTalk(
        0xB,
        (
            "欢迎光临。\x01",
            "要不要玩轮盘？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xB,
        (
            "纪念庆典也到了最终日，\x01",
            "说不定会有什么好事发生呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_17A4")

    Jump("loc_18EF")

    label("loc_17A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_17D1")

    #C0084
    ChrTalk(
        0xB,
        "呵呵，您玩得开心吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_18EF")

    label("loc_17D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1835")

    #C0085
    ChrTalk(
        0xB,
        (
            "欢迎光临。\x01",
            "欢迎光临『巴鲁卡』。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xB,
        (
            "正好有空桌台。\x01",
            "客人，您要不要也来玩一把呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18EF")

    label("loc_1835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_18A5")

    #C0087
    ChrTalk(
        0xB,
        (
            "呵呵……就算是和你们玩，\x01",
            "我也不会手下留情哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xB,
        (
            "不讲情面，只看实力，\x01",
            "这就是比赛的规矩啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18EF")

    label("loc_18A5")


    #C0089
    ChrTalk(
        0xB,
        (
            "在纪念庆典期间，\x01",
            "这里也是一片盛况呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xB,
        (
            "呵呵，请坐，\x01",
            "还有空位呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18EF")

    Jump("loc_15FB")

    label("loc_18F4")

    TalkEnd(0xB)
    Return()

    # Function_12_15EE end

    def Function_13_18F8(): pass

    label("Function_13_18F8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_198C")
    Jump("loc_19D6")

    label("loc_198C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19AC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19D6")

    label("loc_19AC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19CC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19D6")

    label("loc_19CC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19D6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1A81")

    #C0091
    ChrTalk(
        0xC,
        (
            "哎呀……那不是帝国的\x01",
            "卡莱尔伯爵嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xC,
        "他是帝国东部的权威贵族哦。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xC,
        (
            "听说他每年都会来纪念庆典，\x01",
            "看来是真的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D93")

    label("loc_1A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1AF4")

    #C0094
    ChrTalk(
        0xC,
        (
            "彩虹剧团的公演，\x01",
            "今天也是场面火爆啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xC,
        (
            "我真想\x01",
            "再去看一次呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xC,
        (
            "呵呵，\x01",
            "从哪里能弄到票呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D93")

    label("loc_1AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1BF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1B4E")

    #C0097
    ChrTalk(
        0xC,
        (
            "莫非连事务类工作\x01",
            "也是自己做的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xC,
        "市长先生也真是辛苦呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BF1")

    label("loc_1B4E")


    #C0099
    ChrTalk(
        0xC,
        (
            "麦克道尔市长似乎连日\x01",
            "都受邀参加会谈和祝贺会呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xC,
        (
            "以市长的立场来说，\x01",
            "这也是没办法的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xC,
        (
            "不过，我记得市长秘书\x01",
            "被逮捕了吧，\x01",
            "事务类工作要怎么办呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_1BF1")

    Jump("loc_1D93")

    label("loc_1BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1D33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1C7D")

    #C0102
    ChrTalk(
        0xC,
        (
            "现在这个时期，似乎会有\x01",
            "『假货贩子』在克洛斯贝尔出没哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xC,
        (
            "呵呵，他们的买卖是\x01",
            "瞄准了平民对名牌的欲望呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D2E")

    label("loc_1C7D")


    #C0104
    ChrTalk(
        0xC,
        (
            "这么说来……\x01",
            "你们知道吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xC,
        (
            "现在这个时期，会有\x01",
            "『假货贩子』在克洛斯贝尔出没哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xC,
        (
            "听说，他们曾经还试图\x01",
            "向时代百货店兜售假货……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xC,
        (
            "呵呵，真是\x01",
            "不可不防的坏人啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_1D2E")

    Jump("loc_1D93")

    label("loc_1D33")


    #C0108
    ChrTalk(
        0xC,
        (
            "伊莉娅·普拉提耶……\x01",
            "她的表演的确比传闻中更震撼人心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xC,
        (
            "呵呵，难怪\x01",
            "票价定得那么高呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D93")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_18F8 end

    def Function_14_1D9B(): pass

    label("Function_14_1D9B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E2F")
    Jump("loc_1E79")

    label("loc_1E2F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1E4F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E79")

    label("loc_1E4F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E6F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E79")

    label("loc_1E6F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E79")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1FAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1F2A")

    #C0110
    ChrTalk(
        0xD,
        (
            "总感觉，庆典一结束，\x01",
            "运气也会跟着消失了。\x01",
            "每年的最终日都会觉得很伤感。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xD,
        (
            "不行不行，\x01",
            "今天可要放手一搏才行啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FA6")

    label("loc_1F2A")


    #C0112
    ChrTalk(
        0xD,
        "今天也会赢，一定要赢！\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xD,
        "……要趁现在大赚一笔才行呢。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xD,
        (
            "不知为何，总感觉\x01",
            "纪念庆典一结束，运气也会随之消失了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_1FA6")

    Jump("loc_21F1")

    label("loc_1FAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_209B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_201E")

    #C0115
    ChrTalk(
        0xD,
        (
            "虽说是庆典，\x01",
            "但记者和警察之类的人\x01",
            "好像会比平时更加忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xD,
        "呵呵，年轻的劳动者们啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2096")

    label("loc_201E")


    #C0117
    ChrTalk(
        0xD,
        (
            "外面因为有游行，\x01",
            "热闹非凡呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xD,
        (
            "还有个青年\x01",
            "拿着相机追着跑呢，\x01",
            "大概是个杂志社记者吧，\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xD,
        "呵呵，真是辛苦啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_2096")

    Jump("loc_21F1")

    label("loc_209B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2162")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_20F0")

    #C0120
    ChrTalk(
        0xD,
        "老虎机这边的形势也一片大好。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xD,
        "唔呵呵，要大赚一笔呢～\x02",
    )

    CloseMessageWindow()
    Jump("loc_215D")

    label("loc_20F0")


    #C0122
    ChrTalk(
        0xD,
        (
            "那个臭老婆子，今天也试图\x01",
            "妨碍我来『巴鲁卡』呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xD,
        (
            "哼，还差得远呢！\x01",
            "只是这种程度，我才不会服输呢！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_215D")

    Jump("loc_21F1")

    label("loc_2162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_21A6")

    #C0124
    ChrTalk(
        0xD,
        "哦～来了来了！\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xD,
        "唔呵呵，我都笑得合不拢嘴了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_21F1")

    label("loc_21A6")


    #C0126
    ChrTalk(
        0xD,
        "呵呵，来了来了！\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xD,
        (
            "不愧是纪念庆典期间，\x01",
            "连玩老虎机的状态都这么好！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_1D9B end

    def Function_15_21F9(): pass

    label("Function_15_21F9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_228D")
    Jump("loc_22D7")

    label("loc_228D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_22AD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_22D7")

    label("loc_22AD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22CD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_22D7")

    label("loc_22CD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22D7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_23FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23A5")

    #C0128
    ChrTalk(
        0xFE,
        (
            "呜呃……\x01",
            "又输掉了……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "昨天明明赢了一大笔，\x01",
            "运气应该来了才对啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        "可恶，今晚一定要一决胜负！\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x103,
        "#0203F……典型的沉迷模式呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_23F6")

    label("loc_23A5")


    #C0132
    ChrTalk(
        0xFE,
        (
            "昨天明明赢了一大笔，\x01",
            "运气应该来了才对啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        "可恶，今晚一定要一决胜负！\x02",
    )

    CloseMessageWindow()

    label("loc_23F6")

    Jump("loc_2654")

    label("loc_23FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_249A")

    #C0134
    ChrTalk(
        0xFE,
        "喂，听我说哦。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "昨天我在这台老虎机\x01",
            "大赚了一笔哦！\x01",
            "真是欣喜若狂啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "……不过，要是算上至今为止输掉的米拉总数，\x01",
            "还是远远没有回本呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2654")

    label("loc_249A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_25EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257E")

    #C0137
    ChrTalk(
        0xFE,
        (
            "昨天我玩轮盘\x01",
            "输掉了……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "唉唉唉……要是那个球\x01",
            "能再往右边移那么\x01",
            "一里矩……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x104,
        (
            "#0303F那种心情，我很能体会……！\x02\x03",

            "#0309F女神要是\x01",
            "再多赐予那么一点点\x01",
            "帮助就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        "#0006F……不要那么投入啦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_25E6")

    label("loc_257E")


    #C0141
    ChrTalk(
        0xFE,
        (
            "那个轮盘的球\x01",
            "要是能再往右边\x01",
            "移那么一里矩……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "……可恶～！\x01",
            "输掉的部分，一定要用\x01",
            "老虎机赢回来！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25E6")

    Jump("loc_2654")

    label("loc_25EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2654")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2606")
    Call(0, 17)
    Jump("loc_2654")

    label("loc_2606")


    #C0143
    ChrTalk(
        0xFE,
        (
            "呜……头还是好痛，\x01",
            "完全宿醉了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "啧，我反而羡慕\x01",
            "完全倒下的罗基呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2654")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_21F9 end

    def Function_16_265C(): pass

    label("Function_16_265C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_26CD")

    #C0145
    ChrTalk(
        0xFE,
        (
            "昨天虽然大获全胜，\x01",
            "但是今天好像\x01",
            "全都输光了。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "说到底，\x01",
            "这里毕竟还是\x01",
            "要让店里盈利的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28CF")

    label("loc_26CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_271F")

    #C0147
    ChrTalk(
        0xFE,
        (
            "冈兹竟然会赢，\x01",
            "真是少见啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "但我觉得应该\x01",
            "见好就收才对。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28CF")

    label("loc_271F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2866")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D6")

    #C0149
    ChrTalk(
        0xFE,
        (
            "我每天都和冈兹那家伙\x01",
            "来『巴鲁卡』。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "他总是想大捞一笔，\x01",
            "结果从来都赢不了。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "他老想把以前输掉的\x01",
            "一次全赢回来，\x01",
            "难道不觉得，这简直就是在做梦吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2861")

    label("loc_27D6")


    #C0152
    ChrTalk(
        0xFE,
        (
            "冈兹之所以会不断为『巴鲁卡』做着贡献，\x01",
            "都是因为他老想大捞一笔。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "总想把以前输掉的\x01",
            "一次都赢回来，\x01",
            "难道不觉得，这简直就是在做梦吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2861")

    Jump("loc_28CF")

    label("loc_2866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_28CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2881")
    Call(0, 17)
    Jump("loc_28CF")

    label("loc_2881")


    #C0154
    ChrTalk(
        0xFE,
        (
            "我陪冈兹一起\x01",
            "来克洛斯贝尔玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "在纪念庆典期间，\x01",
            "打算一直待在这里呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28CF")

    TalkEnd(0xFE)
    Return()

    # Function_16_265C end

    def Function_17_28D3(): pass

    label("Function_17_28D3")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0xF, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_296F")
    Jump("loc_29B9")

    label("loc_296F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_298F")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29B9")

    label("loc_298F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29AF")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29B9")

    label("loc_29AF")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29B9")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    TurnDirection(0xF, 0xE, 0)

    #C0156
    ChrTalk(
        0xE,
        (
            "呜……\x01",
            "头还在一阵阵地痛呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xF,
        "怎么想都是因为喝多了啊。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xF,
        (
            "……不过，镇长也真是好人啊。\x01",
            "因为是纪念庆典，就请\x01",
            "所有的矿工喝酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xE,
        (
            "因此，罗基那家伙\x01",
            "到现在还在红砖亭\x01",
            "那里睡着呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xE,
        (
            "……不过，昨天也真够开心的，\x01",
            "就不管这些啦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)
    OP_93(0xF, 0x87, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_17_28D3 end

    def Function_18_2AEB(): pass

    label("Function_18_2AEB")

    TalkBegin(0xFE)
    Call(0, 19)
    TalkEnd(0xFE)
    Return()

    # Function_18_2AEB end

    def Function_19_2AF5(): pass

    label("Function_19_2AF5")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0161
    ChrTalk(
        0x11,
        "老公，加油哦！\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x11,
        (
            "要赢个十倍左右，\x01",
            "然后去米修拉姆玩哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x10,
        "哈哈哈，包在我身上！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_19_2AF5 end

    def Function_20_2B5F(): pass

    label("Function_20_2B5F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2BF3")
    Jump("loc_2C3D")

    label("loc_2BF3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2C13")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C3D")

    label("loc_2C13")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C33")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C3D")

    label("loc_2C33")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C3D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2C9B")
    SetChrSubChip(0x15, 0x0)

    #C0164
    ChrTalk(
        0x15,
        (
            "这次，这次一定要……\x01",
            "……混账！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D5D")

    label("loc_2C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2D22")

    #C0165
    ChrTalk(
        0x15,
        (
            "呜哦哦……\x01",
            "明明赢了一晚上～……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x15,
        (
            "竟、竟然在最后一把中\x01",
            "全部输光啦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x15,
        (
            "我、我的米拉……\x01",
            "……代币之山………！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D5D")

    label("loc_2D22")


    #C0168
    ChrTalk(
        0x15,
        "哦，你们也要玩一把吗？\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x15,
        (
            "哈哈哈，可不要\x01",
            "太沉迷哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D5D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_2B5F end

    def Function_21_2D65(): pass

    label("Function_21_2D65")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2D9F")

    #C0170
    ChrTalk(
        0x11,
        (
            "老、老公～……\x01",
            "你可不要兴奋过头哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E43")

    label("loc_2D9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2E05")

    #C0171
    ChrTalk(
        0x11,
        (
            "啊啊啊～～～……\x01",
            "明明都已经是最后一把了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x11,
        (
            "那个庄家，\x01",
            "该不会是耍诈了吧！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E43")

    label("loc_2E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E40")

    #C0173
    ChrTalk(
        0x11,
        (
            "呀，好厉害～！\x01",
            "又赢了！\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x11,
        "真有你的！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E43")

    label("loc_2E40")

    Call(0, 19)

    label("loc_2E43")

    TalkEnd(0xFE)
    Return()

    # Function_21_2D65 end

    def Function_22_2E47(): pass

    label("Function_22_2E47")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2EEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2EA7")

    #C0175
    ChrTalk(
        0x12,
        (
            "能在『巴鲁卡』赚到米拉，\x01",
            "感觉真是爽啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x12,
        (
            "明年也来\x01",
            "这里吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EEA")

    label("loc_2EA7")


    #C0177
    ChrTalk(
        0x12,
        (
            "今年让我\x01",
            "赚了很多呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x12,
        (
            "明年的纪念庆典时\x01",
            "也来这里吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_2EEA")

    Jump("loc_30AB")

    label("loc_2EEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2FCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2F60")

    #C0179
    ChrTalk(
        0x12,
        (
            "状态好的日子，就应该\x01",
            "大胆地继续玩下去。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x12,
        (
            "……当然，也必须冷静地\x01",
            "看清收手的时机。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FC6")

    label("loc_2F60")


    #C0181
    ChrTalk(
        0x12,
        "……今天的状态不错……\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x12,
        (
            "在这种时候，就应该\x01",
            "大胆地继续玩下去。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x12,
        "我今天的状态真是不错。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_2FC6")

    Jump("loc_30AB")

    label("loc_2FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3043")

    #C0184
    ChrTalk(
        0x12,
        (
            "……亏了和输了\x01",
            "完全是两回事……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x12,
        (
            "虽然亏了一次，\x01",
            "但最后也有可能大获全胜。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x12,
        "这里是很深奥的……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30AB")

    label("loc_3043")


    #C0187
    ChrTalk(
        0x12,
        (
            "……轮盘\x01",
            "是比运势啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x12,
        (
            "要是头脑发热，玩得太大，\x01",
            "就肯定会亏损……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x12,
        "所以最重要的就是自制力。\x02",
    )

    CloseMessageWindow()

    label("loc_30AB")

    TalkEnd(0xFE)
    Return()

    # Function_22_2E47 end

    def Function_23_30AF(): pass

    label("Function_23_30AF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3143")
    Jump("loc_318D")

    label("loc_3143")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3163")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_318D")

    label("loc_3163")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3183")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_318D")

    label("loc_3183")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_318D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3276")
    SetChrSubChip(0x13, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_320C")

    #C0190
    ChrTalk(
        0x13,
        "（咕噜咕噜……）噗哈～\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x13,
        (
            "老板是大笨蛋，\x01",
            "跟我聊聊天啦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3271")

    label("loc_320C")


    #C0192
    ChrTalk(
        0x13,
        (
            "（咕噜咕噜……）\x01",
            "老板竟然抛弃我……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x13,
        (
            "跑去陪男人……为什么啊！\x01",
            "（咕噜咕噜、咕噜咕噜）……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_3271")

    Jump("loc_339E")

    label("loc_3276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_32DE")

    #C0194
    ChrTalk(
        0x13,
        (
            "老板真过分，\x01",
            "完全不理我。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x13,
        (
            "讨厌，真是个坏人！\x01",
            "不过一本正经的样子好·可·爱·哦⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_339E")

    label("loc_32DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3348")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3340")
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x13, 0x0)

    #C0196
    ChrTalk(
        0x13,
        (
            "老板欺负人，\x01",
            "大坏蛋～～……！\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x13,
        "但是我就喜欢他这点⊥⊥\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    Jump("loc_3343")

    label("loc_3340")

    Call(0, 5)

    label("loc_3343")

    Jump("loc_339E")

    label("loc_3348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_339B")

    #C0198
    ChrTalk(
        0x13,
        "嗯，应该是我喜欢的类型⊥\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x13,
        (
            "今天不回去了，\x01",
            "就住在这里了～⊥⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_339E")

    label("loc_339B")

    Call(0, 6)

    label("loc_339E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_30AF end

    def Function_24_33A6(): pass

    label("Function_24_33A6")

    TalkBegin(0xFE)
    OP_4B(0x8, 0xFF)

    #C0200
    ChrTalk(
        0x14,
        (
            "呼……那么，今年\x01",
            "也好好开心一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x14,
        (
            "多雷克，房间\x01",
            "准备好了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x8,
        (
            "我来为您带路，\x01",
            "请往里边走。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_24_33A6 end

    def Function_25_341E(): pass

    label("Function_25_341E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B0")
    OP_29(0x46, 0x1, 0x2)

    #C0203
    ChrTalk(
        0x101,
        (
            "#0003F（好，欢乐街的探听\x01",
            "  到这里就足够了吧。）\x02\x03",

            "#0001F（接下来是后巷……\x01",
            "  用同样的方法，继续探听情报吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 3)

    label("loc_34B0")

    Return()

    # Function_25_341E end

    def Function_26_34B1(): pass

    label("Function_26_34B1")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "玩老虎机\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3537")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_3537")

    TalkEnd(0xFF)
    Return()

    # Function_26_34B1 end

    def Function_27_353B(): pass

    label("Function_27_353B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_35CD")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3569")
    Sleep(500)
    Jump("loc_35B1")

    label("loc_3569")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3580")
    Sleep(150)
    Jump("loc_35B1")

    label("loc_3580")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3597")
    Sleep(200)
    Jump("loc_35B1")

    label("loc_3597")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_35AE")
    Sleep(300)
    Jump("loc_35B1")

    label("loc_35AE")

    Sleep(400)

    label("loc_35B1")

    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x12C, 0x7D0)
    Jump("Function_27_353B")

    label("loc_35CD")

    Return()

    # Function_27_353B end

    def Function_28_35CE(): pass

    label("Function_28_35CE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch36300.itc", 0x1E)
    LoadChrToIndex("chr/ch36400.itc", 0x1F)
    LoadChrToIndex("chr/ch36500.itc", 0x20)
    LoadEffect(0x0, "event\\ev300_00.eff")
    LoadEffect(0x1, "event\\ev399_00.eff")
    ClearMapObjFlags(0x7, 0x4)
    OP_68(-4120, 4270, 6410, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(320, 0)
    SetCameraDistance(20500, 0)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x104, -3700, -1200, 6430, 315)
    SetChrPos(0x16, -3370, -1000, 7440, 315)
    SetChrPos(0x18, -2450, -1000, 5890, 315)
    SetChrPos(0x17, -3450, -1000, 5410, 315)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrChipByIndex(0x18, 0x20)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    OP_68(-6000, 0, 8000, 0)
    MoveCamera(43, 33, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -5950, -70, 8050, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    MoveCamera(33, 33, 0, 4000)
    SetCameraDistance(17500, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    OP_68(-4120, 0, 6410, 2000)
    MoveCamera(80, 23, 0, 2000)
    SetCameraDistance(19000, 2000)
    Sleep(3000)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 136000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(1332, 255, 100, 0)    #voice#Randy
    Sound(506, 0, 100, 0)
    Sound(565, 0, 100, 0)
    Sleep(5000)
    Sound(85, 0, 100, 0)
    Sleep(500)
    Sound(1290, 255, 100, 0)    #voice#Randy

    def lambda_37D9():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_37D9)

    def lambda_37E6():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_37E6)

    def lambda_37F3():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_37F3)
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x18, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    BeginChrThread(0x16, 1, 0, 27)
    BeginChrThread(0x18, 1, 0, 27)
    BeginChrThread(0x17, 1, 0, 27)
    Sleep(2000)
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0x5C, 7)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_35CE end

    SaveToFile()

Try(main)
