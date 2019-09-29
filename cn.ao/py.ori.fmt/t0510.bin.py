from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t0510.bin",                # FileName
        "t0510",                    # MapName
        "t0510",                    # Location
        0x003D,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x18,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 61, 0, 3, 0, 4],
    )

    BuildStringList((
        "t0510",                  # 0
        "比克森镇长",             # 1
        "安娜夫人",               # 2
        "米兰达",                 # 3
        "比鲁玛婆婆",             # 4
        "卢利艾达",               # 5
        "亚米",                   # 6
        "亚雷库",                 # 7
        "矿工冈兹",               # 8
        "矿工罗基",               # 9
        "霍夫曼矿山长",           # 10
        "矿工马库斯",             # 11
        "米蕾优三尉",             # 12
        "警备队员",               # 13
    ))

    AddCharChip((
        "chr/ch23200.itc",                   # 00
        "chr/ch23202.itc",                   # 01
        "chr/ch20100.itc",                   # 02
        "chr/ch20102.itc",                   # 03
        "chr/ch22700.itc",                   # 04
        "chr/ch23300.itc",                   # 05
        "chr/ch24300.itc",                   # 06
        "chr/ch23700.itc",                   # 07
        "chr/ch23000.itc",                   # 08
        "chr/ch30700.itc",                   # 09
        "chr/ch26202.itc",                   # 0A
        "chr/ch26302.itc",                   # 0B
        "chr/ch26202.itc",                   # 0C
        "chr/ch32600.itc",                   # 0D
        "chr/ch31200.itc",                   # 0E
        "chr/ch24302.itc",                   # 0F
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

    DeclNpc(-889,    949,     3319,    90,   261,  0x0, 0,   0,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-6530,   750,     59,      270,  261,  0x0, 0,   2,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(96099,   0,       4219,    0,    261,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(49209,   0,       4369,    0,    261,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(147369,  0,       4179,    333,  261,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(47450,   0,       -1500,   0,    389,  0x0, 0,   7,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(101800,  0,       500,     225,  389,  0x0, 0,   8,   0,   0,   2,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   9,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(47450,   300,     0,       180,  389,  0x0, 0,   10,  0,   255, 255, 0,   11,  255,  0)
    DeclNpc(97459,   150,     -1169,   0,    453,  0x0, 0,   11,  0,   255, 255, 0,   7,   255,  0)
    DeclNpc(150729,  250,     100,     270,  453,  0x0, 0,   12,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(1200,    750,     -1000,   270,  389,  0x0, 0,   13,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(2200,    750,     -270,    270,  389,  0x0, 0,   14,  0,   0,   0,   0,   21,  255,  0)

    ChipFrameInfo(732, 0)                                        # 0

    ScpFunction((
        "Function_0_2DC",          # 00, 0
        "Function_1_38C",          # 01, 1
        "Function_2_3B7",          # 02, 2
        "Function_3_3E2",          # 03, 3
        "Function_4_62F",          # 04, 4
        "Function_5_668",          # 05, 5
        "Function_6_1081",         # 06, 6
        "Function_7_1141",         # 07, 7
        "Function_8_1362",         # 08, 8
        "Function_9_1E7D",         # 09, 9
        "Function_10_2001",        # 0A, 10
        "Function_11_20D1",        # 0B, 11
        "Function_12_21A1",        # 0C, 12
        "Function_13_2B69",        # 0D, 13
        "Function_14_2C4A",        # 0E, 14
        "Function_15_2D21",        # 0F, 15
        "Function_16_3AA5",        # 10, 16
        "Function_17_3C21",        # 11, 17
        "Function_18_3E6E",        # 12, 18
        "Function_19_4B65",        # 13, 19
        "Function_20_4C5F",        # 14, 20
        "Function_21_4E3B",        # 15, 21
        "Function_22_4F86",        # 16, 22
        "Function_23_4FD1",        # 17, 23
        "Function_24_5E7F",        # 18, 24
    ))


    def Function_0_2DC(): pass

    label("Function_0_2DC")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_314"),
        (1, "loc_320"),
        (2, "loc_32C"),
        (3, "loc_338"),
        (4, "loc_344"),
        (5, "loc_350"),
        (6, "loc_35C"),
        (SWITCH_DEFAULT, "loc_368"),
    )


    label("loc_314")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_320")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_32C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_338")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_344")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_350")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_35C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_368")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_374")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_38B")

    Return()

    # Function_0_2DC end

    def Function_1_38C(): pass

    label("Function_1_38C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B6")
    OP_94(0xFE, 0xBD74, 0xA8C, 0xC92C, 0xFFFFFD44, 0x3E8)
    Sleep(250)
    Jump("Function_1_38C")

    label("loc_3B6")

    Return()

    # Function_1_38C end

    def Function_2_3B7(): pass

    label("Function_2_3B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E1")
    OP_94(0xFE, 0x192EE, 0x7F8, 0x1863C, 0xFFFFFB82, 0x3E8)
    Sleep(250)
    Jump("Function_2_3B7")

    label("loc_3E1")

    Return()

    # Function_2_3B7 end

    def Function_3_3E2(): pass

    label("Function_3_3E2")

    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrChipByIndex(0x11, 0xB)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    SetChrChipByIndex(0x12, 0xC)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_423")
    Jump("loc_60F")

    label("loc_423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_43B")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_60F")

    label("loc_43B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4C2")
    SetChrPos(0xC, 147900, 100, 100, 90)
    SetChrChipByIndex(0xC, 0xF)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrChipByIndex(0x8, 0x0)
    ClearChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x40)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x8, 0, 750, -1000, 90)
    ClearChrFlags(0x13, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A9")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x13, 0x10)

    label("loc_4A9")

    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)
    Jump("loc_60F")

    label("loc_4C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4D0")
    Jump("loc_60F")

    label("loc_4D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4DE")
    Jump("loc_60F")

    label("loc_4DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_518")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 101600, 0, 500, 225)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 50000, 0, 1000, 315)
    Jump("loc_60F")

    label("loc_518")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_526")
    Jump("loc_60F")

    label("loc_526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_534")
    Jump("loc_60F")

    label("loc_534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_542")
    Jump("loc_60F")

    label("loc_542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_550")
    Jump("loc_60F")

    label("loc_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_55E")
    Jump("loc_60F")

    label("loc_55E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_592")
    ClearChrFlags(0xD, 0x80)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0xA)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    Jump("loc_60F")

    label("loc_592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5EA")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 1200, 750, -1000, 270)
    SetChrChipByIndex(0x8, 0x0)
    ClearChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 0, 650, -1000, 90)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E5")
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_5E5")

    Jump("loc_60F")

    label("loc_5EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_5F8")
    Jump("loc_60F")

    label("loc_5F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_606")
    Jump("loc_60F")

    label("loc_606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_60F")

    label("loc_60F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62E")
    SetMapFlags(0x10000000)
    Event(0, 23)

    label("loc_62E")

    Return()

    # Function_3_3E2 end

    def Function_4_62F(): pass

    label("Function_4_62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_641")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_667")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_667")

    Return()

    # Function_4_62F end

    def Function_5_668(): pass

    label("Function_5_668")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_779")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_714")

    #C0001
    ChrTalk(
        0xA,
        (
            "虽然觉得重开矿山\x01",
            "还为时过早……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xA,
        (
            "但为了让镇上的各位\x01",
            "振奋起来，\x01",
            "也只有这个办法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xA,
        (
            "既然矿山已经重开，希望\x01",
            "老公他们都拼命努力吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_774")

    label("loc_714")


    #C0004
    ChrTalk(
        0xA,
        (
            "既然矿山已经重开，希望\x01",
            "老公他们都拼命努力吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xA,
        (
            "我也要做好美味的盒饭，\x01",
            "支持我老公才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_774")

    Jump("loc_107D")

    label("loc_779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_7F8")

    #C0006
    ChrTalk(
        0xA,
        (
            "亚雷库真是的，竟然满不在乎地\x01",
            "抚摸镇子附近的狼。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xA,
        (
            "虽说是协助反抗组织的\x01",
            "聪明动物……\x01",
            "但还是应该小心点啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_107D")

    label("loc_7F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_93C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CC")

    #C0008
    ChrTalk(
        0xA,
        (
            "现在的情况很不太平，\x01",
            "老公不用进矿山，\x01",
            "从某种意义上说，我倒是松了口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xA,
        (
            "可是，如果一直这样下去，\x01",
            "玛因兹就会越来越荒废萧条吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xA,
        (
            "总统也基本\x01",
            "不管市外，\x01",
            "今后到底会变成怎样呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_937")

    label("loc_8CC")


    #C0011
    ChrTalk(
        0xA,
        (
            "如果矿山一直封锁下去，\x01",
            "玛因兹就会越来越荒废萧条吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xA,
        (
            "总统也基本\x01",
            "不管市外，\x01",
            "今后到底会变成怎样呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_937")

    Jump("loc_107D")

    label("loc_93C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B2")

    #C0013
    ChrTalk(
        0xA,
        (
            "我老公在之前的占领事件中\x01",
            "受了点轻伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xA,
        (
            "虽说没什么\x01",
            "大碍……\x01",
            "但当时真是让人担心呀。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A0E")

    label("loc_9B2")


    #C0015
    ChrTalk(
        0xA,
        (
            "我老公已经回矿山工作了……\x01",
            "当时真是吓死我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xA,
        (
            "勇敢虽然是好事，\x01",
            "但也不能太鲁莽呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0E")

    Jump("loc_107D")

    label("loc_A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9F")

    #C0017
    ChrTalk(
        0xA,
        (
            "一到下雨天，矿山里\x01",
            "就会很冷呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xA,
        (
            "不过矿工们都穿着薄衣，\x01",
            "好像完全不在意。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xA,
        (
            "哎呀呀，只要别\x01",
            "感冒就好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AFA")

    label("loc_A9F")


    #C0020
    ChrTalk(
        0xA,
        (
            "一到下雨天，矿山里\x01",
            "就会很冷呢。\x01",
            "不过矿工们都穿着薄衣。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xA,
        (
            "哎呀呀，只要别\x01",
            "感冒就好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFA")

    Jump("loc_107D")

    label("loc_AFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B4B")

    #C0022
    ChrTalk(
        0xA,
        (
            "亚雷库真是的，\x01",
            "干嘛叫那么大声啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xA,
        (
            "真是\x01",
            "吵死人了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_107D")

    label("loc_B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C19")

    #C0024
    ChrTalk(
        0xA,
        (
            "我老公是矿山长，或许是受\x01",
            "他的影响，亚雷库也想当矿工。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xA,
        (
            "我原本是反对的……\x01",
            "但做父母的，不该过多干涉\x01",
            "孩子的梦想。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xA,
        (
            "我只要好好照顾他，\x01",
            "让他健康长大，\x01",
            "别受什么伤就行了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CAA")

    label("loc_C19")


    #C0027
    ChrTalk(
        0xA,
        (
            "我老公是矿山长，或许是受\x01",
            "他的影响，亚雷库也想当矿工。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xA,
        (
            "我原本是反对的……\x01",
            "但那孩子经过认真思考后才决定了\x01",
            "自己的理想，我应该默默支持他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CAA")

    Jump("loc_107D")

    label("loc_CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D3F")

    #C0029
    ChrTalk(
        0xA,
        (
            "我每天都担心亚雷库\x01",
            "会跑到危险的地方玩……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xA,
        (
            "不过，在主日学校的授课日，\x01",
            "有修女帮我照看他，\x01",
            "总算可以放心一些。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D96")

    label("loc_D3F")


    #C0031
    ChrTalk(
        0xA,
        (
            "在主日学校的授课日，\x01",
            "就不用太担心\x01",
            "孩子了……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xA,
        (
            "机会难得，\x01",
            "我就好好休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D96")

    Jump("loc_107D")

    label("loc_D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_F08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9C")

    #C0033
    ChrTalk(
        0xA,
        (
            "昨天我去给在矿山工作的\x01",
            "老公送饭……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xA,
        (
            "结果看到亚雷库\x01",
            "擅自跑进了矿山。\x01",
            "我自然是把他大骂一顿。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xA,
        (
            "我明明警告过他无数次了，\x01",
            "说那里很危险，绝不能进去。\x01",
            "那孩子可真是的……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        (
            "光是老公就够让我费神了，\x01",
            "别再让我操多余的心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F03")

    label("loc_E9C")


    #C0037
    ChrTalk(
        0xA,
        (
            "我明明警告过他无数次了，\x01",
            "说那里很危险，绝不能进去。\x01",
            "那孩子可真是的……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xA,
        (
            "真希望他能\x01",
            "再听话点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F03")

    Jump("loc_107D")

    label("loc_F08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F6A")

    #C0039
    ChrTalk(
        0xA,
        (
            "霍夫曼真是的，去矿山\x01",
            "竟然忘了带饭。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xA,
        (
            "他肚子应该饿了吧，\x01",
            "我得给他送去才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_107D")

    label("loc_F6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_107D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_102A")

    #C0041
    ChrTalk(
        0xA,
        (
            "我家孩子总是喜欢跑到\x01",
            "危险的地方，真是伤脑筋啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xA,
        (
            "今天早上也是，要不是冈兹阻止了他，\x01",
            "还不知道会出什么事呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xA,
        (
            "唉，真怕他以后到处乱跑，\x01",
            "最后受伤什么的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_107D")

    label("loc_102A")


    #C0044
    ChrTalk(
        0xA,
        (
            "我家孩子的好奇心非常旺盛，\x01",
            "总是喜欢跑到危险的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xA,
        "肯定是我老公遗传的。\x02",
    )

    CloseMessageWindow()

    label("loc_107D")

    TalkEnd(0xFE)
    Return()

    # Function_5_668 end

    def Function_6_1081(): pass

    label("Function_6_1081")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1092")
    Jump("loc_113D")

    label("loc_1092")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_10EE")

    #C0046
    ChrTalk(
        0xE,
        (
            "唉，下雨时就不能\x01",
            "出去玩了，好无聊啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xE,
        (
            "爸爸能不能早点回来\x01",
            "陪我玩啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_113D")

    label("loc_10EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_10FC")
    Jump("loc_113D")

    label("loc_10FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_110A")
    Jump("loc_113D")

    label("loc_110A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1118")
    Jump("loc_113D")

    label("loc_1118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1126")
    Jump("loc_113D")

    label("loc_1126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1134")
    Jump("loc_113D")

    label("loc_1134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_113D")

    label("loc_113D")

    TalkEnd(0xFE)
    Return()

    # Function_6_1081 end

    def Function_7_1141(): pass

    label("Function_7_1141")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1152")
    Jump("loc_135E")

    label("loc_1152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1211")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D3")

    #C0048
    ChrTalk(
        0x11,
        (
            "克洛斯贝尔市\x01",
            "那边好像出了\x01",
            "大事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x11,
        (
            "……我们矿工\x01",
            "也不能就这样干坐下去。\x01",
            "找镇长商量看看吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_120C")

    label("loc_11D3")


    #C0050
    ChrTalk(
        0x11,
        (
            "我们矿工也不能就这样干坐下去。\x01",
            "找镇长商量看看吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_120C")

    Jump("loc_135E")

    label("loc_1211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_135E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E4")

    #C0051
    ChrTalk(
        0x11,
        (
            "成为独立国以后，\x01",
            "七耀石的交易量剧减，\x01",
            "所以矿山暂时封锁了。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x11,
        (
            "因为和其它国家的贸易\x01",
            "已经完全停止了，\x01",
            "这也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x11,
        (
            "说实话，真是难以接受啊……\x01",
            "但现在也只能\x01",
            "静观其变了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_135E")

    label("loc_12E4")


    #C0054
    ChrTalk(
        0x11,
        (
            "成为独立国以后，\x01",
            "七耀石的交易量剧减，\x01",
            "所以矿山暂时封锁了。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x11,
        (
            "说实话，真是难以接受啊……\x01",
            "但现在也只能\x01",
            "静观其变了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_135E")

    TalkEnd(0xFE)
    Return()

    # Function_7_1141 end

    def Function_8_1362(): pass

    label("Function_8_1362")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1467")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_140B")

    #C0056
    ChrTalk(
        0xB,
        (
            "罗基回到矿山，\x01",
            "我也就放心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xB,
        (
            "虽然还不知道\x01",
            "克洛斯贝尔今后\x01",
            "会变成怎样……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xB,
        (
            "但只要年轻人们\x01",
            "脚踏实地的努力，\x01",
            "就一定能开拓未来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1462")

    label("loc_140B")


    #C0059
    ChrTalk(
        0xB,
        (
            "罗基回到矿山，\x01",
            "我也放心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xB,
        (
            "只要年轻人们\x01",
            "脚踏实地的努力，\x01",
            "就一定能开拓未来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1462")

    Jump("loc_1E79")

    label("loc_1467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_151D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14EA")

    #C0061
    ChrTalk(
        0xB,
        (
            "独立无效宣言发表之后，\x01",
            "总统的正当性\x01",
            "也受到了冲击……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xB,
        (
            "我们如今或许\x01",
            "正处于历史上的\x01",
            "重大分歧点。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1518")

    label("loc_14EA")


    #C0063
    ChrTalk(
        0xB,
        (
            "我们如今或许\x01",
            "正处于历史上的\x01",
            "重大分歧点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1518")

    Jump("loc_1E79")

    label("loc_151D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1625")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C8")

    #C0064
    ChrTalk(
        0xB,
        (
            "克洛斯贝尔的独立\x01",
            "竟然会发展成现在这种事态，\x01",
            "真是做梦也没想到啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xB,
        (
            "因为矿山被封锁了，\x01",
            "罗基似乎\x01",
            "彻底泄了气……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xB,
        "唉，该怎么办才好呢？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1620")

    label("loc_15C8")


    #C0067
    ChrTalk(
        0xB,
        (
            "罗基好不容易才提起干劲，\x01",
            "准备在矿山努力工作，\x01",
            "结果却……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xB,
        "唉，该怎么办才好呢？\x02",
    )

    CloseMessageWindow()

    label("loc_1620")

    Jump("loc_1E79")

    label("loc_1625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_169A")

    #C0069
    ChrTalk(
        0xB,
        (
            "没想到会像战争年代一样，\x01",
            "再次发生占领玛因兹\x01",
            "这样的事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xB,
        (
            "唉，克洛斯贝尔到底\x01",
            "会变成怎样呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E79")

    label("loc_169A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_17B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1748")

    #C0071
    ChrTalk(
        0xB,
        (
            "虽然最近去市里的人\x01",
            "越来越多了……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xB,
        (
            "但罗基等年轻人\x01",
            "还是以玛因兹镇\x01",
            "为荣的。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xB,
        (
            "对于长年居住在这镇上的\x01",
            "我来说，再没有比这\x01",
            "更加开心的事了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17B2")

    label("loc_1748")


    #C0074
    ChrTalk(
        0xB,
        (
            "罗基等年轻人\x01",
            "还是以玛因兹镇\x01",
            "为荣的。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xB,
        (
            "对于长年居住在这镇上的\x01",
            "我来说，再没有比这\x01",
            "更加开心的事了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17B2")

    Jump("loc_1E79")

    label("loc_17B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_18CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_186D")

    #C0076
    ChrTalk(
        0xB,
        (
            "自从罗基开始\x01",
            "认真工作之后，\x01",
            "每天似乎都过得很充实。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xB,
        (
            "呵呵，接下来，\x01",
            "只要再带个媳妇回来，\x01",
            "我也就能彻底安心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xB,
        (
            "呼，这或许还需要\x01",
            "好一段时间吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18C6")

    label("loc_186D")


    #C0079
    ChrTalk(
        0xB,
        (
            "要是罗基再带个\x01",
            "媳妇回来，\x01",
            "我也就能彻底安心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xB,
        (
            "呼，这或许还需要\x01",
            "好一段时间吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C6")

    Jump("loc_1E79")

    label("loc_18CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1A1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19AC")

    #C0081
    ChrTalk(
        0xB,
        "克洛斯贝尔独立……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xB,
        (
            "对于一直生活在这里的我来说，\x01",
            "感觉有些不现实。\x01",
            "但要是真能实现，那就太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xB,
        (
            "不过，帝国和共和国\x01",
            "肯定不会善罢甘休……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xB,
        (
            "希望独立这一决定不要成为\x01",
            "引发新战争的火种。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A17")

    label("loc_19AC")


    #C0085
    ChrTalk(
        0xB,
        (
            "克洛斯贝尔宣布独立，\x01",
            "帝国和共和国肯定不会\x01",
            "保持沉默。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xB,
        (
            "希望独立这一决定不要成为\x01",
            "引发新战争的火种。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A17")

    Jump("loc_1E79")

    label("loc_1A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1B6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AE6")

    #C0087
    ChrTalk(
        0xB,
        (
            "以前经常发生\x01",
            "山石塌方和泥石流\x01",
            "之类的事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xB,
        (
            "不过，在导力革命以后，\x01",
            "挖掘技术不断进步，\x01",
            "便很少再发生事故了。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xB,
        (
            "技术的进步确实可以拯救人类。\x01",
            "现在真是个美好的时代啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B69")

    label("loc_1AE6")


    #C0090
    ChrTalk(
        0xB,
        (
            "以前经常发生山石塌方\x01",
            "和泥石流之类的事故……\x01",
            "但最近几乎不会再发生了。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xB,
        (
            "技术的进步确实能拯救人类。\x01",
            "现在真是个美好的时代啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B69")

    Jump("loc_1E79")

    label("loc_1B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1C3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BF0")

    #C0092
    ChrTalk(
        0xB,
        (
            "亚米和罗基只要凑到\x01",
            "一起就吵闹个没完，\x01",
            "真拿他们没办法啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xB,
        (
            "呵呵，算啦，兄妹感情\x01",
            "亲密也是好事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C36")

    label("loc_1BF0")


    #C0094
    ChrTalk(
        0xB,
        "话说回来……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xB,
        (
            "希望他们两个不要\x01",
            "只知道玩，也帮我\x01",
            "做点家务事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C36")

    Jump("loc_1E79")

    label("loc_1C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1D3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC5")

    #C0096
    ChrTalk(
        0xB,
        (
            "我孙子罗基\x01",
            "最近不再偷懒，\x01",
            "开始认真工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xB,
        (
            "啊，再没有比这更令人开心的事了。\x01",
            "……空之女神啊，感谢您。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D37")

    label("loc_1CC5")


    #C0098
    ChrTalk(
        0xB,
        (
            "孙儿们能够\x01",
            "独当一面，\x01",
            "对我来说就是最开心的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xB,
        (
            "……空之女神啊，感谢您。\x01",
            "请您今后也继续\x01",
            "保佑那些孩子吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D37")

    Jump("loc_1E79")

    label("loc_1D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1E79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E0A")

    #C0100
    ChrTalk(
        0xB,
        (
            "镇子外面的旧矿山\x01",
            "是几十年前的主坑道。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xB,
        (
            "在它全盛期的时候，矿工们可以\x01",
            "从中轻松采掘出大颗的结晶，\x01",
            "简直就是座宝山啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xB,
        (
            "可以说那里是帝国和\x01",
            "共和国当年争斗不断\x01",
            "的理由之一。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E79")

    label("loc_1E0A")


    #C0103
    ChrTalk(
        0xB,
        (
            "虽然旧矿山被采掘殆尽，\x01",
            "现在已经变为废坑……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xB,
        (
            "但对过去的克洛斯贝尔\x01",
            "来说，那里绝对是个\x01",
            "非常重要的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E79")

    TalkEnd(0xFE)
    Return()

    # Function_8_1362 end

    def Function_9_1E7D(): pass

    label("Function_9_1E7D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1E8E")
    Jump("loc_1FFD")

    label("loc_1E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1F5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F29")

    #C0105
    ChrTalk(
        0xD,
        (
            "哎呀，你们\x01",
            "连伞都不打，\x01",
            "就在雨中到处走吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xD,
        "哦～原来如此，原来如此……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xD,
        (
            "……这正是\x01",
            "所谓的\x01",
            "『娇艳欲滴的美男子』吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1F57")

    label("loc_1F29")


    #C0108
    ChrTalk(
        0xD,
        (
            "你们正是\x01",
            "所谓的\x01",
            "『娇艳欲滴的美男子』啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F57")

    Jump("loc_1FFD")

    label("loc_1F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1F6A")
    Jump("loc_1FFD")

    label("loc_1F6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1F78")
    Jump("loc_1FFD")

    label("loc_1F78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1F86")
    Jump("loc_1FFD")

    label("loc_1F86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1FE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA1")
    Call(0, 10)
    Jump("loc_1FE1")

    label("loc_1FA1")


    #C0109
    ChrTalk(
        0xD,
        (
            "哥哥没有\x01",
            "什么绯闻，\x01",
            "真是无聊啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xD,
        "呼，不过我也差不多。\x02",
    )

    CloseMessageWindow()

    label("loc_1FE1")

    Jump("loc_1FFD")

    label("loc_1FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1FF4")
    Jump("loc_1FFD")

    label("loc_1FF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1FFD")

    label("loc_1FFD")

    TalkEnd(0xFE)
    Return()

    # Function_9_1E7D end

    def Function_10_2001(): pass

    label("Function_10_2001")

    OP_4B(0xD, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0111
    ChrTalk(
        0xD,
        (
            "喂喂，哥哥，\x01",
            "你有没有什么绯闻呀？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x10,
        (
            "有才怪，\x01",
            "女人太麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xD,
        "什么嘛，好无聊～\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xD,
        (
            "啊，那冈兹先生他们呢？\x01",
            "会不会在赌场跟漂亮的\x01",
            "兔女郎卿卿我我……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x10,
        "我怎么会知道！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x1, 2)
    OP_4C(0xD, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_10_2001 end

    def Function_11_20D1(): pass

    label("Function_11_20D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_20E2")
    Jump("loc_219D")

    label("loc_20E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_20F0")
    Jump("loc_219D")

    label("loc_20F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_20FE")
    Jump("loc_219D")

    label("loc_20FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_210C")
    Jump("loc_219D")

    label("loc_210C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_211A")
    Jump("loc_219D")

    label("loc_211A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2186")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2135")
    Call(0, 10)
    Jump("loc_2181")

    label("loc_2135")


    #C0116
    ChrTalk(
        0x10,
        (
            "真是的，和亚米说话\x01",
            "好累人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x10,
        (
            "难得的休假，\x01",
            "就让我好好休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2181")

    Jump("loc_219D")

    label("loc_2186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2194")
    Jump("loc_219D")

    label("loc_2194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_219D")

    label("loc_219D")

    TalkEnd(0xFE)
    Return()

    # Function_11_20D1 end

    def Function_12_21A1(): pass

    label("Function_12_21A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_22AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2240")

    #C0118
    ChrTalk(
        0xC,
        (
            "马库斯恢复了精神，\x01",
            "我也松了口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xC,
        (
            "矿工们果然还是在\x01",
            "专心工作的时候最迷人。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xC,
        (
            "我身为玛因兹的女人，\x01",
            "也要支持他们才是。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_22A9")

    label("loc_2240")


    #C0121
    ChrTalk(
        0xC,
        (
            "马库斯他们这些矿工，\x01",
            "果然还是在专心工作的\x01",
            "时候最迷人。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xC,
        (
            "我身为玛因兹的女人，\x01",
            "也要支持他们才是。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22A9")

    Jump("loc_2B65")

    label("loc_22AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_23D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2362")

    #C0123
    ChrTalk(
        0xC,
        (
            "反抗组织的成员好像\x01",
            "正在为某个计划做准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xC,
        (
            "……如果他们像那起占领事件时的\x01",
            "警备队员们一样负伤，\x01",
            "我们也会很心痛。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xC,
        "希望他们一定要多加小心啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_23CC")

    label("loc_2362")


    #C0126
    ChrTalk(
        0xC,
        (
            "……如果他们像那起占领事件时的\x01",
            "警备队员们一样负伤，\x01",
            "我们也会很心痛。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xC,
        "希望他们一定要多加小心啊。\x02",
    )

    CloseMessageWindow()

    label("loc_23CC")

    Jump("loc_2B65")

    label("loc_23D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_246F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23EC")
    Call(0, 13)
    Jump("loc_246A")

    label("loc_23EC")


    #C0128
    ChrTalk(
        0xC,
        (
            "马库斯无法\x01",
            "做自己喜欢的工作，\x01",
            "我也很难过……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xC,
        (
            "无论如何也得想些办法，\x01",
            "让他打起精神来，\x01",
            "再这样下去的话，他会憋出病的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_246A")

    Jump("loc_2B65")

    label("loc_246F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_253B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24F1")

    #C0130
    ChrTalk(
        0xC,
        (
            "听说为了救我们，\x01",
            "有很多警备队员\x01",
            "都牺牲了。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xC,
        (
            "他们的家人还在等着他们回去……\x01",
            "真是太令人悲痛了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2536")

    label("loc_24F1")


    #C0132
    ChrTalk(
        0xC,
        (
            "那些警备队员的家人\x01",
            "还在等着他们回去……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xC,
        "真是太令人悲痛了。\x02",
    )

    CloseMessageWindow()

    label("loc_2536")

    Jump("loc_2B65")

    label("loc_253B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2651")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25E8")

    #C0134
    ChrTalk(
        0xC,
        (
            "你们在下雨天来玛因兹，\x01",
            "可要多小心脚下。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xC,
        (
            "要是不小心打滑，\x01",
            "说不定会\x01",
            "坠下悬崖呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xC,
        (
            "在我和马库斯小的时候，\x01",
            "大人们也经常这样提醒我们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_264C")

    label("loc_25E8")


    #C0137
    ChrTalk(
        0xC,
        (
            "你们在下雨天来玛因兹，\x01",
            "可要多小心脚下。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xC,
        (
            "在我和马库斯小的时候，\x01",
            "大人们也经常这样提醒我们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_264C")

    Jump("loc_2B65")

    label("loc_2651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2778")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2703")

    #C0139
    ChrTalk(
        0xC,
        (
            "最近，我老公干起活来\x01",
            "异常起劲。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xC,
        (
            "冈兹先生和罗基先生\x01",
            "有了干劲，\x01",
            "似乎也激励了我老公呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xC,
        (
            "他每天早上出门更早了，\x01",
            "准备盒饭的我\x01",
            "也更加辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2773")

    label("loc_2703")


    #C0142
    ChrTalk(
        0xC,
        (
            "冈兹先生和罗基先生\x01",
            "有了干劲，\x01",
            "似乎也激励了我老公。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xC,
        (
            "他每天早上出门更早了，\x01",
            "准备盒饭的我\x01",
            "也更加辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2773")

    Jump("loc_2B65")

    label("loc_2778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2892")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_281C")

    #C0144
    ChrTalk(
        0xC,
        (
            "听说北边的山岳地带\x01",
            "出现了大型魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xC,
        (
            "那里离镇子也不远，\x01",
            "真担心魔兽会跑到矿山来。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xC,
        (
            "如果出现大型魔兽，\x01",
            "光靠矿工可对付不了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_288D")

    label("loc_281C")


    #C0147
    ChrTalk(
        0xC,
        (
            "听说北边的山岳地带\x01",
            "出现了大型魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xC,
        (
            "真担心魔兽会跑到矿山来。\x01",
            "如果出现大型魔兽，\x01",
            "光靠矿工可对付不了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_288D")

    Jump("loc_2B65")

    label("loc_2892")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_28FA")

    #C0149
    ChrTalk(
        0xC,
        (
            "克洛斯贝尔市似乎\x01",
            "正在开什么\x01",
            "通商会议。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xC,
        (
            "会议内容\x01",
            "会不会也影响到\x01",
            "玛因兹的未来呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B65")

    label("loc_28FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2971")

    #C0151
    ChrTalk(
        0xC,
        (
            "马库斯今天和\x01",
            "矿山长喝酒去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xC,
        (
            "他干活时总是比别人更加努力，\x01",
            "希望在休息时他能\x01",
            "好好转换一下心情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B65")

    label("loc_2971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2A87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A2E")

    #C0153
    ChrTalk(
        0xC,
        (
            "矿山中有时会出现\x01",
            "被七耀石吸引而来的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xC,
        (
            "对普通人来说是很危险的，\x01",
            "但玛因兹的矿工们\x01",
            "都是强壮的男子汉。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xC,
        (
            "只要不是太夸张的魔兽，\x01",
            "一般都可以自己解决。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A82")

    label("loc_2A2E")


    #C0156
    ChrTalk(
        0xC,
        (
            "玛因兹的矿工们\x01",
            "都是强壮的男子汉。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xC,
        (
            "一般出现在矿山的魔兽，\x01",
            "都能自己解决掉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A82")

    Jump("loc_2B65")

    label("loc_2A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2B65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B16")

    #C0158
    ChrTalk(
        0xC,
        (
            "我的老公\x01",
            "是矿工。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xC,
        (
            "在现在的年轻人当中，\x01",
            "他是最能干活的。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xC,
        (
            "好，今天也要\x01",
            "准备丰盛的晚饭，\x01",
            "等他回来享用。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B65")

    label("loc_2B16")


    #C0161
    ChrTalk(
        0xC,
        (
            "老公今天肯定\x01",
            "也会饿着肚子\x01",
            "回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xC,
        (
            "我要准备丰盛的晚饭，\x01",
            "等他回来享用。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B65")

    TalkEnd(0xFE)
    Return()

    # Function_12_21A1 end

    def Function_13_2B69(): pass

    label("Function_13_2B69")

    OP_4B(0xC, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0163
    ChrTalk(
        0x12,
        (
            "唉……除了挖矿之外，\x01",
            "我什么特长都没有，\x01",
            "现在却不能去矿山干活……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xC,
        (
            "马库斯，你也不要\x01",
            "太消沉啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xC,
        (
            "再过一阵子，\x01",
            "应该就可以进矿山了。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x12,
        (
            "但愿如此……\x01",
            "……………唉……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xC,
        "……真是的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0x12, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_13_2B69 end

    def Function_14_2C4A(): pass

    label("Function_14_2C4A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C5B")
    Jump("loc_2D1D")

    label("loc_2C5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2CCF")

    #C0168
    ChrTalk(
        0x12,
        (
            "不能进矿山干活，\x01",
            "我就只能在镇上\x01",
            "干些体力活了。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x12,
        (
            "但我还是\x01",
            "想进矿山啊……\x01",
            "不然怎么都提不起劲。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D1D")

    label("loc_2CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2D1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CEA")
    Call(0, 13)
    Jump("loc_2D1D")

    label("loc_2CEA")


    #C0170
    ChrTalk(
        0x12,
        (
            "唉……毕竟除了挖矿之外，\x01",
            "我什么特长都没有……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D1D")

    TalkEnd(0xFE)
    Return()

    # Function_14_2C4A end

    def Function_15_2D21(): pass

    label("Function_15_2D21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D38")
    Call(0, 24)
    Return()

    label("loc_2D38")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D57")
    Call(0, 16)
    Return()

    label("loc_2D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2E7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E20")

    #C0171
    ChrTalk(
        0x8,
        (
            "组建反抗组织的\x01",
            "各位警备队员好像\x01",
            "已经与国防军会合了。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x8,
        (
            "如今，总统已被拘捕……\x01",
            "他们完全没有\x01",
            "敌对的理由了。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x8,
        (
            "米蕾优他们的反抗行动\x01",
            "总算奏效了。\x01",
            "……我也松了一口气。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2E76")

    label("loc_2E20")


    #C0174
    ChrTalk(
        0x8,
        (
            "玛因兹也重新开放矿山，\x01",
            "恢复了以往的活力。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x8,
        (
            "但是，真正的战斗\x01",
            "从现在才开始啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E76")

    Jump("loc_3AA1")

    label("loc_2E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2FD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F4D")

    #C0176
    ChrTalk(
        0x8,
        (
            "总统的正当性遭到动摇，\x01",
            "听说国防军也在静观其变。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x8,
        (
            "米蕾优他们为了\x01",
            "解放克洛斯贝尔市，\x01",
            "好像正在逐步进行准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x8,
        (
            "……希望反抗组织的各位\x01",
            "顺利完成自己的使命，\x01",
            "我会向女神祈祷的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2FCF")

    label("loc_2F4D")


    #C0179
    ChrTalk(
        0x8,
        (
            "米蕾优他们为了\x01",
            "解放克洛斯贝尔市，\x01",
            "好像正在逐步进行准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x8,
        (
            "……希望反抗组织的各位\x01",
            "顺利完成自己的使命，\x01",
            "我会向女神祈祷的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FCF")

    Jump("loc_3AA1")

    label("loc_2FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_308E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FEF")
    Call(0, 17)
    Jump("loc_3089")

    label("loc_2FEF")


    #C0181
    ChrTalk(
        0x8,
        (
            "那个总统居然可以若无其事地\x01",
            "雇佣袭击过玛因兹居民的猎兵，\x01",
            "我们原本就无法信任他。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x8,
        (
            "努力抵抗，试图改善如今\x01",
            "这种体制的反抗组织成员们\x01",
            "就是我们的希望。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3089")

    Jump("loc_3AA1")

    label("loc_308E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_327B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3219")

    #C0183
    ChrTalk(
        0x8,
        "是你们啊……\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        (
            "#00003F比克森镇长……\x01",
            "玛因兹的情况也不容乐观吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x8,
        (
            "嗯……\x01",
            "虽然没有受到严重损害，\x01",
            "但大家都很受打击。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x8,
        (
            "游击士们也提供了协助，\x01",
            "目前要集中精力，\x01",
            "安抚大家的情绪。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        (
            "#00108F那起事件一定带给大家\x01",
            "相当大的冲击吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x8,
        (
            "嗯……不过现在\x01",
            "已经平静多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x8,
        (
            "总之，我身为镇长，\x01",
            "一定会努力做好\x01",
            "力所能及的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x8,
        (
            "你们应该也很辛苦，\x01",
            "好好加油吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18E, 2)
    Jump("loc_3276")

    label("loc_3219")


    #C0191
    ChrTalk(
        0x8,
        (
            "总之，我身为镇长，\x01",
            "一定会努力做好\x01",
            "力所能及的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x8,
        (
            "你们应该也很辛苦，\x01",
            "好好加油吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3276")

    Jump("loc_3AA1")

    label("loc_327B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_33D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_336D")

    #C0193
    ChrTalk(
        0x8,
        (
            "最近经常听说有人看见了\x01",
            "来历不明的大型魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x8,
        (
            "据说在昨天的脱轨事故中，\x01",
            "也有人目击到了巨大的怪物……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x8,
        (
            "会不会和以前出现在\x01",
            "旧矿山的那头大型魔兽\x01",
            "有关呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x8,
        (
            "……总之，为了大家的安全，\x01",
            "最好多加留意啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_33CF")

    label("loc_336D")


    #C0197
    ChrTalk(
        0x8,
        (
            "最近经常听说有人看见了\x01",
            "来历不明的大型魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "……总之，为了大家的安全，\x01",
            "最好多加留意啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33CF")

    Jump("loc_3AA1")

    label("loc_33D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_352F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34CB")

    #C0199
    ChrTalk(
        0x8,
        (
            "游击士们最近\x01",
            "似乎比以前更忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x8,
        (
            "若不是紧急性非常高的委托，\x01",
            "都不好意思拜托他们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x8,
        (
            "游击士们正在调查\x01",
            "最近突然出现的那些\x01",
            "来历不明的大型魔兽……\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x8,
        (
            "唔，我有种不祥的预感啊。\x01",
            "克洛斯贝尔似乎\x01",
            "发生了什么状况……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_352A")

    label("loc_34CB")


    #C0203
    ChrTalk(
        0x8,
        (
            "游击士们最近\x01",
            "越来越忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x8,
        (
            "唔，我有种不祥的预感啊。\x01",
            "克洛斯贝尔似乎\x01",
            "发生了什么状况……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_352A")

    Jump("loc_3AA1")

    label("loc_352F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_36A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_362A")

    #C0205
    ChrTalk(
        0x8,
        (
            "克洛斯贝尔独立……\x01",
            "没想到还能迎来\x01",
            "听到这种提案的一天啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x8,
        (
            "为了争夺矿山资源，帝国和共和国在\x01",
            "历史中一直争战不休。身为矿山镇的\x01",
            "居民，我们也应该认真讨论这个问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x8,
        (
            "希望镇上的每一位\x01",
            "居民都能认真思考\x01",
            "一下独立的利弊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_369B")

    label("loc_362A")


    #C0208
    ChrTalk(
        0x8,
        (
            "希望镇上的每一位\x01",
            "居民都能认真思考\x01",
            "一下独立的利弊。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x8,
        (
            "我身为居民之一，在投票日到来之前\x01",
            "也好好思考一番吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_369B")

    Jump("loc_3AA1")

    label("loc_36A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_37BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_375E")

    #C0210
    ChrTalk(
        0x8,
        "冈兹是个很豪爽的男人。\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x8,
        (
            "就算偶尔在巴鲁卡赢了几把，\x01",
            "也会把奖品分给大家，或请大家喝酒，\x01",
            "一下就把自己的成果挥霍光了。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x8,
        (
            "说不定比他输光回来的\x01",
            "花销还要大。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_37B6")

    label("loc_375E")


    #C0213
    ChrTalk(
        0x8,
        (
            "冈兹获胜而归时的花销，\x01",
            "说不定比他输光回来时\x01",
            "更多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x8,
        "不过，这正是他的性格啊。\x02",
    )

    CloseMessageWindow()

    label("loc_37B6")

    Jump("loc_3AA1")

    label("loc_37BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_38F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_388B")

    #C0215
    ChrTalk(
        0x8,
        (
            "超高层建筑\x01",
            "兰花塔吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x8,
        (
            "技术的进步\x01",
            "自然令人欣喜，\x01",
            "但心情还真是复杂。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x8,
        (
            "玛因兹镇好像\x01",
            "又落后于时代一步了。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x8,
        (
            "……哈哈，你们不用在意，\x01",
            "这只是我这老头子的自言自语罢了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38F4")

    label("loc_388B")


    #C0219
    ChrTalk(
        0x8,
        (
            "不管怎么说，通商会议的举办\x01",
            "有着重大的意义。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x8,
        (
            "为了自治州的未来，\x01",
            "希望迪塔市长他们\x01",
            "务必要加油啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38F4")

    Jump("loc_3AA1")

    label("loc_38F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3973")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3911")
    Jump("loc_396E")

    label("loc_3911")


    #C0221
    ChrTalk(
        0x8,
        (
            "保险起见，\x01",
            "就把旧矿山的钥匙\x01",
            "交给你们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x8,
        (
            "你们要是能偶尔去看看，\x01",
            "就真是帮了大忙啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_396E")

    Jump("loc_3AA1")

    label("loc_3973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_3AA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A2F")

    #C0223
    ChrTalk(
        0x8,
        (
            "出了矿山镇后，\x01",
            "先走一段下坡路，\x01",
            "再往西北走上去就是旧矿山了。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x8,
        (
            "我们也不清楚门为何会坏掉，\x01",
            "更不清楚坑道内究竟发生了\x01",
            "什么事。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x8,
        (
            "请各位一定要\x01",
            "多加小心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3AA1")

    label("loc_3A2F")


    #C0226
    ChrTalk(
        0x8,
        (
            "出了矿山镇后，\x01",
            "先走一段下坡路，\x01",
            "再往西北走上去就是旧矿山了。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x8,
        (
            "冈兹会给你们\x01",
            "打开入口的，\x01",
            "你们过去找他吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AA1")

    TalkEnd(0xFE)
    Return()

    # Function_15_2D21 end

    def Function_16_3AA5(): pass

    label("Function_16_3AA5")


    #C0228
    ChrTalk(
        0x8,
        (
            "前几天，我们把坏掉的旧矿山大门\x01",
            "换成了结实的新门。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x8,
        (
            "对了，保险起见\x01",
            "你们能不能收下这个？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0230
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x323),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x323, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0231
    ChrTalk(
        0x102,
        (
            "#00105F那个……这样好吗？\x01",
            "我们毕竟是外人……\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x8,
        "嗯，我相信你们。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x8,
        (
            "如果想调查什么，\x01",
            "就随意进去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x8,
        (
            "保险起见，我们还架设了梯子，\x01",
            "可以轻松进入最深处。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        (
            "#00000F非常感谢，\x01",
            "我们会妥善保管的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 3)
    TalkEnd(0x8)
    Return()

    # Function_16_3AA5 end

    def Function_17_3C21(): pass

    label("Function_17_3C21")

    OP_4B(0x8, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0236
    ChrTalk(
        0x8,
        (
            "唔，那么，粮食方面\x01",
            "就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x8,
        (
            "另外，为了维护装备，\x01",
            "还需要油之类的东西吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x8,
        (
            "贝卡莱的店里应该有\x01",
            "那些储备，你们去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x13,
        (
            "#07902F嗯，麻烦您了。\x02\x03",

            "#07908F……真不知该如何感谢\x01",
            "玛因兹的各位。\x02\x03",

            "#07903F如果你们协助我们的事\x01",
            "被国防军知道了，\x01",
            "恐怕会有危险……\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x8,
        (
            "哈哈，没什么……\x01",
            "你们不必介意。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x8,
        (
            "那个总统居然可以若无其事地\x01",
            "雇佣袭击过玛因兹居民的猎兵，\x01",
            "我们原本就无法信任他。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x8,
        (
            "在这种时候……你们这些\x01",
            "敢于对现状表达不满的\x01",
            "反抗军成员就是我们的希望。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x8,
        (
            "我们今后也会尽全力\x01",
            "协助你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x13,
        (
            "#07904F……非常感谢，\x01",
            "我们绝不会忘记大家的恩情。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 7)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x13, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_17_3C21 end

    def Function_18_3E6E(): pass

    label("Function_18_3E6E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3FDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F5C")

    #C0245
    ChrTalk(
        0x9,
        (
            "在漫长的抵抗作战中，\x01",
            "米蕾优小姐他们这些\x01",
            "警备队员真的很努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x9,
        (
            "在离开镇子的时候，\x01",
            "他们还对我们一再表达谢意……\x01",
            "其实，要道谢的应该是我们才对啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x9,
        (
            "等一切都平静下来之后，\x01",
            "一定要招待他们\x01",
            "再来玛因兹。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3FD6")

    label("loc_3F5C")


    #C0248
    ChrTalk(
        0x9,
        (
            "在漫长的抵抗作战中，\x01",
            "米蕾优小姐他们这些\x01",
            "警备队员真的很努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x9,
        (
            "等一切都平静下来之后，\x01",
            "一定要招待他们\x01",
            "再来玛因兹。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FD6")

    Jump("loc_4B61")

    label("loc_3FDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_40BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_406B")

    #C0250
    ChrTalk(
        0x9,
        (
            "米蕾优小姐他们\x01",
            "正在旅店休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x9,
        (
            "听他们说，\x01",
            "在不久之后将会更加忙碌……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x9,
        (
            "希望他们能趁此机会\x01",
            "好好休息一下。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_40B5")

    label("loc_406B")


    #C0253
    ChrTalk(
        0x9,
        (
            "米蕾优小姐他们\x01",
            "正在旅店休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x9,
        (
            "希望他们能趁此机会\x01",
            "好好休息一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40B5")

    Jump("loc_4B61")

    label("loc_40BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_41C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_418C")

    #C0255
    ChrTalk(
        0x9,
        (
            "听说反抗组织的各位在\x01",
            "地形复杂的山岳地带\x01",
            "扎了营。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x9,
        (
            "虽说他们早已适应了野外行动，但这种状态\x01",
            "要是长期持续下去，肯定还是很艰苦……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x9,
        (
            "真希望国防军和猎兵\x01",
            "不要搜捕得\x01",
            "那么频繁……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_41BC")

    label("loc_418C")


    #C0258
    ChrTalk(
        0x9,
        (
            "真希望国防军和猎兵\x01",
            "不要搜捕得\x01",
            "那么频繁……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41BC")

    Jump("loc_4B61")

    label("loc_41C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_42E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_427A")

    #C0259
    ChrTalk(
        0x9,
        (
            "不久前，艾欧莉娅小姐\x01",
            "分给我们一些可以让人\x01",
            "镇静下来的香草茶。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x9,
        (
            "多亏她的茶，在最近这一周，\x01",
            "我的心情真是平定了不少。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x9,
        (
            "真该感谢\x01",
            "艾欧莉娅小姐她们啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_42E4")

    label("loc_427A")


    #C0262
    ChrTalk(
        0x9,
        (
            "艾欧莉娅小姐她们\x01",
            "今天来帮我们消灭\x01",
            "出现在废坑中的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x9,
        (
            "帮了我们这么多忙，\x01",
            "真该好好\x01",
            "感谢她们啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42E4")

    Jump("loc_4B61")

    label("loc_42E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_43ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4382")

    #C0264
    ChrTalk(
        0x9,
        "山里的天气很易变。\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x9,
        (
            "要是天气太差，巴士都有\x01",
            "可能会停止运行。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x9,
        (
            "虽然今天没有下大暴雨，\x01",
            "但来往的时候还是要多加小心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_43E8")

    label("loc_4382")


    #C0267
    ChrTalk(
        0x9,
        (
            "要是天气太差，巴士都有\x01",
            "可能会停止运行。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x9,
        (
            "虽然今天没有下大暴雨，\x01",
            "但来往的时候还是要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43E8")

    Jump("loc_4B61")

    label("loc_43ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_44EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_448A")

    #C0269
    ChrTalk(
        0x9,
        (
            "很难给矿工们找到\x01",
            "相亲对象呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x9,
        (
            "冈兹、玛尔罗和罗基\x01",
            "好像都对相亲一事\x01",
            "不感兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x9,
        (
            "莫非最近的年轻人\x01",
            "都不向往结婚……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_44E7")

    label("loc_448A")


    #C0272
    ChrTalk(
        0x9,
        (
            "冈兹、玛尔罗和罗基\x01",
            "好像都对相亲一事\x01",
            "不感兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x9,
        (
            "莫非最近的年轻人\x01",
            "都不向往结婚……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44E7")

    Jump("loc_4B61")

    label("loc_44EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_463B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45BE")

    #C0274
    ChrTalk(
        0x9,
        (
            "按照规定，克洛斯贝尔要向\x01",
            "帝国和共和国缴纳\x01",
            "总计１０％的税收。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x9,
        (
            "在经济发达的克洛斯贝尔，\x01",
            "税收的１０％可是相当惊人的数额。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x9,
        (
            "可以说，这项规定正是\x01",
            "自治州从属于两大国的\x01",
            "象征。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4636")

    label("loc_45BE")


    #C0277
    ChrTalk(
        0x9,
        (
            "按照规定，克洛斯贝尔要向\x01",
            "帝国和共和国缴纳\x01",
            "总计１０％的税收。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x9,
        (
            "可以说，这项规定正是\x01",
            "自治州从属于两大国的\x01",
            "象征。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4636")

    Jump("loc_4B61")

    label("loc_463B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_47F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4783")

    #C0279
    ChrTalk(
        0x9,
        "哎呀，这位小姑娘……\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x9,
        (
            "如果不介意的话，\x01",
            "要不要和玛因兹的矿工\x01",
            "见面相亲？\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x103,
        (
            "#00205F……莫非您\x01",
            "是在问我吗？\x02\x03",

            "我还没到可以\x01",
            "结婚的年龄呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x9,
        (
            "呵呵，但你长得\x01",
            "真是很漂亮啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x9,
        (
            "如果你长大之后还是没有对象，\x01",
            "请务必考虑一下哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x103,
        "#00211F（……听起来有些别扭呢。）\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        "#00012F（哈、哈哈……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_47EC")

    label("loc_4783")


    #C0286
    ChrTalk(
        0x9,
        (
            "呵呵，如果你长大之后\x01",
            "还是没有对象，\x01",
            "请务必考虑一下哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x9,
        (
            "像你这样可爱的孩子，\x01",
            "我们是热烈欢迎的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47EC")

    Jump("loc_4B61")

    label("loc_47F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4857")

    #C0288
    ChrTalk(
        0x9,
        "矿工们今天停工。\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x9,
        (
            "你们想进矿山也没问题。\x01",
            "不过，如果要进去的话，\x01",
            "请小心魔兽哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B61")

    label("loc_4857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4A36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49D9")

    #C0290
    ChrTalk(
        0x9,
        "对了……你们两个。\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x9,
        (
            "要不要和玛因兹的矿工们\x01",
            "见面相亲？\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x102,
        "#00105F相、相亲吗？\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x9,
        (
            "嗯，像冈兹他们，\x01",
            "如果有人在家里等着，\x01",
            "肯定会工作得更加努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x9,
        "怎么样啊？二位小姑娘。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x102,
        (
            "#00106F呃，那个……不好意思，\x01",
            "我还没有考虑结婚问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x109,
        (
            "#10106F我、我也是，\x01",
            "现在要以工作为重……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x9,
        "是吗……真遗憾啊。\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x9,
        (
            "算啦，如果以后改变主意了，\x01",
            "不妨考虑一下。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4A31")

    label("loc_49D9")


    #C0299
    ChrTalk(
        0x9,
        (
            "如果以后改变主意了，\x01",
            "不妨考虑一下相亲的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x9,
        (
            "我会全力张罗，\x01",
            "为你们安排见面的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A31")

    Jump("loc_4B61")

    label("loc_4A36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_4B61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AF6")

    #C0301
    ChrTalk(
        0x9,
        (
            "那座旧矿山中的坑道\x01",
            "是在数十年前的战争\x01",
            "年代中使用的。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x9,
        (
            "里面的地势复杂又危险，\x01",
            "听说上一代人\x01",
            "将其严密封锁了……\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x9,
        (
            "究竟是谁弄坏了锁呢？\x01",
            "感觉有点后背发冷……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4B61")

    label("loc_4AF6")


    #C0304
    ChrTalk(
        0x9,
        (
            "那座旧矿山的\x01",
            "内部地势复杂又危险，\x01",
            "所以被严密封锁了……\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x9,
        (
            "究竟是谁弄坏了锁呢？\x01",
            "感觉有点后背发冷……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B61")

    TalkEnd(0xFE)
    Return()

    # Function_18_3E6E end

    def Function_19_4B65(): pass

    label("Function_19_4B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B7C")
    Call(0, 24)
    Return()

    label("loc_4B7C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4B8D")
    Jump("loc_4C5B")

    label("loc_4B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4B9B")
    Jump("loc_4C5B")

    label("loc_4B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4BA9")
    Jump("loc_4C5B")

    label("loc_4BA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4BB7")
    Jump("loc_4C5B")

    label("loc_4BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4BC5")
    Jump("loc_4C5B")

    label("loc_4BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4BD3")
    Jump("loc_4C5B")

    label("loc_4BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4C52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BEB")
    Jump("loc_4C4D")

    label("loc_4BEB")


    #C0306
    ChrTalk(
        0xF,
        (
            "竟然大量采购\x01",
            "那么大颗的七耀石，\x01",
            "这可不是普通商人能做到的。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xF,
        "……那些人到底是什么来头啊？\x02",
    )

    CloseMessageWindow()

    label("loc_4C4D")

    Jump("loc_4C5B")

    label("loc_4C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_4C5B")

    label("loc_4C5B")

    TalkEnd(0xFE)
    Return()

    # Function_19_4B65 end

    def Function_20_4C5F(): pass

    label("Function_20_4C5F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4C70")
    Jump("loc_4E37")

    label("loc_4C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4C7E")
    Jump("loc_4E37")

    label("loc_4C7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4E37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C99")
    Call(0, 17)
    Jump("loc_4E37")

    label("loc_4C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DCC")

    #C0308
    ChrTalk(
        0x13,
        (
            "#07903F虽然现在的情况依旧很艰苦，\x01",
            "但我们暂时会在山岳地带\x01",
            "努力下去的。\x02\x03",

            "#07901F兰迪，支援科的各位……\x01",
            "这里就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x104,
        (
            "#00303F嗯，明白了。\x02\x03",

            "#00301F……可别输给\x01",
            "猎兵和国防军哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x104, 500)

    #C0310
    ChrTalk(
        0x13,
        (
            "#07902F呵呵，你在小看我吗？\x02\x03",

            "#07904F放心吧，玛因兹的各位\x01",
            "也都在协助我们，\x01",
            "一定没问题的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4E37")

    label("loc_4DCC")


    #C0311
    ChrTalk(
        0x13,
        (
            "#07900F兰迪，支援科的各位……\x01",
            "这里就交给我们吧。\x02\x03",

            "#07904F玛因兹的各位\x01",
            "也都在协助我们，\x01",
            "一定没问题的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E37")

    TalkEnd(0xFE)
    Return()

    # Function_20_4C5F end

    def Function_21_4E3B(): pass

    label("Function_21_4E3B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4F82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F07")

    #C0312
    ChrTalk(
        0x14,
        (
            "得到了神狼的协助后，\x01",
            "我们就可以更加轻松地行动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x14,
        (
            "监视山道、警戒山岳地带的任务\x01",
            "都可以交给它们，\x01",
            "我们的负担减轻了很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x14,
        (
            "希望米蕾优三尉能趁此机会\x01",
            "好好休息一下。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_4F82")

    label("loc_4F07")


    #C0315
    ChrTalk(
        0x14,
        (
            "监视山道、警戒山岳地带的任务\x01",
            "都可以交给神狼它们，\x01",
            "我们的负担减轻了很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x14,
        (
            "希望米蕾优三尉能趁此机会\x01",
            "好好休息一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F82")

    TalkEnd(0xFE)
    Return()

    # Function_21_4E3B end

    def Function_22_4F86(): pass

    label("Function_22_4F86")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4FD0")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x1555), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4FA6")
    Sleep(1500)
    Jump("loc_4FBB")

    label("loc_4FA6")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2500)

    label("loc_4FBB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4000), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4FCB")
    Sleep(333)

    label("loc_4FCB")

    Jump("Function_22_4F86")

    label("loc_4FD0")

    Return()

    # Function_22_4F86 end

    def Function_23_4FD1(): pass

    label("Function_23_4FD1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30700.itc", 0x1E)
    LoadChrToIndex("chr/ch30702.itc", 0x1F)
    LoadChrToIndex("chr/ch00002.itc", 0x20)
    LoadChrToIndex("chr/ch00102.itc", 0x21)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("chr/ch03002.itc", 0x23)
    OP_68(560, 2250, -1210, 0)
    MoveCamera(312, 18, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x101, 700, 750, -8600, 0)
    SetChrPos(0x102, -500, 750, -8600, 0)
    SetChrPos(0x109, 700, 750, -10000, 0)
    SetChrPos(0x105, -500, 750, -10000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, -250, 650, -1000, 90)
    SetChrChipByIndex(0x8, 0x0)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 600, 750, -500, 135)
    OP_4B(0xF, 0xFF)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2000, 750, -1000, 270)
    FadeToBright(1000, 0)
    SetCameraDistance(34000, 1500)
    BeginChrThread(0x9, 1, 0, 22)
    Sleep(300)
    BeginChrThread(0xF, 1, 0, 22)
    Sleep(300)
    BeginChrThread(0x8, 1, 0, 22)
    OP_0D()
    Sleep(500)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x8, 0x1)
    Sound(103, 0, 100, 0)
    Sleep(300)

    #C0317
    ChrTalk(
        0x101,
        (
            "#2P打扰了，我们是克洛斯贝尔\x01",
            "警察局·特别任务支援科的成员。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetCameraDistance(34000, 4000)
    MoveCamera(315, 30, 0, 4000)
    OP_68(-1500, 250, 0, 4000)

    def lambda_51ED():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_51ED)
    Sleep(50)

    def lambda_51FD():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_51FD)
    Sleep(50)

    def lambda_520D():
        OP_93(0xF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_520D)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xF, 0)
    Sleep(500)

    def lambda_522C():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_522C)

    def lambda_5246():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5246)
    Sleep(100)

    def lambda_525A():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_525A)

    def lambda_5274():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5274)
    Sleep(50)

    def lambda_5288():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5288)

    def lambda_52A2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_52A2)
    Sleep(80)

    def lambda_52B6():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_52B6)

    def lambda_52D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_52D0)
    Sleep(2000)
    Sound(104, 0, 100, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x1)

    #C0318
    ChrTalk(
        0x8,
        (
            "#11P呀，是你们。\x01",
            "麻烦你们特地前来，真是不好意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xF,
        "#2P哟，有一阵子没见啦！\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        "#00002F#6P各位，好久不见了。\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x102,
        (
            "#00100F#6P冈兹先生……\x01",
            "您的身体状况怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xF,
        (
            "#2P哦，没留下什么后遗症，\x01",
            "精神很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xF,
        (
            "#2P当时真是多亏了你们，\x01",
            "请让我再次道谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x102,
        "#00109F#6P呵呵，身体健康就再好不过了。\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x101,
        (
            "#00001F#6P对了……\x01",
            "听说『旧矿山』中\x01",
            "出现了魔兽？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x8,
        (
            "#11P嗯，那是一座位于\x01",
            "镇子附近，已经荒废了\x01",
            "好几十年的废坑……\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x9,
        (
            "#11P好啦，别站着说话，\x01",
            "大家先坐下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x9,
        "#11P我这就给你们泡茶。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_68(1260, 2200, 3060, 0)
    MoveCamera(322, 21, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33750, 0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 2450, 950, 2780, 270)
    SetChrPos(0x102, 2450, 950, 3780, 270)
    SetChrPos(0x109, 1250, 850, 1500, 0)
    SetChrPos(0x105, 250, 850, 1500, 0)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x1)
    SetChrPos(0xF, 800, 950, 5100, 180)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -800, 950, 2780, 90)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -800, 950, 3780, 90)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0329
    AnonymousTalk(
        0x101,
        (
            "#00005F封锁着的入口大门\x01",
            "被人破坏了？\x02",
        )
    )

    CloseMessageWindow()
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(1260, 1950, 3070, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0330
    ChrTalk(
        0x8,
        (
            "#5P嗯，虽说是几十年前的门，\x01",
            "但还是十分结实的。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x8,
        (
            "#5P今天镇上的人\x01",
            "却发现它被破坏了……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xF,
        (
            "#5P两天之前都还没什么异常，\x01",
            "所以多半是在昨天被破坏的。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xF,
        (
            "#5P真是的，竟然会有人\x01",
            "如此胡作非为！\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        "#00003F#12P……真令人在意啊。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x109,
        (
            "#10108F#6P委托中还曾提到，镇上的人进去查看，\x01",
            "发现有魔兽在里面游荡……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x105,
        (
            "#10305F#6P不过，既然是古老的废弃坑道，\x01",
            "出现魔兽也不足为奇吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x8,
        "#5P不，问题并不在这里。\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        (
            "#5P令人奇怪的是\x01",
            "坑道本身。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        "#00105F#12P坑道本身……？\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xF,
        (
            "#5P怎么说呢……\x01",
            "里面散发着朦胧的光。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xF,
        (
            "#5P整个山壁都被映照\x01",
            "成了一片紫红色……\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x102,
        (
            "#00106F#12P这、这……\x01",
            "的确很诡异呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        (
            "#00008F#12P既然是几十年前的坑道，\x01",
            "里面自然不会有导力灯。\x02\x03",

            "#00001F发光的原因\x01",
            "确实很令人在意……\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x8,
        (
            "#5P嗯，虽然没有对本镇造成实际损害，\x01",
            "但实在是有点放心不下。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x9,
        (
            "#5P所以还是在各位百忙之中\x01",
            "联络了你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        "#00003F#12P我已经了解情况了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(200)

    #C0347
    ChrTalk(
        0x101,
        (
            "#00001F#12P从大门遭到破坏这一点来看，\x01",
            "应该不是普通的意外。\x02\x03",

            "我们这就去看看情况吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x102,
        "#00101F#11P嗯，明白了。\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x109,
        "#10101F#6P明白！\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x105,
        (
            "#10302F#6P呵呵……\x01",
            "这起事件似乎很有意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x8,
        (
            "#5P谢谢大家，\x01",
            "那就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(250)

    #C0352
    ChrTalk(
        0x8,
        (
            "#5P冈兹，你先去把入口\x01",
            "前面的路障撤除吧。\x02",
        )
    )

    Sleep(50)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x109, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)
    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xF,
        "#5P嗯，知道了。\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xF,
        (
            "#5P那我就先走一步了，\x01",
            "你们准备好了再来吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, -630, 750, 5180, 270)
    Sleep(500)
    OP_95(0xF, -2150, 750, 4460, 2500, 0x0)

    def lambda_5B74():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD6FC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5B74)
    OP_68(80, 1950, 2060, 3000)
    Sleep(600)
    SetChrSubChip(0x8, 0x2)
    Sleep(100)
    SetChrSubChip(0x9, 0x2)
    Sleep(200)
    SetChrSubChip(0x109, 0x1)
    Sleep(100)
    SetChrSubChip(0x105, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x101, 0x0)
    Sleep(2500)
    Sound(103, 0, 100, 0)
    Sleep(600)
    Sound(104, 0, 100, 0)
    OP_68(1080, 1950, 3060, 1200)
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(150)
    SetChrSubChip(0x9, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)
    Sleep(150)
    OP_6F(0x1)
    WaitChrThread(0xF, 1)
    SetChrFlags(0xF, 0x80)

    #C0355
    ChrTalk(
        0x101,
        (
            "#00002F#12P……太好了，\x01",
            "他似乎真的很健康。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x8,
        "#5P嗯，这多亏了你们啊。\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x8,
        (
            "#5P不过，他嗜赌的坏习惯\x01",
            "完全没有改变。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x8,
        (
            "#5P一到休息日，还是会跑到巴鲁卡，\x01",
            "直到全部输光才回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x102,
        "#00109F#12P呵呵，这样啊。\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x101,
        (
            "#00004F#12P算啦，只要不输到倾家荡产\x01",
            "就没什么问题……\x02\x03",

            "#00005F对了，旧矿山就在\x01",
            "离矿山镇不远的地方吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x9,
        (
            "#5P嗯，先走一段下坡路，\x01",
            "再往西北走上去就到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x8,
        (
            "#5P目前还不知道事情的原因，\x01",
            "各位千万要小心啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_49()
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x8, -890, 950, 3320, 90)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, -6530, 750, 60, 270)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    BeginChrThread(0x9, 0, 0, 0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetChrPos(0x0, -250, 750, -750, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x12A, 0)
    OP_29(0xA2, 0x4, 0x2)
    OP_29(0xA2, 0x1, 0x0)
    ClearMapFlags(0x10000000)
    EventEnd(0x5)
    Return()

    # Function_23_4FD1 end

    def Function_24_5E7F(): pass

    label("Function_24_5E7F")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1850, 750, -1060, 0)
    MoveCamera(316, 22, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(37200, 0)
    SetChrPos(0x101, 700, 750, -3300, 0)
    SetChrPos(0x102, -500, 750, -3300, 0)
    SetChrPos(0x104, 700, 750, -4500, 0)
    SetChrPos(0x109, -500, 750, -4500, 0)
    SetChrPos(0x105, 100, 750, -5700, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_0D()

    #C0363
    ChrTalk(
        0x8,
        (
            "#5P唔……\x01",
            "那些人到底是……\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xF,
        (
            "算啦，也不用\x01",
            "想得太复杂吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xF,
        "反正我们赚了钱。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x8,
        (
            "#5P不，之前那起事件的犯人\x01",
            "至今都没能查明，\x01",
            "还是谨慎一些为好……\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x101,
        (
            "#6P#00000F嗯……\x01",
            "镇长、冈兹先生，\x01",
            "你们好。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6017():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6017)
    Sleep(50)
    OP_93(0xF, 0xB4, 0x1F4)

    #C0368
    ChrTalk(
        0x8,
        "#11P哦哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xF,
        (
            "不好意思，我们正在谈论事情，\x01",
            "没注意到你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x102,
        (
            "#00105F莫非……\x01",
            "正在谈论旧矿山的那起事件吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x8,
        (
            "#11P不，关于那件事情，\x01",
            "警备队的人之后\x01",
            "也来巡逻过几次……\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x8,
        (
            "#11P但至今都没能查明\x01",
            "埋设炸药的犯人和\x01",
            "坑道异常之谜。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xF,
        (
            "#11P我们已经换下了坏掉的门，\x01",
            "重新装上了结实的新门，\x01",
            "把旧矿山严密封锁起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x109,
        (
            "#6P#10104F如此一来，\x01",
            "就不必担心\x01",
            "有人误闯进去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x8,
        (
            "#11P……但是，又有别的事\x01",
            "让人放心不下了。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x8,
        (
            "#11P其实，就在前一阵子，\x01",
            "有一群奇怪的人出现在了玛因兹……\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x8,
        (
            "#11P那些人出高价买下\x01",
            "大量大颗的七耀石结晶。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x109,
        "#6P#10105F一群奇怪的人……？\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x8,
        (
            "#11P怎么说呢，总之就是\x01",
            "有种不寻常的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x8,
        (
            "#11P带头的是个身材魁梧的\x01",
            "红发中年男性……\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x8,
        (
            "#11P哦哦，说起那头红发，\x01",
            "好像和兰迪的发色\x01",
            "一模一样啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0382
    ChrTalk(
        0x102,
        "#00105F（这……）\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x101,
        "#00005F#6P（『赤色星座』……！？）\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x104,
        (
            "#6P#00303F……他们除了\x01",
            "采购七耀石之外，\x01",
            "还做了什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x8,
        (
            "#11P不，并没有什么\x01",
            "特别可疑的行动……\x01",
            "只是看起来完全不像贸易商的样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x8,
        (
            "#11P破坏旧矿山大门的人\x01",
            "至今都没能查明，\x01",
            "所以有些在意……\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x109,
        (
            "#6P#10105F（据兰迪前辈说，\x01",
            "  埋设炸药的犯人\x01",
            "  应该就是他们……）\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x105,
        (
            "#6P#10303F（嗯，但是没有确凿证据，\x01",
            "  还是不要说出来了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x102,
        (
            "#00108F（话说回来，猎兵团\x01",
            "  采购七耀石的结晶，\x01",
            "  要用来做什么呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x104,
        (
            "#6P#00301F（……他们的『深红商会』\x01",
            "  和很多黑市商人\x01",
            "  有所勾结。）\x02\x03",

            "#00303F（如果通过他们的地下渠道\x01",
            "  来贩卖大颗的七耀石，\x01",
            "  应该能赚上一笔小钱吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x101,
        "#11P#00001F（原、原来如此……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0392
    ChrTalk(
        0x8,
        "#11P……唔，对了。\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x8,
        (
            "#11P还是把这个\x01",
            "交给你们比较好。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xF, 500)

    #C0394
    ChrTalk(
        0x8,
        "#5P冈兹，给他们吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x8, 500)

    #C0395
    ChrTalk(
        0xF,
        "嗯，知道了。\x02",
    )

    CloseMessageWindow()

    def lambda_6692():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_6692)
    Sleep(50)
    OP_93(0x8, 0xB4, 0x1F4)

    #C0396
    ChrTalk(
        0xF,
        "来，请收下吧。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0397
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x323),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x323, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0398
    ChrTalk(
        0x101,
        "#00005F#6P这是旧矿山的……？\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xF,
        "嗯，是备用钥匙。\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x102,
        (
            "#00105F那个……这样好吗？\x01",
            "我们毕竟是外人……\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x8,
        "嗯，我相信你们。\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x8,
        (
            "如果想调查什么，\x01",
            "就随意进去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x8,
        (
            "保险起见，我们还架设了梯子，\x01",
            "可以轻松进入最深处。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x101,
        (
            "#6P#00000F非常感谢，\x01",
            "我们会妥善使用的。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0x8, 0xF, 0)
    TurnDirection(0xF, 0x8, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x14F, 2)
    OP_29(0xA3, 0x1, 0x3)
    SetChrPos(0x0, 0, 750, -3500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_24_5E7F end

    SaveToFile()

Try(main)
