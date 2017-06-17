from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e302b.bin",                # FileName
        "e302b",                    # MapName
        "e302b",                    # Location
        0x0000,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e302b",                  # 0
        "正騎士アッバス",         # 1
        "ヨナ",                   # 2
        "ワジ",                   # 3
        "ティオ",                 # 4
        "フラン",                 # 5
        "リーシャ",               # 6
        "ランディ",               # 7
        "ノエル",                 # 8
        "エリィ",                 # 9
        "マクダエル議長",         # 10
        "グレイス",               # 11
        "神狼ツァイト",           # 12
        "従騎士ヴェントス",       # 13
        "従騎士ジュノー",         # 14
    ))

    AddCharChip((
        "chr/ch06712.itc",                   # 00
        "chr/ch06102.itc",                   # 01
        "chr/ch03100.itc",                   # 02
        "chr/ch03102.itc",                   # 03
        "chr/ch00202.itc",                   # 04
        "chr/ch06900.itc",                   # 05
        "chr/ch03200.itc",                   # 06
        "chr/ch00302.itc",                   # 07
        "chr/ch06002.itc",                   # 08
        "chr/ch02902.itc",                   # 09
        "chr/ch00102.itc",                   # 0A
        "chr/ch05802.itc",                   # 0B
        "chr/ch02710.itc",                   # 0C
        "chr/ch48400.itc",                   # 0D
    ))

    DeclNpc(101790,  150,     -94010,  90,   261,  0x0, 0,   0,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(3000,    -1350,   6960,    45,   261,  0x0, 0,   1,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(101790,  150,     -95980,  90,   261,  0x0, 0,   3,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-3119,   -1350,   7039,    315,  261,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(100849,  0,       270,     270,  261,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-1500,   0,       -1500,   0,    389,  0x0, 0,   6,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(97639,   170,     959,     90,   261,  0x0, 0,   7,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(100309,  170,     959,     270,  261,  0x0, 0,   9,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(100169,  100,     -102720, 270,  261,  0x0, 0,   10,  0,   255, 255, 0,   6,   255,  0)
    DeclNpc(98440,   100,     -101110, 180,  261,  0x0, 0,   11,  0,   255, 255, 0,   17,  255,  0)
    DeclNpc(100220,  100,     -104779, 270,  261,  0x0, 0,   8,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(-3000,   0,       -2500,   0,    389,  0x0, 0,   12,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(103569,  0,       -97089,  270,  257,  0x0, 0,   13,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(103949,  0,       -209,    270,  257,  0x0, 0,   13,  0,   0,   0,   0,   21,  255,  0)

    DeclActor(102510,  0,       -97020,  1000,    103570,  1500,    -97090,  0x007E, 0,  18, 0x0000)
    DeclActor(102710,  0,       -200,    400,     103950,  1500,    -210,    0x007E, 0,  20, 0x0000)
    DeclActor(2350,    0,       -92230,  800,     2350,    1500,    -92230,  0x007C, 0,  28, 0x0000)
    DeclActor(103750,  0,       -105640, 2000,    103750,  1500,    -105640, 0x007C, 0,  3,  0x0000)

    ChipFrameInfo(864, 0)                                        # 0

    ScpFunction((
        "Function_0_360",          # 00, 0
        "Function_1_410",          # 01, 1
        "Function_2_509",          # 02, 2
        "Function_3_54E",          # 03, 3
        "Function_4_71C",          # 04, 4
        "Function_5_857",          # 05, 5
        "Function_6_DF9",          # 06, 6
        "Function_7_1193",         # 07, 7
        "Function_8_1738",         # 08, 8
        "Function_9_1AED",         # 09, 9
        "Function_10_1C55",        # 0A, 10
        "Function_11_2190",        # 0B, 11
        "Function_12_230D",        # 0C, 12
        "Function_13_2942",        # 0D, 13
        "Function_14_2BA6",        # 0E, 14
        "Function_15_2D2E",        # 0F, 15
        "Function_16_311A",        # 10, 16
        "Function_17_3549",        # 11, 17
        "Function_18_38D5",        # 12, 18
        "Function_19_38D9",        # 13, 19
        "Function_20_3BEB",        # 14, 20
        "Function_21_3BEF",        # 15, 21
        "Function_22_3E28",        # 16, 22
        "Function_23_45CD",        # 17, 23
        "Function_24_4D08",        # 18, 24
        "Function_25_5484",        # 19, 25
        "Function_26_5EF4",        # 1A, 26
        "Function_27_688F",        # 1B, 27
        "Function_28_6D6A",        # 1C, 28
        "Function_29_76DB",        # 1D, 29
        "Function_30_76FB",        # 1E, 30
    ))


    def Function_0_360(): pass

    label("Function_0_360")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_398"),
        (1, "loc_3A4"),
        (2, "loc_3B0"),
        (3, "loc_3BC"),
        (4, "loc_3C8"),
        (5, "loc_3D4"),
        (6, "loc_3E0"),
        (SWITCH_DEFAULT, "loc_3EC"),
    )


    label("loc_398")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3A4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3B0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3BC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3C8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3D4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_40F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_40F")

    Return()

    # Function_0_360 end

    def Function_1_410(): pass

    label("Function_1_410")

    SetMapFlags(0x10000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0x12, 0x8)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrChipByIndex(0xF, 0x9)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x10, 0xA)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrChipByIndex(0x11, 0xB)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD")
    SetChrFlags(0xB, 0x10)

    label("loc_4BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_4D7")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 30)
    Jump("loc_508")

    label("loc_4D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_4EB")
    ClearScenarioFlags(0x22, 2)
    Event(0, 29)
    Jump("loc_508")

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 3)), scpexpr(EXPR_END)), "loc_508")
    ClearScenarioFlags(0x24, 3)
    SetChrPos(0x0, 102230, 0, -105070, 90)

    label("loc_508")

    Return()

    # Function_1_410 end

    def Function_2_509(): pass

    label("Function_2_509")

    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_527")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_53B")
    OP_24(0x1F2)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_541")

    label("loc_53B")

    Sound(498, 1, 80, 0)

    label("loc_541")

    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x3, 0x10)
    Return()

    # Function_2_509 end

    def Function_3_54E(): pass

    label("Function_3_54E")

    OP_C9(0x0, 0x4)
    OP_C9(0x0, 0x100)
    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_573")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6CF")
    RunExpression(0x5, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_5AC"),
        (1, "loc_5DB"),
        (2, "loc_6B3"),
        (3, "loc_6BB"),
        (SWITCH_DEFAULT, "loc_6CA"),
    )


    label("loc_5AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5CB")
    OP_2B(0x9A, 0x9B, 0x9C, 0x96, 0x97, 0x98, 0x99, 0xFFFF)
    Jump("loc_5D6")

    label("loc_5CB")

    OP_2B(0x96, 0x97, 0x98, 0x99, 0xFFFF)

    label("loc_5D6")

    Jump("loc_6CA")

    label("loc_5DB")

    SetMapFlags(0x40000000)
    OP_E5(0x7)
    Sleep(500)
    SetChrName("自動アナウンス")

    #A0001
    AnonymousTalk(
        0xFF,
        "こちらはクロスベル警察です。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_683")

    #A0002
    AnonymousTalk(
        0xFF,
        "報告を承ります。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    SetChrName("自動アナウンス")

    #A0003
    AnonymousTalk(
        0xFF,
        (
            "報告処理を終了します。\x01",
            "お疲れ様でした。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A5")

    label("loc_683")


    #A0004
    AnonymousTalk(
        0xFF,
        "報告可能な依頼はありません。\x02",
    )

    CloseMessageWindow()

    label("loc_6A5")

    OP_57(0x0)
    OP_E5(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_6CA")

    label("loc_6B3")

    Call(0, 4)
    Jump("loc_6CA")

    label("loc_6BB")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6CA")

    label("loc_6CA")

    Jump("loc_573")

    label("loc_6CF")

    OP_E5(0x6)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70C")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 5)
    Return()

    label("loc_70C")

    FadeToBright(1000, 0)
    OP_0D()
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    # Function_3_54E end

    def Function_4_71C(): pass

    label("Function_4_71C")

    OP_E5(0x6)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 3)), scpexpr(EXPR_END)), "loc_73E")
    SetScenarioFlags(0x2A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73E")
    ClearScenarioFlags(0x2A, 0)

    label("loc_73E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_END)), "loc_75B")
    SetScenarioFlags(0x2A, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75B")
    ClearScenarioFlags(0x2A, 1)

    label("loc_75B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_END)), "loc_778")
    SetScenarioFlags(0x2A, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_778")
    ClearScenarioFlags(0x2A, 2)

    label("loc_778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 6)), scpexpr(EXPR_END)), "loc_795")
    SetScenarioFlags(0x2A, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_795")
    ClearScenarioFlags(0x2A, 3)

    label("loc_795")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_END)), "loc_7B2")
    SetScenarioFlags(0x2A, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B2")
    ClearScenarioFlags(0x2A, 4)

    label("loc_7B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_END)), "loc_7CF")
    SetScenarioFlags(0x2A, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CF")
    ClearScenarioFlags(0x2A, 5)

    label("loc_7CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_END)), "loc_7DB")
    SetScenarioFlags(0x2A, 6)

    label("loc_7DB")

    OP_24(0x1F2)
    RunExpression(0x9, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_820")
    Sound(498, 1, 50, 0)
    Jump("loc_826")

    label("loc_820")

    Sound(498, 1, 100, 0)

    label("loc_826")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_856")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_856")

    Return()

    # Function_4_71C end

    def Function_5_857(): pass

    label("Function_5_857")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0xB, 0x12)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0x8, 0x1A)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0xC, 0x1B)
    SetChrSubChip(0xC, 0x0)
    OP_4B(0xB, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_END)), "loc_8C0")
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 102700, 0, -102930, 180)

    label("loc_8C0")

    OP_68(102970, 1000, -104740, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14560, 0)
    SetChrPos(0x101, 103020, 100, -105800, 90)
    SetChrPos(0xB, 101590, 0, -105440, 90)
    SetChrPos(0xC, 101470, 0, -104110, 135)
    SetChrPos(0x8, 103000, 0, -104100, 180)
    FadeToBright(1000, 0)
    OP_0D()

    #C0005
    ChrTalk(
        0xB,
        (
            "#00205Fおや……\x02\x03",

            "#00204Fどうやらロイドさんは、\x01",
            "『ポムっと！』で全員から\x01",
            "勝利を収めたみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xC,
        (
            "#01905Fええっ、本当ですか～！？\x02\x03",

            "#01909Fさすがロイドさん……\x01",
            "スゴすぎますよ～！！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_END)), "loc_A3E")

    #C0007
    ChrTalk(
        0x9,
        (
            "#02302Fへっ、そうだな。\x01",
            "アンタもなかなかやるじゃん。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3E")

    SetChrSubChip(0x101, 0x1)

    #C0008
    ChrTalk(
        0x101,
        (
            "#00009Fはは、ありがとう。\x01",
            "運がよかっただけかもしれないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#12100Fいや、このパズルゲームにおいては\x01",
            "運だけが勝利の要因たりえまい。\x02\x03",

            "#12102Fバニングス、お前こそが\x01",
            "真の『ポムっと！マスター』だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#00012F……そ、そりゃどうも。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xF0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE3")

    #C0011
    ChrTalk(
        0x8,
        (
            "#12100Fふむ……そうだな。\x02\x03",

            "よければこれを受け取るがいい。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x8, 0x0, 0x1F4, 0x5DC, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xF0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xF0, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0013
    ChrTalk(
        0x8,
        (
            "#12100F教会とエプスタイン財団が\x01",
            "古代の術をもとにして共同開発した、\x01",
            "禁断のマスタークオーツだ。\x02\x03",

            "強力すぎて扱いが難しく、\x01",
            "運用に踏み切れなかったものだが……\x02\x03",

            "#12102Fお前ならば正しく扱えるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00000Fああ、分かった。\x01",
            "是非とも役立たせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DC7")

    label("loc_CE3")


    #C0015
    ChrTalk(
        0x8,
        (
            "#12100Fふむ……そうだな。\x02\x03",

            "#12102F褒賞としてお前にこれをやろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x8, 0x0, 0x1F4, 0x5DC, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0016
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x67),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x67, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    #C0017
    ChrTalk(
        0x101,
        (
            "#00000Fはは、ありがとう。\x01",
            "是非とも役立たせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_DC7")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x2A, 7)
    OP_E0(0x35, 0x0)
    OP_E0(0x80, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    OP_D7(0x1E)
    EventEnd(0x5)
    SetScenarioFlags(0x24, 3)
    NewScene("e302B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_857 end

    def Function_6_DF9(): pass

    label("Function_6_DF9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1C")
    Call(0, 22)
    Jump("loc_E89")

    label("loc_E1C")


    #C0018
    ChrTalk(
        0x10,
        (
            "#00102F（……また、後でね。）\x02\x03",

            "#00104F（遅くなっても構わないから\x01",
            "  ゆっくり準備を済ませてちょうだい。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E89")

    Jump("loc_118F")

    label("loc_E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1100")

    #C0019
    ChrTalk(
        0x10,
        (
            "#00103Fクロスベル市解放作戦……\x01",
            "いよいよ明日に迫ったわね。\x02\x03",

            "#00108Fベルやおじさまに会ったら、\x01",
            "一連の事件の真意を問いただして……\x01",
            "出来るなら説得したいと思ってる。\x02\x03",

            "#00101Fでも、もしそれが叶わなかったら……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#00008Fエリィ……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x10,
        (
            "#00106F……ごめんなさい。\x01",
            "弱音を吐いてしまったわね。\x02\x03",

            "#00100F危険を顧みずに手を貸してくれる\x01",
            "多くの人たちに報いるために……\x02\x03",

            "何よりキーアちゃんを取り戻す為にも、\x01",
            "私たちは負けられないわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#00002F……明日は一緒に頑張ろう、エリィ。\x01",
            "俺やみんながついてるからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x10,
        (
            "#00104F……ふふ、そうね。\x02\x03",

            "#00102Fありがとう、ロイド。\x01",
            "おかげで気持ちが\x01",
            "少し楽になった気がするわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 5)
    Jump("loc_118F")

    label("loc_1100")


    #C0024
    ChrTalk(
        0x10,
        (
            "#00104Fありがとう、ロイド。\x01",
            "おかげで気持ちが少しだけ\x01",
            "楽になった気がするわ。\x02\x03",

            "#00102F今日はゆっくり休んで……\x01",
            "しっかり明日に備えましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_118F")

    TalkEnd(0xFE)
    Return()

    # Function_6_DF9 end

    def Function_7_1193(): pass

    label("Function_7_1193")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_122B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B6")
    Call(0, 23)
    Jump("loc_1226")

    label("loc_11B6")


    #C0025
    ChrTalk(
        0xB,
        (
            "#00204Fこちらが済んだら、\x01",
            "わたしも甲板に向かいます。\x02\x03",

            "#00202F相談のこと……\x01",
            "どうかよろしくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1226")

    Jump("loc_1734")

    label("loc_122B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1686")

    #C0026
    ChrTalk(
        0xB,
        (
            "#00203F（カタカタカタカタ……）\x02\x03",

            "#00200Fふむ、とりあえず準備は万端ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            "#00005Fティオ……\x01",
            "何をやっているんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x101, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1357")
    Jump("loc_13A1")

    label("loc_1357")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1377")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13A1")

    label("loc_1377")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1397")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13A1")

    label("loc_1397")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13A1")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    #C0028
    ChrTalk(
        0xB,
        (
            "#00202F明日の突入に向けて\x01",
            "メルカバのシステムの\x01",
            "最終チェックをしている所です。\x02\x03",

            "#00203Fわたしはロイドさんたちと一緒に\x01",
            "メルカバを降りていくつもりですが……\x02\x03",

            "#00200F通信ターミナルを押さえたあとの\x01",
            "ハッキングなどは、ヨナとフランさんに\x01",
            "お任せする必要がありますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#00001Fそうか……\x01",
            "なんだか大変そうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xB,
        (
            "#00204Fまあ、もうすぐ終わりますし\x01",
            "心配はいりません。\x02\x03",

            "#00202Fロイドさんはリーダーらしく、\x01",
            "ドンと構えておいてくれれば\x01",
            "十分かと。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0031
    ChrTalk(
        0x101,
        (
            "#00006Fいやいや、\x01",
            "明日の準備とか色々あるし。\x02\x03",

            "#00000Fまあ、その調子なら\x01",
            "ここは任せてよさそうだな。\x02\x03",

            "ティオたちもしっかり\x01",
            "休息をとっておいてくれよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xB,
        (
            "#00204Fええ、了解です。\x01",
            "そちらもゆっくり休んでください。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x1DA, 6)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_1734")

    label("loc_1686")


    #C0033
    ChrTalk(
        0xB,
        (
            "#00204F明日の突入に向けて\x01",
            "メルカバのシステムの\x01",
            "最終チェックをしている所です。\x02\x03",

            "#00202F一通り終わったら、\x01",
            "わたしも休息をとるつもりです。\x01",
            "そちらもゆっくり休んでください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1734")

    TalkEnd(0xFE)
    Return()

    # Function_7_1193 end

    def Function_8_1738(): pass

    label("Function_8_1738")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_17BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175B")
    Call(0, 24)
    Jump("loc_17B8")

    label("loc_175B")


    #C0034
    ChrTalk(
        0xE,
        (
            "#00304Fそんじゃあ、また後でな。\x02\x03",

            "#00302F俺もコイツの整備が終わったら\x01",
            "すぐに行くからよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17B8")

    Jump("loc_1AE9")

    label("loc_17BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A6F")

    #C0035
    ChrTalk(
        0xE,
        "#00300Fよっ、ロイド。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#00000Fランディたちは、\x01",
            "武器の整備をしてるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xE,
        (
            "#00302Fああ、なんつっても明日の作戦は\x01",
            "今までで最大の山場だろうからな。\x02\x03",

            "#00304F《ベルゼルガー》の出番もあるだろうし\x01",
            "いざって時にのためにも、\x01",
            "念入りにやっとかねえとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#00005Fうーん、今までドタバタして\x01",
            "あまり機会がなかったけど……\x02\x03",

            "#00003F俺も今夜のうちに\x01",
            "トンファーを手入れしとこうかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xE,
        (
            "#00309Fおお、やっとけやっとけ。\x02\x03",

            "#00303Fお前のはライフルと違って\x01",
            "精密部分の手入れなんかは\x01",
            "必要ないだろうが……\x02\x03",

            "#00300F磨きを入れてやるだけでも\x01",
            "大分違うもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#00005Fな、なるほど……\x01",
            "確かにそうかもしれないな。\x02\x03",

            "#00002Fアドバイス、ありがとう。\x01",
            "俺も後でやっておくとするよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 7)
    Jump("loc_1AE9")

    label("loc_1A6F")


    #C0041
    ChrTalk(
        0xE,
        (
            "#00304Fお前も、明日までに武器を\x01",
            "しっかり整備しとくといい。\x02\x03",

            "#00309Fそれこそ絶世の美女を扱うように\x01",
            "優しく、丁寧にな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AE9")

    TalkEnd(0xFE)
    Return()

    # Function_8_1738 end

    def Function_9_1AED(): pass

    label("Function_9_1AED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x68), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1BB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B10")
    Call(0, 25)
    Jump("loc_1BB0")

    label("loc_1B10")


    #C0042
    ChrTalk(
        0xF,
        (
            "#10106Fえ、えっと……\x01",
            "ロイドさんに是非とも\x01",
            "お願いしたいことがあるんです。\x02\x03",

            "#10101F後で甲板に来てください。\x01",
            "わたしも諸々の用事が済んだら\x01",
            "向かいますから……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB0")

    Jump("loc_1C51")

    label("loc_1BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC7")
    Call(0, 10)
    Jump("loc_1C51")

    label("loc_1BC7")


    #C0043
    ChrTalk(
        0xF,
        (
            "#10100Fあたしの方は今夜の内にもう一度\x01",
            "司令に連絡をとっておきますね。\x02\x03",

            "#10103F明日の作戦の最終確認も\x01",
            "しておいたほうがよさそうですし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C51")

    TalkEnd(0xFE)
    Return()

    # Function_9_1AED end

    def Function_10_1C55(): pass

    label("Function_10_1C55")

    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x101, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1CE6")
    Jump("loc_1D30")

    label("loc_1CE6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1D06")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D30")

    label("loc_1D06")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D26")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D30")

    label("loc_1D26")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D30")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xC, 0x101, 0)
    OP_4B(0xC, 0xFF)

    #C0044
    ChrTalk(
        0x101,
        (
            "#00000Fお疲れ様、ノエル、フラン。\x02\x03",

            "#00002F明日の作戦が迫ってるのに\x01",
            "ここはなんだか和んでるなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xF,
        (
            "#10102Fその、すみません。\x02\x03",

            "#10106F武器の手入れ中にフランが\x01",
            "入ってきちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xC,
        (
            "#01909Fふふっ、お姉ちゃんの\x01",
            "応援に来たんですよ～。\x02\x03",

            "#01904Fわたしは明日の準備を\x01",
            "ばっちりと済ませましたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#00009Fはは、それは頼もしいよ。\x02\x03",

            "#00000Fフランもオペレーターとして\x01",
            "活躍してもらわなきゃならないし、\x01",
            "しっかり英気を養ってくれよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xC,
        (
            "#01902Fはいっ、もちろんです～。\x01",
            "……というか、そのために\x01",
            "ここに来たんですよ～！\x02\x03",

            "#01909F何と言っても、わたしは\x01",
            "お姉ちゃんの側にいることで\x01",
            "エネルギーを充填できるんですから！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0049
    ChrTalk(
        0x101,
        (
            "#00000Fはは、あながち\x01",
            "冗談でもないのかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xF,
        (
            "#10106Fはあ、もう……\x01",
            "せめて邪魔はしないでよね。\x02\x03",

            "#10100Fえ、えっと、ロイドさん。\x01",
            "あたしの方は今夜の内にもう一度\x01",
            "司令に連絡をとっておきますね。\x02\x03",

            "#10103F明日の作戦の最終確認も\x01",
            "しておいたほうがよさそうですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        (
            "#00004Fああ、よろしく頼むよ。\x02\x03",

            "#00000Fノエルも、手入れが終わったら\x01",
            "しっかり休んでおいてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xF,
        "#10109Fはいっ！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0x0)
    OP_93(0xC, 0x10E, 0x0)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x1DB, 0)
    Return()

    # Function_10_1C55 end

    def Function_11_2190(): pass

    label("Function_11_2190")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x69), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2250")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B3")
    Call(0, 26)
    Jump("loc_224B")

    label("loc_21B3")


    #C0053
    ChrTalk(
        0xA,
        (
            "#10404Fもう一つだけ、君に\x01",
            "コッソリと伝えておくべき\x01",
            "ことがあるんだ。\x02\x03",

            "#10402F後で甲板に来てくれ。\x01",
            "僕もアッバスと飲みおわったら\x01",
            "そちらに行くからさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_224B")

    Jump("loc_2309")

    label("loc_2250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2262")
    Call(0, 12)
    Jump("loc_2309")

    label("loc_2262")


    #C0054
    ChrTalk(
        0xA,
        (
            "#10404Fま、上の許可は下りたことだし\x01",
            "僕たちも気兼ねなく\x01",
            "使命を遂行させてもらうよ。\x02\x03",

            "#10402Fフフ、明日は忙しくなりそうだ。\x01",
            "今のうちに十分寛#2Rくつろ#ぐとするかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2309")

    TalkEnd(0xFE)
    Return()

    # Function_11_2190 end

    def Function_12_230D(): pass

    label("Function_12_230D")

    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x101, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_239E")
    Jump("loc_23E8")

    label("loc_239E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_23BE")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23E8")

    label("loc_23BE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23DE")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23E8")

    label("loc_23DE")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23E8")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x101, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_249E")
    Jump("loc_24E8")

    label("loc_249E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_24BE")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24E8")

    label("loc_24BE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24DE")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24E8")

    label("loc_24DE")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24E8")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x8, 0x10)

    #C0055
    ChrTalk(
        0x101,
        (
            "#00005Fワジ、アッバス……\x01",
            "もしかして、飲んでるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xA,
        (
            "#10404F僕らもとりあえずは、\x01",
            "準備は終わったからね。\x02\x03",

            "#10402Fフフ、君も一杯どうだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#00006Fおいおい……\x01",
            "明日は作戦なのに大丈夫か？\x02\x03",

            "#00001Fすでにいくつかグラスを\x01",
            "空けちゃったみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "#12100F心配するな。\x01",
            "ヴェントスに作らせた\x01",
            "ノンアルコールのカクテルだ。\x02\x03",

            "明日の作戦の進行には\x01",
            "支障はあるまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#00006Fあ、ああそうか……\x02\x03",

            "#00000Fまあ、アッバスがそう言うなら\x01",
            "今回は信じてよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xA,
        (
            "#10409Fフフ、１人で飲んでるときでも\x01",
            "信じてくれて構わないんだけど。\x02\x03",

            "#10403F……そうそう、一応君たちにも\x01",
            "言っておいた方がよさそうだな。\x02\x03",

            "#10400F明日の作戦、法王猊下からも\x01",
            "正式に参加の許可が下りたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        "#00005Fあ……そうなのか。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "#12100F隠密活動を主とするメルカバを\x01",
            "大規模な作戦で運用するのは\x01",
            "本来ならば避けるべきだが……\x02\x03",

            "大陸全土の混乱状態を考えれば、\x01",
            "もはや多少の露見は止むを得まい。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#00006Fそうか……\x01",
            "教会の判断に感謝するよ。\x02\x03",

            "#00013F……とにかく、決戦は明日だ。\x01",
            "どうか、改めてよろしく頼む。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xA,
        "#10402Fフフ、了解だリーダー。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        "#12102F無論、力添えはさせてもらおう。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetScenarioFlags(0x1DB, 1)
    Return()

    # Function_12_230D end

    def Function_13_2942(): pass

    label("Function_13_2942")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x69), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2A6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_296A")
    Call(0, 26)
    Jump("loc_2A69")

    label("loc_296A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2974")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A69")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "パーティ編成\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_29C5"),
        (1, "loc_2A3E"),
        (SWITCH_DEFAULT, "loc_2A5A"),
    )


    label("loc_29C5")


    #C0066
    ChrTalk(
        0x8,
        (
            "#12100Fやれやれ……\x01",
            "あれはまだ秘匿事項なのだが。\x02\x03",

            "#12102F……まあ、仕方あるまい。\x01",
            "お前たちなら問題はなかろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A64")

    label("loc_2A3E")

    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(0)
    Fade(500)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A64")

    label("loc_2A5A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A64")

    Jump("loc_2974")

    label("loc_2A69")

    Jump("loc_2BA2")

    label("loc_2A6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A80")
    Call(0, 12)
    Jump("loc_2BA2")

    label("loc_2A80")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A8A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BA2")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "パーティ編成\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2ADB"),
        (1, "loc_2B77"),
        (SWITCH_DEFAULT, "loc_2B93"),
    )


    label("loc_2ADB")


    #C0067
    ChrTalk(
        0x8,
        (
            "#12100F明日の作戦……\x01",
            "こちらはメルカバからの\x01",
            "バックアップに集中しよう。\x02\x03",

            "市内に潜入するお前たちは、\x01",
            "今のうちにしっかりと\x01",
            "準備を整えておくがいい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B9D")

    label("loc_2B77")

    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(0)
    Fade(500)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B9D")

    label("loc_2B93")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B9D")

    Jump("loc_2A8A")

    label("loc_2BA2")

    TalkEnd(0xFE)
    Return()

    # Function_13_2942 end

    def Function_14_2BA6(): pass

    label("Function_14_2BA6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x68), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2C89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BC9")
    Call(0, 25)
    Jump("loc_2C84")

    label("loc_2BC9")


    #C0068
    ChrTalk(
        0xC,
        (
            "#01900Fロイドさん、お姉ちゃんのお願いを\x01",
            "ちゃんと聞いてあげてくださいね。\x02\x03",

            "#01909Fふふ、どうなるか楽しみです～。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#00003F（う～ん、なんでフランが\x01",
            "  こんな楽しそうなんだろう……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C84")

    Jump("loc_2D2A")

    label("loc_2C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C9B")
    Call(0, 10)
    Jump("loc_2D2A")

    label("loc_2C9B")


    #C0070
    ChrTalk(
        0xC,
        (
            "#01902Fロイドさん、明日は本当に\x01",
            "頑張ってくださいね～。\x02\x03",

            "#01909Fわたしもお姉ちゃんから\x01",
            "エネルギーを充填して、\x01",
            "しっかり備えておきますから！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D2A")

    TalkEnd(0xFE)
    Return()

    # Function_14_2BA6 end

    def Function_15_2D2E(): pass

    label("Function_15_2D2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_308E")

    #C0071
    ChrTalk(
        0x9,
        (
            "#02300F明日、あんたらがクロスベル市へ\x01",
            "潜入すると同時に、メルカバから\x01",
            "ハッキングを開始するぜ。\x02\x03",

            "#02303Fま、せいぜい頑張って\x01",
            "市内を引っ掻き回してくれよ？\x02\x03",

            "#02302Fリアルが混乱すれば、\x01",
            "導力ネットからつけ込むスキも\x01",
            "生まれてくるだろうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#00004Fああ、お互いの役割を\x01",
            "きっちりとこなそう。\x02\x03",

            "#00001F……ところで、ヨナ……\x01",
            "今日は徹夜するつもりじゃ\x01",
            "ないだろうな？（ジロリ）\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "#02305F……ギクッ。\x02\x03",

            "#02309Fい、いや～……ほら。\x01",
            "準備はそろそろ終わるけど、\x01",
            "ボクって夜型人間だしさ。\x02\x03",

            "#02304F下手に寝ちゃうより、\x01",
            "徹夜明けのテンションのほうが\x01",
            "調子いいかもしれないし。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#00006Fあのなあ……\x01",
            "明日は長丁場になるだろうし、\x01",
            "徹夜なんてしたらもたないぞ？\x02\x03",

            "#00001Fもうすぐ準備が終わりそうなら\x01",
            "なるべく早めに休んでくれ。\x01",
            "絶対そのほうがいいからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "#02306Fへーへー、分かった分かった。\x02\x03",

            "#02300F適当なとこで切り上げて休むから\x01",
            "いちいちニラむなっつーの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 3)
    Jump("loc_3116")

    label("loc_308E")


    #C0076
    ChrTalk(
        0x9,
        (
            "#02300F明日のハッキングに向けての準備は\x01",
            "もうそろそろ終わるぜ。\x02\x03",

            "#02306F適当なとこで切り上げて休むから\x01",
            "いちいち確認しに来んなよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3116")

    TalkEnd(0xFE)
    Return()

    # Function_15_2D2E end

    def Function_16_311A(): pass

    label("Function_16_311A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34A0")

    #C0077
    ChrTalk(
        0x12,
        (
            "#02103F現在の体制に異を唱えた者たちが\x01",
            "集結し、決死の覚悟で挑む\x01",
            "『クロスベル市解放作戦』……\x02\x03",

            "#02101Fもしこれが失敗すれば、\x01",
            "『大統領が正しかった』という\x01",
            "結論になってしまうでしょう。\x02\x03",

            "#02103F過去のカルバードの民主化、\x01",
            "その裏で行われた陰謀劇が\x01",
            "現在正当化されてしまったように。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#00003F……そうですね。\x02\x03",

            "#00001F全ては明日にかかっている……\x01",
            "そう言っても過言じゃないのは\x01",
            "十分に分かっているつもりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x12,
        (
            "#02109Fあはは、プレッシャーを\x01",
            "与えるつもりはなかったんだけど。\x02\x03",

            "#02103F……あたしはジャーナリストとして\x01",
            "今度のクロスベルの運命を見届け、\x01",
            "人々に伝えていく使命がある。\x02\x03",

            "#02100Fでも、ジャーナリストである前に\x01",
            "１人の人間として、あたしは\x01",
            "君たちを応援したいと思ってるわ。\x02\x03",

            "#02104Fガイさんの意思を受け継いで生まれた、\x01",
            "君たち特務支援課をね。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        "#00002Fグレイスさん……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x12,
        (
            "#02109Fフフ、キーアちゃんのためにも……\x01",
            "明日は頑張ってちょうだいね！\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#00000Fええ、任せてください！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 4)
    Jump("loc_3545")

    label("loc_34A0")


    #C0083
    ChrTalk(
        0x12,
        (
            "#02100Fジャーナリストである前に\x01",
            "１人の人間として、あたしは\x01",
            "君たちを応援したいと思ってる。\x02\x03",

            "#02109Fキーアちゃんって子のためにも……\x01",
            "明日は頑張ってちょうだいね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3545")

    TalkEnd(0xFE)
    Return()

    # Function_16_311A end

    def Function_17_3549(): pass

    label("Function_17_3549")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3841")

    #C0084
    ChrTalk(
        0x11,
        (
            "#02503F……恐らく明日は、\x01",
            "厳しい一日になってしまうだろう。\x02\x03",

            "#02500F何よりも、君たち若者に\x01",
            "『自治州の命運』というあまりに\x01",
            "重い荷物を背負わせてしまった。\x02\x03",

            "#02503F自治州の代表の１人として……\x01",
            "どうか、頭を下げさせてほしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        (
            "#00003F……どうか、そんな事は\x01",
            "おっしゃらないでください。\x02\x03",

            "#00000Fマクダエル議長には、\x01",
            "独立国の無効宣言という\x01",
            "大役を果たして頂きました。\x02\x03",

            "#00004Fあとは、戦える俺たちが\x01",
            "自身の手でやり遂げなくては\x01",
            "いけない問題なんだと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x11,
        (
            "#02503F……すまない。\x01",
            "本当に君たちには苦労をかけるな。\x02\x03",

            "#02500Fならば私は、君たちが必ずや\x01",
            "『解放作戦』を成し遂げる事を信じて、\x01",
            "今後の対策を考えるとしよう。\x02\x03",

            "#02503F混乱するクロスベルの住民たちが、\x01",
            "少しでも早く元の暮らしに戻れるように。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        "#00000Fええ……よろしくお願いします。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 5)
    Jump("loc_38D1")

    label("loc_3841")


    #C0088
    ChrTalk(
        0x11,
        (
            "#02503F私は、君たちが必ずや\x01",
            "『解放作戦』を成し遂げる事を信じて、\x01",
            "今後の対策を考えるとしよう。\x02\x03",

            "#02500F……どうか、女神の加護があらん事を。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38D1")

    TalkEnd(0xFE)
    Return()

    # Function_17_3549 end

    def Function_18_38D5(): pass

    label("Function_18_38D5")

    Call(0, 19)
    Return()

    # Function_18_38D5 end

    def Function_19_38D9(): pass

    label("Function_19_38D9")

    TalkBegin(0x14)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BE7")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "装備品を買う\x01",      # 1
            "消耗品を買う\x01",      # 2
            "やめる\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3951")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3951")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3970")
    OP_AF(0xD8)
    Jump("loc_39C2")

    label("loc_3970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_3980")
    OP_AF(0xD7)
    Jump("loc_39C2")

    label("loc_3980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_3990")
    OP_AF(0xD6)
    Jump("loc_39C2")

    label("loc_3990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_39A0")
    OP_AF(0xD5)
    Jump("loc_39C2")

    label("loc_39A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_39B0")
    OP_AF(0xD4)
    Jump("loc_39C2")

    label("loc_39B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_39C0")
    OP_AF(0xD3)
    Jump("loc_39C2")

    label("loc_39C0")

    OP_AF(0xD2)

    label("loc_39C2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BE2")

    label("loc_39D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39F1")
    OP_AF(0xDC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BE2")

    label("loc_39F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A05")
    Jump("loc_3BE2")

    label("loc_3A05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BE2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B2A")

    #C0089
    ChrTalk(
        0x14,
        (
            "決して楽観視できる\x01",
            "状況じゃないのは\x01",
            "僕にもわかってるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x14,
        (
            "警察に教会、警備隊、黒月、\x01",
            "はては《神狼》や《銀》までが\x01",
            "こちらの味方についてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x14,
        (
            "これだけのメンツが揃ってたら、\x01",
            "どんな事でもやり遂げられるんじゃ\x01",
            "ないかって思えてくるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3BE2")

    label("loc_3B2A")


    #C0092
    ChrTalk(
        0x14,
        (
            "警察に教会、警備隊、黒月、\x01",
            "はては《神狼》や《銀》までが\x01",
            "こちらの味方についてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x14,
        (
            "これだけのメンツが揃ってたら、\x01",
            "どんな事でもやり遂げられるんじゃ\x01",
            "ないかって思えてくるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BE2")

    Jump("loc_38E6")

    label("loc_3BE7")

    TalkEnd(0x14)
    Return()

    # Function_19_38D9 end

    def Function_20_3BEB(): pass

    label("Function_20_3BEB")

    Call(0, 21)
    Return()

    # Function_20_3BEB end

    def Function_21_3BEF(): pass

    label("Function_21_3BEF")

    TalkBegin(0x15)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3BFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E24")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",            # 0
            "改造・合成する\x01",      # 1
            "やめる\x01",              # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C5C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3C5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C7C")
    OP_AF(0xDD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E1F")

    label("loc_3C7C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C90")
    Jump("loc_3E1F")

    label("loc_3C90")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E1F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D93")

    #C0094
    ChrTalk(
        0x15,
        (
            "明日の作戦において、\x01",
            "やはり問題になるのは\x01",
            "３体の《神機》でしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x15,
        (
            "《神機》をいかに退けるか……それが、\x01",
            "市内への潜入の鍵になると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x15,
        (
            "各方面と連携をとって、\x01",
            "何としても作戦を成功させたいですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E1F")

    label("loc_3D93")


    #C0097
    ChrTalk(
        0x15,
        (
            "３体の《神機》をいかに退けるかが、\x01",
            "市内への潜入の鍵になると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x15,
        (
            "各方面と連携をとって、\x01",
            "何としても作戦を成功させたいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E1F")

    Jump("loc_3BFC")

    label("loc_3E24")

    TalkEnd(0x15)
    Return()

    # Function_21_3BEF end

    def Function_22_3E28(): pass

    label("Function_22_3E28")

    EventBegin(0x0)
    Fade(500)
    OP_68(100420, 1000, -101760, 0)
    MoveCamera(47, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15480, 0)
    SetChrPos(0x101, 100110, 0, -101660, 180)
    SetChrSubChip(0x10, 0x2)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4383")

    #C0099
    ChrTalk(
        0x10,
        (
            "#12P#00106Fクロスベル市解放作戦……\x01",
            "いよいよ明日に迫ったわね。\x02\x03",

            "#00108Fベルやおじさまに会ったら、\x01",
            "一連の事件の真意を問いただして……\x01",
            "出来るなら説得したいと思ってる。\x02\x03",

            "#00101Fでも、もしそれが叶わなかったら……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        "#00006F#5P……対立は避けられないだろうな。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x10,
        (
            "#12P#00103Fええ……もう私も\x01",
            "その覚悟はとっくに出来ている。\x02\x03",

            "#00108F危険を顧みずに手を貸してくれる\x01",
            "多くの人たちに報いるために……\x02\x03",

            "#00101F何より、キーアちゃんを\x01",
            "取り戻す為にも、私たちは絶対に\x01",
            "負けるわけにはいかないのだから。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)
    Sleep(500)

    #C0102
    ChrTalk(
        0x101,
        (
            "#00004F#5P……なあ、エリィ。\x02\x03",

            "#00000Fそんなに一人で気負う必要はないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x10,
        "#12P#00105Fえ……\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        (
            "#00003F#5Pディーターさんやマリアベルさんは、\x01",
            "俺たちにとっても親しい人たちだった。\x02\x03",

            "#00001Fだから、その重みはエリィだけじゃなく、\x01",
            "全員で背負っていくべきものだと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x10,
        "#12P#00108Fロイド……\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        (
            "#00002F……明日は一緒に頑張ろう、エリィ。\x01",
            "俺やみんながついてるからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x10,
        (
            "#12P#00104F……ふふ、そうね。\x02\x03",

            "#00102Fありがとう、ロイド。\x01",
            "おかげで気持ちが楽になったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        "#00009F#5Pはは……どういたしまして。\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10)
    Sleep(500)

    #C0109
    ChrTalk(
        0x10,
        (
            "#12P#00106F（……あ、あの、ロイド。）\x02\x03",

            "#00112F（明日の準備を済ませたら、\x01",
            "  後で甲板に来てくれない？）\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        "#00005F#5P（えっ……？）\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x10,
        (
            "#12P#00113F（出来れば、その……\x01",
            "  ふたりきりで話がしたいなあ、\x01",
            "  なんて……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 5)
    Jump("loc_4416")

    label("loc_4383")


    #C0112
    ChrTalk(
        0x10,
        (
            "#12P#00112F（明日の準備を済ませたら、\x01",
            "  後で甲板に来てくれない？）\x02\x03",

            "#00113F（出来れば、その……\x01",
            "  ふたりきりで話がしたいなあ、\x01",
            "  なんて……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4416")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "エリィの誘いを受ける\x01",      # 0
            "やめておく\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44F0")

    #C0113
    ChrTalk(
        0x101,
        (
            "#00002F#5P（……わ、分かった。\x01",
            "  俺でよければ行かせてもらうよ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x10,
        (
            "#12P#00109F（……ふふ、ありがとう。\x01",
            "  それじゃあ、また後でね。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 3)
    Jump("loc_45C6")

    label("loc_44F0")


    #C0115
    ChrTalk(
        0x10,
        (
            "#12P#00106F（……そっか。）\x02\x03",

            "#00102F（ふふ、気にしないで。\x01",
            "  あまり大したことじゃないの。）\x02\x03",

            "#00104F（もし気が向いたらでいいから、\x01",
            "  また声を掛けてちょうだい。）\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        "#00000F#5P（ああ、そうさせてもらうよ。）\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_45C6")

    SetChrSubChip(0x10, 0x0)
    EventEnd(0x5)
    Return()

    # Function_22_3E28 end

    def Function_23_45CD(): pass

    label("Function_23_45CD")

    EventBegin(0x0)
    Fade(500)
    OP_68(-3160, -500, 6480, 0)
    MoveCamera(52, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16170, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 6)), scpexpr(EXPR_END)), "loc_460F")
    SetChrSubChip(0xB, 0x1)

    label("loc_460F")

    SetChrPos(0x101, -3610, -1500, 5780, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B10")

    #C0117
    ChrTalk(
        0xB,
        (
            "#11P#00203F（カタカタカタカタ……）\x02\x03",

            "#00200Fふむ、とりあえず準備は万端ですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)

    #C0118
    ChrTalk(
        0xB,
        (
            "#11P#00208F（カサッ）\x02\x03",

            "#00203F……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#12P#00005F……えっと、ティオ？\x01",
            "何をやっているんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xB, 0x1)

    #C0120
    ChrTalk(
        0xB,
        (
            "#5P#00202F……ええ、明日の突入に向けて\x01",
            "メルカバのシステムの\x01",
            "最終チェックをしていました。\x02\x03",

            "#00203Fわたしはロイドさんたちと一緒に\x01",
            "メルカバを降りていくつもりですが……\x02\x03",

            "#00200F通信ターミナルを押さえたあとの\x01",
            "ハッキングなどは、ヨナとフランさんに\x01",
            "お任せする必要がありますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        (
            "#12P#00003Fそうか……\x01",
            "なんだか大変そうだな。\x02\x03",

            "#00000F何か、俺に手伝えることはあるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xB,
        (
            "#5P#00203F……いえ、特には。\x02\x03",

            "#00202F明らかにわたしの分野ですし、\x01",
            "ヨナもいるので十分です。\x02\x03",

            "#00204Fロイドさんはリーダーらしく、\x01",
            "ドンと構えておいてくれれば\x01",
            "十分かと。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0123
    ChrTalk(
        0x101,
        (
            "#12P#00006Fいやいや、\x01",
            "明日の準備とか色々あるし。\x02\x03",

            "#00000Fまあ、その調子なら\x01",
            "ここは任せてよさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)
    Sleep(500)

    #C0124
    ChrTalk(
        0xB,
        (
            "#5P#00203F……そういえば、\x01",
            "ひとつだけありました。\x02\x03",

            "#00208F実は……ロイドさんに\x01",
            "相談したい事があるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#12P#00005F相談……？\x01",
            "なにか悩み事でもあるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xB,
        (
            "#5P#00206F……いえ、ここではちょっと。\x02\x03",

            "#00201Fそちらの用が済んだら、\x01",
            "後でメルカバの甲板に\x01",
            "来ていただけませんか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 6)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_4B9A")

    label("loc_4B10")


    #C0127
    ChrTalk(
        0xB,
        (
            "#5P#00206F実は……ロイドさんに\x01",
            "相談したい事があるんです。\x02\x03",

            "#00201Fそちらの用が済んだら、\x01",
            "後でメルカバの甲板に\x01",
            "来ていただけませんか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B9A")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "ティオの誘いを受ける\x01",      # 0
            "やめておく\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C5E")

    #C0128
    ChrTalk(
        0x101,
        (
            "#12P#00002F分かった、俺でよければ\x01",
            "喜んで相談に乗らせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xB,
        (
            "#5P#00209Fふふっ……\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 4)
    Jump("loc_4D01")

    label("loc_4C5E")


    #C0130
    ChrTalk(
        0xB,
        (
            "#5P#00204F……そうですか。\x01",
            "まあ、仕方ありませんね。\x02\x03",

            "#00202Fもし相談に乗ってもらえるなら\x01",
            "また声を掛けてくれると嬉しいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        "#12P#00000Fああ、分かった。\x02",
    )

    OP_5A()
    CloseMessageWindow()

    label("loc_4D01")

    SetChrSubChip(0xB, 0x0)
    EventEnd(0x5)
    Return()

    # Function_23_45CD end

    def Function_24_4D08(): pass

    label("Function_24_4D08")

    EventBegin(0x0)
    Fade(500)
    OP_68(98200, 1000, 600, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16090, 0)
    SetChrPos(0x101, 97510, 0, -530, 0)
    SetChrSubChip(0xE, 0x2)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5280")

    #C0132
    ChrTalk(
        0xE,
        "#5P#00300Fよっ、ロイド。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        (
            "#12P#00000Fランディたちは、\x01",
            "武器の整備をしてるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xE,
        (
            "#5P#00302Fああ、なんつっても明日の作戦は\x01",
            "今までで最大の山場だろうからな。\x02\x03",

            "#00304F《ベルゼルガー》の出番もあるだろうし\x01",
            "いざって時にのためにも、\x01",
            "念入りにやっとかねえとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#12P#00005Fうーん、今までドタバタして\x01",
            "あまり機会がなかったけど……\x02\x03",

            "#00003F俺も今夜のうちに\x01",
            "トンファーを手入れしとこうかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xE,
        (
            "#5P#00309Fおお、やっとけやっとけ。\x02\x03",

            "#00303Fお前のはライフルと違って\x01",
            "精密部分の手入れなんかは\x01",
            "必要ないだろうが……\x02\x03",

            "#00300F磨きを入れてやるだけでも\x01",
            "大分違うもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#12P#00009Fはは、そうだな。\x02\x03",

            "#00005Fそれにしても……\x01",
            "ランディって意外とマメだよな。\x02\x03",

            "#00000Fそのライフルだけじゃなく、\x01",
            "スタンハルバードの手入れも\x01",
            "毎日欠かしてないみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xE,
        (
            "#5P#00302Fま、武器の手入れは\x01",
            "初歩中の初歩だからな。\x02\x03",

            "#00304Fそれこそ絶世の美女を扱うように\x01",
            "優しく、丁寧に扱わねえと。\x02\x03",

            "#00300Fじゃねえと、戦場で\x01",
            "余計なトラブルが\x01",
            "舞い込んじまう事だって──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xE)

    #C0139
    ChrTalk(
        0x101,
        (
            "#12P#00011F……悪い、もしかして、\x01",
            "余計なことを思い出させたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xE,
        (
            "#5P#00309F……ハハ、何謝ってんだっつの。\x02\x03",

            "#00306F……でも、そうだな。\x02\x03",

            "#00308Fそろそろ……話しても\x01",
            "いい頃合いかもしれねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#12P#00005Fえっ……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xE,
        (
            "#5P#00300Fなあ、後でヒマだったら\x01",
            "メルカバの甲板にでも出ねえか？\x02\x03",

            "ちょいと付き合って欲しい事が\x01",
            "あるんだけどよ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 7)
    Jump("loc_52F4")

    label("loc_5280")


    #C0143
    ChrTalk(
        0xE,
        (
            "#5P#00300Fよお、後でヒマだったら\x01",
            "メルカバの甲板にでも出ねえか？\x02\x03",

            "ちょいと付き合って欲しい事が\x01",
            "あるんだけどよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52F4")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "ランディの誘いを受ける\x01",      # 0
            "やめておく\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53DD")

    #C0144
    ChrTalk(
        0x101,
        (
            "#12P#00002F……分かった、\x01",
            "後で行かせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xE,
        (
            "#5P#00309Fはは、そんじゃあまた後でな。\x02\x03",

            "#00302F俺もコイツの整備が終わったら\x01",
            "すぐに行くからよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 5)
    Jump("loc_547D")

    label("loc_53DD")


    #C0146
    ChrTalk(
        0xE,
        (
            "#5P#00306F……そうか。\x01",
            "ま、別段楽しい話って\x01",
            "ワケでもねえが……\x02\x03",

            "#00300Fその気になったら\x01",
            "また声をかけてくれや。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        "#12P#00000Fああ、そうさせてもらうよ。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_547D")

    SetChrSubChip(0xE, 0x0)
    EventEnd(0x5)
    Return()

    # Function_24_4D08 end

    def Function_25_5484(): pass

    label("Function_25_5484")

    EventBegin(0x0)
    Fade(500)
    OP_68(100500, 1000, -240, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16970, 0)
    SetChrPos(0x101, 100340, 0, -1010, 0)
    SetChrSubChip(0xF, 0x1)
    OP_93(0xC, 0xB4, 0x0)
    OP_4B(0xC, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C38")

    #C0148
    ChrTalk(
        0xF,
        "#5P#10100Fロイドさん、お疲れ様です！\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xC,
        "#5P#01902Fお疲れ様です～！\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#12P#00000Fお疲れ様、ノエル、フラン。\x02\x03",

            "#00009F明日の作戦が迫ってるのに\x01",
            "ここはなんだか和んでるなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xF,
        (
            "#5P#10102Fその、すみません。\x02\x03",

            "#10106F武器の手入れ中にフランが\x01",
            "入ってきちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xC,
        (
            "#5P#01909Fふふっ、お姉ちゃんの\x01",
            "応援に来たんですよ～。\x02\x03",

            "#01904Fわたしは明日の準備を\x01",
            "ばっちりと済ませましたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        (
            "#12P#00004Fはは、それは頼もしいよ。\x02\x03",

            "#00000Fフランもオペレーターとして\x01",
            "活躍してもらわなきゃならないし、\x01",
            "しっかり英気を養ってくれよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xC,
        (
            "#5P#01902Fはいっ、もちろんです～。\x01",
            "……というか、そのために\x01",
            "ここに来たんですよ～！\x02\x03",

            "#01909F何と言っても、わたしは\x01",
            "お姉ちゃんの側にいることで\x01",
            "エネルギーを充填できるんですから！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0155
    ChrTalk(
        0x101,
        (
            "#12P#00012Fはは、あながち\x01",
            "冗談でもないのかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xF,
        (
            "#5P#10106Fはあ、もう……\x01",
            "せめて邪魔はしないでよね。\x02\x03",

            "#10102Fえ、えっと、ロイドさん。\x01",
            "あたしの方は今夜の内にもう一度\x01",
            "司令に連絡をとっておきますね。\x02\x03",

            "#10103F明日の作戦の最終確認も\x01",
            "しておいたほうがよさそうですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x101,
        (
            "#12P#00000Fああ、よろしく頼むよ。\x02\x03",

            "#00003Fノエルは明日、俺たちと一緒に\x01",
            "市内に潜入することになる……\x02\x03",

            "#00000F万全の準備を整えて、\x01",
            "しっかり休んでおいてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xF,
        "#5P#10109Fはいっ！\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    #C0159
    ChrTalk(
        0xC,
        (
            "#11P#01905F（ねえねえ、お姉ちゃん。\x01",
            "  このままじゃ、今日のおしゃべりが\x01",
            "  終わりそうな雰囲気だよ？）\x02\x03",

            "#01909F（せっかくのチャンスなのに、\x01",
            "  本当にこのままでいいの～？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0160
    ChrTalk(
        0xF,
        (
            "#5P#10111F（チャ、チャンスって……\x01",
            "  フラン、いい加減に……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0161
    ChrTalk(
        0x101,
        (
            "#12P#00005F……えっと、どうしたんだ？\x01",
            "なにか問題でもあったのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xF)

    #C0162
    ChrTalk(
        0xF,
        "#5P#10114Fい、いえっ、えっと……\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xC,
        "#11P#01909F（ガンバレ、お姉ちゃん！）\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xF,
        (
            "#5P#10103F……その……後でいいんですが、\x01",
            "甲板に来て頂けませんか？\x02\x03",

            "#10101F大したことじゃないんですけど、\x01",
            "ロイドさんに是非とも\x01",
            "お願いしたいことがあるんです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 0)
    Jump("loc_5CC3")

    label("loc_5C38")


    #C0165
    ChrTalk(
        0xF,
        (
            "#5P#10103F……後で、甲板に来て頂けませんか？\x02\x03",

            "#10101F大したことじゃないんですが、\x01",
            "ロイドさんに是非とも\x01",
            "お願いしたいことがあるんです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CC3")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "ノエルの誘いを受ける\x01",      # 0
            "やめておく\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DDE")

    #C0166
    ChrTalk(
        0x101,
        (
            "#12P#00002Fああ、分かった。\x01",
            "ノエルが頼み事なんて\x01",
            "珍しい気がするけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xC,
        "#11P#01909F（やったね、お姉ちゃん！）\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xF,
        (
            "#5P#10114Fそ、それじゃあ……\x01",
            "わたしも諸々の用事が済んだら\x01",
            "そちらに向かいますね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 6)
    Jump("loc_5EE2")

    label("loc_5DDE")


    #C0169
    ChrTalk(
        0xF,
        (
            "#5P#10106Fそ、そうですか……\x02\x03",

            "#10112Fいえ、気にしないで下さい！\x01",
            "本当にたいした用事じゃ\x01",
            "ありませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xC,
        (
            "#5P#01906Fむ～、仕方ないですね～。\x02\x03",

            "#01901Fロイドさん、気が向いたら\x01",
            "またお姉ちゃんに\x01",
            "声をかけてくださいね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        "#12P#00000Fああ、分かったよ。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_5EE2")

    SetChrSubChip(0xF, 0x0)
    OP_93(0xC, 0x10E, 0x0)
    OP_4C(0xC, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_25_5484 end

    def Function_26_5EF4(): pass

    label("Function_26_5EF4")

    EventBegin(0x0)
    Fade(500)
    OP_68(102260, 800, -94610, 0)
    MoveCamera(48, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, 100450, 0, -95200, 90)
    SetChrSubChip(0x8, 0x2)
    SetChrSubChip(0xA, 0x1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6625")

    #C0172
    ChrTalk(
        0x101,
        (
            "#6P#00005Fワジ、アッバス……\x01",
            "もしかして、飲んでるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xA,
        (
            "#11P#10404F僕らもとりあえずは、\x01",
            "準備は終わったからね。\x02\x03",

            "#10402Fフフ、君も一杯どうだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        (
            "#6P#00006Fおいおい……\x01",
            "明日は作戦なのに大丈夫か？\x02\x03",

            "#00001Fすでにいくつかグラスを\x01",
            "空けちゃったみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x8,
        (
            "#5P#12100F心配するな。\x01",
            "ヴェントスに作らせた\x01",
            "ノンアルコールのカクテルだ。\x02\x03",

            "明日の作戦の進行には\x01",
            "支障はあるまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        (
            "#6P#00006Fあ、ああそうか……\x02\x03",

            "#00000Fまあ、アッバスがそう言うなら\x01",
            "今回は信じてよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xA,
        (
            "#11P#10409Fフフ、１人で飲んでるときでも\x01",
            "信じてくれて構わないんだけど。\x02\x03",

            "#10403F……そうそう、一応君たちにも\x01",
            "言っておいた方がよさそうだな。\x02\x03",

            "#10400F明日の作戦、法王猊下からも\x01",
            "正式に参加の許可が下りたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        "#6P#00005Fあ……そうなのか。\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x8,
        (
            "#5P#12100F隠密活動を主とするメルカバを\x01",
            "大規模な作戦で運用するのは\x01",
            "本来ならば避けるべきだが……\x02\x03",

            "大陸全土の混乱状態を考えれば、\x01",
            "もはや多少の露見は止むを得まい。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#6P#00006Fそうか……\x01",
            "教会の判断に感謝するよ。\x02\x03",

            "#00013F……とにかく、決戦は明日だ。\x01",
            "どうか、改めてよろしく頼む。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xA,
        "#11P#10402Fフフ、了解だリーダー。\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x8,
        "#5P#12102F無論、力添えはさせてもらおう。\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    #C0183
    ChrTalk(
        0xA,
        (
            "#11P#10403Fああ……そういえば。\x01",
            "もう一つだけ、君に伝えて\x01",
            "おくべきことがあったっけ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0184
    ChrTalk(
        0x101,
        "#6P#00005Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x8,
        (
            "#5P#12100F……ワジ。\x01",
            "あの件は、現時点では\x01",
            "秘匿事項に入るはずだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xA,
        (
            "#11P#10405Fあれ、そうだったっけ？\x02\x03",

            "#10409Fフフ、それじゃあ出来るだけ\x01",
            "コッソリ伝えないといけないな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0187
    ChrTalk(
        0x8,
        (
            "#5P#12100F……まあいい、ワジが\x01",
            "そう言うなら仕方あるまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        (
            "#6P#00012Fな、なんだかよく\x01",
            "分からないんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xA,
        (
            "#11P#10404Fフフ、君たちに\x01",
            "大きく関係することさ。\x02\x03",

            "#10402F──気になるなら、\x01",
            "後で甲板で待ち合わせて\x01",
            "話してあげる事も出来るけど？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 1)
    Jump("loc_66B8")

    label("loc_6625")


    #C0190
    ChrTalk(
        0xA,
        (
            "#11P#10404Fもう一つだけ、君に伝えて\x01",
            "おくべきことがあったっけ。\x02\x03",

            "#10402Fフフ、気になるなら\x01",
            "後で甲板で待ち合わせて\x01",
            "話してあげる事も出来るけど？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66B8")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "ワジの誘いを受ける\x01",      # 0
            "やめておく\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6813")

    #C0191
    ChrTalk(
        0x101,
        (
            "#6P#00006F……分かった。\x01",
            "甲板に行けばいいんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xA,
        "#11P#10409Fフフ、決まりだね。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x8,
        (
            "#5P#12100Fワジ、念の為言っておくが\x01",
            "くれぐれもそれ以上のことは……\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xA,
        (
            "#11P#10404Fフフ、分かってる分かってる。\x02\x03",

            "#10400F僕は飲み終わってから行くから\x01",
            "そんなに急がなくてもいいよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 7)
    Jump("loc_6884")

    label("loc_6813")


    #C0195
    ChrTalk(
        0xA,
        (
            "#11P#10405F……そうかい？\x01",
            "それならいいんだけど……\x02\x03",

            "#10404Fフフ、気が変わったら\x01",
            "もう一度声をかけるといい。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_6884")

    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0x8, 0x0)
    EventEnd(0x5)
    Return()

    # Function_26_5EF4 end

    def Function_27_688F(): pass

    label("Function_27_688F")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_6954")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0196
    AnonymousTalk(
        0x101,
        (
            "#00006F（……エリィに、行けなくなることを\x01",
            "  ちゃんと謝っておかないとな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0197
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはエリィに、\x01",
            "約束に行けなくなったことを謝った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 3)
    Jump("loc_6D69")

    label("loc_6954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_6A0E")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0198
    AnonymousTalk(
        0x101,
        (
            "#00006F（……ティオに、行けなくなることを\x01",
            "  ちゃんと謝っておかないとな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0199
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはティオに、\x01",
            "約束に行けなくなったことを謝った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 4)
    Jump("loc_6D69")

    label("loc_6A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_6ACC")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0200
    AnonymousTalk(
        0x101,
        (
            "#00006F（……ランディに、行けなくなることを\x01",
            "  ちゃんと謝っておかないとな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0201
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはランディに、\x01",
            "約束に行けなくなったことを謝った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 5)
    Jump("loc_6D69")

    label("loc_6ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_6B86")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0202
    AnonymousTalk(
        0x101,
        (
            "#00006F（……ノエルに、行けなくなることを\x01",
            "  ちゃんと謝っておかないとな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0203
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはノエルに、\x01",
            "約束に行けなくなったことを謝った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 6)
    Jump("loc_6D69")

    label("loc_6B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_6C3C")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0204
    AnonymousTalk(
        0x101,
        (
            "#00006F（……ワジに、行けなくなることを\x01",
            "  ちゃんと謝っておかないとな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0205
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはワジに、\x01",
            "約束に行けなくなったことを謝った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 7)
    Jump("loc_6D69")

    label("loc_6C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_6CFA")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0206
    AnonymousTalk(
        0x101,
        (
            "#00006F（……リーシャに、行けなくなることを\x01",
            "  ちゃんと謝っておかないとな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0207
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはリーシャに、\x01",
            "約束に行けなくなったことを謝った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AB, 0)
    Jump("loc_6D69")

    label("loc_6CFA")

    SetMessageWindowPos(-1, -1, -1, -1)

    #A0208
    AnonymousTalk(
        0x101,
        (
            "#00003F（……仮眠室で一通り\x01",
            "  明日の準備を済ませてから、\x01",
            "  甲板に向かうとしよう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_6D69")

    Return()

    # Function_27_688F end

    def Function_28_6D6A(): pass

    label("Function_28_6D6A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_739D")
    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, 1420, 0, -92300, 90)
    OP_68(2300, 1000, -92050, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_6E8A")

    #C0209
    ChrTalk(
        0x101,
        (
            "#00005F#6P（そういえば……\x01",
            "  エリィと話す約束をしていたな。）\x02\x03",

            "#00003F（…………………………………）\x02\x03",

            "#00000F（……ど、どうする？\x01",
            "  明日の準備を済ませておくか？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_721D")

    label("loc_6E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_6F46")

    #C0210
    ChrTalk(
        0x101,
        (
            "#00005F#6P（そういえば、ティオが\x01",
            "  相談したい事があるって言ってたな。）\x02\x03",

            "#00003F（…………………………………）\x02\x03",

            "#00000F（……どうする？\x01",
            "  明日の準備を済ませておくか？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_721D")

    label("loc_6F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_7002")

    #C0211
    ChrTalk(
        0x101,
        (
            "#00005F#6P（そういえば、ランディが\x01",
            "  話したい事があるって言ってたな。）\x02\x03",

            "#00003F（…………………………………）\x02\x03",

            "#00000F（……どうする？\x01",
            "  明日の準備を済ませておくか？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_721D")

    label("loc_7002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_70B8")

    #C0212
    ChrTalk(
        0x101,
        (
            "#00005F#6P（そういえば、ノエルが\x01",
            "  頼み事があるって言ってたな。）\x02\x03",

            "#00003F（…………………………………）\x02\x03",

            "#00000F（……どうする？\x01",
            "  明日の準備を済ませておくか？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_721D")

    label("loc_70B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_716C")

    #C0213
    ChrTalk(
        0x101,
        (
            "#00005F#6P（そういえば、ワジが\x01",
            "  気になることを言っていたな。）\x02\x03",

            "#00003F（…………………………………）\x02\x03",

            "#00000F（……どうする？\x01",
            "  明日の準備を済ませておくか？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_721D")

    label("loc_716C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_721D")

    #C0214
    ChrTalk(
        0x101,
        (
            "#00005F#6P（そういえば、リーシャと\x01",
            "  話をする約束をしていたな。）\x02\x03",

            "#00003F（…………………………………）\x02\x03",

            "#00000F（……どうする？\x01",
            "  明日の準備を済ませておくか？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_721D")

    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0215
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "自由行動を終了するとその日が終了し、\x01",
            "イベントが進むので注意が必要です。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【まだ他に用事がある】\x01",                        # 0
            "【自由行動を終了して約束した相手と話す】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_72FD"),
        (1, "loc_7302"),
        (SWITCH_DEFAULT, "loc_7384"),
    )


    label("loc_72FD")

    Jump("loc_7384")

    label("loc_7302")

    StopSound(498, 1500, 70)
    FadeToDark(1500, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0216
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後──ロイドは明日の解放作戦の準備を\x01",
            "一通り済ませてから夜の甲板に出た。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 0)
    NewScene("e440B", 0, 0, 0)
    IdleLoop()
    Jump("loc_7384")

    label("loc_7384")

    OP_5A()
    SetChrPos(0x0, 550, 0, -92390, 270)
    EventEnd(0x5)
    Jump("loc_76D7")

    label("loc_739D")


    #C0217
    ChrTalk(
        0x101,
        (
            "#00005F（……今日は早めに\x01",
            "  休んだほうがいいかな？）\x02\x03",

            "#00003F（一応、明日の作戦前に\x01",
            "  みんなの様子を確認した方が\x01",
            "  いいかもしれないけど……）\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0218
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "仮眠室で休むことを選択すると\x01",
            "そのままその日が終了し、\x01",
            "イベントが進むので注意が必要です。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Sleep(300)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【まだ他に用事がある】\x01",          # 0
            "【自由行動を終了して休む】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_751D")
    Jump("loc_76D7")

    label("loc_751D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76D7")
    EventBegin(0x0)
    Fade(500)
    OP_68(2040, 1000, -91940, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 1300, 0, -92030, 90)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    OP_0D()
    Sleep(300)

    #C0219
    ChrTalk(
        0x101,
        (
            "#00003F#6P（……仮眠室で一通り準備をして、\x01",
            "  今夜はもう休みをとろう。）\x02\x03",

            "#00001F（明日のクロスベル市解放作戦……\x01",
            "  絶対に成功させてみせるぞ！）\x02",
        )
    )

    CloseMessageWindow()
    Sound(100, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0xA, 0x1, 0x8)
    Sleep(500)

    def lambda_7655():
        OP_95(0xFE, 4300, 0, -92030, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7655)
    Sleep(1000)
    StopSound(498, 2000, 70)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    EventEnd(0x3)

    label("loc_76D7")

    TalkEnd(0xFF)
    Return()

    # Function_28_6D6A end

    def Function_29_76DB(): pass

    label("Function_29_76DB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, -150, 0, -88230, 180)
    EventEnd(0x5)
    Return()

    # Function_29_76DB end

    def Function_30_76FB(): pass

    label("Function_30_76FB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    LoadChrToIndex("chr/ch06902.itc", 0x1F)
    LoadChrToIndex("chr/ch06000.itc", 0x20)
    LoadChrToIndex("chr/ch05800.itc", 0x21)
    SoundLoad(943)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7735")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_7735")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7748")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_7748")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_775B")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_775B")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x13, 0x5)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x14)
    OP_70(0x1, 0x24)
    Sleep(1000)
    SetChrName("")

    #A0220
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "こうして──クロスベル市を覆っていた\x01",
            "不可侵の《結界》は消滅した。\x02\x03",

            "ロイドたちは《黒月》のツァオや\x01",
            "レジスタンスのミレイユらと連絡を取り……\x02\x03",

            "さらにソーニャ司令からは\x01",
            "ベルガード門、タングラム門の部隊が\x01",
            "中立を保つという約束を取り付けた。\x02\x03",

            "そして──\x02\x03",

            "夜、メルカバのブリッジに\x01",
            "ケビン神父からの連絡があった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0x11, -3300, 0, 250, 45)
    SetChrPos(0x12, -3800, 0, -1000, 45)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0xC, 3000, -1350, 6960, 45)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x104, 650, 0, -1250, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x103, -1460, 0, -1190, 0)
    SetChrPos(0x109, -700, 0, -1770, 0)
    SetChrPos(0x106, 200, 0, -2200, 0)
    PlayBGM("ed7583", 0)
    Sound(498, 1, 80, 0)
    FadeToBright(1000, 0)
    OP_68(660, 800, 3830, 0)
    MoveCamera(44, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(22500, 2000)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    SetMessageWindowPos(95, 70, -1, -1)
    SetChrName("ケビン神父")

    #A0221
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──そんじゃあ、\x01",
            "領空内に入ったくらいじゃ\x01",
            "攻撃される心配はなさそうか。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0222
    ChrTalk(
        0x105,
        (
            "#10403F#6Pああ、どうやら神機#4Rアイオーン#たちは\x01",
            "都市防衛に集中しているみたいだ。\x02\x03",

            "#10400Fクロスベル市に接近しない限りは\x01",
            "大丈夫だと思うよ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(90, -1, -1, -1)
    SetChrName("ケビン神父")

    #A0223
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "よっしゃ、これで何とか\x01",
            "目処が付きそうやな……\x02\x03",

            "明日の明け方にはそっちに戻る。\x02\x03",

            "タイミングについては\x01",
            "そん時に話すとしようや。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0224
    ChrTalk(
        0x105,
        "#10402F#6Pフフ、了解。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(190, -1, -1, -1)
    SetChrName("リースの声")

    #A0225
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2S……ケビン、代わって。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(250)
    OP_70(0x1, 0x1F)
    Sound(73, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0226
    ChrTalk(
        0x102,
        "#00102F#12Pリースさん……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(160, -1, -1, -1)
    SetChrName("シスター・リース")

    #A0227
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……エリィさん。\x01",
            "ご無事で何よりです。\x02\x03",

            "ロイドさんに、\x01",
            "他の皆さんたちも。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0228
    ChrTalk(
        0x101,
        "#00002F#12Pはは、おかげさまで。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x104,
        (
            "#00309F#12Pいや～、こんな形でリースちゃんと\x01",
            "話せるとは思わなかったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x103,
        (
            "#00202F#12P#Nわたしたちの突入を\x01",
            "助けてくださるんですよね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(140, 70, -1, -1)
    SetChrName("シスター・リース")

    #A0231
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ええ、こちらのメルカバで\x01",
            "都市を防衛する神機#4Rアイオーン#たちを\x01",
            "引き付ける予定です。\x02\x03",

            "猟兵と国防軍の方までは\x01",
            "対処できませんが……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0232
    ChrTalk(
        0x101,
        (
            "#00004F#12P……十分です。\x01",
            "本当に助かります。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x102,
        (
            "#00106F#12Pリースさん、ケビン神父。\x01",
            "何とお礼を言ったらいいか……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(90, -1, -1, -1)
    SetChrName("ケビン神父")

    #A0234
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ま、礼を言うんは\x01",
            "無事成功してからにしてや。\x02\x03",

            "一応、こっちも助っ人を\x01",
            "連れて来るつもりやけど……\x02\x03",

            "それでも、あの人形ども相手じゃ\x01",
            "分が悪すぎるかもしれへん。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0235
    ChrTalk(
        0x103,
        "#00208F#12P#N確かに……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0236
    ChrTalk(
        0x104,
        (
            "#00301F#12Pま、あんまり\x01",
            "無理だけはすんなよな？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(105, -1, -1, -1)
    SetChrName("ケビン神父")

    #A0237
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はは、おおきに。\x02\x03",

            "──ワジ。\x01",
            "そんじゃ、明日の朝にな。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0238
    ChrTalk(
        0x105,
        "#10400F#6Pああ、待ってるよ。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(180, -1, -1, -1)
    SetChrName("シスター・リース")

    #A0239
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "それでは失礼します。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(250)
    OP_70(0x1, 0x1E)
    Sound(73, 0, 100, 0)
    OP_0D()
    Sleep(500)
    Sound(943, 2, 60, 0)
    OP_71(0x1, 0x2F, 0x4C, 0x0, 0x8)
    OP_68(-340, 800, 2640, 2000)
    MoveCamera(40, 22, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(22440, 2000)
    Sleep(1000)
    SetChrFlags(0x13, 0x20)

    def lambda_816A():
        TurnDirection(0x11, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_816A)
    Sleep(50)

    def lambda_817A():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_817A)
    Sleep(50)

    def lambda_818A():
        TurnDirection(0x13, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_818A)
    Sleep(50)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)
    OP_6F(0x79)
    ClearChrFlags(0x13, 0x20)
    OP_24(0x3AF)
    Sound(143, 0, 50, 0)
    Sleep(500)

    #C0240
    ChrTalk(
        0x11,
        (
            "#02501F#5P──ふむ。\x01",
            "厳しい一日になりそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x12,
        (
            "#02106F#6P#Nそうですね……\x01",
            "地上の戦力差についても\x01",
            "大統領側が上回っていますし。\x02\x03",

            "#02101F何と言っても、あの人形たちが\x01",
            "とんでもない強さなんでしょう？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0242
    ChrTalk(
        0x106,
        (
            "#10708F#12Pマイスターによれば、\x01",
            "白い機体の“空間消滅”の力は\x01",
            "使えなくなったそうですが……\x02\x03",

            "#10701Fそれでも基本的な性能は\x01",
            "変わっていないのですよね？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(100)

    #C0243
    ChrTalk(
        0x8,
        (
            "#12100F#5Pうむ、そう思っていた方が\x01",
            "恐らく無難だろう。\x02\x03",

            "白い機体はこの玖#2Rきゅう#号機が、\x01",
            "様子を見ておく必要があるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x105,
        (
            "#10403F#5Pいずれにせよ、都市周辺では\x01",
            "膠着状態になる事が予想される。\x02\x03",

            "#10401F鍵を握るとしたら\x01",
            "潜入を担当する僕らだろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        (
            "#00003F#12Pああ、分かってる。\x02\x03",

            "#00013F……何とか入り込んで\x01",
            "課長やダドリーさんたちと\x01",
            "合流しないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x104,
        (
            "#00306F#11Pしかし、大丈夫なのか？\x02\x03",

            "#00301Fダドリーからの連絡が\x01",
            "途中で切れちまったそうだが。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x1)
    Sleep(200)

    #C0247
    ChrTalk(
        0x9,
        (
            "#02305F#5P多分、通信ターミナルで\x01",
            "強制遮断されたんじゃね？\x02\x03",

            "#02303F特定のエニグマ登録番号だけ\x01",
            "送受信を無効に出来たはずだし。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x2)
    Sleep(100)

    #C0248
    ChrTalk(
        0xC,
        (
            "#01901F#5Pそれじゃあ市内では、\x01",
            "大統領側は通信が使えるけど\x01",
            "わたしたちは使えない……？\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x103,
        (
            "#00203F#12Pはい、通信ターミナルも\x01",
            "押さえる必要がありそうです。\x02\x03",

            "#00208Fオルキスタワー内にありますから\x01",
            "簡単ではなさそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x109,
        (
            "#10101F#12Pいずれにしても……\x01",
            "全ては明日の朝ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x102,
        (
            "#00103F#12Pええ……\x01",
            "『クロスベル市解放作戦』。\x02\x03",

            "#00101Fキーアちゃんを取り戻すためにも\x01",
            "何としても成功させないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        (
            "#00006F#11Pああ……今夜は休んで\x01",
            "英気を養っておく必要がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0253
    ChrTalk(
        0x101,
        (
            "#00004F#5Pみんな、仮眠室もあるから\x01",
            "疲れていたら休んでくれ。\x02\x03",

            "#00000F万全の態勢で……\x01",
            "明日の朝に臨むとしよう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(290, 50, -1, -1)
    SetChrName("一同")

    #A0254
    AnonymousTalk(
        0xFF,
        "#4Sおおっ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(22940, 2000)
    StopSound(498, 2000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearChrFlags(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetScenarioFlags(0x1A5, 2)
    OP_29(0xB0, 0x4, 0x10)
    OP_29(0xB1, 0x4, 0x2)
    OP_29(0xB1, 0x1, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x79), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_885D")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_885D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7A), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8874")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8874")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7B), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_888B")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_888B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7D), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_88A2")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_88A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7C), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_88B9")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_88B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7E), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_88D0")
    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_88D0")

    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7513", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x201), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(498, 1, 80, 0)
    OP_24(0x3AF)
    Sleep(500)
    SetScenarioFlags(0x22, 2)
    NewScene("e302B", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_30_76FB end

    SaveToFile()

Try(main)
