from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0240.bin",                # FileName
        "c0240",                    # MapName
        "c0240",                    # Location
        0x000F,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 15, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0240",                  # 0
        "萨米",                   # 1
        "金德尔",                 # 2
        "布里吉塔",               # 3
        "卢威克老人",             # 4
        "奥丽加夫人",             # 5
        "伊莉娅",                 # 6
        "修利",                   # 7
        "阿鲁姆",                 # 8
        "艾娅莉",                 # 9
        "庞斯",                   # 10
    ))

    AddCharChip((
        "chr/ch25600.itc",                   # 00
        "chr/ch21800.itc",                   # 01
        "chr/ch21802.itc",                   # 02
        "chr/ch20300.itc",                   # 03
        "chr/ch21600.itc",                   # 04
        "chr/ch21602.itc",                   # 05
        "chr/ch20100.itc",                   # 06
        "chr/ch20102.itc",                   # 07
        "chr/ch05100.itc",                   # 08
        "chr/ch10002.itc",                   # 09
        "chr/ch46300.itc",                   # 0A
        "chr/ch46200.itc",                   # 0B
        "chr/ch20200.itc",                   # 0C
    ))

    DeclNpc(9060,    10000,   18000,   45,   261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-2009,   1149,    60479,   270,  261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(8470,    1019,    62380,   0,    261,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-45650,  1019,    60169,   180,  261,  0x0, 0,   4,   0,   0,   2,   0,   8,   255,  0)
    DeclNpc(7030,    150,     6969,    180,  261,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(54020,   1019,    60490,   270,  261,  0x0, 0,   8,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(52540,   1149,    60540,   270,  261,  0x0, 0,   9,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(-45360,  1029,    61159,   135,  389,  0x0, 0,   10,  0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-46959,  1049,    60360,   180,  389,  0x0, 0,   11,  0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-15119,  0,       5829,    270,  389,  0x0, 0,   12,  0,   0,   0,   0,   14,  255,  0)

    DeclActor(-340,    10000,   20320,   1200,    -340,    11500,   20320,   0x007C, 0,  18, 0x0000)

    ChipFrameInfo(596, 0)                                        # 0

    ScpFunction((
        "Function_0_254",          # 00, 0
        "Function_1_304",          # 01, 1
        "Function_2_32F",          # 02, 2
        "Function_3_35A",          # 03, 3
        "Function_4_731",          # 04, 4
        "Function_5_7DC",          # 05, 5
        "Function_6_17AC",         # 06, 6
        "Function_7_2653",         # 07, 7
        "Function_8_3093",         # 08, 8
        "Function_9_380D",         # 09, 9
        "Function_10_38F7",        # 0A, 10
        "Function_11_40DC",        # 0B, 11
        "Function_12_4110",        # 0C, 12
        "Function_13_4160",        # 0D, 13
        "Function_14_430E",        # 0E, 14
        "Function_15_4370",        # 0F, 15
        "Function_16_449F",        # 10, 16
        "Function_17_4631",        # 11, 17
        "Function_18_4F89",        # 12, 18
        "Function_19_5276",        # 13, 19
    ))


    def Function_0_254(): pass

    label("Function_0_254")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_28C"),
        (1, "loc_298"),
        (2, "loc_2A4"),
        (3, "loc_2B0"),
        (4, "loc_2BC"),
        (5, "loc_2C8"),
        (6, "loc_2D4"),
        (SWITCH_DEFAULT, "loc_2E0"),
    )


    label("loc_28C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_298")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_303")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_303")

    Return()

    # Function_0_254 end

    def Function_1_304(): pass

    label("Function_1_304")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32E")
    OP_94(0xFE, 0xFFFFF858, 0x2A44, 0x866, 0x311A, 0x3E8)
    Sleep(300)
    Jump("Function_1_304")

    label("loc_32E")

    Return()

    # Function_1_304 end

    def Function_2_32F(): pass

    label("Function_2_32F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_359")
    OP_94(0xFE, 0xFFFF4C46, 0xE4C0, 0xFFFF592A, 0xF078, 0x3E8)
    Sleep(300)
    Jump("Function_2_32F")

    label("loc_359")

    Return()

    # Function_2_32F end

    def Function_3_35A(): pass

    label("Function_3_35A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_38A")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_730")

    label("loc_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3E1")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0x8, 2310, 0, 1000, 225)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 1570, 0, 1740, 225)
    Jump("loc_730")

    label("loc_3E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_416")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xC, -39810, 1030, 62640, 0)
    Jump("loc_730")

    label("loc_416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_446")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_730")

    label("loc_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_485")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45E")
    SetChrFlags(0x9, 0x10)

    label("loc_45E")

    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_730")

    label("loc_485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4EF")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xB, -44550, 1020, 59150, 315)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EA")
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_4EA")

    Jump("loc_730")

    label("loc_4EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_52E")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, 5740, 1000, 62320, 0)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_730")

    label("loc_52E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_568")
    SetChrPos(0x8, -52720, 1000, 63170, 0)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_730")

    label("loc_568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_598")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_730")

    label("loc_598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5C8")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_730")

    label("loc_5C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_635")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xB, 0x5)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xB, -48700, 1200, 60400, 270)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -51460, 1200, 60400, 90)
    Jump("loc_730")

    label("loc_635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_68F")
    SetChrFlags(0x9, 0x80)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xC, -51460, 1200, 60400, 90)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x9)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x10)
    Jump("loc_730")

    label("loc_68F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6BF")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_730")

    label("loc_6BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6EF")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_730")

    label("loc_6EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_730")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xC, -51460, 1200, 60400, 90)

    label("loc_730")

    Return()

    # Function_3_35A end

    def Function_4_731(): pass

    label("Function_4_731")

    ClearMapObjFlags(0x2, 0x10)
    OP_66(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_753")
    OP_65(0x0, 0x1)
    SetMapObjFlags(0x2, 0x10)

    label("loc_753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_79C")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_79C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DB")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_7DB")

    Return()

    # Function_4_731 end

    def Function_5_7DC(): pass

    label("Function_5_7DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_925")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B7")

    #C0001
    ChrTalk(
        0xFE,
        (
            "湿地竟然出现了那种东西……\x01",
            "虽然感觉很不安，\x01",
            "但还是要认真完成工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "修利好像\x01",
            "一直在彩虹剧团\x01",
            "努力练习呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "为了迎接伊莉娅小姐归来的那一天，\x01",
            "我也得好好努力，把公寓认真打扫干净。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_920")

    label("loc_8B7")


    #C0004
    ChrTalk(
        0xFE,
        (
            "修利好像\x01",
            "一直在彩虹剧团\x01",
            "努力练习呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "为了迎接伊莉娅小姐归来的那一天，\x01",
            "我得把公寓认真打扫干净。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_920")

    Jump("loc_17A8")

    label("loc_925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_997")

    #C0006
    ChrTalk(
        0xFE,
        (
            "啊，怎么办呢……\x01",
            "市里竟然发生了这种事。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "总、总之，必须要通知\x01",
            "房间里的各位，让他们别出门。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17A8")

    label("loc_997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A07")

    #C0008
    ChrTalk(
        0xFE,
        (
            "听说那起袭击事件的\x01",
            "幕后黑手是帝国呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "绝对饶不了他们。\x01",
            "伊莉娅小姐就是因为那起事件才……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17A8")

    label("loc_A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABC")

    #C0010
    ChrTalk(
        0xFE,
        (
            "住在这间公寓\x01",
            "三楼的人原来\x01",
            "是伊莉娅小姐……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "看到修利\x01",
            "来收拾东西，\x01",
            "我才察觉到。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "……这原本是件值得高兴的事，\x01",
            "但伊莉娅小姐\x01",
            "却遭遇了那种事……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B0D")

    label("loc_ABC")


    #C0013
    ChrTalk(
        0xFE,
        (
            "修利一直是一副\x01",
            "无精打采的样子。\x01",
            "真可怜……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "唉，希望她能\x01",
            "尽快恢复精神。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0D")

    Jump("loc_17A8")

    label("loc_B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCA")

    #C0015
    ChrTalk(
        0xFE,
        (
            "『金之太阳、银之月』的\x01",
            "新版……\x01",
            "终于要在今晚公演了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "遗憾的是，\x01",
            "我没能买到票……\x01",
            "但我会在这里给他们加油的。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "唉，真想亲眼目睹\x01",
            "修利的英姿啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C2B")

    label("loc_BCA")


    #C0018
    ChrTalk(
        0xFE,
        (
            "『金之太阳、银之月』的\x01",
            "新版……\x01",
            "终于要在今晚公演了。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "唉，真想亲眼目睹\x01",
            "修利的英姿啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2B")

    Jump("loc_17A8")

    label("loc_C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_E79")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD0")

    #C0020
    ChrTalk(
        0xFE,
        (
            "修利今天一大早\x01",
            "就出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "她最近的情绪\x01",
            "好像很紧张……\x01",
            "让我有些担心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "新版舞剧的公演\x01",
            "让她很有压力吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D15")

    label("loc_CD0")


    #C0023
    ChrTalk(
        0xFE,
        (
            "新版舞剧的\x01",
            "公演让修利\x01",
            "很有压力吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "我一定要\x01",
            "全力支持她。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D15")

    Jump("loc_E74")

    label("loc_D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E05")

    #C0025
    ChrTalk(
        0xFE,
        (
            "刚、刚才……\x01",
            "伊莉娅小姐从修利的\x01",
            "房间里出来了！\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "她、她还和我打了招呼……\x01",
            "我高兴得都快哭出来了！\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐是来\x01",
            "找修利玩的吧？\x01",
            "呼，真羡慕修利啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00006F（不，那本来就是\x01",
            "  伊莉娅小姐的房间啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E74")

    label("loc_E05")


    #C0029
    ChrTalk(
        0xFE,
        (
            "真羡慕修利啊……\x01",
            "伊莉娅小姐竟然会来找她玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "呼，算了……\x01",
            "能够近距离见到伊莉娅小姐，\x01",
            "已经非常幸运了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E74")

    Jump("loc_17A8")

    label("loc_E79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_EDD")

    #C0031
    ChrTalk(
        0xFE,
        (
            "卢威克先生那里的\x01",
            "扫除已经做完了……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "嗯，接下来是三楼了。\x01",
            "大概又会很乱吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17A8")

    label("loc_EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_FF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6E")

    #C0033
    ChrTalk(
        0xFE,
        (
            "卢威克先生\x01",
            "好像带着夫人\x01",
            "去兜风了。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "听说要把车开到\x01",
            "边境大门附近去。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "真是悠闲自在的老年生活啊。\x01",
            "好羡慕～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FEC")

    label("loc_F6E")


    #C0036
    ChrTalk(
        0xFE,
        (
            "咦，说起来……\x01",
            "我记得卢威克先生之前好像和\x01",
            "他的夫人吵过架……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "……呼，不管了。\x01",
            "总之，得赶快把委托我的\x01",
            "扫除工作做完。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FEC")

    Jump("loc_17A8")

    label("loc_FF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_10D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1084")

    #C0038
    ChrTalk(
        0xFE,
        (
            "在彩虹剧团这次的\x01",
            "新版舞剧中……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "住在三楼的修利\x01",
            "被破格提拔为\x01",
            "次要主角之一了！\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "呀，好厉害啊！\x01",
            "真想去看！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10D2")

    label("loc_1084")


    #C0041
    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "好想去看修利的\x01",
            "重要演出……！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "……但是我没有\x01",
            "买到票。\x01",
            "唉……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D2")

    Jump("loc_17A8")

    label("loc_10D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_11E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1177")

    #C0043
    ChrTalk(
        0xFE,
        (
            "卢威克先生好像\x01",
            "和他的夫人吵架了。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "我去收钱的时候，\x01",
            "气氛非常压抑……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "唉，我虽然不是当事人，\x01",
            "但也不由自主得紧张起来了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11DB")

    label("loc_1177")


    #C0046
    ChrTalk(
        0xFE,
        (
            "卢威克先生和奥丽加夫人\x01",
            "好像正在吵架呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "唉，真希望他们早点和好，\x01",
            "这样会让我也很紧张的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11DB")

    Jump("loc_17A8")

    label("loc_11E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_12A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1270")

    #C0048
    ChrTalk(
        0xFE,
        (
            "听说各国首脑\x01",
            "今天将会去观看\x01",
            "彩虹剧团的演出。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "唔，他们肯定是坐在\x01",
            "很棒的位置享受演出吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        "唔～真羡慕啊！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12A3")

    label("loc_1270")


    #C0051
    ChrTalk(
        0xFE,
        (
            "我最后也没有买到\x01",
            "新版舞剧的门票。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "唉……\x02",
    )

    CloseMessageWindow()

    label("loc_12A3")

    Jump("loc_17A8")

    label("loc_12A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1394")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132A")

    #C0053
    ChrTalk(
        0xFE,
        (
            "喂，你听说了吗？\x01",
            "据说那部『金之太阳、银之月』\x01",
            "要推出新版呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "唔～真期待啊。\x01",
            "我得赶快去买票！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_138F")

    label("loc_132A")


    #C0055
    ChrTalk(
        0xFE,
        (
            "听说彩虹剧团的\x01",
            "『金之太阳、银之月』\x01",
            "要推出新版呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "这可绝对不能错过啊……\x01",
            "我得赶快去买票！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_138F")

    Jump("loc_17A8")

    label("loc_1394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_14C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1467")

    #C0057
    ChrTalk(
        0xFE,
        (
            "住在一楼的卢威克先生\x01",
            "向我提出想要改造\x01",
            "公寓。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "还说钱全都\x01",
            "由他来出，\x01",
            "最后被他的夫人制止了。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "哎呀，吓了我一跳呢。\x01",
            "话说回来，我只是公寓的管理员，\x01",
            "这种事情和我说也没用啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14C4")

    label("loc_1467")


    #C0060
    ChrTalk(
        0xFE,
        (
            "卢威克先生以前是议员，\x01",
            "非常富有呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "但即使如此，\x01",
            "一般人也不会有\x01",
            "改造公寓的想法吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C4")

    Jump("loc_17A8")

    label("loc_14C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_16C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_163A")

    #C0062
    ChrTalk(
        0xFE,
        (
            "因为时机的问题，\x01",
            "我之前一直遇不到\x01",
            "住在三楼的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "但今天早上终于遇到了，\x01",
            "还打了招呼。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "住在那里的是个叫\x01",
            "修利的女孩子，\x01",
            "她正在彩虹剧团见习呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "呵呵，虽然现在还默默无闻，\x01",
            "但今后可要多关注她了。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#00005F（修利好像\x01",
            "  借住在伊莉娅\x01",
            "  小姐的房间吧……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        (
            "#00100F（她好像一直都没发现\x01",
            "  住在三楼的人\x01",
            "  是伊莉娅小姐呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16BE")

    label("loc_163A")


    #C0068
    ChrTalk(
        0xFE,
        (
            "话说回来，彩虹剧团\x01",
            "果然薪酬丰厚啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "连见习的孩子都能\x01",
            "租住这么大的公寓。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00006F（那其实是伊莉娅\x01",
            "  小姐的房间啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16BE")

    Jump("loc_17A8")

    label("loc_16C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_17A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1767")

    #C0071
    ChrTalk(
        0xFE,
        (
            "我是这所\x01",
            "公寓的\x01",
            "管理员……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "这里真是\x01",
            "又宽敞又漂亮。\x01",
            "我也好想住在这样的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "……但实在是太过宽敞了，\x01",
            "扫除时有点辛苦呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17A8")

    label("loc_1767")


    #C0074
    ChrTalk(
        0xFE,
        (
            "唔，接下来，\x01",
            "还得打扫中庭……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        "呼，当管理员也不容易啊。\x02",
    )

    CloseMessageWindow()

    label("loc_17A8")

    TalkEnd(0xFE)
    Return()

    # Function_5_7DC end

    def Function_6_17AC(): pass

    label("Function_6_17AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_18E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187C")

    #C0076
    ChrTalk(
        0xFE,
        (
            "听说总统在兰花塔的内部\x01",
            "建造了古怪的设施。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "兰花塔的外观是由我负责设计的，\x01",
            "但他竟然在里面动手脚，\x01",
            "而且还用来作恶……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "我们全都被他欺骗了。\x01",
            "哎呀呀，实在是不可饶恕啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18E0")

    label("loc_187C")


    #C0079
    ChrTalk(
        0xFE,
        (
            "听说总统在兰花塔的内部\x01",
            "建造了古怪的设施。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "我们全都被他欺骗了。\x01",
            "哎呀呀，实在是不可饶恕啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E0")

    Jump("loc_264F")

    label("loc_18E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_19AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1981")

    #C0081
    ChrTalk(
        0xFE,
        (
            "可、可恶的总统……\x01",
            "没想到他居然这么过分！\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "虽然我很感谢他将\x01",
            "兰花塔的外观设计\x01",
            "工作交给我……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        "但已经不能再相信他了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19AA")

    label("loc_1981")


    #C0084
    ChrTalk(
        0xFE,
        (
            "可恶的总统……\x01",
            "已经不能再相信他了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19AA")

    Jump("loc_264F")

    label("loc_19AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1A20")

    #C0085
    ChrTalk(
        0xFE,
        (
            "在如今这种状况下，\x01",
            "我也无法接受帝国和\x01",
            "共和国的工作了……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "唔，至少要把\x01",
            "手头的工作完成……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_264F")

    label("loc_1A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AFD")

    #C0087
    ChrTalk(
        0xFE,
        (
            "多亏亚里欧斯先生，\x01",
            "兰花塔才能\x01",
            "幸免于难……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "但ＩＢＣ大楼真让人痛惜啊。\x01",
            "那也是克洛斯贝尔的\x01",
            "象征之一，如今却……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "那些袭击犯的行为就相当于\x01",
            "侮辱克洛斯贝尔的历史。\x01",
            "绝不能饶恕他们……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B60")

    label("loc_1AFD")


    #C0090
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ大楼是克洛斯贝尔的\x01",
            "标志性建筑物，如今却被他们……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        "可恶的袭击犯，真是不可饶恕……！\x02",
    )

    CloseMessageWindow()

    label("loc_1B60")

    Jump("loc_264F")

    label("loc_1B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1D62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D0F")

    #C0092
    ChrTalk(
        0xFE,
        (
            "………………………………\x01",
            "…………………………啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C40")
    Jump("loc_1C8A")

    label("loc_1C40")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C60")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C8A")

    label("loc_1C60")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C80")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C8A")

    label("loc_1C80")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C8A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0093
    ChrTalk(
        0xFE,
        "……有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "我正在集中精神画设计图呢，\x01",
            "不好意思，请不要打扰我。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D5D")

    label("loc_1D0F")


    #C0095
    ChrTalk(
        0xFE,
        (
            "最近我可以集中精神\x01",
            "投入工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "但缺点就是几乎\x01",
            "察觉不到周围的情况。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D5D")

    Jump("loc_264F")

    label("loc_1D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1DB9")

    #C0097
    ChrTalk(
        0xFE,
        (
            "雨声为何\x01",
            "能让人感到\x01",
            "如此惬意呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "似乎连画设计图\x01",
            "都更加顺畅了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_264F")

    label("loc_1DB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1E15")

    #C0099
    ChrTalk(
        0xFE,
        (
            "唔……\x01",
            "外面真吵闹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "而且还有警笛的声音……\x01",
            "难道发生了什么事故吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_264F")

    label("loc_1E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1EE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E9F")

    #C0101
    ChrTalk(
        0xFE,
        (
            "我的祖父是一位伟大的建筑家，\x01",
            "我与他之间的差距有没有缩短些呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        "……唔，不管怎么说，现在要专心工作。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EE1")

    label("loc_1E9F")


    #C0103
    ChrTalk(
        0xFE,
        (
            "对了，还有帝国客户\x01",
            "委托我画的设计图……\x01",
            "就从这项工作开始吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EE1")

    Jump("loc_264F")

    label("loc_1EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1F58")

    #C0104
    ChrTalk(
        0xFE,
        (
            "自从兰花塔正式亮相之后，\x01",
            "我肩上的担子就卸下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "我今后要转换心情，\x01",
            "参与多种多样的工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_264F")

    label("loc_1F58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2097")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2027")

    #C0106
    ChrTalk(
        0xFE,
        (
            "我虽然参与了\x01",
            "兰花塔的外观设计工作，\x01",
            "但对导力网络方面的知识却没什么了解。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "所以内部设计工作就交给\x01",
            "市长推荐的其他建筑家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "呵呵，真是亲身体会到了\x01",
            "与别人合作的重要性。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2092")

    label("loc_2027")


    #C0109
    ChrTalk(
        0xFE,
        (
            "兰花塔内部的设计工作\x01",
            "由市长推荐的其他建筑家\x01",
            "负责完成。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "这次真是亲身体会到了\x01",
            "与别人合作的重要性。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2092")

    Jump("loc_264F")

    label("loc_2097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2211")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2182")

    #C0111
    ChrTalk(
        0xFE,
        (
            "兰花塔这种规模的建筑物\x01",
            "能以如此惊人的速度完工，\x01",
            "导力网络绝对功不可没。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "在工作过程中，\x01",
            "技术人员都是通过导力网络\x01",
            "来收发设计图等资料的。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "这使工作效率\x01",
            "有了明显提升……\x01",
            "科学技术的进步真令人赞叹啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_220C")

    label("loc_2182")


    #C0114
    ChrTalk(
        0xFE,
        (
            "在兰花塔的建设过程中，\x01",
            "技术人员都是通过导力网络\x01",
            "而收发设计图等资料的。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "我总算理解市长为何\x01",
            "要为了普及导力网络\x01",
            "而专门修改法律了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_220C")

    Jump("loc_264F")

    label("loc_2211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_221F")
    Jump("loc_264F")

    label("loc_221F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2316")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B4")

    #C0116
    ChrTalk(
        0xFE,
        (
            "由我负责设计外观的\x01",
            "『兰花塔』终于要在\x01",
            "明天初次亮相了。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "虽然都已经这么大年纪了，\x01",
            "但还是不由自主地紧张啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2311")

    label("loc_22B4")


    #C0118
    ChrTalk(
        0xFE,
        (
            "『兰花塔』终于要在\x01",
            "明天正式亮相了……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "揭幕式结束之后，\x01",
            "去和建设人员们\x01",
            "打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2311")

    Jump("loc_264F")

    label("loc_2316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_24E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244E")

    #C0120
    ChrTalk(
        0xFE,
        (
            "市政厅……\x01",
            "不，现在已经是市民会馆了。\x01",
            "那座建筑物是我祖父设计的。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "祖父是一位伟大的建筑家，\x01",
            "克洛斯贝尔过去的公共设施\x01",
            "几乎都是他设计的。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "我也是追随着祖父的脚步，\x01",
            "才会立志成为建筑家的……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "而如今，身为他孙子的我，\x01",
            "设计了新市政厅大楼的外观……\x01",
            "呵呵，人生真是耐人寻味啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24E4")

    label("loc_244E")


    #C0124
    ChrTalk(
        0xFE,
        (
            "我的祖父是一位伟大的建筑家，\x01",
            "现在的市民会馆\x01",
            "就是他设计的。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "而如今，身为他孙子的我，\x01",
            "设计了新市政厅大楼的外观……\x01",
            "呵呵，人生真是耐人寻味啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24E4")

    Jump("loc_264F")

    label("loc_24E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_264F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25E9")

    #C0126
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的新市政厅大楼\x01",
            "终于落成了。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "多亏新市长大力支持\x01",
            "建设计划，\x01",
            "才能走到如今这一步。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "由于预算冻结等原因，建设工作\x01",
            "曾停滞不前，连能否完工都成了问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "如今彻底竣工，负责设计外观的我\x01",
            "总算也可以松一口气了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_264F")

    label("loc_25E9")


    #C0130
    ChrTalk(
        0xFE,
        (
            "我作为一名建筑家，\x01",
            "参与了新市政厅的外观设计。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "这项工作已经接近尾声……\x01",
            "真是令人感慨万千啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_264F")

    TalkEnd(0xFE)
    Return()

    # Function_6_17AC end

    def Function_7_2653(): pass

    label("Function_7_2653")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_27CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2747")

    #C0132
    ChrTalk(
        0xFE,
        (
            "我老公虽然对总统感到愤怒，\x01",
            "但还是着手于下一项工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "市里发生了那样的事情，\x01",
            "所以各公司纷纷前来委托\x01",
            "防盗、警备方面的改装工程……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "在这种时候，希望他专心做好现在的工作，\x01",
            "不要再对兰花塔的事情耿耿于怀。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27C7")

    label("loc_2747")


    #C0135
    ChrTalk(
        0xFE,
        (
            "各公司纷纷前来委托\x01",
            "防盗、警备方面的改装工程……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "在这种时候，希望他专心做好现在的工作，\x01",
            "不要再对兰花塔的事情耿耿于怀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27C7")

    Jump("loc_308F")

    label("loc_27CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_281B")

    #C0137
    ChrTalk(
        0xFE,
        (
            "虽然外面的怪物\x01",
            "似乎无意进入室内……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        "但还是很可怕啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_308F")

    label("loc_281B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2876")

    #C0139
    ChrTalk(
        0xFE,
        (
            "要冻结两大国资金的\x01",
            "宣言真是让我\x01",
            "大吃一惊。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "这、这么做\x01",
            "没关系吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308F")

    label("loc_2876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_297A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2923")

    #C0141
    ChrTalk(
        0xFE,
        (
            "城市竟然遭到暴徒的袭击，\x01",
            "真是可怕的事件啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "虽然这一带没有遭受\x01",
            "太大的损失，\x01",
            "但还是很担心今后的状况……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "希望不要再发生\x01",
            "这种事了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2975")

    label("loc_2923")


    #C0144
    ChrTalk(
        0xFE,
        (
            "城市竟然遭到暴徒的袭击，\x01",
            "真是可怕的事件啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "希望不要再发生\x01",
            "这种事了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2975")

    Jump("loc_308F")

    label("loc_297A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_29C8")

    #C0146
    ChrTalk(
        0xFE,
        (
            "最近这段时间\x01",
            "似乎事件不断。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "不久之前都还\x01",
            "很平静呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308F")

    label("loc_29C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2A95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A34")

    #C0148
    ChrTalk(
        0xFE,
        (
            "真讨厌啊……\x01",
            "我今天本打算\x01",
            "去百货商店购物。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "真没办法啊，\x01",
            "必须要打伞……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A90")

    label("loc_2A34")


    #C0150
    ChrTalk(
        0xFE,
        (
            "进口杂货店那里\x01",
            "有很好的咖啡豆。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "如果受了潮，会有损它的风味，\x01",
            "所以下雨会很麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A90")

    Jump("loc_308F")

    label("loc_2A95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2AD0")

    #C0152
    ChrTalk(
        0xFE,
        (
            "唔，我老公喜欢的\x01",
            "利贝尔产咖啡是放在……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308F")

    label("loc_2AD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2BF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B90")

    #C0153
    ChrTalk(
        0xFE,
        (
            "我老公以前一直活在\x01",
            "自己祖父的阴影下，\x01",
            "总是很自卑。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "不过，自从参与了兰花塔的\x01",
            "外观设计工作之后，\x01",
            "他好像就乐观积极多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "看来这份工作\x01",
            "让他找到了自信呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2BEE")

    label("loc_2B90")


    #C0156
    ChrTalk(
        0xFE,
        (
            "我老公已经\x01",
            "渐渐走出了\x01",
            "祖父的阴影。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "设计兰花塔外观的\x01",
            "这件工作好像\x01",
            "让他找到了自信呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BEE")

    Jump("loc_308F")

    label("loc_2BF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2C67")

    #C0158
    ChrTalk(
        0xFE,
        (
            "为了让老公更顺利的工作，\x01",
            "我来给他煮杯咖啡吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "今天煮的是利贝尔产的咖啡豆，\x01",
            "一定会很香醇的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308F")

    label("loc_2C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2CDD")

    #C0160
    ChrTalk(
        0xFE,
        (
            "今天早上，\x01",
            "又接到了不少\x01",
            "新工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "虽然兰花塔的工作\x01",
            "已经结束了，\x01",
            "但我老公还是没什么时间休息呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308F")

    label("loc_2CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2D70")

    #C0162
    ChrTalk(
        0xFE,
        (
            "我老公啊，即使我什么都没问，\x01",
            "他也会兴致勃勃地\x01",
            "给我讲很多兰花塔方面的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "呵呵，他白天参加揭幕式的\x01",
            "兴奋劲似乎还没消退呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308F")

    label("loc_2D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2DE7")

    #C0164
    ChrTalk(
        0xFE,
        (
            "我老公参与了\x01",
            "兰花塔的设计工作，\x01",
            "今天还出席了揭幕式。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "他现在大概正沉浸在\x01",
            "大功告成的喜悦感中吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308F")

    label("loc_2DE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E49")

    #C0166
    ChrTalk(
        0xFE,
        (
            "这次的工作格外重要，\x01",
            "我老公好像很紧张呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "给他煮杯咖啡，\x01",
            "让他定下心来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308F")

    label("loc_2E49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2F84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EF6")

    #C0168
    ChrTalk(
        0xFE,
        (
            "我经常听老公\x01",
            "讲他祖父的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "老公的祖父是一位非常优秀的\x01",
            "建筑家，也是他永远的目标。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "但在某种程度上，\x01",
            "似乎也让他产生了\x01",
            "些许自卑感。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F7F")

    label("loc_2EF6")


    #C0171
    ChrTalk(
        0xFE,
        (
            "我老公的祖父是一位\x01",
            "非常优秀的建筑家，\x01",
            "这似乎让他产生了一些自卑感。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "不过，我老公在工作上一直非常努力，\x01",
            "我觉得这样不就很好了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F7F")

    Jump("loc_308F")

    label("loc_2F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_308F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_303D")

    #C0173
    ChrTalk(
        0xFE,
        (
            "我老公参与了\x01",
            "新市政厅大楼的设计工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "这是一项重要的工作，\x01",
            "所以他这个月一直\x01",
            "都在集中精力拼命工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "不过，工作似乎已经告一段落了，\x01",
            "我也放心了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_308F")

    label("loc_303D")


    #C0176
    ChrTalk(
        0xFE,
        (
            "我们的家就是\x01",
            "设计事务所。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "最近一直都在忙着完成\x01",
            "新市政厅大楼的设计工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_308F")

    TalkEnd(0xFE)
    Return()

    # Function_7_2653 end

    def Function_8_3093(): pass

    label("Function_8_3093")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_30FC")

    #C0178
    ChrTalk(
        0xFE,
        (
            "这个世道真是\x01",
            "越来越不太平了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "要不要挖个地下避难所，\x01",
            "和老婆子一起藏起来呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3809")

    label("loc_30FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_315E")

    #C0180
    ChrTalk(
        0xFE,
        (
            "唔，不知我停在外面的车\x01",
            "会不会有事。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "要是划伤了的话，\x01",
            "我一定会去要求赔偿。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3809")

    label("loc_315E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_316C")
    Jump("loc_3809")

    label("loc_316C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_32DA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_320B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31A8")
    Call(0, 19)
    Return()

    label("loc_31A8")


    #C0182
    ChrTalk(
        0xFE,
        (
            "盖巴尔现在应该在\x01",
            "阿尔摩利卡村。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "你们过去找找，应该能找到，\x01",
            "具体情况就问他本人好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32D5")

    label("loc_320B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32A8")

    #C0184
    ChrTalk(
        0xFE,
        (
            "我在慈善活动的会场\x01",
            "把卖掉旧家具的钱\x01",
            "捐出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "比起我自己花掉，\x01",
            "这样应该\x01",
            "更有意义。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "现在大家都不容易，\x01",
            "我们必须互相帮助啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_32D5")

    label("loc_32A8")


    #C0187
    ChrTalk(
        0xFE,
        (
            "现在大家都不容易，\x01",
            "我们必须互相帮助啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32D5")

    Jump("loc_3809")

    label("loc_32DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_33E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3381")

    #C0188
    ChrTalk(
        0xFE,
        (
            "武装集团居然占领了矿山镇，\x01",
            "这真是前所未闻。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "如果我当时去玛因兹\x01",
            "那边兜风，\x01",
            "说不定就被牵连进去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "啊，真可怕。\x01",
            "（发抖）……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_33DC")

    label("loc_3381")


    #C0191
    ChrTalk(
        0xFE,
        (
            "如果我当时去玛因兹\x01",
            "那边兜风，\x01",
            "说不定就被牵连进去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "啊，真可怕。\x01",
            "（发抖）……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33DC")

    Jump("loc_3809")

    label("loc_33E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_344C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33FC")
    Call(0, 13)
    Jump("loc_3447")

    label("loc_33FC")


    #C0193
    ChrTalk(
        0xFE,
        (
            "（唔……阿鲁姆那孩子\x01",
            "  已经长这么大了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        "（但那个蠢材却……）\x02",
    )

    CloseMessageWindow()

    label("loc_3447")

    Jump("loc_3809")

    label("loc_344C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_345A")
    Jump("loc_3809")

    label("loc_345A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3468")
    Jump("loc_3809")

    label("loc_3468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_34CF")

    #C0195
    ChrTalk(
        0xFE,
        (
            "我明天打算开车\x01",
            "兜风，这次准备\x01",
            "邀请老婆子一起。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "希望这样能让\x01",
            "她的心情好一些……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3809")

    label("loc_34CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_35D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3576")

    #C0197
    ChrTalk(
        0xFE,
        (
            "我和老婆子从昨天\x01",
            "就开始闹别扭……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "唔唔，住在一起的两个人\x01",
            "持续这种冷战状态，\x01",
            "还真是不好受啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "唔，怎么才能\x01",
            "跟老婆子和好呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_35D0")

    label("loc_3576")


    #C0200
    ChrTalk(
        0xFE,
        (
            "怎么才能\x01",
            "跟老婆子和好呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "不然就买瓶高级葡萄酒……？\x01",
            "不行不行，这应该行不通。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35D0")

    Jump("loc_3809")

    label("loc_35D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3659")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35F0")
    Call(0, 9)
    Jump("loc_3654")

    label("loc_35F0")


    #C0202
    ChrTalk(
        0xFE,
        (
            "我难得想和老婆子一起喝酒，\x01",
            "特意买了瓶高级葡萄酒，可她却……\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "哼，算了，\x01",
            "我一个人喝就是了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3654")

    Jump("loc_3809")

    label("loc_3659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3667")
    Jump("loc_3809")

    label("loc_3667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_370D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36E5")

    #C0204
    ChrTalk(
        0xFE,
        (
            "我原本很想要个车库，\x01",
            "免得导力车\x01",
            "遭受风吹雨打……\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "但老婆子发了那么大的火，\x01",
            "也只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3708")

    label("loc_36E5")


    #C0206
    ChrTalk(
        0xFE,
        (
            "呼，但也用不着\x01",
            "那么生气吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3708")

    Jump("loc_3809")

    label("loc_370D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3800")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3795")

    #C0207
    ChrTalk(
        0xFE,
        (
            "唔，停在外面的导力车\x01",
            "会被雨淋湿的。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "我真想要\x01",
            "一个车库啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "呼，算了，明天好好\x01",
            "洗洗车就是了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_37FB")

    label("loc_3795")


    #C0210
    ChrTalk(
        0xFE,
        (
            "但把导力车一直\x01",
            "放在外面风吹日晒，\x01",
            "终究不是办法啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "住公寓就不能\x01",
            "建造车库，\x01",
            "真是让人受不了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37FB")

    Jump("loc_3809")

    label("loc_3800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3809")

    label("loc_3809")

    TalkEnd(0xFE)
    Return()

    # Function_8_3093 end

    def Function_9_380D(): pass

    label("Function_9_380D")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0212
    ChrTalk(
        0xB,
        (
            "啊，这瓶葡萄酒\x01",
            "果然很好喝，\x01",
            "真是买对了。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xB,
        (
            "老婆子既然不想喝，\x01",
            "我就一个人喝掉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xC,
        "……嗯，随你高兴吧。\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xC,
        (
            "反正你就是为了自己享受\x01",
            "才花了那么多钱的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xB,
        (
            "……哼！\x01",
            "（咕嘟咕嘟咕嘟咕嘟）。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_9_380D end

    def Function_10_38F7(): pass

    label("Function_10_38F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_397C")

    #C0217
    ChrTalk(
        0xFE,
        (
            "老头子可真是的，\x01",
            "我们哪有建造地下避难所的钱啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "他这个老毛病总是改不掉，\x01",
            "遇到什么问题都想通过花钱来解决。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40D8")

    label("loc_397C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_39B7")

    #C0219
    ChrTalk(
        0xFE,
        (
            "真是的，老头子在\x01",
            "这种时候还在担心车……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40D8")

    label("loc_39B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3A3E")

    #C0220
    ChrTalk(
        0xFE,
        (
            "我听了演讲……\x01",
            "看来帝国和共和国一直在\x01",
            "克洛斯贝尔进行暗斗啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "身为克洛斯贝尔的居民，\x01",
            "无论如何也无法原谅他们……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40D8")

    label("loc_3A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3AC3")

    #C0222
    ChrTalk(
        0xFE,
        (
            "为了城市的复兴，\x01",
            "我家老头子去捐了款。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "我原以为他是个挥霍成性的人，\x01",
            "只会为自己而花钱，\x01",
            "这下可对他有些改观了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40D8")

    label("loc_3AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3B15")

    #C0224
    ChrTalk(
        0xFE,
        (
            "没想到会发生\x01",
            "这么严重的事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "希望警备队\x01",
            "能够设法解决。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40D8")

    label("loc_3B15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3B75")

    #C0226
    ChrTalk(
        0xFE,
        (
            "阿鲁姆带着家人\x01",
            "来克洛斯贝尔了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "呵呵，他好像过得\x01",
            "很幸福，真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40D8")

    label("loc_3B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3B83")
    Jump("loc_40D8")

    label("loc_3B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3B91")
    Jump("loc_40D8")

    label("loc_3B91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3C09")

    #C0228
    ChrTalk(
        0xFE,
        (
            "不知道吹的\x01",
            "什么风……\x01",
            "老头子竟然邀请我去兜风。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "真是的……\x01",
            "他难道以为这样\x01",
            "就能让我的心情转好吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40D8")

    label("loc_3C09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3C6E")

    #C0230
    ChrTalk(
        0xFE,
        (
            "我决定一段\x01",
            "时间之内不和\x01",
            "老头子说话了。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "除非他向我道歉，\x01",
            "不然我才不会原谅他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40D8")

    label("loc_3C6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3CB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C89")
    Call(0, 9)
    Jump("loc_3CB0")

    label("loc_3C89")


    #C0232
    ChrTalk(
        0xFE,
        (
            "……哼，我才懒得管\x01",
            "那个老头子呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CB0")

    Jump("loc_40D8")

    label("loc_3CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3D87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D3E")

    #C0233
    ChrTalk(
        0xFE,
        (
            "老头子瞒着我，\x01",
            "买了陈年高级\x01",
            "葡萄酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "上次因为车库的事情，\x01",
            "我刚发过那么大的火……\x01",
            "他完全没有反省呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3D82")

    label("loc_3D3E")


    #C0235
    ChrTalk(
        0xFE,
        (
            "老头子可真是的……\x01",
            "他难道以为这种挥霍式的\x01",
            "消费可以让我开心吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D82")

    Jump("loc_40D8")

    label("loc_3D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3EB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E46")

    #C0236
    ChrTalk(
        0xFE,
        (
            "老头子可真是的，竟然想在\x01",
            "公寓内部建造车库。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "虽然我总算说服了他，\x01",
            "但萨米小姐真是\x01",
            "被他惊得目瞪口呆呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "唉，他那浪费的坏习惯\x01",
            "已经到了无可救药的程度了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3EAC")

    label("loc_3E46")


    #C0239
    ChrTalk(
        0xFE,
        (
            "老头子可真是的，竟然想在\x01",
            "公寓内部建造车库。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "唉，他那浪费的坏习惯\x01",
            "已经到了无可救药的程度了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EAC")

    Jump("loc_40D8")

    label("loc_3EB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3FD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F6A")

    #C0241
    ChrTalk(
        0xFE,
        (
            "在这种下雨的日子，\x01",
            "就要专心做自己喜欢做的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "顺便一说，我的兴趣是手工，\x01",
            "最近尤其喜欢\x01",
            "拼缀布艺。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "（缝个不停）……\x01",
            "这门手艺相当深奥，很有趣呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3FD0")

    label("loc_3F6A")


    #C0244
    ChrTalk(
        0xFE,
        (
            "我的兴趣是手工，\x01",
            "最近尤其喜欢\x01",
            "拼缀布艺。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "老头子要是也像我这样，\x01",
            "找些不会\x01",
            "花钱的兴趣就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FD0")

    Jump("loc_40D8")

    label("loc_3FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_40D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_407E")

    #C0246
    ChrTalk(
        0xFE,
        "老头子挥霍成性，真让人头疼啊。\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "家具明明还没必要更换，\x01",
            "他就非要买新的，\x01",
            "一直都是如此……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "不久前，\x01",
            "他还买了导力车呢。\x01",
            "真是的……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_40D8")

    label("loc_407E")


    #C0249
    ChrTalk(
        0xFE,
        (
            "都不跟我说一声，\x01",
            "就擅自买了导力车……\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "老头子那挥霍成性的坏习惯\x01",
            "真是让人头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40D8")

    TalkEnd(0xFE)
    Return()

    # Function_10_38F7 end

    def Function_11_40DC(): pass

    label("Function_11_40DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40F1")
    Call(0, 13)
    Jump("loc_410C")

    label("loc_40F1")


    #C0251
    ChrTalk(
        0xFE,
        (
            "好～今天就去\x01",
            "医院吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_410C")

    TalkEnd(0xFE)
    Return()

    # Function_11_40DC end

    def Function_12_4110(): pass

    label("Function_12_4110")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4125")
    Call(0, 13)
    Jump("loc_415C")

    label("loc_4125")


    #C0252
    ChrTalk(
        0xFE,
        (
            "呵呵，虽然进展不快，\x01",
            "但我们确实在一步步接近他呢⊥\x02",
        )
    )

    CloseMessageWindow()

    label("loc_415C")

    TalkEnd(0xFE)
    Return()

    # Function_12_4110 end

    def Function_13_4160(): pass

    label("Function_13_4160")

    OP_4B(0xB, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0253
    ChrTalk(
        0xF,
        (
            "原来如此，他在几个月之前\x01",
            "就离开了乌尔斯拉医院……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xB,
        (
            "是的，我也不清楚\x01",
            "他之后的去向……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xB,
        (
            "你们专程前来，\x01",
            "我却只能告诉你们这些，\x01",
            "真是不好意思啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x10,
        (
            "不，哪里的话，\x01",
            "这对我们很有帮助。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)

    #C0257
    ChrTalk(
        0x10,
        "对吧？亲爱的⊥\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 500)

    #C0258
    ChrTalk(
        0xF,
        (
            "是啊，艾娅莉。\x01",
            "这是我们一家三口的大胜利！\x02",
        )
    )

    CloseMessageWindow()

    #N0259
    NpcTalk(
        0x10,
        "婴儿",
        "呀呀¤\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)

    #C0260
    ChrTalk(
        0xB,
        (
            "哈哈，你们真是\x01",
            "很亲密啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_93(0xF, 0x87, 0x0)
    OP_93(0x10, 0xB4, 0x0)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_13_4160 end

    def Function_14_430E(): pass

    label("Function_14_430E")

    TalkBegin(0xFE)

    #C0261
    ChrTalk(
        0xFE,
        (
            "完、完全没想到\x01",
            "会发生这种事。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "总、总之……\x01",
            "要尽量多拍些照片，\x01",
            "记录下现在的情况。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_430E end

    def Function_15_4370(): pass

    label("Function_15_4370")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4385")
    Call(0, 17)
    Jump("loc_449B")

    label("loc_4385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_446E")
    OP_4B(0xD, 0xFF)

    #C0263
    ChrTalk(
        0xE,
        (
            "#04206F呼……呼……\x02\x03",

            "#04201F我说，伊莉娅小姐，\x01",
            "已经够了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xD,
        (
            "#01703F嗯～你好像还是有些紧张，\x01",
            "再多给你按摩一会吧。\x02\x03",

            "#01702F总之，你就安静一些，\x01",
            "乖乖听我的话吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xE,
        (
            "#04206F呜呜……\x01",
            "到底还要多久啊？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xD, 0xFF)
    Jump("loc_449B")

    label("loc_446E")


    #C0266
    ChrTalk(
        0xE,
        (
            "#04206F呜呜……\x01",
            "怎样都好，\x01",
            "赶快结束吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_449B")

    TalkEnd(0xFE)
    Return()

    # Function_15_4370 end

    def Function_16_449F(): pass

    label("Function_16_449F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44B4")
    Call(0, 17)
    Jump("loc_462D")

    label("loc_44B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4598")

    #C0267
    ChrTalk(
        0xD,
        (
            "#01700F呵呵，警察弟弟，\x01",
            "不然我也给你们按摩一下吧～\x02\x03",

            "#01709F不过，我的原则\x01",
            "还是女性优先⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x102,
        "#00102F啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x109,
        "#10106F还、还是不用了。\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xE,
        (
            "#04206F（唉，还没喝酒就这样，\x01",
            "  真是让人没办法啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_462D")

    label("loc_4598")


    #C0271
    ChrTalk(
        0xD,
        (
            "#01700F为了晚上的公演，必须让\x01",
            "修利的身体彻底放松下来。\x02\x03",

            "#01709F这就叫有备无患……\x01",
            "女孩子就应该接受我的按摩哦⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xE,
        "#04206F（莫、莫名其妙……）\x02",
    )

    CloseMessageWindow()

    label("loc_462D")

    TalkEnd(0xFE)
    Return()

    # Function_16_449F end

    def Function_17_4631(): pass

    label("Function_17_4631")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch51814.itc", 0x1E)
    OP_68(51500, 2300, 59170, 0)
    MoveCamera(58, 18, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19700, 0)
    SetChrPos(0x101, 51430, 1050, 58470, 45)
    SetChrPos(0x102, 50280, 1050, 58640, 45)
    SetChrPos(0x104, 51460, 1000, 57280, 45)
    SetChrPos(0x109, 49800, 1050, 57410, 45)
    SetChrPos(0x105, 50350, 1000, 56530, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xD, 0xFF)
    TurnDirection(0xD, 0x101, 0)
    SetChrSubChip(0xE, 0x1)
    FadeToBright(1000, 0)
    OP_0D()

    #C0273
    ChrTalk(
        0xD,
        "#11P#01709F啊，警察弟弟☆\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xE,
        (
            "#04205F#5P你、你们好……\x02\x03",

            "#04206F……疼疼疼！\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x101,
        "#12P#00005F您、您在做什么？\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xD,
        (
            "#11P#01704F呵呵，今天晚上，\x01",
            "各国首脑会到\x01",
            "彩虹剧团观看演出……\x02\x03",

            "#01702F修利也要在演出中\x01",
            "担任配角呢。\x02\x03",

            "#01709F现在是按摩时间，\x01",
            "目的是让她的身体更加柔韧……嘿！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(50)
    SetChrSubChip(0xE, 0x0)

    def lambda_4813():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_4813)
    WaitChrThread(0xE, 2)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0277
    ChrTalk(
        0xE,
        "#04212F#11P#4S好疼啊！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0278
    ChrTalk(
        0x102,
        "#6P#00102F原、原来如此……\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x109,
        (
            "#6P#10105F那、那个，真的没问题吗？\x02\x03",

            "#10106F听说外行人按摩肌肉，\x01",
            "也许会起到反效果的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 500)

    #C0280
    ChrTalk(
        0xD,
        (
            "#11P#01704F呵呵，不用担心。\x02\x03",

            "#01702F我以前向专业按摩师\x01",
            "认真学习过，\x01",
            "现在已经非常精通了呢。\x02\x03",

            "在练习间隙，舒展身体的时候，\x01",
            "我也经常给莉夏按摩呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x105,
        (
            "#12P#10302F原来如此，为了舞台表演，\x01",
            "无论哪个领域的知识\x01",
            "都要吸收并化为己用啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x104,
        "#12P#00309F哎呀～真不愧是伊莉娅小姐！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x1)
    Sleep(100)

    #C0283
    ChrTalk(
        0xE,
        (
            "#04206F#5P可、可是……\x01",
            "不管怎么说，也还是很疼啊！！\x02\x03",

            "#04201F伊、伊莉娅小姐，\x01",
            "真的不要紧吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xD,
        (
            "#11P#01706F我不是说过好几次了嘛，\x01",
            "肯定不会有事的。\x02\x03",

            "#01700F你之所以会这么疼，是因为今天晚上的表演\x01",
            "让你很紧张，所以身体非常僵硬。\x02\x03",

            "#01709F放心好啦，只要继续下去，\x01",
            "就会渐渐舒服起来啦⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xE,
        "#04207F#5P别、别说那种会引起误会的话！\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xD,
        (
            "#11P#01701F真是的，你太啰嗦了。\x01",
            "如果不老实待着……就会这样！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x2)
    SetChrFlags(0xD, 0x2)
    SetChrPos(0xD, 53710, 1200, 60530, 270)
    OP_A6(0xD, 0x0, 0x14, 0x190, 0x1388)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x2)
    OP_63(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_82(0x1F4, 0x0, 0xBB8, 0x3E8)

    #C0287
    ChrTalk(
        0xE,
        "#5P#04212F#5S哇哇哇哇哇！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0288
    ChrTalk(
        0xE,
        "#5P#04207F你、你你你……你在摸哪里啊！？\x02",
    )

    CloseMessageWindow()
    OP_64(0xE)
    SetChrSubChip(0xE, 0x1)

    #C0289
    ChrTalk(
        0xD,
        (
            "#11P#01709F呵呵呵，放心吧，\x01",
            "这也是效果很好的按摩方法。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xE,
        (
            "#04207F#5P骗、骗人！！\x02\x03",

            "#04209F啊哈哈，好、好痒……\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xD,
        (
            "#11P#01709F嗯嗯，身体还在发育呢⊥\x01",
            "你将来也许会很有前途哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xE,
        "#04212F#5P谁、谁关心那些！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0293
    ChrTalk(
        0x102,
        (
            "#6P#00113F这、这种情景\x01",
            "实在是有点……\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x105,
        "#12P#10309F呵呵，不是很有情趣嘛。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x101,
        (
            "#12P#00012F哈哈，不管怎么说，\x01",
            "修利好像已经完全\x01",
            "融入彩虹剧团了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)

    #C0296
    ChrTalk(
        0xE,
        (
            "#5P#04207F不、不用做那种总结性发言，\x01",
            "快来救救我啊！！\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xD,
        "#11P#01709F喂喂，别想逃跑～\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0xD, 0x8)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x2)
    SetChrPos(0xD, 54020, 1020, 60490, 270)
    SetChrChipByIndex(0xE, 0x9)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x2)
    OP_4C(0xD, 0xFF)
    OP_93(0xD, 0x10E, 0x0)
    SetChrPos(0x0, 50040, 1050, 57020, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x14C, 5)
    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_17_4631 end

    def Function_18_4F89(): pass

    label("Function_18_4F89")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5255")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_512F")
    SetChrName("")

    #A0298
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从门内传来了\x01",
            "伊莉娅和修利的\x01",
            "嬉闹声。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(130, 20, -1, -1)
    SetChrName("修利的声音")

    #A0299
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊、啊哈哈哈……\x01",
            "都说过不是那里了啊！\x02\x03",

            "呼……呼……\x01",
            "伊莉娅小姐，\x01",
            "你根本就是故意的吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("伊莉娅的声音")

    #A0300
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "没有啦，只是你的错觉⊥\x02",
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

    #C0301
    ChrTalk(
        0x101,
        "#00012F伊莉娅小姐好像相当乐在其中呢。\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x102,
        "#00106F修利……真可怜。\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetScenarioFlags(0x0, 7)
    Jump("loc_5250")

    label("loc_512F")

    SetChrName("")

    #A0303
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从门内传来了\x01",
            "伊莉娅和修利的\x01",
            "嬉闹声。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(130, 20, -1, -1)
    SetChrName("修利的声音")

    #A0304
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呼……呼……\x01",
            "到底还要多久啊？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(130, 20, -1, -1)
    SetChrName("伊莉娅的声音")

    #A0305
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个嘛……如果你\x01",
            "能老实点，\x01",
            "说不定可以早点结束哦⊥\x02",
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

    label("loc_5250")

    Jump("loc_5272")

    label("loc_5255")

    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0306
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上了锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5272")

    TalkEnd(0xFF)
    Return()

    # Function_18_4F89 end

    def Function_19_5276(): pass

    label("Function_19_5276")

    EventBegin(0x0)
    Fade(500)
    OP_68(-42750, 2270, 60900, 0)
    MoveCamera(58, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23950, 0)
    SetChrPos(0xB, -40610, 1030, 60630, 270)
    SetChrPos(0x101, -42710, 1020, 61350, 90)
    SetChrPos(0x102, -42900, 1020, 60110, 90)
    SetChrPos(0x103, -44070, 1020, 61440, 90)
    SetChrPos(0x104, -44470, 1020, 60240, 90)
    SetChrPos(0x109, -45710, 1020, 61170, 90)
    SetChrPos(0x105, -45790, 1020, 59690, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xB, 0xFF)
    OP_0D()

    #C0307
    ChrTalk(
        0xB,
        (
            "#2P哎呀，你们……\x01",
            "找我有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x101,
        (
            "#00004F突然拜访，\x01",
            "真是不好意思……\x02\x03",

            "#00000F请问您对盖巴尔\x01",
            "这个名字有印象吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0309
    ChrTalk(
        0xB,
        "#2P嗯？你们认识盖巴尔吗？\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xB,
        (
            "#2P在他担当议员的时候，\x01",
            "我曾经照顾过他……\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x105,
        "#10300F呵呵，似乎找对地方了。\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x102,
        "#00100F其实是这样……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0313
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人向对方解释了\x01",
            "盖巴尔的儿子儿媳正在找他的情况。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0314
    ChrTalk(
        0xB,
        (
            "#2P嗯，原来如此，\x01",
            "你们是受他们所托……\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xB,
        (
            "#2P其实……在不久之前，\x01",
            "盖巴尔曾来找过我，\x01",
            "希望我帮他『在克洛斯贝尔隐居生活』。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xB,
        (
            "#2P哎呀呀，真是个蠢材……\x01",
            "有那么好的儿子和儿媳，\x01",
            "为什么要逃跑呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x103,
        (
            "#00205F您果然知道\x01",
            "盖巴尔先生的行踪啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x104,
        (
            "#00305F不过，所谓的『隐居』\x01",
            "又是怎么回事呢？\x02\x03",

            "#00303F我们完全搞不懂理由……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x109,
        (
            "#10101F是、是啊！\x01",
            "阿鲁姆先生一家特意\x01",
            "过来见他……\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xB,
        (
            "#2P唔，在外人看来，\x01",
            "这个原因或许很无聊……\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xB,
        (
            "#2P……不，这件事情\x01",
            "不应该由我来说。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0322
    ChrTalk(
        0xB,
        (
            "#2P……那家伙现在应该在\x01",
            "阿尔摩利卡村。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xB,
        (
            "#2P你们过去找找，应该能找到，\x01",
            "具体情况就问他本人好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x101,
        (
            "#00003F明白了……\x01",
            "非常感谢。\x02\x03",

            "#00000F我们这就去\x01",
            "阿尔摩利卡村吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x102,
        "#00100F嗯，出发吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x90, 0x1, 0x2)
    SetScenarioFlags(0x19B, 0)
    OP_4C(0xB, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -49950, 1000, 56930, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_19_5276 end

    SaveToFile()

Try(main)
