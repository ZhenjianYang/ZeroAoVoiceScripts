from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1040.bin",                # FileName
        "c1040",                    # MapName
        "c1040",                    # Location
        0x0015,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 21, 0, 4, 0, 5],
    )

    BuildStringList((
        "c1040",                  # 0
        "玛西",                   # 1
        "玛西",                   # 2
        "莎丽娜",                 # 3
        "尤格特",                 # 4
        "克拉莉丝",               # 5
        "亚泽尔",                 # 6
        "艾丝蒂尔",               # 7
        "艾丝蒂尔",               # 8
        "约修亚",                 # 9
        "芙兰",                   # 10
    ))

    AddCharChip((
        "chr/ch21800.itc",                   # 00
        "chr/ch20500.itc",                   # 01
        "chr/ch34200.itc",                   # 02
        "chr/ch10400.itc",                   # 03
        "apl/ch50375.itc",                   # 04
        "chr/ch21802.itc",                   # 05
        "chr/ch00600.itc",                   # 06
        "chr/ch00602.itc",                   # 07
        "chr/ch00702.itc",                   # 08
        "chr/ch08500.itc",                   # 09
    ))

    DeclNpc(48880,   29,      -55000,  135,  261,  0x0, 0,   0,   0,   0,   2,   0,   6,   255,  0)
    DeclNpc(46200,   100,     -53479,  270,  389,  0x0, 0,   5,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(3789,    0,       55279,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-2410,   29,      52169,   225,  261,  0x0, 0,   2,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(3660,    29,      -56599,  90,   261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(1029,    29,      55659,   90,   405,  0x0, 0,   4,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(53740,   0,       51459,   90,   405,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(52040,   150,     53650,   270,  469,  0x0, 0,   7,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(49349,   50,      53750,   90,   469,  0x0, 0,   8,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(-400,    29,      -53770,  135,  389,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)

    DeclActor(51690,   0,       5670,    1200,    51690,   1500,    5670,    0x007C, 0,  22, 0x0000)
    DeclActor(-4890,   0,       -52820,  1200,    -4890,   1500,    -52820,  0x007C, 0,  23, 0x0000)

    ScpFunction((
        "Function_0_27C",          # 00, 0
        "Function_1_334",          # 01, 1
        "Function_2_35F",          # 02, 2
        "Function_3_38A",          # 03, 3
        "Function_4_3B5",          # 04, 4
        "Function_5_647",          # 05, 5
        "Function_6_6E8",          # 06, 6
        "Function_7_14E1",         # 07, 7
        "Function_8_16EA",         # 08, 8
        "Function_9_236A",         # 09, 9
        "Function_10_296C",        # 0A, 10
        "Function_11_3CD6",        # 0B, 11
        "Function_12_3D63",        # 0C, 12
        "Function_13_3EDA",        # 0D, 13
        "Function_14_3F56",        # 0E, 14
        "Function_15_3FBA",        # 0F, 15
        "Function_16_41D1",        # 10, 16
        "Function_17_4568",        # 11, 17
        "Function_18_4A9F",        # 12, 18
        "Function_19_4B6D",        # 13, 19
        "Function_20_5175",        # 14, 20
        "Function_21_5777",        # 15, 21
        "Function_22_5D19",        # 16, 22
        "Function_23_5E75",        # 17, 23
    ))


    def Function_0_27C(): pass

    label("Function_0_27C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2BC"),
        (1, "loc_2C8"),
        (2, "loc_2D4"),
        (3, "loc_2E0"),
        (4, "loc_2EC"),
        (5, "loc_2F8"),
        (6, "loc_304"),
        (SWITCH_DEFAULT, "loc_310"),
    )


    label("loc_2BC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2C8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2D4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2E0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2EC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2F8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_304")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_310")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_31C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_333")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_333")

    Return()

    # Function_0_27C end

    def Function_1_334(): pass

    label("Function_1_334")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_35E")
    OP_94(0xFE, 0xFFFFF204, 0xCD3C, 0xFFFFFA24, 0xC602, 0x3E8)
    Sleep(300)
    Jump("Function_1_334")

    label("loc_35E")

    Return()

    # Function_1_334 end

    def Function_2_35F(): pass

    label("Function_2_35F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_389")
    OP_94(0xFE, 0xBC16, 0xFFFF213A, 0xBDCE, 0xFFFF2FB8, 0x3E8)
    Sleep(300)
    Jump("Function_2_35F")

    label("loc_389")

    Return()

    # Function_2_35F end

    def Function_3_38A(): pass

    label("Function_3_38A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B4")
    OP_94(0xFE, 0xFFFFFC90, 0xFFFF2F04, 0xFFFFF6F0, 0xFFFF263A, 0x3E8)
    Sleep(300)
    Jump("Function_3_38A")

    label("loc_3B4")

    Return()

    # Function_3_38A end

    def Function_4_3B5(): pass

    label("Function_4_3B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3C3")
    Jump("loc_646")

    label("loc_3C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3D1")
    Jump("loc_646")

    label("loc_3D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_40D")
    SetChrPos(0xA, 2500, 30, 55660, 270)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_408")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)

    label("loc_408")

    Jump("loc_646")

    label("loc_40D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_420")
    SetChrFlags(0xB, 0x80)
    Jump("loc_646")

    label("loc_420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_46F")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, 3790, 0, 55280, 180)
    SetChrPos(0xB, 3990, 30, 54010, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_646")

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_487")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_646")

    label("loc_487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_49F")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_646")

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4B7")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_646")

    label("loc_4B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4C5")
    Jump("loc_646")

    label("loc_4C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4EA")
    SetChrPos(0xB, 2590, 30, 55740, 135)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_646")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_520")
    SetChrPos(0xA, 3790, 0, 55280, 180)
    SetChrPos(0xB, 3990, 30, 54010, 0)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_646")

    label("loc_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_55B")
    SetChrPos(0xA, 3790, 0, 55280, 180)
    SetChrPos(0xB, 3990, 30, 54010, 0)
    SetChrFlags(0xA, 0x10)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_646")

    label("loc_55B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_59B")
    SetChrPos(0xA, 3790, 0, 55280, 180)
    SetChrPos(0xB, 3990, 30, 54010, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_646")

    label("loc_59B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5B3")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_646")

    label("loc_5B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5DD")
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xB, -1120, 30, -53900, 225)
    BeginChrThread(0xB, 0, 0, 3)
    Jump("loc_646")

    label("loc_5DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5EB")
    Jump("loc_646")

    label("loc_5EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5F9")
    Jump("loc_646")

    label("loc_5F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_622")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_61D")
    SetChrFlags(0x8, 0x80)

    label("loc_61D")

    Jump("loc_646")

    label("loc_622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_646")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_646")
    SetChrFlags(0x8, 0x80)

    label("loc_646")

    Return()

    # Function_4_3B5 end

    def Function_5_647(): pass

    label("Function_5_647")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_660")
    OP_10(0x0, 0x0)
    OP_10(0xB, 0x1)
    Jump("loc_666")

    label("loc_660")

    OP_10(0x0, 0x1)
    OP_10(0xB, 0x0)

    label("loc_666")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_682")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_699")

    label("loc_682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_699")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_699")

    label("loc_699")

    OP_65(0x0, 0x1)
    SetMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BB")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_6BB")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D5")
    OP_66(0x1, 0x1)

    label("loc_6D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E7")
    OP_66(0x1, 0x1)

    label("loc_6E7")

    Return()

    # Function_5_647 end

    def Function_6_6E8(): pass

    label("Function_6_6E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_770")

    #C0001
    ChrTalk(
        0xFE,
        (
            "住我家对面的那位邻居\x01",
            "大约在半个月之前搬走了。\x01",
            "现在那间房空了下来。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "说起来……那个人的性格\x01",
            "还真是散漫随性呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DD")

    label("loc_770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7D6")

    #C0003
    ChrTalk(
        0xFE,
        (
            "说起来……\x01",
            "不知预算会议结果如何了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "预算的下拨计划对股价\x01",
            "也有着相当大的影响。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DD")

    label("loc_7D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_848")

    #C0005
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔时代周刊……\x01",
            "对了，是明天发行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "嗯～因为临时休刊了，\x01",
            "都有点搞不清发行时间呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DD")

    label("loc_848")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8B7")

    #C0007
    ChrTalk(
        0xFE,
        (
            "港湾区那里好像发生了\x01",
            "重大事件呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "说到港湾区，\x01",
            "离这里没几步远吧？\x01",
            "真、真是好危险呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DD")

    label("loc_8B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_986")

    #C0009
    ChrTalk(
        0xFE,
        (
            "我寄给家人的纪念庆典照片，\x01",
            "他们都已经收到了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "在导力通讯中通话时，孩子们\x01",
            "甚至开心地说谢谢呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "……（抽泣）\x01",
            "已经很久都没听到过家人的声音了……\x01",
            "乡愁真是催人落泪啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9E6")

    label("loc_986")


    #C0012
    ChrTalk(
        0xFE,
        (
            "不行不行，现在可不是\x01",
            "想家思乡的时候。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "单身赴任，责任在身，\x01",
            "必须要把要做的事情完成啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E6")

    Jump("loc_14DD")

    label("loc_9EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_9F9")
    Jump("loc_14DD")

    label("loc_9F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_ABF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7A")

    #C0014
    ChrTalk(
        0xFE,
        (
            "啊，导力相机的导力\x01",
            "好像已经用完了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "本来还想拍摄烟花的……\x01",
            "算了，到晚上应该就能恢复了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_ABA")

    label("loc_A7A")


    #C0016
    ChrTalk(
        0xFE,
        (
            "导力器中的导力\x01",
            "经过一段时间就会自行恢复，\x01",
            "真是非常方便哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABA")

    Jump("loc_14DD")

    label("loc_ABF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_B22")

    #C0017
    ChrTalk(
        0xFE,
        "游行真是太壮观了啊……\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "虽然我还是第一次使用相机，\x01",
            "但一定拍下了很棒的照片。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DD")

    label("loc_B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_BCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9A")

    #C0019
    ChrTalk(
        0xFE,
        (
            "我和家人约好了，要拍摄\x01",
            "游行的照片给他们看。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "再、再不赶快把工作完成就来不及了……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BC9")

    label("loc_B9A")


    #C0021
    ChrTalk(
        0xFE,
        (
            "啊啊，再不快点的话，\x01",
            "游行就要开始了……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC9")

    Jump("loc_14DD")

    label("loc_BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C1F")

    #C0022
    ChrTalk(
        0xFE,
        "总公司发来了紧急指示。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "呜呜，看来今天\x01",
            "是没机会出门逛了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DD")

    label("loc_C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_C8A")

    #C0024
    ChrTalk(
        0xFE,
        "好，拿好钱包，还有……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "……如果可以的话，真希望和\x01",
            "居住在帝国的家人们一起去参观啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DD")

    label("loc_C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_CF0")

    #C0026
    ChrTalk(
        0xFE,
        (
            "嗯……下个月\x01",
            "会不会放假呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "如果可能的话，真想和家人\x01",
            "一起参观创立纪念庆典啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DD")

    label("loc_CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_E41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCC")

    #C0028
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ集团的证券公司\x01",
            "是全世界最大的证券公司。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "对于我们公司来说，\x01",
            "算是有力的竞争对手，不过……\x01",
            "我们也会进行合作。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "也就是证券的互相持有，\x01",
            "我们公司的一部分证券\x01",
            "就交由ＩＢＣ掌控了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E3C")

    label("loc_DCC")


    #C0031
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ集团的证券公司\x01",
            "是我们公司的最大竞争对手。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "但我们也会进行合作。\x01",
            "在这个世界上，并不是只有争斗的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3C")

    Jump("loc_14DD")

    label("loc_E41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_FAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F18")

    #C0033
    ChrTalk(
        0xFE,
        (
            "大概是因为最近的负面事件太多了吧，\x01",
            "股票的价格波动情况实在是不能令人满意。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "由于是事件发生的现场，所以仓库租赁公司\x01",
            "的市值大幅度下降了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "那些被牵连进来的公司真是不幸呢……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FAA")

    label("loc_F18")


    #C0036
    ChrTalk(
        0xFE,
        (
            "大概是因为最近的负面事件太多了吧，\x01",
            "股票的价格波动情况实在是不能令人满意。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "不过，应该很快就会恢复吧，\x01",
            "那些被牵连进来的公司也真是不幸呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FAA")

    Jump("loc_14DD")

    label("loc_FAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_105B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_102C")

    #C0038
    ChrTalk(
        0xFE,
        (
            "偶尔也想放个假，\x01",
            "回去见见家人……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "但我们的公司从事证券相关业务，\x01",
            "很难有机会获得休假的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1056")

    label("loc_102C")


    #C0040
    ChrTalk(
        0xFE,
        "唉，这就是单身就任最大的痛苦之处……\x02",
    )

    CloseMessageWindow()

    label("loc_1056")

    Jump("loc_14DD")

    label("loc_105B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_10F2")

    #C0041
    ChrTalk(
        0xFE,
        (
            "玛因兹出产的七耀石，\x01",
            "其交易价格最近稍有下滑呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "嗯，七耀石的交易状况也会\x01",
            "影响到我们公司的行情呢。\x01",
            "必须提前将原因调查清楚啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DD")

    label("loc_10F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1158")

    #C0043
    ChrTalk(
        0xFE,
        (
            "街上实在太吵闹了，\x01",
            "连午觉都睡不好……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "这座公寓的墙真是很薄，\x01",
            "都不能隔音啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DD")

    label("loc_1158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_12BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1234")

    #C0045
    ChrTalk(
        0xFE,
        (
            "就在最近，隔壁搬来了\x01",
            "两个年轻人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "我和他们打过一次招呼，\x01",
            "一个是梳着双马尾辫的少女，\x01",
            "另一个是黑头发的青年。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "没记错的话，他们好像说过\x01",
            "自己是游击士吧。\x01",
            "真是两个朝气蓬勃的孩子啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12B7")

    label("loc_1234")


    #C0048
    ChrTalk(
        0xFE,
        (
            "就在最近，隔壁搬来了\x01",
            "两个年轻人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "一个是精神饱满，梳着双马尾辫的女孩，\x01",
            "还有一个是黑头发的青年。\x01",
            "他们好像都是游击士呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B7")

    Jump("loc_14DD")

    label("loc_12BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_13BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135C")

    #C0050
    ChrTalk(
        0xFE,
        (
            "详细调查克洛斯贝尔的市场动向\x01",
            "就是我的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "周边诸国的情报也都会\x01",
            "传到克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "对证券公司来说，\x01",
            "情报可是重中之重。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13BA")

    label("loc_135C")


    #C0053
    ChrTalk(
        0xFE,
        (
            "嗯嗯，共和国那边\x01",
            "仍然气候不调吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "必须要总结好市场行情的动向，\x01",
            "并向总公司报告啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13BA")

    Jump("loc_14DD")

    label("loc_13BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_14DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1469")

    #C0055
    ChrTalk(
        0xFE,
        (
            "我在埃雷波尼亚帝国的\x01",
            "证券公司上班。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "这次是单身就任，来主要业务点\x01",
            "克洛斯贝尔这边工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "相比之下，确实还是\x01",
            "这边的设施更加便利啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14DD")

    label("loc_1469")


    #C0058
    ChrTalk(
        0xFE,
        (
            "嗯，可是……\x01",
            "这一带都是东方风格的建筑啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "对帝国人来说，总觉得有些稀奇，\x01",
            "不是很适应，但是也无可奈何呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14DD")

    TalkEnd(0xFE)
    Return()

    # Function_6_6E8 end

    def Function_7_14E1(): pass

    label("Function_7_14E1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1575")
    Jump("loc_15BF")

    label("loc_1575")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1595")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15BF")

    label("loc_1595")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15B5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15BF")

    label("loc_15B5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15BF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_16E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1689")

    #C0060
    ChrTalk(
        0xFE,
        (
            "我接下来就要将在纪念庆典期间\x01",
            "拍摄的照片寄给居住在帝国的家人们。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "我拍到了不少很有观赏性的照片呢。\x01",
            "这样一来，孩子们也会很高兴吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16E2")

    label("loc_1689")


    #C0062
    ChrTalk(
        0xFE,
        (
            "对了，都忘了还要写封信，\x01",
            "到时和照片一起寄过去。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        "嗯～『你们都还好吗』，这样……\x02",
    )

    CloseMessageWindow()

    label("loc_16E2")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_14E1 end

    def Function_8_16EA(): pass

    label("Function_8_16EA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_17F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1797")

    #C0064
    ChrTalk(
        0xFE,
        (
            "我对圣书会的印象\x01",
            "已经与从前有了很大的不同。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "下次准备找个时间，\x01",
            "和尤格特一起去亚泽尔\x01",
            "工作的地方吃点东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        "……要对那孩子保密哦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17F3")

    label("loc_1797")


    #C0067
    ChrTalk(
        0xFE,
        (
            "我准备找个时间和尤格特一起，\x01",
            "去亚泽尔工作的地方\x01",
            "吃点东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        "……要对那孩子保密哦。\x02",
    )

    CloseMessageWindow()

    label("loc_17F3")

    Jump("loc_2366")

    label("loc_17F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1881")

    #C0069
    ChrTalk(
        0xFE,
        (
            "自从亚泽尔开始工作之后，\x01",
            "家里的气氛好像\x01",
            "也开始有所好转了。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "虽然生活还是很艰苦……\x01",
            "但照这样干下去，应该很有希望。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2366")

    label("loc_1881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1990")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_193A")
    OP_4B(0xD, 0xFF)

    #C0071
    ChrTalk(
        0xFE,
        "嗯，咱们家什么事都没有哦。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "……你是急着赶回来了吗？\x01",
            "呵呵，亚泽尔也有可爱的一面啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xD,
        (
            "我说啊……\x01",
            "我是真的很担心，\x01",
            "你就别开我玩笑了。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_198B")

    label("loc_193A")


    #C0074
    ChrTalk(
        0xFE,
        (
            "昨天晚上发生了那种事件，亚泽尔\x01",
            "很担心，所以就赶回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        "……真开心呢。\x02",
    )

    CloseMessageWindow()

    label("loc_198B")

    Jump("loc_2366")

    label("loc_1990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_19F4")

    #C0076
    ChrTalk(
        0xFE,
        (
            "尤格特今天要去\x01",
            "主日学校。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "本来还担心他一个人留下看家\x01",
            "会很寂寞，这下正好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2366")

    label("loc_19F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1A3F")

    #C0078
    ChrTalk(
        0xFE,
        (
            "好啦，尤格特，\x01",
            "姐姐去工作了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        "要乖乖在家看家哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2366")

    label("loc_1A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1AE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA7")

    #C0080
    ChrTalk(
        0xFE,
        (
            "昨天，旧城区的不良团伙\x01",
            "好像引起了很大骚乱呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        "那些孩子可真是的……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AE0")

    label("loc_1AA7")


    #C0082
    ChrTalk(
        0xFE,
        (
            "真没办法……亚泽尔回来之后，\x01",
            "必须要好好教训他一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AE0")

    Jump("loc_2366")

    label("loc_1AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1B7D")

    #C0083
    ChrTalk(
        0xFE,
        (
            "亚泽尔那孩子，\x01",
            "竟然说纪念庆典中的一半时间\x01",
            "都想去和组织中的朋友一起玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "……那个组织是叫圣书会吧，\x01",
            "那些人好像也\x01",
            "并没有那么坏呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2366")

    label("loc_1B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1C3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C0A")

    #C0085
    ChrTalk(
        0xFE,
        (
            "亚泽尔和我说过，下个月的\x01",
            "纪念庆典期间一定会回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "难得的纪念庆典……\x01",
            "真希望能全家一起度过。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C35")

    label("loc_1C0A")


    #C0087
    ChrTalk(
        0xFE,
        (
            "……呵呵。\x01",
            "真是期待下个月啊，尤格特。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C35")

    Jump("loc_2366")

    label("loc_1C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1CB6")

    #C0088
    ChrTalk(
        0xFE,
        (
            "对了，虽然我买不起什么\x01",
            "太昂贵的东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "但我们姐弟已经很久没好好聚聚了，\x01",
            "真希望能一起悠闲地度过啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2366")

    label("loc_1CB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1D24")

    #C0090
    ChrTalk(
        0xFE,
        (
            "那么，尤格特……\x01",
            "姐姐要去工作了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "这段时间必须好好干活，\x01",
            "把之前休假的部分都补回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2366")

    label("loc_1D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1F26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E66")

    #C0092
    ChrTalk(
        0xFE,
        (
            "我那个加入不良组织的\x01",
            "弟弟亚泽尔……开始在\x01",
            "旧城区打工赚钱了。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "作为不脱离组织的代价，\x01",
            "他答应我要好好工作，\x01",
            "并不时回趟家。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "呼……话虽如此，但其实也只是\x01",
            "在同伴的酒吧里帮帮忙而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "算了，毕竟他也说过，要自己承担起\x01",
            "住院时所花的治疗费，把钱都还给我……\x01",
            "暂时就先观察一下他的状态吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F21")

    label("loc_1E66")


    #C0096
    ChrTalk(
        0xFE,
        (
            "亚泽尔仍然留在\x01",
            "不良团伙中，\x01",
            "我实在是很担心……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "不过他能回到家里，\x01",
            "至少也让我稍微放心了一些。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "……果然，平时一向都不发火的我\x01",
            "爆发一次，对他来说也许才是\x01",
            "最有效的教育方法吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F21")

    Jump("loc_2366")

    label("loc_1F26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2034")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FEC")

    #C0099
    ChrTalk(
        0xFE,
        (
            "为了把整天在旧城区鬼混的\x01",
            "弟弟带回家，\x01",
            "我申请了休假。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "这完全属于我个人的家庭问题，\x01",
            "却能获得带薪休假的待遇……\x01",
            "真是得救了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "……我准备明天就去\x01",
            "旧城区看看。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_202F")

    label("loc_1FEC")


    #C0102
    ChrTalk(
        0xFE,
        (
            "……我准备明天就去\x01",
            "旧城区看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        "必须要把亚泽尔给带回来。\x02",
    )

    CloseMessageWindow()

    label("loc_202F")

    Jump("loc_2366")

    label("loc_2034")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2166")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20D8")

    #C0104
    ChrTalk(
        0xFE,
        (
            "我的弟弟待在旧城区，\x01",
            "不愿意回家。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "我和医院那边联系过，\x01",
            "听说他都已经出院了……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "看来，我果然必须要亲自\x01",
            "把他带回来才行……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2161")

    label("loc_20D8")


    #C0107
    ChrTalk(
        0xFE,
        (
            "生活本来就很贫困，我却还要\x01",
            "申请休假，实在是挺不安……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "但我毕竟是他现在的监护人。\x01",
            "无论如何，也必须在近期之内\x01",
            "把亚泽尔带回来……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2161")

    Jump("loc_2366")

    label("loc_2166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2285")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2213")

    #C0109
    ChrTalk(
        0xFE,
        (
            "刚才接到\x01",
            "医院那边的联络，\x01",
            "说亚泽尔住院了。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "虽然并没有什么生命危险，\x01",
            "但伤势也相当严重……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "那孩子真是的，他到底\x01",
            "都在干些什么啊……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2280")

    label("loc_2213")


    #C0112
    ChrTalk(
        0xFE,
        (
            "竟然在我一无所知的情况下\x01",
            "受伤住院了……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "亚泽尔真是的，\x01",
            "他到底还要让我担心多少次\x01",
            "才能安分下来啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2280")

    Jump("loc_2366")

    label("loc_2285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2366")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22F4")

    #C0114
    ChrTalk(
        0xFE,
        (
            "我的弟弟都已经有\x01",
            "一个星期没回家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "肯定又在不良组织的\x01",
            "同伴那里住下了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2366")

    label("loc_22F4")


    #C0116
    ChrTalk(
        0xFE,
        (
            "我的弟弟都已经有\x01",
            "一个星期没回家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "如果你看见一个名叫亚泽尔的孩子，\x01",
            "能不能帮我传句话，让他快点回家呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2366")

    TalkEnd(0xFE)
    Return()

    # Function_8_16EA end

    def Function_9_236A(): pass

    label("Function_9_236A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_23F4")

    #C0118
    ChrTalk(
        0xFE,
        (
            "从主日学校毕业之后，\x01",
            "我也打算立刻开始工作哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "如果可能的话，\x01",
            "我希望成为一名游击士，\x01",
            "赚钱给姐姐和哥哥买好吃的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2968")

    label("loc_23F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2478")

    #C0120
    ChrTalk(
        0xFE,
        "姐姐她最近好像很开心呢。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "在哥哥愿意回家看看之前，她看上去\x01",
            "总是很难过，现在能重新开心起来，\x01",
            "我也替她高兴呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2968")

    label("loc_2478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_24A6")

    #C0122
    ChrTalk(
        0xFE,
        "哥哥他今天的工作会顺利吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2968")

    label("loc_24A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_24B4")
    Jump("loc_2968")

    label("loc_24B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_250E")

    #C0123
    ChrTalk(
        0xFE,
        (
            "嗯，没问题的～\x01",
            "我还要去克拉莉丝阿姨\x01",
            "那里哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        "姐姐也要努力工作哦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2968")

    label("loc_250E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2580")

    #C0125
    ChrTalk(
        0xFE,
        (
            "就在昨天，亚泽尔哥哥他们\x01",
            "所在的旧城区发生了\x01",
            "很有趣的事情呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        "真羡慕～我也好想亲眼看看啊～\x02",
    )

    CloseMessageWindow()
    Jump("loc_2968")

    label("loc_2580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_262C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2600")

    #C0127
    ChrTalk(
        0xFE,
        (
            "嘁……\x01",
            "本来还以为能一直和\x01",
            "亚泽尔哥哥在一起呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "……不过，无所谓啦。\x01",
            "姐姐，我们去玩吧～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2627")

    label("loc_2600")


    #C0129
    ChrTalk(
        0xFE,
        (
            "只要有姐姐在，\x01",
            "我就不会寂寞了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2627")

    Jump("loc_2968")

    label("loc_262C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_266D")

    #C0130
    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，我要和亚泽尔哥哥\x01",
            "玩扮演游击士的游戏～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2968")

    label("loc_266D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_26D2")

    #C0131
    ChrTalk(
        0xFE,
        "下个月就是纪念庆典了呢。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "好久没和亚泽尔哥哥一起玩了，\x01",
            "真想赶快和他一起玩呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2968")

    label("loc_26D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2709")

    #C0133
    ChrTalk(
        0xFE,
        (
            "我去克拉莉丝阿姨\x01",
            "那里等姐姐回来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2968")

    label("loc_2709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2779")

    #C0134
    ChrTalk(
        0xFE,
        "姐姐她好像很开心呢。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "她说，自从亚泽尔哥哥也开始\x01",
            "工作之后，生活就变得稍微轻松\x01",
            "一点了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2968")

    label("loc_2779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_27C0")

    #C0136
    ChrTalk(
        0xFE,
        (
            "姐姐去旧城区接\x01",
            "亚泽尔哥哥了。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "不、不要紧吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2968")

    label("loc_27C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2822")

    #C0138
    ChrTalk(
        0xFE,
        (
            "亚泽尔哥哥\x01",
            "一直都不回来……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "让姐姐那么担心，真是的，\x01",
            "他到底在干什么嘛……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2968")

    label("loc_2822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_287E")

    #C0140
    ChrTalk(
        0xFE,
        (
            "喂喂，我们来玩\x01",
            "扮演游击士的游戏吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "喝喝，呀～！\x01",
            "游击士是无敌的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2968")

    label("loc_287E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_28BB")

    #C0142
    ChrTalk(
        0xFE,
        (
            "亚泽尔哥哥\x01",
            "受伤了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        "不要紧吧……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2968")

    label("loc_28BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2968")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2918")

    #C0144
    ChrTalk(
        0xFE,
        (
            "游击士真是\x01",
            "超级帅气的～\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "我也曾见到过亚里欧斯\x01",
            "先生呢～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2968")

    label("loc_2918")


    #C0146
    ChrTalk(
        0xFE,
        (
            "我也曾见到过亚里欧斯\x01",
            "先生呢～！\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿～很厉害吧。\x01",
            "他真是超级帅啊～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2968")

    TalkEnd(0xFE)
    Return()

    # Function_9_236A end

    def Function_10_296C(): pass

    label("Function_10_296C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_29D2")

    #C0148
    ChrTalk(
        0xFE,
        "……啊，都已经这么晚了啊。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "芙兰白天非常着急匆忙，\x01",
            "不知道有没有好好吃东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CCF")

    label("loc_29D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2A60")

    #C0150
    ChrTalk(
        0xFE,
        (
            "芙兰忘记了带饭，我送到警察局\x01",
            "想交给她，可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "她好像相当繁忙，\x01",
            "最后都没能找到机会给她。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        "难道发生什么事情了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CCF")

    label("loc_2A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2B96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B2B")

    #C0153
    ChrTalk(
        0xFE,
        "听传闻说，港湾区那里发生了争斗呢。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "芙兰做的是接待工作，\x01",
            "一般很少需要她直接\x01",
            "赶往现场，不过……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "最近这段时间，警察局的人\x01",
            "好像经常会涉足危险事件，\x01",
            "偶尔也会担心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2B91")

    label("loc_2B2B")


    #C0156
    ChrTalk(
        0xFE,
        (
            "你们几个也是，身为警察，\x01",
            "去处理各种事件自然值得肯定……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "但也不要让自己身边的人\x01",
            "太过担心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B91")

    Jump("loc_3CCF")

    label("loc_2B96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2DFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D87")
    TurnDirection(0xFE, 0x109, 0)

    #C0158
    ChrTalk(
        0xFE,
        "啊，这不是诺艾尔嘛。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x109,
        "#0505F啊，妈妈。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x104,
        (
            "#0306F怎、怎么回事？\x01",
            "这母女再会的场面怎么会这么平淡啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x109,
        (
            "#0500F那个，算是吧……\x01",
            "因为我们最近经常见面的。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        "#0000F哈哈，看来上士你很孝顺呢。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x102,
        "#0102F阿姨也很高兴吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 500)

    #C0164
    ChrTalk(
        0xFE,
        "呵呵，还好吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x109, 500)

    #C0165
    ChrTalk(
        0xFE,
        (
            "诺艾尔，你有时间的话，\x01",
            "要多和家里联络啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "妈妈和芙兰都很\x01",
            "担心你哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x109,
        (
            "#0506F妈、妈妈你可真是的……\x01",
            "在大家的面前，别说这么让人难为情的话嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x103,
        "#0200F一向干练的诺艾尔小姐也无所适从了呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2DF5")

    label("loc_2D87")


    #C0169
    ChrTalk(
        0xFE,
        (
            "诺艾尔，知道了吗？\x01",
            "今后可要多和家里联系呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x109,
        (
            "#0506F不用重复这么多次，\x01",
            "这种事情我也明白啊，真是的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DF5")

    Jump("loc_3CCF")

    label("loc_2DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2F5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ED4")

    #C0171
    ChrTalk(
        0xFE,
        (
            "在纪念庆典最终日的晚上，\x01",
            "我们和莎丽娜一家一起\x01",
            "开了个晚餐会。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "可是，芙兰好像是为了\x01",
            "帮助遇到困难的游客，\x01",
            "直到很晚才回来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "我还在想，她是不是找到了男朋友，\x01",
            "所以觉得有点高兴呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2F59")

    label("loc_2ED4")


    #C0174
    ChrTalk(
        0xFE,
        (
            "在纪念庆典的最终日，\x01",
            "芙兰好像去帮助遇到困难的游客了。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "我这女儿也到年龄了，\x01",
            "要是能赶快找到一个男朋友，\x01",
            "我也就可以放心了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F59")

    Jump("loc_3CCF")

    label("loc_2F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2FCF")

    #C0176
    ChrTalk(
        0xFE,
        (
            "说起来，莎丽娜那个\x01",
            "稍大一点的弟弟\x01",
            "今天好像会回家呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "机会难得，不如叫他们\x01",
            "一起来吃饭吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CCF")

    label("loc_2FCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3058")

    #C0178
    ChrTalk(
        0xFE,
        (
            "趁着大家去看游行，我跑到空荡荡的\x01",
            "百货店里完成了采购。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "游行结束时的壮观\x01",
            "场面也没有错过……\x01",
            "呵呵，计划非常成功啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CCF")

    label("loc_3058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_30FB")

    #C0180
    ChrTalk(
        0xFE,
        (
            "嗯，今天是第四天了啊……\x01",
            "有游行呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "趁着大家都在关注游行，\x01",
            "不如去百货店里买东西好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "大家都不知道，游行期间的百货店\x01",
            "可是个好地方啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CCF")

    label("loc_30FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_317A")

    #C0183
    ChrTalk(
        0xFE,
        (
            "那么，我也去逛逛\x01",
            "纪念庆典吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "庆典第一天，诺艾尔和芙兰\x01",
            "在港湾区玩得很开心呢。\x01",
            "不然我也稍微去看看好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CCF")

    label("loc_317A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_32E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3245")

    #C0185
    ChrTalk(
        0xFE,
        (
            "诺艾尔和芙兰\x01",
            "昨天回家了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "她们两个人晚上一起\x01",
            "去港湾区观赏活动了……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "姐妹两人的感情一直都是这么好呢。\x01",
            "要总是这样，男人们根本就没有\x01",
            "介入的余地，很难接近她们呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_32E3")

    label("loc_3245")


    #C0188
    ChrTalk(
        0xFE,
        (
            "诺艾尔和芙兰一直都是一对\x01",
            "感情相当要好的姐妹，\x01",
            "平时总是在一起玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "要是一直这样下去，\x01",
            "男人们就很难接近她们了吧。\x01",
            "姐妹两人的恋爱之路似乎都会很艰难呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32E3")

    Jump("loc_3CCF")

    label("loc_32E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_342E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33BE")

    #C0190
    ChrTalk(
        0xFE,
        (
            "说起来，诺艾尔好像说过，\x01",
            "要在纪念庆典的\x01",
            "第一天回家呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "芙兰她每天都唠叨着\x01",
            "『期待下个月』，『期待下个月』，\x01",
            "真是吵死人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "……呵呵，不过她们感情如此要好，\x01",
            "真是令人高兴呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3429")

    label("loc_33BE")


    #C0193
    ChrTalk(
        0xFE,
        (
            "诺艾尔好像要在纪念庆典\x01",
            "的第一天回来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "警备队应该也很忙的，\x01",
            "她这个休假，不会是\x01",
            "勉强争取来的吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3429")

    Jump("loc_3CCF")

    label("loc_342E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_358F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F3")

    #C0195
    ChrTalk(
        0xFE,
        (
            "我以前是个经营露天店的商人，\x01",
            "就在那边的那条街上做买卖，生意特别好。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "我当年开店的那个位置，\x01",
            "现在已经被库隆克继承了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        "呵呵，真庆幸他是个热衷于经商的孩子。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_358A")

    label("loc_34F3")


    #C0198
    ChrTalk(
        0xFE,
        (
            "我当年开店的那个地方，\x01",
            "现在已经被库隆克继承了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "露天店商人退休之后，曾经开店的地段\x01",
            "就留给下一代露天店商人继承。\x01",
            "这是露天市场的传统风俗哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_358A")

    Jump("loc_3CCF")

    label("loc_358F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_363C")

    #C0200
    ChrTalk(
        0xFE,
        (
            "那么，今天就是帮忙照看\x01",
            "尤格特的日子了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "机会难得，我一定要施展\x01",
            "最佳厨艺，好好招待他。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "如果到时食材还有剩余，就用来\x01",
            "给芙兰做晚饭就好了，呵呵。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CCF")

    label("loc_363C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3774")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3712")

    #C0203
    ChrTalk(
        0xFE,
        (
            "最近，在唐古拉姆门工作的\x01",
            "诺艾尔寄来了信呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "信中的内容虽然都只是一些\x01",
            "乱七八糟的小事情，\x01",
            "不过，能看出她很有精神呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "那个孩子平时很少给家里\x01",
            "寄信，所以我和芙兰都很\x01",
            "担心她呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_376F")

    label("loc_3712")


    #C0206
    ChrTalk(
        0xFE,
        (
            "诺艾尔平时很少\x01",
            "和家里联络呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "算了，身为上士，\x01",
            "终究不能将太多时间\x01",
            "用于处理私事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_376F")

    Jump("loc_3CCF")

    label("loc_3774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3831")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3791")
    Call(0, 11)
    Jump("loc_382C")

    label("loc_3791")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_3814")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_37AF")
    Call(0, 11)
    Jump("loc_380F")

    label("loc_37AF")


    #C0208
    ChrTalk(
        0xC,
        (
            "我想给隔壁那个小弟弟\x01",
            "念书听，所以就把书\x01",
            "借来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xC,
        (
            "如果有机会，\x01",
            "你们不妨也读读看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_380F")

    Jump("loc_382C")

    label("loc_3814")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_3829")
    Call(0, 21)
    Jump("loc_382C")

    label("loc_3829")

    Call(0, 11)

    label("loc_382C")

    Jump("loc_3CCF")

    label("loc_3831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_38EE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_384E")
    Call(0, 12)
    Jump("loc_38E9")

    label("loc_384E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_38D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_386C")
    Call(0, 12)
    Jump("loc_38CC")

    label("loc_386C")


    #C0210
    ChrTalk(
        0xC,
        (
            "我想给隔壁那个小弟弟\x01",
            "念书听，所以就把书\x01",
            "借来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xC,
        (
            "如果有机会，\x01",
            "你们不妨也读读看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_38CC")

    Jump("loc_38E9")

    label("loc_38D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_38E6")
    Call(0, 21)
    Jump("loc_38E9")

    label("loc_38E6")

    Call(0, 12)

    label("loc_38E9")

    Jump("loc_3CCF")

    label("loc_38EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_39AB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_390B")
    Call(0, 13)
    Jump("loc_39A6")

    label("loc_390B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_398E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3929")
    Call(0, 13)
    Jump("loc_3989")

    label("loc_3929")


    #C0212
    ChrTalk(
        0xC,
        (
            "我想给隔壁那个小弟弟\x01",
            "念书听，所以就把书\x01",
            "借来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xC,
        (
            "如果有机会，\x01",
            "你们不妨也读读看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_3989")

    Jump("loc_39A6")

    label("loc_398E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_39A3")
    Call(0, 21)
    Jump("loc_39A6")

    label("loc_39A3")

    Call(0, 13)

    label("loc_39A6")

    Jump("loc_3CCF")

    label("loc_39AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3BA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B18")

    #C0214
    ChrTalk(
        0xFE,
        (
            "我的女儿在警察局总部\x01",
            "从事一种叫做『接线员』\x01",
            "的工作哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "我对那种新兴事物\x01",
            "实在是没有多少了解。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "每次听她给我讲述工作内容时，\x01",
            "我都听得一头雾水，稀里糊涂的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B10")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0217
    ChrTalk(
        0x101,
        "#0005F（哎，莫非……）\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x102,
        "#0100F（看上去，这位阿姨好像是芙兰小姐的母亲呢。）\x02",
    )

    CloseMessageWindow()

    label("loc_3B10")

    SetScenarioFlags(0x0, 3)
    Jump("loc_3B9E")

    label("loc_3B18")


    #C0219
    ChrTalk(
        0xFE,
        (
            "我的女儿在警察局总部\x01",
            "从事一种叫做『接线员』\x01",
            "的工作哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "至于她的工作内容，\x01",
            "虽然让她给我说明了好几次，\x01",
            "但我还是听得似懂非懂。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B9E")

    Jump("loc_3CCF")

    label("loc_3BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C6F")

    #C0221
    ChrTalk(
        0xFE,
        "我有两个女儿呢。\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "姐姐在警备队工作，\x01",
            "妹妹在警察局工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "呵呵，两个人都这么有出息，\x01",
            "我这个当妈妈的可真是走运啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#0005F（警察局……莫非\x01",
            "  是我们认识的人吗？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3CCF")

    label("loc_3C6F")


    #C0225
    ChrTalk(
        0xFE,
        (
            "我的两个女儿都很出色，\x01",
            "分别在警备队和警察局工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "呵呵，我这个当妈妈的\x01",
            "可真是走运啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CCF")

    SetScenarioFlags(0x71, 6)
    TalkEnd(0xFE)
    Return()

    # Function_10_296C end

    def Function_11_3CD6(): pass

    label("Function_11_3CD6")


    #C0227
    ChrTalk(
        0xFE,
        (
            "今天受莎丽娜的委托，\x01",
            "要代替她照看尤格特。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "听说她为了寻找那个大一点的弟弟，\x01",
            "去了旧城区……\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        "那个地方的治安很差，有点担心她啊。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_11_3CD6 end

    def Function_12_3D63(): pass

    label("Function_12_3D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E5F")

    #C0230
    ChrTalk(
        0xFE,
        (
            "住在对门的莎丽娜\x01",
            "为了支撑起家庭，\x01",
            "一个人努力地工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "年纪轻轻的，可真了不起。\x01",
            "实在是让人敬佩啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "芙兰虽然当上了警察局的接待员，\x01",
            "工作非常努力出色，\x01",
            "而且也到了可以离家自立的年纪……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "但那个孩子，非常\x01",
            "容易感到寂寞呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3ED9")

    label("loc_3E5F")


    #C0234
    ChrTalk(
        0xFE,
        (
            "别看芙兰平时很开朗，\x01",
            "她其实非常容易感到寂寞呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "她必须要向对门的莎丽娜好好学习，\x01",
            "尽量让自己变得更加成熟自立啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ED9")

    Return()

    # Function_12_3D63 end

    def Function_13_3EDA(): pass

    label("Function_13_3EDA")


    #C0236
    ChrTalk(
        0xFE,
        (
            "芙兰在警察局应该\x01",
            "工作得很努力吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "呵呵，别看那孩子平时有点脱线，\x01",
            "但对待工作却非常认真努力，\x01",
            "应该不必担心她吧。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_13_3EDA end

    def Function_14_3F56(): pass

    label("Function_14_3F56")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3FB6")

    #C0238
    ChrTalk(
        0xFE,
        "姐姐，没事吧……？\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "不，那个……\x01",
            "我们家离港湾公园很近，\x01",
            "所以有点担心啦……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FB6")

    TalkEnd(0xFE)
    Return()

    # Function_14_3F56 end

    def Function_15_3FBA(): pass

    label("Function_15_3FBA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_41CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40CE")
    SetChrName("")

    #A0240
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔带着一脸认真的神情，\x01",
            "来回打量鞋架上的多款运动鞋。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0241
    ChrTalk(
        0xE,
        (
            "#0801F那么，谨慎起见，\x01",
            "还是换上我最珍藏的那双\x01",
            "运动靴吧。\x02\x03",

            "#0803F嗯～这双纪念版\x01",
            "更加轻便合脚，但是那双\x01",
            "限定版却更加结实……\x02\x03",

            "#0802F两双都很令人满意，\x01",
            "真是难以抉择啊～\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 5)
    Jump("loc_41CD")

    label("loc_40CE")


    #C0242
    ChrTalk(
        0xE,
        (
            "#0809F啊哈哈，由于发生了那起\x01",
            "黑手党事件，所以市内的状况也开始不稳定了，\x01",
            "谨慎起见，还是要检查一下装备啊。\x02\x03",

            "#0802F罗伊德，你们最好也\x01",
            "选择一双合脚的好鞋子哦。\x02\x03",

            "#0804F当然，我推荐斯托雷加公司的产品哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x101,
        "#0012F（她是斯托雷加公司的忠实支持者吗……？）\x02",
    )

    CloseMessageWindow()

    label("loc_41CD")

    TalkEnd(0xFE)
    Return()

    # Function_15_3FBA end

    def Function_16_41D1(): pass

    label("Function_16_41D1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4265")
    Jump("loc_42AF")

    label("loc_4265")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4285")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_42AF")

    label("loc_4285")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_42A5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_42AF")

    label("loc_42A5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_42AF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4560")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44AD")

    #C0244
    ChrTalk(
        0x10,
        "#0900F啊，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xF,
        "#0809F你们好啊～罗伊德诸位！\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#0005F你们好……\x01",
            "哎，莫非……\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x102,
        (
            "#0105F这个房间就是\x01",
            "你们的……？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xF,
        (
            "#0804F嗯！是我们在克洛斯贝尔\x01",
            "暂时租住的房间。\x02\x03",

            "#0802F虽然白天基本都不会待在房间里，\x01",
            "不过，有机会的话，欢迎来玩哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#0002F啊，好的……\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x103,
        (
            "#0200F（最后也没搞清楚啊，\x01",
            "  这两个人究竟是什么关系呢？）\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x104,
        (
            "#0303F（虽然姓氏好像是一样的，\x01",
            "  但看起来也并不像是兄妹呢……）\x02\x03",

            "#0305F（哇，难道会是夫妇吗……！？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x92, 5)
    Jump("loc_4560")

    label("loc_44AD")


    #C0252
    ChrTalk(
        0xF,
        (
            "#0802F那么，我们就赶快开始工作吧，\x01",
            "虽然都已经有点晚了。\x02\x03",

            "#0809F在克洛斯贝尔，每天都会\x01",
            "接到大量的委托任务呢，\x01",
            "实在是超有挑战性啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        "#0012F（她的表情看上去非常满意啊……）\x02",
    )

    CloseMessageWindow()

    label("loc_4560")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_41D1 end

    def Function_17_4568(): pass

    label("Function_17_4568")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_45FC")
    Jump("loc_4646")

    label("loc_45FC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_461C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4646")

    label("loc_461C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_463C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4646")

    label("loc_463C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4646")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_4856")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4800")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_4742")

    #C0254
    ChrTalk(
        0x101,
        (
            "#0005F咦，约修亚。\x01",
            "从协会回来了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x10,
        (
            "#0900F啊，是的。\x01",
            "我们暂时先解散了。\x02\x03",

            "#0903F看样子，报复行动\x01",
            "好像并不会马上展开呢。\x02\x03",

            "#0901F但我们仍然大意不得，\x01",
            "所以大家都要在市内待命。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F8")

    label("loc_4742")


    #C0256
    ChrTalk(
        0x10,
        (
            "#0900F为了防范黑手党之间的内斗，\x01",
            "我们都要在协会内待命，\x01",
            "不过眼下先暂时解散了。\x02\x03",

            "#0903F看样子，报复行动\x01",
            "好像并不会马上展开呢。\x02\x03",

            "#0901F但我们仍然大意不得，\x01",
            "所以大家要在市内待命。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47F8")

    SetScenarioFlags(0x0, 6)
    Jump("loc_4851")

    label("loc_4800")


    #C0257
    ChrTalk(
        0x10,
        (
            "#0903F黑手党团伙之间的争斗吗……\x02\x03",

            "#0901F要是能防患于未然，\x01",
            "就再好不过了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4851")

    Jump("loc_4A97")

    label("loc_4856")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4A97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4871")
    Call(0, 16)
    Jump("loc_4A97")

    label("loc_4871")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49F0")

    #C0258
    ChrTalk(
        0x104,
        (
            "#0303F（喂，帅哥……）\x02\x03",

            "#0301F（你和艾丝蒂尔\x01",
            "  之间到底是什么样\x01",
            "  的关系啊？）\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x10,
        (
            "#0905F（啊……\x01",
            "  我们是义姐弟。）\x02\x03",

            "#0910F（那个，但同时也是\x01",
            "  恋人关系啦。）\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x104,
        (
            "#0306F（呜啊……\x01",
            "  果然是这样啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x103,
        "#0204F（谜底总算是揭开了呢。）\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        (
            "#0000F（不过…又是家人，\x01",
            "  又是恋人吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x102,
        (
            "#0109F（呵呵，这样一来，就不难理解\x01",
            "  他们的配合为何会如此默契了。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4A97")

    label("loc_49F0")


    #C0264
    ChrTalk(
        0x10,
        (
            "#0901F说起来……\x01",
            "黑手党的军犬事件\x01",
            "好像也相当棘手吧？\x02\x03",

            "#0902F虽然有各种各样的困难……\x01",
            "但我们互相加油吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        (
            "#0002F……嗯。\x01",
            "你能这么说，\x01",
            "对我们实在是很大的鼓励。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A97")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_4568 end

    def Function_18_4A9F(): pass

    label("Function_18_4A9F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AB4")
    Call(0, 19)
    Jump("loc_4B69")

    label("loc_4AB4")


    #C0266
    ChrTalk(
        0x11,
        (
            "#11P#6405F说起来，今天晚上，\x01",
            "姐姐就该回来了。\x02\x03",

            "#6409F上次全家聚在一起吃晚饭，\x01",
            "好像已经是十天之前的事情了呢。\x02\x03",

            "今天能和姐姐一起吃饭，而且还见到\x01",
            "了小琪雅，真是最棒的休息日啊～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B69")

    TalkEnd(0xFE)
    Return()

    # Function_18_4A9F end

    def Function_19_4B6D(): pass

    label("Function_19_4B6D")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1050, 1500, -53430, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(17330, 0)
    SetChrPos(0x101, -400, 30, -52100, 180)
    SetChrPos(0xEF, -1600, 30, -52500, 135)
    SetChrPos(0x153, -1500, 30, -53770, 90)
    SetChrSubChip(0x11, 0x0)
    OP_93(0x11, 0x87, 0x0)
    OP_0D()

    #C0267
    ChrTalk(
        0x153,
        "#6P#1105F啊，是芙兰～！\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x11, 0x153, 500)

    #C0268
    ChrTalk(
        0x11,
        "#11P#6405F啊，小琪雅！？\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x101,
        (
            "#5P#0002F是吗……\x01",
            "这里就是芙兰的家啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C9A")

    #C0270
    ChrTalk(
        0x102,
        "#6P#0102F今天休息吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4CF5")

    label("loc_4C9A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CCA")

    #C0271
    ChrTalk(
        0x103,
        "#6P#0202F今天休假呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4CF5")

    label("loc_4CCA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CF5")

    #C0272
    ChrTalk(
        0x104,
        "#6P#0300F今天放假啊？\x02",
    )

    CloseMessageWindow()

    label("loc_4CF5")

    TurnDirection(0x11, 0xEF, 500)

    #C0273
    ChrTalk(
        0x11,
        (
            "#11P#6406F是呀～\x01",
            "自纪念庆典以来，\x01",
            "总算能得到休假了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x153, 500)
    Sleep(300)

    #C0274
    ChrTalk(
        0x11,
        (
            "#11P#6409F──可是可是！\x01",
            "真没想到小琪雅\x01",
            "会来看我啊～！\x02\x03",

            "#6400F以前只通过终端说过话，\x01",
            "这好像还是第一次见面吧？\x01",
            "……欢迎来我家玩哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x153,
        (
            "#6P#1100F嗯。\x02\x03",

            "#1110F不过，芙兰现在穿着的衣服，\x01",
            "和在终端上看到的不一样呢～\x02\x03",

            "#1109F嘿嘿嘿，这件粉色的衣服\x01",
            "真是特别可爱呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0276
    ChrTalk(
        0x11,
        (
            "#11P#6409F啊，谢谢夸奖～\x02\x03",

            "#6401F……小琪雅才可爱呢，\x01",
            "比在终端屏幕上看到的样子\x01",
            "还要可爱好多哦……\x02\x03",

            "#6406F太、太可爱了～超级可爱～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x11)
    TurnDirection(0x11, 0x101, 500)
    Sleep(300)

    #C0277
    ChrTalk(
        0x11,
        (
            "#11P#6401F罗、罗伊德警官！\x01",
            "我也想和小琪雅\x01",
            "一起散步！\x02\x03",

            "#6406F啊啊～请你们也带我\x01",
            "一起去吧～！\x02",
        )
    )

    CloseMessageWindow()
    Sound(892, 0, 100, 0)
    OP_63(0x11, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_64(0x11)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5005")

    #C0278
    ChrTalk(
        0x102,
        (
            "#6P#0109F芙、芙兰小姐……\x01",
            "你稍微冷静一点啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5083")

    label("loc_5005")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_504C")

    #C0279
    ChrTalk(
        0x103,
        (
            "#6P#0203F咳咳……芙兰小姐。\x01",
            "请稍微冷静一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5083")

    label("loc_504C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5083")

    #C0280
    ChrTalk(
        0x104,
        "#6P#0309F冷、冷静一下啦，小芙兰。\x02",
    )

    CloseMessageWindow()

    label("loc_5083")


    #C0281
    ChrTalk(
        0x101,
        (
            "#5P#0012F不、不好意思啊，\x01",
            "我们马上还要去其它地方呢……\x02\x03",

            "#0002F下次有机会，\x01",
            "再满足你的愿望吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x11,
        (
            "#11P#6401F呜呜……\x01",
            "约好了哦～！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x153, 500)
    Sleep(300)

    #C0283
    ChrTalk(
        0x11,
        (
            "#11P#6409F小琪雅！\x01",
            "我们下次要一起去散步哦？\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x153,
        "#6P#1109F嗯！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -1150, 30, -53080, 135)
    OP_66(0x1, 0x1)
    SetScenarioFlags(0xB6, 5)
    EventEnd(0x5)
    Return()

    # Function_19_4B6D end

    def Function_20_5175(): pass

    label("Function_20_5175")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 0xFF)
    OP_68(51230, 1420, 3870, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, 50930, 0, 3560, 0)
    SetChrPos(0x102, 52070, 0, 3560, 0)
    SetChrPos(0x103, 50930, 0, 2150, 0)
    SetChrPos(0x104, 52070, 0, 2150, 0)
    SetChrPos(0x8, 45830, -1840, 0, 0)
    SetChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_95(0x101, 51620, 0, 4810, 1000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)
    Sound(810, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    #A0285
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门上着锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(300)

    #C0286
    ChrTalk(
        0x101,
        (
            "#11P#0000F对不起！\x01",
            "请问有人在吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1400)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)

    #C0287
    ChrTalk(
        0x103,
        "#12P#0200F似乎感觉不到有人呢。\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x101,
        "#11P#0003F嗯，看起来是这样啊……\x02",
    )

    CloseMessageWindow()

    #N0289
    NpcTalk(
        0x8,
        "男性的声音",
        "哎呀，你们在干什么呢？\x02",
    )

    CloseMessageWindow()

    def lambda_5365():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5365)

    def lambda_5372():

        label("loc_5372")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_5372")

    QueueWorkItem2(0x102, 1, lambda_5372)

    def lambda_5384():

        label("loc_5384")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_5384")

    QueueWorkItem2(0x103, 1, lambda_5384)

    def lambda_5396():

        label("loc_5396")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_5396")

    QueueWorkItem2(0x104, 1, lambda_5396)
    OP_68(50380, 1420, 1610, 2000)
    OP_95(0x8, 49910, 0, 0, 2000, 0x0)
    OP_93(0x8, 0x2D, 0x1F4)
    Sleep(500)
    OP_6F(0x1)

    #C0290
    ChrTalk(
        0x8,
        "#12P那是个空房间。\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x104,
        "#11P#0305F噢，果然如此啊。\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x8,
        (
            "#12P嗯，房客大概是在\x01",
            "半个月之前搬走的。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x8,
        (
            "#12P如果你们想入住，\x01",
            "就直接去和房东联系吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_5470():

        label("loc_5470")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_5470")

    QueueWorkItem2(0x101, 1, lambda_5470)
    OP_95(0x8, 51410, 30, -1640, 2000, 0x0)
    OP_95(0x8, 51410, 0, -7420, 2000, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    Sleep(300)
    Fade(500)
    OP_68(51230, 1420, 3870, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20900, 0)
    Sleep(100)

    def lambda_54F3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54F3)

    def lambda_5500():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5500)

    def lambda_550D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_550D)
    Sleep(300)

    #C0294
    ChrTalk(
        0x101,
        (
            "#5P#0003F看起来，那个东街的空房\x01",
            "应该就是指这里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x104,
        (
            "#0306F之前的住户搬家时，\x01",
            "难道没有提交正式的\x01",
            "乔迁通知吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x103,
        (
            "#12P#0200F说起来……市政厅的人\x01",
            "好像也说过『资料未必正确』\x01",
            "之类的话呢。\x02\x03",

            "#0206F原来是这么回事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x102,
        (
            "#0103F嗯……空房是\x01",
            "洋槐庄园的２０２号室啊……\x01",
            "（必须要记录清楚才行……）\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x3, 0x1, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56D8")

    #C0298
    ChrTalk(
        0x101,
        (
            "#0003F好，这样一来，好像已经把\x01",
            "三处空房全部确认完毕了……\x02\x03",

            "#0000F我们赶快回市政厅的\x01",
            "接待处报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x3, 0x1, 0x1E)
    Jump("loc_570B")

    label("loc_56D8")


    #C0299
    ChrTalk(
        0x101,
        (
            "#0000F好，那么我们就赶快\x01",
            "去检查其它的空房吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_570B")

    Sleep(200)
    SetChrPos(0x0, 51710, 0, 4590, 180)
    SetChrPos(0x1, 51710, 0, 4590, 180)
    SetChrPos(0x2, 51710, 0, 4590, 180)
    SetChrPos(0x3, 51710, 0, 4590, 180)
    ClearChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 48880, 30, -55000, 135)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 7)
    EventEnd(0x5)
    Return()

    # Function_20_5175 end

    def Function_21_5777(): pass

    label("Function_21_5777")

    EventBegin(0x0)
    Fade(500)
    OP_68(3230, 1530, -56000, 0)
    MoveCamera(62, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19760, 0)
    SetChrPos(0x101, 2610, 30, -55580, 135)
    SetChrPos(0x102, 4019, 0, -54690, 180)
    SetChrPos(0x103, 2360, 30, -54400, 135)
    SetChrPos(0x104, 3880, 0, -53400, 180)
    TurnDirection(0xC, 0x101, 0)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 6)), scpexpr(EXPR_END)), "loc_5844")

    #C0300
    ChrTalk(
        0x101,
        (
            "#6P#0000F那个，克拉莉丝女士。\x01",
            "可以稍微打扰您一下吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5874")

    label("loc_5844")


    #C0301
    ChrTalk(
        0x101,
        (
            "#6P#0000F那个……\x01",
            "请问您是克拉莉丝女士吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5874")


    #C0302
    ChrTalk(
        0xC,
        "#11P啊……找我有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        (
            "#6P#0003F嗯，其实是……\x01",
            "图书馆的管理员委托\x01",
            "我们来处理一点事情。\x02\x03",

            "#0000F克拉莉丝女士，\x01",
            "您在图书馆借的书\x01",
            "是不是还没有返还呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0304
    ChrTalk(
        0xC,
        (
            "#11P啊～啊～！\x01",
            "完全忘得干干净净了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xC,
        (
            "#11P这么一说，好像都已经\x01",
            "超过返还期限了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x103,
        (
            "#6P#0200F看样子，好像只是\x01",
            "不小心忘记了而已呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xC,
        (
            "#11P呵呵，上了年纪之后，\x01",
            "就总是忘东忘西啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xC,
        (
            "#11P老是这个样子，\x01",
            "可是会被诺艾尔批评的。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xC,
        (
            "#11P那个……\x01",
            "请稍微等一下哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_95(0xC, 2250, 0, -57250, 2000, 0x0)
    OP_95(0xC, -1980, 0, -57290, 2000, 0x0)
    OP_0D()
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 3660, 30, -56600, 315)
    FadeToBright(500, 0)
    OP_0D()

    #C0310
    ChrTalk(
        0xC,
        "#11P……嗯，就是这本。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0311
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('玛尔克与森林深处的魔女·上', 1)
    TurnDirection(0x102, 0x101, 500)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0312
    ChrTalk(
        0x102,
        "#11P#0105F啊，这本书……\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x104,
        "#5P#0305F怎么了，大小姐看过这本书吗？\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x102,
        (
            "#11P#0100F嗯。\x02\x03",

            "这是图书馆中借阅率最高的\x01",
            "一本著名童话哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xC,
        (
            "#11P隔壁的莎丽娜在外出\x01",
            "工作的时候，将她年幼的弟弟\x01",
            "拜托我照顾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xC,
        (
            "#11P那时我想念些书给他听，\x01",
            "所以就把这本书借来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xC,
        "#11P呵呵，他好像也听得很开心呢。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x101,
        (
            "#6P#0005F是吗……\x01",
            "（我也开始产生一点兴趣了呢……）\x02\x03",

            "#0000F嗯，那么，\x01",
            "非常感谢您的合作。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xC,
        "#11P哪里，你们辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xC,
        (
            "#11P以后我会对返还期限\x01",
            "多加注意的。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x5, 0x1, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D05")
    OP_29(0x5, 0x1, 0x1F)

    label("loc_5D05")

    SetChrPos(0x0, 2610, 30, -55580, 135)
    EventEnd(0x5)
    Return()

    # Function_21_5777 end

    def Function_22_5D19(): pass

    label("Function_22_5D19")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D42")
    Call(0, 20)
    Jump("loc_5E71")

    label("loc_5D42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E52")
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0321
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门上着锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0322
    ChrTalk(
        0x102,
        "#0100F这里可能也是空房吧……\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        (
            "#0000F不，也许只是住户\x01",
            "刚好不在家而已。\x01",
            "我们无法断定。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x103,
        (
            "#0200F根据资料上的记载，东街的空房\x01",
            "应该紧邻游击士协会的右侧。\x02\x03",

            "我们也许应该去那里的\x01",
            "民宅看一看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5E71")

    label("loc_5E52")

    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0325
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门上着锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5E71")

    TalkEnd(0xFF)
    Return()

    # Function_22_5D19 end

    def Function_23_5E75(): pass

    label("Function_23_5E75")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6146")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_610C")
    OP_4B(0x11, 0xFF)

    #C0326
    ChrTalk(
        0x101,
        "#0005F这个玩具熊是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x0, 500)
    Sleep(500)

    #C0327
    ChrTalk(
        0x11,
        (
            "#6400F啊，你说那孩子啊，\x01",
            "那可是我的知心朋友，小熊邦邦哦。\x02\x03",

            "#6409F嘿嘿嘿，很可爱吧？\x01",
            "某位非常重要的人也有个一样的哦～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x11, 500)
    Sleep(200)

    #C0328
    ChrTalk(
        0x153,
        (
            "#1109F真的哦！确实\x01",
            "非常可爱啊～！\x02\x03",

            "#1110F那个，芙兰～\x01",
            "邦邦几岁了呀？\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x11,
        (
            "#6409F邦邦三岁了哦！\x01",
            "……小琪雅果然也能\x01",
            "体会到邦邦的可爱之处啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x153, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_603B")

    #C0330
    ChrTalk(
        0x102,
        (
            "#0102F（这两个人还真是\x01",
            "  相当投缘啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60BA")

    label("loc_603B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_607D")

    #C0331
    ChrTalk(
        0x103,
        (
            "#0202F（这两个人真的是\x01",
            "  相当投缘呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60BA")

    label("loc_607D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60BA")

    #C0332
    ChrTalk(
        0x104,
        (
            "#0302F（这两个人还真是\x01",
            "  兴趣相投啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60BA")


    #C0333
    ChrTalk(
        0x101,
        (
            "#0004F（完全都看不出她们以前\x01",
            "  只通过终端说过话而已……）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_93(0x11, 0x87, 0x1F4)
    SetScenarioFlags(0xD1, 0)
    Jump("loc_6146")

    label("loc_610C")

    SetChrName("")

    #A0334
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是芙兰十分喜爱的玩具熊。\x01",
            "……名字好像叫邦邦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6522")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_642D")

    #C0335
    ChrTalk(
        0x109,
        "#0505F啊，这是……\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x102,
        "#0100F诺艾尔小姐，怎么了吗？\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x109,
        (
            "#0500F哈哈，这个玩具熊\x01",
            "是芙兰的。\x02\x03",

            "#0503F名字应该是叫邦邦，\x01",
            "十分得芙兰的喜爱呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 2)), scpexpr(EXPR_END)), "loc_626E")

    #C0338
    ChrTalk(
        0x104,
        (
            "#0300F嗯，诺艾尔上士也有个\x01",
            "一模一样的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x101,
        (
            "#0004F如此珍爱玩偶，还给它起了名字，\x01",
            "真的很符合芙兰的风格啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62E9")

    label("loc_626E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 0)), scpexpr(EXPR_END)), "loc_62E9")

    #C0340
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，说起来，\x01",
            "芙兰好像也说过这件事呢。\x02\x03",

            "#0004F如此珍爱玩偶，还给它起了名字，\x01",
            "真是很符合芙兰的风格啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63AB")

    #C0341
    ChrTalk(
        0x109,
        (
            "#0503F（……其、其实我也……\x01",
            "  有个一样的玩具熊。）\x02\x03",

            "#0508F（但实在是很难为情，说不出口呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x103,
        (
            "#0200F…………………………？\x01",
            "（我感觉诺艾尔上士\x01",
            "  好像有什么话想说呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6425")

    label("loc_63AB")


    #C0343
    ChrTalk(
        0x109,
        (
            "#0500F是啊……\x02\x03",

            "#0508F要是我也能像她这么有女孩子气……\x01",
            "唉呼……\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x103,
        (
            "#0200F（诺艾尔上士的心里\x01",
            "  好像有什么烦恼啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6425")

    SetScenarioFlags(0xD1, 1)
    Jump("loc_6522")

    label("loc_642D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_647C")
    SetChrName("")

    #A0345
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "芙兰十分喜爱的玩具熊\x01",
            "摆在这里。\x02\x03",

            "名字好像是叫邦邦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_6522")

    label("loc_647C")

    SetChrName("")

    #A0346
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是芙兰的玩具熊。\x01",
            "诺艾尔似乎有个一模一样的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0347
    ChrTalk(
        0x109,
        (
            "#0503F（我是不是也该给那个玩具熊\x01",
            "  起个名字呢……）\x02\x03",

            "#0506F（算了算了，这种行为\x01",
            "  毕竟还是太难为情了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6522")

    TalkEnd(0xFF)
    Return()

    # Function_23_5E75 end

    SaveToFile()

Try(main)
