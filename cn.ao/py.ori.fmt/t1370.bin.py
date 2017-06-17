from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1370.bin",                # FileName
        "t1370",                    # MapName
        "t1370",                    # Location
        0x00B9,                     # MapIndex
        "ed7160",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 185, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1370",                  # 0
        "兰迪",                   # 1
        "诺艾尔",                 # 2
        "瓦吉",                   # 3
        "琪雅",                   # 4
        "蔡特",                   # 5
        "塞茜尔",                 # 6
        "伊莉娅",                 # 7
        "莉夏",                   # 8
        "修利",                   # 9
        "咪雪",                   # 10
        "梅尔斯",                 # 11
        "柯洛娜",                 # 12
        "利玛",                   # 13
        "奇幻乐园工作人员",       # 14
        "游客",                   # 15
        "游客",                   # 16
        "游客",                   # 17
        "游客",                   # 18
        "游客",                   # 19
        "游客",                   # 20
        "游客",                   # 21
        "职员亨克斯",             # 22
        "奇幻乐园入口广场方向",   # 23
    ))

    AddCharChip((
        "chr/ch00302.itc",                   # 00
        "chr/ch02902.itc",                   # 01
        "chr/ch03002.itc",                   # 02
        "chr/ch08200.itc",                   # 03
        "chr/ch02707.itc",                   # 04
        "chr/ch07502.itc",                   # 05
        "chr/ch05102.itc",                   # 06
        "chr/ch05202.itc",                   # 07
        "chr/ch10100.itc",                   # 08
        "chr/ch45400.itc",                   # 09
        "chr/ch26202.itc",                   # 0A
        "chr/ch22702.itc",                   # 0B
        "chr/ch20702.itc",                   # 0C
        "chr/ch44600.itc",                   # 0D
        "chr/ch23500.itc",                   # 0E
        "chr/ch23800.itc",                   # 0F
        "chr/ch23900.itc",                   # 10
        "chr/ch33102.itc",                   # 11
        "chr/ch34302.itc",                   # 12
        "chr/ch21602.itc",                   # 13
        "chr/ch21702.itc",                   # 14
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

    DeclNpc(-2750,   200,     13850,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-2750,   200,     10949,   0,    389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-4250,   200,     12250,   90,   389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(769,     0,       8899,    0,    389,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(270,     0,       10720,   225,  389,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-1250,   200,     12250,   270,  389,  0x0, 0,   5,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-1250,   200,     12250,   270,  389,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-4250,   200,     12250,   90,   389,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-230,    0,       8899,    0,    389,  0x0, 0,   8,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(18000,   0,       -469,    90,   389,  0x0, 0,   9,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-8600,   200,     2400,    270,  389,  0x0, 0,   10,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-10100,  200,     3900,    180,  389,  0x0, 0,   11,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-11600,  200,     2400,    90,   389,  0x0, 0,   12,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(17700,   0,       4750,    270,  389,  0x0, 0,   13,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(10250,   0,       7349,    180,  389,  0x0, 0,   14,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(10750,   0,       6250,    270,  389,  0x0, 0,   15,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(9750,    0,       6250,    90,   389,  0x0, 0,   16,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-250,    200,     899,     0,    389,  0x0, 0,   17,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-250,    200,     3900,    180,  389,  0x0, 0,   18,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-17100,  200,     2400,    270,  389,  0x0, 0,   19,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-20100,  200,     2400,    90,   389,  0x0, 0,   20,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(16700,   0,       4750,    1000,    17700,   1500,    4750,    0x007E, 0,  18, 0x0000)
    DeclActor(-22000,  500,     9250,    1200,    -22000,  750,     9250,    0x007C, 0,  3,  0x0000)
    DeclActor(15870,   0,       -630,    1200,    18000,   1500,    -470,    0x007C, 0,  13, 0x0000)
    DeclActor(8450,    0,       9280,    1200,    8450,    2000,    9280,    0x007C, 0,  34, 0x0000)

    PlaceName(10.0, 0.0, -45.0, 0x0000, 0x0000, "奇幻乐园入口广场方向")
    PlaceName(17.68000030517578, 0.0, 4.739999771118164, 0x0000, 0x0053, "")

    ChipFrameInfo(1208, 0)                                       # 0

    ScpFunction((
        "Function_0_4B8",          # 00, 0
        "Function_1_570",          # 01, 1
        "Function_2_5FC",          # 02, 2
        "Function_3_715",          # 03, 3
        "Function_4_7BC",          # 04, 4
        "Function_5_93A",          # 05, 5
        "Function_6_A6F",          # 06, 6
        "Function_7_C78",          # 07, 7
        "Function_8_D22",          # 08, 8
        "Function_9_E31",          # 09, 9
        "Function_10_1045",        # 0A, 10
        "Function_11_11C7",        # 0B, 11
        "Function_12_1278",        # 0C, 12
        "Function_13_132F",        # 0D, 13
        "Function_14_1333",        # 0E, 14
        "Function_15_1337",        # 0F, 15
        "Function_16_13C5",        # 10, 16
        "Function_17_1460",        # 11, 17
        "Function_18_14E6",        # 12, 18
        "Function_19_14EA",        # 13, 19
        "Function_20_163C",        # 14, 20
        "Function_21_16B2",        # 15, 21
        "Function_22_1712",        # 16, 22
        "Function_23_1781",        # 17, 23
        "Function_24_1814",        # 18, 24
        "Function_25_1885",        # 19, 25
        "Function_26_1924",        # 1A, 26
        "Function_27_19A0",        # 1B, 27
        "Function_28_1A42",        # 1C, 28
        "Function_29_1CC1",        # 1D, 29
        "Function_30_221C",        # 1E, 30
        "Function_31_2335",        # 1F, 31
        "Function_32_24BC",        # 20, 32
        "Function_33_3084",        # 21, 33
        "Function_34_364A",        # 22, 34
    ))


    def Function_0_4B8(): pass

    label("Function_0_4B8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4F8"),
        (1, "loc_504"),
        (2, "loc_510"),
        (3, "loc_51C"),
        (4, "loc_528"),
        (5, "loc_534"),
        (6, "loc_540"),
        (SWITCH_DEFAULT, "loc_54C"),
    )


    label("loc_4F8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_504")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_510")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_51C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_528")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_534")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_540")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_54C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_558")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_56F")

    Return()

    # Function_0_4B8 end

    def Function_1_570(): pass

    label("Function_1_570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_57E")
    Jump("loc_5EC")

    label("loc_57E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_58C")
    Jump("loc_5EC")

    label("loc_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_59A")
    Jump("loc_5EC")

    label("loc_59A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_5AB")
    Call(0, 28)
    Jump("loc_5EC")

    label("loc_5AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_5B9")
    Jump("loc_5EC")

    label("loc_5B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_5C7")
    Jump("loc_5EC")

    label("loc_5C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_5D5")
    Jump("loc_5EC")

    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_5E3")
    Jump("loc_5EC")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_5EC")

    label("loc_5EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_5FB")
    ClearScenarioFlags(0x22, 0)
    Event(0, 33)

    label("loc_5FB")

    Return()

    # Function_1_570 end

    def Function_2_5FC(): pass

    label("Function_2_5FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62F")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x78, 0x0)

    label("loc_62F")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_641")
    Jump("loc_6B0")

    label("loc_641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_64F")
    Jump("loc_6B0")

    label("loc_64F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_65D")
    Jump("loc_6B0")

    label("loc_65D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_66F")
    OP_66(0x0, 0x1)
    Jump("loc_6B0")

    label("loc_66F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_67D")
    Jump("loc_6B0")

    label("loc_67D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_68B")
    Jump("loc_6B0")

    label("loc_68B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_699")
    Jump("loc_6B0")

    label("loc_699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_6A7")
    Jump("loc_6B0")

    label("loc_6A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_6B0")

    label("loc_6B0")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D6")
    OP_66(0x2, 0x1)

    label("loc_6D6")

    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_END)), "loc_708")
    OP_24(0x335)
    Jump("loc_70E")

    label("loc_708")

    Sound(821, 1, 50, 0)

    label("loc_70E")

    Sound(126, 1, 80, 0)
    Return()

    # Function_2_5FC end

    def Function_3_715(): pass

    label("Function_3_715")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着《点心王国　第三卷》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_7B8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B8")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『七色棉花糖』\x07\x00",
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_7B8")

    TalkEnd(0xFF)
    Return()

    # Function_3_715 end

    def Function_4_7BC(): pass

    label("Function_4_7BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D5")
    Jump("loc_936")

    label("loc_7D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EB")
    Jump("loc_936")

    label("loc_7EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B1")

    #C0003
    ChrTalk(
        0x8,
        (
            "#00306F唔……我本想和\x01",
            "塞茜尔小姐一起\x01",
            "开心地喝茶呢。\x02\x03",

            "#00309F算了，就先用诺艾尔\x01",
            "凑和一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0004
    ChrTalk(
        0x9,
        "#10106F说、说得真过分啊，前辈……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_90A")

    label("loc_8B1")


    #C0005
    ChrTalk(
        0x8,
        (
            "#00306F我本想和\x01",
            "塞茜尔小姐一起\x01",
            "开心地喝茶呢。\x02\x03",

            "#00309F算了，就让诺艾尔\x01",
            "陪我坐坐吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90A")

    Jump("loc_936")

    label("loc_90F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_925")
    Jump("loc_936")

    label("loc_925")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_936")

    label("loc_936")

    TalkEnd(0xFE)
    Return()

    # Function_4_7BC end

    def Function_5_93A(): pass

    label("Function_5_93A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_953")
    Jump("loc_A6B")

    label("loc_953")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_969")
    Jump("loc_A6B")

    label("loc_969")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D8")

    #C0006
    ChrTalk(
        0x9,
        (
            "#10100F塞茜尔小姐\x01",
            "好像去玩了。\x02\x03",

            "#10109F呵呵，兰迪前辈，\x01",
            "真是不凑巧呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_A3F")

    label("loc_9D8")


    #C0007
    ChrTalk(
        0x9,
        (
            "#10105F话说回来……\x01",
            "蔡特是不是打算\x01",
            "一直在这里睡午觉啊？\x02\x03",

            "#10104F唔，去小卖部\x01",
            "给它买点东西吃吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3F")

    Jump("loc_A6B")

    label("loc_A44")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5A")
    Jump("loc_A6B")

    label("loc_A5A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6B")

    label("loc_A6B")

    TalkEnd(0xFE)
    Return()

    # Function_5_93A end

    def Function_6_A6F(): pass

    label("Function_6_A6F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A88")
    Jump("loc_C74")

    label("loc_A88")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9E")
    Jump("loc_C74")

    label("loc_A9E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB4")
    Jump("loc_C74")

    label("loc_AB4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACA")
    Jump("loc_C74")

    label("loc_ACA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C0A")

    #C0008
    ChrTalk(
        0x101,
        (
            "#00005F瓦吉，你在做什么？\x02\x03",

            "#00003F该不会是想对\x01",
            "塞茜尔姐出手吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xA,
        (
            "#10306F哎呀呀，不要对我\x01",
            "这么不信任嘛。\x02\x03",

            "#10302F虽然我工作的俱乐部\x01",
            "也会有她这样的妙龄女子光顾……\x01",
            "但我今天正在休息，是不会对她出手的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0010
    ChrTalk(
        0x101,
        (
            "#00006F正是因为这样，\x01",
            "所以才信不过你啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_C74")

    label("loc_C0A")


    #C0011
    ChrTalk(
        0xA,
        (
            "#10305F虽然我们店也会有塞茜尔小姐\x01",
            "这样的妙龄女子光顾……\x02\x03",

            "#10300F呵呵，但我不会对\x01",
            "你的好姐姐出手的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C74")

    TalkEnd(0xFE)
    Return()

    # Function_6_A6F end

    def Function_7_C78(): pass

    label("Function_7_C78")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C91")
    Jump("loc_D1E")

    label("loc_C91")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB4")
    Call(0, 27)
    Jump("loc_CDC")

    label("loc_CB4")


    #C0012
    ChrTalk(
        0xB,
        (
            "#01105F哎，但是蔡特\x01",
            "明明这么可爱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDC")

    Jump("loc_D1E")

    label("loc_CE1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF7")
    Jump("loc_D1E")

    label("loc_CF7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0D")
    Jump("loc_D1E")

    label("loc_D0D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1E")

    label("loc_D1E")

    TalkEnd(0xFE)
    Return()

    # Function_7_C78 end

    def Function_8_D22(): pass

    label("Function_8_D22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D58")

    #C0013
    ChrTalk(
        0xC,
        "#01200F咕噜噜噜……嗷。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E2D")

    label("loc_D58")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7B")
    Call(0, 27)
    Jump("loc_D90")

    label("loc_D7B")


    #C0014
    ChrTalk(
        0xC,
        "#01200F……嗷。\x02",
    )

    CloseMessageWindow()

    label("loc_D90")

    Jump("loc_E2D")

    label("loc_D95")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC8")

    #C0015
    ChrTalk(
        0xC,
        "#01200F……咕噜噜噜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_E2D")

    label("loc_DC8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFF")

    #C0016
    ChrTalk(
        0xC,
        "#01200F……咕噜噜噜……嗷。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E2D")

    label("loc_DFF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E2D")

    #C0017
    ChrTalk(
        0xC,
        "#01200F咕噜噜噜……嗷。\x02",
    )

    CloseMessageWindow()

    label("loc_E2D")

    TalkEnd(0xFE)
    Return()

    # Function_8_D22 end

    def Function_9_E31(): pass

    label("Function_9_E31")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAB")

    #C0018
    ChrTalk(
        0xD,
        (
            "#05900F我会尽量\x01",
            "待在这里的。\x02\x03",

            "#05909F呵呵，你们不用在意我，\x01",
            "要玩得尽兴一点哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_F09")

    label("loc_EAB")


    #C0019
    ChrTalk(
        0xD,
        (
            "#05904F我就和蔡特一起\x01",
            "悠闲地休息一下吧。\x02\x03",

            "#05909F呵呵，但你要是想邀请我，\x01",
            "我也会接受的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F09")

    Jump("loc_1041")

    label("loc_F0E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F24")
    Jump("loc_1041")

    label("loc_F24")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F3A")
    Jump("loc_1041")

    label("loc_F3A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F50")
    Jump("loc_1041")

    label("loc_F50")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1041")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FDE")

    #C0020
    ChrTalk(
        0xD,
        (
            "#05900F呵呵，白天的活动\x01",
            "快要结束了，\x01",
            "我就在这里等大家。\x02\x03",

            "#05904F罗伊德，你玩够了以后，\x01",
            "也先回这里吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1041")

    label("loc_FDE")


    #C0021
    ChrTalk(
        0xD,
        (
            "#05900F罗伊德，你玩够了以后，\x01",
            "也先回这里吧。\x02\x03",

            "#05909F呵呵，\x01",
            "但你要是想邀请我，\x01",
            "我也会接受的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1041")

    TalkEnd(0xFE)
    Return()

    # Function_9_E31 end

    def Function_10_1045(): pass

    label("Function_10_1045")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105E")
    Jump("loc_11C3")

    label("loc_105E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1074")
    Jump("loc_11C3")

    label("loc_1074")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_108A")
    Jump("loc_11C3")

    label("loc_108A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_115D")

    #C0022
    ChrTalk(
        0xE,
        (
            "#01700F这孩子是叫做蔡特吧？\x01",
            "它这么乖，\x01",
            "肯定很聪明吧。\x02\x03",

            "#01704F克洛斯贝尔时代周刊\x01",
            "以前好像也介绍过它……\x01",
            "说不定有当明星的潜质呢。\x02\x03",

            "#01709F呵呵，要不要\x01",
            "把它挖到彩虹剧团呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_11AD")

    label("loc_115D")


    #C0023
    ChrTalk(
        0xE,
        (
            "#01704F蔡特很有\x01",
            "当明星的潜质呢。\x02\x03",

            "#01709F呵呵，要不要\x01",
            "把它挖到彩虹剧团呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11AD")

    Jump("loc_11C3")

    label("loc_11B2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C3")

    label("loc_11C3")

    TalkEnd(0xFE)
    Return()

    # Function_10_1045 end

    def Function_11_11C7(): pass

    label("Function_11_11C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E0")
    Jump("loc_1274")

    label("loc_11E0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F6")
    Jump("loc_1274")

    label("loc_11F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120C")
    Jump("loc_1274")

    label("loc_120C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1263")

    #C0024
    ChrTalk(
        0xF,
        (
            "#01803F那家小卖部卖的\x01",
            "棉花糖很好吃哦。\x02\x03",

            "#01809F你尝过了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1274")

    label("loc_1263")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1274")

    label("loc_1274")

    TalkEnd(0xFE)
    Return()

    # Function_11_11C7 end

    def Function_12_1278(): pass

    label("Function_12_1278")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1291")
    Jump("loc_132B")

    label("loc_1291")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B4")
    Call(0, 27)
    Jump("loc_12E9")

    label("loc_12B4")


    #C0025
    ChrTalk(
        0x10,
        (
            "#14006F可爱也好，\x01",
            "帅气也好，\x01",
            "不行就是不行啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E9")

    Jump("loc_132B")

    label("loc_12EE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1304")
    Jump("loc_132B")

    label("loc_1304")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131A")
    Jump("loc_132B")

    label("loc_131A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_132B")

    label("loc_132B")

    TalkEnd(0xFE)
    Return()

    # Function_12_1278 end

    def Function_13_132F(): pass

    label("Function_13_132F")

    Call(0, 29)
    Return()

    # Function_13_132F end

    def Function_14_1333(): pass

    label("Function_14_1333")

    Call(0, 30)
    Return()

    # Function_14_1333 end

    def Function_15_1337(): pass

    label("Function_15_1337")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_136E")

    #C0026
    ChrTalk(
        0x12,
        "好，接下来要去玩什么呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_13C1")

    label("loc_136E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1384")
    Jump("loc_13C1")

    label("loc_1384")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139A")
    Jump("loc_13C1")

    label("loc_139A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B0")
    Jump("loc_13C1")

    label("loc_13B0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C1")

    label("loc_13C1")

    TalkEnd(0xFE)
    Return()

    # Function_15_1337 end

    def Function_16_13C5(): pass

    label("Function_16_13C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1409")

    #C0027
    ChrTalk(
        0x13,
        (
            "呵呵，好啊。\x01",
            "我们就去高处放松一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_145C")

    label("loc_1409")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_141F")
    Jump("loc_145C")

    label("loc_141F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1435")
    Jump("loc_145C")

    label("loc_1435")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144B")
    Jump("loc_145C")

    label("loc_144B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145C")

    label("loc_145C")

    TalkEnd(0xFE)
    Return()

    # Function_16_13C5 end

    def Function_17_1460(): pass

    label("Function_17_1460")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148F")

    #C0028
    ChrTalk(
        0x14,
        "利玛想坐摩天轮！\x02",
    )

    CloseMessageWindow()
    Jump("loc_14E2")

    label("loc_148F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A5")
    Jump("loc_14E2")

    label("loc_14A5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14BB")
    Jump("loc_14E2")

    label("loc_14BB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D1")
    Jump("loc_14E2")

    label("loc_14D1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E2")

    label("loc_14E2")

    TalkEnd(0xFE)
    Return()

    # Function_17_1460 end

    def Function_18_14E6(): pass

    label("Function_18_14E6")

    Call(0, 19)
    Return()

    # Function_18_14E6 end

    def Function_19_14EA(): pass

    label("Function_19_14EA")

    TalkBegin(0x15)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1638")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1547")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1547")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1567")
    OP_AF(0x6B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1633")

    label("loc_1567")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_157B")
    Jump("loc_1633")

    label("loc_157B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1593")
    TalkEnd(0x15)
    Return()

    label("loc_1593")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1633")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15F6")

    #C0029
    ChrTalk(
        0x15,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x15,
        "要不要来一个好吃的棉花糖～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1633")

    label("loc_15F6")


    #C0031
    ChrTalk(
        0x15,
        (
            "肚子已经开始\x01",
            "咕咕叫了吧～？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x15,
        "来尝尝甜甜的棉花糖吧～\x02",
    )

    CloseMessageWindow()

    label("loc_1633")

    Jump("loc_14F7")

    label("loc_1638")

    TalkEnd(0x15)
    Return()

    # Function_19_14EA end

    def Function_20_163C(): pass

    label("Function_20_163C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_168C")

    #C0033
    ChrTalk(
        0x16,
        (
            "啊，真是的，难得来主题公园玩，\x01",
            "你们就不要吵架了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16AE")

    label("loc_168C")


    #C0034
    ChrTalk(
        0x16,
        "好啦好啦，这次就忍耐一下吧！\x02",
    )

    CloseMessageWindow()

    label("loc_16AE")

    TalkEnd(0xFE)
    Return()

    # Function_20_163C end

    def Function_21_16B2(): pass

    label("Function_21_16B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16EC")

    #C0035
    ChrTalk(
        0x17,
        (
            "嘿嘿，就吃一口\x01",
            "也没关系吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_170E")

    label("loc_16EC")


    #C0036
    ChrTalk(
        0x17,
        "现在就回去，未免也太早啦～！\x02",
    )

    CloseMessageWindow()

    label("loc_170E")

    TalkEnd(0xFE)
    Return()

    # Function_21_16B2 end

    def Function_22_1712(): pass

    label("Function_22_1712")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_174C")

    #C0037
    ChrTalk(
        0x18,
        (
            "哇！哥哥抢我的\x01",
            "棉花糖吃～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_177D")

    label("loc_174C")


    #C0038
    ChrTalk(
        0x18,
        (
            "哇——不要不要～！\x01",
            "晚上的巡游也一定要看～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_177D")

    TalkEnd(0xFE)
    Return()

    # Function_22_1712 end

    def Function_23_1781(): pass

    label("Function_23_1781")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17E0")

    #C0039
    ChrTalk(
        0x19,
        (
            "久等了，亲爱的，\x01",
            "我把果汁买来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x19,
        (
            "我们用情侣吸管\x01",
            "一起喝吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1810")

    label("loc_17E0")


    #C0041
    ChrTalk(
        0x19,
        "亲爱的，夕阳真美啊。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x19,
        "不过还是你更美。\x02",
    )

    CloseMessageWindow()

    label("loc_1810")

    TalkEnd(0xFE)
    Return()

    # Function_23_1781 end

    def Function_24_1814(): pass

    label("Function_24_1814")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1856")

    #C0043
    ChrTalk(
        0x1A,
        (
            "情侣吸管还是算了，\x01",
            "你去买两杯来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1881")

    label("loc_1856")


    #C0044
    ChrTalk(
        0x1A,
        (
            "这种话就不用说了，\x01",
            "我们也该回去了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1881")

    TalkEnd(0xFE)
    Return()

    # Function_24_1814 end

    def Function_25_1885(): pass

    label("Function_25_1885")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1920")

    #C0045
    ChrTalk(
        0x1B,
        (
            "米修拉姆原本是个宁静美丽的疗养地，\x01",
            "如今真是变化很大啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x1B,
        (
            "所有设施都是面向年轻人的，\x01",
            "真希望他们也替上了年纪的人考虑一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1920")

    label("loc_1920")

    TalkEnd(0xFE)
    Return()

    # Function_25_1885 end

    def Function_26_1924(): pass

    label("Function_26_1924")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_199C")

    #C0047
    ChrTalk(
        0x1C,
        (
            "呵呵，老伴虽然\x01",
            "嘴上那么说，\x01",
            "但心里其实很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x1C,
        (
            "他今天都已经玩了\x01",
            "四次恐怖过山车了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_199C")

    label("loc_199C")

    TalkEnd(0xFE)
    Return()

    # Function_26_1924 end

    def Function_27_19A0(): pass

    label("Function_27_19A0")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0049
    ChrTalk(
        0xB,
        (
            "#01109F好，我们带\x01",
            "蔡特一起去玩下一个\x01",
            "游乐设施吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xC,
        "#01200F……嗷？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x10,
        (
            "#14006F不不……那肯定是不行的，\x01",
            "用常识来考虑一下啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_27_19A0 end

    def Function_28_1A42(): pass

    label("Function_28_1A42")

    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x10)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x10)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x10)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x19, 0x11)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x10)
    ClearChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x1A, 0x12)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x10)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1B, 0x13)
    SetChrSubChip(0x1B, 0x0)
    EndChrThread(0x1B, 0x0)
    SetChrBattleFlags(0x1B, 0x4)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1C, 0x14)
    SetChrSubChip(0x1C, 0x0)
    EndChrThread(0x1C, 0x0)
    SetChrBattleFlags(0x1C, 0x4)
    SetChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B53")
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0xA)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0xB)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0xC)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x10)
    Jump("loc_1CC0")

    label("loc_1B53")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B7D")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    Jump("loc_1CC0")

    label("loc_1B7D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BBF")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_1CC0")

    label("loc_1BBF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C6B")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 6)), scpexpr(EXPR_END)), "loc_1C1B")
    SetChrPos(0x11, 14920, 0, -450, 270)

    label("loc_1C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 2)), scpexpr(EXPR_END)), "loc_1C29")
    SetChrFlags(0x11, 0x80)

    label("loc_1C29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_1C58")
    SetChrFlags(0xE, 0x80)
    Jump("loc_1C66")

    label("loc_1C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_1C66")
    SetChrFlags(0xF, 0x80)

    label("loc_1C66")

    Jump("loc_1CC0")

    label("loc_1C6B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CC0")
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    TurnDirection(0x17, 0x16, 0)
    TurnDirection(0x18, 0x16, 0)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)

    label("loc_1CC0")

    Return()

    # Function_28_1A42 end

    def Function_29_1CC1(): pass

    label("Function_29_1CC1")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(17030, 400, 460, 0)
    MoveCamera(43, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19900, 0)
    SetChrPos(0x101, 13520, 0, -380, 90)
    OP_65(0x2, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0052
    ChrTalk(
        0x101,
        (
            "#00005F咦，好像藏着\x01",
            "什么粉红色的东西呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x11, 0xFF)
    OP_9C(0x11, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    TurnDirection(0x11, 0x101, 500)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0053
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "呀，被发现了☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(15090, 0, 480, 0)
    MoveCamera(43, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19900, 0)
    SetChrPos(0x101, 11950, 0, -590, 90)
    SetChrPos(0x11, 14500, 0, -450, 270)
    Sound(1025, 0, 100, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0054
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "初次见面，小哥哥⊥\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "我是『咪雪』哦～¤\x01",
            "咪嘻嘻，请多指教哦～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0056
    ChrTalk(
        0x101,
        (
            "#00000F啊，莫非你就是\x01",
            "咪西的妹妹？\x02\x03",

            "#00004F缇欧之前说过，如果运气好，\x01",
            "有可能会见到咪雪……\x01",
            "哈哈，真幸运啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "啊，原来你知道我呀～！\x01",
            "咪嘻嘻，真开心～☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0058
    ChrTalk(
        0x101,
        (
            "#00005F话说回来……\x01",
            "你为什么要\x01",
            "藏在这种地方？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "咪嘻嘻，因为人家\x01",
            "最喜欢捉迷藏了～\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "我总是在奇幻乐园里\x01",
            "找个地方藏起来，\x01",
            "等着白马王子来找到我⊥\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0061
    ChrTalk(
        0x101,
        (
            "#00006F（如果运气不好，\x01",
            "  就见不到它了啊……）\x02\x03",

            "#00012F哈哈，也就是说，\x01",
            "我就是这次的白马王子吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "咪嘻嘻，没错～\x01",
            "能被你找到，\x01",
            "人家很开心哦！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "你比一脸颓相的哥哥\x01",
            "帅气一百倍，\x01",
            "完全有资格当王子哟☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#00006F（说、说得\x01",
            "  真过分啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "所以呢……\x01",
            "小哥哥，要不要\x01",
            "跟我玩捉迷藏？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0066
    ChrTalk(
        0x101,
        "#00005F咦……？\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "这是很特别的游戏哟，\x01",
            "只有找到我的\x01",
            "王子才能参加～\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "我会藏在奇幻乐园里，\x01",
            "小哥哥要和朋友\x01",
            "一起找到我五次！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "找到之后，还有豪华奖品哟☆\x01",
            "怎么样？要不要试试看？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 31)
    Return()

    # Function_29_1CC1 end

    def Function_30_221C(): pass

    label("Function_30_221C")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x11, 0xFF)
    OP_68(15090, 0, 480, 0)
    MoveCamera(43, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19900, 0)
    SetChrPos(0x101, 11950, 0, -590, 90)
    SetChrPos(0x11, 14500, 0, -450, 270)
    FadeToBright(1000, 0)
    OP_0D()

    #C0070
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "啊，小哥哥！\x01",
            "你还是想和我玩捉迷藏吧～？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "我会藏在奇幻乐园里，\x01",
            "小哥哥要和朋友\x01",
            "一起找到我五次！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "找到之后，还有豪华奖品哟☆\x01",
            "怎么样？要不要试试看？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 31)
    Return()

    # Function_30_221C end

    def Function_31_2335(): pass

    label("Function_31_2335")


    #C0073
    ChrTalk(
        0x101,
        (
            "#00003F（一旦开始捉迷藏，\x01",
            "  在结束之前，就不能去玩\x01",
            "  其它的游乐设施了……）\x02",
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
            "【接受】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23E9")
    Call(0, 32)
    Jump("loc_2484")

    label("loc_23E9")


    #C0074
    ChrTalk(
        0x101,
        (
            "#00000F这个……抱歉，\x01",
            "我还在体验\x01",
            "各种游乐设施呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "咦，是这样吗～？\x01",
            "真失望……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "不过，要是你想玩了，\x01",
            "可以再来找我哦！\x01",
            "我会等你的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C7, 6)

    label("loc_2484")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x11, 14920, 0, -450, 270)
    OP_4C(0x11, 0xFF)
    SetChrPos(0x0, 12800, 0, -380, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_31_2335 end

    def Function_32_24BC(): pass

    label("Function_32_24BC")


    #C0077
    ChrTalk(
        0x101,
        (
            "#00000F那就……\x01",
            "试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0078
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "咪嘻嘻，这才对☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "那么，我这就开始藏啦，\x01",
            "小哥哥，\x01",
            "你去找搭档吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "想放弃的时候，\x01",
            "去广场和咪西哥哥\x01",
            "说一声就可以了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "咪嘻嘻，再见啦～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(12510, 0, 1310, 3000)

    def lambda_25AF():

        label("loc_25AF")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_25AF")

    QueueWorkItem2(0x101, 1, lambda_25AF)
    SetChrFlags(0x11, 0x1000)
    OP_95(0x11, 13790, 0, 1620, 5000, 0x0)
    OP_95(0x11, 2640, 0, 1210, 5000, 0x0)
    EndChrThread(0x101, 0x1)
    OP_6F(0x1)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0082
    ChrTalk(
        0x101,
        (
            "#00003F总、总之……\x01",
            "似乎需要找个搭档\x01",
            "和我一起找咪雪啊。\x02\x03",

            "#00000F邀请谁好呢……？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【艾莉】\x01",        # 0
            "【缇欧】\x01",        # 1
            "【兰迪】\x01",        # 2
            "【诺艾尔】\x01",      # 3
            "【瓦吉】\x01",        # 4
            "【琪雅】\x01",        # 5
            "【芙兰】\x01",        # 6
            "【塞茜尔】\x01",      # 7
            "【伊莉娅】\x01",      # 8
            "【莉夏】\x01",        # 9
            "【修利】\x01",        # 10
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_274D"),
        (1, "loc_2787"),
        (2, "loc_27C1"),
        (3, "loc_27FB"),
        (4, "loc_2837"),
        (5, "loc_2871"),
        (6, "loc_28AB"),
        (7, "loc_28E5"),
        (8, "loc_2925"),
        (9, "loc_2965"),
        (10, "loc_299F"),
        (SWITCH_DEFAULT, "loc_29D9"),
    )


    label("loc_274D")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C7, 7)

    #C0083
    ChrTalk(
        0x101,
        "#00000F（好……邀请艾莉吧。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x0)
    Jump("loc_29D9")

    label("loc_2787")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 0)

    #C0084
    ChrTalk(
        0x101,
        "#00000F（好……邀请缇欧吧。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x1)
    Jump("loc_29D9")

    label("loc_27C1")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 1)

    #C0085
    ChrTalk(
        0x101,
        "#00000F（好……邀请兰迪吧。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x2)
    Jump("loc_29D9")

    label("loc_27FB")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 2)

    #C0086
    ChrTalk(
        0x101,
        "#00000F（好……邀请诺艾尔吧。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x3)
    Jump("loc_29D9")

    label("loc_2837")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 3)

    #C0087
    ChrTalk(
        0x101,
        "#00000F（好……邀请瓦吉吧。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x4)
    Jump("loc_29D9")

    label("loc_2871")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 4)

    #C0088
    ChrTalk(
        0x101,
        "#00000F（好……邀请琪雅吧。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x5)
    Jump("loc_29D9")

    label("loc_28AB")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 5)

    #C0089
    ChrTalk(
        0x101,
        "#00000F（好……邀请芙兰吧。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x6)
    Jump("loc_29D9")

    label("loc_28E5")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 6)

    #C0090
    ChrTalk(
        0x101,
        "#00000F（好……邀请塞茜尔姐姐吧。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x7)
    Jump("loc_29D9")

    label("loc_2925")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 7)

    #C0091
    ChrTalk(
        0x101,
        "#00000F（好……邀请伊莉娅小姐吧。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x8)
    Jump("loc_29D9")

    label("loc_2965")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C9, 0)

    #C0092
    ChrTalk(
        0x101,
        "#00000F（好……邀请莉夏吧。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x9)
    Jump("loc_29D9")

    label("loc_299F")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C9, 1)

    #C0093
    ChrTalk(
        0x101,
        "#00000F（好……邀请修利吧。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0xA)
    Jump("loc_29D9")

    label("loc_29D9")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_29F6")
    AddParty(0x1, 0xEF, 0xFF)
    Jump("loc_2AA6")

    label("loc_29F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_2A08")
    AddParty(0x2, 0xEF, 0xFF)
    Jump("loc_2AA6")

    label("loc_2A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_2A1A")
    AddParty(0x3, 0xEF, 0xFF)
    Jump("loc_2AA6")

    label("loc_2A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_2A2C")
    AddParty(0x8, 0xEF, 0xFF)
    Jump("loc_2AA6")

    label("loc_2A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_2A3E")
    AddParty(0x4, 0xEF, 0xFF)
    Jump("loc_2AA6")

    label("loc_2A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_2A50")
    AddParty(0x52, 0xEF, 0xFF)
    Jump("loc_2AA6")

    label("loc_2A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_2A62")
    AddParty(0x55, 0xEF, 0xFF)
    Jump("loc_2AA6")

    label("loc_2A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_2A74")
    AddParty(0x4B, 0xEF, 0xFF)
    Jump("loc_2AA6")

    label("loc_2A74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_2A8B")
    AddParty(0x33, 0xEF, 0xFF)
    SetChrFlags(0xE, 0x80)
    Jump("loc_2AA6")

    label("loc_2A8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_2AA2")
    AddParty(0x34, 0xEF, 0xFF)
    SetChrFlags(0xF, 0x80)
    Jump("loc_2AA6")

    label("loc_2AA2")

    AddParty(0x65, 0xEF, 0xFF)

    label("loc_2AA6")

    OP_68(14480, 0, 520, 0)
    MoveCamera(44, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19900, 0)
    SetChrPos(0xEF, 13000, 0, 200, 180)
    SetChrPos(0x101, 13000, 0, -1690, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_2B5F")

    #C0094
    ChrTalk(
        0x102,
        (
            "#00100F嗯，我已经明白了。\x02\x03",

            "#00109F呵呵，听起来好像很有趣，\x01",
            "我们努力去找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F75")

    label("loc_2B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_2BCE")

    #C0095
    ChrTalk(
        0x103,
        (
            "#00200F原来如此……\x01",
            "我已经明白了。\x02\x03",

            "#00204F和咪雪玩捉迷藏……\x01",
            "必须要打起全部精神\x01",
            "来应战呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F75")

    label("loc_2BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_2C2D")

    #C0096
    ChrTalk(
        0x104,
        (
            "#00300F原来如此，我明白了。\x02\x03",

            "#00304F好，就在乘坐游乐设施的间隙\x01",
            "稍微玩玩吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F75")

    label("loc_2C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_2C9A")

    #C0097
    ChrTalk(
        0x109,
        (
            "#10105F哦，原来是这样……\x02\x03",

            "#10109F不过，听起来倒是很有趣呢。\x01",
            "既然要玩，我们就认真去找吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F75")

    label("loc_2C9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_2D08")

    #C0098
    ChrTalk(
        0x105,
        (
            "#10300F唔，原来如此，\x01",
            "听起来好像很有趣呢。\x02\x03",

            "#10309F呵呵，机会难得，\x01",
            "我们就打起精神去找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F75")

    label("loc_2D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_2D5A")

    #C0099
    ChrTalk(
        0x153,
        (
            "#01100F捉迷藏吗，好有趣！！\x02\x03",

            "#01109F罗伊德，我们要加油找啊！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F75")

    label("loc_2D5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_2DB8")

    #C0100
    ChrTalk(
        0x156,
        (
            "#06405F嘿，和咪雪\x01",
            "玩捉迷藏吗～\x02\x03",

            "#06409F呵呵，罗伊德警官！\x01",
            "我们努力去找吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F75")

    label("loc_2DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_2E17")

    #C0101
    ChrTalk(
        0x14C,
        (
            "#05905F哎，原来是这样啊。\x02\x03",

            "#05909F呵呵，那我们就去找找\x01",
            "那个叫咪雪的孩子吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F75")

    label("loc_2E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_2EA4")

    #C0102
    ChrTalk(
        0x134,
        (
            "#01700F嗯嗯，我已经明白了，\x01",
            "听起来好像挺有趣的。\x02\x03",

            "#01709F虽然只是捉迷藏，\x01",
            "但似乎需要拿出真本事呢！\x01",
            "一起努力吧，警察弟弟！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F75")

    label("loc_2EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_2F05")

    #C0103
    ChrTalk(
        0x135,
        (
            "#01802F原来如此……我明白了。\x02\x03",

            "#01809F呵呵，我很擅长玩捉迷藏呢，\x01",
            "一起去找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F75")

    label("loc_2F05")


    #C0104
    ChrTalk(
        0x166,
        (
            "#14000F唔，捉迷藏啊，\x01",
            "听起来好像很奇怪。\x02\x03",

            "#14004F算了，反正我也有空，就陪你去找找吧。\x01",
            "……好啦，赶快出发。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_2FCA")

    #C0105
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，多谢帮忙。\x02\x03",

            "#00000F那我们这就开始\x01",
            "在主题公园里找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3011")

    label("loc_2FCA")


    #C0106
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，多谢帮忙。\x02\x03",

            "#00000F那我们这就开始\x01",
            "在主题公园里找吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3011")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0107
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【咪雪的挑战】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1C9, 2)
    OP_29(0x7F, 0x4, 0x2)
    SetChrFlags(0x11, 0x80)
    OP_65(0x2, 0x1)
    SetChrPos(0x0, 12800, 0, -380, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_32_24BC end

    def Function_33_3084(): pass

    label("Function_33_3084")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10200.itc", 0x1E)
    LoadChrToIndex("chr/ch45400.itc", 0x1F)
    LoadChrToIndex("chr/ch28100.itc", 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrFlags(0x1D, 0x8000)
    OP_68(12380, 0, 8690, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18770, 0)
    SetChrPos(0x101, 10510, 0, 7810, 90)
    SetChrPos(0x103, 11970, 0, 7490, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    #C0108
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200F呼，总算完成了……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F……很累了吧。\x02\x03",

            "#05526F穿着道具服跳舞\x01",
            "相当辛苦呢……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F是啊……\x01",
            "真是热死人了。\x02\x03",

            "#05209F真正的扮演者\x01",
            "每天都要做这些事情，\x01",
            "真是了不起啊。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522F呵呵……是啊。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 6440, 0, 1530, 45)

    #N0112
    NpcTalk(
        0x1D,
        "男性的声音",
        (
            "喂！\x01",
            "咪西、咪雪！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(11850, 0, 8160, 3000)
    SetCameraDistance(20690, 3000)

    def lambda_32A6():

        label("loc_32A6")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_32A6")

    QueueWorkItem2(0x101, 1, lambda_32A6)

    def lambda_32B8():

        label("loc_32B8")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_32B8")

    QueueWorkItem2(0x103, 1, lambda_32B8)
    OP_95(0x1D, 10760, 0, 5250, 2000, 0x0)
    OP_93(0x1D, 0x0, 0x1F4)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    OP_6F(0x79)

    #C0113
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200F啊……\x01",
            "您辛苦了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x1D,
        (
            "哦，辛苦了，\x01",
            "真是麻烦你们了！\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x1D,
        (
            "你们知道吗？\x01",
            "『咪雪』今天成为\x01",
            "热门话题了呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F热门话题吗……？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x1D,
        (
            "嗯，大家都说陪伴在咪西身边，\x01",
            "偶尔会表现出冷傲举止的\x01",
            "咪雪非常迷人呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x1D,
        (
            "唔，如此看来，\x01",
            "似乎有必要重新考虑一下\x01",
            "『咪雪』的性格设定呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212F是、是吗……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2300, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x103)

    #C0120
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524F……咳咳……\x01",
            "总之，能帮上您的忙就好。\x02\x03",

            "#05520F话说回来……\x01",
            "真正的扮演者还没到吗……？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x1D,
        (
            "……哦哦，我都给忘了！\x01",
            "刚才已经到了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x1D,
        (
            "他让你们先去\x01",
            "更衣室等等，\x01",
            "他稍后就会过去。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x1D,
        (
            "真是辛苦二位啦，\x01",
            "不介意的话，请收下这个，\x01",
            "就当作打工的酬劳吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_97(0x1D, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0124
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '咪雪玩偶'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('咪雪玩偶', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0125
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05202F非常感谢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0126
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200F那么，缇欧……\x01",
            "我们先过去吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0127
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522F嗯，走吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    StopSound(821, 4000, 50)
    StopSound(126, 4000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1390", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_3084 end

    def Function_34_364A(): pass

    label("Function_34_364A")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0128
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

    # Function_34_364A end

    SaveToFile()

Try(main)
