from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t1040.bin",                # FileName
        "t1040",                    # MapName
        "t1040",                    # Location
        0x0044,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 68, 0, 2, 0, 3],
    )

    BuildStringList((
        "t1040",                  # 0
        "雾香",                   # 1
        "鲁特",                   # 2
        "梅夏",                   # 3
        "男孩",                   # 4
        "男性",                   # 5
        "男性",                   # 6
        "女性",                   # 7
        "少女",                   # 8
        "青年",                   # 9
        "游客",                   # 10
        "老人",                   # 11
        "老妇人",                 # 12
        "薇娜",                   # 13
        "德罗娜",                 # 14
        "少女",                   # 15
        "青年",                   # 16
    ))

    AddCharChip((
        "chr/ch07302.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch34500.itc",                   # 02
        "chr/ch21302.itc",                   # 03
        "chr/ch21202.itc",                   # 04
        "chr/ch24602.itc",                   # 05
        "chr/ch24202.itc",                   # 06
        "chr/ch20202.itc",                   # 07
        "chr/ch20302.itc",                   # 08
        "chr/ch27900.itc",                   # 09
        "chr/ch26600.itc",                   # 0A
        "chr/ch21602.itc",                   # 0B
        "chr/ch33002.itc",                   # 0C
        "chr/ch21702.itc",                   # 0D
        "chr/ch21300.itc",                   # 0E
        "chr/ch21200.itc",                   # 0F
    ))

    DeclNpc(-97889,  100,     18979,   45,   469,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(-104069, 0,       2980,    90,   257,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-101099, 0,       5880,    90,   257,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-102949, 200,     10859,   225,  469,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-104839, 170,     9050,    45,   469,  0x0, 0,   6,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-93970,  150,     10840,   225,  469,  0x0, 0,   7,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-95839,  200,     9050,    45,   469,  0x0, 0,   8,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-104849, 100,     9100,    45,   469,  0x0, 0,   3,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-103000, 159,     10859,   225,  469,  0x0, 0,   4,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(-93940,  170,     10869,   225,  469,  0x0, 0,   11,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(-97919,  170,     19000,   45,   469,  0x0, 0,   12,  0,   255, 255, 0,   15,  255,  0)
    DeclNpc(-97930,  170,     20979,   135,  469,  0x0, 0,   13,  0,   255, 255, 0,   16,  255,  0)
    DeclNpc(-1860,   0,       10640,   180,  257,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-6250,   0,       6099,    180,  257,  0x0, 0,   10,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-6019,   0,       4829,    90,   385,  0x0, 0,   14,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-7389,   0,       3789,    45,   385,  0x0, 0,   15,  0,   0,   0,   0,   22,  255,  0)

    DeclActor(-1770,   0,       8810,    1000,    -1860,   1500,    10640,   0x007E, 0,  17, 0x0000)
    DeclActor(-101650, 0,       2470,    1000,    -104070, 1500,    2980,    0x007E, 0,  5,  0x0000)
    DeclActor(-102930, 0,       14990,   1200,    -102930, 800,     14990,   0x007C, 0,  33, 0x0000)

    ScpFunction((
        "Function_0_388",          # 00, 0
        "Function_1_440",          # 01, 1
        "Function_2_4C9",          # 02, 2
        "Function_3_591",          # 03, 3
        "Function_4_656",          # 04, 4
        "Function_5_87E",          # 05, 5
        "Function_6_882",          # 06, 6
        "Function_7_A96",          # 07, 7
        "Function_8_D55",          # 08, 8
        "Function_9_D97",          # 09, 9
        "Function_10_F5B",         # 0A, 10
        "Function_11_10DA",        # 0B, 11
        "Function_12_1206",        # 0C, 12
        "Function_13_13CC",        # 0D, 13
        "Function_14_15CC",        # 0E, 14
        "Function_15_17B3",        # 0F, 15
        "Function_16_192A",        # 10, 16
        "Function_17_1AA6",        # 11, 17
        "Function_18_1AAA",        # 12, 18
        "Function_19_1BD3",        # 13, 19
        "Function_20_1C0E",        # 14, 20
        "Function_21_1C5D",        # 15, 21
        "Function_22_1CE4",        # 16, 22
        "Function_23_1D38",        # 17, 23
        "Function_24_1D81",        # 18, 24
        "Function_25_2A8B",        # 19, 25
        "Function_26_2AE4",        # 1A, 26
        "Function_27_2B3D",        # 1B, 27
        "Function_28_2B96",        # 1C, 28
        "Function_29_2BEF",        # 1D, 29
        "Function_30_2C48",        # 1E, 30
        "Function_31_3443",        # 1F, 31
        "Function_32_3C97",        # 20, 32
        "Function_33_45CD",        # 21, 33
    ))


    def Function_0_388(): pass

    label("Function_0_388")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3C8"),
        (1, "loc_3D4"),
        (2, "loc_3E0"),
        (3, "loc_3EC"),
        (4, "loc_3F8"),
        (5, "loc_404"),
        (6, "loc_410"),
        (SWITCH_DEFAULT, "loc_41C"),
    )


    label("loc_3C8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3D4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3E0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3EC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3F8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_404")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_410")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_41C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_428")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_43F")

    Return()

    # Function_0_388 end

    def Function_1_440(): pass

    label("Function_1_440")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C8")
    OP_95(0xFE, -98090, 0, 5880, 2000, 0x0)
    OP_95(0xFE, -98090, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 5880, 2000, 0x0)
    Jump("Function_1_440")

    label("loc_4C8")

    Return()

    # Function_1_440 end

    def Function_2_4C9(): pass

    label("Function_2_4C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E3")
    Event(0, 24)

    label("loc_4E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_4F1")
    Jump("loc_58A")

    label("loc_4F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_4FF")
    Jump("loc_58A")

    label("loc_4FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_50D")
    Jump("loc_58A")

    label("loc_50D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_51B")
    Jump("loc_58A")

    label("loc_51B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_529")
    Jump("loc_58A")

    label("loc_529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_550")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_58A")

    label("loc_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_581")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_58A")

    label("loc_581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_58A")

    label("loc_58A")

    BeginChrThread(0xA, 0, 0, 1)
    Return()

    # Function_2_4C9 end

    def Function_3_591(): pass

    label("Function_3_591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C8")
    SetMapObjFrame(0xFF, "t1040_sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "t1040_sky_y", 0x1, 0x1)
    Jump("loc_5EC")

    label("loc_5C8")

    SetMapObjFrame(0xFF, "t1040_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1040_sky_y", 0x0, 0x1)

    label("loc_5EC")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_655")
    LoadEffect(0x0, "event\\eva00_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0x0, -102930, 800, 14990, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_655")

    Return()

    # Function_3_591 end

    def Function_4_656(): pass

    label("Function_4_656")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6EA")
    Jump("loc_734")

    label("loc_6EA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_70A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_734")

    label("loc_70A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_72A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_734")

    label("loc_72A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_734")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F9")
    SetChrSubChip(0xFE, 0x0)

    #C0001
    ChrTalk(
        0xFE,
        (
            "#3403F唔……\x01",
            "不愧是打着\x01",
            "高级西餐厅的名号。\x02\x03",

            "#3400F……只不过……\x02\x03",

            "#3404F（呵呵……\x01",
            "  还是麻绪婆婆那质朴的料理\x01",
            "  更加合我的口味呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_876")

    label("loc_7F9")


    #C0002
    ChrTalk(
        0xFE,
        (
            "#3405F……哎呀，你们\x01",
            "也是来用餐的吗？\x02\x03",

            "#3400F这里的食物虽然价格不菲，\x01",
            "但味道很值得称赞哦。\x01",
            "有兴趣的话，不如就点一些吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_876")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_4_656 end

    def Function_5_87E(): pass

    label("Function_5_87E")

    Call(0, 6)
    Return()

    # Function_5_87E end

    def Function_6_882(): pass

    label("Function_6_882")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_88F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A92")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8DF")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_8DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FF")
    OP_AF(0x66)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8D")

    label("loc_8FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_913")
    Jump("loc_A8D")

    label("loc_913")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_93A")
    Jump("loc_A8D")

    label("loc_93A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_948")
    Jump("loc_A8D")

    label("loc_948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_956")
    Jump("loc_A8D")

    label("loc_956")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_964")
    Jump("loc_A8D")

    label("loc_964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_972")
    Jump("loc_A8D")

    label("loc_972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_9E4")

    #C0003
    ChrTalk(
        0x9,
        (
            "太阳也落山了，\x01",
            "从米修拉姆回来的客人们\x01",
            "差不多要蜂涌而至了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            "得趁现在\x01",
            "为晚餐做好准备\x01",
            "才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8D")

    label("loc_9E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_A84")

    #C0005
    ChrTalk(
        0x9,
        (
            "欢迎，\x01",
            "欢迎光临『幸运』西餐厅。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x9,
        (
            "我倾注心血制作的料理，\x01",
            "还请您赏光品尝。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x9,
        (
            "用最高级食材烹制的料理，\x01",
            "一定能将客人们\x01",
            "引入幸福的漩涡吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8D")

    label("loc_A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_A8D")

    label("loc_A8D")

    Jump("loc_88F")

    label("loc_A92")

    TalkEnd(0x9)
    Return()

    # Function_6_882 end

    def Function_7_A96(): pass

    label("Function_7_A96")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_AA7")
    Jump("loc_D51")

    label("loc_AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_AB5")
    Jump("loc_D51")

    label("loc_AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_AC3")
    Jump("loc_D51")

    label("loc_AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_AD1")
    Jump("loc_D51")

    label("loc_AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_ADF")
    Jump("loc_D51")

    label("loc_ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_BF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8C")

    #C0008
    ChrTalk(
        0xFE,
        (
            "有个满身大汗的奇怪大叔\x01",
            "经常来这里吃午餐。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "我想他多半是\x01",
            "某个设施里的工作人员……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "……莫非是咪西里面的……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "……不不，当我没说。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_BF3")

    label("loc_B8C")


    #C0012
    ChrTalk(
        0xFE,
        (
            "有个满身大汗的奇怪大叔\x01",
            "经常来这里吃午餐。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "……莫非是咪西里面的……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "……不不，当我没说。\x02",
    )

    CloseMessageWindow()

    label("loc_BF3")

    Jump("loc_D51")

    label("loc_BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_D48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD5")

    #C0015
    ChrTalk(
        0xFE,
        (
            "那个东方长相的女性……\x01",
            "吃东西时的表情好像很严肃呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "……难不成，\x01",
            "是竞争对手派来的间谍吗……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "………………………………！\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "……但仔细一想，\x01",
            "这家店好像也没有\x01",
            "什么竞争对手呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_D43")

    label("loc_CD5")


    #C0019
    ChrTalk(
        0xFE,
        (
            "呵呵，仔细一想，\x01",
            "这家店好像也没有\x01",
            "什么竞争对手呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "把客人当成间谍，\x01",
            "真是太失礼了啊，\x01",
            "必须要反省呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D43")

    Jump("loc_D51")

    label("loc_D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_D51")

    label("loc_D51")

    TalkEnd(0xFE)
    Return()

    # Function_7_A96 end

    def Function_8_D55(): pass

    label("Function_8_D55")

    TalkBegin(0xFE)

    #C0021
    ChrTalk(
        0xFE,
        "（大口吃）……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "爸爸，快点吃完，\x01",
            "再回主题公园吧！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_D55 end

    def Function_9_D97(): pass

    label("Function_9_D97")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E2B")
    Jump("loc_E75")

    label("loc_E2B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E4B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E75")

    label("loc_E4B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E6B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E75")

    label("loc_E6B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E75")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1A")

    #C0023
    ChrTalk(
        0xFE,
        (
            "主题公园里\x01",
            "没有对我口味的店啦，\x01",
            "所以就先出来用餐了。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xB,
        "（大口吃）……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)

    #C0025
    ChrTalk(
        0xFE,
        "喂喂，吃饭时安静一点。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_F53")

    label("loc_F1A")

    SetChrSubChip(0xFE, 0x0)

    #C0026
    ChrTalk(
        0xFE,
        (
            "我知道你想去主题公园玩，\x01",
            "但是吃饭的时候要安静。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F53")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_D97 end

    def Function_10_F5B(): pass

    label("Function_10_F5B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FEF")
    Jump("loc_1039")

    label("loc_FEF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_100F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1039")

    label("loc_100F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_102F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1039")

    label("loc_102F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1039")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0027
    ChrTalk(
        0xFE,
        (
            "米修拉姆的开发\x01",
            "是由ＩＢＣ进行的，\x01",
            "这你知道吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "这家西餐厅似乎是ＩＢＣ\x01",
            "审查会评定的最优秀厨师\x01",
            "所开的店哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_F5B end

    def Function_11_10DA(): pass

    label("Function_11_10DA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_116E")
    Jump("loc_11B8")

    label("loc_116E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_118E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11B8")

    label("loc_118E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11AE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11B8")

    label("loc_11AE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11B8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0029
    ChrTalk(
        0xFE,
        (
            "嘿……这里的厨师\x01",
            "好厉害啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_10DA end

    def Function_12_1206(): pass

    label("Function_12_1206")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_129A")
    Jump("loc_12E4")

    label("loc_129A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12BA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12E4")

    label("loc_12BA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12DA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12E4")

    label("loc_12DA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12E4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1387")

    #C0030
    ChrTalk(
        0xFE,
        (
            "虽然买到了漂亮的裙子……\x01",
            "但珠宝店竟然拒绝新客人啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "真是的～气死我了！\x01",
            "既然如此，我就要吃个痛快！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_13C4")

    label("loc_1387")


    #C0032
    ChrTalk(
        0xFE,
        (
            "为了平息不让我进珠宝店的愤怒，\x01",
            "我要大吃大喝到满意为止！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13C4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_1206 end

    def Function_13_13CC(): pass

    label("Function_13_13CC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1460")
    Jump("loc_14AA")

    label("loc_1460")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1480")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14AA")

    label("loc_1480")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14A0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14AA")

    label("loc_14A0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14AA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_158E")

    #C0033
    ChrTalk(
        0xFE,
        (
            "说实话，不能进\x01",
            "珠宝店真是救了我一命。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "在精品店买了裙子之后，\x01",
            "如果再买什么宝石的话，\x01",
            "肯定要破产了。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "……但是，这个西餐厅的菜价\x01",
            "似乎也很贵啊。\x01",
            "……没问题吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_15C4")

    label("loc_158E")


    #C0036
    ChrTalk(
        0xFE,
        (
            "这个西餐厅的菜价\x01",
            "似乎也很贵啊。\x01",
            "……没问题吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_13CC end

    def Function_14_15CC(): pass

    label("Function_14_15CC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1660")
    Jump("loc_16AA")

    label("loc_1660")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1680")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16AA")

    label("loc_1680")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16A0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16AA")

    label("loc_16A0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16AA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175C")

    #C0037
    ChrTalk(
        0xFE,
        (
            "（大吃大嚼）……\x01",
            "唔唔，果然好味道！\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "从Ｂ级小吃到三星级\x01",
            "西餐厅全部吃遍的我\x01",
            "竟然也觉得美味……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        "唔，太出色了！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_17AB")

    label("loc_175C")


    #C0040
    ChrTalk(
        0xFE,
        (
            "不愧是高级疗养地的西餐厅……\x01",
            "竟然能让我也觉得美味呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        "唔，太出色了！\x02",
    )

    CloseMessageWindow()

    label("loc_17AB")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_15CC end

    def Function_15_17B3(): pass

    label("Function_15_17B3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1847")
    Jump("loc_1891")

    label("loc_1847")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1867")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1891")

    label("loc_1867")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1887")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1891")

    label("loc_1887")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1891")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0042
    ChrTalk(
        0xFE,
        (
            "今晚我要带妻子去参加\x01",
            "哈尔特曼议长举办的宴会。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "那可是很刺激的地方呢。\x01",
            "呵呵，真期待我妻子的反应啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_17B3 end

    def Function_16_192A(): pass

    label("Function_16_192A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_19BE")
    Jump("loc_1A08")

    label("loc_19BE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19DE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A08")

    label("loc_19DE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19FE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A08")

    label("loc_19FE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A08")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0044
    ChrTalk(
        0xFE,
        (
            "今天和我先生乘坐了\x01",
            "摩天轮等设施，玩得很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "不用乘坐激烈的游乐设施\x01",
            "就能有十二分的享受，\x01",
            "真是不错呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_192A end

    def Function_17_1AA6(): pass

    label("Function_17_1AA6")

    Call(0, 18)
    Return()

    # Function_17_1AA6 end

    def Function_18_1AAA(): pass

    label("Function_18_1AAA")

    TalkBegin(0x14)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1AB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BCF")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B07")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1B07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B27")
    OP_AF(0x69)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BCA")

    label("loc_1B27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B3B")
    Jump("loc_1BCA")

    label("loc_1B3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BCA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0046
    ChrTalk(
        0x14,
        (
            "精品店『柯赛利卡』\x01",
            "为您准备了从正装到休闲装\x01",
            "的各种服饰哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x14,
        (
            "愿意的话，也可以让服务员\x01",
            "为您来搭配\x01",
            "适合的服装。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BCA")

    Jump("loc_1AB7")

    label("loc_1BCF")

    TalkEnd(0x14)
    Return()

    # Function_18_1AAA end

    def Function_19_1BD3(): pass

    label("Function_19_1BD3")

    TalkBegin(0xFE)
    TurnDirection(0x15, 0x16, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BEF")
    Call(0, 21)
    Jump("loc_1C0A")

    label("loc_1BEF")


    #C0048
    ChrTalk(
        0xFE,
        (
            "呵呵……\x01",
            "很适合您哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C0A")

    TalkEnd(0xFE)
    Return()

    # Function_19_1BD3 end

    def Function_20_1C0E(): pass

    label("Function_20_1C0E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C2A")
    OP_93(0xFE, 0x5A, 0x0)
    Call(0, 21)
    Jump("loc_1C59")

    label("loc_1C2A")


    #C0049
    ChrTalk(
        0x16,
        (
            "嗯～这种清纯的感觉……\x01",
            "好像的确很适合我⊥\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C59")

    TalkEnd(0xFE)
    Return()

    # Function_20_1C0E end

    def Function_21_1C5D(): pass

    label("Function_21_1C5D")

    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    #C0050
    ChrTalk(
        0x15,
        (
            "客人，那套裙子……\x01",
            "非常适合您哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x16,
        (
            "呵呵，是这样吗？\x01",
            "那就决定了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x15,
        (
            "那么，就赶快\x01",
            "到里边来量尺寸吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_21_1C5D end

    def Function_22_1CE4(): pass

    label("Function_22_1CE4")

    TalkBegin(0xFE)

    #C0053
    ChrTalk(
        0xFE,
        (
            "才试穿了一下，\x01",
            "就打算买那么贵的东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        "……呜呜，我的存款……！！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_1CE4 end

    def Function_23_1D38(): pass

    label("Function_23_1D38")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0055
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x32A, 1)
    Return()

    # Function_23_1D38 end

    def Function_24_1D81(): pass

    label("Function_24_1D81")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 0, 0, -3000, 0)
    SetChrPos(0x102, 0, 0, -3000, 0)
    SetChrPos(0x103, 0, 0, -3000, 0)
    SetChrPos(0x104, 0, 0, -3000, 0)
    SetChrPos(0x151, 0, 0, -3000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x151, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x15, 1860, 0, 5910, 90)
    OP_68(-2760, 200, 3570, 0)
    MoveCamera(345, 14, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(21520, 0)
    FadeToBright(1000, 0)
    OP_68(-2760, 200, 5070, 7000)
    BeginChrThread(0x101, 3, 0, 25)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 26)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 27)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 28)
    Sleep(1000)
    BeginChrThread(0x151, 3, 0, 29)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x151, 3)
    OP_6F(0x1)
    OP_0D()

    #C0056
    ChrTalk(
        0x101,
        (
            "#0011F#12P嗯～……\x01",
            "话说，这家店的东西好像很贵啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#0304F#6P嗯，这就是所谓的\x01",
            "高级名品店吧。\x02\x03",

            "#0300F从正装\x01",
            "到漂亮的休闲服，\x01",
            "可谓是应有尽有啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x151,
        (
            "#5704F#6P呵呵……\x01",
            "但是相对地，价格也很高呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0059
    ChrTalk(
        0x102,
        (
            "#0100F#6P不用担心价格问题。\x02\x03",

            "那么，罗伊德……\x01",
            "你决定带谁去了吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1FCE():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FCE)
    Sleep(100)

    def lambda_1FDE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1FDE)

    def lambda_1FEB():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1FEB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x151, 1)
    Sleep(300)

    #C0060
    ChrTalk(
        0x101,
        "#0004F#11P──嗯。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【让艾莉同行】\x01",      # 0
            "【让缇欧同行】\x01",      # 1
            "【让兰迪同行】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2087"),
        (1, "loc_22C7"),
        (2, "loc_258E"),
        (SWITCH_DEFAULT, "loc_2A46"),
    )


    label("loc_2087")

    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA9, 1)
    OP_29(0x47, 0x1, 0x6)
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0061
    ChrTalk(
        0x101,
        (
            "#0000F#11P艾莉──\x01",
            "你可以一起来吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0062
    ChrTalk(
        0x102,
        (
            "#0104F#6P……嗯，好的。\x02\x03",

            "#0102F或许这也是\x01",
            "看起来最自然，\x01",
            "最容易混进去的组合吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#0002F#11P嗯，我就是这么想的。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x151,
        (
            "#5702F#6P呵呵，如果是你们的话，\x01",
            "扮装成一对普通的情侣\x01",
            "应该是最佳选择吧。\x02\x03",

            "#5703F活跃的资产家大小姐\x01",
            "带着平民出身的男朋友\x01",
            "参加倍受瞩目的宴会……\x02\x03",

            "#5700F这种感觉怎么样？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#0005F#11P原来如此……\x01",
            "似乎很有说服力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        (
            "#0106F#6P……我觉得\x01",
            "你应该生气才对。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        (
            "#0309F#6P哈哈，别管这么多了，\x01",
            "赶快搭配服装吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        (
            "#0202F#12P会变成什么样呢……\x01",
            "有点期待。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A46")

    label("loc_22C7")

    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA9, 2)
    OP_29(0x47, 0x1, 0x7)
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0069
    ChrTalk(
        0x101,
        (
            "#0000F#5P──缇欧，\x01",
            "你可以一起来吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0070
    ChrTalk(
        0x103,
        (
            "#0205F#12P……选我真的好吗？\x02\x03",

            "#0206F我虽然不是小孩子，\x01",
            "但是，那个……多少还是\x01",
            "有点显眼吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        (
            "#0004F#5P嗯，我明白。\x02\x03",

            "#0000F但反过来一想，\x01",
            "如果和缇欧在一起，\x01",
            "应该最不会被怀疑为警察吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x103,
        "#0205F#12P啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 500)
    Sleep(300)

    #C0073
    ChrTalk(
        0x151,
        (
            "#5702F#6P呵呵，像你这样的孩子，\x01",
            "我去年也在那里见过呢。\x02\x03",

            "#5704F来自边境小国，\x01",
            "不谙世事的贵族兄妹……\x02\x03",

            "#5700F这种设定不错吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2492():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2492)

    def lambda_249F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_249F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    Sleep(300)

    #C0074
    ChrTalk(
        0x101,
        "#0005F#11P原、原来如此……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        (
            "#0205F#11P我和罗伊德前辈\x01",
            "扮成兄妹吗……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2504():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2504)
    Sleep(50)

    def lambda_2514():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2514)
    Sleep(300)

    #C0076
    ChrTalk(
        0x102,
        (
            "#0109F#5P呵呵，虽然长得完全不像，\x01",
            "但应该也能扮出这种感觉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x104,
        (
            "#0302F#6P那好，就赶快\x01",
            "搭配服装吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A46")

    label("loc_258E")

    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA9, 3)
    OP_29(0x47, 0x1, 0x8)
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0078
    ChrTalk(
        0x101,
        (
            "#0000F#5P……兰迪，\x01",
            "你可以一起来吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0079
    ChrTalk(
        0x104,
        (
            "#0305F#6P我倒是无所谓啦……\x01",
            "不过，两个大男人一起去的话，不会很显眼吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        "#0006F#5P嗯，话虽如此……\x02",
    )

    CloseMessageWindow()

    def lambda_265C():
        OP_93(0xFE, 0x5A, 0xC8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_265C)

    def lambda_2669():
        OP_93(0xFE, 0x10E, 0xC8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2669)

    def lambda_2676():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2676)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sleep(500)

    #C0081
    ChrTalk(
        0x101,
        (
            "#0008F#5P（但会场里还有黑手党吧？\x01",
            "  带女孩子去的话，总有点……）\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x104,
        "#0300F#6P（嗯，那倒也是。）\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        (
            "#0111F#5P嗯……\x01",
            "你们在说什么悄悄话呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        (
            "#0211F#12P难道说……\x01",
            "你们不知不觉都已经发展成那种关系了？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)

    #C0085
    ChrTalk(
        0x101,
        "#0012F#5P当然没有。\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        (
            "#0309F#6P哎呀～如果你有那种想法，\x01",
            "我倒是随时都欢迎啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x151,
        (
            "#5702F#6P呵呵，两个男人的组合\x01",
            "倒也不是没见过哦。\x02\x03",

            "#5704F#6P年纪略大的损友邀请一本正经的\x01",
            "良家少爷去参加不良游乐活动……\x02\x03",

            "#5700F这种感觉如何？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_285A():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_285A)
    Sleep(50)

    def lambda_286A():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_286A)
    Sleep(50)

    def lambda_287A():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_287A)
    Sleep(50)

    def lambda_288A():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_288A)
    Sleep(300)

    #C0088
    ChrTalk(
        0x101,
        "#0005F#11P原来如此……\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x104,
        "#0302F#12P哈哈，的确有点像呢。\x02",
    )

    CloseMessageWindow()

    def lambda_28DA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_28DA)
    WaitChrThread(0x103, 1)
    Sleep(300)

    #C0090
    ChrTalk(
        0x102,
        (
            "#0105F#5P这样的话，兰迪应该\x01",
            "打扮得稍微张扬一点呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2926():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2926)
    WaitChrThread(0x102, 1)
    Sleep(300)

    #C0091
    ChrTalk(
        0x102,
        (
            "#0109F#5P反之，罗伊德就应该\x01",
            "体现出传统、清爽一点的感觉……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_297A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_297A)
    WaitChrThread(0x103, 1)

    #C0092
    ChrTalk(
        0x103,
        (
            "#0202F#12P机会难得，\x01",
            "可以多尝试一下呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_29EB():
        OP_93(0xFE, 0xB4, 0xC8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29EB)
    Sleep(300)

    #C0093
    ChrTalk(
        0x101,
        "#0011F#5P那个～……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0094
    ChrTalk(
        0x104,
        (
            "#0306F#6P好啦，老实地\x01",
            "当他们的换装人偶吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A46")

    SetCameraDistance(22020, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2A6D")
    Call(0, 30)
    Jump("loc_2A8A")

    label("loc_2A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2A7E")
    Call(0, 31)
    Jump("loc_2A8A")

    label("loc_2A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2A8A")
    Call(0, 32)

    label("loc_2A8A")

    Return()

    # Function_24_1D81 end

    def Function_25_2A8B(): pass

    label("Function_25_2A8B")


    def lambda_2A90():
        OP_95(0xFE, 0, 0, -1440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A90)

    def lambda_2AAA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2AAA)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2AC3():
        OP_95(0xFE, 0, 0, 2020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AC3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_25_2A8B end

    def Function_26_2AE4(): pass

    label("Function_26_2AE4")


    def lambda_2AE9():
        OP_95(0xFE, 0, 0, -1440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AE9)

    def lambda_2B03():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B03)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2B1C():
        OP_95(0xFE, -790, 0, 650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B1C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_26_2AE4 end

    def Function_27_2B3D(): pass

    label("Function_27_2B3D")


    def lambda_2B42():
        OP_95(0xFE, 0, 0, -1440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B42)

    def lambda_2B5C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B5C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2B75():
        OP_95(0xFE, 870, 0, 920, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B75)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_27_2B3D end

    def Function_28_2B96(): pass

    label("Function_28_2B96")


    def lambda_2B9B():
        OP_95(0xFE, 0, 0, -1440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B9B)

    def lambda_2BB5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2BB5)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2BCE():
        OP_95(0xFE, 0, 0, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BCE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_28_2B96 end

    def Function_29_2BEF(): pass

    label("Function_29_2BEF")


    def lambda_2BF4():
        OP_95(0xFE, -460, 0, -1690, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BF4)

    def lambda_2C0E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C0E)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2C27():
        OP_95(0xFE, -1630, 0, -530, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C27)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_29_2BEF end

    def Function_30_2C48(): pass

    label("Function_30_2C48")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08100.itc", 0x1E)
    SetChrChipPat(0x0, 0x1, 0x4C)
    LoadChrChipPat()
    SetChrChipPat(0x1, 0x1, 0x4D)
    LoadChrChipPat()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05000.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05300.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05100.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    SetChrPos(0x101, -7700, 0, 9950, 180)
    SetChrPos(0x102, -6350, 0, 9950, 180)
    SetChrPos(0x103, -6350, 0, 8150, 0)
    SetChrPos(0x104, -7000, 0, 6850, 0)
    SetChrPos(0x151, -7700, 0, 8150, 0)
    FadeToBright(1000, 0)
    OP_68(-7640, 900, 9240, 0)
    MoveCamera(311, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetCameraDistance(23000, 2500)
    OP_6F(0x10)
    OP_0D()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0095
    AnonymousTalk(
        0x102,
        "呵呵，久等了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0096
    AnonymousTalk(
        0x101,
        "姑且穿上试了试……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0097
    ChrTalk(
        0x104,
        (
            "#0305F#6P嘿……不错嘛。\x02\x03",

            "#0309F不愧是经常穿正装的人，\x01",
            "大小姐穿上晚礼服，真是无可挑剔啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x103,
        (
            "#0204F#6P是呀……非常漂亮。\x02\x03",

            "#0202F罗伊德前辈的打扮\x01",
            "也很合适。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        (
            "#5005F#11P是、是吗……？\x02\x03",

            "#5006F我倒觉得，站在艾莉身边，\x01",
            "总有点配不上她的感觉……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    #C0100
    ChrTalk(
        0x102,
        (
            "#5304F#12P呵呵，没有那回事啦。\x02\x03",

            "#5302F你的肩膀挺宽的，\x01",
            "很适合穿西装哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0101
    ChrTalk(
        0x101,
        (
            "#5004F#5P哈哈，谢谢。\x02\x03",

            "#5000F要是看起来能像是艾莉\x01",
            "的男朋友就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#5313F#12P那个……\x01",
            "我觉得应该很像啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x151,
        (
            "#5704F#6P呵呵，看样子，也不需要\x01",
            "多余的建议了呢。\x02\x03",

            "#5702F对了，顺便\x01",
            "把这个也带去吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_30C0():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30C0)

    def lambda_30CD():

        label("loc_30CD")

        TurnDirection(0x102, 0x101, 200)
        Yield()
        Jump("loc_30CD")

    QueueWorkItem2(0x102, 1, lambda_30CD)

    def lambda_30DF():

        label("loc_30DF")

        TurnDirection(0x103, 0x101, 200)
        Yield()
        Jump("loc_30DF")

    QueueWorkItem2(0x103, 1, lambda_30DF)

    def lambda_30F1():

        label("loc_30F1")

        TurnDirection(0x104, 0x101, 200)
        Yield()
        Jump("loc_30F1")

    QueueWorkItem2(0x104, 1, lambda_30F1)

    def lambda_3103():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3103)
    WaitChrThread(0x151, 1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    Call(0, 23)

    #C0104
    ChrTalk(
        0x101,
        "#5005F#11P这是……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x151,
        (
            "#5703F#6P女性穿上晚礼服之后，\x01",
            "感觉就会有很大的改变……\x02\x03",

            "#5700F但你就算穿了正装，\x01",
            "气质也没有太大的变化嘛。\x02\x03",

            "至少在会场内的时候，\x01",
            "还是戴上这个为好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        "#5000F#11P原来如此……谢啦。\x02",
    )

    CloseMessageWindow()

    def lambda_31FF():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_31FF)
    WaitChrThread(0x151, 1)
    Sleep(300)
    Fade(1000)
    Sound(820, 0, 100, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sound(882, 0, 100, 0)
    Sleep(500)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0107
    AnonymousTalk(
        0x101,
        "……怎么样？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)

    #C0108
    ChrTalk(
        0x151,
        "#5702F#6P哦……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x102,
        (
            "#5302F#12P真令人惊讶……\x01",
            "感觉变化好大呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        "#0202F#6P而且意外地很合适。\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x104,
        (
            "#0309F#6P哈哈，不然你以后就转换风格，\x01",
            "当个眼镜男怎么样？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        "#5106F#11P还是不要了，我的视力又不差。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(500)

    #C0113
    ChrTalk(
        0x101,
        (
            "#5004F#11P──好。\x01",
            "这样的话，就算是准备就绪了吧。\x02\x03",

            "#5000F接下来就只剩等待\x01",
            "『竞拍会』开场了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(2000)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("e3110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_2C48 end

    def Function_31_3443(): pass

    label("Function_31_3443")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08100.itc", 0x1E)
    SetChrChipPat(0x0, 0x1, 0x4C)
    LoadChrChipPat()
    SetChrChipPat(0x2, 0x1, 0x4E)
    LoadChrChipPat()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05000.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05400.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05100.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    SetChrPos(0x101, -7700, 0, 9950, 180)
    SetChrPos(0x102, -6350, 0, 8150, 0)
    SetChrPos(0x103, -6350, 0, 9950, 180)
    SetChrPos(0x104, -7000, 0, 6850, 0)
    SetChrPos(0x151, -7700, 0, 8150, 0)
    FadeToBright(1000, 0)
    OP_68(-7640, 900, 9240, 0)
    MoveCamera(311, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetCameraDistance(23000, 2500)
    OP_6F(0x10)
    OP_0D()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0114
    AnonymousTalk(
        0x101,
        "嗯，换好了，大概就是这样吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0115
    AnonymousTalk(
        0x103,
        (
            "……不知道\x01",
            "合不合身……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0116
    ChrTalk(
        0x102,
        (
            "#0109F#6P哎呀，很不错嘛！\x02\x03",

            "#0102F虽然罗伊德的打扮也很合身，\x01",
            "但还是缇欧的更合适，真是超级可爱啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x104,
        (
            "#0304F#6P嗯，因为几乎都没见过\x01",
            "阿缇穿战斗装以外的样子啊。\x02\x03",

            "#0300F这种打扮，感觉还真新鲜啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x103,
        "#5405F#11P是、是这样吗……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    #C0119
    ChrTalk(
        0x101,
        (
            "#5002F#5P嗯，真的很适合你呢。\x02\x03",

            "#5004F这样的话，说是兄妹\x01",
            "好像就很不协调了。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x151,
        (
            "#5702F#6P既然如此，那就改成跟随大小姐的\x01",
            "年轻管家，这个设定怎么样？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x151, 400)

    #C0121
    ChrTalk(
        0x101,
        "#5000F#11P这个不错……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    #C0122
    ChrTalk(
        0x103,
        (
            "#5403F#12P……不，兄妹就好。\x02\x03",

            "#5402F我也没有大小姐的气质。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0123
    ChrTalk(
        0x101,
        "#5005F#5P是、是吗……？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x151,
        (
            "#5704F#6P呵呵，你似乎\x01",
            "也有不少坚持呢。\x02\x03",

            "#5702F也罢，顺便\x01",
            "把这个也带去吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3912():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3912)

    def lambda_391F():

        label("loc_391F")

        TurnDirection(0x102, 0x101, 200)
        Yield()
        Jump("loc_391F")

    QueueWorkItem2(0x102, 1, lambda_391F)

    def lambda_3931():

        label("loc_3931")

        TurnDirection(0x103, 0x101, 200)
        Yield()
        Jump("loc_3931")

    QueueWorkItem2(0x103, 1, lambda_3931)

    def lambda_3943():

        label("loc_3943")

        TurnDirection(0x104, 0x101, 200)
        Yield()
        Jump("loc_3943")

    QueueWorkItem2(0x104, 1, lambda_3943)

    def lambda_3955():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3955)
    WaitChrThread(0x151, 1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    Call(0, 23)

    #C0125
    ChrTalk(
        0x101,
        "#5005F#11P这是……\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x151,
        (
            "#5703F#6P女孩子穿上晚礼服之后，\x01",
            "感觉就会有很大的改变……\x02\x03",

            "#5700F但你就算穿了正装，\x01",
            "气质也没有太大的变化嘛。\x02\x03",

            "至少在会场内的时候，\x01",
            "还是戴上这个为好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        "#5000F#11P原来如此……谢啦。\x02",
    )

    CloseMessageWindow()

    def lambda_3A53():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3A53)
    WaitChrThread(0x151, 1)
    Sleep(300)
    Fade(1000)
    Sound(820, 0, 100, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sound(882, 0, 100, 0)
    Sleep(500)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0128
    AnonymousTalk(
        0x101,
        "……怎么样？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)

    #C0129
    ChrTalk(
        0x151,
        "#5702F#6P哦……\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x102,
        (
            "#0102F#6P真令人惊讶……\x01",
            "感觉变化好大呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x103,
        "#5402F#12P而且意外地很合适。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x104,
        (
            "#0309F#6P哈哈，不然你以后就转换风格，\x01",
            "当个眼镜男怎么样？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        "#5106F#11P还是不要了，我的视力又不差。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(500)

    #C0134
    ChrTalk(
        0x101,
        (
            "#5004F#11P──好。\x01",
            "这样的话，就算是准备就绪了吧。\x02\x03",

            "#5000F接下来就只剩等待\x01",
            "『竞拍会』开场了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(2000)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("e3110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_3443 end

    def Function_32_3C97(): pass

    label("Function_32_3C97")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08100.itc", 0x1E)
    SetChrChipPat(0x0, 0x1, 0x4C)
    LoadChrChipPat()
    SetChrChipPat(0x3, 0x1, 0x4F)
    LoadChrChipPat()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05000.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05600.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05100.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    SetChrPos(0x101, -7700, 0, 9950, 180)
    SetChrPos(0x102, -7000, 0, 6850, 0)
    SetChrPos(0x103, -6350, 0, 8150, 0)
    SetChrPos(0x104, -6350, 0, 9950, 180)
    SetChrPos(0x151, -7700, 0, 8150, 0)
    FadeToBright(1000, 0)
    OP_68(-7640, 900, 9240, 0)
    MoveCamera(311, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetCameraDistance(23000, 2500)
    OP_6F(0x10)
    OP_0D()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0135
    AnonymousTalk(
        0x101,
        "──久等了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0136
    AnonymousTalk(
        0x104,
        "嗯，也就这样了吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0137
    ChrTalk(
        0x102,
        "#0105F#6P哎呀……\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x103,
        "#0201F#6P……唔……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0139
    ChrTalk(
        0x101,
        (
            "#5011F#11P那个……\x01",
            "果然不合适吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x104,
        (
            "#5605F#11P我个人倒是\x01",
            "觉得还挺帅的。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x102,
        (
            "#0102F#6P不不，你们两个的打扮\x01",
            "都非常合适呢。\x02\x03",

            "#0109F呵呵，感觉真是和\x01",
            "刚才的设定完全一样啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x103,
        (
            "#0204F#6P年纪略大的损友邀请一本正经的\x01",
            "良家少爷去参加不良游乐活动……\x02\x03",

            "#0202F的确就是这种感觉呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    #C0143
    ChrTalk(
        0x101,
        "#5005F#5P是、是吗……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    #C0144
    ChrTalk(
        0x104,
        (
            "#5609F#12P哈哈，那我就遵照你们的期待，\x01",
            "带他去参加些不良活动吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x102,
        (
            "#0107F#6P那、那可不行！\x02\x03",

            "#0111F这个人原本就有点\x01",
            "品性恶劣……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x103,
        (
            "#0211F#6P要是再染上什么不良嗜好，\x01",
            "恐怕就更加无可救药了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x104,
        "#5603F#12P原来如此……的确很危险啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0148
    ChrTalk(
        0x101,
        (
            "#5011F#5P──请等一下。\x02\x03",

            "#5013F我感觉自己好像被人强加了\x01",
            "一些极其没道理的评价……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x151,
        (
            "#5709F#6P呵呵，看来你还真是\x01",
            "受人宠爱呢。\x02\x03",

            "#5702F对了对了，顺便\x01",
            "把这个也带去吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4243():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4243)

    def lambda_4250():

        label("loc_4250")

        TurnDirection(0x102, 0x101, 200)
        Yield()
        Jump("loc_4250")

    QueueWorkItem2(0x102, 1, lambda_4250)

    def lambda_4262():

        label("loc_4262")

        TurnDirection(0x103, 0x101, 200)
        Yield()
        Jump("loc_4262")

    QueueWorkItem2(0x103, 1, lambda_4262)

    def lambda_4274():

        label("loc_4274")

        TurnDirection(0x104, 0x101, 200)
        Yield()
        Jump("loc_4274")

    QueueWorkItem2(0x104, 1, lambda_4274)

    def lambda_4286():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4286)
    WaitChrThread(0x151, 1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    Call(0, 23)

    #C0150
    ChrTalk(
        0x101,
        "#5005F#11P这是……\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x151,
        (
            "#5703F#6P兰迪换上了这套华丽的装扮之后，\x01",
            "感觉一下就改变了很多……\x02\x03",

            "#5700F但你就算穿了正装，\x01",
            "气质也没有太大的变化嘛。\x02\x03",

            "至少在会场内的时候，\x01",
            "还是戴上这个好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        "#5000F#11P原来如此……谢啦。\x02",
    )

    CloseMessageWindow()

    def lambda_438A():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_438A)
    WaitChrThread(0x151, 1)
    Sleep(300)
    Fade(1000)
    Sound(820, 0, 100, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sound(882, 0, 100, 0)
    Sleep(500)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0153
    AnonymousTalk(
        0x101,
        "……怎么样？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)

    #C0154
    ChrTalk(
        0x151,
        "#5702F#6P哦……\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x102,
        (
            "#0102F#6P真令人惊讶……\x01",
            "感觉变化好大呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x103,
        "#0202F#6P而且意外地很合适。\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x104,
        (
            "#5609F#12P哈哈，不然你以后就转换风格，\x01",
            "当个眼镜男怎么样？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        "#5106F#5P还是不要了，我的视力又不差。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(500)

    #C0159
    ChrTalk(
        0x101,
        (
            "#5004F#11P──好。\x01",
            "这样的话，就算是准备就绪了吧。\x02\x03",

            "#5000F接下来就只剩等待\x01",
            "『竞拍会』开场了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(2000)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("e3110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_3C97 end

    def Function_33_45CD(): pass

    label("Function_33_45CD")

    EventBegin(0x0)
    Fade(500)
    OP_68(-102630, 1400, 14570, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21880, 0)
    SetChrPos(0x101, -101580, 0, 14400, 270)
    SetChrPos(0x102, -101560, 0, 15620, 225)
    SetChrPos(0x103, -101840, 0, 13530, 315)
    SetChrPos(0x104, -100390, 0, 14710, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_4660")
    SetChrPos(0x151, -100780, 0, 13600, 270)

    label("loc_4660")

    StopEffect(0x0, 0x2)
    SetChrFlags(0xA, 0x80)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0160
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '冲浪板'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('冲浪板', 1)

    #C0161
    ChrTalk(
        0x101,
        "#11P#0005F在这种地方竟然有戒指……？\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x103,
        (
            "#6P#0200F有可能是托马先生\x01",
            "说的订婚戒指。\x02\x03",

            "稍后去他在酒店里的房间\x01",
            "确认一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x24, 0x1, 0x5)
    OP_65(0x2, 0x1)
    SetChrPos(0x0, -101580, 0, 14400, 270)
    ClearChrFlags(0xA, 0x80)
    EventEnd(0x5)
    Return()

    # Function_33_45CD end

    SaveToFile()

Try(main)
