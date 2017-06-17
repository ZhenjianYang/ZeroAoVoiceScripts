from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1220.bin",                # FileName
        "c1220",                    # MapName
        "c1220",                    # Location
        0x0020,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 32, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1220",                  # 0
        "受付嬢トリア",           # 1
        "マッケネン",             # 2
        "レインズ",               # 3
        "グレイス",               # 4
        "ニールセン",             # 5
        "記者ノティシア",         # 6
        "編集長",                 # 7
    ))

    AddCharChip((
        "chr/ch26602.itc",                   # 00
        "chr/ch45100.itc",                   # 01
        "chr/ch28100.itc",                   # 02
        "chr/ch06000.itc",                   # 03
        "chr/ch06002.itc",                   # 04
        "chr/ch26700.itc",                   # 05
        "chr/ch47900.itc",                   # 06
        "chr/ch20202.itc",                   # 07
        "chr/ch26600.itc",                   # 08
        "chr/ch20200.itc",                   # 09
        "chr/ch26702.itc",                   # 0A
    ))

    DeclNpc(5789,    0,       -430,    270,  261,  0x0, 0,   8,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(5099,    0,       60020,   0,    261,  0x0, 0,   5,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-519,    0,       360,     0,    389,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(6420,    0,       55520,   135,  389,  0x0, 0,   1,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(66250,   150,     8420,    270,  389,  0x0, 0,   9,   0,   255, 255, 0,   17,  255,  0)

    DeclEvent(0x0000, 0, 26,  -6.510000228881836,    5.110000133514404,     -0.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.255000114440918,     -2.555000066757202,    0.10000000149011612,   1.0])

    DeclActor(4100,    0,       -520,    1500,    5500,    1800,    -470,    0x007E, 0,  3,  0x0000)
    DeclActor(7270,    0,       54230,   1000,    7270,    1400,    54230,   0x007C, 0,  25, 0x0000)
    DeclActor(-1750,   0,       60890,   1000,    -1750,   1800,    60890,   0x007C, 0,  27, 0x0000)

    ChipFrameInfo(704, 0)                                        # 0

    ScpFunction((
        "Function_0_2C0",          # 00, 0
        "Function_1_370",          # 01, 1
        "Function_2_7B3",          # 02, 2
        "Function_3_863",          # 03, 3
        "Function_4_867",          # 04, 4
        "Function_5_1BE2",         # 05, 5
        "Function_6_1D8F",         # 06, 6
        "Function_7_1F71",         # 07, 7
        "Function_8_2139",         # 08, 8
        "Function_9_2D70",         # 09, 9
        "Function_10_3000",        # 0A, 10
        "Function_11_3396",        # 0B, 11
        "Function_12_3D95",        # 0C, 12
        "Function_13_4CBB",        # 0D, 13
        "Function_14_4E4C",        # 0E, 14
        "Function_15_5008",        # 0F, 15
        "Function_16_5199",        # 10, 16
        "Function_17_53CC",        # 11, 17
        "Function_18_566B",        # 12, 18
        "Function_19_5FB2",        # 13, 19
        "Function_20_672A",        # 14, 20
        "Function_21_6B8E",        # 15, 21
        "Function_22_7F46",        # 16, 22
        "Function_23_81E2",        # 17, 23
        "Function_24_99FA",        # 18, 24
        "Function_25_9E15",        # 19, 25
        "Function_26_9EE6",        # 1A, 26
        "Function_27_A0FD",        # 1B, 27
    ))


    def Function_0_2C0(): pass

    label("Function_0_2C0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_2F8"),
        (1, "loc_304"),
        (2, "loc_310"),
        (3, "loc_31C"),
        (4, "loc_328"),
        (5, "loc_334"),
        (6, "loc_340"),
        (SWITCH_DEFAULT, "loc_34C"),
    )


    label("loc_2F8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_304")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_310")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_31C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_328")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_334")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_340")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_34C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_358")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_36F")

    Return()

    # Function_0_2C0 end

    def Function_1_370(): pass

    label("Function_1_370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38B")
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)

    label("loc_38B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3FB")
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x9, 2160, 0, 60470, 270)
    SetChrPos(0xA, 760, 0, 60470, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F6")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)

    label("loc_3F6")

    Jump("loc_7B2")

    label("loc_3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_487")
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44F")
    SetChrPos(0x9, 66800, 0, 6990, 315)
    SetChrPos(0x8, 66780, 0, 5780, 315)
    SetChrSubChip(0xE, 0x1)
    Jump("loc_482")

    label("loc_44F")

    SetChrPos(0x9, 61280, 150, 340, 0)
    SetChrChipByIndex(0x9, 0xA)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0x8, 51300, 20, -970, 270)

    label("loc_482")

    Jump("loc_7B2")

    label("loc_487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4CB")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xB, 480, 0, 760, 270)
    SetChrPos(0xA, -760, 0, 760, 90)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_7B2")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_50A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x9, 6300, 0, 57090, 180)
    SetChrPos(0xD, 6420, 0, 55520, 0)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xD, 0x10)
    Jump("loc_7B2")

    label("loc_50A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_555")
    SetChrPos(0x9, -1000, 0, 60290, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xB, 6300, 0, 57090, 180)
    SetChrPos(0xA, 6420, 0, 55520, 0)
    Jump("loc_7B2")

    label("loc_555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5B0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57F")
    Jump("loc_5AB")

    label("loc_57F")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xB, 480, 0, 760, 270)
    SetChrPos(0xA, -760, 0, 760, 90)

    label("loc_5AB")

    Jump("loc_7B2")

    label("loc_5B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_5D9")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 2690, 0, 60030, 0)
    Jump("loc_7B2")

    label("loc_5D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_602")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 2690, 0, 60030, 0)
    Jump("loc_7B2")

    label("loc_602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_67E")
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    SetChrPos(0xD, 3490, 20, 490, 135)
    SetChrFlags(0xD, 0x10)
    SetChrPos(0x9, -3840, 0, -1380, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 530, 150, 56890, 180)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -420, 0, 710, 0)
    Jump("loc_7B2")

    label("loc_67E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_68C")
    Jump("loc_7B2")

    label("loc_68C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_69A")
    Jump("loc_7B2")

    label("loc_69A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6D4")
    SetChrPos(0x9, 3350, 0, 56470, 225)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3490, 20, 490, 135)
    SetChrFlags(0xD, 0x10)
    Jump("loc_7B2")

    label("loc_6D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_718")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, 2690, 0, 60030, 270)
    SetChrPos(0xC, 1190, 0, 60030, 90)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_7B2")

    label("loc_718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_74D")
    SetChrPos(0x9, -3840, 0, -1380, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 2690, 0, 60030, 0)
    Jump("loc_7B2")

    label("loc_74D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7B2")
    SetChrPos(0x9, 6420, 0, 55520, 0)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 6300, 0, 57090, 180)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 3380, 0, 60280, 135)
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 2)), scpexpr(EXPR_END)), "loc_7B2")
    OP_93(0xA, 0x0, 0x0)

    label("loc_7B2")

    Return()

    # Function_1_370 end

    def Function_2_7B3(): pass

    label("Function_2_7B3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7CC")
    OP_10(0x0, 0x0)
    OP_10(0x5, 0x1)
    Jump("loc_7D2")

    label("loc_7CC")

    OP_10(0x0, 0x1)
    OP_10(0x5, 0x0)

    label("loc_7D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_7E0")
    ModifyEventFlags(0, 0, 0x80)

    label("loc_7E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_81D")
    SetMapObjFrame(0xFF, "light1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light0", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_81D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_850")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "light1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light0", 0x0, 0x1)

    label("loc_850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_862")
    OP_65(0x0, 0x1)

    label("loc_862")

    Return()

    # Function_2_7B3 end

    def Function_3_863(): pass

    label("Function_3_863")

    Call(0, 4)
    Return()

    # Function_3_863 end

    def Function_4_867(): pass

    label("Function_4_867")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A92")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_986")

    #C0001
    ChrTalk(
        0x8,
        (
            "特務支援課の皆様……\x01",
            "もしかして、当社からの依頼の件で\x01",
            "お越しいただいたのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "実は、担当者が脱線事故の取材で\x01",
            "出かけてしまいまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "申し訳ありませんが、日を改めて\x01",
            "お越しいただけますようお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A8E")

    label("loc_986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_A13")

    #C0004
    ChrTalk(
        0x8,
        (
            "今、２階の編集部では\x01",
            "列車脱線事故の速報対応を\x01",
            "行っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "記者の方々に御用の際は\x01",
            "こちらに伝言をお願い致します。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8E")

    label("loc_A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_A8E")

    #C0006
    ChrTalk(
        0x8,
        (
            "西クロスベル街道で\x01",
            "脱線事故が起こったなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "まさかまた、テロリストの\x01",
            "仕業とかじゃないですよね……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8E")

    TalkEnd(0x8)
    Return()

    label("loc_A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_END)), "loc_CBB")
    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "話をする\x01",                # 0
            "取材内容を報告する\x01",      # 1
            "やめる\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B13")
    TalkEnd(0x8)
    Return()

    label("loc_B13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_B3F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_B52")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_B65")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_B78")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_B8B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_B9E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_BB1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_BC4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_BD7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_BEA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_BFD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C2A")
    TalkEnd(0x8)
    Call(0, 22)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C24")
    Call(0, 23)

    label("loc_C24")

    Return()

    label("loc_C2A")


    #C0008
    ChrTalk(
        0x101,
        (
            "#00005F（おっと、まだ各地の飲食店を\x01",
            "  ６ヶ所以上回ってないな。）\x02\x03",

            "#00003F（今のままじゃ報告できない。\x01",
            "  もう少し頑張らないとな。）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    label("loc_CB6")

    Jump("loc_CC9")

    label("loc_CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC9")
    Call(0, 20)
    Return()

    label("loc_CC9")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_DDE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7A")

    #C0009
    ChrTalk(
        0x8,
        (
            "みなさん、グルメガイドの取材を\x01",
            "どうか頑張ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "美味しい物を食べられるんですし、\x01",
            "楽しみながら進めると\x01",
            "よろしいかと思いますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD9")

    label("loc_D7A")


    #C0011
    ChrTalk(
        0x8,
        "皆様、本当にお疲れ様でした。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "また何かありましたら、\x01",
            "是非ともよろしくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD9")

    Jump("loc_1BDE")

    label("loc_DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E85")

    #C0013
    ChrTalk(
        0x8,
        (
            "レインズ君、どうやら\x01",
            "ジオフロントに潜り込むことができて\x01",
            "そこで難を逃れていたらしいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "ふふ、とにかく無事で\x01",
            "いてくれて本当に良かったです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDE")

    label("loc_E85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_E93")
    Jump("loc_1BDE")

    label("loc_E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_FFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5D")

    #C0015
    ChrTalk(
        0x8,
        (
            "今朝ここに国防軍の兵士が\x01",
            "入ってきた時は本当に驚きました。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "宣言からたった１週間で\x01",
            "事態がここまで大きく動くなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "風雲急を告げるとは、\x01",
            "まさにこのことですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FF8")

    label("loc_F5D")


    #C0018
    ChrTalk(
        0x8,
        (
            "街の様子を見ていると、\x01",
            "変わらず大統領を支持される方も\x01",
            "多いようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "正直、私は戸惑いの方が大きいです。\x01",
            "……この先一体どうなるんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FF8")

    Jump("loc_1BDE")

    label("loc_FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_11BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1125")

    #C0020
    ChrTalk(
        0x8,
        (
            "事件後の復興活動と、\x01",
            "３日後に迫った住民投票。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "この２つの事柄が、\x01",
            "街にかつてない一体感を\x01",
            "生んでいるようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "個人的には、独立を肯定する\x01",
            "議論が異様に白熱している\x01",
            "様子が気になるのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "市民感情を考えると、\x01",
            "仕方ないというか当然だとは\x01",
            "思います。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11B9")

    label("loc_1125")


    #C0024
    ChrTalk(
        0x8,
        (
            "個人的には、独立を肯定する\x01",
            "議論が異様に白熱している\x01",
            "様子が気になるのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "市民感情を考えると、\x01",
            "仕方ないというか当然だとは\x01",
            "思います。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B9")

    Jump("loc_1BDE")

    label("loc_11BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_11CC")
    Jump("loc_1BDE")

    label("loc_11CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1294")

    #C0026
    ChrTalk(
        0x8,
        (
            "グレイスさんたち、昨日はかなり\x01",
            "現場の方に踏み込んで警備隊の方から\x01",
            "お叱りを受けたみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "記者魂は分かりますけど……\x01",
            "心配なので、もう少し身の安全を\x01",
            "考えて欲しいものです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDE")

    label("loc_1294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_144A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13BF")

    #C0028
    ChrTalk(
        0x8,
        (
            "昨日は脱線事故の速報対応で、\x01",
            "各方面への連絡業務も大忙しでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "振り返ると、本年度は例年以上に\x01",
            "号外を出す機会が多いんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "良いニュースで号外が増える分には\x01",
            "一向に構わないんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "事件や事故のニュースばかりだと、\x01",
            "少し気が滅入ってしまいますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1445")

    label("loc_13BF")


    #C0032
    ChrTalk(
        0x8,
        (
            "良いニュースで号外が増える分には\x01",
            "一向に構わないんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "事件や事故のニュースばかりだと、\x01",
            "少し気が滅入ってしまいますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1445")

    Jump("loc_1BDE")

    label("loc_144A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_14D7")

    #C0034
    ChrTalk(
        0x8,
        (
            "今、２階の編集部では\x01",
            "列車脱線事故の速報対応を\x01",
            "行っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "記者の方々に御用の際は\x01",
            "こちらに伝言をお願い致します。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDE")

    label("loc_14D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1557")

    #C0036
    ChrTalk(
        0x8,
        (
            "西クロスベル街道で\x01",
            "脱線事故が起こったなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "まさかまた、テロリストの\x01",
            "仕業とかじゃないですよね……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDE")

    label("loc_1557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1568")
    Call(0, 6)
    Jump("loc_1BDE")

    label("loc_1568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1797")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16DC")

    #C0038
    ChrTalk(
        0x8,
        (
            "２日後に『国家独立の是非』を\x01",
            "テーマとした市民フォーラムが\x01",
            "市民会館で開催されるのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "これは当社が提案を行い、\x01",
            "市の方に共同開催を呼び掛ける形で\x01",
            "実現した企画なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "独立提唱以降、当社には\x01",
            "住民投票の判断基準を求める\x01",
            "読者の声が多く寄せられまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "記事以外にも何かできないか――\x01",
            "ということで提案をさせて頂いたんです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1792")

    label("loc_16DC")


    #C0042
    ChrTalk(
        0x8,
        (
            "独立提唱以降、当社には\x01",
            "住民投票の判断基準を求める\x01",
            "読者の声が多く寄せられまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "記事以外にも何かできないか――\x01",
            "ということで市民フォーラム開催の\x01",
            "提案をさせて頂きました。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1792")

    Jump("loc_1BDE")

    label("loc_1797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1852")

    #C0044
    ChrTalk(
        0x8,
        (
            "グレイスさんとレインズ君、\x01",
            "急に買い物が必要になったって言って\x01",
            "百貨店に向かったみたいですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "まさかそれが原因で本会議に遅刻、\x01",
            "……なんてことはありませんよね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDE")

    label("loc_1852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1863")
    Call(0, 7)
    Jump("loc_1BDE")

    label("loc_1863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_18E8")

    #C0046
    ChrTalk(
        0x8,
        (
            "とうとう明日から\x01",
            "通商会議が始まりますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "記者の皆さんも\x01",
            "準備に大忙しという感じで、\x01",
            "緊張感が伝わって来ます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDE")

    label("loc_18E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1AC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A1C")

    #C0048
    ChrTalk(
        0x8,
        (
            "レインズ君、何でも今日は\x01",
            "遺跡の調査に付き添うそうなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "従順な助手がいなくて残念って\x01",
            "グレイスさんがぼやいてましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "よく考えると、レインズ君って\x01",
            "まだ今年入社したばかりなんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "なのにすっかり\x01",
            "色々と頼りにされていて\x01",
            "本当に立派な事だと思いますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1ABC")

    label("loc_1A1C")


    #C0052
    ChrTalk(
        0x8,
        (
            "みんな忘れがちなんですけど\x01",
            "レインズ君って、まだ今年\x01",
            "入社したばかりなんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "なのにすっかり\x01",
            "色々と頼りにされていて\x01",
            "本当に立派な事だと思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ABC")

    Jump("loc_1BDE")

    label("loc_1AC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1BDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B63")

    #C0054
    ChrTalk(
        0x8,
        (
            "あら、お久しぶりです。\x01",
            "特務支援課の皆さんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "クロスベル通信社へようこそ。\x01",
            "何か御用があれば、\x01",
            "遠慮なく仰ってくださいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BDE")

    label("loc_1B63")


    #C0056
    ChrTalk(
        0x8,
        (
            "ふふ、皆さんが活動を\x01",
            "再開したとなったら\x01",
            "グレイスさんも喜びますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "何か御用があれば、\x01",
            "遠慮なく仰ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BDE")

    TalkEnd(0x8)
    Return()

    # Function_4_867 end

    def Function_5_1BE2(): pass

    label("Function_5_1BE2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1C8C")

    #C0058
    ChrTalk(
        0xFE,
        (
            "レインズ君、どうやら\x01",
            "ジオフロントに潜り込むことができて\x01",
            "そこで難を逃れていたらしいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "ふふ、とにかく無事で\x01",
            "いてくれて本当に良かったです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D8B")

    label("loc_1C8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1D26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CAB")
    TalkEnd(0xFE)
    Call(0, 18)
    Return()

    label("loc_1CAB")


    #C0060
    ChrTalk(
        0xFE,
        (
            "レインズ君、本当に無茶を\x01",
            "していなければいいのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "とにかく、無事で\x01",
            "いてくれていることを祈っています。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D8B")

    label("loc_1D26")


    #C0062
    ChrTalk(
        0xFE,
        (
            "あ、皆さん。\x01",
            "こちら側に入って来ちゃ\x01",
            "ダメですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "御用ならカウンター越しに\x01",
            "仰ってください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D8B")

    TalkEnd(0xFE)
    Return()

    # Function_5_1BE2 end

    def Function_6_1D8F(): pass

    label("Function_6_1D8F")

    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ECD")

    #C0064
    ChrTalk(
        0xD,
        (
            "う～ん、そっかぁ。\x01",
            "今日こそは思ってたんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "ちなみに本日は\x01",
            "マインツ鉱山町の方なので\x01",
            "帰りも遅くなるかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "やはり確実にお会いするには\x01",
            "伝言を残した方が\x01",
            "よろしいかと思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xD,
        "まあ、確かにそうよね。\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xD,
        (
            "それじゃあ、\x01",
            "伝言お願いできるかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        "はい、かしこまりました。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F6C")

    label("loc_1ECD")


    #C0070
    ChrTalk(
        0x8,
        (
            "では改めて、ご滞在先を\x01",
            "お聞きしてよろしいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xD,
        "ええ、東通りの龍老飯店よ。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xD,
        (
            "連絡をもらえれば、\x01",
            "すぐに駆けつけるって\x01",
            "伝えておいて頂けるかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F6C")

    OP_4C(0xD, 0xFF)
    Return()

    # Function_6_1D8F end

    def Function_7_1F71(): pass

    label("Function_7_1F71")

    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20BB")

    #C0073
    ChrTalk(
        0xD,
        (
            "う～ん、残念。\x01",
            "じゃあニールセンさんは\x01",
            "外出中なのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "すみません、何分基本的に\x01",
            "通信社におられることの方が\x01",
            "少ない方でして。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            "今日は友人に会いに行くと\x01",
            "仰っていましたが、\x01",
            "伝言をお承りしましょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xD,
        (
            "いえ、大丈夫よ。\x01",
            "ただの世間話に時間を\x01",
            "割いてもらうのも悪いしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xD,
        "またの機会にしておくわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2134")

    label("loc_20BB")


    #C0078
    ChrTalk(
        0xD,
        (
            "それはそれとして、\x01",
            "編集長に挨拶をしたいんだけど\x01",
            "今大丈夫かしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "はい、只今連絡しますので\x01",
            "少々お待ちください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2134")

    OP_4C(0xD, 0xFF)
    Return()

    # Function_7_1F71 end

    def Function_8_2139(): pass

    label("Function_8_2139")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_214A")
    Jump("loc_2D6C")

    label("loc_214A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2158")
    Jump("loc_2D6C")

    label("loc_2158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_21EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2173")
    Call(0, 9)
    Jump("loc_21E5")

    label("loc_2173")

    OP_4B(0xA, 0xFF)

    #C0080
    ChrTalk(
        0xB,
        (
            "#02100Fそれじゃ、レインズ君は\x01",
            "引き続き国防軍への交渉をお願いね。\x02\x03",

            "何かあったら、すぐに連絡するのよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)

    label("loc_21E5")

    Jump("loc_2D6C")

    label("loc_21EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_21F8")
    Jump("loc_2D6C")

    label("loc_21F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2295")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2217")
    TalkEnd(0xFE)
    Call(0, 19)
    Return()

    label("loc_2217")


    #C0081
    ChrTalk(
        0xB,
        (
            "#02100Fロイド君たち、\x01",
            "くれぐれも気を付けてね。\x02\x03",

            "#02109Fそしてまた、\x01",
            "特務支援課が活躍する\x01",
            "記事を書かせてちょうだい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D6C")

    label("loc_2295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_24CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2435")

    #C0082
    ChrTalk(
        0xB,
        (
            "#02100Fああ、ロイド君たち。\x01",
            "昨日は夜遅くまでお疲れ様。\x02\x03",

            "#02101Fあれから……\x01",
            "ヴァルド君のことは何か分かった？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#00003Fああいえ……\x02\x03",

            "#00001F今朝イグニスにも行ったんですが、\x01",
            "何も情報は得られませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xB,
        (
            "#02103Fそう……\x02\x03",

            "#02102Fまあ、こちらでも心当たりは\x01",
            "色々と当たらせてもらうわ。\x02\x03",

            "#02100Fそれからワジ君も……\x01",
            "あまり考えすぎないようにね。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x105,
        "#10304Fふふ、ご心配ありがとう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 1)
    Jump("loc_24C8")

    label("loc_2435")


    #C0086
    ChrTalk(
        0xB,
        (
            "#02101Fそれにしても……\x01",
            "蒼い花のことも心配ね。\x02\x03",

            "#02103Fもし、あのヨアヒム以外に\x01",
            "薬を作れる人間がいたとしたら……\x01",
            "かなり厄介な話になりそうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24C8")

    Jump("loc_2D6C")

    label("loc_24CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_24DB")
    Jump("loc_2D6C")

    label("loc_24DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2885")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_273D")

    #C0087
    ChrTalk(
        0xB,
        (
            "#02104Fふう、朝の一服は落ち着くわね～。\x02\x03",

            "#02102Fよかったらロイド君たちもどう？\x01",
            "といっても、ただの缶コーヒーだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#00000Fああいえ、\x01",
            "気持ちだけ頂いておきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xB,
        (
            "#02102Fあらそう？\x01",
            "ふふ、まあいいけど。\x02\x03",

            "#02104Fとりあえず、\x01",
            "昨日は《幻獣》退治の方、\x01",
            "お疲れ様だったみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x102,
        "#00105F確かにそうですけど……\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x103,
        "#00206F……相変わらず耳が早いですね。\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xB,
        (
            "#02109Fまあね～、こちとらそれを\x01",
            "飯の種にしているわけだし。\x02\x03",

            "#02100F何はともあれ、くれぐれも\x01",
            "怪我のないように頑張ってね。\x02\x03",

            "#02102F何といっても、\x01",
            "お互い身体が資本なんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        "#00000Fええ、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 2)
    Jump("loc_2880")

    label("loc_273D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27E6")

    #C0094
    ChrTalk(
        0xB,
        (
            "#02103Fそれにしても《幻獣》ねぇ。\x01",
            "よく分からないけど、\x01",
            "奇妙としか言い様がないわ。\x02\x03",

            "#02100Fロイド君たちも、くれぐれも\x01",
            "怪我のないように頑張ってね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2863")

    label("loc_27E6")


    #C0095
    ChrTalk(
        0xB,
        (
            "#02100Fあ、そうそう。\x01",
            "一押しグルメがまとまったら\x01",
            "受付の方に報告を頼むわね。\x02\x03",

            "#02109Fそれじゃ、よろしく頼んだわよ～♪\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)

    label("loc_2863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2880")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2880")
    ClearScenarioFlags(0x0, 2)

    label("loc_2880")

    Jump("loc_2D6C")

    label("loc_2885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2893")
    Jump("loc_2D6C")

    label("loc_2893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_28A1")
    Jump("loc_2D6C")

    label("loc_28A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_28AF")
    Jump("loc_2D6C")

    label("loc_28AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2953")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28CA")
    Call(0, 10)
    Jump("loc_294E")

    label("loc_28CA")


    #C0096
    ChrTalk(
        0xB,
        (
            "#02102Fあ、これって今話題の\x01",
            "《雪華堂》のヤツじゃないですか。\x02\x03",

            "#02109Fありがとうございます。\x01",
            "一度、食べてみたかったんですよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_294E")

    Jump("loc_2D6C")

    label("loc_2953")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2D63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CD2")

    #C0097
    ChrTalk(
        0xB,
        (
            "#02102Fあ、ロイド君たち。\x01",
            "昨日ぶりね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#00000Fはは、そうですね。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#00100Fあれから\x01",
            "黒月の調査はどうでしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xB,
        (
            "#02106Fまあ、ぼちぼちってところね。\x02\x03",

            "#02100Fその他の入札業者についても\x01",
            "一通り調べてみたけど……\x02\x03",

            "おそらく余程の事がない限り、\x01",
            "あの一帯はこのまま\x01",
            "黒月のものになると思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x109,
        "#10103Fそうですか……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xB,
        (
            "#02106Fま、これ以上のことは\x01",
            "実際に蓋が開かれてみないと\x01",
            "何とも言えないけどね。\x02\x03",

            "#02100Fというわけで、あたしの方は\x01",
            "今日は溜めていた仕事を\x01",
            "まとめて片付ける予定なの。\x02\x03",

            "#02102Fそうそう、特務支援課の\x01",
            "再始動についてはバッチリ\x01",
            "記事にさせてもらうから。\x02\x03",

            "#02109F使って欲しい写真とか\x01",
            "コメントがもしあったら、\x01",
            "今の内に言ってちょうだいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x105,
        (
            "#10303Fフフ、なら僕からは\x01",
            "ホストクラブで使っている\x01",
            "写真でも提供しようかな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x105, 500)
    Sleep(200)

    #C0104
    ChrTalk(
        0x101,
        "#00006F……お願いだから止めてくれ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 3)
    Jump("loc_2D5E")

    label("loc_2CD2")


    #C0105
    ChrTalk(
        0xB,
        (
            "#02106Fふう、だけどこんな日に限って\x01",
            "レインズ君が外出中だなんてね。\x02\x03",

            "雑用をうんと\x01",
            "押し付けようと思ってたのに……\x01",
            "残念でしょうがないわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D5E")

    Jump("loc_2D6C")

    label("loc_2D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2D6C")

    label("loc_2D6C")

    TalkEnd(0xFE)
    Return()

    # Function_8_2139 end

    def Function_9_2D70(): pass

    label("Function_9_2D70")

    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xB, 0x0, 0)
    TurnDirection(0xA, 0x0, 0)

    #C0106
    ChrTalk(
        0xB,
        (
            "#02101Fあ、ロイド君たち。\x01",
            "大統領演説は当然見たわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#00001Fはい、連絡をくださって\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x102,
        (
            "#00101Fグレイスさんたちは\x01",
            "これからどうするんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xB,
        (
            "#02103Fええ、何はともあれ\x01",
            "とにかく取材活動に奔走するわ。\x02\x03",

            "#02101F改めて国防軍の方に\x01",
            "問い合わせて具体的な話を\x01",
            "引き出すのはもちろん……\x02\x03",

            "街に出て市民の声を集めたり、ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        (
            "あとは国外メディアへの\x01",
            "応対と反応調査ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xA,
        (
            "今は２階にある国際通信器も\x01",
            "フル稼働の状態です。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x103,
        "#00203Fなるほど、お忙しそうですね。\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xB,
        (
            "#02104Fまあね～。\x01",
            "そちらも色々あると思うけど\x01",
            "お互い出来ることを尽くしましょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#00000Fええ、了解です。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 2)
    OP_93(0xB, 0x10E, 0x0)
    OP_93(0xA, 0x5A, 0x0)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_2D70 end

    def Function_10_3000(): pass

    label("Function_10_3000")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0115
    ChrTalk(
        0xB,
        (
            "#02109Fふふ、ニールセンさん。\x01",
            "ようやくお会いできましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xC,
        "ええ、私も心待ちでした。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xC,
        (
            "そういえば、\x01",
            "編集長から伺っていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xC,
        (
            "この３年で、グレイス君がとても\x01",
            "たくましくなってくれたってね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    #C0119
    ChrTalk(
        0xB,
        (
            "#02109Fそんな、私なんてまだまだですから。\x02\x03",

            "#02104Fいつもやりたいように\x01",
            "やっているだけっていうか……\x01",
            "好きなことしかしていないっていうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xC,
        (
            "はは、そうやって\x01",
            "仕事を楽しめていることが\x01",
            "何よりじゃないですか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3264")

    #C0121
    ChrTalk(
        0x101,
        (
            "#00000F（グレイスさん……\x01",
            "  ニールセンさんの前だと\x01",
            "  いつもと違う感じがするな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x102,
        (
            "#00102F（ふふ、そうね。\x01",
            "  ちょっと珍しい光景かも。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_338A")

    label("loc_3264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_END)), "loc_3308")

    #C0123
    ChrTalk(
        0x101,
        (
            "#00000F（グレイスさん、なんだか\x01",
            "  いつもと違う感じがするな。）\x02\x03",

            "#00003F（確かニールセンさんって言ったっけ。\x01",
            "  どうやら知り合いみたいだけど……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_338A")

    label("loc_3308")


    #C0124
    ChrTalk(
        0x101,
        (
            "#00000F（グレイスさん、なんだか\x01",
            "  いつもと違う感じがするな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x102,
        (
            "#00100F（ええ、確かにね。\x01",
            "  隣にいるのは誰なのかしら？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_338A")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x148, 1)
    Return()

    # Function_10_3000 end

    def Function_11_3396(): pass

    label("Function_11_3396")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3465")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33B4")
    Call(0, 13)
    Jump("loc_3460")

    label("loc_33B4")


    #C0126
    ChrTalk(
        0xFE,
        (
            "大樹の取材はグレイス先輩に任せて\x01",
            "僕たちは政府の動向を\x01",
            "徹底的に追いかける予定です。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "２大国が動く前に\x01",
            "どこまでの体制を築けるか……\x01",
            "見逃すわけにはいきませんからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3460")

    Jump("loc_3D91")

    label("loc_3465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3473")
    Jump("loc_3D91")

    label("loc_3473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_34F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_348E")
    Call(0, 9)
    Jump("loc_34EF")

    label("loc_348E")

    OP_4B(0xB, 0xFF)

    #C0128
    ChrTalk(
        0xFE,
        "ええ、了解です。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "グレイスさんこそ国防軍には\x01",
            "あまり突込み過ぎないでくださいね。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)

    label("loc_34EF")

    Jump("loc_3D91")

    label("loc_34F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3502")
    Jump("loc_3D91")

    label("loc_3502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3590")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3521")
    TalkEnd(0xFE)
    Call(0, 19)
    Return()

    label("loc_3521")


    #C0130
    ChrTalk(
        0xFE,
        (
            "……《赤い星座》は\x01",
            "尋常じゃない相手と聞きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "皆さん、マインツに\x01",
            "向かわれる際はお気をつけて。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D91")

    label("loc_3590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3618")

    #C0132
    ChrTalk(
        0xFE,
        (
            "列車事故の方はとりあえず\x01",
            "大きな混乱にならずに幸いでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "あとは例の薬のルートが\x01",
            "解明できればいいんですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D91")

    label("loc_3618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3626")
    Jump("loc_3D91")

    label("loc_3626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_36AC")

    #C0134
    ChrTalk(
        0xFE,
        "今日は朝から編集会議なんです。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "最近は大きなニュース続きで\x01",
            "議論も熱くなることが多いので、\x01",
            "気合いが入りますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D91")

    label("loc_36AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_36BA")
    Jump("loc_3D91")

    label("loc_36BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_36C8")
    Jump("loc_3D91")

    label("loc_36C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_36D6")
    Jump("loc_3D91")

    label("loc_36D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_36E4")
    Jump("loc_3D91")

    label("loc_36E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_36F2")
    Jump("loc_3D91")

    label("loc_36F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3D91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D27")

    #C0136
    ChrTalk(
        0xFE,
        (
            "あの人が我が社の伝説……\x01",
            "やっぱり偉大な人は\x01",
            "佇まいからして違うなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "……っと、いけないいけない。\x01",
            "早く資料を揃えてデスクに戻らないと。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)
    Sleep(200)

    #C0138
    ChrTalk(
        0xFE,
        "あ、皆さんは特務支援課の。\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#00005Fあなたは確か、グレイスさんと\x01",
            "よく一緒に行動している……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        "ええ、記者のレインズと言います。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "……といっても、\x01",
            "最近はカメラマンとして\x01",
            "定着しつつあるんですけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "はあ、周りにも僕は記者だと\x01",
            "言っているんですが、ぶつぶつ……\x02",
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

    #C0143
    ChrTalk(
        0x102,
        "#00106Fい、色々あるんですね……\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、理想と現実の\x01",
            "ギャップってヤツだね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AD8")

    #C0145
    ChrTalk(
        0x101,
        (
            "#00000Fあの、ちなみに今、\x01",
            "グレイスさんはこちらに？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "ああいえ、グレイス先輩なら\x01",
            "今日は取材に出かけている所です。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "何でも今日の取材は\x01",
            "１人の方が動きやすいとかで……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "そして代わりに、\x01",
            "先輩の仕事のいくつかが\x01",
            "僕に押し付けられている状況なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "まあ、ヘルプでも何でも\x01",
            "記事を書けるのは嬉しいんですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C01")

    label("loc_3AD8")


    #C0150
    ChrTalk(
        0x101,
        (
            "#00000Fあの、ちなみにさっき\x01",
            "グレイスさんと会ったんですが\x01",
            "今日は一緒じゃないんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "ええ、何でも今日の取材は\x01",
            "１人の方が動きやすいとかで……\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "そして代わりに、\x01",
            "先輩の仕事のいくつかが\x01",
            "僕に押し付けられている状況なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "まあ、ヘルプでも何でも\x01",
            "記事を書けるのは嬉しいんですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C01")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0154
    ChrTalk(
        0xFE,
        (
            "ああ、こうしている間にも\x01",
            "締め切りの時間が……！\x02",
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

    #C0155
    ChrTalk(
        0x109,
        "#10100Fな、何だかお邪魔でしたね。\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x102,
        "#00100Fあの、頑張ってくださいね。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_93(0xFE, 0x0, 0x1F4)
    SetScenarioFlags(0x13E, 2)
    Return()

    label("loc_3D27")


    #C0157
    ChrTalk(
        0xFE,
        (
            "えっと、あと１つ\x01",
            "記事に必要な資料はどこだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "うう、こうしている間にも\x01",
            "締め切りの時間が……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D91")

    TalkEnd(0xFE)
    Return()

    # Function_11_3396 end

    def Function_12_3D95(): pass

    label("Function_12_3D95")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DB3")
    Call(0, 13)
    Jump("loc_3E2F")

    label("loc_3DB3")


    #C0159
    ChrTalk(
        0xFE,
        (
            "とにかく今は、足を使って情報を\x01",
            "なるべく多くかき集めねえとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "一仕事終えたからって、\x01",
            "一服なんざしてる暇もねえぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E2F")

    Jump("loc_4CB7")

    label("loc_3E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3F42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E53")
    TalkEnd(0xFE)
    Call(0, 18)
    Return()

    label("loc_3E53")


    #C0161
    ChrTalk(
        0xFE,
        (
            "俺たちはこれから\x01",
            "グレイスから得た情報を元に\x01",
            "速報の準備に入る所なんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "情けねえ話、今の体制下じゃあ\x01",
            "大統領の不正を記事にすることが\x01",
            "出来ねえんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "ってなわけで、\x01",
            "アンタらの突入作戦が\x01",
            "うまく行くことを信じてるからな！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB7")

    label("loc_3F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_40E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_403D")

    #C0164
    ChrTalk(
        0xFE,
        (
            "おいおいおい……\x01",
            "いくら何でもこの展開は\x01",
            "急すぎんだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "正直これから何が起きても\x01",
            "不思議じゃねえが……\x01",
            "ただ騒ぎ立てても仕方がねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "とにかく、こうなった以上は\x01",
            "最悪の状況を想定しつつ、\x01",
            "やることをやるしかねえな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_40E3")

    label("loc_403D")


    #C0167
    ChrTalk(
        0xFE,
        (
            "正直、これから何が起きても\x01",
            "不思議じゃねえが……\x01",
            "ただ騒ぎ立てても仕方がねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "とにかく、こうなった以上は\x01",
            "最悪の状況を想定しつつ、\x01",
            "やることをやるしかねえな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40E3")

    Jump("loc_4CB7")

    label("loc_40E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_41AE")
    OP_4B(0xD, 0xFF)

    #C0169
    ChrTalk(
        0xFE,
        (
            "この間の襲撃は帝国の\x01",
            "陰謀だって噂が、既に市民の間に\x01",
            "浸透しているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "確かに自然な論理ですが、\x01",
            "決め付けるのも危険っつうか……\x01",
            "何とか真相を掴めませんかねぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    Jump("loc_4CB7")

    label("loc_41AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_41BC")
    Jump("loc_4CB7")

    label("loc_41BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_42CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_426B")

    #C0171
    ChrTalk(
        0xFE,
        (
            "どうやら警備隊は\x01",
            "かなり厳しい状況らしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "そんで、このまま占拠が続けば\x01",
            "最終的には帝国軍が介入ってか……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        "やれやれ、笑えねえ話だぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_42C6")

    label("loc_426B")


    #C0174
    ChrTalk(
        0xFE,
        (
            "このまま占拠が続けば\x01",
            "最終的には帝国軍が介入ってか……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        "やれやれ、笑えねえ話だぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_42C6")

    Jump("loc_4CB7")

    label("loc_42CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4415")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_439E")

    #C0176
    ChrTalk(
        0xFE,
        (
            "ふう、速報記事の編集ってヤツは\x01",
            "毎度毎度、マジで体力を使うぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "２０代の頃はなんてことなかったが……\x01",
            "最近はきつく感じることも多くてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        "まったく、歳は取りたくねえモンだ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4410")

    label("loc_439E")


    #C0179
    ChrTalk(
        0xFE,
        (
            "ま、といっても俺はまだ３０代だ。\x01",
            "むしろ働き盛りは\x01",
            "これからだ、つってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        "泣き言ばかり言ってられねえぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_4410")

    Jump("loc_4CB7")

    label("loc_4415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4423")
    Jump("loc_4CB7")

    label("loc_4423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4527")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4506")

    #C0181
    ChrTalk(
        0xFE,
        "スパー。\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "さてと、会議の前に\x01",
            "改めて資料に目を通しておくか。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "なんつっても、今日も\x01",
            "議題の中心は国家独立についてだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "色んな要素を\x01",
            "事前に頭に叩き込んでおかねえと\x01",
            "議論も尽くせえからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4522")

    label("loc_4506")


    #C0185
    ChrTalk(
        0xFE,
        "さて、資料、資料と……\x02",
    )

    CloseMessageWindow()

    label("loc_4522")

    Jump("loc_4CB7")

    label("loc_4527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4728")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_468E")

    #C0186
    ChrTalk(
        0xFE,
        (
            "政治・経済を始めとする社会問題から\x01",
            "文化・芸能に関する娯楽情報まで……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "ウチの記者たちが抱える案件は、\x01",
            "呆れるほどにバラエティー豊かでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "これがもっと大きな通信社なら\x01",
            "それぞれ専門分野に特化して\x01",
            "仕事を担当分けするもんなんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "ウチは少数精鋭の機動力重視でな。\x01",
            "１人であらゆる分野を\x01",
            "カバーすんのが基本ってわけだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4723")

    label("loc_468E")


    #C0190
    ChrTalk(
        0xFE,
        (
            "今日は午後から取材が\x01",
            "３件ほど入ってるんだが……\x01",
            "コラムの仕事もちぃと残ってんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "ま、こんなのは暇のある内に\x01",
            "パッパと片付けちまわねえとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4723")

    Jump("loc_4CB7")

    label("loc_4728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_489D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4825")

    #C0192
    ChrTalk(
        0xFE,
        (
            "本会議の現場に\x01",
            "直接入れる記者の数には\x01",
            "各社ごとに制限があってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "ウチからは、\x01",
            "グレイスとレインズの奴を\x01",
            "送り込むことになってんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "ま、ここに残ったメンバーは\x01",
            "グレイスたちの連絡を待って\x01",
            "速報の準備対応って所だな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4898")

    label("loc_4825")


    #C0195
    ChrTalk(
        0xFE,
        (
            "グレイスとレインズを\x01",
            "組ませた時の取材力には\x01",
            "定評があるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "ま、あいつらなら\x01",
            "うまくやってくれるだろ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4898")

    Jump("loc_4CB7")

    label("loc_489D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_49D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4961")

    #C0197
    ChrTalk(
        0xFE,
        (
            "今さっきグレイスとレインズが\x01",
            "撮って来た写真を現像した所でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "ほれ、どれもなかなか\x01",
            "うまく撮れてやがるだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "さて、号外に使う\x01",
            "写真はどれにすっかねっと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_49D3")

    label("loc_4961")


    #C0200
    ChrTalk(
        0xFE,
        (
            "こいつとそいつ、あとは\x01",
            "その右のヤツも良さそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "絞り込んだら最後に\x01",
            "編集長チェックをもらって、っと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49D3")

    Jump("loc_4CB7")

    label("loc_49D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4B82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ACF")

    #C0202
    ChrTalk(
        0xFE,
        (
            "へっ、あれだけ黒月が\x01",
            "動いてたっつうのに、結局最後は\x01",
            "クリムゾン商会ってか。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "あそこはそもそも、実態が掴めん上に\x01",
            "コネクションも底が知れねえからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "ま、とにかくしばらくは\x01",
            "黙って様子を見るしかなさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4B7D")

    label("loc_4ACF")


    #C0205
    ChrTalk(
        0xFE,
        (
            "明日にはいよいよ\x01",
            "通商会議も始まるっつうのに……\x01",
            "キナ臭えったらありゃしねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "ま、考えてもはじまらねえ。\x01",
            "とにかく今は、通商会議関連の\x01",
            "記事をまとめちまわねえとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B7D")

    Jump("loc_4CB7")

    label("loc_4B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4C33")

    #C0207
    ChrTalk(
        0xFE,
        (
            "すぱー……\x01",
            "黒月がルバーチェ跡を、か。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "ま、そうなったらそうなったで\x01",
            "帝国も黙っちゃいないだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "やれやれ……徐々に\x01",
            "キナ臭くなって来やがったな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB7")

    label("loc_4C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4CB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C4E")
    Call(0, 15)
    Jump("loc_4CB7")

    label("loc_4C4E")


    #C0210
    ChrTalk(
        0xFE,
        "いやぁ、わざわざすみませんね。\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "これはバウムクーヘンですか。\x01",
            "はは、相変わらずお好きなんですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CB7")

    TalkEnd(0xFE)
    Return()

    # Function_12_3D95 end

    def Function_13_4CBB(): pass

    label("Function_13_4CBB")

    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0212
    ChrTalk(
        0x9,
        (
            "おい、レインズ。\x01",
            "カメラの準備はできたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xA,
        "ええ、バッチリです。\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x9,
        (
            "よし、じゃあさっそく\x01",
            "オルキスタワー方面の\x01",
            "取材に向かうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x9,
        (
            "グレイスに負けねえように\x01",
            "俺たちも気張ってくぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xA,
        "ええ、了解です！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 3)), scpexpr(EXPR_END)), "loc_4E36")

    #C0217
    ChrTalk(
        0x101,
        (
            "#00000F（レインズさん、記者の仕事も\x01",
            "  普通に再開してるんだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x102,
        (
            "#00104F（一石二鳥なんでしょうけど……\x01",
            "  何ていうか凄いバイタリティよね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E36")

    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_13_4CBB end

    def Function_14_4E4C(): pass

    label("Function_14_4E4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4E5D")
    Jump("loc_5004")

    label("loc_4E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4E6B")
    Jump("loc_5004")

    label("loc_4E6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4E79")
    Jump("loc_5004")

    label("loc_4E79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4E87")
    Jump("loc_5004")

    label("loc_4E87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4E95")
    Jump("loc_5004")

    label("loc_4E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4EA3")
    Jump("loc_5004")

    label("loc_4EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4EB1")
    Jump("loc_5004")

    label("loc_4EB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4EBF")
    Jump("loc_5004")

    label("loc_4EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4ECD")
    Jump("loc_5004")

    label("loc_4ECD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4F5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EE8")
    Call(0, 10)
    Jump("loc_4F5A")

    label("loc_4EE8")


    #C0219
    ChrTalk(
        0xFE,
        (
            "はは、流石はグレイス君ですね。\x01",
            "既にチェック済みでしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "約束します――\x01",
            "一口でほっぺがとけ落ちますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F5A")

    Jump("loc_5004")

    label("loc_4F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4F6D")
    Jump("loc_5004")

    label("loc_4F6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5004")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F88")
    Call(0, 15)
    Jump("loc_5004")

    label("loc_4F88")


    #C0221
    ChrTalk(
        0xFE,
        (
            "そうそう、皆さんに\x01",
            "お土産をお渡ししているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "共和国でいいお店を見つけましてね。\x01",
            "ふふ、きっと気に入りますよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5004")

    TalkEnd(0xFE)
    Return()

    # Function_14_4E4C end

    def Function_15_5008(): pass

    label("Function_15_5008")

    OP_4B(0xC, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0223
    ChrTalk(
        0x9,
        (
            "いや～、しかし\x01",
            "本当にお久しぶりですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x9,
        (
            "最後にここへ来て頂いてから、\x01",
            "もう３年になりますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xC,
        "ええ、丁度そのくらいかと。\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xC,
        (
            "とりあえず、しばらくの間\x01",
            "こちらには特別相談員という形で\x01",
            "出入りさせて頂きますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xC,
        (
            "面倒をおかけしますが、\x01",
            "どうぞよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x9,
        "ああいや、滅相もないですよ。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x9,
        (
            "何かあれば、どんなことでも\x01",
            "遠慮なく言い付けてやって下さい。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_15_5008 end

    def Function_16_5199(): pass

    label("Function_16_5199")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_51AA")
    Jump("loc_53C8")

    label("loc_51AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_525E")
    OP_4B(0x9, 0xFF)

    #C0230
    ChrTalk(
        0xFE,
        (
            "ま、事実がどうあれ、\x01",
            "とにかく帝国が襲撃を\x01",
            "認めることはないでしょうしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "この状況に対して\x01",
            "次に帝国がどう出るか……\x01",
            "それを見守るしかないと思うわよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_53C8")

    label("loc_525E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_526C")
    Jump("loc_53C8")

    label("loc_526C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_527A")
    Jump("loc_53C8")

    label("loc_527A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_52DF")

    #C0232
    ChrTalk(
        0xFE,
        (
            "さてと、編集部も一層\x01",
            "慌しくなってきたみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        "そろそろ、お暇しないとね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_53C8")

    label("loc_52DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5365")

    #C0234
    ChrTalk(
        0xFE,
        (
            "２階ではさっそく速報の\x01",
            "対応に当たっているみたいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "何ていうか、この騒々しさは\x01",
            "どこの通信社も同じって感じね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53C8")

    label("loc_5365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5376")
    Call(0, 6)
    Jump("loc_53C8")

    label("loc_5376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5384")
    Jump("loc_53C8")

    label("loc_5384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5392")
    Jump("loc_53C8")

    label("loc_5392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_53A3")
    Call(0, 7)
    Jump("loc_53C8")

    label("loc_53A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_53B1")
    Jump("loc_53C8")

    label("loc_53B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_53BF")
    Jump("loc_53C8")

    label("loc_53BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_53C8")

    label("loc_53C8")

    TalkEnd(0xFE)
    Return()

    # Function_16_5199 end

    def Function_17_53CC(): pass

    label("Function_17_53CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_55AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54E1")

    #C0236
    ChrTalk(
        0xFE,
        (
            "大統領拘束の速報記事は\x01",
            "私とマッケネン君で何とか仕上げて\x01",
            "急いで発行させてもらったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "ちなみに他の記者たちも早速\x01",
            "取材を再開している状態なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "今後はグレイス君とも\x01",
            "堂々と連絡を取ることができるし、\x01",
            "新たな情報をどんどん集めないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_55A7")

    label("loc_54E1")


    #C0239
    ChrTalk(
        0xFE,
        (
            "今後はグレイス君とも\x01",
            "堂々と連絡を取ることができるし、\x01",
            "新たな情報をどんどん集めないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "市民の動揺や混乱を抑えるためにも\x01",
            "一分一秒でも早く、正確な情報を\x01",
            "伝えられるよう尽力させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55A7")

    Jump("loc_5667")

    label("loc_55AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5667")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55CB")
    TalkEnd(0xFE)
    Call(0, 18)
    Return()

    label("loc_55CB")


    #C0241
    ChrTalk(
        0xFE,
        (
            "グレイス君が\x01",
            "お世話になっているようで\x01",
            "君たちには本当に感謝しているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "この先もどうか気を付けて……\x01",
            "そして是非、君たちの活躍を\x01",
            "記事にさせてくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5667")

    TalkEnd(0xFE)
    Return()

    # Function_17_53CC end

    def Function_18_566B(): pass

    label("Function_18_566B")

    TalkBegin(0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x9, 0x0, 0)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5715")
    Jump("loc_575F")

    label("loc_5715")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5735")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_575F")

    label("loc_5735")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5755")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_575F")

    label("loc_5755")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_575F")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    #C0243
    ChrTalk(
        0x9,
        "おお、特務支援課じゃねえか。\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x8,
        "皆さん、よくぞご無事でしたね。\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xE,
        (
            "ふむ、大きな声では言えないが\x01",
            "君たちの事情や活躍は大体\x01",
            "グレイス君から聞いているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xE,
        (
            "よければ今の状況について\x01",
            "少し情報交換させてもらって\x01",
            "構わないだろうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        "#00000Fええ、こちらこそお願いします。\x02",
    )

    CloseMessageWindow()
    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(61910, 1500, -2140, 0)
    MoveCamera(59, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21850, 0)
    SetChrPos(0x101, 62030, 0, -2100, 90)
    SetChrPos(0x102, 61830, 0, -1090, 90)
    SetChrPos(0x103, 61480, 0, -3030, 90)
    SetChrPos(0x104, 60040, 0, -1980, 90)
    SetChrPos(0xF4, 59440, 0, -990, 90)
    SetChrPos(0xF5, 59440, 0, -2990, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xE, 0x9)
    ClearChrBattleFlags(0xE, 0x4)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0xE, 64370, 0, -1800, 270)
    SetChrPos(0x9, 63780, 0, -800, 270)
    SetChrPos(0x8, 64349, 0, -2890, 270)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0248
    ChrTalk(
        0xE,
        (
            "なるほど……するとこれから\x01",
            "オルキスタワーに突入するわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x9,
        (
            "で、その作戦が成功すりゃあ\x01",
            "この独裁体制も終了ってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x9,
        (
            "ったく、独立無効宣言で少しは\x01",
            "動きやすくなったと思った途端に\x01",
            "この厳戒令だったからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x9,
        (
            "あの変なモヤが出始めてから\x01",
            "なんでか通信器も極端に\x01",
            "通じにくくなっちう始末だしよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x102,
        (
            "#6P#00105Fそうなんですか、\x01",
            "通常の導力通信まで……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x103,
        (
            "#12P#00203F恐らく、あのモヤに\x01",
            "何らかの妨害波が\x01",
            "含まれているんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x104,
        (
            "#6P#00301Fふむ、早く何とかしねえと\x01",
            "混乱は増してくばかりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        (
            "#6P#00003Fああ……そうだな。\x02\x03",

            "#00000Fちなみに、こちらにいるのは\x01",
            "皆さんで全員なんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xE,
        (
            "ああ、他のスタッフはみんな\x01",
            "出先で巻き込まれてしまってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xE,
        (
            "それでも一応、ほとんどの者と\x01",
            "連絡自体は付いているんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xE,
        (
            "ただ１人、レインズ君だけ\x01",
            "全く連絡が付かない状態なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xE,
        (
            "いったい今頃\x01",
            "どこでどうしているんだか……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x101,
        "#6P#00005Fレインズさんが……\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xE,
        (
            "ま、市内のどこかにいるのは\x01",
            "間違いないんだろうけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x8,
        (
            "レインズ君、\x01",
            "グレイスさんに感化されて\x01",
            "無茶していなければいいんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xE,
        (
            "ただ、彼はそこそこ危険慣れも\x01",
            "しているし、それほど\x01",
            "心配はしていないんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xE,
        (
            "ま、こちらの話はともかく\x01",
            "これ以上君たちの時間を\x01",
            "奪うわけにもいかなさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x9,
        (
            "とりあえず、俺たちはここで\x01",
            "速報の準備をしながらアンタらの\x01",
            "武運を祈らせてもらうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x9,
        (
            "必ず作戦を成功させて、\x01",
            "この窮屈な体制を\x01",
            "是が非でもブチ壊してくれ！\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        (
            "#6P#00000Fええ、了解です！\x02\x03",

            "#00003F（レインズさんと\x01",
            "  連絡が取れない、か……）\x02\x03",

            "#00001F（彼の安否はグレイスさんも\x01",
            "  気にするだろうし、\x01",
            "  こちらでも気にかけておくか。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrPos(0x0, -6570, 20, 2860, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1BF, 0)
    EventEnd(0x5)
    Return()

    # Function_18_566B end

    def Function_19_5FB2(): pass

    label("Function_19_5FB2")

    EventBegin(0x0)
    Fade(500)
    OP_68(4720, 1500, 56190, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19720, 0)
    SetChrPos(0x101, 4520, 0, 56690, 90)
    SetChrPos(0x102, 4500, 0, 55000, 45)
    SetChrPos(0x103, 3360, 0, 56510, 90)
    SetChrPos(0x109, 4950, 0, 58190, 135)
    SetChrPos(0x105, 3550, 0, 57990, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_93(0xB, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_0D()

    #C0268
    ChrTalk(
        0xA,
        "支援課の皆さん……\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xB,
        (
            "#02101Fロイド君たち、\x01",
            "大変なことになったわね。\x02\x03",

            "#02105Fそうだ、ランディ君は――\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0270
    ChrTalk(
        0xB,
        (
            "#02101Fランディ君はどうしたの？\x01",
            "もしかして――\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x101,
        "#6P#00003F……っ………\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x102,
        "#6P#00108F……それは………\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        (
            "#6P#00001Fすみません。\x01",
            "その話はまた別の機会に――\x02\x03",

            "#00003F――行こう、みんな。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0x102, 0x0, 0x1F4)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0274
    ChrTalk(
        0xB,
        (
            "#02101Fちょっと待って、ロイド君！\x02\x03",

            "#02104Fあたしは追求するつもりはないわ。\x01",
            "よければ“相談”してみない？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0275
    ChrTalk(
        0x101,
        "#6P#00005Fえ……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    OP_93(0x102, 0x2D, 0x1F4)

    #C0276
    ChrTalk(
        0x109,
        "#6P#10105Fあの、それはどういう……\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xB,
        (
            "#02101Fまず前提として……\x01",
            "ランディ君の素性については\x01",
            "あたしもある程度知っているわ。\x02\x03",

            "#02103Fこう言っちゃ何だけど、\x01",
            "可能性の話として疑いの目を\x01",
            "持っていないわけでもない。\x02\x03",

            "#02100Fけど同時に彼の支援課での活躍は\x01",
            "これまで十分に見てきているし、\x01",
            "個人的に信頼しているのも確かよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x102,
        "#6P#00105Fグレイスさん……\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xB,
        (
            "#02103Fそして、貴方たちの反応で\x01",
            "事情は何となく分かったわ。\x02\x03",

            "#02101Fランディ君は１人で\x01",
            "マインツに向かったのね？\x02\x03",

            "この事件を解決するために。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x101,
        "#6P#00001F……そこまで分かりますか。\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x103,
        (
            "#6P#00203F……さすがは、\x01",
            "クロスベルタイムズの\x01",
            "記者ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xB,
        (
            "#02102Fふふ、やっぱり図星か。\x02\x03",

            "#02103Fそして、貴方たちは\x01",
            "そんな彼を連れ戻そうと\x01",
            "行動している……\x02\x03",

            "#02101F聞くまでもない気はするけど、\x01",
            "当然、相応の覚悟はあるのよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x101,
        (
            "#6P#00001Fもちろんです！\x01",
            "ランディは俺たちの仲間ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x102,
        "#6P#00101Fええ、その通りです。\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xB,
        (
            "#02104Fなるほど、相談なんて\x01",
            "乗るまでもなかったってわけね。\x02\x03",

            "#02101Fならあたしも、\x01",
            "あくまであたしらしく\x01",
            "声を掛けさせてもらうわ。\x02\x03",

            "#02104F――くれぐれも気を付けて！\x02\x03",

            "#02109Fそしてまた、\x01",
            "特務支援課が活躍する\x01",
            "記事を書かせてちょうだい！\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x101,
        "#6P#00000Fはい、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0xB, 0xB4, 0x0)
    OP_93(0xA, 0x0, 0x0)
    SetChrPos(0x0, 4720, 0, 56190, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x171, 3)
    EventEnd(0x5)
    Return()

    # Function_19_5FB2 end

    def Function_20_672A(): pass

    label("Function_20_672A")

    EventBegin(0x0)
    Fade(500)
    OP_68(3050, 1520, -1840, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20950, 0)
    SetChrPos(0x101, 2700, 20, -1900, 90)
    SetChrPos(0x102, 2700, 20, -800, 90)
    SetChrPos(0x103, 1500, 20, -1900, 90)
    SetChrPos(0x109, 1500, 20, -800, 90)
    SetChrPos(0x105, 300, 20, -1900, 90)
    SetChrPos(0x104, 300, 20, -800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_693E")

    #C0287
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "クロスベル通信社へようこそ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0288
    ChrTalk(
        0x8,
        "あら、皆様は特務支援課の……\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x101,
        (
            "#00000Fこんにちは、\x01",
            "支援要請の件で伺いました。\x02\x03",

            "グルメガイドの取材について\x01",
            "協力が必要とのことですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x8,
        (
            "ふふ、わざわざお越しいただき\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x8,
        (
            "では、早速ですが\x01",
            "依頼を引き受けて\x01",
            "いただけますでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x17D, 0)
    Jump("loc_69AB")

    label("loc_693E")


    #C0292
    ChrTalk(
        0x8,
        (
            "わざわざお越しいただき\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x8,
        (
            "早速ですが\x01",
            "依頼を引き受けて\x01",
            "いただけますでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69AB")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "引き受ける\x01",      # 0
            "やめる\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AB2")

    #C0294
    ChrTalk(
        0x101,
        "#00000Fええ、引き受けさせて頂きます。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x8,
        "かしこまりました。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x8,
        (
            "では、担当の者から依頼について\x01",
            "説明いたしますので、\x01",
            "２階の方でお待ち下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 21)
    Jump("loc_6B8D")

    label("loc_6AB2")


    #C0297
    ChrTalk(
        0x101,
        (
            "#00006Fすみません、今は他にも\x01",
            "用事がありまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x8,
        (
            "あら、そうなのですか……\x01",
            "それではお待ちしています。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x8,
        (
            "依頼を受けてくださる場合は\x01",
            "出来るだけ早めにお越しくださいね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2700, 20, -2000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)

    label("loc_6B8D")

    Return()

    # Function_20_672A end

    def Function_21_6B8E(): pass

    label("Function_21_6B8E")

    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 60010, 150, 10690, 270)
    OP_68(57490, 1500, 11620, 0)
    MoveCamera(76, 28, -1, 0)
    OP_6E(400, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 58200, 0, 11760, 135)
    SetChrPos(0x102, 58650, 0, 12660, 135)
    SetChrPos(0x103, 57000, 0, 11920, 135)
    SetChrPos(0x109, 57480, 0, 13060, 135)
    SetChrPos(0x104, 55980, 0, 12490, 135)
    SetChrPos(0x105, 55580, 0, 11290, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0300
    ChrTalk(
        0xB,
        (
            "#02100Fハロハロー♪\x01",
            "特務支援課の皆さん。\x02\x03",

            "#02109Fお待たせしちゃって\x01",
            "ゴメンなさいね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        (
            "#00006Fやっぱり……担当者は\x01",
            "グレイスさんでしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x103,
        "#00200Fある程度予想はしていましたが。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6E09")

    #C0303
    ChrTalk(
        0xB,
        (
            "#02103Fもう、反応薄いわね～。\x02\x03",

            "#02100Fせっかくまた一緒に仕事が出来るんだし、\x01",
            "もっと喜んでくれてもいいのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x102,
        (
            "#00109Fあはは……前のときは\x01",
            "クロスベル中を回って大変でしたし。\x02\x03",

            "#00105Fそれで、今回は\x01",
            "どういった依頼なんでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F03")

    label("loc_6E09")


    #C0305
    ChrTalk(
        0xB,
        (
            "#02103Fもう、反応薄いわね～。\x02\x03",

            "#02100Fせっかく一緒に仕事が出来るんだし、\x01",
            "もっと喜んでくれてもいいのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x102,
        (
            "#00109Fあ、あはは……\x01",
            "グレイスさんが関わっているとなると\x01",
            "なんだか大変そうですし。\x02\x03",

            "#00105Fそれで、今回は\x01",
            "どういった依頼なんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F03")


    #C0307
    ChrTalk(
        0x105,
        (
            "#10300F確か、グルメガイドの取材の\x01",
            "協力って話だったっけ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)

    #C0308
    ChrTalk(
        0xB,
        (
            "#02100Fええ、その通りよ。\x02\x03",

            "#02104F少し前、『ディーター市長の\x01",
            "勢いにあやかって何かしたい』って、\x01",
            "クロスベル商工会から提案があってね。\x02\x03",

            "#02102F通信社もそれに乗っかって、\x01",
            "合同でグルメガイドを\x01",
            "作ることになったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x109,
        (
            "#10105F商工会と合同で……\x01",
            "具体的に何をするんですか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)

    #C0310
    ChrTalk(
        0xB,
        (
            "#02104F基本的には、クロスベル自治州内の\x01",
            "飲食店を紹介するわけだけど……\x02\x03",

            "#02100F各店舗には取材のほかに、\x01",
            "割引サービスとかにも協力して\x01",
            "もらったりしてるのよね。\x02\x03",

            "#02109Fまあ、そういう感じで\x01",
            "面白そうな企画が\x01",
            "色々と進行中ってワケ。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x101,
        (
            "#00000Fなるほど……\x01",
            "それはなかなか画期的そうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xB,
        (
            "#02109F──で！\x01",
            "ここからが本題なんだけど……\x02\x03",

            "#02100F企画の一つに、\x01",
            "『噂のあの人の一押しグルメ』\x01",
            "っていうのあってね。\x02\x03",

            "#02104FＩＢＣのマリアベル女史や、\x01",
            "アルカンシェルのイリア、\x01",
            "テオドール＆ユージーン……\x02\x03",

            "#02102Fそういう、クロスベルタイムズを\x01",
            "いつも賑わしてくれてる著名人に\x01",
            "お勧めの一品を紹介してもらってるの。\x02\x03",

            "#02109Fそこで、アナタたち特務支援課にも\x01",
            "是非協力してもらいたいと思って。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x103,
        "#00200Fふむ……それが今回の依頼ですか。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x102,
        (
            "#00103F確かに面白そうな企画ですけど……\x02\x03",

            "#00105Fその顔ぶれの中に\x01",
            "私たちが入って大丈夫なんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x104,
        (
            "#00306Fだな。\x01",
            "イリアさんやマリアベルさんと\x01",
            "肩を並べられるのは嬉しいが……\x02\x03",

            "#00301F俺たちが参加したところで、\x01",
            "何だかパッとしねえ記事に\x01",
            "なっちまうんじゃないんッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、察するに、\x01",
            "僕たちは体のいい\x01",
            "当て馬って所かな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0317
    ChrTalk(
        0xB,
        (
            "#02105Fノンノン、\x01",
            "当て馬だなんてとんでもない！\x02\x03",

            "#02102F最近じゃ、あなたたちを応援する\x01",
            "純粋なファンだって増えてるのよ？\x02\x03",

            "#02109F支援課メンバーのプライベートを\x01",
            "激写して欲しいなんて要望も\x01",
            "来ているくらいだし㈱\x02",
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
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0318
    ChrTalk(
        0x102,
        (
            "#00106Fさ、流石にそれは\x01",
            "勘弁してもらいたいですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xB,
        (
            "#02100Fふふ、とにかく\x01",
            "あなたたちはあなたたちなりに\x01",
            "注目されてるってことよ。\x02\x03",

            "#02104Fそうじゃなかったらこんな依頼、\x01",
            "そもそも頼んでいないわけだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        (
            "#00003Fとにかく、話は大体分かりました。\x02\x03",

            "#00000F具体的にはどう進めればいいんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xB,
        (
            "#02102Fうふふ、それじゃあ続けて\x01",
            "取材のやり方を説明するわね。\x02\x03",

            "#02104Fまずは、各地の料理屋や\x01",
            "屋台を回って、実際にその店の\x01",
            "料理を食べてきてちょうだい。\x02\x03",

            "#02109Fその中からあなたたちが\x01",
            "『これは！』と思った料理を\x01",
            "それぞれ見つけてきて欲しいの。\x02\x03",

            "#02102Fそして、最後にこの通信社で、\x01",
            "あなたたち自身に\x01",
            "記事を書いてもらうってわけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x109,
        (
            "#10103F自治州の店を回って、\x01",
            "６人がそれぞれ、お気に入りを\x01",
            "探してくるってわけですね。\x02\x03",

            "#10105Fでも、もし見つからなかったら……？\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xB,
        (
            "#02102Fクロスベルは広いんだし、\x01",
            "絶対ひとつくらいは\x01",
            "気に入る料理が見つかるって。\x02\x03",

            "#02104Fもし見つからなくても、\x01",
            "６軒回ってもらえれば\x01",
            "とりあえず記事は作れるから。\x02\x03",

            "#2100Fま、やっぱり理想は\x01",
            "あなたたち６人全員のお気に入りを\x01",
            "紹介できることだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x104,
        (
            "#00303Fふむ、とにかく最低でも\x01",
            "６ヶ所以上は回んなきゃ\x01",
            "ダメってことだな。\x02\x03",

            "#00300F他に注意しとくべきことは\x01",
            "ないんッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xB,
        (
            "#02103Fんー、そうね……\x02\x03",

            "#02105Fあ、ミシュラムにあるお店と\x01",
            "いわゆる『飲み屋』は\x01",
            "除外してもらえるかしら。\x02\x03",

            "#02102Fそっちは他の方面で\x01",
            "取材してもらうのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x105,
        (
            "#10303Fふむ、となると\x01",
            "旧市街の《トリニティ》も\x01",
            "対象外ってことか。\x02\x03",

            "#10300Fフフ、せっかく店が繁盛する\x01",
            "チャンスだったのに、\x01",
            "アッバスには悪いかな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)

    #C0327
    ChrTalk(
        0xB,
        (
            "#02109Fいや～、ごめんねワジ君！\x01",
            "そっち方面の取材班には\x01",
            "あたしの方から言っとくから。\x02\x03",

            "#02104F……あ、それと取材については\x01",
            "既に各店舗に話を通してるから、\x01",
            "飲食代については心配いらないわ。\x02\x03",

            "#02102Fお店に行って事情を話せば、\x01",
            "試食メニューを出してもらえるはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x102,
        (
            "#00100Fとにかく、飲み屋以外の店舗を\x01",
            "６ヶ所以上回ってくればいいんですね。\x02\x03",

            "#00103F私たち全員のお気に入りを\x01",
            "見つけるためには\x01",
            "根気よく回る必要がありそうだけど……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)

    #C0329
    ChrTalk(
        0xB,
        (
            "#02104Fふふ、急ぎの仕事ってわけじゃないから\x01",
            "とにかく頑張ってちょうだい。\x02\x03",

            "#02100F一通り回って取材が済んだと思ったら、\x01",
            "通信社に戻って報告してね。\x02\x03",

            "#02109Fあたしが通信社にいない時でも、\x01",
            "受付のトリアちゃんに言ってもらえれば\x01",
            "すぐにでも駆けつけるから！\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x101,
        (
            "#00000Fええ、了解しました。\x01",
            "さっそく取り掛かってみます。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0331
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【グルメガイドの取材協力】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x0, 6)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x0, -6370, 250, 2630, 180)
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x172, 0)
    OP_29(0x80, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_21_6B8E end

    def Function_22_7F46(): pass

    label("Function_22_7F46")

    EventBegin(0x0)
    Fade(500)
    OP_68(3050, 1520, -1840, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20950, 0)
    SetChrPos(0x101, 2700, 20, -1900, 90)
    SetChrPos(0x102, 2700, 20, -800, 90)
    SetChrPos(0x103, 1500, 20, -1900, 90)
    SetChrPos(0x109, 1500, 20, -800, 90)
    SetChrPos(0x105, 300, 20, -1900, 90)
    SetChrPos(0x104, 300, 20, -800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0332
    ChrTalk(
        0x8,
        "お疲れ様です、皆さん。\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x8,
        (
            "グルメガイドの取材で\x01",
            "６ヶ所以上の飲食店を\x01",
            "回られたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x8,
        (
            "早速、グレイスさんに\x01",
            "報告いたしますか？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "まだ報告しない\x01",          # 0
            "グレイスに報告する\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8168")

    #C0335
    ChrTalk(
        0x8,
        "かしこまりました。\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x8,
        (
            "では、グレイスさんを\x01",
            "お呼びしますので、皆さんは\x01",
            "２階の方でお待ち下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jump("loc_81E1")

    label("loc_8168")


    #C0337
    ChrTalk(
        0x8,
        "あら、そうですか？\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        (
            "それでは、報告する場合は\x01",
            "また声をおかけくださいね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2700, 20, -2000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    label("loc_81E1")

    Return()

    # Function_22_7F46 end

    def Function_23_81E2(): pass

    label("Function_23_81E2")

    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 60010, 150, 10690, 270)
    OP_68(57490, 1500, 11620, 0)
    MoveCamera(76, 28, -1, 0)
    OP_6E(400, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 58200, 0, 11760, 135)
    SetChrPos(0x102, 58650, 0, 12660, 135)
    SetChrPos(0x103, 57000, 0, 11920, 135)
    SetChrPos(0x109, 57480, 0, 13060, 135)
    SetChrPos(0x104, 55980, 0, 12490, 135)
    SetChrPos(0x105, 55580, 0, 11290, 90)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0339
    ChrTalk(
        0xB,
        (
            "#02109Fハーイ、お疲れ様㈱\x02\x03",

            "#02102F『一押しグルメ』の取材は\x01",
            "どうだった～？\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x101,
        (
            "#00009Fはは、まあ……\x01",
            "楽しませて頂きました。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x104,
        (
            "#00306F結構広い範囲を回ったから\x01",
            "疲れたけどなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xB,
        (
            "#02100Fフフ、美味しいものが\x01",
            "沢山食べられてよかったじゃない。\x02\x03",

            "#02109Fそれじゃあ、さっそく取材結果を\x01",
            "聞かせてもらうとしましょうか！\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        "#00000Fええ、では……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0344
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちは取材に行った\x01",
            "店について報告した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_8458")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_846B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_846B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_847E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_847E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_8491")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_84A4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_84B7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_84CA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_84DD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_84F0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_8503")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_8516")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8516")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_861C")

    #C0345
    ChrTalk(
        0xB,
        (
            "#02104Fふんふん、全部で１１ヶ所の店を\x01",
            "回ってきてくれたのね。\x02\x03",

            "#02109Fこりゃまた随分念入りに\x01",
            "取材してきてくれたみたいね～！\x01",
            "フフ、お姉さん嬉しいわ！\x02\x03",

            "#02102Fじゃあ次は……\x01",
            "その中であなたたちが出会った\x01",
            "『一押しグルメ』を教えてちょうだい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A98")

    label("loc_861C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8701")

    #C0346
    ChrTalk(
        0xB,
        (
            "#02104Fふんふん、全部で１０ヶ所の店を\x01",
            "回ってきてくれたのね。\x02\x03",

            "#02102Fふふ、しっかり取材して\x01",
            "くれたみたいじゃない。\x02\x03",

            "#02100Fじゃあ次は……\x01",
            "その中であなたたちが出会った\x01",
            "『一押しグルメ』を教えてちょうだい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A98")

    label("loc_8701")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87E8")

    #C0347
    ChrTalk(
        0xB,
        (
            "#02104Fふんふん、全部で９ヶ所の店を\x01",
            "回ってきてくれたのね。\x02\x03",

            "#02102Fふふ、しっかり取材してきて\x01",
            "くれたみたいじゃない。\x02\x03",

            "#02100Fじゃあ次は……\x01",
            "その中であなたたちが出会った\x01",
            "『一押しグルメ』を教えてちょうだい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A98")

    label("loc_87E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88CF")

    #C0348
    ChrTalk(
        0xB,
        (
            "#02104Fふんふん、全部で８ヶ所の店を\x01",
            "回ってきてくれたのね。\x02\x03",

            "#02102Fふふ、しっかり取材してきて\x01",
            "くれたみたいじゃない。\x02\x03",

            "#02100Fじゃあ次は……\x01",
            "その中であなたたちが出会った\x01",
            "『一押しグルメ』を教えてちょうだい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A98")

    label("loc_88CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89B6")

    #C0349
    ChrTalk(
        0xB,
        (
            "#02104Fふんふん、全部で７ヶ所の店を\x01",
            "回ってきてくれたのね。\x02\x03",

            "#02102Fふふ、しっかり取材してきて\x01",
            "くれたみたいじゃない。\x02\x03",

            "#02100Fじゃあ次は……\x01",
            "その中であなたたちが出会った\x01",
            "『一押しグルメ』を教えてちょうだい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A98")

    label("loc_89B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A98")

    #C0350
    ChrTalk(
        0xB,
        (
            "#02104Fふんふん、全部で６ヶ所の店を\x01",
            "回ってきてくれたのね。\x02\x03",

            "#02102Fふふ、しっかり取材してきて\x01",
            "くれたみたいじゃない。\x02\x03",

            "#02100Fじゃあ次は……\x01",
            "その中であなたたちが出会った\x01",
            "『一押しグルメ』を教えてちょうだい！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A98")

    Fade(500)
    OP_68(58050, 1900, 10380, 0)
    MoveCamera(12, 26, -1, 0)
    OP_6E(400, 0)
    SetCameraDistance(17470, 0)
    OP_0D()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_8BD2")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0351
    ChrTalk(
        0x101,
        (
            "#00000F俺はアルモリカ村にある\x01",
            "宿酒場《トネリコ亭》の\x01",
            "『匠風オムライス』ですね。\x02\x03",

            "#00002Fアルモリカ村ならではの素朴な味が\x01",
            "俺の琴線に触れたっていうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xB,
        (
            "#02102Fなるほど、確かにあのオムライスは\x01",
            "あそこでしか味わえないもんね～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_8CD4")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0353
    ChrTalk(
        0x102,
        (
            "#00104F私はウルスラ病院にある\x01",
            "ビュッフェ《レクチェ》の\x01",
            "『三日煮込みシチュー』です。\x02\x03",

            "#00109F長い間煮込まれてトロトロで、\x01",
            "その上、体にもとっても良さそうで。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xB,
        (
            "#02109Fうんうん、あのシチューは食べるだけで\x01",
            "たちまち元気になりそうよね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_8DD5")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0355
    ChrTalk(
        0x103,
        (
            "#00204Fわたしは、歓楽街のアイス屋台にあった\x01",
            "『氷菓≪七彩≫』を推したいです。\x02\x03",

            "#00202Fあの不思議な食感と七色の味わい……\x01",
            "今までのアイスの常識を覆す絶品かと。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xB,
        (
            "#02105Fおおっ、ティオちゃん絶賛ね！\x01",
            "確かにこれから人気が出そうよね～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_8EEE")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0357
    ChrTalk(
        0x104,
        (
            "#00300F俺は港湾区の麺屋台で出された\x01",
            "『天上麺≪日輪≫』ッスね。\x02\x03",

            "#00309Fコシのあるちぢれ麺が\x01",
            "真紅の辛口スープに絡んで……\x01",
            "思い出しただけでもヨダレが出るッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xB,
        (
            "#02104Fふむふむ、あの屋台には\x01",
            "あたしもお昼によく行くわね。\x01",
            "マスターの拘りが半端ないのよね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_8FE8")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0359
    ChrTalk(
        0x109,
        (
            "#10107Fあたしは、東通り《龍老飯店》の\x01",
            "『天下一炒飯』です！\x02\x03",

            "#10104Fシンプルながらも深みのある味わいは、\x01",
            "一度食べ始めると止まりません！\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xB,
        (
            "#02109Fチャンホイさんの得意料理よね！\x01",
            "うーん、あたしもまた\x01",
            "食べたくなってきちゃった。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_90E8")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0361
    ChrTalk(
        0x105,
        (
            "#10304F僕の一押しはタングラム門の\x01",
            "食堂にあった『芳醇潮鍋』かな。\x02\x03",

            "#10302F風味もいいし、みんなでワイワイやるには\x01",
            "これ以上のものは無いと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xB,
        (
            "#02102F国境門の食堂は\x01",
            "隠れたグルメスポットなのよね！\x01",
            "ふふっ、ワジ君も通なんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90E8")


    #C0363
    ChrTalk(
        0x101,
        (
            "#00004F……とりあえずは\x01",
            "こんな所でしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_92E1")
    OP_2C(0x80, 0x2)
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0364
    ChrTalk(
        0xB,
        (
            "#02102Fうんうん、ちゃんと\x01",
            "メンバー全員の『一押しグルメ』を\x01",
            "見つけてきてくれたみたいね。\x02\x03",

            "#02104Fこれでグルメガイドの特集ページも\x01",
            "かなり充実するはずよ。\x02\x03",

            "#02109F本当にありがとね、あなたたち！\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x101,
        "#00000Fはは、ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x103,
        "#00202F頑張って回った甲斐がありましたね。\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xB,
        (
            "#02105Fおっと、まだ仕事は終わってないわよ。\x02\x03",

            "#02102Fあなたたちにはさっそく\x01",
            "紹介コメントを仕上げてもらわないとね！\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x80, 0x1, 0xF)
    Jump("loc_964C")

    label("loc_92E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_94AC")
    OP_2C(0x80, 0x1)

    #C0368
    ChrTalk(
        0xB,
        (
            "#02106Fうーん、さすがに全員分の\x01",
            "『一押しグルメ』は\x01",
            "見つからなかったかぁ。\x02\x03",

            "#02102Fでもまあ、及第点かしら。\x01",
            "ひとまずお礼を言っておくわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x101,
        "#00012Fあ、ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x103,
        (
            "#00206F（もう少し頑張ってみても\x01",
            "  よかったかもしれませんね……）\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xB,
        (
            "#02104Fでも、お気に入りが無い人も\x01",
            "ナンバー２やナンバー３は\x01",
            "いくつかあったはずよね？\x02\x03",

            "#02102F足りない分は上手く補填しつつ、\x01",
            "さっそく紹介コメントを\x01",
            "仕上げてもらおうかしら！\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x80, 0x1, 0x10)
    Jump("loc_964C")

    label("loc_94AC")

    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0372
    ChrTalk(
        0xB,
        (
            "#02105Fあ、あれ？　あなたたちの\x01",
            "『一押しグルメ』はこれだけなの？\x02\x03",

            "#02106Fうーん、仕方ないと思うけど……\x01",
            "もう少し何とかならなかったかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x101,
        "#00006Fめ、面目ありません。\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x103,
        "#00206F（もっと頑張ればよかったですね……）\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xB,
        (
            "#02103F……まあ、仕方ないわね。\x01",
            "最低限は回ってくれたみたいだし。\x02\x03",

            "#02100F足りない分は上手く補填しつつ、\x01",
            "さっそく紹介コメントを\x01",
            "仕上げてもらおうかしら！\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x80, 0x1, 0x11)

    label("loc_964C")

    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0376
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドたちは\x01",
            "慣れない物書きに\x01",
            "四苦八苦しつつ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0377
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "なんとかグルメガイドの\x01",
            "『一押しグルメ』紹介記事を\x01",
            "仕上げるのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(57490, 1500, 11620, 0)
    MoveCamera(76, 28, -1, 0)
    OP_6E(400, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(2000, 0)
    OP_0D()

    #C0378
    ChrTalk(
        0xB,
        (
            "#02100Fうん、こんなところかしら。\x02\x03",

            "#02104F後でこっちでも校正はするけど、\x01",
            "とりあえずこれでＯＫ！\x02\x03",

            "#02102Fふふ、おかげ様で\x01",
            "おもしろいグルメガイドが\x01",
            "作れるんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x109,
        "#10109Fあはは、大変でしたけど……\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x105,
        (
            "#10304Fま、これでひとまずは\x01",
            "任務完了かな？\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xB,
        (
            "#02104Fええ、本当にお世話になったわ。\x02\x03",

            "#02109Fグルメガイドの発行には\x01",
            "まだ少しかかるだろうけど、\x01",
            "是非楽しみにしててちょうだい！\x02\x03",

            "#02102Fまた何かあったらヨロシクね～♪\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        "#00000Fええ、それでは失礼します。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0383
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【グルメガイドの取材協力】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 6)
    OP_29(0x80, 0x1, 0x12)
    OP_29(0x80, 0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_9981")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_9993")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_99A5")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_99B7")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_99C9")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99C9")

    SetChrFlags(0xB, 0x80)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -6370, 250, 2630, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_23_81E2 end

    def Function_24_99FA(): pass

    label("Function_24_99FA")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9A04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9E14")
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_9A3E")
    MenuCmd(1, 1, "★フェアリージェラート")
    Jump("loc_9A56")

    label("loc_9A3E")

    MenuCmd(1, 1, "フェアリージェラート")

    label("loc_9A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_9A70")
    MenuCmd(1, 1, "★鳳凰麺")
    Jump("loc_9A7A")

    label("loc_9A70")

    MenuCmd(1, 1, "鳳凰麺")

    label("loc_9A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_9A9E")
    MenuCmd(1, 1, "★会心バジルパスタ")
    Jump("loc_9AB2")

    label("loc_9A9E")

    MenuCmd(1, 1, "会心バジルパスタ")

    label("loc_9AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_9AD6")
    MenuCmd(1, 1, "★にがトマトソーダ")
    Jump("loc_9AEA")

    label("loc_9AD6")

    MenuCmd(1, 1, "にがトマトソーダ")

    label("loc_9AEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_9B0C")
    MenuCmd(1, 1, "★ピリ辛麻婆豆腐")
    Jump("loc_9B1E")

    label("loc_9B0C")

    MenuCmd(1, 1, "ピリ辛麻婆豆腐")

    label("loc_9B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_9B44")
    MenuCmd(1, 1, "★夕焼けクロワッサン")
    Jump("loc_9B5A")

    label("loc_9B44")

    MenuCmd(1, 1, "夕焼けクロワッサン")

    label("loc_9B5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_9B7C")
    MenuCmd(1, 1, "★匠風オムライス")
    Jump("loc_9B8E")

    label("loc_9B7C")

    MenuCmd(1, 1, "匠風オムライス")

    label("loc_9B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_9BB6")
    MenuCmd(1, 1, "★肉厚スタミナステーキ")
    Jump("loc_9BCE")

    label("loc_9BB6")

    MenuCmd(1, 1, "肉厚スタミナステーキ")

    label("loc_9BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_9BF4")
    MenuCmd(1, 1, "★完熟ビーフシチュー")
    Jump("loc_9C0A")

    label("loc_9BF4")

    MenuCmd(1, 1, "完熟ビーフシチュー")

    label("loc_9C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_9C2E")
    MenuCmd(1, 1, "★やみつきカレー鍋")
    Jump("loc_9C42")

    label("loc_9C2E")

    MenuCmd(1, 1, "やみつきカレー鍋")

    label("loc_9C42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_9C64")
    MenuCmd(1, 1, "★うるおい豆乳鍋")
    Jump("loc_9C76")

    label("loc_9C64")

    MenuCmd(1, 1, "うるおい豆乳鍋")

    label("loc_9C76")

    MenuCmd(1, 1, "やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 0)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9CED"),
        (1, "loc_9D06"),
        (2, "loc_9D1F"),
        (3, "loc_9D38"),
        (4, "loc_9D51"),
        (5, "loc_9D6A"),
        (6, "loc_9D83"),
        (7, "loc_9D9C"),
        (8, "loc_9DB5"),
        (9, "loc_9DCE"),
        (10, "loc_9DE7"),
        (11, "loc_9E00"),
        (SWITCH_DEFAULT, "loc_9E0F"),
    )


    label("loc_9CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_9CFE")
    ClearScenarioFlags(0x172, 1)
    Jump("loc_9D01")

    label("loc_9CFE")

    SetScenarioFlags(0x172, 1)

    label("loc_9D01")

    Jump("loc_9E0F")

    label("loc_9D06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_9D17")
    ClearScenarioFlags(0x172, 2)
    Jump("loc_9D1A")

    label("loc_9D17")

    SetScenarioFlags(0x172, 2)

    label("loc_9D1A")

    Jump("loc_9E0F")

    label("loc_9D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_9D30")
    ClearScenarioFlags(0x172, 3)
    Jump("loc_9D33")

    label("loc_9D30")

    SetScenarioFlags(0x172, 3)

    label("loc_9D33")

    Jump("loc_9E0F")

    label("loc_9D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_9D49")
    ClearScenarioFlags(0x172, 4)
    Jump("loc_9D4C")

    label("loc_9D49")

    SetScenarioFlags(0x172, 4)

    label("loc_9D4C")

    Jump("loc_9E0F")

    label("loc_9D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_9D62")
    ClearScenarioFlags(0x172, 5)
    Jump("loc_9D65")

    label("loc_9D62")

    SetScenarioFlags(0x172, 5)

    label("loc_9D65")

    Jump("loc_9E0F")

    label("loc_9D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_9D7B")
    ClearScenarioFlags(0x172, 6)
    Jump("loc_9D7E")

    label("loc_9D7B")

    SetScenarioFlags(0x172, 6)

    label("loc_9D7E")

    Jump("loc_9E0F")

    label("loc_9D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_9D94")
    ClearScenarioFlags(0x172, 7)
    Jump("loc_9D97")

    label("loc_9D94")

    SetScenarioFlags(0x172, 7)

    label("loc_9D97")

    Jump("loc_9E0F")

    label("loc_9D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_9DAD")
    ClearScenarioFlags(0x173, 0)
    Jump("loc_9DB0")

    label("loc_9DAD")

    SetScenarioFlags(0x173, 0)

    label("loc_9DB0")

    Jump("loc_9E0F")

    label("loc_9DB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_9DC6")
    ClearScenarioFlags(0x173, 1)
    Jump("loc_9DC9")

    label("loc_9DC6")

    SetScenarioFlags(0x173, 1)

    label("loc_9DC9")

    Jump("loc_9E0F")

    label("loc_9DCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_9DDF")
    ClearScenarioFlags(0x173, 2)
    Jump("loc_9DE2")

    label("loc_9DDF")

    SetScenarioFlags(0x173, 2)

    label("loc_9DE2")

    Jump("loc_9E0F")

    label("loc_9DE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_9DF8")
    ClearScenarioFlags(0x173, 3)
    Jump("loc_9DFB")

    label("loc_9DF8")

    SetScenarioFlags(0x173, 3)

    label("loc_9DFB")

    Jump("loc_9E0F")

    label("loc_9E00")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9E0F")

    label("loc_9E0F")

    Jump("loc_9A04")

    label("loc_9E14")

    Return()

    # Function_24_99FA end

    def Function_25_9E15(): pass

    label("Function_25_9E15")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0384
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《百日戦役》を巡る戦場取材、\x01",
            "３ヶ月間に渡る報道連載は\x01",
            "誠実で正義感溢れるものであった。\x02\x03",

            "その功績を讃え\x01",
            "ここにフューリッツァ賞を贈る。\x01",
            "Ｓ１１９２　１１月\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_25_9E15 end

    def Function_26_9EE6(): pass

    label("Function_26_9EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9EF0")
    Return()

    label("loc_9EF0")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A09C")

    #C0385
    ChrTalk(
        0x8,
        "あ、皆さん……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9F62():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_9F62)
    Sleep(50)

    def lambda_9F72():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_9F72)
    Sleep(50)

    def lambda_9F82():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_9F82)
    Sleep(50)

    def lambda_9F92():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_9F92)
    Sleep(50)

    def lambda_9FA2():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x4, 2, lambda_9FA2)
    Sleep(50)

    def lambda_9FB2():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x5, 2, lambda_9FB2)
    WaitChrThread(0x0, 2)
    Fade(1000)
    OP_68(-2860, 1510, 720, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(25500, 0)
    OP_0D()

    #C0386
    ChrTalk(
        0x8,
        (
            "すみませんが、基本的に\x01",
            "２階の編集部は関係者以外\x01",
            "立ち入り禁止でして。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x8,
        "御用なら私の方に仰ってください。\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x101,
        (
            "#00005Fす、すみません。\x01",
            "これは失礼しました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_A0E6")

    label("loc_A09C")


    #C0389
    ChrTalk(
        0x101,
        (
            "#00000F２階は立ち入り禁止みたいだ。\x01",
            "勝手に上がるわけにはいかないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0E6")

    Sleep(50)
    SetChrPos(0x0, -6370, 20, 2470, 180)
    EventEnd(0x4)
    Return()

    # Function_26_9EE6 end

    def Function_27_A0FD(): pass

    label("Function_27_A0FD")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0390
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "資料棚にクロスベルタイムズの\x01",
            "バックナンバーが並べられている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【０４年度前期①を読む】\x01",      # 0
            "【０４年度前期②を読む】\x01",      # 1
            "【やめる】\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2CB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【クロスベルタイムズ①】\x01",        # 0
            "【クロスベルタイムズ②】\x01",        # 1
            "【クロスベルタイムズ③】\x01",        # 2
            "【クロスベルタイムズ号外】\x01",      # 3
            "【クロスベルタイムズ④】\x01",        # 4
            "【やめる】\x01",                      # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A276")
    UseItem(0x2BC, 0xFF)

    label("loc_A276")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A28A")
    UseItem(0x2BD, 0xFF)

    label("loc_A28A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A29E")
    UseItem(0x2BE, 0xFF)

    label("loc_A29E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2B2")
    UseItem(0x2BF, 0xFF)

    label("loc_A2B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2C6")
    UseItem(0x2C0, 0xFF)

    label("loc_A2C6")

    Jump("loc_A3C9")

    label("loc_A2CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3C0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【クロスベルタイムズ⑤】\x01",      # 0
            "【クロスベルタイムズ⑥】\x01",      # 1
            "【クロスベルタイムズ⑦】\x01",      # 2
            "【クロスベルタイムズ⑧】\x01",      # 3
            "【やめる】\x01",                    # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A37F")
    UseItem(0x2C1, 0xFF)

    label("loc_A37F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A393")
    UseItem(0x2C2, 0xFF)

    label("loc_A393")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3A7")
    UseItem(0x2C3, 0xFF)

    label("loc_A3A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3BB")
    UseItem(0x2C4, 0xFF)

    label("loc_A3BB")

    Jump("loc_A3C9")

    label("loc_A3C0")

    FadeToBright(300, 0)

    label("loc_A3C9")

    TalkEnd(0xFF)
    Return()

    # Function_27_A0FD end

    SaveToFile()

Try(main)
