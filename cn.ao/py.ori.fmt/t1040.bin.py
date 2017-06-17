from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1040.bin",                # FileName
        "t1040",                    # MapName
        "t1040",                    # Location
        0x0043,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 67, 0, 2, 0, 3],
    )

    BuildStringList((
        "t1040",                  # 0
        "鲁特",                   # 1
        "梅夏",                   # 2
        "夫人",                   # 3
        "游客",                   # 4
        "游客",                   # 5
        "游客",                   # 6
        "游客",                   # 7
        "游客",                   # 8
        "游客",                   # 9
        "游客",                   # 10
        "瓦吉",                   # 11
        "玛格丽特夫人",           # 12
        "薇娜",                   # 13
        "德罗娜",                 # 14
        "游客",                   # 15
        "艾莉",                   # 16
        "芙兰",                   # 17
        "塞茜尔",                 # 18
        "伊莉娅",                 # 19
        "莉夏",                   # 20
    ))

    AddCharChip((
        "chr/ch25000.itc",                   # 00
        "chr/ch34500.itc",                   # 01
        "chr/ch33202.itc",                   # 02
        "chr/ch24002.itc",                   # 03
        "chr/ch21702.itc",                   # 04
        "chr/ch21802.itc",                   # 05
        "chr/ch21902.itc",                   # 06
        "chr/ch33102.itc",                   # 07
        "chr/ch44202.itc",                   # 08
        "chr/ch34402.itc",                   # 09
        "chr/ch27900.itc",                   # 0A
        "chr/ch26600.itc",                   # 0B
        "chr/ch33300.itc",                   # 0C
        "chr/ch03002.itc",                   # 0D
        "chr/ch00100.itc",                   # 0E
        "chr/ch08500.itc",                   # 0F
        "chr/ch07500.itc",                   # 10
        "chr/ch05100.itc",                   # 11
        "chr/ch05200.itc",                   # 12
        "chr/ch44002.itc",                   # 13
    ))

    DeclNpc(-104069, 0,       2980,    90,   261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-101099, 0,       5880,    90,   257,  0x0, 0,   1,   0,   0,   1,   0,   8,   255,  0)
    DeclNpc(-101819, 119,     -879,    270,  453,  0x0, 0,   2,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-104800, 119,     8930,    45,   453,  0x0, 0,   3,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-103000, 119,     10930,   225,  453,  0x0, 0,   4,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-97959,  119,     19090,   45,   453,  0x0, 0,   5,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-97959,  119,     19090,   45,   453,  0x0, 0,   6,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(-104800, 119,     8930,    45,   453,  0x0, 0,   7,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   8,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(-96120,  119,     20889,   225,  453,  0x0, 0,   9,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(-101790, 119,     1120,    270,  453,  0x0, 0,   13,  0,   255, 255, 0,   4,   255,  0)
    DeclNpc(-101790, 119,     -910,    270,  453,  0x0, 0,   19,  0,   255, 255, 0,   29,  255,  0)
    DeclNpc(-1860,   0,       10640,   180,  261,  0x0, 0,   10,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-6250,   0,       6099,    180,  261,  0x0, 0,   11,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(-8189,   0,       7510,    0,    389,  0x0, 0,   12,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(-4050,   0,       4530,    270,  389,  0x0, 0,   14,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-8170,   0,       7940,    270,  389,  0x0, 0,   15,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(4300,    0,       5079,    90,   389,  0x0, 0,   16,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   17,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   18,  0,   0,   0,   0,   17,  255,  0)

    DeclActor(-1770,   0,       8810,    1000,    -1860,   1500,    10640,   0x007E, 0,  24, 0x0000)
    DeclActor(-101650, 0,       2470,    1000,    -104070, 1500,    2980,    0x007E, 0,  6,  0x0000)

    ChipFrameInfo(980, 0)                                        # 0

    ScpFunction((
        "Function_0_3D4",          # 00, 0
        "Function_1_48C",          # 01, 1
        "Function_2_515",          # 02, 2
        "Function_3_74D",          # 03, 3
        "Function_4_7AC",          # 04, 4
        "Function_5_8A9",          # 05, 5
        "Function_6_9DC",          # 06, 6
        "Function_7_9E0",          # 07, 7
        "Function_8_CFA",          # 08, 8
        "Function_9_EAD",          # 09, 9
        "Function_10_102B",        # 0A, 10
        "Function_11_10B0",        # 0B, 11
        "Function_12_1125",        # 0C, 12
        "Function_13_118A",        # 0D, 13
        "Function_14_11FB",        # 0E, 14
        "Function_15_126C",        # 0F, 15
        "Function_16_134B",        # 10, 16
        "Function_17_13B6",        # 11, 17
        "Function_18_142C",        # 12, 18
        "Function_19_15DB",        # 13, 19
        "Function_20_168D",        # 14, 20
        "Function_21_1801",        # 15, 21
        "Function_22_1CD3",        # 16, 22
        "Function_23_1E78",        # 17, 23
        "Function_24_24C8",        # 18, 24
        "Function_25_24CC",        # 19, 25
        "Function_26_2747",        # 1A, 26
        "Function_27_28E9",        # 1B, 27
        "Function_28_2975",        # 1C, 28
        "Function_29_29F7",        # 1D, 29
    ))


    def Function_0_3D4(): pass

    label("Function_0_3D4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_414"),
        (1, "loc_420"),
        (2, "loc_42C"),
        (3, "loc_438"),
        (4, "loc_444"),
        (5, "loc_450"),
        (6, "loc_45C"),
        (SWITCH_DEFAULT, "loc_468"),
    )


    label("loc_414")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_420")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_42C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_438")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_444")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_450")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_45C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_468")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_474")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_48B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_48B")

    Return()

    # Function_0_3D4 end

    def Function_1_48C(): pass

    label("Function_1_48C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_514")
    OP_95(0xFE, -98090, 0, 5880, 2000, 0x0)
    OP_95(0xFE, -98090, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 5880, 2000, 0x0)
    Jump("Function_1_48C")

    label("loc_514")

    Return()

    # Function_1_48C end

    def Function_2_515(): pass

    label("Function_2_515")

    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x10, 0x8)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    SetChrChipByIndex(0x12, 0xD)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrChipByIndex(0x13, 0x13)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_5CD")
    Jump("loc_74C")

    label("loc_5CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_5DB")
    Jump("loc_74C")

    label("loc_5DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_664")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x15, 1590, 0, 8900, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61F")
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1050, 0, 2180, 0)
    Jump("loc_655")

    label("loc_61F")

    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -1530, 0, 2530, 90)
    SetChrFlags(0x1B, 0x10)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -540, 0, 2530, 270)
    SetChrFlags(0x1A, 0x10)

    label("loc_655")

    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_74C")

    label("loc_664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_6F4")
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrSubChip(0xA, 0x2)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -103000, 120, 10930, 225)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x15, -1530, 0, 2530, 90)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -540, 0, 2530, 270)
    SetChrFlags(0x1A, 0x10)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_74C")

    label("loc_6F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_74C")
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x10, -96120, 120, 20890, 225)
    SetChrPos(0x15, -8189, 0, 8640, 180)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x10)

    label("loc_74C")

    Return()

    # Function_2_515 end

    def Function_3_74D(): pass

    label("Function_3_74D")

    SetMapObjFrame(0xFF, "t1040_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1040_sky_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "t1040_sky01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1040_sky01_y", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7AB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7AB")

    Return()

    # Function_3_74D end

    def Function_4_7AC(): pass

    label("Function_4_7AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_7BD")
    Jump("loc_8A5")

    label("loc_7BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_7CB")
    Jump("loc_8A5")

    label("loc_7CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_7D9")
    Jump("loc_8A5")

    label("loc_7D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_7E7")
    Jump("loc_8A5")

    label("loc_7E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_880")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_802")
    Call(0, 5)
    Jump("loc_87B")

    label("loc_802")


    #C0001
    ChrTalk(
        0x12,
        (
            "#10304F呵呵，如你所见，\x01",
            "我被俱乐部的老主顾抓住了呢。\x02\x03",

            "#10300F不过，我会尽快搞定的，\x01",
            "一定可以准时集合，\x01",
            "你就放心吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87B")

    Jump("loc_8A5")

    label("loc_880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_88E")
    Jump("loc_8A5")

    label("loc_88E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_89C")
    Jump("loc_8A5")

    label("loc_89C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_8A5")

    label("loc_8A5")

    TalkEnd(0xFE)
    Return()

    # Function_4_7AC end

    def Function_5_8A9(): pass

    label("Function_5_8A9")


    #C0002
    ChrTalk(
        0xA,
        (
            "呵呵，这可真是奇遇啊，\x01",
            "没想到瓦吉会来这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xA,
        (
            "你怎么不和我联系呢，\x01",
            "我随时都可以陪你哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x12,
        (
            "#10304F呵呵，因为我今天是和朋友一起来的。\x02\x03",

            "#10302F不好意思，我稍后还要去赴约，\x01",
            "今天就提前说再见吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xA,
        "啊啊，这种冷淡的态度也好帅⊥\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#00006F（身、身为男公关，\x01",
            "  这种态度没问题吗……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0xA, 0x10)
    Return()

    # Function_5_8A9 end

    def Function_6_9DC(): pass

    label("Function_6_9DC")

    Call(0, 7)
    Return()

    # Function_6_9DC end

    def Function_7_9E0(): pass

    label("Function_7_9E0")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF6")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A3D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_A3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5D")
    OP_AF(0x66)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CF1")

    label("loc_A5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A71")
    Jump("loc_CF1")

    label("loc_A71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A98")
    Jump("loc_CF1")

    label("loc_A98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_BDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B68")

    #C0007
    ChrTalk(
        0x8,
        (
            "本餐厅之所以\x01",
            "以『幸运』为名，\x01",
            "是希望能给客人们带来幸福与好运。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "我们将会为客人提供\x01",
            "最完美的服务，\x01",
            "让客人幸福地享用美食。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "如果您有什么意见，\x01",
            "请不要客气，尽管告诉我们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BD9")

    label("loc_B68")


    #C0010
    ChrTalk(
        0x8,
        (
            "我们将会为客人提供\x01",
            "最完美的服务，\x01",
            "让客人幸福地享用美食。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "如果您有什么意见，\x01",
            "请不要客气，尽管告诉我们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD9")

    Jump("loc_CF1")

    label("loc_BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_CF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C84")

    #C0012
    ChrTalk(
        0x8,
        "欢迎光临西餐厅『幸运』。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "本店使用最高等的食材，\x01",
            "为顾客提供最好的料理\x01",
            "和最完美的用餐环境。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "祝您度过一段\x01",
            "优雅而幸福的时光……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CF1")

    label("loc_C84")


    #C0015
    ChrTalk(
        0x8,
        (
            "本店使用最高等的食材，\x01",
            "为顾客提供最好的料理\x01",
            "和最完美的用餐环境。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "祝您度过一段\x01",
            "优雅而幸福的时光……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF1")

    Jump("loc_9ED")

    label("loc_CF6")

    TalkEnd(0x8)
    Return()

    # Function_7_9E0 end

    def Function_8_CFA(): pass

    label("Function_8_CFA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_D0B")
    Jump("loc_EA9")

    label("loc_D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_D7C")

    #C0017
    ChrTalk(
        0xFE,
        (
            "主题公园最近\x01",
            "好像增添了新的\x01",
            "游乐设施呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "听说是很可怕的那种～\x01",
            "到底是什么样的游乐设施呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA9")

    label("loc_D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_EA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E40")

    #C0019
    ChrTalk(
        0xFE,
        (
            "前段时间新开放的湖水浴场很受欢迎，\x01",
            "无论男女老少，都非常喜欢。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "天气还会继续热上一阵，\x01",
            "来米修拉姆的游客\x01",
            "似乎会比往年更多。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "唔，我也很想去湖水浴场玩一次呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_EA9")

    label("loc_E40")


    #C0022
    ChrTalk(
        0xFE,
        (
            "前段时间新开放的湖水浴场很受欢迎，\x01",
            "无论男女老少，都非常喜欢。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "唔，我也很想去湖水浴场玩一次呢。\x02",
    )

    CloseMessageWindow()

    label("loc_EA9")

    TalkEnd(0xFE)
    Return()

    # Function_8_CFA end

    def Function_9_EAD(): pass

    label("Function_9_EAD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_EBE")
    Jump("loc_1027")

    label("loc_EBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_F99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F47")

    #C0024
    ChrTalk(
        0xFE,
        "唉，瓦吉已经走了。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "话虽如此，但回家之后\x01",
            "也只能照顾那个\x01",
            "无趣的丈夫……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        "我还是一个人再喝几杯吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_F94")

    label("loc_F47")


    #C0027
    ChrTalk(
        0xFE,
        "唉，瓦吉已经走了。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "实在不想回家照顾丈夫，\x01",
            "我还是一个人再喝几杯吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F94")

    Jump("loc_1027")

    label("loc_F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_101E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FBC")
    Call(0, 5)
    TalkEnd(0xFE)
    SetChrSubChip(0xA, 0x2)
    Return()

    label("loc_FBC")


    #C0029
    ChrTalk(
        0xFE,
        (
            "瓦吉虽然是男公关，\x01",
            "但态度有时会很冷淡呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        "……不过，这种性格也很吸引人啊⊥\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0xA, 0x2)
    Return()

    label("loc_101E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1027")

    label("loc_1027")

    TalkEnd(0xFE)
    Return()

    # Function_9_EAD end

    def Function_10_102B(): pass

    label("Function_10_102B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_103C")
    Jump("loc_10AC")

    label("loc_103C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_104A")
    Jump("loc_10AC")

    label("loc_104A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_10AC")

    #C0031
    ChrTalk(
        0xFE,
        "这应该算是吃晚了的早餐吧。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "呵呵呵，不过以早餐标准来看，\x01",
            "这顿吃得可真是高级呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10AC")

    TalkEnd(0xFE)
    Return()

    # Function_10_102B end

    def Function_11_10B0(): pass

    label("Function_11_10B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_10C1")
    Jump("loc_1121")

    label("loc_10C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_10CF")
    Jump("loc_1121")

    label("loc_10CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1121")

    #C0033
    ChrTalk(
        0xFE,
        "嗯嗯，吃什么好呢？\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "天气还很热，还是吃些\x01",
            "可以解暑的食物比较好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1121")

    TalkEnd(0xFE)
    Return()

    # Function_11_10B0 end

    def Function_12_1125(): pass

    label("Function_12_1125")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1136")
    Jump("loc_1186")

    label("loc_1136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1144")
    Jump("loc_1186")

    label("loc_1144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1186")

    #C0035
    ChrTalk(
        0xFE,
        "（狼吞虎咽）\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "真好吃啊（嚼嚼）……\x01",
            "（狼吞虎咽）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1186")

    TalkEnd(0xFE)
    Return()

    # Function_12_1125 end

    def Function_13_118A(): pass

    label("Function_13_118A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_119B")
    Jump("loc_11F7")

    label("loc_119B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_11EE")

    #C0037
    ChrTalk(
        0xFE,
        (
            "嗯，湖水浴场的包场\x01",
            "好像只到中午……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        "吃过饭之后就去看看吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_11F7")

    label("loc_11EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_11F7")

    label("loc_11F7")

    TalkEnd(0xFE)
    Return()

    # Function_13_118A end

    def Function_14_11FB(): pass

    label("Function_14_11FB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_120C")
    Jump("loc_1268")

    label("loc_120C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_125F")

    #C0039
    ChrTalk(
        0xFE,
        (
            "哈哈，怎么样，\x01",
            "我选的餐厅很不错吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "尽情品味美味的料理吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1268")

    label("loc_125F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1268")

    label("loc_1268")

    TalkEnd(0xFE)
    Return()

    # Function_14_11FB end

    def Function_15_126C(): pass

    label("Function_15_126C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_127D")
    Jump("loc_1347")

    label("loc_127D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_12DF")

    #C0041
    ChrTalk(
        0xFE,
        (
            "（虽然料理的味道\x01",
            "  相当不错……）\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "（唔……但似乎找错了\x01",
            "  同来的人选呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1347")

    label("loc_12DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1347")

    #C0043
    ChrTalk(
        0xFE,
        "等、等一下，爸爸你可真是的！\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "在这种高档餐厅，必须要严格\x01",
            "遵守用餐礼仪，请你注意下啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1347")

    TalkEnd(0xFE)
    Return()

    # Function_15_126C end

    def Function_16_134B(): pass

    label("Function_16_134B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_135C")
    Jump("loc_13B2")

    label("loc_135C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_13A9")

    #C0045
    ChrTalk(
        0xFE,
        "我开始觉得热了。\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "妈妈，我们吃完午饭\x01",
            "就去湖水浴场吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B2")

    label("loc_13A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_13B2")

    label("loc_13B2")

    TalkEnd(0xFE)
    Return()

    # Function_16_134B end

    def Function_17_13B6(): pass

    label("Function_17_13B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_13C7")
    Jump("loc_1428")

    label("loc_13C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_13D5")
    Jump("loc_1428")

    label("loc_13D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_13E3")
    Jump("loc_1428")

    label("loc_13E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1403")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13FB")
    Jump("loc_13FE")

    label("loc_13FB")

    Call(0, 20)

    label("loc_13FE")

    Jump("loc_1428")

    label("loc_1403")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1411")
    Jump("loc_1428")

    label("loc_1411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_141F")
    Jump("loc_1428")

    label("loc_141F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1428")

    label("loc_1428")

    TalkEnd(0xFE)
    Return()

    # Function_17_13B6 end

    def Function_18_142C(): pass

    label("Function_18_142C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_143D")
    Jump("loc_15D7")

    label("loc_143D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_144B")
    Jump("loc_15D7")

    label("loc_144B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1459")
    Jump("loc_15D7")

    label("loc_1459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_154F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1547")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14E9")

    #C0047
    ChrTalk(
        0x1A,
        (
            "#01703F唔，这家店里的衣服\x01",
            "和我不是很相配呢。\x02\x03",

            "#01702F要是有那种\x01",
            "更富热情、更有异国情调的\x01",
            "衣服就好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_1542")

    label("loc_14E9")


    #C0048
    ChrTalk(
        0x1A,
        (
            "#01705F话说回来，\x01",
            "莉夏还真慢啊。\x02\x03",

            "#01706F她要是再不快点来，\x01",
            "就没时间\x01",
            "给她选衣服了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1542")

    Jump("loc_154A")

    label("loc_1547")

    Call(0, 20)

    label("loc_154A")

    Jump("loc_15D7")

    label("loc_154F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_15C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156A")
    Call(0, 19)
    Jump("loc_15BB")

    label("loc_156A")


    #C0049
    ChrTalk(
        0x1A,
        (
            "#01705F咦，说起来，\x01",
            "莉夏还没来吗？\x02\x03",

            "#01706F我想给她\x01",
            "也挑些比较\x01",
            "性感的衣服。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15BB")

    Jump("loc_15D7")

    label("loc_15C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_15CE")
    Jump("loc_15D7")

    label("loc_15CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_15D7")

    label("loc_15D7")

    TalkEnd(0xFE)
    Return()

    # Function_18_142C end

    def Function_19_15DB(): pass

    label("Function_19_15DB")

    OP_4B(0x1A, 0xFF)
    OP_4B(0x15, 0xFF)

    #C0050
    ChrTalk(
        0x15,
        (
            "嗯……客人您看，\x01",
            "这条裙子怎么样呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x1A,
        (
            "#01703F唔……这个嘛……\x01",
            "我还是喜欢\x01",
            "再华丽些的。\x02\x03",

            "#01702F啊，能不能让我看看帽子之类的？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x15,
        "好的，请到这边来。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    ClearChrFlags(0x1A, 0x10)
    OP_4C(0x1A, 0xFF)
    Return()

    # Function_19_15DB end

    def Function_20_168D(): pass

    label("Function_20_168D")

    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1797")

    #C0053
    ChrTalk(
        0x1A,
        (
            "#01700F这是我刚才找到的衣服，\x01",
            "胸间是镂空的，很性感吧？\x02\x03",

            "#01709F怎么样？莉夏。\x01",
            "要不要穿穿看？我送给你哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x1B,
        (
            "#01805F咦、咦！？\x01",
            "要穿这个吗！？\x02\x03",

            "#01809F实、实在是\x01",
            "有点不好意思……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x1A,
        (
            "#01709F不会不会啦！你穿上之后，\x01",
            "一定会很有魅力的！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_17F8")

    label("loc_1797")


    #C0056
    ChrTalk(
        0x1A,
        (
            "#01709F好啦，\x01",
            "你就当作被骗了，\x01",
            "试穿一下嘛。\x02\x03",

            "#01701F我很想看看呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x1B,
        "#01806F这、这……！\x02",
    )

    CloseMessageWindow()

    label("loc_17F8")

    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    Return()

    # Function_20_168D end

    def Function_21_1801(): pass

    label("Function_21_1801")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1812")
    Jump("loc_1CCF")

    label("loc_1812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1820")
    Jump("loc_1CCF")

    label("loc_1820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_182E")
    Jump("loc_1CCF")

    label("loc_182E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1ACF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A1B")

    #C0058
    ChrTalk(
        0x19,
        (
            "#05900F罗伊德，我刚才听艾莉小姐说，\x01",
            "你以前在这家精品店\x01",
            "买过西装？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#00005F嗯，是不久之前的事情……\x01",
            "有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x19,
        (
            "#05906F呜呜，你在婚礼上穿的\x01",
            "西装，应该让姐姐我来\x01",
            "挑选才对啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x153,
        (
            "#01105F咦，罗伊德，\x01",
            "你果然要结婚吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#00012F不、不是不是，才没有那回事！\x02\x03",

            "#00006F那只是为了完成调查任务\x01",
            "而选购的衣服啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x19,
        (
            "#05905F哎呀，原来是这样吗？\x01",
            "还真是让人遗憾啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0064
    ChrTalk(
        0x101,
        (
            "#00006F（塞茜尔姐姐……\x01",
            "  好像在以观察我的反应取乐吧？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_1ACA")

    label("loc_1A1B")


    #C0065
    ChrTalk(
        0x19,
        (
            "#05902F呵呵，你举行婚礼的时候，\x01",
            "可一定要记得叫我啊。\x02\x03",

            "#05901F从婚礼会场的布置，\x01",
            "到新婚旅行的地点，\x01",
            "全都要让姐姐来帮你决定！\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#00006F这离西装的话题\x01",
            "未免也太远了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ACA")

    Jump("loc_1CCF")

    label("loc_1ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1CB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C48")

    #C0067
    ChrTalk(
        0x19,
        "#05903F………………………………\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#00005F塞茜尔姐姐，怎么了？\x02",
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0069
    ChrTalk(
        0x19,
        (
            "#05902F……啊，罗伊德。\x02\x03",

            "#05909F嗯，我还是第一次\x01",
            "去主题公园，\x01",
            "正在想那是个什么样的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00004F啊，我也是第一次。\x02\x03",

            "#00000F兰迪和诺艾尔以前去过，\x01",
            "从他们的形容来看，\x01",
            "似乎很值得期待呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x19,
        (
            "#05909F呵呵，这样啊。\x01",
            "难得来一次，要请他们\x01",
            "多介绍介绍呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_1CB3")

    label("loc_1C48")


    #C0072
    ChrTalk(
        0x19,
        (
            "#05904F嗯，今天\x01",
            "一定要玩得尽兴啊。\x02\x03",

            "#05902F我还是第一次来，\x01",
            "干脆请兰迪和诺艾尔小姐\x01",
            "为我介绍一下好了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB3")

    Jump("loc_1CCF")

    label("loc_1CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1CC6")
    Jump("loc_1CCF")

    label("loc_1CC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1CCF")

    label("loc_1CCF")

    TalkEnd(0xFE)
    Return()

    # Function_21_1801 end

    def Function_22_1CD3(): pass

    label("Function_22_1CD3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1CE4")
    Jump("loc_1E74")

    label("loc_1CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1CF2")
    Jump("loc_1E74")

    label("loc_1CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1D00")
    Jump("loc_1E74")

    label("loc_1D00")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_1D10")
    Jump("loc_1E74")

    label("loc_1D10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1D1E")
    Jump("loc_1E74")

    label("loc_1D1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1E5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E10")

    #C0073
    ChrTalk(
        0x18,
        (
            "#06405F啊，罗伊德警官！\x01",
            "请帮我出出主意吧～\x02\x03",

            "#06409F这件衣服怎么样？\x01",
            "适合我吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        "#00000F嗯，好像挺不错呢。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x18,
        (
            "#06402F哦哦！得到了罗伊德警官的认可呢！\x01",
            "那我就买啦……\x02\x03",

            "#06409F呵呵，也替姐姐\x01",
            "选几件衣服吧～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_1E58")

    label("loc_1E10")


    #C0076
    ChrTalk(
        0x18,
        (
            "#06409F这里有很多漂亮的衣服呢～！\x02\x03",

            "#06406F要是姐姐也一起来就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E58")

    Jump("loc_1E74")

    label("loc_1E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1E6B")
    Jump("loc_1E74")

    label("loc_1E6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1E74")

    label("loc_1E74")

    TalkEnd(0xFE)
    Return()

    # Function_22_1CD3 end

    def Function_23_1E78(): pass

    label("Function_23_1E78")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1E89")
    Jump("loc_24C4")

    label("loc_1E89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1E97")
    Jump("loc_24C4")

    label("loc_1E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1EA5")
    Jump("loc_24C4")

    label("loc_1EA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_20BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_203B")

    #C0077
    ChrTalk(
        0x17,
        (
            "#00113F唉，虽然多少有些心理准备，\x01",
            "但没想到会遇到那种事……\x02\x03",

            "#00111F……喂，罗伊德，\x01",
            "你真的没看到吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#00012F真、真的，\x01",
            "放心好了，我绝对没看到。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x17,
        (
            "#00106F呼，那就好。\x02\x03",

            "#00112F……你要是看到了，\x01",
            "可就要负起责任了。\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0080
    ChrTalk(
        0x101,
        "#00011F#4S哎！？#3S\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x17,
        (
            "#00104F……才怪，只是开个玩笑啦。\x02\x03",

            "#00109F呵呵，捉弄你真是一件\x01",
            "很有趣的事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#00006F饶、饶了我吧……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_20B7")

    label("loc_203B")


    #C0083
    ChrTalk(
        0x17,
        (
            "#00113F算啦，对于这种情况，\x01",
            "我在事前就有了一定程度的心理准备……\x02\x03",

            "#00102F总之，能够击退魔兽就好，\x01",
            "其它事情也无所谓了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20B7")

    Jump("loc_24C4")

    label("loc_20BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_2247")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21EE")

    #C0084
    ChrTalk(
        0x17,
        (
            "#00105F啊，小琪雅。\x02\x03",

            "#00102F你看，这件礼服怎么样？\x01",
            "我觉得很适合\x01",
            "你呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x153,
        "#01110F哇，好漂亮！\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#00003F礼、礼服啊……\x01",
            "平时有机会穿吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x17,
        (
            "#00109F呵呵，就算没机会穿也不要紧。\x02\x03",

            "#00104F但要尽量让小琪雅\x01",
            "尝试多种风格的衣服。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#00012F（唔……一副乐在其中的样子呢……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2242")

    label("loc_21EE")


    #C0089
    ChrTalk(
        0x17,
        (
            "#00102F呵呵，我还要\x01",
            "在这里看一阵子。\x02\x03",

            "#00109F想给小琪雅多挑\x01",
            "几件不一样的衣服。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2242")

    Jump("loc_24C4")

    label("loc_2247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_249F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2424")

    #C0090
    ChrTalk(
        0x17,
        (
            "#00103F这家精品店的服装，\x01",
            "品质确实出众呢。\x02\x03",

            "#00100F比如这套礼服的丝绸面料，\x01",
            "还有那边那件巴利亚哈特的皮草，\x01",
            "触感都很柔软……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#00005F巴利亚哈特……\x01",
            "好像是一座位于\x01",
            "帝国东部的城市吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x17,
        (
            "#00100F嗯，那里是以\x01",
            "出产优质毛皮而闻名的。\x02\x03",

            "#00104F在出席社交宴会的时候，\x01",
            "经常可以看到贵妇人\x01",
            "身穿产自那里的皮草。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#00000F呵呵，你对这方面的事情真是很熟悉啊。\x02\x03",

            "#00003F不过，在这种季节，\x01",
            "穿皮草未免也太热了……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x17,
        (
            "#00111F……你说得还真是\x01",
            "不解风情啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_249A")

    label("loc_2424")


    #C0095
    ChrTalk(
        0x17,
        (
            "#00104F在社交场合中，\x01",
            "服装也是身份象征\x01",
            "的一种。\x02\x03",

            "#00100F但我个人认为，\x01",
            "只要做工精细就好，\x01",
            "没必要太过拘泥于名牌。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_249A")

    Jump("loc_24C4")

    label("loc_249F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_24AD")
    Jump("loc_24C4")

    label("loc_24AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_24BB")
    Jump("loc_24C4")

    label("loc_24BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_24C4")

    label("loc_24C4")

    TalkEnd(0xFE)
    Return()

    # Function_23_1E78 end

    def Function_24_24C8(): pass

    label("Function_24_24C8")

    Call(0, 25)
    Return()

    # Function_24_24C8 end

    def Function_25_24CC(): pass

    label("Function_25_24CC")

    TalkBegin(0x14)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2743")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2529")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2529")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2549")
    OP_AF(0x69)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_273E")

    label("loc_2549")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_255D")
    Jump("loc_273E")

    label("loc_255D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_273E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2584")
    Jump("loc_273E")

    label("loc_2584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_265B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2614")

    #C0096
    ChrTalk(
        0x14,
        (
            "呼，德罗娜可真是的，\x01",
            "实在是兴奋过头了……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x14,
        (
            "虽然我理解她的心情，\x01",
            "但是在客人面前，\x01",
            "还是希望她稍微控制一下啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2656")

    label("loc_2614")


    #C0098
    ChrTalk(
        0x14,
        (
            "呼，德罗娜可真是的，\x01",
            "希望她在客人面前\x01",
            "能控制一下兴奋的心情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2656")

    Jump("loc_273E")

    label("loc_265B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_26B7")

    #C0099
    ChrTalk(
        0x14,
        (
            "我们这里的客人\x01",
            "以女性居多。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x14,
        (
            "呵呵，每位客人都很美丽，\x01",
            "真是令人惊叹。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_273E")

    label("loc_26B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_273E")

    #C0101
    ChrTalk(
        0x14,
        (
            "随着湖水浴场的开放，\x01",
            "精品店『柯赛利卡』\x01",
            "也开始经营泳装了。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x14,
        (
            "我们提供从大陆沿岸\x01",
            "地区进口的时尚泳装，\x01",
            "您一定要看看哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_273E")

    Jump("loc_24D9")

    label("loc_2743")

    TalkEnd(0x14)
    Return()

    # Function_25_24CC end

    def Function_26_2747(): pass

    label("Function_26_2747")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2758")
    Jump("loc_28E5")

    label("loc_2758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_2820")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27C2")

    #C0103
    ChrTalk(
        0xFE,
        (
            "我拿到了伊莉娅·普拉提耶\x01",
            "的亲笔签名！\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        "啊，我会把这件宝物珍藏一生的！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_281B")

    label("loc_27C2")


    #C0105
    ChrTalk(
        0xFE,
        (
            "没想到能在这种地方\x01",
            "见到大名鼎鼎的伊莉娅……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        "我会把这个签名当作珍藏一生的宝物！\x02",
    )

    CloseMessageWindow()

    label("loc_281B")

    Jump("loc_28E5")

    label("loc_2820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2880")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_283B")
    Call(0, 19)
    Jump("loc_287B")

    label("loc_283B")


    #C0107
    ChrTalk(
        0xFE,
        (
            "（……咦？\x01",
            "  说起来，好像曾在什么地方\x01",
            "  见过这位客人……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_287B")

    Jump("loc_28E5")

    label("loc_2880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_28E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_289B")
    Call(0, 27)
    Jump("loc_28E5")

    label("loc_289B")


    #C0108
    ChrTalk(
        0xFE,
        "呵呵呵，非常合身呢。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "这件衣服最大限度地\x01",
            "衬托出了您的\x01",
            "优雅气质。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28E5")

    TalkEnd(0xFE)
    Return()

    # Function_26_2747 end

    def Function_27_28E9(): pass

    label("Function_27_28E9")

    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    #C0110
    ChrTalk(
        0x15,
        (
            "对了，为了搭配这件衣服，\x01",
            "我认为您戴上这条丝巾\x01",
            "会显得更加优雅……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x16,
        "……这样吗？\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x15,
        "呵呵呵，真是非常适合您呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    Return()

    # Function_27_28E9 end

    def Function_28_2975(): pass

    label("Function_28_2975")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2986")
    Jump("loc_29F3")

    label("loc_2986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2994")
    Jump("loc_29F3")

    label("loc_2994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_29F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29AF")
    Call(0, 27)
    Jump("loc_29F3")

    label("loc_29AF")


    #C0113
    ChrTalk(
        0xFE,
        (
            "呵呵，你确实\x01",
            "很有眼光啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "那么，我就把这一整套\x01",
            "买下来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29F3")

    TalkEnd(0xFE)
    Return()

    # Function_28_2975 end

    def Function_29_29F7(): pass

    label("Function_29_29F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AAC")

    #C0115
    ChrTalk(
        0xFE,
        (
            "疗养地米修拉姆……\x01",
            "我还是第一次来，这里真是很棒呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "要是能在这里定居下来，\x01",
            "也就可以告别与丈夫\x01",
            "同住的无趣生活了。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "吃过饭之后，就去\x01",
            "别墅区看看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_2B13")

    label("loc_2AAC")


    #C0118
    ChrTalk(
        0xFE,
        (
            "要是能在这里定居下来，\x01",
            "也就可以告别与丈夫\x01",
            "同住的无趣生活了。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "吃过饭之后，就去\x01",
            "别墅区看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B13")

    TalkEnd(0xFE)
    Return()

    # Function_29_29F7 end

    SaveToFile()

Try(main)
