from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0150.bin",                # FileName
        "c0150",                    # MapName
        "c0150",                    # Location
        0x0007,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 7, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0150",                  # 0
        "霍伊斯托夫",             # 1
        "布拉温",                 # 2
        "赛尔缇欧",               # 3
        "侬诺",                   # 4
        "阿奈斯特秘书",           # 5
        "格蕾丝",                 # 6
        "弗罗缇",                 # 7
        "金德尔",                 # 8
        "商务人士",               # 9
        "商务人士",               # 10
        "游客",                   # 11
        "市民",                   # 12
        "市民",                   # 13
        "市民",                   # 14
        "游客",                   # 15
        "游客",                   # 16
        "游客",                   # 17
        "游客",                   # 18
        "介绍人",                 # 19
        "青年",                   # 20
        "女性",                   # 21
        "游客",                   # 22
        "游客",                   # 23
        "游客",                   # 24
        "基隆德",                 # 25
        "多诺邦警督",             # 26
        "雷蒙德搜查官",           # 27
        "罗伯兹主任",             # 28
        "芙兰",                   # 29
    ))

    AddCharChip((
        "chr/ch25200.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch25100.itc",                   # 02
        "chr/ch25600.itc",                   # 03
        "chr/ch21302.itc",                   # 04
        "chr/ch27600.itc",                   # 05
        "chr/ch20402.itc",                   # 06
        "chr/ch32302.itc",                   # 07
        "chr/ch33202.itc",                   # 08
        "chr/ch21002.itc",                   # 09
        "chr/ch22002.itc",                   # 0A
        "chr/ch20502.itc",                   # 0B
        "chr/ch24102.itc",                   # 0C
        "chr/ch21202.itc",                   # 0D
        "chr/ch24502.itc",                   # 0E
        "chr/ch23702.itc",                   # 0F
        "chr/ch21802.itc",                   # 10
        "chr/ch20200.itc",                   # 11
        "chr/ch27602.itc",                   # 12
        "chr/ch02302.itc",                   # 13
        "chr/ch30300.itc",                   # 14
        "chr/ch30200.itc",                   # 15
        "chr/ch06002.itc",                   # 16
        "chr/ch29300.itc",                   # 17
        "chr/ch34302.itc",                   # 18
    ))

    DeclNpc(-509,    0,       12449,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-42889,  0,       5699,    0,    261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-52029,  0,       3650,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-8880,   0,       3240,    45,   261,  0x0, 0,   3,   0,   0,   1,   0,   13,  255,  0)
    DeclNpc(-3250,   150,     4570,    180,  469,  0x0, 0,   19,  0,   255, 255, 0,   15,  255,  0)
    DeclNpc(-3299,   0,       4480,    180,  469,  0x0, 0,   22,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(-7449,   150,     8510,    270,  341,  0x0, 0,   24,  0,   255, 255, 0,   16,  255,  0)
    DeclNpc(2450,    5150,    17559,   180,  469,  0x0, 0,   16,  0,   255, 255, 0,   17,  255,  0)
    DeclNpc(8739,    5000,    14520,   270,  389,  0x0, 0,   5,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(2450,    5150,    13479,   0,    469,  0x0, 0,   18,  0,   255, 255, 0,   17,  255,  0)
    DeclNpc(4559,    150,     5920,    180,  469,  0x0, 0,   6,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(5519,    150,     -3880,   270,  469,  0x0, 0,   7,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(3259,    150,     -6150,   0,    469,  0x0, 0,   8,   0,   255, 255, 0,   21,  255,  0)
    DeclNpc(1009,    150,     -3920,   90,   469,  0x0, 0,   12,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(1009,    129,     -3920,   90,   469,  0x0, 0,   9,   0,   255, 255, 0,   23,  255,  0)
    DeclNpc(3259,    150,     -1799,   180,  469,  0x0, 0,   6,   0,   255, 255, 0,   24,  255,  0)
    DeclNpc(6400,    5150,    13449,   0,    469,  0x0, 0,   10,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(6400,    5150,    17700,   180,  469,  0x0, 0,   11,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(1009,    100,     -3920,   90,   469,  0x0, 0,   13,  0,   255, 255, 0,   28,  255,  0)
    DeclNpc(5519,    150,     -3880,   270,  469,  0x0, 0,   6,   0,   255, 255, 0,   29,  255,  0)
    DeclNpc(3259,    150,     -1799,   180,  469,  0x0, 0,   4,   0,   255, 255, 0,   29,  255,  0)
    DeclNpc(3210,    150,     -1879,   180,  469,  0x0, 0,   15,  0,   255, 255, 0,   30,  255,  0)
    DeclNpc(3210,    150,     -6130,   0,    469,  0x0, 0,   14,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(-1159,   150,     2180,    270,  469,  0x0, 0,   7,   0,   255, 255, 0,   32,  255,  0)
    DeclNpc(60580,   -1000,   -8600,   270,  261,  0x0, 0,   17,  0,   0,   0,   0,   5,   255,  0)
    DeclNpc(56610,   -1000,   -11899,  270,  405,  0x0, 0,   20,  0,   0,   0,   0,   6,   255,  0)
    DeclNpc(55229,   -1000,   -11899,  90,   405,  0x0, 0,   21,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(57790,   -1000,   -12300,  90,   405,  0x0, 0,   23,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(59140,   -1000,   -8880,   1500,    60580,   500,     -8600,   0x007E, 0,  4,  0x0000)
    DeclActor(-510,    0,       10640,   1000,    -510,    1500,    12450,   0x007E, 0,  8,  0x0000)

    ScpFunction((
        "Function_0_518",          # 00, 0
        "Function_1_5D0",          # 01, 1
        "Function_2_66D",          # 02, 2
        "Function_3_8B5",          # 03, 3
        "Function_4_8E9",          # 04, 4
        "Function_5_8ED",          # 05, 5
        "Function_6_208B",         # 06, 6
        "Function_7_25F6",         # 07, 7
        "Function_8_26C3",         # 08, 8
        "Function_9_26C7",         # 09, 9
        "Function_10_3020",        # 0A, 10
        "Function_11_3CBC",        # 0B, 11
        "Function_12_3F32",        # 0C, 12
        "Function_13_4B23",        # 0D, 13
        "Function_14_5396",        # 0E, 14
        "Function_15_542D",        # 0F, 15
        "Function_16_570A",        # 10, 16
        "Function_17_6619",        # 11, 17
        "Function_18_68B3",        # 12, 18
        "Function_19_69F8",        # 13, 19
        "Function_20_6BDB",        # 14, 20
        "Function_21_6DAD",        # 15, 21
        "Function_22_6F8F",        # 16, 22
        "Function_23_70E6",        # 17, 23
        "Function_24_7320",        # 18, 24
        "Function_25_754F",        # 19, 25
        "Function_26_764D",        # 1A, 26
        "Function_27_791C",        # 1B, 27
        "Function_28_7BEC",        # 1C, 28
        "Function_29_8223",        # 1D, 29
        "Function_30_86AB",        # 1E, 30
        "Function_31_88F6",        # 1F, 31
        "Function_32_8AD7",        # 20, 32
        "Function_33_8C70",        # 21, 33
        "Function_34_8C7A",        # 22, 34
        "Function_35_8EFE",        # 23, 35
        "Function_36_924B",        # 24, 36
        "Function_37_96A9",        # 25, 37
        "Function_38_CD1C",        # 26, 38
        "Function_39_D54F",        # 27, 39
        "Function_40_E15B",        # 28, 40
        "Function_41_E3BE",        # 29, 41
        "Function_42_EA52",        # 2A, 42
    ))


    def Function_0_518(): pass

    label("Function_0_518")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_558"),
        (1, "loc_564"),
        (2, "loc_570"),
        (3, "loc_57C"),
        (4, "loc_588"),
        (5, "loc_594"),
        (6, "loc_5A0"),
        (SWITCH_DEFAULT, "loc_5AC"),
    )


    label("loc_558")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_564")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_570")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_57C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_588")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_594")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_5A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_5AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_5B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5CF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_5CF")

    Return()

    # Function_0_518 end

    def Function_1_5D0(): pass

    label("Function_1_5D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_66C")
    OP_95(0xFE, -4260, 0, 8920, 2000, 0x0)
    OP_95(0xFE, 720, 0, 6870, 2000, 0x0)
    OP_95(0xFE, 780, 0, 1070, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -2090, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -6010, 2000, 0x0)
    OP_95(0xFE, 3280, 0, -8790, 2000, 0x0)
    OP_95(0xFE, -8880, 0, 3240, 2000, 0x0)
    Jump("Function_1_5D0")

    label("loc_66C")

    Return()

    # Function_1_5D0 end

    def Function_2_66D(): pass

    label("Function_2_66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_67C")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 37)

    label("loc_67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6A6")
    SetChrPos(0xB, -7600, 0, 6990, 0)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_8B4")

    label("loc_6A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6B9")
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_8B4")

    label("loc_6B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6D1")
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_8B4")

    label("loc_6D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_6DF")
    Jump("loc_8B4")

    label("loc_6DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6FC")
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x23, 0x80)
    Jump("loc_8B4")

    label("loc_6FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_70A")
    Jump("loc_8B4")

    label("loc_70A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_74C")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrSubChip(0xD, 0x1)
    SetChrPos(0xB, -1730, 0, 4050, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xB, 0x10)
    Jump("loc_8B4")

    label("loc_74C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_777")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_772")
    ClearChrFlags(0xC, 0x80)

    label("loc_772")

    Jump("loc_8B4")

    label("loc_777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_7BC")
    SetChrPos(0xA, 6790, 0, 13090, 180)
    SetChrPos(0xB, 6790, 0, 11430, 0)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jump("loc_8B4")

    label("loc_7BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7E3")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    Jump("loc_8B4")

    label("loc_7E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_800")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jump("loc_8B4")

    label("loc_800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_82C")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_8B4")

    label("loc_82C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_84E")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_8B4")

    label("loc_84E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_870")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_8B4")

    label("loc_870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_897")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_8B4")

    label("loc_897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_8B4")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)

    label("loc_8B4")

    Return()

    # Function_2_66D end

    def Function_3_8B5(): pass

    label("Function_3_8B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D1")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_8E8")

    label("loc_8D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8E8")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_8E8")

    label("loc_8E8")

    Return()

    # Function_3_8B5 end

    def Function_4_8E9(): pass

    label("Function_4_8E9")

    Call(0, 5)
    Return()

    # Function_4_8E9 end

    def Function_5_8ED(): pass

    label("Function_5_8ED")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A98")

    #C0001
    ChrTalk(
        0x20,
        (
            "嘿，欢迎光临。\x01",
            "虽然我是想这么说……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x20,
        (
            "可是，小鬼们，在克洛斯贝尔，\x01",
            "没有许可证是不能购买武器的啊。\x01",
            "如果只是来闲逛的话，还是赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#0000F啊，其实我们是\x01",
            "克洛斯贝尔警察局的人……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0004
    ChrTalk(
        0x20,
        "像你们这种小孩子会是警察……？\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x20,
        (
            "对了，你们就是赛尔盖那家伙\x01",
            "之前说过的……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x20,
        (
            "哼，我明白了。\x01",
            "你们随便看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x20,
        (
            "要买武器的时候，\x01",
            "记得拿调查手册给我看啊。\x01",
            "那个可以用来代替许可证。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4C, 2)

    label("loc_A98")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2087")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF2")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_AF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B11")
    OP_AF(0x5)
    Jump("loc_B53")

    label("loc_B11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_B21")
    OP_AF(0x4)
    Jump("loc_B53")

    label("loc_B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_B31")
    OP_AF(0x3)
    Jump("loc_B53")

    label("loc_B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_B41")
    OP_AF(0x2)
    Jump("loc_B53")

    label("loc_B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_B51")
    OP_AF(0x1)
    Jump("loc_B53")

    label("loc_B51")

    OP_AF(0x0)

    label("loc_B53")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2082")

    label("loc_B62")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B76")
    Jump("loc_2082")

    label("loc_B76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2082")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 36)
    Jump("loc_2082")

    label("loc_BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_D16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCE")

    #C0008
    ChrTalk(
        0x20,
        (
            "嘿，欢迎光临，\x01",
            "虽然我是想这么说……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x20,
        (
            "但已经快到打烊时间了，\x01",
            "要买东西就抓紧时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x104,
        (
            "#0300F店主大叔还是老样子，\x01",
            "没什么做生意的干劲啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x20,
        "没错，我可是一点干劲都没啊。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x20,
        (
            "说来……空港那边\x01",
            "好像发生什么事件了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x20,
        "最近总感觉有些不太平呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D11")

    label("loc_CCE")


    #C0014
    ChrTalk(
        0x20,
        (
            "空港那边好像\x01",
            "发生什么事件了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x20,
        "最近总感觉有些不太平呢。\x02",
    )

    CloseMessageWindow()

    label("loc_D11")

    Jump("loc_2082")

    label("loc_D16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_E9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E44")

    #C0016
    ChrTalk(
        0x20,
        "……这不是达德利嘛。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x20,
        (
            "居然和支援科一起行动，还真是稀奇啊。\x01",
            "难道是岁月不饶人，连你也需要帮手了？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x10A,
        (
            "#0603F这种话我可不能假装没听见啊，店主。\x02\x03",

            "#0600F我并不是和这帮家伙一起行动，\x01",
            "而是在率领他们进行案件调查！\x02\x03",

            "……另外，这件事可\x01",
            "不要随意外传啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x20,
        "是是，我知道啦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E98")

    label("loc_E44")


    #C0020
    ChrTalk(
        0x20,
        (
            "不过，一科的王牌警官\x01",
            "居然在和支援科一起行动啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x20,
        (
            "这也真是稀奇\x01",
            "的组合了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E98")

    Jump("loc_2082")

    label("loc_E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_FC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F74")

    #C0022
    ChrTalk(
        0x20,
        (
            "怎么……一大早的\x01",
            "就来买武器啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x20,
        "真是一帮不懂享受生活的家伙。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x20,
        (
            "要选武器的话，\x01",
            "下午再来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        (
            "#0200F店主大叔其实\x01",
            "只是想过得悠闲些吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x20,
        (
            "哈，一语中的，\x01",
            "就是这么回事啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FBF")

    label("loc_F74")


    #C0027
    ChrTalk(
        0x20,
        (
            "我上午就想看看杂志，\x01",
            "轻松悠闲地度过。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x20,
        "所以你们尽量别来打扰我啊。\x02",
    )

    CloseMessageWindow()

    label("loc_FBF")

    Jump("loc_2082")

    label("loc_FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1094")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1064")

    #C0029
    ChrTalk(
        0x20,
        (
            "嘿，欢迎光临。\x01",
            "想要看点什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x20,
        (
            "我可懒得卖东西，\x01",
            "你们自己随便看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        (
            "#0100F啊，还是和往日一样，\x01",
            "没有做生意的干劲呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_108F")

    label("loc_1064")


    #C0032
    ChrTalk(
        0x20,
        (
            "我可懒得卖东西，\x01",
            "你们自己随便看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_108F")

    Jump("loc_2082")

    label("loc_1094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_1109")

    #C0033
    ChrTalk(
        0x20,
        (
            "怎么，这不是支援科\x01",
            "的小鬼们嘛。\x01",
            "都这种时间了还在工作吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x20,
        (
            "我已经关店了。\x01",
            "好了，都给我回去吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2082")

    label("loc_1109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1266")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120B")

    #C0035
    ChrTalk(
        0x20,
        (
            "鲁巴彻那群家伙\x01",
            "最近真是频繁闹事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x20,
        (
            "托他们的福，游击士们\x01",
            "都在抱怨忙得不可开交呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x20,
        (
            "你们这些警察，\x01",
            "也应该再多努力\x01",
            "一点才对吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#0000F哈哈哈……真是抱歉。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        (
            "#0300F和黑手党有关的事情，\x01",
            "都是由搜查一科来负责的啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1261")

    label("loc_120B")


    #C0040
    ChrTalk(
        0x20,
        (
            "鲁巴彻那群家伙\x01",
            "最近真是频繁闹事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x20,
        (
            "托他们的福，游击士们\x01",
            "好像相当出风头呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1261")

    Jump("loc_2082")

    label("loc_1266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_15AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C0")

    #C0042
    ChrTalk(
        0x20,
        "……是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x20,
        (
            "最近没怎么看到你们呢，\x01",
            "都在干些什么啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#0000F哈哈，最近有些忙……\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x153,
        (
            "#1110F哇～这是什么～！\x01",
            "有好多没见过的东西哦～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0046
    ChrTalk(
        0x20,
        (
            "小姑娘，那可不能乱碰啊。\x01",
            "这里摆着的\x01",
            "可都是些危险物品呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x20,
        (
            "喂，你们几个，\x01",
            "赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x20,
        (
            "我这里可没有东西能卖给\x01",
            "带着小孩的顾客啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCC, 7)
    Jump("loc_15A9")

    label("loc_13C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1555")

    #C0049
    ChrTalk(
        0x20,
        (
            "喂，你们几个，\x01",
            "赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x20,
        (
            "我这里可没有东西能卖给\x01",
            "带着小孩的顾客啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        (
            "#0004F（……嘴上虽然这么说，\x01",
            "  但要是拜托他的话，还是会卖的嘛。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_149C")

    #C0052
    ChrTalk(
        0x102,
        (
            "#0100F（这里的店主\x01",
            "  其实是个好人呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_154D")

    label("loc_149C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_14F7")

    #C0053
    ChrTalk(
        0x103,
        (
            "#0200F（嗯，虽然从外表上看不出来，\x01",
            "  但这里的店主大叔其实是个好人呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_154D")

    label("loc_14F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_154D")

    #C0054
    ChrTalk(
        0x104,
        (
            "#0300F（哈，从这个方面来看，这位大叔\x01",
            "  倒也是个具有常识的细心之人呢。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_154D")

    SetScenarioFlags(0x0, 0)
    Jump("loc_15A9")

    label("loc_1555")


    #C0055
    ChrTalk(
        0x20,
        (
            "喂，你们几个，\x01",
            "快回去，快回去。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x20,
        (
            "我这里可没有东西能卖给\x01",
            "带着小孩的顾客啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A9")

    Jump("loc_2082")

    label("loc_15AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_16B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1643")

    #C0057
    ChrTalk(
        0x20,
        (
            "最近，牵涉到黑手党\x01",
            "的事件好像多起来了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x20,
        "我听一个游击士老兄说了。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x20,
        (
            "好像是……在和外国的黑手党\x01",
            "进行争斗吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16B1")

    label("loc_1643")


    #C0060
    ChrTalk(
        0x20,
        (
            "嘁，克洛斯贝尔还是一点都没变，\x01",
            "仍然是个危险的多事之地。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x20,
        (
            "感觉那些什么都不知道的\x01",
            "游客真是挺可怜的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B1")

    Jump("loc_2082")

    label("loc_16B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1785")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1753")

    #C0062
    ChrTalk(
        0x20,
        "……一大早就有客人吗。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x20,
        (
            "不是我自夸，我这里绝对\x01",
            "算得上是克洛斯贝尔最萧条的店。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x20,
        (
            "一大清早就来，\x01",
            "就不能让我轻松一点嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1780")

    label("loc_1753")


    #C0065
    ChrTalk(
        0x20,
        (
            "……真没办法，\x01",
            "差不多也只能开门了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1780")

    Jump("loc_2082")

    label("loc_1785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_17E7")

    #C0066
    ChrTalk(
        0x20,
        (
            "嗯……？\x01",
            "怎么，都这么晚了还跑来。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x20,
        (
            "要买东西的话就快点，\x01",
            "我马上就要关店了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2082")

    label("loc_17E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1861")

    #C0068
    ChrTalk(
        0x20,
        (
            "嘁，今天的客人好多啊……\x01",
            "想安静地看一会杂志都不行。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x20,
        (
            "你们几个，如果买完东西了，\x01",
            "就赶快给我回去吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2082")

    label("loc_1861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1957")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18FB")

    #C0070
    ChrTalk(
        0x20,
        (
            "鲁巴彻的那些家伙\x01",
            "好像都已经被释放了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x20,
        (
            "哎呀呀，警察那边\x01",
            "就不能稍微有点长进吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x20,
        (
            "这样根本就没法\x01",
            "向市民们交代吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1952")

    label("loc_18FB")


    #C0073
    ChrTalk(
        0x20,
        "哼……算了，反正不关我事。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x20,
        (
            "总是这种德性，所以市民们\x01",
            "不信任警察也是难怪的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1952")

    Jump("loc_2082")

    label("loc_1957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1AC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A45")

    #C0075
    ChrTalk(
        0x20,
        (
            "你们知道\x01",
            "哈尔特曼议长吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x20,
        (
            "他是帝国派议员的领袖，\x01",
            "克洛斯贝尔政界的\x01",
            "重量级政治家之一。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x20,
        (
            "事实上，有传闻说\x01",
            "那家伙准备参加\x01",
            "下一届的市长选举呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x20,
        (
            "所以好像正在到处\x01",
            "拉选票呢。\x01",
            "真是让人讨厌的家伙啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1ABF")

    label("loc_1A45")


    #C0079
    ChrTalk(
        0x20,
        (
            "传闻说那个哈尔特曼议长\x01",
            "将会参加下届市长\x01",
            "选举呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x20,
        (
            "那样的人要是当上了市长，\x01",
            "……克洛斯贝尔可真的就\x01",
            "前途未卜了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ABF")

    Jump("loc_2082")

    label("loc_1AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1D2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC0")

    #C0081
    ChrTalk(
        0x20,
        (
            "怎么，又来客人了吗。\x01",
            "……真是的，好麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#0012F好、好像打扰到您了呢……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x20,
        "嗯，确实打扰到了。\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x20,
        (
            "我希望能在这里安静地坐上一天，\x01",
            "轻松悠闲地看看杂志。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x20,
        (
            "客人都别来才好呢。\x01",
            "你们要是买完东西了，就赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 1)
    Jump("loc_1D2A")

    label("loc_1BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB5")

    #C0086
    ChrTalk(
        0x20,
        (
            "在克洛斯贝尔，卖武器的店\x01",
            "真是少的令人意外啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x20,
        (
            "所以警察和游击士\x01",
            "都经常来我这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x20,
        (
            "……哈，不过那也只是表面上而已，\x01",
            "凡事都有不为人知的另一面。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x20,
        (
            "据说在旧城区那边\x01",
            "就有一家大型走私店。\x01",
            "你们最好不要和那边扯上关系。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D2A")

    label("loc_1CB5")


    #C0090
    ChrTalk(
        0x20,
        (
            "据说在旧城区那边\x01",
            "就有一家大型走私店。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x20,
        (
            "当然，他们卖的肯定\x01",
            "都不是什么合法产品。\x01",
            "你们最好不要和那边扯上关系。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D2A")

    Jump("loc_2082")

    label("loc_1D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1F3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EAC")
    SetScenarioFlags(0x4C, 4)

    #C0092
    ChrTalk(
        0x20,
        (
            "对了，小姑娘，\x01",
            "那个男人又来了哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0093
    ChrTalk(
        0x103,
        "#0205F哎……是主任吗？\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x20,
        (
            "嗯，和上次一样，\x01",
            "又把魔导杖放到我这里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x20,
        (
            "如果想买的话，\x01",
            "最好趁早吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x103,
        "#0203F了、了解。\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x102,
        (
            "#0100F缇欧的这位上司\x01",
            "还真是个喜欢兜圈子的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#0000F是啊……为什么不直接\x01",
            "交给缇欧呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x103,
        (
            "#0201F（主任……\x01",
            "  再这么兜圈子的话，\x01",
            "  我可要生气了哦。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F37")

    label("loc_1EAC")


    #C0100
    ChrTalk(
        0x20,
        (
            "对了，今天早上，\x01",
            "达德利那家伙也来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x20,
        (
            "那家伙最近好像十分忙碌。\x01",
            "他从以前开始就是那么认真又固执，\x01",
            "真担心他会不会把身体给累坏啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F37")

    Jump("loc_2082")

    label("loc_1F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1FC4")

    #C0102
    ChrTalk(
        0x20,
        (
            "在克洛斯贝尔，如果想要携带武器，\x01",
            "是需要许可证的。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x20,
        (
            "哈，不过伪造的证件早就泛滥了，\x01",
            "这规定基本上也没有什么意义呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2082")

    label("loc_1FC4")


    #C0104
    ChrTalk(
        0x20,
        (
            "放心吧，魔导杖的话，\x01",
            "我只卖给小姑娘一个人。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x20,
        (
            "但是，明明是想交给小姑娘，\x01",
            "却要扔在我这里……\x01",
            "仔细想想，这种举动好像也很奇怪吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x103,
        (
            "#0211F（主任，你在哪里呢……）\x01",
            "  （自言自语）……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2082")

    Jump("loc_AA2")

    label("loc_2087")

    TalkEnd(0x20)
    Return()

    # Function_5_8ED end

    def Function_6_208B(): pass

    label("Function_6_208B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2528")
    OP_4B(0x21, 0xFF)
    OP_4B(0x22, 0xFF)
    TurnDirection(0x21, 0x0, 0)
    TurnDirection(0x22, 0x0, 0)

    #C0107
    ChrTalk(
        0x101,
        (
            "#0000F多诺邦警督，还有雷蒙德警官……\x02\x03",

            "两位辛苦了，正在询问情报吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x21,
        (
            "嗯，正在追查仓库街\x01",
            "枪击事件的幕后内情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x22,
        (
            "反正，十有八九都和\x01",
            "鲁巴彻的人有关吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x22,
        (
            "那些家伙最近这段时间\x01",
            "一直在制造各种各样的麻烦。\x01",
            "比如说，像上次的那个卡车事故～\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        "#0105F卡车事故……？\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        "#0305F那是什么啊……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        "#0201F很让人在意呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x21, 0x22, 500)
    Sleep(300)

    #C0114
    ChrTalk(
        0x21,
        (
            "雷蒙德，你还是一点都没变，\x01",
            "嘴巴总是那么不严。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x22,
        "呜呜，果然不该说的吗～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x0, 500)
    Sleep(300)

    #C0116
    ChrTalk(
        0x21,
        "总之，这虽然只是流传在二科的传闻……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x21,
        (
            "上周末，在共和国那边发生事故的\x01",
            "卡车，据说是鲁巴彻\x01",
            "的搬运车呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x21,
        (
            "似乎是被什么人所袭击，\x01",
            "结果就起火爆炸了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(15)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(12)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0119
    ChrTalk(
        0x101,
        "#0005F什么……竟然有那种事吗！？\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x21,
        (
            "嗯……上面虽然想把消息压下来，\x01",
            "但最近关于这件事的小道消息越来越多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x21,
        (
            "虽然并没有把市民们卷进来……\x01",
            "但游击士似乎也开始出动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x103,
        "#0200F火药味好像开始变浓了呢。\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#0003F遇袭方是鲁巴彻，也就是说，\x01",
            "袭击者是黑月的人吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#0303F大概吧。\x01",
            "……能干出这种事的，\x01",
            "除了他们也没有别人了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x102,
        (
            "#0106F虽然应该轮不到我们来出面，\x01",
            "但还是稍微留意一下为好呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x21, 0xFF)
    OP_4C(0x22, 0xFF)
    OP_93(0x21, 0x10E, 0x0)
    OP_93(0x22, 0x5A, 0x0)
    SetScenarioFlags(0x94, 7)
    Jump("loc_25F2")

    label("loc_2528")

    TurnDirection(0x21, 0x0, 0)

    #C0126
    ChrTalk(
        0xFE,
        (
            "一科好像正在调查这\x01",
            "一连串卡车事故呢，\x01",
            "具体情况我们也不清楚。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "总之，最近的事件似乎在增多，\x01",
            "所以我们也没时间管那么多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "你们在市内巡逻的时候，\x01",
            "最好也顺便注意一下街上的情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x21, 0x10E, 0x0)

    label("loc_25F2")

    TalkEnd(0xFE)
    Return()

    # Function_6_208B end

    def Function_7_25F6(): pass

    label("Function_7_25F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_260B")
    Call(0, 6)
    Jump("loc_26BF")

    label("loc_260B")

    OP_4B(0x21, 0xFF)

    #C0129
    ChrTalk(
        0xFE,
        (
            "警督～我们差不多该回去啦～\x01",
            "我昨天也通宵工作了啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x21,
        (
            "你在唠唠叨叨说什么呢。\x01",
            "好啦，前往下个目的地！\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        "呜呜～警督你是魔鬼～！\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        "#0000F（看、看起来好像很忙呢。）\x02",
    )

    CloseMessageWindow()
    OP_4C(0x21, 0xFF)

    label("loc_26BF")

    TalkEnd(0xFE)
    Return()

    # Function_7_25F6 end

    def Function_8_26C3(): pass

    label("Function_8_26C3")

    Call(0, 9)
    Return()

    # Function_8_26C3 end

    def Function_9_26C7(): pass

    label("Function_9_26C7")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_301C")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2724")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2724")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2744")
    OP_AF(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3017")

    label("loc_2744")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2758")
    Jump("loc_3017")

    label("loc_2758")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3017")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_27A0")

    #C0133
    ChrTalk(
        0x8,
        (
            "赛尔缇欧果然\x01",
            "还差得远啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3017")

    label("loc_27A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2866")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2834")

    #C0134
    ChrTalk(
        0x8,
        (
            "有客人投诉说，我们的厨师\x01",
            "总是擅自端出一些乱七八糟的\x01",
            "奇特料理……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        (
            "……咳咳，十分抱歉，\x01",
            "本店的厨师给您添麻烦了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2861")

    label("loc_2834")


    #C0136
    ChrTalk(
        0x8,
        (
            "赛尔缇欧要是能\x01",
            "再稍微认真一点就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2861")

    Jump("loc_3017")

    label("loc_2866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_28E3")

    #C0137
    ChrTalk(
        0x8,
        (
            "……赛尔缇欧总是频繁地\x01",
            "从厨房跑出来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        (
            "而且好像还擅自\x01",
            "给客人们上一些\x01",
            "奇怪的菜……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x8,
        "那究竟是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3017")

    label("loc_28E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_29CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2993")

    #C0140
    ChrTalk(
        0x8,
        (
            "我和本店的大厨布拉温\x01",
            "是交往了四十年的好友，\x01",
            "还是一同修行的同伴。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        "但问题就是下一代。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "赛尔缇欧要是能努力修行，\x01",
            "把手艺再提高一些就好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_29C5")

    label("loc_2993")


    #C0143
    ChrTalk(
        0x8,
        (
            "实在是想不出能让\x01",
            "赛尔缇欧拿出干劲\x01",
            "的方法啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29C5")

    Jump("loc_3017")

    label("loc_29CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2A44")

    #C0144
    ChrTalk(
        0x8,
        (
            "在今年的纪念庆典期间，\x01",
            "本店也获得了最大利润。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        (
            "但庆典终归是庆典……\x01",
            "结束之后，就又要恢复沉寂了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3017")

    label("loc_2A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2B83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B29")

    #C0146
    ChrTalk(
        0x8,
        (
            "侬诺的一句话\x01",
            "竟然就让赛尔缇欧变得这么卖力……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x8,
        "那句话，你猜是什么呢。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x8,
        (
            "『在纪念庆典时，\x01",
            "会有很多女孩子来光顾哦。』\x01",
            "……就是这样。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x8,
        (
            "虽然确实是很有效果，\x01",
            "但反而觉得有效过了头，真担心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B7E")

    label("loc_2B29")


    #C0150
    ChrTalk(
        0x8,
        (
            "侬诺的一句话\x01",
            "让赛尔缇欧变得\x01",
            "十分卖力。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x8,
        (
            "平常总是不用心，\x01",
            "让我稍有些不安呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B7E")

    Jump("loc_3017")

    label("loc_2B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2C04")

    #C0152
    ChrTalk(
        0x8,
        (
            "有不少游客事先就想到了\x01",
            "会有纪念庆典，所以很早\x01",
            "就来到克洛斯贝尔了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x8,
        (
            "顺便还能享受一下\x01",
            "市内观光的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3017")

    label("loc_2C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2C77")

    #C0154
    ChrTalk(
        0x8,
        (
            "店内似乎稍微\x01",
            "有些吵闹呢，\x01",
            "真是十分抱歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x8,
        (
            "赛尔缇欧……要是能再稍微\x01",
            "认真一点工作就好了啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3017")

    label("loc_2C77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2D26")

    #C0156
    ChrTalk(
        0x8,
        (
            "本店的二楼是预约席位，\x01",
            "非常受顾客们的欢迎呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x8,
        (
            "其中也包括一位很重要的客人——\x01",
            "亚里欧斯·马克莱因先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x8,
        (
            "他每个月都会带女儿来一次，\x01",
            "在楼上享受美食。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3017")

    label("loc_2D26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2DAC")

    #C0159
    ChrTalk(
        0x8,
        (
            "随着纪念庆典的临近，\x01",
            "预约也越来越多了。\x01",
            "安排工作也很麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x8,
        (
            "采购的安排，\x01",
            "还有店内的装饰……\x01",
            "真是变得好忙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3017")

    label("loc_2DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2E31")

    #C0161
    ChrTalk(
        0x8,
        (
            "赛尔缇欧一边喊着好忙好忙，\x01",
            "一边频繁地从厨房钻出来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x8,
        (
            "好像是想自己给\x01",
            "妙龄女性端菜……\x01",
            "真是个让人头疼的家伙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3017")

    label("loc_2E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2EB4")

    #C0163
    ChrTalk(
        0x8,
        (
            "采购的工作似乎\x01",
            "稍微有些麻烦，\x01",
            "要和厨师一起调整一下安排呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x8,
        (
            "什么，请不必担心。\x01",
            "本店的特色风味绝对不会改变。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3017")

    label("loc_2EB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2F10")

    #C0165
    ChrTalk(
        0x8,
        (
            "今天有新婚的客人\x01",
            "前来光顾呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x8,
        (
            "稍后再给他们赠送一瓶\x01",
            "美味的葡萄酒吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3017")

    label("loc_2F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2F8D")

    #C0167
    ChrTalk(
        0x8,
        (
            "二层的客人预约的位子\x01",
            "似乎是商谈席位啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x8,
        (
            "呵呵，二层的预约席还有空位哦。\x01",
            "如果有兴趣，\x01",
            "就请上去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3017")

    label("loc_2F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3017")

    #C0169
    ChrTalk(
        0x8,
        (
            "欢迎光临。\x01",
            "欢迎光顾『温赛特』。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x8,
        (
            "您是来用餐的吗？\x01",
            "还是要外卖？\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x8,
        (
            "本店同时提供以上两种服务，\x01",
            "想点餐的话就请尽管吩咐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3017")

    Jump("loc_26D4")

    label("loc_301C")

    TalkEnd(0x8)
    Return()

    # Function_9_26C7 end

    def Function_10_3020(): pass

    label("Function_10_3020")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_30DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_307C")

    #C0172
    ChrTalk(
        0xFE,
        "噢，已经到晚餐时间了啊。\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        "看来今天晚上也有得忙了啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_30D8")

    label("loc_307C")


    #C0174
    ChrTalk(
        0xFE,
        (
            "我让赛尔缇欧专门\x01",
            "负责制作新菜式了。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "要是让我一个人制作全部的菜，\x01",
            "肯定会累死人的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30D8")

    Jump("loc_3CB8")

    label("loc_30DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_31C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3173")

    #C0176
    ChrTalk(
        0xFE,
        (
            "……客人并没有提出要求，\x01",
            "他却做出了那么奇怪的菜，\x01",
            "还被投诉了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "真头疼啊，我想那只是赛尔缇欧\x01",
            "那家伙的试做品吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_31BE")

    label("loc_3173")


    #C0178
    ChrTalk(
        0xFE,
        (
            "其实我也想让他\x01",
            "尽量按照自己的意愿发展……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        "教育年轻人真是很难啊。\x02",
    )

    CloseMessageWindow()

    label("loc_31BE")

    Jump("loc_3CB8")

    label("loc_31C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_32C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3279")

    #C0180
    ChrTalk(
        0xFE,
        (
            "今天早上，港湾区那边\x01",
            "好像发生什么事件了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "不过，反正离中央广场那么远，\x01",
            "应该也不会影响到客流量吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "麻烦的事件不断增加，\x01",
            "真是让人头疼啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_32C1")

    label("loc_3279")


    #C0183
    ChrTalk(
        0xFE,
        "这类事件增多的话，客人也会远远避开。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        "再这样下去可真让人头疼。\x02",
    )

    CloseMessageWindow()

    label("loc_32C1")

    Jump("loc_3CB8")

    label("loc_32C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_33CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3366")

    #C0185
    ChrTalk(
        0xFE,
        (
            "我给赛尔缇欧那家伙\x01",
            "提出了课题。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "那家伙自从来了我们店之后，\x01",
            "就只知道追女孩而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "必须要让他多少也\x01",
            "做一点厨师的修行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33C6")

    label("loc_3366")


    #C0188
    ChrTalk(
        0xFE,
        (
            "研究新菜式的任务\x01",
            "已经交给赛尔缇欧了。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "如果不把年轻人培养起来，\x01",
            "我也就无法安心退休啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33C6")

    Jump("loc_3CB8")

    label("loc_33CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_34E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3472")

    #C0190
    ChrTalk(
        0xFE,
        (
            "纪念庆典最终日，\x01",
            "我们店长也来厨房里\x01",
            "帮忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "霍伊斯托夫那家伙，\x01",
            "手艺还是和从前一样棒呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "……平时要是也能\x01",
            "多发挥发挥就好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_34E3")

    label("loc_3472")


    #C0193
    ChrTalk(
        0xFE,
        (
            "那家伙的做菜速度很快，\x01",
            "味道也令人无可挑剔。\x01",
            "烹饪技术可以说是在我之上……\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "但他已经不再\x01",
            "做厨房工作了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34E3")

    Jump("loc_3CB8")

    label("loc_34E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3628")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35BD")

    #C0195
    ChrTalk(
        0xFE,
        (
            "在纪念庆典期间，\x01",
            "我们店似乎也要举办个小活动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "那活动是赛尔缇欧刚才想到的，\x01",
            "现在似乎正在考虑具体计划呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "顺便一说……在背后撺掇他的\x01",
            "就是侬诺啊，\x01",
            "那家伙还真是很了解他呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3623")

    label("loc_35BD")


    #C0198
    ChrTalk(
        0xFE,
        (
            "在纪念庆典期间，\x01",
            "我们店似乎也要举办个小活动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "赛尔缇欧那家伙\x01",
            "现在似乎正在考虑具体计划呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3623")

    Jump("loc_3CB8")

    label("loc_3628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3718")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36B9")

    #C0200
    ChrTalk(
        0xFE,
        (
            "我要和霍伊斯托夫\x01",
            "做好纪念庆典期间\x01",
            "的安排表。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "特别是预约席，\x01",
            "菜式顺序也要写清楚。\x01",
            "要好好安排一下预定计划啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3713")

    label("loc_36B9")


    #C0202
    ChrTalk(
        0xFE,
        (
            "顺便一说，预约席的菜式\x01",
            "是霍伊斯托夫选定的。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "那家伙的厨师生涯\x01",
            "还远远没有结束呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3713")

    Jump("loc_3CB8")

    label("loc_3718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3771")

    #C0204
    ChrTalk(
        0xFE,
        "侬诺应该会找个比她小的丈夫。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "那样一看，真为她\x01",
            "将来的丈夫担心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CB8")

    label("loc_3771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_37BC")

    #C0206
    ChrTalk(
        0xFE,
        "不劳者则不获。\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "希望赛尔缇欧也能\x01",
            "更加认真地工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CB8")

    label("loc_37BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_380A")

    #C0208
    ChrTalk(
        0xFE,
        "下个月终于就是创立纪念庆典了啊……\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        "看来又要开始忙了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CB8")

    label("loc_380A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_395F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3913")

    #C0210
    ChrTalk(
        0xFE,
        (
            "霍伊斯托夫那家伙，\x01",
            "从很久以前开始，就一直\x01",
            "想开家大众化的西餐厅。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "说是希望顾客不仅能在餐厅中\x01",
            "享受美味的料理，同时还能\x01",
            "感受一下店里热闹的气氛。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "明明是个一流厨师，\x01",
            "却总是考虑这种奇怪的问题啊。\x01",
            "哈哈，不过我好像也受他感染了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_395A")

    label("loc_3913")


    #C0213
    ChrTalk(
        0xFE,
        (
            "他真的很喜欢考虑一些奇怪的问题啊，\x01",
            "不过，连我好像也被他感染了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_395A")

    Jump("loc_3CB8")

    label("loc_395F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39FE")

    #C0214
    ChrTalk(
        0xFE,
        (
            "铁路运输似乎\x01",
            "又延迟了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "算了，交给我吧。\x01",
            "而且霍伊斯托夫也会\x01",
            "立刻想出备用菜式的。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "具体味道就由我来\x01",
            "进行细微调整吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A49")

    label("loc_39FE")


    #C0217
    ChrTalk(
        0xFE,
        (
            "霍伊斯托夫那家伙\x01",
            "马上就能想出替代的新菜式。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        "他的头脑非常灵活啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3A49")

    Jump("loc_3CB8")

    label("loc_3A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3B2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ADB")

    #C0219
    ChrTalk(
        0xFE,
        "两位客人，稍等……\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "噢，想点餐的话\x01",
            "请去大厅哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "不过，就算直接和我说，\x01",
            "也能给你们做出来的，哈哈哈。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B27")

    label("loc_3ADB")


    #C0222
    ChrTalk(
        0xFE,
        (
            "随便指定\x01",
            "一个菜式吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "说不定我马上就能给你们\x01",
            "做出来的呢，哈哈哈。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B27")

    Jump("loc_3CB8")

    label("loc_3B2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3BE0")

    #C0224
    ChrTalk(
        0xFE,
        (
            "制作料理需要的就是毅力、诚意，\x01",
            "然后还有玩心。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "不管有多忙，\x01",
            "也不能让自己的心变得干涸。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "……差不多也该教教\x01",
            "赛尔缇欧，让他明白什么\x01",
            "才是料理人的『心』了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CB8")

    label("loc_3BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3CB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C81")

    #C0227
    ChrTalk(
        0xFE,
        "今天的料理准备工作……\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "嗯～感觉非常好啊。\x01",
            "在这三十年来也算是最成功的一次啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "很好，就继续努力，\x01",
            "将这个味道保持下去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3CB8")

    label("loc_3C81")


    #C0230
    ChrTalk(
        0xFE,
        (
            "在午餐时间到来之前，\x01",
            "必须要先把这些杂事都做完啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CB8")

    TalkEnd(0xFE)
    Return()

    # Function_10_3020 end

    def Function_11_3CBC(): pass

    label("Function_11_3CBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CDD")
    Call(0, 38)
    Return()

    label("loc_3CDD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F2B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F26")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "交付料理\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D59")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 12)
    Jump("loc_3F21")

    label("loc_3D59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F21")
    Call(0, 40)
    Call(0, 41)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DEF")

    #C0231
    ChrTalk(
        0xFE,
        (
            "……异想天开的料理……\x01",
            "你们好像并没有携带啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "收集到十种以上之后，\x01",
            "再来找我吧，\x01",
            "我会给你们回礼的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F12")

    label("loc_3DEF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3E62")

    #C0233
    ChrTalk(
        0xFE,
        (
            "种类不够啊，\x01",
            "请你们至少提供十种。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "收集到十种以上之后\x01",
            "再来找我吧，\x01",
            "我会给你们回礼的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F12")

    label("loc_3E62")


    #C0235
    ChrTalk(
        0xFE,
        "现在要报告吗？\x02",
    )

    CloseMessageWindow()

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【报告】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EAF")
    Call(0, 39)
    Return()

    label("loc_3EAF")


    #C0236
    ChrTalk(
        0xFE,
        (
            "是吗……\x01",
            "如果能尽量多收集一些，\x01",
            "我也会很高兴的。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "如果再收集到了料理，\x01",
            "请一定拿来给我啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F12")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F21")

    label("loc_3F21")

    Jump("loc_3D07")

    label("loc_3F26")

    Jump("loc_3F2E")

    label("loc_3F2B")

    Call(0, 12)

    label("loc_3F2E")

    TalkEnd(0xFE)
    Return()

    # Function_11_3CBC end

    def Function_12_3F32(): pass

    label("Function_12_3F32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_401D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FC3")

    #C0238
    ChrTalk(
        0xA,
        (
            "新菜式终于\x01",
            "开始成形了。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xA,
        "这次真的是我的自信之作了！\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xA,
        (
            "好，今天也去找找可爱的女孩，\x01",
            "然后邀请她们试吃吧～¤\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4018")

    label("loc_3FC3")


    #C0241
    ChrTalk(
        0xA,
        (
            "因为被人说过看起来很诡异，\x01",
            "所以在外观方面做了改良哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xA,
        "客人的意见果然重要。\x02",
    )

    CloseMessageWindow()

    label("loc_4018")

    Jump("loc_4B22")

    label("loc_401D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_40E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40AB")

    #C0243
    ChrTalk(
        0xA,
        (
            "之前也曾邀请客人试吃\x01",
            "我的试做品……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xA,
        "但大家连碰都不碰呢。\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xA,
        (
            "嘁，什么嘛。\x01",
            "果然是因为\x01",
            "外观太诡异了吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_40DE")

    label("loc_40AB")


    #C0246
    ChrTalk(
        0xA,
        (
            "关于新菜式，大概还是\x01",
            "不要太新颖奇异比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40DE")

    Jump("loc_4B22")

    label("loc_40E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_41F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4160")

    #C0247
    ChrTalk(
        0xA,
        (
            "你不觉得坐在正中座位上的\x01",
            "那些女孩很可爱吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xA,
        (
            "好，这就去请她们免费品尝\x01",
            "我的试做品吧……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_41F1")

    label("loc_4160")


    #C0249
    ChrTalk(
        0xA,
        (
            "『这是我以你的形象为灵感\x01",
            "  独立自创的菜式哦！』……\x01",
            "这样说的话，任何女孩都会中招吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xA,
        (
            "同时还能听取客人对试做品的感想，\x01",
            "真是一举两得啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41F1")

    Jump("loc_4B22")

    label("loc_41F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_42D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42AB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_422B")
    Jump("loc_4232")

    label("loc_422B")

    OP_93(0xA, 0x10E, 0x0)

    label("loc_4232")


    #C0251
    ChrTalk(
        0xA,
        (
            "嗯嗯……按照肉料理、\x01",
            "鱼料理来分类的话，\x01",
            "和以前就没有不同了……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xA,
        (
            "果然还是应该以\x01",
            "珍稀一点的食材为基础……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_42D4")

    label("loc_42AB")


    #C0253
    ChrTalk(
        0xA,
        (
            "我正在思考新菜式呢，\x01",
            "不要打扰我啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42D4")

    Jump("loc_4B22")

    label("loc_42D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4371")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4349")

    #C0254
    ChrTalk(
        0xA,
        "纪念庆典已经结束了，终于有了空闲。\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xA,
        (
            "今天我要集中注意力，\x01",
            "专心欣赏漂亮女孩。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_436C")

    label("loc_4349")


    #C0256
    ChrTalk(
        0xA,
        (
            "呵呵……真期待\x01",
            "下午的客人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_436C")

    Jump("loc_4B22")

    label("loc_4371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_43DA")

    #C0257
    ChrTalk(
        0xA,
        (
            "在纪念庆典期间，很多活泼可爱的\x01",
            "年轻女孩都会来这里用餐……\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xA,
        "我必须要加油干了～！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B22")

    label("loc_43DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4493")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_444A")

    #C0259
    ChrTalk(
        0xA,
        (
            "随着纪念庆典的临近，冒出了\x01",
            "菜式调整之类乱七八糟的活～\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xA,
        "实在是拿不出干劲啊～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_448E")

    label("loc_444A")


    #C0261
    ChrTalk(
        0xA,
        (
            "啊～不然就去广场转转，\x01",
            "欣赏一下可爱的女孩吧。\x01",
            "（自言自语）……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_448E")

    Jump("loc_4B22")

    label("loc_4493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4539")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44AE")
    Call(0, 14)
    Jump("loc_4534")

    label("loc_44AE")

    OP_93(0xA, 0xB4, 0x0)
    OP_4B(0xB, 0xFF)

    #C0262
    ChrTalk(
        0xA,
        (
            "我、我只是把料理端给了\x01",
            "那边那个女孩而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xB,
        (
            "真是的……又去\x01",
            "纠缠客人了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xB,
        (
            "这可不行哦。\x01",
            "好啦，回去工作！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)

    label("loc_4534")

    Jump("loc_4B22")

    label("loc_4539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4604")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45D2")

    #C0265
    ChrTalk(
        0xA,
        "好，薏面套餐一份～¤\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xA,
        (
            "这是中间座位那个\x01",
            "可爱女孩点的。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xA,
        (
            "嘿嘿嘿，送过去以后，\x01",
            "大概还能顺便和她聊点有意思的话题啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_45FF")

    label("loc_45D2")


    #C0268
    ChrTalk(
        0xA,
        (
            "女孩的点单就能让我\x01",
            "不自觉地拿出干劲啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45FF")

    Jump("loc_4B22")

    label("loc_4604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4712")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46B7")

    #C0269
    ChrTalk(
        0xA,
        (
            "呼～午餐高峰期\x01",
            "总算过去了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xA,
        (
            "大概是因为纪念庆典临近了吧，\x01",
            "最近真是忙得要命啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xA,
        (
            "但布拉温先生好像\x01",
            "却还是游刃有余的呢……\x01",
            "这是为什么呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_470D")

    label("loc_46B7")


    #C0272
    ChrTalk(
        0xA,
        (
            "如果我也能像布拉温先生那样\x01",
            "迅速完成工作的话，\x01",
            "就能有更多时间去和女孩聊天了啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_470D")

    Jump("loc_4B22")

    label("loc_4712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4831")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47D6")

    #C0273
    ChrTalk(
        0xA,
        (
            "有个女孩总是在\x01",
            "店中最里面的座位上喝咖啡。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xA,
        (
            "仔细一看还真是可爱呢。\x01",
            "刚才看她好像有空，\x01",
            "就试着去和她说话……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xA,
        "但几乎完全没反应呢。\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xA,
        "可恶……真令人沮丧……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_482C")

    label("loc_47D6")


    #C0277
    ChrTalk(
        0xA,
        (
            "我难道真的就那么\x01",
            "不受女孩子欢迎吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xA,
        (
            "再怎么说，被人无视\x01",
            "是很令人沮丧的啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_482C")

    Jump("loc_4B22")

    label("loc_4831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4901")

    #C0279
    ChrTalk(
        0xA,
        "克洛斯贝尔有很多美人呢。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xA,
        (
            "像那个大明星伊莉娅·普拉提耶，\x01",
            "还有那个经济界巨头的女儿，\x01",
            "好像是叫玛丽亚贝尔·库罗伊斯吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xA,
        (
            "街上的那些女孩也都很时尚，\x01",
            "都是相当漂亮的美人呢。\x01",
            "嘻嘻嘻嘻……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B22")

    label("loc_4901")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4977")

    #C0282
    ChrTalk(
        0xA,
        (
            "嘁，今天来店里用餐\x01",
            "的女孩子真少啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xA,
        (
            "不不，接下来才是决战。\x01",
            "在午餐时段到来之前，还不能下定论。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B22")

    label("loc_4977")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_49EF")

    #C0284
    ChrTalk(
        0xA,
        (
            "可恶，午餐高峰时段简直就是地狱。\x01",
            "会忙得焦头烂额。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xA,
        (
            "呼……如果客人全都是\x01",
            "漂亮可爱的女孩该多好……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B22")

    label("loc_49EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4B22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AA7")

    #C0286
    ChrTalk(
        0xA,
        (
            "这家店，每天都会有\x01",
            "很多客人前来光顾。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xA,
        (
            "而且，有很多朝气蓬勃\x01",
            "的年轻小姐也会来。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xA,
        (
            "而我却要一天到晚待在厨房里……\x01",
            "忙得连偷窥店里女孩的时间都没有。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4B22")

    label("loc_4AA7")


    #C0289
    ChrTalk(
        0xA,
        (
            "我来克洛斯贝尔的目的\x01",
            "可并不是为了忙碌工作啊。\x01",
            "而是为了结识无数可爱的女孩。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xA,
        (
            "我是不会就此放弃的！\x01",
            "（自言自语）……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B22")

    Return()

    # Function_12_3F32 end

    def Function_13_4B23(): pass

    label("Function_13_4B23")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4C0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BB2")
    TurnDirection(0xFE, 0xE, 0)

    #C0291
    ChrTalk(
        0xFE,
        (
            "实在非常抱歉。\x01",
            "由于本店的采购失误，所以……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        (
            "如果您不介意用红茶来代替的话，\x01",
            "立刻就能给您端上……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4C08")

    label("loc_4BB2")


    #C0293
    ChrTalk(
        0xFE,
        (
            "（似乎是因为赛尔缇欧\x01",
            "  使用了大量的\x01",
            "  咖啡豆呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        "（呼，真让人头疼啊……）\x02",
    )

    CloseMessageWindow()

    label("loc_4C08")

    Jump("loc_5392")

    label("loc_4C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4CD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C9C")

    #C0295
    ChrTalk(
        0xFE,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        (
            "今天的客人\x01",
            "好像稍微有点少呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "虽然太多了也会让人疲于应付，\x01",
            "但这么少的话，也令人头疼呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4CD1")

    label("loc_4C9C")


    #C0298
    ChrTalk(
        0xFE,
        (
            "不然就像纪念庆典期间那样，\x01",
            "出去招揽一下客人吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CD1")

    Jump("loc_5392")

    label("loc_4CD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4D2B")

    #C0299
    ChrTalk(
        0xFE,
        "今天街上来了很多警察呢……\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        (
            "好像从早上开始\x01",
            "就一直在到处巡逻。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5392")

    label("loc_4D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4E05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DD8")

    #C0301
    ChrTalk(
        0xFE,
        (
            "赛尔缇欧好像\x01",
            "在烦恼着什么呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "甚至还来问我一些\x01",
            "料理方面的问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "问什么『你知不知道一些\x01",
            "奇特稀有的料理』，\x01",
            "或许他是想做些什么吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4E00")

    label("loc_4DD8")


    #C0304
    ChrTalk(
        0xFE,
        (
            "赛尔缇欧\x01",
            "时常会说一些\x01",
            "奇怪的话呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E00")

    Jump("loc_5392")

    label("loc_4E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4E9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E63")

    #C0305
    ChrTalk(
        0xFE,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xFE,
        (
            "啊，好可爱的小姑娘呀，\x01",
            "要不要来份儿童套餐？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4E98")

    label("loc_4E63")


    #C0307
    ChrTalk(
        0xFE,
        (
            "这个时间有很多空位子。\x01",
            "三位客人吗，非常欢迎哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E98")

    Jump("loc_5392")

    label("loc_4E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4EAE")
    Call(0, 34)
    Jump("loc_5392")

    label("loc_4EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4F5E")

    #C0308
    ChrTalk(
        0xFE,
        (
            "店长好像正在为\x01",
            "纪念庆典做准备呢，\x01",
            "我们也要去帮忙了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "每年我们店都会免费赠送饮料\x01",
            "或是纪念品之类的东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xFE,
        (
            "另外儿童套餐上的旗子\x01",
            "还会换成庆祝旗哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5392")

    label("loc_4F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4FD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F79")
    Call(0, 14)
    Jump("loc_4FCF")

    label("loc_4F79")


    #C0311
    ChrTalk(
        0xFE,
        (
            "赛尔缇欧经常从\x01",
            "厨房里跑出来呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "现在正是最忙的时候，\x01",
            "必须让他认真工作啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FCF")

    Jump("loc_5392")

    label("loc_4FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_502D")

    #C0313
    ChrTalk(
        0xFE,
        (
            "今天的客人，不知为何，\x01",
            "给人很舒服的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xFE,
        "让人看上去就有好感。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5392")

    label("loc_502D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5063")

    #C0315
    ChrTalk(
        0xFE,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        "要点些什么吗～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5392")

    label("loc_5063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_50DA")

    #C0317
    ChrTalk(
        0xFE,
        (
            "二楼的席位可以预约哦。\x01",
            "如果预约的话，还可以\x01",
            "事先指定具体菜式。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "带着家人一起来的客人\x01",
            "相当多呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5392")

    label("loc_50DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_51F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5192")

    #C0319
    ChrTalk(
        0xFE,
        (
            "店长和布拉温先生\x01",
            "是很要好的朋友呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        (
            "餐厅的经营方针好像也总是经过\x01",
            "他们两个人商量之后才决定的。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "……成年之后仍然保持着友情，\x01",
            "真有点让人憧憬呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_51F0")

    label("loc_5192")


    #C0322
    ChrTalk(
        0xFE,
        (
            "店长和布拉温先生\x01",
            "是很要好的朋友呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xFE,
        (
            "经营方针好像也总是经过\x01",
            "两个人商量之后才决定的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51F0")

    Jump("loc_5392")

    label("loc_51F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_52B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_526A")

    #C0324
    ChrTalk(
        0xFE,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "本店正在推行早餐特供服务哦。\x01",
            "如果还没吃早饭的话，\x01",
            "就请马上点餐吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_52B0")

    label("loc_526A")


    #C0326
    ChrTalk(
        0xFE,
        (
            "本店正在推行早餐特供服务。\x01",
            "如果还没吃早饭的话，\x01",
            "就请马上点餐吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52B0")

    Jump("loc_5392")

    label("loc_52B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5310")

    #C0327
    ChrTalk(
        0xFE,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        (
            "呼，午餐时间真是好忙啊。\x01",
            "还得要打起精神，继续努力呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5392")

    label("loc_5310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5392")

    #C0329
    ChrTalk(
        0xFE,
        (
            "让您久等了～！\x01",
            "Ａ套餐两份～！\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        "啊，客人您请坐！\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "我们这里相当忙乱，\x01",
            "如果客人站在店里的话，\x01",
            "我们会很困扰的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5392")

    TalkEnd(0xFE)
    Return()

    # Function_13_4B23 end

    def Function_14_5396(): pass

    label("Function_14_5396")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)

    #C0332
    ChrTalk(
        0xB,
        (
            "赛尔缇欧～\x01",
            "要不要我好好敲敲你的脑袋啊～？\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xA,
        (
            "我、我并没\x01",
            "做什么坏事……！\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xB,
        (
            "你在偷懒吧？\x01",
            "好了，快点回厨房！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_14_5396 end

    def Function_15_542D(): pass

    label("Function_15_542D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_54C1")
    Jump("loc_550B")

    label("loc_54C1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_54E1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_550B")

    label("loc_54E1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5501")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_550B")

    label("loc_5501")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_550B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_563F")

    #C0335
    ChrTalk(
        0xFE,
        "#2600F啊，是各位啊。\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x102,
        (
            "#0105F阿奈斯特先生。\x01",
            "您在用餐吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "#2606F不，只是稍微休息一下。\x02\x03",

            "#2600F晚上还要随同市长\x01",
            "出席听证会。\x02\x03",

            "我正在检查\x01",
            "到时候要提交的资料呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x102,
        (
            "#0102F是吗……\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x101,
        (
            "#0000F（看起来，似乎\x01",
            "  比我们还要忙呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5702")

    label("loc_563F")

    SetChrSubChip(0xFE, 0x0)

    #C0340
    ChrTalk(
        0xFE,
        (
            "#2601F嗯～以这些资料，\x01",
            "似乎无法完全回避帝国派\x01",
            "提出的要求呢……\x02\x03",

            "#2603F但如果提出这些资料的话，\x01",
            "共和国派那边恐怕又……\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x101,
        "#0000F（打扰他可不好……）\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x102,
        "#0104F（嗯……我们还是走吧。）\x02",
    )

    CloseMessageWindow()

    label("loc_5702")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_542D end

    def Function_16_570A(): pass

    label("Function_16_570A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_579E")
    Jump("loc_57E8")

    label("loc_579E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_57BE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57E8")

    label("loc_57BE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_57DE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57E8")

    label("loc_57DE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_57E8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_587E")

    #C0343
    ChrTalk(
        0xFE,
        (
            "……居然说咖啡\x01",
            "已经没有了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "简直不敢相信。\x01",
            "西餐厅里居然没有咖啡，\x01",
            "这也太不可思议了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6611")

    label("loc_587E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_58CC")

    #C0345
    ChrTalk(
        0xFE,
        "今天早上，街上好像很安静呢。\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xFE,
        "警官也很少，令人在意呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6611")

    label("loc_58CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_597F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5951")

    #C0347
    ChrTalk(
        0xFE,
        (
            "（啜饮）……\x01",
            "……………呜……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        "没带着克洛斯贝尔时代周刊……\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xFE,
        (
            "可能是出门之前\x01",
            "忘记拿了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_597A")

    label("loc_5951")


    #C0350
    ChrTalk(
        0xFE,
        (
            "议会现在进展如何了呢，\x01",
            "好在意啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_597A")

    Jump("loc_6611")

    label("loc_597F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5A7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A47")

    #C0351
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔时代周刊\x01",
            "又刊登了关于预算会议的话题啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "一群成年人吵得面红耳赤，\x01",
            "口沫横飞地相互争论。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xFE,
        (
            "虽然每次都是如此，\x01",
            "但还是滑稽得让人发笑啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5A7A")

    label("loc_5A47")


    #C0355
    ChrTalk(
        0xFE,
        (
            "议员们一脸正经地争吵，\x01",
            "想想就觉得滑稽可笑啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A7A")

    Jump("loc_6611")

    label("loc_5A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5B80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B35")

    #C0356
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "街上终于从纪念庆典的氛围中\x01",
            "安静下来了，不错……\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        (
            "亚里欧斯·马克莱因\x01",
            "好像又出差离开了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        (
            "那个人几乎都不会\x01",
            "留在自治州里呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5B7B")

    label("loc_5B35")


    #C0360
    ChrTalk(
        0xFE,
        (
            "亚里欧斯·马克莱因\x01",
            "明明是克洛斯贝尔人，\x01",
            "却几乎都不待在自治州里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B7B")

    Jump("loc_6611")

    label("loc_5B80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5C78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C0C")

    #C0361
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "警备队的司令，\x01",
            "似乎经常会参加\x01",
            "接待宴会呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xFE,
        (
            "传闻说他连工作也不做，\x01",
            "只是到处散步游玩。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5C73")

    label("loc_5C0C")


    #C0364
    ChrTalk(
        0xFE,
        (
            "警备队的司令\x01",
            "好像很喜欢接待宴会呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        (
            "他以后会不会被\x01",
            "克洛斯贝尔时代周刊揭露，\x01",
            "然后直接垮台呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C73")

    Jump("loc_6611")

    label("loc_5C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5D93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D0D")

    #C0366
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ的库罗伊斯总裁\x01",
            "以积极参与慈善事业而闻名。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        (
            "本来就已经那么忙了，\x01",
            "竟然还能做那么多善事啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5D8E")

    label("loc_5D0D")


    #C0369
    ChrTalk(
        0xFE,
        (
            "说起ＩＢＣ，\x01",
            "可是世界上最大的银行集团啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "本来就已经那么忙了，\x01",
            "竟然还能积极参与慈善事业。\x01",
            "库罗伊斯总裁也真是了不起呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D8E")

    Jump("loc_6611")

    label("loc_5D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_5E47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E26")

    #C0371
    ChrTalk(
        0xFE,
        (
            "（啜饮）……\x01",
            "…………………………？\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        "咖啡已经没有了啊。\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "用一杯咖啡来打发时间，\x01",
            "这么久差不多也算是极限了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5E42")

    label("loc_5E26")


    #C0374
    ChrTalk(
        0xFE,
        "……差不多也该回去了。\x02",
    )

    CloseMessageWindow()

    label("loc_5E42")

    Jump("loc_6611")

    label("loc_5E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5F51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EEE")

    #C0375
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "听说彩虹剧团的第二主角\x01",
            "是个被破格提拔的新人女孩哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "名字是……叫什么来着，\x01",
            "杂志上可是刊登了关于她的大篇报道哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5F4C")

    label("loc_5EEE")


    #C0378
    ChrTalk(
        0xFE,
        (
            "那个新人女孩好像\x01",
            "还没有任何舞台经验呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "那样的纯外行人\x01",
            "竟然能得到第二主角的位置啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F4C")

    Jump("loc_6611")

    label("loc_5F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6056")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6016")

    #C0380
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "彩虹剧团的门票好像\x01",
            "被争抢得相当激烈哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        "所以说，不懂放弃的庶民真让人头疼啊……\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        (
            "反正最后也无法得到，\x01",
            "还是从最初开始就不去争取才比较明智。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6051")

    label("loc_6016")


    #C0384
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "……我才不是吃不到葡萄\x01",
            "说葡萄酸呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6051")

    Jump("loc_6611")

    label("loc_6056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_61C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6149")

    #C0386
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        (
            "说到玛因兹，\x01",
            "那是个被北方群山所包围的矿山镇哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xFE,
        (
            "由于导力已经有了一定程度的普及，\x01",
            "所以大概并不像阿尔摩利卡村\x01",
            "那么富有乡土气息吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "但毕竟也只是个乡下地方啦，\x01",
            "不是什么值得去观光的地方。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_61BD")

    label("loc_6149")


    #C0390
    ChrTalk(
        0xFE,
        (
            "说到玛因兹，\x01",
            "那是个被北方群山所包围的矿山镇哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        (
            "也就是所谓的穷乡僻壤啦。\x01",
            "并不是什么值得特意去参观的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61BD")

    Jump("loc_6611")

    label("loc_61C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6303")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_629A")

    #C0392
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xFE,
        (
            "最近似乎也有不少商人\x01",
            "去阿尔摩利卡村商谈生意呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xFE,
        (
            "呵，毕竟那里蔬菜的品质都不错，\x01",
            "多少也有些商业价值吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        (
            "但竟然为此就特意跑到那种偏僻\x01",
            "的农村去，他们可真行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_62FE")

    label("loc_629A")


    #C0396
    ChrTalk(
        0xFE,
        (
            "如果要赚钱，\x01",
            "去什么地方不能赚啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xFE,
        (
            "竟然还特意跑到阿尔摩利卡村\x01",
            "去进货，他们可真是不嫌远呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62FE")

    Jump("loc_6611")

    label("loc_6303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_63E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63A3")

    #C0398
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xFE,
        (
            "听说警察终于介入旧城区\x01",
            "那些乱七八糟的事件了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "但最后也没有\x01",
            "逮捕到犯人啊。\x01",
            "做法还是和从前一样敷衍了事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_63E3")

    label("loc_63A3")


    #C0401
    ChrTalk(
        0xFE,
        (
            "警察还真是喜欢敷衍了事啊。\x01",
            "对待犯罪者，\x01",
            "就要严厉打击才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63E3")

    Jump("loc_6611")

    label("loc_63E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6545")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64AA")

    #C0402
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        (
            "说起克洛斯贝尔时代周刊，\x01",
            "还真是喜欢对游击士大加赞扬呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        (
            "虽然能理解这种文章确实受欢迎，\x01",
            "但还是觉得应该多刊登一些\x01",
            "批判议会和政府的尖锐文章。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6540")

    label("loc_64AA")


    #C0405
    ChrTalk(
        0xFE,
        (
            "我觉得克洛斯贝尔时代周刊应该\x01",
            "多刊登一些批判议会和政府\x01",
            "的尖锐文章。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "……算啦，那确实也很勉强吧。\x01",
            "就我个人来说，还是觉得\x01",
            "那样的报道更有意思。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6540")

    Jump("loc_6611")

    label("loc_6545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6611")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65C5")

    #C0407
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        "我很喜欢这家店的氛围。\x02",
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xFE,
        (
            "在这里一边喝咖啡一边读书，\x01",
            "心情很快就能平静下来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6611")

    label("loc_65C5")


    #C0410
    ChrTalk(
        0xFE,
        (
            "我很喜欢这家店的氛围。\x01",
            "一边喝咖啡一边读书的话，\x01",
            "心情很快就能平静下来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6611")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_570A end

    def Function_17_6619(): pass

    label("Function_17_6619")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_66AD")
    Jump("loc_66F7")

    label("loc_66AD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_66CD")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_66F7")

    label("loc_66CD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_66ED")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_66F7")

    label("loc_66ED")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_66F7")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x11, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67F7")

    #C0411
    ChrTalk(
        0x11,
        (
            "哎呀，真是很棒的装修设计呢！\x01",
            "不愧是金德尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xF,
        "能让您感到满意，我非常荣幸。\x02",
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xF,
        (
            "那么……另一件想要委托\x01",
            "的工作是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x11,
        (
            "嗯嗯，其实是在埃雷波尼亚的帝都\x01",
            "有了建造新的酒店大厦计划……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_68AB")

    label("loc_67F7")


    #C0415
    ChrTalk(
        0x11,
        (
            "我想，我们应该去\x01",
            "挑战一下……\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xF,
        (
            "原来如此，你的想法\x01",
            "我完全明白了。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xF,
        (
            "人总是喜欢追求新鲜事物的，\x01",
            "而我们也必须顺应人们的这一心理啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x11,
        (
            "哈哈，您能同意，\x01",
            "那真是最好不过。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68AB")

    SetChrSubChip(0xF, 0x0)
    TalkEnd(0xF)
    Return()

    # Function_17_6619 end

    def Function_18_68B3(): pass

    label("Function_18_68B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_690E")

    #C0419
    ChrTalk(
        0xFE,
        (
            "嗯……今天顺便\x01",
            "吃个饭吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        (
            "为了谨慎起见，\x01",
            "必须要先确认一下味道。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69F4")

    label("loc_690E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_69F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_699C")

    #C0421
    ChrTalk(
        0xFE,
        (
            "这次的生意对象，\x01",
            "是个非常重要的客户。\x01",
            "绝对不允许有一点失败的可能。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xFE,
        (
            "必须要定好预约席，\x01",
            "做好万全的准备啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_69F4")

    label("loc_699C")


    #C0423
    ChrTalk(
        0xFE,
        (
            "这家西餐厅以料理的美味度\x01",
            "而声名远播。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xFE,
        (
            "这次我就先定好席位，\x01",
            "用美食款待对方吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69F4")

    TalkEnd(0xFE)
    Return()

    # Function_18_68B3 end

    def Function_19_69F8(): pass

    label("Function_19_69F8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6A8C")
    Jump("loc_6AD6")

    label("loc_6A8C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6AAC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6AD6")

    label("loc_6AAC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6ACC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6AD6")

    label("loc_6ACC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6AD6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6B67")

    #C0425
    ChrTalk(
        0xFE,
        (
            "嗯，满足满足。\x01",
            "啊，这味道真是无可挑剔啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xFE,
        (
            "下次来克洛斯贝尔的时候，\x01",
            "把朋友也带上吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BD3")

    label("loc_6B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6BD3")

    #C0427
    ChrTalk(
        0xFE,
        (
            "（嚼嚼）……\x01",
            "嘿嘿，真是美味啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xFE,
        (
            "以这种价格居然能吃到\x01",
            "如此美味的料理，\x01",
            "感觉真是赚到了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BD3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_69F8 end

    def Function_20_6BDB(): pass

    label("Function_20_6BDB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6C6F")
    Jump("loc_6CB9")

    label("loc_6C6F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6C8F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6CB9")

    label("loc_6C8F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CAF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6CB9")

    label("loc_6CAF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6CB9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6D3A")

    #C0429
    ChrTalk(
        0xFE,
        (
            "我习惯每周和\x01",
            "家人一起吃一次饭。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xFE,
        (
            "如果老是见不到母亲，\x01",
            "我会很担心的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DA5")

    label("loc_6D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6DA5")

    #C0431
    ChrTalk(
        0xFE,
        (
            "和家人吃饭，\x01",
            "自然要选定这家店啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xFE,
        (
            "公道的价格，美味的料理。\x01",
            "从以前开始就一直未曾改变呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DA5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_6BDB end

    def Function_21_6DAD(): pass

    label("Function_21_6DAD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6E41")
    Jump("loc_6E8B")

    label("loc_6E41")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6E61")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E8B")

    label("loc_6E61")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E81")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E8B")

    label("loc_6E81")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6E8B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6F2E")
    SetChrSubChip(0xFE, 0x0)

    #C0433
    ChrTalk(
        0xFE,
        (
            "不过婆婆\x01",
            "一个人生活，\x01",
            "会不会有些危险呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xFE,
        (
            "请您务必多加小心啊。\x01",
            "如果发生什么事，\x01",
            "我会马上赶过去的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F87")

    label("loc_6F2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6F87")

    #C0435
    ChrTalk(
        0xFE,
        (
            "婆婆好慢啊，\x01",
            "明明约好要一起吃饭的。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xFE,
        (
            "婆婆也上了年纪，\x01",
            "真是让人担心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F87")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_6DAD end

    def Function_22_6F8F(): pass

    label("Function_22_6F8F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7023")
    Jump("loc_706D")

    label("loc_7023")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7043")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_706D")

    label("loc_7043")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7063")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_706D")

    label("loc_7063")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_706D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    #C0437
    ChrTalk(
        0xFE,
        (
            "真是抱歉啊，出门的时间\x01",
            "稍微晚了一些。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xFE,
        (
            "那么，要点些\x01",
            "什么好呢？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_6F8F end

    def Function_23_70E6(): pass

    label("Function_23_70E6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_717A")
    Jump("loc_71C4")

    label("loc_717A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_719A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_71C4")

    label("loc_719A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_71BA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_71C4")

    label("loc_71BA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_71C4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_724C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7204")
    Call(0, 25)
    Jump("loc_7247")

    label("loc_7204")


    #C0439
    ChrTalk(
        0xFE,
        "呵呵，真是能吃呢。\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xFE,
        (
            "算了，回去之后\x01",
            "我会给你加大练习量的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7247")

    Jump("loc_7318")

    label("loc_724C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_72A7")
    SetChrSubChip(0xFE, 0x0)

    #C0441
    ChrTalk(
        0xFE,
        "什么，欢乐街可不行啊！\x02",
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xFE,
        (
            "如果出了什么问题，\x01",
            "我们会被禁止出场的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7318")

    label("loc_72A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7318")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72C2")
    Call(0, 25)
    Jump("loc_7318")

    label("loc_72C2")


    #C0443
    ChrTalk(
        0xFE,
        (
            "我们可是帝国的名门骑马俱乐部\x01",
            "『女皇』的成员哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xFE,
        (
            "为了比赛，\x01",
            "必须要养精蓄锐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7318")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_70E6 end

    def Function_24_7320(): pass

    label("Function_24_7320")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_73B4")
    Jump("loc_73FE")

    label("loc_73B4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_73D4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_73FE")

    label("loc_73D4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_73F4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_73FE")

    label("loc_73F4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_73FE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7482")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_743E")
    Call(0, 25)
    Jump("loc_747D")

    label("loc_743E")

    SetChrSubChip(0xFE, 0x0)

    #C0445
    ChrTalk(
        0xFE,
        (
            "（狼吞虎咽）\x01",
            "（大吃大嚼）……\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xFE,
        "吃完了，再来一份！\x02",
    )

    CloseMessageWindow()

    label("loc_747D")

    Jump("loc_7547")

    label("loc_7482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_74ED")
    SetChrSubChip(0xFE, 0x0)

    #C0447
    ChrTalk(
        0xFE,
        (
            "明明建筑和风景都很美，\x01",
            "但一点兴趣都没有啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xFE,
        "要是能有让人玩个痛快的地方就好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7547")

    label("loc_74ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7547")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7508")
    Call(0, 25)
    Jump("loc_7547")

    label("loc_7508")

    SetChrSubChip(0xFE, 0x0)

    #C0449
    ChrTalk(
        0xFE,
        (
            "（狼吞虎咽）\x01",
            "（大吃大嚼）……\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xFE,
        "吃完了，再来一份！\x02",
    )

    CloseMessageWindow()

    label("loc_7547")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_7320 end

    def Function_25_754F(): pass

    label("Function_25_754F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_75D7")
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)

    #C0451
    ChrTalk(
        0x16,
        "明明是来观光的，结果却成了暴食吗……\x02",
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x16,
        (
            "算啦，不管了。\x01",
            "为了比赛，必须要吃个痛快！\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x17,
        "噢，是这边点的！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_764C")

    label("loc_75D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_75E5")
    Jump("loc_764C")

    label("loc_75E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_764C")
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)

    #C0454
    ChrTalk(
        0x16,
        "要吃个痛快啊！\x02",
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x16,
        (
            "今天一天要把所有的景点\x01",
            "都给看遍啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x17,
        "噢，是这边点的！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_764C")

    Return()

    # Function_25_754F end

    def Function_26_764D(): pass

    label("Function_26_764D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_76E1")
    Jump("loc_772B")

    label("loc_76E1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7701")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_772B")

    label("loc_7701")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7721")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_772B")

    label("loc_7721")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_772B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_77D5")

    #C0457
    ChrTalk(
        0xFE,
        (
            "怎、怎么会这样。\x01",
            "我们明明是来新婚旅行的，\x01",
            "结果竟然遇到这种事……\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0xFE,
        (
            "如果不做点别的事挽回她的心，\x01",
            "可就麻烦了啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7914")

    label("loc_77D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_78BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7870")

    #C0459
    ChrTalk(
        0xFE,
        (
            "那个，接下来是去『巴鲁卡』，\x01",
            "晚上预定在高级酒店过夜……\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xFE,
        (
            "哎，预定好的酒店\x01",
            "在什么地方来着……\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xFE,
        "应该就在这附近的……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_78B5")

    label("loc_7870")


    #C0462
    ChrTalk(
        0xFE,
        (
            "真、真麻烦啊……\x01",
            "把酒店的地址给忘了。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xFE,
        "必须快点想起来啊……\x02",
    )

    CloseMessageWindow()

    label("loc_78B5")

    Jump("loc_7914")

    label("loc_78BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7914")

    #C0464
    ChrTalk(
        0xFE,
        "我是和妻子一起来新婚旅行的。\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市真是繁华啊，\x01",
            "让人目不暇接呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7914")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_764D end

    def Function_27_791C(): pass

    label("Function_27_791C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_79B0")
    Jump("loc_79FA")

    label("loc_79B0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_79D0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_79FA")

    label("loc_79D0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_79F0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_79FA")

    label("loc_79F0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_79FA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7B12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AC2")

    #C0466
    ChrTalk(
        0xFE,
        "昨天晚上在欢乐街迷路了……\x02",
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xFE,
        (
            "但还好遇到了一位漂亮少年，\x01",
            "为我带了路。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xFE,
        (
            "呼，那孩子的微笑真是让人\x01",
            "神魂颠倒，难以移开视线呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_7B0D")

    label("loc_7AC2")


    #C0469
    ChrTalk(
        0xFE,
        (
            "虽然还是个少年，\x01",
            "却有种很神秘的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xFE,
        "唉，还能不能再遇到他呢～\x02",
    )

    CloseMessageWindow()

    label("loc_7B0D")

    Jump("loc_7BE4")

    label("loc_7B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7B7F")

    #C0471
    ChrTalk(
        0xFE,
        "……从刚才开始，我老公的举动就很可疑。\x02",
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xFE,
        (
            "也许是因为第一次来外国旅行，\x01",
            "所以有些紧张吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BE4")

    label("loc_7B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7BE4")

    #C0473
    ChrTalk(
        0xFE,
        (
            "新婚旅行的日程安排，\x01",
            "我老公已经全部预约过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xFE,
        (
            "这样一来，就可以\x01",
            "尽情地四处参观了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BE4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_27_791C end

    def Function_28_7BEC(): pass

    label("Function_28_7BEC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x1A)
    ClearChrFlags(0x1A, 0x10)
    TurnDirection(0x1A, 0x0, 0)
    OP_52(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7C80")
    Jump("loc_7CCA")

    label("loc_7C80")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7CA0")
    OP_52(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7CCA")

    label("loc_7CA0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7CC0")
    OP_52(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7CCA")

    label("loc_7CC0")

    OP_52(0x1A, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7CCA")

    OP_52(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1A, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7D9A")
    SetChrSubChip(0x1A, 0x0)
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0475
    ChrTalk(
        0x1B,
        "今、今天我送你。\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x1C,
        "好……\x02",
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x1A,
        "啊啊，急死人了！！\x02",
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x1A,
        (
            "说想要在纪念庆典之前\x01",
            "把事情了结的不就是\x01",
            "你们吗！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_821B")

    label("loc_7D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7E73")
    SetChrSubChip(0x1A, 0x0)
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0479
    ChrTalk(
        0x1B,
        "……（扭扭捏捏）………………\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x1C,
        "……（扭扭捏捏）………………\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x1A,
        (
            "喂～只是相亲而已，\x01",
            "不用那么紧张啦～\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x1A,
        (
            "你们俩的家不是住得很近吗？\x01",
            "又不是以前不认识～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_821B")

    label("loc_7E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_7FB5")
    SetChrSubChip(0x1A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F82")

    #C0483
    ChrTalk(
        0x1A,
        (
            "哎～那么，\x01",
            "请两位将兴趣告诉对方……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0484
    ChrTalk(
        0x1B,
        "………读书…………吧………\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x1C,
        "…………算、算是花道呢………\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0486
    ChrTalk(
        0x1A,
        "耗费一天就只有这些吗……\x02",
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x1A,
        (
            "你们两个，\x01",
            "稍微放松一点啦……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_7FB0")

    label("loc_7F82")


    #C0488
    ChrTalk(
        0x1A,
        (
            "你们两个，\x01",
            "稍微放松一点啦……\x01",
            "拜托了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FB0")

    Jump("loc_821B")

    label("loc_7FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_80E4")
    SetChrSubChip(0x1A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8085")

    #C0489
    ChrTalk(
        0x1A,
        (
            "哎～那么，\x01",
            "自从你们两位相遇之后……\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x1B,
        "………………相、相遇…………\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x1C,
        "……………那……那个………\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0492
    ChrTalk(
        0x1A,
        (
            "……你们两个有在听吗？\x01",
            "太过紧张了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_80DF")

    label("loc_8085")


    #C0493
    ChrTalk(
        0x1A,
        (
            "哎～那么，\x01",
            "自从你们两位相遇之后……\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x1A,
        (
            "……喂，你们两个有在听吗！？\x01",
            "太过紧张了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80DF")

    Jump("loc_821B")

    label("loc_80E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_821B")
    SetChrSubChip(0x1A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81B7")

    #C0495
    ChrTalk(
        0x1A,
        "哎～今天也是个好日子……\x02",
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x1B,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x1C,
        "………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0498
    ChrTalk(
        0x1A,
        (
            "喂，你们，多少也说点什么啊！\x01",
            "这不是一点进展都没有吗～！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_821B")

    label("loc_81B7")


    #C0499
    ChrTalk(
        0x1A,
        "哎～今天也是个好日子……\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x1A,
        (
            "喂，你们不要那么紧张啦。\x01",
            "就算说是相亲，\x01",
            "但你们以前不就认识了吗～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_821B")

    SetChrSubChip(0x1A, 0x0)
    TalkEnd(0x1A)
    Return()

    # Function_28_7BEC end

    def Function_29_8223(): pass

    label("Function_29_8223")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_82B7")
    Jump("loc_8301")

    label("loc_82B7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_82D7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8301")

    label("loc_82D7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_82F7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8301")

    label("loc_82F7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8301")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_8395")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8345")
    Call(0, 28)
    Jump("loc_8390")

    label("loc_8345")

    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0501
    ChrTalk(
        0x1B,
        "今、今天我送你。\x02",
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x1C,
        "好的……\x02",
    )

    CloseMessageWindow()

    label("loc_8390")

    Jump("loc_86A3")

    label("loc_8395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8420")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83B0")
    Call(0, 28)
    Jump("loc_841B")

    label("loc_83B0")

    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0503
    ChrTalk(
        0x1B,
        "……（扭扭捏捏）………………\x02",
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x1C,
        "……（扭扭捏捏）………………\x02",
    )

    CloseMessageWindow()

    label("loc_841B")

    Jump("loc_86A3")

    label("loc_8420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_8521")

    #C0505
    ChrTalk(
        0x1A,
        (
            "哎～那么，\x01",
            "请两位将兴趣告诉对方……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0506
    ChrTalk(
        0x1B,
        "………读书…………吧………\x02",
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x1C,
        "…………算、算是花道呢………\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0508
    ChrTalk(
        0x1A,
        "耗费一天就只有这些吗……\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x1A,
        (
            "你们两个，\x01",
            "稍微放松一点啦……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_86A3")

    label("loc_8521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_85E3")

    #C0510
    ChrTalk(
        0x1A,
        (
            "哎～那么，\x01",
            "自从你们两位相遇之后……\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x1B,
        "………………相、相遇…………\x02",
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x1C,
        "……………那……那个………\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0513
    ChrTalk(
        0x1A,
        (
            "……你们两个有在听吗？\x01",
            "太过紧张了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_86A3")

    label("loc_85E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_86A3")

    #C0514
    ChrTalk(
        0x1A,
        "哎～今天也是个好日子……\x02",
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x1B,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x1C,
        "………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0517
    ChrTalk(
        0x1A,
        (
            "喂，你们，多少也说点什么啊！\x01",
            "这不是一点进展都没有吗～！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)

    label("loc_86A3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_29_8223 end

    def Function_30_86AB(): pass

    label("Function_30_86AB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_873F")
    Jump("loc_8789")

    label("loc_873F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_875F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8789")

    label("loc_875F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_877F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8789")

    label("loc_877F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8789")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8812")

    #C0518
    ChrTalk(
        0xFE,
        (
            "我昨天终于去看了\x01",
            "彩虹剧团的表演哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xFE,
        (
            "果然很棒呢～\x01",
            "必须要买本纪念资料集回去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88EE")

    label("loc_8812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_88EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88A2")

    #C0520
    ChrTalk(
        0xFE,
        (
            "虽然纪念庆典已经结束了，\x01",
            "但我们还是滞留在这里哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xFE,
        (
            "因为还没有去过米修拉姆，\x01",
            "也还没有看过\x01",
            "彩虹剧团的表演呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_88EE")

    label("loc_88A2")


    #C0522
    ChrTalk(
        0xFE,
        (
            "至少也要去米修拉姆玩一次\x01",
            "才能回去～\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xFE,
        (
            "必须要尽情地\x01",
            "购物一番才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88EE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_86AB end

    def Function_31_88F6(): pass

    label("Function_31_88F6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_898A")
    Jump("loc_89D4")

    label("loc_898A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_89AA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_89D4")

    label("loc_89AA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89CA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_89D4")

    label("loc_89CA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_89D4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8A5F")

    #C0524
    ChrTalk(
        0xFE,
        (
            "刚才有个厨师\x01",
            "一直在我眼前转。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xFE,
        (
            "和他目光相对之后，还向我挥手，\x01",
            "究竟想干什么……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8ACF")

    label("loc_8A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8ACF")

    #C0526
    ChrTalk(
        0xFE,
        (
            "我的目标是\x01",
            "彩虹剧团的门票。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0xFE,
        (
            "根据我的计算，\x01",
            "如果是这个月的票，\x01",
            "应该还能在别的什么地方弄到手～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8ACF")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_88F6 end

    def Function_32_8AD7(): pass

    label("Function_32_8AD7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8B57")

    #C0528
    ChrTalk(
        0xFE,
        (
            "那么～还是先在市内\x01",
            "观光一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xFE,
        (
            "虽然听说克洛斯贝尔的治安\x01",
            "不太好，不过算了，\x01",
            "应该也不会遇到什么危险。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C6C")

    label("loc_8B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8C6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C30")

    #C0530
    ChrTalk(
        0xFE,
        (
            "我是今天早上乘列车到克洛斯贝尔的。\x01",
            "终于可以吃上一些美味的食物了～\x01",
            "虽然是这么想的……\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xFE,
        (
            "……但厨师竟然给我\x01",
            "拿来了一些奇怪的料理。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0xFE,
        (
            "这到底是怎么回事，\x01",
            "难道是把我点的菜搞错了吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_8C6C")

    label("loc_8C30")


    #C0533
    ChrTalk(
        0xFE,
        (
            "嗯～这到底是怎么回事嘛。\x01",
            "果然是把我\x01",
            "点的菜搞错了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C6C")

    TalkEnd(0xFE)
    Return()

    # Function_32_8AD7 end

    def Function_33_8C70(): pass

    label("Function_33_8C70")

    TalkBegin(0xFE)
    Call(0, 34)
    TalkEnd(0xFE)
    Return()

    # Function_33_8C70 end

    def Function_34_8C7A(): pass

    label("Function_34_8C7A")

    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xD)
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0xB, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D0E")
    Jump("loc_8D58")

    label("loc_8D0E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8D2E")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D58")

    label("loc_8D2E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D4E")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D58")

    label("loc_8D4E")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8D58")

    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)
    OP_4B(0xD, 0xFF)
    OP_4B(0xB, 0xFF)
    SetChrSubChip(0xD, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_8E11")

    #C0534
    ChrTalk(
        0xD,
        (
            "#2100F那么，去市政厅的接待处，\x01",
            "申请再看一下名册……\x02\x03",

            "#2103F嗯～在昨天已经全部\x01",
            "复制了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0xB,
        "真是的，快点给我看吧～\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EF5")

    label("loc_8E11")


    #C0536
    ChrTalk(
        0xD,
        (
            "#2100F没错没错，就是\x01",
            "照片这边的这个人。\x02\x03",

            "是不是感觉曾经见过这个人呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xB,
        "啊～或许吧。\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xB,
        (
            "好像是个看上去很傲气\x01",
            "的中年大叔……\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xB,
        "究竟是谁呢？\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0xD,
        (
            "#2100F呵呵，秘密。\x02\x03",

            "不过，如果能成为爆炸性新闻，\x01",
            "会赠你一份谢礼哦～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)

    label("loc_8EF5")

    OP_4C(0xD, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_34_8C7A end

    def Function_35_8EFE(): pass

    label("Function_35_8EFE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 7)), scpexpr(EXPR_END)), "loc_8FB6")
    TurnDirection(0xFE, 0x0, 0)

    #C0541
    ChrTalk(
        0xFE,
        (
            "纪念庆典之后，听说你们和黑手党\x01",
            "之间产生了纠纷呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xFE,
        (
            "之后又没有再听到新的消息，\x01",
            "所以有些担心呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0xFE,
        (
            "算了，没事就好。\x01",
            "要努力做好警察的工作哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x5A, 0x0)
    Jump("loc_9247")

    label("loc_8FB6")


    #C0544
    ChrTalk(
        0xFE,
        "（惊恐）……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 500)
    Sleep(300)

    #C0545
    ChrTalk(
        0xFE,
        "你、你好啊，缇欧……\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x103,
        "#0200F主任，好久不见呢。\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x101,
        (
            "#0000F您好像是爱普斯泰恩财团的……\x02\x03",

            "……那个，\x01",
            "又是来为缇欧提供武器的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xFE,
        (
            "那、那个嘛，我听说你们支援科\x01",
            "被卷进了危险的事件中……\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xFE,
        (
            "……咳，只是来与店主\x01",
            "闲聊一下的，\x01",
            "真的仅此而已啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x103,
        (
            "#0203F………………………………\x01",
            "让您担心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x104,
        (
            "#0300F哈，虽然经历了很多，\x01",
            "但已经没事啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x102,
        (
            "#0100F嗯，在最近这两三周，\x01",
            "总算是完全平静下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0xFE,
        "是、是吗……那就好。\x02",
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0xFE,
        (
            "缇欧，我带来了\x01",
            "最新型的魔导杖。\x01",
            "请务必要使用！\x02",
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

    #C0555
    ChrTalk(
        0x103,
        (
            "#0211F果然还是\x01",
            "带到这里来了呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x5A, 0x0)
    SetScenarioFlags(0xD0, 7)

    label("loc_9247")

    TalkEnd(0xFE)
    Return()

    # Function_35_8EFE end

    def Function_36_924B(): pass

    label("Function_36_924B")

    EventBegin(0x0)
    Fade(500)
    OP_68(58650, 500, -8880, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 58000, -1000, -9000, 90)
    SetChrPos(0x102, 57900, -1000, -8200, 90)
    SetChrPos(0x103, 56550, -1000, -9000, 90)
    SetChrPos(0x104, 56450, -1000, -8200, 90)
    OP_93(0x20, 0x10E, 0x0)
    SetChrSubChip(0x20, 0x0)
    OP_0D()

    #C0556
    ChrTalk(
        0x20,
        (
            "#11P对了对了，刚才有个\x01",
            "看起来像是技术员的男人来了。\x01",
            "把一个叫『魔导杖』的东西放在了这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x20,
        "#11P说是什么新开发的武器吧……\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x20,
        (
            "#11P但这种莫名其妙的东西，\x01",
            "要我卖给谁啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0559
    ChrTalk(
        0x102,
        (
            "#0105F#5P魔导杖？应该是……\x01",
            "缇欧用的\x01",
            "武器吧？\x02\x03",

            "听说是还在\x01",
            "实验中的东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x104,
        (
            "#0305F#5P为什么那种东西\x01",
            "会被卖到这里呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x101,
        (
            "#0001F#5P看起来像是技术员的男人……吗。\x01",
            "稍微有些可疑啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x103,
        (
            "#0206F#6P那个……\x01",
            "我想那个人多半是我的上司。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_94C8():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_94C8)
    Sleep(50)

    def lambda_94D8():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_94D8)
    Sleep(50)

    def lambda_94E8():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_94E8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0563
    ChrTalk(
        0x104,
        "#0305F#5P哎，上司……？\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x103,
        (
            "#0211F#6P……嗯，我想他恐怕是\x01",
            "来这里送魔导杖的\x01",
            "改良试用版的。\x02\x03",

            "#0206F明明直接交给我就好了\x01",
            "（自言自语）……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0565
    ChrTalk(
        0x101,
        (
            "#0012F#11P（那个……\x01",
            "  为什么不来直接交给你呢？）\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x20,
        (
            "#11P虽然不是很明白……\x01",
            "不过，把这武器卖给\x01",
            "小姑娘就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x20,
        (
            "#11P那就赶快买走吧。\x01",
            "再怎么说，我也是付钱收来的啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 58000, -1000, -8600, 90)
    SetScenarioFlags(0x4C, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_96A6")
    SetScenarioFlags(0x4C, 4)

    label("loc_96A6")

    EventEnd(0x5)
    Return()

    # Function_36_924B end

    def Function_37_96A9(): pass

    label("Function_37_96A9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch06900.itc", 0x1E)
    LoadChrToIndex("chr/ch06902.itc", 0x1F)
    LoadChrToIndex("chr/ch37302.itc", 0x20)
    LoadChrToIndex("apl/ch50422.itc", 0x21)
    OP_68(6500, 1300, 9000, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrPos(0x24, 6500, 0, 7750, 0)
    SetChrPos(0x102, 6500, 0, 10250, 180)
    SetChrPos(0x103, 7750, 0, 9000, 270)
    SetChrPos(0x104, 5250, 0, 9000, 90)
    SetChrPos(0x101, 15000, 0, 9000, 270)
    SetChrPos(0x109, 17000, 0, 9000, 270)
    SetChrPos(0x19F, 16000, 0, 9000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x19F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0568
    ChrTalk(
        0x102,
        (
            "#5P#0103F……好慢啊，罗伊德他们，\x01",
            "要让我们等到什么时候啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x103,
        (
            "#11P#0200F让女性等待\x01",
            "可是非常失礼的行为。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x104,
        (
            "#6P#0304F哼哼哼……\x01",
            "男人的穿着打扮，可是和女性化妆\x01",
            "一样耗时间哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x104, 500)

    #C0571
    ChrTalk(
        0x24,
        (
            "#12P#1900F嘿，兰迪先生的经验\x01",
            "好像很丰富嘛～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x24, 500)

    #C0572
    ChrTalk(
        0x104,
        (
            "#6P#0300F哈哈，看得出来啊？\x02\x03",

            "#0300F怎么样，下次和我约会吧。\x01",
            "如果是小芙兰这么可爱的女孩，\x01",
            "我一定会带你去最棒的地方哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x24,
        "#12P#1909F真是的～好会对付女孩子呀。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0574
    ChrTalk(
        0x102,
        (
            "#11P#0111F（那个……\x01",
            "  你要是在这里跟她搭讪，\x01",
            "  我们还怎么完成委托……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0575
    ChrTalk(
        0x104,
        (
            "#6P#0309F（哎呀，只是开个小玩笑啦。\x01",
            "  我是想尽量拖延时间，等罗伊德他们来啊……）\x02",
        )
    )

    CloseMessageWindow()

    #N0576
    NpcTalk(
        0x101,
        "罗伊德的声音",
        "抱歉，好像让你们久等了呢。\x02",
    )

    CloseMessageWindow()
    OP_68(7750, 1100, 9000, 3000)
    MoveCamera(33, 25, 0, 3000)

    def lambda_9A5F():
        OP_97(0x101, 0xFFFFE98A, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9A5F)

    def lambda_9A79():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9A79)
    Sleep(50)

    def lambda_9A8D():
        OP_97(0x19F, 0xFFFFE5A2, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_9A8D)

    def lambda_9AA7():
        OP_A7(0x19F, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19F, 2, lambda_9AA7)
    Sleep(50)

    def lambda_9ABB():
        OP_97(0x109, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9ABB)

    def lambda_9AD5():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9AD5)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_9B31():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9B31)
    Sleep(50)

    def lambda_9B41():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9B41)
    Sleep(50)

    def lambda_9B51():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9B51)
    Sleep(50)

    def lambda_9B61():
        OP_93(0x24, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_9B61)
    WaitChrThread(0x101, 1)

    def lambda_9B72():
        OP_97(0x101, 0x0, 0x0, 0x2EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B72)
    WaitChrThread(0x19F, 1)

    def lambda_9B90():
        OP_97(0x19F, 0x0, 0x0, 0xFFFFFB1E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_9B90)
    WaitChrThread(0x101, 1)

    def lambda_9BAE():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9BAE)
    WaitChrThread(0x19F, 1)

    def lambda_9BBF():
        OP_93(0x19F, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_9BBF)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x24, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x19F, 1)
    OP_6F(0x79)

    #C0577
    ChrTalk(
        0x24,
        (
            "#6P#1905F啊，是罗伊德警官和姐姐。\x01",
            "还有……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0578
    ChrTalk(
        0x19F,
        (
            "#11P那、那个……\x01",
            "你、你好啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x19F)

    #C0579
    ChrTalk(
        0x19F,
        (
            "#11P好久不……啊，不对，\x01",
            "那个，让你久等了，\x01",
            "很抱歉啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x24,
        "#6P#1900F安敦先生，您好。\x02",
    )

    CloseMessageWindow()
    OP_63(0x19F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0581
    ChrTalk(
        0x19F,
        (
            "#11P为为为……\x01",
            "为什么……会知道我的名字！？\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x24,
        (
            "#6P#1900F啊，之前罗伊德警官他们\x01",
            "已经告诉我了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x19F,
        (
            "#11P哈、哈哈……是这样啊……\x01",
            "（一阵空欢喜啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x102,
        (
            "#5P#0111F（我说……\x01",
            "  有点太慢了啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x101,
        (
            "#11P#0006F（抱、抱歉，\x01",
            "  选礼物花费了\x01",
            "  不少时间呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x103,
        (
            "#12P#0200F（看样子，应该已经\x01",
            "  选好了吧。）\x02\x03",

            "（买到称心的好礼物了吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x109,
        (
            "#11P#0500F（嗯……\x01",
            "  算是吧，至少我觉得\x01",
            "  不会太奇怪。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x24, 500)
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x104)

    #C0588
    ChrTalk(
        0x104,
        (
            "#6P#0304F好了好了，你们两位，\x01",
            "有什么话都先\x01",
            "坐下再说吧。\x02\x03",

            "#0300F小芙兰的\x01",
            "休息时间\x01",
            "也没有多长吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x104, 500)

    #C0589
    ChrTalk(
        0x24,
        "#12P#1905F啊，说得也是呢～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x19F, 500)

    #C0590
    ChrTalk(
        0x24,
        (
            "#6P#1900F……那么，安敦先生，\x01",
            "先坐下好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x19F,
        "#11P好、好的！\x02",
    )

    CloseMessageWindow()

    def lambda_9F50():
        OP_97(0x24, 0xFFFFE0C0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_9F50)
    Sleep(50)

    def lambda_9F6D():
        OP_97(0x19F, 0xFFFFE0C0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_9F6D)
    Sleep(500)

    def lambda_9F8A():
        OP_93(0x101, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9F8A)

    def lambda_9F97():
        OP_93(0x102, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9F97)

    def lambda_9FA4():
        OP_93(0x103, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9FA4)

    def lambda_9FB1():
        OP_93(0x104, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9FB1)

    def lambda_9FBE():
        OP_93(0x109, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9FBE)
    WaitChrThread(0x24, 1)
    WaitChrThread(0x19F, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    TurnDirection(0x104, 0x101, 500)

    #C0592
    ChrTalk(
        0x104,
        (
            "#6P#0304F……那么，我们差不多\x01",
            "也该去二层了吧。\x02\x03",

            "#0300F我们要是在这里看着，\x01",
            "他们大概会有很多不便吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A057():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A057)

    def lambda_A064():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A064)

    def lambda_A071():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A071)

    def lambda_A07E():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A07E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x109, 1)

    #C0593
    ChrTalk(
        0x101,
        "#11P#0005F你、你是打算暗中偷窥吗……？\x02",
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x104,
        (
            "#6P#0309F那当然，你也很在意\x01",
            "接下来将会怎样发展吧～？\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x103,
        (
            "#12P#0204F守护委托人到最后\x01",
            "也是我们的义务嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x102,
        (
            "#5P#0100F呵呵，也对，\x01",
            "这也是正当权利呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x109,
        (
            "#11P#0506F……抱歉，\x01",
            "说实话，我也很在意。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    TurnDirection(0x101, 0x109, 500)
    Sleep(500)

    #C0598
    ChrTalk(
        0x101,
        (
            "#5P#0003F连上士都……\x02\x03",

            "#0000F算了，也有道理啊……\x01",
            "安敦先生看起来好像都\x01",
            "紧张得不知所措了……\x02\x03",

            "为了防止他有什么失态，\x01",
            "我们还是看下去比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x104,
        (
            "#6P#0309F很好～既然已经决定了，\x01",
            "那就赶快走吧☆\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0600
    ChrTalk(
        0x101,
        "#11P#0006F（大家都是一副乐在其中的样子呢……）\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(2000, 6500, 9730, 0)
    MoveCamera(48, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrChipByIndex(0x19F, 0x20)
    SetChrSubChip(0x19F, 0x0)
    SetChrFlags(0x19F, 0x4)
    SetChrFlags(0x19F, 0x8000)
    SetChrChipByIndex(0x24, 0x1F)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x19F, -1100, 150, 2300, 270)
    SetChrPos(0x24, -5350, 50, 2300, 90)
    SetChrPos(0x101, 0, 5000, 10000, 180)
    SetChrPos(0x102, 750, 5000, 9750, 180)
    SetChrPos(0x104, 1500, 5000, 10000, 180)
    SetChrPos(0x109, -750, 5000, 9750, 180)
    SetChrPos(0x103, -1500, 5000, 10000, 180)
    OP_68(0, 6500, 9750, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    StopBGM(0x157C)
    OP_6F(0x79)
    Fade(500)
    OP_68(-3240, 1100, 2340, 0)
    MoveCamera(36, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19950, 0)
    SetCameraDistance(19000, 3000)
    OP_0D()
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7105", 0)

    #C0601
    ChrTalk(
        0x19F,
        (
            "#11P那、那个……芙兰小姐\x01",
            "对我还有什么印象吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x24,
        (
            "#6P#1909F呵呵，发生在纪念庆典，\x01",
            "而且还是最终日的事情，\x01",
            "当然记得啦～\x02\x03",

            "#1900F那天还真是麻烦呢～\x01",
            "之后您没有再丢钱包吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x19F,
        "#11P当、当然了！\x02",
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x19F,
        (
            "#11P因为是芙兰小姐\x01",
            "那么辛苦才帮我找到的，\x01",
            "我绝对不会再将它弄丢！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x24)

    #C0605
    ChrTalk(
        0x24,
        (
            "#6P#1909F啊哈哈，安敦先生\x01",
            "还真是有趣啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x19F,
        (
            "#11P（太、太好了……\x01",
            "  虽然还不是很明白，\x01",
            "  但她好像对我挺有好感……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x24,
        (
            "#6P#1905F说起来，安敦先生，\x01",
            "在找到钱包之后，\x01",
            "您好像发了好一阵子呆呢。\x02\x03",

            "#1900F我还担心您是不是\x01",
            "突然发了高烧什么的。\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x19F,
        (
            "#11P#2S那一定是因为看你\x01",
            "看到发呆了啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x24, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0609
    ChrTalk(
        0x24,
        "#6P#1905F啊？您刚才说了什么吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x19F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0610
    ChrTalk(
        0x19F,
        (
            "#11P啊，没、没什么！\x01",
            "啊哈哈……\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xFFFF)
    Fade(500)
    OP_68(0, 6500, 9730, 0)
    MoveCamera(48, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20000, 0)
    OP_0D()

    #C0611
    ChrTalk(
        0x104,
        (
            "#5P#0304F哈哈，安敦他\x01",
            "还嫩得很啊。\x02\x03",

            "#0300F如果连那种甜言蜜语\x01",
            "都不能顺利说出来，\x01",
            "可没法追到姑娘哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x101,
        (
            "#5P#0000F说起来……\x01",
            "芙兰的态度\x01",
            "相当温和自然呢。\x02\x03",

            "#0012F而安敦先生还是\x01",
            "一直很紧张，好像\x01",
            "已经完全手足无措了……\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x109,
        (
            "#5P#0503F……芙兰的社交能力\x01",
            "要比我更高。\x02\x03",

            "#0500F即使与对方是初次见面，\x01",
            "她也能以亲切的态度来应对。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x109, 500)
    Sleep(150)

    #C0614
    ChrTalk(
        0x103,
        (
            "#6P#0205F……总觉得诺艾尔上士\x01",
            "有些奇怪啊。\x02\x03",

            "#0200F你的心情好像\x01",
            "不太好吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x109, 0x103, 500)
    Sleep(750)
    OP_64(0x109)

    #C0615
    ChrTalk(
        0x109,
        (
            "#11P#0502F那个，不是的。\x01",
            "也不能说是\x01",
            "心情不好……\x02\x03",

            "#0506F该怎么说呢……\x01",
            "那孩子虽然很招人喜欢，\x01",
            "但至今为止从没有过恋爱经历。\x02\x03",

            "#0508F可是，她好像却对\x01",
            "安敦先生有些莫名的好感……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    #C0616
    ChrTalk(
        0x102,
        (
            "#11P#0102F呵呵，诺艾尔上士，\x01",
            "你好像很担心芙兰啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    #C0617
    ChrTalk(
        0x109,
        (
            "#6P#0505F……那、那个……\x02\x03",

            "#0504F……哈哈，是啊，\x01",
            "毕竟是唯一的妹妹……\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x101,
        (
            "#5P#0000F（这就是身为姐姐的关心吗……）\x02\x03",

            "#0006F（塞茜尔姐姐或许\x01",
            "  也是这样担心着我的吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0x104,
        (
            "#5P#0305F──噢噢，快看！\x01",
            "安敦一副下定决心的表情呢。\x02\x03",

            "#0309F那家伙，\x01",
            "差不多该准备一决胜负了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_AAF1():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AAF1)

    def lambda_AAFE():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AAFE)

    def lambda_AB0B():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AB0B)
    Sleep(1000)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x102, 1)
    Fade(500)
    OP_68(-3240, 1100, 2340, 0)
    MoveCamera(36, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19950, 0)
    OP_0D()
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    OP_64(0x24)
    OP_63(0x19F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    OP_64(0x19F)
    OP_63(0x19F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x19F)

    #C0620
    ChrTalk(
        0x19F,
        "#11P……那、那个……芙兰小姐！\x02",
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0x24,
        "#6P#1905F嗯，有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x19F,
        (
            "#11P其实，我找你并没有\x01",
            "什么别的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x19F,
        (
            "#11P只是，你在纪念庆典时那么\x01",
            "拼命地帮我寻找钱包……\x01",
            "作为答谢，我希望能回赠你一份礼物。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x19F,
        "#11P可不可以请你收下这个呢？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_ADD7")
    OP_2C(0x2A, 0x1)
    SetChrName("")

    #A0625
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "安敦将『咪西玩偶』交给了芙兰。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0626
    ChrTalk(
        0x24,
        (
            "#6P#1905F这是……\x01",
            "这不是\x01",
            "咪西玩偶吗？\x02\x03",

            "#1909F哇，谢谢您！\x02\x03",

            "虽然我已经有一个了……\x01",
            "但正好还想再\x01",
            "要一个呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x19F,
        (
            "#11P（已、已经有了吗……？\x01",
            "  虽然看起来还是很开心，\x01",
            "  但这情况真是在预料之外！）\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x19F,
        (
            "#11P（……不管了，\x01",
            "  是成是败，关键就看现在了！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B34B")

    label("loc_ADD7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_AF0E")
    SetChrName("")

    #A0629
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "安敦将『清凉果酱』交给了芙兰。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0630
    ChrTalk(
        0x24,
        (
            "#6P#1905F这是……\x01",
            "只有百货店里才有的\x01",
            "稀有进口果酱吧？\x02\x03",

            "#1900F呵呵，谢谢您。\x01",
            "总觉得有一种\x01",
            "收到了年终礼物的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x19F,
        (
            "#11P（年、年终礼物……\x01",
            "　难道选错礼物的风格了吗……！？）\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x19F,
        (
            "#11P（不、不过……\x01",
            "  成败就在此一举了！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B34B")

    label("loc_AF0E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_B060")
    OP_2C(0x2A, 0x3)
    SetChrName("")

    #A0633
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "安敦将『波波绒线帽』交给了芙兰。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0634
    ChrTalk(
        0x24,
        (
            "#6P#1905F哇哇，这是……\x01",
            "白色波波的绒线帽吗？\x02\x03",

            "#1900F姐姐在穿便装时\x01",
            "就喜欢戴\x01",
            "白色的帽子。\x02\x03",

            "所以我一直也\x01",
            "都想要个\x01",
            "白色的帽子呢。\x02\x03",

            "#1909F谢谢您，\x01",
            "我会好好珍惜的～！\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x19F,
        (
            "#11P（噢噢……\x01",
            "  她很高兴呢！）\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0x19F,
        (
            "#11P（好、好的！\x01",
            "  成败就在此一举了！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B34B")

    label("loc_B060")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_B1D9")
    SetChrName("")

    #A0637
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "安敦将『斯托雷加长靴』交给了芙兰。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0638
    ChrTalk(
        0x24,
        (
            "#6P#1905F这是……\x01",
            "斯托雷加公司新出的款式吗？\x02\x03",

            "#1900F这个款式现在确实也\x01",
            "很受女孩子的欢迎呢。\x01",
            "我见过有女孩穿着它呢～\x02\x03",

            "我虽然\x01",
            "不怎么习惯穿长靴……\x01",
            "但一定会好好珍惜的。\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x19F,
        (
            "#11P（不、不习惯穿长靴……！\x01",
            "  好、好像是选了\x01",
            "  不太适合的礼物吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0x19F,
        (
            "#11P（不、不过……\x01",
            "  成败就在此一举了！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B34B")

    label("loc_B1D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_B34B")
    SetChrName("")

    #A0641
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "安敦将饰品『粉色月亮』交给了芙兰。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0642
    ChrTalk(
        0x24,
        (
            "#6P#1905F这是……\x01",
            "以前在杂志上看到过，\x01",
            "是相当高档的项链吧……！？\x02\x03",

            "这、这有点……\x01",
            "收下这么昂贵的东西\x01",
            "真的好吗？\x02\x03",

            "#1900F谢、谢谢您。\x01",
            "那个……我一定会好好珍惜的。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x19F,
        (
            "#11P（作、作为初次赠送\x01",
            "  的礼物，这种东西好像\x01",
            "  太过贵重了吧……！？）\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x19F,
        (
            "#11P（不、不过……\x01",
            "  成败就在此一举了！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B34B")


    #C0645
    ChrTalk(
        0x19F,
        (
            "#11P芙、芙兰小姐……！\x01",
            "你现在，有没有恋人呢！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x24, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x24)
    OP_63(0x24, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0646
    ChrTalk(
        0x24,
        (
            "#6P#1905F那个～……\x01",
            "恋人倒是没有哦。\x02\x03",

            "#1904F不过……\x02\x03",

            "#1909F有非常喜欢的人呢⊥\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    StopBGM(0x1F4)
    Sound(889, 0, 100, 0)

    #C0647
    ChrTalk(
        0x19F,
        "#11P#4S！！！！！！！！！！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x24, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x24)
    OP_63(0x24, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0648
    ChrTalk(
        0x24,
        (
            "#6P#1905F……啊、咦？\x01",
            "安敦先生……\x01",
            "您怎么了？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x24)

    #C0649
    ChrTalk(
        0x104,
        (
            "#N#0306F（哎呀呀……\x01",
            "  面对超直接的问题，\x01",
            "  报以超直接的回答吗？）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0650
    ChrTalk(
        0x101,
        (
            "#N#0006F（虽然芙兰小姐并没有恶意，\x01",
            "  但似乎还是在他的伤口上撒了盐呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0651
    ChrTalk(
        0x102,
        (
            "#N#0106F（嗯～既然情况如此，\x01",
            "  我想应该是束手无策了呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0652
    ChrTalk(
        0x103,
        "#N#0203F（为他合掌默哀吧。）\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0653
    ChrTalk(
        0x109,
        "#N#0505F（…………………）\x02",
    )

    CloseMessageWindow()
    OP_5A()
    PlayBGM("ed7005", 0)

    #C0654
    ChrTalk(
        0x19F,
        "#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x19F,
        (
            "#11P…………哈、哈哈，\x01",
            "是、是这样的……啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0x19F,
        "#11P………………………………\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x19F, 0xFF)
    SetChrSubChip(0x19F, 0x0)
    SetChrPos(0x19F, -1100, 0, 3300, 270)
    Sound(820, 0, 100, 0)
    OP_0D()

    #C0657
    ChrTalk(
        0x24,
        "#6P#1905F……安敦先生？\x02",
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x19F,
        "#11P……抱歉，我必须要走了。\x02",
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0x19F,
        (
            "#11P…………芙兰小姐，\x01",
            "与那个人的关系…………请加油哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x24,
        "#6P#1905F哎……？\x02",
    )

    CloseMessageWindow()

    def lambda_B6EE():
        OP_97(0x19F, 0x1B58, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_B6EE)
    Sleep(3000)
    Fade(500)
    OP_68(7790, 1400, 6860, 0)
    MoveCamera(41, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19800, 0)
    EndChrThread(0x19F, 0x1)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrPos(0x19F, 7000, 0, 9000, 0)
    SetChrPos(0x24, 0, 0, 9000, 0)
    SetChrPos(0x101, 8500, 0, 4750, 0)
    SetChrPos(0x109, 7750, 0, 3750, 0)
    SetChrPos(0x102, 9250, 0, 4250, 0)
    SetChrPos(0x103, 7750, 0, 2750, 0)
    SetChrPos(0x104, 9250, 0, 3250, 0)

    def lambda_B7BD():
        OP_97(0x19F, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_B7BD)

    def lambda_B7D7():
        OP_97(0x101, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B7D7)
    Sleep(30)

    def lambda_B7F4():
        OP_97(0x109, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B7F4)
    Sleep(30)

    def lambda_B811():
        OP_97(0x102, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B811)
    Sleep(30)

    def lambda_B82E():
        OP_97(0x103, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B82E)
    Sleep(30)

    def lambda_B84B():
        OP_97(0x104, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B84B)
    OP_0D()
    WaitChrThread(0x19F, 1)
    OP_93(0x19F, 0xB4, 0x1F4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_B8FE")

    #C0661
    ChrTalk(
        0x19F,
        "#5P……啊，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x19F,
        (
            "#5P多谢你们的帮忙。\x01",
            "……托你们的福，\x01",
            "我看到了芙兰小姐发自内心的美丽笑容哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BABE")

    label("loc_B8FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_B96B")

    #C0663
    ChrTalk(
        0x19F,
        "#5P……啊，是你们吗。\x02",
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x19F,
        (
            "#5P连选礼物都让你们陪我一起，\x01",
            "实在是麻烦你们了，不好意思。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BABE")

    label("loc_B96B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_B9E9")

    #C0665
    ChrTalk(
        0x19F,
        "#5P……啊，是你们吗。\x02",
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x19F,
        (
            "#5P多谢你们的帮忙。\x01",
            "……托你们的福，\x01",
            "我看到了芙兰小姐发自内心的美丽笑容哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BABE")

    label("loc_B9E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_BA56")

    #C0667
    ChrTalk(
        0x19F,
        "#5P……啊，是你们吗。\x02",
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x19F,
        (
            "#5P连选礼物都让你们陪我一起，\x01",
            "实在是麻烦你们了，不好意思。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BABE")

    label("loc_BA56")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_BABE")

    #C0669
    ChrTalk(
        0x19F,
        "#5P……啊，是你们吗。\x02",
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x19F,
        (
            "#5P连选礼物都让你们陪我一起，\x01",
            "实在是麻烦你们啦，不好意思。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BABE")


    #C0671
    ChrTalk(
        0x101,
        (
            "#12P#0006F安、安敦先生……\x01",
            "该怎么说呢，那个……\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x19F,
        (
            "#5P……呼……\x01",
            "用不着安慰我啦，\x01",
            "我已经习惯了。\x02",
        )
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x19F,
        (
            "#5P我的人生，一直都是这样，\x01",
            "永远永远，都在重复着\x01",
            "选择＆错误这个过程啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0674
    ChrTalk(
        0x103,
        "#12P#0206F……不太明白您在说什么。\x02",
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x19F,
        "#5P呵呵……我注意到了。\x02",
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x19F,
        (
            "#5P在说『非常喜欢的人』时，\x01",
            "芙兰小姐那副\x01",
            "平和安心的表情……\x02",
        )
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x19F,
        (
            "#5P看到她那样的表情，\x01",
            "我也只能放弃了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0678
    ChrTalk(
        0x19F,
        "#5P…………总之，就是这么回事。\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)

    def lambda_BCB9():
        OP_97(0x19F, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_BCB9)
    Sleep(1000)

    def lambda_BCD6():
        OP_93(0x101, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BCD6)
    Sleep(50)

    def lambda_BCE6():
        OP_93(0x102, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BCE6)
    Sleep(50)

    def lambda_BCF6():
        OP_93(0x103, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BCF6)
    Sleep(50)

    def lambda_BD06():
        OP_93(0x104, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BD06)
    Sleep(50)

    def lambda_BD16():
        OP_93(0x109, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BD16)
    Sleep(1000)

    def lambda_BD26():
        OP_A7(0x19F, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19F, 2, lambda_BD26)
    WaitChrThread(0x19F, 1)
    WaitChrThread(0x19F, 2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    #C0679
    ChrTalk(
        0x104,
        "#12P#0306F哎呀呀，真是重大打击啊。\x02",
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x102,
        (
            "#12P#0100F不过他看上去意外地坚强呢，\x01",
            "我想应该不要紧吧……\x02",
        )
    )

    CloseMessageWindow()

    #N0681
    NpcTalk(
        0x24,
        "芙兰的声音",
        (
            "哎～\x01",
            "安敦先生果然\x01",
            "已经回去了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_BE45():
        OP_93(0x101, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE45)

    def lambda_BE52():
        OP_93(0x102, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BE52)

    def lambda_BE5F():
        OP_93(0x103, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BE5F)

    def lambda_BE6C():
        OP_93(0x104, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BE6C)

    def lambda_BE79():
        OP_93(0x109, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BE79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)

    def lambda_BE8E():
        OP_97(0x24, 0x2134, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_BE8E)
    Sleep(2500)

    def lambda_BEAB():
        OP_93(0x101, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BEAB)
    Sleep(50)

    def lambda_BEBB():
        OP_93(0x102, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BEBB)
    Sleep(50)

    def lambda_BECB():
        OP_93(0x103, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BECB)
    Sleep(50)

    def lambda_BEDB():
        OP_93(0x104, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BEDB)
    Sleep(50)

    def lambda_BEEB():
        OP_93(0x109, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BEEB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x24, 1)
    OP_93(0x24, 0xB4, 0x1F4)

    #C0682
    ChrTalk(
        0x24,
        (
            "#5P#1905F嗯～大概快到\x01",
            "回程飞行船的起飞时间了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0x109,
        "#6P#0507F芙、芙兰！\x02",
    )

    CloseMessageWindow()
    OP_97(0x109, 0x0, 0x0, 0xCB2, 0x1388, 0x0)
    TurnDirection(0x109, 0x24, 0)
    TurnDirection(0x24, 0x109, 500)

    #C0684
    ChrTalk(
        0x24,
        (
            "#11P#1905F姐姐……？\x01",
            "你怎么了，一脸惊慌的样子……\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x109,
        (
            "#6P#0503F芙兰……\x02\x03",

            "#0501F#4S你非常喜欢的那个人到底是谁！？\x02\x03",

            "#0501F#4S莫非是罗伊德警官吗！？\x02\x03",

            "#0505F#4S难道是……兰迪前辈吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0686
    ChrTalk(
        0x101,
        "#12P#0011F上、上士……！？\x02",
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x103,
        (
            "#12P#0206F（……从刚刚开始\x01",
            "  就一直默不作声……\x01",
            "  原来是一直在想这件事啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x104,
        (
            "#11P#0309F哈，哎呀呀～\x01",
            "既然都暴露了，我也只能──\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0689
    ChrTalk(
        0x102,
        (
            "#5P#0109F……兰迪？\x01",
            "如果你又想说什么奇怪的话，\x01",
            "最好还是不要开口了。\x02",
        )
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x104,
        "#11P#0306F（好、好可怕的笑容……）\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x1F4)

    #C0691
    ChrTalk(
        0x109,
        (
            "#6P#0508F芙兰明明什么都会告诉我，\x01",
            "但这次竟然悄悄有了最喜欢的人……\x02\x03",

            "#0510F难、难道是那种见不得人\x01",
            "的问题人物吗……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x24,
        (
            "#11P#1906F稍、稍微冷静一下啊～\x01",
            "大家都在看着呢～……\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x109,
        (
            "#6P#0501F总之，那个人是谁？\x01",
            "马上告诉姐姐啦！\x02\x03",

            "不要管其他人，把他们\x01",
            "都当成是土豆什么的就好！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x24, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0694
    ChrTalk(
        0x24,
        (
            "#11P#1906F真是的，姐姐……\x01",
            "拿你没办法啊。\x02\x03",

            "#1900F嗯，那么……\x01",
            "我给个提示吧。\x02\x03",

            "#1904F……那个人，\x01",
            "在警备队中工作。\x01",
            "正义感非常强……\x02\x03",

            "#1902F而且，一直都对我\x01",
            "非常温柔体贴。\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x109,
        (
            "#6P#0505F警、警备队……！？\x01",
            "莫非是唐古拉姆门这边的人吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x24,
        "#11P#1909F……嗯⊥\x02",
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0x109,
        (
            "#6P#0506F怎、怎么会……\x01",
            "警备队里竟然会有那种人……！\x02\x03",

            "#0508F是杰克队员……还是巴雷尔队员！？\x01",
            "不，难道是食堂的提马斯先生吗……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x101,
        "#12P#0006F好、好像一发不可收拾了呢……\x02",
    )

    CloseMessageWindow()
    OP_63(0x24, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0699
    ChrTalk(
        0x24,
        (
            "#11P#1906F呼……\x01",
            "姐姐还真是意外地\x01",
            "迟钝呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0700
    ChrTalk(
        0x109,
        "#6P#0501F哎……\x02",
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x24,
        (
            "#11P#1902F真是的，非要让我说得这么明白吗～\x02\x03",

            "#1909F那个人……\x01",
            "当然就是姐姐你了嘛⊥\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0702
    ChrTalk(
        0x109,
        "#6P#0505F#4S……哎？\x02",
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x24,
        (
            "#11P#1905F……啊，不好，\x01",
            "休息时间马上就要结束了！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x101, 500)

    #C0704
    ChrTalk(
        0x24,
        (
            "#5P#1909F各位，那就先这样吧，\x01",
            "我先告辞了！\x02",
        )
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x101,
        (
            "#12P#0012F啊……嗯，\x01",
            "路上小心哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C714():
        OP_97(0x24, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_C714)
    Sleep(1000)

    def lambda_C731():
        OP_93(0x101, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C731)
    Sleep(50)

    def lambda_C741():
        OP_93(0x102, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C741)
    Sleep(50)

    def lambda_C751():
        OP_93(0x103, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C751)
    Sleep(50)

    def lambda_C761():
        OP_93(0x104, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C761)
    Sleep(1000)

    def lambda_C771():
        OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_C771)
    WaitChrThread(0x19F, 1)
    WaitChrThread(0x19F, 2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0706
    ChrTalk(
        0x104,
        (
            "#12P#0304F哈哈……原来是这么回事啊。\x02\x03",

            "#0300F照这样子来看，芙兰小姐在短时间内\x01",
            "应该是与恋爱什么的无缘了吧。\x02\x03",

            "#0309F也好，这样一来，诺艾尔也就能放心了吧……\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x109, 0x21)
    Sleep(200)
    SetChrSubChip(0x109, 0x0)
    Sleep(200)
    SetChrSubChip(0x109, 0x1)
    Sound(804, 0, 100, 0)
    Sleep(200)
    SetChrSubChip(0x109, 0x2)
    Sleep(300)

    #C0707
    ChrTalk(
        0x109,
        "#5P#0506F#40W呼～～…………\x02",
    )

    CloseMessageWindow()

    def lambda_C8D3():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C8D3)
    Sleep(50)

    def lambda_C8E3():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C8E3)
    Sleep(50)

    def lambda_C8F3():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C8F3)
    Sleep(50)

    def lambda_C903():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C903)
    WaitChrThread(0x101, 1)

    def lambda_C914():
        OP_97(0x101, 0x0, 0x0, 0x640, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C914)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x109, 500)

    #C0708
    ChrTalk(
        0x101,
        "#11P#0011F那个……你没事吧，上士！？\x02",
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0x109,
        (
            "#5P#0509F啊……对、对不起，\x01",
            "总之是松了一口气……\x02",
        )
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0x102,
        (
            "#12P#0102F呵呵，你还真是\x01",
            "非常担心芙兰小姐呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x109,
        (
            "#5P#0506F一时乱了情绪……\x01",
            "让各位看到了我\x01",
            "失态的一面呢。\x02\x03",

            "#0500F不过……谢谢大家了，\x01",
            "让你们如此费心……\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x101,
        (
            "#11P#0012F哈哈……不过，\x01",
            "对安敦先生来说，\x01",
            "可真是个遗憾的结果啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x103,
        (
            "#12P#0204F对罗伊德前辈来说，\x01",
            "也是个遗憾的结果吧？\x02\x03",

            "#0202F在诺艾尔上士问芙兰小姐\x01",
            "『最喜欢的人是谁』的时候，\x01",
            "我感觉你好像有些期待呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0714
    ChrTalk(
        0x101,
        (
            "#5P#0011F怎、怎么可能啊！？\x01",
            "真是的，不要随便说一些\x01",
            "莫名其妙的话啦……\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x104,
        (
            "#12P#0304F好啦，至于安敦那边，\x01",
            "等我们稍后有空的时候\x01",
            "再去看看好了。\x02\x03",

            "#0300F话说回来，\x01",
            "这就算是将委托完成了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x101,
        (
            "#5P#0000F是啊……\x02\x03",

            "好，我们差不多也该走了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0717
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【真心的报恩】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x19F, 0x80)
    SetChrBattleFlags(0x19F, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    RemoveParty(0x9E, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_68(8500, 1500, 9000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, 8500, 0, 9000, 180)
    SetChrPos(0x1, 8500, 0, 9000, 180)
    SetChrPos(0x2, 8500, 0, 9000, 180)
    SetChrPos(0x3, 8500, 0, 9000, 180)
    OP_29(0x2A, 0x1, 0x9)
    OP_29(0x2A, 0x4, 0x10)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_37_96A9 end

    def Function_38_CD1C(): pass

    label("Function_38_CD1C")

    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x0, 0xA, 0)
    Fade(800)
    OP_68(-51320, 1500, 3430, 0)
    MoveCamera(41, 23, -2, 0)
    OP_6E(540, 0)
    SetCameraDistance(13800, 0)
    SetChrPos(0x101, -50000, 0, 3500, 270)
    SetChrPos(0x102, -48800, 0, 3500, 270)
    SetChrPos(0x103, -50000, 0, 4900, 270)
    SetChrPos(0x104, -48800, 0, 4900, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CDD0")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x109, -47860, 0, 4640, 270)
    Jump("loc_CDFB")

    label("loc_CDD0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CDFB")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, -47860, 0, 4640, 270)

    label("loc_CDFB")

    OP_0D()

    #C0718
    ChrTalk(
        0xA,
        (
            "#6P呜噢噢噢……\x01",
            "该怎么办才好啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0xA,
        (
            "#6P店长和布拉温先生\x01",
            "全都不帮我……\x02",
        )
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0x101,
        (
            "#11P#0000F那个，不好意思。\x01",
            "请问您是发出委托的\x01",
            "赛尔缇欧先生吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_68(-50110, 1300, 4210, 1000)
    OP_95(0xA, -51650, 0, 4140, 2000, 0x0)
    OP_93(0xA, 0x5A, 0x1F4)
    Sleep(200)

    #C0721
    ChrTalk(
        0xA,
        (
            "#6P噢，来了吗！！\x01",
            "你们是……那个……\x02",
        )
    )

    CloseMessageWindow()

    #C0722
    ChrTalk(
        0x103,
        (
            "#11P#0200F克洛斯贝尔警察局·特别任务支援科，\x01",
            "请多指教。\x02",
        )
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0x102,
        (
            "#11P#0100F我们是来接受\x01",
            "您的委托的。\x02",
        )
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0x104,
        "#11P#0309F顾客就是神明啊。\x02",
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0x101,
        (
            "#11P#0000F那个，请多关照。\x01",
            "（最近大家越来越有商人气质了……）\x02\x03",

            "那个……您的委托内容，\x01",
            "好像是要寻找些\x01",
            "什么东西吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0xA,
        (
            "#6P没错没错，正是如此。\x01",
            "总之请帮帮我！\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0xA,
        (
            "#6P事实上，是店长要\x01",
            "我来负责研制全新的\x01",
            "菜式……\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0xA,
        (
            "#6P但我实在是想不出来啊，\x01",
            "无论怎样都会走入死路。\x02",
        )
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0x102,
        (
            "#11P#0100F原来如此……\x01",
            "这种事也是会经常发生的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x104,
        (
            "#11P#0303F既然是职业厨师，\x01",
            "只要发挥一下手艺，\x01",
            "随便做个一两道不就行了嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0xA,
        (
            "#6P不能随便做啊，因为我们\x01",
            "店里的客人中，也有不少名流呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0xA,
        (
            "#6P所以……希望\x01",
            "能够借助你们的力量。\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0xA,
        (
            "#6P听说你们是融入到市民\x01",
            "中的部门，那么，应该也会\x01",
            "经常去各种餐馆吃饭吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0xA,
        (
            "#6P……委托你们寻找的东西，\x01",
            "坦白地说，那就是在制作料理的过程中\x01",
            "所发现的『异想天开的料理』！\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x103,
        (
            "#11P#0203F『异想天开的料理』……\x02\x03",

            "#0200F原本想做蛋包饭，\x01",
            "结果却做成其它东西……\x01",
            "就是那类料理吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0xA,
        "#6P没错，那才是创意性料理的精髓！\x02",
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0xA,
        (
            "#6P它们代表着游走于失败与成功之间的微妙界线！\x01",
            "通过那些料理，一定能激发我的灵感！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0738
    ChrTalk(
        0xA,
        (
            "#6P……话说，你们也会制作料理吗？\x01",
            "太好了，这可真是让我非常期待！\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0x101,
        (
            "#11P#0012F哈哈，不过也没达到\x01",
            "能让职业厨师过目的水平啦……\x02\x03",

            "#0000F好了，情况我已经明白了。\x01",
            "只要把异想天开的料理\x01",
            "带来就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0xA,
        (
            "#6P是啊，因为要进行多方比较尝试，\x01",
            "所以希望你们最少能带来十种。\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0xA,
        (
            "#6P不过……\x01",
            "自然是越多越好啦，\x01",
            "请尽量帮我多收集一些吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0xA,
        (
            "#6P那么，万事拜托啦！\x01",
            "我期待着你们的好消息！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0743
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻求创造性料理！】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, -50150, 0, 4140, 270)
    SetChrPos(0xA, -52030, 0, 3650, 270)
    OP_4C(0xA, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D546")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_D546")

    OP_29(0x29, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_38_CD1C end

    def Function_39_D54F(): pass

    label("Function_39_D54F")

    TalkEnd(0xFE)
    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    Fade(800)
    OP_68(-50110, 1300, 4210, 0)
    MoveCamera(41, 23, -2, 0)
    OP_6E(540, 0)
    SetCameraDistance(13800, 0)
    SetChrPos(0x101, -50000, 0, 3500, 270)
    SetChrPos(0x102, -48800, 0, 3500, 270)
    SetChrPos(0x103, -50000, 0, 4900, 270)
    SetChrPos(0x104, -48800, 0, 4900, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D5FF")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x109, -47860, 0, 4640, 270)
    Jump("loc_D62A")

    label("loc_D5FF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D62A")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, -47860, 0, 4640, 270)

    label("loc_D62A")

    SetChrPos(0xA, -51650, 0, 4140, 90)
    OP_0D()

    #C0744
    ChrTalk(
        0xA,
        (
            "#6P好，那么就赶快\x01",
            "交给我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D6B3")

    #C0745
    ChrTalk(
        0xA,
        (
            "#6P嗯，虽然数量不多，\x01",
            "但其中也有能够让我受到\x01",
            "启发的料理呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D90D")

    label("loc_D6B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D713")
    OP_2C(0x29, 0x2)

    #C0746
    ChrTalk(
        0xA,
        (
            "#6P嗯……这些就足够了。\x01",
            "嘿嘿，我要努力试吃，\x01",
            "然后做出更好的料理！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D90D")

    label("loc_D713")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D784")
    OP_2C(0x29, 0x4)

    #C0747
    ChrTalk(
        0xA,
        (
            "#6P竟然能拿来\x01",
            "这么多种……\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0xA,
        (
            "#6P实在是太棒了！\x01",
            "这样一来，绝对能做出崭新的料理！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D90D")

    label("loc_D784")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D90D")
    OP_2C(0x29, 0x6)

    #C0749
    ChrTalk(
        0xA,
        (
            "#6P不过……你们究竟是什么人啊？\x01",
            "竟然能将一切料理都网罗在手，\x01",
            "收集得如此齐全……\x02",
        )
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0xA,
        (
            "#6P简直就是对克洛斯贝尔\x01",
            "的一切料理都知无不尽啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0x101,
        (
            "#11P#0000F哈哈，这并不算什么。\x02\x03",

            "我们基本都是自己做饭，\x01",
            "所以在日常生活中经常制作料理。\x02",
        )
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0x104,
        (
            "#11P#0300F不知不觉间，\x01",
            "也就各自掌握了一些拿手的菜式了。\x01",
            "比如我就非常擅长做麻婆豆腐。\x02",
        )
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0xA,
        (
            "#6P是吗，看来你们\x01",
            "也拥有着一颗\x01",
            "料理人之心呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D90D")

    Call(0, 42)

    #C0754
    ChrTalk(
        0xA,
        (
            "#6P哎呀～总之帮大忙啦。\x01",
            "如果想不出新食谱，\x01",
            "我还不知道会有什么下场呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0755
    ChrTalk(
        0x101,
        "#11P#0005F下场……？\x02",
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0xA,
        (
            "#6P不、不，没什么，\x01",
            "没什么大不了的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0757
    ChrTalk(
        0xA,
        (
            "#6P对了，就算是作为这次的谢礼，\x01",
            "要不要尝尝我的试做品？\x02",
        )
    )

    CloseMessageWindow()

    #C0758
    ChrTalk(
        0xA,
        (
            "#6P『松露鱼眼汤』——\x01",
            "虽然味道还不太好……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DAAA")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_DAAA")

    Sleep(1200)

    #C0759
    ChrTalk(
        0x103,
        "#11P#0211F在品尝味道之前，诡异的外观就让人没胃口了。\x02",
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0x102,
        "#11P#0106F完全是道奇怪的菜啊……\x02",
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x104,
        "#11P#0300F好意还是心领了吧。\x02",
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0xA,
        (
            "#6P是吗……那还真是遗憾啊，\x01",
            "还想听听你们的感想呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_DF0C")

    #C0763
    ChrTalk(
        0xA,
        (
            "#6P算了，那么作为替代，\x01",
            "把这个给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCC4")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0764
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1BE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的食谱收下了。\x02",
        )
    )

    CloseMessageWindow()

    #A0765
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1BE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x10)

    #C0766
    ChrTalk(
        0xA,
        (
            "#6P刚才你们给我的料理中，\x01",
            "有个奶油汤对吧？\x01",
            "看了那个之后，我突然有了灵感。\x02",
        )
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0xA,
        (
            "#6P但实在是太普通了，\x01",
            "恐怕不会受客人欢迎呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0xA,
        (
            "#6P如果不嫌弃的话，\x01",
            "你们来吃吃看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD9E")

    label("loc_DCC4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0769
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1BE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('七色棉花糖', 1)

    #C0770
    ChrTalk(
        0xA,
        (
            "#6P这是以『松露鱼眼汤』为基础\x01",
            "制作的一道料理，可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0xA,
        (
            "#6P这未免也太普通了，\x01",
            "没法端给客人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0xA,
        (
            "#6P如果不嫌弃的话，\x01",
            "你们来吃吃看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD9E")


    #C0773
    ChrTalk(
        0x101,
        (
            "#11P#0000F谢谢了……\x02\x03",

            "#0003F可是，就创造性料理来说，\x01",
            "这种普通的东西是不是不太……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0774
    ChrTalk(
        0xA,
        "#6P嗯，你说了什么吗？\x02",
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0x101,
        "#11P#0006F不，没什么……\x02",
    )

    CloseMessageWindow()

    #C0776
    ChrTalk(
        0x102,
        (
            "#11P#0100F（感觉这个人的品位\x01",
            "  有些奇特呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0777
    ChrTalk(
        0xA,
        (
            "#6P好，那么，我也开始\x01",
            "试吃料理吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0xA,
        (
            "#6P真是承蒙你们相助啊。\x01",
            "如果以后再有什么事情，还请多关照！\x02",
        )
    )

    CloseMessageWindow()

    #C0779
    ChrTalk(
        0x103,
        "#11P#0200F嗯，随时欢迎。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_E0AB")

    label("loc_DF0C")


    #C0780
    ChrTalk(
        0xA,
        (
            "#6P算了，作为替代，\x01",
            "把这个给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0781
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('中回复药', 1)

    #C0782
    ChrTalk(
        0xA,
        (
            "#6P为了预防食物中毒，\x01",
            "我会随身携带这个东西呢。\x01",
            "你们就拿去用吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x101,
        (
            "#11P#0005F啊，谢谢了……\x02\x03",

            "#0006F不过，您竟然拼命到了\x01",
            "不惜食物中毒的地步吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0xA,
        (
            "#6P哼……这次我要赌上一切。\x01",
            "毕竟我也是个料理人呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0785
    ChrTalk(
        0xA,
        (
            "#6P真是承蒙你们相助啊。\x01",
            "如果以后再有什么事情，还请多关照！\x02",
        )
    )

    CloseMessageWindow()

    #C0786
    ChrTalk(
        0x101,
        "#11P#0000F嗯，随时欢迎。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_E0AB")

    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0787
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻求创造性料理！】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, -50150, 0, 4140, 270)
    SetChrPos(0xA, -52030, 0, 3650, 270)
    OP_4C(0xA, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E14D")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_E14D")

    OP_29(0x29, 0x4, 0x10)
    OP_29(0x29, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_39_D54F end

    def Function_40_E15B(): pass

    label("Function_40_E15B")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('极苦面『断头』', 0x0)"), scpexpr(EXPR_END)), "loc_E17E")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E17E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('炼狱麻婆『阎魔』', 0x0)"), scpexpr(EXPR_END)), "loc_E197")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E197")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('杂色锅巴饭', 0x0)"), scpexpr(EXPR_END)), "loc_E1B0")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E1B0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('顽固肉排『岩』', 0x0)"), scpexpr(EXPR_END)), "loc_E1C9")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E1C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('混沌久煮『浊』', 0x0)"), scpexpr(EXPR_END)), "loc_E1E2")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E1E2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('男人料理『山』', 0x0)"), scpexpr(EXPR_END)), "loc_E1FB")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E1FB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('男人料理『川』', 0x0)"), scpexpr(EXPR_END)), "loc_E214")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E214")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('箭之鱼', 0x0)"), scpexpr(EXPR_END)), "loc_E22D")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E22D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('激辣炸弹蛋包饭', 0x0)"), scpexpr(EXPR_END)), "loc_E246")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E246")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('细针面', 0x0)"), scpexpr(EXPR_END)), "loc_E25F")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E25F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('苦味汉堡', 0x0)"), scpexpr(EXPR_END)), "loc_E278")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E278")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('四重番茄比萨', 0x0)"), scpexpr(EXPR_END)), "loc_E291")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E291")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('守护三明治', 0x0)"), scpexpr(EXPR_END)), "loc_E2AA")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E2AA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('不可思议盒饭『仰天』', 0x0)"), scpexpr(EXPR_END)), "loc_E2C3")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E2C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('奇妙汤', 0x0)"), scpexpr(EXPR_END)), "loc_E2DC")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E2DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('秘密棉花糖', 0x0)"), scpexpr(EXPR_END)), "loc_E2F5")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E2F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('反射巧克力蛋糕', 0x0)"), scpexpr(EXPR_END)), "loc_E30E")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E30E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('爽弹布丁', 0x0)"), scpexpr(EXPR_END)), "loc_E327")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E327")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('痊愈冰激凌', 0x0)"), scpexpr(EXPR_END)), "loc_E340")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E340")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('隐秘爆米花', 0x0)"), scpexpr(EXPR_END)), "loc_E359")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E359")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('良药『熊竹』', 0x0)"), scpexpr(EXPR_END)), "loc_E372")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E372")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('紫色液体', 0x0)"), scpexpr(EXPR_END)), "loc_E38B")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E38B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('褐色液体', 0x0)"), scpexpr(EXPR_END)), "loc_E3A4")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E3A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('粉红液体', 0x0)"), scpexpr(EXPR_END)), "loc_E3BD")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E3BD")

    Return()

    # Function_40_E15B end

    def Function_41_E3BE(): pass

    label("Function_41_E3BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3D2")
    Jump("loc_EA51")

    label("loc_E3D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E416")

    #C0788
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有一种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E416")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E45A")

    #C0789
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有两种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E45A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E49E")

    #C0790
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有三种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E49E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E4E2")

    #C0791
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有四种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E4E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E526")

    #C0792
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有五种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E526")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E56A")

    #C0793
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有六种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E56A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5AE")

    #C0794
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有七种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E5AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5F2")

    #C0795
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有八种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E5F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E636")

    #C0796
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有九种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E636")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E67A")

    #C0797
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有十种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E67A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6C0")

    #C0798
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有十一种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E6C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E706")

    #C0799
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有十二种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E706")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E74C")

    #C0800
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有十三种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E74C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E792")

    #C0801
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有十四种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E792")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E7D8")

    #C0802
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有十五种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E7D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E81E")

    #C0803
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有十六种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E81E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E864")

    #C0804
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有十七种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E864")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8AA")

    #C0805
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有十八种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E8AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8F0")

    #C0806
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有十九种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E8F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E936")

    #C0807
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有二十种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E936")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E97E")

    #C0808
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有二十一种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E97E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E9C6")

    #C0809
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有二十二种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_E9C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA0E")

    #C0810
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有二十三种啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA51")

    label("loc_EA0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA51")

    #C0811
    ChrTalk(
        0xA,
        (
            "你们携带着的\x01",
            "异想天开的料理……\x01",
            "有二十四种啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA51")

    Return()

    # Function_41_E3BE end

    def Function_42_EA52(): pass

    label("Function_42_EA52")

    ClearScenarioFlags(0x2, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('极苦面『断头』', 0x0)"), scpexpr(EXPR_END)), "loc_EA65")
    SubItemNumber('极苦面『断头』', 1)

    label("loc_EA65")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('炼狱麻婆『阎魔』', 0x0)"), scpexpr(EXPR_END)), "loc_EA75")
    SubItemNumber('炼狱麻婆『阎魔』', 1)

    label("loc_EA75")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('杂色锅巴饭', 0x0)"), scpexpr(EXPR_END)), "loc_EA85")
    SubItemNumber('杂色锅巴饭', 1)

    label("loc_EA85")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('顽固肉排『岩』', 0x0)"), scpexpr(EXPR_END)), "loc_EA95")
    SubItemNumber('顽固肉排『岩』', 1)

    label("loc_EA95")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('混沌久煮『浊』', 0x0)"), scpexpr(EXPR_END)), "loc_EAA5")
    SubItemNumber('混沌久煮『浊』', 1)

    label("loc_EAA5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('男人料理『山』', 0x0)"), scpexpr(EXPR_END)), "loc_EAB5")
    SubItemNumber('男人料理『山』', 1)

    label("loc_EAB5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('男人料理『川』', 0x0)"), scpexpr(EXPR_END)), "loc_EAC5")
    SubItemNumber('男人料理『川』', 1)

    label("loc_EAC5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('箭之鱼', 0x0)"), scpexpr(EXPR_END)), "loc_EAD5")
    SubItemNumber('箭之鱼', 1)

    label("loc_EAD5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('激辣炸弹蛋包饭', 0x0)"), scpexpr(EXPR_END)), "loc_EAE5")
    SubItemNumber('激辣炸弹蛋包饭', 1)

    label("loc_EAE5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('细针面', 0x0)"), scpexpr(EXPR_END)), "loc_EAF5")
    SubItemNumber('细针面', 1)

    label("loc_EAF5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('苦味汉堡', 0x0)"), scpexpr(EXPR_END)), "loc_EB05")
    SubItemNumber('苦味汉堡', 1)

    label("loc_EB05")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('四重番茄比萨', 0x0)"), scpexpr(EXPR_END)), "loc_EB15")
    SubItemNumber('四重番茄比萨', 1)

    label("loc_EB15")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('守护三明治', 0x0)"), scpexpr(EXPR_END)), "loc_EB25")
    SubItemNumber('守护三明治', 1)

    label("loc_EB25")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('不可思议盒饭『仰天』', 0x0)"), scpexpr(EXPR_END)), "loc_EB35")
    SubItemNumber('不可思议盒饭『仰天』', 1)

    label("loc_EB35")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('奇妙汤', 0x0)"), scpexpr(EXPR_END)), "loc_EB48")
    SubItemNumber('奇妙汤', 1)
    SetScenarioFlags(0x2, 1)

    label("loc_EB48")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('秘密棉花糖', 0x0)"), scpexpr(EXPR_END)), "loc_EB58")
    SubItemNumber('秘密棉花糖', 1)

    label("loc_EB58")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('反射巧克力蛋糕', 0x0)"), scpexpr(EXPR_END)), "loc_EB68")
    SubItemNumber('反射巧克力蛋糕', 1)

    label("loc_EB68")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('爽弹布丁', 0x0)"), scpexpr(EXPR_END)), "loc_EB78")
    SubItemNumber('爽弹布丁', 1)

    label("loc_EB78")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('痊愈冰激凌', 0x0)"), scpexpr(EXPR_END)), "loc_EB88")
    SubItemNumber('痊愈冰激凌', 1)

    label("loc_EB88")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('隐秘爆米花', 0x0)"), scpexpr(EXPR_END)), "loc_EB98")
    SubItemNumber('隐秘爆米花', 1)

    label("loc_EB98")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('良药『熊竹』', 0x0)"), scpexpr(EXPR_END)), "loc_EBA8")
    SubItemNumber('良药『熊竹』', 1)

    label("loc_EBA8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('紫色液体', 0x0)"), scpexpr(EXPR_END)), "loc_EBB8")
    SubItemNumber('紫色液体', 1)

    label("loc_EBB8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('褐色液体', 0x0)"), scpexpr(EXPR_END)), "loc_EBC8")
    SubItemNumber('褐色液体', 1)

    label("loc_EBC8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('粉红液体', 0x0)"), scpexpr(EXPR_END)), "loc_EBD8")
    SubItemNumber('粉红液体', 1)

    label("loc_EBD8")

    Return()

    # Function_42_EA52 end

    SaveToFile()

Try(main)
