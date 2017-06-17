from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0800.bin",                # FileName
        "c0800",                    # MapName
        "c0800",                    # Location
        0x0003,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 3, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0800",                  # 0
        "罗梅奥队员",             # 1
        "乘客",                   # 2
        "乘客",                   # 3
        "乘客",                   # 4
        "库瓦特罗安检官",         # 5
        "老人",                   # 6
        "老妇人",                 # 7
        "乘客",                   # 8
        "乘客",                   # 9
        "乘客",                   # 10
        "乘客",                   # 11
        "乘客",                   # 12
        "乘客",                   # 13
        "乘客",                   # 14
        "站员",                   # 15
        "站员",                   # 16
        "乘客",                   # 17
        "列车",                   # 18
        "坎贝尔议员",             # 19
        "卡拉",                   # 20
        "玛夏",                   # 21
        "SE控制",                 # 22
    ))

    AddCharChip((
        "chr/ch31200.itc",                   # 00
        "chr/ch20302.itc",                   # 01
        "chr/ch24400.itc",                   # 02
        "chr/ch20802.itc",                   # 03
        "chr/ch28500.itc",                   # 04
    ))

    DeclNpc(-1500,   0,       -18530,  0,    385,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(43000,   100,     -17200,  180,  453,  0x0, 0,   1,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(49700,   0,       -14050,  0,    385,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(15000,   100,     -17200,  180,  453,  0x0, 0,   3,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(7500,    0,       -12500,  270,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 33,  58.0,                  -16.0,                 0.0,                   17.015625,             [0.3333333134651184,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3636363446712494,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -19.333332061767578,   5.81818151473999,      -0.0,                  1.0])

    DeclActor(24500,   0,       0,       2000,    24500,   1500,    0,       0x007C, 0,  34, 0x0000)
    DeclActor(24500,   0,       -16000,  2000,    24500,   1500,    -16000,  0x007C, 0,  34, 0x0000)
    DeclActor(18000,   0,       0,       2000,    17500,   1500,    0,       0x007C, 0,  35, 0x0000)
    DeclActor(18000,   0,       -16000,  2000,    17500,   1500,    -16000,  0x007C, 0,  35, 0x0000)

    ScpFunction((
        "Function_0_498",          # 00, 0
        "Function_1_550",          # 01, 1
        "Function_2_623",          # 02, 2
        "Function_3_6E3",          # 03, 3
        "Function_4_8FF",          # 04, 4
        "Function_5_B38",          # 05, 5
        "Function_6_BD0",          # 06, 6
        "Function_7_D8B",          # 07, 7
        "Function_8_DC8",          # 08, 8
        "Function_9_EE9",          # 09, 9
        "Function_10_14F8",        # 0A, 10
        "Function_11_168E",        # 0B, 11
        "Function_12_1783",        # 0C, 12
        "Function_13_1A2F",        # 0D, 13
        "Function_14_1A58",        # 0E, 14
        "Function_15_1ACD",        # 0F, 15
        "Function_16_2490",        # 10, 16
        "Function_17_24E5",        # 11, 17
        "Function_18_2A22",        # 12, 18
        "Function_19_2A66",        # 13, 19
        "Function_20_2B3A",        # 14, 20
        "Function_21_2B99",        # 15, 21
        "Function_22_2BF8",        # 16, 22
        "Function_23_2C57",        # 17, 23
        "Function_24_2CB6",        # 18, 24
        "Function_25_3112",        # 19, 25
        "Function_26_3154",        # 1A, 26
        "Function_27_31B1",        # 1B, 27
        "Function_28_31C8",        # 1C, 28
        "Function_29_3651",        # 1D, 29
        "Function_30_4316",        # 1E, 30
        "Function_31_433F",        # 1F, 31
        "Function_32_4360",        # 20, 32
        "Function_33_4CBE",        # 21, 33
        "Function_34_4DD4",        # 22, 34
        "Function_35_4E15",        # 23, 35
        "Function_36_4E4E",        # 24, 36
        "Function_37_4E99",        # 25, 37
    ))


    def Function_0_498(): pass

    label("Function_0_498")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4D8"),
        (1, "loc_4E4"),
        (2, "loc_4F0"),
        (3, "loc_4FC"),
        (4, "loc_508"),
        (5, "loc_514"),
        (6, "loc_520"),
        (SWITCH_DEFAULT, "loc_52C"),
    )


    label("loc_4D8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_4E4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_4F0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_4FC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_508")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_514")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_520")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_52C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_538")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_54F")

    Return()

    # Function_0_498 end

    def Function_1_550(): pass

    label("Function_1_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_564")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 17)
    Jump("loc_5C6")

    label("loc_564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_578")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 8)
    Jump("loc_5C6")

    label("loc_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_58C")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 15)
    Jump("loc_5C6")

    label("loc_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_5A6")
    ClearScenarioFlags(0x5C, 3)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 3)
    Event(0, 28)
    Jump("loc_5C6")

    label("loc_5A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x9)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C6")
    Event(0, 24)

    label("loc_5C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5EB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E1")
    Jump("loc_5E6")

    label("loc_5E1")

    ClearChrFlags(0x8, 0x80)

    label("loc_5E6")

    Jump("loc_622")

    label("loc_5EB")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_610")
    Jump("loc_622")

    label("loc_610")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_622")
    ClearChrFlags(0xC, 0x80)

    label("loc_622")

    Return()

    # Function_1_550 end

    def Function_2_623(): pass

    label("Function_2_623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_635")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_635")

    SetMapObjFlags(0x1, 0x1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_680")
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)

    label("loc_680")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CB")
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6DC")
    OP_24(0x323)
    Jump("loc_6E2")

    label("loc_6DC")

    Sound(803, 1, 100, 0)

    label("loc_6E2")

    Return()

    # Function_2_623 end

    def Function_3_6E3(): pass

    label("Function_3_6E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_771")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_701")
    Jump("loc_76C")

    label("loc_701")


    #C0001
    ChrTalk(
        0xFE,
        (
            "哎呀，你们刚从\x01",
            "共和国回来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "我也想去\x01",
            "那里旅行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#0003F（……我们可不是\x01",
            "  去旅行的……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76C")

    Jump("loc_8FB")

    label("loc_771")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_840")

    #C0004
    ChrTalk(
        0xFE,
        (
            "向警备队运送物资的货运列车\x01",
            "都是从这个车站发车的。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "我刚刚才目送一辆前往\x01",
            "贝尔加德门的列车驶出了车站。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "警备队员并不是只要\x01",
            "做好警备工作就行了，\x01",
            "我们实在是很辛苦呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8A4")

    label("loc_840")


    #C0007
    ChrTalk(
        0xFE,
        (
            "刚才把货物都装上了\x01",
            "开往贝尔加德门的货运列车。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "３号月台是货运线专用的，\x01",
            "可不能随便进入哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A4")

    Jump("loc_8FB")

    label("loc_8A9")


    #C0009
    ChrTalk(
        0xFE,
        (
            "哦……开往帝国的列车的安检\x01",
            "也告一段落了。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "我也差不多该\x01",
            "回贝尔加德门了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FB")

    TalkEnd(0xFE)
    Return()

    # Function_3_6E3 end

    def Function_4_8FF(): pass

    label("Function_4_8FF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_993")
    Jump("loc_9DD")

    label("loc_993")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9B3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9DD")

    label("loc_9B3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9DD")

    label("loc_9D3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9DD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB5")

    #C0011
    ChrTalk(
        0xFE,
        (
            "他们不会对进入克洛斯贝尔的\x01",
            "乘客进行安检哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "只会检查去帝国\x01",
            "和共和国的乘客。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "就因为这样，\x01",
            "所以才会有那么多人\x01",
            "利用列车非法入境或走私。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B02")

    label("loc_AB5")


    #C0014
    ChrTalk(
        0xFE,
        (
            "所以才会有那么多人\x01",
            "利用列车非法入境或走私。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        "算了，反正跟我没关系。\x02",
    )

    CloseMessageWindow()

    label("loc_B02")

    Jump("loc_B30")

    label("loc_B07")


    #C0016
    ChrTalk(
        0xFE,
        (
            "那么……休息结束，\x01",
            "差不多也该走了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B30")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_4_8FF end

    def Function_5_B38(): pass

    label("Function_5_B38")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B90")

    #C0017
    ChrTalk(
        0xFE,
        (
            "有一个朋友要去帝国，\x01",
            "我是来给他送行的。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        "……还不发车吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_BCC")

    label("loc_B90")


    #C0019
    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "还不发车吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "我想快点把他送走，\x01",
            "我好回去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCC")

    TalkEnd(0xFE)
    Return()

    # Function_5_B38 end

    def Function_6_BD0(): pass

    label("Function_6_BD0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C64")
    Jump("loc_CAE")

    label("loc_C64")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C84")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CAE")

    label("loc_C84")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CA4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CAE")

    label("loc_CA4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CAE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D25")

    #C0021
    ChrTalk(
        0xFE,
        "有个朋友会坐下一班列车过来。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        "十年没见了……真怀念啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D83")

    label("loc_D25")


    #C0023
    ChrTalk(
        0xFE,
        (
            "安检官也出来了，\x01",
            "差不多要发车了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "等这班列车出站后，\x01",
            "朋友乘坐的列车应该就会来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D83")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_BD0 end

    def Function_7_D8B(): pass

    label("Function_7_D8B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D9F")
    Jump("loc_DC4")

    label("loc_D9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_DB4")
    Call(0, 10)
    Jump("loc_DC4")

    label("loc_DB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_DC4")
    Call(0, 9)

    label("loc_DC4")

    TalkEnd(0xFE)
    Return()

    # Function_7_D8B end

    def Function_8_DC8(): pass

    label("Function_8_DC8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(452)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    OP_49()
    SetChrPos(0x19, 7000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_68(61500, 2500, -10500, 0)
    MoveCamera(60, 15, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(16000, 0)
    OP_EE(0x0, 0x1)
    OP_68(58500, 2500, -11500, 5000)
    MoveCamera(45, 20, 0, 5000)
    SetCameraDistance(24000, 5000)
    ClearMapObjFlags(0x1, 0x4)
    BeginChrThread(0x19, 3, 0, 18)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(5500, 3300, -8000, 0)
    MoveCamera(48, -15, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(14000, 0)
    OP_68(5500, 2300, -8000, 4000)
    OP_0D()
    WaitChrThread(0x19, 3)
    OP_6F(0x1)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_DC8 end

    def Function_9_EE9(): pass

    label("Function_9_EE9")

    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_68(5270, 1500, -12980, 0)
    MoveCamera(29, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17840, 0)
    SetChrPos(0x101, 5500, 0, -13000, 90)
    SetChrPos(0x102, 5250, 0, -12000, 90)
    SetChrPos(0x103, 4000, 0, -13000, 90)
    SetChrPos(0x104, 3700, 0, -12000, 90)
    OP_93(0xC, 0x10E, 0x0)
    SetChrSubChip(0xC, 0x0)
    OP_0D()

    #C0025
    ChrTalk(
        0xFE,
        (
            "#11P……那么，\x01",
            "我来说明一下工作的内容。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#6P#0000F嗯，麻烦您了。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "#11P接下来，\x01",
            "你们每个人负责一节车厢，\x01",
            "对车厢内的人进行安检。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "#11P具体来说，你们要和每个乘客对话，\x01",
            "然后检查他们的入境申请书和随身携带的行李。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "#11P如果没有入境申请书，\x01",
            "或者携带有危险物品，\x01",
            "就当场对其拘捕。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#6P#0003F原来如此……明白了。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#0303F嗯，虽然安检工作还算没问题……\x02\x03",

            "#0301F但如果乘客不在座位上的话，\x01",
            "要怎么办啊？\x02\x03",

            "#0306F不管怎么说，\x01",
            "我们都还是新手，总觉得\x01",
            "单靠我们几个，没法检查全面……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "#11P嗯，这问题我们已经考虑到了。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "#11P我们规定，安检一旦开始，\x01",
            "到结束之前，乘客都不可以\x01",
            "在车上走动。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "#11P因为有时候会有些人\x01",
            "耍小聪明，意图制造混乱\x01",
            "来混过安检。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        "#6P#0200F安检工作果然很严谨啊。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#6P#0001F原来如此……\x01",
            "我们知道该怎么做了。\x02\x03",

            "#0003F嗯，不过……\x01",
            "每人负责一节车厢吗……\x02\x03",

            "#0000F我和兰迪单独一个人也没问题，\x01",
            "但艾莉和缇欧……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12FA():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12FA)

    def lambda_1307():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1307)

    def lambda_1314():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1314)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0037
    ChrTalk(
        0x102,
        (
            "#5P#0105F事到如今，\x01",
            "还有必要担心那种事吗？\x02\x03",

            "#0104F身为一名警察，\x01",
            "我也是会一些擒拿术的。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        (
            "#6P#0203F我也一样。\x02\x03",

            "#0200F就算有可疑的人想对我不利，\x01",
            "我也不觉得他能打得赢我。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        (
            "#5P#0309F哈哈，我们这边的女生\x01",
            "可都不是好欺负的啊。\x02\x03",

            "你也差不多该记住这点了吧，罗伊德。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0040
    ChrTalk(
        0x101,
        "#12P#0003F确、确实如此啊。\x02",
    )

    CloseMessageWindow()

    def lambda_1461():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1461)

    def lambda_146E():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_146E)

    def lambda_147B():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_147B)

    def lambda_1488():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1488)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0041
    ChrTalk(
        0xC,
        (
            "那么……\x01",
            "可以请你们\x01",
            "开始了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x9, 0x1, 0x2)
    Call(0, 11)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E4")
    Call(0, 12)
    Jump("loc_14F7")

    label("loc_14E4")

    SetChrPos(0x0, 5000, 0, -13500, 90)
    EventEnd(0x5)

    label("loc_14F7")

    Return()

    # Function_9_EE9 end

    def Function_10_14F8(): pass

    label("Function_10_14F8")

    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_68(5270, 1500, -12980, 0)
    MoveCamera(29, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17840, 0)
    SetChrPos(0x101, 5500, 0, -13000, 90)
    SetChrPos(0x102, 5250, 0, -12000, 90)
    SetChrPos(0x103, 4000, 0, -13000, 90)
    SetChrPos(0x104, 3700, 0, -12000, 90)
    OP_93(0xC, 0x10E, 0x0)
    SetChrSubChip(0xC, 0x0)
    OP_0D()

    #C0042
    ChrTalk(
        0xC,
        (
            "#11P接下来，\x01",
            "你们每个人负责一节车厢，\x01",
            "对车厢内的人进行安检。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xC,
        (
            "#11P你们要做的是，\x01",
            "检查乘客的随身行李，\x01",
            "和『入境申请书』。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xC,
        (
            "#11P那么……\x01",
            "可以请你们\x01",
            "开始了吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 11)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_167A")
    Call(0, 12)
    Jump("loc_168D")

    label("loc_167A")

    SetChrPos(0x0, 5000, 0, -13500, 90)
    EventEnd(0x5)

    label("loc_168D")

    Return()

    # Function_10_14F8 end

    def Function_11_168E(): pass

    label("Function_11_168E")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1782")

    #C0045
    ChrTalk(
        0x101,
        "#6P#0006F那个，我们还没做好心理准备……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xC,
        (
            "#11P……真没办法啊。\x01",
            "确实，我也不希望你们因为太紧张而失败。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xC,
        (
            "#11P不过，发车\x01",
            "可不能拖延太久。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xC,
        "#11P希望你们能尽快准备好啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1782")

    Return()

    # Function_11_168E end

    def Function_12_1783(): pass

    label("Function_12_1783")


    #C0049
    ChrTalk(
        0x101,
        "#6P#0000F好的，知道了。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xC,
        (
            "#11P……哦！\x01",
            "看来已经没问题了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xC,
        (
            "#11P那么，就请你们\x01",
            "马上开始吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xC,
        (
            "#11P我检查第一节车厢。\x01",
            "后面的你们自己分吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1822():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1822)
    Sleep(300)

    def lambda_1832():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1832)

    def lambda_183F():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_183F)

    def lambda_184C():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_184C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0053
    ChrTalk(
        0x101,
        (
            "#12P#0000F那么……我负责第二节车厢。\x02\x03",

            "后面几节车厢就按照\x01",
            "艾莉、缇欧、兰迪的\x01",
            "顺序来分配吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        "#5P#0300F收到！\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        "#6P#0200F了解。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        "#5P#0100F那待会见了。\x02",
    )

    CloseMessageWindow()

    def lambda_190E():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_190E)

    def lambda_191B():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_191B)

    def lambda_1928():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1928)

    def lambda_1935():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1935)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0057
    ChrTalk(
        0xC,
        (
            "#11P嗯，你们检查时\x01",
            "请务必认真仔细。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 1, 0, 13)
    Sleep(500)
    BeginChrThread(0x101, 1, 0, 14)
    WaitChrThread(0xC, 1)
    WaitChrThread(0x101, 1)

    #C0058
    ChrTalk(
        0x101,
        (
            "#6P#0001F好……\x01",
            "任务开始！\x02",
        )
    )

    CloseMessageWindow()
    Sound(454, 0, 100, 0)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    OP_79(0x1)

    def lambda_19C7():
        OP_97(0x101, 0x12C, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19C7)
    BeginChrThread(0x1D, 0, 0, 36)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 1)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    StopBGM(0x7D0)
    WaitBGM()
    EndChrThread(0x1D, 0x0)
    SetScenarioFlags(0x5C, 1)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1783 end

    def Function_13_1A2F(): pass

    label("Function_13_1A2F")

    OP_97(0xC, 0xFFFFFA24, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    OP_97(0xC, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_13_1A2F end

    def Function_14_1A58(): pass

    label("Function_14_1A58")


    def lambda_1A5D():
        OP_97(0x102, 0x3A98, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A5D)
    Sleep(300)
    OP_97(0x103, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)

    def lambda_1A8E():
        OP_97(0x103, 0x3A98, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A8E)
    Sleep(400)

    def lambda_1AAB():
        OP_97(0x104, 0x3A98, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1AAB)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Return()

    # Function_14_1A58 end

    def Function_15_1ACD(): pass

    label("Function_15_1ACD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_68(5270, 1500, -12980, 0)
    MoveCamera(29, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17840, 0)
    SetChrPos(0x101, 5500, 0, -13000, 90)
    SetChrPos(0x102, 5250, 0, -12000, 90)
    SetChrPos(0x103, 4000, 0, -13000, 90)
    SetChrPos(0x104, 3700, 0, -12000, 90)
    OP_93(0xC, 0x10E, 0x0)
    SetChrSubChip(0xC, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0xB)"), scpexpr(EXPR_END)), "loc_2034")
    OP_2C(0x9, 0x2)

    #C0059
    ChrTalk(
        0xC,
        (
            "#11P……那家伙在入境申请书上\x01",
            "填写了虚假的申报资料哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#6P#0005F虚假的申报资料……？\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        "#6P#0200F是填写了不真实的履历吗？\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xC,
        "#11P那家伙原本是共和国的诈骗犯。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xC,
        (
            "#11P好像很喜欢旅行，以前也有过一次\x01",
            "填写虚假资料的前科，\x01",
            "那次就是被我抓到的。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xC,
        (
            "#11P这次已经是第二次了……\x01",
            "真是一个白痴。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x104,
        (
            "#5P#0301F原本是诈骗犯……？\x01",
            "那他现在在做什么啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xC,
        (
            "#11P在共和国刑满释放后，\x01",
            "好像一直过着正经日子。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xC,
        (
            "#11P听说那家伙犯的诈骗案\x01",
            "影响不那么恶劣，\x01",
            "所以没有被判重罪。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#5P#0103F不过，『前科』这两个字\x01",
            "还是会陪伴他一生的……\x02\x03",

            "#0108F如果在入境申请书上写明有过前科，\x01",
            "那么在旅行中的行动就会受到限制。\x01",
            "他应该是想避免这点吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xC,
        (
            "#11P虽然那家伙有悔过之意，\x01",
            "但为时已晚，\x01",
            "这就叫自作自受。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xC,
        (
            "#11P自己犯下的罪，必须由自己背负一生。\x01",
            "所以千万不能犯罪。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        "#6P#0001F……那名男子现在怎么样了？\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xC,
        "#11P被拘留在我的办公室里。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xC,
        (
            "#11P等我严厉警告他一下后，\x01",
            "就把他遣送回共和国。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xC,
        "#11P毕竟也不是什么严重的事。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        "#6P#0003F这样啊……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xC,
        (
            "#11P……总之，终于顺利\x01",
            "检查完所有车厢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xC,
        (
            "#11P虽然比预期要迟了点……\x01",
            "但总算能让列车顺利发车了。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xC,
        (
            "#11P感谢你们，\x01",
            "特别任务支援科的各位……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xC,
        "#11P以后也请你们多多帮忙啊。\x02",
    )

    CloseMessageWindow()
    OP_29(0x9, 0x1, 0xC)
    Jump("loc_20AF")

    label("loc_2034")


    #C0080
    ChrTalk(
        0xC,
        (
            "#11P终于顺利\x01",
            "检查完所有车厢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xC,
        (
            "#11P多亏了你们，\x01",
            "列车才能准时发车。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xC,
        (
            "#11P感谢你们，\x01",
            "特别任务支援科的各位……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20AF")


    #C0083
    ChrTalk(
        0x101,
        (
            "#6P#0000F您客气了，我们也借此机会\x01",
            "学会了不少东西。\x02\x03",

            "如果还有什么需要，\x01",
            "请随时联系我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xC,
        "#11P嗯，那么再见。\x02",
    )

    CloseMessageWindow()
    OP_68(5080, 1000, -12450, 5000)
    MoveCamera(26, 13, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(17840, 5000)
    BeginChrThread(0xC, 1, 0, 13)
    BeginChrThread(0x101, 1, 0, 16)
    WaitChrThread(0xC, 1)
    EndChrThread(0x101, 0x1)

    def lambda_216B():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_216B)

    def lambda_2178():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2178)

    def lambda_2185():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2185)

    def lambda_2192():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2192)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0085
    ChrTalk(
        0x101,
        (
            "#12P#0006F呼……这真是\x01",
            "累人的工作啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x102,
        (
            "#11P#0100F嗯，确实……\x02\x03",

            "#0106F不过，我们这些人里，\x01",
            "缇欧应该是最累的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0087
    ChrTalk(
        0x101,
        "#12P#0005F……为什么啊？\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x104,
        (
            "#5P#0309F不知是把她当成了『一日站长』还是什么的，\x01",
            "乘客们都很喜欢围着她啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0089
    ChrTalk(
        0x101,
        (
            "#12P#0005F一、一日站长……\x01",
            "缇欧，你不要紧吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x103,
        "#6P#0203F…………………………\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#12P#0005F累得连说话的力气\x01",
            "都没有了吗……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        (
            "#6P#0206F没、没有。\x01",
            "只是精神上有些疲劳而已，\x01",
            "没什么大问题。\x02\x03",

            "#0200F……我们走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#12P#0003F这、这样啊……\x01",
            "总之，你可千万不要勉强啊。\x02",
        )
    )

    CloseMessageWindow()
    Sound(9, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0094
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找代理安检官】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 5000, 0, -13500, 90)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_29(0x9, 0x1, 0xD)
    OP_29(0x9, 0x4, 0x10)
    OP_4C(0xC, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_15_1ACD end

    def Function_16_2490(): pass

    label("Function_16_2490")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24E4")

    def lambda_24A0():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_24A0)

    def lambda_24AD():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_24AD)

    def lambda_24BA():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_24BA)

    def lambda_24C7():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_24C7)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    Jump("Function_16_2490")

    label("loc_24E4")

    Return()

    # Function_16_2490 end

    def Function_17_24E5(): pass

    label("Function_17_24E5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(452)
    LoadChrToIndex("chr/ch20800.itc", 0x1E)
    LoadChrToIndex("chr/ch20900.itc", 0x1F)
    LoadChrToIndex("chr/ch20000.itc", 0x20)
    LoadChrToIndex("chr/ch20400.itc", 0x21)
    LoadChrToIndex("chr/ch20700.itc", 0x22)
    LoadChrToIndex("chr/ch28300.itc", 0x23)
    LoadChrToIndex("chr/ch20200.itc", 0x24)
    LoadChrToIndex("chr/ch20500.itc", 0x25)
    LoadChrToIndex("chr/ch28400.itc", 0x26)
    LoadChrToIndex("chr/ch21802.itc", 0x27)
    LoadChrToIndex("apl/ch50003.itc", 0x28)
    OP_68(17500, 3800, -200, 0)
    MoveCamera(58, 1, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(17000, 0)
    OP_EE(0x0, 0x1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 15700, 0, -9700, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xD, 15700, 0, -9700, 180)
    SetChrPos(0xE, 15700, 0, -9700, 180)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 3000, 0, -2600, 90)
    SetChrChipByIndex(0x10, 0x25)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 20000, 0, 2200, 270)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x2)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x1)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 19500, 100, -1300, 180)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -3000, 0, 3300, 90)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 20000, 0, -30000, 270)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 52500, 0, -13300, 45)
    SetChrChipByIndex(0x18, 0x27)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 32800, 100, -14600, 0)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    OP_49()
    SetChrPos(0x19, 7000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_E5()
    ClearChrFlags(0xF, 0x80)

    def lambda_2736():
        OP_95(0xFE, 40000, 0, -2600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2736)
    ClearChrFlags(0x10, 0x80)

    def lambda_2755():
        OP_95(0xFE, 8000, 0, 2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2755)
    ClearChrFlags(0x13, 0x80)
    OP_68(17500, 1800, -200, 10000)
    FadeToBright(2000, 0)
    OP_0D()
    ClearChrFlags(0x14, 0x80)

    def lambda_2794():
        OP_95(0xFE, 34000, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2794)
    OP_6F(0x1)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    Fade(1000)
    OP_68(27000, 1500, -15000, 0)
    MoveCamera(54, 5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(28000, 0)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)

    def lambda_2805():
        OP_95(0xFE, 12000, 0, -30000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2805)
    MoveCamera(60, 5, 0, 8000)
    SetCameraDistance(38000, 8000)
    WaitChrThread(0x16, 1)
    PlaceName2(340, 200, "c_plac00", 0x0, 0)
    Sleep(2000)

    def lambda_284B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_284B)
    WaitChrThread(0x16, 2)
    Sleep(500)

    def lambda_285F():
        OP_95(0xFE, 22000, 0, -30000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_285F)
    OP_6F(0x40)
    OP_6F(0x10)
    Sleep(1000)
    Fade(500)
    OP_68(57000, 1500, -8500, 0)
    OP_6E(780, 0)
    SetCameraDistance(21000, 0)
    MoveCamera(53, 2, 0, 0)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_68(10000, 500, -8500, 10000)
    MoveCamera(57, 12, 0, 10000)
    ClearMapObjFlags(0x1, 0x4)
    BeginChrThread(0x19, 3, 0, 18)
    WaitChrThread(0x19, 3)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_68(18400, -900, -4400, 0)
    MoveCamera(54, 10, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(30500, 0)
    SetCameraDistance(33500, 20000)
    Sleep(1000)
    Sound(454, 0, 100, 0)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    OP_79(0x1)
    BeginChrThread(0x11, 3, 0, 21)
    Sleep(500)
    BeginChrThread(0x12, 3, 0, 20)
    Sleep(500)
    BeginChrThread(0xF, 3, 0, 22)
    Sleep(800)
    BeginChrThread(0x14, 3, 0, 20)
    Sleep(2200)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(300)
    BeginChrThread(0x10, 3, 0, 23)
    Sleep(700)
    BeginChrThread(0x15, 3, 0, 23)
    BeginChrThread(0xD, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0xE, 3, 0, 21)
    Sleep(8000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    OP_EE(0x0, 0xA)
    OP_E6()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_24E5 end

    def Function_18_2A22(): pass

    label("Function_18_2A22")

    Sound(452, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x3D, 0x168, 0x0, 0x0)
    Sleep(2000)

    def lambda_2A40():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_2A40)
    OP_79(0x1)
    Sound(143, 0, 100, 0)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    Sleep(500)
    Return()

    # Function_18_2A22 end

    def Function_19_2A66(): pass

    label("Function_19_2A66")


    def lambda_2A6B():
        OP_96(0xFE, 0x1B58, 0xFFFFF9F2, 0xFFFFE05C, 0x2260, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2A6B)
    Sleep(2000)

    def lambda_2A88():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_2A88)
    Sleep(1000)

    def lambda_2A98():
        OP_96(0xFE, 0x1B58, 0xFFFFF9F2, 0xFFFFE05C, 0x1E78, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2A98)
    Sleep(2000)

    def lambda_2AB5():
        OP_96(0xFE, 0x1B58, 0xFFFFF9F2, 0xFFFFE05C, 0x1A90, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2AB5)
    Sleep(2000)

    def lambda_2AD2():
        OP_96(0xFE, 0x1B58, 0xFFFFF9F2, 0xFFFFE05C, 0x16A8, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2AD2)
    Sleep(2000)

    def lambda_2AEF():
        OP_96(0xFE, 0x1B58, 0xFFFFF9F2, 0xFFFFE05C, 0x12C0, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2AEF)
    Sleep(1500)

    def lambda_2B0C():
        OP_96(0xFE, 0x1B58, 0xFFFFF9F2, 0xFFFFE05C, 0xED8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2B0C)
    WaitChrThread(0x19, 1)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    Sleep(500)
    Return()

    # Function_19_2A66 end

    def Function_20_2B3A(): pass

    label("Function_20_2B3A")

    SetChrPos(0xFE, 6000, 0, -9700, 180)

    def lambda_2B50():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B50)

    def lambda_2B61():
        OP_95(0xFE, 6000, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B61)
    WaitChrThread(0xFE, 1)

    def lambda_2B7F():
        OP_95(0xFE, -5000, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B7F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_20_2B3A end

    def Function_21_2B99(): pass

    label("Function_21_2B99")

    SetChrPos(0xFE, 15700, 0, -9700, 180)

    def lambda_2BAF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2BAF)

    def lambda_2BC0():
        OP_95(0xFE, 15700, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BC0)
    WaitChrThread(0xFE, 1)

    def lambda_2BDE():
        OP_95(0xFE, -5000, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BDE)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_21_2B99 end

    def Function_22_2BF8(): pass

    label("Function_22_2BF8")

    SetChrPos(0xFE, 18700, 0, -9700, 180)

    def lambda_2C0E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C0E)

    def lambda_2C1F():
        OP_95(0xFE, 18700, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C1F)
    WaitChrThread(0xFE, 1)

    def lambda_2C3D():
        OP_95(0xFE, -5000, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C3D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_2BF8 end

    def Function_23_2C57(): pass

    label("Function_23_2C57")

    SetChrPos(0xFE, 28400, 0, -9700, 180)

    def lambda_2C6D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C6D)

    def lambda_2C7E():
        OP_95(0xFE, 28400, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C7E)
    WaitChrThread(0xFE, 1)

    def lambda_2C9C():
        OP_95(0xFE, -5000, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C9C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_2C57 end

    def Function_24_2CB6(): pass

    label("Function_24_2CB6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(453)
    SoundLoad(805)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x0, 0x19)
    OP_49()
    SetChrPos(0x19, 55000, -1550, 8000, 0)
    OP_D3(0x19, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_70(0x0, 0x1E)
    OP_68(-22350, 3240, -810, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -21570, 600, 190, 90)
    SetChrPos(0x102, -21570, 600, -1220, 90)
    SetChrPos(0x103, -22700, 600, -1220, 90)
    SetChrPos(0x104, -22700, 600, 190, 90)
    OP_68(-14120, 2100, 690, 2000)

    def lambda_2D8E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2D8E)

    def lambda_2DA3():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2DA3)

    def lambda_2DB8():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2DB8)

    def lambda_2DCD():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2DCD)
    StopBGM(0x1388)
    Sound(805, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x3, 1)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("站员的声音")

    #A0095
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "１号线，前往共和国的列车\x01",
            "即将发车。\x02",
        )
    )

    CloseMessageWindow()

    #A0096
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "送行人员\x01",
            "请退往月台。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_2EAF():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2EAF)

    def lambda_2EBC():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2EBC)

    def lambda_2EC9():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2EC9)

    def lambda_2ED6():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2ED6)
    Sleep(300)

    #C0097
    ChrTalk(
        0x104,
        (
            "#5P#0305F喂……\x01",
            "那不是议员千金\x01",
            "乘坐的列车吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#11P#0001F还来得及……\x01",
            "我们也上车吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x2, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_2F8E():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2F8E)

    def lambda_2F9B():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2F9B)

    def lambda_2FA8():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2FA8)

    def lambda_2FB5():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2FB5)
    WaitChrThread(0x3, 1)
    BeginChrThread(0x19, 3, 0, 25)
    BeginChrThread(0x101, 3, 0, 26)
    Sleep(150)
    BeginChrThread(0x102, 3, 0, 26)
    Sleep(250)
    BeginChrThread(0x104, 3, 0, 26)
    Sleep(150)
    BeginChrThread(0x103, 3, 0, 26)
    Sleep(2000)
    BeginChrThread(0x1D, 0, 0, 37)
    Sleep(3000)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x104, 3)
    EndChrThread(0x1D, 0x0)
    Sound(454, 0, 100, 0)
    OP_71(0x0, 0x14, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    Sound(143, 0, 100, 0)
    OP_82(0x64, 0x32, 0xBB8, 0x1F4)
    Sleep(800)
    Fade(500)
    OP_68(5700, 1500, 4200, 0)
    MoveCamera(58, 1, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(17000, 0)
    OP_EE(0x0, 0x1)
    OP_0D()
    BeginChrThread(0x19, 1, 0, 27)
    OP_68(61700, 1500, 4200, 9000)
    Sleep(8000)
    BeginChrThread(0x1D, 0, 0, 36)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    EndChrThread(0x1D, 0x0)
    OP_EE(0x0, 0xA)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x325)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 0)
    NewScene("r0040", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_2CB6 end

    def Function_25_3112(): pass

    label("Function_25_3112")

    OP_68(-9530, 2100, -200, 2000)
    OP_6F(0x1)
    OP_68(700, 1500, 4200, 1500)
    MoveCamera(44, 13, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(18000, 1500)
    Return()

    # Function_25_3112 end

    def Function_26_3154(): pass

    label("Function_26_3154")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x1)
    OP_95(0xFE, -1000, 0, 3000, 5000, 0x1)

    def lambda_317C():
        OP_95(0xFE, -1000, 0, 7000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_317C)
    Sleep(400)

    def lambda_3199():
        OP_A7(0xFE, 0x0, 0x0, 0x0, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3199)
    OP_64(0xFE)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_26_3154 end

    def Function_27_31B1(): pass

    label("Function_27_31B1")

    Sound(453, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x169, 0x294, 0x0, 0x0)
    Return()

    # Function_27_31B1 end

    def Function_28_31C8(): pass

    label("Function_28_31C8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(452)
    LoadChrToIndex("chr/ch20800.itc", 0x1E)
    LoadChrToIndex("chr/ch20900.itc", 0x1F)
    LoadChrToIndex("chr/ch20000.itc", 0x20)
    LoadChrToIndex("chr/ch20400.itc", 0x21)
    LoadChrToIndex("chr/ch20700.itc", 0x22)
    LoadChrToIndex("chr/ch28300.itc", 0x23)
    LoadChrToIndex("chr/ch20200.itc", 0x24)
    LoadChrToIndex("chr/ch20500.itc", 0x25)
    LoadChrToIndex("chr/ch28400.itc", 0x26)
    LoadChrToIndex("chr/ch21802.itc", 0x27)
    LoadChrToIndex("chr/ch27700.itc", 0x28)
    LoadChrToIndex("chr/ch33200.itc", 0x29)
    LoadChrToIndex("chr/ch34500.itc", 0x2A)
    LoadChrToIndex("apl/ch50111.itc", 0x2B)
    SoundLoad(803)
    OP_68(17500, 3800, -200, 0)
    MoveCamera(58, 1, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(17000, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x0, 15700, 0, -9700, 180)
    SetChrPos(0x1, 15700, 0, -9700, 180)
    SetChrPos(0x2, 15700, 0, -9700, 180)
    SetChrPos(0x3, 15700, 0, -9700, 180)
    SetChrPos(0x1B, 15700, 0, -9700, 180)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1B, 0x29)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1A, 0x28)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1C, 0x2A)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x12, 0x2)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -3000, 0, 3300, 90)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 3000, 0, -2600, 90)
    SetChrChipByIndex(0x10, 0x25)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 20000, 0, 2200, 270)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x23)
    SetChrChipByIndex(0x13, 0x1)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 19500, 100, -1300, 180)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 20000, 0, -30000, 270)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 52500, 0, -13300, 45)
    SetChrChipByIndex(0x18, 0x27)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 32800, 100, -14600, 0)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    OP_49()
    SetChrPos(0x19, 7000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetChrName("")

    #A0099
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德一行在阿尔泰尔市\x01",
            "换乘了返回自治州的列车。\x02",
        )
    )

    CloseMessageWindow()

    #A0100
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "三十分钟后……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7103", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 2)
    Sound(803, 2, 100, 0)
    ClearScenarioFlags(0x0, 3)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    Sleep(2500)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_68(61500, 2500, -10500, 0)
    MoveCamera(60, 15, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(16000, 0)
    OP_EE(0x0, 0x1)
    OP_68(58500, 2500, -11500, 5000)
    MoveCamera(45, 20, 0, 5000)
    SetCameraDistance(24000, 5000)
    ClearMapObjFlags(0x1, 0x4)
    BeginChrThread(0x19, 3, 0, 18)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(5500, 3300, -8000, 0)
    MoveCamera(48, -15, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(14000, 0)
    OP_68(5500, 2300, -8000, 4000)
    OP_0D()
    WaitChrThread(0x19, 3)
    OP_6F(0x1)
    Sleep(1000)
    Fade(500)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_68(18400, -900, -4400, 0)
    MoveCamera(54, 10, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(30500, 0)
    SetCameraDistance(33500, 20000)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_364D")
    Call(0, 29)
    Jump("loc_3650")

    label("loc_364D")

    Call(0, 32)

    label("loc_3650")

    Return()

    # Function_28_31C8 end

    def Function_29_3651(): pass

    label("Function_29_3651")

    Sound(454, 0, 100, 0)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    OP_79(0x1)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    BeginChrThread(0x11, 3, 0, 21)
    Sleep(500)
    BeginChrThread(0x12, 3, 0, 20)
    Sleep(500)
    BeginChrThread(0xF, 3, 0, 22)
    Sleep(800)
    BeginChrThread(0x14, 3, 0, 20)
    Sleep(2200)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(300)
    BeginChrThread(0x10, 3, 0, 23)
    Sleep(700)
    BeginChrThread(0x15, 3, 0, 23)
    BeginChrThread(0x102, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x1B, 3, 0, 21)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x0, 0x2)
    EndChrThread(0x0, 0x3)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x1, 0x2)
    EndChrThread(0x1, 0x3)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x2, 0x2)
    EndChrThread(0x2, 0x3)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x3, 0x2)
    EndChrThread(0x3, 0x3)
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1B, 0x2)
    EndChrThread(0x1B, 0x3)
    EndChrThread(0xF, 0x1)
    EndChrThread(0xF, 0x2)
    EndChrThread(0xF, 0x3)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x1B, 0x0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrPos(0x101, 4059, 0, -15180, 45)
    SetChrPos(0x102, 4920, 0, -15560, 0)
    SetChrPos(0x103, 3910, 0, -13780, 135)
    SetChrPos(0x104, 4810, 0, -12940, 180)
    SetChrPos(0x1B, 5870, 0, -14030, 270)
    SetChrPos(0xF, 5500, 0, -14560, 270)
    SetChrPos(0x1A, -7130, 600, -15750, 90)
    SetChrPos(0x1C, -9130, 600, -16740, 90)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    OP_68(4760, 1500, -14530, 0)
    MoveCamera(49, 27, 0, 0)
    OP_6E(720, 0)
    SetCameraDistance(12050, 0)
    OP_EE(0x0, 0xA)
    FadeToBright(1000, 0)
    OP_0D()

    #C0101
    ChrTalk(
        0x104,
        "#5P#0306F呼，终于回来了。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x103,
        "#6P#0200F真不容易啊。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x1B,
        "#11P各位，给你们添麻烦了。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x1B,
        (
            "#11P还听我说了那么多话，\x01",
            "真是谢谢你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x102,
        "#12P#0100F呵呵，不用客气。\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        (
            "#6P#0000F如果有事想要商量，随时都可以来找我们。\x01",
            "以后要是还有什么需要的话，\x01",
            "就请联系我们支援科。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x1B,
        "#11P好、好的……\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(200)
    TurnDirection(0x1B, 0x1A, 400)
    Sleep(400)

    #C0108
    ChrTalk(
        0x1B,
        "#11P啊……\x02",
    )

    CloseMessageWindow()
    OP_68(1960, 1500, -15420, 3000)
    MoveCamera(320, 30, 0, 3000)

    def lambda_39E6():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39E6)

    def lambda_39F3():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_39F3)

    def lambda_3A00():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3A00)

    def lambda_3A0D():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3A0D)

    def lambda_3A1A():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3A1A)

    def lambda_3A2F():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_3A2F)
    Sleep(2500)
    Sleep(800)

    #C0109
    ChrTalk(
        0x1A,
        (
            "#5P哼，笨蛋女儿，\x01",
            "这种时候还让人担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x1B,
        "#12P父、父亲您才是笨蛋呢！\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x1B,
        (
            "#12P不自己来找我，\x01",
            "竟然拜托别人……！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 1, 0, 30)
    OP_96(0x1C, 0xFFFFFCD6, 0x0, 0xFFFFBEB0, 0x3E8, 0x0)
    TurnDirection(0x1C, 0x1B, 400)
    Sleep(300)

    #C0112
    ChrTalk(
        0x1C,
        "#5P那个，小姐……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x1C,
        (
            "#5P实在对不起，\x01",
            "是我擅作主张了……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1B, 0xE1, 0x190)
    Sleep(300)

    #C0114
    ChrTalk(
        0x1B,
        (
            "#12P哼，真是的！\x01",
            "我也在生玛夏你的气哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x1C,
        "#5P十、十、十分抱歉……\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x1B,
        (
            "#12P不过，那个……\x01",
            "还是谢谢你。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x1B,
        "#12P你还会陪着我吗？\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x1C,
        "#5P是、是的，非常乐意。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x1B,
        (
            "#12P……太好了，\x01",
            "这样我就能下定决心了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1A, 400)
    Sleep(300)

    #C0120
    ChrTalk(
        0x1B,
        "#12P父亲，我有个要求。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x1B,
        (
            "#12P以后要进我房间的时候，\x01",
            "请您一定要敲门！\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x1B,
        (
            "#12P还有，以后不许\x01",
            "过问我的私生活！\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x1B,
        (
            "#12P……如果您做不到的话，\x01",
            "我现在就离家出走。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x1A,
        "#5P唔唔……\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x1A,
        (
            "#5P算了，但你要给我老实\x01",
            "在家待几天。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x1B,
        (
            "#12P您这是答应我的要求吗？\x01",
            "还是不答应？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x101, 0)

    #C0127
    ChrTalk(
        0x1A,
        (
            "#5P哼，不必担心，\x01",
            "我也不想再看到这种骚乱了。\x01",
            "所以我答应你，会遵守这个约定的。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(2670, 1500, -15870, 2000)

    def lambda_3D88():

        label("loc_3D88")

        TurnDirection(0xFE, 0x1A, 400)
        Yield()
        Jump("loc_3D88")

    QueueWorkItem2(0x1B, 1, lambda_3D88)

    def lambda_3D9A():

        label("loc_3D9A")

        TurnDirection(0xFE, 0x1A, 400)
        Yield()
        Jump("loc_3D9A")

    QueueWorkItem2(0x1C, 1, lambda_3D9A)

    def lambda_3DAC():
        OP_95(0xFE, 2040, 0, -14970, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3DAC)
    Sleep(300)
    OP_96(0x1B, 0x244, 0x0, 0xFFFFC180, 0x3E8, 0x0)
    Sleep(400)

    #C0128
    ChrTalk(
        0x1A,
        "#5P那个警察局的什么科。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x1A,
        (
            "#5P对于将小女平安带回一事，\x01",
            "我暂且表示感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x1A,
        (
            "#5P不过，你们记住，\x01",
            "这次的事不可跟他人提起。\x01",
            "知道了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        "#11P#0300F嗯，当然了。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        "#12P#0000F这一点请您放心。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x1A,
        "#5P那就好。\x02",
    )

    CloseMessageWindow()
    OP_95(0x1A, -630, 0, -14820, 2000, 0x0)

    #C0134
    ChrTalk(
        0x1A,
        "#5P卡拉，回家了！\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x1B,
        "#12P哼，别对我指手划脚的！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1A, 0, 0, 31)
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1C, 0x1)

    def lambda_3F14():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_3F14)

    def lambda_3F21():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_3F21)
    Sleep(300)

    #C0136
    ChrTalk(
        0x1B,
        (
            "#5P艾莉小姐，各位。\x01",
            "……再见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x1C,
        (
            "#5P各位，\x01",
            "真是非常谢谢你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x1C,
        (
            "#5P那个，有时间\x01",
            "请来家里玩啊。\x01",
            "我们将热情款待你们……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")
    FadeToDark(300, 0, 100)

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "两人深深低下了头，表示感谢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    BeginChrThread(0x1B, 1, 0, 31)

    def lambda_3FF6():

        label("loc_3FF6")

        TurnDirection(0xFE, 0x1B, 400)
        Yield()
        Jump("loc_3FF6")

    QueueWorkItem2(0x1C, 1, lambda_3FF6)
    Sleep(1200)
    BeginChrThread(0x1C, 1, 0, 31)
    OP_63(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(2400)

    #C0140
    ChrTalk(
        0x101,
        "#12P#0004F事情总算解决了。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x104,
        (
            "#11P#0300F虽然花了很多时间，\x01",
            "但帮助人的感觉真是不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x103,
        (
            "#11P#0200F看这样子，\x01",
            "应该是没问题了。\x01",
            "结果还算不错吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        (
            "#12P#0104F是啊……\x01",
            "希望他们能好好相处。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(4580, 1500, -14920, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12550, 0)
    SetChrPos(0x102, 5380, 0, -15280, 270)
    OP_0D()

    def lambda_4130():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4130)

    def lambda_413D():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_413D)

    def lambda_414A():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_414A)

    def lambda_4157():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4157)
    Sleep(300)

    #C0144
    ChrTalk(
        0x102,
        (
            "#11P#0100F那么，罗伊德，\x01",
            "我们也该回去了吧，\x02\x03",

            "还有一些工作\x01",
            "必须完成呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        (
            "#6P#0005F啊，对哦……\x02\x03",

            "#0000F好，这项工作就此告一段落。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0146
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【重要人士的搜索委托】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_64(0x1C)
    SetChrPos(0x0, 4780, 0, -14570, 275)
    ClearChrFlags(0x8, 0x80)
    OP_70(0x1, 0x0)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_29(0x2D, 0x4, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_29_3651 end

    def Function_30_4316(): pass

    label("Function_30_4316")

    OP_96(0xFE, 0xDC0, 0x0, 0xFFFFC89C, 0x7D0, 0x0)
    OP_96(0xFE, 0x244, 0x0, 0xFFFFC39C, 0x7D0, 0x0)
    Return()

    # Function_30_4316 end

    def Function_31_433F(): pass

    label("Function_31_433F")

    OP_93(0xFE, 0x10E, 0x190)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_31_433F end

    def Function_32_4360(): pass

    label("Function_32_4360")

    Sound(454, 0, 100, 0)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    OP_79(0x1)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    BeginChrThread(0x11, 3, 0, 21)
    Sleep(500)
    BeginChrThread(0x12, 3, 0, 20)
    Sleep(500)
    BeginChrThread(0xF, 3, 0, 22)
    Sleep(800)
    BeginChrThread(0x14, 3, 0, 20)
    Sleep(2200)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(300)
    BeginChrThread(0x10, 3, 0, 23)
    Sleep(700)
    BeginChrThread(0x15, 3, 0, 23)
    BeginChrThread(0x102, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 21)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x0, 0x2)
    EndChrThread(0x0, 0x3)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x1, 0x2)
    EndChrThread(0x1, 0x3)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x2, 0x2)
    EndChrThread(0x2, 0x3)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x3, 0x2)
    EndChrThread(0x3, 0x3)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrPos(0x101, 3910, 0, -14550, 90)
    SetChrPos(0x102, 4920, 0, -15560, 0)
    SetChrPos(0x103, 5870, 0, -14030, 270)
    SetChrPos(0x104, 4810, 0, -12940, 180)
    SetChrPos(0x1C, -8130, 600, -16740, 90)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    OP_68(4760, 1500, -14530, 0)
    MoveCamera(49, 27, 0, 0)
    OP_6E(720, 0)
    SetCameraDistance(12050, 0)
    OP_EE(0x0, 0xA)
    FadeToBright(1000, 0)
    OP_0D()

    #C0147
    ChrTalk(
        0x104,
        "#5P#0306F呼，终于回来了。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x103,
        "#11P#0203F真是不容易啊。\x02",
    )

    CloseMessageWindow()

    #N0149
    NpcTalk(
        0x1C,
        "声音",
        "那个，各位……\x02",
    )

    CloseMessageWindow()
    OP_68(2670, 1500, -15870, 3000)
    MoveCamera(320, 30, 0, 3000)

    def lambda_4597():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4597)

    def lambda_45A4():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_45A4)

    def lambda_45B1():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_45B1)

    def lambda_45BE():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_45BE)
    OP_95(0x1C, 130, 0, -15210, 2000, 0x0)
    Sleep(300)

    #C0150
    ChrTalk(
        0x1C,
        (
            "#5P小姐……\x01",
            "卡拉小姐的情况怎么样了……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#12P#0006F对不起，其实\x01",
            "我们没能成功将她劝回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x102,
        (
            "#6P#0106F卡拉小姐就那样\x01",
            "直接去共和国了。\x02\x03",

            "#0108F不好意思，\x01",
            "枉费你特意来找我们帮忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x1C,
        (
            "#5P没、没事……\x01",
            "这不是各位的错。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x1C,
        (
            "#5P都怪我没能\x01",
            "阻止小姐……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0155
    ChrTalk(
        0x1C,
        (
            "#5P啊，不过……我要怎么\x01",
            "跟老爷说啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x1C,
        (
            "#5P这样回去的话，\x01",
            "我说不定会被开除……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x102,
        (
            "#6P#0103F坎贝尔议员那边\x01",
            "由我来联系。\x02\x03",

            "#0100F我会帮你说情的，\x01",
            "请不用担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x1C,
        "#5P真、真的吗……？\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x1C,
        (
            "#5P我知道了，\x01",
            "那就拜托您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x1C,
        (
            "#5P那、那个，真是\x01",
            "给你们添麻烦了……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")
    FadeToDark(300, 0, 100)

    #A0161
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "玛夏低头感谢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    BeginChrThread(0x1C, 1, 0, 31)
    Sleep(2400)

    #C0162
    ChrTalk(
        0x104,
        (
            "#12P#0306F唉……\x01",
            "不过，也没办法啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x103,
        (
            "#12P#0200F毕竟问到了联系方法，\x01",
            "也算尽到了警察\x01",
            "最低限度的职责。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            "#12P#0000F是啊，而且也确认了\x01",
            "她的安全情况。\x02\x03",

            "接下来只需向议员报告了……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x102,
        (
            "#6P#0103F这由我来联系吧。\x01",
            "……我必须在玛夏回去之前\x01",
            "把情况告诉他。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_68(4580, 1500, -14920, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12550, 0)
    OP_0D()

    def lambda_4976():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4976)
    Sleep(20)

    def lambda_4986():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4986)
    Sleep(12)

    def lambda_4996():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4996)
    Sleep(80)
    OP_93(0x102, 0xB4, 0x190)
    Sleep(300)
    Fade(300)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    Sleep(600)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2800)
    OP_64(0x102)
    Sleep(300)
    SetChrName("")
    FadeToDark(300, 0, 100)

    #A0166
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾莉使用艾尼格玛联系了坎贝尔议员，\x01",
            "将事情的始末和卡拉的联系方式告诉了他。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    OP_93(0x102, 0x0, 0x190)
    Sleep(200)

    #C0167
    ChrTalk(
        0x101,
        "#6P#0005F议员说了什么？\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x102,
        "#12P#0103F说『辛苦了』。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x104,
        (
            "#5P#0306F哎呀呀，\x01",
            "这反应真没意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x103,
        "#11P#0203F嗯，虽然是在预料之中的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    Sleep(300)

    #C0171
    ChrTalk(
        0x103,
        (
            "#11P#0200F……罗伊德前辈，\x01",
            "我们差不多该回去了吧。\x01",
            "还有一些工作必须完成。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(300)

    #C0172
    ChrTalk(
        0x101,
        (
            "#11P#0005F啊，对哦……\x02\x03",

            "#0000F好，这项工作就此告一段落。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0173
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【重要人士的搜索委托】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 4780, 0, -14570, 275)
    OP_70(0x1, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_29(0x2D, 0x4, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_32_4360 end

    def Function_33_4CBE(): pass

    label("Function_33_4CBE")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xC)"), scpexpr(EXPR_END)), "loc_4D1C")

    #C0174
    ChrTalk(
        0x101,
        (
            "#0003F这是去其它\x01",
            "月台的通道。\x02\x03",

            "#0000F工作都做完了，\x01",
            "我们直接回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DBD")

    label("loc_4D1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4D73")

    #C0175
    ChrTalk(
        0x101,
        (
            "#0000F安检都结束了……\x01",
            "所以没有必要去前往\x01",
            "共和国方向列车的月台。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DBD")

    label("loc_4D73")


    #C0176
    ChrTalk(
        0x101,
        (
            "#0003F这是去其它\x01",
            "月台的通道。\x02\x03",

            "#0001F必须在列车出发之前\x01",
            "开始任务……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DBD")

    Sleep(50)
    SetChrPos(0x0, 54500, 0, -16000, 270)
    EventEnd(0x4)
    Return()

    # Function_33_4CBE end

    def Function_34_4DD4(): pass

    label("Function_34_4DD4")

    TalkBegin(0xFF)
    SetChrName("")

    #A0177
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有开往克洛斯贝尔自治州\x01",
            "周边地区的列车时刻表。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_34_4DD4 end

    def Function_35_4E15(): pass

    label("Function_35_4E15")

    TalkBegin(0xFF)
    SetChrName("")

    #A0178
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有克洛斯贝尔自治州\x01",
            "周边地区的路线图。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_35_4E15 end

    def Function_36_4E4E(): pass

    label("Function_36_4E4E")

    OP_25(0x323, 0x64)
    Sleep(200)
    OP_25(0x323, 0x5A)
    Sleep(200)
    OP_25(0x323, 0x50)
    Sleep(200)
    OP_25(0x323, 0x46)
    Sleep(200)
    OP_25(0x323, 0x3C)
    Sleep(200)
    OP_25(0x323, 0x32)
    Sleep(200)
    OP_25(0x323, 0x28)
    Sleep(200)
    OP_25(0x323, 0x1E)
    Sleep(200)
    OP_25(0x323, 0x14)
    Sleep(200)
    OP_25(0x323, 0xA)
    Sleep(200)
    OP_25(0x323, 0x0)
    Return()

    # Function_36_4E4E end

    def Function_37_4E99(): pass

    label("Function_37_4E99")

    OP_25(0x325, 0x64)
    Sleep(80)
    OP_25(0x325, 0x5A)
    Sleep(80)
    OP_25(0x325, 0x50)
    Sleep(80)
    OP_25(0x325, 0x46)
    Sleep(80)
    OP_25(0x325, 0x3C)
    Sleep(80)
    OP_25(0x325, 0x32)
    Sleep(80)
    OP_25(0x325, 0x28)
    Sleep(80)
    OP_25(0x325, 0x1E)
    Sleep(80)
    OP_25(0x325, 0x14)
    Sleep(80)
    OP_25(0x325, 0xA)
    Sleep(80)
    OP_25(0x325, 0x0)
    Return()

    # Function_37_4E99 end

    SaveToFile()

Try(main)
