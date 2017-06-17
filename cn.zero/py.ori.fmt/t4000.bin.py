from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t4000.bin",                # FileName
        "t4000",                    # MapName
        "t4000",                    # Location
        0x005D,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 93, 0, 3, 0, 4],
    )

    BuildStringList((
        "t4000",                  # 0
        "罗兰德祭司",             # 1
        "久久修女",               # 2
        "塔米尔",                 # 3
        "哈米尔",                 # 4
        "艾丝蒂尔",               # 5
        "约修亚",                 # 6
        "游击士林",               # 7
        "游击士艾欧莉娅",         # 8
        "游客弗恩缇亚努",         # 9
        "玛因兹山道",             # 10
    ))

    AddCharChip((
        "chr/ch25400.itc",                   # 00
        "chr/ch25500.itc",                   # 01
        "chr/ch23800.itc",                   # 02
        "chr/ch00600.itc",                   # 03
        "chr/ch00700.itc",                   # 04
        "chr/ch32000.itc",                   # 05
        "chr/ch32100.itc",                   # 06
        "chr/ch32400.itc",                   # 07
    ))

    DeclNpc(-2630,   0,       9369,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(2299,    0,       14270,   180,  257,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-5780,   0,       14529,   180,  385,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-5780,   0,       13680,   0,    385,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(21059,   0,       40569,   90,   405,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(20940,   0,       44159,   180,  389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-9,      0,       5010,    0,    389,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(1200,    0,       4199,    315,  389,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-1940,   9,       19950,   0,    385,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)

    DeclActor(-10390,  500,     13820,   1200,    -10390,  2000,    13820,   0x007C, 0,  18, 0x0000)

    PlaceName(5.0, -0.0, -35.0, 0x0000, 0x0000, "玛因兹山道")

    ScpFunction((
        "Function_0_234",          # 00, 0
        "Function_1_2EC",          # 01, 1
        "Function_2_43D",          # 02, 2
        "Function_3_49E",          # 03, 3
        "Function_4_621",          # 04, 4
        "Function_5_634",          # 05, 5
        "Function_6_F11",          # 06, 6
        "Function_7_1F41",         # 07, 7
        "Function_8_21DE",         # 08, 8
        "Function_9_24B1",         # 09, 9
        "Function_10_2550",        # 0A, 10
        "Function_11_2837",        # 0B, 11
        "Function_12_29AC",        # 0C, 12
        "Function_13_2D19",        # 0D, 13
        "Function_14_2DB6",        # 0E, 14
        "Function_15_2E22",        # 0F, 15
        "Function_16_2F0C",        # 10, 16
        "Function_17_37A2",        # 11, 17
        "Function_18_3BA5",        # 12, 18
    ))


    def Function_0_234(): pass

    label("Function_0_234")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_274"),
        (1, "loc_280"),
        (2, "loc_28C"),
        (3, "loc_298"),
        (4, "loc_2A4"),
        (5, "loc_2B0"),
        (6, "loc_2BC"),
        (SWITCH_DEFAULT, "loc_2C8"),
    )


    label("loc_274")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_280")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_28C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_298")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2A4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2B0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2EB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2EB")

    Return()

    # Function_0_234 end

    def Function_1_2EC(): pass

    label("Function_1_2EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43C")
    OP_95(0xFE, -2510, 0, 14270, 2000, 0x0)
    OP_95(0xFE, -2510, 0, 12920, 2000, 0x0)
    OP_95(0xFE, 11020, 0, 12920, 2000, 0x0)
    OP_95(0xFE, 18830, 0, 20000, 2000, 0x0)
    OP_95(0xFE, 18830, 0, 24520, 2000, 0x0)
    OP_95(0xFE, 26350, 0, 31740, 2000, 0x0)
    OP_95(0xFE, 26350, 0, 46780, 2000, 0x0)
    OP_95(0xFE, 23030, 0, 51110, 2000, 0x0)
    OP_95(0xFE, 23030, 0, 54060, 2000, 0x0)
    OP_95(0xFE, 21080, 0, 54060, 2000, 0x0)
    OP_95(0xFE, 21080, 0, 48950, 2000, 0x0)
    OP_95(0xFE, 25050, 0, 44720, 2000, 0x0)
    OP_95(0xFE, 25050, 0, 34580, 2000, 0x0)
    OP_95(0xFE, 17430, 0, 27090, 2000, 0x0)
    OP_95(0xFE, 17430, 0, 21180, 2000, 0x0)
    OP_95(0xFE, 9240, 0, 14270, 2000, 0x0)
    Jump("Function_1_2EC")

    label("loc_43C")

    Return()

    # Function_1_2EC end

    def Function_2_43D(): pass

    label("Function_2_43D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49D")
    OP_95(0xFE, 23000, 0, 42000, 6000, 0x0)
    OP_95(0xFE, 19000, 0, 42000, 6000, 0x0)
    OP_95(0xFE, 19000, 0, 39000, 6000, 0x0)
    OP_95(0xFE, 23000, 0, 39000, 6000, 0x0)
    Jump("Function_2_43D")

    label("loc_49D")

    Return()

    # Function_2_43D end

    def Function_3_49E(): pass

    label("Function_3_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4B6")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_5DB")

    label("loc_4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4C4")
    Jump("loc_5DB")

    label("loc_4C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4DC")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_5DB")

    label("loc_4DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4EA")
    Jump("loc_5DB")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 2)), scpexpr(EXPR_END)), "loc_4F8")
    Jump("loc_5DB")

    label("loc_4F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_510")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_5DB")

    label("loc_510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_528")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_5DB")

    label("loc_528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_578")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, 23000, 0, 41500, 0)
    SetChrPos(0xB, 23000, 0, 39000, 0)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_5DB")

    label("loc_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_586")
    Jump("loc_5DB")

    label("loc_586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_59E")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_5DB")

    label("loc_59E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5AC")
    Jump("loc_5DB")

    label("loc_5AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5BA")
    Jump("loc_5DB")

    label("loc_5BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5C8")
    Jump("loc_5DB")

    label("loc_5C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5DB")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_5DB")

    BeginChrThread(0x9, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FC")
    SetMapFlags(0x10000000)
    Event(0, 16)
    Jump("loc_60D")

    label("loc_5FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60D")
    Event(0, 17)

    label("loc_60D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_620")
    ClearChrFlags(0x10, 0x80)

    label("loc_620")

    Return()

    # Function_3_49E end

    def Function_4_621(): pass

    label("Function_4_621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_633")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)

    label("loc_633")

    Return()

    # Function_4_621 end

    def Function_5_634(): pass

    label("Function_5_634")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6B0")

    #C0001
    ChrTalk(
        0xFE,
        (
            "太阳下山了呢……\x01",
            "在能见度不好的黄昏，\x01",
            "魔兽的危险度也会增加。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "若打算去郊外街道的话，\x01",
            "请多加注意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0D")

    label("loc_6B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6F5")

    #C0003
    ChrTalk(
        0xFE,
        (
            "今天警备队的\x01",
            "上士来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "到底有什么事呢……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_F0D")

    label("loc_6F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_777")

    #C0005
    ChrTalk(
        0xFE,
        (
            "我感觉克洛斯贝尔最近\x01",
            "好像变得更加危险了。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "大圣堂作为主日学校的授课点，\x01",
            "聚集了很多孩子们，必须多加留心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0D")

    label("loc_777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7E8")

    #C0007
    ChrTalk(
        0xFE,
        (
            "下午好，\x01",
            "欢迎来到克洛斯贝尔大圣堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "今天是主日学校的开课日，\x01",
            "请注意不要妨碍\x01",
            "到老师上课。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0D")

    label("loc_7E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_839")

    #C0009
    ChrTalk(
        0xFE,
        "哎呀……就要回去了吗？\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "欢迎随时再来。\x01",
            "愿女神保佑各位……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0D")

    label("loc_839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_AD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A67")

    #C0011
    ChrTalk(
        0xFE,
        (
            "下午好，\x01",
            "欢迎来到克洛斯贝尔大圣堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x153,
        "#1110F下午好！我是琪雅！\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "哈哈……这么有精神，真是再好不过了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 3)), scpexpr(EXPR_END)), "loc_A5F")

    #C0014
    ChrTalk(
        0x101,
        (
            "#0000F那个……请问\x01",
            "玛布尔老师在吗？\x02\x03",

            "我想跟她商量一下\x01",
            "有关这个孩子的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        "哎呀，是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "玛布尔修女她\x01",
            "正在主日学校的教室里\x01",
            "处理杂事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#0000F啊，是这样啊……\x01",
            "谢谢你。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_9BC")

    #C0018
    ChrTalk(
        0x102,
        (
            "#0104F呼，太好了，\x01",
            "老师好像在呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A18")

    label("loc_9BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_9E8")

    #C0019
    ChrTalk(
        0x103,
        "#0200F真是位热心的人呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A18")

    label("loc_9E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_A18")

    #C0020
    ChrTalk(
        0x104,
        (
            "#0300F似乎没有\x01",
            "与那位修女错过啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A18")


    #C0021
    ChrTalk(
        0x101,
        (
            "#0000F……好了，那么快一点去\x01",
            "找玛布尔老师吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x153,
        "#1109F出发～！\x02",
    )

    CloseMessageWindow()

    label("loc_A5F")

    SetScenarioFlags(0x0, 0)
    Jump("loc_AD3")

    label("loc_A67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 3)), scpexpr(EXPR_END)), "loc_AA9")

    #C0023
    ChrTalk(
        0xFE,
        (
            "玛布尔修女她\x01",
            "正在主日学校的教室里\x01",
            "处理杂事呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD3")

    label("loc_AA9")


    #C0024
    ChrTalk(
        0xFE,
        "呵呵……小孩子最重要的就是要有精神。\x02",
    )

    CloseMessageWindow()

    label("loc_AD3")

    Jump("loc_F0D")

    label("loc_AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_B8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4B")

    #C0025
    ChrTalk(
        0xFE,
        (
            "纪念庆典期间大圣堂内\x01",
            "会举行弥撒。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "今天纪念庆典也要结束了……\x01",
            "最后再加把劲吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B87")

    label("loc_B4B")


    #C0027
    ChrTalk(
        0xFE,
        (
            "今天纪念庆典也要结束了……\x01",
            "我想再加把劲\x01",
            "做好守卫工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B87")

    Jump("loc_F0D")

    label("loc_B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_BEE")

    #C0028
    ChrTalk(
        0xFE,
        (
            "这几天，纪念庆典\x01",
            "真是盛况空前呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "那么多的人，\x01",
            "让守卫工作变得也很辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0D")

    label("loc_BEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C4A")

    #C0030
    ChrTalk(
        0xFE,
        (
            "纪念庆典期间大圣堂内\x01",
            "会举行弥撒。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "似乎也有很多国外游客\x01",
            "前来造访呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0D")

    label("loc_C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_CE0")

    #C0032
    ChrTalk(
        0xFE,
        (
            "纪念庆典期间大圣堂内\x01",
            "会举行弥撒。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "各位若想参加，\x01",
            "就请自便吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "举办弥撒期间还会给\x01",
            "孩子们发放点心，\x01",
            "若不嫌弃，请务必收下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0D")

    label("loc_CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_D52")

    #C0035
    ChrTalk(
        0xFE,
        (
            "今天也是个吉日，\x01",
            "仪式似乎能平安无事地顺利结束呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "这样的日子\x01",
            "要是可以永远持续下去就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0D")

    label("loc_D52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_E6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DEB")

    #C0037
    ChrTalk(
        0xFE,
        (
            "今天主日学校要在\x01",
            "讲堂开课。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "为了避免可疑人员进入\x01",
            "我正在此处进行守卫……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "不过你们……\x01",
            "好像是警察吧，\x01",
            "请过去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E65")

    label("loc_DEB")


    #C0040
    ChrTalk(
        0xFE,
        (
            "为了保护聚集在这里的孩子们的安全，\x01",
            "作为守卫的我必须要严加留心。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "比如之前的狼形魔兽骚乱，\x01",
            "危险事件实在是太多了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E65")

    Jump("loc_F0D")

    label("loc_E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_F0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EEF")

    #C0042
    ChrTalk(
        0xFE,
        (
            "身为教区长的艾拉尔达大主教\x01",
            "正在这所克洛斯贝尔大圣堂里\x01",
            "传授七耀的教诲。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        "在教会用地内请保持安静。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F0D")

    label("loc_EEF")


    #C0044
    ChrTalk(
        0xFE,
        "在教会用地内请保持安静。\x02",
    )

    CloseMessageWindow()

    label("loc_F0D")

    TalkEnd(0xFE)
    Return()

    # Function_5_634 end

    def Function_6_F11(): pass

    label("Function_6_F11")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1054")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FEB")

    #C0045
    ChrTalk(
        0xFE,
        (
            "我在这里做修女的工作，\x01",
            "差不多也快半年了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "因此也认识了许多\x01",
            "市民和孩子们……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "但与玛布尔修女比起来，\x01",
            "我还远远不够成熟。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "真希望有一天，我也能成为\x01",
            "像她一样的出色修女……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_104F")

    label("loc_FEB")


    #C0049
    ChrTalk(
        0xFE,
        (
            "我在这里做修女的工作，\x01",
            "差不多也快半年了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "真希望有一天我也能成为\x01",
            "像她一样出色的修女……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_104F")

    Jump("loc_1F3D")

    label("loc_1054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1110")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E2")

    #C0051
    ChrTalk(
        0xFE,
        (
            "今天来的那位警备队上士，\x01",
            "私下里也会经常\x01",
            "来这里祈祷。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "记得是叫诺艾尔吧……\x01",
            "真是个有礼貌又心地善良的人啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_110B")

    label("loc_10E2")


    #C0053
    ChrTalk(
        0xFE,
        (
            "诺艾尔小姐私下里\x01",
            "也经常来这里祈祷。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_110B")

    Jump("loc_1F3D")

    label("loc_1110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_116A")

    #C0054
    ChrTalk(
        0xFE,
        (
            "塔米尔和哈米尔\x01",
            "经常会来这里玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "那个……\x01",
            "哎，好像搞不清方向了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F3D")

    label("loc_116A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_12C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1254")

    #C0056
    ChrTalk(
        0xFE,
        (
            "今天东街的\x01",
            "孩子们来了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "……话说回来，现在的孩子们\x01",
            "都懂事得很早呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "比如库塔，小小年纪\x01",
            "就对各家店铺的打折情况\x01",
            "了解得非常清楚。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "刚才他告诉了我一些物价便宜的店，\x01",
            "稍后就去那里买东西好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_12BF")

    label("loc_1254")


    #C0060
    ChrTalk(
        0xFE,
        (
            "今天东街的\x01",
            "孩子们来了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "现在的孩子都懂事得很早，\x01",
            "作为大人的我\x01",
            "还真觉得自己的地位岌岌可危呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BF")

    Jump("loc_1F3D")

    label("loc_12C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_1545")
    TurnDirection(0xFE, 0x153, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F5")

    #C0062
    ChrTalk(
        0xFE,
        (
            "说起来……\x01",
            "你没有在主日学校\x01",
            "上学吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x153,
        (
            "#1111F上学？\x01",
            "琪雅也要去那里吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#0003F那、那个……\x01",
            "情况解释起来有些麻烦，\x01",
            "但这个孩子的情况比较特殊，所以现在……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "啊，不……\x01",
            "都怪我这么刨根问底的，\x01",
            "真是对不起。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "但要是以后能来上学了……\x01",
            "请一定要送她来主日学校哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "多了个小伙伴，\x01",
            "其他的孩子们也肯定会非常高兴的……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x153,
        "#1110F嗯，如果琪雅有兴趣的话～！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_148B")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_14D2")

    label("loc_148B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_14B1")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_14D2")

    label("loc_14B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_14D2")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_14D2")

    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)
    SetScenarioFlags(0x0, 1)
    Jump("loc_1540")

    label("loc_14F5")


    #C0069
    ChrTalk(
        0xFE,
        (
            "那个……小琪雅，\x01",
            "希望你以后能来主日学校哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        "我们一定会欢迎你的。\x02",
    )

    CloseMessageWindow()

    label("loc_1540")

    Jump("loc_1F3D")

    label("loc_1545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_178E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165D")
    TurnDirection(0xFE, 0x153, 0)

    #C0071
    ChrTalk(
        0xFE,
        (
            "……哎呀，好可爱呢！\x01",
            "呵呵，你叫什么名字呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x153,
        (
            "#1110F琪雅的名字叫做琪雅哦！\x02\x03",

            "#1109F……啊，姐姐你\x01",
            "打扮得好有趣～\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "是、是吗？\x01",
            "这只是一般的修女服而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x153,
        "#1111F修……女？\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        (
            "#0003F（嗯，七耀教会的事，\x01",
            "　琪雅基本都不知道吗……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1789")

    label("loc_165D")


    #C0076
    ChrTalk(
        0xFE,
        (
            "打扮得好有趣……打扮得好有趣……\x01",
            "是这样吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "莫非……\x01",
            "被孩子们小瞧的原因是\x01",
            "这身衣服……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1700")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_1747")

    label("loc_1700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_1726")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_1747")

    label("loc_1726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1747")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1747")

    Sleep(1000)

    #C0078
    ChrTalk(
        0x101,
        (
            "#0006F那、那个……童言无忌，\x01",
            "我觉得您还是别太在意比较好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1789")

    Jump("loc_1F3D")

    label("loc_178E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1883")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1832")

    #C0079
    ChrTalk(
        0xFE,
        (
            "我听说过有关各位的传闻哦。\x01",
            "一个小孩子在街上迷路了……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "随后很多人都看到\x01",
            "你们为了帮助他\x01",
            "而四处奔走呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        "呵呵，立下大功了呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_187E")

    label("loc_1832")


    #C0082
    ChrTalk(
        0xFE,
        (
            "各位昨天真是立下大功了呢，\x01",
            "竟然能在那么广阔的自治州中\x01",
            "找到迷路的孩子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_187E")

    Jump("loc_1F3D")

    label("loc_1883")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1A11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_198A")

    #C0083
    ChrTalk(
        0xFE,
        (
            "我总是被孩子们小看，\x01",
            "虽然曾经找玛布尔修女\x01",
            "商量过这件事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "可是她却说\x01",
            "『那是因为你很讨\x01",
            "  孩子们的喜欢』。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        "……到底是怎么一回事呢？\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "裙子突然被掀，\x01",
            "这算是被孩子们喜欢吗……？？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "我还是一个新人，不是很明白。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A0C")

    label("loc_198A")


    #C0088
    ChrTalk(
        0xFE,
        (
            "裙子突然被掀\x01",
            "或是突然受到攻击……\x01",
            "这算是被孩子喜欢吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "我要是能变得像玛布尔修女\x01",
            "那样老练的话，\x01",
            "是不是就能明白了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A0C")

    Jump("loc_1F3D")

    label("loc_1A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1B6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1A")

    #C0090
    ChrTalk(
        0xFE,
        (
            "我觉得自己好像\x01",
            "总会被孩子们小瞧。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "今天也是，一个来参加弥撒的男孩\x01",
            "突然就踢了我的屁股……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "但在我生气地追着他到处跑时，\x01",
            "却不知不觉的变得开心起来，\x01",
            "最后两个人都在开始笑了。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "作为一个修女，\x01",
            "我想采取更加清楚\x01",
            "而果断的态度……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B66")

    label("loc_1B1A")


    #C0094
    ChrTalk(
        0xFE,
        (
            "总觉得我\x01",
            "很容易被孩子们小看。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "啊……下次找玛布尔修女\x01",
            "商量一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B66")

    Jump("loc_1F3D")

    label("loc_1B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1C81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C46")

    #C0096
    ChrTalk(
        0xFE,
        (
            "昨天带孩子来做礼拜的客人\x01",
            "比想象中的多了不少，\x01",
            "真是辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "以至于事先烤制好的曲奇\x01",
            "根本就不够，\x01",
            "很多孩子都哭了……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "嗯，真是对不起那些孩子呢。\x01",
            "今晚之前，必须要\x01",
            "烤更多更多的曲奇。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C7C")

    label("loc_1C46")


    #C0099
    ChrTalk(
        0xFE,
        (
            "为了避免\x01",
            "曲奇不够的情况，\x01",
            "所以今天必须多烤一点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C7C")

    Jump("loc_1F3D")

    label("loc_1C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1CDB")

    #C0100
    ChrTalk(
        0xFE,
        (
            "今天要举办弥撒，\x01",
            "所以主日学校放假。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "如果有空的话，\x01",
            "请务必参加哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F3D")

    label("loc_1CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1E5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E24")

    #C0102
    ChrTalk(
        0xFE,
        (
            "我很擅长做料理，\x01",
            "孩子们来主日学校的时候，\x01",
            "我就会给他们做午饭。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "不过最近挑食的孩子\x01",
            "增加了不少……\x01",
            "这正是我发挥手艺的时候。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "在孩子们喜欢吃的东西中，\x01",
            "悄悄混入一些他们不喜欢吃的东西，\x01",
            "借此让他们逐渐习惯。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "之后再透露其中混入了他们讨厌的食物，\x01",
            "那个时候孩子们的表情……\x01",
            "真的是非常有趣啊⊥\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E58")

    label("loc_1E24")


    #C0106
    ChrTalk(
        0xFE,
        (
            "让孩子们变得不挑食\x01",
            "是件非常有趣的事情。\x01",
            "呵呵。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E58")

    Jump("loc_1F3D")

    label("loc_1E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1F3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE7")

    #C0107
    ChrTalk(
        0xFE,
        (
            "哎呀……\x01",
            "来大圣堂是有什么事情吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "还是说……各位\x01",
            "是来扫墓的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "沿着岔道一直走的话\x01",
            "就是墓地了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F3D")

    label("loc_1EE7")


    #C0110
    ChrTalk(
        0xFE,
        (
            "如果是来扫墓的话，\x01",
            "请沿着岔道一直走。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "安眠于此的灵魂们\x01",
            "也一定会感到喜悦的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F3D")

    TalkEnd(0xFE)
    Return()

    # Function_6_F11 end

    def Function_7_1F41(): pass

    label("Function_7_1F41")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1F89")

    #C0112
    ChrTalk(
        0xA,
        (
            "啊，已经这么晚了……\x01",
            "不快点回家的话会被妈妈骂的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21DA")

    label("loc_1F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1F97")
    Jump("loc_21DA")

    label("loc_1F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2011")

    #C0113
    ChrTalk(
        0xA,
        (
            "我们只有在主日学校放假的时候，\x01",
            "才会来这里玩耍。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "这么宽阔的地方，不拿来做\x01",
            "游戏的话，不是很浪费嘛～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21DA")

    label("loc_2011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_201F")
    Jump("loc_21DA")

    label("loc_201F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_20F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_203A")
    Call(0, 10)
    Jump("loc_20F0")

    label("loc_203A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_20A0")
    TurnDirection(0xA, 0x153, 0)

    #C0115
    ChrTalk(
        0xA,
        (
            "啊，要回去了啊……\x01",
            "……下次见面的时候再一起玩吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x153,
        "#1100F嗯，可以哦～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_20F0")

    label("loc_20A0")


    #C0117
    ChrTalk(
        0xA,
        (
            "（哈米尔这小子……\x01",
            "  就算这孩子再怎么可爱，\x01",
            "  你也有点兴奋过头了吧～……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20F0")

    Jump("loc_21DA")

    label("loc_20F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_213B")

    #C0118
    ChrTalk(
        0xA,
        "这个姐姐说她是游击士。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xA,
        "啊哈哈，看不出来呢～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_21DA")

    label("loc_213B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2149")
    Jump("loc_21DA")

    label("loc_2149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2157")
    Jump("loc_21DA")

    label("loc_2157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2165")
    Jump("loc_21DA")

    label("loc_2165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2173")
    Jump("loc_21DA")

    label("loc_2173")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2181")
    Jump("loc_21DA")

    label("loc_2181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_21DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_219C")
    Call(0, 9)
    Jump("loc_21DA")

    label("loc_219C")


    #C0120
    ChrTalk(
        0xA,
        (
            "我跟哈米尔虽然是双胞胎，\x01",
            "但是这家伙几乎没有\x01",
            "运动神经呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21DA")

    TalkEnd(0xFE)
    Return()

    # Function_7_1F41 end

    def Function_8_21DE(): pass

    label("Function_8_21DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2230")

    #C0121
    ChrTalk(
        0xB,
        (
            "做小孩子最痛苦的地方就是有门限啊。\x01",
            "肚子也饿了，快点回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24AD")

    label("loc_2230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_223E")
    Jump("loc_24AD")

    label("loc_223E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_22A5")

    #C0122
    ChrTalk(
        0xB,
        "喂，塔米尔，今天要做些什么呢？\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xB,
        (
            "在外面到处跑的话会很累，\x01",
            "还是跟修女一起说话吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24AD")

    label("loc_22A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_22B3")
    Jump("loc_24AD")

    label("loc_22B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_23B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22CE")
    Call(0, 10)
    Jump("loc_23B0")

    label("loc_22CE")

    TurnDirection(0xB, 0x153, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2365")

    #C0124
    ChrTalk(
        0xB,
        (
            "啊，你要回去了啊……\x01",
            "……那个，下次一起读书吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x153,
        (
            "#1109F嘿嘿，可以哦～\x01",
            "反正琪雅也很喜欢读书。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xB,
        "（好、好可爱啊……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_23B0")

    label("loc_2365")


    #C0127
    ChrTalk(
        0xB,
        "（哈……好可爱啊……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0128
    ChrTalk(
        0x153,
        "#1105F嗯……？\x02",
    )

    CloseMessageWindow()

    label("loc_23B0")

    Jump("loc_24AD")

    label("loc_23B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_241D")

    #C0129
    ChrTalk(
        0xB,
        (
            "呼……呼……\x01",
            "……玩得好累啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        (
            "塔米尔，我们给姐姐他们添麻烦了，\x01",
            "还是快点回去吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24AD")

    label("loc_241D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_242B")
    Jump("loc_24AD")

    label("loc_242B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2439")
    Jump("loc_24AD")

    label("loc_2439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2447")
    Jump("loc_24AD")

    label("loc_2447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2455")
    Jump("loc_24AD")

    label("loc_2455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2463")
    Jump("loc_24AD")

    label("loc_2463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_24AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247E")
    Call(0, 9)
    Jump("loc_24AD")

    label("loc_247E")


    #C0131
    ChrTalk(
        0xB,
        (
            "嘁……真是的，\x01",
            "四肢发达、头脑简单的家伙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24AD")

    TalkEnd(0xFE)
    Return()

    # Function_8_21DE end

    def Function_9_24B1(): pass

    label("Function_9_24B1")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)

    #C0132
    ChrTalk(
        0xA,
        (
            "好了，哈米尔！\x01",
            "接下来要玩什么呢！？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xB,
        (
            "呼……呼……\x01",
            "等、等一下，塔米尔，\x01",
            "稍微休息一下吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        "什么啊，你还真没用。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_9_24B1 end

    def Function_10_2550(): pass

    label("Function_10_2550")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)

    #C0135
    ChrTalk(
        0xA,
        "好了，哈米尔，今天要玩些什么呢？\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xB,
        "嗯～我想要在家里玩……\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x153,
        (
            "#1105F哇，一模一样的脸！\x01",
            "好厉害啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x153, 400)
    TurnDirection(0xB, 0x153, 400)
    Sleep(400)

    #C0138
    ChrTalk(
        0xA,
        "哎……\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xB,
        "（好、好可爱……）\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x153,
        "#1110F喂喂，你们的脸为什么一样呢？\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        (
            "那、那个……\x01",
            "我跟哈米尔是双胞胎。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xB,
        (
            "没、没错哦！很不可思议吧！？\x01",
            "好像是叫同卵双胞胎……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x153,
        "#1111F……双胞胎？\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        (
            "#0004F（嗯，果然都是小孩子……\x01",
            "　很快就混熟了。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_273C")

    #C0145
    ChrTalk(
        0x102,
        "#0100F（呵呵，总觉得很令人欣慰呢。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_281D")

    label("loc_273C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_277D")

    #C0146
    ChrTalk(
        0x103,
        (
            "#0203F（只有琪雅才\x01",
            "  这么擅于和别人相处啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_281D")

    label("loc_277D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_281D")

    #C0147
    ChrTalk(
        0x104,
        (
            "#0300F（可恶的臭小鬼们……\x01",
            "  要是敢一直盯着我家可爱的女儿，\x01",
            "  罗伊德可不会放过你们的。）\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        (
            "#0006F（为、为什么要在这里\x01",
            "  把我的名字搬出来……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_281D")

    SetScenarioFlags(0xAE, 0)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_10_2550 end

    def Function_11_2837(): pass

    label("Function_11_2837")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_29A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2951")

    #C0149
    ChrTalk(
        0xC,
        (
            "#0802F好了好了，孩子们！\x01",
            "乖乖站好哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(500)

    #C0150
    ChrTalk(
        0xC,
        (
            "#0801F……啊，真是的，根本一点\x01",
            "都不听我的话……\x02\x03",

            "#0809F你们要是再这么调皮的话，\x01",
            "姐姐也就不客气了哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x102,
        "#0109F（艾、艾丝蒂尔小姐……）\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x104,
        "#0309F（嗯，好像很开心的样子……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_29A8")

    label("loc_2951")


    #C0153
    ChrTalk(
        0xC,
        (
            "#0809F再不适可而止的话，\x01",
            "我可就要挠你们痒痒了哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xA,
        "啊哈哈哈！\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xB,
        "呀哈哈哈！\x02",
    )

    CloseMessageWindow()

    label("loc_29A8")

    TalkEnd(0xFE)
    Return()

    # Function_11_2837 end

    def Function_12_29AC(): pass

    label("Function_12_29AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2D15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C43")

    #C0156
    ChrTalk(
        0x101,
        (
            "#0002F你们好啊，约修亚。\x01",
            "两位看上去好像很高兴啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xD,
        (
            "#0902F哈哈，我们是来给这里的大主教\x01",
            "送东西的……\x02\x03",

            "不过，跟预想相同，艾丝蒂尔\x01",
            "被孩子们缠上了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x103,
        "#0202F气氛好像十分热烈呢。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x102,
        (
            "#0102F呵呵，因为艾丝蒂尔小姐\x01",
            "很受孩子欢迎嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xD,
        (
            "#0904F说得也是……艾丝蒂尔从\x01",
            "以前开始就很受孩子们欢迎呢。\x02\x03",

            "#0900F该怎么说呢，这也可以\x01",
            "算是一种才能吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFE)

    #C0161
    ChrTalk(
        0xD,
        (
            "#0903F……昨天真是太谢谢你们了。\x02\x03",

            "感觉我跟艾丝蒂尔\x01",
            "心中的结\x01",
            "终于解开了。\x02\x03",

            "#0902F请让我正式向你们道声谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        (
            "#0011F不，你言重了……\x01",
            "我们并没有做什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x104,
        (
            "#0304F哎，想要道谢的话。\x01",
            "等顺利抓住那个让人头痛的\x01",
            "小姑娘之后再说吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xD,
        "#0909F哈哈……说得也是呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB4, 0)
    Jump("loc_2D15")

    label("loc_2C43")


    #C0165
    ChrTalk(
        0xD,
        (
            "#0904F纪念庆典也终于到了最后一天。\x02\x03",

            "#0900F再怎么说，应该也\x01",
            "不会比昨天更忙了吧，\x01",
            "我们不要掉以轻心，互相加油，继续努力吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D12")

    #C0166
    ChrTalk(
        0x101,
        (
            "#0002F啊，好的。\x02\x03",

            "#0003F（在这种气氛下，\x01",
            "　没法提起竞拍会呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D12")

    SetScenarioFlags(0x0, 4)

    label("loc_2D15")

    TalkEnd(0xFE)
    Return()

    # Function_12_29AC end

    def Function_13_2D19(): pass

    label("Function_13_2D19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2DB2")

    #C0167
    ChrTalk(
        0xFE,
        (
            "我是受艾拉尔达大主教所托，\x01",
            "来这里送药材的。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "多亏了艾欧莉娅帮我挑选，\x01",
            "这项工作才能顺利完成呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "真不愧是拥有医生资格证\x01",
            "的人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DB2")

    TalkEnd(0xFE)
    Return()

    # Function_13_2D19 end

    def Function_14_2DB6(): pass

    label("Function_14_2DB6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E1E")

    #C0170
    ChrTalk(
        0xFE,
        (
            "那个，这种药草再加上\x01",
            "有滋补效果的果实……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "……嗯，似乎没有纰漏呢。\x01",
            "快点送过去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E1E")

    TalkEnd(0xFE)
    Return()

    # Function_14_2DB6 end

    def Function_15_2E22(): pass

    label("Function_15_2E22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E97")

    #C0172
    ChrTalk(
        0xFE,
        (
            "话说回来，克洛斯贝尔的教堂\x01",
            "可真够气派的。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "相比我所去过的教区的教堂，\x01",
            "要大上一两倍呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2F08")

    label("loc_2E97")


    #C0174
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的教堂\x01",
            "可真够气派呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "即使是与七耀教会的总部——\x01",
            "亚尔特利亚法典国的圣堂比起来\x01",
            "也毫不逊色呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F08")

    TalkEnd(0xFE)
    Return()

    # Function_15_2E22 end

    def Function_16_2F0C(): pass

    label("Function_16_2F0C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_11(0xA0, 0xDC, 0xDC, 0x3C, 0x64, 0x0)
    OP_68(13460, 3600, 9960, 0)
    MoveCamera(310, 9, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(31000, 0)
    SetChrPos(0x101, 600, 0, -6100, 0)
    SetChrPos(0x153, 0, 0, -4500, 0)
    SetChrPos(0xEF, -600, 0, -6100, 0)
    FadeToBright(1000, 0)
    OP_68(13460, 10600, 9960, 10000)
    PlaceName2(100, 40, "c_plac33", 0x0, 4000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_11(0xA0, 0xDC, 0xDC, 0x3C, 0x64, 0x0)
    OP_68(0, 900, -4500, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(17900, 0)
    OP_0D()

    #C0176
    ChrTalk(
        0x153,
        (
            "#1105F#5P咦咦～……\x02\x03",

            "#1110F好大的建筑物啊，\x01",
            "这里就是教堂吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        (
            "#0004F#6P是啊……\x01",
            "这里是克洛斯贝尔大圣堂哦。\x02\x03",

            "#0001F当然，琪雅应该也在\x01",
            "某处的教堂做过礼拜……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x153, 0xB4, 0x1F4)

    #C0178
    ChrTalk(
        0x153,
        "#1100F#11P？？？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_313B")

    #C0179
    ChrTalk(
        0x102,
        (
            "#0106F#5P但是普通城市的教堂\x01",
            "应该没有这么大呢……\x02\x03",

            "#0100F这里好像无法成为小琪雅\x01",
            "恢复记忆的契机呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_321A")

    label("loc_313B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_31B0")

    #C0180
    ChrTalk(
        0x103,
        (
            "#0206F#5P但是普通城市的教堂\x01",
            "应该不会有这么大吧……\x02\x03",

            "#0200F这里似乎无法成为琪雅\x01",
            "恢复记忆的契机呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_321A")

    label("loc_31B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_321A")

    #C0181
    ChrTalk(
        0x104,
        (
            "#0306F#5P我说，普通城市的教堂\x01",
            "应该没这么大的……\x02\x03",

            "#0300F似乎无法成为阿琪\x01",
            "恢复记忆的契机呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_321A")

    TurnDirection(0x101, 0xEF, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 3)), scpexpr(EXPR_END)), "loc_3414")

    #C0182
    ChrTalk(
        0x101,
        (
            "#0006F#12P……好像是啊。\x02\x03",

            "#0000F不过算了，总之先\x01",
            "找玛布尔老师谈谈吧。\x02\x03",

            "说不定还会给我们介绍\x01",
            "教会的相关专家呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_330B")

    #C0183
    ChrTalk(
        0x102,
        (
            "#0104F#5P说得也是，找玛布尔老师\x01",
            "一定不会有错的……\x02\x03",

            "#0102F那么，赶快去\x01",
            "主日学校的教室吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_340C")

    label("loc_330B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3393")

    #C0184
    ChrTalk(
        0x103,
        (
            "#0202F#5P说到玛布尔老师，\x01",
            "就是那位之前跟罗伊德前辈你们\x01",
            "说过话的主日学校的修女吧。\x02\x03",

            "那么，赶快前往\x01",
            "主日学校的教室吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_340C")

    label("loc_3393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_340C")

    #C0185
    ChrTalk(
        0x104,
        (
            "#0302F#5P玛布尔老师就是\x01",
            "之前跟罗伊德和大小姐说过话的\x01",
            "主日学校的修女对吧。\x02\x03",

            "那么，赶快去\x01",
            "主日学校的教室吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_340C")

    OP_57(0x0)
    OP_5A()
    Jump("loc_3785")

    label("loc_3414")


    #C0186
    ChrTalk(
        0x101,
        (
            "#0006F#12P……好像是呢。\x02\x03",

            "#0000F没关系，总之先\x01",
            "找认识的人商量一下吧。\x02\x03",

            "我以前曾受过主日学校一位老师\x01",
            "的多方照顾。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_366B")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0187
    ChrTalk(
        0x102,
        (
            "#0105F#5P咦，莫非你指的是……\x01",
            "修女玛布尔老师吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        (
            "#0005F#12P是啊，没错……\x02\x03",

            "#0004F原来如此，艾莉自然也\x01",
            "在这所主日学校上过学啊。\x02\x03",

            "#0000F但是我们上课的日子不同，\x01",
            "所以之前从没有见过。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x102,
        (
            "#0102F#5P呵呵，是啊……\x01",
            "而且我之后就去留学了。\x02\x03",

            "#0106F嗯，要是从小就认识的话，\x01",
            "如今的进展或许就会稍微再……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        "#0005F#12P哎……？\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x102,
        (
            "#0112F#5P没、没什么啦。\x02\x03",

            "#0104F那个，我觉得找玛布尔老师\x01",
            "一定不会有错。\x02\x03",

            "#0100F快点去圣堂里面的\x01",
            "主日学校拜会她吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3782")

    label("loc_366B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_36FC")

    #C0192
    ChrTalk(
        0x103,
        (
            "#0202F#5P原来如此，\x01",
            "看来确实是找对人了呢。\x02\x03",

            "那么我们赶快去\x01",
            "主日学校的教室吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x101,
        "#0000F#12P是啊，教室就在位于正面的圣堂里。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3782")

    label("loc_36FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3782")

    #C0194
    ChrTalk(
        0x104,
        (
            "#0300F#5P原来如此，\x01",
            "看来是找对人了啊。\x02\x03",

            "那我们赶快去\x01",
            "主日学校的教室吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x101,
        "#0000F#12P是啊，教室就在位于正面的圣堂里。\x02",
    )

    CloseMessageWindow()

    label("loc_3782")

    OP_57(0x0)
    OP_5A()

    label("loc_3785")

    SetChrPos(0x0, 0, 0, -4500, 0)
    SetScenarioFlags(0xA8, 1)
    OP_29(0x48, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_16_2F0C end

    def Function_17_37A2(): pass

    label("Function_17_37A2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_68(-200, 2950, 35510, 0)
    MoveCamera(325, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24530, 0)
    SetChrPos(0x101, -500, 2000, 37440, 180)
    SetChrPos(0x153, 870, 2000, 38370, 180)
    SetChrPos(0xEF, -370, 2000, 39460, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x10, 0x0, 0x0)
    Sound(121, 0, 100, 0)
    OP_79(0x0)
    OP_68(-200, 2950, 31510, 4500)

    def lambda_3878():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3878)

    def lambda_388D():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_388D)

    def lambda_38A2():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_38A2)

    def lambda_38B7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_38B7)
    Sleep(300)

    def lambda_38CB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_38CB)
    Sleep(300)

    def lambda_38DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_38DF)
    Sleep(1500)
    OP_71(0x0, 0x10, 0x0, 0x0, 0x0)
    Sound(890, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 1)

    def lambda_3912():
        TurnDirection(0xFE, 0xEF, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3912)
    WaitChrThread(0x153, 1)

    def lambda_3923():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_3923)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0xEF, 2)
    WaitChrThread(0x153, 2)
    OP_6F(0x1)

    #C0196
    ChrTalk(
        0x101,
        "#0000F#6P那么，接下来是去乌尔斯拉医院吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)
    Sleep(100)
    TurnDirection(0xEF, 0x153, 500)

    #C0197
    ChrTalk(
        0x101,
        (
            "#0001F#5P看来要走很长一段路了。\x01",
            "……琪雅，累了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x153,
        (
            "#1110F#12P完全不累！\x02\x03",

            "#1109F散步真开心啊！\x01",
            "琪雅最喜欢在外面散步了！\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x101,
        "#0012F#5P哈哈，真有精神呢。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3A92")

    #C0200
    ChrTalk(
        0x102,
        (
            "#0109F#5P呵呵，那我们就\x01",
            "快点去南出口吧。\x02\x03",

            "#0102F如果乘坐巴士，\x01",
            "我想是用不了多长时间的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B59")

    label("loc_3A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3B01")

    #C0201
    ChrTalk(
        0x103,
        (
            "#0202F#5P呵呵……那么\x01",
            "快点去南出口吧。\x02\x03",

            "#0204F我想，如果乘坐巴士，\x01",
            "应该不会花费太长时间吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B59")

    label("loc_3B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3B59")

    #C0202
    ChrTalk(
        0x104,
        (
            "#0304F#5P哈哈，那就\x01",
            "赶快去南出口吧。\x02\x03",

            "#0302F如果坐巴士的话，\x01",
            "一会就到了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B59")

    OP_93(0x153, 0x10E, 0x1F4)
    Sleep(300)

    #C0203
    ChrTalk(
        0x153,
        "#1110F#12P哦哦，我们走！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 2000, 32200, 180)
    SetScenarioFlags(0xA8, 3)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_17_37A2 end

    def Function_18_3BA5(): pass

    label("Function_18_3BA5")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0204
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～克洛斯贝尔大圣堂宿舍～\x01",
            "　来做礼拜的各位请前往\x01",
            "　    　礼拜堂。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_3BA5 end

    SaveToFile()

Try(main)
