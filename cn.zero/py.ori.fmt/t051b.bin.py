from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t051b.bin",                # FileName
        "t051b",                    # MapName
        "t051b",                    # Location
        0x003D,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 61, 0, 1, 0, 2],
    )

    BuildStringList((
        "t051b",                  # 0
        "比克森镇长",             # 1
        "安娜夫人",               # 2
        "比鲁玛婆婆",             # 3
        "亚米",                   # 4
        "矿工罗基",               # 5
        "米兰达",                 # 6
        "亚雷库",                 # 7
        "霍夫曼矿山长",           # 8
        "矿工马库斯",             # 9
        "卢利艾达",               # 10
    ))

    AddCharChip((
        "chr/ch23202.itc",                   # 00
        "chr/ch20100.itc",                   # 01
        "chr/ch23700.itc",                   # 02
        "chr/ch26200.itc",                   # 03
        "chr/ch23300.itc",                   # 04
        "chr/ch23000.itc",                   # 05
        "chr/ch26302.itc",                   # 06
        "chr/ch22702.itc",                   # 07
        "apl/ch50130.itc",                   # 08
        "chr/ch24300.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
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

    DeclNpc(-889,    949,     2640,    90,   341,  0x0, 0,   0,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(-6530,   750,     59,      270,  261,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(49209,   0,       4369,    0,    261,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(50959,   0,       1389,    270,  389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(49689,   0,       1389,    90,   389,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(97519,   150,     2130,    180,  469,  0x0, 0,   7,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(98349,   0,       -1129,   270,  389,  0x0, 0,   5,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(97459,   150,     -1169,   0,    469,  0x0, 0,   6,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(154710,  300,     2500,    315,  471,  0x0, 0,   8,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(147369,  0,       4179,    333,  261,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)

    ScpFunction((
        "Function_0_264",          # 00, 0
        "Function_1_31C",          # 01, 1
        "Function_2_421",          # 02, 2
        "Function_3_42D",          # 03, 3
        "Function_4_6A5",          # 04, 4
        "Function_5_6ED",          # 05, 5
        "Function_6_721",          # 06, 6
        "Function_7_7B5",          # 07, 7
        "Function_8_897",          # 08, 8
        "Function_9_8E4",          # 09, 9
        "Function_10_973",         # 0A, 10
        "Function_11_ACC",         # 0B, 11
        "Function_12_BDD",         # 0C, 12
        "Function_13_D62",         # 0D, 13
        "Function_14_E18",         # 0E, 14
        "Function_15_ED8",         # 0F, 15
    ))


    def Function_0_264(): pass

    label("Function_0_264")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2A4"),
        (1, "loc_2B0"),
        (2, "loc_2BC"),
        (3, "loc_2C8"),
        (4, "loc_2D4"),
        (5, "loc_2E0"),
        (6, "loc_2EC"),
        (SWITCH_DEFAULT, "loc_2F8"),
    )


    label("loc_2A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_304")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_31B")

    Return()

    # Function_0_264 end

    def Function_1_31C(): pass

    label("Function_1_31C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_32A")
    Jump("loc_420")

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_338")
    Jump("loc_420")

    label("loc_338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_346")
    Jump("loc_420")

    label("loc_346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_354")
    Jump("loc_420")

    label("loc_354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_362")
    Jump("loc_420")

    label("loc_362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_370")
    Jump("loc_420")

    label("loc_370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_37E")
    Jump("loc_420")

    label("loc_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_38C")
    Jump("loc_420")

    label("loc_38C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_39A")
    Jump("loc_420")

    label("loc_39A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3A8")
    Jump("loc_420")

    label("loc_3A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3B6")
    Jump("loc_420")

    label("loc_3B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_409")
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 2)), scpexpr(EXPR_END)), "loc_3FD")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_404")

    label("loc_3FD")

    TurnDirection(0xE, 0xD, 0)

    label("loc_404")

    Jump("loc_420")

    label("loc_409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_417")
    Jump("loc_420")

    label("loc_417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_420")

    label("loc_420")

    Return()

    # Function_1_31C end

    def Function_2_421(): pass

    label("Function_2_421")

    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_421 end

    def Function_3_42D(): pass

    label("Function_3_42D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C1")
    Jump("loc_50B")

    label("loc_4C1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4E1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50B")

    label("loc_4E1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_501")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50B")

    label("loc_501")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    OP_64(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63D")
    SetChrSubChip(0xFE, 0x0)

    #C0001
    ChrTalk(
        0xFE,
        "独占七耀石的采购权吗……\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "的确，矿工们的安全\x01",
            "是最重要的……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "但还有商人正在与我们做生意。\x01",
            "我也不能失信于他们……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#0003F（镇长先生……\x01",
            "　好像很苦恼呢。）\x02\x03",

            "#0001F（……那些家伙今晚一定会出现。\x01",
            "　准备完毕后，就在房间内待命吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_68B")

    label("loc_63D")


    #C0005
    ChrTalk(
        0xFE,
        (
            "呀，是你们啊……\x01",
            "今晚要住在镇里吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "有矿工受伤了，\x01",
            "你们也要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68B")

    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_3_42D end

    def Function_4_6A5(): pass

    label("Function_4_6A5")

    TalkBegin(0xFE)

    #C0007
    ChrTalk(
        0xFE,
        "老伴他……好像很苦恼。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "做一些能让他打起精神的\x01",
            "食物吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_6A5 end

    def Function_5_6ED(): pass

    label("Function_5_6ED")

    TalkBegin(0xFE)

    #C0009
    ChrTalk(
        0xFE,
        (
            "我家孙儿们也真是的，\x01",
            "大半夜还这么吵闹。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_6ED end

    def Function_6_721(): pass

    label("Function_6_721")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_736")
    Call(0, 7)
    Jump("loc_7B1")

    label("loc_736")


    #C0010
    ChrTalk(
        0xFE,
        (
            "真是的，哥哥，\x01",
            "去和工友们一起喝点酒不是挺好的嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "……听说马库斯先生\x01",
            "刚被袭击过，\x01",
            "应该不会这么快再出现魔兽吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B1")

    TalkEnd(0xFE)
    Return()

    # Function_6_721 end

    def Function_7_7B5(): pass

    label("Function_7_7B5")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    TurnDirection(0xB, 0xC, 0)
    TurnDirection(0xC, 0xB, 0)

    #C0012
    ChrTalk(
        0xB,
        (
            "哥哥，\x01",
            "今天没去喝酒吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xC,
        (
            "镇长说过，让我\x01",
            "早点回家的。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xC,
        "我直接回家，你有什么不满的啊？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xB,
        "……如果一定要说的话……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        "对了，……可以说是『你真不合群』吧？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xC,
        "你、你烦不烦啊。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_7_7B5 end

    def Function_8_897(): pass

    label("Function_8_897")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AC")
    Call(0, 7)
    Jump("loc_8E0")

    label("loc_8AC")


    #C0018
    ChrTalk(
        0xFE,
        "嘁，多管闲事。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        "……我平时也不怎么喝酒的。\x02",
    )

    CloseMessageWindow()

    label("loc_8E0")

    TalkEnd(0xFE)
    Return()

    # Function_8_897 end

    def Function_9_8E4(): pass

    label("Function_9_8E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 2)), scpexpr(EXPR_END)), "loc_921")
    TurnDirection(0xFE, 0xF, 0)

    #C0020
    ChrTalk(
        0xFE,
        (
            "喂喂，快点吃饭啦。\x01",
            "我肚子饿了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96F")

    label("loc_921")


    #C0021
    ChrTalk(
        0xFE,
        (
            "等爸爸回来才能吃晚饭，\x01",
            "要忍一忍。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "……肚子好饿啊，\x01",
            "爸爸还不回来吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96F")

    TalkEnd(0xFE)
    Return()

    # Function_9_8E4 end

    def Function_10_973(): pass

    label("Function_10_973")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A07")
    Jump("loc_A51")

    label("loc_A07")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A27")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A51")

    label("loc_A27")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A47")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A51")

    label("loc_A47")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A51")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A88")
    Call(0, 11)
    Jump("loc_AC4")

    label("loc_A88")


    #C0023
    ChrTalk(
        0xFE,
        (
            "啊，是你们呀。\x01",
            "进矿山是可以，\x01",
            "但是要小心点，别受伤啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_973 end

    def Function_11_ACC(): pass

    label("Function_11_ACC")

    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xF, 0x0)

    #C0024
    ChrTalk(
        0xD,
        (
            "你问被魔兽袭击的马库斯先生……\x01",
            "现在是不是还没痊愈？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xF,
        (
            "嗯……\x01",
            "虽然伤得\x01",
            "不算很严重……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xF,
        (
            "但再怎么说，也是被咬到了腿，\x01",
            "还是不要硬撑比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xD,
        "是啊……真让人担心啊。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xD,
        "……你也要小心哦。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xF,
        (
            "哈哈，没问题。\x01",
            "我可是矿山长呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xD,
        "说点正经话啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_11_ACC end

    def Function_12_BDD(): pass

    label("Function_12_BDD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C71")
    Jump("loc_CBB")

    label("loc_C71")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C91")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CBB")

    label("loc_C91")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CB1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CBB")

    label("loc_CB1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CBB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 2)), scpexpr(EXPR_END)), "loc_D2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CFB")
    Call(0, 11)
    Jump("loc_D2A")

    label("loc_CFB")


    #C0031
    ChrTalk(
        0xFE,
        (
            "因为那个人过于拼命，\x01",
            "所以很让人担心呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2A")

    Jump("loc_D5A")

    label("loc_D2F")


    #C0032
    ChrTalk(
        0xFE,
        (
            "呼，我老公可真是的，\x01",
            "回来得好晚啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D5A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_BDD end

    def Function_13_D62(): pass

    label("Function_13_D62")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D77")
    Call(0, 14)
    Jump("loc_E14")

    label("loc_D77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE4")

    #C0033
    ChrTalk(
        0xFE,
        (
            "我要是不进入矿山，\x01",
            "晚上都睡不着觉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "……可恶。\x01",
            "如果没有被魔兽袭击\x01",
            "就好了啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_E14")

    label("loc_DE4")


    #C0035
    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "再这样下去的话，\x01",
            "身体都要变迟钝了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E14")

    TalkEnd(0xFE)
    Return()

    # Function_13_D62 end

    def Function_14_E18(): pass

    label("Function_14_E18")


    #C0036
    ChrTalk(
        0xFE,
        "啊……夜晚好漫长啊……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "买来的书\x01",
            "也都读完了……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "……有兴趣的话，你也读读看如何？\x01",
            "这本书就送给你好了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2C8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2C8, 1)
    SetScenarioFlags(0x9C, 2)
    Return()

    # Function_14_E18 end

    def Function_15_ED8(): pass

    label("Function_15_ED8")

    TalkBegin(0xFE)

    #C0040
    ChrTalk(
        0xFE,
        (
            "我的丈夫\x01",
            "从白天开始就一直很沮丧。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        "……希望他的身体能早日康复……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_ED8 end

    SaveToFile()

Try(main)
