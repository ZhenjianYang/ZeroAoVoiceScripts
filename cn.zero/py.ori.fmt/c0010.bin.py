from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0010.bin",                # FileName
        "c0010",                    # MapName
        "c0010",                    # Location
        0x0003,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 3, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0010",                  # 0
        "站员卢克斯",             # 1
        "站员莉莎",               # 2
        "站员艾姆",               # 3
        "站员仙莉",               # 4
        "站员玛吉斯",             # 5
        "库瓦特罗安检官",         # 6
        "游击士斯克特",           # 7
        "游击士温蔡尔",           # 8
        "游击士林",               # 9
        "游击士艾欧莉娅",         # 10
        "乘客",                   # 11
        "乘客",                   # 12
        "乘客",                   # 13
        "乘客",                   # 14
        "乘客",                   # 15
        "乘客",                   # 16
        "乘客",                   # 17
        "乘客",                   # 18
    ))

    AddCharChip((
        "chr/ch28300.itc",                   # 00
        "chr/ch28400.itc",                   # 01
        "chr/ch28500.itc",                   # 02
        "chr/ch22002.itc",                   # 03
        "chr/ch22102.itc",                   # 04
        "chr/ch21202.itc",                   # 05
        "chr/ch20000.itc",                   # 06
        "chr/ch20400.itc",                   # 07
        "chr/ch34200.itc",                   # 08
        "chr/ch21600.itc",                   # 09
        "chr/ch27200.itc",                   # 0A
        "chr/ch27300.itc",                   # 0B
        "chr/ch32000.itc",                   # 0C
        "chr/ch32100.itc",                   # 0D
    ))

    DeclNpc(4750,    0,       7500,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(9500,    0,       7500,    180,  257,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(33000,   4000,    8000,    270,  257,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(33000,   4000,    -8000,   270,  257,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(18260,   0,       10229,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(28000,   4000,    10000,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(12439,   29,      -409,    180,  389,  0x0, 0,   10,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(12439,   29,      -2549,   0,    405,  0x0, 0,   11,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(6420,    29,      -2569,   180,  389,  0x0, 0,   12,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(6420,    0,       -4050,   0,    389,  0x0, 0,   13,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(14000,   100,     -8899,   0,    469,  0x0, 0,   3,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(13000,   100,     -8899,   0,    469,  0x0, 0,   4,   0,   255, 255, 0,   21,  255,  0)
    DeclNpc(5500,    100,     -5400,   0,    469,  0x0, 0,   5,   0,   255, 255, 0,   22,  255,  0)
    DeclNpc(29500,   4000,    1350,    90,   385,  0x0, 0,   6,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(28500,   4000,    1350,    90,   385,  0x0, 0,   7,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(13500,   100,     -8899,   0,    469,  0x0, 0,   4,   0,   255, 255, 0,   25,  255,  0)
    DeclNpc(11000,   0,       0,       90,   385,  0x0, 0,   8,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(12000,   0,       0,       270,  385,  0x0, 0,   9,   0,   0,   0,   0,   27,  255,  0)

    DeclActor(4750,    0,       6500,    1000,    4750,    1500,    7500,    0x007E, 0,  5,  0x0000)
    DeclActor(9500,    0,       6500,    1000,    9500,    1500,    7500,    0x007E, 0,  7,  0x0000)
    DeclActor(32000,   4000,    8000,    1000,    33000,   5500,    8000,    0x007E, 0,  9,  0x0000)
    DeclActor(32000,   4000,    -8000,   1000,    33000,   5500,    -8000,   0x007E, 0,  11, 0x0000)
    DeclActor(20560,   0,       4090,    1000,    20560,   1500,    4090,    0x007C, 0,  35, 0x0000)
    DeclActor(20130,   0,       -4810,   1000,    20130,   1500,    -4810,   0x007C, 0,  36, 0x0000)
    DeclActor(31150,   4000,    1130,    1000,    31150,   5500,    1130,    0x007C, 0,  37, 0x0000)
    DeclActor(28100,   4000,    11510,   1000,    28100,   5500,    11510,   0x007C, 0,  38, 0x0000)
    DeclActor(30940,   4000,    -1900,   1000,    30940,   5500,    -1900,   0x007C, 0,  39, 0x0000)

    ScpFunction((
        "Function_0_4A8",          # 00, 0
        "Function_1_560",          # 01, 1
        "Function_2_58B",          # 02, 2
        "Function_3_600",          # 03, 3
        "Function_4_6F4",          # 04, 4
        "Function_5_781",          # 05, 5
        "Function_6_785",          # 06, 6
        "Function_7_A90",          # 07, 7
        "Function_8_A94",          # 08, 8
        "Function_9_1077",         # 09, 9
        "Function_10_107B",        # 0A, 10
        "Function_11_121F",        # 0B, 11
        "Function_12_1223",        # 0C, 12
        "Function_13_15FC",        # 0D, 13
        "Function_14_1B8B",        # 0E, 14
        "Function_15_1CB4",        # 0F, 15
        "Function_16_1FD3",        # 10, 16
        "Function_17_22F7",        # 11, 17
        "Function_18_23DB",        # 12, 18
        "Function_19_27BD",        # 13, 19
        "Function_20_2938",        # 14, 20
        "Function_21_2B26",        # 15, 21
        "Function_22_2CEB",        # 16, 22
        "Function_23_2ECF",        # 17, 23
        "Function_24_2F90",        # 18, 24
        "Function_25_30C8",        # 19, 25
        "Function_26_32C8",        # 1A, 26
        "Function_27_3362",        # 1B, 27
        "Function_28_3444",        # 1C, 28
        "Function_29_3748",        # 1D, 29
        "Function_30_390B",        # 1E, 30
        "Function_31_39EA",        # 1F, 31
        "Function_32_3B1A",        # 20, 32
        "Function_33_3F13",        # 21, 33
        "Function_34_427C",        # 22, 34
        "Function_35_42D0",        # 23, 35
        "Function_36_4346",        # 24, 36
        "Function_37_43BE",        # 25, 37
        "Function_38_4401",        # 26, 38
        "Function_39_4477",        # 27, 39
    ))


    def Function_0_4A8(): pass

    label("Function_0_4A8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4E8"),
        (1, "loc_4F4"),
        (2, "loc_500"),
        (3, "loc_50C"),
        (4, "loc_518"),
        (5, "loc_524"),
        (6, "loc_530"),
        (SWITCH_DEFAULT, "loc_53C"),
    )


    label("loc_4E8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_4F4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_500")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_50C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_518")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_524")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_530")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_53C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_548")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_55F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_55F")

    Return()

    # Function_0_4A8 end

    def Function_1_560(): pass

    label("Function_1_560")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_58A")
    OP_94(0xFE, 0x4D12, 0x686, 0x3F6F, 0xFFFFF81C, 0x3E8)
    Sleep(300)
    Jump("Function_1_560")

    label("loc_58A")

    Return()

    # Function_1_560 end

    def Function_2_58B(): pass

    label("Function_2_58B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5FF")
    OP_95(0xFE, 20920, 4000, -8210, 1000, 0x0)
    OP_95(0xFE, 20920, 4000, 760, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0xC8)
    Sleep(2500)
    OP_95(0xFE, 20920, 4000, -8210, 1000, 0x0)
    OP_95(0xFE, 18700, 4000, -8210, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0xC8)
    Sleep(4500)
    Jump("Function_2_58B")

    label("loc_5FF")

    Return()

    # Function_2_58B end

    def Function_3_600(): pass

    label("Function_3_600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_614")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 33)
    Jump("loc_621")

    label("loc_614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_621")
    Event(0, 28)

    label("loc_621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6A1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_668")
    SetChrPos(0xD, 18820, 0, 4500, 90)
    SetChrPos(0xC, 19970, 0, 4500, 270)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_679")

    label("loc_668")

    SetChrPos(0xD, 19970, 0, -4490, 90)

    label("loc_679")

    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x18, 0x10)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_6F3")

    label("loc_6A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D0")
    SetChrFlags(0xD, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C6")
    Jump("loc_6CB")

    label("loc_6C6")

    SetChrFlags(0xD, 0x80)

    label("loc_6CB")

    Jump("loc_6DF")

    label("loc_6D0")

    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)

    label("loc_6DF")

    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)

    label("loc_6F3")

    Return()

    # Function_3_600 end

    def Function_4_6F4(): pass

    label("Function_4_6F4")

    ClearMapObjFlags(0x2, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x9)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71D")
    SetMapObjFlags(0x2, 0x10)

    label("loc_71D")

    ClearMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_731")
    Jump("loc_769")

    label("loc_731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_769")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_751")
    SetMapObjFlags(0x1, 0x10)
    Jump("loc_769")

    label("loc_751")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_769")
    SetMapObjFlags(0x1, 0x10)
    OP_1B(0x0, 0x0, 0x22)

    label("loc_769")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_780")
    SetMapObjFlags(0x1, 0x10)

    label("loc_780")

    Return()

    # Function_4_6F4 end

    def Function_5_781(): pass

    label("Function_5_781")

    Call(0, 6)
    Return()

    # Function_5_781 end

    def Function_6_785(): pass

    label("Function_6_785")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9BA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_884")

    #C0001
    ChrTalk(
        0x8,
        (
            "在十几年前的『百日战役』中，\x01",
            "帝国和共和国之间曾经是对立的关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "当年，连铁道的运营都停止了，\x01",
            "所以来克洛斯贝尔旅行的人们\x01",
            "只能被困在这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "现今，为了不让这样的事情再次发生，\x01",
            "已经建立起了完备的体制。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_915")

    label("loc_884")


    #C0004
    ChrTalk(
        0x8,
        (
            "在十几年前的『百日战役』中，\x01",
            "这里的铁道曾被临时停运，\x01",
            "导致许多人都沦为难民。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "如今为了不让这样的事情再次发生，\x01",
            "已经建立起了完备的体制。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_915")

    Jump("loc_9B5")

    label("loc_91A")


    #C0006
    ChrTalk(
        0x8,
        (
            "麦克道尔市长出席\x01",
            "在帝国或共和国举办的会议时，\x01",
            "也会选择乘坐列车呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "虽然乘飞行船会比较快，\x01",
            "但要花费不少米拉的。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        "哎呀，真是个廉洁的好市长啊。\x02",
    )

    CloseMessageWindow()

    label("loc_9B5")

    Jump("loc_A8C")

    label("loc_9BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1F")

    #C0009
    ChrTalk(
        0x8,
        (
            "感谢您今日光临\x01",
            "克洛斯贝尔车站。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "列车到站时\x01",
            "将会非常拥挤，\x01",
            "请您注意安全。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8C")

    label("loc_A1F")


    #C0011
    ChrTalk(
        0x8,
        (
            "铁道是由『大陆铁道公司』\x01",
            "负责运营的。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "另外，库瓦特罗先生\x01",
            "是帝国派来的安检人员，\x01",
            "不是公司的职员哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8C")

    TalkEnd(0x8)
    Return()

    # Function_6_785 end

    def Function_7_A90(): pass

    label("Function_7_A90")

    Call(0, 8)
    Return()

    # Function_7_A90 end

    def Function_8_A94(): pass

    label("Function_8_A94")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1073")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_AF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B10")
    OP_AF(0x89)
    Jump("loc_B72")

    label("loc_B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_B20")
    OP_AF(0x88)
    Jump("loc_B72")

    label("loc_B20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_B30")
    OP_AF(0x87)
    Jump("loc_B72")

    label("loc_B30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_B40")
    OP_AF(0x86)
    Jump("loc_B72")

    label("loc_B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_B50")
    OP_AF(0x85)
    Jump("loc_B72")

    label("loc_B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_B60")
    OP_AF(0x84)
    Jump("loc_B72")

    label("loc_B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_B70")
    OP_AF(0x83)
    Jump("loc_B72")

    label("loc_B70")

    OP_AF(0x82)

    label("loc_B72")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_106E")

    label("loc_B81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B95")
    Jump("loc_106E")

    label("loc_B95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_106E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_DE5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3A")

    #C0013
    ChrTalk(
        0x9,
        (
            "开往共和国的列车\x01",
            "马上就要从一号站台发车了。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            "如需搭乘，请尽快上车，\x01",
            "或者请等待下一班列车。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_CA2")

    label("loc_C3A")


    #C0015
    ChrTalk(
        0x9,
        (
            "开往共和国的列车\x01",
            "马上就要从一号站台发车了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "匆忙挤上车是很危险的，\x01",
            "搭乘时请预留出充裕的时间。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA2")

    Jump("loc_DE0")

    label("loc_CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6C")

    #C0017
    ChrTalk(
        0x9,
        (
            "国境门那里也有\x01",
            "开往帝国和共和国的\x01",
            "定期巴士。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            "虽然乘坐巴士比较花费时间，\x01",
            "不过我们也提供利用这种方式\x01",
            "回国的乘车指南。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        (
            "万一错过了列车的乘车时间，\x01",
            "还请随时与我们联系。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_DE0")

    label("loc_D6C")


    #C0020
    ChrTalk(
        0x9,
        (
            "我们也提供乘坐在国境门始发的巴士，\x01",
            "由陆路回国的乘车指南。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        (
            "万一错过了列车的乘车时间，\x01",
            "还请随时与我们联系。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE0")

    Jump("loc_106E")

    label("loc_DE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F14")

    #C0022
    ChrTalk(
        0x9,
        "啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0023
    ChrTalk(
        0x9,
        (
            "……不好意思。\x01",
            "你们不就是《克洛斯贝尔时代周刊》\x01",
            "最近报道过的……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x9,
        (
            "今天是来处理\x01",
            "委托的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        (
            "要找库瓦特罗先生的话，\x01",
            "他就在楼上左边的\x01",
            "安检室前等着呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_F6F")

    label("loc_F14")


    #C0026
    ChrTalk(
        0x9,
        (
            "今天是来处理\x01",
            "委托的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        (
            "要找库瓦特罗先生的话，\x01",
            "他就在楼上左边的\x01",
            "安检室前等着呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F6F")

    Jump("loc_106E")

    label("loc_F74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1002")

    #C0028
    ChrTalk(
        0x9,
        (
            "开往由警备队驻守的东西国境门方向的\x01",
            "货物列车，也是从本站发车的。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x9,
        (
            "由于可以直接运输物资，\x01",
            "所以警备队十分仰赖这里呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_106E")

    label("loc_1002")


    #C0030
    ChrTalk(
        0x9,
        (
            "开往由警备队驻守的东西国境门方向的\x01",
            "货物列车，也是从本站发车的。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        (
            "普通乘客不能乘坐，\x01",
            "还请多加注意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_106E")

    Jump("loc_AA1")

    label("loc_1073")

    TalkEnd(0x9)
    Return()

    # Function_8_A94 end

    def Function_9_1077(): pass

    label("Function_9_1077")

    Call(0, 10)
    Return()

    # Function_9_1077 end

    def Function_10_107B(): pass

    label("Function_10_107B")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1137")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10DE")

    #C0032
    ChrTalk(
        0xA,
        "哎呀……您在赶时间吗？\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xA,
        (
            "请不要在站台上奔走，\x01",
            "那样很危险哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1132")

    label("loc_10DE")


    #C0034
    ChrTalk(
        0xA,
        "最近不太平的事情真多。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xA,
        (
            "希望乘客们能在\x01",
            "注意安全的前提下\x01",
            "享受旅途的乐趣哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1132")

    Jump("loc_121B")

    label("loc_1137")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1189")

    #C0036
    ChrTalk(
        0xA,
        (
            "列车内也出售\x01",
            "饮料和食品。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xA,
        (
            "在长途旅行时，\x01",
            "请多多利用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_121B")

    label("loc_1189")


    #C0038
    ChrTalk(
        0xA,
        (
            "在本站乘车的商务人士中，\x01",
            "有不少人每天都往返于\x01",
            "帝国和共和国之间。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xA,
        (
            "每当想到是这些人\x01",
            "支撑着克洛斯贝尔的经济发展，\x01",
            "就对他们充满了钦佩之意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121B")

    TalkEnd(0xA)
    Return()

    # Function_10_107B end

    def Function_11_121F(): pass

    label("Function_11_121F")

    Call(0, 12)
    Return()

    # Function_11_121F end

    def Function_12_1223(): pass

    label("Function_12_1223")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_13B2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1331")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FA")

    #C0040
    ChrTalk(
        0xB,
        (
            "啊……不好意思，\x01",
            "请稍等片刻。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "……乘客们请注意。\x02\x03",

            "当听到列车发车的警铃后，\x01",
            "请退至安全线后。\x02\x03",

            "有列车驶过时，\x01",
            "请勿探出身体，\x01",
            "谢谢合作。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_132C")

    label("loc_12FA")


    #C0042
    ChrTalk(
        0xB,
        (
            "那个……\x01",
            "总之很危险，\x01",
            "请不要把身子探出去哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_132C")

    Jump("loc_13AD")

    label("loc_1331")


    #C0043
    ChrTalk(
        0xB,
        (
            "我本来是个内向的人，\x01",
            "但自从当上广播员之后，\x01",
            "就变得口齿伶俐了。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xB,
        (
            "嘻嘻……\x01",
            "能在适合自己的岗位上工作，\x01",
            "实在是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13AD")

    Jump("loc_15F8")

    label("loc_13B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_144D")

    #C0045
    ChrTalk(
        0xB,
        (
            "感谢您\x01",
            "今天光临\x01",
            "克洛斯贝尔车站。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xB,
        (
            "除了出售车票，\x01",
            "本站也提供其它指南服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xB,
        (
            "如有不明白的地方，\x01",
            "请尽管前来咨询。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_14AE")

    label("loc_144D")


    #C0048
    ChrTalk(
        0xB,
        (
            "我还担任\x01",
            "站内的广播员。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xB,
        (
            "有关乘坐列车方面的事情，\x01",
            "如果有不明白的地方，\x01",
            "请尽管前来咨询。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14AE")

    Jump("loc_15F8")

    label("loc_14B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1596")

    #C0050
    ChrTalk(
        0xB,
        (
            "啊……不好意思，\x01",
            "请稍等片刻。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0051
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "……乘客们请注意。\x02\x03",

            "１号站台停靠的列车开往共和国\x01",
            "方向，而２号站台停靠的列车则\x01",
            "开往帝国方向。\x02\x03",

            "３号站台是货车及特别列车的专用站台，\x01",
            "请勿入内，\x01",
            "谢谢配合。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_15F8")

    label("loc_1596")


    #C0052
    ChrTalk(
        0xB,
        (
            "３号线的列车都是专用列车，\x01",
            "一般人是不能乘坐的。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xB,
        (
            "警备队的特殊列车也在此停靠，\x01",
            "请勿入内。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F8")

    TalkEnd(0xB)
    Return()

    # Function_12_1223 end

    def Function_13_15FC(): pass

    label("Function_13_15FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_18F5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_174A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D8")
    OP_4B(0xD, 0xFF)

    #C0054
    ChrTalk(
        0xFE,
        (
            "负责对开往共和国的列车进行安检工作，\x01",
            "真是辛苦您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        "看样子，依旧很匆忙啊。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xD,
        (
            "呵呵，这不算什么……\x01",
            "和纪念庆典时期的繁忙相比的话，\x01",
            "这种程度根本就不值一提吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 4)
    Jump("loc_1745")

    label("loc_16D8")


    #C0057
    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "刚才看到的那位小姐……\x01",
            "感觉有些奇怪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "明明看起来像是个有钱人，\x01",
            "可身边却连个随从都没有。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1745")

    Jump("loc_18F0")

    label("loc_174A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175C")
    Call(0, 14)
    Jump("loc_18F0")

    label("loc_175C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1865")

    #C0059
    ChrTalk(
        0xFE,
        (
            "纪念庆典的时候虽然很忙，\x01",
            "不过也有不少有趣的乘客。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "有个看上去就像是个\x01",
            "花花公子的男人，\x01",
            "居然敢戏耍库瓦特罗先生呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "虽然库瓦特罗先生大发雷霆，\x01",
            "不过作为旁观者，我倒是乐在其中啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#0000F（我们认识一个似乎\x01",
            "  会做出这种事的人呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_18F0")

    label("loc_1865")


    #C0063
    ChrTalk(
        0xFE,
        (
            "纪念庆典的时候虽然很忙，\x01",
            "不过也有不少有趣的乘客。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "看那个红头发的花花公子\x01",
            "戏耍库瓦特罗先生的样子，\x01",
            "作为旁观者，倒真是乐在其中啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18F0")

    Jump("loc_1B87")

    label("loc_18F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C4")

    #C0065
    ChrTalk(
        0xFE,
        (
            "每天都有很多人从共和国和帝国\x01",
            "造访克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "正是由于他们的到来，\x01",
            "克洛斯贝尔市才会有如今这种\x01",
            "各国文化融汇交织的街道风景。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "……克洛斯贝尔市原本\x01",
            "又是什么样的呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1A3F")

    label("loc_19C4")


    #C0068
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市融汇了各种文化的\x01",
            "街道风景，\x01",
            "正是受共和国和帝国的影响而形成的。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "……克洛斯贝尔市原本\x01",
            "又是什么样的呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A3F")

    Jump("loc_1B87")

    label("loc_1A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B02")

    #C0070
    ChrTalk(
        0xFE,
        (
            "我已经在这里\x01",
            "工作了五年左右啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "一开始还想记住\x01",
            "所有乘客的样子，\x01",
            "不过，在很久以前就完全放弃了。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "即便是不可能的事情，也坚信可以做到，\x01",
            "这就是所谓的青春热血啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1B87")

    label("loc_1B02")


    #C0073
    ChrTalk(
        0xFE,
        (
            "一开始还想记住\x01",
            "所有乘客的样子，\x01",
            "不过在很久以前就完全放弃了。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "即便是不可能的事情，也坚信可以做到，\x01",
            "这就是所谓的青春热血啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B87")

    TalkEnd(0xFE)
    Return()

    # Function_13_15FC end

    def Function_14_1B8B(): pass

    label("Function_14_1B8B")


    #C0075
    ChrTalk(
        0xFE,
        (
            "刚才还以为你们\x01",
            "是要去共和国那边呢……\x01",
            "你们是频繁外出旅行的人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "如果习惯了乘坐列车，\x01",
            "在路途中，大概经常会觉得无聊吧。\x01",
            "在这种时候，看书是个不错的选择。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "对了，这本书我已经看完了，\x01",
            "不嫌弃的话，就送给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0078
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '黑市医生格伦　13卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('黑市医生格伦　13卷', 1)
    SetScenarioFlags(0x9D, 4)
    Return()

    # Function_14_1B8B end

    def Function_15_1CB4(): pass

    label("Function_15_1CB4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1F7C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D65")
    OP_4B(0xC, 0xFF)

    #C0079
    ChrTalk(
        0xFE,
        (
            "接下来，就稍微休息一下，\x01",
            "然后对开往帝国的列车进行安检。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "不过可不能\x01",
            "休息过头，\x01",
            "太过松懈了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xC,
        "（依旧是个认真尽责的人呢……）\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    Jump("loc_1F77")

    label("loc_1D65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EBD")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0082
    ChrTalk(
        0xFE,
        "哦，你们是特别任务支援科的……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#0000F安检官先生，\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "之前真是承蒙各位的帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "我现在正要去\x01",
            "２号站台进行安检……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "你们好像去了\x01",
            "一趟共和国吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#0006F这个，算是吧。\x01",
            "这也是工作的一环……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "嗯……不错不错。\x01",
            "你们工作得似乎很努力，\x01",
            "这就最好不过了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1F0F")

    label("loc_1EBD")


    #C0089
    ChrTalk(
        0xFE,
        (
            "你们工作得似乎很努力，\x01",
            "这就最好不过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "你们好像也很忙啊，\x01",
            "努力加油吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F0F")

    Jump("loc_1F77")

    label("loc_1F14")


    #C0091
    ChrTalk(
        0xFE,
        (
            "我现在正要去\x01",
            "２号站台进行安检。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "对前往帝国的入境者\x01",
            "进行仔细的检查，\x01",
            "这是必不可少的工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F77")

    Jump("loc_1FCF")

    label("loc_1F7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F8D")
    Jump("loc_1FCF")

    label("loc_1F8D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_1FA2")
    Call(0, 30)
    Jump("loc_1FCF")

    label("loc_1FA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1FB6")
    Call(0, 29)
    Jump("loc_1FCF")

    label("loc_1FB6")


    #C0093
    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "还没来吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FCF")

    TalkEnd(0xFE)
    Return()

    # Function_15_1CB4 end

    def Function_16_1FD3(): pass

    label("Function_16_1FD3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_22F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_225E")
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xE, 0x0, 0)
    TurnDirection(0xF, 0x0, 0)

    #C0094
    ChrTalk(
        0xE,
        (
            "哎呀，你们是……\x01",
            "那群小警察们，没错吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 7)), scpexpr(EXPR_END)), "loc_2056")

    #C0095
    ChrTalk(
        0x101,
        "#0005F啊，两位辛苦了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_20A3")

    label("loc_2056")


    #C0096
    ChrTalk(
        0x101,
        (
            "#0005F啊，两位辛苦了。\x02\x03",

            "#0003F（是游击士斯克特先生\x01",
            "  和温蔡尔先生吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A3")


    #C0097
    ChrTalk(
        0x102,
        "#0100F你们两位刚工作回来吗？\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xF,
        "嗯，刚从帝国那里回来。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xF,
        "话说，你们在干什么呢？\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x104,
        (
            "#0300F在处理\x01",
            "一项支援请求。\x02\x03",

            "就是帮忙进行安检啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xE,
        (
            "嘿……\x01",
            "这倒是很意外，竟然把这么\x01",
            "责任重大的工作交给你们了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xE,
        "哈，总之就保持这种势头，继续加油吧。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xF,
        (
            "……只要别妨碍我们的\x01",
            "正常工作就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x103,
        (
            "#0200F（……看上去，似乎还没有\x01",
            "  完全认同我们啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#0006F（哈，这也没办法啊。\x01",
            "  一步一步慢慢来吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x0)
    OP_93(0xF, 0x0, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 7)
    Jump("loc_22F3")

    label("loc_225E")


    #C0106
    ChrTalk(
        0xFE,
        (
            "你们已经见到\x01",
            "艾丝蒂尔和约修亚了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "他们年纪轻轻的，\x01",
            "却已经如此了不起了。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "他们的年龄好像和你们差不多吧？\x01",
            "哈哈，凡事总会被拿来比较啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22F3")

    TalkEnd(0xFE)
    Return()

    # Function_16_1FD3 end

    def Function_17_22F7(): pass

    label("Function_17_22F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_23D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2315")
    Call(0, 16)
    Jump("loc_23D7")

    label("loc_2315")


    #C0109
    ChrTalk(
        0xFE,
        (
            "安检吗……\x01",
            "以游击士的立场来说，\x01",
            "确实比较难以参与。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "能完成我们不能做到的工作，\x01",
            "算是帮了大忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "剩下的就是要多加注意，\x01",
            "别妨碍到我们的工作就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x103,
        "#0200F（真是趾高气扬啊……）\x02",
    )

    CloseMessageWindow()

    label("loc_23D7")

    TalkEnd(0xFE)
    Return()

    # Function_17_22F7 end

    def Function_18_23DB(): pass

    label("Function_18_23DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_27B9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244F")

    #C0113
    ChrTalk(
        0xFE,
        (
            "有关这次的黑手党事件，\x01",
            "现在已经着手开始调查了。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "……你们似乎正在\x01",
            "赶时间啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27B9")

    label("loc_244F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_271E")
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    TurnDirection(0x10, 0x0, 0)
    TurnDirection(0x11, 0x0, 0)

    #C0115
    ChrTalk(
        0x10,
        (
            "……你们好像是从共和国方向的\x01",
            "站台中出来的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x11,
        (
            "要当天往返于国外，\x01",
            "你们也真是够忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#0012F哈、哈哈……\x01",
            "没办法，正好接到了\x01",
            "相关的支援请求……\x02\x03",

            "#0001F……话说回来，\x01",
            "之前那次袭击事件的调查工作，\x01",
            "进展得如何了？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x10,
        "……嗯，那件事情啊。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x10,
        (
            "前不久，好像有些危险的\x01",
            "东西从帝国那边\x01",
            "被走私了过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x102,
        "#0105F危险的东西……？\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x11,
        (
            "就是昨天的袭击事件中使用的\x01",
            "莱恩福尔特公司制造的重型机关枪。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x11,
        (
            "鲁巴彻商会似乎在很久以前\x01",
            "就做好了周密的准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x104,
        "#0301F是那个重型机关枪啊……\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x103,
        (
            "#0203F虽然进行了周密准备，\x01",
            "结果却被黑月\x01",
            "打退了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x10,
        (
            "嗯，是这样的。\x01",
            "昨晚的那场袭击事件，\x01",
            "总觉得手段过于草率。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x10,
        (
            "而且还有种不大协调的感觉，\x01",
            "必须要仔细进行调查啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0xB4, 0x0)
    OP_93(0x11, 0x0, 0x0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    SetScenarioFlags(0x1, 0)
    Jump("loc_27B9")

    label("loc_271E")


    #C0127
    ChrTalk(
        0xFE,
        (
            "话说回来，虽然从帝国进入\x01",
            "克洛斯贝尔的装载货物\x01",
            "无需进行安检……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "但是，难道就不能实行\x01",
            "稍微严格一些的取缔措施吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        "#0006F（这话真是刺耳啊……）\x02",
    )

    CloseMessageWindow()

    label("loc_27B9")

    TalkEnd(0xFE)
    Return()

    # Function_18_23DB end

    def Function_19_27BD(): pass

    label("Function_19_27BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_2934")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2897")

    #C0130
    ChrTalk(
        0xFE,
        (
            "从今天起，我要和温蔡尔他们\x01",
            "分头行动，开始进行调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "如果你们知道了什么情况，\x01",
            "也请通知我们一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#0003F（关于那个药物的情报……\x01",
            "  目前尚未得到确认，\x01",
            "  暂时还是不说为好吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2934")

    label("loc_2897")


    #C0133
    ChrTalk(
        0xFE,
        (
            "话说回来，莱恩福尔特公司\x01",
            "制造的重型机关枪吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "那可是连警备队都还没有配备的\x01",
            "强力装备，竟然能弄到这种东西，\x01",
            "鲁巴彻商会还真是让人觉得有些毛骨悚然。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2934")

    TalkEnd(0xFE)
    Return()

    # Function_19_27BD end

    def Function_20_2938(): pass

    label("Function_20_2938")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_29CC")
    Jump("loc_2A16")

    label("loc_29CC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29EC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A16")

    label("loc_29EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A0C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A16")

    label("loc_2A0C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A16")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AD0")

    #C0135
    ChrTalk(
        0xFE,
        (
            "哈哈……从帝国乘坐列车而来，\x01",
            "这也是一件相当优雅的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "虽说也曾乘坐飞行船\x01",
            "去过雷米菲利亚一带，\x01",
            "不过，乘坐列车也不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B1E")

    label("loc_2AD0")


    #C0137
    ChrTalk(
        0xFE,
        (
            "呵呵……今天会带你去个\x01",
            "美妙的地方哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "去米修拉姆的\x01",
            "高级西餐厅如何？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B1E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_2938 end

    def Function_21_2B26(): pass

    label("Function_21_2B26")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2BBA")
    Jump("loc_2C04")

    label("loc_2BBA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BDA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C04")

    label("loc_2BDA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BFA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C04")

    label("loc_2BFA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C04")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CB8")

    #C0139
    ChrTalk(
        0xFE,
        "我更喜欢飞行船呢。\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        "不过，飞行船的班次比列车要少哦。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "从帝国飞往克洛斯贝尔的飞行船，\x01",
            "要是再多加些班次就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CE3")

    label("loc_2CB8")


    #C0142
    ChrTalk(
        0xFE,
        (
            "我这个男朋友啊，\x01",
            "做事情总是很老套……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CE3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_2B26 end

    def Function_22_2CEB(): pass

    label("Function_22_2CEB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D7F")
    Jump("loc_2DC9")

    label("loc_2D7F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D9F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2DC9")

    label("loc_2D9F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2DBF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2DC9")

    label("loc_2DBF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2DC9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E5F")

    #C0143
    ChrTalk(
        0xFE,
        (
            "我是从共和国\x01",
            "搭乘列车过来的，\x01",
            "但却把车票弄丢了……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "唉，不知道站员\x01",
            "能不能通融一下……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC7")

    label("loc_2E5F")


    #C0145
    ChrTalk(
        0xFE,
        (
            "本以为把车票丢了，\x01",
            "结果居然夹在座位的缝隙里。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "呼，太好啦～\x01",
            "这下就能放心地进入克洛斯贝尔啦～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_2CEB end

    def Function_23_2ECF(): pass

    label("Function_23_2ECF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F5D")

    #C0147
    ChrTalk(
        0xFE,
        (
            "在共和国，好像有种温泉\x01",
            "可以有效地治疗各种腰痛呢，\x01",
            "所以我正准备去那里看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "这就是所谓的温泉疗法，\x01",
            "真是期待啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F8C")

    label("loc_2F5D")


    #C0149
    ChrTalk(
        0xFE,
        (
            "那么，开往共和国的\x01",
            "下一班列车几点发车呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F8C")

    TalkEnd(0xFE)
    Return()

    # Function_23_2ECF end

    def Function_24_2F90(): pass

    label("Function_24_2F90")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3058")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_300A")

    #C0150
    ChrTalk(
        0xFE,
        (
            "我打算去共和国的\x01",
            "东方人街。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "想先去《牌技师杰克》这本小说的\x01",
            "故事舞台看一看呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3053")

    label("loc_300A")


    #C0152
    ChrTalk(
        0xFE,
        (
            "这班列车发车之后，下一班列车\x01",
            "就是我要乘坐的了。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        "哇，好兴奋啊！\x02",
    )

    CloseMessageWindow()

    label("loc_3053")

    Jump("loc_30C4")

    label("loc_3058")


    #C0154
    ChrTalk(
        0xFE,
        (
            "共和国的东方人街，\x01",
            "治安方面没问题吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "要是像杰克的世界那样，\x01",
            "到处都是地痞流氓，那可怎么办啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30C4")

    TalkEnd(0xFE)
    Return()

    # Function_24_2F90 end

    def Function_25_30C8(): pass

    label("Function_25_30C8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_315C")
    Jump("loc_31A6")

    label("loc_315C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_317C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31A6")

    label("loc_317C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_319C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31A6")

    label("loc_319C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31A6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3253")

    #C0156
    ChrTalk(
        0xFE,
        (
            "被男友甩了呢……\x01",
            "从现在开始我的伤心之旅。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        "……但我不会气馁的。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "因为在国外一定能\x01",
            "找到更加英俊的人……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32C0")

    label("loc_3253")


    #C0159
    ChrTalk(
        0xFE,
        (
            "嗯，既然是伤心之旅，\x01",
            "该选择帝国，还是共和国呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "总之一定要选择\x01",
            "帅哥多的地方……\x01",
            "真有点难以取舍啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32C0")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_30C8 end

    def Function_26_32C8(): pass

    label("Function_26_32C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_332B")

    #C0161
    ChrTalk(
        0xFE,
        (
            "爷爷，\x01",
            "终于到车站了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "虽然国外的工作应该会很辛苦，\x01",
            "但您要加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_335E")

    label("loc_332B")


    #C0163
    ChrTalk(
        0xFE,
        (
            "虽然要寂寞一阵子了……\x01",
            "但爷爷您一定要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_335E")

    TalkEnd(0xFE)
    Return()

    # Function_26_32C8 end

    def Function_27_3362(): pass

    label("Function_27_3362")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33E5")

    #C0164
    ChrTalk(
        0xFE,
        (
            "年轻时就职的帝国公司，\x01",
            "经常找我去做顾问。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "虽然工作十分辛苦……\x01",
            "不过拜此所赐，年老以后倒也不会无聊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3440")

    label("loc_33E5")


    #C0166
    ChrTalk(
        0xFE,
        (
            "开往帝国的列车\x01",
            "快要发车了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "虽然有些恋恋不舍，\x01",
            "不过还是回到站台，\x01",
            "等待发车吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3440")

    TalkEnd(0xFE)
    Return()

    # Function_27_3362 end

    def Function_28_3444(): pass

    label("Function_28_3444")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(5300, 1500, 6460, 0)
    MoveCamera(44, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 2500, 0, -500, 90)
    SetChrPos(0x102, 2250, 0, 500, 90)
    SetChrPos(0x103, 1000, 0, -500, 90)
    SetChrPos(0x104, 750, 0, 500, 90)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    OP_68(6300, 1500, 6460, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3900)
    Fade(500)
    OP_68(29620, 5500, -8119, 0)
    MoveCamera(42, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_68(29590, 5500, 9120, 7000)
    Sleep(6900)
    Fade(500)
    OP_68(12760, 3000, -8000, 0)
    MoveCamera(48, 8, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    OP_68(5320, 1530, 440, 5000)
    Sleep(5000)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3671")

    #C0168
    ChrTalk(
        0x103,
        (
            "#5P#0200F克洛斯贝尔车站……\x01",
            "议员的千金\x01",
            "应该来了这里才对……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        (
            "#11P#0001F开往共和国的列车\x01",
            "应该在１号站台。\x01",
            "……赶快过去吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3713")

    label("loc_3671")


    #C0170
    ChrTalk(
        0x101,
        (
            "#11P#0005F……车站还是这么气派啊。\x02\x03",

            "#0004F都已经有一个月没来了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x102,
        (
            "#5P#0100F车站的安检官好像\x01",
            "提出了那项支援请求吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        "#11P#0000F那么，赶快去问问吧。\x02",
    )

    CloseMessageWindow()

    label("loc_3713")

    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    SetChrPos(0x0, 2500, 0, 0, 90)
    SetScenarioFlags(0x44, 3)
    EventEnd(0x5)
    Return()

    # Function_28_3444 end

    def Function_29_3748(): pass

    label("Function_29_3748")

    EventBegin(0x0)
    Fade(500)
    OP_68(27680, 5500, 8290, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17870, 0)
    SetChrPos(0x101, 28500, 4000, 8500, 0)
    SetChrPos(0x102, 27500, 4000, 8250, 0)
    SetChrPos(0x103, 28500, 4000, 7000, 0)
    SetChrPos(0x104, 27500, 4000, 6750, 0)
    SetChrSubChip(0xD, 0x0)
    OP_0D()

    #C0173
    ChrTalk(
        0xD,
        (
            "#5P嗯嗯……\x01",
            "还没来吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        (
            "#11P#0000F那个……请问……\x01",
            "您就是安检官先生吗？\x02\x03",

            "我们想来确认一下\x01",
            "支援请求的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xD,
        (
            "#5P这么说……\x01",
            "你们就是那个支援科的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xD,
        (
            "#5P我是埃雷波尼亚帝国\x01",
            "军部委派来的安检官\x01",
            "库瓦特罗。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xD,
        (
            "#5P那么，关于这件委托……\x01",
            "你们可以立刻接受吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x9, 0x1, 0x0)
    Call(0, 31)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38F7")
    Call(0, 32)
    Jump("loc_390A")

    label("loc_38F7")

    SetChrPos(0x0, 28000, 4000, 8500, 0)
    EventEnd(0x5)

    label("loc_390A")

    Return()

    # Function_29_3748 end

    def Function_30_390B(): pass

    label("Function_30_390B")

    EventBegin(0x0)
    Fade(500)
    OP_68(27680, 5500, 8290, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17870, 0)
    SetChrPos(0x101, 28500, 4000, 8500, 0)
    SetChrPos(0x102, 27500, 4000, 8250, 0)
    SetChrPos(0x103, 28500, 4000, 7000, 0)
    SetChrPos(0x104, 27500, 4000, 6750, 0)
    SetChrSubChip(0xD, 0x0)
    OP_0D()

    #C0178
    ChrTalk(
        0xD,
        "#5P嗯，你们……\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xD,
        (
            "#5P可以接受\x01",
            "这项委托吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 31)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39D6")
    Call(0, 32)
    Jump("loc_39E9")

    label("loc_39D6")

    SetChrPos(0x0, 28000, 4000, 8500, 0)
    EventEnd(0x5)

    label("loc_39E9")

    Return()

    # Function_30_390B end

    def Function_31_39EA(): pass

    label("Function_31_39EA")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A6B")

    #C0180
    ChrTalk(
        0x101,
        (
            "#11P#0000F嗯，没有问题。\x02\x03",

            "可以请您说明一下\x01",
            "工作内容吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B19")

    label("loc_3A6B")


    #C0181
    ChrTalk(
        0x101,
        (
            "#11P#0006F对不起，我们现在还有点\x01",
            "别的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xD,
        (
            "#5P……是吗，\x01",
            "那就没办法了……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xD,
        (
            "#5P那么，尽快把别的事情\x01",
            "处理好之后再来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xD,
        (
            "#5P我这边也很急的，\x01",
            "拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3B19")

    Return()

    # Function_31_39EA end

    def Function_32_3B1A(): pass

    label("Function_32_3B1A")


    #C0185
    ChrTalk(
        0xD,
        "#5P好吧。\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xD,
        "#5P……嗯……话说回来………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0187
    ChrTalk(
        0x101,
        "#11P#0005F请、请问……？\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xD,
        "#5P……没想到你们都这么年轻啊。\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xD,
        (
            "#5P唉，不过也没办法了。\x01",
            "总比谁都不来要好。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x104,
        (
            "#12P#0301F（这叫什么话嘛，这大叔……\x01",
            "  好像趾高气扬的。）\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xD,
        "#5P……你刚才说了什么吗？\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x103,
        (
            "#12P#0203F……请别介意。\x02\x03",

            "#0200F对了，您的请求是\x01",
            "『帮忙进行安检』，\x01",
            "没错吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xD,
        "#5P嗯……是的。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xD,
        (
            "#5P再过不久，开往帝国的列车\x01",
            "就要到站了。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xD,
        (
            "#5P希望你们帮忙\x01",
            "进行列车内的安检。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        (
            "#11P#0005F所谓的安检……\x02\x03",

            "#0000F也就是检查开往帝国的\x01",
            "列车中有没有可疑人物\x01",
            "和可疑物品吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xD,
        "#5P是的。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xD,
        (
            "#5P本来是有其他安检官的，\x01",
            "但很不巧，他们居然都接二连三地病倒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xD,
        (
            "#5P这次真的是无计可施了，\x01",
            "所以才决定找帮手过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x102,
        (
            "#12P#0100F……原来如此。\x01",
            "事情的大概，我们已经了解了。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xD,
        "#5P那就好。\x02",
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("站员的声音")

    #A0202
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……开往帝国的列车\x01",
            "即将到达２号站台。\x02",
        )
    )

    CloseMessageWindow()

    #A0203
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "需要搭乘的旅客，\x01",
            "请迅速前往站台。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(1000, 0)
    OP_0D()
    SetScenarioFlags(0x5C, 1)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_3B1A end

    def Function_33_3F13(): pass

    label("Function_33_3F13")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x1, 0x5, 0x5, 0x0, 0x0)
    OP_68(28050, 5500, 8960, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17870, 0)
    SetChrPos(0x101, 28500, 4000, 8500, 0)
    SetChrPos(0x102, 27500, 4000, 8250, 0)
    SetChrPos(0x103, 28500, 4000, 7000, 0)
    SetChrPos(0x104, 27500, 4000, 6750, 0)
    SetChrPos(0xD, 28000, 4000, 10000, 180)
    OP_4B(0xD, 0xFF)
    SetChrSubChip(0xD, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0204
    ChrTalk(
        0xD,
        "#5P……列车好像已经到了啊。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xD,
        (
            "#5P那么，我就立刻开始说明\x01",
            "２号站台的\x01",
            "工作内容吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xD,
        "#5P跟我过来。\x02",
    )

    CloseMessageWindow()
    OP_97(0xD, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)

    def lambda_4044():
        OP_93(0x101, 0xFF79, 0x96)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4044)

    def lambda_4051():
        OP_93(0x102, 0xFF79, 0x96)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4051)

    def lambda_405E():
        OP_93(0x103, 0xFF79, 0x96)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_405E)

    def lambda_406B():
        OP_93(0x104, 0xFF79, 0x96)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_406B)
    OP_97(0xD, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
    Fade(500)
    SetChrPos(0xD, 18000, 0, -8000, 90)
    SetChrFlags(0xD, 0x8000)
    OP_68(19030, 1500, -9110, 0)
    MoveCamera(29, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    OP_68(20030, 1500, -9110, 3000)
    OP_97(0xD, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
    ClearChrFlags(0xD, 0x8000)
    OP_0D()
    Fade(500)
    OP_68(27830, 5500, 7060, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17870, 0)
    OP_0D()

    #C0207
    ChrTalk(
        0x101,
        (
            "#5P#0006F嗯……\x01",
            "居然会接到\x01",
            "这样的工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x104,
        (
            "#12P#0303F虽然不喜欢他那种盛气凌人的样子……\x02\x03",

            "#0300F不过，看样子，他是真的遇到困难了，\x01",
            "也只能帮帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x102,
        "#6P#0100F那么，我们快点去站台吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0210
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找代理安检官】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 28000, 4000, 8500, 180)
    OP_71(0x1, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x10)
    OP_1B(0x0, 0x0, 0x22)
    OP_29(0x9, 0x1, 0x1)
    OP_4C(0xD, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_33_3F13 end

    def Function_34_427C(): pass

    label("Function_34_427C")

    EventBegin(0x1)

    #C0211
    ChrTalk(
        0x101,
        (
            "#0000F安检官先生在２号站台\x01",
            "等着我们。\x02\x03",

            "最好快点过去。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 500, 0, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_34_427C end

    def Function_35_42D0(): pass

    label("Function_35_42D0")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0212
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "←开往共和国方向·１号线站台\x01",
            "　　　共和国阿尔泰尔市　３５分钟\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_35_42D0 end

    def Function_36_4346(): pass

    label("Function_36_4346")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0213
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "开往帝国方向·２号线站台→\x01",
            "　　　　帝国卡雷利亚要塞　　３２分钟\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_36_4346 end

    def Function_37_43BE(): pass

    label("Function_37_43BE")

    TalkBegin(0xFF)
    SetChrName("")

    #A0214
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "贴有驶向克洛斯贝尔自治州\x01",
            "周边地区的列车时刻表。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_37_43BE end

    def Function_38_4401(): pass

    label("Function_38_4401")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0215
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※※　安检官办公室　※※\x01",
            " 　　　非工作人员\x01",
            "     　 严禁入内。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_38_4401 end

    def Function_39_4477(): pass

    label("Function_39_4477")

    TalkBegin(0xFF)
    SetChrName("")

    #A0216
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "贴有克洛斯贝尔自治州\x01",
            "周边地区的线路图。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_39_4477 end

    SaveToFile()

Try(main)
