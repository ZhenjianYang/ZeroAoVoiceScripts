from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1440.bin",                # FileName
        "c1440",                    # MapName
        "c1440",                    # Location
        0x0031,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 49, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1440",                  # 0
        "亚修莉",                 # 1
        "金格",                   # 2
        "哈缇娜修女",             # 3
        "游击士林",               # 4
        "游击士艾欧莉娅",         # 5
        "加尔西亚",               # 6
    ))

    AddCharChip((
        "chr/ch09200.itc",                   # 00
        "chr/ch23900.itc",                   # 01
        "chr/ch25500.itc",                   # 02
        "chr/ch32000.itc",                   # 03
        "chr/ch32100.itc",                   # 04
    ))

    DeclNpc(-2859,   0,       13750,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(5670,    29,      8649,    225,  261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(2930,    0,       7659,    315,  389,  0x0, 0,   2,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-2170,   19,      5400,    180,  389,  0x0, 0,   3,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-2170,   29,      4110,    0,    389,  0x0, 0,   4,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 17,  9.899999618530273,     14.0,                  -0.5,                  16.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -2.4749999046325684,   -7.0,                  0.10000000149011612,   1.0])

    DeclActor(4590,    0,       7540,    1000,    5670,    1500,    8650,    0x007E, 0,  9,  0x0000)

    ScpFunction((
        "Function_0_21C",          # 00, 0
        "Function_1_2D4",          # 01, 1
        "Function_2_3FE",          # 02, 2
        "Function_3_451",          # 03, 3
        "Function_4_246D",         # 04, 4
        "Function_5_289F",         # 05, 5
        "Function_6_2A6C",         # 06, 6
        "Function_7_2CCC",         # 07, 7
        "Function_8_2EFF",         # 08, 8
        "Function_9_3547",         # 09, 9
        "Function_10_354B",        # 0A, 10
        "Function_11_4B49",        # 0B, 11
        "Function_12_4EEB",        # 0C, 12
        "Function_13_53C5",        # 0D, 13
        "Function_14_5490",        # 0E, 14
        "Function_15_5594",        # 0F, 15
        "Function_16_5787",        # 10, 16
        "Function_17_5EA5",        # 11, 17
    ))


    def Function_0_21C(): pass

    label("Function_0_21C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_25C"),
        (1, "loc_268"),
        (2, "loc_274"),
        (3, "loc_280"),
        (4, "loc_28C"),
        (5, "loc_298"),
        (6, "loc_2A4"),
        (SWITCH_DEFAULT, "loc_2B0"),
    )


    label("loc_25C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_268")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_274")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_280")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_28C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_298")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_2A4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_2B0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_2BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_2D3")

    Return()

    # Function_0_21C end

    def Function_1_2D4(): pass

    label("Function_1_2D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EA")
    Event(0, 16)

    label("loc_2EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2F8")
    Jump("loc_3FD")

    label("loc_2F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_310")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_3FD")

    label("loc_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_31E")
    Jump("loc_3FD")

    label("loc_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_351")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 1850, 0, 8750, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34C")
    SetChrFlags(0x8, 0x10)

    label("loc_34C")

    Jump("loc_3FD")

    label("loc_351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_364")
    SetChrFlags(0x8, 0x80)
    Jump("loc_3FD")

    label("loc_364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_372")
    Jump("loc_3FD")

    label("loc_372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_391")
    SetChrPos(0x8, 1810, 0, 10210, 135)
    Jump("loc_3FD")

    label("loc_391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_39F")
    Jump("loc_3FD")

    label("loc_39F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3B2")
    SetChrFlags(0x8, 0x80)
    Jump("loc_3FD")

    label("loc_3B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3C0")
    Jump("loc_3FD")

    label("loc_3C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3EE")
    SetChrPos(0x8, -1940, 30, 10250, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E9")
    SetChrFlags(0x8, 0x10)

    label("loc_3E9")

    Jump("loc_3FD")

    label("loc_3EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FD")
    SetChrFlags(0x8, 0x10)

    label("loc_3FD")

    Return()

    # Function_1_2D4 end

    def Function_2_3FE(): pass

    label("Function_2_3FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_417")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_41D")

    label("loc_417")

    OP_10(0x0, 0x1)
    OP_10(0x3, 0x0)

    label("loc_41D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_439")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_450")

    label("loc_439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_450")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_450")

    label("loc_450")

    Return()

    # Function_2_3FE end

    def Function_3_451(): pass

    label("Function_3_451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EB")
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_491")
    Call(0, 7)
    SetScenarioFlags(0x6B, 3)
    Jump("loc_5E3")

    label("loc_491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4A2")
    Call(0, 4)
    Jump("loc_5E3")

    label("loc_4A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4B6")
    Call(0, 7)
    SetScenarioFlags(0x6B, 3)
    Jump("loc_5E3")

    label("loc_4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_539")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_531")

    #C0001
    ChrTalk(
        0x8,
        (
            "修女最近总是纠缠不休，\x01",
            "时不时就跑到这里来。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "真是个烦人的女人啊，\x01",
            "恨不得把她的舌头拔下来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_534")

    label("loc_531")

    Call(0, 5)

    label("loc_534")

    Jump("loc_5E3")

    label("loc_539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_547")
    Jump("loc_5E3")

    label("loc_547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_55B")
    Call(0, 7)
    SetScenarioFlags(0x6B, 3)
    Jump("loc_5E3")

    label("loc_55B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_59A")

    #C0003
    ChrTalk(
        0x8,
        (
            "接下来，要对那些货品\x01",
            "进行库存整理，还有……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E3")

    label("loc_59A")


    #C0004
    ChrTalk(
        0x8,
        "哎呀呀，又有新产品吗？\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "嘁……商品管理的麻烦程度\x01",
            "又要增加了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E3")

    TalkEnd(0xFE)
    Jump("loc_246C")

    label("loc_5EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_606")
    Call(0, 7)
    Jump("loc_6D3")

    label("loc_606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_617")
    Call(0, 4)
    Jump("loc_6D3")

    label("loc_617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_628")
    Call(0, 7)
    Jump("loc_6D3")

    label("loc_628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6B1")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6A6")

    #C0006
    ChrTalk(
        0x8,
        (
            "修女最近总是纠缠不休，\x01",
            "时不时就跑到这里来。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "真是个烦人的女人啊，\x01",
            "恨不得把她的舌头拔下来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A9")

    label("loc_6A6")

    Call(0, 5)

    label("loc_6A9")

    TalkEnd(0xFE)
    Jump("loc_6D3")

    label("loc_6B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6BF")
    Jump("loc_6D3")

    label("loc_6BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6D0")
    Call(0, 7)
    Jump("loc_6D3")

    label("loc_6D0")

    Call(0, 8)

    label("loc_6D3")

    Jump("loc_246C")

    label("loc_6D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FA")
    Call(0, 6)
    Jump("loc_246C")

    label("loc_6FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_86C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_775")

    #C0008
    ChrTalk(
        0x8,
        "听说空港那边收到了炸弹恐吓信？\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "呵呵，虽然不知道是什么人干的，\x01",
            "但还真是够高调大胆的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_867")

    label("loc_775")


    #C0010
    ChrTalk(
        0x8,
        "听说空港那边收到了炸弹恐吓信？\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "空港要是真被人炸掉，\x01",
            "我也会很头疼的……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "在这种时候，也只能期待\x01",
            "一下克洛斯贝尔警察的表现啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        (
            "#0305F（身为黑市掮客，竟然能满不在乎地\x01",
            "　说出这种话……）\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        "#0106F（听起来只是在讽刺呢……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_867")

    Jump("loc_2469")

    label("loc_86C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_87D")
    Call(0, 4)
    Jump("loc_2469")

    label("loc_87D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_974")

    #C0015
    ChrTalk(
        0xFE,
        (
            "我女儿最近很想要个\x01",
            "什么什么的玩偶呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "你们几个，如果有空的话，\x01",
            "能不能陪她玩玩呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "因为我平时总是很忙，\x01",
            "她好像感觉很无聊呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#0003F这、这个………\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x104,
        (
            "#0300F（看起来，她的走私生意似乎\x01",
            "　很红火呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD3, 5)
    Jump("loc_BB9")

    label("loc_974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A38")

    #C0020
    ChrTalk(
        0x8,
        (
            "对了，关于那件事情，\x01",
            "本以为达德利会来找我的，\x01",
            "结果却没有啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "真奇怪啊，如果是平时的他，\x01",
            "肯定会一马当先地四处调查的。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#0001F（达德利警官他……\x01",
            "　现在不方便行动啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB9")

    label("loc_A38")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0023
    ChrTalk(
        0x101,
        (
            "#0005F对了……\x02\x03",

            "#0001F那个，莫非你们这里\x01",
            "也出售那种危险的药物吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        "危险的药物……？\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "啊啊，你难道是指\x01",
            "『带来幸运的蓝色药片』……\x01",
            "这个传闻吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "很不巧，没有呢。\x01",
            "呼，那些东西的流通渠道\x01",
            "与我们毫不相干呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        "#0203F……是吗。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#0101F不过，根据传闻，\x01",
            "好像确实是如此呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        (
            "#0301F但毕竟是无风不起浪……\x02\x03",

            "那种药，该不会已经\x01",
            "大范围销售了吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_BB9")

    Jump("loc_2469")

    label("loc_BBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_E19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C3D")

    #C0030
    ChrTalk(
        0x8,
        (
            "不过，不管怎么说……\x01",
            "加尔西亚那家伙也真是辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "他自从加入鲁巴彻之后，\x01",
            "头发好像白了不少吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E14")

    label("loc_C3D")


    #C0032
    ChrTalk(
        0x8,
        "哎呀呀，终于下手了啊。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "如果曹那家伙真被惹火了，\x01",
            "也许会在克洛斯贝尔市内直接开战吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0034
    ChrTalk(
        0x101,
        (
            "#0003F……请不要说这种\x01",
            "令人不安的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        (
            "#0301F这话说得\x01",
            "还真是超级直接……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        (
            "#0200F那个，难道说，\x01",
            "您掌握到什么\x01",
            "情报了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "也没多少，袭击事件确实是鲁巴彻\x01",
            "的那些家伙干的，我知道的就这么多。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "我又不是情报商，对这种事也没兴趣。\x01",
            "想调查的话，就去直接找当事人吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_E14")

    Jump("loc_2469")

    label("loc_E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_E9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E94")

    #C0039
    ChrTalk(
        0x8,
        (
            "修女最近总是纠缠不休，\x01",
            "时不时就跑到这里来。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "真是个烦人的女人啊，\x01",
            "恨不得把她的舌头拔下来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E97")

    label("loc_E94")

    Call(0, 5)

    label("loc_E97")

    Jump("loc_2469")

    label("loc_E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1061")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F14")

    #C0041
    ChrTalk(
        0x8,
        "你们出门在外时也要小心。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "『我是为了参观庆典而来』——\x01",
            "嘴上这么说的家伙们，根本不可信。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_105C")

    label("loc_F14")


    #C0043
    ChrTalk(
        0x8,
        (
            "嘁……今天总能隐隐\x01",
            "感觉到一些火药味。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "大概都是因为鲁巴彻\x01",
            "的那个活动吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#0005F那个活动……\x01",
            "难道是指『黑之竞拍会』吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0046
    ChrTalk(
        0x8,
        (
            "什么啊，原来你们\x01",
            "也知道啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "那是从七八年前开始，\x01",
            "由马尔克尼开展的事业。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "拜他所赐，活动当天总会有一些\x01",
            "来意不善的客人到处徘徊……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "嘁，真是让人不爽啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_105C")

    Jump("loc_2469")

    label("loc_1061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_112F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10BA")

    #C0050
    ChrTalk(
        0x8,
        (
            "那么，先把店交给金格看管，\x01",
            "我先去崔尼蒂\x01",
            "喝一杯，放松放松吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_112A")

    label("loc_10BA")


    #C0051
    ChrTalk(
        0x8,
        "库存货物终于清点完毕了。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        "呼～真是忙了好一阵啊。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "纪念庆典期间有很多采购工作，\x01",
            "真是好麻烦啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_112A")

    Jump("loc_2469")

    label("loc_112F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_131D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11FF")

    #C0054
    ChrTalk(
        0x8,
        (
            "在克洛斯贝尔，安放炸弹之类的\x01",
            "恐怖活动早已经不稀奇了。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#0003F可是……我却连一次\x01",
            "都没有听说过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "那是因为消息都被搜查一科压下了。\x01",
            "而且这类事件，基本上也都能防患于未然呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1318")

    label("loc_11FF")


    #C0057
    ChrTalk(
        0x8,
        "今天好像有游行呢。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "呵呵……说起来的话，\x01",
            "大概是十年前左右的事情吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "在游行期间，发生了在花车中\x01",
            "安置炸弹的恐怖事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        "呵呵，希望今年不要出什么乱子啊。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        (
            "#0301F别说这么可怕的话啊……\x01",
            "都开始感到不安了。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "算了，搜查一科也会出动的吧。\x01",
            "你们用不着那么担心啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1318")

    Jump("loc_2469")

    label("loc_131D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1515")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_139F")

    #C0063
    ChrTalk(
        0x8,
        (
            "（点烟）……\x01",
            "加尔西亚那家伙\x01",
            "好像也挺辛苦的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "都是因为加入鲁巴彻那种\x01",
            "组织才会这样的，真是的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1510")

    label("loc_139F")

    OP_93(0x8, 0xB4, 0x0)

    #C0065
    ChrTalk(
        0x8,
        (
            "（点烟）……\x01",
            "加尔西亚那家伙好像很焦躁呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "自己的交易渠道被人\x01",
            "击溃了，所以跑到\x01",
            "我这里来哭诉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#0003F那个……对于这件事，\x01",
            "我们还真的完全看不出来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        (
            "#0300F莫非，你和那个家伙\x01",
            "的关系很好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "以前，在他还没加入鲁巴彻的时候，\x01",
            "曾经来这里交易过好几次。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "呵呵，说简单一点的话，也就是老顾客吧。\x01",
            "但最近这段时间，每次来都是一副嚣张的样子。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1510")

    Jump("loc_2469")

    label("loc_1515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_160E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1569")

    #C0071
    ChrTalk(
        0x8,
        (
            "今天新进了一些好东西哦。\x01",
            "呵呵，想看的话就去和金格说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1609")

    label("loc_1569")


    #C0072
    ChrTalk(
        0x8,
        (
            "今天新进了一些好东西哦。\x01",
            "呵呵，这种进货量真是前所未有。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "在纪念庆典的前后，\x01",
            "生意好了很多，真不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#0006F但对警察来说，\x01",
            "可就不是什么好事了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1609")

    Jump("loc_2469")

    label("loc_160E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_182E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1677")

    #C0075
    ChrTalk(
        0x8,
        (
            "搜查一科的那些家伙\x01",
            "好像正在四处调查些什么呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "算了，反正也\x01",
            "不关我的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1829")

    label("loc_1677")


    #C0077
    ChrTalk(
        0x8,
        "搜查一科的家伙刚才来了。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        "他们好像正在四处调查些什么呢。\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        "#0000F哈哈，是吗……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x102,
        (
            "#0105F这家店难道也\x01",
            "贩卖一些秘密情报吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "可不是哦？\x01",
            "我出售的就只有实体货物而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "不过呢，有时的确也会无意中\x01",
            "探听到一些小道消息。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "像鲁巴彻的传闻，黑月的传闻，\x01",
            "还有蔓延克洛斯贝尔的黑道势力的传闻……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "如果有人来买东西，\x01",
            "说不定我就会顺口\x01",
            "透露一些呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        (
            "#0003F（看上去，对一科来说，\x01",
            "　这里也算是很重要的情报来源呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1829")

    Jump("loc_2469")

    label("loc_182E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1C9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 7)), scpexpr(EXPR_END)), "loc_1A0F")

    #C0086
    ChrTalk(
        0x8,
        (
            "听说黑月的曹是个计谋派，\x01",
            "手腕相当高明。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "呵呵……在进行斗争的时候，\x01",
            "他的手段也总是稳扎稳打，一点都不可爱。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        (
            "我也开始有点\x01",
            "产生兴趣了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A0A")

    #C0089
    ChrTalk(
        0x102,
        (
            "#0101F那个……您能不能停止\x01",
            "向他们双方提供武器呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "呵呵……无所谓啊。虽然不算是正式答应你，\x01",
            "但以现在的情况，也没有卖给他们武器的必要了。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "因为他们双方已经都\x01",
            "拥有非常充足的武器储备了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 0)

    label("loc_1A0A")

    Jump("loc_1C98")

    label("loc_1A0F")


    #C0092
    ChrTalk(
        0x8,
        "曹好像要开始进行一些有趣的活动了。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        (
            "以鲁巴彻为对手，\x01",
            "这招出得还真是相当漂亮嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0094
    ChrTalk(
        0x101,
        (
            "#0005F曹……？\x02\x03",

            "难道是黑月首领\x01",
            "的名字吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "嗯，是啊……\x01",
            "其实我也没见过他。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "但好像是被派到克洛斯贝尔的『分公司经理』呢。\x01",
            "听说，不管是组织间的斗争也好，公司的管理也好，\x01",
            "他的手腕都相当高明。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        (
            "先在克洛斯贝尔站稳脚跟，\x01",
            "然后再转守为攻。\x01",
            "就黑手党来说，这手段确实很稳扎稳打呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        (
            "#0101F莫非……\x01",
            "最近的事故如此频繁，\x01",
            "就是因为黑月进入攻势了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#0303F难怪最近这一个月，\x01",
            "觉得突发事件好像多了不少呢……\x02\x03",

            "#0301F全都是因为那些家伙在别人\x01",
            "察觉不到的地方暗中进行斗争吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 7)

    label("loc_1C98")

    Jump("loc_2469")

    label("loc_1C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1F9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E07")

    #C0100
    ChrTalk(
        0x8,
        (
            "这款新型重机关枪是从\x01",
            "上个星期才开始流通的，\x01",
            "我马上就进了货。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "……鲁巴彻的家伙们\x01",
            "似乎也买了不少，\x01",
            "你们可要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0102
    ChrTalk(
        0x101,
        (
            "#0003F我们确实不希望有人\x01",
            "在市内使用那种危险武器啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x104,
        (
            "#0306F如果血肉之躯被打中，\x01",
            "恐怕一瞬间就会变成筛子了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F96")

    label("loc_1E07")


    #C0104
    ChrTalk(
        0x104,
        (
            "#0305F嗯，那是……\x01",
            "莱恩福尔特公司制造的重型机关枪……？\x02\x03",

            "看起来好像是新型的……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        "嗯，这是上周才刚刚开始销售的新品。\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "呵呵……不仅是可填装的子弹数量增加了，\x01",
            "威力似乎也强化了两成左右呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        "红毛，你要不要拿去试试看啊？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0108
    ChrTalk(
        0x104,
        (
            "#0305F不、不必了……\x02\x03",

            "#0306F我说，你居然把这种走私品\x01",
            "拿到警察的面前招摇啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x102,
        "#0106F唉，真是的……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1F96")

    Jump("loc_2469")

    label("loc_1F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_20DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1FF3")

    #C0110
    ChrTalk(
        0x8,
        "哎呀呀，没办法……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "把店交给金格看管，\x01",
            "我先出去转转吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D7")

    label("loc_1FF3")


    #C0112
    ChrTalk(
        0x8,
        (
            "稍后和帝国的人还有\x01",
            "一场推脱不开的商谈呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "嘁，我可是低血压呢。\x01",
            "明明和他们说过，\x01",
            "不要一大早就把我叫出去的……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#0005F（商谈……\x01",
            "　是关于武器的进购吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x104,
        (
            "#0301F（大概吧……帝国好像也有\x01",
            "　规模很大的制造商。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_20D7")

    Jump("loc_2469")

    label("loc_20DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_22D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2179")

    #C0116
    ChrTalk(
        0x8,
        (
            "警备队好像也更换了\x01",
            "新规格的导力器呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "除了一直以来的几种旧回路之外，\x01",
            "新型的回路也开始流通了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x8,
        "不过数量还很少就是了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22CC")

    label("loc_2179")

    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0119
    ChrTalk(
        0x103,
        (
            "#0205F啊……\x02\x03",

            "那是艾尼格玛专用的\x01",
            "新型回路啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        "嗯，好像是吧。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        "这些都是警备队倒卖给我的东西。\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "嘁，可是新型的导力器还没有普及，\x01",
            "这种回路就算倒卖给我，\x01",
            "也很难转手啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#0003F警备队……\x01",
            "还会干这种事吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#0300F这种事情很常见啊。\x01",
            "在那些高层的大老爷之中，\x01",
            "存在着不少腐败的家伙呢……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_22CC")

    Jump("loc_2469")

    label("loc_22D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2362")

    #C0125
    ChrTalk(
        0x8,
        (
            "算了，他们之间的斗争\x01",
            "跟我一点关系也没有。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "只要生意红火，\x01",
            "我就无所谓。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x104,
        (
            "#0306F（这种话还真是\x01",
            "　典型的掮客台词啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2469")

    label("loc_2362")


    #C0128
    ChrTalk(
        0x8,
        (
            "那么，这些都是黑月订购的货。\x01",
            "差不多也该开始搬运出去了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#0005F黑月……\x01",
            "是那个东方的黑手党组织吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    #C0130
    ChrTalk(
        0x8,
        "嗯，你知道啊。\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x8,
        (
            "每次出现新产品的时候，\x01",
            "他们都会购买一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        (
            "哼哼……大概是想在这些东西流通到鲁巴彻之前，\x01",
            "提前先把性能摸清吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_2469")

    TalkEnd(0xFE)

    label("loc_246C")

    Return()

    # Function_3_451 end

    def Function_4_246D(): pass

    label("Function_4_246D")

    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    TurnDirection(0x8, 0x10A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 1)), scpexpr(EXPR_END)), "loc_2583")

    #C0133
    ChrTalk(
        0x8,
        (
            "以后还想问什么秘密情报的话，\x01",
            "就再过来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x8,
        (
            "哼哼，你也算是老客户了，\x01",
            "总得给点特别服务啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x103,
        "#0205F（达德利警官是这里的常客吗？）\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x10A,
        (
            "#0603F（这里是很有力的情报来源处，\x01",
            "　我们之间是互利互惠的合作关系……\x01",
            "　这也算是办案的一个环节。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2886")

    label("loc_2583")


    #C0137
    ChrTalk(
        0x8,
        "哟，这不是达德利吗？\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        (
            "今天是来维修手枪的吗？\x01",
            "还是想收集什么情报？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x10A,
        (
            "#0603F……亚修莉小姐，\x01",
            "请容我冒昧地问一句……\x02\x03",

            "#0600F你们这家店应该没有销售\x01",
            "违禁药物之类的东西吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0140
    ChrTalk(
        0x101,
        "#0001F（达德利警官……还真是开门见山啊……）\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "呵呵……『带来幸运的蓝色药片』……\x01",
            "你要问的是这个传闻吧？\x01",
            "我就猜到你该来问这个了。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "很不巧，我们可没有销售这东西，\x01",
            "但最近时常听到关于它的传闻呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x8,
        "大概也就是这两三周的事。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x10A,
        (
            "#0603F是吗……\x02\x03",

            "#0600F失礼了，\x01",
            "那就请忘掉我刚才说的话吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        (
            "了解。\x01",
            "作为补偿，来买点东西吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x8,
        (
            "刚进了一批新型的穿甲弹，\x01",
            "很适合你那把枪使用呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x10A,
        "#0603F……多谢推荐了。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x102,
        "#0101F（这两个人……莫非……）\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x104,
        "#0301F（一直都是这样的关系吗？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCE, 1)

    label("loc_2886")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0x8)
    Return()

    # Function_4_246D end

    def Function_5_289F(): pass

    label("Function_5_289F")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0150
    ChrTalk(
        0x8,
        "真是的，到底要说多少遍才能听懂……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    #C0151
    ChrTalk(
        0x8,
        (
            "金格，我说你，\x01",
            "应该学过算术吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x8,
        (
            "将莱恩福尔特公司制造的来复枪，\x01",
            "以一支一万五千米拉的价格卖出去。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x8,
        "一周内一共卖掉了四十支。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x8,
        "总销售额是多少呢？\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x9,
        "嗯～……\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x9,
        "……是六十万米拉！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 500)

    #C0157
    ChrTalk(
        0x8,
        "回答得很完美哦。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xA,
        (
            "……一点都不完美！真是的，\x01",
            "题目居然用这种内容……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    ClearChrFlags(0x8, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_5_289F end

    def Function_6_2A6C(): pass

    label("Function_6_2A6C")

    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    TurnDirection(0x8, 0x104, 500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AC4")

    #C0159
    ChrTalk(
        0x8,
        (
            "对了，红毛，\x01",
            "你对军用品了解得还真是详细啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF5")

    label("loc_2AC4")


    #C0160
    ChrTalk(
        0x8,
        (
            "对了，红毛，\x01",
            "你对军用品了解得还真是详细啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AF5")


    #C0161
    ChrTalk(
        0x8,
        "你是军人吧？\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0162
    ChrTalk(
        0x104,
        (
            "#0305F哎……？\x02\x03",

            "#0300F哈哈，那个……\x01",
            "以前确实曾在警备队待过一阵子。\x02\x03",

            "不过严格来说，\x01",
            "警备队并不是军队，\x01",
            "所以我也算不上是军人……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        (
            "红色的长发……\x01",
            "再加上那副看似很有战斗经验的面孔……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    #C0164
    ChrTalk(
        0x8,
        "嗯～……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0165
    ChrTalk(
        0x104,
        "#0305F……那个，难道有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x8,
        "不，没什么。\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x8,
        (
            "打扰了。\x01",
            "以后如果有什么需要，\x01",
            "还请再来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        (
            "#0005F咦、咦……\x01",
            "（怎么回事呢……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 2)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xFE)
    Return()

    # Function_6_2A6C end

    def Function_7_2CCC(): pass

    label("Function_7_2CCC")

    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    TurnDirection(0x8, 0x0, 0)

    #C0169
    ChrTalk(
        0x8,
        (
            "……你们不是警察局的那个什么科的人吗。\x01",
            "呵呵，看起来好像很有精神啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x8,
        (
            "要来挑点什么吗？\x01",
            "最近进了不少好货哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#0006F不必了，那个……\x01",
            "这里毕竟是经营走私品的店，\x01",
            "我们总不能……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x104,
        (
            "#0306F这家店还是一点都没变，可疑得很。\x01",
            "全都是一些走私货……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x8,
        (
            "表面上却伪装成贩卖\x01",
            "酒与食品的店。\x01",
            "呵呵……有什么不满吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x103,
        (
            "#0200F算了，我听说，\x01",
            "这里的销售对象主要都是\x01",
            "国外的军队与猎兵团……\x02\x03",

            "这两者并不像鲁巴彻那样具有威胁性，\x01",
            "所以大可睁一只眼闭一只眼……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x102,
        (
            "#0106F这种店竟然能明目张胆地开在这里，\x01",
            "实在是令人叹息呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 1)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0x8)
    Return()

    # Function_7_2CCC end

    def Function_8_2EFF(): pass

    label("Function_8_2EFF")

    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0176
    ChrTalk(
        0x8,
        (
            "六十把莱恩福尔特公司的\x01",
            "２４口径型号，还有……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x102,
        (
            "#0101F（我说，罗伊德……）\x02\x03",

            "（我看到那边的那个木箱里\x01",
            "　装着手枪呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x103,
        (
            "#0201F（……而那边的那个木箱里\x01",
            "　好像全都是弹药呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x104,
        (
            "#0301F（炸药、手榴弹……\x01",
            "　那边还有防弹背心和\x01",
            "　榴弹枪用的榴弹……）\x02\x03",

            "#0306F（哇，那个铁桶里装的\x01",
            "　不就是警备队使用的\x01",
            "　液体燃料吗？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0180
    ChrTalk(
        0x101,
        (
            "#0001F那、那个……打扰一下。\x02\x03",

            "不好意思，请问这里\x01",
            "是家什么样的店呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x8, 0x0, 500)

    #C0181
    ChrTalk(
        0x8,
        (
            "……嗯嗯？\x01",
            "怎么，是客人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x8,
        "我只是个中间商而已啊。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x8,
        (
            "而这家店经营从各处\x01",
            "收购来的各式武器。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x8,
        (
            "你们是新来的警察吧？\x01",
            "呵呵，都是些生面孔呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x101,
        "#0005F中、中间商……\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x104,
        (
            "#0303F……当然前面还要加上『黑市』二字。\x02\x03",

            "#0301F说起来，我倒是听说过\x01",
            "这样的传闻，在克洛斯贝尔存在着\x01",
            "一些经营范围相当广的商店……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        (
            "#0101F私下出售武器和来路不正的货物……\x01",
            "难道你们与鲁巴彻……？\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x8,
        (
            "哎呀呀……\x01",
            "不要把我和那些差劲的\x01",
            "黑手党相提并论啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x8,
        (
            "我可是个认真勤奋的经销商。\x01",
            "和十多个国家的军队、猎兵团\x01",
            "都有生意上的往来。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x8,
        (
            "其中可不包括不分场合滥用武器的小鬼，\x01",
            "而且如果不会被找麻烦，\x01",
            "就算和警察做生意也无所谓。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x8,
        (
            "……事实上，克洛斯贝尔警察局搜查一科的警官们，\x01",
            "也会定期来这里露个面呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x8,
        (
            "哈，不过他们会来，\x01",
            "一半为购物，另一半好像\x01",
            "打算调查案件相关情报呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x103,
        (
            "#0200F也就是说……对警察来说，\x01",
            "这里也有利用价值啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        (
            "#0003F不管怎么说，\x01",
            "还是非常可疑呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x8,
        (
            "呵呵，你们要不要\x01",
            "也来买点什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x8,
        (
            "……只是，我不会把武器\x01",
            "卖给没有信用的家伙。\x01",
            "干我们这行的，也都有自己的规矩呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x8,
        (
            "如果你们可以接受，\x01",
            "就去柜台那里\x01",
            "和我女儿说吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 1)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0x8)
    Return()

    # Function_8_2EFF end

    def Function_9_3547(): pass

    label("Function_9_3547")

    Call(0, 10)
    Return()

    # Function_9_3547 end

    def Function_10_354B(): pass

    label("Function_10_354B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_356A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3565")
    Call(0, 11)
    SetScenarioFlags(0x6B, 3)
    Return()

    label("loc_3565")

    Jump("loc_3578")

    label("loc_356A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3578")
    Call(0, 12)
    Return()

    label("loc_3578")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3585")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B45")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",              # 0
            "交换（装备）\x01",      # 1
            "交换（回路）\x01",      # 2
            "交换（其它）\x01",      # 3
            "放弃\x01",              # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3601")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3601")

    RunExpression(0x4, (scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D3, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_366B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_362A")
    OP_AF(0x90)
    Jump("loc_365C")

    label("loc_362A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_363A")
    OP_AF(0x8F)
    Jump("loc_365C")

    label("loc_363A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_364A")
    OP_AF(0x8E)
    Jump("loc_365C")

    label("loc_364A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_365A")
    OP_AF(0x8D)
    Jump("loc_365C")

    label("loc_365A")

    OP_AF(0x8C)

    label("loc_365C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B40")

    label("loc_366B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_368A")
    OP_AF(0x9A)
    Jump("loc_36BC")

    label("loc_368A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_369A")
    OP_AF(0x99)
    Jump("loc_36BC")

    label("loc_369A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_36AA")
    OP_AF(0x98)
    Jump("loc_36BC")

    label("loc_36AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_36BA")
    OP_AF(0x97)
    Jump("loc_36BC")

    label("loc_36BA")

    OP_AF(0x96)

    label("loc_36BC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B40")

    label("loc_36CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_374D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_36EA")
    OP_AF(0xA4)
    Jump("loc_372C")

    label("loc_36EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_36FA")
    OP_AF(0xA5)
    Jump("loc_372C")

    label("loc_36FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_370A")
    OP_AF(0xA3)
    Jump("loc_372C")

    label("loc_370A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_371A")
    OP_AF(0xA2)
    Jump("loc_372C")

    label("loc_371A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_372A")
    OP_AF(0xA1)
    Jump("loc_372C")

    label("loc_372A")

    OP_AF(0xA0)

    label("loc_372C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D3, 0x0)"), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3748")
    SetScenarioFlags(0x9D, 5)

    label("loc_3748")

    Jump("loc_4B40")

    label("loc_374D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3761")
    Jump("loc_4B40")

    label("loc_3761")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B40")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_37C4")

    #C0198
    ChrTalk(
        0x9,
        "客人，我们马上就要打烊了～\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x9,
        "想买东西的话就快点吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B40")

    label("loc_37C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3A5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 5)), scpexpr(EXPR_END)), "loc_3917")

    #C0200
    ChrTalk(
        0x9,
        (
            "咪西一只……\x01",
            "咪西两只……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x9,
        (
            "『……上校，接下来\x01",
            "  就要开始雪中行军了！』\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x9,
        (
            "啊～咪西大战\x01",
            "果然最好玩了～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_390F")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0203
    ChrTalk(
        0x101,
        "#0006F（硝烟味好浓的过家家……）\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x103,
        (
            "#0200F（那些『咪西』们\x01",
            "　现在过得幸福吗……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_390F")

    SetScenarioFlags(0x0, 1)
    Jump("loc_3A57")

    label("loc_3917")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A22")

    #C0205
    ChrTalk(
        0x9,
        "嗯～要来买点什么吗？\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x9,
        (
            "既然是常客，\x01",
            "给你们优惠一点也没问题哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x9,
        "好，附送一颗子弹。\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0208
    ChrTalk(
        0x102,
        (
            "#0106F（让小孩子在这种地方工作，\x01",
            "　没问题吗……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3A57")

    label("loc_3A22")


    #C0209
    ChrTalk(
        0x9,
        "啊～今天很闲呢～\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x9,
        (
            "但妈妈最近还是\x01",
            "特别忙呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A57")

    Jump("loc_4B40")

    label("loc_3A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3BBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3AC9")

    #C0211
    ChrTalk(
        0x9,
        (
            "妈妈她啊～在生下金格之前，\x01",
            "在战乱地区开店呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x9,
        (
            "听说还经常与客人\x01",
            "发生枪战呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BBA")

    label("loc_3AC9")


    #C0213
    ChrTalk(
        0x9,
        "那个～……\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x9,
        "我们店根本不怕什么袭击。\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x9,
        (
            "因为妈妈都已经习惯啦～\x01",
            "马上就会把仇给报了～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0216
    ChrTalk(
        0x104,
        "#0306F（这家店的话，确实可以想象……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3BBA")

    Jump("loc_4B40")

    label("loc_3BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3C11")

    #C0217
    ChrTalk(
        0x9,
        (
            "那个～不用在意修女，\x01",
            "随意购物吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x9,
        (
            "金格可是很擅长\x01",
            "算术的～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B40")

    label("loc_3C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3FE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_END)), "loc_3CE6")

    #C0219
    ChrTalk(
        0x9,
        (
            "那个～我们这里\x01",
            "是不接待小孩子的～\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x9,
        (
            "不过，如果想来的话，\x01",
            "就当是来找我玩，那样就没问题啦～\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x153,
        "#1109F嗯，明白啦～！\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x101,
        (
            "#0003F琪雅……在那之前，\x01",
            "一定要先和我们打好招呼哦。\x01",
            "拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FDB")

    label("loc_3CE6")


    #C0223
    ChrTalk(
        0x153,
        (
            "#1110F那个那个，这里是干什么的啊？\x01",
            "总觉得好奇怪哦～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)

    #C0224
    ChrTalk(
        0x9,
        "什、什么啊，你是客人吗？\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x9,
        "我们这里是不接待小孩子的！！\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x153,
        (
            "#1105F哎～是这样的吗～！？\x02\x03",

            "#1108F呜呜，这里摆着这么多东西，\x01",
            "还以为会很有趣呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0227
    ChrTalk(
        0x9,
        (
            "嗯～看来你还是\x01",
            "挺有眼光的嘛～\x01",
            "没办法啦～\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x9,
        (
            "……要不要和金格一起玩呢？\x01",
            "那样的话就没问题了～\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x153,
        "#1109F真的吗？太好了～！\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x9,
        (
            "看啊～这是１８口径的，\x01",
            "这个是２４口径的……\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x153,
        "#1109F嗯嗯¤\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        (
            "#0003F暂停、暂停……\x02\x03",

            "琪雅，不要玩这种危险的游戏。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F35")

    #C0233
    ChrTalk(
        0x102,
        (
            "#0103F她为什么在这种地方\x01",
            "也能与其他孩子玩得那么开心呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FD8")

    label("loc_3F35")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F8D")

    #C0234
    ChrTalk(
        0x103,
        (
            "#0206F没想到琪雅在这种地方\x01",
            "竟然也能与其他孩子玩得那么开心……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FD8")

    label("loc_3F8D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FD8")

    #C0235
    ChrTalk(
        0x104,
        (
            "#0306F在这种地方竟然也能\x01",
            "和别的小鬼玩得那么开心啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FD8")

    SetScenarioFlags(0xB0, 3)

    label("loc_3FDB")

    Jump("loc_4B40")

    label("loc_3FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_409A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4046")

    #C0236
    ChrTalk(
        0x9,
        (
            "……妈妈她之后会不会\x01",
            "带我去看庆典呀～\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x9,
        "她心情好像不太好，大概不行吧～\x02",
    )

    CloseMessageWindow()
    Jump("loc_4095")

    label("loc_4046")


    #C0238
    ChrTalk(
        0x9,
        (
            "啊～庆典啊～……\x01",
            "金格也很想出去～\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x9,
        (
            "可是还要看店啊～\x01",
            "真是没有办法～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4095")

    Jump("loc_4B40")

    label("loc_409A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4102")

    #C0240
    ChrTalk(
        0x9,
        "……客人，您看上去好像很疲劳啊？\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x9,
        "那就买点东西吧！\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x9,
        "买完以后就能打起精神啦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B40")

    label("loc_4102")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_427C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_414B")

    #C0243
    ChrTalk(
        0x9,
        (
            "这个相机也可以\x01",
            "拍出普通的照片，\x01",
            "相当划算呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4277")

    label("loc_414B")


    #C0244
    ChrTalk(
        0x9,
        (
            "刚才有个游客来了，\x01",
            "说要买什么导力相机……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x9,
        (
            "我推荐他买这个带有小型手枪功能的，\x01",
            "结果他就惊慌失措地跑出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x9,
        (
            "真遗憾啊～\x01",
            "这东西可是很好用的哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0247
    ChrTalk(
        0x101,
        (
            "#0006F这家店里难道\x01",
            "只卖危险品吗……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4277")

    Jump("loc_4B40")

    label("loc_427C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4338")

    #C0248
    ChrTalk(
        0x9,
        (
            "嘻嘻……\x01",
            "猎兵大叔，看我的厉害！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4333")

    #C0249
    ChrTalk(
        0x104,
        (
            "#0306F哇啊，这太危险了吧！？\x01",
            "把我吓出了一身冷汗呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x103,
        "#0200F……真是的。\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#0006F这对母子，\x01",
            "平时总是这样吗……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4333")

    Jump("loc_4B40")

    label("loc_4338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_43FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4389")

    #C0252
    ChrTalk(
        0x9,
        "客人，要看点高价货吗？\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x9,
        "虽然很贵，但物有所值啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_43F7")

    label("loc_4389")


    #C0254
    ChrTalk(
        0x9,
        "客人，到新品了哦，\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x9,
        "这次进的可是上等货啊。\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x9,
        (
            "不过价格肯定也很高就是了，\x01",
            "这点小事就不要计较啦～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_43F7")

    Jump("loc_4B40")

    label("loc_43FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_44BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_444D")

    #C0257
    ChrTalk(
        0x9,
        "……客人，买点东西吧！\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x9,
        "一到傍晚就要关门了哦～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_44B6")

    label("loc_444D")


    #C0259
    ChrTalk(
        0x9,
        (
            "因为妈妈说我今天可以\x01",
            "跟她去进货～\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x9,
        (
            "到了傍晚，店就要关门啦。\x01",
            "客人，想买东西的话就早点买吧～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_44B6")

    Jump("loc_4B40")

    label("loc_44BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_46D2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_462D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_452E")

    #C0261
    ChrTalk(
        0x9,
        "妈妈还没回来啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0262
    ChrTalk(
        0x9,
        (
            "好慢啊～\x01",
            "到底在做什么呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4628")

    label("loc_452E")


    #C0263
    ChrTalk(
        0x9,
        "……啊～喂，客人们！\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x9,
        "#4S请不要太吵闹啦！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0265
    ChrTalk(
        0x101,
        "#0006F……对不起。\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x9,
        (
            "会妨碍我们做生意的吧？\x01",
            "是吧？　是吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x9,
        "想玩的话就安静一点！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4628")

    Jump("loc_46CD")

    label("loc_462D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_468B")

    #C0268
    ChrTalk(
        0x9,
        "妈妈还没回来啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0269
    ChrTalk(
        0x9,
        (
            "好慢啊～\x01",
            "到底在做什么呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46CD")

    label("loc_468B")


    #C0270
    ChrTalk(
        0x9,
        (
            "外面那些小鬼，\x01",
            "实在是吵死人了～\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x9,
        "真想去教训他们一顿！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_46CD")

    Jump("loc_4B40")

    label("loc_46D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4785")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4722")

    #C0272
    ChrTalk(
        0x9,
        (
            "今天是妈妈\x01",
            "去喝酒的日子哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x9,
        "有事的话就快说吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4780")

    label("loc_4722")


    #C0274
    ChrTalk(
        0x9,
        "嗯～找妈妈有事吗～？\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x9,
        "有事的话就快说吧。\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x9,
        (
            "妈妈准备清点完\x01",
            "库存之后就去喝酒呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4780")

    Jump("loc_4B40")

    label("loc_4785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4881")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_47E5")

    #C0277
    ChrTalk(
        0x9,
        (
            "妈妈最近都不带我\x01",
            "一起去进货呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x9,
        "呜～每天都留下看店，好无聊啊～\x02",
    )

    CloseMessageWindow()
    Jump("loc_487C")

    label("loc_47E5")


    #C0279
    ChrTalk(
        0x9,
        "听说～最近去进货会很危险啊～\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x9,
        (
            "鲁巴彻的交易场所\x01",
            "好像遭到袭击了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x9,
        (
            "因为很危险，妈妈最近也都\x01",
            "不带我一起去进货了～\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x9,
        "呜～好没意思啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_487C")

    Jump("loc_4B40")

    label("loc_4881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4A94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_48DD")

    #C0283
    ChrTalk(
        0x9,
        (
            "这些１８口径\x01",
            "的子弹很不受欢迎啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x9,
        "嗯～要不要低价处理掉呢～\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A8F")

    label("loc_48DD")


    #C0285
    ChrTalk(
        0x9,
        (
            "普通的子弹放到这边～\x01",
            "火药较多的都放在这边～……\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x9,
        (
            "嗯～……果然还是应该\x01",
            "放进那边的箱子里吧。\x01",
            "那样也许更容易被客人注意到～……\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x9,
        "客人，您是怎么想的呢～？\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0288
    ChrTalk(
        0x101,
        "#0006F这个，这种事情，你就算问我也……\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x102,
        (
            "#0105F啊，还是不要碰那些\x01",
            "危险的东西比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0290
    ChrTalk(
        0x9,
        (
            "不把货物都摆好的话，\x01",
            "客人就不会买了吧～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4A8F")

    Jump("loc_4B40")

    label("loc_4A94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4AF3")

    #C0291
    ChrTalk(
        0x9,
        "妈妈和猎兵们也有来往～\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x9,
        (
            "那个猎兵大叔看上去很凶呢。\x01",
            "他以前也来过店里呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B40")

    label("loc_4AF3")


    #C0293
    ChrTalk(
        0x9,
        "客人，要买点什么吗？\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x9,
        (
            "现金交易可是不行的～\x01",
            "请用适当的东西来交换吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B40")

    Jump("loc_3585")

    label("loc_4B45")

    TalkEnd(0x9)
    Return()

    # Function_10_354B end

    def Function_11_4B49(): pass

    label("Function_11_4B49")

    TalkBegin(0x9)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0295
    ChrTalk(
        0x9,
        (
            "啊，客人～\x01",
            "今天要买点什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x9,
        (
            "啊哈～最近进购了一些\x01",
            "威力比较强大的手榴弹呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x9,
        "用它的话，一枚就能灭掉一个小队～\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        "#0006F啊，这家店还是一如既往地可疑呢……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C8C")

    #C0299
    ChrTalk(
        0x102,
        (
            "#0103F表面上虽然只是个\x01",
            "从事物物交换的店……\x02\x03",

            "但经营范围并不仅限于此，\x01",
            "算是无限接近于黑的灰色行业呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D99")

    label("loc_4C8C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D0B")

    #C0300
    ChrTalk(
        0x103,
        (
            "#0203F表面上虽然是个以物易物\x01",
            "的交换店……\x02\x03",

            "但营业范围不止于此，\x01",
            "可以说是无限接近于黑的灰色行业吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D99")

    label("loc_4D0B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D99")

    #C0301
    ChrTalk(
        0x104,
        (
            "#0303F表面上看，虽然只是个\x01",
            "交换物品的商店……\x02\x03",

            "但实际上，它的营业范围要广得多，\x01",
            "可以说是一家无限接近黑色的灰色店铺吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D99")

    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetChrName("")

    #A0302
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※与金格交谈，并选择『交换』，\x01",
            "　就会出现可交换商品一览表。\x01",
            "　如果携带有交换所需的物品，就可以进行交换。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0303
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※这里的装备与回路都是一些\x01",
            "　在其它地方无法得到的高价稀有品。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0304
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※虽然不用花费米拉，但要用相应的物品\x01",
            "　来进行交换。所以，是否真的需要交换，\x01",
            "　请在仔细考虑之后再做出决定。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetScenarioFlags(0xB3, 4)
    TalkEnd(0x9)
    Return()

    # Function_11_4B49 end

    def Function_12_4EEB(): pass

    label("Function_12_4EEB")

    TalkBegin(0x9)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0305
    ChrTalk(
        0x9,
        "啊，是客人～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    #C0306
    ChrTalk(
        0x9,
        "#4S妈妈～有不认识的客人来了～！\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x9,
        "#4S可以把武器卖给他们吗～？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FF2")
    Sleep(1500)

    #C0308
    ChrTalk(
        0x9,
        "………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x0, 500)

    #C0309
    ChrTalk(
        0x9,
        (
            "啊，抱歉～\x01",
            "妈妈现在不在呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x9,
        (
            "算啦～\x01",
            "你们想买点什么吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5065")

    label("loc_4FF2")


    #C0311
    ChrTalk(
        0x8,
        "#4P哈？没见过的客人啊。\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x8,
        "#4P我现在正忙得焦头烂额呢！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 500)

    #C0313
    ChrTalk(
        0x9,
        "……不管啦～\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x9,
        "你们要不要买点什么呢？\x02",
    )

    CloseMessageWindow()

    label("loc_5065")

    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0315
    ChrTalk(
        0x101,
        "#0005F那个，嗯……\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x102,
        "#0100F这里是家什么店呢？\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x9,
        (
            "货品店，\x01",
            "也就是什么都有。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x9,
        (
            "不过现在只有\x01",
            "药品和回路哦～\x01",
            "嗯～这个，还有这个～……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0319
    ChrTalk(
        0x9,
        (
            "啊，还有就是，不能用现金交易哦～\x01",
            "支付方式是用适当的物品来交换～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0320
    ChrTalk(
        0x103,
        "#0203F啊，感觉真是好可疑呢。\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#0306F也就是说……\x01",
            "这里是一家以物换物\x01",
            "的交换店吧？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetChrName("")

    #A0322
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※与金格交谈，并选择『交换』，\x01",
            "　就会出现可交换商品一览表。\x01",
            "　如果携带有交换所需的物品，就可以进行交换。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0323
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※这里的装备品与回路都是一些\x01",
            "　在其它地方无法得到的高价稀有品。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0324
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※虽然不用花费米拉，但要用相应的物品\x01",
            "　来进行交换。所以，是否真的需要交换，\x01",
            "　请在考虑清楚之后再做出决定。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetScenarioFlags(0x6B, 3)
    SetScenarioFlags(0xB3, 4)
    TalkEnd(0x9)
    Return()

    # Function_12_4EEB end

    def Function_13_53C5(): pass

    label("Function_13_53C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5418")

    #C0325
    ChrTalk(
        0xA,
        (
            "呼……\x01",
            "要想教育旧城区的这些孩子们，\x01",
            "用一般的方法是行不通的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_548C")

    label("loc_5418")


    #C0326
    ChrTalk(
        0xA,
        (
            "虽然曾经多次要求金格\x01",
            "也来参加主日学校的课程，\x01",
            "但每次都吃闭门羹呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xA,
        (
            "亚修莉小姐要是\x01",
            "能予以理解就好了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_548C")

    TalkEnd(0xFE)
    Return()

    # Function_13_53C5 end

    def Function_14_5490(): pass

    label("Function_14_5490")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5590")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5535")

    #C0328
    ChrTalk(
        0xFE,
        (
            "关于昨天的袭击事件，\x01",
            "我想来询问一下情况……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        (
            "但这里的店主\x01",
            "实在是很难接近呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "我不是这里的常客，\x01",
            "所以待在店里挺不舒服的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5590")

    label("loc_5535")


    #C0331
    ChrTalk(
        0xFE,
        (
            "我是那种无论遇到什么事情，\x01",
            "都只依靠自己这一双拳头的类型。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        "看来是和这家店无缘啊。\x02",
    )

    CloseMessageWindow()

    label("loc_5590")

    TalkEnd(0xFE)
    Return()

    # Function_14_5490 end

    def Function_15_5594(): pass

    label("Function_15_5594")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5783")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56FB")

    #C0333
    ChrTalk(
        0xFE,
        (
            "温蔡尔他们去\x01",
            "贝尔加德门那边进行调查了。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "根据目击情报，\x01",
            "那边好像有黑手党呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x101,
        (
            "#0005F黑手党竟然跑到警备队的驻扎地……\x01",
            "又想做些什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        (
            "至今为止，已经有过\x01",
            "很多目击情报了。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "有不少小道消息都说，好像和\x01",
            "警备队的司令有什么牵扯呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x104,
        (
            "#0301F大概又是行贿受贿之类的事情吧。\x02\x03",

            "#0306F真是的，那个司令真是不知悔改……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5783")

    label("loc_56FB")


    #C0339
    ChrTalk(
        0xFE,
        (
            "呼，贝尔加德门那边的调查虽然\x01",
            "不是什么大不了的事情，不过……\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "刚刚发生过那种袭击事件，谨慎起见，\x01",
            "还是应该把事情的真相搞清楚啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5783")

    TalkEnd(0xFE)
    Return()

    # Function_15_5594 end

    def Function_16_5787(): pass

    label("Function_16_5787")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    LoadChrToIndex("chr/ch02200.itc", 0x1E)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    OP_68(2670, 1200, 7100, 0)
    MoveCamera(63, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, -270, 0, 1360, 45)
    SetChrPos(0x102, 860, 0, 1510, 0)
    SetChrPos(0x103, -810, 0, 500, 45)
    SetChrPos(0x104, 1130, 0, 760, 0)
    SetChrPos(0xD, 2330, 0, 6050, 0)
    SetChrPos(0x8, 2920, 0, 7720, 180)
    SetChrPos(0x9, 4380, -1920, 14500, 270)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetCameraDistance(17000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0341
    ChrTalk(
        0xD,
        (
            "#3104F……我可是很亲切的\x01",
            "和你说这些话哦。\x02\x03",

            "#3100F亚修莉，难听的话我就不说了，\x01",
            "你快点加入鲁巴彻吧。\x02\x03",

            "你做的这些买卖，\x01",
            "和我们存在着一些微妙的冲突呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x8,
        (
            "关于这个问题，我应该已经\x01",
            "拒绝过你很多次了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xD,
        (
            "#3104F……真是不识时务啊。\x02\x03",

            "#3101F我是看得起你，所以才一直忍让，\x01",
            "否则的话，想击溃你可是易如反掌啊。\x01",
            "你可不要搞错自己的立场……！\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x8,
        (
            "哈哈……有意思，\x01",
            "那你就试试看啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x8,
        (
            "我的营业范围可是从克洛斯贝尔\x01",
            "一直延伸到大陆东部呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x8,
        (
            "怎么会输给你们这种只局限在\x01",
            "一个自治州之内的小小黑手党。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x8,
        (
            "听明白的话，就给我乖乖坐到一边去，\x01",
            "副头目先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xD,
        (
            "#3107F……你让谁坐到一边啊！\x01",
            "竟敢如此得意忘形！！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3790, 1200, 8640, 3000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    OP_95(0x9, 9740, 0, 14440, 2000, 0x0)
    OP_95(0x9, 9740, 0, 12440, 2000, 0x0)
    TurnDirection(0x9, 0xD, 500)

    #C0349
    ChrTalk(
        0x9,
        "喂，客人，你太吵啦，\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x9,
        "说话小声点！\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xD,
        (
            "#3103F……嘁………\x01",
            "你和这个小鬼头\x01",
            "都是一点没变啊。\x02\x03",

            "#3100F算了，好好考虑一下吧。\x01",
            "如果你还打算在\x01",
            "克洛斯贝尔继续开店的话。\x02",
        )
    )

    CloseMessageWindow()
    Fade(300)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    OP_93(0x8, 0xE1, 0x0)
    OP_68(1500, 500, 4580, 0)
    OP_68(40, 1200, 2580, 2000)
    MoveCamera(41, 17, 0, 0)
    SetCameraDistance(17000, 0)
    OP_95(0xD, 730, 20, 3170, 2000, 0x0)

    #C0352
    ChrTalk(
        0xD,
        "#3101F……别挡道，一边去。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_5CD3():
        OP_96(0x101, 0xFFFFFD6C, 0x0, 0x6E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5CD3)

    def lambda_5CED():
        OP_96(0x102, 0x532, 0x0, 0x6E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5CED)

    def lambda_5D07():
        OP_96(0x103, 0xFFFFF9E8, 0x0, 0x460, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5D07)
    OP_95(0xD, -110, 0, 70, 2000, 0x0)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)

    def lambda_5D3E():
        TurnDirection(0x101, 0xD, 350)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D3E)

    def lambda_5D4B():
        TurnDirection(0x102, 0xD, 350)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D4B)

    def lambda_5D58():
        TurnDirection(0x103, 0xD, 350)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5D58)

    def lambda_5D65():
        TurnDirection(0x104, 0xD, 350)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5D65)

    def lambda_5D72():
        OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5D72)
    OP_95(0xD, -320, 0, -2350, 2000, 0x0)

    #C0353
    ChrTalk(
        0x104,
        (
            "#0301F加尔西亚·罗西……\x01",
            "还会来这种地方吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x103,
        "#0200F看起来，好像发生了争执呢……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    Sleep(1000)
    OP_D5(0x1E)
    OP_68(130, 1200, 1760, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, 130, 0, 1760, 45)
    SetChrPos(0x1, 130, 0, 1760, 45)
    SetChrPos(0x2, 130, 0, 1760, 45)
    SetChrPos(0x3, 130, 0, 1760, 45)
    SetChrPos(0x9, 5670, 30, 8650, 225)
    SetScenarioFlags(0xB5, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_16_5787 end

    def Function_17_5EA5(): pass

    label("Function_17_5EA5")

    EventBegin(0x1)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F18")

    #C0355
    ChrTalk(
        0x9,
        (
            "喔？\x01",
            "……客人，请稍等。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x9,
        (
            "那边是地下仓库，\x01",
            "不能进去啊～\x01",
            "想买东西的话，就来这边！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5F7E")

    label("loc_5F18")


    #C0357
    ChrTalk(
        0x9,
        (
            "喂喂，客人！\x01",
            "你难道没听到我说的话吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x9,
        (
            "地下仓库是不能随便进的！！\x01",
            "想买东西的话，就来这边！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F7E")

    Sleep(50)
    SetChrPos(0x0, 9940, 0, 11910, 180)
    OP_4C(0x9, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_17_5EA5 end

    SaveToFile()

Try(main)
