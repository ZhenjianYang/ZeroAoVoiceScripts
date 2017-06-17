from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e0510.bin",                # FileName
        "e0510",                    # MapName
        "e0510",                    # Location
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
        "e0510",                  # 0
        "艾莉",                   # 1
        "诺艾尔",                 # 2
        "兰迪",                   # 3
        "萨尔莎乘务员",           # 4
        "市民",                   # 5
        "游客",                   # 6
        "游客",                   # 7
        "梅尔斯",                 # 8
        "利玛",                   # 9
        "柯洛娜",                 # 10
        "芙兰",                   # 11
        "塞茜尔",                 # 12
        "伊莉娅",                 # 13
        "莉夏",                   # 14
        "修利",                   # 15
        "玛丽亚贝尔",             # 16
        "蔡特",                   # 17
        "SE控制",                 # 18
    ))

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch02900.itc",                   # 01
        "chr/ch00302.itc",                   # 02
        "chr/ch28400.itc",                   # 03
        "chr/ch33002.itc",                   # 04
        "chr/ch20402.itc",                   # 05
        "chr/ch22102.itc",                   # 06
        "chr/ch26202.itc",                   # 07
        "chr/ch22702.itc",                   # 08
        "chr/ch20702.itc",                   # 09
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
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    388,  0x0, 1,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(-100,    0,       -15420,  0,    389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-2450,   150,     -3799,   180,  453,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-2450,   150,     -6449,   180,  453,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-3450,   150,     -6449,   180,  453,  0x0, 0,   6,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-3049,   150,     -11350,  180,  389,  0x0, 0,   7,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-3750,   150,     -11350,  180,  389,  0x0, 0,   9,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-2250,   150,     -11350,  180,  389,  0x0, 0,   8,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(844, 0)                                        # 0

    ScpFunction((
        "Function_0_34C",          # 00, 0
        "Function_1_3FC",          # 01, 1
        "Function_2_4FF",          # 02, 2
        "Function_3_554",          # 03, 3
        "Function_4_82C",          # 04, 4
        "Function_5_A5E",          # 05, 5
        "Function_6_D04",          # 06, 6
        "Function_7_E61",          # 07, 7
        "Function_8_F22",          # 08, 8
        "Function_9_FAA",          # 09, 9
        "Function_10_1008",        # 0A, 10
        "Function_11_116F",        # 0B, 11
        "Function_12_12E4",        # 0C, 12
        "Function_13_134F",        # 0D, 13
        "Function_14_2453",        # 0E, 14
        "Function_15_3215",        # 0F, 15
        "Function_16_323D",        # 10, 16
        "Function_17_3265",        # 11, 17
    ))


    def Function_0_34C(): pass

    label("Function_0_34C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_384"),
        (1, "loc_390"),
        (2, "loc_39C"),
        (3, "loc_3A8"),
        (4, "loc_3B4"),
        (5, "loc_3C0"),
        (6, "loc_3CC"),
        (SWITCH_DEFAULT, "loc_3D8"),
    )


    label("loc_384")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_390")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_39C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3A8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3B4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3C0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3FB")

    Return()

    # Function_0_34C end

    def Function_1_3FC(): pass

    label("Function_1_3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EF")
    SetChrPos(0x8, 630, -1000, 9000, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, -620, -1000, 9000, 90)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, 3250, 150, -9100, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x80)
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
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x9)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)
    SetChrSubChip(0x10, 0x2)

    label("loc_4EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_4FE")
    ClearScenarioFlags(0x22, 0)
    Event(0, 17)

    label("loc_4FE")

    Return()

    # Function_1_3FC end

    def Function_2_4FF(): pass

    label("Function_2_4FF")

    Sound(480, 1, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_533")
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_553")
    SetChrSubChip(0xA, 0x1)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_553")

    Return()

    # Function_2_4FF end

    def Function_3_554(): pass

    label("Function_3_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56B")
    Call(0, 13)
    Return()

    label("loc_56B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_57C")
    Jump("loc_828")

    label("loc_57C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_58A")
    Jump("loc_828")

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_598")
    Jump("loc_828")

    label("loc_598")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_5A8")
    Jump("loc_828")

    label("loc_5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_5B6")
    Jump("loc_828")

    label("loc_5B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_5C4")
    Jump("loc_828")

    label("loc_5C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_5D2")
    Jump("loc_828")

    label("loc_5D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_5E0")
    Jump("loc_828")

    label("loc_5E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_828")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F8")
    Jump("loc_828")

    label("loc_5F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CB")

    #C0001
    ChrTalk(
        0x8,
        (
            "#00100F难得有机会过来度假，\x01",
            "不尽情享受可就太亏了。\x02\x03",

            "#00104F贝尔说，她给我们\x01",
            "准备了很多惊喜……\x02\x03",

            "#00102F呵呵，一想到这里，\x01",
            "真是很期待呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#00012F惊喜吗……\x01",
            "我倒是有点担心。\x02\x03",

            "#00003F如果她动员米修拉姆的所有\x01",
            "工作人员一起招待我们，\x01",
            "实在是消受不起呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "#00109F不、不管贝尔有多讲究排场，\x01",
            "应该也不会那么夸张吧……\x02\x03",

            "#00103F……虽然我也不能断言。\x02\x03",

            "#00102F总、总之就向女神祈祷，\x01",
            "希望她不要做出一些奇怪的事情吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#00006F（真、真担心啊……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_828")

    label("loc_7CB")


    #C0005
    ChrTalk(
        0x8,
        (
            "#00103F唔……话说回来，\x01",
            "贝尔说的惊喜究竟是什么呢？\x02\x03",

            "#00111F……但愿不是什么奇怪的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_828")

    TalkEnd(0xFE)
    Return()

    # Function_3_554 end

    def Function_4_82C(): pass

    label("Function_4_82C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_843")
    Call(0, 13)
    Return()

    label("loc_843")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_854")
    Jump("loc_A5A")

    label("loc_854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_862")
    Jump("loc_A5A")

    label("loc_862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_870")
    Jump("loc_A5A")

    label("loc_870")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_880")
    Jump("loc_A5A")

    label("loc_880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_88E")
    Jump("loc_A5A")

    label("loc_88E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_89C")
    Jump("loc_A5A")

    label("loc_89C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_8AA")
    Jump("loc_A5A")

    label("loc_8AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_8B8")
    Jump("loc_A5A")

    label("loc_8B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_A5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D0")
    Jump("loc_A5A")

    label("loc_8D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A02")

    #C0006
    ChrTalk(
        0x9,
        (
            "#10105F说起来，赛尔盖科长\x01",
            "没有一起来，真是遗憾啊。\x02\x03",

            "#10106F虽说他满不在乎地对\x01",
            "咱们说『玩得开心些』，\x01",
            "但总觉得有些对不住他……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#00003F毕竟科长的工作很繁忙……\x02\x03",

            "#00002F哈哈，不过，说不定他只是\x01",
            "害羞而已，不想让我们\x01",
            "看到他日常生活中的样子吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        "#10109F啊哈哈，那可能会很有趣的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_A5A")

    label("loc_A02")


    #C0009
    ChrTalk(
        0x9,
        (
            "#10103F赛尔盖科长没有一起来，\x01",
            "真是遗憾啊。\x02\x03",

            "#10102F他现在应该在支援科\x01",
            "独自吸烟吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5A")

    TalkEnd(0xFE)
    Return()

    # Function_4_82C end

    def Function_5_A5E(): pass

    label("Function_5_A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A75")
    Call(0, 14)
    Return()

    label("loc_A75")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_A86")
    Jump("loc_D00")

    label("loc_A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A94")
    Jump("loc_D00")

    label("loc_A94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_AA2")
    Jump("loc_D00")

    label("loc_AA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_AB0")
    Jump("loc_D00")

    label("loc_AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_ABE")
    Jump("loc_D00")

    label("loc_ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_ACC")
    Jump("loc_D00")

    label("loc_ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_ADA")
    Jump("loc_D00")

    label("loc_ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_D00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF2")
    Jump("loc_D00")

    label("loc_AF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C98")

    #C0010
    ChrTalk(
        0xA,
        (
            "#00303F呼，烦躁焦虑\x01",
            "果然不是我的风格啊。\x02\x03",

            "#00301F既然如此，今天一定要在\x01",
            "米修拉姆玩个痛快！\x02\x03",

            "#00309F罗伊德，晚上可得陪我一起去找大姐姐搭讪哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        (
            "#00012F哈哈，反正到时候的事情\x01",
            "都要交给你，不介意就没问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xA,
        (
            "#00306F什么嘛，这也太消极了吧。\x02\x03",

            "#00309F你明明很有潜力的，\x01",
            "赶快脱离弟弟角色，\x01",
            "彻底变成一个大人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#00006F听、听不懂你在说什么……\x02\x03",

            "#00000F（……不过，兰迪总算\x01",
            "  恢复平时的样子了。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_CF8")

    label("loc_C98")


    #C0014
    ChrTalk(
        0xA,
        (
            "#00305F啊，对了，\x01",
            "还得给那家伙买点礼物……\x02\x03",

            "#00304F听说她最近要升职了，\x01",
            "去挑些祝贺礼品吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF8")

    TalkEnd(0xFE)
    SetChrSubChip(0xA, 0x1)
    Return()

    label("loc_D00")

    TalkEnd(0xFE)
    Return()

    # Function_5_A5E end

    def Function_6_D04(): pass

    label("Function_6_D04")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_D15")
    Jump("loc_E5D")

    label("loc_D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_D23")
    Jump("loc_E5D")

    label("loc_D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_D31")
    Jump("loc_E5D")

    label("loc_D31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_E5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE6")

    #C0015
    ChrTalk(
        0xB,
        (
            "感谢大家今日\x01",
            "乘坐水上巴士。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        (
            "各位是玛丽亚贝尔小姐\x01",
            "招待的客人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xB,
        (
            "在到达米修拉姆之前，\x01",
            "请各位暂时享受一下这趟\x01",
            "在波涛中微微摇晃的悠闲旅程吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E5D")

    label("loc_DE6")


    #C0018
    ChrTalk(
        0xB,
        (
            "如果感到头晕，\x01",
            "只要到甲板上眺望远方的景色，\x01",
            "就可以有效缓解不适的感觉哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xB,
        (
            "我们这里还备有止晕药，\x01",
            "请尽管放心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5D")

    TalkEnd(0xFE)
    Return()

    # Function_6_D04 end

    def Function_7_E61(): pass

    label("Function_7_E61")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_F1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE8")

    #C0020
    ChrTalk(
        0xC,
        (
            "通商会议中的独立提案\x01",
            "真是让我大吃一惊。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xC,
        (
            "迪塔先生究竟要如何\x01",
            "实现自己的构想呢……\x01",
            "真让人期待啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_F1E")

    label("loc_EE8")


    #C0022
    ChrTalk(
        0xC,
        (
            "迪塔先生究竟要如何\x01",
            "实现独立呢……\x01",
            "真让人期待啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1E")

    TalkEnd(0xFE)
    Return()

    # Function_7_E61 end

    def Function_8_F22(): pass

    label("Function_8_F22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_FA6")

    #C0023
    ChrTalk(
        0xD,
        (
            "做梦都想来克洛斯贝尔旅行！\x01",
            "疗养地米修拉姆的主题公园，我来了！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xD,
        (
            "哎呀呀，太期待了，\x01",
            "一定要和女友一起玩个痛快～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA6")

    TalkEnd(0xFE)
    Return()

    # Function_8_F22 end

    def Function_9_FAA(): pass

    label("Function_9_FAA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1004")

    #C0025
    ChrTalk(
        0xE,
        (
            "我比较想去西餐厅\x01",
            "和时装店～\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xE,
        (
            "呵呵呵，今天一定要\x01",
            "让他给我买很多礼物。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1004")

    TalkEnd(0xFE)
    Return()

    # Function_9_FAA end

    def Function_10_1008(): pass

    label("Function_10_1008")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1019")
    Jump("loc_116B")

    label("loc_1019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1027")
    Jump("loc_116B")

    label("loc_1027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1035")
    Jump("loc_116B")

    label("loc_1035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1043")
    Jump("loc_116B")

    label("loc_1043")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_116B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_110A")

    #C0027
    ChrTalk(
        0xF,
        (
            "克洛斯贝尔独立吗……\x01",
            "也只有迪塔市长\x01",
            "才能提出这样的设想呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xF,
        (
            "虽然这条道路\x01",
            "绝不易走……\x01",
            "但他的话语中饱含梦想。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xF,
        (
            "市长一定会为克洛斯贝尔\x01",
            "带来光明，\x01",
            "我有这种感觉。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_116B")

    label("loc_110A")


    #C0030
    ChrTalk(
        0xF,
        (
            "哦哦，难得全家\x01",
            "一起出来玩，\x01",
            "还是不要谈这种话题了。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xF,
        (
            "今天一定要陪利玛和柯洛娜\x01",
            "玩个痛快。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_116B")

    TalkEnd(0xFE)
    Return()

    # Function_10_1008 end

    def Function_11_116F(): pass

    label("Function_11_116F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1180")
    Jump("loc_12E0")

    label("loc_1180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_118E")
    Jump("loc_12E0")

    label("loc_118E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_119C")
    Jump("loc_12E0")

    label("loc_119C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_11AA")
    Jump("loc_12E0")

    label("loc_11AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_12E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1280")

    #C0032
    ChrTalk(
        0x11,
        (
            "兰花塔竣工之后，\x01",
            "我老公领到了奖金，\x01",
            "所以全家一起出来游玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x11,
        (
            "本想把那些钱存起来，\x01",
            "但老公却说『偶尔也想全家出游』，\x01",
            "真是拗不过他。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x11,
        (
            "不过，这一趟真是来对了。\x01",
            "利玛竟然那么开心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_12E0")

    label("loc_1280")


    #C0035
    ChrTalk(
        0x11,
        (
            "我老公领到了奖金，\x01",
            "所以全家一起出来游玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x11,
        (
            "呵呵，这一趟真是来对了。\x01",
            "利玛竟然那么开心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E0")

    TalkEnd(0xFE)
    Return()

    # Function_11_116F end

    def Function_12_12E4(): pass

    label("Function_12_12E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_12F5")
    Jump("loc_134B")

    label("loc_12F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1303")
    Jump("loc_134B")

    label("loc_1303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1311")
    Jump("loc_134B")

    label("loc_1311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_131F")
    Jump("loc_134B")

    label("loc_131F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_134B")

    #C0037
    ChrTalk(
        0x10,
        (
            "爸爸！看啊看啊！！\x01",
            "鱼在跳呢！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_134B")

    TalkEnd(0xFE)
    Return()

    # Function_12_12E4 end

    def Function_13_134F(): pass

    label("Function_13_134F")

    EventBegin(0x0)
    SoundLoad(3515)
    SoundLoad(3394)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00101.itp")
    Fade(500)
    OP_68(700, 200, 8350, 0)
    MoveCamera(15, 33, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33390, 0)
    OP_64(0x8)
    OP_64(0x9)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x8, 500, -1000, 9000, 230)
    SetChrPos(0x9, -500, -1000, 9000, 80)
    SetChrPos(0x101, 1500, -1000, 8200, 315)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_145D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_145D)
    Sleep(50)

    def lambda_146D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_146D)
    WaitChrThread(0x9, 1)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_C9(0x0, 0x80000000)

    #A0038
    AnonymousTalk(
        0x9,
        "#30W#3515V啊……罗伊德警官。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_C9(0x1, 0x80000000)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sound(2189, 255, 100, 0)    #voice#Elie
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0039
    AnonymousTalk(
        0x8,
        "#30W你刚才去甲板了吧？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0040
    ChrTalk(
        0x101,
        (
            "#00004F#12P嗯，上去吹了吹风。\x02\x03",

            "#00005F那个……我打扰到你们了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        "#00108F#5P啊，没有的事……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x9,
        (
            "#10106F#5P……我们正在聊通商会议时\x01",
            "发生的那起事件……\x02\x03",

            "#10113F还有迪塔市长\x01",
            "的那个提案。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#00001F#12P提案……\x01",
            "是指『独立为主权国家』的提案吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "#00106F#5P嗯……毕竟这件事\x01",
            "也和我切身相关。\x02\x03",

            "#00108F没想到迪塔叔叔竟然\x01",
            "有那样的想法……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        (
            "#10106F#5P我也一样……\x01",
            "没办法置身事外啊。\x02\x03",

            "#10108F因为这关系到\x01",
            "警备队的存续……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#00003F#12P说起来……\x01",
            "帝国和共和国还提出了克\x01",
            "洛斯贝尔缩减警备队规模的要求呢。\x02\x03",

            "#00013F他们想让两大国的军队\x01",
            "取而代之，负责驻守唐古拉姆门\x01",
            "和贝尔加德门……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "#00103F#5P嗯……\x02\x03",

            "#00108F无论怎么想，两国也都是\x01",
            "为了从克洛斯贝尔榨取\x01",
            "更多的财富而串通一气。\x02\x03",

            "#00101F日后如果有机会抓住对方的破绽，\x01",
            "将对方势力吞并，\x01",
            "就能独占克洛斯贝尔的收益……\x02\x03",

            "#00106F他们的企图是显而易见的。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#00006F#12P确实……\x02\x03",

            "#00001F……也就是说，市长的提案\x01",
            "是为了对抗他们的图谋啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "#10103F#5P嗯，一旦独立为主权国家，\x01",
            "至今为止一直被两大国压制的警备队\x01",
            "就可以扩充规模，强化军备了。\x02\x03",

            "#10101F到时候，不仅可以强化个人武装，\x01",
            "还可以采购战车及军用飞艇，\x01",
            "从而抵御他国的侵略。\x02\x03",

            "#10106F……不过我有点讨厌\x01",
            "会这样思考问题的自己。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#00008F#12P诺艾尔……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#00103F#5P说到迪塔叔叔那项\x01",
            "提案的可行性……\x02\x03",

            "#00108F帝国和共和国很快就\x01",
            "发出了反对声明。\x02\x03",

            "#00100F不过，利贝尔、雷米菲利亚\x01",
            "和亚尔特利亚法典国则发表了\x01",
            "善意的支持声明……\x02\x03",

            "#00106F老实说，目前的状况很让人焦虑。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#00006F#12P是啊……\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        (
            "#10113F#5P……今天招待我们\x01",
            "来玩的玛丽亚贝尔小姐\x01",
            "又是如何考虑的呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(100)

    #C0054
    ChrTalk(
        0x8,
        (
            "#00106F#11P她如今的主要职责\x01",
            "还是专心经营\x01",
            "ＩＢＣ的事务。\x02\x03",

            "#00108F这次的提案好像\x01",
            "和她没什么关联。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x2D, 0x1F4)
    Sleep(100)

    #C0055
    ChrTalk(
        0x9,
        (
            "#10106F#6P这样啊……\x02\x03",

            "#10108F……机会难得，\x01",
            "本来还想听听她的意见呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "#00103F#11P是啊……我也有\x01",
            "很多话想问贝尔……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0057
    ChrTalk(
        0x101,
        (
            "#00004F#12P好啦，二位。\x02\x03",

            "#00000F越是在这种时期，才越应该\x01",
            "尽情游玩一番，不是吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1D03():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1D03)
    Sleep(50)

    def lambda_1D13():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1D13)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)

    #C0058
    ChrTalk(
        0x8,
        "#00105F#5P哎……\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        "#10105F#5P……？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#00002F#12P难得有机会度假，\x01",
            "我们要在米修拉姆的酒店住宿。\x02\x03",

            "还要到主题公园\x01",
            "尽情游玩。\x02\x03",

            "#00009F这样一定会让我们\x01",
            "彻底放松下来吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        "#00106F#5P#30W可、可是……\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        "#10108F#5P#30W……毕竟刚刚发生过那样的事……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#00000F#12P正因为刚刚发生过那样的事，才更需要放松。\x02\x03",

            "#00003F现在没人能预料到\x01",
            "克洛斯贝尔接下来的发展……\x02\x03",

            "我们今后很有可能要\x01",
            "面对相当严峻的工作。\x02\x03",

            "#00002F所以，该怎么说才好呢……\x01",
            "我希望能留下珍贵的『回忆』。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0064
    ChrTalk(
        0x8,
        "#00112F#5P哎哎……！？\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        "#10114F#5P那、那是指……！？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#00005F#12P（……哎？\x01",
            "  为什么反应这么大？）\x02\x03",

            "#00012F哈哈……\x01",
            "我说得太煽情了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "#10112F#5P与其说是煽情，倒不如说……\x02\x03",

            "#10108F（艾莉小姐……\x01",
            "  他是故意的吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "#00111F#5P（不……\x01",
            "  应该只是天生迟钝而已……）\x02\x03",

            "#00113F……那个……罗伊德。\x02\x03",

            "#00112F你所谓的『回忆』，\x01",
            "没有什么特定的对象吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#00005F#12P嗯？当然没有啊……\x02\x03",

            "#00000F因为大家一起享受休假\x01",
            "是很少有的机会啊。\x02\x03",

            "#00012F哈哈，只是有些对不起科长呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0070
    ChrTalk(
        0x8,
        "#00113F#5P唉～\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "#10112F#5P也、也是啊。\x01",
            "这才像罗伊德警官呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0072
    ChrTalk(
        0x101,
        (
            "#00005F#12P嗯？莫非我从刚才开始\x01",
            "就搞错你们的意思了？\x02\x03",

            "#00006F我只是觉得大家好像都很消沉，\x01",
            "所以想给你们稍微鼓—#3500W—#30W",
            "#00011F啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        "#10102F#5P噗……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0074
    ChrTalk(
        0x8,
        (
            "#00114F#5P啊哈哈哈……！\x02\x03",

            "#00116F你、你可真是……\x01",
            "该说是天生迟钝，还是笨拙呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "#10109F#5P呵呵，突然觉得自己之前那么烦恼，\x01",
            "简直就像个傻瓜一样呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0076
    ChrTalk(
        0x101,
        (
            "#00006F#12P……抱歉，\x01",
            "我会好好反省的。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "#00104F#5P呵呵，不要介意嘛。\x02\x03",

            "#00102F……对不起，\x01",
            "其实是我们有点\x01",
            "不解风情。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "#10102F#5P是啊……\x01",
            "既然出来度假，\x01",
            "自然要尽兴而归！\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        (
            "#00002F#12P是吗……\x01",
            "（总算是达到目的了吧？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x8, 630, -1000, 9000, 270)
    SetChrPos(0x9, -620, -1000, 9000, 90)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x0, 3000, -1000, 6500, 180)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x144, 2)
    EventEnd(0x5)
    Return()

    # Function_13_134F end

    def Function_14_2453(): pass

    label("Function_14_2453")

    EventBegin(0x0)
    Fade(500)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00301.itp")
    OP_68(3170, 1300, -9560, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34500, 0)
    OP_64(0xA)
    SetChrPos(0x101, 800, 0, -9770, 90)
    SetCameraDistance(34000, 1500)
    OP_9B(0x0, 0x101, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_93(0x101, 0x2D, 0x1F4)
    OP_6F(0x79)
    OP_0D()
    SetChrSubChip(0xA, 0x0)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(200)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    #Sound(2756, 255, 100, 0)    #voice#Randy

    #A0080
    AnonymousTalk(
        0xA,
        (
            "#30W哟，罗伊德。\x02\x03",

            "#20W说起来，玛丽亚贝尔大小姐\x01",
            "可真是慷慨啊。\x02\x03",

            "竟然让我们免费住在米修拉姆的酒店，\x01",
            "还招待我们去主题公园玩。\x02\x03",

            "这可真是盛情款待啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xAC4)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0081
    ChrTalk(
        0x101,
        (
            "#00002F#6P……是啊。\x02\x03",

            "#00008F………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xA,
        "#00302F#5P哈哈……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    #C0083
    ChrTalk(
        0xA,
        (
            "#00304F#5P喂，罗伊德。\x02\x03",

            "#00300F我看你好像有点误会，\x01",
            "所以有句话还是要说出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#00005F#6P哎……\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xA,
        (
            "#00303F#5P恐怖分子遭受屠杀的事件……\x02\x03",

            "#00301F你是不是觉得，\x01",
            "因为我的亲属做了那样的事情，\x01",
            "所以我很受刺激？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        "#00011F#6P这、这个……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0087
    ChrTalk(
        0x101,
        (
            "#00006F#6P……不，似乎有点不同。\x02\x03",

            "#00008F我总觉得，你对你叔叔他们的\x01",
            "所作所为并没有那么纠结。\x02\x03",

            "#00001F而是一直对自己的\x01",
            "某些事情耿耿于怀。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xBB8)
    BeginChrThread(0x19, 1, 0, 15)

    #C0088
    ChrTalk(
        0xA,
        (
            "#00308F#5P……是吗。\x02\x03",

            "#00303F#30W…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7534", 0)
    SetChrSubChip(0xA, 0x0)
    Sleep(150)
    SetChrSubChip(0xA, 0x1)
    SetCameraDistance(33000, 20000)
    Sleep(1000)

    #C0089
    ChrTalk(
        0xA,
        (
            "#00304F#5P我曾经有个朋友。\x02\x03",

            "他比我小一岁，\x01",
            "眼神就像小狗一样……\x02\x03",

            "#00300F那应该是我在猎兵团之外\x01",
            "所结交的第一个朋友。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#00005F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xA,
        (
            "#00308F#5P当时发生了很多事情，\x01",
            "导致那家伙离开人世……\x02\x03",

            "因为那些事，\x01",
            "使我逃离猎兵团，并陷入迷茫。\x02\x03",

            "#00303F后来，我来到克洛斯贝尔，\x01",
            "加入警备队……\x01",
            "并认识了你们……\x02\x03",

            "#00302F……但是，我始终还是当年的自己，\x01",
            "骨子里好像并没有任何改变。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        "#00005F#6P哎……\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "#00312F#5P正如叔叔所说，\x01",
            "对我而言，恐怖分子被屠杀\x01",
            "之类的场面并不稀奇。\x02\x03",

            "像那种程度的歼灭战，\x01",
            "在战场上不过是家常便饭而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        "#00008F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        (
            "#00303F#5P我当时会情绪失控……\x01",
            "并不是义愤填膺。\x02\x03",

            "也不是同情恐怖分子，\x01",
            "或是对叔叔他们的做法感到愤怒。\x02\x03",

            "#00308F#30W我只是……突然发现自己\x01",
            "两年来没有丝毫改变……\x02\x03",

            "骨子里仍旧是个彻头彻尾的猎兵，\x01",
            "这让我发自内心地感到震惊……\x02\x03",

            "#00306F于是就彻底暴发，冲上去泄愤，\x01",
            "结果却被一下放倒……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#00008F#6P是吗……\x02\x03",

            "#00006F……确实有些\x01",
            "难看呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xA,
        (
            "#00302F#5P哈哈，是吧？\x02\x03",

            "#00306F真是的，我这个\x01",
            "冷酷美男子竟会如此丢脸——\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#00002F#6P……不过，\x01",
            "我却有点开心呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0xA, 0x0)
    Sleep(120)
    SetChrSubChip(0xA, 0x2)
    Sleep(250)

    #C0099
    ChrTalk(
        0xA,
        "#00305F#5P哎……\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        (
            "#00004F#6P该怎么说呢……兰迪平时\x01",
            "既成熟又从容不迫，\x01",
            "每次都是我们依靠你。\x02\x03",

            "#00000F但你这次却主动\x01",
            "吐露自己的感受，\x01",
            "身为同伴，总觉得有点开心呢。\x02\x03",

            "也许并非只有我这么想……\x01",
            "其他同伴大概也是一样的。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        "#00305F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#00006F#6P另外……\x01",
            "所谓的『骨子里就是猎兵』，\x01",
            "只是你太爱钻牛角尖了吧？\x02\x03",

            "#00008F至少我不觉得\x01",
            "你是那种愿意为钱而\x01",
            "参加战争的人。\x02\x03",

            "#00000F虽然你态度轻浮，喜欢夜游，\x01",
            "性格有点好战，而且容易激动……\x01",
            "但你做事情很有度，该收手时也懂得收手。\x02\x03",

            "#00002F而且，由于自己年长，你总是主动\x01",
            "帮助我们，是个很可靠的大哥……\x02\x03",

            "#00009F这就是我所认识的男人──\x01",
            "兰迪·奥兰多。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        "#00305F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        (
            "#00003F#6P所以说，偶尔被我们\x01",
            "看到一点丢脸的场面，\x01",
            "根本就不必在意。\x02\x03",

            "#00000F倒不如说，这样反而\x01",
            "让我和艾莉他们更加——\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        (
            "#00303F#5P我知道啦，不用再说了。\x02\x03",

            "#00306F看样子，我还是小看了\x01",
            "你的潜力啊……\x02\x03",

            "#00310F你小子未免也太擅长在不知不觉中攻陷别人了吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        (
            "#00011F#6P攻、攻陷？\x02\x03",

            "#00006F虽然不是很明白，\x01",
            "但我说了什么让你不高兴的话吗？\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7565", 0)
    BeginChrThread(0x19, 1, 0, 16)

    #C0107
    ChrTalk(
        0xA,
        (
            "#00315F#5P唉，真是的，总觉得自己\x01",
            "刚才那么忧虑，就像个傻瓜一样……\x02\x03",

            "#00306F既然如此，\x01",
            "就去米修拉姆玩个痛快吧！\x02\x03",

            "#00301F先到主题公园玩个够，\x01",
            "晚上还要去找大姐姐搭讪！\x02\x03",

            "#00307F你这混账弟弟也要陪我一起去！\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#00012F#6P知、知道啦。\x02\x03",

            "#00002F（虽然不是很明白……\x01",
            "  但他好像恢复精神了吧？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 980, 0, -10170, 270)
    SetChrSubChip(0xA, 0x1)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x144, 3)
    EventEnd(0x5)
    Return()

    # Function_14_2453 end

    def Function_15_3215(): pass

    label("Function_15_3215")

    OP_25(0x1E0, 0x5A)
    Sleep(200)
    OP_25(0x1E0, 0x50)
    Sleep(200)
    OP_25(0x1E0, 0x46)
    Sleep(200)
    OP_25(0x1E0, 0x3C)
    Sleep(200)
    OP_25(0x1E0, 0x32)
    Sleep(200)
    OP_25(0x1E0, 0x28)
    Return()

    # Function_15_3215 end

    def Function_16_323D(): pass

    label("Function_16_323D")

    OP_25(0x1E0, 0x32)
    Sleep(200)
    OP_25(0x1E0, 0x3C)
    Sleep(200)
    OP_25(0x1E0, 0x46)
    Sleep(200)
    OP_25(0x1E0, 0x50)
    Sleep(200)
    OP_25(0x1E0, 0x5A)
    Sleep(200)
    OP_25(0x1E0, 0x64)
    Return()

    # Function_16_323D end

    def Function_17_3265(): pass

    label("Function_17_3265")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08502.itc", 0x1E)
    LoadChrToIndex("chr/ch05202.itc", 0x1F)
    LoadChrToIndex("chr/ch05102.itc", 0x20)
    LoadChrToIndex("chr/ch07502.itc", 0x21)
    LoadChrToIndex("chr/ch10002.itc", 0x22)
    LoadChrToIndex("chr/ch05502.itc", 0x23)
    LoadChrToIndex("chr/ch05602.itc", 0x24)
    LoadChrToIndex("chr/ch00102.itc", 0x25)
    LoadChrToIndex("chr/ch00202.itc", 0x26)
    LoadChrToIndex("chr/ch02902.itc", 0x28)
    LoadChrToIndex("chr/ch03002.itc", 0x29)
    LoadChrToIndex("chr/ch02702.itc", 0x2A)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x1)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x103, 0x26)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x104, 0x2)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x109, 0x28)
    SetChrSubChip(0x109, 0x1)
    SetChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x105, 0x29)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x18, 0x2A)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x18, 1, 0, 0)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x2)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x1)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x1)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x2)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x16, 0x22)
    SetChrSubChip(0x16, 0x2)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x2)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x101, 0, 0, 0, 0)
    SetChrFlags(0x101, 0x8)
    SetChrPos(0x102, 1000, -800, 7350, 0)
    SetChrPos(0x17, 0, -800, 7350, 0)
    SetChrPos(0x103, -2200, 150, -13850, 180)
    SetChrPos(0x18, -1200, 0, -14850, 270)
    SetChrPos(0x104, -3550, 150, -3850, 180)
    SetChrPos(0x105, -2350, 150, -3850, 180)
    SetChrPos(0x109, 2100, 150, -11350, 180)
    SetChrPos(0x12, 3250, 150, -11350, 180)
    SetChrPos(0x15, -3550, 150, -8850, 180)
    SetChrPos(0x16, -2350, 150, -8850, 180)
    SetChrPos(0x14, 2100, 150, -8850, 180)
    SetChrPos(0x13, 3250, 150, -8850, 180)
    OP_68(0, 1000, -15000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1000, 10000, 20000)
    Sleep(14000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("e3000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_3265 end

    SaveToFile()

Try(main)
