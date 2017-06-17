from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "サミィ",                 # 1
        "キンドール",             # 2
        "ブリジッタ",             # 3
        "ルーヴィック老人",       # 4
        "オリガ夫人",             # 5
        "イリア",                 # 6
        "シュリ",                 # 7
        "アルム",                 # 8
        "エアリー",               # 9
        "ポンス",                 # 10
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
        "Function_6_1C12",         # 06, 6
        "Function_7_2D43",         # 07, 7
        "Function_8_39FF",         # 08, 8
        "Function_9_4383",         # 09, 9
        "Function_10_44A1",        # 0A, 10
        "Function_11_4E4C",        # 0B, 11
        "Function_12_4E9A",        # 0C, 12
        "Function_13_4EE8",        # 0D, 13
        "Function_14_50E2",        # 0E, 14
        "Function_15_5168",        # 0F, 15
        "Function_16_52D9",        # 10, 16
        "Function_17_54BD",        # 11, 17
        "Function_18_5F63",        # 12, 18
        "Function_19_62CE",        # 13, 19
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_985")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E7")

    #C0001
    ChrTalk(
        0xFE,
        (
            "湿地帯にあんなものが現れて……\x01",
            "不安だけど、仕事はちゃんと\x01",
            "やっておかないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "シュリちゃんだって、\x01",
            "ずっとアルカンシェルで\x01",
            "練習をがんばってるみたいだし！\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "イリア様が戻ってきた時のためにも\x01",
            "しっかりアパートを綺麗にしなきゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_980")

    label("loc_8E7")


    #C0004
    ChrTalk(
        0xFE,
        (
            "シュリちゃんだって、\x01",
            "ずっとアルカンシェルで\x01",
            "練習をがんばってるみたいだし！\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "イリア様が戻ってきた時のためにも\x01",
            "しっかりアパートを綺麗にしなきゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_980")

    Jump("loc_1C0E")

    label("loc_985")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_A11")

    #C0006
    ChrTalk(
        0xFE,
        (
            "ああっ、どうしよう……\x01",
            "街でこんな事が起こるなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "と、とにかく、部屋にいる皆さんに\x01",
            "外に出ないよう呼びかけないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C0E")

    label("loc_A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A7F")

    #C0008
    ChrTalk(
        0xFE,
        (
            "あの襲撃事件……\x01",
            "黒幕は帝国だったそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "絶対に許せないわ。\x01",
            "あの事件でイリア様は……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C0E")

    label("loc_A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B68")

    #C0010
    ChrTalk(
        0xFE,
        (
            "このマンションの\x01",
            "３階に住んでたのは、\x01",
            "イリア様だったのね……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "荷物を取りに来てた\x01",
            "シュリちゃんを見て、\x01",
            "ようやく気づいたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "……本当なら嬉しいのに、\x01",
            "イリア様があんなことに\x01",
            "なっちゃうなんて……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BE3")

    label("loc_B68")


    #C0013
    ChrTalk(
        0xFE,
        (
            "シュリちゃん、\x01",
            "ずっと生気がない顔をしているの。\x01",
            "かわいそうに……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "はあ、何とか元気を\x01",
            "取り戻してくれるといいけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE3")

    Jump("loc_1C0E")

    label("loc_BE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC2")

    #C0015
    ChrTalk(
        0xFE,
        (
            "《金の太陽、銀の月》の\x01",
            "リニューアル公演……\x01",
            "いよいよ今夜なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "残念ながらチケットは\x01",
            "買えなかったけど……\x01",
            "私はここで応援するわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "はあ、シュリちゃんの勇姿、\x01",
            "見たかったなあ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D3B")

    label("loc_CC2")


    #C0018
    ChrTalk(
        0xFE,
        (
            "《金の太陽、銀の月》の\x01",
            "リニューアル公演……\x01",
            "いよいよ今夜なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "はあ、シュリちゃんの勇姿、\x01",
            "見たかったなあ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3B")

    Jump("loc_1C0E")

    label("loc_D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_104F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E18")

    #C0020
    ChrTalk(
        0xFE,
        (
            "今朝早くシュリちゃんが\x01",
            "出かけていったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "最近なんだか\x01",
            "気が張ってるみたいだし……\x01",
            "ちょっと心配なのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "やっぱりリニューアル公演が\x01",
            "プレッシャーなのかしら……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E8D")

    label("loc_E18")


    #C0023
    ChrTalk(
        0xFE,
        (
            "シュリちゃん、\x01",
            "やっぱりリニューアル公演が\x01",
            "プレッシャーなのかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "私がしっかりと\x01",
            "応援してあげなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E8D")

    Jump("loc_104A")

    label("loc_E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FBF")

    #C0025
    ChrTalk(
        0xFE,
        (
            "さ、さっき……\x01",
            "３階のシュリちゃんの部屋から\x01",
            "イリア様が出て行ったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "あ、挨拶されちゃった……\x01",
            "うれしすぎて泣いちゃいそう！\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "イリア様、シュリちゃんの部屋に\x01",
            "遊びに来てたのかしらね。\x01",
            "はあ、うらやましい……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00006F（いや、本当はイリアさんの\x01",
            "  部屋なんだけどな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_104A")

    label("loc_FBF")


    #C0029
    ChrTalk(
        0xFE,
        (
            "はあ、イリア様が遊びにくるなんて、\x01",
            "シュリちゃんうらやましい……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "まあいっか……\x01",
            "イリア様を間近で見られて\x01",
            "すごいラッキーだったし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_104A")

    Jump("loc_1C0E")

    label("loc_104F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_10C7")

    #C0031
    ChrTalk(
        0xFE,
        (
            "ルーヴィックさんとこは\x01",
            "お掃除終わりっと……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "えっと、次は３階かしら。\x01",
            "また散らかってそうねえ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C0E")

    label("loc_10C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_121F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118C")

    #C0033
    ChrTalk(
        0xFE,
        (
            "ルーヴィックさん、\x01",
            "奥さんを連れてドライブに\x01",
            "行ってるみたいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "国境門あたりまで\x01",
            "車を走らせるって言ってたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "まさに悠々自適な老後よね。\x01",
            "うらやましいわ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_121A")

    label("loc_118C")


    #C0036
    ChrTalk(
        0xFE,
        (
            "あれ、そういえば……\x01",
            "ルーヴィックさんと奥さんって\x01",
            "夫婦喧嘩してた気が……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "……まあいっか。\x01",
            "とにかく、たのまれた\x01",
            "お掃除をしないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121A")

    Jump("loc_1C0E")

    label("loc_121F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_136D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12EC")

    #C0038
    ChrTalk(
        0xFE,
        (
            "今度のアルカンシェルの\x01",
            "リニューアル公演……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "３階に住んでるシュリちゃんが\x01",
            "準主人公の一人に大抜擢された\x01",
            "みたいなのよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "キャー、すごいわよね！\x01",
            "ほんと見てみたいわ！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1368")

    label("loc_12EC")


    #C0041
    ChrTalk(
        0xFE,
        (
            "ああっ……\x01",
            "シュリちゃんの晴れ舞台、\x01",
            "見てみたいっ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "……でも、チケットは\x01",
            "買い逃しちゃったのよね。\x01",
            "はあぁ～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1368")

    Jump("loc_1C0E")

    label("loc_136D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1494")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141D")

    #C0043
    ChrTalk(
        0xFE,
        (
            "ルーヴィックさんのお宅、\x01",
            "夫婦喧嘩中みたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "集金に行ったら\x01",
            "空気が重くて重くて……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "はあ、当事者でもないのに\x01",
            "妙に気を使っちゃったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_148F")

    label("loc_141D")


    #C0046
    ChrTalk(
        0xFE,
        (
            "ルーヴィックさんとオリガさん、\x01",
            "夫婦喧嘩中みたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "はあ、勘弁してほしいわ。\x01",
            "気を使っちゃうじゃない……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_148F")

    Jump("loc_1C0E")

    label("loc_1494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_15A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1544")

    #C0048
    ChrTalk(
        0xFE,
        (
            "今日は各国の首脳が\x01",
            "アルカンシェルを観劇している\x01",
            "らしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "うーん、さぞ、いい席で\x01",
            "楽しんでるんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        "くう～、うらやましいわ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_159B")

    label("loc_1544")


    #C0051
    ChrTalk(
        0xFE,
        (
            "結局、今度のリニューアル公演の\x01",
            "チケットは買い逃しちゃったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "はーあ……\x02",
    )

    CloseMessageWindow()

    label("loc_159B")

    Jump("loc_1C0E")

    label("loc_15A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_16DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_164C")

    #C0053
    ChrTalk(
        0xFE,
        (
            "ねえ聞いた？　噂じゃ、\x01",
            "あの《金の太陽、銀の月》が\x01",
            "リニューアルするそうじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "う～ん、楽しみよね。\x01",
            "早速チケットを買いに行かないと！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16D7")

    label("loc_164C")


    #C0055
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの\x01",
            "《金の太陽、銀の月》が\x01",
            "リニューアルするらしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "これは絶対に見逃せないわ……\x01",
            "早速チケットを買いに行かないと！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D7")

    Jump("loc_1C0E")

    label("loc_16DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1867")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D7")

    #C0057
    ChrTalk(
        0xFE,
        (
            "１階のルーヴィックさんに、\x01",
            "マンションの改築工事を\x01",
            "もちかけられたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "ミラは全部持つからとか\x01",
            "言ってたけど、\x01",
            "結局奥さんが止めに来たわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "いやー、びっくりしたわよ。\x01",
            "そもそも雇われ管理人の\x01",
            "私に言われても……ねぇ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1862")

    label("loc_17D7")


    #C0060
    ChrTalk(
        0xFE,
        (
            "ルーヴィックさんって、\x01",
            "元議員ですごく裕福なのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "だからといって、\x01",
            "マンションを改築しようとか\x01",
            "なかなか思いつかないと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1862")

    Jump("loc_1C0E")

    label("loc_1867")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1AEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A30")

    #C0062
    ChrTalk(
        0xFE,
        (
            "３階の人とは、\x01",
            "いつもタイミングが悪くて\x01",
            "会えてなかったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "今朝、鉢合わせして\x01",
            "やっとご挨拶できたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "シュリっていう女の子で、\x01",
            "なんとアルカンシェルの見習いを\x01",
            "やってるんですって！\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "んふふ、まだまだ無名みたいだけど、\x01",
            "これからチェックしていかないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#00005F（確かシュリって、\x01",
            "  イリアさんの部屋の\x01",
            "  居候だよな……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        (
            "#00100F（３階がイリアさんの\x01",
            "  部屋ってことに、\x01",
            "  気づいてないみたいね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AE6")

    label("loc_1A30")


    #C0068
    ChrTalk(
        0xFE,
        (
            "でも、アルカンシェルって\x01",
            "やっぱり給料がいいのね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "見習いの子でも、こんなに大きな\x01",
            "マンションに住めちゃうんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00006F（本当はイリアさんの\x01",
            "  部屋だからなあ……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AE6")

    Jump("loc_1C0E")

    label("loc_1AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1C0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BBB")

    #C0071
    ChrTalk(
        0xFE,
        (
            "私はこのアパートで\x01",
            "雇われ管理人を\x01",
            "してるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "ここはほんと、\x01",
            "広くて綺麗でいいわね。\x01",
            "私もこんなところに住みたいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "……広すぎて、\x01",
            "ちょっと掃除が大変だけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C0E")

    label("loc_1BBB")


    #C0074
    ChrTalk(
        0xFE,
        (
            "ええっと、あとは中庭の\x01",
            "掃除もしないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        "ふう、雇われ管理人も大変よね。\x02",
    )

    CloseMessageWindow()

    label("loc_1C0E")

    TalkEnd(0xFE)
    Return()

    # Function_5_7DC end

    def Function_6_1C12(): pass

    label("Function_6_1C12")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1DB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D1E")

    #C0076
    ChrTalk(
        0xFE,
        (
            "大統領は、オルキスタワーの内部に\x01",
            "怪しげな施設を建造していたそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "私が外観デザインを手がけた\x01",
            "オルキスタワーに怪しげな手を加え、\x01",
            "それを悪用していたなど……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "我々はみんな騙されていたのだ。\x01",
            "やれやれ、到底許す事はできんよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1DAE")

    label("loc_1D1E")


    #C0079
    ChrTalk(
        0xFE,
        (
            "大統領は、オルキスタワーの内部に\x01",
            "怪しげな施設を建造していたそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "我々はみんな騙されていたのだ。\x01",
            "やれやれ、到底許す事はできんよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DAE")

    Jump("loc_2D3F")

    label("loc_1DB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1EB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E7D")

    #C0081
    ChrTalk(
        0xFE,
        (
            "だ、大統領め……\x01",
            "まさかここまでの事をやるとは！\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "オルキスタワーの外観デザインを\x01",
            "任せてくれたことには\x01",
            "感謝していたものだったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        "もはや信用することはできんな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EAE")

    label("loc_1E7D")


    #C0084
    ChrTalk(
        0xFE,
        (
            "大統領め……\x01",
            "もはや信用することはできんな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EAE")

    Jump("loc_2D3F")

    label("loc_1EB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1F50")

    #C0085
    ChrTalk(
        0xFE,
        (
            "こうなってしまっては、\x01",
            "帝国や共和国での仕事は\x01",
            "受けることはできないか……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "くっ、せめて今進めている仕事は\x01",
            "終わらせておきたかったが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D3F")

    label("loc_1F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_20B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2057")

    #C0087
    ChrTalk(
        0xFE,
        (
            "オルキスタワーは\x01",
            "アリオス殿のおかげで\x01",
            "守られたそうだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "ＩＢＣビルは残念だった。\x01",
            "あれもまたクロスベルの\x01",
            "象徴というべきものなのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "襲撃犯どもはクロスベルの\x01",
            "歴史そのものを侮辱したに等しい。\x01",
            "全く許し難いやつらだ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20B4")

    label("loc_2057")


    #C0090
    ChrTalk(
        0xFE,
        (
            "ＩＢＣビルはクロスベルを\x01",
            "象徴する建造物だったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        "襲撃犯め、全く許し難い……！\x02",
    )

    CloseMessageWindow()

    label("loc_20B4")

    Jump("loc_2D3F")

    label("loc_20B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_22CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_226D")

    #C0092
    ChrTalk(
        0xFE,
        (
            "………………………………\x01",
            "…………………………はっ。\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2196")
    Jump("loc_21E0")

    label("loc_2196")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_21B6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21E0")

    label("loc_21B6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21D6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21E0")

    label("loc_21D6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21E0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0093
    ChrTalk(
        0xFE,
        "……何か用かね？\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "図面を引くのに集中しててな、\x01",
            "悪いが邪魔をしないでくれるか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_22C5")

    label("loc_226D")


    #C0095
    ChrTalk(
        0xFE,
        (
            "最近、仕事によく\x01",
            "集中できるのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "周りがあまり見えないのが\x01",
            "欠点ではあるがな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C5")

    Jump("loc_2D3F")

    label("loc_22CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2345")

    #C0097
    ChrTalk(
        0xFE,
        (
            "雨音というのは、\x01",
            "どうしてこうも\x01",
            "心地いいのだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "何だか図面をひくのも\x01",
            "はかどるような気がするな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D3F")

    label("loc_2345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_23B5")

    #C0099
    ChrTalk(
        0xFE,
        (
            "むう……\x01",
            "やけに通りが騒がしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "しかし、あのサイレンは……\x01",
            "事故でもあったのだろうか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D3F")

    label("loc_23B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2490")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_243B")

    #C0101
    ChrTalk(
        0xFE,
        (
            "私は、偉大な建築家である祖父に\x01",
            "少しは近づけているのだろうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        "……うむ、今はとにかく仕事だな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_248B")

    label("loc_243B")


    #C0103
    ChrTalk(
        0xFE,
        (
            "たしか、帝国から\x01",
            "図面の依頼が来ていたはず……\x01",
            "そちらに取り掛かってみるか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_248B")

    Jump("loc_2D3F")

    label("loc_2490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_251E")

    #C0104
    ChrTalk(
        0xFE,
        (
            "オルキスタワーのお披露目が\x01",
            "終わったあとから、肩の荷が下りた。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "これからは心機一転して、\x01",
            "色々な仕事を手がけたいものだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D3F")

    label("loc_251E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_26A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2619")

    #C0106
    ChrTalk(
        0xFE,
        (
            "私はオルキスタワーの\x01",
            "外観デザインを手がけたのだが、\x01",
            "導力ネット関係がよく分からなくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "内部の図面は市長が推薦する\x01",
            "他の建築家に任せたのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "いや、他人と協力する事の大切さを\x01",
            "身をもって教えられた気がしたな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26A4")

    label("loc_2619")


    #C0109
    ChrTalk(
        0xFE,
        (
            "オルキスタワー内部の図面は\x01",
            "市長が推薦する\x01",
            "他の建築家に任せたのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "他人と協力する事の大切さを\x01",
            "身をもって教えられた気がしたよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26A4")

    Jump("loc_2D3F")

    label("loc_26A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_287B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D0")

    #C0111
    ChrTalk(
        0xFE,
        (
            "オルキスタワーほどの建物が\x01",
            "ここまでのスピードで完成した背景に、\x01",
            "導力ネットの功績があったのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "建設関係者の間では、\x01",
            "図面などの情報のやりとりを\x01",
            "導力ネットで行っていたのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "それが作業の効率化に\x01",
            "つながったのだから……\x01",
            "技術の進歩とは素晴らしいものだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2876")

    label("loc_27D0")


    #C0114
    ChrTalk(
        0xFE,
        (
            "オルキスタワーの建設では\x01",
            "導力ネットによって\x01",
            "情報のやりとりが行われていたのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "市長が法整備をしてまで\x01",
            "普及させようとする理由が\x01",
            "なんとなく分かる気がするな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2876")

    Jump("loc_2D3F")

    label("loc_287B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2889")
    Jump("loc_2D3F")

    label("loc_2889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_29A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_292E")

    #C0116
    ChrTalk(
        0xFE,
        (
            "いよいよ明日、\x01",
            "私が外観のデザインを手がけた\x01",
            "『オルキスタワー』がお披露目される。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "ふう……\x01",
            "なんだか年甲斐もなく\x01",
            "緊張してきたな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_29A1")

    label("loc_292E")


    #C0118
    ChrTalk(
        0xFE,
        (
            "いよいよ『オルキスタワー』も\x01",
            "明日、お披露目か……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "除幕式のあとは、\x01",
            "建築関係者に挨拶して\x01",
            "回るとしようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29A1")

    Jump("loc_2D3F")

    label("loc_29A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2BB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B04")

    #C0120
    ChrTalk(
        0xFE,
        (
            "市庁舎……\x01",
            "いや、今は市民会館だったか。\x01",
            "あの建物は私の祖父が設計したのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "祖父は偉大な建築家でな。\x01",
            "クロスベルの旧い公共施設などは、\x01",
            "ほとんど祖父が手がけたのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "そんな祖父の背中を見て、\x01",
            "私もまた建築家を目指した……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "そして、孫である私が\x01",
            "新市庁ビルの外観をデザインした……\x01",
            "いや、人生とは面白いものだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BAC")

    label("loc_2B04")


    #C0124
    ChrTalk(
        0xFE,
        (
            "私の祖父は偉大な建築家だった。\x01",
            "今の市民会館は、\x01",
            "私の祖父が手がけたのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "そして、孫である私が\x01",
            "新市庁ビルの外観をデザインした……\x01",
            "いや、人生とは面白いものだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BAC")

    Jump("loc_2D3F")

    label("loc_2BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2D3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CCB")

    #C0126
    ChrTalk(
        0xFE,
        (
            "クロスベル市の新市庁ビルが\x01",
            "ようやく完成してな。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "新市長が建設計画を\x01",
            "引きついでくれだおかげで、\x01",
            "ようやくそこまでに至ったのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "一時は、予算が凍結されるなどで\x01",
            "完成が危ぶまれたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "外観のデザインに携わった私も\x01",
            "腰を落ち着けられそうだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D3F")

    label("loc_2CCB")


    #C0130
    ChrTalk(
        0xFE,
        (
            "私は建築家として新市庁ビルの\x01",
            "外観のデザインに携わったのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "それももうすぐ完成……\x01",
            "感慨深いものがあるな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D3F")

    TalkEnd(0xFE)
    Return()

    # Function_6_1C12 end

    def Function_7_2D43(): pass

    label("Function_7_2D43")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2EE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E51")

    #C0132
    ChrTalk(
        0xFE,
        (
            "主人は大統領に怒りつつも、\x01",
            "次の仕事に着手し始めたようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "街であんな事がありましたから、\x01",
            "防犯・警備面での改築の依頼が\x01",
            "色んな会社から殺到していまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "この際タワーのことは引き摺らず、\x01",
            "ひたすら仕事をこなして欲しいですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2EE1")

    label("loc_2E51")


    #C0135
    ChrTalk(
        0xFE,
        (
            "防犯・警備面での改築の依頼が\x01",
            "色んな会社から殺到していまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "この際タワーのことは引き摺らず、\x01",
            "ひたすら仕事をこなして欲しいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EE1")

    Jump("loc_39FB")

    label("loc_2EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2F5D")

    #C0137
    ChrTalk(
        0xFE,
        (
            "外にいる化物は建物の中にまで\x01",
            "入ってくる気配はありませんけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        "やはり怖いものは怖いですね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_39FB")

    label("loc_2F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2FDC")

    #C0139
    ChrTalk(
        0xFE,
        (
            "ＩＢＣの資金を\x01",
            "凍結するという宣言には、\x01",
            "流石に驚きました。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "こ、こんなことして\x01",
            "大丈夫なんでしょうか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FB")

    label("loc_2FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3112")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A5")

    #C0141
    ChrTalk(
        0xFE,
        (
            "街が賊に襲撃されるなんて、\x01",
            "恐ろしい事件でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "この辺りは大した被害も\x01",
            "なかったのですけど、\x01",
            "これから心配です……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "またこんな事が起きなければ\x01",
            "いいのですが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_310D")

    label("loc_30A5")


    #C0144
    ChrTalk(
        0xFE,
        (
            "街が賊に襲撃されるなんて、\x01",
            "恐ろしい事件でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "またこんな事が起きなければ\x01",
            "いいのですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_310D")

    Jump("loc_39FB")

    label("loc_3112")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_319C")

    #C0146
    ChrTalk(
        0xFE,
        (
            "なんだかこの間から、\x01",
            "色々と事件が起きていますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "少し前までは表立った事件なんて\x01",
            "ほとんど起きていなかったのに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FB")

    label("loc_319C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_32A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3228")

    #C0148
    ChrTalk(
        0xFE,
        (
            "いやだわ……\x01",
            "今日は百貨店に買い物に\x01",
            "いこうと思っていたのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "仕方ないですね、\x01",
            "傘を差していかないと……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_329E")

    label("loc_3228")


    #C0150
    ChrTalk(
        0xFE,
        (
            "輸入雑貨店のほうに\x01",
            "いいコーヒー豆があるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "湿気させると風味を損ねるので、\x01",
            "雨だと困ってしまいますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_329E")

    Jump("loc_39FB")

    label("loc_32A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_32E8")

    #C0152
    ChrTalk(
        0xFE,
        (
            "ええと、主人の好きな\x01",
            "リベール産のコーヒーはと……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FB")

    label("loc_32E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_346D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D8")

    #C0153
    ChrTalk(
        0xFE,
        (
            "主人は以前から、\x01",
            "お爺さまへのコンプレックスに\x01",
            "喘いでいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "ですが、オルキスタワーの\x01",
            "外観デザインに関わったことで\x01",
            "かなり前向きになったと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "自分でも自信がもてた\x01",
            "仕事になったのでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3468")

    label("loc_33D8")


    #C0156
    ChrTalk(
        0xFE,
        (
            "主人はお爺さまへの\x01",
            "コンプレックスが\x01",
            "薄れてきたみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "タワーの外観デザインをしたことが\x01",
            "主人に自信を持たせて\x01",
            "くれたのでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3468")

    Jump("loc_39FB")

    label("loc_346D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_34FD")

    #C0158
    ChrTalk(
        0xFE,
        (
            "主人の仕事がはかどる様に、\x01",
            "コーヒーを淹れてあげましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "今日のはリベール産の豆だから\x01",
            "きっといい香りがするでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FB")

    label("loc_34FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3599")

    #C0160
    ChrTalk(
        0xFE,
        (
            "実は、今朝ごろ\x01",
            "色々と新しい仕事が\x01",
            "舞い込んできたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "主人もタワーの仕事が\x01",
            "終わったからといって、\x01",
            "なかなか休む間がありませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FB")

    label("loc_3599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3630")

    #C0162
    ChrTalk(
        0xFE,
        (
            "主人ったら聞いてもないのに\x01",
            "オルキスタワーのことを\x01",
            "色々と教えてくれるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "ふふ、昼間の除幕式の\x01",
            "興奮が冷めきらないみたいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FB")

    label("loc_3630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_36C3")

    #C0164
    ChrTalk(
        0xFE,
        (
            "オルキスタワーの\x01",
            "デザインに関わった主人も、\x01",
            "除幕式に出席していたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "今頃は、完成の余韻に\x01",
            "浸ってる頃かもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FB")

    label("loc_36C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3749")

    #C0166
    ChrTalk(
        0xFE,
        (
            "今回は特に大きな仕事だったので\x01",
            "主人は緊張してるみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "コーヒーでも淹れて\x01",
            "落ち着いてもらいましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FB")

    label("loc_3749")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_38C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3826")

    #C0168
    ChrTalk(
        0xFE,
        (
            "主人のお爺さまについては\x01",
            "私もよく聞かされています。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "とても優秀な建築家だったらしく、\x01",
            "主人の永遠の目標なんだとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "少し、コンプレックスに\x01",
            "感じている部分もあるのかも\x01",
            "しれませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38BD")

    label("loc_3826")


    #C0171
    ChrTalk(
        0xFE,
        (
            "主人は優秀な建築家だった\x01",
            "お爺さまにコンプレックスを\x01",
            "感じているみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "主人は主人なりにがんばってますし、\x01",
            "私はそれでいいと思うんですが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38BD")

    Jump("loc_39FB")

    label("loc_38C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_39FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3995")

    #C0173
    ChrTalk(
        0xFE,
        (
            "主人は、新市庁ビルの設計に\x01",
            "改めて関わる事になったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "大きな仕事ですから、\x01",
            "ここ１ヶ月は根を詰めて\x01",
            "働いていたんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "でも、それも一段落したみたいで\x01",
            "安心しました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_39FB")

    label("loc_3995")


    #C0176
    ChrTalk(
        0xFE,
        (
            "うちは自宅が設計事務所に\x01",
            "なっているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "最近は新市庁ビルの設計に\x01",
            "大忙しだったんですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39FB")

    TalkEnd(0xFE)
    Return()

    # Function_7_2D43 end

    def Function_8_39FF(): pass

    label("Function_8_39FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3A92")

    #C0178
    ChrTalk(
        0xFE,
        (
            "やはり、どうにも物騒な\x01",
            "世の中になってしまったものじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "何処かの地下にシェルターを作って\x01",
            "婆さんと隠れていようかのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_437F")

    label("loc_3A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3B0E")

    #C0180
    ChrTalk(
        0xFE,
        (
            "むうう、外においてある\x01",
            "わしの車は無事じゃろうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "もし傷つけでもしたら\x01",
            "損害賠償を請求してやるわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_437F")

    label("loc_3B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3B1C")
    Jump("loc_437F")

    label("loc_3B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3CEC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B58")
    Call(0, 19)
    Return()

    label("loc_3B58")


    #C0182
    ChrTalk(
        0xFE,
        (
            "ゲバル君は今、アルモリカ村に\x01",
            "滞在しておるはずじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "探せば見つかるじゃろうから、\x01",
            "事情は彼自身に聞いてみるがええ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CE7")

    label("loc_3BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CB4")

    #C0184
    ChrTalk(
        0xFE,
        (
            "旧い家具を売り払ったミラを、\x01",
            "チャリティイベント会場で\x01",
            "寄付してきたんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "わしが使ってしまうよりも\x01",
            "よっぽど有意義に使われる\x01",
            "ことじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "皆が大変なときじゃ。\x01",
            "助け合っていかんとのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3CE7")

    label("loc_3CB4")


    #C0187
    ChrTalk(
        0xFE,
        (
            "皆が大変なときじゃ。\x01",
            "助け合っていかんとのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CE7")

    Jump("loc_437F")

    label("loc_3CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3E2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DB3")

    #C0188
    ChrTalk(
        0xFE,
        (
            "武装集団に町が占拠されるなど、\x01",
            "前代未聞じゃわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "もしマインツ方面に\x01",
            "ドライブにでも行っておったら\x01",
            "巻き込まれていた可能性も……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "ああ、恐ろしや。\x01",
            "ぶるぶる……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E28")

    label("loc_3DB3")


    #C0191
    ChrTalk(
        0xFE,
        (
            "もしマインツ方面に\x01",
            "ドライブにでも行っておったら\x01",
            "巻き込まれていた可能性も……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "ああ、恐ろしや。\x01",
            "ぶるぶる……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E28")

    Jump("loc_437F")

    label("loc_3E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3EB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E48")
    Call(0, 13)
    Jump("loc_3EB1")

    label("loc_3E48")


    #C0193
    ChrTalk(
        0xFE,
        (
            "（ふむ……あのアルム君が\x01",
            "  これほどまでに大きくなって……）\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        "（それなのに、あの馬鹿モンは……）\x02",
    )

    CloseMessageWindow()

    label("loc_3EB1")

    Jump("loc_437F")

    label("loc_3EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3EC4")
    Jump("loc_437F")

    label("loc_3EC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3ED2")
    Jump("loc_437F")

    label("loc_3ED2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F59")

    #C0195
    ChrTalk(
        0xFE,
        (
            "明日行こうと思っておった\x01",
            "ドライブに、婆さんを\x01",
            "誘ってみたんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "これで少しでも機嫌を\x01",
            "直してくれるといいが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_437F")

    label("loc_3F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4093")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_401E")

    #C0197
    ChrTalk(
        0xFE,
        (
            "昨日から婆さんと\x01",
            "ケンカしておるんじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "うむむ、２人暮らしで\x01",
            "この冷戦状態は\x01",
            "ツラいものがあるのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "ふむ、どうしたら婆さんと\x01",
            "仲直りできるじゃろうか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_408E")

    label("loc_401E")


    #C0200
    ChrTalk(
        0xFE,
        (
            "どうしたら婆さんと\x01",
            "仲直りできるじゃろうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "やはり高級なワインを……\x01",
            "いやいや、流石にそれはないか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_408E")

    Jump("loc_437F")

    label("loc_4093")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4129")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40AE")
    Call(0, 9)
    Jump("loc_4124")

    label("loc_40AE")


    #C0202
    ChrTalk(
        0xFE,
        (
            "せっかく一緒に飲もうと思って\x01",
            "いいワインを買ってきたのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "ふん、もういいわい。\x01",
            "一人で飲んでしまうからの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4124")

    Jump("loc_437F")

    label("loc_4129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4137")
    Jump("loc_437F")

    label("loc_4137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4217")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41D9")

    #C0204
    ChrTalk(
        0xFE,
        (
            "導力車を雨風から守るために、\x01",
            "ガレージはぜひとも\x01",
            "欲しかったのじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "あそこまで怒られてしまっては、\x01",
            "諦めるしかないかのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4212")

    label("loc_41D9")


    #C0206
    ChrTalk(
        0xFE,
        (
            "ふう、しかしあそこまで\x01",
            "怒らんでもよかろうにのう……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4212")

    Jump("loc_437F")

    label("loc_4217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4376")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42E3")

    #C0207
    ChrTalk(
        0xFE,
        (
            "むう、表に出している導力車が\x01",
            "雨に濡れてしまうのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "やはり、ガレージのようなものが\x01",
            "欲しいところじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "まあいい、明日になったら\x01",
            "丹念に洗車するとしようかのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4371")

    label("loc_42E3")


    #C0210
    ChrTalk(
        0xFE,
        (
            "しかし、このまま導力車を\x01",
            "野ざらしにおいておくのも\x01",
            "なんじゃのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "マンション暮らしだと\x01",
            "ガレージが設置できんのが\x01",
            "辛いところじゃわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4371")

    Jump("loc_437F")

    label("loc_4376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_437F")

    label("loc_437F")

    TalkEnd(0xFE)
    Return()

    # Function_8_39FF end

    def Function_9_4383(): pass

    label("Function_9_4383")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0212
    ChrTalk(
        0xB,
        (
            "あーあ、やっぱり\x01",
            "このワインは美味いのーう。\x01",
            "買ってよかったわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xB,
        (
            "婆さんは要らんようじゃし、\x01",
            "わしが一人で飲むかのーう。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xC,
        "……ええ、お好きにどうぞ。\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xC,
        (
            "そのために高いミラを支払って\x01",
            "買ったんでしょうしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xB,
        (
            "……ふん！\x01",
            "ぐびぐびぐびぐび。\x02",
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

    # Function_9_4383 end

    def Function_10_44A1(): pass

    label("Function_10_44A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4542")

    #C0217
    ChrTalk(
        0xFE,
        (
            "主人ったら、地下シェルターなんて\x01",
            "買うミラなんかあるわけないでしょうに。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "なんでも高い買い物をして\x01",
            "解決しようとするクセは治らないわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E48")

    label("loc_4542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4589")

    #C0219
    ChrTalk(
        0xFE,
        (
            "まったく、主人ったら\x01",
            "こんな時まで車の心配なんか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E48")

    label("loc_4589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4630")

    #C0220
    ChrTalk(
        0xFE,
        (
            "演説を聞いたのだけど……\x01",
            "帝国と共和国は今までクロスベルで\x01",
            "暗闘を繰り広げてたらしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "クロスベル住人として、\x01",
            "とても許せることではないわ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E48")

    label("loc_4630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_46BD")

    #C0222
    ChrTalk(
        0xFE,
        (
            "街の復興のために\x01",
            "主人が寄付をしてきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "自分のためだけにミラを使う\x01",
            "浪費家だと思っていたけど、\x01",
            "少しだけ見直したわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E48")

    label("loc_46BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_472F")

    #C0224
    ChrTalk(
        0xFE,
        (
            "まさか、こんな大事件が\x01",
            "起きてしまうなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "なんとか警備隊が\x01",
            "解決してくれるといいけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E48")

    label("loc_472F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4797")

    #C0226
    ChrTalk(
        0xFE,
        (
            "アルム君が家庭を持って\x01",
            "クロスベルにねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "ふふ、とにかく\x01",
            "幸せそうで何よりだわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E48")

    label("loc_4797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_47A5")
    Jump("loc_4E48")

    label("loc_47A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_47B3")
    Jump("loc_4E48")

    label("loc_47B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4853")

    #C0228
    ChrTalk(
        0xFE,
        (
            "どういう風の吹き回しか\x01",
            "知らないけれど……\x01",
            "主人にドライブに誘われたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "まったく……\x01",
            "その程度で私の機嫌がとれる\x01",
            "とでも思ってるのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E48")

    label("loc_4853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_48CA")

    #C0230
    ChrTalk(
        0xFE,
        (
            "しばらく主人とは\x01",
            "口を利いてやらない\x01",
            "ことにしたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "一言謝ってくるまでは\x01",
            "許してやるもんですか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E48")

    label("loc_48CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_491B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48E5")
    Call(0, 9)
    Jump("loc_4916")

    label("loc_48E5")


    #C0232
    ChrTalk(
        0xFE,
        (
            "……ふん、主人のことなんて\x01",
            "知るもんですか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4916")

    Jump("loc_4E48")

    label("loc_491B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4A1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49D2")

    #C0233
    ChrTalk(
        0xFE,
        (
            "主人は、私に黙って\x01",
            "高級なヴィンテージワインを\x01",
            "買ってきたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "この間のガレージの件でも、\x01",
            "あれだけ怒ったのに……\x01",
            "まったく反省してないってことね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4A16")

    label("loc_49D2")


    #C0235
    ChrTalk(
        0xFE,
        (
            "主人ったら……\x01",
            "自分の浪費癖で私が喜ぶとでも\x01",
            "思ってるのかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A16")

    Jump("loc_4E48")

    label("loc_4A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4BA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B14")

    #C0236
    ChrTalk(
        0xFE,
        (
            "主人ったら、マンションの内部に\x01",
            "ガレージを増築しようとしていたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "なんとか主人を説得したけど、\x01",
            "相談されていたサミィさんが\x01",
            "呆気にとられてたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "まったく、浪費癖もここまでくると\x01",
            "あきれてものも言えないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4BA0")

    label("loc_4B14")


    #C0239
    ChrTalk(
        0xFE,
        (
            "主人ったら、マンションの内部に\x01",
            "ガレージを増築しようとしていたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "まったく、浪費癖もここまでくると\x01",
            "あきれてものも言えないわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BA0")

    Jump("loc_4E48")

    label("loc_4BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4D17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C7E")

    #C0241
    ChrTalk(
        0xFE,
        (
            "こんな雨の日は、\x01",
            "趣味に没頭するに限るわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "ちなみに、私の趣味は手芸なの。\x01",
            "最近じゃ、パッチワークなんかを\x01",
            "特に楽しんでいるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "ちくちくちく……\x01",
            "なかなか奥が深くて楽しいのよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4D12")

    label("loc_4C7E")


    #C0244
    ChrTalk(
        0xFE,
        (
            "私の趣味は手芸なの。\x01",
            "最近じゃ、パッチワークなんかを\x01",
            "特に楽しんでいるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "主人も私みたいに、\x01",
            "ミラがかからない趣味を\x01",
            "選べばよかったのに。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D12")

    Jump("loc_4E48")

    label("loc_4D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4E48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE4")

    #C0246
    ChrTalk(
        0xFE,
        "主人が浪費癖で困っているのよ。\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "以前から必要でもないのに\x01",
            "家具を買い換えたりして\x01",
            "いたのだけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "ついこの間なんて、\x01",
            "導力車を買ってしまったのよ。\x01",
            "まったくもう……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4E48")

    label("loc_4DE4")


    #C0249
    ChrTalk(
        0xFE,
        (
            "何の相談もなしに\x01",
            "導力車なんて買ってしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "あの人の浪費癖には\x01",
            "本当に困ったものだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E48")

    TalkEnd(0xFE)
    Return()

    # Function_10_44A1 end

    def Function_11_4E4C(): pass

    label("Function_11_4E4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E61")
    Call(0, 13)
    Jump("loc_4E96")

    label("loc_4E61")


    #C0251
    ChrTalk(
        0xFE,
        (
            "よ～し、今日はこのまま\x01",
            "病院の方へ足を運ぶかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E96")

    TalkEnd(0xFE)
    Return()

    # Function_11_4E4C end

    def Function_12_4E9A(): pass

    label("Function_12_4E9A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EAF")
    Call(0, 13)
    Jump("loc_4EE4")

    label("loc_4EAF")


    #C0252
    ChrTalk(
        0xFE,
        (
            "ふふ、少しずつだけど\x01",
            "着実に近づいて来てるわね㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EE4")

    TalkEnd(0xFE)
    Return()

    # Function_12_4E9A end

    def Function_13_4EE8(): pass

    label("Function_13_4EE8")

    OP_4B(0xB, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0253
    ChrTalk(
        0xF,
        (
            "なるほど、それじゃあ\x01",
            "数ヶ月前にウルスラ病院から……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xB,
        (
            "ああ、その後のことはわしも\x01",
            "詳しく知らんのじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xB,
        (
            "わざわざ来てくれたのに、\x01",
            "この程度しか教えてあげられんで\x01",
            "ほんと申し訳ないのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x10,
        (
            "いえ、そんなこと。\x01",
            "十分参考になりました。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)

    #C0257
    ChrTalk(
        0x10,
        "ね、あなた㈱\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 500)

    #C0258
    ChrTalk(
        0xF,
        (
            "ああ、エアリー。\x01",
            "家族３人で掴んだ大金星さ！\x02",
        )
    )

    CloseMessageWindow()

    #N0259
    NpcTalk(
        0x10,
        "赤ん坊",
        "きゃっきゃっ♪\x02",
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
            "はは、おぬしたち、\x01",
            "本当に仲が良いのう。\x02",
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

    # Function_13_4EE8 end

    def Function_14_50E2(): pass

    label("Function_14_50E2")

    TalkBegin(0xFE)

    #C0261
    ChrTalk(
        0xFE,
        (
            "こ、こんな事が起きるなんて\x01",
            "想像だにしなかったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "と、とにかく……\x01",
            "今の事態を一枚でも多く\x01",
            "写真に収めておかないとね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_50E2 end

    def Function_15_5168(): pass

    label("Function_15_5168")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_517D")
    Call(0, 17)
    Jump("loc_52D5")

    label("loc_517D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_529C")
    OP_4B(0xD, 0xFF)

    #C0263
    ChrTalk(
        0xE,
        (
            "#04206Fはあはあはあ……\x02\x03",

            "#04201Fなあ、イリアさん。\x01",
            "もう十分なんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xD,
        (
            "#01703Fん～、まだ緊張の色が窺えるから\x01",
            "もう少しほぐしとくかな。\x02\x03",

            "#01702Fとりあえず、いいから\x01",
            "あんたは黙って身を委ねてなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xE,
        (
            "#04206Fうう……\x01",
            "一体いつまで続くんだ、コレ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xD, 0xFF)
    Jump("loc_52D5")

    label("loc_529C")


    #C0266
    ChrTalk(
        0xE,
        (
            "#04206Fうう……\x01",
            "何でもいいから\x01",
            "早く終わらせてくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52D5")

    TalkEnd(0xFE)
    Return()

    # Function_15_5168 end

    def Function_16_52D9(): pass

    label("Function_16_52D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52EE")
    Call(0, 17)
    Jump("loc_54B9")

    label("loc_52EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5400")

    #C0267
    ChrTalk(
        0xD,
        (
            "#01700Fフフ、何だったら弟君たちも\x01",
            "マッサージしてあげましょうか？\x02\x03",

            "#01709F個人的には女性陣優先で\x01",
            "いきたいところなんだけど㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x102,
        "#00102Fあ、あはは……\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x109,
        "#10106Fえ、遠慮しておきます。\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xE,
        (
            "#04206F（はあ、これでシラフなんだから\x01",
            "  参っちゃうよな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_54B9")

    label("loc_5400")


    #C0271
    ChrTalk(
        0xD,
        (
            "#01700F夜の公演に向けて、しっかりと\x01",
            "シュリの身体をほぐしておかないとね。\x02\x03",

            "#01709F備えあれば憂いなし……\x01",
            "女子にはあたしのマッサージってね㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xE,
        "#04206F（い、意味が分かんねえ……）\x02",
    )

    CloseMessageWindow()

    label("loc_54B9")

    TalkEnd(0xFE)
    Return()

    # Function_16_52D9 end

    def Function_17_54BD(): pass

    label("Function_17_54BD")

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
        "#11P#01709Fあ、やっほー弟君☆\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xE,
        (
            "#04205F#5Pよ、よう……\x02\x03",

            "#04206F……いででででっ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x101,
        "#12P#00005Fな、何をしてるんですか？\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xD,
        (
            "#11P#01704Fフフ、今夜アルカンシェルに\x01",
            "各国の首脳さんたちが\x01",
            "観劇に来るんだけど……\x02\x03",

            "#01702Fシュリにも端役として\x01",
            "手伝ってもらうことになっててね。\x02\x03",

            "#01709F身体を柔らかくするための\x01",
            "マッサージタイムなの……よっと！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(50)
    SetChrSubChip(0xE, 0x0)

    def lambda_56E5():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_56E5)
    WaitChrThread(0xE, 2)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0277
    ChrTalk(
        0xE,
        "#04212F#11P#4Sいったあああああ！！\x02",
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
        "#6P#00102Fな、なるほど……\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x109,
        (
            "#6P#10105Fそ、その、大丈夫なんですか？\x02\x03",

            "#10106F素人が筋肉を触ると逆効果って\x01",
            "話も聞きますけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 500)

    #C0280
    ChrTalk(
        0xD,
        (
            "#11P#01704Fフフ、心配には及ばないわよ。\x02\x03",

            "#01702F以前プロのマッサージ師の人に\x01",
            "みっちり教えてもらって、\x01",
            "完璧にマスターしたからね。\x02\x03",

            "練習の合間のストレッチとかで、\x01",
            "リーシャにもよくやってるのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x105,
        (
            "#12P#10302Fなるほど、舞台のためなら\x01",
            "どんな分野のことでも吸収して\x01",
            "役立ててるってワケか。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x104,
        "#12P#00309Fいや～、さすがイリアさんッス！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x1)
    Sleep(100)

    #C0283
    ChrTalk(
        0xE,
        (
            "#04206F#5Pいやいやいやいや……\x01",
            "痛いものは痛いから！！\x02\x03",

            "#04201Fイ、イリアさん、本当の本当に\x01",
            "大丈夫なんだろうな！？\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xD,
        (
            "#11P#01706Fだから、ダイジョーブって\x01",
            "さっきから言ってるじゃないの。\x02\x03",

            "#01700F余計に痛いのは、今夜の舞台に\x01",
            "緊張して体が硬くなってるからよ。\x02\x03",

            "#01709F安心なさい、続けているうちに\x01",
            "だんだん気持ちよくなっていくから㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xE,
        "#04207F#5Pい、いかがわしい言い方すんなっ！\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xD,
        (
            "#11P#01701Fもー、うるさいわねえ。\x01",
            "じっとしてないと……こうよっ！\x02",
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
        "#5P#04212F#5Sひょわああああっ！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0288
    ChrTalk(
        0xE,
        "#5P#04207Fど、どどどどこ触ってんだ！！？？\x02",
    )

    CloseMessageWindow()
    OP_64(0xE)
    SetChrSubChip(0xE, 0x1)

    #C0289
    ChrTalk(
        0xD,
        (
            "#11P#01709Fムフフ、安心なさい。\x01",
            "これもしっかり効くマッサージだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xE,
        (
            "#04207F#5Pう、ウソつけー！！\x02\x03",

            "#04209Fあはは、く、くすぐった……\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xD,
        (
            "#11P#01709Fうんうん、育ってる育ってる㈱\x01",
            "あんた意外と将来有望なんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xE,
        "#04212F#5Pし、知るかっ！！\x02",
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
            "#6P#00113Fさ、さすがにちょっと\x01",
            "アレな光景な気がするけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x105,
        "#12P#10309Fフフ、これはこれで趣があるじゃない。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x101,
        (
            "#12P#00012Fはは、まあなんだかんだ言って\x01",
            "シュリもアルカンシェルに\x01",
            "馴染んでるって感じかな。\x02",
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
            "#5P#04207Fま、まとめに入らないでいいから\x01",
            "助けてくれよ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xD,
        "#11P#01709Fほらほら、逃がさないわよ～。\x02",
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

    # Function_17_54BD end

    def Function_18_5F63(): pass

    label("Function_18_5F63")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_629F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6141")
    SetChrName("")

    #A0298
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉の向こう側から、\x01",
            "イリアとシュリの賑やかな声が\x01",
            "聞こえて来る。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(130, 20, -1, -1)
    SetChrName("シュリの声")

    #A0299
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あは、あはははっ……\x01",
            "だから、ソコは違うって！\x02\x03",

            "はあはあ……\x01",
            "イリアさん、さっきから\x01",
            "わざとやってないか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("イリアの声")

    #A0300
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "やーねー、気のせいよ㈱\x02",
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
        "#00012Fイリアさん、凄く楽しそうだな。\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x102,
        "#00106Fシュリちゃん……かわいそうに。\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetScenarioFlags(0x0, 7)
    Jump("loc_629A")

    label("loc_6141")

    SetChrName("")

    #A0303
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉の向こう側から、\x01",
            "イリアとシュリの賑やかな声が\x01",
            "聞こえて来る。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(130, 20, -1, -1)
    SetChrName("シュリの声")

    #A0304
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はあはあはあ……\x01",
            "一体コレ、いつまで続くんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(130, 20, -1, -1)
    SetChrName("イリアの声")

    #A0305
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "さーねー、アンタが\x01",
            "もう少し大人しくしてるなら\x01",
            "早く済むと思うけど㈱\x02",
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

    label("loc_629A")

    Jump("loc_62CA")

    label("loc_629F")

    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0306
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵がかかっている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_62CA")

    TalkEnd(0xFF)
    Return()

    # Function_18_5F63 end

    def Function_19_62CE(): pass

    label("Function_19_62CE")

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
            "#2Pおや、君たち……\x01",
            "このわしに何か用かね？\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x101,
        (
            "#00004Fすみません、突然訪ねてしまって\x01",
            "申し訳ないんですが……\x02\x03",

            "#00000Fゲバルさん、というお名前に\x01",
            "心当たりはないでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0309
    ChrTalk(
        0xB,
        "#2Pふむ、君達はゲバル君の知り合いか？\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xB,
        (
            "#2P確かに彼は、議員時代に\x01",
            "私が面倒をみていた男だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x105,
        "#10300Fフフ、ビンゴだったみたいだね。\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x102,
        "#00100Fあの、実は……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0313
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちは、ゲバルの息子夫婦が\x01",
            "彼を探していることを説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0314
    ChrTalk(
        0xB,
        (
            "#2Pふむ、なるほどな。\x01",
            "君たちは彼らから頼まれて……\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xB,
        (
            "#2P実はこの間、ゲバル君が\x01",
            "『クロスベルから身を隠したい』と\x01",
            "わしの元に相談にきおったんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xB,
        (
            "#2Pやれやれ、あの馬鹿モンは……\x01",
            "あんな優しい息子夫婦に恵まれて、\x01",
            "なにを逃げることがあろうかのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x103,
        (
            "#00205Fやはりゲバルさんの行方を\x01",
            "知ってらっしゃいましたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x104,
        (
            "#00305Fしかし、『身を隠す』たあ\x01",
            "どういうことッスか？\x02\x03",

            "#00303Fいまいち理由が分からねえが……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x109,
        (
            "#10101Fそ、そうですよ！\x01",
            "せっかくアルムさんたちが\x01",
            "会いたいとおっしゃってるのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xB,
        (
            "#2Pうむ、他人から見れば\x01",
            "下らないことなのじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xB,
        (
            "#2P……いや、それについては\x01",
            "わしの口からは言うまい。\x02",
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
            "#2P……あやつは今、アルモリカ村に\x01",
            "滞在しておるはずじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xB,
        (
            "#2P探せば見つかるじゃろうから、\x01",
            "事情は彼自身に聞いてみるがええ。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x101,
        (
            "#00003F分かりました……\x01",
            "ありがとうございます。\x02\x03",

            "#00000Fさっそく、アルモリカ村に\x01",
            "向かってみるとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x102,
        "#00100Fええ、そうしましょう。\x02",
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

    # Function_19_62CE end

    SaveToFile()

Try(main)
