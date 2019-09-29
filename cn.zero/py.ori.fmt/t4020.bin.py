from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t4020.bin",                # FileName
        "t4020",                    # MapName
        "t4020",                    # Location
        0x005D,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 260000, 0, 0, 0, 0, 1, 93, 0, 2, 0, 3],
    )

    BuildStringList((
        "t4020",                  # 0
        "昆特老人",               # 1
    ))

    AddCharChip((
        "chr/ch20000.itc",                   # 00
    ))

    DeclNpc(260260,  0,       250,     0,    257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)

    ScpFunction((
        "Function_0_E8",           # 00, 0
        "Function_1_1A0",          # 01, 1
        "Function_2_1CB",          # 02, 2
        "Function_3_31C",          # 03, 3
        "Function_4_32F",          # 04, 4
        "Function_5_C1A",          # 05, 5
        "Function_6_EC3",          # 06, 6
        "Function_7_F99",          # 07, 7
        "Function_8_176E",         # 08, 8
        "Function_9_1CED",         # 09, 9
        "Function_10_1F11",        # 0A, 10
        "Function_11_1F44",        # 0B, 11
        "Function_12_1F74",        # 0C, 12
    ))


    def Function_0_E8(): pass

    label("Function_0_E8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_128"),
        (1, "loc_134"),
        (2, "loc_140"),
        (3, "loc_14C"),
        (4, "loc_158"),
        (5, "loc_164"),
        (6, "loc_170"),
        (SWITCH_DEFAULT, "loc_17C"),
    )


    label("loc_128")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_134")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_140")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_14C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_158")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_164")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_170")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_17C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_188")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_19F")

    Return()

    # Function_0_E8 end

    def Function_1_1A0(): pass

    label("Function_1_1A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CA")
    OP_94(0xFE, 0x3F516, 0xFFFFFA38, 0x3FD0E, 0x8B6, 0x3E8)
    Sleep(600)
    Jump("Function_1_1A0")

    label("loc_1CA")

    Return()

    # Function_1_1A0 end

    def Function_2_1CB(): pass

    label("Function_2_1CB")

    BeginChrThread(0x8, 0, 0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E9")
    Event(0, 9)

    label("loc_1E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_209")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_204")
    SetChrFlags(0x8, 0x80)

    label("loc_204")

    Jump("loc_31B")

    label("loc_209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_242")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23D")
    SetChrPos(0x8, 260000, 0, 2000, 270)
    BeginChrThread(0x8, 0, 0, 0)

    label("loc_23D")

    Jump("loc_31B")

    label("loc_242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_27B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_276")
    SetChrPos(0x8, 260000, 0, 2000, 270)
    BeginChrThread(0x8, 0, 0, 0)

    label("loc_276")

    Jump("loc_31B")

    label("loc_27B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_28E")
    SetChrFlags(0x8, 0x80)
    Jump("loc_31B")

    label("loc_28E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2A1")
    SetChrFlags(0x8, 0x80)
    Jump("loc_31B")

    label("loc_2A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2B4")
    SetChrFlags(0x8, 0x80)
    Jump("loc_31B")

    label("loc_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2C2")
    Jump("loc_31B")

    label("loc_2C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2D5")
    SetChrFlags(0x8, 0x80)
    Jump("loc_31B")

    label("loc_2D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E3")
    Jump("loc_31B")

    label("loc_2E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2F1")
    Jump("loc_31B")

    label("loc_2F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_304")
    SetChrFlags(0x8, 0x80)
    Jump("loc_31B")

    label("loc_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_312")
    Jump("loc_31B")

    label("loc_312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_31B")

    label("loc_31B")

    Return()

    # Function_2_1CB end

    def Function_3_31C(): pass

    label("Function_3_31C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_32E")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_32E")

    Return()

    # Function_3_31C end

    def Function_4_32F(): pass

    label("Function_4_32F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B6")
    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        (
            "多亏你们，\x01",
            "我才能给重要的朋友们扫墓，\x01",
            "真是非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "如果以后还有什么事的话，\x01",
            "我就再联系你们吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_3B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E4")
    Call(0, 8)
    Return()

    label("loc_3E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C4")
    TalkBegin(0xFE)

    #C0003
    ChrTalk(
        0xFE,
        (
            "三番五次地前来确认委托\x01",
            "是不够成熟的表现，真让人不敢恭维啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "已经把花的生长场所\x01",
            "记录在手册上了吧？\x01",
            "自己在手册里确认一下就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "收集到三种花之后，\x01",
            "就带来交给我吧。\x01",
            "拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_4C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DD")
    Call(0, 5)
    Return()

    label("loc_4DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6C2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_65C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C1")

    #C0006
    ChrTalk(
        0xFE,
        (
            "在这样的黄昏，\x01",
            "会让人回想起盖伊呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "罗伊德，如果有朝一日，\x01",
            "你能够独当一面了……\x01",
            "到那个时候，就来和我一起喝酒吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "我会请你喝盖伊\x01",
            "当年最喜欢的酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        "#0004F嗯，我很期待。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEA, 0)
    Jump("loc_657")

    label("loc_5C1")


    #C0010
    ChrTalk(
        0xFE,
        (
            "以前，盖伊在休息的时候，\x01",
            "经常会带酒过来，\x01",
            "在这里和我喝到天亮。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "罗伊德，如果有朝一日，\x01",
            "你能够独当一面了……\x01",
            "到那个时候，就来和我一起喝酒吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_657")

    Jump("loc_6BD")

    label("loc_65C")


    #C0012
    ChrTalk(
        0xFE,
        (
            "在这样的黄昏，\x01",
            "真让人怀念那家伙啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "……哈哈哈，\x01",
            "好像说了些没意义的话呢。\x01",
            "忘掉它吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BD")

    Jump("loc_C16")

    label("loc_6C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_73D")

    #C0014
    ChrTalk(
        0xFE,
        "好了……今天的工作也要开始了。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "对于很久以前就失去了家人的我来说，\x01",
            "这份守墓的工作就是生活的全部了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C16")

    label("loc_73D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7B4")

    #C0016
    ChrTalk(
        0xFE,
        (
            "虽然这个国家的人大多都不会诉之于口，\x01",
            "但很多人的心里都残留有巨大的伤痕。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "……你要将此谨记于心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C16")

    label("loc_7B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7C2")
    Jump("loc_C16")

    label("loc_7C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_7D0")
    Jump("loc_C16")

    label("loc_7D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7DE")
    Jump("loc_C16")

    label("loc_7DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_86C")

    #C0018
    ChrTalk(
        0xFE,
        (
            "刚才上街去买东西，\x01",
            "看到港湾区已经人山人海了。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "大概都是想去米修拉姆疗养地\x01",
            "游玩的人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "……我要是再年轻点的话……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C16")

    label("loc_86C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_87A")
    Jump("loc_C16")

    label("loc_87A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8FB")

    #C0021
    ChrTalk(
        0xFE,
        (
            "虽然试着对来扫墓的夫人说了\x01",
            "『至少在纪念庆典期间好好享受一下吧』\x01",
            "这种话……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "……但是不是\x01",
            "有些多事了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C16")

    label("loc_8FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B7")

    #C0023
    ChrTalk(
        0xFE,
        (
            "昨天的弥撒\x01",
            "比想象中的要热闹。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "大部分来做礼拜的人，\x01",
            "在弥撒结束之后\x01",
            "都会到墓地祈祷。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "创立七十年……\x01",
            "无论对谁来说，今年果然\x01",
            "也都是个很特别的年份吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9FB")

    label("loc_9B7")


    #C0026
    ChrTalk(
        0xFE,
        (
            "创立七十年……\x01",
            "无论对谁来说，今年果然\x01",
            "也都是个很特别的年份吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FB")

    Jump("loc_C16")

    label("loc_A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_A0E")
    Jump("loc_C16")

    label("loc_A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_B07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA3")

    #C0027
    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "下个月就是创立纪念庆典了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        "……时间过得真是快呢。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "大概是因为在这种地方生活，\x01",
            "才会有这种感觉吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B02")

    label("loc_AA3")


    #C0030
    ChrTalk(
        0xFE,
        "下个月就是创立纪念庆典了啊……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "去年的纪念庆典还历历在目，\x01",
            "仿佛就像是发生在昨天一般。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B02")

    Jump("loc_C16")

    label("loc_B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_C16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC2")

    #C0032
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔自治州位于\x01",
            "帝国与共和国的夹缝之间，\x01",
            "曾经被卷入过很多场战争……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "很多生命也因此被时代的洪流所吞没，\x01",
            "就此消亡。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "请为他们\x01",
            "献上一份祈祷吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C16")

    label("loc_BC2")


    #C0035
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市的发展\x01",
            "是以许多生命为代价换来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "请为他们\x01",
            "献上一份祈祷吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C16")

    TalkEnd(0xFE)
    Return()

    # Function_4_32F end

    def Function_5_C1A(): pass

    label("Function_5_C1A")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_68(259100, 1700, -800, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33530, 0)
    SetChrPos(0x101, 259000, 0, -300, 0)
    SetChrPos(0x102, 260200, 0, -300, 0)
    SetChrPos(0x103, 259000, 0, -1500, 0)
    SetChrPos(0x104, 260200, 0, -1500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CC2")
    SetChrPos(0x10A, 257760, 0, -580, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_CC2")

    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF9")

    #C0037
    ChrTalk(
        0x101,
        (
            "#12P#0000F不好意思，\x01",
            "请问您是昆特先生吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0038
    ChrTalk(
        0x8,
        "#5P……你们是警察吗？\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#12P#0000F啊，是的。\x01",
            "我们是特别任务支援科，\x01",
            "接到支援请求而来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        "#5P……嗯。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "#5P有件任务想交给你们，\x01",
            "请替我收集三种\x01",
            "用来献祭的花。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        "#5P可以尽快接受我的委托吗？\x02",
    )

    CloseMessageWindow()
    OP_29(0x2E, 0x1, 0x0)
    Jump("loc_E75")

    label("loc_DF9")


    #C0043
    ChrTalk(
        0x8,
        (
            "#5P嗯，其它的事情\x01",
            "都解决了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "#5P有件任务想交给你们，\x01",
            "请替我收集三种\x01",
            "用来献祭的花。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        "#5P可以接受我的委托吗？\x02",
    )

    CloseMessageWindow()

    label("loc_E75")

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8A")
    Call(0, 7)

    label("loc_E8A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA4")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_EA4")

    SetChrPos(0x0, 259600, 0, -300, 0)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_5_C1A end

    def Function_6_EC3(): pass

    label("Function_6_EC3")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F98")

    #C0046
    ChrTalk(
        0x101,
        (
            "#12P#0006F十分抱歉……\x01",
            "现在还有其它事需要处理，\x01",
            "不能立刻……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "#5P唔，这样啊，\x01",
            "那就没办法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "#5P等你们有空接受我的委托时\x01",
            "再过来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F98")

    Return()

    # Function_6_EC3 end

    def Function_7_F99(): pass

    label("Function_7_F99")


    #C0049
    ChrTalk(
        0x101,
        (
            "#12P#0000F明白了，\x01",
            "我们可以接受。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        "#5P嗯，很好。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#5P那就别浪费时间了，\x01",
            "我现在就告诉你们\x01",
            "要收集哪三种花吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        "#5P准备好做笔记了吗？\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        "#12P#0005F是，准备好了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    #C0054
    ChrTalk(
        0x101,
        "#12P#0000F缇欧，拜托你了。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        "#12P#0203F了解。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    #C0056
    ChrTalk(
        0x8,
        (
            "#5P第一种叫做『蕾瓦斯之花』，\x01",
            "盛开在西克洛斯贝尔街道的\x01",
            "警察学校附近。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "#5P第二种叫做『利奎姆之花』，\x01",
            "可以在克洛斯贝尔市西街的\x01",
            "塔利兹商店买到。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "#5P最后一种叫做『菲奈尔之花』，\x01",
            "进入东克洛斯贝尔街道后，\x01",
            "就能在附近的瞭望台旁找到。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "#5P不过附近可能也会开有类似的花。\x01",
            "注意不要采错了。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "#5P……全部都收集完之后，\x01",
            "就带来交给我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        (
            "#12P#0203F……收集地点已经记下了。\x02\x03",

            "#0200F话说回来……\x01",
            "您为什么要收集这三种花呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    #C0062
    ChrTalk(
        0x102,
        (
            "#0100F在克洛斯贝尔自治州，\x01",
            "黄、蓝、白这三种颜色\x01",
            "代表『安魂』。\x02\x03",

            "在举行葬礼的时候，要用这三种颜色的花\x01",
            "做成花束，献给死者，\x01",
            "这是克洛斯贝尔的传统。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x104,
        "#12P#0305F哎，这就是所谓的花语吗？\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x103,
        (
            "#12P#0203F我想这两者之间应该\x01",
            "有些微妙的区别……\x02\x03",

            "#0200F硬要说的话，\x01",
            "这应该算是克洛斯贝尔的\x01",
            "地方习俗。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#12P#0003F（说起来，在大哥的葬礼上，\x01",
            "　好像也有人献上了三色花束……）\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0067
    ChrTalk(
        0x101,
        "#12P#0005F那、那个……\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        "#12P#0305F怎么了，突然就不说话了。\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "#5P唉，真是的，\x01",
            "现在这些见识狭隘的年轻人\x01",
            "真是令人悲哀啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "#5P竟连这种常识都不知道，\x01",
            "真为你们的未来感到担忧。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        "#12P#0005F那、那个……\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x104,
        (
            "#12P#0300F哈哈，不好意思，\x01",
            "我并不是克洛斯贝尔\x01",
            "出身的。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        "#5P嗯，算啦。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "#5P我已经把事情交代完了，\x01",
            "你们就尽快处理吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        "#12P#0005F知、知道了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1714")

    #C0076
    ChrTalk(
        0x10A,
        "#6P#0603F………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_15F1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15F1)
    Sleep(50)

    def lambda_1601():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1601)
    Sleep(50)

    def lambda_1611():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1611)
    Sleep(50)

    def lambda_1621():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1621)

    #C0077
    ChrTalk(
        0x101,
        (
            "#11P#0012F那个……\x01",
            "情况就是这么回事……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x10A,
        (
            "#6P#0600F……哼，\x01",
            "什么叫『情况就是这么回事』啊。\x02\x03",

            "#0606F算了，话都听到这里了，\x01",
            "也总不能拒绝委托。\x02\x03",

            "#0600F既然要做就要做好，完美解决之后\x01",
            "再继续进行调查吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x104,
        "#12P#0309F收到，明白了！\x02",
    )

    CloseMessageWindow()

    label("loc_1714")

    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0080
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【收集慰灵之花】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x2E, 0x1, 0x1)
    Return()

    # Function_7_F99 end

    def Function_8_176E(): pass

    label("Function_8_176E")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_4B(0x8, 0xFF)
    OP_68(259100, 1700, -800, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33530, 0)
    SetChrPos(0x101, 259000, 0, -300, 0)
    SetChrPos(0x102, 260200, 0, -300, 0)
    SetChrPos(0x103, 259000, 0, -1500, 0)
    SetChrPos(0x104, 260200, 0, -1500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_181F")
    SetChrPos(0x10A, 257760, 0, -580, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_181F")

    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x40)
    FadeToBright(500, 0)
    OP_0D()

    #C0081
    ChrTalk(
        0x101,
        (
            "#12P#0000F昆特先生，\x01",
            "我们回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "#5P嗯，\x01",
            "挺快的嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        "#5P已经把花全部集齐了吗？\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#12P#0000F是的，请您确认一下。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x349),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了。\x02\x03",
            scpstr(SCPSTR_CODE_ITEM, 0x34A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了。\x02\x03",
            scpstr(SCPSTR_CODE_ITEM, 0x34B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x349, 1)
    SubItemNumber(0x34A, 1)
    SubItemNumber(0x34B, 1)

    #C0086
    ChrTalk(
        0x8,
        (
            "#5P……嗯，没错，\x01",
            "三种花全部都集齐了。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "#5P辛苦了，\x01",
            "特别任务支援科的各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#12P#0000F请不必客气，\x01",
            "完成委托是我们的分内之事。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x104,
        (
            "#12P#0306F呼～这委托出乎意料地麻烦呢。\x02\x03",

            "还出现了杂货店没有花卖\x01",
            "这种意外。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x103,
        "#12P#0200F不过，最后总算还是完成了。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        "#0100F老爷爷，可以向您请教一个问题吗？\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        "#5P……什么事？\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x102,
        (
            "#0103F按照最近的风俗习惯来说，\x01",
            "在葬礼之外的场合使用三色花束\x01",
            "来献祭是很少见的。\x02\x03",

            "#0100F而您这次为什么要收集三色花束呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "#5P嗯，这次的确\x01",
            "不是为了葬礼而收集的……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "#5P……机会难得，现在我正好要去献花，\x01",
            "你们也一起来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        "#5P到时再告诉你们我要收集三色花束的理由。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 10)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 11)
    BeginChrThread(0x102, 3, 0, 12)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 11)
    BeginChrThread(0x104, 3, 0, 12)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BC9")
    Sleep(200)

    def lambda_1BC1():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1BC1)

    label("loc_1BC9")

    WaitChrThread(0x8, 3)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0097
    ChrTalk(
        0x103,
        "#6P#0205F……到底是怎么回事呢？\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#5P#0005F不、不知道……\x02\x03",

            "#0003F虽然不是很清楚，\x01",
            "不过，总之还是去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CD2")

    #C0099
    ChrTalk(
        0x10A,
        "#6P#0603F（……难道……）\x02",
    )

    CloseMessageWindow()

    label("loc_1CD2")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2E, 0x1, 0x7)
    NewScene("t4100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_176E end

    def Function_9_1CED(): pass

    label("Function_9_1CED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(259100, 1700, -800, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33530, 0)
    SetChrPos(0x101, 259000, 0, -300, 0)
    SetChrPos(0x102, 260200, 0, -300, 0)
    SetChrPos(0x103, 259000, 0, -1500, 0)
    SetChrPos(0x104, 260200, 0, -1500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D96")
    SetChrPos(0x10A, 257760, 0, -580, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_1D96")

    OP_93(0x8, 0xB4, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x0)
    SetCameraDistance(30720, 3000)
    FadeToBright(500, 0)
    OP_0D()

    #C0100
    ChrTalk(
        0x8,
        (
            "#5P多亏你们，\x01",
            "我才能给重要的朋友们扫墓，\x01",
            "真是非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "#5P如果以后还有什么事的话，\x01",
            "我就再联系你们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#12P#0000F嗯，随时欢迎。\x01",
            "……那我们就先告辞了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0103
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【收集慰灵之花】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -350, 0, 12250, 0)
    OP_29(0x2E, 0x4, 0x10)
    SetScenarioFlags(0x0, 1)
    Sleep(500)
    SetChrPos(0x0, 259600, 0, -300, 0)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F0E")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1F0E")

    EventEnd(0x5)
    Return()

    # Function_9_1CED end

    def Function_10_1F11(): pass

    label("Function_10_1F11")


    def lambda_1F16():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1F16)
    Sleep(2500)

    def lambda_1F33():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1F33)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_10_1F11 end

    def Function_11_1F44(): pass

    label("Function_11_1F44")


    def lambda_1F49():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1F49)
    WaitChrThread(0xFE, 1)

    def lambda_1F67():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1F67)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_11_1F44 end

    def Function_12_1F74(): pass

    label("Function_12_1F74")


    def lambda_1F79():
        OP_98(0xFE, 0x12C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1F79)
    WaitChrThread(0xFE, 1)

    def lambda_1F97():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1F97)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_1F74 end

    SaveToFile()

Try(main)
