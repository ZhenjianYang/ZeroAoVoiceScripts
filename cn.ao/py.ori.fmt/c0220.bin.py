from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0220.bin",                # FileName
        "c0220",                    # MapName
        "c0220",                    # Location
        0x000D,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 13, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0220",                  # 0
        "伊安律师",               # 1
        "皮特",                   # 2
        "上班族",                 # 3
        "艾玛搜查官",             # 4
        "警官",                   # 5
        "搜查官",                 # 6
        "搜查官",                 # 7
    ))

    AddCharChip((
        "chr/ch05900.itc",                   # 00
        "chr/ch05902.itc",                   # 01
        "chr/ch22200.itc",                   # 02
        "chr/ch27802.itc",                   # 03
        "chr/ch30500.itc",                   # 04
        "chr/ch30000.itc",                   # 05
        "chr/ch27600.itc",                   # 06
        "chr/ch27800.itc",                   # 07
    ))

    DeclNpc(4510,    1169,    15779,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(12869,   1000,    4809,    90,   261,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(2259,    140,     5500,    90,   453,  0x0, 0,   3,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(5289,    1019,    16959,   225,  389,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(1370,    29,      1990,    180,  389,  0x0, 0,   5,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-8510,   0,       45979,   0,    389,  0x0, 0,   6,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-569,    29,      39380,   90,   389,  0x0, 0,   7,   0,   0,   0,   0,   9,   255,  0)

    DeclActor(14350,   1000,    -70,     2000,    14350,   2500,    -70,     0x007C, 0,  20, 0x0000)

    ChipFrameInfo(496, 0)                                        # 0

    ScpFunction((
        "Function_0_1F0",          # 00, 0
        "Function_1_2A0",          # 01, 1
        "Function_2_4F7",          # 02, 2
        "Function_3_599",          # 03, 3
        "Function_4_1CB3",         # 04, 4
        "Function_5_2DF5",         # 05, 5
        "Function_6_2F09",         # 06, 6
        "Function_7_305E",         # 07, 7
        "Function_8_30D0",         # 08, 8
        "Function_9_321D",         # 09, 9
        "Function_10_332D",        # 0A, 10
        "Function_11_401F",        # 0B, 11
        "Function_12_429A",        # 0C, 12
        "Function_13_4879",        # 0D, 13
        "Function_14_632E",        # 0E, 14
        "Function_15_6379",        # 0F, 15
        "Function_16_63C4",        # 10, 16
        "Function_17_640F",        # 11, 17
        "Function_18_645A",        # 12, 18
        "Function_19_64A5",        # 13, 19
        "Function_20_64F0",        # 14, 20
    ))


    def Function_0_1F0(): pass

    label("Function_0_1F0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_228"),
        (1, "loc_234"),
        (2, "loc_240"),
        (3, "loc_24C"),
        (4, "loc_258"),
        (5, "loc_264"),
        (6, "loc_270"),
        (SWITCH_DEFAULT, "loc_27C"),
    )


    label("loc_228")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_234")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_240")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_24C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_258")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_264")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_270")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_27C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_288")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_29F")

    Return()

    # Function_0_1F0 end

    def Function_1_2A0(): pass

    label("Function_1_2A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2D8")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, 5510, 1020, 16030, 225)
    Jump("loc_4C9")

    label("loc_2D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2F0")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_4C9")

    label("loc_2F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_30F")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_349")
    SetChrPos(0x8, 3150, 1020, 12920, 0)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4C9")

    label("loc_349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_368")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_387")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_39F")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_4C9")

    label("loc_39F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_408")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3C3")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_403")

    label("loc_3C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DA")
    SetChrFlags(0x8, 0x80)
    Jump("loc_403")

    label("loc_3DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_END)), "loc_3FE")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_403")

    label("loc_3FE")

    SetChrFlags(0x8, 0x80)

    label("loc_403")

    Jump("loc_4C9")

    label("loc_408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_41B")
    SetChrFlags(0x8, 0x80)
    Jump("loc_4C9")

    label("loc_41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_42E")
    SetChrFlags(0x8, 0x80)
    Jump("loc_4C9")

    label("loc_42E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_452")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x10)
    Jump("loc_4C9")

    label("loc_452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_471")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_490")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4AF")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_4AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4C9")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)

    label("loc_4C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F6")
    SetMapFlags(0x10000000)
    Event(0, 13)

    label("loc_4F6")

    Return()

    # Function_1_2A0 end

    def Function_2_4F7(): pass

    label("Function_2_4F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_540")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57F")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_57F")

    ClearMapObjFlags(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_598")
    OP_65(0x0, 0x1)
    SetMapObjFlags(0x0, 0x10)

    label("loc_598")

    Return()

    # Function_2_4F7 end

    def Function_3_599(): pass

    label("Function_3_599")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B3")
    Call(0, 12)
    Jump("loc_1CAF")

    label("loc_5B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_911")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A2")

    #C0001
    ChrTalk(
        0xFE,
        (
            "#02200F是你们啊……\x01",
            "你们看了迪塔的演说吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        "#00001F嗯，可是……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "#02200F由于事态的急剧变化\x01",
            "而感到困惑……\x01",
            "是这样吧？\x02\x03",

            "#02203F大部分市民应该都\x01",
            "怀有这样的心情。\x02\x03",

            "#02201F但是，两大国之间的『暗斗』\x01",
            "确实造成了种种灾难，这是不争的事实。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x102,
        (
            "#00108F……就是迪塔叔叔之前所说的\x01",
            "那些无法解释的『事故』吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "#02203F嗯……\x02\x03",

            "#02201F可我们却对这些事实视而不见，\x01",
            "一直自欺欺人地享受着\x01",
            "眼前的幸福……\x02\x03",

            "正如迪塔所说，\x01",
            "这是我们克洛斯贝尔\x01",
            "全体居民的罪孽。\x02\x03",

            "#02203F我认为，如果想\x01",
            "坦然直面这一点，\x01",
            "独立是必要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        "#00005F伊安律师……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "#02203F……抱歉，\x01",
            "大概是被那演说所感染，\x01",
            "我好像有些控制不住情绪了。\x02\x03",

            "#02200F不管怎么说……\x01",
            "命运的齿轮已经开始转动了。\x02\x03",

            "#02203F接下来要怎么做……\x01",
            "这是我们每个居民\x01",
            "都应该仔细思考的问题。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 1)
    Jump("loc_90C")

    label("loc_8A2")


    #C0008
    ChrTalk(
        0xFE,
        (
            "#02203F命运的齿轮已经开始转动了。\x02\x03",

            "#02200F接下来要怎么做……\x01",
            "这是我们每个居民\x01",
            "都应该仔细思考的问题。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90C")

    Jump("loc_1CAF")

    label("loc_911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_DA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D34")

    #C0009
    ChrTalk(
        0xFE,
        (
            "#02203F呼……\x01",
            "那位客人的公司资料，\x01",
            "还有……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#00000F伊安律师……\x01",
            "您好像很忙啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    #C0011
    ChrTalk(
        0xFE,
        (
            "#02205F哦，是你们啊……\x02\x03",

            "#02203F那起袭击事件似乎\x01",
            "使很多企业遭受到了损失。\x02\x03",

            "#02200F在最近这一周，\x01",
            "我一直在受理他们的咨询，\x01",
            "完全没有时间休息呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        "#00303F……真辛苦啊。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "#02203F嗯……\x01",
            "但这也是没办法的事。\x02\x03",

            "#02200F由于ＩＢＣ遭到破坏，\x01",
            "很多人失去了交易平台\x01",
            "与工作场所。\x02\x03",

            "我身为一名律师，\x01",
            "也必须要尽最大努力，\x01",
            "做好自己能做的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，真不愧是\x01",
            "大胡子熊律师啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        (
            "#00105F可、可是……\x01",
            "您不是还要负责\x01",
            "制订宪法草案吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "#02200F哦，那件工作\x01",
            "总算是完成了，\x01",
            "不久前已经提交给了自治州政府。\x02\x03",

            "#02202F只要肯努力，总还是可以完成的。\x01",
            "为了它，我最近连睡觉的时间都没有了。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        "#00200F这就是所谓的不眠不休啊……\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x109,
        (
            "#10100F那个……请您不要\x01",
            "太勉强自己啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "#02202F呵呵，多谢关心，愧不敢当。\x02\x03",

            "#02203F把今天的咨询处理\x01",
            "完毕之后，我也准备\x01",
            "暂时松口气，在今晚好好休息一下。\x02\x03",

            "#02200F……好了，还有客人在等着我，\x01",
            "就先聊到这里吧。\x02\x03",

            "你们大概也接到了\x01",
            "很多支援请求吧？\x01",
            "要加油啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#00000F嗯，谢谢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 0)
    ClearChrFlags(0x8, 0x10)
    Jump("loc_D9B")

    label("loc_D34")


    #C0021
    ChrTalk(
        0xFE,
        (
            "#02200F为了广大市民，\x01",
            "我一定要充分尽到\x01",
            "律师的职责。\x02\x03",

            "你们大概也接到了\x01",
            "很多支援请求吧？\x01",
            "要加油啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9B")

    Jump("loc_1CAF")

    label("loc_DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E97")

    #C0022
    ChrTalk(
        0xFE,
        (
            "#02200F就在居民投票日\x01",
            "逐渐临近的时候，\x01",
            "发生了占领玛因兹的事件……\x02\x03",

            "似乎有很多市民都认为，\x01",
            "这是帝国或共和国为了让我们\x01",
            "撤回独立提案而策动的阴谋。\x02\x03",

            "#02203F……没想到竟然会\x01",
            "引发如此严重的事态，\x01",
            "连我都没预料到这一点呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F39")

    label("loc_E97")


    #C0023
    ChrTalk(
        0xFE,
        (
            "#02200F有很多人都认为，这次的事件\x01",
            "是帝国或共和国为了让我们\x01",
            "撤回独立提案而策动的阴谋。\x02\x03",

            "#02203F……没想到竟然会\x01",
            "引发如此严重的事态，\x01",
            "连我都没预料到这一点呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F39")

    Jump("loc_1CAF")

    label("loc_F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1434")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135E")

    #C0024
    ChrTalk(
        0xFE,
        "#02200F哦，是你们……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10D8")

    #C0025
    ChrTalk(
        0x101,
        (
            "#00004F伊安律师……\x01",
            "昨天真是\x01",
            "太感谢您了。\x02\x03",

            "#00000F您找到的证据\x01",
            "发挥了很关键的作用呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "#02203F哦，皮特已经把事情的经过告诉我了。\x01",
            "听说已经指名通缉\x01",
            "那个叫敏涅斯的男人了。\x02\x03",

            "#02202F哈哈，话说回来，\x01",
            "其实我也没帮上什么忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            "#00004F哪里的话，真是帮了我们的大忙了。\x02\x03",

            "#00000F制订宪法草案的工作肯定十分繁忙，\x01",
            "我们却还来麻烦您，真是不好意思……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_111F")

    label("loc_10D8")


    #C0028
    ChrTalk(
        0x101,
        (
            "#00000F伊安律师……\x01",
            "好久不见了。\x02\x03",

            "您好像正在忙着\x01",
            "制订宪法草案吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_111F")


    #C0029
    ChrTalk(
        0xFE,
        (
            "#02200F嗯，不过已经\x01",
            "取得一定进展了。\x02\x03",

            "正准备泡杯咖啡，\x01",
            "稍微休息一下呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        (
            "#00105F啊……\x01",
            "我们好像打扰\x01",
            "您休息了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "#02202F哪里，没有的事。\x01",
            "和你们聊一聊，\x01",
            "也能让我转换心情呢。\x02\x03",

            "#02205F……对了，\x01",
            "据说你们调查了\x01",
            "昨天的脱轨事故……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#00000F嗯，已经查明了\x01",
            "事故发生的原因。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x103,
        (
            "#00203F详细说明暂且略过……\x01",
            "总之，可以确定那是一起\x01",
            "人为引发的事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "#02205F唔，是这样啊……\x02\x03",

            "#02203F………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        (
            "#00305F伊安律师……\x01",
            "您怎么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "#02203F……没什么，我只是在想，\x01",
            "没有出现死难者真是万幸啊。\x02\x03",

            "#02200F最近的局势似乎很乱，\x01",
            "你们也要多加小心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16C, 0)
    Jump("loc_142F")

    label("loc_135E")


    #C0037
    ChrTalk(
        0xFE,
        (
            "#02200F宪法草案的制订工作已经取得了一定进展……\x01",
            "但似乎还有继续改良的余地。\x02\x03",

            "#02203F这对我的体力也是个很严峻的考验，\x01",
            "但为了克洛斯贝尔的未来，\x01",
            "绝不能有所松懈。\x02\x03",

            "#02200F我一定会努力制订出\x01",
            "最完善的宪法草案。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_142F")

    Jump("loc_1CAF")

    label("loc_1434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_14C8")

    #C0038
    ChrTalk(
        0x8,
        (
            "#02200F关于这次的事件……\x01",
            "我会在时间允许\x01",
            "的前提下尽量提供协助的。\x02\x03",

            "#02202F呵呵，我稍后会过去露个面的，\x01",
            "你们也要努力\x01",
            "展开调查啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CAF")

    label("loc_14C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_155C")

    #C0039
    ChrTalk(
        0x8,
        (
            "#02200F关于这次的事件……\x01",
            "我会在时间允许\x01",
            "的前提下尽量提供协助的。\x02\x03",

            "#02202F呵呵，我稍后会过去露个面的，\x01",
            "你们也要努力\x01",
            "展开调查啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CAF")

    label("loc_155C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_156A")
    Jump("loc_1CAF")

    label("loc_156A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1578")
    Jump("loc_1CAF")

    label("loc_1578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1744")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16DD")

    #C0040
    ChrTalk(
        0xFE,
        (
            "#02205F哦，是你们啊。\x01",
            "这么晚来，真是少见呢。\x02\x03",

            "#02200F达德利竟然也在一起……\x01",
            "是不是发生了什么与明天的\x01",
            "正式会议有关的问题？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x10A,
        (
            "#00603F我们正要去\x01",
            "确认这一点。\x02\x03",

            "#00600F为了确保万无一失，\x01",
            "最重要的事情就是在事前\x01",
            "消除一切不安定要素。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "#02203F嗯，谨慎一些\x01",
            "终究没有坏处啊。\x02\x03",

            "#02200F虽然不知道事情的详情……\x01",
            "但各位一定要加油啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_173F")

    label("loc_16DD")


    #C0043
    ChrTalk(
        0xFE,
        (
            "#02200F好了……\x01",
            "准备工作至此已经足够了。\x02\x03",

            "#02203F为了顺利完成明天的任务，\x01",
            "今天就早点休息吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_173F")

    Jump("loc_1CAF")

    label("loc_1744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1886")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17FD")

    #C0044
    ChrTalk(
        0xFE,
        (
            "#02200F首脑们都已经\x01",
            "来到克洛斯贝尔了啊。\x02\x03",

            "#02203F通商会议召开首日，\x01",
            "市里的警备\x01",
            "似乎更加森严了。\x02\x03",

            "#02200F事故很容易\x01",
            "在这种时期发生……\x01",
            "你们也要多加注意。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1881")

    label("loc_17FD")


    #C0045
    ChrTalk(
        0xFE,
        (
            "#02203F首脑们均已抵达，\x01",
            "克洛斯贝尔市内的警戒势态\x01",
            "恐怕将会更加森严吧。\x02\x03",

            "#02200F事故很容易\x01",
            "在这种时期发生……\x01",
            "你们也要多加注意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1881")

    Jump("loc_1CAF")

    label("loc_1886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_19CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_195C")

    #C0046
    ChrTalk(
        0xFE,
        (
            "#02200F通商会议终于\x01",
            "要在明天召开了啊。\x02\x03",

            "按照预定计划，各国首脑\x01",
            "都会出席揭幕式……\x02\x03",

            "万一他们发生了什么人身意外，\x01",
            "恐怕就会发展成国际问题了。\x02\x03",

            "你们这些警察一定要\x01",
            "比平时更加努力才行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19C8")

    label("loc_195C")


    #C0047
    ChrTalk(
        0xFE,
        (
            "#02200F如果有什么担心的事情，\x01",
            "随时都可以来找我商量。\x02\x03",

            "只要我能帮得上忙，\x01",
            "一定尽力为大家提供\x01",
            "各种协助。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C8")

    Jump("loc_1CAF")

    label("loc_19CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1B90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B22")

    #C0048
    ChrTalk(
        0xFE,
        (
            "#02203F『黑月』有意收购鲁巴彻旧址，\x01",
            "似乎正在逐步推进计划。\x02\x03",

            "#02201F如果那里真的被黑月收入囊中，\x01",
            "后果实在是不堪设想呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#00008F是啊……\x01",
            "如果那样，恐怕会很棘手呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "#02203F……话虽如此，但我们终究无计可施。\x01",
            "不出意外的话，\x01",
            "那种情况早晚会变为现实吧……\x02\x03",

            "#02200F唉……\x01",
            "克洛斯贝尔的问题\x01",
            "仍旧是堆积如山啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B8B")

    label("loc_1B22")


    #C0051
    ChrTalk(
        0xFE,
        (
            "#02200F鲁巴彻旧址\x01",
            "落入黑月的手中\x01",
            "恐怕只是时间问题而已。\x02\x03",

            "唉……\x01",
            "克洛斯贝尔的问题\x01",
            "仍旧是堆积如山啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B8B")

    Jump("loc_1CAF")

    label("loc_1B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1CAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C55")

    #C0052
    ChrTalk(
        0xFE,
        (
            "#02203F特别任务支援科\x01",
            "深受广大市民\x01",
            "的期待。\x02\x03",

            "#02202F交付给你们的委托\x01",
            "恐怕将会比以往更多，\x01",
            "请一定要加油啊。\x02\x03",

            "只要一步一步慢慢积累，\x01",
            "你们一定能成为\x01",
            "克洛斯贝尔的希望。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CAF")

    label("loc_1C55")


    #C0053
    ChrTalk(
        0xFE,
        (
            "#02200F我也很期待你们\x01",
            "特别任务支援科的表现。\x02\x03",

            "#02202F请一定不要辜负\x01",
            "市民们的期待啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CAF")

    TalkEnd(0xFE)
    Return()

    # Function_3_599 end

    def Function_4_1CB3(): pass

    label("Function_4_1CB3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1DC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CD5")
    TalkEnd(0xFE)
    Call(0, 10)
    Return()

    label("loc_1CD5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CDF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DBE")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",                        # 0
            "阅读伊安律师留下的字条\x01",      # 1
            "放弃\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D53")
    Call(0, 11)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DB9")

    label("loc_1D53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D67")
    Jump("loc_1DB9")

    label("loc_1D67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DB9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0054
    ChrTalk(
        0xFE,
        "各位……谢谢你们。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "伊安律师……\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB9")

    Jump("loc_1CDF")

    label("loc_1DBE")

    Jump("loc_2DF1")

    label("loc_1DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1DD1")
    Jump("loc_2DF1")

    label("loc_1DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1E57")

    #C0056
    ChrTalk(
        0xFE,
        (
            "为了使克洛斯贝尔独立\x01",
            "而制定宪法草案的人\x01",
            "正是伊安律师。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "身为独立的倡导者之一，\x01",
            "伊安律师肯定\x01",
            "怀有很多想法吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF1")

    label("loc_1E57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1F32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EC9")

    #C0058
    ChrTalk(
        0xFE,
        (
            "伊安律师好像\x01",
            "非常忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "如果我能早日独当一面，\x01",
            "就能代替伊安律师\x01",
            "接受咨询了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F2D")

    label("loc_1EC9")


    #C0060
    ChrTalk(
        0xFE,
        (
            "……总之，我现在要\x01",
            "全力协助伊安律师。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "为了给他多争取一些休息时间，\x01",
            "必须要将工作尽早完成。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F2D")

    Jump("loc_2DF1")

    label("loc_1F32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2023")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC6")

    #C0062
    ChrTalk(
        0xFE,
        (
            "玛因兹竟然被\x01",
            "武装集团占领了……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "居民们可是无辜的啊，\x01",
            "这真是太过分了。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "我们这些市民难道\x01",
            "什么都做不了吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_201E")

    label("loc_1FC6")


    #C0065
    ChrTalk(
        0xFE,
        (
            "这次的事件似乎也让\x01",
            "伊安律师感到无比痛心。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "我们这些市民难道\x01",
            "什么都做不了吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_201E")

    Jump("loc_2DF1")

    label("loc_2023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_22EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22AF")

    #C0067
    ChrTalk(
        0xFE,
        (
            "我必须要把昨天发生在\x01",
            "阿尔摩利卡村的事件做个整理……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "如果交给伊安律师，\x01",
            "这份重要的资料肯定又会被掩埋在\x01",
            "堆积如山的文件中了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_215C")

    #C0069
    ChrTalk(
        0x101,
        (
            "#00000F哈哈……不管怎么说，\x01",
            "能把事情解决，真是太好了。\x02\x03",

            "你帮了我们不少忙，\x01",
            "多谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        "哪里，不用客气。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "支援科的各位\x01",
            "才真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22A7")

    label("loc_215C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_END)), "loc_21E6")

    #C0072
    ChrTalk(
        0x101,
        (
            "#00003F（阿尔摩利卡村的事件……\x01",
            "  莫非和那个名叫\x01",
            "  敏涅斯的男子有关吗？）\x02\x03",

            "（……我们真是应该\x01",
            "  努力调查到最后啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22A7")

    label("loc_21E6")


    #C0073
    ChrTalk(
        0x101,
        (
            "#00005F阿尔摩利卡村的事件……\x01",
            "那里发生了什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        "嗯，有个无德商人……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "……啊，抱歉。\x01",
            "真是的，差点说漏嘴……\x01",
            "我可是有保密义务的。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#00000F是、是吗……\x01",
            "算啦，总之\x01",
            "解决了就好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22A7")

    SetScenarioFlags(0x16C, 2)
    Jump("loc_22E9")

    label("loc_22AF")


    #C0077
    ChrTalk(
        0xFE,
        (
            "不管怎么说……\x01",
            "能成功挽救阿尔摩利卡村，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22E9")

    Jump("loc_2DF1")

    label("loc_22EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_230E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2309")
    SetScenarioFlags(0x0, 1)
    Jump("loc_2309")

    label("loc_2309")

    Jump("loc_2DF1")

    label("loc_230E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2594")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2438")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23CF")

    #C0078
    ChrTalk(
        0xFE,
        (
            "我正在调查过去那个\x01",
            "与阿尔摩利卡村这起事件十分相似的案例。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "也许能从意想不到的地方\x01",
            "发现解决事件的突破口呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "伊安律师已经去\x01",
            "哈罗德先生家了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2433")

    label("loc_23CF")


    #C0081
    ChrTalk(
        0xFE,
        (
            "我正在调查过去那个\x01",
            "与阿尔摩利卡村这起事件十分相似的案例。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "伊安律师已经去\x01",
            "哈罗德先生家了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2433")

    Jump("loc_258F")

    label("loc_2438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 3)), scpexpr(EXPR_END)), "loc_2535")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24DA")

    #C0083
    ChrTalk(
        0xFE,
        (
            "伊安律师正在制订宪法草案，\x01",
            "已经忙得焦头烂额了……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "但即使如此，他也绝不会\x01",
            "对这样的事件坐视不管。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "我也会尽全力\x01",
            "来帮忙的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2530")

    label("loc_24DA")


    #C0086
    ChrTalk(
        0xFE,
        (
            "伊安律师虽然很忙，但也绝不会\x01",
            "对这样的事件坐视不管。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "我也会尽全力\x01",
            "来帮忙的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2530")

    Jump("loc_258F")

    label("loc_2535")


    #C0088
    ChrTalk(
        0xFE,
        (
            "伊安律师正在二层\x01",
            "埋头制订宪法草案呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "他今天也十分繁忙，\x01",
            "我必须要努力帮忙才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_258F")

    Jump("loc_2DF1")

    label("loc_2594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_29D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2959")

    #C0090
    ChrTalk(
        0xFE,
        "啊，是特别任务支援科的各位……\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "伊安律师\x01",
            "正在二层\x01",
            "埋头工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x102,
        (
            "#00104F律师最近似乎\x01",
            "相当忙碌吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        "#00005F是这样吗？\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        "嗯，其实……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "律师接受了市长的委托，\x01",
            "正在为实现独立而制定\x01",
            "宪法草案。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26A0")
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_26A0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26C6")
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_26C6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26EC")
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_26EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2712")
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_2712")

    Sleep(1000)

    #C0096
    ChrTalk(
        0x101,
        "#00007F什么！？\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x109,
        (
            "#10101F是『宪法』……\x01",
            "而不是自治州法吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        (
            "#00104F所谓的『宪法』，\x01",
            "是以主权国家为基本前提\x01",
            "而制定的根本法。\x02\x03",

            "#00100F它是决定国家统治权、政治结构，\x01",
            "以及各种重要原则问题的最高法律，\x01",
            "不容别国干涉。\x02\x03",

            "如果想以国家的形式独立，\x01",
            "宪法绝对必不可少。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#00305F呼……\x01",
            "又是个复杂的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x103,
        (
            "#00204F不过，伊安律师\x01",
            "似乎正是最合适的人选……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，在周边诸国\x01",
            "也有活跃表现的大胡子熊律师，\x01",
            "想必可以顺利完成吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "嗯，他一定会制订出\x01",
            "完善的宪法草案。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        (
            "#00000F那就请你代我们\x01",
            "向伊安律师\x01",
            "问个好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "嗯，谢谢。\x01",
            "我想律师一定会受到鼓舞的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16C, 1)
    Jump("loc_29CB")

    label("loc_2959")


    #C0105
    ChrTalk(
        0xFE,
        (
            "律师好像接受了\x01",
            "市长的委托，正在制订\x01",
            "与独立相关的宪法草案。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "我相信伊安律师\x01",
            "一定能制订出\x01",
            "完善的宪法草案。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29CB")

    Jump("loc_2DF1")

    label("loc_29D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A28")

    #C0107
    ChrTalk(
        0xFE,
        (
            "伊安律师今天\x01",
            "外出工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "如果有什么事情，\x01",
            "我稍后可以代为转达。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF1")

    label("loc_2A28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2A90")

    #C0109
    ChrTalk(
        0xFE,
        (
            "哎，这份文件……\x01",
            "放错地方了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "伊安律师可真是的，\x01",
            "在这些方面实在是糊涂马虎……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF1")

    label("loc_2A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2BAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B4E")

    #C0111
    ChrTalk(
        0xFE,
        (
            "哎，刚才那位客人的咨询费……\x01",
            "似乎相当少啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "……伊安律师可真是的，\x01",
            "又随便给人家\x01",
            "降低费用了。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "毕竟是个法律界人士，\x01",
            "在这种方面还是要\x01",
            "有点原则才行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BA6")

    label("loc_2B4E")


    #C0114
    ChrTalk(
        0xFE,
        (
            "……伊安律师可真是的，\x01",
            "又随便给人家\x01",
            "降低费用了。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        "真拿他没办法……（嘀嘀咕咕）\x02",
    )

    CloseMessageWindow()

    label("loc_2BA6")

    Jump("loc_2DF1")

    label("loc_2BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2CA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C41")

    #C0116
    ChrTalk(
        0xFE,
        (
            "伊安律师最近\x01",
            "特别忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "由于通商会议日渐临近的缘故，\x01",
            "前来咨询的人比以前更多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "我也必须要尽己所能地\x01",
            "协助他。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2CA1")

    label("loc_2C41")


    #C0119
    ChrTalk(
        0xFE,
        (
            "由于通商会议日渐临近的缘故，\x01",
            "前来咨询的人比以前更多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "我也必须要尽己所能地\x01",
            "协助他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA1")

    Jump("loc_2DF1")

    label("loc_2CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2D1F")

    #C0121
    ChrTalk(
        0xFE,
        (
            "不知为什么，\x01",
            "最近来咨询的客人\x01",
            "比过去更多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "伊安律师一直在不停工作，\x01",
            "再不休息一下就该累坏了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF1")

    label("loc_2D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2DF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DB0")

    #C0123
    ChrTalk(
        0xFE,
        (
            "啊，是特别任务支援科的各位……\x01",
            "好久不见了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "伊安律师就在办公桌前工作呢。\x01",
            "如果有什么事情，就请过去找他吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2DF1")

    label("loc_2DB0")


    #C0125
    ChrTalk(
        0xFE,
        (
            "伊安律师就在办公桌前工作。\x01",
            "如果有什么事情，就请过去找他吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DF1")

    TalkEnd(0xFE)
    Return()

    # Function_4_1CB3 end

    def Function_5_2DF5(): pass

    label("Function_5_2DF5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E94")

    #C0126
    ChrTalk(
        0xFE,
        (
            "我所任职的公司\x01",
            "就在遭到破坏的\x01",
            "ＩＢＣ大楼内……\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "如今没有了工作场所，\x01",
            "已经陷入完全停业的状态了。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "呼……今后该\x01",
            "怎么办才好啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F05")

    label("loc_2E94")


    #C0129
    ChrTalk(
        0xFE,
        (
            "我所任职的公司在ＩＢＣ内，\x01",
            "如今没有了工作场所，\x01",
            "已经陷入完全停业的状态了。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "呼……今后该\x01",
            "怎么办才好啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F05")

    TalkEnd(0xFE)
    Return()

    # Function_5_2DF5 end

    def Function_6_2F09(): pass

    label("Function_6_2F09")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F22")
    TalkEnd(0xFE)
    Call(0, 10)
    Return()

    label("loc_2F22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3000")

    #C0131
    ChrTalk(
        0xFE,
        (
            "如今看来……\x01",
            "他们从很久以前就开始\x01",
            "谋划此次计划了。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "接下来，就由我们\x01",
            "搜查一科继续搜查\x01",
            "格里姆伍德法律事务所。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        "……各位也要多加小心。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FF8")

    #C0134
    ChrTalk(
        0x10A,
        (
            "#00600F嗯……\x01",
            "这里就拜托你了，艾玛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FF8")

    SetScenarioFlags(0x0, 3)
    Jump("loc_305A")

    label("loc_3000")


    #C0135
    ChrTalk(
        0xFE,
        (
            "接下来，就由我们\x01",
            "搜查一科继续搜查\x01",
            "格里姆伍德法律事务所。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        "……各位也要多加小心。\x02",
    )

    CloseMessageWindow()

    label("loc_305A")

    TalkEnd(0xFE)
    Return()

    # Function_6_2F09 end

    def Function_7_305E(): pass

    label("Function_7_305E")

    TalkBegin(0xFE)

    #C0137
    ChrTalk(
        0xFE,
        (
            "搜查一科正在\x01",
            "搜查格里姆伍德\x01",
            "法律事务所。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "现在已经撬开门锁，进入二层调查了，\x01",
            "希望能找到一些线索。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_305E end

    def Function_8_30D0(): pass

    label("Function_8_30D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_319C")

    #C0139
    ChrTalk(
        0xFE,
        (
            "好像都是些\x01",
            "中世纪炼金术或塞姆里亚\x01",
            "文明方面的资料啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "这些资料相当古老……\x01",
            "想收集到如此大量的古籍，\x01",
            "恐怕需要长年的积累。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "嫌疑人伊安究竟是从何时\x01",
            "开始谋划此次计划的……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3219")

    label("loc_319C")


    #C0142
    ChrTalk(
        0xFE,
        (
            "这些资料相当古老……\x01",
            "想收集到如此大量的古籍，\x01",
            "恐怕需要长年的积累。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "嫌疑人伊安究竟是从何时\x01",
            "开始谋划此次计划的……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3219")

    TalkEnd(0xFE)
    Return()

    # Function_8_30D0 end

    def Function_9_321D(): pass

    label("Function_9_321D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32C1")

    #C0144
    ChrTalk(
        0xFE,
        (
            "在终端中发现了与ＩＢＣ及兰花塔\x01",
            "频繁通讯的记录。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "事件的幕后黑手伊安恐怕就是在这个地方\x01",
            "向总统……不，向嫌疑人库罗伊斯等人\x01",
            "做出指示的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3329")

    label("loc_32C1")


    #C0146
    ChrTalk(
        0xFE,
        (
            "事件的幕后黑手伊安恐怕就是在这个地方\x01",
            "向嫌疑人库罗伊斯等人\x01",
            "做出指示的。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        "必须要慎重展开调查……\x02",
    )

    CloseMessageWindow()

    label("loc_3329")

    TalkEnd(0xFE)
    Return()

    # Function_9_321D end

    def Function_10_332D(): pass

    label("Function_10_332D")

    EventBegin(0x0)
    Fade(500)
    OP_68(6060, 2320, 15510, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18770, 0)
    SetChrPos(0x101, 7120, 1020, 15230, 270)
    SetChrPos(0x102, 7010, 1020, 16640, 270)
    SetChrPos(0x103, 7000, 1020, 13880, 315)
    SetChrPos(0x104, 8300, 1000, 14190, 270)
    SetChrPos(0xF4, 8600, 1000, 15690, 270)
    SetChrPos(0xF5, 8400, 1000, 17000, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xB, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_93(0xB, 0x5A, 0x0)
    OP_93(0x9, 0xE1, 0x0)
    OP_0D()

    #C0148
    ChrTalk(
        0x9,
        "#11P（抽泣）呜呜……\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        "#11P伊安律师……为什么……\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        "#11P#00005F皮特……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x9, 0x5A, 0x1F4)

    #C0151
    ChrTalk(
        0x9,
        "#6P各、各位……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34E0")

    #C0152
    ChrTalk(
        0xB,
        (
            "#5P达德利长官……\x01",
            "还有特别任务支援科，\x01",
            "各位辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x10A,
        "#11P#00603F……嗯。\x02",
    )

    CloseMessageWindow()
    Jump("loc_350A")

    label("loc_34E0")


    #C0154
    ChrTalk(
        0xB,
        (
            "#5P特别任务支援科的各位……\x01",
            "辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_350A")


    #C0155
    ChrTalk(
        0x101,
        (
            "#11P#00001F艾玛搜查官，您也辛苦了。\x01",
            "……正在搜查伊安律师的事务所吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        (
            "#5P嗯……搜查一科已将其认定为\x01",
            "重要参考人，正在展开调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xB,
        (
            "#5P虽然有些残酷……\x01",
            "但这位少年是格里姆伍德的助手，\x01",
            "只好请他以相关人士的身份留在调查现场。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x9,
        (
            "#6P（哽咽）……\x01",
            "不，这是我主动提出的要求。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x9,
        (
            "#6P伊安律师……在消失不见之前，\x01",
            "曾对我说过很耐人寻味的话……\x01",
            "所以我无论如何也想确认其中的含义。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 5)), scpexpr(EXPR_END)), "loc_3705")

    #C0160
    ChrTalk(
        0x104,
        (
            "#11P#00308F哦……是指让你\x01",
            "整理办公桌吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        (
            "#11P#00106F在那种时候\x01",
            "突然提出如此请求，\x01",
            "的确是很令人在意……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_394F")

    label("loc_3705")


    #C0162
    ChrTalk(
        0x102,
        "#11P#00105F耐人寻味的话……？\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x9,
        "#6P……是的。\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x9,
        (
            "#6P伊安律师让我在『魔导兵』四处徘徊的\x01",
            "异常事态平息下来之后……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x9,
        (
            "#6P返回事务所，\x01",
            "整理他的办公桌。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        "#11P#00005F整理办公桌……？\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x9,
        (
            "#6P嗯，一开始我还以为他走得太急，\x01",
            "所以来不及整理……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x9,
        (
            "#6P可仔细一想，虽然伊安律师一直\x01",
            "都让我负责扫除和整理文件，但他曾多次提醒过我，\x01",
            "说唯独桌子是绝对不能碰的。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x9,
        (
            "#6P由于工作性质的缘故，他有不少东西，\x01",
            "连我这个当助手的都不能随便看，\x01",
            "一直都那样放在原处……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x102,
        (
            "#11P#00108F伊安律师……\x01",
            "嗯，这确实令人在意呢……\x02\x03",

            "#00106F在那种时候竟然\x01",
            "拜托别人整理通常不能碰的办公桌，\x01",
            "真是难以理解啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_394F")


    #C0171
    ChrTalk(
        0x9,
        (
            "#6P这个谜题的答案……\x01",
            "刚刚已经在伊安律师的办公桌内找到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x9,
        "#6P……就是这个。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0173
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "皮特递过一枚已经开封的信封。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_39D6():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_39D6)
    Sleep(50)

    def lambda_39E6():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_39E6)
    Sleep(50)

    def lambda_39F6():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_39F6)
    Sleep(50)

    def lambda_3A06():
        TurnDirection(0xF4, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_3A06)
    Sleep(50)

    def lambda_3A16():
        TurnDirection(0xF5, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_3A16)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(500)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3ADF")

    #C0174
    ChrTalk(
        0x105,
        "#11P#10401F这是……留言条吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B48")

    label("loc_3ADF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B15")

    #C0175
    ChrTalk(
        0x109,
        "#11P#10101F这是……留言条？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B48")

    label("loc_3B15")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B48")

    #C0176
    ChrTalk(
        0x106,
        "#11P#10701F这是……留言条吗？\x02",
    )

    CloseMessageWindow()

    label("loc_3B48")


    #C0177
    ChrTalk(
        0x101,
        "#11P#00001F……我们可以看吗？\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x9,
        "#6P………………（点头）\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(300)
    Call(0, 11)

    #C0179
    ChrTalk(
        0x101,
        "#11P#00006F……伊安律师……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C09")

    #C0180
    ChrTalk(
        0x101,
        "#11P#00008F……………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C88")

    label("loc_3C09")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C4B")

    #C0181
    ChrTalk(
        0x109,
        "#11P#10108F……………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C88")

    label("loc_3C4B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C88")

    #C0182
    ChrTalk(
        0x105,
        "#11P#10408F……………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_3C88")


    #C0183
    ChrTalk(
        0xB,
        (
            "#5P……除此之外，\x01",
            "他的办公桌内\x01",
            "还保存着一些文件。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xB,
        (
            "#5P详细记录着事务所\x01",
            "正在受理的咨询内容，\x01",
            "以及今后应对委托人的方针……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xB,
        (
            "#5P另外，还发现了过继手续\x01",
            "方面的文件，看来格里姆伍德已经\x01",
            "为这名少年选好了接下来的监护人。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x9,
        (
            "#6P……呜呜，伊安律师……\x01",
            "为什么要这样做……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3DA0():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3DA0)
    Sleep(50)

    def lambda_3DB0():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3DB0)
    Sleep(50)

    def lambda_3DC0():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3DC0)
    Sleep(50)

    def lambda_3DD0():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3DD0)
    Sleep(50)

    def lambda_3DE0():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_3DE0)
    Sleep(50)

    def lambda_3DF0():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_3DF0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(500)

    #C0187
    ChrTalk(
        0x9,
        (
            "#6P要我忘记对自己关怀备至的律师，\x01",
            "幸福地生活下去？\x01",
            "我怎么可能做得到啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x102,
        "#11P#00106F皮特……\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x103,
        "#11P#00208F……伊安律师真是个大笨蛋。\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x104,
        (
            "#11P#00306F嗯，虽然我没资格这么说别人……\x01",
            "但这种留封书信便一走了之的做法\x01",
            "是绝对不能让人接受的。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x101,
        (
            "#11P#00003F……正是如此。\x02\x03",

            "#00008F皮特，我们接下来准备\x01",
            "前往伊安律师所在的地方。\x02\x03",

            "#00001F我们一定会在那里查明一切真相……\x01",
            "并把律师他们带回来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x9,
        (
            "#6P各、各位……\x01",
            "……呜，谢谢你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x9,
        (
            "#6P伊安律师……\x01",
            "就拜托各位了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x9, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_93(0x9, 0xE1, 0x0)
    OP_93(0xB, 0xE1, 0x0)
    SetScenarioFlags(0x1BD, 6)
    EventEnd(0x5)
    Return()

    # Function_10_332D end

    def Function_11_401F(): pass

    label("Function_11_401F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(18, 0, 40, 0)
    SetChrName("")

    #A0194
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "致皮特──\x01",
            "首先，请容我表示歉意。\x01",
            "我突然不辞而别，只给你留下了一封这样的书信。\x02\x01",

            "自从当年我以监护人的身份将你收留，\x01",
            "并让你在事务所工作之后，\x01",
            "每一天都过得无比灿烂愉快。\x02\x01",

            "自那命中注定的残酷之日起，我的人生便被哀伤与叹息所支配，\x01",
            "唯一的生存目标便是达成此次计划。\x01",
            "你的到来使我的人生照进了一线光芒……我对你的感谢之情难以言表。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 40, 0)

    #A0195
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "由于你的出现，\x01",
            "我也曾苦恼并动摇过……\x02\x01",

            "但终究还是无法将计划终止。\x01",
            "我已经无法再回头了。\x02\x01",

            "皮特……\x01",
            "希望你能将我遗忘，幸福地生活下去。\x02\x01",

            "我会在遥远的地方向女神祈祷，\x01",
            "祝愿聪明能干的你逐渐成长为优秀的大人。\x02\x01",

            "　　　　　　　──伊安·格里姆伍德\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_11_401F end

    def Function_12_429A(): pass

    label("Function_12_429A")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02200.itp")
    OP_68(4790, 1920, 14330, 0)
    MoveCamera(39, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20480, 0)
    SetChrPos(0x101, 4830, 1020, 12570, 0)
    SetChrPos(0x102, 3990, 1020, 12720, 0)
    SetChrPos(0x109, 5650, 1000, 11990, 0)
    SetChrPos(0x105, 2910, 1000, 11990, 0)
    SetChrSubChip(0x8, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0196
    ChrTalk(
        0x8,
        "#5P#02205F哦哦，是你们……\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        "#00000F好久不见了，伊安律师。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "#5P#02200F哈哈，好久不见啊。\x01",
            "之前听说你们暂时\x01",
            "停止工作了……\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x101,
        (
            "#00000F嗯，如今已经恢复工作了，\x01",
            "今后也请您继续关照。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x8,
        (
            "#5P#02200F呵呵，原来如此。\x01",
            "而且还加入了新成员，\x01",
            "这就是所谓的焕然一新吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x105,
        (
            "#12P#10300F您就是那位\x01",
            "有名的『大胡子熊律师』吧？\x02\x03",

            "#10304F呵呵，今后还请多多关照了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)
    Sleep(150)

    #C0202
    ChrTalk(
        0x8,
        (
            "#5P#02205F哦哦，太客气了。\x02\x03",

            "#02203F……嗯？\x01",
            "我把名片放到哪里了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4542")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4542")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4568")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4568")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_458E")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_458E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45B4")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_45B4")

    Sleep(1000)
    TurnDirection(0x109, 0x105, 500)
    Sleep(500)

    #C0203
    ChrTalk(
        0x109,
        (
            "#10106F瓦、瓦吉……\x01",
            "你在面对长辈的时候\x01",
            "倒是很有礼貌啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x102,
        (
            "#12P#00100F真是的，伊安律师\x01",
            "未免也太郑重其事了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(150)

    #C0205
    ChrTalk(
        0x8,
        (
            "#5P#02202F哈哈，哪里的话……\x01",
            "在人与人的交往中，\x01",
            "自我介绍可是非常重要的。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x109, 0x0, 0x1F4)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0206
    AnonymousTalk(
        0x8,
        (
            "咳咳，那么，\x01",
            "正式自我介绍一下。\x02\x03",

            "我的名字是伊安·格里姆伍德，\x01",
            "担任这家法律事务所\x01",
            "所长的律师。\x02\x03",

            "特别任务支援科的诸位，\x01",
            "今后还请多多关照。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0207
    ChrTalk(
        0x109,
        (
            "#10100F我们才是，\x01",
            "请您多多关照！\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        (
            "#00000F我们今后说不定还要\x01",
            "找您咨询各方面的事情。\x02\x03",

            "#00004F到时还请助我们\x01",
            "一臂之力。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x8,
        (
            "#5P#02200F嗯，随时欢迎\x01",
            "你们过来。\x02\x03",

            "只要我能帮得上忙，\x01",
            "无论遇到什么事情都可以来和我商量。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x12C, 4)
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_429A end

    def Function_13_4879(): pass

    label("Function_13_4879")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x8, 6600, 140, 5500, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("chr/ch03002.itc", 0x23)
    OP_68(-940, 1300, -180, 0)
    MoveCamera(38, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, -2710, 0, -490, 90)
    SetChrPos(0x102, -2710, 0, -490, 90)
    SetChrPos(0x103, -2710, 0, -490, 90)
    SetChrPos(0x104, -2710, 0, -490, 90)
    SetChrPos(0x109, -2710, 0, -490, 90)
    SetChrPos(0x105, -2710, 0, -490, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 15)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 16)
    Sleep(700)
    OP_68(2570, 1300, 1440, 5000)
    MoveCamera(65, 23, 0, 5000)
    OP_6E(440, 5000)
    SetCameraDistance(20900, 5000)
    BeginChrThread(0x104, 3, 0, 17)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 18)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 19)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x8, 0x1)

    #C0210
    ChrTalk(
        0x8,
        "#02205F哦……？\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x101,
        "#00000F伊安律师！\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x103,
        (
            "#00204F太好了……\x01",
            "您在事务所啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x8,
        (
            "#02200F嗯，现在正好\x01",
            "在休息……\x02\x03",

            "#02201F……唔，莫非有什么事情\x01",
            "要找我商量吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x102,
        (
            "#00100F您看出来了啊……\x01",
            "真不愧是伊安律师。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x8,
        (
            "#02203F呵呵，\x01",
            "毕竟我接触过的委托人\x01",
            "都已经成百上千了啊。\x02\x03",

            "#02200F好了，请到那边就坐吧。\x01",
            "虽然我现在比较忙，\x01",
            "不过还是可以和各位谈谈的。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x101,
        "#00004F不好意思……真是太感谢了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0217
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人将日前调查到的\x01",
            "敏涅斯个人信息与具体行动……\x02\x03",

            "以及今日了解到的\x01",
            "敏涅斯收集土地产权证的情况\x01",
            "向伊安律师做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x1)
    SetChrSubChip(0x8, 0x0)
    OP_68(5320, 500, 6810, 0)
    MoveCamera(39, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21670, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 2310, 200, 5400, 90)
    SetChrPos(0x102, 2310, 200, 4570, 90)
    SetChrPos(0x103, 2260, 200, 6070, 90)
    SetChrPos(0x104, 4530, 200, 7520, 180)
    SetChrPos(0x109, 3780, 200, 7520, 180)
    SetChrPos(0x105, 5160, 200, 7520, 180)
    FadeToBright(1000, 0)
    OP_0D()

    #C0218
    ChrTalk(
        0x8,
        (
            "#02200F唔……原来如此。\x01",
            "我已经了解事情的大致情况了。\x02\x03",

            "虽然我很想正式受理\x01",
            "这起事件……\x02\x03",

            "#02203F但你们也知道，\x01",
            "我如今还有制订宪法草案\x01",
            "这件重要工作在身。\x02\x03",

            "#02203F所以很抱歉，我实在是\x01",
            "挤不出调查的时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x103,
        "#00203F虽然遗憾……但也没办法呢。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x102,
        (
            "#00102F您能陪我们\x01",
            "商讨一阵，\x01",
            "就已经帮了大忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x8,
        (
            "#02203F真对不起……\x01",
            "作为补偿，我尽量给你们\x01",
            "提供一些建议吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x101,
        (
            "#00004F非常感谢。\x02\x03",

            "#00001F那么……是什么建议呢？\x02\x03",

            "通过敏涅斯至今为止的行动……\x01",
            "您是否可以推测出\x01",
            "他的某些犯罪征兆呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0223
    ChrTalk(
        0x8,
        "#02203F我只是想起了一起类似的事件。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0224
    ChrTalk(
        0x104,
        "#00309F嘿，真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x8,
        (
            "#02200F嗯……某位帝国的朋友\x01",
            "曾给过我一份参考资料，\x01",
            "其中记载了一件十分相似的案例。\x02\x03",

            "话虽如此，但我也不能断言\x01",
            "这两起事件完全相同……\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        (
            "#00003F……我们如今\x01",
            "需要一切与\x01",
            "调查相关的线索。\x02\x03",

            "#00003F能否和我们说说\x01",
            "那起类似的事件呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x8,
        (
            "#02200F……嗯，好吧。\x01",
            "毕竟是你们的请求。\x02\x03",

            "#02203F咳咳，是这样的……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    #C0228
    ChrTalk(
        0x8,
        (
            "#02203F数年前……\x01",
            "埃雷波尼亚帝国的某位男爵家中，\x01",
            "有一位男子前来拜访。\x02\x03",

            "#02201F那个男人的名字是『利德纳』……\x01",
            "他自称是在某家著名酿酒公司中\x01",
            "任职的精英商务人士。\x02\x03",

            "随后，利德纳开始\x01",
            "向男爵提起了和赚钱有关的话题。\x02\x03",

            "男爵家拥有一片广阔的麦田，\x01",
            "那是家族世代相传的领地……\x01",
            "而利德纳便提议使用那片土地来建立酿酒公司。\x02\x03",

            "#02203F在领地内建造啤酒工厂，\x01",
            "经营权由男爵家掌管……\x01",
            "大概就是这样的内容。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        "#00005F……！这内容……\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x105,
        (
            "#10300F呵呵……\x01",
            "好像曾在什么地方\x01",
            "听到过类似的话呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x8,
        (
            "#02203F男爵一口应承了下来，\x01",
            "并在利德纳带来的合同上\x01",
            "签了字。\x02\x03",

            "#02200F就这样，利德纳以管理和\x01",
            "建造工厂为名义，得到了\x01",
            "整片麦田及部分土地的产权证。\x02\x03",

            "另外，男爵还拿出了一部分资产，\x01",
            "作为创建公司的启动资金，\x01",
            "逐步做着开展事业的准备工作……\x02\x03",

            "#02203F可是……利德纳却带着\x01",
            "土地产权证与那一部分资产，\x01",
            "突然消失不见了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0232
    ChrTalk(
        0x104,
        "#00305F什么……！？\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x8,
        (
            "#02203F突然与利纳德失去了联系，\x01",
            "男爵家的人都很焦急……\x02\x03",

            "但他们却没能察觉到\x01",
            "当时正在发生的重大事态。\x02\x03",

            "#02201F令人万万没有想到的是，\x01",
            "利德纳将对方寄存在自己手中的\x01",
            "土地产权证转卖给了第三方。\x02\x03",

            "——那片土地，正是最适合建造高级别墅区的好地方。\x02\x03",

            "#02203F最后，留给男爵一家的，\x01",
            "只有一笔巨大的债务……\x01",
            "很快，他们就陷入到了被迫变卖全部领地的困境。\x02\x03",

            "由于失去了领地，爵位也随之被剥夺了……\x01",
            "在那之后，他们一家便下落不明了……\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x104,
        (
            "#00306F这真是……\x01",
            "一段惊人的往事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x109,
        (
            "#10101F竟然擅自变卖他人的土地……\x02\x03",

            "这实在是太过分了！\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x8,
        (
            "#02203F这就是听了你们的话之后，\x01",
            "我首先回想起来的事件。\x02\x03",

            "伪造自己的身份，骗取对方的信任，\x01",
            "最终骗取巨大数额的财产……\x02\x03",

            "#02201F在所谓的『诈骗』行为中，\x01",
            "这可以算是一种很典型的手段吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0237
    ChrTalk(
        0x102,
        "#00105F诈骗……！\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x103,
        (
            "#00203F也就是说，那个名叫敏涅斯的人\x01",
            "并不是昆西公司的董事……\x02\x03",

            "#00200F有可能只是一名诈骗犯？\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x8,
        (
            "#02203F嗯……虽然还不能断定，\x01",
            "但可能性恐怕很高。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        (
            "#00003F经过我们的调查可以确认，\x01",
            "两起事件的确有很多相同点……\x02\x03",

            "#00001F暂且就将这起事件\x01",
            "视为诈骗事件，\x01",
            "在此前提下展开调查吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x109,
        (
            "#10103F既然如此……\x01",
            "我们应该调查的事情\x01",
            "也就显而易见了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x101,
        (
            "#00000F嗯，是啊。\x01",
            "那个名叫敏涅斯的男人\x01",
            "主要有两个可疑之处。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(300)

    #C0243
    ChrTalk(
        0x101,
        (
            "#00001F首先是他的计划……\x01",
            "『阿尔摩利卡·甜蜜商社』\x01",
            "是否真的存在，这是一个疑点。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x105,
        (
            "#10303F关于这个问题，\x01",
            "只要能了解其财产的动向，\x01",
            "说不定就可以确认了。\x02\x03",

            "#10300F既然要在克洛斯贝尔开拓事业，\x01",
            "想必需要到ＩＢＣ\x01",
            "请求融资。\x02\x03",

            "如果他的计划是假的，\x01",
            "在ＩＢＣ留下证据\x01",
            "的可能性应该很高。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        (
            "#00003F而另一个需要确认的问题就是，\x01",
            "敏涅斯究竟是不是\x01",
            "『昆西公司』的董事。\x02\x03",

            "#00001F……那家公司是外国企业，\x01",
            "如果想取证，恐怕会相当麻烦……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)

    #C0246
    ChrTalk(
        0x102,
        (
            "#00103F虽然也许起不到\x01",
            "什么作用……\x02\x03",

            "#00100F不过，我家说不定\x01",
            "有一些可供参考的资料。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(50)

    #C0247
    ChrTalk(
        0x103,
        "#00205F可供参考的资料……？\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        (
            "#00100F嗯，我家有一本\x01",
            "昆西公司的宣传手册。\x02\x03",

            "里面应该记载着一些\x01",
            "公司概要之类的内容，\x01",
            "说不定能从中得到参考。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x104,
        (
            "#00300F昆西公司的宣传手册……\x01",
            "大小姐家里为什么会有那种东西啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    #C0250
    ChrTalk(
        0x102,
        (
            "#00113F那个，其实……\x01",
            "我很喜欢制作甜点……\x02\x03",

            "#00100F所以当时对昆西公司\x01",
            "非常有兴趣，\x01",
            "就索要了一本宣传手册。\x02\x03",

            "那本手册应该就放在\x01",
            "我房间的书架上……\x02\x03",

            "#00106F……唔，仔细想想，还是不行啊。\x01",
            "再怎么说，那种普通的宣传手册也……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "#02203F不，从中得到收获的可能性还是有的。\x02\x03",

            "#02200F既然是公司的正式资料，\x01",
            "说不定能从里面发现一些\x01",
            "与敏涅斯之言产生矛盾的内容。\x02\x03",

            "谨慎起见，还是去调查一下如何？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x109, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    #C0252
    ChrTalk(
        0x101,
        (
            "#00003F说的对……\x01",
            "我们就去艾莉家看看吧。\x02\x03",

            "#00000F……伊安律师，\x01",
            "感谢您的宝贵建议。\x02\x03",

            "多亏您的协助，我基本已经\x01",
            "定好了接下来的调查方针。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x8,
        (
            "#02200F嗯，要是能稍微帮上忙的话，\x01",
            "那就再好不过了。\x02\x03",

            "……你们现在好像\x01",
            "是以哈罗德家为据点\x01",
            "展开调查吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        "#00005F嗯，是的……\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x8,
        (
            "#02200F关于这次的事件……\x01",
            "我会在时间允许\x01",
            "的前提下尽量提供协助的。\x02\x03",

            "#02203F但我现在实在是太忙，\x01",
            "恐怕也起不到太大作用了。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x102,
        (
            "#00109F哪里的话……\x01",
            "有您帮忙，让我们信心百倍！\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x105,
        (
            "#10302F有专业人士相助，\x01",
            "胜过百人之力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x8,
        (
            "#02202F呵呵，我稍后会过去露个面的，\x01",
            "你们也要努力\x01",
            "展开调查啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#00000F嗯，十分感谢。\x02\x03",

            "#00003F……好，那我们就\x01",
            "赶快开始调查吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(300)

    #C0260
    ChrTalk(
        0x101,
        (
            "#00001F去ＩＢＣ调查其资金流向，\x01",
            "从而确认敏涅斯的计划……\x02\x03",

            "另外就是调查麦克道尔官邸\x01",
            "的资料，以其中的内容为参考，\x01",
            "探寻敏涅斯之言中的矛盾之处……\x02\x03",

            "调查任务就是以上两点。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x109,
        (
            "#10102F明白……\x01",
            "我们一定要找到证据！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x87, 0x1, 0x1)
    SetScenarioFlags(0x177, 3)
    ClearMapFlags(0x10000000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    SetChrPos(0x0, 2400, 30, 1120, 225)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_13_4879 end

    def Function_14_632E(): pass

    label("Function_14_632E")


    def lambda_6333():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6333)

    def lambda_6344():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6344)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 3290, 30, 900, 2000, 0x0)
    TurnDirection(0x101, 0x8, 500)
    Return()

    # Function_14_632E end

    def Function_15_6379(): pass

    label("Function_15_6379")


    def lambda_637E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_637E)

    def lambda_638F():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_638F)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 2330, 30, 1420, 2000, 0x0)
    TurnDirection(0x102, 0x8, 500)
    Return()

    # Function_15_6379 end

    def Function_16_63C4(): pass

    label("Function_16_63C4")


    def lambda_63C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_63C9)

    def lambda_63DA():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_63DA)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 3210, 30, -360, 2000, 0x0)
    TurnDirection(0x103, 0x8, 500)
    Return()

    # Function_16_63C4 end

    def Function_17_640F(): pass

    label("Function_17_640F")


    def lambda_6414():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6414)

    def lambda_6425():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6425)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 2300, 30, 80, 2000, 0x0)
    TurnDirection(0x104, 0x8, 500)
    Return()

    # Function_17_640F end

    def Function_18_645A(): pass

    label("Function_18_645A")


    def lambda_645F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_645F)

    def lambda_6470():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6470)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 1960, 30, -1080, 2000, 0x0)
    TurnDirection(0x109, 0x8, 500)
    Return()

    # Function_18_645A end

    def Function_19_64A5(): pass

    label("Function_19_64A5")


    def lambda_64AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_64AA)

    def lambda_64BB():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_64BB)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 1200, 0, 350, 2000, 0x0)
    TurnDirection(0x105, 0x8, 500)
    Return()

    # Function_19_64A5 end

    def Function_20_64F0(): pass

    label("Function_20_64F0")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0262
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门被锁住了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_20_64F0 end

    SaveToFile()

Try(main)
