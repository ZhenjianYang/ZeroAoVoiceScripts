from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0310.bin",                # FileName
        "c0310",                    # MapName
        "c0310",                    # Location
        0x002B,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 43, 0, 4, 0, 5],
    )

    BuildStringList((
        "c0310",                  # 0
        "海尔玛",                 # 1
        "乔安娜",                 # 2
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch25700.itc",                   # 01
    ))

    DeclNpc(0,       4059,    7760,    180,  257,  0x0, 0,   0,   0,   0,   2,   0,   6,   255,  0)
    DeclNpc(-45349,  59,      3900,    360,  257,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)

    DeclActor(-40820,  0,       40910,   1500,    -40820,  1500,    40910,   0x007C, 0,  9,  0x0000)

    ChipFrameInfo(296, 0)                                        # 0

    ScpFunction((
        "Function_0_128",          # 00, 0
        "Function_1_1E0",          # 01, 1
        "Function_2_20B",          # 02, 2
        "Function_3_236",          # 03, 3
        "Function_4_261",          # 04, 4
        "Function_5_392",          # 05, 5
        "Function_6_43B",          # 06, 6
        "Function_7_14A9",         # 07, 7
        "Function_8_16A7",         # 08, 8
        "Function_9_2859",         # 09, 9
        "Function_10_33A5",        # 0A, 10
        "Function_11_3990",        # 0B, 11
    ))


    def Function_0_128(): pass

    label("Function_0_128")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_168"),
        (1, "loc_174"),
        (2, "loc_180"),
        (3, "loc_18C"),
        (4, "loc_198"),
        (5, "loc_1A4"),
        (6, "loc_1B0"),
        (SWITCH_DEFAULT, "loc_1BC"),
    )


    label("loc_168")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_174")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_180")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_18C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_198")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_1A4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_1B0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_1BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_1C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_1DF")

    Return()

    # Function_0_128 end

    def Function_1_1E0(): pass

    label("Function_1_1E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_20A")
    OP_94(0xFE, 0xFFFFF63C, 0x0, 0x9C4, 0x73A, 0x3E8)
    Sleep(300)
    Jump("Function_1_1E0")

    label("loc_20A")

    Return()

    # Function_1_1E0 end

    def Function_2_20B(): pass

    label("Function_2_20B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_235")
    OP_94(0xFE, 0xFFFFF8B2, 0x1A36, 0x744, 0x26DE, 0x3E8)
    Sleep(300)
    Jump("Function_2_20B")

    label("loc_235")

    Return()

    # Function_2_20B end

    def Function_3_236(): pass

    label("Function_3_236")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_260")
    OP_94(0xFE, 0xA00A, 0xA05A, 0xB31A, 0xB220, 0x3E8)
    Sleep(300)
    Jump("Function_3_236")

    label("loc_260")

    Return()

    # Function_3_236 end

    def Function_4_261(): pass

    label("Function_4_261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_26F")
    Jump("loc_391")

    label("loc_26F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2A5")
    SetChrPos(0x8, 810, 0, 500, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, -810, 0, 500, 90)
    Jump("loc_391")

    label("loc_2A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2B3")
    Jump("loc_391")

    label("loc_2B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2D2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2CD")
    SetChrFlags(0x9, 0x80)

    label("loc_2CD")

    Jump("loc_391")

    label("loc_2D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2E0")
    Jump("loc_391")

    label("loc_2E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2EE")
    Jump("loc_391")

    label("loc_2EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_301")
    SetChrFlags(0x9, 0x80)
    Jump("loc_391")

    label("loc_301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_30F")
    Jump("loc_391")

    label("loc_30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_31D")
    Jump("loc_391")

    label("loc_31D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_32B")
    Jump("loc_391")

    label("loc_32B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_339")
    Jump("loc_391")

    label("loc_339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_347")
    Jump("loc_391")

    label("loc_347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_355")
    Jump("loc_391")

    label("loc_355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_379")
    SetChrPos(0x9, -42190, 0, 48970, 0)
    SetChrFlags(0x9, 0x10)
    Jump("loc_391")

    label("loc_379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_391")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_391")
    SetChrFlags(0x8, 0x10)

    label("loc_391")

    Return()

    # Function_4_261 end

    def Function_5_392(): pass

    label("Function_5_392")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BA")
    OP_66(0x0, 0x1)

    label("loc_3BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FF")
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model05_light", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_3FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43A")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model05_light", 0x0, 0x1)

    label("loc_43A")

    Return()

    # Function_5_392 end

    def Function_6_43B(): pass

    label("Function_6_43B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_57F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FF")

    #C0001
    ChrTalk(
        0xFE,
        (
            "老爷好像正在兰花塔内\x01",
            "指挥今后的行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "总统已经被拘捕，\x01",
            "如今能引领克洛斯贝尔的\x01",
            "只有老爷一个人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "虽然这肯定是很重的负担……\x01",
            "但还是希望老爷能好好加油。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_57A")

    label("loc_4FF")


    #C0004
    ChrTalk(
        0xFE,
        (
            "总统已经被拘捕，\x01",
            "如今能引领克洛斯贝尔的\x01",
            "只有老爷一个人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "虽然这肯定是很重的负担……\x01",
            "但还是希望老爷能好好加油。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57A")

    Jump("loc_14A5")

    label("loc_57F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_610")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59A")
    Call(0, 7)
    Jump("loc_60B")

    label("loc_59A")


    #C0006
    ChrTalk(
        0xFE,
        (
            "自从老爷和大小姐\x01",
            "被软禁在米修拉姆之后，\x01",
            "我就一直担心得坐立不安……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "能再次见到您，\x01",
            "我也总算可以安心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60B")

    Jump("loc_14A5")

    label("loc_610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_788")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_721")
    TurnDirection(0xFE, 0x102, 0)

    #C0008
    ChrTalk(
        0xFE,
        (
            "……大小姐……\x01",
            "老爷有和您联络\x01",
            "过吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        "#00103F不，我这边也完全没消息……\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "是吗……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "唔，总之……\x01",
            "如果我了解到什么情况，\x01",
            "一定会和您联络的。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "大小姐与各位就\x01",
            "专心处理\x01",
            "自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x102,
        (
            "#00100F嗯，拜托你了，\x01",
            "海尔玛先生。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 2)
    Jump("loc_783")

    label("loc_721")


    #C0014
    ChrTalk(
        0xFE,
        (
            "如果我了解到\x01",
            "有关老爷的情况，\x01",
            "一定会和您联络的。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "大小姐与各位就\x01",
            "专心处理\x01",
            "自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_783")

    Jump("loc_14A5")

    label("loc_788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_864")

    #C0016
    ChrTalk(
        0xFE,
        (
            "……之前的那起袭击事件\x01",
            "真是一场惨痛的经历。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "虽然重建工作\x01",
            "总算是取得了一些进展……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "但现在还是有不少人\x01",
            "无法从恐惧中解脱。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "为了防止那种事件再次发生，\x01",
            "希望老爷和市长\x01",
            "都要加油。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8CD")

    label("loc_864")


    #C0020
    ChrTalk(
        0xFE,
        (
            "不久前的那起袭击事件\x01",
            "真是一场惨痛的经历。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "为了防止那种事件再次发生，\x01",
            "希望老爷和市长\x01",
            "都要加油。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CD")

    Jump("loc_14A5")

    label("loc_8D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A4")

    #C0022
    ChrTalk(
        0xFE,
        (
            "老爷正在和市长\x01",
            "一起研究玛因兹地区\x01",
            "遭到占领事件的对策。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "据说，在武装集团面前，\x01",
            "连警备队都束手无策，\x01",
            "而且这样的状况还在持续……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "……真让人担心啊。\x01",
            "但愿能尽早将事件解决。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A06")

    label("loc_9A4")


    #C0025
    ChrTalk(
        0xFE,
        (
            "据说武装集团十分强悍，\x01",
            "连警备队都束手无策……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "……真让人担心啊。\x01",
            "但愿能尽早将事件解决。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A06")

    Jump("loc_14A5")

    label("loc_A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABE")

    #C0027
    ChrTalk(
        0xFE,
        (
            "昨天那起脱轨事故……\x01",
            "呼，真是让人震惊。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "大家现在都议论纷纷，\x01",
            "说事故发生的原因是落石或\x01",
            "巨大怪物的袭击……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "唔……真正的原因\x01",
            "究竟是什么呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B1E")

    label("loc_ABE")


    #C0030
    ChrTalk(
        0xFE,
        "昨天那起脱轨事故真是让人震惊。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "市内流传着各种各样的传言……\x01",
            "真正的原因\x01",
            "究竟是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1E")

    Jump("loc_14A5")

    label("loc_B23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_B6E")

    #C0032
    ChrTalk(
        0xFE,
        (
            "好像有警笛声\x01",
            "从西街那边传来……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "大概是我听错了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14A5")

    label("loc_B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C0E")

    #C0034
    ChrTalk(
        0xFE,
        (
            "独立的提案给社会各界\x01",
            "都造成了一定影响，\x01",
            "老爷正在努力制订应对措施。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "他今天也要和迪塔市长\x01",
            "一起在兰花塔开会……\x01",
            "希望他能注意自己的身体啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A5")

    label("loc_C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDE")

    #C0036
    ChrTalk(
        0xFE,
        (
            "调查独立意向的居民投票活动\x01",
            "已经渐渐临近了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "关于这个问题，\x01",
            "老爷认为应该采取\x01",
            "慎重的态度来对待……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "而克洛斯贝尔的居民们\x01",
            "最终又会做出怎样的选择呢……\x01",
            "我对此也很有兴趣。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D55")

    label("loc_CDE")


    #C0039
    ChrTalk(
        0xFE,
        (
            "调查独立意向的居民投票活动\x01",
            "已经渐渐临近了。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的居民们\x01",
            "最终会做出怎样的选择呢……\x01",
            "我对此也很有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D55")

    Jump("loc_14A5")

    label("loc_D5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_DB7")

    #C0041
    ChrTalk(
        0xFE,
        (
            "老爷今天也\x01",
            "一大早就前往\x01",
            "兰花塔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "希望今天的正式会议\x01",
            "能顺利结束……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A5")

    label("loc_DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_ED4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6E")

    #C0043
    ChrTalk(
        0xFE,
        (
            "老爷最近很忙，\x01",
            "经常连家都不回，\x01",
            "在市政厅过夜休息……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "刚才接到了联络，\x01",
            "老爷今天总算\x01",
            "要回家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "希望老爷养精蓄锐，\x01",
            "为明天的正式会议\x01",
            "做好准备。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_ECF")

    label("loc_E6E")


    #C0046
    ChrTalk(
        0xFE,
        (
            "今晚为老爷\x01",
            "准备了营养价值\x01",
            "很高的料理。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "希望老爷能养足精神，\x01",
            "为明天的正式会议做好准备。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ECF")

    Jump("loc_14A5")

    label("loc_ED4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_102A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA8")

    #C0048
    ChrTalk(
        0xFE,
        (
            "在哈尔特曼担任议长的时期，\x01",
            "老爷光是为了制衡帝国派与共和国派\x01",
            "的议员，就耗尽了心神。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "但最近和新市长联手协力，\x01",
            "总算能够与他们形成\x01",
            "势均力敌之势……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "为此，我也感到\x01",
            "十分高兴。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1025")

    label("loc_FA8")


    #C0051
    ChrTalk(
        0xFE,
        (
            "迪塔先生能成为市长，\x01",
            "也让我感到十分欣喜。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "在从明天开始的正式会议中……\x01",
            "希望老爷和市长都能\x01",
            "充分展现自己的政治手腕。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1025")

    Jump("loc_14A5")

    label("loc_102A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_10AE")

    #C0053
    ChrTalk(
        0xFE,
        (
            "为了明日开始的通商会议，\x01",
            "老爷和迪塔市长\x01",
            "都在精心进行准备工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "老爷最近几乎\x01",
            "都不回家了……\x01",
            "真是让人担心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A5")

    label("loc_10AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1242")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AF")

    #C0055
    ChrTalk(
        0xFE,
        (
            "不久前，有几个人搬到\x01",
            "隔壁的房子居住了……\x01",
            "他们很快就造成了很多问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "比如开着导力车在市内横冲直撞，\x01",
            "半夜播放音量超大的音乐……\x01",
            "这种行为实在是让人看不下去。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "但就算提出抗议，\x01",
            "他们也充耳不闻……\x01",
            "到底该怎么办才好呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_123D")

    label("loc_11AF")


    #C0058
    ChrTalk(
        0xFE,
        (
            "不久前，有几个人搬到\x01",
            "隔壁的房子居住了……\x01",
            "他们的行为实在是让人难以容忍。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "但就算提出抗议，\x01",
            "他们也充耳不闻……\x01",
            "到底该怎么办才好呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_123D")

    Jump("loc_14A5")

    label("loc_1242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_14A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1440")
    TurnDirection(0xFE, 0x102, 0)

    #C0060
    ChrTalk(
        0xFE,
        (
            "这不是艾莉大小姐吗！\x01",
            "欢迎您回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        "#00100F我回来了，海尔玛先生。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x105,
        (
            "#10300F原来如此，\x01",
            "这里就是艾莉的家啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x109,
        "#10102F真是一座大房子呢。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#00004F嗯……\x01",
            "毕竟是麦克道尔议长\x01",
            "的宅邸嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x102,
        "#00109F呵呵，请大家不要拘束。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "是啊，各位都是\x01",
            "大小姐的同事，\x01",
            "请放松些，不必拘谨。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "特别任务支援科\x01",
            "总算恢复工作了，\x01",
            "接下来大概会非常繁忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "今后也请各位\x01",
            "继续关照艾莉大小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        "#00000F嗯，放心吧。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        (
            "#00102F呵呵，谢谢了，海尔玛先生。\x01",
            "我会继续努力的。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x134, 1)
    Jump("loc_14A5")

    label("loc_1440")


    #C0071
    ChrTalk(
        0xFE,
        (
            "特别任务支援科\x01",
            "总算恢复工作了，\x01",
            "接下来大概会非常繁忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "今后也请各位\x01",
            "继续关照艾莉大小姐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A5")

    TalkEnd(0xFE)
    Return()

    # Function_6_43B end

    def Function_7_14A9(): pass

    label("Function_7_14A9")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    #C0073
    ChrTalk(
        0x8,
        "哦哦，各位……！\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "大、大小姐…………\x01",
            "……艾莉大小姐……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        (
            "#00100F我回来啦，海尔玛先生，乔安娜。\x01",
            "……让你们担心了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        "…………（哽咽）\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "自从老爷发表独立无效宣言之后，\x01",
            "我一直都非常担心，\x01",
            "不知你们是否平安无事……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "能再次见到您，\x01",
            "我也总算可以安心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，谢谢。\x02\x03",

            "#00103F……不过，我们现在无论如何\x01",
            "也必须要去某个地方。\x02\x03",

            "#00101F请二位暂时留在这里等我们，\x01",
            "可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        "嗯，当然。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "艾莉大小姐，各位……\x01",
            "请你们一定要小心。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0x9, 0x5A, 0x0)
    SetScenarioFlags(0x1CC, 7)
    Return()

    # Function_7_14A9 end

    def Function_8_16A7(): pass

    label("Function_8_16A7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_17FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B4")

    #C0082
    ChrTalk(
        0xFE,
        (
            "艾莉大小姐，\x01",
            "你们要前往那棵\x01",
            "诡异的大树吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x102,
        (
            "#00104F别担心，乔安娜，\x01",
            "我们一定会平安归来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "……嗯。\x01",
            "至今为止，大小姐每次\x01",
            "都平安回到了这里……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "所以我相信您这次也不会有事的。\x01",
            "……请一定要小心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17F8")

    label("loc_17B4")


    #C0087
    ChrTalk(
        0xFE,
        (
            "我相信艾莉大小姐和各位\x01",
            "一定能平安归来。\x01",
            "……请大家一定要小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F8")

    Jump("loc_2855")

    label("loc_17FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1864")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1818")
    Call(0, 7)
    Jump("loc_185F")

    label("loc_1818")


    #C0088
    ChrTalk(
        0xFE,
        "外面好像非常危险……\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "艾莉大小姐，各位……\x01",
            "请你们一定要小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_185F")

    Jump("loc_2855")

    label("loc_1864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1A20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C2")

    #C0090
    ChrTalk(
        0xFE,
        (
            "老爷他……\x01",
            "到底到什么地方\x01",
            "去了呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        "我好担心……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#00003F在刚才的演说现场直播里\x01",
            "也没有见到议长呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x102,
        "#00108F外公……到底在什么地方……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 500)

    #C0094
    ChrTalk(
        0xFE,
        (
            "……啊啊，对不起！\x01",
            "我竟然口无遮拦，\x01",
            "害得大小姐也开始不安了……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x102,
        (
            "#00103F……哪里，我不要紧。\x02\x03",

            "#00100F乔安娜，你也不要\x01",
            "太过担心哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        "明、明白了……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 3)
    Jump("loc_1A1B")

    label("loc_19C2")


    #C0097
    ChrTalk(
        0xFE,
        (
            "……我竟然口无遮拦，\x01",
            "害得大小姐\x01",
            "也开始不安了……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "老爷……\x01",
            "一定会平安无事的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A1B")

    Jump("loc_2855")

    label("loc_1A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B27")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A52")
    Call(0, 10)
    Return()

    label("loc_1A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_END)), "loc_1AC9")

    #C0099
    ChrTalk(
        0xFE,
        (
            "……我还是…………\x01",
            "决定参加\x01",
            "职业女性选秀活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "……活动开始前请通知我吧，\x01",
            "我会立刻赶过去的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B22")

    label("loc_1AC9")


    #C0101
    ChrTalk(
        0xFE,
        (
            "听说今天要在\x01",
            "行政区举办一场\x01",
            "慈善宴会……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "……有没有什么\x01",
            "我能帮上忙的事情呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B22")

    Jump("loc_2855")

    label("loc_1B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1B89")

    #C0103
    ChrTalk(
        0xFE,
        "矿山镇竟然被占领了……\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "……我好害怕……\x01",
            "总觉得接下来\x01",
            "还会发生什么事情……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2855")

    label("loc_1B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1BD4")

    #C0105
    ChrTalk(
        0xFE,
        "最近经常下雨啊……\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "……洗好的衣物都晒不干。\x01",
            "呼……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2855")

    label("loc_1BD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1BE2")
    Jump("loc_2855")

    label("loc_1BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1D6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D10")

    #C0107
    ChrTalk(
        0xFE,
        (
            "老爷最近特别繁忙，\x01",
            "得用心为他准备些有营养的食物……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        "……做什么料理才好呢？\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x102,
        (
            "#00100F这个嘛……\x01",
            "羔羊肉如何呢？\x02\x03",

            "#00104F高蛋白，低热量，\x01",
            "而且应该很合外公的口味。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 500)

    #C0110
    ChrTalk(
        0xFE,
        (
            "……似乎不错呢……\x01",
            "真不愧是艾莉大小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        (
            "#00109F啊、啊哈哈，\x01",
            "这点小事不值得夸奖啦……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D69")

    label("loc_1D10")


    #C0112
    ChrTalk(
        0xFE,
        (
            "我的饭量很小，\x01",
            "一般不吃肉，\x01",
            "不过做给老爷应该不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "一会得去百货店\x01",
            "买食材……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D69")

    Jump("loc_2855")

    label("loc_1D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1EC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E94")

    #C0114
    ChrTalk(
        0xFE,
        (
            "听说在前不久召开的通商会议中，\x01",
            "有恐怖分子发动了袭击……\x01",
            "听到这消息时，我的心脏都快停止跳动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "自那之后，我一直非常担心\x01",
            "艾莉大小姐和老爷……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        (
            "#00103F乔安娜……\x01",
            "你不用那么担心的。\x02\x03",

            "#00100F有支援科的同伴陪着我……\x01",
            "一定不会出什么事的。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        "嗯……是啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EBB")

    label("loc_1E94")


    #C0118
    ChrTalk(
        0xFE,
        (
            "各位……\x01",
            "艾莉大小姐就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EBB")

    Jump("loc_2855")

    label("loc_1EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1F17")

    #C0119
    ChrTalk(
        0xFE,
        (
            "艾莉大小姐……\x01",
            "市里今天好像也维持着戒严状态。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        "请您一定小心……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2855")

    label("loc_1F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_208D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2002")

    #C0121
    ChrTalk(
        0xFE,
        (
            "今天的晚餐\x01",
            "是老爷最喜欢的\x01",
            "苦西红柿料理。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "苦西红柿沙拉、\x01",
            "苦西红柿酱的薏面，\x01",
            "还有１００％浓度的苦西红柿汁……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#00005F（哇……\x01",
            "  好极端的菜单啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x102,
        (
            "#00106F（外公竟然那么喜欢\x01",
            "  苦西红柿……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2088")

    label("loc_2002")


    #C0125
    ChrTalk(
        0xFE,
        (
            "我今天做了老爷最喜欢的\x01",
            "苦西红柿料理。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "听说吃苦西红柿有利于健康，\x01",
            "我也准备忍耐着\x01",
            "试试……\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x102,
        "#00105F可、可不要太勉强哦……\x02",
    )

    CloseMessageWindow()

    label("loc_2088")

    Jump("loc_2855")

    label("loc_208D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_21D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2151")

    #C0128
    ChrTalk(
        0xFE,
        (
            "今天早上，我正好在门口\x01",
            "遇到了住在隔壁的那几个人……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "他们突然就对我发出邀请，\x01",
            "说『一起去兜风吧』。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "我自然是礼貌地回绝了，\x01",
            "总觉得那些人实在是欠缺教养啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21CE")

    label("loc_2151")


    #C0131
    ChrTalk(
        0xFE,
        (
            "今天早上，住在隔壁的\x01",
            "那几个人突然邀请我\x01",
            "和他们一起去兜风。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "我自然是礼貌地回绝了，\x01",
            "总觉得那些人实在是欠缺教养啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21CE")

    Jump("loc_2855")

    label("loc_21D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_224E")

    #C0133
    ChrTalk(
        0xFE,
        (
            "新市政厅大楼\x01",
            "明天就要正式揭幕了……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "就算隔着帷幕，\x01",
            "都能充分感受到它的魄力，\x01",
            "简直让人头昏目眩呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2855")

    label("loc_224E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_238B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2337")

    #C0135
    ChrTalk(
        0xFE,
        "（吱吱……吱吱……）\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x102,
        (
            "#00105F哎，乔安娜，\x01",
            "你在窗户上画东西吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x9, 0x102, 1000)
    Sleep(1000)

    #C0137
    ChrTalk(
        0xFE,
        (
            "……窗、窗户上蒙了一层白雾，\x01",
            "所以我不由自主就……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "失、失礼了，\x01",
            "我这就继续做扫除。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_2386")

    label("loc_2337")


    #C0139
    ChrTalk(
        0xFE,
        (
            "不知为何，只要听到雨声，\x01",
            "我就会分心走神……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        "唉，真是不喜欢下雨天啊。\x02",
    )

    CloseMessageWindow()

    label("loc_2386")

    Jump("loc_2855")

    label("loc_238B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2855")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27DF")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x102, 0)
    Sleep(1000)

    #C0141
    ChrTalk(
        0xFE,
        "啊……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        "欢迎回来，艾莉大小姐。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        (
            "#00100F我回来了，乔安娜，\x01",
            "今天没有什么异常情况吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        "是的……托您的福。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "大小姐外出旅行归来，\x01",
            "我也总算可以安心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x102,
        (
            "#00102F呵呵，乔安娜，你可真是的……\x01",
            "根本不用那么担心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "不，对我来说，大小姐\x01",
            "和老爷就是一切……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x105,
        "#10309F呵呵，真是一位关怀主人的女仆小姐啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0149
    ChrTalk(
        0xFE,
        (
            "……那个，艾莉大小姐，\x01",
            "前几天收到了先生和小姐\x01",
            "寄来的信……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0150
    ChrTalk(
        0x101,
        "#00005F那是……\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x102,
        (
            "#00103F……嗯，是我分别居住在共和国\x01",
            "和帝国的父母。\x02\x03",

            "#00100F他们以前也时常来信，\x01",
            "自从教团那起事件结束之后，\x01",
            "似乎寄得比以前更加频繁了。\x02\x03",

            "#00104F信中内容主要都是表达\x01",
            "对我和外公的关心，\x01",
            "最近都成为我的心灵支柱之一了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x109,
        "#10105F这样啊……\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x105,
        "#10303F（……亲人……吗……）\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        (
            "#00100F乔安娜，我稍后会去看的，\x01",
            "请你帮我仔细保管好哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        "是……谨遵吩咐。\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "那个，听说特别任务支援科\x01",
            "已经恢复工作了……\x01",
            "请您一定要注意身体。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "老爷、先生以及小姐……\x01",
            "大家全都在挂念着大小姐。\x01",
            "我自然也是一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x102,
        (
            "#00109F呵呵，我明白的。\x01",
            "谢谢你，乔安娜。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x134, 2)
    Jump("loc_2855")

    label("loc_27DF")

    TurnDirection(0x9, 0x102, 0)

    #C0159
    ChrTalk(
        0xFE,
        (
            "艾莉大小姐，\x01",
            "请一定要注意保重身体。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "老爷、先生以及小姐……\x01",
            "大家全都在挂念着大小姐。\x01",
            "我自然也是一样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2855")

    TalkEnd(0xFE)
    Return()

    # Function_8_16A7 end

    def Function_9_2859(): pass

    label("Function_9_2859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_END)), "loc_28F6")
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0161
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K要阅读昆西公司的宣传手册吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "阅读\x01",        # 0
            "不阅读\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28E5")
    Call(0, 11)
    TalkEnd(0xFF)
    Jump("loc_28F1")

    label("loc_28E5")

    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_28F1")

    Jump("loc_33A4")

    label("loc_28F6")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-41830, 1500, 40450, 0)
    MoveCamera(52, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(18820, 0)
    SetChrPos(0x101, -43440, 60, 40740, 90)
    SetChrPos(0x102, -41310, 0, 40520, 90)
    SetChrPos(0x103, -42890, 0, 39580, 45)
    SetChrPos(0x104, -42860, 60, 41860, 135)
    SetChrPos(0x109, -42020, 0, 38900, 0)
    SetChrPos(0x105, -41650, 0, 42460, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0162
    ChrTalk(
        0x102,
        "#00105F唔……找到了。\x02",
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)
    Sleep(400)
    OP_93(0x102, 0x10E, 0x1F4)

    #C0163
    ChrTalk(
        0x102,
        (
            "#00100F这就是昆西公司\x01",
            "的宣传手册。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x104,
        (
            "#00305F嘿……\x01",
            "装订得很精美啊。\x02\x03",

            "#00300F看起来并不像是\x01",
            "普通的资料呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x103,
        (
            "#00200F只有大企业才会\x01",
            "在这种细节方面如此讲究。\x02\x03",

            "看来这本手册中的内容\x01",
            "有很高的可信度。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        "#00109F呵呵，那就好。\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        (
            "#00001F好……\x01",
            "我们先来粗略浏览一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 11)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    #C0168
    ChrTalk(
        0x105,
        (
            "#10303F嗯，已经大致看了一遍……\x01",
            "但并没找到什么重要资料呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x109,
        (
            "#10105F有没有发现什么与敏涅斯的话\x01",
            "有矛盾的内容呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x102,
        (
            "#00106F唔～这个……\x01",
            "在这种资料中果然还是\x01",
            "不会有什么收获……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        "#00003F不……我发现矛盾了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2CC4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2CC4)
    Sleep(50)

    def lambda_2CD4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2CD4)
    Sleep(50)

    def lambda_2CE4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2CE4)
    Sleep(50)

    def lambda_2CF4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2CF4)

    #C0172
    ChrTalk(
        0x103,
        "#00205F……真的吗？\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x104,
        (
            "#00309F哈哈，你还是\x01",
            "这么靠得住啊。\x02\x03",

            "#00300F那就说说吧，到底是什么矛盾？\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        (
            "#00004F只要仔细回想一下我们昨天\x01",
            "在酒店中与敏涅斯的对话，\x01",
            "也就不难得出答案了。\x02\x03",

            "#00000F敏涅斯随口说出的一句牢骚话……\x01",
            "与手册中的内容存在着明显矛盾。\x02\x03",

            "那正是敏涅斯\x01",
            "并非『昆西公司董事』\x01",
            "的证据……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x109,
        (
            "#10105F这、这本手册中\x01",
            "竟然有那么重要的线索……？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        "#00000F嗯，那句话就是——\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x105,
        (
            "#10304F等一下，\x01",
            "暂时还是不要说出来了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2EAF():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2EAF)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0178
    ChrTalk(
        0x101,
        "#00005F哎……为什么呢？\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，只有你一个人想到答案，\x01",
            "未免让人不甘心。\x02\x03",

            "#10309F所以，在揭穿敏涅斯\x01",
            "之前暂时保密，就当作\x01",
            "留给大家的作业如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#00006F那、那个……\x01",
            "这又不是在做游戏……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x103,
        (
            "#00203F不，我认为瓦吉先生\x01",
            "说的很有道理。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2FCF():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FCF)
    Sleep(100)

    #C0182
    ChrTalk(
        0x103,
        (
            "#00203F罗伊德前辈的想法\x01",
            "也存在错误的可能性，\x01",
            "如果现在就统一意见，多少有些危险。\x02\x03",

            "#00211F而且，每次都\x01",
            "被罗伊德前辈比下去，\x01",
            "实在是让人有些不爽。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_314C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0183
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "◆ＩＢＣ事件（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【不做变更】\x01",      # 0
            "【已调查】\x01",        # 1
            "【未调查】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3137"),
        (1, "loc_313C"),
        (2, "loc_3144"),
        (SWITCH_DEFAULT, "loc_314C"),
    )


    label("loc_3137")

    Jump("loc_314C")

    label("loc_313C")

    SetScenarioFlags(0x177, 4)
    Jump("loc_314C")

    label("loc_3144")

    ClearScenarioFlags(0x177, 4)
    Jump("loc_314C")

    label("loc_314C")

    OP_29(0x87, 0x1, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_END)), "loc_327F")

    #C0184
    ChrTalk(
        0x101,
        (
            "#00006F（后面那些才是她的真心话吧……）\x02\x03",

            "#00001F我、我明白了。\x01",
            "既然如此，这个问题\x01",
            "就留给大家继续思考……\x02\x03",

            "至于这本资料中的要点部分，\x01",
            "最好记录在调查手册中。\x02\x03",

            "#00003F好……我们已经收集到\x01",
            "不少可以证明敏涅斯\x01",
            "行事可疑的证据了。\x02\x03",

            "#00000F先回哈罗德\x01",
            "先生家吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x102,
        "#00100F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x4)
    Jump("loc_336B")

    label("loc_327F")


    #C0186
    ChrTalk(
        0x101,
        (
            "#00006F（后面那些才是她的真心话吧……）\x02\x03",

            "#00001F我、我明白了。\x01",
            "既然如此，这个问题\x01",
            "就留给大家继续思考……\x02\x03",

            "至于这本资料中的要点部分，\x01",
            "最好记录在调查手册中。\x02\x03",

            "#00003F……接下来还要去ＩＢＣ调查，\x01",
            "尽快行动吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        "#00100F嗯，明白了。\x02",
    )

    CloseMessageWindow()

    label("loc_336B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x177, 5)
    SetChrPos(0x0, -43000, 60, 40720, 90)
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)

    label("loc_33A4")

    Return()

    # Function_9_2859 end

    def Function_10_33A5(): pass

    label("Function_10_33A5")

    EventBegin(0x0)
    Fade(500)
    OP_68(-45700, 1560, 2610, 0)
    MoveCamera(38, 32, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(23160, 0)
    SetChrPos(0x101, -44780, 60, 2500, 0)
    SetChrPos(0x102, -45960, 0, 2500, 0)
    SetChrPos(0x103, -46730, 0, 1660, 0)
    SetChrPos(0x104, -44030, 0, 1620, 0)
    SetChrPos(0x105, -45860, 0, 980, 0)
    SetChrPos(0x109, -44820, 0, 940, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0xB4, 0x0)
    OP_0D()

    #C0188
    ChrTalk(
        0x9,
        (
            "啊……\x01",
            "艾莉大小姐，各位……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x105,
        (
            "#10300F（职业女性选秀活动中的『女仆』……\x01",
            "  邀请她来担当如何？）\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        (
            "#00003F（是啊……\x01",
            "  这主意不错。）\x02\x03",

            "#00000F（艾莉，\x01",
            "  你去问问她可以吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x102,
        (
            "#00102F（明白了，\x01",
            "  不过我觉得很难成功……）\x02\x03",

            "#00100F那个，乔安娜，\x01",
            "有件事情想请你帮忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x9,
        (
            "好的……\x01",
            "只要是艾莉大小姐的请求，\x01",
            "无论要我做什么都可以。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0193
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾莉邀请乔安娜参加\x01",
            "慈善宴会中的职业女性选秀活动。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0194
    ChrTalk(
        0x9,
        (
            "……啊……\x01",
            "选、选秀………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0195
    ChrTalk(
        0x9,
        "#4S……咦咦咦咦咦咦咦！？\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x103,
        "#00205F……好像很吃惊呢。\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x9,
        (
            "唔、唔唔，我不行的……\x01",
            "我怎么能参加什么职业女性选秀……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x104,
        (
            "#00302F不不不，绝对没问题的，\x01",
            "大哥哥我可以向你保证。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x101,
        "#00006F你拿什么保证啊……\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x102,
        (
            "#00105F那、那个，乔安娜，\x01",
            "不用太介意哦。\x02\x03",

            "#00103F我们再去找找，\x01",
            "应该会有其他的\x01",
            "女仆小姐愿意参加……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0201
    ChrTalk(
        0x9,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x9,
        (
            "……那个，我…………\x01",
            "还是让我参加吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x109,
        (
            "#10105F主、主意变得好快啊。\x01",
            "这虽然再好不过，可是你……\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x9,
        (
            "因、因为我才是……\x01",
            "……大小姐的女仆…………\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x102,
        (
            "#00102F呵呵，谢谢啦，乔安娜。\x01",
            "不过没必要勉强自己哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x9,
        (
            "……活动开始前请通知我吧，\x01",
            "我会立刻赶过去的…………\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x101,
        "#00000F嗯，拜托你了。\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3956")

    #C0208
    ChrTalk(
        0x101,
        (
            "#00003F好，我们总算\x01",
            "把参选者找齐了。\x02\x03",

            "#00000F这就去市民会馆，\x01",
            "向洛依先生他们报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x5)

    label("loc_3956")

    SetScenarioFlags(0x199, 6)
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x0, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -45350, 60, 2400, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_10_33A5 end

    def Function_11_3990(): pass

    label("Function_11_3990")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(18, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    #A0209
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3S……本公司身为糕点制造业界的领头羊，\x01",
            "为了糕点制造业的未来，始终在不断钻研。\x01",
            "本手册将会为您展示\x01",
            "本公司的部分方面。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(18, 0, 100, 0)
    SetChrName("")

    #A0210
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3S对于糕点而言，\x01",
            "最重要的就是\x01",
            "能否让食用者感到『美味』。\x01",
            "为此，本公司在\x01",
            "『提高糕点的品质』\x01",
            "这一点上绝对不会妥协。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(18, 0, 100, 0)
    SetChrName("")

    #A0211
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3S糕点制造工厂中配备了最新型设备，\x01",
            "卫生方面也采取了最完善的处理措施，\x01",
            "这些基本条件自不必说。\x01",
            "至于糕点原材料的品质与产地，\x01",
            "本公司也有着严格的要求。\x01",
            "此外，关于商品开发这一过程，\x01",
            "本公司也制定了严谨的步骤与基准。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(18, 0, 100, 0)
    SetChrName("")

    #A0212
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3S董事要亲自试吃开发中的商品，\x01",
            "以便判断其上市销售的可行性。\x01",
            "之后，还要经过多次企划会议讨论，\x01",
            "才会正式投入到生产线。\x01",
            "这都是为了能给顾客献上\x01",
            "最美味的糕点，给顾客最好的享受，\x01",
            "而从公司初创时便一直继承下来的传统。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(18, 0, 100, 0)
    SetChrName("")

    #A0213
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3S昆西公司正是因为长期\x01",
            "给顾客提供高品质的糕点，\x01",
            "才能获得如今的成就……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(18, 0, 100, 0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_11_3990 end

    SaveToFile()

Try(main)
