from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1330.bin",                # FileName
        "t1330",                    # MapName
        "t1330",                    # Location
        0x00B7,                     # MapIndex
        "ed7160",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, -16000, 0, 0, 1, 183, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1330",                  # 0
        "艾莉",                   # 1
        "缇欧",                   # 2
        "兰迪",                   # 3
        "诺艾尔",                 # 4
        "瓦吉",                   # 5
        "琪雅",                   # 6
        "芙兰",                   # 7
        "塞茜尔",                 # 8
        "修利",                   # 9
        "梅尔斯",                 # 10
        "柯洛娜",                 # 11
        "利玛",                   # 12
        "奇幻乐园工作人员",       # 13
        "游客",                   # 14
        "游客",                   # 15
        "游客",                   # 16
        "游客",                   # 17
        "游客",                   # 18
        "咪雪",                   # 19
        "模型",                   # 20
        "男子",                   # 21
        "女子",                   # 22
        "奇幻乐园入口广场方向",   # 23
    ))

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch00200.itc",                   # 01
        "chr/ch00300.itc",                   # 02
        "chr/ch02900.itc",                   # 03
        "chr/ch03000.itc",                   # 04
        "chr/ch08200.itc",                   # 05
        "chr/ch08500.itc",                   # 06
        "chr/ch07500.itc",                   # 07
        "chr/ch10100.itc",                   # 08
        "chr/ch26200.itc",                   # 09
        "chr/ch22700.itc",                   # 0A
        "chr/ch20700.itc",                   # 0B
        "chr/ch44600.itc",                   # 0C
        "chr/ch22100.itc",                   # 0D
        "chr/ch24500.itc",                   # 0E
        "chr/ch22000.itc",                   # 0F
        "chr/ch20500.itc",                   # 10
        "chr/ch32300.itc",                   # 11
        "chr/ch03002.itc",                   # 12
        "chr/ch45400.itc",                   # 13
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

    DeclNpc(8600,    9,       -15670,  25,   389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(2970,    3549,    -33750,  25,   389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-7480,   9,       -15380,  205,  389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(7869,    9,       -16059,  295,  389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(11350,   200,     -12800,  225,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(10130,   9,       -17000,  115,  389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(9850,    9,       -15010,  205,  389,  0x0, 0,   7,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-3990,   2309,    -28940,  250,  389,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-1360,   0,       -17809,  295,  389,  0x0, 0,   9,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-2420,   0,       -17649,  25,   389,  0x0, 0,   10,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-2279,   0,       -16440,  160,  389,  0x0, 0,   11,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-949,    0,       -14699,  160,  389,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-3170,   4619,    -37919,  115,  389,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-2150,   4739,    -38400,  295,  389,  0x0, 0,   14,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-5900,   9,       -13130,  295,  389,  0x0, 0,   15,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-6829,   9,       -12550,  115,  389,  0x0, 0,   16,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-5030,   9,       -17719,  25,   389,  0x0, 0,   17,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(9819,    0,       -10560,  315,  389,  0x0, 0,   19,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 56,  -0.23999999463558197,  -12.220000267028809,   0.0,                   144.0,                 [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   0.029999999329447746,  4.073333740234375,     -0.0,                  1.0])

    DeclActor(8730,    0,       -11330,  1000,    9820,    1500,    -10560,  0x007E, 0,  51, 0x0000)
    DeclActor(-5950,   0,       -12040,  1200,    -5950,   2000,    -12040,  0x007C, 0,  55, 0x0000)

    PlaceName(-0.38999998569488525, 0.0, -83.0999984741211, 0x0000, 0x0000, "奇幻乐园入口广场方向")

    ChipFrameInfo(1300, 0)                                       # 0

    ScpFunction((
        "Function_0_514",          # 00, 0
        "Function_1_5CC",          # 01, 1
        "Function_2_658",          # 02, 2
        "Function_3_6B3",          # 03, 3
        "Function_4_767",          # 04, 4
        "Function_5_81B",          # 05, 5
        "Function_6_9C4",          # 06, 6
        "Function_7_A82",          # 07, 7
        "Function_8_B90",          # 08, 8
        "Function_9_C3D",          # 09, 9
        "Function_10_DA4",         # 0A, 10
        "Function_11_E4A",         # 0B, 11
        "Function_12_F08",         # 0C, 12
        "Function_13_F9D",         # 0D, 13
        "Function_14_103D",        # 0E, 14
        "Function_15_10DA",        # 0F, 15
        "Function_16_11BB",        # 10, 16
        "Function_17_120B",        # 11, 17
        "Function_18_1243",        # 12, 18
        "Function_19_12F4",        # 13, 19
        "Function_20_1378",        # 14, 20
        "Function_21_146C",        # 15, 21
        "Function_22_150C",        # 16, 22
        "Function_23_15AC",        # 17, 23
        "Function_24_1653",        # 18, 24
        "Function_25_185C",        # 19, 25
        "Function_26_2213",        # 1A, 26
        "Function_27_2250",        # 1B, 27
        "Function_28_228D",        # 1C, 28
        "Function_29_2398",        # 1D, 29
        "Function_30_23FA",        # 1E, 30
        "Function_31_2469",        # 1F, 31
        "Function_32_24E0",        # 20, 32
        "Function_33_254B",        # 21, 33
        "Function_34_25B6",        # 22, 34
        "Function_35_2601",        # 23, 35
        "Function_36_2672",        # 24, 36
        "Function_37_27B1",        # 25, 37
        "Function_38_27EF",        # 26, 38
        "Function_39_2837",        # 27, 39
        "Function_40_2877",        # 28, 40
        "Function_41_316B",        # 29, 41
        "Function_42_3B27",        # 2A, 42
        "Function_43_44AE",        # 2B, 43
        "Function_44_4D58",        # 2C, 44
        "Function_45_5693",        # 2D, 45
        "Function_46_5FE6",        # 2E, 46
        "Function_47_6869",        # 2F, 47
        "Function_48_7177",        # 30, 48
        "Function_49_7BD3",        # 31, 49
        "Function_50_8482",        # 32, 50
        "Function_51_8DAC",        # 33, 51
        "Function_52_9563",        # 34, 52
        "Function_53_A60B",        # 35, 53
        "Function_54_A6A1",        # 36, 54
        "Function_55_A737",        # 37, 55
        "Function_56_A769",        # 38, 56
    ))


    def Function_0_514(): pass

    label("Function_0_514")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_554"),
        (1, "loc_560"),
        (2, "loc_56C"),
        (3, "loc_578"),
        (4, "loc_584"),
        (5, "loc_590"),
        (6, "loc_59C"),
        (SWITCH_DEFAULT, "loc_5A8"),
    )


    label("loc_554")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_560")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_56C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_578")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_584")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_590")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_59C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_5A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_5B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5CB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_5CB")

    Return()

    # Function_0_514 end

    def Function_1_5CC(): pass

    label("Function_1_5CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_5DA")
    Jump("loc_648")

    label("loc_5DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_5E8")
    Jump("loc_648")

    label("loc_5E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_5F6")
    Jump("loc_648")

    label("loc_5F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_607")
    Call(0, 24)
    Jump("loc_648")

    label("loc_607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_615")
    Jump("loc_648")

    label("loc_615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_623")
    Jump("loc_648")

    label("loc_623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_631")
    Jump("loc_648")

    label("loc_631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_63F")
    Jump("loc_648")

    label("loc_63F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_648")

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_657")
    ClearScenarioFlags(0x22, 0)
    Event(0, 52)

    label("loc_657")

    Return()

    # Function_1_5CC end

    def Function_2_658(): pass

    label("Function_2_658")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x1C2)
    Call(0, 28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_END)), "loc_679")
    OP_24(0x335)
    Jump("loc_67F")

    label("loc_679")

    Sound(821, 1, 50, 0)

    label("loc_67F")

    Sound(126, 1, 80, 0)
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B2")
    OP_66(0x0, 0x1)

    label("loc_6B2")

    Return()

    # Function_2_658 end

    def Function_3_6B3(): pass

    label("Function_3_6B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CC")
    Jump("loc_763")

    label("loc_6CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E2")
    Jump("loc_763")

    label("loc_6E2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_705")
    Call(0, 21)
    Jump("loc_737")

    label("loc_705")


    #C0001
    ChrTalk(
        0x8,
        (
            "#00102F呵呵，我去买饮料，\x01",
            "你先好好休息一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_737")

    Jump("loc_763")

    label("loc_73C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_752")
    Jump("loc_763")

    label("loc_752")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_763")

    label("loc_763")

    TalkEnd(0xFE)
    Return()

    # Function_3_6B3 end

    def Function_4_767(): pass

    label("Function_4_767")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_780")
    Jump("loc_817")

    label("loc_780")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A3")
    Call(0, 22)
    Jump("loc_7D5")

    label("loc_7A3")


    #C0002
    ChrTalk(
        0x9,
        (
            "#00204F芙兰小姐真了不起……\x01",
            "完全懂得精髓呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D5")

    Jump("loc_817")

    label("loc_7DA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F0")
    Jump("loc_817")

    label("loc_7F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_806")
    Jump("loc_817")

    label("loc_806")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_817")

    label("loc_817")

    TalkEnd(0xFE)
    Return()

    # Function_4_767 end

    def Function_5_81B(): pass

    label("Function_5_81B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_834")
    Jump("loc_9C0")

    label("loc_834")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84A")
    Jump("loc_9C0")

    label("loc_84A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_860")
    Jump("loc_9C0")

    label("loc_860")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92E")

    #C0003
    ChrTalk(
        0xA,
        (
            "#00300F刚才从摩天轮上下来一个大姐姐，\x01",
            "正是我喜欢的类型，\x01",
            "本想去搭个讪……\x02\x03",

            "#00306F但她好像是和\x01",
            "男朋友一起来的。\x02\x03",

            "#00302F哎，想在主题公园里搭讪，\x01",
            "果然还是不大可能啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_9AA")

    label("loc_92E")


    #C0004
    ChrTalk(
        0xA,
        (
            "#00306F仔细想想，来主题公园玩的人，\x01",
            "肯定以情侣或全家出游的客人为主。\x02\x03",

            "#00302F想在主题公园里搭讪，\x01",
            "果然还是不大可能啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AA")

    Jump("loc_9C0")

    label("loc_9AF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C0")

    label("loc_9C0")

    TalkEnd(0xFE)
    Return()

    # Function_5_81B end

    def Function_6_9C4(): pass

    label("Function_6_9C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DD")
    Jump("loc_A7E")

    label("loc_9DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F3")
    Jump("loc_A7E")

    label("loc_9F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A09")
    Jump("loc_A7E")

    label("loc_A09")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1F")
    Jump("loc_A7E")

    label("loc_A1F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A42")
    Call(0, 23)
    Jump("loc_A7E")

    label("loc_A42")


    #C0005
    ChrTalk(
        0xB,
        (
            "#10100F啊，罗伊德警官，\x01",
            "你想好最后一张票要玩什么了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7E")

    TalkEnd(0xFE)
    Return()

    # Function_6_9C4 end

    def Function_7_A82(): pass

    label("Function_7_A82")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B02")

    #C0006
    ChrTalk(
        0xC,
        (
            "#10304F在这里观察\x01",
            "往来者的感觉也不错。\x02\x03",

            "#10302F呵呵，其中说不定\x01",
            "就有扮演咪西的人呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_B34")

    label("loc_B02")


    #C0007
    ChrTalk(
        0xC,
        (
            "#10302F呵呵，其中说不定\x01",
            "就有扮演咪西的人呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B34")

    Jump("loc_B8C")

    label("loc_B39")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4F")
    Jump("loc_B8C")

    label("loc_B4F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B65")
    Jump("loc_B8C")

    label("loc_B65")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7B")
    Jump("loc_B8C")

    label("loc_B7B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8C")

    label("loc_B8C")

    TalkEnd(0xFE)
    Return()

    # Function_7_A82 end

    def Function_8_B90(): pass

    label("Function_8_B90")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA9")
    Jump("loc_C39")

    label("loc_BA9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBF")
    Jump("loc_C39")

    label("loc_BBF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C12")

    #C0008
    ChrTalk(
        0xD,
        (
            "#01102F这里的湖\x01",
            "真漂亮啊。\x02\x03",

            "#01109F清澈得可以看到水底。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C39")

    label("loc_C12")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C28")
    Jump("loc_C39")

    label("loc_C28")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C39")

    label("loc_C39")

    TalkEnd(0xFE)
    Return()

    # Function_8_B90 end

    def Function_9_C3D(): pass

    label("Function_9_C3D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C56")
    Jump("loc_DA0")

    label("loc_C56")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C79")
    Call(0, 22)
    Jump("loc_CBE")

    label("loc_C79")


    #C0009
    ChrTalk(
        0xE,
        (
            "#06409F正如缇欧所说，\x01",
            "那副太阳的笑脸\x01",
            "肯定就是受欢迎的秘密呢～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CBE")

    Jump("loc_DA0")

    label("loc_CC3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD9")
    Jump("loc_DA0")

    label("loc_CD9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEF")
    Jump("loc_DA0")

    label("loc_CEF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D12")
    Call(0, 23)
    Jump("loc_DA0")

    label("loc_D12")


    #C0010
    ChrTalk(
        0xE,
        (
            "#06402F在这个时间段乘坐摩天轮，\x01",
            "似乎能看到非常\x01",
            "漂亮的风景哦～\x02\x03",

            "#06409F如果还没想好玩什么，\x01",
            "罗伊德警官要不要找个同伴\x01",
            "一起乘坐摩天轮呢～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA0")

    TalkEnd(0xFE)
    Return()

    # Function_9_C3D end

    def Function_10_DA4(): pass

    label("Function_10_DA4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DBD")
    Jump("loc_E46")

    label("loc_DBD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD3")
    Jump("loc_E46")

    label("loc_DD3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF6")
    Call(0, 21)
    Jump("loc_E1A")

    label("loc_DF6")


    #C0011
    ChrTalk(
        0xF,
        (
            "#05909F呵呵，那我\x01",
            "就不客气啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E1A")

    Jump("loc_E46")

    label("loc_E1F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E35")
    Jump("loc_E46")

    label("loc_E35")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E46")

    label("loc_E46")

    TalkEnd(0xFE)
    Return()

    # Function_10_DA4 end

    def Function_11_E4A(): pass

    label("Function_11_E4A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E63")
    Jump("loc_F04")

    label("loc_E63")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E79")
    Jump("loc_F04")

    label("loc_E79")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8F")
    Jump("loc_F04")

    label("loc_E8F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF3")

    #C0012
    ChrTalk(
        0x10,
        (
            "#14006F啊，玩了好多游乐设施，\x01",
            "已经有点累了呢。\x02\x03",

            "#14000F在这里\x01",
            "吹吹风吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F04")

    label("loc_EF3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F04")

    label("loc_F04")

    TalkEnd(0xFE)
    Return()

    # Function_11_E4A end

    def Function_12_F08(): pass

    label("Function_12_F08")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F21")
    Jump("loc_F99")

    label("loc_F21")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5C")

    #C0013
    ChrTalk(
        0x11,
        (
            "哈哈，利玛好像\x01",
            "很喜欢摩天轮呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F99")

    label("loc_F5C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F72")
    Jump("loc_F99")

    label("loc_F72")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F88")
    Jump("loc_F99")

    label("loc_F88")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F99")

    label("loc_F99")

    TalkEnd(0xFE)
    Return()

    # Function_12_F08 end

    def Function_13_F9D(): pass

    label("Function_13_F9D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB6")
    Jump("loc_1039")

    label("loc_FB6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FFC")

    #C0014
    ChrTalk(
        0x12,
        (
            "哎呀呀，利玛……\x01",
            "还有很多可以\x01",
            "玩的地方哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1039")

    label("loc_FFC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1012")
    Jump("loc_1039")

    label("loc_1012")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1028")
    Jump("loc_1039")

    label("loc_1028")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1039")

    label("loc_1039")

    TalkEnd(0xFE)
    Return()

    # Function_13_F9D end

    def Function_14_103D(): pass

    label("Function_14_103D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1056")
    Jump("loc_10D6")

    label("loc_1056")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1099")

    #C0015
    ChrTalk(
        0x13,
        (
            "爸爸，我们再坐一次吧！\x01",
            "我还想看兰花塔！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D6")

    label("loc_1099")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AF")
    Jump("loc_10D6")

    label("loc_10AF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C5")
    Jump("loc_10D6")

    label("loc_10C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D6")

    label("loc_10D6")

    TalkEnd(0xFE)
    Return()

    # Function_14_103D end

    def Function_15_10DA(): pass

    label("Function_15_10DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11B7")
    TalkBegin(0xFE)

    #C0016
    ChrTalk(
        0xFE,
        (
            "这边的游乐设施是\x01",
            "『阳光摩天轮』！\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "座舱将会缓缓环绕一圈，\x01",
            "让大家尽情观赏\x01",
            "米修拉姆最美丽的风景。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#00000F（我们正在和咪雪捉迷藏……\x01",
            "　现在还是不要去\x01",
            "　游乐设施游玩了。）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_11BA")

    label("loc_11B7")

    Call(0, 25)

    label("loc_11BA")

    Return()

    # Function_15_10DA end

    def Function_16_11BB(): pass

    label("Function_16_11BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1207")

    #C0019
    ChrTalk(
        0x15,
        (
            "我们去坐摩天轮吧！\x01",
            "从那上面看风景很漂亮的～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1207")

    label("loc_1207")

    TalkEnd(0xFE)
    Return()

    # Function_16_11BB end

    def Function_17_120B(): pass

    label("Function_17_120B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_123F")

    #C0020
    ChrTalk(
        0x16,
        (
            "不要，\x01",
            "我很恐高的～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_123F")

    label("loc_123F")

    TalkEnd(0xFE)
    Return()

    # Function_17_120B end

    def Function_18_1243(): pass

    label("Function_18_1243")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_128C")

    #C0021
    ChrTalk(
        0x17,
        (
            "呃……\x01",
            "座舱摇摇晃晃的，\x01",
            "让我头晕得要命……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12F0")

    label("loc_128C")


    #C0022
    ChrTalk(
        0x17,
        (
            "我、我说……\x01",
            "还是选择其它游乐设施\x01",
            "作为今天的最后娱乐吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x17,
        "要是再晕一次，我可就受不了啦……\x02",
    )

    CloseMessageWindow()

    label("loc_12F0")

    TalkEnd(0xFE)
    Return()

    # Function_18_1243 end

    def Function_19_12F4(): pass

    label("Function_19_12F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1338")

    #C0024
    ChrTalk(
        0x18,
        (
            "真是的，难得的约会，\x01",
            "你打起精神来嘛～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1374")

    label("loc_1338")


    #C0025
    ChrTalk(
        0x18,
        (
            "没关系啦！\x01",
            "到了最高处之后，看看夕阳，\x01",
            "就不会觉得晕了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1374")

    TalkEnd(0xFE)
    Return()

    # Function_19_12F4 end

    def Function_20_1378(): pass

    label("Function_20_1378")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1401")

    #C0026
    ChrTalk(
        0x19,
        (
            "一个人坐摩天轮\x01",
            "需要相当的勇气呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x19,
        (
            "……果然还是应该叫朋友一起来啊。\x01",
            "哪怕叫上同性朋友，也比自己来要好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1468")

    label("loc_1401")


    #C0028
    ChrTalk(
        0x19,
        (
            "最高处的风景真是太棒了。\x01",
            "鼓起勇气坐摩天轮\x01",
            "真是正确的选择。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x19,
        (
            "不过，一个人坐\x01",
            "还是有点孤单呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1468")

    TalkEnd(0xFE)
    Return()

    # Function_20_1378 end

    def Function_21_146C(): pass

    label("Function_21_146C")

    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0030
    ChrTalk(
        0x8,
        (
            "#00100F好，我去买些\x01",
            "饮料之类的回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xF,
        (
            "#05905F哎呀，那怎么好意思，\x01",
            "还是我去买吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "#00102F呵呵，塞茜尔小姐\x01",
            "就在这里好好休息吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_21_146C end

    def Function_22_150C(): pass

    label("Function_22_150C")

    OP_4B(0x9, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0033
    ChrTalk(
        0x9,
        (
            "#00204F摩天轮果然\x01",
            "很受欢迎呢。\x02\x03",

            "#00200F正中间那张太阳的笑脸……\x01",
            "应该就是它\x01",
            "成功的关键。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xE,
        "#06409F啊哈哈，一定就是那样～！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xE, 0x10)
    Return()

    # Function_22_150C end

    def Function_23_15AC(): pass

    label("Function_23_15AC")

    OP_4B(0xB, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0035
    ChrTalk(
        0xE,
        (
            "#06400F导览上说，\x01",
            "在这个时间段乘坐摩天轮，\x01",
            "可以看到非常漂亮的风景～！\x02\x03",

            "#06409F姐姐，我们待会一起去坐吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xB,
        "#10100F呵呵，好啊。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xB, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_23_15AC end

    def Function_24_1653(): pass

    label("Function_24_1653")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16B8")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)

    label("loc_16B8")

    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x10)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x10)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1716")
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x12)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_185B")

    label("loc_1716")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176F")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 3970, 3590, -33910, 25)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    Jump("loc_185B")

    label("loc_176F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_179E")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    Jump("loc_185B")

    label("loc_179E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1816")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_17E8")
    SetChrFlags(0xA, 0x80)
    Jump("loc_17F6")

    label("loc_17E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 1)), scpexpr(EXPR_END)), "loc_17F6")
    SetChrFlags(0x10, 0x80)

    label("loc_17F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1811")
    ClearChrFlags(0x1A, 0x80)

    label("loc_1811")

    Jump("loc_185B")

    label("loc_1816")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_185B")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 6760, 10, -15090, 115)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x10)

    label("loc_185B")

    Return()

    # Function_24_1653 end

    def Function_25_185C(): pass

    label("Function_25_185C")

    EventBegin(0x0)
    Fade(500)
    OP_68(-950, 1300, -15300, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(8500, 0)
    OP_4B(0x14, 0xFF)
    SetChrPos(0x101, -950, 0, -16000, 0)
    Call(0, 26)
    OP_0D()

    #C0037
    ChrTalk(
        0x14,
        (
            "这边的游乐设施是\x01",
            "『阳光摩天轮』！\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x14,
        (
            "座舱将会缓缓环绕一圈，\x01",
            "让大家尽情观赏\x01",
            "米修拉姆最美丽的风景。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x14,
        (
            "如果有兴趣，\x01",
            "要不要和同伴一起乘坐呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#00004F#12P（……邀请谁好呢？）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 5, -1, -1)
    SetChrName("")

    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K要邀请谁？\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "艾莉")
    MenuCmd(1, 0, "缇欧")
    MenuCmd(1, 0, "兰迪")
    MenuCmd(1, 0, "诺艾尔")
    MenuCmd(1, 0, "瓦吉")
    MenuCmd(1, 0, "琪雅")
    MenuCmd(1, 0, "芙兰")
    MenuCmd(1, 0, "塞茜尔")
    MenuCmd(1, 0, "伊莉娅")
    MenuCmd(1, 0, "莉夏")
    MenuCmd(1, 0, "修利")
    MenuCmd(1, 0, "放弃")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1A16")
    MenuCmd(3, 0, 0x0)

    label("loc_1A16")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1A28")
    MenuCmd(3, 0, 0x1)

    label("loc_1A28")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1A3A")
    MenuCmd(3, 0, 0x2)

    label("loc_1A3A")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1A4C")
    MenuCmd(3, 0, 0x3)

    label("loc_1A4C")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1A5E")
    MenuCmd(3, 0, 0x4)

    label("loc_1A5E")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1A70")
    MenuCmd(3, 0, 0x5)

    label("loc_1A70")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1A82")
    MenuCmd(3, 0, 0x6)

    label("loc_1A82")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1A94")
    MenuCmd(3, 0, 0x7)

    label("loc_1A94")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1AA6")
    MenuCmd(3, 0, 0x8)

    label("loc_1AA6")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1AB8")
    MenuCmd(3, 0, 0x9)

    label("loc_1AB8")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1ACA")
    MenuCmd(3, 0, 0xA)

    label("loc_1ACA")

    MenuCmd(2, 0, -1, 55, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21C5")
    OP_D2(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B50"),
        (1, "loc_1B87"),
        (2, "loc_1BBE"),
        (3, "loc_1BF5"),
        (4, "loc_1C2E"),
        (5, "loc_1C65"),
        (6, "loc_1C9C"),
        (7, "loc_1CD3"),
        (8, "loc_1D10"),
        (9, "loc_1D4D"),
        (10, "loc_1D84"),
        (SWITCH_DEFAULT, "loc_1DBB"),
    )


    label("loc_1B50")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0042
    ChrTalk(
        0x101,
        "#00000F#12P（好……去邀请艾莉吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1B87")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0043
    ChrTalk(
        0x101,
        "#00000F#12P（好……去邀请缇欧吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1BBE")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0044
    ChrTalk(
        0x101,
        "#00000F#12P（好……去邀请兰迪吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1BF5")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0045
    ChrTalk(
        0x101,
        "#00000F#12P（好……去邀请诺艾尔吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1C2E")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0046
    ChrTalk(
        0x101,
        "#00000F#12P（好……去邀请瓦吉吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1C65")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0047
    ChrTalk(
        0x101,
        "#00000F#12P（好……去邀请琪雅吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1C9C")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0048
    ChrTalk(
        0x101,
        "#00000F#12P（好……去邀请芙兰吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1CD3")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0049
    ChrTalk(
        0x101,
        "#00000F#12P（好……去邀请塞茜尔姐姐吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1D10")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0050
    ChrTalk(
        0x101,
        "#00000F#12P（好……去邀请伊莉娅小姐吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1D4D")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0051
    ChrTalk(
        0x101,
        "#00000F#12P（好……去邀请莉夏吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1D84")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0052
    ChrTalk(
        0x101,
        "#00000F#12P（好……去邀请修利吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1DBB")

    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch05100.itc", 0x20)
    LoadChrToIndex("chr/ch05200.itc", 0x21)
    LoadChrToIndex("apl/ch51356.itc", 0x22)
    LoadChrToIndex("chr/ch10000.itc", 0x23)
    SoundLoad(148)
    ClearChrFlags(0x1B, 0x80)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E38"),
        (1, "loc_1E47"),
        (2, "loc_1E56"),
        (3, "loc_1E65"),
        (4, "loc_1E74"),
        (5, "loc_1E7D"),
        (6, "loc_1E8C"),
        (7, "loc_1E9B"),
        (8, "loc_1EAA"),
        (9, "loc_1EB9"),
        (10, "loc_1EC8"),
        (SWITCH_DEFAULT, "loc_1ED7"),
    )


    label("loc_1E38")

    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x0)
    Jump("loc_1ED7")

    label("loc_1E47")

    LoadChrToIndex("chr/ch00202.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x1)
    Jump("loc_1ED7")

    label("loc_1E56")

    LoadChrToIndex("chr/ch00302.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x2)
    Jump("loc_1ED7")

    label("loc_1E65")

    LoadChrToIndex("chr/ch02902.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x3)
    Jump("loc_1ED7")

    label("loc_1E74")

    SetChrChipByIndex(0x1B, 0x4)
    Jump("loc_1ED7")

    label("loc_1E7D")

    LoadChrToIndex("chr/ch08202.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x5)
    Jump("loc_1ED7")

    label("loc_1E8C")

    LoadChrToIndex("chr/ch08502.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x6)
    Jump("loc_1ED7")

    label("loc_1E9B")

    LoadChrToIndex("chr/ch07502.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x7)
    Jump("loc_1ED7")

    label("loc_1EAA")

    LoadChrToIndex("chr/ch05102.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x20)
    Jump("loc_1ED7")

    label("loc_1EB9")

    LoadChrToIndex("chr/ch05202.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x21)
    Jump("loc_1ED7")

    label("loc_1EC8")

    LoadChrToIndex("chr/ch10002.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x8)
    Jump("loc_1ED7")

    label("loc_1ED7")

    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x101, -950, 0, -16000, 0)
    SetChrPos(0x1B, -250, 0, -16700, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0053
    ChrTalk(
        0x14,
        "那就把票给我吧。\x02",
    )

    CloseMessageWindow()
    SubItemNumber('米修拉姆·奇幻乐园游乐券', 1)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0054
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将一张票交给了工作人员。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0055
    ChrTalk(
        0x14,
        "两位客人请进～！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0x1E)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FB4")
    SetChrChipByIndex(0x1B, 0x12)
    Jump("loc_1FB8")

    label("loc_1FB4")

    SetChrChipByIndex(0x1B, 0x1F)

    label("loc_1FB8")

    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 999000, 200, 0, 90)
    SetChrPos(0x1B, 1001000, 200, 0, 270)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_202B"),
        (1, "loc_2033"),
        (2, "loc_203B"),
        (3, "loc_2043"),
        (4, "loc_204B"),
        (5, "loc_2053"),
        (6, "loc_205B"),
        (7, "loc_2063"),
        (8, "loc_206B"),
        (9, "loc_2073"),
        (10, "loc_207B"),
        (SWITCH_DEFAULT, "loc_2083"),
    )


    label("loc_202B")

    Call(0, 40)
    Jump("loc_2083")

    label("loc_2033")

    Call(0, 41)
    Jump("loc_2083")

    label("loc_203B")

    Call(0, 42)
    Jump("loc_2083")

    label("loc_2043")

    Call(0, 43)
    Jump("loc_2083")

    label("loc_204B")

    Call(0, 44)
    Jump("loc_2083")

    label("loc_2053")

    Call(0, 45)
    Jump("loc_2083")

    label("loc_205B")

    Call(0, 46)
    Jump("loc_2083")

    label("loc_2063")

    Call(0, 47)
    Jump("loc_2083")

    label("loc_206B")

    Call(0, 48)
    Jump("loc_2083")

    label("loc_2073")

    Call(0, 49)
    Jump("loc_2083")

    label("loc_207B")

    Call(0, 50)
    Jump("loc_2083")

    label("loc_2083")

    SetChrFlags(0x1B, 0x80)
    OP_49()
    OP_D7(0x1E)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_209B")
    OP_D7(0x1F)

    label("loc_209B")

    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_20EE"),
        (1, "loc_20FC"),
        (2, "loc_210A"),
        (3, "loc_2118"),
        (4, "loc_2126"),
        (5, "loc_2134"),
        (6, "loc_2142"),
        (7, "loc_2150"),
        (8, "loc_215E"),
        (9, "loc_216C"),
        (10, "loc_217A"),
        (SWITCH_DEFAULT, "loc_2188"),
    )


    label("loc_20EE")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2188")

    label("loc_20FC")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2188")

    label("loc_210A")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2188")

    label("loc_2118")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2188")

    label("loc_2126")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2188")

    label("loc_2134")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2188")

    label("loc_2142")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2188")

    label("loc_2150")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2188")

    label("loc_215E")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2188")

    label("loc_216C")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2188")

    label("loc_217A")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2188")

    label("loc_2188")

    OP_D2(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21C0")
    StopSound(821, 1000, 40)
    StopSound(126, 1000, 70)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()

    label("loc_21C0")

    Jump("loc_21F8")

    label("loc_21C5")


    #C0056
    ChrTalk(
        0x14,
        "哎呀，您不坐了吗？\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x14,
        "期待您的再次光临！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_21F8")

    Call(0, 27)
    OP_4C(0x14, 0xFF)
    SetChrPos(0x0, 0, 0, -16500, 180)
    EventEnd(0x5)
    Return()

    # Function_25_185C end

    def Function_26_2213(): pass

    label("Function_26_2213")

    SetChrFlags(0xC, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    Return()

    # Function_26_2213 end

    def Function_27_2250(): pass

    label("Function_27_2250")

    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0x10, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0x11, 0x8)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0x13, 0x8)
    Return()

    # Function_27_2250 end

    def Function_28_228D(): pass

    label("Function_28_228D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_232E")
    SetMapObjFrame(0xFF, "sky01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_in", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_in", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_y_in", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_y_in", 0x1, 0x1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x1F4, 0x0)
    Jump("loc_2397")

    label("loc_232E")

    SetMapObjFrame(0xFF, "sky01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_in", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_in", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_y_in", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_y_in", 0x0, 0x1)

    label("loc_2397")

    Return()

    # Function_28_228D end

    def Function_29_2398(): pass

    label("Function_29_2398")

    Sleep(500)
    FadeToBright(1000, 0)
    OP_68(-11850, 18700, -640, 0)
    OP_68(-11850, 21700, -640, 5000)
    MoveCamera(35, 22, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(26940, 0)
    OP_0D()
    Sleep(3000)
    StopSound(126, 1000, 70)
    StopSound(821, 1000, 40)
    VolumeBGM(0x46, 0x1F4)
    Return()

    # Function_29_2398 end

    def Function_30_23FA(): pass

    label("Function_30_23FA")

    StopSound(148, 500, 70)
    Sound(821, 2, 50, 0)
    Sound(126, 2, 80, 0)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_68(1020, 38900, 2930, 0)
    MoveCamera(330, 11, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(31100, 0)
    SetCameraDistance(28100, 5000)
    OP_0D()
    Sleep(3000)
    StopSound(126, 1000, 70)
    StopSound(821, 1000, 40)
    VolumeBGM(0x46, 0x1F4)
    Return()

    # Function_30_23FA end

    def Function_31_2469(): pass

    label("Function_31_2469")

    StopSound(148, 500, 70)
    Sound(821, 2, 50, 0)
    Sound(126, 2, 80, 0)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_68(11580, 21300, -1090, 0)
    OP_68(11580, 18300, -1090, 5000)
    MoveCamera(331, 30, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(26940, 0)
    OP_0D()
    Sleep(3000)
    StopSound(126, 1000, 70)
    StopSound(821, 1000, 40)
    VolumeBGM(0x46, 0x1F4)
    Return()

    # Function_31_2469 end

    def Function_32_24E0(): pass

    label("Function_32_24E0")

    Sound(148, 2, 80, 0)
    Fade(1000)
    SetMapObjFrame(0xFF, "Null_in", 0x2, "loop00")
    OP_68(1000000, 1350, 0, 0)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_252C")
    MoveCamera(30, 23, 0, 0)
    Jump("loc_2537")

    label("loc_252C")

    MoveCamera(45, 23, 0, 0)

    label("loc_2537")

    OP_6E(600, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    Return()

    # Function_32_24E0 end

    def Function_33_254B(): pass

    label("Function_33_254B")

    Sound(148, 2, 80, 0)
    Fade(1000)
    SetMapObjFrame(0xFF, "Null_in", 0x2, "loop01")
    OP_68(1000000, 1350, 0, 0)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2597")
    MoveCamera(30, 23, 0, 0)
    Jump("loc_25A2")

    label("loc_2597")

    MoveCamera(45, 23, 0, 0)

    label("loc_25A2")

    OP_6E(600, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    Return()

    # Function_33_254B end

    def Function_34_25B6(): pass

    label("Function_34_25B6")

    Sound(148, 2, 80, 0)
    Fade(1000)
    SetMapObjFrame(0xFF, "Null_in", 0x2, "goal")
    OP_68(1000000, 1350, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    Return()

    # Function_34_25B6 end

    def Function_35_2601(): pass

    label("Function_35_2601")

    Sleep(500)
    SetChrPos(0x101, 400, 0, -15500, 90)
    SetChrPos(0x1B, 1600, 0, -15500, 270)
    FadeToBright(1000, 0)
    OP_68(1100, 1700, -15500, 0)
    OP_68(1100, 1300, -15500, 2500)
    MoveCamera(45, 24, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(7500, 0)
    OP_6F(0x79)
    OP_0D()
    Return()

    # Function_35_2601 end

    def Function_36_2672(): pass

    label("Function_36_2672")

    Fade(250)
    Sound(812, 0, 100, 0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_26D6"),
        (1, "loc_26DF"),
        (2, "loc_26E8"),
        (3, "loc_26F1"),
        (4, "loc_26FA"),
        (5, "loc_2703"),
        (6, "loc_270C"),
        (7, "loc_2715"),
        (8, "loc_271E"),
        (9, "loc_2727"),
        (10, "loc_2730"),
        (SWITCH_DEFAULT, "loc_2739"),
    )


    label("loc_26D6")

    SetChrChipByIndex(0x1B, 0x0)
    Jump("loc_2739")

    label("loc_26DF")

    SetChrChipByIndex(0x1B, 0x1)
    Jump("loc_2739")

    label("loc_26E8")

    SetChrChipByIndex(0x1B, 0x2)
    Jump("loc_2739")

    label("loc_26F1")

    SetChrChipByIndex(0x1B, 0x3)
    Jump("loc_2739")

    label("loc_26FA")

    SetChrChipByIndex(0x1B, 0x4)
    Jump("loc_2739")

    label("loc_2703")

    SetChrChipByIndex(0x1B, 0x5)
    Jump("loc_2739")

    label("loc_270C")

    SetChrChipByIndex(0x1B, 0x6)
    Jump("loc_2739")

    label("loc_2715")

    SetChrChipByIndex(0x1B, 0x7)
    Jump("loc_2739")

    label("loc_271E")

    SetChrChipByIndex(0x1B, 0x20)
    Jump("loc_2739")

    label("loc_2727")

    SetChrChipByIndex(0x1B, 0x21)
    Jump("loc_2739")

    label("loc_2730")

    SetChrChipByIndex(0x1B, 0x23)
    Jump("loc_2739")

    label("loc_2739")

    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x101, 999300, 0, 0, 90)
    SetChrPos(0x1B, 1000700, 0, 0, 270)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 37)
    BeginChrThread(0x1B, 3, 0, 38)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x1B, 3)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    StopSound(148, 500, 70)
    Sound(821, 2, 50, 0)
    Sound(126, 2, 80, 0)
    VolumeBGM(0x64, 0x1F4)
    Return()

    # Function_36_2672 end

    def Function_37_27B1(): pass

    label("Function_37_27B1")

    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_27BD():
        OP_96(0xFE, 0xF4240, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27BD)
    Sleep(500)

    def lambda_27DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27DA)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_37_27B1 end

    def Function_38_27EF(): pass

    label("Function_38_27EF")

    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(600)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_2805():
        OP_96(0xFE, 0xF4240, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2805)
    Sleep(500)

    def lambda_2822():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2822)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_38_27EF end

    def Function_39_2837(): pass

    label("Function_39_2837")


    def lambda_283C():
        OP_93(0xFE, 0xB4, 0xC8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_283C)
    OP_93(0x1B, 0xB4, 0x1F4)

    def lambda_2850():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_2850)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x1B, 1)
    EndChrThread(0x101, 0x2)
    Return()

    # Function_39_2837 end

    def Function_40_2877(): pass

    label("Function_40_2877")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00101.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    #N0058
    NpcTalk(
        0x1B,
        "艾莉",
        (
            "#00105F座舱越升越高……\x02\x03",

            "#00102F呵呵，不由自主地紧张起来了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2982")

    #C0059
    ChrTalk(
        0x101,
        (
            "#00002F#6P嗯，我还是第一次坐摩天轮，\x01",
            "感觉心跳加速啊。\x02\x03",

            "#00005F……哎，艾莉，\x01",
            "你以前不是来过\x01",
            "主题公园吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F8")

    label("loc_2982")


    #C0060
    ChrTalk(
        0x101,
        (
            "#00000F#6P嗯，虽然不是第一次坐摩天轮，\x01",
            "但我也感觉心跳加速呢。\x02\x03",

            "#00005F……哎，艾莉，\x01",
            "你以前不是来过\x01",
            "主题公园吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29F8")

    SetChrSubChip(0x1B, 0x0)

    #N0061
    NpcTalk(
        0x1B,
        "艾莉",
        (
            "#00104F嗯，是的……\x02\x03",

            "#00100F但上次来的时候，\x01",
            "玩的都是其它\x01",
            "游乐设施。\x02\x03",

            "#00106F一天时间，很难\x01",
            "把所有游乐设施玩遍呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#00004F#6P是这样啊。\x02\x03",

            "#00009F哈哈，那接下来\x01",
            "可就值得期待了。\x02",
        )
    )

    CloseMessageWindow()

    #N0063
    NpcTalk(
        0x1B,
        "艾莉",
        (
            "#00102F是啊，在最高处看到的风景\x01",
            "究竟会是什么样子呢……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 33)

    #N0064
    NpcTalk(
        0x1B,
        "艾莉",
        "#00102F啊……快看，罗伊德。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#00002F#6P嗯……\x01",
            "风景真漂亮。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D1E")

    #N0066
    NpcTalk(
        0x1B,
        "艾莉",
        (
            "#00109F是啊，晚霞将湖水\x01",
            "映得一片通红……\x02\x03",

            "#00104F呼……真是让人情不自禁地感叹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#00002F#6P是啊……\x01",
            "看来我们赶上了好时段。\x02\x03",

            "#00009F把最后一张票用在这里，\x01",
            "果然是正确决定啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("艾莉")

    #A0068
    AnonymousTalk(
        0xFF,
        (
            "呵呵，罗伊德，\x01",
            "谢谢你邀请我。\x02\x03",

            "如此美丽的风景，\x01",
            "短时间内恐怕是很难忘记了。\x02",
        )
    )

    CloseMessageWindow()
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
        "#00000F#6P哈哈，不用客气。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DA3")

    label("loc_2D1E")


    #N0070
    NpcTalk(
        0x1B,
        "艾莉",
        (
            "#00102F嗯，是啊。\x01",
            "湖水倒映着阳光，\x01",
            "闪烁着熠熠光芒……\x02\x03",

            "#00104F呼……真是让人情不自禁地感叹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        "#00000F#6P哈哈，确实。\x02",
    )

    CloseMessageWindow()

    label("loc_2DA3")

    SetChrSubChip(0x1B, 0x0)
    Sleep(300)
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0072
    NpcTalk(
        0x1B,
        "艾莉",
        "#00105F……啊…………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x2)
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0073
    ChrTalk(
        0x101,
        "#00005F#6P艾莉，怎么了？\x02",
    )

    CloseMessageWindow()

    #N0074
    NpcTalk(
        0x1B,
        "艾莉",
        (
            "#00112F没、没有，那个……\x02\x03",

            "#00113F我们后面的座舱里\x01",
            "坐着一对情侣……\x02\x03",

            "他们……那、那个，在、在接吻……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        "#00005F#6P咦……？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0076
    ChrTalk(
        0x101,
        (
            "#00012F#6P哈、哈哈……那个……\x01",
            "真是如胶似漆啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    #N0077
    NpcTalk(
        0x1B,
        "艾莉",
        (
            "#00109F啊、啊哈哈……是啊。\x01",
            "一直听说摩天轮\x01",
            "很受情侣们的欢迎……\x02\x03",

            "#00106F#1S莫、莫非我们看起来\x01",
            "也像是那种关系……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        "#00005F#6P咦……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #N0079
    NpcTalk(
        0x1B,
        "艾莉",
        (
            "#00109F没、没什么，我什么都没说。\x01",
            "呵呵呵……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        (
            "#00012F#6P啊、啊哈哈哈……\x01",
            "（气氛好像变得很尴尬啊。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    #C0081
    ChrTalk(
        0x101,
        "#00000F#6P……好像快到了呢。\x05\x02",
    )

    CloseMessageWindow()

    #N0082
    NpcTalk(
        0x1B,
        "艾莉",
        "#00100F是啊，我们下去吧。\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    #N0083
    NpcTalk(
        0x1B,
        "艾莉",
        (
            "#00100F#11P呵呵，谢谢，罗伊德。\x01",
            "跟你一起乘坐摩天轮很开心哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#00000F#6P嗯，我也很高兴能邀请到你。\x02\x03",

            "那么，待会见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0085
    NpcTalk(
        0x1B,
        "艾莉",
        "#00100F#11P嗯，再见。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_40_2877 end

    def Function_41_316B(): pass

    label("Function_41_316B")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00201.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    #N0086
    NpcTalk(
        0x1B,
        "缇欧",
        (
            "#00203F……唔，这到底\x01",
            "算是什么情况呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0087
    ChrTalk(
        0x101,
        "#00005F#6P哎，你指什么？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    #N0088
    NpcTalk(
        0x1B,
        "缇欧",
        (
            "#00203F第一次来主题公园，\x01",
            "在摩天轮上和罗伊德前辈独处……\x02\x03",

            "#00200F仔细一想，我认为\x01",
            "这是相当特殊的情况。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_330A")

    #C0089
    ChrTalk(
        0x101,
        (
            "#00012F#6P哈哈……抱歉，\x01",
            "我也是第一次乘坐摩天轮，\x01",
            "总觉得有点紧张。\x02\x03",

            "#00006F听你这么一说，\x01",
            "也许还是多叫几个人\x01",
            "一起坐更加开心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3365")

    label("loc_330A")


    #C0090
    ChrTalk(
        0x101,
        (
            "#00003F#6P唔，也有道理。\x02\x03",

            "#00012F听你这么一说，\x01",
            "也许还是多叫几个人\x01",
            "一起坐更加开心呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3365")


    #N0091
    NpcTalk(
        0x1B,
        "缇欧",
        "#00211F我不是那个意思……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #N0092
    NpcTalk(
        0x1B,
        "缇欧",
        (
            "#00202F……算了。\x01",
            "难得的机会，\x01",
            "我们就随便聊聊吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        "#00000F#6P哈哈，是啊。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    Call(0, 33)

    #N0094
    NpcTalk(
        0x1B,
        "缇欧",
        (
            "#00203F……总之，毫不夸张地说，\x01",
            "咪西的可爱之处\x01",
            "主要就集中在它的八字眉。\x02\x03",

            "#00201F有专家这样说过，哪怕它的角度\x01",
            "出现一丝偏差，都会使如今的大陆\x01",
            "像当年的黑暗时代一样动荡……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0095
    ChrTalk(
        0x101,
        (
            "#00012F#6P那、那个，缇欧……\x01",
            "就快到最高处了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0096
    NpcTalk(
        0x1B,
        "缇欧",
        (
            "#00205F……我好像太过投入了。\x02\x03",

            "#00204F那么，之后的授课\x01",
            "就暂且推后吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        "#00006F#6P（什么时候变成授课了……！？）\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A6")
    SetChrSubChip(0x1B, 0x2)

    #N0098
    NpcTalk(
        0x1B,
        "缇欧",
        (
            "#00205F……好美……\x01",
            "广阔的艾鲁姆湖\x01",
            "被映照得一片通红呢。\x02\x03",

            "#00204F和在港湾区看到的景色相比，\x01",
            "真是完全不同的一番风情。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)

    #C0099
    ChrTalk(
        0x101,
        (
            "#00000F#6P是啊……\x01",
            "看来我们赶上了好时段。\x02\x03",

            "#00009F把最后一张票用在这里，\x01",
            "果然是正确决定啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("缇欧")

    #A0100
    AnonymousTalk(
        0xFF,
        (
            "……罗伊德前辈，\x01",
            "谢谢你邀请我。\x02\x03",

            "这副景象一定会成为我\x01",
            "非常美好的回忆。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0101
    ChrTalk(
        0x101,
        "#00000F#6P哈哈，不用客气。\x02",
    )

    CloseMessageWindow()
    Jump("loc_38F6")

    label("loc_37A6")

    SetChrSubChip(0x1B, 0x1)

    #N0102
    NpcTalk(
        0x1B,
        "缇欧",
        (
            "#00205F罗伊德前辈，\x01",
            "你看乐园广场的方向。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0103
    ChrTalk(
        0x101,
        (
            "#00005F#6P啊……可以看得到\x01",
            "花坛内咪西的脸呢。\x02\x03",

            "#00009F哈哈，看到那个，\x01",
            "就更加真切地体会到了\x01",
            "主题公园的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    #N0104
    NpcTalk(
        0x1B,
        "缇欧",
        (
            "#00202F呵呵，是啊。\x02\x03",

            "#00204F真想把支援科的\x01",
            "楼顶也布置成\x01",
            "那样的园艺造型。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#00006F#6P还、还是不要了。\x01",
            "那样的话，我们的工作地点\x01",
            "未免也太标新立异了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38F6")

    SetChrSubChip(0x1B, 0x0)

    #N0106
    NpcTalk(
        0x1B,
        "缇欧",
        (
            "#00203F……咳，那么，趁着兴致正高，\x01",
            "我们开始下半部分的授课吧。\x02\x03",

            "#00201F刚才我已经说过，\x01",
            "咪西的可爱之处就在于它的眉毛，\x01",
            "根据最近的研究成果……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0107
    ChrTalk(
        0x101,
        (
            "#00006F#6P（看样子，在下去之前，\x01",
            "  只能一直听她讲了啊……）\x02\x03",

            "#00012F（算啦，她好像很开心，这样也不错。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    #C0108
    ChrTalk(
        0x101,
        "#00000F#6P……好像快到了呢。\x05\x02",
    )

    CloseMessageWindow()

    #N0109
    NpcTalk(
        0x1B,
        "缇欧",
        "#00200F是啊，我们下去吧。\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    #N0110
    NpcTalk(
        0x1B,
        "缇欧",
        (
            "#00200F谢谢，罗伊德前辈，\x01",
            "我玩得很愉快。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        (
            "#00000F#6P嗯，我也很高兴能邀请到你。\x02\x03",

            "那么，待会见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0112
    NpcTalk(
        0x1B,
        "缇欧",
        "#00200F好的，稍后再见。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_41_316B end

    def Function_42_3B27(): pass

    label("Function_42_3B27")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00301.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)
    Sleep(500)
    SetChrSubChip(0x1B, 0x0)

    #N0113
    NpcTalk(
        0x1B,
        "兰迪",
        (
            "#00306F唉，两个大男人竟然\x01",
            "一起坐摩天轮。\x02\x03",

            "#00301F罗伊德，你……该不会\x01",
            "真的把我当成目标了吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CA8")

    #C0114
    ChrTalk(
        0x101,
        (
            "#00006F#6P喂……\x01",
            "我可没有那种兴趣。\x02\x03",

            "#00000F只是因为你以前来过，\x01",
            "对主题公园\x01",
            "应该很熟悉。\x02\x03",

            "#00002F有你陪伴，我就可以尽情的\x01",
            "享受初次乘坐摩天轮时看到的风景了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D43")

    label("loc_3CA8")


    #C0115
    ChrTalk(
        0x101,
        (
            "#00006F#6P喂……\x01",
            "我可没有那种兴趣。\x02\x03",

            "#00000F只是因为你以前来过，\x01",
            "对主题公园\x01",
            "应该很熟悉。\x02\x03",

            "#00002F有你陪伴，\x01",
            "在摩天轮上欣赏风景时\x01",
            "或许会有什么新发现。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D43")


    #N0116
    NpcTalk(
        0x1B,
        "兰迪",
        (
            "#00305F什么嘛，原来你把我\x01",
            "当成了导览指南的替代品吗？\x02\x03",

            "#00308F看来我在你的眼中只是个\x01",
            "招之即来，挥之即去的男人……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0117
    ChrTalk(
        0x101,
        (
            "#00011F#6P啊啊，不要总说\x01",
            "这种容易产生\x01",
            "误会的话啊！\x02",
        )
    )

    CloseMessageWindow()

    #N0118
    NpcTalk(
        0x1B,
        "兰迪",
        "#00309F哇哈哈，开个玩笑啦。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    Call(0, 33)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)

    #C0119
    ChrTalk(
        0x101,
        "#00002F#6P……马上就到最高处了呢。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x2)

    #N0120
    NpcTalk(
        0x1B,
        "兰迪",
        (
            "#00304F是啊，快了。\x02\x03",

            "#00300F虽然比不上兰花塔，\x01",
            "但也有相当的高度，\x01",
            "在这里看到的风景堪称一绝呢。\x02\x03",

            "而且身处这种封闭的座舱，\x01",
            "气氛非常好，\x01",
            "俘获芳心的成功率也会加倍。\x02\x03",

            "#00309F对于想让关系进一步发展的男女来说，\x01",
            "实在是再理想不过的好地方了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0121
    ChrTalk(
        0x101,
        "#00006F#6P……你在说什么啊。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1B, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41E2")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("兰迪")

    #A0122
    AnonymousTalk(
        0xFF,
        (
            "哈哈，算是一点\x01",
            "恋爱方面的指导吧。\x02\x03",

            "话说回来……\x01",
            "你居然在这种夕阳照耀的\x01",
            "绝妙时段邀请我。\x02\x03",

            "这明明是向女孩子\x01",
            "发动进攻的最佳时机啊，\x01",
            "你到底在想什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0123
    ChrTalk(
        0x101,
        (
            "#00012F#6P你、你把我当成什么人了？\x02\x03",

            "#00000F……我只是觉得，这次同行的伙伴中，\x01",
            "女性数量相当多。\x02\x03",

            "所以，偶尔创造一些这样的时间，\x01",
            "和兰迪聊聊天也不错呢。\x02\x03",

            "#00009F话说回来，没想到能看到这么美的夕阳……\x01",
            "把最后一张票用在这里，果然是正确决定啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_432E")

    label("loc_41E2")


    #N0124
    NpcTalk(
        0x1B,
        "兰迪",
        (
            "#00309F哈哈，算是一点\x01",
            "恋爱方面的指导吧。\x02\x03",

            "#00303F话说回来……\x01",
            "难得坐一次摩天轮，\x01",
            "你居然邀请我。\x02\x03",

            "#00301F这明明是向女孩子发动进攻的最佳场所啊，\x01",
            "你到底在想什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#00012F#6P你、你把我当成什么人了？\x02\x03",

            "#00000F……我只是觉得，这次同行的伙伴中，\x01",
            "女性数量相当多。\x02\x03",

            "#00004F所以，偶尔创造一些这样的时间，\x01",
            "和兰迪聊聊天也不错呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_432E")

    OP_63(0x1B, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #N0126
    NpcTalk(
        0x1B,
        "兰迪",
        (
            "#00306F唉，你小子还真是\x01",
            "无意之间就能打动人心啊……\x02\x03",

            "#00300F算啦，我就接受\x01",
            "你的好意吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 31)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 34)
    Sleep(3000)

    #C0127
    ChrTalk(
        0x101,
        "#00000F#6P……好像快到了呢。\x05\x02",
    )

    CloseMessageWindow()

    #N0128
    NpcTalk(
        0x1B,
        "兰迪",
        "#00300F是啊，我们下去吧。\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    #N0129
    NpcTalk(
        0x1B,
        "兰迪",
        (
            "#00300F谢谢你邀请我啦，\x01",
            "还算挺开心的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        (
            "#00000F#6P嗯，我也很高兴能邀请到你。\x02\x03",

            "那么，待会见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0131
    NpcTalk(
        0x1B,
        "兰迪",
        "#00300F嗯，我走啦。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_42_3B27 end

    def Function_43_44AE(): pass

    label("Function_43_44AE")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10101.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    #N0132
    NpcTalk(
        0x1B,
        "诺艾尔",
        "#10101F………………………………\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        "#00005F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #N0134
    NpcTalk(
        0x1B,
        "诺艾尔",
        "#10106F………………………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0135
    ChrTalk(
        0x101,
        (
            "#00006F#6P……那个，诺艾尔，\x01",
            "你为什么一直默不作声？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x1B, 0x0)

    #N0136
    NpcTalk(
        0x1B,
        "诺艾尔",
        (
            "#10105F啊，没有！那个……\x01",
            "因为我还是第一次和男性\x01",
            "一起乘坐摩天轮。\x02\x03",

            "#10100F上次来主题公园，\x01",
            "是和芙兰一起坐的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46C4")

    #C0137
    ChrTalk(
        0x101,
        (
            "#00009F#6P是、是吗……原来如此。\x02\x03",

            "#00000F好啦，别紧张，我还是第一次坐摩天轮呢。\x01",
            "希望你能多告诉我一些享受心得。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4739")

    label("loc_46C4")


    #C0138
    ChrTalk(
        0x101,
        (
            "#00009F#6P是、是吗……原来如此。\x02\x03",

            "#00000F好啦，别紧张，\x01",
            "我也没坐过几次摩天轮……\x01",
            "希望你能多告诉我一些享受心得。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4739")


    #N0139
    NpcTalk(
        0x1B,
        "诺艾尔",
        "#10102F好、好的！没问题！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 33)

    #N0140
    NpcTalk(
        0x1B,
        "诺艾尔",
        (
            "#10100F已经升得很高了呢。\x02\x03",

            "#10104F唔……在这里看到的\x01",
            "风景果然很棒。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#00009F#6P是啊，风景确实很好呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)
    SetChrSubChip(0x1B, 0x0)

    #N0142
    NpcTalk(
        0x1B,
        "诺艾尔",
        (
            "#10106F那个……罗伊德警官，\x01",
            "邀请我\x01",
            "真的好吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0143
    ChrTalk(
        0x101,
        "#00005F#6P咦，为什么这么问？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A34")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("诺艾尔")

    #A0144
    AnonymousTalk(
        0xFF,
        (
            "那个……难得赶上\x01",
            "如此美丽的夕阳。\x02\x03",

            "还是邀请艾莉小姐或塞茜尔小姐\x01",
            "那种更加优秀的女性比较好吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0145
    ChrTalk(
        0x101,
        (
            "#00003F#6P唔……你没必要\x01",
            "这样妄自菲薄啊。\x02\x03",

            "#00000F我认为诺艾尔\x01",
            "也有可爱之处。\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0146
    NpcTalk(
        0x1B,
        "诺艾尔",
        "#10114F#4S哎？\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#00009F#6P话说回来，好美的夕阳……\x01",
            "把最后一张票用在这里，\x01",
            "果然是正确决定啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AF2")

    label("loc_4A34")


    #N0148
    NpcTalk(
        0x1B,
        "诺艾尔",
        (
            "#10108F那个……难得坐一次摩天轮。\x02\x03",

            "还是邀请艾莉小姐或塞茜尔小姐\x01",
            "那种更加优秀的女性比较好吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#00003F#6P唔……你没必要\x01",
            "这样妄自菲薄啊。\x02\x03",

            "#00000F我认为诺艾尔\x01",
            "也有可爱之处。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AF2")

    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)

    #C0150
    ChrTalk(
        0x101,
        (
            "#00005F#6P哎？\x01",
            "我说了什么奇怪的话吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0151
    NpcTalk(
        0x1B,
        "诺艾尔",
        (
            "#10109F没、没有……\x01",
            "那个……谢谢。\x02\x03",

            "#10106F（他完全不觉得刚才的话有什么问题吗……）\x02\x03",

            "#10101F（罗伊德警官似乎比我\x01",
            "  想象中还要危险啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1B)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0152
    ChrTalk(
        0x101,
        (
            "#00006F#6P（唔……\x01",
            "  又开始默不作声了啊。\x01",
            "  难道我说了什么奇怪的话吗……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    #C0153
    ChrTalk(
        0x101,
        "#00000F#6P……好像快到了呢。\x05\x02",
    )

    CloseMessageWindow()

    #N0154
    NpcTalk(
        0x1B,
        "诺艾尔",
        (
            "#10100F啊，是的，\x01",
            "我们下去吧。\x05\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    #N0155
    NpcTalk(
        0x1B,
        "诺艾尔",
        (
            "#10100F谢谢你\x01",
            "邀请我，\x01",
            "我玩得很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        (
            "#00000F#6P嗯，我也很高兴能邀请到你。\x02\x03",

            "那么，待会见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0157
    NpcTalk(
        0x1B,
        "诺艾尔",
        "#10100F好的，再见！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_43_44AE end

    def Function_44_4D58(): pass

    label("Function_44_4D58")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10301.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)
    Sleep(500)
    SetChrSubChip(0x101, 0x0)

    #C0158
    ChrTalk(
        0x101,
        (
            "#00000F#6P……对了，瓦吉，\x01",
            "你坐过摩天轮吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    #N0159
    NpcTalk(
        0x1B,
        "瓦吉",
        (
            "#10309F呵呵，没坐过几次。\x02\x03",

            "#10300F和俱乐部的客人一起来米修拉姆时，\x01",
            "一般都会选择酒吧\x01",
            "这种安静的地方。\x02\x03",

            "#10304F所以，主题公园对我而言\x01",
            "其实是很新鲜的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F28")

    #C0160
    ChrTalk(
        0x101,
        (
            "#00000F#6P呵呵……这倒是有点意外。\x02\x03",

            "#00003F大概是因为\x01",
            "第一次坐摩天轮吧，\x01",
            "我感觉相当紧张呢。\x02\x03",

            "#00002F哈哈，仔细想想，也有点奇怪呢，\x01",
            "这又不是刺激型的游乐设施。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FD6")

    label("loc_4F28")


    #C0161
    ChrTalk(
        0x101,
        (
            "#00000F#6P呵呵……这倒是有点意外。\x02\x03",

            "#00003F虽然我刚才已经坐过摩天轮了，\x01",
            "但是还没有习惯，感觉很紧张呢。\x02\x03",

            "#00002F哈哈，仔细想想，也有点奇怪呢，\x01",
            "这又不是刺激型的游乐设施。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FD6")


    #N0162
    NpcTalk(
        0x1B,
        "瓦吉",
        (
            "#10300F不，我认为摩天轮应该\x01",
            "归为恐怖类项目。\x02\x03",

            "#10304F有些人光是身在高处就会害怕……\x02\x03",

            "#10302F更何况，万一吊着\x01",
            "座舱的连接部分出现问题，\x01",
            "就会酿成重大惨剧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0163
    ChrTalk(
        0x101,
        (
            "#00006F#6P不要突然说这种\x01",
            "让人不安的话啊……\x02",
        )
    )

    CloseMessageWindow()

    #N0164
    NpcTalk(
        0x1B,
        "瓦吉",
        (
            "#10309F呵呵，找点刺激不好吗？\x02\x03",

            "#10304F算了，现在就专心享受摩天轮的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 33)

    #C0165
    ChrTalk(
        0x101,
        "#00000F#6P快到最高处了吧……\x02",
    )

    CloseMessageWindow()

    #N0166
    NpcTalk(
        0x1B,
        "瓦吉",
        (
            "#10304F的确升得很高了，\x01",
            "说起来，座舱的移动速度\x01",
            "还真是意外的缓慢呢。\x02\x03",

            "这应该是为了让游客\x01",
            "尽情欣赏美景吧……\x02\x03",

            "#10302F呵呵，但也有可能是考虑到\x01",
            "吊桥效应才这样设计的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0167
    ChrTalk(
        0x101,
        (
            "#00005F#6P哦，就是心跳因恐惧感而加快，\x01",
            "从而产生疑似恋爱的感觉吧……\x01",
            "我以前也听说过。\x02\x03",

            "#00009F来这里的情侣很多，\x01",
            "也许真被你说中了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1B, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5430")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("瓦吉")

    #A0168
    AnonymousTalk(
        0xFF,
        (
            "呵呵，托你的福，\x01",
            "让我欣赏到了\x01",
            "如此美丽的夕阳。\x02\x03",

            "在这种情况下，就算对你\x01",
            "萌生爱意也不奇怪呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0169
    ChrTalk(
        0x101,
        (
            "#00012F#6P不、不不不……\x02\x03",

            "虽然看到这么美的夕阳后，\x01",
            "我也觉得把最后一张票用在这里\x01",
            "是正确决定……\x02\x03",

            "#00003F但、但绝不会出现你说的那种情况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54F2")

    label("loc_5430")


    #N0170
    NpcTalk(
        0x1B,
        "瓦吉",
        (
            "#10304F呵呵，两个人在密闭空间内独处……\x02\x03",

            "#10309F在这种情况下，就算对你\x01",
            "萌生爱意也不奇怪呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0171
    ChrTalk(
        0x101,
        (
            "#00012F#6P不、不不不……\x02\x03",

            "#00003F不会不会，不会有那种事的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54F2")


    #N0172
    NpcTalk(
        0x1B,
        "瓦吉",
        (
            "#10304F呵呵，真冷淡啊，\x01",
            "我可是认真的哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0173
    ChrTalk(
        0x101,
        (
            "#00011F#6P都、都和你说过了！\x01",
            "别再说这种奇怪的话啦！\x02",
        )
    )

    CloseMessageWindow()

    #N0174
    NpcTalk(
        0x1B,
        "瓦吉",
        (
            "#10309F呵呵，戏弄你\x01",
            "果然很好玩呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    #C0175
    ChrTalk(
        0x101,
        "#00000F#6P……好像快到了。\x05\x02",
    )

    CloseMessageWindow()

    #N0176
    NpcTalk(
        0x1B,
        "瓦吉",
        "#10300F是啊，我们下去吧。\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    #N0177
    NpcTalk(
        0x1B,
        "瓦吉",
        "#10300F呵呵，玩得很开心。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#00000F#6P嗯，我也很高兴能邀请到你。\x02\x03",

            "那么，待会见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0179
    NpcTalk(
        0x1B,
        "瓦吉",
        "#10300F嗯，待会见。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_44_4D58 end

    def Function_45_5693(): pass

    label("Function_45_5693")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01102.itp")
    Call(0, 29)
    SetChrSubChip(0x101, 0x1)
    SetChrPos(0x1B, 1000260, 0, 970, 0)
    SetChrChipByIndex(0x1B, 0x5)
    SetChrSubChip(0x1B, 0x0)
    Call(0, 32)
    OP_63(0x1B, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #N0180
    NpcTalk(
        0x1B,
        "琪雅",
        "#01105F#11P哇，越升越高了！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_9C(0x1B, 0x0, 0x0, 0x0, 0x12C, 0x7D0)
    OP_82(0x0, 0x32, 0x5DC, 0x12C)
    Sleep(100)
    OP_9C(0x1B, 0x0, 0x0, 0x0, 0x12C, 0x7D0)
    OP_82(0x0, 0x32, 0x5DC, 0x12C)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0181
    ChrTalk(
        0x101,
        (
            "#00012F#6P琪、琪雅，让座舱摇晃是很危险的，\x01",
            "在这里面要乖乖坐好哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1B, 0xE1, 0x1F4)

    #N0182
    NpcTalk(
        0x1B,
        "琪雅",
        (
            "#01105F#11P啊，说的也对呢。\x02\x03",

            "#01109F嘿嘿嘿，我太兴奋了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_95(0x1B, 1000610, 0, 40, 2000, 0x0)
    OP_93(0x1B, 0x10E, 0x1F4)
    Fade(250)
    SetChrChipByIndex(0x1B, 0x1F)
    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x1B, 1001000, 200, 0, 270)
    OP_0D()

    #N0183
    NpcTalk(
        0x1B,
        "琪雅",
        (
            "#01100F罗伊德，罗伊德。\x02\x03",

            "#01109F在最高处看到的风景\x01",
            "是不是非常漂亮呢？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5915")

    #C0184
    ChrTalk(
        0x101,
        (
            "#00004F#6P哦，我也是第一次坐摩天轮，\x01",
            "所以还不清楚……\x02\x03",

            "#00000F但肯定很值得期待。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5961")

    label("loc_5915")


    #C0185
    ChrTalk(
        0x101,
        (
            "#00004F#6P是啊，我刚才也坐过，\x01",
            "风景确实很好。\x02\x03",

            "#00000F非常值得期待哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5961")

    OP_63(0x1B, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)

    #N0186
    NpcTalk(
        0x1B,
        "琪雅",
        (
            "#01109F（兴奋）……\x01",
            "真期待！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x1B, 0x5)
    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x1B, 1000610, 0, 40, 270)
    OP_0D()
    OP_9C(0x1B, 0x0, 0x0, 0x0, 0x12C, 0x7D0)
    OP_82(0x0, 0x32, 0x5DC, 0x12C)
    Sleep(100)
    OP_9C(0x1B, 0x0, 0x0, 0x0, 0x12C, 0x7D0)
    OP_82(0x0, 0x32, 0x5DC, 0x12C)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0187
    ChrTalk(
        0x101,
        "#00011F#6P我、我知道了，你冷静一点。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    SetChrSubChip(0x101, 0x1)
    SetChrPos(0x1B, 1000260, 0, 970, 0)
    SetChrChipByIndex(0x1B, 0x5)
    SetChrSubChip(0x1B, 0x0)
    Call(0, 33)
    OP_63(0x1B, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C1A")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("琪雅")

    #A0188
    AnonymousTalk(
        0xFF,
        (
            "哇啊啊啊，好高！！\x02\x03",

            "而且天空一片通红，\x01",
            "好漂亮！！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0189
    ChrTalk(
        0x101,
        (
            "#00004F#6P是啊……\x01",
            "看来我们赶上了好时段。\x02\x03",

            "#00009F把最后一张票用在这里，\x01",
            "果然是正确决定啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0190
    NpcTalk(
        0x1B,
        "琪雅",
        (
            "#01102F#11P嘿嘿嘿，谢谢你邀请我。\x02\x03",

            "#01110F啊，快看快看，罗伊德！\x01",
            "刚才有鱼在跳啊！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C74")

    label("loc_5C1A")


    #N0191
    NpcTalk(
        0x1B,
        "琪雅",
        (
            "#01110F#11P哇啊啊啊，好高！！\x02\x03",

            "#01109F啊，快看快看，罗伊德！\x01",
            "刚才有鱼在跳啊！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C74")


    #C0192
    ChrTalk(
        0x101,
        (
            "#00002F#6P是啊，那是什么鱼呢？\x01",
            "实在是看不清楚……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)
    OP_93(0x1B, 0xE1, 0x1F4)

    #N0193
    NpcTalk(
        0x1B,
        "琪雅",
        (
            "#01105F#11P说起来……\x02\x03",

            "#01100F罗伊德，这里的风景\x01",
            "和在兰花塔上看到的风景，\x01",
            "哪个比较好看？\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        (
            "#00005F#6P嗯？这个嘛……\x01",
            "要说高度的话，那毫无疑问，\x01",
            "还是兰花塔更高……\x02\x03",

            "#00003F但两处风景完全不同，\x01",
            "很难断言哪一方\x01",
            "更胜一筹。\x02",
        )
    )

    CloseMessageWindow()

    #N0195
    NpcTalk(
        0x1B,
        "琪雅",
        (
            "#01103F#11P嗯嗯，原来如此……\x02\x03",

            "#01109F……罗伊德说的话好深奥！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1B, 0x0, 0x1F4)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0196
    ChrTalk(
        0x101,
        (
            "#00012F#6P你的兴致真高啊……\x02\x03",

            "#00004F（……呼，有精神就好，\x01",
            "  暂时可以安心了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0197
    NpcTalk(
        0x1B,
        "琪雅",
        "#01110F#11P啊，又有鱼在跳！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x1B, 0x1F)
    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x1B, 1001000, 200, 0, 270)
    Call(0, 34)
    Sleep(3000)

    #C0198
    ChrTalk(
        0x101,
        (
            "#00000F#6P……好像快到了呢。\x01",
            "琪雅，我们下去吧。\x05\x02",
        )
    )

    CloseMessageWindow()

    #N0199
    NpcTalk(
        0x1B,
        "琪雅",
        "#01100F嗯，好的！\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    #N0200
    NpcTalk(
        0x1B,
        "琪雅",
        (
            "#01109F嘿嘿，风景很好，\x01",
            "玩得非常开心呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        (
            "#00000F#6P嗯，我也很高兴能邀请到你。\x02\x03",

            "那么，待会见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0202
    NpcTalk(
        0x1B,
        "琪雅",
        "#01100F嗯！再见啦，罗伊德！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_45_5693 end

    def Function_46_5FE6(): pass

    label("Function_46_5FE6")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06400.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)
    OP_63(0x1B, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #N0203
    NpcTalk(
        0x1B,
        "芙兰",
        (
            "#06404F这种逐渐\x01",
            "离开地面的感觉……\x02\x03",

            "#06409F嘿嘿，每次一坐上摩天轮，\x01",
            "就会觉得心跳加速～\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_611B")

    #C0204
    ChrTalk(
        0x101,
        (
            "#00004F#6P嗯，我也很紧张，\x01",
            "毕竟这是我第一次坐摩天轮呢。\x02\x03",

            "#00000F但相比紧张，\x01",
            "你的表现更像是兴奋吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_617A")

    label("loc_611B")


    #C0205
    ChrTalk(
        0x101,
        (
            "#00004F#6P哈哈，我理解你的心情，\x01",
            "确实很紧张。\x02\x03",

            "#00000F但相比紧张，\x01",
            "你的表现更像是兴奋吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_617A")

    SetChrSubChip(0x1B, 0x0)

    #N0206
    NpcTalk(
        0x1B,
        "芙兰",
        (
            "#06402F啊，看得出来吗～？\x02\x03",

            "#06404F毕竟我从没和男性\x01",
            "一起坐过摩天轮～\x02\x03",

            "#06409F更何况这次还是和罗伊德警官一起！\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x101,
        (
            "#00009F#6P哈哈，我好像还没资格\x01",
            "让别人用『更何况』来形容……\x02\x03",

            "#00000F但仔细想想，和你独处的时候\x01",
            "确实很少呢。\x02",
        )
    )

    CloseMessageWindow()

    #N0208
    NpcTalk(
        0x1B,
        "芙兰",
        (
            "#06409F呵呵，机会难得，\x01",
            "我们就多聊聊吧～！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 33)

    #N0209
    NpcTalk(
        0x1B,
        "芙兰",
        "#06400F啊，罗伊德警官，快看！\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        "#00000F#6P嗯，快到最高处了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_648F")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("芙兰")

    #A0211
    AnonymousTalk(
        0xFF,
        (
            "啊啊啊啊～真是太棒了。\x02\x03",

            "在通红夕阳的照耀下，\x01",
            "实在是太浪漫了～！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0212
    ChrTalk(
        0x101,
        (
            "#00004F#6P是啊……\x01",
            "看来我们赶上了好时段。\x02\x03",

            "#00009F把最后一张票用在这里，\x01",
            "果然是正确决定啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0213
    NpcTalk(
        0x1B,
        "芙兰",
        (
            "#06402F呵呵，谢谢你\x01",
            "邀请我！\x02\x03",

            "虽然以前和姐姐一起坐过了，\x01",
            "但风景真的好棒啊～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64EF")

    label("loc_648F")


    #N0214
    NpcTalk(
        0x1B,
        "芙兰",
        (
            "#06402F啊啊啊啊～真是太棒了。\x02\x03",

            "#06409F虽然以前和姐姐一起坐过了，\x01",
            "但风景真的好棒啊～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64EF")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    SetChrSubChip(0x101, 0x0)

    #C0215
    ChrTalk(
        0x101,
        (
            "#00005F#6P对了，芙兰，\x01",
            "你以前从没和\x01",
            "男性交往过吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x1B, 0x0)

    #N0216
    NpcTalk(
        0x1B,
        "芙兰",
        (
            "#06405F嗯，是啊……\x01",
            "为什么这么问呢～？\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        (
            "#00012F#6P这、这个……\x01",
            "没什么特别的意思。\x02\x03",

            "#00000F我只是觉得，\x01",
            "你应该很受欢迎吧？\x02",
        )
    )

    CloseMessageWindow()

    #N0218
    NpcTalk(
        0x1B,
        "芙兰",
        (
            "#06402F啊哈哈，我完全不行啦～\x02\x03",

            "#06404F而且，也很难遇到\x01",
            "比姐姐更帅、\x01",
            "更可靠的男人。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0219
    ChrTalk(
        0x101,
        "#00012F#6P你的标准是这样的啊……\x02",
    )

    CloseMessageWindow()

    #N0220
    NpcTalk(
        0x1B,
        "芙兰",
        (
            "#06409F嘿嘿嘿，那当然。\x02\x03",

            "从小时候开始，\x01",
            "姐姐就一直是我心目中最棒的人！\x02\x03",

            "#06400F啊，不过，如果是罗伊德警官，\x01",
            "大概可以勉强及格呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x101,
        (
            "#00009F#6P哈哈……那还真是多谢了。\x01",
            "（她们姐妹间的关系真好啊……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    #C0222
    ChrTalk(
        0x101,
        (
            "#00000F#6P……好像快到了呢。\x01",
            "芙兰，我们下去吧。\x05\x02",
        )
    )

    CloseMessageWindow()

    #N0223
    NpcTalk(
        0x1B,
        "芙兰",
        "#06400F嗯，好的。\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    #N0224
    NpcTalk(
        0x1B,
        "芙兰",
        (
            "#06400F嘿嘿嘿，风景真好，\x01",
            "玩得很开心～！\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#00000F#6P嗯，我也很高兴能邀请到你。\x02\x03",

            "那么，待会见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0226
    NpcTalk(
        0x1B,
        "芙兰",
        "#06400F好的！再见～\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_46_5FE6 end

    def Function_47_6869(): pass

    label("Function_47_6869")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu05900.itp")
    Call(0, 29)
    Call(0, 32)

    #N0227
    NpcTalk(
        0x1B,
        "塞茜尔",
        (
            "#05900F呵呵……座舱里面\x01",
            "原来是这样的啊。\x02\x03",

            "#05904F简直就像一个巨大的摇篮。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_697E")

    #C0228
    ChrTalk(
        0x101,
        (
            "#00004F#6P是啊，我也是第一次坐，\x01",
            "确实有这种感觉呢。\x02\x03",

            "#00000F稍后应该会摇晃得比较厉害，\x01",
            "塞茜尔姐姐，小心一点哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69DE")

    label("loc_697E")


    #C0229
    ChrTalk(
        0x101,
        (
            "#00004F#6P是啊，确实有这种感觉呢。\x02\x03",

            "#00000F稍后会摇晃得比较厉害，\x01",
            "塞茜尔姐姐，小心一点哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69DE")


    #N0230
    NpcTalk(
        0x1B,
        "塞茜尔",
        (
            "#05900F呵呵，谢谢提醒，罗伊德。\x02\x03",

            "#05904F自从纪念庆典时一起去看\x01",
            "彩虹剧团的演出之后，\x01",
            "我们还是第一次独处呢。\x02\x03",

            "#05909F机会难得，\x01",
            "就多聊聊天吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x101,
        (
            "#00005F#6P是、是啊……没错呢。\x02\x03",

            "#00003F（这么一想，\x01",
            "  就不由得紧张起来了……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    Call(0, 33)

    #N0232
    NpcTalk(
        0x1B,
        "塞茜尔",
        (
            "#05904F呵呵，话说回来，\x01",
            "主题公园还真是个有趣的地方呢。\x02\x03",

            "#05902F有可爱的咪西迎接我们，\x01",
            "还有很多好玩的游乐设施……\x01",
            "就像误入了梦幻世界一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x101,
        "#00002F#6P哈哈……的确如此。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0234
    ChrTalk(
        0x101,
        (
            "#00008F#6P如果大哥还活着……\x01",
            "你是不是很想和他一起来呢？\x02",
        )
    )

    CloseMessageWindow()

    #N0235
    NpcTalk(
        0x1B,
        "塞茜尔",
        (
            "#05904F呵呵……有一点吧。\x01",
            "毕竟当时的克洛斯贝尔\x01",
            "还没有这样的地方。\x02\x03",

            "#05900F但是，过去曾和盖伊\x01",
            "约会过好几次，开心程度和\x01",
            "现在相比也毫不逊色呢。\x02\x03",

            "#05909F在吃饭的时候，\x01",
            "他还给我介绍过很多\x01",
            "不错的路边摊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0236
    ChrTalk(
        0x101,
        (
            "#00012F#6P约、约会时去路边摊吃吗……\x02\x03",

            "#00006F难得的约会，\x01",
            "大哥应该找些\x01",
            "有气氛的餐厅啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0237
    NpcTalk(
        0x1B,
        "塞茜尔",
        (
            "#05905F啊，可路边摊的东西非常好吃，\x01",
            "我很喜欢呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x101,
        (
            "#00003F#6P（唔……塞茜尔姐姐和大哥\x01",
            "  果然很相配呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x1B, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F64")

    #N0239
    NpcTalk(
        0x1B,
        "塞茜尔",
        (
            "#05905F啊……快到最高处了呢。\x02\x03",

            "#05909F火红的夕阳真美……\x01",
            "和在医院看到的风景\x01",
            "完全不同呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)

    #C0240
    ChrTalk(
        0x101,
        (
            "#00004F#6P是啊……\x01",
            "看来我们赶上了好时段。\x02\x03",

            "#00009F把最后一张票用在这里，\x01",
            "果然是正确决定啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1B, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("塞茜尔")

    #A0241
    AnonymousTalk(
        0xFF,
        (
            "呵呵，谢谢你邀请我。\x02\x03",

            "这夕阳一定会成为我\x01",
            "美好的回忆。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_7022")

    label("loc_6F64")


    #N0242
    NpcTalk(
        0x1B,
        "塞茜尔",
        (
            "#05905F啊……快到最高处了呢。\x02\x03",

            "#05909F湖水真美……\x01",
            "和在医院看到的风景\x01",
            "完全不同呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)

    #C0243
    ChrTalk(
        0x101,
        "#00002F#6P呵呵……是啊。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    #N0244
    NpcTalk(
        0x1B,
        "塞茜尔",
        (
            "#05902F呵呵，这景色一定会\x01",
            "成为我美好的回忆。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7022")

    SetChrSubChip(0x101, 0x0)

    #C0245
    ChrTalk(
        0x101,
        "#00009F#6P哈哈，看到你这么高兴，我也很开心。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    #C0246
    ChrTalk(
        0x101,
        (
            "#00000F#6P……好像快到了呢。\x01",
            "塞茜尔姐姐，我们下去吧。\x05\x02",
        )
    )

    CloseMessageWindow()

    #N0247
    NpcTalk(
        0x1B,
        "塞茜尔",
        "#05900F嗯，好的。\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    #N0248
    NpcTalk(
        0x1B,
        "塞茜尔",
        (
            "#05900F呵呵，玩得很开心呢。\x01",
            "谢谢，罗伊德。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        (
            "#00000F#6P嗯，我也很高兴能邀请到你。\x02\x03",

            "那么，待会见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0250
    NpcTalk(
        0x1B,
        "塞茜尔",
        "#05900F好的，待会见。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_47_6869 end

    def Function_48_7177(): pass

    label("Function_48_7177")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01700.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    #N0251
    NpcTalk(
        0x1B,
        "伊莉娅",
        (
            "#01704F唔……\x01",
            "对我来说，摩天轮\x01",
            "似乎略欠刺激性……\x02\x03",

            "#01700F不过，偶尔坐坐这种\x01",
            "悠闲的游乐设施也不错呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72CA")

    #C0252
    ChrTalk(
        0x101,
        (
            "#00002F#6P哈哈，听您这么一说，\x01",
            "我好像也轻松多了。\x02\x03",

            "#00004F听说升到最高处之后，\x01",
            "风景相当美丽……\x02\x03",

            "#00000F伊莉娅小姐应该\x01",
            "也会很开心的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7351")

    label("loc_72CA")


    #C0253
    ChrTalk(
        0x101,
        (
            "#00002F#6P哈哈，听您这么一说，\x01",
            "我好像也轻松多了。\x02\x03",

            "#00004F升到最高处之后，\x01",
            "风景相当美丽……\x02\x03",

            "#00000F伊莉娅小姐应该\x01",
            "也会很开心的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7351")

    SetChrSubChip(0x1B, 0x0)

    #N0254
    NpcTalk(
        0x1B,
        "伊莉娅",
        (
            "#01709F风景真有那么好吗？\x01",
            "呵呵，那我就期待一下吧。\x02\x03",

            "#01703F嗯，但照着这种速度，\x01",
            "要到达最高处，恐怕还得花些时间呢。\x02\x03",

            "#01702F呵呵，机会难得，\x01",
            "我们要不要推心置腹地谈谈？\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        (
            "#00012F#6P好、好的，没问题啊。\x01",
            "（总有种不好的预感……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    Call(0, 33)

    #N0256
    NpcTalk(
        0x1B,
        "伊莉娅",
        (
            "#01709F坦白交代吧，警察弟弟，\x01",
            "你的目标到底是谁啊？\x02\x03",

            "#01705F果然还是塞茜尔吧？\x01",
            "或者是同事中的某个女孩？\x01",
            "该不会是我或莉夏吧？\x02\x03",

            "#01704F啊，我事先声明，修利还不行哦。\x01",
            "身为她的监护人，在她长大成人之前……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0257
    ChrTalk(
        0x101,
        (
            "#00006F#6P请、请稍等一下！\x02\x03",

            "#00011F您不停问我把谁\x01",
            "当作目标这种问题……\x01",
            "会……会让我很伤脑筋的！\x02",
        )
    )

    CloseMessageWindow()

    #N0258
    NpcTalk(
        0x1B,
        "伊莉娅",
        (
            "#01706F哎，这有什么嘛。\x01",
            "不用顾虑，偷偷告诉我吧。\x02\x03",

            "#01700F我是塞茜尔的好朋友，\x01",
            "对你来说，不就相当于\x01",
            "另一个姐姐吗～\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#00012F#6P这、这种理由未免太牵强了……\x01",
            "而且塞茜尔姐姐也不是我的亲姐姐。\x02",
        )
    )

    CloseMessageWindow()

    #N0260
    NpcTalk(
        0x1B,
        "伊莉娅",
        (
            "#01709F啊，真不识趣！\x01",
            "既然如此，我就要用\x01",
            "挠痒痒来逼你说实话了哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x101,
        (
            "#00011F#6P（不、不好了，\x01",
            "  必须得想办法换个话题……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)

    #C0262
    ChrTalk(
        0x101,
        (
            "#00005F#6P快、快看啊，伊莉娅小姐！\x01",
            "不知不觉间，\x01",
            "好像已经快到最高处了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x1B, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7939")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("伊莉娅")

    #A0263
    AnonymousTalk(
        0xFF,
        (
            "啊……！\x01",
            "风景确实很好呢。\x02\x03",

            "晚霞将湖面\x01",
            "映照得一片朱红，\x01",
            "似乎有种浓浓的乡愁感……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0264
    ChrTalk(
        0x101,
        (
            "#00004F#6P是啊……\x01",
            "看来我们赶上了好时段。\x02\x03",

            "#00009F把最后一张票用在这里，\x01",
            "果然是正确决定啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0265
    NpcTalk(
        0x1B,
        "伊莉娅",
        (
            "#01709F呵呵，老实说，比我想象中的更美呢。\x01",
            "谢谢你邀请我。\x02\x03",

            "#01703F唔……能不能把这个场面\x01",
            "运用到舞台上呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A18")

    label("loc_7939")


    #N0266
    NpcTalk(
        0x1B,
        "伊莉娅",
        (
            "#01705F啊……！\x01",
            "风景确实很好呢。\x02\x03",

            "#01709F没想到在克洛斯贝尔这种大都市，\x01",
            "还能看到这样的自然风景……\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        (
            "#00000F#6P哈哈……\x01",
            "这样一想，确实觉得很意外。\x02",
        )
    )

    CloseMessageWindow()

    #N0268
    NpcTalk(
        0x1B,
        "伊莉娅",
        (
            "#01703F唔……能不能把这个场面\x01",
            "运用到舞台上呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A18")

    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)

    #C0269
    ChrTalk(
        0x101,
        (
            "#00006F#6P（呼……\x01",
            "  总算分散她的注意力了。）\x02\x03",

            "#00002F（话说回来，她无论何时\x01",
            "  都在想着舞台表演啊。\x01",
            "  真不愧是伊莉娅小姐……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    #C0270
    ChrTalk(
        0x101,
        (
            "#00000F#6P……好像快到了呢。\x01",
            "伊莉娅小姐，我们下去吧。\x05\x02",
        )
    )

    CloseMessageWindow()

    #N0271
    NpcTalk(
        0x1B,
        "伊莉娅",
        "#01700F好的好的～\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    #N0272
    NpcTalk(
        0x1B,
        "伊莉娅",
        (
            "#01700F呵呵，玩得很开心哦，\x01",
            "谢谢了，警察弟弟。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        (
            "#00000F#6P我也很高兴能邀请到您。\x02\x03",

            "那么，待会见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0274
    NpcTalk(
        0x1B,
        "伊莉娅",
        "#01700F嗯，待会见了～\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_48_7177 end

    def Function_49_7BD3(): pass

    label("Function_49_7BD3")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01800.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    #N0275
    NpcTalk(
        0x1B,
        "莉夏",
        (
            "#01802F呼……\x01",
            "摩天轮真好啊。\x02\x03",

            "#01804F既悠闲，又安静，\x01",
            "能使人心情平静。\x02\x03",

            "#01802F由此也不难理解它\x01",
            "为何会受到全家出游的游客\x01",
            "和情侣们的欢迎。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D13")

    #C0276
    ChrTalk(
        0x101,
        (
            "#00004F#6P哈哈，确实如此。\x02\x03",

            "#00000F另外，听说升到最高处之后，\x01",
            "看到的风景格外美丽呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D75")

    label("loc_7D13")


    #C0277
    ChrTalk(
        0x101,
        (
            "#00004F#6P哈哈，确实如此。\x02\x03",

            "#00002F我刚才已经坐过了，升到最高处之后，\x01",
            "看到的风景格外美丽呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D75")

    SetChrSubChip(0x1B, 0x0)

    #N0278
    NpcTalk(
        0x1B,
        "莉夏",
        (
            "#01809F呵呵，那还真令人期待。\x02\x03",

            "#01802F那么，在到达最高处之前，\x01",
            "我们先随便聊聊吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0279
    ChrTalk(
        0x101,
        (
            "#00002F#6P好啊，\x01",
            "反正还要过好一阵子\x01",
            "才能升到最高处。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    SetChrFlags(0x1B, 0x2)
    SetChrChipByIndex(0x1B, 0x22)
    SetChrSubChip(0x1B, 0x0)
    Call(0, 33)

    #N0280
    NpcTalk(
        0x1B,
        "莉夏",
        "#01804F……（昏昏欲睡）…………\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x101,
        (
            "#00012F#6P（唔……她好像很困呢。）\x02\x03",

            "#00006F（这也难怪，每天都练习得很辛苦，\x01",
            "  之前又在沙滩上玩得那么累。）\x02\x03",

            "#00002F（马上就要到最高处了，\x01",
            "  到底该叫醒她，还是让她继续睡呢……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x1B, 0x1F)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x2)
    OP_0D()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0282
    NpcTalk(
        0x1B,
        "莉夏",
        "#01805F啊……\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x101,
        "#00005F#6P哦，你醒了啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #N0284
    NpcTalk(
        0x1B,
        "莉夏",
        (
            "#01805F非、非常抱歉！\x01",
            "不知不觉地就睡着了……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        (
            "#00009F#6P哈哈，不用道歉啦。\x01",
            "先不说这些，你看……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(250)
    SetChrSubChip(0x1B, 0x2)
    Sleep(250)
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8188")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("莉夏")

    #A0286
    AnonymousTalk(
        0xFF,
        (
            "啊……已经到最高处了呢。\x02\x03",

            "晚霞的光辉将水面映照得一片朱红……\x01",
            "好美的景色。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0287
    ChrTalk(
        0x101,
        (
            "#00004F#6P是啊……\x01",
            "看来我们赶上了好时段。\x02\x03",

            "#00009F把最后一张票用在这里，\x01",
            "果然是正确决定啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0288
    NpcTalk(
        0x1B,
        "莉夏",
        (
            "#01809F呵呵，多谢你\x01",
            "特地邀请我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8204")

    label("loc_8188")


    #N0289
    NpcTalk(
        0x1B,
        "莉夏",
        (
            "#01805F啊……已经到最高处了呢。\x02\x03",

            "#01802F广阔的湖面环绕在周围……\x01",
            "好美的景色。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        "#00002F#6P是啊……风景很好呢。\x02",
    )

    CloseMessageWindow()

    label("loc_8204")

    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)

    #N0291
    NpcTalk(
        0x1B,
        "莉夏",
        (
            "#01808F（……在二人独处于密室时，\x01",
            "  我居然险些睡着……）\x02\x03",

            "#01803F（虽说现在的情况很安全，\x01",
            "  但假如对方是『银』的目标……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0292
    ChrTalk(
        0x101,
        (
            "#00005F#6P……那个，莉夏？\x02\x03",

            "#00002F如果你还是很困的话，\x01",
            "就继续睡吧，不必在意我。\x02\x03",

            "快到下面的时候，我会叫醒你的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    #N0293
    NpcTalk(
        0x1B,
        "莉夏",
        (
            "#01804F……不……\x01",
            "只是风景太美了，我看得有些出神。\x02\x03",

            "#01802F呵呵，请不用在意。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    #C0294
    ChrTalk(
        0x101,
        (
            "#00000F#6P……好像快到了呢。\x01",
            "莉夏，我们下去吧。\x05\x02",
        )
    )

    CloseMessageWindow()

    #N0295
    NpcTalk(
        0x1B,
        "莉夏",
        "#01802F好的。\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    #N0296
    NpcTalk(
        0x1B,
        "莉夏",
        (
            "#01802F那个，我玩得很开心。\x01",
            "非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x101,
        (
            "#00000F#6P嗯，我也很高兴能邀请到你。\x02\x03",

            "那么，待会见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0298
    NpcTalk(
        0x1B,
        "莉夏",
        "#01802F好的，待会见。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_49_7BD3 end

    def Function_50_8482(): pass

    label("Function_50_8482")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04201.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #N0299
    NpcTalk(
        0x1B,
        "修利",
        (
            "#04211F哇哇，越升越高了……\x02\x03",

            "#04206F我、我说，不会出事吧！？\x01",
            "这个箱子会不会受到\x01",
            "一点冲击就直接掉下去……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0300
    ChrTalk(
        0x101,
        (
            "#00004F#6P哈哈，不用担心，\x01",
            "肯定不会掉下去的。\x02\x03",

            "#00002F你在彩虹剧团练习的时候，\x01",
            "不是也经常在高处飞来飞去嘛，\x01",
            "用不着那么害怕……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    #N0301
    NpcTalk(
        0x1B,
        "修利",
        (
            "#04206F我、我才没有害怕……\x01",
            "而且……这高度完全不能相比吧！？\x02\x03",

            "#04201F真是的……\x01",
            "如果不好玩，\x01",
            "我一定要揍你一顿。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86FF")

    #C0302
    ChrTalk(
        0x101,
        (
            "#00006F#6P这可不是女孩子\x01",
            "该说的话啊……\x02\x03",

            "#00002F听说升到最高处之后，\x01",
            "看到的风景相当壮观。\x02\x03",

            "我想这完全值得\x01",
            "你忍受这种恐惧感。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_878F")

    label("loc_86FF")


    #C0303
    ChrTalk(
        0x101,
        (
            "#00006F#6P这可不是女孩子\x01",
            "该说的话啊……\x02\x03",

            "#00002F我刚才已经坐过了，升到最高处之后，\x01",
            "看到的风景相当壮观。\x02\x03",

            "我想这完全值得\x01",
            "你忍受这种恐惧感。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_878F")

    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #N0304
    NpcTalk(
        0x1B,
        "修利",
        "#04206F我都说过没有害怕了！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    Call(0, 33)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)

    #C0305
    ChrTalk(
        0x101,
        (
            "#00002F#6P哦……\x01",
            "好像快到最高处了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #N0306
    NpcTalk(
        0x1B,
        "修利",
        (
            "#04211F哇哇哇……\x01",
            "这、这、这也太高了……！\x02\x03",

            "#04207F让、让我下去！现在马上让我下去！！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0307
    ChrTalk(
        0x101,
        (
            "#00012F#6P喂喂，冷静一点啊。\x02\x03",

            "#00002F你总是看下面，所以才会害怕。\x01",
            "……不如看看对面吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0308
    NpcTalk(
        0x1B,
        "修利",
        "#04205F对、对面……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B3A")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("修利")

    #A0309
    AnonymousTalk(
        0xFF,
        (
            "啊……\x02\x03",

            "坐水上巴士的时候都没发现，\x01",
            "原来这里是被这么\x01",
            "一大片湖水包围着啊……\x02\x03",

            "而且整片湖水都被晚霞\x01",
            "映照得通红，真漂亮……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0310
    ChrTalk(
        0x101,
        (
            "#00004F#6P是啊……\x01",
            "看来我们赶上了好时段。\x02\x03",

            "#00009F把最后一张票用在这里，\x01",
            "果然是正确决定啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #N0311
    NpcTalk(
        0x1B,
        "修利",
        (
            "#04203F哼、哼……\x01",
            "我才不会向你道谢呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#00012F#6P哈哈……真是不坦率啊。\x02\x03",

            "#00000F现在的心情如何？\x01",
            "恐高的感觉已经一扫而空了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BF2")

    label("loc_8B3A")


    #N0313
    NpcTalk(
        0x1B,
        "修利",
        (
            "#04205F啊……\x02\x03",

            "坐水上巴士的时候都没发现，\x01",
            "原来这里是被这么\x01",
            "一大片湖水包围着啊……\x02\x03",

            "#04202F……风景真美啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x101,
        (
            "#00000F#6P哈哈，现在的心情如何？\x01",
            "恐高的感觉已经一扫而空了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BF2")

    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1B)
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0315
    NpcTalk(
        0x1B,
        "修利",
        (
            "#04211F呜、呜哇！好高好高！！\x02\x03",

            "#04206F真、真是的！！\x01",
            "别让我想起来啊！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0316
    ChrTalk(
        0x101,
        "#00006F#6P抱、抱歉。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    #C0317
    ChrTalk(
        0x101,
        (
            "#00000F#6P……好像快到了呢。\x01",
            "修利，我们下去吧。\x05\x02",
        )
    )

    CloseMessageWindow()

    #N0318
    NpcTalk(
        0x1B,
        "修利",
        "#04200F……嗯、嗯。\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    SetChrChipByIndex(0x1B, 0x8)
    SetChrSubChip(0x1B, 0x0)
    Call(0, 35)

    #N0319
    NpcTalk(
        0x1B,
        "修利",
        (
            "#14012F总、总之……\x01",
            "玩得还算比较开心吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        (
            "#00000F#6P嗯，我也很高兴能邀请到你。\x02\x03",

            "那么，待会见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0321
    NpcTalk(
        0x1B,
        "修利",
        "#14000F哼，我走啦。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_50_8482 end

    def Function_51_8DAC(): pass

    label("Function_51_8DAC")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(12330, 4300, -17760, 0)
    MoveCamera(336, 16, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(3220, 0)
    SetChrPos(0x101, 7370, 0, -12510, 45)
    SetChrPos(0xEF, 8660, 0, -13430, 20)
    OP_4B(0x1A, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0322
    ChrTalk(
        0x101,
        "#00005F找到了……！\x02",
    )

    CloseMessageWindow()
    OP_9C(0x1A, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    TurnDirection(0x1A, 0x101, 500)
    OP_63(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0323
    ChrTalk(
        0x1A,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "呀，被发现了☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(8240, 4300, -19760, 0)
    MoveCamera(356, 30, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(3220, 0)
    SetChrPos(0x1A, 8450, 0, -12880, 200)
    SetChrPos(0x101, 7200, 0, -14240, 20)
    SetChrPos(0xEF, 8750, 0, -14780, 300)
    FadeToBright(1000, 0)
    OP_0D()

    #C0324
    ChrTalk(
        0x1A,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "咪嘻嘻，小哥哥，\x01",
            "你真是很擅长捉迷藏呀☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x1A,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "在我拿出真本事之后，竟然还能找到我，\x01",
            "这可不是一般人做得到的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x101,
        (
            "#00006F我、我感觉并没有\x01",
            "你说的那么夸张……\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x1A,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "总之，只要再找到我两次，\x01",
            "就算是小哥哥你赢了哦～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x1A,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "咪嘻嘻，加油吧～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8FFE():

        label("loc_8FFE")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_8FFE")

    QueueWorkItem2(0x101, 1, lambda_8FFE)

    def lambda_9010():

        label("loc_9010")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_9010")

    QueueWorkItem2(0xEF, 1, lambda_9010)
    SetChrFlags(0x1A, 0x1000)
    OP_95(0x1A, 10920, 0, -15100, 5000, 0x0)
    OP_95(0x1A, 6460, 0, -18160, 5000, 0x0)

    def lambda_904F():
        OP_95(0xFE, 710, 0, -17500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_904F)
    Sleep(800)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    OP_68(-3070, 5000, -23400, 0)
    MoveCamera(39, 36, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(3220, 0)
    SetChrPos(0x101, -540, 0, -18390, 180)
    SetChrPos(0xEF, 530, 0, -18400, 180)
    SetChrFlags(0x1A, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    #C0329
    ChrTalk(
        0x101,
        (
            "#00012F唔……它好像\x01",
            "很喜欢我……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_9159")

    #C0330
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，那不是很好嘛。\x02\x03",

            "好啦，我们赶快去找\x01",
            "它的下一个藏身之处吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94ED")

    label("loc_9159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_91AD")

    #C0331
    ChrTalk(
        0x103,
        (
            "#00200F让我很羡慕呢。\x02\x03",

            "好了，我们赶快去找\x01",
            "它的下一个藏身之处吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94ED")

    label("loc_91AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_921A")

    #C0332
    ChrTalk(
        0x104,
        (
            "#00300F哈哈，阿缇要是看到了，\x01",
            "肯定会很羡慕吧。\x02\x03",

            "好啦，我们赶快去找\x01",
            "它的下一个藏身之处吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94ED")

    label("loc_921A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_9274")

    #C0333
    ChrTalk(
        0x109,
        (
            "#10100F呵呵，那不是很好嘛。\x02\x03",

            "好啦，我们赶快去找\x01",
            "它的下一个藏身之处吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94ED")

    label("loc_9274")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_92D8")

    #C0334
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，受欢迎的男人真不容易啊。\x02\x03",

            "好啦，我们赶快去找\x01",
            "它的下一个藏身之处吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94ED")

    label("loc_92D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_9336")

    #C0335
    ChrTalk(
        0x153,
        (
            "#01100F嘿嘿嘿，真好啊，罗伊德。\x02\x03",

            "好啦，我们赶快去找\x01",
            "它的下一个藏身地点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94ED")

    label("loc_9336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_9390")

    #C0336
    ChrTalk(
        0x156,
        (
            "#06400F呵呵，那不是很好嘛。\x02\x03",

            "好啦，我们赶快去找\x01",
            "它的下一个藏身之处吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94ED")

    label("loc_9390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_93EF")

    #C0337
    ChrTalk(
        0x14C,
        (
            "#05900F呵呵，罗伊德\x01",
            "真受欢迎呢。\x02\x03",

            "好啦，我们赶快去找\x01",
            "它的下一个藏身之处吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94ED")

    label("loc_93EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_9449")

    #C0338
    ChrTalk(
        0x134,
        (
            "#01700F呵呵，那不是很好嘛。\x02\x03",

            "好啦，我们赶快去找\x01",
            "它的下一个藏身之处吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94ED")

    label("loc_9449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_94A3")

    #C0339
    ChrTalk(
        0x135,
        (
            "#01802F呵呵，那不是很好嘛。\x02\x03",

            "好啦，我们赶快去找\x01",
            "它的下一个藏身之处吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94ED")

    label("loc_94A3")


    #C0340
    ChrTalk(
        0x166,
        (
            "#14000F哼，这不是挺好嘛。\x02\x03",

            "好啦，我们赶快去找\x01",
            "它的下一个躲藏地点吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_9516")

    #C0341
    ChrTalk(
        0x101,
        "#00000F嗯，我们走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9533")

    label("loc_9516")


    #C0342
    ChrTalk(
        0x101,
        "#00000F好的，我们走吧。\x02",
    )

    CloseMessageWindow()

    label("loc_9533")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C9, 5)
    OP_65(0x0, 0x1)
    OP_29(0x7F, 0x1, 0xD)
    SetChrPos(0x0, -200, 10, -18640, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_51_8DAC end

    def Function_52_9563(): pass

    label("Function_52_9563")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10200.itc", 0x1E)
    LoadChrToIndex("chr/ch45400.itc", 0x1F)
    LoadChrToIndex("chr/ch24400.itc", 0x20)
    LoadChrToIndex("chr/ch24500.itc", 0x21)
    LoadChrToIndex("apl/ch50387.itc", 0x22)
    LoadEffect(0x0, "event\\eva02_00.eff")
    LoadEffect(0x1, "battle/ms00109.eff")
    SoundLoad(810)
    SoundLoad(862)
    SoundLoad(645)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x1C, 0x20)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x21)
    SetChrFlags(0x1D, 0x8000)
    OP_68(-510, 3010, -21510, 0)
    MoveCamera(48, 32, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(6590, 0)
    SetChrPos(0x101, 840, 1910, -27360, 0)
    SetChrPos(0x103, -60, 2190, -28450, 0)
    SetChrPos(0x102, 2750, 0, -18900, 180)
    SetChrPos(0x104, 2750, 90, -20300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    OP_68(-1330, 3010, -21710, 3000)
    SetCameraDistance(8010, 3000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_96A0():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_96A0)
    Sleep(50)

    def lambda_96BD():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_96BD)
    Sleep(500)
    OP_63(0x102, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    WaitChrThread(0x103, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9734():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9734)
    Sleep(50)

    def lambda_9744():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9744)
    Sleep(300)

    #C0343
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200F啊，是艾莉和兰迪。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(6870, 3000)

    def lambda_9780():

        label("loc_9780")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_9780")

    QueueWorkItem2(0x102, 1, lambda_9780)

    def lambda_9792():

        label("loc_9792")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_9792")

    QueueWorkItem2(0x104, 1, lambda_9792)

    def lambda_97A4():
        OP_95(0xFE, 860, 0, -18960, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_97A4)
    Sleep(50)

    def lambda_97C1():
        OP_95(0xFE, -120, 50, -20150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_97C1)
    WaitChrThread(0x101, 1)

    def lambda_97DF():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_97DF)
    WaitChrThread(0x103, 1)

    def lambda_97F0():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_97F0)
    OP_6F(0x10)
    Sleep(300)

    #C0344
    ChrTalk(
        0x104,
        "#00309F哟，辛苦啦。\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x102,
        (
            "#00100F呵呵呵，你们两人\x01",
            "好像都很努力啊。\x02\x03",

            "情况怎么样？\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212F哎，相当不容易呢……\x01",
            "道具服里面真是很热。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0347
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526F罗伊德前辈……\x01",
            "巡游可不是散步。\x02\x03",

            "#05521F必须要态度亲切，充满热情，\x01",
            "给游客带来『找到咪西啦！真幸运☆』\x01",
            "这样的感觉。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F好、好的……我明白了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x102,
        (
            "#00109F缇欧……\x01",
            "一旦谈起与咪西相关的事情，\x01",
            "就会相当强势呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x104,
        "#00304F哈哈，罗伊德也拿她没办法呢。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 2880, 1730, -1360, 170)

    #N0351
    NpcTalk(
        0x1D,
        "女性的声音",
        "啊，是咪西～！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9A38():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9A38)
    Sleep(50)

    def lambda_9A48():
        OP_95(0xFE, -7940, 0, -14050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9A48)
    Sleep(50)

    def lambda_9A65():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9A65)
    Sleep(50)

    def lambda_9A75():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9A75)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1C, 2710, 800, -7600, 180)
    SetChrPos(0x1D, 1300, 1050, -7030, 180)
    OP_68(-1280, 3010, -20050, 3000)

    def lambda_9ABF():
        OP_95(0xFE, 1930, 0, -16000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_9ABF)
    Sleep(50)

    def lambda_9ADC():
        OP_95(0xFE, 830, 0, -15580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_9ADC)
    OP_6F(0x1)
    WaitChrThread(0x1C, 1)
    OP_93(0x1C, 0xE1, 0x1F4)
    Sleep(300)

    #C0352
    ChrTalk(
        0x1C,
        (
            "哈哈，真的是啊。\x01",
            "刚坐完摩天轮，就遇到了咪西，\x01",
            "真幸运啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x1D,
        (
            "呀～好可爱☆\x01",
            "请它和我们合张影吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x1C,
        "嗯，好主意。\x02",
    )

    CloseMessageWindow()
    OP_95(0x1C, 2800, 0, -17840, 2000, 0x0)
    TurnDirection(0x1C, 0x102, 500)

    def lambda_9B98():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B98)
    Sleep(50)

    def lambda_9BA8():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9BA8)
    Sleep(300)

    #C0355
    ChrTalk(
        0x1C,
        (
            "那个……打扰一下，\x01",
            "可以用这台相机\x01",
            "帮我们拍张合影吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x102,
        "#00100F好的，没问题。\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x10E, 0x1F4)
    OP_68(-1870, 3010, -20590, 3000)
    OP_95(0x102, 0, 690, -22620, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Sleep(300)
    OP_6F(0x1)
    Fade(250)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    OP_0D()

    #C0357
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203F（拍、拍照吗……\x01",
            "  在这种时候，\x01",
            "  应该怎么办呢？）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "站在男性旁边\x01",      # 0
            "站在女性旁边\x01",      # 1
            "站在两人之间\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-2290, 3010, -22170, 0)
    MoveCamera(35, 29, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(5360, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9D3D"),
        (1, "loc_9E10"),
        (2, "loc_9EFD"),
        (SWITCH_DEFAULT, "loc_9FC4"),
    )


    label("loc_9D3D")

    SetChrPos(0x101, 0, 0, -18900, 180)
    SetChrPos(0x1C, 1000, 0, -18900, 180)
    SetChrPos(0x1D, -1000, 0, -18900, 180)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 53)
    WaitChrThread(0x101, 3)
    Sleep(500)
    OP_63(0x1D, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0358
    ChrTalk(
        0x1D,
        "呀，不公平～！\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x1C,
        (
            "哈哈哈，\x01",
            "羡慕吧羡慕吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x102,
        (
            "#00109F准备好了吗？那我就拍啦。\x02\x03",

            "#00102F好，茄子！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FC4")

    label("loc_9E10")

    SetChrPos(0x101, 0, 0, -18900, 180)
    SetChrPos(0x1C, 1000, 0, -18900, 180)
    SetChrPos(0x1D, -1000, 0, -18900, 180)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 54)
    WaitChrThread(0x101, 3)
    Sleep(500)

    #C0361
    ChrTalk(
        0x1D,
        (
            "呀，太好了！\x01",
            "咪西是我一个人的了～¤\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x1C,
        (
            "哈、哈哈哈……\x01",
            "（郁闷……）\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x102,
        (
            "#00111F（恼火……）\x02\x03",

            "#00109F……那、那个，\x01",
            "我这就要拍了哦。\x02\x03",

            "#00102F好，茄子！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FC4")

    label("loc_9EFD")

    OP_2C(0x86, 0x1)
    SetScenarioFlags(0x176, 7)
    SetChrPos(0x101, 0, 0, -18900, 180)
    SetChrPos(0x1C, 1000, 0, -18900, 180)
    SetChrPos(0x1D, -1000, 0, -18900, 180)
    FadeToBright(1000, 0)
    OP_0D()

    #C0364
    ChrTalk(
        0x1D,
        (
            "呵呵呵，\x01",
            "今天是我们和咪西邂逅的纪念日☆\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x1C,
        "请多关照哦，咪西～\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x102,
        (
            "#00109F准备好了吗？那我就拍啦。\x02\x03",

            "#00102F好，茄子！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FC4")

    label("loc_9FC4")

    Sound(810, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    #C0367
    ChrTalk(
        0x1D,
        "非常感谢～\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x1C,
        "谢啦。\x02",
    )

    CloseMessageWindow()

    def lambda_A025():
        OP_95(0xFE, 0, 440, -21620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_A025)
    Sleep(50)

    def lambda_A042():
        OP_95(0xFE, -1000, 440, -20620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A042)
    WaitChrThread(0x1D, 1)

    def lambda_A060():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A060)
    WaitChrThread(0x1C, 1)

    def lambda_A071():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_A071)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Sleep(500)

    #C0369
    ChrTalk(
        0x102,
        "#00100F好了，给。\x02",
    )

    CloseMessageWindow()
    OP_97(0x1C, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)

    def lambda_A0BC():
        OP_95(0xFE, -940, 2840, -31020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_A0BC)
    Sleep(50)

    def lambda_A0D9():
        OP_95(0xFE, -940, 2840, -31020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A0D9)
    Sleep(50)

    def lambda_A0F6():
        OP_95(0xFE, 0, 0, -18900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A0F6)

    def lambda_A110():
        OP_95(0xFE, -400, 0, -17600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A110)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xB4, 0x1F4)
    WaitChrThread(0x103, 1)
    TurnDirection(0x103, 0x101, 500)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A273")

    #C0370
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05204F呼……\x01",
            "刚才做得还可以吧？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    #Sound(2680, 255, 100, 0)    #voice#Tio

    #C0371
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524F非常完美，罗伊德前辈。\x02\x03",

            "#05520F咪西可以说是\x01",
            "主题公园的象征……\x01",
            "就像一个会走路的旅游胜地。\x02\x03",

            "#05524F在那种情况下，\x01",
            "站在正中间\x01",
            "是最好的选择。\x02\x03",

            "#05522F咪西已经开始\x01",
            "有模有样了呢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0372
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05209F哈哈，谢谢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x5)
    Jump("loc_A4A6")

    label("loc_A273")


    #C0373
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05204F呼……\x01",
            "刚才做得还算……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x103, 0x101, 0xFA, 0x1388, 0x0)
    PlayEffect(0x1, 0x0, 0xFF, 0x0, 0, 300, -18900, 180, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(645, 0, 30, 0)
    Sound(862, 0, 50, 0)
    Sound(811, 0, 100, 0)
    OP_9B(0x1, 0x103, 0xB4, 0x3E8, 0x1388, 0x0)
    Sleep(500)
    #Sound(3318, 255, 100, 0)    #voice#Lloyd

    #C0374
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211F呜哇！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCF6)
    TurnDirection(0x101, 0x103, 500)
    #Sound(2682, 255, 100, 0)    #voice#Tio

    #C0375
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526F……我对罗伊德前辈太失望了。\x02\x03",

            "#05531F……为什么要特意\x01",
            "改变站立位置？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05205F这、这个……\x01",
            "我只是觉得插在情侣\x01",
            "中间不太好……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526F唉……\x01",
            "请你仔细想一想。\x02\x03",

            "#05520F咪西可以说是\x01",
            "主题公园的象征……\x01",
            "就像一个会走路的旅游胜地。\x02\x03",

            "#05531F在那种情况下，\x01",
            "站在正中间\x01",
            "才是最好的选择。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F是、是吗……\x01",
            "（真不应该\x01",
            "  多此一举啊……）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x6)

    label("loc_A4A6")


    #C0379
    ChrTalk(
        0x102,
        (
            "#00104F呵呵，照这种情况来看，\x01",
            "只要有缇欧在，\x01",
            "就一定没问题了。\x02\x03",

            "#00100F你们两个都要加油哦，\x01",
            "我们会在旁边看着的。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x104,
        (
            "#00309F哇哈哈，\x01",
            "同时也算是在约会！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 1000)
    Sleep(300)

    #C0381
    ChrTalk(
        0x102,
        "#00103F没有的事。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)
    Sleep(300)

    #C0382
    ChrTalk(
        0x104,
        "#00306F呜，回应得好果断……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0383
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200F哈哈……我们会尽量\x01",
            "做好这项工作的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F出发吧，去下一个地点。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_52_9563 end

    def Function_53_A60B(): pass

    label("Function_53_A60B")

    OP_97(0x101, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    OP_97(0x101, 0x6A4, 0x0, 0x0, 0x7D0, 0x0)
    OP_97(0x101, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)

    def lambda_A64C():
        OP_97(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_A64C)
    Sleep(50)

    def lambda_A669():
        OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A669)
    WaitChrThread(0x1C, 1)

    def lambda_A687():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_A687)
    WaitChrThread(0x101, 1)

    def lambda_A698():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A698)
    Return()

    # Function_53_A60B end

    def Function_54_A6A1(): pass

    label("Function_54_A6A1")

    OP_97(0x101, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    OP_97(0x101, 0xFFFFF95C, 0x0, 0x0, 0x7D0, 0x0)
    OP_97(0x101, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)

    def lambda_A6E2():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A6E2)
    Sleep(50)

    def lambda_A6FF():
        OP_97(0xFE, 0x1F4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A6FF)
    WaitChrThread(0x1D, 1)

    def lambda_A71D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A71D)
    WaitChrThread(0x101, 1)

    def lambda_A72E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A72E)
    Return()

    # Function_54_A6A1 end

    def Function_55_A737(): pass

    label("Function_55_A737")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0385
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "张贴着主题公园的\x01",
            "导览地图。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_55_A737 end

    def Function_56_A769(): pass

    label("Function_56_A769")

    EventBegin(0x1)
    TurnDirection(0x14, 0x0, 500)
    OP_4B(0x14, 0xFF)

    #C0386
    ChrTalk(
        0x14,
        (
            "客人，如果您想\x01",
            "乘坐摩天轮，\x01",
            "请把票交给我。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -330, 0, -15900, 350)
    OP_93(0x14, 0xA0, 0x0)
    OP_4C(0x14, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_56_A769 end

    SaveToFile()

Try(main)
