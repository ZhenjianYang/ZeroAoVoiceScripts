from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c041c.bin",                # FileName
        "c041c",                    # MapName
        "c041c",                    # Location
        0x0023,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 35, 0, 1, 0, 2],
    )

    BuildStringList((
        "c041c",                  # 0
        "伊莉娅",                 # 1
        "莉夏",                   # 2
        "巴尔萨摩经理",           # 3
        "接待员罗兰多",           # 4
        "尤金",                   # 5
        "缇奥多尔",               # 6
        "普莉埃",                 # 7
        "瑟蕾奴",                 # 8
        "卡雷利亚",               # 9
        "亚邦剧团长",             # 10
        "客人",                   # 11
        "客人",                   # 12
        "客人",                   # 13
        "客人",                   # 14
        "客人",                   # 15
    ))

    AddCharChip((
        "chr/ch05100.itc",                   # 00
        "chr/ch05200.itc",                   # 01
        "chr/ch21900.itc",                   # 02
        "chr/ch25800.itc",                   # 03
        "chr/ch25900.itc",                   # 04
        "chr/ch28700.itc",                   # 05
        "chr/ch28800.itc",                   # 06
        "chr/ch36900.itc",                   # 07
        "chr/ch37000.itc",                   # 08
        "chr/ch27500.itc",                   # 09
    ))

    DeclNpc(-91550,  0,       1679,    180,  405,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-90209,  0,       1070,    225,  389,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-2250,   2500,    15000,   180,  261,  0x0, 0,   3,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(6969,    0,       3480,    270,  261,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-91199,  0,       -870,    0,    405,  0x0, 0,   5,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-121580, 0,       1669,    0,    389,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-121709, 0,       3109,    180,  389,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-91300,  0,       4960,    90,   389,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-121709, 0,       3109,    90,   277,  0x0, 0,   2,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-3240,   0,       4179,    180,  389,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 25,  9.0,                   14.0,                  2.5,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -4.5,                  -2.799999713897705,    -0.4999999701976776,   1.0])

    DeclActor(6500,    0,       3480,    1200,    6970,    1500,    3480,    0x007E, 0,  4,  0x0000)

    ScpFunction((
        "Function_0_34C",          # 00, 0
        "Function_1_404",          # 01, 1
        "Function_2_4EE",          # 02, 2
        "Function_3_511",          # 03, 3
        "Function_4_8AA",          # 04, 4
        "Function_5_8AE",          # 05, 5
        "Function_6_B05",          # 06, 6
        "Function_7_B99",          # 07, 7
        "Function_8_E83",          # 08, 8
        "Function_9_108B",         # 09, 9
        "Function_10_119D",        # 0A, 10
        "Function_11_12B6",        # 0B, 11
        "Function_12_134C",        # 0C, 12
        "Function_13_13F2",        # 0D, 13
        "Function_14_150C",        # 0E, 14
        "Function_15_1716",        # 0F, 15
        "Function_16_1928",        # 10, 16
        "Function_17_1B3B",        # 11, 17
        "Function_18_1CEA",        # 12, 18
        "Function_19_1F25",        # 13, 19
        "Function_20_20D6",        # 14, 20
        "Function_21_2BA0",        # 15, 21
        "Function_22_2BE6",        # 16, 22
        "Function_23_2C2C",        # 17, 23
        "Function_24_2C58",        # 18, 24
        "Function_25_2CC2",        # 19, 25
    ))


    def Function_0_34C(): pass

    label("Function_0_34C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_38C"),
        (1, "loc_398"),
        (2, "loc_3A4"),
        (3, "loc_3B0"),
        (4, "loc_3BC"),
        (5, "loc_3C8"),
        (6, "loc_3D4"),
        (SWITCH_DEFAULT, "loc_3E0"),
    )


    label("loc_38C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_398")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_403")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_403")

    Return()

    # Function_0_34C end

    def Function_1_404(): pass

    label("Function_1_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41A")
    SetMapFlags(0x10000000)
    Event(0, 20)

    label("loc_41A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_430")
    Event(0, 19)
    Jump("loc_4A7")

    label("loc_430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_43E")
    Jump("loc_4A7")

    label("loc_43E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_454")
    Event(0, 18)
    Jump("loc_4A7")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46A")
    Event(0, 17)
    Jump("loc_4A7")

    label("loc_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_49A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_495")
    SetChrPos(0xA, -3460, 0, 2440, 0)
    ClearChrFlags(0x11, 0x80)

    label("loc_495")

    Jump("loc_4A7")

    label("loc_49A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A7")
    Event(0, 16)

    label("loc_4A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_4ED")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x10, -90300, 0, 4960, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 4)), scpexpr(EXPR_END)), "loc_4ED")
    SetChrFlags(0x9, 0x10)

    label("loc_4ED")

    Return()

    # Function_1_404 end

    def Function_2_4EE(): pass

    label("Function_2_4EE")

    OP_1B(0x3, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_510")
    ModifyEventFlags(1, 0, 0x80)
    OP_1B(0x3, 0x0, 0x18)

    label("loc_510")

    Return()

    # Function_2_4EE end

    def Function_3_511(): pass

    label("Function_3_511")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_615")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_577")

    #C0001
    ChrTalk(
        0xA,
        (
            "看起来，似乎\x01",
            "不在剧场内……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xA,
        (
            "如果发现他的话，\x01",
            "我会立即联络警察的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_610")

    label("loc_577")


    #C0003
    ChrTalk(
        0xA,
        (
            "罗伊德警官，事情我听说了。\x01",
            "你们好像在寻找一个小男孩吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xA,
        (
            "看起来，似乎\x01",
            "不在剧场内……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xA,
        (
            "不过请放心。\x01",
            "如果发现他的话，\x01",
            "我会立即联络警察的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_610")

    Jump("loc_8A6")

    label("loc_615")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F7")

    #C0006
    ChrTalk(
        0xFE,
        (
            "原以为是跟踪狂的犯人，\x01",
            "竟然是个年轻的少女吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "总之，现在正依照伊莉娅小姐的要求\x01",
            "办理接收手续。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "这没什么，只要伊莉娅小姐开口，\x01",
            "入团也不是什么问题吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "那位莉夏小姐\x01",
            "也是这样的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_79B")

    label("loc_6F7")


    #C0010
    ChrTalk(
        0xFE,
        (
            "莉夏小姐原本\x01",
            "也是被伊莉娅小姐硬拉进来的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "剧团长一开始\x01",
            "也不太同意，\x01",
            "不过她确实拥有出色的才能。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐的眼光是不会出错的。\x01",
            "我当然是热烈欢迎了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79B")

    Jump("loc_8A6")

    label("loc_7A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_841")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_821")

    #C0013
    ChrTalk(
        0xFE,
        "事情我听说了……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "没错，这次有跟踪狂\x01",
            "盯上了伊莉娅小姐……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "呼，还请各位\x01",
            "多多帮忙啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_83C")

    label("loc_821")


    #C0016
    ChrTalk(
        0xFE,
        (
            "还请各位\x01",
            "多多帮忙啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83C")

    Jump("loc_8A6")

    label("loc_841")


    #C0017
    ChrTalk(
        0xA,
        (
            "呀……是各位啊，\x01",
            "欢迎光临。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xA,
        (
            "找伊莉娅小姐有事吗？\x01",
            "她和剧团长，还有莉夏小姐\x01",
            "都在舞台那边呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A6")

    TalkEnd(0xFE)
    Return()

    # Function_3_511 end

    def Function_4_8AA(): pass

    label("Function_4_8AA")

    Call(0, 5)
    Return()

    # Function_4_8AA end

    def Function_5_8AE(): pass

    label("Function_5_8AE")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_996")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_91E")

    #C0019
    ChrTalk(
        0xB,
        (
            "各位在找的小男孩\x01",
            "似乎不在剧场内。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xB,
        (
            "等晚上的公演开始之后，\x01",
            "我也多留意一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_991")

    label("loc_91E")


    #C0021
    ChrTalk(
        0xB,
        (
            "经过接待处的客人，\x01",
            "我基本都会看到……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xB,
        (
            "不过，好像所有的孩子\x01",
            "都有监护人同行。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xB,
        "帮不上忙，实在抱歉。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_991")

    Jump("loc_B01")

    label("loc_996")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A17")

    #C0024
    ChrTalk(
        0xB,
        (
            "哦，我不是\x01",
            "太清楚……\x01",
            "是有新团员要加入了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xB,
        (
            "伊莉娅小姐看中的人，\x01",
            "一定是相当厉害的天才吧。\x01",
            "真期待呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B01")

    label("loc_A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A8D")

    #C0026
    ChrTalk(
        0xB,
        (
            "如此说来，昨晚的公演结束后，\x01",
            "伊莉娅小姐和莉夏小姐还有剧团长\x01",
            "长谈了很久……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xB,
        "不知道在说什么呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B01")

    label("loc_A8D")


    #C0028
    ChrTalk(
        0xB,
        (
            "本日是彩虹剧团的\x01",
            "休演日。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xB,
        (
            "不过……\x01",
            "伊莉娅小姐和莉夏小姐\x01",
            "都来剧团了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xB,
        "她们两人都很热衷于排练呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_B01")

    TalkEnd(0xB)
    Return()

    # Function_5_8AE end

    def Function_6_B05(): pass

    label("Function_6_B05")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_B92")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0031
    ChrTalk(
        0x8,
        (
            "#1700F莉夏似乎也已经习惯了\x01",
            "公演的节奏呢。\x02\x03",

            "#1709F嗯嗯，感觉不错。\x01",
            "今天剩下的部分也要加油哦～！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Jump("loc_B95")

    label("loc_B92")

    Call(0, 7)

    label("loc_B95")

    TalkEnd(0xFE)
    Return()

    # Function_6_B05 end

    def Function_7_B99(): pass

    label("Function_7_B99")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0032
    ChrTalk(
        0xC,
        (
            "哈哈，真没想到\x01",
            "莉夏能做得这么好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#1709F是啊，今天的表演\x01",
            "是至今以来最好的一次。\x02\x03",

            "#1702F呵呵，虽说也是因为\x01",
            "全体成员的演技都日渐纯熟……\x02\x03",

            "不过，莉夏好像也渐渐掌握了\x01",
            "公演的节奏吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x9,
        (
            "#1809F啊哈哈……一天演出两场，\x01",
            "比预想中还要辛苦……\x02\x03",

            "#1802F不过，刚才的演出，\x01",
            "感觉十分畅快呢。\x01",
            "从中途开始，身体就变得好轻盈……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "#1709F对对，就是这样。\x01",
            "要好好珍惜这种感觉哦！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_E73")

    #C0036
    ChrTalk(
        0x160,
        (
            "#3305F（这就是伊莉娅·普拉提耶……？\x01",
            "  嗯～感觉好像很普通啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x101,
        (
            "#0012F（感觉普通吗……）\x02\x03",

            "#0000F（伊莉娅小姐可是『天才』哦。\x01",
            "  只不过，好像仅限于舞台之上呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x160,
        (
            "#3304F（嘻嘻……原来如此。\x01",
            "  那可真是有趣的『天才』啊。）\x02\x03",

            "#3302F（那位看起来像东方人的姐姐\x01",
            "  似乎也有点意思……）\x02\x03",

            "（玲要不要也来看一次\x01",
            "  彩虹剧团的演出呢。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E73")

    SetScenarioFlags(0x0, 2)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_7_B99 end

    def Function_8_E83(): pass

    label("Function_8_E83")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 4)), scpexpr(EXPR_END)), "loc_F3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F36")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0039
    ChrTalk(
        0x9,
        (
            "#1810F纪念庆典到明天就是最终日了吧。\x02\x03",

            "#1804F……好吧。\x01",
            "要调整好状态，努力表演才行……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#0001F（到底是有些累了吧……？）\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Jump("loc_F39")

    label("loc_F36")

    Call(0, 7)

    label("loc_F39")

    Jump("loc_1087")

    label("loc_F3E")


    #C0041
    ChrTalk(
        0x9,
        (
            "#1805F啊，罗伊德警官。\x02\x03",

            "那个小男孩\x01",
            "还没有找到吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_END)), "loc_FE1")

    #C0042
    ChrTalk(
        0x101,
        (
            "#0006F嗯，现在还没……\x02\x03",

            "#0000F不过已经有了目击情报，\x01",
            "我想很快就能找到的。\x01",
            "请不用太担心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102C")

    label("loc_FE1")


    #C0043
    ChrTalk(
        0x101,
        (
            "#0006F嗯，现在还没……\x02\x03",

            "#0000F不过，搜寻才刚刚开始呢，\x01",
            "不用太担心啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_102C")


    #C0044
    ChrTalk(
        0x9,
        (
            "#1806F……好的。\x02\x03",

            "#1810F不好意思，\x01",
            "要是我没有演出的话，\x01",
            "就可以帮忙了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x0)
    SetChrFlags(0x9, 0x10)
    SetScenarioFlags(0xB2, 4)

    label("loc_1087")

    TalkEnd(0xFE)
    Return()

    # Function_8_E83 end

    def Function_9_108B(): pass

    label("Function_9_108B")

    TalkBegin(0xFE)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_10E0")

    #C0045
    ChrTalk(
        0xC,
        (
            "共和国的苦茶\x01",
            "还挺不错的呢，\x01",
            "对缓解疲劳相当有效哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_118D")

    label("loc_10E0")


    #C0046
    ChrTalk(
        0xC,
        "（啜饮～）……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xC,
        (
            "哦，是真的，\x01",
            "感觉真的能缓解疲劳呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xC,
        (
            "不愧是东方出身的人，\x01",
            "莉夏还有这种好东西啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "#1704F嗯嗯，这个不错呢。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        "#1809F啊哈哈，多谢夸奖。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_118D")

    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_9_108B end

    def Function_10_119D(): pass

    label("Function_10_119D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 6)), scpexpr(EXPR_END)), "loc_11F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_11EC")

    #C0051
    ChrTalk(
        0xD,
        (
            "………………………………\x01",
            "剧团是按资历排位的嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11EF")

    label("loc_11EC")

    Call(0, 12)

    label("loc_11EF")

    Jump("loc_12B2")

    label("loc_11F4")


    #C0052
    ChrTalk(
        0xD,
        "……你好像在找小孩子吧。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xD,
        "要我帮忙找找吗？\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#0001F啊，不用……\x01",
            "不好意思，您的好意心领了。\x02\x03",

            "因为这很花时间的，还是不麻烦您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xD,
        "……是吗。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xD,
        "希望你能早点找到那孩子啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB2, 6)

    label("loc_12B2")

    TalkEnd(0xFE)
    Return()

    # Function_10_119D end

    def Function_11_12B6(): pass

    label("Function_11_12B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 7)), scpexpr(EXPR_END)), "loc_12FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_12F7")

    #C0057
    ChrTalk(
        0xE,
        (
            "（大口咬）……\x01",
            "甜品就是正义呢～⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12FA")

    label("loc_12F7")

    Call(0, 12)

    label("loc_12FA")

    Jump("loc_1348")

    label("loc_12FF")


    #C0058
    ChrTalk(
        0xE,
        (
            "哎呀，你在找伊莉娅\x01",
            "说的那个小男孩？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xE,
        (
            "没见过呢，\x01",
            "不好意思哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB2, 7)

    label("loc_1348")

    TalkEnd(0xFE)
    Return()

    # Function_11_12B6 end

    def Function_12_134C(): pass

    label("Function_12_134C")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    TurnDirection(0xD, 0xE, 0)
    TurnDirection(0xE, 0xD, 0)

    #C0060
    ChrTalk(
        0xD,
        (
            "普莉埃小姐，要吃点心的话，\x01",
            "还是先换了衣服再吃比较好吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xE,
        (
            "……缇奥多尔，\x01",
            "居然来管我，你好像有点嚣张吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xD,
        "……对不起。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_12_134C end

    def Function_13_13F2(): pass

    label("Function_13_13F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1450")

    #C0063
    ChrTalk(
        0xF,
        (
            "竟然会被伊莉娅小姐表扬……\x01",
            "好、好开心哦……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xF,
        "…………………………⊥\x02",
    )

    CloseMessageWindow()
    Jump("loc_1508")

    label("loc_1450")


    #C0065
    ChrTalk(
        0xF,
        "……那个，你可以听我说吗？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xF,
        (
            "其实，我今天的演技\x01",
            "被伊莉娅小姐表扬了！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xF)

    #C0067
    ChrTalk(
        0xF,
        (
            "伊、伊莉娅大人……\x01",
            "咳咳，入团以来，还是第一次\x01",
            "受到伊莉娅小姐的表扬呢……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_1508")

    TalkEnd(0xFE)
    Return()

    # Function_13_13F2 end

    def Function_14_150C(): pass

    label("Function_14_150C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_167B")
    OP_4B(0x10, 0xFF)
    OP_4B(0xF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1571")

    #C0068
    ChrTalk(
        0x10,
        (
            "总而言之，夜场时\x01",
            "请穿这套吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x10,
        "我会把平时的服装缝补好的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_166E")

    label("loc_1571")


    #C0070
    ChrTalk(
        0x10,
        (
            "（唰唰唰）……\x01",
            "嗯嗯，感觉好多了呢。\x01",
            "长度不会不方便吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xF,
        "嗯，没问题。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xF,
        (
            "而且这本来\x01",
            "就是松垮垮的衣服嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0073
    ChrTalk(
        0x10,
        (
            "是、是啊，\x01",
            "的确做得比较宽大呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xF,
        (
            "我、我觉得这种松松垮垮的\x01",
            "服装感觉最棒了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_166E")

    OP_4C(0x10, 0xFF)
    OP_4C(0xF, 0xFF)
    Jump("loc_1712")

    label("loc_167B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_16BD")

    #C0075
    ChrTalk(
        0x10,
        (
            "必须要趁着休演日\x01",
            "赶紧打扫干净才行。\x01",
            "真是的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1712")

    label("loc_16BD")


    #C0076
    ChrTalk(
        0x10,
        (
            "哎呀，普莉埃小姐可真是的，\x01",
            "又把点心藏在这种地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x10,
        "没收了，没收！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x0, 6)

    label("loc_1712")

    TalkEnd(0xFE)
    Return()

    # Function_14_150C end

    def Function_15_1716(): pass

    label("Function_15_1716")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1924")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1866")

    #C0078
    ChrTalk(
        0xFE,
        (
            "事情我听说了。\x01",
            "你们似乎顺利解决了呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        "#0000F嗯，算是吧……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x103,
        (
            "#0200F虽然事态的发展\x01",
            "有点出乎意料。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "哈哈，说得是啊。\x01",
            "伊莉娅总是强人所难……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "对了，拉莉夏\x01",
            "加入剧团的时候也是……\x01",
            "（絮絮叨叨）……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#0305F哎呀，已经进入\x01",
            "回忆模式了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x102,
        (
            "#0100F伊莉娅小姐似乎总是让\x01",
            "剧团长很头疼呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 2)
    Jump("loc_1924")

    label("loc_1866")


    #C0085
    ChrTalk(
        0xFE,
        (
            "总、总而言之，谢谢你们了。\x01",
            "这样就能放心地\x01",
            "举行公演了。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "必须要向你们道谢才是……\x01",
            "稍后再送你们一张票如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        (
            "#0309F那可太令人高兴了。\x01",
            "我就感恩戴德地收下了！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#0000F哈哈哈……\x02",
    )

    CloseMessageWindow()

    label("loc_1924")

    TalkEnd(0xFE)
    Return()

    # Function_15_1716 end

    def Function_16_1928(): pass

    label("Function_16_1928")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xA, 0x80)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_68(0, 1450, -4360, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 500, 0, -3230, 0)
    SetChrPos(0x102, -500, 0, -3430, 0)
    SetChrPos(0x103, 500, 0, -4730, 0)
    SetChrPos(0x104, -500, 0, -4930, 0)
    SetChrPos(0xA, 0, 0, -1760, 180)
    FadeToBright(500, 0)
    OP_0D()

    #C0089
    ChrTalk(
        0xA,
        (
            "哎呀，各位，\x01",
            "欢迎光临。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xA,
        (
            "……你们解决了预演时的事件，\x01",
            "真是感激不尽。\x01",
            "请容许我再次道谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#0012F哈哈，那件事就不用客气了。\x02\x03",

            "#0000F话说回来，舞台那边\x01",
            "好像正在公演啊。\x01",
            "连日来大获好评，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xA,
        "是啊，这都多亏了各位。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "对了……明天是\x01",
            "休演日。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xA,
        (
            "各位方便的话，\x01",
            "请再来玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x102,
        (
            "#0100F谢谢，那我们就下次\x01",
            "再来打扰了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0xB8, 7)
    SetScenarioFlags(0x5C, 2)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_1928 end

    def Function_17_1B3B(): pass

    label("Function_17_1B3B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xA, 0x80)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_68(0, 1450, -4360, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 500, 0, -3230, 0)
    SetChrPos(0x102, -500, 0, -3430, 0)
    SetChrPos(0x103, 500, 0, -4730, 0)
    SetChrPos(0x104, -500, 0, -4930, 0)
    SetChrPos(0xA, 0, 0, -1760, 180)
    FadeToBright(500, 0)
    OP_0D()

    #C0096
    ChrTalk(
        0xA,
        (
            "这不是支援科的各位吗，\x01",
            "欢迎光临。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xA,
        (
            "不过，实在抱歉。\x01",
            "伊莉娅小姐和莉夏小姐现在正在……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#0000F不好意思，\x01",
            "大家正在进行准备吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#0300F嗯，我们也没什么事，\x01",
            "下次有机会再来拜访吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        "#0100F嗯，是呀。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x103,
        "#0200F打扰你们了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0xB9, 0)
    SetScenarioFlags(0x5C, 2)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_1B3B end

    def Function_18_1CEA(): pass

    label("Function_18_1CEA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    LoadChrToIndex("chr/ch21800.itc", 0x1E)
    LoadChrToIndex("chr/ch21900.itc", 0x1F)
    LoadChrToIndex("chr/ch20800.itc", 0x20)
    LoadChrToIndex("chr/ch21200.itc", 0x21)
    LoadChrToIndex("chr/ch21300.itc", 0x22)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrChipByIndex(0x14, 0x20)
    SetChrChipByIndex(0x15, 0x21)
    SetChrChipByIndex(0x16, 0x22)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrPos(0x12, 3540, 0, -2890, 315)
    SetChrPos(0x13, 2540, 0, -1890, 135)
    SetChrPos(0x14, 5100, 0, 3030, 89)
    SetChrPos(0x15, -1210, 0, -1120, 225)
    SetChrPos(0x16, -2410, 0, -2320, 45)
    OP_68(0, 1450, -4360, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 500, 0, -3230, 0)
    SetChrPos(0x102, -500, 0, -3430, 0)
    SetChrPos(0x103, 500, 0, -4730, 0)
    SetChrPos(0x104, -500, 0, -4930, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0102
    ChrTalk(
        0x101,
        (
            "#0005F咦，好热闹啊。\x01",
            "公演应该在\x01",
            "游行之前就结束了……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x102,
        (
            "#0100F公演的余热还没有散去，\x01",
            "似乎还有很多人留下来呢。\x02\x03",

            "恐怕还要\x01",
            "再拥挤一阵子吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x103,
        (
            "#0200F还是不要去打扰\x01",
            "他们为好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x104,
        "#0300F哎呀呀，就这么办吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0xB9, 1)
    SetScenarioFlags(0x5C, 2)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_1CEA end

    def Function_19_1F25(): pass

    label("Function_19_1F25")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xA, 0x80)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_68(0, 1450, -4360, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 500, 0, -3230, 0)
    SetChrPos(0x102, -500, 0, -3430, 0)
    SetChrPos(0x103, 500, 0, -4730, 0)
    SetChrPos(0x104, -500, 0, -4930, 0)
    SetChrPos(0xA, 0, 0, -1760, 180)
    FadeToBright(500, 0)
    OP_0D()

    #C0106
    ChrTalk(
        0xA,
        (
            "这不是支援科的各位吗，\x01",
            "欢迎光临。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "不过，实在抱歉。\x01",
            "伊莉娅小姐和莉夏小姐现在正在……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#0000F不好意思，\x01",
            "大家正在进行准备吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x104,
        (
            "#0300F算了，我们也没什么事，\x01",
            "下次有机会再来拜访吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x102,
        "#0100F嗯，是呀。\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x103,
        "#0200F打扰你们了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0xB9, 2)
    SetScenarioFlags(0x5C, 2)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_1F25 end

    def Function_20_20D6(): pass

    label("Function_20_20D6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1100, -2000, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 0, 0, -7000, 0)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, -5100, 0, 3000, 135)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x9, -6000, 0, 2400, 135)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10000000)
    MoveCamera(45, 21, 0, 3000)
    SetCameraDistance(19000, 3000)

    def lambda_219D():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_219D)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(750)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(500)
    OP_6F(0x50)

    #C0112
    ChrTalk(
        0x101,
        (
            "#0005F咦？没有客人呢……\x02\x03",

            "#0000F对了，下午的演出\x01",
            "已经结束了呢……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)

    #N0113
    NpcTalk(
        0x9,
        "少女的声音",
        "#2P……罗伊德警官？\x02",
    )

    CloseMessageWindow()

    #N0114
    NpcTalk(
        0x8,
        "女性的声音",
        "#2P哎呀，怎么了吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-860, 1100, -1110, 2500)
    MoveCamera(10, 21, 0, 2500)
    SetCameraDistance(18000, 2500)

    def lambda_22BD():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22BD)

    def lambda_22CA():
        OP_96(0xFE, 0xFFFFFBB4, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_22CA)
    Sleep(100)

    def lambda_22E7():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_22E7)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23A1")

    #C0115
    ChrTalk(
        0x101,
        "#12P#0005F伊莉娅小姐、莉夏。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x8,
        (
            "#5P#1702F怎么怎么？\x01",
            "是来找我们的吗？\x02\x03",

            "#1709F离晚上的演出还有点时间，\x01",
            "要不要一起去喝个茶？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2649")

    label("loc_23A1")


    #C0117
    ChrTalk(
        0x101,
        (
            "#12P#0005F伊莉娅小姐、莉夏。\x02\x03",

            "#0002F好久不见了。\x01",
            "新剧目似乎大受好评呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x8,
        (
            "#5P#1702F呵呵，\x01",
            "那是当然了。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "#1809F#5P罗伊德警官第一天\x01",
            "也来看了吧。\x02\x03",

            "#1802F呵呵，多谢捧场了。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        (
            "#12P#0012F哪里……\x01",
            "我只是塞茜尔姐姐的跟班而已啦。\x02\x03",

            "#0002F不过，演出真是棒极了！\x02\x03",

            "#0009F伊莉娅小姐自不必说，\x01",
            "莉夏也开始让我崇拜了呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        "#1810F#5P哪、哪里……真不好意思。\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "#1705F#5P哎呀呀，真亲昵呢。\x02\x03",

            "#1709F要不要把警察弟弟搭讪的事\x01",
            "向塞茜尔打个小报告呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0123
    ChrTalk(
        0x101,
        (
            "#12P#0011F什么……\x01",
            "这才不是搭讪啦！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    #C0124
    ChrTalk(
        0x9,
        "#1801F#6P讨、讨厌啦，伊莉娅小姐真是的。\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        (
            "#5P#1702F好吧，这个暂且不提……\x01",
            "怎么，是来找我们的吗？\x02\x03",

            "离晚上的演出还有点时间，\x01",
            "要不要一起去喝个茶？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2641():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2641)

    label("loc_2649")


    #C0126
    ChrTalk(
        0x101,
        (
            "#12P#0008F啊，不了……\x01",
            "只是在工作中顺路过来的。\x02\x03",

            "#0001F其实……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0127
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "向伊莉娅等人说明了\x01",
            "正在寻找走失小男孩的事由。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    #C0128
    ChrTalk(
        0x9,
        "#1801F#5P这可……真令人担心啊。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        (
            "#5P#1706F嗯～这里的确是\x01",
            "小孩子也可以享受乐趣的地方……\x02\x03",

            "说不定，他有可能会在\x01",
            "公演时混进来呢。\x02\x03",

            "#1702F──好，稍微等一下哦。\x02\x03",

            "我去问问正在休息的成员，\x01",
            "确认一下他有没有进来过。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 21)
    Sleep(100)

    def lambda_27C3():

        label("loc_27C3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_27C3")

    QueueWorkItem2(0x9, 2, lambda_27C3)
    Sleep(500)

    #C0130
    ChrTalk(
        0x101,
        (
            "#12P#0005F啊……\x02\x03",

            "#0006F嗯～其实没打算\x01",
            "这么麻烦你们的……\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x9, 0x2)
    TurnDirection(0x9, 0x101, 500)

    #C0131
    ChrTalk(
        0x9,
        (
            "#1804F#5P呵呵，伊莉娅小姐就是\x01",
            "这种想到之后就立刻行动的类型嘛。\x02\x03",

            "#1802F我也去找一圈，\x01",
            "罗伊德警官，请在这里稍等片刻。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 3)
    BeginChrThread(0x9, 3, 0, 22)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    EndChrThread(0x9, 0x1)
    EndChrThread(0x9, 0x2)
    EndChrThread(0x9, 0x3)
    SetChrPos(0x8, -1100, 0, 600, 135)
    SetChrPos(0x9, -2000, 0, 0, 135)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrSubChip(0x9, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0132
    ChrTalk(
        0x8,
        (
            "#5P#1706F嗯～总之，\x01",
            "他好像不在剧场里呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        (
            "#1806F#5P实在抱歉……\x01",
            "帮不上什么忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        (
            "#12P#0002F不，哪里的话……\x01",
            "是我给你们添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        "#5P#1702F呵呵，这点小事没关系啦。\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "#1800F#5P已经把小男孩的事情\x01",
            "告诉剧团长和经理了。\x02\x03",

            "如果找到他的话，\x01",
            "只要联络警察局就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#12P#0004F嗯，那样最好不过。\x02\x03",

            "#0002F──非常感谢，\x01",
            "晚上的公演也请加油。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        "#5P#1709F警察弟弟你也是哦～¤\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x9,
        (
            "#1802F#5P罗伊德警官，\x01",
            "请下次再来哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    def lambda_2AC0():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AC0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B6B")
    StopBGM(0x7D0)
    WaitBGM()

    #A0140
    AnonymousTalk(
        0x101,
        (
            "#0003F（好，在欢乐街的探听\x01",
            "  应该足够了吧。）\x02\x03",

            "#0001F（接下来是后巷……\x01",
            "  用同样的方法，继续探听情报吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2B6B")

    SetScenarioFlags(0xA1, 7)
    OP_29(0x46, 0x1, 0x1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B94")
    OP_29(0x46, 0x1, 0x2)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 3)

    label("loc_2B94")

    EventEnd(0x5)
    NewScene("c040C", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_20_20D6 end

    def Function_21_2BA0(): pass

    label("Function_21_2BA0")

    OP_92(0xFE, 0xFFFFE69C, 0xBB8, 0x1F4)

    def lambda_2BB2():
        OP_95(0xFE, -5500, 0, 5000, 3500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BB2)
    WaitChrThread(0xFE, 1)

    def lambda_2BD0():
        OP_95(0xFE, -10500, 0, 5000, 3500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BD0)
    Return()

    # Function_21_2BA0 end

    def Function_22_2BE6(): pass

    label("Function_22_2BE6")

    OP_92(0xFE, 0xFFFFE69C, 0xBB8, 0x1F4)

    def lambda_2BF8():
        OP_95(0xFE, -5500, 0, 5000, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BF8)
    WaitChrThread(0xFE, 1)

    def lambda_2C16():
        OP_95(0xFE, -10500, 0, 5000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C16)
    Return()

    # Function_22_2BE6 end

    def Function_23_2C2C(): pass

    label("Function_23_2C2C")

    OP_92(0xFE, 0xFFFFE69C, 0xBB8, 0x1F4)

    def lambda_2C3E():
        OP_95(0xFE, -6500, 0, 5000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C3E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_2C2C end

    def Function_24_2C58(): pass

    label("Function_24_2C58")

    EventBegin(0x1)
    Sleep(50)

    #C0141
    ChrTalk(
        0x101,
        (
            "#0000F这边好像是二楼的观众席吧。\x02\x03",

            "四处乱转会给人添麻烦的，\x01",
            "还是不要进去了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -8260, 2500, 14010, 90)
    EventEnd(0x4)
    Return()

    # Function_24_2C58 end

    def Function_25_2CC2(): pass

    label("Function_25_2CC2")

    EventBegin(0x1)
    Sleep(50)

    #C0142
    ChrTalk(
        0x101,
        (
            "#0000F这边好像是二楼的观众席吧。\x02\x03",

            "四处乱转会给人添麻烦的，\x01",
            "还是不要进去了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 5760, 2500, 13790, 270)
    EventEnd(0x4)
    Return()

    # Function_25_2CC2 end

    SaveToFile()

Try(main)
