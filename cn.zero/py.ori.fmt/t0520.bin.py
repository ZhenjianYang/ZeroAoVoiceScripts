from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t0520.bin",                # FileName
        "t0520",                    # MapName
        "t0520",                    # Location
        0x003F,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 63, 0, 2, 0, 3],
    )

    BuildStringList((
        "t0520",                  # 0
        "诺玛",                   # 1
        "琉卡",                   # 2
        "矿工罗基",               # 3
        "弗里吉亚",               # 4
        "莱缇娜",                 # 5
        "艾丝蒂尔",               # 6
        "约修亚",                 # 7
        "游击士斯克特",           # 8
        "游击士温蔡尔",           # 9
        "游客沃伦斯",             # 10
    ))

    AddCharChip((
        "chr/ch23500.itc",                   # 00
        "chr/ch25700.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "apl/ch50130.itc",                   # 04
        "chr/ch33300.itc",                   # 05
        "chr/ch34500.itc",                   # 06
        "chr/ch00602.itc",                   # 07
        "chr/ch00702.itc",                   # 08
        "chr/ch27202.itc",                   # 09
        "chr/ch27302.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch24402.itc",                   # 0C
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

    DeclNpc(3700,    0,       4289,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-4880,   -750,    -860,    270,  261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(147360,  500,     4599,    0,    469,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(204809,  0,       560,     270,  261,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(203350,  0,       560,     90,   261,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-7530,   -600,    -3140,   270,  469,  0x0, 0,   7,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-8640,   -600,    -4380,   0,    469,  0x0, 0,   8,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-6199,   -600,    4199,    270,  469,  0x0, 0,   9,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(-9289,   -600,    3869,    90,   469,  0x0, 0,   10,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(-9510,   -600,    -1200,   180,  405,  0x0, 0,   12,  0,   255, 255, 0,   15,  255,  0)

    DeclActor(3700,    0,       2920,    1000,    3700,    1500,    4290,    0x007E, 0,  4,  0x0000)

    ScpFunction((
        "Function_0_290",          # 00, 0
        "Function_1_348",          # 01, 1
        "Function_2_373",          # 02, 2
        "Function_3_573",          # 03, 3
        "Function_4_5B2",          # 04, 4
        "Function_5_5B6",          # 05, 5
        "Function_6_11EB",         # 06, 6
        "Function_7_1AAD",         # 07, 7
        "Function_8_1B2B",         # 08, 8
        "Function_9_22CF",         # 09, 9
        "Function_10_29AA",        # 0A, 10
        "Function_11_2B70",        # 0B, 11
        "Function_12_2E0D",        # 0C, 12
        "Function_13_2F8C",        # 0D, 13
        "Function_14_31EF",        # 0E, 14
        "Function_15_3422",        # 0F, 15
        "Function_16_35D3",        # 10, 16
        "Function_17_386E",        # 11, 17
    ))


    def Function_0_290(): pass

    label("Function_0_290")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2D0"),
        (1, "loc_2DC"),
        (2, "loc_2E8"),
        (3, "loc_2F4"),
        (4, "loc_300"),
        (5, "loc_30C"),
        (6, "loc_318"),
        (SWITCH_DEFAULT, "loc_324"),
    )


    label("loc_2D0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_2DC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_2E8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_2F4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_300")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_30C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_318")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_324")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_330")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_347")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_347")

    Return()

    # Function_0_290 end

    def Function_1_348(): pass

    label("Function_1_348")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_372")
    OP_94(0xFE, 0x31678, 0xFFFFFF1A, 0x321B8, 0x3DE, 0x3E8)
    Sleep(300)
    Jump("Function_1_348")

    label("loc_372")

    Return()

    # Function_1_348 end

    def Function_2_373(): pass

    label("Function_2_373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_38B")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_55F")

    label("loc_38B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3A3")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_55F")

    label("loc_3A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_3BB")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_55F")

    label("loc_3BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3D3")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_55F")

    label("loc_3D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3EB")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_55F")

    label("loc_3EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_421")
    SetChrPos(0xB, 204010, 0, 560, 270)
    BeginChrThread(0xB, 0, 0, 1)
    SetChrPos(0xC, 199530, 0, 3160, 225)
    Jump("loc_55F")

    label("loc_421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_457")
    SetChrPos(0xB, 204010, 0, 560, 270)
    BeginChrThread(0xB, 0, 0, 1)
    SetChrPos(0xC, 199530, 0, 3160, 225)
    Jump("loc_55F")

    label("loc_457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_48D")
    SetChrPos(0xB, 204010, 0, 560, 270)
    BeginChrThread(0xB, 0, 0, 1)
    SetChrPos(0xC, 199530, 0, 3160, 225)
    Jump("loc_55F")

    label("loc_48D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4C8")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xB, 204010, 0, 560, 270)
    BeginChrThread(0xB, 0, 0, 1)
    SetChrPos(0xC, 199530, 0, 3160, 225)
    Jump("loc_55F")

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4F5")
    SetChrPos(0x9, 10680, 0, -830, 90)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)

    label("loc_4F5")

    Jump("loc_55F")

    label("loc_4FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_53A")
    SetChrPos(0xB, 204010, 0, 560, 270)
    BeginChrThread(0xB, 0, 0, 1)
    SetChrPos(0xC, 199530, 0, 3160, 225)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_55F")

    label("loc_53A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_548")
    Jump("loc_55F")

    label("loc_548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_556")
    Jump("loc_55F")

    label("loc_556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_55F")

    label("loc_55F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_572")
    ClearChrFlags(0x11, 0x80)

    label("loc_572")

    Return()

    # Function_2_373 end

    def Function_3_573(): pass

    label("Function_3_573")

    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59A")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_5B1")

    label("loc_59A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B1")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_5B1")

    Return()

    # Function_3_573 end

    def Function_4_5B2(): pass

    label("Function_4_5B2")

    Call(0, 5)
    Return()

    # Function_4_5B2 end

    def Function_5_5B6(): pass

    label("Function_5_5B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CC")
    Call(0, 17)
    Jump("loc_11EA")

    label("loc_5CC")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E7")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "休息\x01",      # 2
            "放弃\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_638")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_638")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_658")
    OP_AF(0x52)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11E2")

    label("loc_658")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_678")
    OP_AF(0x50)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11E2")

    label("loc_678")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68C")
    Jump("loc_11E2")

    label("loc_68C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_719")

    #C0001
    ChrTalk(
        0x8,
        (
            "冈兹先生失踪的原因，\x01",
            "以及镇长还没回来的理由……\x01",
            "我们直到现在都还一无所知。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        "唉，好担心啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_11E2")

    label("loc_719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_781")

    #C0003
    ChrTalk(
        0x8,
        (
            "我当时看到了\x01",
            "正打算上巴士的镇长，\x01",
            "他的表情似乎很阴沉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        "冈兹先生出了什么事吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_11E2")

    label("loc_781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_818")

    #C0005
    ChrTalk(
        0x8,
        (
            "几个月前的魔兽骚动也好，\x01",
            "这次的矿工失踪也罢……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "总觉得在短短时间内\x01",
            "发生了好多事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "希望这不是什么\x01",
            "坏事即将发生的征兆……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11E2")

    label("loc_818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_851")

    #C0008
    ChrTalk(
        0x8,
        (
            "你们看起来好像很累啊，\x01",
            "要不要住宿呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11E2")

    label("loc_851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8AA")

    #C0009
    ChrTalk(
        0x8,
        "感觉最近总是提不起劲呢……\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "是不是因为喝酒最豪爽\x01",
            "的那位没来呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11E2")

    label("loc_8AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97F")

    #C0011
    ChrTalk(
        0x8,
        (
            "我们这里的酒\x01",
            "都是从一位名叫哈罗德\x01",
            "的商人那里进的货哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "他穿得那么体面，\x01",
            "拿来的酒果然\x01",
            "也都是好酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "麦酒最近差不多\x01",
            "都快被矿工们喝光了……\x01",
            "他下次再来的时候，得再订一些货呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9CE")

    label("loc_97F")


    #C0014
    ChrTalk(
        0x8,
        (
            "哈罗德先生卖给我们的酒\x01",
            "大多都是好酒呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        "对我们来说，真是必不可少的。\x02",
    )

    CloseMessageWindow()

    label("loc_9CE")

    Jump("loc_11E2")

    label("loc_9D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_B68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B08")

    #C0016
    ChrTalk(
        0x8,
        (
            "女招待琉卡总是\x01",
            "一脸不高兴的样子。\x01",
            "只会说些刻薄的话呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        "……下次要不要给她灌点酒呢。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "那孩子的酒量非常非常小，\x01",
            "喝醉时的表情特别好玩哦。\x02",
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

    #C0019
    ChrTalk(
        0x102,
        "#0106F这算不算轻度犯罪啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B63")

    label("loc_B08")


    #C0020
    ChrTalk(
        0x8,
        "……下次要不要给琉卡灌点酒呢。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "那孩子的酒量非常非常小，\x01",
            "喝醉时的表情特别好玩哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B63")

    Jump("loc_11E2")

    label("loc_B68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_BF7")

    #C0022
    ChrTalk(
        0x8,
        (
            "毕竟是创立七十周年嘛。\x01",
            "今年的游客比去年多了不少，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "纪念庆典期间，矿工们都去市里玩了，\x01",
            "酒馆完全赚不到钱呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11E2")

    label("loc_BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_CEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C76")

    #C0024
    ChrTalk(
        0x8,
        "昨天，全体矿工在这开了个宴会。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "虽然很忙碌，\x01",
            "但能让他们那么开心，\x01",
            "就算是酒馆最大的幸福了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CE5")

    label("loc_C76")


    #C0026
    ChrTalk(
        0x8,
        (
            "说起来，矿工罗基\x01",
            "完全醉倒了呢。\x01",
            "没办法，只好让他在店里睡下了。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "真是的，年纪轻轻，\x01",
            "竟然这么没出息呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE5")

    Jump("loc_11E2")

    label("loc_CEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_D54")

    #C0028
    ChrTalk(
        0x8,
        (
            "今天来的客人好像很年轻，\x01",
            "但听说是游击士呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "……气氛好像很沉重，\x01",
            "是出了什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11E2")

    label("loc_D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_EA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E30")

    #C0030
    ChrTalk(
        0x8,
        (
            "这家店在白天\x01",
            "还真是闲啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "……好吧，反正也很闲，\x01",
            "就告诉你们一个秘密吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "女招待琉卡\x01",
            "虽然总是一脸不高兴的表情……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "但笑起来时可是超级可爱的。\x01",
            "我要是男人的话，\x01",
            "一定会迷上她哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E9D")

    label("loc_E30")


    #C0034
    ChrTalk(
        0x8,
        (
            "琉卡虽然总是一脸不高兴的样子，\x01",
            "但笑容可是超级可爱的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "不过她很少露出\x01",
            "那种笑容，\x01",
            "还真是很可惜呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E9D")

    Jump("loc_11E2")

    label("loc_EA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_FB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F54")

    #C0036
    ChrTalk(
        0x8,
        (
            "魔兽骚动平息了，\x01",
            "我们镇子也恢复了平静。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "虽然矿工们\x01",
            "老是抱怨什么『不能提早回家了』\x01",
            "之类的胡话。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "总而言之，\x01",
            "不会再遭遇危险，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FB3")

    label("loc_F54")


    #C0039
    ChrTalk(
        0x8,
        (
            "魔兽骚动平息了，\x01",
            "矿工和镇上的人\x01",
            "也不会再受到袭击了。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "这都多亏了你们，\x01",
            "真是太谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB3")

    Jump("loc_11E2")

    label("loc_FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_1058")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1016")

    #C0041
    ChrTalk(
        0x8,
        "嗯，要出门吗？\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "最近镇上有些不太平，\x01",
            "所以最好早点回来哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1053")

    label("loc_1016")


    #C0043
    ChrTalk(
        0x8,
        (
            "要不就来喝点酒，\x01",
            "暖暖身子吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        "……虽然已经满座了。\x02",
    )

    CloseMessageWindow()

    label("loc_1053")

    Jump("loc_11E2")

    label("loc_1058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_11E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_107A")
    SetScenarioFlags(0x66, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_107A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_114E")

    #C0045
    ChrTalk(
        0x8,
        (
            "哎呀，你们看上去很面生呢。\x01",
            "是从克洛斯贝尔市来的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "话说回来，\x01",
            "你们来的时机真是不巧啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "最近有狼形魔兽\x01",
            "在这一带肆虐呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "不久前，我们这里的粮仓也被破坏了。\x01",
            "真是的，太可恶了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11E2")

    label("loc_114E")


    #C0049
    ChrTalk(
        0x8,
        (
            "对了对了，\x01",
            "不嫌弃的话，要不要吃点什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "要是想好好休息一下的话，\x01",
            "最好趁现在休息哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "到了晚上，\x01",
            "收工回来的矿工们\x01",
            "就会把席位都占满的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E2")

    Jump("loc_5D9")

    label("loc_11E7")

    TalkEnd(0x8)

    label("loc_11EA")

    Return()

    # Function_5_5B6 end

    def Function_6_11EB(): pass

    label("Function_6_11EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1257")

    #C0052
    ChrTalk(
        0xFE,
        (
            "我感觉冈兹先生失踪\x01",
            "事件的背后……\x01",
            "隐藏着巨大的谜团。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "……是悬疑小说\x01",
            "看多了吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA9")

    label("loc_1257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_12C0")

    #C0054
    ChrTalk(
        0xFE,
        (
            "既然找到冈兹先生了……\x01",
            "很可能会再开一场庆祝宴会吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        "唉……收拾残局又会很辛苦呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AA9")

    label("loc_12C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_1328")

    #C0056
    ChrTalk(
        0xFE,
        (
            "冈兹先生好像真的\x01",
            "很不擅长玩牌呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "在这里喝醉的时候，\x01",
            "话题基本都是对输钱的抱怨。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA9")

    label("loc_1328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1385")

    #C0058
    ChrTalk(
        0xFE,
        "嗯，打扫得差不多了吧。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "只是少了冈兹先生一个人，\x01",
            "打扫就变得简单多了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA9")

    label("loc_1385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1427")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F5")

    #C0060
    ChrTalk(
        0xFE,
        "好了～要趁客人不在时快点打扫才行。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "话说回来，最近好像\x01",
            "都不怎么开宴会了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1422")

    label("loc_13F5")


    #C0062
    ChrTalk(
        0xFE,
        (
            "最近一直没什么宴会，\x01",
            "所以打扫很轻松呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1422")

    Jump("loc_1AA9")

    label("loc_1427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_149C")

    #C0063
    ChrTalk(
        0xFE,
        "纪念庆典在今天就要结束了啊。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "游客们也许要走了，\x01",
            "不过矿工们也该回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        "唉唉～好忙好忙。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AA9")

    label("loc_149C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1513")

    #C0066
    ChrTalk(
        0xFE,
        (
            "算啦，虽然有点忙……\x01",
            "不过，你们要不要也喝点什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        "……但就算你们因此搞砸了工作，我也不负责哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AA9")

    label("loc_1513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1594")

    #C0068
    ChrTalk(
        0xFE,
        (
            "在举办纪念庆典的时候\x01",
            "特地跑到这种冷清之地的\x01",
            "游客吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "……不过，心情也可以理解吧。\x01",
            "我也很讨厌人山人海。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA9")

    label("loc_1594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1725")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_168C")

    #C0070
    ChrTalk(
        0xFE,
        "真是的，每天都快累死了。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "……酒这种东西，到底好在哪里啊？\x01",
            "我完全不能喝酒，所以真是不明白它有什么吸引人的。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#0006F以、以酒馆女招待的身份来说，\x01",
            "这种发言还真是意外呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "你好烦啊，客人。\x01",
            "这是我的自由吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1720")

    label("loc_168C")


    #C0074
    ChrTalk(
        0xFE,
        "真是的，酒这种东西，到底好在哪里啊。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "……之前因为好奇而喝了一点，\x01",
            "但现在已经完全不记得当时的情况了，\x01",
            "所以真不明白酒这东西有什么吸引人的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1720")

    Jump("loc_1AA9")

    label("loc_1725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_180A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C2")

    #C0076
    ChrTalk(
        0xFE,
        (
            "……干什么啊，\x01",
            "不要一直盯着人家看啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "要点菜就去找老板娘。\x01",
            "我只管送菜。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "……完毕。\x01",
            "听明白的话，\x01",
            "就别再烦我了好吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1805")

    label("loc_17C2")


    #C0079
    ChrTalk(
        0xFE,
        (
            "每天晚上都要应付\x01",
            "喝醉的矿工，累死人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        "别再烦我了好吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1805")

    Jump("loc_1AA9")

    label("loc_180A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1943")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C4")

    #C0081
    ChrTalk(
        0xFE,
        (
            "呼啊……\x01",
            "啊～真是的，好困好困。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "矿工们收工回来\x01",
            "就会开宴会，\x01",
            "所以我和老板娘都睡眠不足。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "那个『击退魔兽纪念宴会』\x01",
            "到底要开到什么时候啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_193E")

    label("loc_18C4")


    #C0084
    ChrTalk(
        0xFE,
        (
            "那些矿工们，直到现在，\x01",
            "每天晚上还都要开什么\x01",
            "『击退魔兽纪念宴会』。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "只不过就是想找个借口\x01",
            "喝酒而已吧。\x01",
            "真是的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_193E")

    Jump("loc_1AA9")

    label("loc_1943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_1951")
    Jump("loc_1AA9")

    label("loc_1951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_19F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C0")

    #C0086
    ChrTalk(
        0xFE,
        (
            "我擦我擦……\x01",
            "好，这样就没问题了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "嗯，接下来会很忙……\x01",
            "稍微休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19EB")

    label("loc_19C0")


    #C0088
    ChrTalk(
        0xFE,
        (
            "嗯，接下来会很忙……\x01",
            "稍微休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19EB")

    Jump("loc_1AA9")

    label("loc_19F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1AA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A12")
    SetScenarioFlags(0x66, 5)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A70")

    #C0089
    ChrTalk(
        0xFE,
        (
            "……欢迎光临，\x01",
            "要点菜的话请去柜台。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "……怎么了，\x01",
            "找我有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AA9")

    label("loc_1A70")


    #C0091
    ChrTalk(
        0xFE,
        (
            "想点菜的话，能不能去柜台？\x01",
            "我正忙着为晚场做准备呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA9")

    TalkEnd(0xFE)
    Return()

    # Function_6_11EB end

    def Function_7_1AAD(): pass

    label("Function_7_1AAD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B07")

    #C0092
    ChrTalk(
        0xFE,
        (
            "呜呕…………\x01",
            "喝……喝不下了……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        "让、让我一个人待着…………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1B27")

    label("loc_1B07")


    #C0094
    ChrTalk(
        0xFE,
        "让、让我一个人待着…………\x02",
    )

    CloseMessageWindow()

    label("loc_1B27")

    TalkEnd(0xFE)
    Return()

    # Function_7_1AAD end

    def Function_8_1B2B(): pass

    label("Function_8_1B2B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1C9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C21")

    #C0095
    ChrTalk(
        0xFE,
        "呵呵呵！\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "终于、终于……\x01",
            "我终于成功收购到\x01",
            "七耀石的结晶了！\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "而且还是\x01",
            "这么大的红耀石……\x01",
            "我还是第一次见呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "呵呵，这样应该就能向\x01",
            "身在帝国的父亲提交令他满意的报告了！\x01",
            "距离大商人的目标又迈进了一步啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1C98")

    label("loc_1C21")


    #C0099
    ChrTalk(
        0xFE,
        (
            "竟然能开采到\x01",
            "这么大的红耀石……\x01",
            "不愧是七耀石的产地呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "呵呵，似乎能向身在帝国的父亲\x01",
            "提交令他满意的报告了呢！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C98")

    Jump("loc_22CB")

    label("loc_1C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1D01")

    #C0101
    ChrTalk(
        0xFE,
        (
            "我今晚要去镇长家\x01",
            "进行收购七耀石的交涉。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "在弄到手之前……\x01",
            "我绝对不会放弃的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22CB")

    label("loc_1D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1E58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DFF")

    #C0103
    ChrTalk(
        0xFE,
        (
            "我为了收购到\x01",
            "七耀石的结晶，\x01",
            "从之前开始就一直与镇长交涉……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "可是那个镇长也很难对付呢，\x01",
            "怎么都不肯说ＹＥＳ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "不，我可不能\x01",
            "一直消沉下去。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "父亲是大商人，而我是继承他血脉的人，\x01",
            "一定要将它弄到手，对此我志在必得！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1E53")

    label("loc_1DFF")


    #C0107
    ChrTalk(
        0xFE,
        (
            "既然决定了，\x01",
            "就必须要好好考虑交涉的手段了。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "首先要将收购价\x01",
            "下狠心提高……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E53")

    Jump("loc_22CB")

    label("loc_1E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1EB6")

    #C0109
    ChrTalk(
        0xFE,
        (
            "呜呜……一楼昨天好吵，\x01",
            "害得我都没睡着。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "好困啊……\x01",
            "今天要好好睡一觉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22CB")

    label("loc_1EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_202F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB2")

    #C0111
    ChrTalk(
        0xFE,
        (
            "我想在玛因兹\x01",
            "收购的七耀石结晶\x01",
            "是相当贵重的物品。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "嗯，据说开采量很少，\x01",
            "如果运气不好\x01",
            "就肯定买不到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "昨天的交涉结果很令人遗憾，\x01",
            "是我被拒绝了。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "……没关系，\x01",
            "我准备了很充足的滞留资金，\x01",
            "一定要坚持到最后一刻！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_202A")

    label("loc_1FB2")


    #C0115
    ChrTalk(
        0xFE,
        (
            "滞留资金我多得是，\x01",
            "为了照顾我兼供我消遣，\x01",
            "还带了莱缇娜来。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "呵呵呵，\x01",
            "直到买到结晶为止，\x01",
            "我一定不会放弃交涉的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_202A")

    Jump("loc_22CB")

    label("loc_202F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_21D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_214B")

    #C0117
    ChrTalk(
        0xFE,
        (
            "贵重的七耀石结晶……\x01",
            "我就是想买这个，\x01",
            "才会一直留在这里的。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "结晶可不是像魔兽掉落的\x01",
            "耀晶片那样的小东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "每一块都蕴藏着妖艳的光辉，\x01",
            "帝国的贵族阶层\x01",
            "都将它用来做首饰的。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "如果能顺利收购，带回帝国的话，\x01",
            "一定可以卖到很高的价钱呢。\x01",
            "呵呵呵……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_21CF")

    label("loc_214B")


    #C0121
    ChrTalk(
        0xFE,
        (
            "七耀石的结晶\x01",
            "可不是魔兽掉落的\x01",
            "那种小小的耀晶片哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "如果能顺利收购，带回帝国的话，\x01",
            "一定可以卖到很高的价钱呢。\x01",
            "呵呵呵……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21CF")

    Jump("loc_22CB")

    label("loc_21D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_21E2")
    Jump("loc_22CB")

    label("loc_21E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_225B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21FD")
    Call(0, 10)
    Jump("loc_2256")

    label("loc_21FD")


    #C0123
    ChrTalk(
        0xFE,
        (
            "差不多快到矿工们\x01",
            "回来的时候了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "要是还像昨天那样\x01",
            "大吵大嚷的，\x01",
            "可没法吃饭呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2256")

    Jump("loc_22CB")

    label("loc_225B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_22CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2276")
    Call(0, 10)
    Jump("loc_22CB")

    label("loc_2276")


    #C0125
    ChrTalk(
        0xFE,
        (
            "哎呀……你们\x01",
            "也是来收购七耀石的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "呵呵～！\x01",
            "你们的交涉手腕\x01",
            "能赢过我吗！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22CB")

    TalkEnd(0xFE)
    Return()

    # Function_8_1B2B end

    def Function_9_22CF(): pass

    label("Function_9_22CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_23F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2395")

    #C0127
    ChrTalk(
        0xFE,
        (
            "小姐买到了七耀石结晶……\x01",
            "唉……太久了。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "虽然确实是非常不错的商品……\x01",
            "但是用了将近四个月的滞留费，\x01",
            "她真的明白这一点吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "…………\x01",
            "还是不要想太多为好吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_23F1")

    label("loc_2395")


    #C0130
    ChrTalk(
        0xFE,
        (
            "……总而言之，\x01",
            "这下总算能回帝国了。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "离家出走了将近四个月，\x01",
            "家中现在怎么样了呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23F1")

    Jump("loc_29A6")

    label("loc_23F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_24AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_246D")

    #C0132
    ChrTalk(
        0xFE,
        (
            "（小姐只要\x01",
            "  一说到交易的事，\x01",
            "  就变得这么认真……）\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        "（结、结果到底会怎样呢……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_24A9")

    label("loc_246D")


    #C0134
    ChrTalk(
        0xFE,
        (
            "（紧张紧张……\x01",
            "  今晚的交易，\x01",
            "  结果到底会怎样呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24A9")

    Jump("loc_29A6")

    label("loc_24AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_255C")

    #C0135
    ChrTalk(
        0xFE,
        (
            "小姐凭借她特有的强硬态度\x01",
            "和雄厚的资金在进行交涉……\x01",
            "但似乎还是很困难呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "……真是的，既然都走到这一步，就已经没有退路了。\x01",
            "希望小姐\x01",
            "能努力到最后一步！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A6")

    label("loc_255C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_263F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25DA")

    #C0137
    ChrTalk(
        0xFE,
        (
            "昨天矿工们开宴会\x01",
            "好像开到很晚。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "……我也一直努力\x01",
            "想让小姐睡着，熬到很晚，\x01",
            "真是好辛苦……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_263A")

    label("loc_25DA")


    #C0139
    ChrTalk(
        0xFE,
        (
            "镇长先生今天似乎也很累……\x01",
            "收购的交涉只好暂缓了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "……要到什么时候\x01",
            "才能回帝国呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_263A")

    Jump("loc_29A6")

    label("loc_263F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2765")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26F6")

    #C0141
    ChrTalk(
        0xFE,
        (
            "小姐的滞留资金……\x01",
            "好像是从家中的金库里\x01",
            "偷偷拿出来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "在这里待上一年都绰绰有余……\x01",
            "小姐是这样说的……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "呜呜，她到底\x01",
            "偷拿了多少米拉啊……！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2760")

    label("loc_26F6")


    #C0144
    ChrTalk(
        0xFE,
        (
            "可以供我们在此滞留一年的米拉，\x01",
            "外加两张往返列车票……\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "呜呜，家里现在\x01",
            "大概已经闹翻天了吧……！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2760")

    Jump("loc_29A6")

    label("loc_2765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_28A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2839")

    #C0146
    ChrTalk(
        0xFE,
        (
            "小姐是埃雷波尼亚帝国中\x01",
            "屈指可数的大商人的独生女。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "她希望自己将来\x01",
            "也能成为一个厉害的女商人，\x01",
            "所以就把我拖来这个自治州……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "唉，瞒着老爷离家出走，\x01",
            "回去以后一定会被\x01",
            "骂死的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_289B")

    label("loc_2839")


    #C0149
    ChrTalk(
        0xFE,
        (
            "总之，再不快点回去的话，\x01",
            "我百分之百会被解雇的。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "真希望能早点将七耀石的结晶\x01",
            "弄到手呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_289B")

    Jump("loc_29A6")

    label("loc_28A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_28AE")
    Jump("loc_29A6")

    label("loc_28AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_2925")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28C9")
    Call(0, 10)
    Jump("loc_2920")

    label("loc_28C9")


    #C0151
    ChrTalk(
        0xFE,
        (
            "呜呜……\x01",
            "得去取晚餐才行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "我笨手笨脚的……\x01",
            "真担心会不会\x01",
            "从楼梯上滚下来……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2920")

    Jump("loc_29A6")

    label("loc_2925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_29A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2940")
    Call(0, 10)
    Jump("loc_29A6")

    label("loc_2940")


    #C0153
    ChrTalk(
        0xFE,
        (
            "小姐和我\x01",
            "是从帝国来这里\x01",
            "收购七耀石的。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "可是，听说最近镇子周边\x01",
            "有魔兽出没，\x01",
            "真有点害怕呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29A6")

    TalkEnd(0xFE)
    Return()

    # Function_9_22CF end

    def Function_10_29AA(): pass

    label("Function_10_29AA")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    TurnDirection(0xB, 0xC, 0)
    TurnDirection(0xC, 0xB, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_2A7F")

    #C0155
    ChrTalk(
        0xB,
        (
            "哎呀，都这么晚了啊。\x01",
            "肚子饿了。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        (
            "莱缇娜，你去老板娘那里\x01",
            "拿晚餐来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xC,
        (
            "那、那个……\x01",
            "直接去上面的餐桌\x01",
            "吃不好吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xB,
        (
            "不好，太麻烦。\x01",
            "好啦，你快去。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xC,
        "呜呜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B61")

    label("loc_2A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2B61")

    #C0160
    ChrTalk(
        0xB,
        (
            "呵呵～\x01",
            "不愧是大陆首屈一指的\x01",
            "七耀石产地呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xC,
        (
            "是、是呀，小姐。\x01",
            "昨天也和比克森镇长\x01",
            "做了笔成功的交易……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xB,
        (
            "看这样子，\x01",
            "购买到七耀石的结晶\x01",
            "也只是时间问题了。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xB,
        (
            "嗯，虽然之前有点犹豫，\x01",
            "但我决定暂时留在这里了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B61")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_10_29AA end

    def Function_11_2B70(): pass

    label("Function_11_2B70")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2C04")
    Jump("loc_2C4E")

    label("loc_2C04")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2C24")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C4E")

    label("loc_2C24")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C44")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C4E")

    label("loc_2C44")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C4E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2E05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C8E")
    Call(0, 16)
    Jump("loc_2E05")

    label("loc_2C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DAC")

    #C0164
    ChrTalk(
        0xD,
        (
            "#0805F啊、罗伊德，是你们……\x02\x03",

            "#0809F啊哈哈……\x01",
            "我完全没注意到。\x01",
            "你们来工作吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x101,
        (
            "#0002F啊，是的，\x01",
            "差不多吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        (
            "#0108F（艾丝蒂尔……\x01",
            "  似乎在强颜欢笑呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x104,
        (
            "#0303F（嗯……\x01",
            "  的确有点令人在意……）\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x103,
        (
            "#0208F（……这是困惑……？\x01",
            "  还是深沉的哀伤……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2E05")

    label("loc_2DAC")


    #C0169
    ChrTalk(
        0xD,
        (
            "#0809F好、好了～！\x01",
            "稍微休息一下，就要赶快回市里啦！\x02\x03",

            "#0802F罗伊德，你们也要加油哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E05")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_2B70 end

    def Function_12_2E0D(): pass

    label("Function_12_2E0D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2EA1")
    Jump("loc_2EEB")

    label("loc_2EA1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2EC1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EEB")

    label("loc_2EC1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EE1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EEB")

    label("loc_2EE1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EEB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2F84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F2B")
    Call(0, 16)
    Jump("loc_2F84")

    label("loc_2F2B")


    #C0170
    ChrTalk(
        0xE,
        (
            "#0903F（抱歉，发生了一些事……）\x02\x03",

            "#0900F（现在能不能让艾丝蒂尔\x01",
            "  一个人静一静呢？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F84")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_2E0D end

    def Function_13_2F8C(): pass

    label("Function_13_2F8C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3020")
    Jump("loc_306A")

    label("loc_3020")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3040")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_306A")

    label("loc_3040")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3060")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_306A")

    label("loc_3060")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_306A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_31E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_316E")

    #C0171
    ChrTalk(
        0xFE,
        (
            "警察局的孩子们吗，\x01",
            "辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "那些黑手党的事\x01",
            "好像已经立案了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x103,
        (
            "#0200F……是鲁巴彻吧。\x01",
            "但只过了两天就被释放了……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        "哈哈，别那么沮丧啦。\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "就算是游击士，\x01",
            "也会经常碰到这种事的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_31E7")

    label("loc_316E")


    #C0176
    ChrTalk(
        0xFE,
        (
            "自从那次的魔兽事件以来，\x01",
            "我们在解决各地委托的时候，\x01",
            "都会顺便巡视一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "虽然更加忙碌了……\x01",
            "不过，这也是必要的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31E7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_2F8C end

    def Function_14_31EF(): pass

    label("Function_14_31EF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3283")
    Jump("loc_32CD")

    label("loc_3283")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_32A3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32CD")

    label("loc_32A3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32C3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32CD")

    label("loc_32C3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32CD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_341A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33B1")

    #C0178
    ChrTalk(
        0xFE,
        (
            "那起事件的解决……\x01",
            "就你们一贯的实力来说，算是干得漂亮了。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "不过，可不要骄傲哦。\x01",
            "要经常保持上进心，\x01",
            "不断进取。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#0003F（好像稍微\x01",
            "  认可我们了吧……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_341A")

    label("loc_33B1")


    #C0181
    ChrTalk(
        0xFE,
        (
            "成功往往会招致骄傲。\x01",
            "要是沉溺于自满中，\x01",
            "就无法获得下一次的成功。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "要经常保持上进心，\x01",
            "不断进取。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_341A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_31EF end

    def Function_15_3422(): pass

    label("Function_15_3422")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_34B6")
    Jump("loc_3500")

    label("loc_34B6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_34D6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3500")

    label("loc_34D6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34F6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3500")

    label("loc_34F6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3500")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A3")

    #C0183
    ChrTalk(
        0xFE,
        "（唠唠叨叨）……\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "呼～……\x01",
            "大白天的就一个人来酒馆，\x01",
            "真是太奢侈啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        "不过，只是喝杯冰茶而已啦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_35CB")

    label("loc_35A3")


    #C0186
    ChrTalk(
        0xFE,
        "（咕嘟咕嘟）……\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        "呼～好喝～！\x02",
    )

    CloseMessageWindow()

    label("loc_35CB")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_3422 end

    def Function_16_35D3(): pass

    label("Function_16_35D3")

    EventBegin(0x0)
    Fade(500)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    OP_68(-8200, 750, -3800, 0)
    MoveCamera(55, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x101, -6100, -750, -4050, 270)
    SetChrPos(0x102, -5950, -750, -5050, 270)
    SetChrPos(0x103, -5100, -750, -4050, 270)
    SetChrPos(0x104, -4950, -750, -5050, 270)
    OP_0D()

    #C0188
    ChrTalk(
        0xD,
        "#0808F#11P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xE,
        (
            "#0906F#12P看来，和我们调查的一样，\x01",
            "是一位相当正派的人呢。\x02\x03",

            "#0908F那孩子果然是误会了……\x01",
            "不，或许是钻进牛角尖了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xD,
        (
            "#0808F#11P……我明白……\x01",
            "那并不是那个人的错。\x02\x03",

            "当然，也绝对不是\x01",
            "那孩子的错……\x02\x03",

            "#0811F那个，约修亚……\x01",
            "我们……该怎么办才好？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xE,
        (
            "#0903F#12P……冷静点，艾丝蒂尔。\x01",
            "这并不是能够简单解决的问题。\x02\x03",

            "#0900F不要焦躁，要踏踏实实地努力尝试，\x01",
            "关于这点，在来之前不是就已经决定了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xD,
        "#0806F#11P……嗯。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x101,
        (
            "#0001F#11P（好像在谈什么\x01",
            "  严肃的话题啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -6100, -750, -4550, 270)
    SetScenarioFlags(0x94, 4)
    EventEnd(0x5)
    Return()

    # Function_16_35D3 end

    def Function_17_386E(): pass

    label("Function_17_386E")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(1000)
    OP_68(3040, 1500, 1600, 0)
    MoveCamera(30, 19, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34000, 0)
    SetChrPos(0x101, 2900, 0, 1900, 0)
    SetChrPos(0x102, 4100, 0, 1900, 0)
    SetChrPos(0x103, 2900, 0, 700, 0)
    SetChrPos(0x104, 4100, 0, 700, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0194
    ChrTalk(
        0x8,
        (
            "#1P呀，你们几个……\x01",
            "都已经是傍晚了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x8,
        (
            "#1P巴士的末班车是在八点左右，\x01",
            "不用去赶车吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x102,
        (
            "#0100F#2P没关系……我们今天\x01",
            "打算在这里住下。\x02\x03",

            "请问，还有带着桌子\x01",
            "的大房间空着吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x8,
        "#1P嗯，有啊。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "#1P呵呵，好开心啊。\x01",
            "像你们这样的年轻人\x01",
            "也会住我们这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x8,
        "#1P晚餐也在我们这里吃吗？\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        "#0000F#2P嗯，麻烦您了。\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x8,
        (
            "#1P好啊，那就让我大展身手，\x01",
            "给你们做点好吃的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x8,
        (
            "#1P房间在下楼之后左手边的最里面。\x01",
            "吃晚饭之前，先去休息休息吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x104,
        "#0300F#4P谢啦，阿姨。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x103,
        "#0200F#4P……打扰了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("t052B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_386E end

    SaveToFile()

Try(main)
