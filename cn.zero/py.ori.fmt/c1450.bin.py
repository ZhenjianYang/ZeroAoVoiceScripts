from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1450.bin",                # FileName
        "c1450",                    # MapName
        "c1450",                    # Location
        0x0033,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 51, 0, 4, 0, 5],
    )

    BuildStringList((
        "c1450",                  # 0
        "坦特斯老人",             # 1
        "盖特纳",                 # 2
        "柯洛娜",                 # 3
        "利玛",                   # 4
        "梅尔斯",                 # 5
        "坦特斯老人",             # 6
        "米修",                   # 7
        "盖特纳",                 # 8
        "莉夏",                   # 9
        "看似议员的男人",         # 10
        "穿西装的男人",           # 11
        "男人的声音",             # 12
    ))

    AddCharChip((
        "chr/ch24000.itc",                   # 00
        "chr/ch24002.itc",                   # 01
        "chr/ch21000.itc",                   # 02
        "chr/ch21002.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch24402.itc",                   # 05
        "chr/ch22700.itc",                   # 06
        "chr/ch20700.itc",                   # 07
        "chr/ch26200.itc",                   # 08
        "chr/ch27700.itc",                   # 09
        "chr/ch27600.itc",                   # 0A
        "chr/ch23000.itc",                   # 0B
        "chr/ch24700.itc",                   # 0C
        "chr/ch05200.itc",                   # 0D
    ))

    DeclNpc(4269,    0,       -52159,  90,   261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(52340,   29,      959,     180,  261,  0x0, 0,   2,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(51200,   0,       54049,   0,    261,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(10270,   3500,    11050,   135,  261,  0x0, 0,   7,   0,   0,   2,   0,   13,  255,  0)
    DeclNpc(9609,    3500,    13869,   135,  389,  0x0, 0,   8,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-1399,   119,     -55000,  90,   389,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-46349,  200,     1899,    180,  261,  0x0, 0,   5,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(1549,    200,     -55159,  270,  389,  0x0, 0,   3,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-1639,   29,      56029,   0,    389,  0x0, 0,   13,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(3809,    0,       1059,    135,  389,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(2700,    0,       1490,    135,  389,  0x0, 0,   10,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(17899,   3500,    -39,     0,    126,  0x0, 0,   10,  0,   255, 255, 255, 255, 255,  0)

    DeclActor(17900,   3500,    -40,     1500,    17900,   4800,    -40,     0x007C, 0,  16, 0x0000)
    DeclActor(-140,    3500,    21470,   1500,    -140,    5000,    21470,   0x007C, 0,  29, 0x0000)

    ScpFunction((
        "Function_0_2DC",          # 00, 0
        "Function_1_394",          # 01, 1
        "Function_2_3BF",          # 02, 2
        "Function_3_3EA",          # 03, 3
        "Function_4_415",          # 04, 4
        "Function_5_6F2",          # 05, 5
        "Function_6_76D",          # 06, 6
        "Function_7_1815",         # 07, 7
        "Function_8_1969",         # 08, 8
        "Function_9_1A33",         # 09, 9
        "Function_10_2962",        # 0A, 10
        "Function_11_2AEB",        # 0B, 11
        "Function_12_3C4B",        # 0C, 12
        "Function_13_4BF9",        # 0D, 13
        "Function_14_560A",        # 0E, 14
        "Function_15_567F",        # 0F, 15
        "Function_16_5701",        # 10, 16
        "Function_17_5F52",        # 11, 17
        "Function_18_5F8B",        # 12, 18
        "Function_19_6099",        # 13, 19
        "Function_20_61C7",        # 14, 20
        "Function_21_667C",        # 15, 21
        "Function_22_6829",        # 16, 22
        "Function_23_6D03",        # 17, 23
        "Function_24_7314",        # 18, 24
        "Function_25_733C",        # 19, 25
        "Function_26_7378",        # 1A, 26
        "Function_27_73AA",        # 1B, 27
        "Function_28_73DC",        # 1C, 28
        "Function_29_776C",        # 1D, 29
    ))


    def Function_0_2DC(): pass

    label("Function_0_2DC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_31C"),
        (1, "loc_328"),
        (2, "loc_334"),
        (3, "loc_340"),
        (4, "loc_34C"),
        (5, "loc_358"),
        (6, "loc_364"),
        (SWITCH_DEFAULT, "loc_370"),
    )


    label("loc_31C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_328")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_334")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_340")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_34C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_358")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_364")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_370")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_37C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_393")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_393")

    Return()

    # Function_0_2DC end

    def Function_1_394(): pass

    label("Function_1_394")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BE")
    OP_94(0xFE, 0xC602, 0xFFFFF538, 0xCFDA, 0xF50, 0x3E8)
    Sleep(300)
    Jump("Function_1_394")

    label("loc_3BE")

    Return()

    # Function_1_394 end

    def Function_2_3BF(): pass

    label("Function_2_3BF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E9")
    OP_94(0xFE, 0x1CFC, 0x208A, 0x2FBC, 0x337C, 0x3E8)
    Sleep(300)
    Jump("Function_2_3BF")

    label("loc_3E9")

    Return()

    # Function_2_3BF end

    def Function_3_3EA(): pass

    label("Function_3_3EA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_414")
    OP_94(0xFE, 0xCC74, 0xBCCA, 0xD8C2, 0xC4C2, 0x3E8)
    Sleep(300)
    Jump("Function_3_3EA")

    label("loc_414")

    Return()

    # Function_3_3EA end

    def Function_4_415(): pass

    label("Function_4_415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_453")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, 10270, 3500, 13330, 315)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44E")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_44E")

    Jump("loc_6D0")

    label("loc_453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_466")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_6D0")

    label("loc_466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_474")
    Jump("loc_6D0")

    label("loc_474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_499")
    SetChrPos(0xB, 53980, 30, 49050, 135)
    BeginChrThread(0xB, 0, 0, 3)
    Jump("loc_6D0")

    label("loc_499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4AC")
    SetChrFlags(0xE, 0x80)
    Jump("loc_6D0")

    label("loc_4AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_4D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D3")
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D3")
    SetChrFlags(0x10, 0x10)

    label("loc_4D3")

    Jump("loc_6D0")

    label("loc_4D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_50B")
    SetChrPos(0xE, -48650, 200, 4460, 270)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_506")
    SetChrFlags(0x10, 0x10)

    label("loc_506")

    Jump("loc_6D0")

    label("loc_50B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_528")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_6D0")

    label("loc_528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_540")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_6D0")

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_56C")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_6D0")

    label("loc_56C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_57A")
    Jump("loc_6D0")

    label("loc_57A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5B4")
    SetChrPos(0x8, 10280, 3500, 14670, 180)
    SetChrPos(0xA, 10270, 3500, 13330, 0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    Jump("loc_6D0")

    label("loc_5B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_636")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x8, 3880, 0, -500, 45)
    SetChrPos(0xA, 10270, 3500, 13330, 315)
    SetChrPos(0xB, 53980, 30, 49050, 135)
    SetChrPos(0x11, 9270, 3500, 14320, 135)
    SetChrPos(0x12, 8210, 3500, 14680, 135)
    BeginChrThread(0xB, 0, 0, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_631")
    SetChrFlags(0xA, 0x10)

    label("loc_631")

    Jump("loc_6D0")

    label("loc_636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_65F")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x8, 5020, 0, -150, 315)
    Jump("loc_6D0")

    label("loc_65F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_66D")
    Jump("loc_6D0")

    label("loc_66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6A0")
    SetChrPos(0xB, 51970, 0, 53350, 315)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_69B")
    SetChrFlags(0xA, 0x10)

    label("loc_69B")

    Jump("loc_6D0")

    label("loc_6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_6BF")
    SetChrPos(0xA, 10060, 3500, 14220, 180)
    Jump("loc_6D0")

    label("loc_6BF")

    SetChrPos(0xA, 10060, 3500, 14220, 180)

    label("loc_6D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F1")
    Event(0, 23)

    label("loc_6F1")

    Return()

    # Function_4_415 end

    def Function_5_6F2(): pass

    label("Function_5_6F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70B")
    OP_10(0x0, 0x0)
    OP_10(0xD, 0x1)
    Jump("loc_711")

    label("loc_70B")

    OP_10(0x0, 0x1)
    OP_10(0xD, 0x0)

    label("loc_711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72D")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_744")

    label("loc_72D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_744")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_744")

    label("loc_744")

    ClearMapObjFlags(0x4, 0x10)
    OP_65(0x1, 0x1)
    SetMapObjFlags(0x2, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76C")
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_76C")

    Return()

    # Function_5_6F2 end

    def Function_6_76D(): pass

    label("Function_6_76D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_7E5")

    #C0001
    ChrTalk(
        0xFE,
        (
            "这幢公寓的空房\x01",
            "现在应该只有一间哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "嗯，是二楼最左边的那间。\x01",
            "如果有些在意的话，\x01",
            "就去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1811")

    label("loc_7E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_841")

    #C0003
    ChrTalk(
        0x8,
        (
            "那么，今天的晚饭\x01",
            "该吃什么好呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "不管发生什么事件，\x01",
            "饭总是要吃的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1811")

    label("loc_841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_97B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8C6")

    #C0005
    ChrTalk(
        0x8,
        (
            "从今天早上开始，那些不良少年们\x01",
            "好像就一直在寻找同伴呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "嗯，虽然事不关己，\x01",
            "但终归还是有些担心啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_976")

    label("loc_8C6")


    #C0007
    ChrTalk(
        0x8,
        (
            "从今天早上开始，那些不良少年们\x01",
            "好像就一直在寻找同伴呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "不过，既然是旧城区的年轻人，\x01",
            "大概只是跑到什么地方去玩了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "但至少应该把自己的行程\x01",
            "告诉同伴一声啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_976")

    Jump("loc_1811")

    label("loc_97B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A0C")

    #C0010
    ChrTalk(
        0x8,
        (
            "刚才去街上时，\x01",
            "被不良团伙的成员缠住了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "嗯……那个蓝头发的孩子\x01",
            "应该只是个新入伙的小弟而已，\x01",
            "但他的眼神莫名地凶狠呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1811")

    label("loc_A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_B3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A66")

    #C0012
    ChrTalk(
        0x8,
        (
            "那些不良团伙的成员\x01",
            "安分了不少呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        "终于可以和平相处了啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B35")

    label("loc_A66")


    #C0014
    ChrTalk(
        0x8,
        (
            "最近这一个月，那些不良团伙\x01",
            "的孩子们好像安分了不少呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "再也不像以前那样，\x01",
            "整天争斗吵闹个不停了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "不过……我听说他们的\x01",
            "内部关系变得很坏。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "你们几个，如果要在旧城区办事，\x01",
            "可要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_B35")

    Jump("loc_1811")

    label("loc_B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_C2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BAA")

    #C0018
    ChrTalk(
        0x8,
        (
            "在这个旧城区，没有哪个年轻人\x01",
            "比那个孩子更有出息了。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "呵呵，她可真是个好孩子呀。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C2A")

    label("loc_BAA")


    #C0020
    ChrTalk(
        0x8,
        (
            "今天早上，我在门口\x01",
            "突然遇到了莉夏。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "她说稍后要去和朋友\x01",
            "一起玩呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "呵呵，她的性格开朗又乐观，\x01",
            "真是个好孩子啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_C2A")

    Jump("loc_1811")

    label("loc_C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_CEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C9A")

    #C0023
    ChrTalk(
        0x8,
        (
            "今天就去见见\x01",
            "市长好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "呵呵，因为闭幕式既不是很挤，\x01",
            "而且还能免费参加哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE9")

    label("loc_C9A")


    #C0025
    ChrTalk(
        0x8,
        (
            "那么，今天就去参加\x01",
            "闭幕式好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "呵呵，我每年都会\x01",
            "去观看闭幕式的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_CE9")

    Jump("loc_1811")

    label("loc_CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_DC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D52")

    #C0027
    ChrTalk(
        0x8,
        (
            "虽然住在这种破旧的公寓中，\x01",
            "但我过得也算很安稳了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "真是不可思议啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_DBB")

    label("loc_D52")


    #C0029
    ChrTalk(
        0x8,
        (
            "我出去观看了游行，\x01",
            "真是走得我筋疲力尽啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "虽然住在这种破旧的公寓中，\x01",
            "但我过得也算很安稳了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_DBB")

    Jump("loc_1811")

    label("loc_DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_EC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E1A")

    #C0031
    ChrTalk(
        0x8,
        (
            "即使在我们旧城区居民看来，\x01",
            "麦克道尔市长也是一位杰出的人物呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC1")

    label("loc_E1A")


    #C0032
    ChrTalk(
        0x8,
        "麦克道尔市长也是一位杰出的人物啊。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "即使发生了那种事件，也仍然为了\x01",
            "克洛斯贝尔的政治而竭尽全力，\x01",
            "还将纪念庆典也顺利举办成功了。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        "真是位坚强刚毅的人啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_EC1")

    Jump("loc_1811")

    label("loc_EC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1020")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F3F")

    #C0035
    ChrTalk(
        0x8,
        (
            "一会不如去给考试的孩子\x01",
            "送些慰问品吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "如果附近的邻居们有什么困难，\x01",
            "我可无法视而不见啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101B")

    label("loc_F3F")


    #C0037
    ChrTalk(
        0x8,
        (
            "这所公寓内的住户们好像也\x01",
            "都很享受纪念庆典啊。\x01",
            "呵呵，不错不错。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    #C0038
    ChrTalk(
        0x8,
        "不对，好像把一个人给忘了。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "有个要考试的孩子\x01",
            "一个人在家里，\x01",
            "好像很寂寞呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "哎呀呀，一会就去给他\x01",
            "送点慰问品吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_101B")

    Jump("loc_1811")

    label("loc_1020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_10EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1091")

    #C0041
    ChrTalk(
        0x8,
        (
            "虽然是旧城区的居民，\x01",
            "但也想在庆典期间奢侈一番呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "必须要趁现在\x01",
            "多攒些私房钱啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E6")

    label("loc_1091")


    #C0043
    ChrTalk(
        0x8,
        (
            "我的私房钱应该是\x01",
            "放在这里的，嗯……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "呵呵，为了纪念庆典，\x01",
            "我正在存钱呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_10E6")

    Jump("loc_1811")

    label("loc_10EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_11CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1106")
    Call(0, 12)
    Jump("loc_11C9")

    label("loc_1106")

    TurnDirection(0xFE, 0x0, 0)

    #C0045
    ChrTalk(
        0xFE,
        (
            "莉夏那样的孩子\x01",
            "居然会住在旧城区，\x01",
            "真是出乎我的意料啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "哈哈哈，那群奸诈的可恶议员，\x01",
            "嘴上嘟嘟囔囔说个不停，\x01",
            "但最终还是打道回府了。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "这都是托那个性格和善的\x01",
            "孩子的福啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)

    label("loc_11C9")

    Jump("loc_1811")

    label("loc_11CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_12C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_124A")

    #C0048
    ChrTalk(
        0xFE,
        (
            "那些议员好像去了\x01",
            "柯洛娜那里啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "我们都已经习惯了，\x01",
            "总能应付过去……\x01",
            "柯洛娜没事吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12BF")

    label("loc_124A")


    #C0050
    ChrTalk(
        0xFE,
        (
            "从很久以前就一直有\x01",
            "重新开发旧城区的计划……\x01",
            "所以议员时不时就会前来骚扰。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "希望柯洛娜能把\x01",
            "他们应付过去啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BF")

    Jump("loc_1811")

    label("loc_12C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_132C")

    #C0052
    ChrTalk(
        0xFE,
        (
            "（哎呀呀，又有议员\x01",
            "  来骚扰了啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "（动不动就来烦人……\x01",
            "  想办法应付过去吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1811")

    label("loc_132C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_138B")

    #C0054
    ChrTalk(
        0x8,
        "今天也是个好天气啊。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "不然就去东街看看，\x01",
            "到店里拿点他们不要的东西好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1811")

    label("loc_138B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_13E3")

    #C0056
    ChrTalk(
        0x8,
        (
            "听说有一个\x01",
            "年轻女孩搬来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "也许和我一样，\x01",
            "是个无亲无故的人吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1811")

    label("loc_13E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1517")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_144C")

    #C0058
    ChrTalk(
        0x8,
        (
            "我已经在这旧城区\x01",
            "住了六十年了。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "事到如今，也不想再\x01",
            "搬到其它地方生活了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1512")

    label("loc_144C")


    #C0060
    ChrTalk(
        0x8,
        (
            "我已经在这旧城区\x01",
            "住了六十年了。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "呵呵，在那些最近新建起来的\x01",
            "商业街，欢乐街出现之前，\x01",
            "这一带也是充满活力的。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "而现在这里简直算是被政府\x01",
            "彻底抛弃的地方了，\x01",
            "但即使如此，我也没打算离开。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1512")

    Jump("loc_1811")

    label("loc_1517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1675")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_15BA")

    #C0063
    ChrTalk(
        0x8,
        (
            "在旧城区生活的人们，\x01",
            "都有着各自的苦衷。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "但谁都不会被排斥，这就是旧城区的特色。不过，\x01",
            "正因为居民鱼龙混杂，这里时常会发生许多纠纷。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1670")

    label("loc_15BA")


    #C0065
    ChrTalk(
        0x8,
        (
            "正在找工作的失业者，\x01",
            "或者是被人追债的破落户……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "在这旧城区之中，\x01",
            "也有很多来自外国的异乡人。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "不过，只要生活在这里，大家就都是同伴。\x01",
            "大家要相互支撑，和睦地生活下去。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1670")

    Jump("loc_1811")

    label("loc_1675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_1739")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16CB")

    #C0068
    ChrTalk(
        0x8,
        (
            "都是生活在旧城区的伙伴嘛。\x01",
            "希望可以相处得稍微和睦一点啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1734")

    label("loc_16CB")


    #C0069
    ChrTalk(
        0x8,
        (
            "哎呀呀，那些年轻人。\x01",
            "又开始打架了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "我虽然理解他们精力过剩，\x01",
            "但打架可不好啊，不能打架的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1734")

    Jump("loc_1811")

    label("loc_1739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_17C2")

    #C0071
    ChrTalk(
        0x8,
        (
            "这所公寓的面积\x01",
            "倒是很宽敞。\x01",
            "但光是宽敞也没用，墙上有很多开裂的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "看，站在这里，就能感觉\x01",
            "到从外面吹来的风吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1811")

    label("loc_17C2")


    #C0073
    ChrTalk(
        0x8,
        (
            "噢，今天的天气\x01",
            "可真不错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "从羽扇河流向这边的\x01",
            "空气真是清新怡人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1811")

    TalkEnd(0xFE)
    Return()

    # Function_6_76D end

    def Function_7_1815(): pass

    label("Function_7_1815")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_18A9")
    Jump("loc_18F3")

    label("loc_18A9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_18C9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18F3")

    label("loc_18C9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18E9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18F3")

    label("loc_18E9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18F3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_195E")

    #C0075
    ChrTalk(
        0xD,
        "你们也来喝点如何？\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xD,
        "呵呵，我这里有白薯烧酒哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1961")

    label("loc_195E")

    Call(0, 8)

    label("loc_1961")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_1815 end

    def Function_8_1969(): pass

    label("Function_8_1969")

    OP_4B(0xD, 0xFF)
    OP_4B(0xF, 0xFF)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xF, 0x0)

    #C0077
    ChrTalk(
        0xD,
        "总之，先干一杯吧。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xD,
        (
            "话说回来，莉夏应该\x01",
            "没法来喝酒了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xF,
        (
            "她在彩虹剧团\x01",
            "好像是第二主角……\x01",
            "哎呀，真是了不起呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xF,
        (
            "我以前一直都不知道，\x01",
            "都把她当作普通人来对待。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_8_1969 end

    def Function_9_1A33(): pass

    label("Function_9_1A33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1B44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1AD0")

    #C0081
    ChrTalk(
        0x9,
        (
            "话说，莉夏小姐好像\x01",
            "一直都很努力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "我也必须要拼命加油，\x01",
            "争取东山再起啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            "至少也要让自己买得起\x01",
            "彩虹剧团的门票啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B3F")

    label("loc_1AD0")


    #C0084
    ChrTalk(
        0x9,
        (
            "今天中午，莉夏慌慌张张地\x01",
            "从房间里跑出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        (
            "好像说是白天的公演要迟到了，\x01",
            "不知道有没有顺利开演呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1B3F")

    Jump("loc_295E")

    label("loc_1B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1C21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1BAD")

    #C0086
    ChrTalk(
        0x9,
        (
            "经济学果然很有意思啊。\x01",
            "我也希望……有朝一日可以重整旗鼓，\x01",
            "再次成为一名商人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C1C")

    label("loc_1BAD")


    #C0087
    ChrTalk(
        0x9,
        "我在百货店买到了经济杂志哦。\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "唔唔……这期的头条报道\x01",
            "是玛丽亚贝尔小姐的特辑啊，\x01",
            "好像很值得一读呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1C1C")

    Jump("loc_295E")

    label("loc_1C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1CEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1C6D")

    #C0089
    ChrTalk(
        0x9,
        (
            "嗯，今天就到好久都没\x01",
            "去过的百货店里买点东西吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CE5")

    label("loc_1C6D")


    #C0090
    ChrTalk(
        0x9,
        (
            "噢，今天好像就是那本\x01",
            "经济杂志的发刊日啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "我以前一直都定期购买阅读。\x01",
            "哈哈哈……不过现在已经\x01",
            "彻底落魄了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1CE5")

    Jump("loc_295E")

    label("loc_1CEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1DC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1D5F")

    #C0092
    ChrTalk(
        0x9,
        (
            "最近，和米修的关系\x01",
            "刚刚变得亲密起来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "所以很担心啊，\x01",
            "他是不是把身体搞坏了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DC2")

    label("loc_1D5F")


    #C0094
    ChrTalk(
        0x9,
        (
            "隔壁的米修\x01",
            "去乌尔斯拉医院了……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        (
            "他最近一直都在拼命学习呢，\x01",
            "说不定是把身体给累坏了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1DC2")

    Jump("loc_295E")

    label("loc_1DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1EE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1E39")

    #C0096
    ChrTalk(
        0x9,
        (
            "旧城区虽然不是什么坏地方，\x01",
            "但对小孩子来说，还是有些危险的。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        "你们可要保护好她啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EDD")

    label("loc_1E39")


    #C0098
    ChrTalk(
        0x9,
        (
            "呀……这么小的孩子\x01",
            "怎么来旧城区了？\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "你们几个，这可不行啊。\x01",
            "不能带小孩来这种地方。\x02\x03",

            "要是有什么困难的话，还是去游击士协会\x01",
            "或大圣堂之类的地方请求帮助吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1EDD")

    Jump("loc_295E")

    label("loc_1EE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2016")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1F48")

    #C0100
    ChrTalk(
        0x9,
        (
            "那么痛痛快快地大闹一场，\x01",
            "反而让人觉得酣畅淋漓啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        "总觉得干劲十足了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2011")

    label("loc_1F48")


    #C0102
    ChrTalk(
        0x9,
        (
            "昨天，正在和大家一起吃火锅呢，\x01",
            "那些不良少年们却突然开始赛跑了……\x01",
            "那么突然，真是让人大吃一惊。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "不过呢，那场精彩激烈的比赛\x01",
            "让我看得非常开心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "哈哈，偶尔来场那样的比赛\x01",
            "其实也不坏啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2011")

    Jump("loc_295E")

    label("loc_2016")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_210B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_207A")

    #C0105
    ChrTalk(
        0x9,
        (
            "毕竟，在旧城区过纪念庆典，\x01",
            "这好像还是第一次呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        "今年要怎么过呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2106")

    label("loc_207A")


    #C0107
    ChrTalk(
        0x9,
        "那么，纪念庆典要怎么过呢……\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        (
            "不然叫隔壁的\x01",
            "坦特斯先生一起\x01",
            "过来吃火锅吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        (
            "哈哈……考虑到我的钱包，\x01",
            "这应该是个最好的选择吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2106")

    Jump("loc_295E")

    label("loc_210B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_222D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2188")

    #C0110
    ChrTalk(
        0x9,
        (
            "我曾经也尝试过投机炒股……\x01",
            "但最后却失去了一切。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "相比之下，坦特斯先生\x01",
            "真是个脚踏实地的人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2228")

    label("loc_2188")


    #C0112
    ChrTalk(
        0x9,
        (
            "坦特斯先生确实是个\x01",
            "热心肠的好人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x9,
        (
            "在我以往的认识中，一提到在旧城区\x01",
            "长大的人，只会给人一种不好的印象……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "但他确实是一个\x01",
            "比我老实很多的好人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2228")

    Jump("loc_295E")

    label("loc_222D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2309")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_22A5")

    #C0115
    ChrTalk(
        0x9,
        (
            "只要在旧城区生活一段时间，就能\x01",
            "深刻体会到那些政府官员们有多虚伪。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        "哼，最好能快点回去。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2304")

    label("loc_22A5")


    #C0117
    ChrTalk(
        0x9,
        (
            "这群可恶的政府官员，只会在\x01",
            "这种时候虚张声势……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x9,
        (
            "平时却胆小如鼠，\x01",
            "连接近都不敢呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2304")

    Jump("loc_295E")

    label("loc_2309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_248A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2397")

    #C0119
    ChrTalk(
        0x9,
        (
            "已经好多年没见过哈罗德了啊……\x01",
            "面对已经如此落魄的我，\x01",
            "他的态度也没有任何改变。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x9,
        (
            "呵呵……真是让我\x01",
            "不禁落泪呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2485")

    label("loc_2397")


    #C0121
    ChrTalk(
        0x9,
        (
            "昨天，我和从前的商业伙伴，\x01",
            "一位名叫哈罗德的男人见了面。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x9,
        (
            "那时候，我以为他是个胆小懦弱的男人，\x01",
            "所以看不起他……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "时隔这么久，他一点都没变，\x01",
            "仍然还是那么温和随性啊，\x01",
            "我们一起去喝了一杯呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        (
            "呵呵……真是让我\x01",
            "不禁落泪呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2485")

    Jump("loc_295E")

    label("loc_248A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2572")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_24EF")

    #C0125
    ChrTalk(
        0x9,
        (
            "刚才差点被那些\x01",
            "不良少年纠缠住。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x9,
        (
            "真吓人，怎么会埋伏在\x01",
            "那种地方啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_256D")

    label("loc_24EF")


    #C0127
    ChrTalk(
        0x9,
        (
            "刚才差点被那些\x01",
            "不良少年纠缠住。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x9,
        (
            "真是吓人，所以我才讨厌\x01",
            "治安差的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x9,
        (
            "不过，他们为什么要埋伏在\x01",
            "公寓前面呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_256D")

    Jump("loc_295E")

    label("loc_2572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_267F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_25ED")

    #C0130
    ChrTalk(
        0x9,
        (
            "即使我如今已经如此落魄，\x01",
            "也仍然会购买经济杂志。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x9,
        (
            "呵呵……\x01",
            "虽然有些可笑，但还是无法放弃啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_267A")

    label("loc_25ED")


    #C0132
    ChrTalk(
        0x9,
        "这周的股市行情……嗯嗯。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        (
            "……真是难以启齿啊，直到现在，\x01",
            "我也仍然在购买经济杂志。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x9,
        (
            "经商时期养成的习惯，\x01",
            "现在已经戒不掉了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_267A")

    Jump("loc_295E")

    label("loc_267F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_274D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_26E2")

    #C0135
    ChrTalk(
        0x9,
        "我以前也是个商人……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "但如你所见，\x01",
            "现在已经落魄成这样了。\x01",
            "呵呵……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2748")

    label("loc_26E2")


    #C0137
    ChrTalk(
        0x9,
        (
            "这间公寓的房租\x01",
            "真是很便宜啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        (
            "像我这种穷苦潦倒的落魄之人，\x01",
            "总算也能有个地方住。\x01",
            "呜呜……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2748")

    Jump("loc_295E")

    label("loc_274D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2805")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_278D")

    #C0139
    ChrTalk(
        0x9,
        (
            "可恶，为什么我要\x01",
            "生活在旧城区呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2800")

    label("loc_278D")


    #C0140
    ChrTalk(
        0x9,
        (
            "我、我以前好歹也是一个\x01",
            "很成功的商人。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x9,
        (
            "不要将我和这些品行低劣，从小就生长在\x01",
            "旧城区的家伙们相提并论啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2800")

    Jump("loc_295E")

    label("loc_2805")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_2842")

    #C0142
    ChrTalk(
        0x9,
        (
            "外、外面好像很吵闹啊。\x01",
            "发生什么事情了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_295E")

    label("loc_2842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2897")

    #C0143
    ChrTalk(
        0x9,
        (
            "呜呜，可恶……\x01",
            "不应该变成这样啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x9,
        "我并没有做错什么啊……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_295E")

    label("loc_2897")


    #C0145
    ChrTalk(
        0x9,
        (
            "呜呜，可恶……\x01",
            "不应该变成这样啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x9,
        (
            "那支股票绝对应该买进！\x01",
            "我并没有做错什么啊……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0147
    ChrTalk(
        0x9,
        "你、你们是干什么的！？\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x9,
        (
            "难道是那些不良少年的伙伴吗？\x01",
            "赶、赶快给我出去！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_295E")

    TalkEnd(0xFE)
    Return()

    # Function_9_1A33 end

    def Function_10_2962(): pass

    label("Function_10_2962")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_29F6")
    Jump("loc_2A40")

    label("loc_29F6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2A16")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A40")

    label("loc_2A16")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A36")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A40")

    label("loc_2A36")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A40")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2AE0")

    #C0149
    ChrTalk(
        0xF,
        (
            "我连出去玩的钱都没有，\x01",
            "所以只能和公寓中的住户\x01",
            "一起吃火锅来庆祝。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xF,
        (
            "坦特斯先生真是个\x01",
            "很热心的好人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AE3")

    label("loc_2AE0")

    Call(0, 8)

    label("loc_2AE3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_2962 end

    def Function_11_2AEB(): pass

    label("Function_11_2AEB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B7F")
    Jump("loc_2BC9")

    label("loc_2B7F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B9F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BC9")

    label("loc_2B9F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BBF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BC9")

    label("loc_2BBF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BC9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2CBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2C42")

    #C0151
    ChrTalk(
        0xE,
        (
            "一到了傍晚，就特别想睡。\x01",
            "可恶，必须要再加把劲才行……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CBA")

    label("loc_2C42")

    SetChrSubChip(0xE, 0x0)

    #C0152
    ChrTalk(
        0xE,
        "（昏昏欲睡）……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0153
    ChrTalk(
        0xE,
        "呼啊……不、不能睡！\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xE,
        "这个时间段很容易犯困，是最危险的……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2CBA")

    Jump("loc_3C43")

    label("loc_2CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2DAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2D26")

    #C0155
    ChrTalk(
        0xE,
        (
            "今年的考试，\x01",
            "我绝对要通过……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xE,
        (
            "可恶的不良团伙，\x01",
            "能不能别再打扰我了！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DA8")

    label("loc_2D26")


    #C0157
    ChrTalk(
        0xE,
        "那些不良团伙的成员……最近安静得不正常啊。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xE,
        "……算了，这样最好不过了。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xE,
        (
            "只要别打扰我复习，\x01",
            "随便他们怎样都好……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2DA8")

    Jump("loc_3C43")

    label("loc_2DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2E2E")

    #C0160
    ChrTalk(
        0xE,
        (
            "我昨天去了乌尔斯拉医院，\x01",
            "和医生谈了很多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xE,
        (
            "呵呵……真是一次宝贵的体验啊。\x01",
            "越来越想考上\x01",
            "乌尔斯拉大学了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C43")

    label("loc_2E2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2F59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2EC5")

    #C0162
    ChrTalk(
        0xE,
        (
            "模拟考试的成绩非常不错。\x01",
            "只要继续这么努力下去，考上\x01",
            "乌尔斯拉大学的几率应该有８０％！\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xE,
        "很好～就照这种势头继续加油吧～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F54")

    label("loc_2EC5")

    SetChrSubChip(0xE, 0x0)

    #C0164
    ChrTalk(
        0xE,
        (
            "为了祈祷自己在模拟考试中取得成功，\x01",
            "一个人来干一杯吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xE,
        "（咕噜噜……）\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xE,
        (
            "好～就照这种势头继续努力，\x01",
            "准备挑战正式考试吧～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2F54")

    Jump("loc_3C43")

    label("loc_2F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_300F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2FA3")

    #C0167
    ChrTalk(
        0xE,
        (
            "哪怕只有今天一天也好……\x01",
            "拜托，饶了我吧……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_300A")

    label("loc_2FA3")


    #C0168
    ChrTalk(
        0xE,
        "外、外面怎么又开始吵闹起来了！？\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xE,
        (
            "饶了我吧……\x01",
            "明天就是乌尔斯拉大学\x01",
            "的模拟入学考试啊……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_300A")

    Jump("loc_3C43")

    label("loc_300F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_30E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3065")

    #C0170
    ChrTalk(
        0xE,
        (
            "离模拟考试还有两天……\x01",
            "虽然只是模拟考试，但绝对不能轻视！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30E2")

    label("loc_3065")


    #C0171
    ChrTalk(
        0xE,
        (
            "我中午出去吃饭，\x01",
            "结果被挤在人群中动弹不得。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xE,
        "费了九牛二虎之力才冲出包围。\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xE,
        (
            "真是的……\x01",
            "白白浪费了宝贵的时间。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_30E2")

    Jump("loc_3C43")

    label("loc_30E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3180")

    #C0174
    ChrTalk(
        0xE,
        (
            "坦特斯先生昨天\x01",
            "给我送来了烤鱼。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xE,
        (
            "……听说吃烤鱼好像可以\x01",
            "增强记忆力呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xE,
        (
            "嘿嘿、嘿嘿嘿……\x01",
            "这样的话，背诵应该就能进展顺利了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C43")

    label("loc_3180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_329C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_320B")

    #C0177
    ChrTalk(
        0xE,
        (
            "通过这次的模拟考试，\x01",
            "可以了解到考进大学的成功率。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xE,
        (
            "如果不能考到一个好分数……\x01",
            "我就会大受打击，一蹶不振的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3297")

    label("loc_320B")


    #C0179
    ChrTalk(
        0xE,
        "呼，那些可恶的不良少年们……\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xE,
        (
            "我昨天的学习\x01",
            "连一点进展都没有啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xE,
        (
            "不好，不好了……\x01",
            "纪念庆典结束之后，\x01",
            "马上就是模拟考试了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3297")

    Jump("loc_3C43")

    label("loc_329C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_334B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_330B")

    #C0182
    ChrTalk(
        0xE,
        "可恶，大家都在喧哗玩乐……\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xE,
        (
            "说心里话，我其实也\x01",
            "很想出去玩……\x01",
            "（狂写笔记）……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3346")

    label("loc_330B")


    #C0184
    ChrTalk(
        0xE,
        "……临考生是没有休假的。\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xE,
        "你能体会我的心情吧？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3346")

    Jump("loc_3C43")

    label("loc_334B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3463")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_33A5")

    #C0186
    ChrTalk(
        0xE,
        (
            "还、还是不行。\x01",
            "一背书，我就想睡觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xE,
        "我最不擅长背书了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_345E")

    label("loc_33A5")

    SetChrSubChip(0xE, 0x0)

    #C0188
    ChrTalk(
        0xE,
        "（昏昏欲睡）……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0189
    ChrTalk(
        0xE,
        (
            "呼啊……不、不能睡！\x01",
            "不自觉地就开始打瞌睡了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xE,
        (
            "三十分钟的小睡都会要了我的命啊！\x01",
            "在考前复习时期，打瞌睡是绝对不行的！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_345E")

    Jump("loc_3C43")

    label("loc_3463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_358B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_34D7")

    #C0191
    ChrTalk(
        0xE,
        (
            "乌尔斯拉大学虽然是医科大学，\x01",
            "但考试中也包括一般科目。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xE,
        "呜呜，要背的东西堆积如山啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3586")

    label("loc_34D7")


    #C0193
    ChrTalk(
        0xE,
        (
            "嗯……埃雷波尼亚帝国\x01",
            "的宰相奥斯本是一位\x01",
            "出身于军队的政治家……\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xE,
        (
            "主要的功绩是，下令铺设覆盖帝国\x01",
            "全域的铁路网以及……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xE,
        (
            "然后是『铁血政策』的宣言……\x01",
            "那个…………\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3586")

    Jump("loc_3C43")

    label("loc_358B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3648")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_35C3")

    #C0196
    ChrTalk(
        0xE,
        (
            "希望他们不要\x01",
            "打扰我学习啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3643")

    label("loc_35C3")


    #C0197
    ChrTalk(
        0xE,
        (
            "刚才有两位大人物\x01",
            "来确认居民信息了。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xE,
        (
            "哼，那种基本信息\x01",
            "应该都有记录才对吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xE,
        (
            "为什么还要特意过来\x01",
            "确认那种东西啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3643")

    Jump("loc_3C43")

    label("loc_3648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_37D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_36D9")

    #C0200
    ChrTalk(
        0xE,
        (
            "纪念庆典之后，我马上就要参加\x01",
            "乌尔斯拉大学的模拟入学考试。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xE,
        (
            "今年一定要好好加油，而且\x01",
            "在正式考试时也绝对要合格……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37D0")

    label("loc_36D9")


    #C0202
    ChrTalk(
        0xE,
        (
            "在纪念庆典之后，我马上要参加\x01",
            "乌尔斯拉大学的模拟入学考试。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xE,
        (
            "经过这次模拟考试，\x01",
            "就能明白自己的真正实力，\x01",
            "进而得以避免在正式考试时过于紧张了。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xE,
        (
            "……我去年没有参加模拟考试，\x01",
            "结果在正式考试中惨败。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xE,
        "所以今年必须要认真对待模拟考试。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_37D0")

    Jump("loc_3C43")

    label("loc_37D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_393A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38CB")

    #C0206
    ChrTalk(
        0xFE,
        (
            "外面的那些不良少年们，\x01",
            "好像看上了那位在不久前\x01",
            "搬进楼上房间的女孩。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "哈，不过那女孩确实非常可爱，\x01",
            "和她打招呼，她都会充满活力地\x01",
            "回应，真是个好女孩啊……⊥\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    #C0208
    ChrTalk(
        0xFE,
        (
            "……不不不！\x01",
            "怎么开始说那种事了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3935")

    label("loc_38CB")


    #C0209
    ChrTalk(
        0xFE,
        (
            "呼，不能再胡思乱想了，\x01",
            "必须要集中精神学习……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "那些不良团伙的成员真幸福啊……\x01",
            "永远都那么悠闲……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3935")

    Jump("loc_3C43")

    label("loc_393A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3A57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_39BB")

    #C0211
    ChrTalk(
        0xE,
        (
            "身为临考生，光靠父母给的生活费，\x01",
            "生活实在是很艰苦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xE,
        (
            "嗯～怎么办呢～……\x01",
            "这个月真是严峻啊～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A52")

    label("loc_39BB")


    #C0213
    ChrTalk(
        0xE,
        (
            "呜啊～这本参考书…\x01",
            "未免也太难了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xE,
        (
            "真想要本简单易懂\x01",
            "的参考书啊，\x01",
            "但是我手里没有闲钱。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xE,
        (
            "嗯～该怎么办呢～……\x01",
            "这个月真是严峻啊～……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3A52")

    Jump("loc_3C43")

    label("loc_3A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3B08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3A86")

    #C0216
    ChrTalk(
        0xE,
        "明年必须考上啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B03")

    label("loc_3A86")


    #C0217
    ChrTalk(
        0xE,
        (
            "我以考进乌尔斯拉大学为目标，\x01",
            "离开乡下，来到了这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xE,
        (
            "……不过，今年也没有考上呢。\x01",
            "我准备在明年的考试中再拼一拼。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3B03")

    Jump("loc_3C43")

    label("loc_3B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3B82")

    #C0219
    ChrTalk(
        0xE,
        (
            "不良团伙的那些家伙，\x01",
            "好像已经闹够了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xE,
        "嗯，这就好。\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xE,
        (
            "他们也应该像我一样努力学习，\x01",
            "考取大学。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C43")

    label("loc_3B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_3BB0")

    #C0222
    ChrTalk(
        0xE,
        "嗯？怎么突然安静下来了啊？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C43")

    label("loc_3BB0")


    #C0223
    ChrTalk(
        0xE,
        (
            "在这附近，有『剑蛇帮』\x01",
            "和『圣书会』这两个\x01",
            "不良团伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xE,
        "那些家伙总是吵闹个没完……\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xE,
        (
            "如果害我在这次的考试中再次落榜，\x01",
            "他们要怎么补偿我！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C43")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_2AEB end

    def Function_12_3C4B(): pass

    label("Function_12_3C4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3D11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3CC3")

    #C0226
    ChrTalk(
        0xA,
        (
            "已经很久没有全家一起围坐在饭桌前了。\x01",
            "呵呵……偶尔享受一下这样的日子，\x01",
            "我也感到很开心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D0C")

    label("loc_3CC3")


    #C0227
    ChrTalk(
        0xA,
        (
            "我老公好像\x01",
            "回来了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xA,
        (
            "太好了……\x01",
            "今天可以全家聚在餐桌前了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3D0C")

    Jump("loc_4BF5")

    label("loc_3D11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3DAC")

    #C0229
    ChrTalk(
        0xA,
        (
            "好像是建设日程要调整吧……\x01",
            "我老公今天也许\x01",
            "会提早回家呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xA,
        "呵呵，他刚才和我联络过了。\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xA,
        (
            "……今天就小试身手，\x01",
            "做一桌美味的料理吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BF5")

    label("loc_3DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3E78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3DFD")

    #C0232
    ChrTalk(
        0xA,
        (
            "莉夏小姐的工作\x01",
            "非常辛苦……\x01",
            "但每天早上都起得很早呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E73")

    label("loc_3DFD")


    #C0233
    ChrTalk(
        0xA,
        (
            "隔壁的莉夏小姐，\x01",
            "今天早上好像也是\x01",
            "很早就出门了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xA,
        (
            "比我老公起得还早呢……\x01",
            "不是还有两三个小时才到时间吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3E73")

    Jump("loc_4BF5")

    label("loc_3E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3FB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3F00")

    #C0235
    ChrTalk(
        0xA,
        (
            "听老公说，最近这段时间，就算赶赴工地，\x01",
            "也没有什么工作可以做。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFF)

    #C0236
    ChrTalk(
        0xA,
        (
            "……既然如此的话，\x01",
            "还不如干脆放假呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FAB")

    label("loc_3F00")


    #C0237
    ChrTalk(
        0xA,
        (
            "在自治州议会\x01",
            "召开期间，\x01",
            "大楼的建设工作被暂时搁置了。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xA,
        (
            "因为不知道预算能否到位，\x01",
            "所以只能暂且观望。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xA,
        (
            "我老公在施工现场工作……\x01",
            "所以最近的生活变得很没有规律。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3FAB")

    Jump("loc_4BF5")

    label("loc_3FB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_402F")

    #C0240
    ChrTalk(
        0xA,
        (
            "纪念庆典时虽然\x01",
            "都会有休假，\x01",
            "但我老公的工作还是和往常一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xA,
        (
            "如果他能多一些休息时间，\x01",
            "利玛也会很高兴的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BF5")

    label("loc_402F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_411E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_40AB")

    #C0242
    ChrTalk(
        0xA,
        (
            "我的丈夫难得有了休假。\x01",
            "这样一来，就可以全家一起度过纪念庆典了。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xA,
        "呵呵，我也变得期待起来了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4119")

    label("loc_40AB")


    #C0244
    ChrTalk(
        0xA,
        "利玛真是的，那么兴奋……\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xA,
        (
            "不过，我丈夫真是好久\x01",
            "都没有放过假了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xA,
        "呵呵，我也变得期待起来了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4119")

    Jump("loc_4BF5")

    label("loc_411E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_43EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4348")
    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    TurnDirection(0xA, 0x0, 0)
    TurnDirection(0x8, 0x0, 0)

    #C0247
    ChrTalk(
        0xA,
        (
            "今天也有议员跑到这里，\x01",
            "气势汹汹地来刁难我们……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xA,
        (
            "就在这时，住在隔壁的莉夏小姐\x01",
            "正好经过。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xA,
        (
            "莉夏小姐笑容满面的与他们打过招呼之后，\x01",
            "那些议员当场就圆睁双眼，\x01",
            "连话都说不出了。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x8,
        (
            "那些家伙当时的那种表情，\x01",
            "真是够夸张啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "莉夏就是那个彩虹剧团\x01",
            "的团员啊。\x01",
            "……他们自然会相当吃惊吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 500)
    Sleep(300)

    #C0252
    ChrTalk(
        0xA,
        (
            "呵呵，然后嘴里嘟嘟囔囔个不停……\x01",
            "今天终归还是打道回府了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 500)
    Sleep(300)

    #C0253
    ChrTalk(
        0x8,
        (
            "嗯，那些令人生厌的议员\x01",
            "已经夹着尾巴回去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x8,
        (
            "哈哈哈，太好了。\x01",
            "我们真是被\x01",
            "那孩子的笑容拯救了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x0)
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 3)
    Jump("loc_43E7")

    label("loc_4348")

    TurnDirection(0xFE, 0x0, 0)

    #C0255
    ChrTalk(
        0xFE,
        (
            "那些议员经常会来这里\x01",
            "找麻烦，不过……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "我感觉只要有莉夏小姐在，\x01",
            "应该就不用再担心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "呵呵，稍后给她送些小菜过去，\x01",
            "就当作是谢礼吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x0)

    label("loc_43E7")

    Jump("loc_4BF5")

    label("loc_43EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4587")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4522")
    OP_4B(0x11, 0xFF)

    #C0258
    ChrTalk(
        0xFE,
        (
            "暂住许可证……\x01",
            "住户登记……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "不好意思，\x01",
            "我来到克洛斯贝尔\x01",
            "都已经有五年了……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x11,
        (
            "呵，但如果没有登记信息，\x01",
            "那可就很麻烦了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x11,
        (
            "根据自治州的法律，\x01",
            "是会被下达驱除令的……\x01",
            "所以要不要自觉一点，主动离开呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0262
    ChrTalk(
        0xFE,
        (
            "怎、怎么会……\x01",
            "#2S……怎么办啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    SetScenarioFlags(0x0, 3)
    Jump("loc_4582")

    label("loc_4522")

    TurnDirection(0xA, 0x0, 0)

    #C0263
    ChrTalk(
        0xFE,
        "太头疼了……\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "如果不提交申请的话，\x01",
            "我们可能就会成为\x01",
            "非法滞留的黑户了……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x13B, 0x0)

    label("loc_4582")

    Jump("loc_4BF5")

    label("loc_4587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_46CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4617")

    #C0265
    ChrTalk(
        0xA,
        (
            "住在隔壁的那个女孩，\x01",
            "最近好像有点无精打采的。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xA,
        (
            "也许是我多管闲事……\x01",
            "但年轻女孩子一个人生活，\x01",
            "总让人有些在意呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46C8")

    label("loc_4617")


    #C0267
    ChrTalk(
        0xA,
        (
            "搬到隔壁的那个女孩\x01",
            "不管什么时候都很开朗，\x01",
            "是个充满活力的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xA,
        (
            "我平时也总让利玛\x01",
            "以她为榜样呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xA,
        (
            "不过……感觉她最近\x01",
            "好像有点没精神呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xA,
        "是不是在担心什么事呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_46C8")

    Jump("loc_4BF5")

    label("loc_46CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_47F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4772")

    #C0271
    ChrTalk(
        0xA,
        "利玛非常喜欢她爸爸。\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xA,
        (
            "我老公是个临时工，整天都要出去工作，\x01",
            "平时基本都不在家，不过……\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xA,
        (
            "她是什么时候变得\x01",
            "那么喜欢粘着爸爸的呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47EB")

    label("loc_4772")


    #C0274
    ChrTalk(
        0xA,
        "利马也真是的，昨天晚上强撑着不睡……\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xA,
        (
            "今天一定会说很困，\x01",
            "要去睡午觉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xA,
        (
            "在陪她午睡之前要\x01",
            "把衣服洗好啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_47EB")

    Jump("loc_4BF5")

    label("loc_47F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4936")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4882")

    #C0277
    ChrTalk(
        0xA,
        (
            "旧城区的房租都很便宜，\x01",
            "即使是我们也可以生活下去。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xA,
        (
            "如果这里翻建成了\x01",
            "豪华漂亮的公寓……\x01",
            "我们也许就只能搬出去了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4931")

    label("loc_4882")


    #C0279
    ChrTalk(
        0xA,
        "之前有政府职员来找过我们。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xA,
        (
            "好像说是要把旧城区推翻再建，\x01",
            "进行重新开发……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    #C0281
    ChrTalk(
        0xA,
        (
            "旧城区难道\x01",
            "要就此消失吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xA,
        "要是那样的话，我们可就……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4931")

    Jump("loc_4BF5")

    label("loc_4936")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4A0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_49AF")

    #C0283
    ChrTalk(
        0xA,
        (
            "年轻的女孩子\x01",
            "独身一人生活……\x01",
            "真让人担心啊，会不会出什么事呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xA,
        "我们必须要多关心她才行。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A06")

    label("loc_49AF")


    #C0285
    ChrTalk(
        0xA,
        (
            "隔壁搬来了一个\x01",
            "年轻女孩。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xA,
        (
            "而且好像还是独自一人生活……\x01",
            "我真是吃了一惊呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4A06")

    Jump("loc_4BF5")

    label("loc_4A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4ACF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4A5C")
    OP_4B(0xB, 0xFF)

    #C0287
    ChrTalk(
        0xA,
        "好～请稍等一下哦～\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xA,
        "炖菜马上就做好啦～！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_4ACA")

    label("loc_4A5C")


    #C0289
    ChrTalk(
        0xA,
        (
            "能像现在这样，每天吃上热腾腾的饭菜，\x01",
            "全都靠我丈夫每天出去劳动。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xA,
        "必须要好好感谢他呢。\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 3)

    label("loc_4ACA")

    Jump("loc_4BF5")

    label("loc_4ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_4B93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4B13")

    #C0291
    ChrTalk(
        0xA,
        (
            "不过，治安较差确实\x01",
            "是这个地区的缺点呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B8E")

    label("loc_4B13")


    #C0292
    ChrTalk(
        0xA,
        (
            "治安差是这个地区\x01",
            "的一大缺点呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xA,
        (
            "啊，不过，我们并不打算\x01",
            "因此就离开这里哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xA,
        "而且也没有其它地方可以去……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4B8E")

    Jump("loc_4BF5")

    label("loc_4B93")


    #C0295
    ChrTalk(
        0xA,
        (
            "我女儿很有精神，\x01",
            "总是到处跑来跑去的。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xA,
        (
            "呼，我做料理，她也好奇，\x01",
            "隔不了多久就要过来看看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BF5")

    TalkEnd(0xFE)
    Return()

    # Function_12_3C4B end

    def Function_13_4BF9(): pass

    label("Function_13_4BF9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4C6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4C66")
    OP_63(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    #C0297
    ChrTalk(
        0xB,
        "爸爸今天回来得很早！\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xB,
        (
            "哇～一定要让他\x01",
            "陪我玩个够！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C69")

    label("loc_4C66")

    Call(0, 14)

    label("loc_4C69")

    Jump("loc_5606")

    label("loc_4C6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4CEB")

    #C0299
    ChrTalk(
        0xB,
        (
            "听说爸爸今天可能会\x01",
            "提前回来呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    #C0300
    ChrTalk(
        0xB,
        "哇～是真的吗？\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xB,
        "什么时候就能回来了呢～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5606")

    label("loc_4CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4DAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4D40")

    #C0302
    ChrTalk(
        0xB,
        "先要把垃圾都捡起来！\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xB,
        "利玛要把家里打扫得干干净净～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DA9")

    label("loc_4D40")


    #C0304
    ChrTalk(
        0xB,
        (
            "妈妈和我说，只要多帮忙做家务，\x01",
            "爸爸也许就会提早回来了呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xB,
        (
            "……利玛今天一定会\x01",
            "努力帮忙的！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_4DA9")

    Jump("loc_5606")

    label("loc_4DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4E16")

    #C0306
    ChrTalk(
        0xB,
        (
            "莉夏姐姐刚才\x01",
            "出门了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xB,
        (
            "她还是像平时一样，\x01",
            "摸了我的头呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xB,
        "哇～好开心哦～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5606")

    label("loc_4E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4EE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4E58")

    #C0309
    ChrTalk(
        0xB,
        (
            "……爸爸到底要到什么时候\x01",
            "才能回来啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EDC")

    label("loc_4E58")


    #C0310
    ChrTalk(
        0xB,
        (
            "爸爸已经把大楼\x01",
            "盖好啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xB,
        (
            "不过呢，好像还要继续盖\x01",
            "新的大楼呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)

    #C0312
    ChrTalk(
        0xB,
        (
            "……爸爸今天能\x01",
            "早点回来吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_4EDC")

    Jump("loc_5606")

    label("loc_4EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4FA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4F37")

    #C0313
    ChrTalk(
        0xB,
        "爸爸终于要休假了！\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xB,
        (
            "哇～我们可以一起\x01",
            "去参观庆典啦～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FA0")

    label("loc_4F37")


    #C0315
    ChrTalk(
        0xB,
        "对啦，对啦～！\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xB,
        "爸爸这次终于要休假啦！\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    #C0317
    ChrTalk(
        0xB,
        "哇～！　最喜欢爸爸了～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_4FA0")

    Jump("loc_5606")

    label("loc_4FA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5097")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5012")

    #C0318
    ChrTalk(
        0xB,
        (
            "莉夏姐姐真是\x01",
            "非常温柔啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xB,
        (
            "哎～不过她有时会上蹿下跳的，\x01",
            "那应该是她的工作吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5092")

    label("loc_5012")


    #C0320
    ChrTalk(
        0xB,
        (
            "住在隔壁的那个\x01",
            "莉夏姐姐真是个\x01",
            "非常温柔的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xB,
        (
            "而且哦，\x01",
            "上蹿下跳就是\x01",
            "她的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xB,
        (
            "她今天也精神十足地\x01",
            "出门了呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5092")

    Jump("loc_5606")

    label("loc_5097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_50DD")

    #C0323
    ChrTalk(
        0xB,
        "妈妈让我乖乖在家里待着。\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xB,
        "外面发生什么事了吗～\x02",
    )

    CloseMessageWindow()
    Jump("loc_5606")

    label("loc_50DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5165")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_510C")

    #C0325
    ChrTalk(
        0xB,
        "我想去找爸爸啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5160")

    label("loc_510C")


    #C0326
    ChrTalk(
        0xB,
        (
            "爸爸最近的工作\x01",
            "好像很忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xB,
        "每天到很晚都不能回家。\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xB,
        "呜，好寂寞……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5160")

    Jump("loc_5606")

    label("loc_5165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5281")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_51DC")

    #C0329
    ChrTalk(
        0xB,
        (
            "昨天晚上我拼命忍着不睡……\x01",
            "但也没能和他多说几句话……\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xB,
        (
            "呜呜呜呜～……\x01",
            "爸爸，对不起……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_527C")

    label("loc_51DC")


    #C0331
    ChrTalk(
        0xB,
        (
            "呜呜呜呜～……\x01",
            "总是忍不住想睡……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xB,
        (
            "昨天我努力忍着不睡，\x01",
            "一直等到爸爸回家……\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xB,
        (
            "不过，被爸爸抱起来后，\x01",
            "我就这么睡着了～\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xB,
        "都没说上几句话呢……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_527C")

    Jump("loc_5606")

    label("loc_5281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_53B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_52DE")

    #C0335
    ChrTalk(
        0xB,
        (
            "利玛平时很少有机会\x01",
            "能见到爸爸……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xB,
        (
            "爸爸今天会早点\x01",
            "回家吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53AD")

    label("loc_52DE")


    #C0337
    ChrTalk(
        0xB,
        (
            "利玛的爸爸每天\x01",
            "都在辛苦工作～\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xB,
        (
            "他在大楼的施工现场\x01",
            "工作，每天早上\x01",
            "很早就要出门。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xB,
        (
            "然后，每天晚上，要等到利玛\x01",
            "睡着之后，他才会回家～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)

    #C0340
    ChrTalk(
        0xB,
        "利玛平时很少能见到爸爸的面……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_53AD")

    Jump("loc_5606")

    label("loc_53B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5474")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5407")

    #C0341
    ChrTalk(
        0xB,
        "那个大姐姐真是好温柔啊。\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xB,
        "嘿嘿嘿，她还摸了我的头呢～\x02",
    )

    CloseMessageWindow()
    Jump("loc_546F")

    label("loc_5407")


    #C0343
    ChrTalk(
        0xB,
        (
            "哈哈～我昨天遇到了\x01",
            "一位不认识的大姐姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xB,
        (
            "那个大姐姐好像\x01",
            "搬到隔壁住了呢～\x01",
            "她还摸了摸我的头～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_546F")

    Jump("loc_5606")

    label("loc_5474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_551A")

    #C0345
    ChrTalk(
        0xB,
        "唔唔，好香的味道！\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xB,
        (
            "怎么样？味道很香吧？\x01",
            "我的肚子都饿瘪了呢～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    #C0347
    ChrTalk(
        0xB,
        (
            "真想让爸爸也来一起吃呢～\x01",
            "他要是能早点回来就好了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5606")

    label("loc_551A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_555D")

    #C0348
    ChrTalk(
        0xB,
        "啦啦啦，啦～啦¤\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xB,
        (
            "爸爸今天能\x01",
            "早点回来吗～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5606")

    label("loc_555D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_55A3")

    #C0350
    ChrTalk(
        0xB,
        "我正在等爸爸回家呢。\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xB,
        "希望爸爸能早点回来呀～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5606")

    label("loc_55A3")


    #C0352
    ChrTalk(
        0xB,
        (
            "我爸爸在建筑工地\x01",
            "工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xB,
        (
            "爸爸今天要到\x01",
            "几点才能回家呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xB,
        "希望爸爸能早点回来呀～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5606")

    TalkEnd(0xFE)
    Return()

    # Function_13_4BF9 end

    def Function_14_560A(): pass

    label("Function_14_560A")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_63(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    #C0355
    ChrTalk(
        0xB,
        "哇～爸爸，欢迎回家！！\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xC,
        (
            "我回来啦，利玛。\x01",
            "等很久了吗？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 4)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_14_560A end

    def Function_15_567F(): pass

    label("Function_15_567F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_56FA")

    #C0357
    ChrTalk(
        0xC,
        (
            "今天发生了不少事……\x01",
            "所以比预想中提早下班了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xC,
        (
            "多亏如此，才能和家人们\x01",
            "一起享用热乎乎的晚饭啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56FD")

    label("loc_56FA")

    Call(0, 14)

    label("loc_56FD")

    TalkEnd(0xFE)
    Return()

    # Function_15_567F end

    def Function_16_5701(): pass

    label("Function_16_5701")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_575E")
    Call(0, 17)

    #C0359
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "唔唔……嗝。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "王，比起食物，酒更重要。\x01",
            "再给我拿些酒来～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F4E")

    label("loc_575E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_57FF")
    Call(0, 17)

    #C0361
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "疼疼疼……\x01",
            "不小心从床上掉下来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "酒……不对，不然还是先去上个厕所吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "………………………………\x01",
            "……嗯～……嗝～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F4E")

    label("loc_57FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5857")
    Call(0, 17)

    #C0364
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "咕～……嗝～……\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "……真正幸福的地方～……\x01",
            "只有天国啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F4E")

    label("loc_5857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5925")
    Call(0, 17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_58AA")

    #C0366
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "咕啊～……嗝～……\x01",
            "嗯，下次我可不会放过你哦……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5920")

    label("loc_58AA")


    #C0367
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "咕啊～……嗝～……\x01",
            "咕～……嗝～……\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "谁啊，谁偷喝了我的酒……\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "我明明没喝，怎么成了空瓶子啊！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_5920")

    Jump("loc_5F4E")

    label("loc_5925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5994")
    Call(0, 17)

    #C0370
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "咕～……嗝～……\x01",
            "我……哪怕只有看病的钱，\x01",
            "也会拿去买酒喝……\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "我就是这样的人……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F4E")

    label("loc_5994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_59E6")
    Call(0, 17)

    #C0372
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "嗯～……怎么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "为什么外面飘舞着\x01",
            "那么多彩纸屑啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F4E")

    label("loc_59E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5A3C")
    Call(0, 17)

    #C0374
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "咕～……嗝～……\x01",
            "酒、给我酒啊～……\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "咕～……嗝嗝～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F4E")

    label("loc_5A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5A90")
    Call(0, 17)

    #C0376
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "酒～……只有酒……\x01",
            "……才是我的朋友～……\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "啊嚏……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F4E")

    label("loc_5A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5AD3")
    Call(0, 17)

    #C0378
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "呜～想去厕所了。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "厕所……在哪里……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F4E")

    label("loc_5AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5B18")
    Call(0, 17)

    #C0380
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "酒，我要酒～……！\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "咕啊～……嗝～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F4E")

    label("loc_5B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5B97")
    Call(0, 17)

    #C0382
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "丢了饭碗，只能借酒消愁～……\x01",
            "嗝……\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "……喂，这不是空瓶子吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "王，王！\x01",
            "赶快去给我买酒啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F4E")

    label("loc_5B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5BF3")
    Call(0, 17)

    #C0385
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "王……你太吵了……\x01",
            "你就不能安静一点吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "咕～……嗝～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F4E")

    label("loc_5BF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5C53")
    Call(0, 17)

    #C0387
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "咕～……嗝～……\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "王，王在哪里啊！？\x01",
            "……酒……还没买回来吗……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F4E")

    label("loc_5C53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5CAF")
    Call(0, 17)

    #C0389
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "人生不过就是这么回事罢了……！\x01",
            "只有酒……呼啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "呜～呼……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F4E")

    label("loc_5CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5CFB")
    Call(0, 17)

    #C0391
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "呼……\x01",
            "……已经醒了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "酒，给我拿酒来～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F4E")

    label("loc_5CFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5D53")
    Call(0, 17)

    #C0393
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "酒～……只有酒～……\x01",
            "才是我的人生～……\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "咕～……嗝～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F4E")

    label("loc_5D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5DAB")
    Call(0, 17)

    #C0395
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "王，你吵死人了！\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "别出这么大声……！\x01",
            "……咕～……嗝～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F4E")

    label("loc_5DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5E3F")
    Call(0, 17)

    #C0397
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "王，给我酒！\x01",
            "给我拿酒来～……\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "咕～……嗝～……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E3A")

    #C0399
    ChrTalk(
        0x101,
        (
            "#0003F（看起来，这里好像\x01",
            "  不是空房啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E3A")

    Jump("loc_5F4E")

    label("loc_5E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_5EC6")
    Call(0, 17)

    #C0400
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "嗯？　嗯嗯～……\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "咕～……嗝～……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EC1")

    #C0402
    ChrTalk(
        0x101,
        (
            "#0003F（看起来，这里好像\x01",
            "  不是空房啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EC1")

    Jump("loc_5F4E")

    label("loc_5EC6")

    Call(0, 17)

    #C0403
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "咕～……嗝～……\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "酒～酒。\x01",
            "……给我拿酒来～……！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F4E")

    #C0405
    ChrTalk(
        0x101,
        (
            "#0003F（看起来，这里好像\x01",
            "  不是空房啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F4E")

    TalkEnd(0x13)
    Return()

    # Function_16_5701 end

    def Function_17_5F52(): pass

    label("Function_17_5F52")

    SetChrName("")

    #A0406
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门紧紧关闭着，\x01",
            "可以听到从里面传来的声音。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Return()

    # Function_17_5F52 end

    def Function_18_5F8B(): pass

    label("Function_18_5F8B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5FF8")

    #C0407
    ChrTalk(
        0xFE,
        (
            "这所公寓中的家伙们\x01",
            "还真是意外的顽固啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "呵呵，算了……\x01",
            "早晚会把他们全部赶出去的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6095")

    label("loc_5FF8")

    OP_93(0xFE, 0x87, 0x0)
    OP_4B(0x8, 0xFF)

    #C0409
    ChrTalk(
        0xFE,
        (
            "那么，首先还是要确认\x01",
            "一下住户的登记信息啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "呵呵……您应该不会\x01",
            "还没有登记过吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x8,
        (
            "嗯，当然不会……\x01",
            "我已经在这里住了六十年了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 7)

    label("loc_6095")

    TalkEnd(0xFE)
    Return()

    # Function_18_5F8B end

    def Function_19_6099(): pass

    label("Function_19_6099")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6135")

    #C0412
    ChrTalk(
        0xFE,
        (
            "只要再开发计划能落实，\x01",
            "就还会有企业来投标的。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        (
            "呵呵……到时候就又能获得大量资金了。\x01",
            "必须要赶在共和国派的人\x01",
            "之前，抢先一步行动啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61C3")

    label("loc_6135")


    #C0414
    ChrTalk(
        0xFE,
        (
            "旧城区的这些人，\x01",
            "就只能委屈他们牺牲一下了。\x01",
            "想想的话，倒也有点内疚呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xFE,
        (
            "呵呵……\x01",
            "不过，就当作是让他们为\x01",
            "克洛斯贝尔的发展做点贡献吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61C3")

    TalkEnd(0xFE)
    Return()

    # Function_19_6099 end

    def Function_20_61C7(): pass

    label("Function_20_61C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_64DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_6260")

    #C0416
    ChrTalk(
        0x10,
        (
            "#1808F剧团长和伊莉娅小姐，\x01",
            "已经把脚本修正好了吧……\x02\x03",

            "#1802F我差不多也该回去\x01",
            "参加彩排了。\x02\x03",

            "各位，尼克鲁先生就\x01",
            "拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64D8")

    label("loc_6260")


    #C0417
    ChrTalk(
        0x101,
        (
            "#0005F莉夏？\x01",
            "这种时候，你在这里做什么呢？\x02\x03",

            "#0001F马上就到公演的时间了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x10,
        (
            "#1805F啊，那个……\x02\x03",

            "#1800F因为白天公演的时间稍微延迟了一点，\x01",
            "所以我回来取些东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10)

    #C0419
    ChrTalk(
        0x10,
        (
            "#1808F各位，那个…\x01",
            "尼克鲁先生的事情就……\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x101,
        (
            "#0006F嗯，我们也正在着手寻找，\x01",
            "不过……\x02\x03",

            "#0001F目前还没有发现\x01",
            "任何线索呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x104,
        (
            "#0300F哈，不过多少\x01",
            "也开始有点头绪啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x10,
        (
            "#1806F是吗……\x02\x03",

            "#1801F不好意思，那尼克鲁先生\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x102,
        "#0100F嗯，交给我们好了。\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x103,
        (
            "#0204F我们可是及时阻止了\x01",
            "暗杀市长事件的特别任务支援科。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x10A,
        "#0601F（唔……）\x02",
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x10,
        (
            "#1809F呵呵……说得也是呢。\x02\x03",

            "#1804F…………………………（低头行礼）\x01",
            "那就万事拜托了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_64D8")

    Jump("loc_6678")

    label("loc_64DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_65B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_END)), "loc_65A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_65A0")

    #C0427
    ChrTalk(
        0x10,
        (
            "#1809F今天是久违的休假日，\x01",
            "我准备和朋友一起出去玩。\x02\x03",

            "#1804F虽然也邀请了伊莉娅小姐，\x01",
            "不过她多半起不来吧……\x02\x03",

            "#1802F每到休息日，她一般都会\x01",
            "睡到接近太阳下山呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65A3")

    label("loc_65A0")

    Call(0, 21)

    label("loc_65A3")

    Jump("loc_65AB")

    label("loc_65A8")

    Call(0, 22)

    label("loc_65AB")

    Jump("loc_6678")

    label("loc_65B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_END)), "loc_6675")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_666D")

    #C0428
    ChrTalk(
        0x10,
        (
            "#1809F今天是久违的休假日，\x01",
            "我准备和朋友一起出去玩。\x02\x03",

            "#1804F虽然也邀请了伊莉娅小姐，\x01",
            "不过她多半起不来吧……\x02\x03",

            "#1810F每到休息日，她一般都会\x01",
            "睡到接近太阳下山呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB3, 2)
    Jump("loc_6670")

    label("loc_666D")

    Call(0, 21)

    label("loc_6670")

    Jump("loc_6678")

    label("loc_6675")

    Call(0, 22)

    label("loc_6678")

    TalkEnd(0xFE)
    Return()

    # Function_20_61C7 end

    def Function_21_667C(): pass

    label("Function_21_667C")

    TurnDirection(0x10, 0x153, 0)

    #C0429
    ChrTalk(
        0x10,
        (
            "#1808F（是吗……\x01",
            "  这个孩子就是那时候的……）\x02\x03",

            "#1803F（……从外表上来看，只是个\x01",
            "  普通的小孩子，不过……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0430
    ChrTalk(
        0x153,
        (
            "#1110F嗯～？\x01",
            "琪雅的脸上\x01",
            "粘着什么东西吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x101,
        (
            "#0005F莫非……\x01",
            "你见过这孩子吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x10,
        (
            "#1802F没有，只是她太可爱了，\x01",
            "所以不禁看得入神了……\x02\x03",

            "#1809F呵呵，罗伊德警官，真羡慕\x01",
            "你们能和她一起散步呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x153,
        (
            "#1109F嘿嘿嘿～\x01",
            "莉夏也很可爱啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x10,
        (
            "#1810F谢、谢谢。\x01",
            "（这孩子，真是很可爱呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_21_667C end

    def Function_22_6829(): pass

    label("Function_22_6829")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-1640, 1330, 55710, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -1630, 30, 54460, 0)
    SetChrPos(0xEF, -520, 30, 54660, 315)
    SetChrPos(0x153, -2610, 30, 55090, 45)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x10, 0x101, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_691B")

    #C0435
    ChrTalk(
        0x10,
        (
            "#1805F咦，罗伊德警官？\x01",
            "还有艾莉小姐也……\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x102,
        "#0102F呵呵，你好啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_69C8")

    label("loc_691B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_696D")

    #C0437
    ChrTalk(
        0x10,
        (
            "#1805F咦，罗伊德警官？\x01",
            "还有缇欧也……\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x103,
        "#0202F你好。\x02",
    )

    CloseMessageWindow()
    Jump("loc_69C8")

    label("loc_696D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_69C8")

    #C0439
    ChrTalk(
        0x10,
        (
            "#1805F咦，罗伊德警官？\x01",
            "还有兰迪先生也……\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x104,
        "#0309F你好啊，小莉夏！\x02",
    )

    CloseMessageWindow()

    label("loc_69C8")


    #C0441
    ChrTalk(
        0x101,
        (
            "#0002F你好，莉夏。\x02\x03",

            "听说过你住在旧城区，\x01",
            "原来就是这里啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x10,
        (
            "#1809F呵呵，是的。\x02\x03",

            "#1800F因为租金比较便宜，\x01",
            "所以就选了这里。\x02\x03",

            "#1805F不过，那个……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    TurnDirection(0x10, 0x153, 500)
    Sleep(500)

    #C0443
    ChrTalk(
        0x101,
        (
            "#0012F啊，你是想问这个孩子吗，\x01",
            "她是暂时由我们负责看护的──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(892, 0, 100, 0)
    Sleep(1000)
    OP_64(0x153)

    #C0444
    ChrTalk(
        0x153,
        (
            "#1105F哎哎哎～～……\x02\x03",

            "#1109F那个那个，罗伊德！\x01",
            "这个姐姐好丰满啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6B8D")

    #C0445
    ChrTalk(
        0x102,
        "#0105F小、小琪雅……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C00")

    label("loc_6B8D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6BC9")

    #C0446
    ChrTalk(
        0x103,
        (
            "#0206F琪雅……\x01",
            "说得也太直接了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C00")

    label("loc_6BC9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C00")

    #C0447
    ChrTalk(
        0x104,
        (
            "#0305F哦哦……\x01",
            "真不愧是阿琪……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C00")

    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x101, 0x153, 500)
    Sleep(1000)
    OP_64(0x101)

    #C0448
    ChrTalk(
        0x101,
        "#0011F别、别乱说啊，琪雅！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 500)

    #C0449
    ChrTalk(
        0x101,
        (
            "#0006F抱歉啊，莉夏。\x01",
            "她实在是太失礼了……\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x10,
        (
            "#1810F哪、哪里，没关系啦。\x02\x03",

            "#1809F……呵呵，\x01",
            "你是叫琪雅吧。\x02\x03",

            "我是莉夏，\x01",
            "莉夏·毛。\x02\x03",

            "#1802F请多关照哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x153,
        "#1109F嗯！\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0x0, 0x0)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0xB3, 1)
    EventEnd(0x5)
    Return()

    # Function_22_6829 end

    def Function_23_6D03(): pass

    label("Function_23_6D03")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 0xFF)
    OP_68(8420, 4790, 16630, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19850, 0)
    SetChrPos(0x101, 1590, 0, 2420, 0)
    SetChrPos(0x102, 2600, 0, 1420, 45)
    SetChrPos(0x103, 440, 0, 1710, 0)
    SetChrPos(0x104, 1800, 0, 210, 135)
    SetChrPos(0x8, 3900, 2000, 11730, 180)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x4)
    FadeToBright(1000, 0)
    OP_68(2260, 1300, 1970, 4800)
    MoveCamera(45, 30, 0, 4800)
    OP_6E(500, 4800)
    SetCameraDistance(19850, 4800)
    Sleep(4800)
    BeginChrThread(0x101, 3, 0, 24)
    BeginChrThread(0x102, 3, 0, 25)
    BeginChrThread(0x103, 3, 0, 26)
    BeginChrThread(0x104, 3, 0, 27)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E77")

    #C0452
    ChrTalk(
        0x102,
        (
            "#11P#0100F这里就是莲花公馆……\x01",
            "应该没有弄错吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x101,
        (
            "#5P#0000F根据市政厅提供的资料，\x01",
            "空房应该有三处……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F4B")

    label("loc_6E77")


    #C0454
    ChrTalk(
        0x101,
        (
            "#5P#0000F那个，虽然现在还有任务在身……\x01",
            "不过，其它的工作也可以顺便处理一下。\x02\x03",

            "这里好像就是市政厅\x01",
            "委托我们调查的公寓了……\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x102,
        (
            "#11P#0100F旧城区的『莲花公馆』啊……\x02\x03",

            "根据市政厅提供的资料，\x01",
            "空房应该有三处……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F4B")

    ClearChrFlags(0x8, 0x80)
    OP_95(0x8, 3900, 0, 3680, 2000, 0x0)
    OP_93(0x8, 0xE1, 0x1F4)

    #C0456
    ChrTalk(
        0x8,
        "#11P哎呀，你们是政府职员吗？\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x0, 0x3)
    EndChrThread(0x1, 0x3)
    EndChrThread(0x2, 0x3)
    EndChrThread(0x3, 0x3)

    def lambda_6FA2():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6FA2)

    def lambda_6FAF():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_6FAF)

    def lambda_6FBC():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_6FBC)

    def lambda_6FC9():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_6FC9)
    Sleep(300)

    #C0457
    ChrTalk(
        0x101,
        (
            "#6P#0005F啊，不，我们是警察。\x02\x03",

            "#0000F出于预防犯罪的目的，\x01",
            "前来检查一下这里的\x01",
            "三处空房。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x8,
        (
            "#11P哦，空房吗，\x01",
            "但空房应该只有一处才对啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0459
    ChrTalk(
        0x103,
        "#6P#0205F是吗……？\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x8,
        "#5P嗯，应该是，不过……\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x8,
        (
            "#5P政府机关根本就掌握不了\x01",
            "旧城区的人口流动情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x8,
        (
            "#5P正因如此，这里\x01",
            "才会被称为旧城区啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x8,
        (
            "#5P算了，要检查的话，就尽管去吧。\x01",
            "但不要惊动了这里的各位住户啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7190():

        label("loc_7190")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_7190")

    QueueWorkItem2(0x0, 1, lambda_7190)

    def lambda_71A2():

        label("loc_71A2")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_71A2")

    QueueWorkItem2(0x1, 1, lambda_71A2)

    def lambda_71B4():

        label("loc_71B4")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_71B4")

    QueueWorkItem2(0x2, 1, lambda_71B4)

    def lambda_71C6():

        label("loc_71C6")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_71C6")

    QueueWorkItem2(0x3, 1, lambda_71C6)
    OP_95(0x8, 4330, 0, 0, 2000, 0x0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    def lambda_71FC():
        OP_93(0xFE, 0x5A, 0x1E)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_71FC)

    def lambda_7209():
        OP_93(0xFE, 0x5A, 0x1E)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7209)

    def lambda_7216():
        OP_93(0xFE, 0x5A, 0x1E)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_7216)

    def lambda_7223():
        OP_93(0xFE, 0x5A, 0x1E)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_7223)
    OP_95(0x8, 7800, 0, 0, 2000, 0x0)

    def lambda_7244():
        OP_95(0xFE, 7800, 0, -5680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7244)

    #C0464
    ChrTalk(
        0x101,
        (
            "#5P#0000F总之，我们就来\x01",
            "确认一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x104,
        (
            "#11P#0300F是啊，\x01",
            "走吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x0, 1590, 0, 1570, 45)
    SetChrPos(0x1, 1590, 0, 1570, 45)
    SetChrPos(0x2, 1590, 0, 1570, 45)
    SetChrPos(0x3, 1590, 0, 1570, 45)
    EndChrThread(0x8, 0x1)
    SetChrPos(0x8, 4270, 0, -52160, 90)
    OP_29(0x3, 0x1, 0x6)
    SetScenarioFlags(0x1, 2)
    EventEnd(0x5)
    Return()

    # Function_23_6D03 end

    def Function_24_7314(): pass

    label("Function_24_7314")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_733B")
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(10000)
    Jump("Function_24_7314")

    label("loc_733B")

    Return()

    # Function_24_7314 end

    def Function_25_733C(): pass

    label("Function_25_733C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7377")
    Sleep(1200)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1600)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1100)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1200)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(10000)
    Jump("Function_25_733C")

    label("loc_7377")

    Return()

    # Function_25_733C end

    def Function_26_7378(): pass

    label("Function_26_7378")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_73A9")
    Sleep(1300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(10000)
    Jump("Function_26_7378")

    label("loc_73A9")

    Return()

    # Function_26_7378 end

    def Function_27_73AA(): pass

    label("Function_27_73AA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_73DB")
    Sleep(1000)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1100)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(10000)
    Jump("Function_27_73AA")

    label("loc_73DB")

    Return()

    # Function_27_73AA end

    def Function_28_73DC(): pass

    label("Function_28_73DC")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-200, 4800, 21200, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, -1000, 3500, 19700, 0)
    SetChrPos(0x102, 370, 3500, 19700, 0)
    SetChrPos(0x103, 370, 3500, 18420, 0)
    SetChrPos(0x104, -1000, 3500, 18420, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_95(0x101, -460, 3500, 20950, 1000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0466
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

    #C0467
    ChrTalk(
        0x101,
        (
            "#0001F不好意思！\x01",
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

    #C0468
    ChrTalk(
        0x103,
        "#0200F感觉好像没有人在呢。\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x101,
        "#0003F嗯，而且……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0470
    ChrTalk(
        0x101,
        (
            "#0001F门把手上堆积了\x01",
            "很多灰尘。\x02\x03",

            "看起来，这里已经\x01",
            "空了有一段时间了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x104,
        (
            "#0300F原来如此，\x01",
            "应该就是这样了。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x103,
        (
            "#0200F其它房间\x01",
            "好像都有住户……\x01",
            "看来空房只有一处啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x102,
        (
            "#0103F莲花公馆的……\x01",
            "嗯，是２０３号室吧。\x01",
            "（认真记录……）\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x3, 0x1, 0x7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76EE")

    #C0474
    ChrTalk(
        0x101,
        (
            "#0003F好，这样一来，三处空房\x01",
            "应该就全部确认完毕了……\x02\x03",

            "#0000F我们赶快回市政厅\x01",
            "的接待处报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x3, 0x1, 0x1E)
    Jump("loc_771F")

    label("loc_76EE")


    #C0475
    ChrTalk(
        0x101,
        (
            "#0000F好，那我们就赶快\x01",
            "去检查其它的空房吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_771F")

    Sleep(200)
    SetChrPos(0x0, -250, 3500, 20480, 180)
    SetChrPos(0x1, -250, 3500, 20480, 180)
    SetChrPos(0x2, -250, 3500, 20480, 180)
    SetChrPos(0x3, -250, 3500, 20480, 180)
    SetScenarioFlags(0x1, 3)
    EventEnd(0x5)
    Return()

    # Function_28_73DC end

    def Function_29_776C(): pass

    label("Function_29_776C")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7795")
    Call(0, 28)
    Jump("loc_77FC")

    label("loc_7795")

    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0476
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_77FC")

    #C0477
    ChrTalk(
        0x101,
        (
            "#0001F门把手上积满了灰尘……\x01",
            "看起来，好像很久没人打扫了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77FC")

    TalkEnd(0xFF)
    Return()

    # Function_29_776C end

    SaveToFile()

Try(main)
