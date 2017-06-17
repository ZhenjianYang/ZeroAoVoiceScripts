from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1530.bin",                # FileName
        "c1530",                    # MapName
        "c1530",                    # Location
        0x00AE,                     # MapIndex
        "ed7151",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 174, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1530",                  # 0
        "イアン弁護士",           # 1
        "警官",                   # 2
        "警官",                   # 3
        "ピエール副局長",         # 4
        "グレイス",               # 5
        "レインズ",               # 6
        "記者ノティシア",         # 7
        "記者クロード",           # 8
        "記者パーカー",           # 9
        "帝国時報記者",           # 10
        "警官",                   # 11
        "警官",                   # 12
        "警官",                   # 13
        "記者トンプソン",         # 14
        "タイレル通信記者",       # 15
        "ダドリー捜査官",         # 16
        "捜査官",                 # 17
        "捜査官",                 # 18
        "グラント一尉",           # 19
        "ジゼル曹長",             # 20
        "市役所職員",             # 21
        "市役所職員",             # 22
        "市役所職員",             # 23
        "レクター書記官",         # 24
        "ディーター市長",         # 25
        "遊撃士スコット",         # 26
        "遊撃士ヴェンツェル",     # 27
        "遊撃士リン",             # 28
        "遊撃士エオリア",         # 29
        "ソーニャ司令",           # 30
        "ダグラス副司令",         # 31
        "ダミー",                 # 32
        "椅子",                   # 33
        "椅子",                   # 34
        "椅子",                   # 35
        "椅子",                   # 36
        "食器",                   # 37
        "警備隊員",               # 38
        "警備隊員",               # 39
        "警備隊員",               # 40
        "警備隊員",               # 41
    ))

    AddCharChip((
        "chr/ch05902.itc",                   # 00
        "chr/ch30000.itc",                   # 01
        "chr/ch06400.itc",                   # 02
        "chr/ch06000.itc",                   # 03
        "chr/ch28100.itc",                   # 04
        "chr/ch47900.itc",                   # 05
        "chr/ch27400.itc",                   # 06
        "chr/ch27800.itc",                   # 07
        "chr/ch27900.itc",                   # 08
        "chr/ch27600.itc",                   # 09
        "chr/ch21800.itc",                   # 0A
        "chr/ch47500.itc",                   # 0B
        "chr/ch00900.itc",                   # 0C
        "chr/ch27600.itc",                   # 0D
        "chr/ch27800.itc",                   # 0E
        "chr/ch31300.itc",                   # 0F
        "chr/ch34100.itc",                   # 10
        "chr/ch30002.itc",                   # 11
        "chr/ch25800.itc",                   # 12
        "chr/ch28200.itc",                   # 13
        "chr/ch05900.itc",                   # 14
        "chr/ch12402.itc",                   # 15
        "chr/ch27902.itc",                   # 16
        "chr/ch27802.itc",                   # 17
        "chr/ch06002.itc",                   # 18
        "chr/ch47902.itc",                   # 19
        "chr/ch21802.itc",                   # 1A
        "chr/ch47502.itc",                   # 1B
        "chr/ch06402.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 0,   28,  255,  0)
    DeclNpc(26739,   0,       1529,    180,  389,  0x0, 0,   1,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(266920,  0,       11329,   45,   389,  0x0, 0,   1,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(336769,  0,       2880,    265,  389,  0x0, 0,   3,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(337769,  0,       2880,    265,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(265570,  0,       2539,    180,  389,  0x0, 0,   1,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   30,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   10,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(274320,  0,       9760,    315,  389,  0x0, 0,   12,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(275320,  0,       13649,   89,   389,  0x0, 0,   13,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   14,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(208529,  0,       11590,   135,  389,  0x0, 0,   15,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(209529,  0,       11590,   135,  389,  0x0, 0,   16,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(136970,  0,       -1250,   45,   389,  0x0, 0,   18,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(137970,  0,       -1250,   45,   389,  0x0, 0,   19,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(147710,  0,       -850,    89,   389,  0x0, 0,   14,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   21,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    236,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 67,  34.47999954223633,     -1.190000057220459,    -1.0,                  576.0,                 [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -5.74666690826416,     0.14875000715255737,   0.20000001788139343,   1.0])

    DeclActor(80610,   0,       2930,    1000,    80610,   1500,    2930,    0x007C, 0,  68, 0x0000)
    DeclActor(86730,   0,       3250,    1000,    86730,   1500,    3250,    0x007C, 0,  68, 0x0000)
    DeclActor(-55790,  0,       3070,    1000,    -55790,  1500,    3070,    0x007C, 0,  69, 0x0000)
    DeclActor(148500,  0,       11990,   1000,    148500,  1500,    11990,   0x007C, 0,  70, 0x0000)
    DeclActor(148500,  0,       9700,    1000,    148500,  1500,    9700,    0x007C, 0,  70, 0x0000)

    ChipFrameInfo(1976, 0)                                       # 0

    ScpFunction((
        "Function_0_7B8",          # 00, 0
        "Function_1_868",          # 01, 1
        "Function_2_F03",          # 02, 2
        "Function_3_10DF",         # 03, 3
        "Function_4_13A1",         # 04, 4
        "Function_5_176B",         # 05, 5
        "Function_6_1AE1",         # 06, 6
        "Function_7_238C",         # 07, 7
        "Function_8_25C4",         # 08, 8
        "Function_9_2699",         # 09, 9
        "Function_10_27FF",        # 0A, 10
        "Function_11_293E",        # 0B, 11
        "Function_12_2D55",        # 0C, 12
        "Function_13_2F29",        # 0D, 13
        "Function_14_30AB",        # 0E, 14
        "Function_15_32BF",        # 0F, 15
        "Function_16_33FA",        # 10, 16
        "Function_17_390E",        # 11, 17
        "Function_18_3A41",        # 12, 18
        "Function_19_3D6A",        # 13, 19
        "Function_20_3EB1",        # 14, 20
        "Function_21_40E3",        # 15, 21
        "Function_22_4243",        # 16, 22
        "Function_23_42FA",        # 17, 23
        "Function_24_4494",        # 18, 24
        "Function_25_4988",        # 19, 25
        "Function_26_4B31",        # 1A, 26
        "Function_27_4F3A",        # 1B, 27
        "Function_28_549B",        # 1C, 28
        "Function_29_5677",        # 1D, 29
        "Function_30_56A6",        # 1E, 30
        "Function_31_5DDA",        # 1F, 31
        "Function_32_5E39",        # 20, 32
        "Function_33_5E7B",        # 21, 33
        "Function_34_5EBB",        # 22, 34
        "Function_35_691A",        # 23, 35
        "Function_36_6921",        # 24, 36
        "Function_37_694A",        # 25, 37
        "Function_38_6C40",        # 26, 38
        "Function_39_6CB0",        # 27, 39
        "Function_40_6D05",        # 28, 40
        "Function_41_6D95",        # 29, 41
        "Function_42_6DEA",        # 2A, 42
        "Function_43_6E3F",        # 2B, 43
        "Function_44_6E94",        # 2C, 44
        "Function_45_6EE9",        # 2D, 45
        "Function_46_6F3E",        # 2E, 46
        "Function_47_86E2",        # 2F, 47
        "Function_48_872C",        # 30, 48
        "Function_49_877D",        # 31, 49
        "Function_50_87D2",        # 32, 50
        "Function_51_8827",        # 33, 51
        "Function_52_887C",        # 34, 52
        "Function_53_88D1",        # 35, 53
        "Function_54_8926",        # 36, 54
        "Function_55_897B",        # 37, 55
        "Function_56_8C13",        # 38, 56
        "Function_57_8EAB",        # 39, 57
        "Function_58_AEAF",        # 3A, 58
        "Function_59_B41F",        # 3B, 59
        "Function_60_B477",        # 3C, 60
        "Function_61_B4CC",        # 3D, 61
        "Function_62_B506",        # 3E, 62
        "Function_63_B5AA",        # 3F, 63
        "Function_64_B64E",        # 40, 64
        "Function_65_B6F2",        # 41, 65
        "Function_66_B796",        # 42, 66
        "Function_67_C8A5",        # 43, 67
        "Function_68_CC8B",        # 44, 68
        "Function_69_CF7B",        # 45, 69
        "Function_70_D212",        # 46, 70
    ))


    def Function_0_7B8(): pass

    label("Function_0_7B8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_7F0"),
        (1, "loc_7FC"),
        (2, "loc_808"),
        (3, "loc_814"),
        (4, "loc_820"),
        (5, "loc_82C"),
        (6, "loc_838"),
        (SWITCH_DEFAULT, "loc_844"),
    )


    label("loc_7F0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_850")

    label("loc_7FC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_850")

    label("loc_808")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_850")

    label("loc_814")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_850")

    label("loc_820")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_850")

    label("loc_82C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_850")

    label("loc_838")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_850")

    label("loc_844")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_850")

    label("loc_850")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_867")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_850")

    label("loc_867")

    Return()

    # Function_0_7B8 end

    def Function_1_868(): pass

    label("Function_1_868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 4)), scpexpr(EXPR_END)), "loc_876")
    Jump("loc_E34")

    label("loc_876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_BA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_911")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 22570, 0, 1190, 180)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 337170, 0, 1160, 89)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xF, 338100, 0, 12950, 270)
    SetChrPos(0x11, 337100, 0, 12950, 90)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x16, 331320, 0, 2060, 90)
    SetChrPos(0x10, 332320, 0, 2060, 270)
    Jump("loc_A1A")

    label("loc_911")

    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x9, 35270, 0, -1190, 270)
    SetChrPos(0xD, 34300, 0, 420, 135)
    SetChrPos(0x11, 33320, 0, -1250, 90)
    SetChrPos(0x16, 34270, 0, -2590, 45)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99F")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xC, 331320, 0, 2060, 90)
    SetChrPos(0x10, 332820, 0, 2060, 270)

    label("loc_99F")

    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0xE, 335410, 150, 4740, 270)
    SetChrPos(0x15, 335610, 150, 6960, 270)
    SetChrChipByIndex(0xE, 0x19)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0x15, 0x1A)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrSubChip(0xE, 0x2)
    SetChrSubChip(0x15, 0x1)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 337580, 0, 13090, 0)
    SetChrFlags(0xF, 0x10)

    label("loc_A1A")

    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 275320, 0, 13650, 89)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 275390, 0, 6760, 90)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 266920, 0, 11330, 45)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x17, 206870, 0, 11800, 135)
    SetChrPos(0x1A, 207940, 0, 10900, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9C")
    SetChrFlags(0x17, 0x10)
    SetChrFlags(0x1A, 0x10)

    label("loc_A9C")

    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 208140, 0, 9500, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_B62")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0xC, 142060, 150, 5790, 225)
    SetChrPos(0x8, 140450, 150, 6350, 185)
    SetChrPos(0x1F, 138590, 150, 5700, 125)
    SetChrChipByIndex(0xC, 0x18)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrChipByIndex(0x1F, 0x15)
    SetChrSubChip(0x1F, 0x0)
    EndChrThread(0x1F, 0x0)
    SetChrBattleFlags(0x1F, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x1F, 0x10)
    SetChrSubChip(0xC, 0x2)
    SetChrSubChip(0x1F, 0x1)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -15420, 0, 20630, 90)
    Jump("loc_B9F")

    label("loc_B62")

    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 140450, 150, 6350, 185)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -15420, 0, 20630, 90)

    label("loc_B9F")

    Jump("loc_E34")

    label("loc_BA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_E34")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 22570, 0, 1190, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, 335770, 0, 2880, 90)
    SetChrPos(0xE, 337270, 0, 2880, 270)
    SetChrPos(0xD, 336790, 0, 830, 0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 332390, 150, 4870, 90)
    SetChrPos(0x16, 332390, 150, 7060, 90)
    SetChrChipByIndex(0x16, 0x1B)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    SetChrChipByIndex(0x15, 0x1A)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrSubChip(0x16, 0x2)
    SetChrSubChip(0x15, 0x1)
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xF, 337050, 0, 11080, 90)
    SetChrPos(0x10, 338550, 0, 11080, 270)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 331310, 150, 12280, 180)
    SetChrChipByIndex(0x11, 0x16)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 274320, 0, 9760, 315)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 275320, 0, 13650, 89)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x19, 0x17)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrPos(0x19, 272550, 150, 4750, 270)
    SetChrSubChip(0x19, 0x2)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x11)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0xA, 269050, 0, 10840, 90)
    SetChrSubChip(0xA, 0x1)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x12, 265570, 0, 2540, 0)
    SetChrPos(0x13, 265570, 0, 3940, 180)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1A, 208530, 0, 11590, 180)
    SetChrPos(0x1B, 208530, 0, 9990, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 140990, 150, 12360, 180)
    SetChrChipByIndex(0xB, 0x1C)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -15420, 0, 20630, 90)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1C, 136970, 0, -1250, 180)
    SetChrPos(0x1D, 136970, 0, -2550, 0)
    SetChrFlags(0x1C, 0x10)
    SetChrFlags(0x1D, 0x10)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 147710, 0, -850, 89)

    label("loc_E34")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E5E")
    ClearScenarioFlags(0x25, 1)
    Call(0, 35)

    label("loc_E5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E72")
    ClearScenarioFlags(0x22, 0)
    Event(0, 37)
    Jump("loc_EBD")

    label("loc_E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_E86")
    ClearScenarioFlags(0x22, 1)
    Event(0, 46)
    Jump("loc_EBD")

    label("loc_E86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_E9A")
    ClearScenarioFlags(0x22, 2)
    Event(0, 57)
    Jump("loc_EBD")

    label("loc_E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_EAE")
    ClearScenarioFlags(0x22, 3)
    Event(0, 58)
    Jump("loc_EBD")

    label("loc_EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_EBD")
    ClearScenarioFlags(0x22, 4)
    Event(0, 66)

    label("loc_EBD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EDB")
    Event(0, 55)

    label("loc_EDB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F02")
    Event(0, 56)

    label("loc_F02")

    Return()

    # Function_1_868 end

    def Function_2_F03(): pass

    label("Function_2_F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F18")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F2C")
    VolumeBGM(0x46, 0xC8)

    label("loc_F2C")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F44")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_F44")

    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x11, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FCE")
    ClearChrFlags(0x28, 0x80)
    OP_78(0xD, 0x28)
    ClearChrFlags(0x28, 0x40)
    ClearChrFlags(0x2A, 0x80)
    OP_78(0xF, 0x2A)
    ClearChrFlags(0x2A, 0x40)
    SetChrPos(0x28, 142300, 0, 6000, 45)
    OP_D5(0x28, 0x0, 0xAFC8, 0x0, 0x0)
    SetChrPos(0x2A, 138600, 0, 6000, 315)
    OP_D5(0x2A, 0x0, 0x4CE78, 0x0, 0x0)

    label("loc_FCE")

    ClearMapObjFlags(0x3, 0x10)
    ClearMapObjFlags(0x4, 0x10)
    ClearMapObjFlags(0x5, 0x10)
    ClearMapObjFlags(0x6, 0x10)
    ClearMapObjFlags(0x7, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_100C")
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x7, 0x4)

    label("loc_100C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_102B")
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    OP_65(0x2, 0x1)

    label("loc_102B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_END)), "loc_105E")
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0xC, 0x10)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0xC, 0x4)

    label("loc_105E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10A3")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_10A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10DE")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)

    label("loc_10DE")

    Return()

    # Function_2_F03 end

    def Function_3_10DF(): pass

    label("Function_3_10DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_121F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AC")

    #C0001
    ChrTalk(
        0xFE,
        (
            "記者の方たちも上階への進入は\x01",
            "ようやく諦めてくれたようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "ふう、しかし\x01",
            "職業柄というか何というか……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "記者のああいった強引な行動は\x01",
            "どこの国でも同じなんですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_121A")

    label("loc_11AC")


    #C0004
    ChrTalk(
        0xFE,
        (
            "ふう、しかし\x01",
            "職業柄というか何というか……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "記者のああいった強引な行動は\x01",
            "どこの国でも同じなんですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121A")

    Jump("loc_139D")

    label("loc_121F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_122D")
    Jump("loc_139D")

    label("loc_122D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_139D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1312")

    #C0006
    ChrTalk(
        0xFE,
        (
            "こちらは各国から招待された\x01",
            "報道記者の控え室です。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "会議の進行中は原則、\x01",
            "報道陣は控え室の外に出られない\x01",
            "決まりとなっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "今は皆さんお集まりなので、\x01",
            "どうぞ中へ入ってご確認ください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_139D")

    label("loc_1312")


    #C0009
    ChrTalk(
        0xFE,
        (
            "こちらは、各国から招待された\x01",
            "報道記者の控え室です。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "会議の進行中は原則、\x01",
            "報道陣は控え室の外に出られない\x01",
            "決まりとなっております。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_139D")

    TalkEnd(0xFE)
    Return()

    # Function_3_10DF end

    def Function_4_13A1(): pass

    label("Function_4_13A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_13B5")
    Call(0, 6)
    Jump("loc_1767")

    label("loc_13B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_1745")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16BF")

    #C0011
    ChrTalk(
        0xC,
        (
            "#02100Fあらロイド君たち。\x01",
            "警備の方は大丈夫そう？\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00002Fええまあ、今のところは。\x02\x03",

            "グレイスさんこそ\x01",
            "合同取材はどうでしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xC,
        (
            "#02102Fふふ、そうね～。\x01",
            "おかげ様で成果は上々よ。\x02\x03",

            "とりあえず、思っていたより\x01",
            "前向きな記事が書けそうかな？\x02\x03",

            "#02109Fあとは、もう少し大衆受けする\x01",
            "ネタでもあればいいんだけどね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#00006Fあの、判ってると思いますが……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        (
            "#00106Fくれぐれも余計な場所には\x01",
            "顔を出さないで下さいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xC,
        (
            "#02104F大丈夫、その辺りは\x01",
            "ちゃんとレインズ君にも――\x02\x03",

            "#02101Fじゃなくて、\x01",
            "ルールはちゃんと守るから。\x02\x03",

            "#02109Fお姉さんたちのことなら\x01",
            "なーんにも心配いらないわよ？\x02",
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

    #C0017
    ChrTalk(
        0x101,
        "#00006F（はぁ、心配だ……）\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        "#00106F（ええ、心配ね……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 1)
    Jump("loc_1740")

    label("loc_16BF")


    #C0019
    ChrTalk(
        0xC,
        (
            "#02109Fルールなら\x01",
            "ちゃんと守るから安心してね～。\x02\x03",

            "#02100Fさてと、一度\x01",
            "通信社に連絡を入れたら\x01",
            "休憩室の方にでも行こうかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1740")

    Jump("loc_1767")

    label("loc_1745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_1767")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1764")
    TalkEnd(0xFE)
    Call(0, 34)
    Return()

    label("loc_1764")

    Call(0, 5)

    label("loc_1767")

    TalkEnd(0xFE)
    Return()

    # Function_4_13A1 end

    def Function_5_176B(): pass

    label("Function_5_176B")

    OP_4B(0xC, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19BD")

    #C0020
    ChrTalk(
        0xC,
        (
            "#02100Fそれで、ナイアルさんたちは\x01",
            "こちらへは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xE,
        (
            "ええ、共和国方面の取材が\x01",
            "手の離せない状態らしくって\x01",
            "急に来られなくなったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xE,
        (
            "今はあちらはあちらで、\x01",
            "少し良くない状況らしいから。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xC,
        (
            "#02103Fなるほど、それって例の\x01",
            "民族主義の過激派連中ですよね。\x02\x03",

            "#02101F今回の通商会議でも何らかの\x01",
            "動きを見せるんじゃないかって\x01",
            "小耳には挟みましたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xE,
        (
            "ふふ、貴女も伊達に\x01",
            "記者をやっていないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xE,
        (
            "確かにそういう話もあるわね。\x01",
            "もっとも確証はないけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#00001F（グレイスさんの所にも\x01",
            "  そんな情報が……）\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#00303F（とにかく、\x01",
            "  警戒を続けねえとな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1AD8")

    label("loc_19BD")


    #C0028
    ChrTalk(
        0xC,
        (
            "#02100Fそうだ、ノティシアさん。\x01",
            "今度ナイアルさんに会ったら\x01",
            "よろしく伝えておいてくれますか。\x02\x03",

            "『フューリッツァ賞の受賞、\x01",
            "  おめでとうございます。\x01",
            "  次こそ私が頂きます』って。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xE,
        (
            "ふふ、そういえば貴女\x01",
            "ナイアル君と面識があったって\x01",
            "話だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xE,
        "ええ、バッチリ伝えておくわ。\x02",
    )

    CloseMessageWindow()

    label("loc_1AD8")

    OP_4C(0xC, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_5_176B end

    def Function_6_1AE1(): pass

    label("Function_6_1AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB8")

    #C0031
    ChrTalk(
        0x1F,
        (
            "#11505Fなるほど、熊ヒゲ先生は\x01",
            "コーヒー党ですか。\x02\x03",

            "#11500F宰相閣下と気が合いそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "#02200Fふむ、閣下もよくコーヒーを？\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x1F,
        (
            "#11503Fええ、それもブラックでがぶがぶ。\x02\x03",

            "#11502Fだからいつも\x01",
            "あんな風に目がギンギンに\x01",
            "冴えているんだと思いますよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0034
    ChrTalk(
        0x8,
        "#02202Fな、なるほど……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xC,
        "#02109Fふふ、確かに納得はできますね。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#00005F（な、何かすごい\x01",
            "  組み合わせだなぁ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        (
            "#00206F（ええ……\x01",
            "  かなり濃ゆいですね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 2)
    Jump("loc_238B")

    label("loc_1CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2052")

    #C0038
    ChrTalk(
        0xC,
        (
            "#02104Fふむふむ、オズボーン宰相は\x01",
            "コーヒー党、と……\x02\x03",

            "#02100Fで、レクターさんはどうなんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x1F,
        (
            "#11510Fんー、自分はどちらかと言うと\x01",
            "紅茶党ですが。\x02\x03",

            "#11500Fたかが二等書記官の嗜好を\x01",
            "聞いてどうするつもりですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xC,
        (
            "#02109Fいや～、なかなか\x01",
            "甘いマスクをお持ちなので\x01",
            "ツバでもつけておこうかと思いまして。\x02\x03",

            "#02102Fなんといっても、美男美女は\x01",
            "それだけで記事の華になりますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x1F,
        (
            "#11509Fはは、なるほど。\x01",
            "嬉しいことを言ってくれますね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 0)), scpexpr(EXPR_END)), "loc_1F61")

    #C0042
    ChrTalk(
        0x101,
        (
            "#00006F（う～ん、あからさまに\x01",
            "  上辺の会話って感じだな。）\x02\x03",

            "#00001F（グレイスさんも\x01",
            "  レクターさんの事はある程度\x01",
            "  掴んでいるみたいだったし……）\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x105,
        (
            "#10302F（フフ、虚実入り混じりの\x01",
            "  探り合いってところかな？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_204A")

    label("loc_1F61")


    #C0044
    ChrTalk(
        0x101,
        (
            "#00006F（う～ん、あからさまに\x01",
            "  上辺の会話って感じだな。）\x02\x03",

            "#00001F（グレイスさんもレクターさんが\x01",
            "  ただの書記官じゃないことくらいは\x01",
            "  分かっているだろうし……）\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x105,
        (
            "#10302F（フフ、虚実入り混じりの\x01",
            "  探り合いってところかな？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_204A")

    SetScenarioFlags(0x1C1, 3)
    Jump("loc_238B")

    label("loc_2052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B3")

    #C0046
    ChrTalk(
        0x1F,
        (
            "#11501Fそうそう熊ヒゲ先生、\x01",
            "実は先生に相談したいことが\x01",
            "あるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        "#02205Fふむ、なんでしょう？\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x1F,
        (
            "#11506Fいや～、実はちょっと\x01",
            "職場のことで悩んでいましてね。\x02\x03",

            "人権問題で有名な\x01",
            "熊ヒゲ先生の見解を一度\x01",
            "お伺いしたいと思っていたんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "#02202Fそうですか……\x01",
            "まあ流石に今は無理ですが。\x02\x03",

            "よければまた改めて\x01",
            "事務所の方に連絡して下さい。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0050
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "イアン弁護士はレクター書記官に\x01",
            "名刺を差し出した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0051
    ChrTalk(
        0x1F,
        "#11509Fおお、助かります。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#00001F（なるほど、こうやって\x01",
            "  人脈を広げているんだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        (
            "#00103F（まあ、こういう外向性も\x01",
            "  諜報員には必要な\x01",
            "  スキルでしょうからね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 4)
    Jump("loc_238B")

    label("loc_22B3")


    #C0054
    ChrTalk(
        0x1F,
        "#11500Fそれで、熊ヒゲ先生……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        "#02202Fええ、それは……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xC,
        "#02100Fふむふむ、なるほど……\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#00003F（……３人の会話をずっと\x01",
            "  聞いているわけにもいかないな。）\x02\x03",

            "（これ以上、\x01",
            "  踏み込むのは止めておこう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_238B")

    Return()

    # Function_6_1AE1 end

    def Function_7_238C(): pass

    label("Function_7_238C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_2415")

    #C0058
    ChrTalk(
        0xFE,
        (
            "ふう、やっぱりＶＩＰフロアに\x01",
            "潜入しようだなんて無茶だったなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "……それにしても先輩、\x01",
            "どこに行ったんだろう？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C0")

    label("loc_2415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2423")
    Jump("loc_25C0")

    label("loc_2423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_25C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2442")
    TalkEnd(0xFE)
    Call(0, 34)
    Return()

    label("loc_2442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2528")

    #C0060
    ChrTalk(
        0xFE,
        (
            "リベール通信の天才カメラマン、\x01",
            "ドロシー・ハイアット……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "彼女の撮る写真は、何ていうか\x01",
            "すごく生き生きとしていて\x01",
            "見る者を惹き付けるんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "カメラマンとして是非お話を\x01",
            "聞いてみたかったんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_25C0")

    label("loc_2528")


    #C0063
    ChrTalk(
        0xFE,
        (
            "う～ん、今度リベールに\x01",
            "旅行に行った時にでも\x01",
            "通信社を訪ねてみようかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "確かルーアンから王都までは\x01",
            "それほど時間も\x01",
            "かからなかったはずだし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C0")

    TalkEnd(0xFE)
    Return()

    # Function_7_238C end

    def Function_8_25C4(): pass

    label("Function_8_25C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2673")

    #C0065
    ChrTalk(
        0xFE,
        (
            "ま、両国の思惑はさておいても\x01",
            "会議前半の成果は\x01",
            "それはそれで喜ぶべきことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "大陸経済の活性化は、\x01",
            "リベールやレミフェリアにとっても\x01",
            "前向きな話だしね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2695")

    label("loc_2673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2695")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2692")
    TalkEnd(0xFE)
    Call(0, 34)
    Return()

    label("loc_2692")

    Call(0, 5)

    label("loc_2695")

    TalkEnd(0xFE)
    Return()

    # Function_8_25C4 end

    def Function_9_2699(): pass

    label("Function_9_2699")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2737")

    #C0067
    ChrTalk(
        0xFE,
        (
            "ふむ、２大国がここまで\x01",
            "自治州の提案に歩み寄るなんて\x01",
            "本当に珍しいことですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "確かに自治州の利は\x01",
            "２大国の利に直結するわけですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27FB")

    label("loc_2737")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_27FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2752")
    Call(0, 10)
    Jump("loc_27FB")

    label("loc_2752")


    #C0069
    ChrTalk(
        0xFE,
        (
            "しかし、このオルキスタワーは\x01",
            "まったくとんでもない建物ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "レミフェリアは流石に無理ですが、\x01",
            "共和国でもアルタイル市からなら\x01",
            "バッチリ見えるんじゃないですか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27FB")

    TalkEnd(0xFE)
    Return()

    # Function_9_2699 end

    def Function_10_27FF(): pass

    label("Function_10_27FF")


    #C0071
    ChrTalk(
        0x15,
        (
            "改めまして、アーデントプレスの\x01",
            "トンプソンと言います。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x15,
        (
            "貴方はタイレル通信の\x01",
            "カメラマンさんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x16,
        "ええ、まだまだ弱輩ですが。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x16,
        (
            "アーデントということは、\x01",
            "レミフィリアの方ですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x16,
        (
            "国が違えば競争もなし――\x01",
            "今日は共同戦線でお願いしますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x15,
        (
            "はは、そうですね。\x01",
            "こちらこそ宜しくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_10_27FF end

    def Function_11_293E(): pass

    label("Function_11_293E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_2A78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A05")

    #C0077
    ChrTalk(
        0xFE,
        (
            "ふう、会議前半の整理も\x01",
            "ようやく落ち着きましたかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "ですが、後半からは\x01",
            "さらに突っ込んだ内容について\x01",
            "議論がなされるはず……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        "まだまだ本番はこれからですね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2A73")

    label("loc_2A05")


    #C0080
    ChrTalk(
        0xFE,
        (
            "会議の後半からは\x01",
            "さらに突っ込んだ内容について\x01",
            "議論がなされるはず……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        "まだまだ本番はこれからですね。\x02",
    )

    CloseMessageWindow()

    label("loc_2A73")

    Jump("loc_2D51")

    label("loc_2A78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2C8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C07")
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0082
    ChrTalk(
        0xFE,
        (
            "そうです、その件についても\x01",
            "各国の合意は得られたとのことで……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        "では、その内容で本社に報告を……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#00000F（エニグマで誰かと\x01",
            "  通信しているみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        (
            "#00100F（おそらく、タワーの外に\x01",
            "  記者仲間がいるんでしょうね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x105,
        (
            "#10302F（フフ、一分一秒でも早く\x01",
            "  通商会議の情報を、か……）\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        "#00303F（なんつうか、ご苦労なこったな。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2C88")

    label("loc_2C07")

    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0088
    ChrTalk(
        0xFE,
        (
            "そうです、その件についても\x01",
            "各国の合意は得られたとのことで……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        "では、その内容で本社に報告を……\x02",
    )

    CloseMessageWindow()

    label("loc_2C88")

    Jump("loc_2D51")

    label("loc_2C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2D51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA8")
    Call(0, 12)
    Jump("loc_2D51")

    label("loc_2CA8")


    #C0090
    ChrTalk(
        0xFE,
        (
            "フフ、それを言うなら\x01",
            "ロックスミス大統領も然りですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        "百聞は一見にしかず――\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "普段タイレル通信の記事から\x01",
            "受ける印象以上に、\x01",
            "堂々とした風格を感じましたよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D51")

    TalkEnd(0xFE)
    Return()

    # Function_11_293E end

    def Function_12_2D55(): pass

    label("Function_12_2D55")

    OP_4B(0x10, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0093
    ChrTalk(
        0x10,
        (
            "いや～、それにしても\x01",
            "今度の会議は何もかもが\x01",
            "規格外ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x10,
        (
            "２国間の会議は数あれど、\x01",
            "今回は自治州と周辺４ヶ国……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x10,
        (
            "しかも、あのオズボーン宰相と\x01",
            "ロックスミス大統領が\x01",
            "直接会談することになろうとは。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xF,
        (
            "それに何と言いましても\x01",
            "２人が実際に顔を合わせたのは\x01",
            "今回が初めてですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xF,
        (
            "今日はまさしく、\x01",
            "歴史的な一日になるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x10,
        "ええ、まったくです。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x10,
        (
            "貴方がた帝国時報を始め\x01",
            "各国記者も揃い踏み――\x01",
            "取材にも気合いが入りますよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_12_2D55 end

    def Function_13_2F29(): pass

    label("Function_13_2F29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_2FC7")

    #C0100
    ChrTalk(
        0xFE,
        (
            "ＶＩＰフロアの取材が\x01",
            "できなかったのは残念ですが……\x01",
            "まだ取材の機会はありますからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "記者質問の要綱を\x01",
            "改めて見直しておかなければ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A7")

    label("loc_2FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2FD5")
    Jump("loc_30A7")

    label("loc_2FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_30A7")

    #C0102
    ChrTalk(
        0xFE,
        (
            "様々な方面でクロスベル警察は\x01",
            "よく無能と評価されがちですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "ビル内の警備を見る限り、\x01",
            "存外優秀な組織という印象を受けますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "問題は人ではなく自治州の構造……\x01",
            "そう強く感じさせられます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30A7")

    TalkEnd(0xFE)
    Return()

    # Function_13_2F29 end

    def Function_14_30AB(): pass

    label("Function_14_30AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_312A")

    #C0105
    ChrTalk(
        0xFE,
        (
            "さてと、そうこうしている間に\x01",
            "休憩時間も終わりですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "会議の後半に向けて\x01",
            "そろそろ準備を始めないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32BB")

    label("loc_312A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_3222")

    #C0107
    ChrTalk(
        0xFE,
        (
            "こと経済関連の協定に関しては、\x01",
            "目を見張る成果が出たと言えるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "この辺り、流石に提案者が\x01",
            "ＩＢＣ総裁を兼任されている\x01",
            "ディーター市長なだけはある。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "経済の発展が大陸の安定を促す……\x01",
            "あながち夢物語ではない気がします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32BB")

    label("loc_3222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_32BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_323D")
    Call(0, 12)
    Jump("loc_32BB")

    label("loc_323D")


    #C0110
    ChrTalk(
        0xFE,
        (
            "それにしても……\x01",
            "オズボーン宰相の迫力は本物ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "写真で見るのとはワケが違う。\x01",
            "色んなことに合点が行った気分です。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32BB")

    TalkEnd(0xFE)
    Return()

    # Function_14_30AB end

    def Function_15_32BF(): pass

    label("Function_15_32BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_3315")

    #C0112
    ChrTalk(
        0xFE,
        (
            "休憩時間もそろそろ終わり……\x01",
            "今の内に飲み物でも買ってくるかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F6")

    label("loc_3315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_3323")
    Jump("loc_33F6")

    label("loc_3323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_33F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_333E")
    Call(0, 10)
    Jump("loc_33F6")

    label("loc_333E")


    #C0113
    ChrTalk(
        0xFE,
        (
            "ええ、天気の良い日は\x01",
            "それはもうくっきりと。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "おかげで、アルタイル市に\x01",
            "訪れる観光客の数も若干\x01",
            "増えたと言いますからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "このタワーの経済効果には\x01",
            "凄まじいものがありますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33F6")

    TalkEnd(0xFE)
    Return()

    # Function_15_32BF end

    def Function_16_33FA(): pass

    label("Function_16_33FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_34B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3418")
    Call(0, 17)
    Jump("loc_34AE")

    label("loc_3418")


    #C0116
    ChrTalk(
        0x17,
        (
            "#00600Fああ、お前たちか。\x02\x03",

            "まだ時間はあるとはいえ、\x01",
            "両首脳の元へはなるべく早く\x01",
            "向かうようにな。\x02\x03",

            "当然だが、あまり\x01",
            "待たせるわけにもいかんからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34AE")

    Jump("loc_390A")

    label("loc_34B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_390A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_387E")

    #C0117
    ChrTalk(
        0x17,
        (
            "#00600Fお前たちか。\x02\x03",

            "何か異常はないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        "#00000Fはい、今のところは。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x102,
        (
            "#00100Fこのモニターで警備全体の\x01",
            "様子を俯瞰しているんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x17,
        (
            "#00603Fああ、会議場はもちろん\x01",
            "オスキスタワーの要所要所が\x01",
            "リアルタイムで確認できる。\x02\x03",

            "#00600Fこのビルに備えられた、\x01",
            "最新の防犯カメラシステムでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x103,
        (
            "#00203F防犯カメラ……ＩＢＣを始め\x01",
            "オーバルストアなどでも\x01",
            "運用されている技術ですね。\x02\x03",

            "#00200Fもっとも、こちらは\x01",
            "台数が桁違いのようですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x104,
        (
            "#00306Fしれっと言ってるが、\x01",
            "何気に凄いテクノロジーだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、いずれは街の外でも\x01",
            "こうやって監視されたりしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x109,
        (
            "#10106Fう～ん、その辺は市民の理解を\x01",
            "得られるかが微妙な気はするけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x17,
        (
            "#00603F……とにかく、利用できるものは\x01",
            "最大限に利用するだけだ。\x02\x03",

            "#00601Fテロリストの動向が掴めない以上、\x01",
            "ヤツらが行動を起こす直前、\x01",
            "もしくはその直後を叩くしかない。\x02\x03",

            "そのためには、どんな些細な情報も\x01",
            "見過ごすことはできないからな。\x02\x03",

            "何かあれば、すぐに連絡して来い。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        "#00001Fええ、了解です。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 5)
    Call(0, 36)
    Jump("loc_390A")

    label("loc_387E")


    #C0127
    ChrTalk(
        0x17,
        (
            "#00603F各方面とも常に連絡を取っているが、\x01",
            "まだ目立った問題は起きていない。\x02\x03",

            "#00600Fお前たちは引き続き、\x01",
            "当該フロアの警戒を続けてくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_390A")

    TalkEnd(0xFE)
    Return()

    # Function_16_33FA end

    def Function_17_390E(): pass

    label("Function_17_390E")

    OP_4B(0x17, 0xFF)
    OP_4B(0x1A, 0xFF)

    #C0128
    ChrTalk(
        0x17,
        (
            "#00600Fグラント一尉、現在の\x01",
            "中隊の様子はいかがですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x1A,
        (
            "勿論、皆それぞれ緊張感を\x01",
            "維持したまま待機していますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x1A,
        (
            "いついかなる時も有事に\x01",
            "備えるのが我々の務めですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x17,
        (
            "#00603Fなるほど、心強いことです。\x02\x03",

            "#00601Fでは、会議後半の\x01",
            "警官隊の配備についてですが――\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x17, 0xFF)
    OP_4C(0x1A, 0xFF)
    ClearChrFlags(0x17, 0x10)
    ClearChrFlags(0x1A, 0x10)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_17_390E end

    def Function_18_3A41(): pass

    label("Function_18_3A41")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_3BBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B29")

    #C0132
    ChrTalk(
        0xFE,
        (
            "市内・市外ともに、\x01",
            "現状特に変事は確認されていない。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "監視班の報告によれば、\x01",
            "《赤い星座》も《黒月》も\x01",
            "未だ動く気配はないとのことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "嵐の前の静けさと言うか……\x01",
            "正直、不気味で仕方がないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_3BBA")

    label("loc_3B29")


    #C0135
    ChrTalk(
        0xFE,
        (
            "監視班の報告によれば、\x01",
            "《赤い星座》も《黒月》も\x01",
            "未だ動く気配はないとのことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "嵐の前の静けさと言うか……\x01",
            "正直、不気味で仕方がないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BBA")

    Jump("loc_3D66")

    label("loc_3BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_3D66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CC0")

    #C0137
    ChrTalk(
        0xFE,
        (
            "この警備対策室には、\x01",
            "各方面の情報が即座に集中する\x01",
            "体制が整っている。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "なお、ここにある導力端末は\x01",
            "限定的だが警察本部の\x01",
            "データベースとも繋がっていてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "必要があれば、\x01",
            "不審人物などの照会も\x01",
            "この場で行えるというわけだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_3D66")

    label("loc_3CC0")


    #C0140
    ChrTalk(
        0xFE,
        (
            "ここまでの体制が整えられたのは\x01",
            "ディーター市長の全面協力が\x01",
            "あったからこそだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "今回の警備体制はまさに\x01",
            "このクロスベルの総力……\x01",
            "だからこそ失敗は許されんのだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D66")

    TalkEnd(0xFE)
    Return()

    # Function_18_3A41 end

    def Function_19_3D6A(): pass

    label("Function_19_3D6A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_3E01")

    #C0142
    ChrTalk(
        0xFE,
        (
            "これだけ警戒活動を続けていて\x01",
            "まだ何も情報が得られないなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "テロリストたちは一体どこに\x01",
            "潜伏しているというのでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EAD")

    label("loc_3E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_3EAD")

    #C0144
    ChrTalk(
        0xFE,
        (
            "テロリストたちは、まだ一向に\x01",
            "その気配すら掴ませてくれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "この万全の体制を前に計画を\x01",
            "諦めた……だといいんですが、\x01",
            "とても楽観は出来ませんね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0x19, 0x2)
    Return()

    label("loc_3EAD")

    TalkEnd(0xFE)
    Return()

    # Function_19_3D6A end

    def Function_20_3EB1(): pass

    label("Function_20_3EB1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_4047")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FA9")

    #C0146
    ChrTalk(
        0xFE,
        (
            "休憩中にしろ会議中にしろ、\x01",
            "我々の警戒活動が緩むことはない。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "この万全の体制の中、\x01",
            "テロリストたちがどこをどう\x01",
            "突いてくるつもりなのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "想定パターンはいくつかあるが、\x01",
            "事が起これば臨機応変に動かないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4042")

    label("loc_3FA9")


    #C0149
    ChrTalk(
        0xFE,
        (
            "この万全の体制の中、\x01",
            "テロリストたちがどこをどう\x01",
            "突いてくるつもりなのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "想定パターンはいくつかあるが、\x01",
            "事が起これば臨機応変に動かないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4042")

    Jump("loc_40DF")

    label("loc_4047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_40DF")

    #C0151
    ChrTalk(
        0xFE,
        (
            "こうしてモニターを見ていると、\x01",
            "みんな真剣に警戒しているのが\x01",
            "伝わってくるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "テロリストか……\x01",
            "杞憂で済めば世話がないんだが。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0xA, 0x1)
    Return()

    label("loc_40DF")

    TalkEnd(0xFE)
    Return()

    # Function_20_3EB1 end

    def Function_21_40E3(): pass

    label("Function_21_40E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41B8")

    #C0153
    ChrTalk(
        0xFE,
        (
            "オルキスタワーの警備は、\x01",
            "我々警護課の人間が総出で\x01",
            "行っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "我々は常に有事に備えて\x01",
            "訓練している実戦派ですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "いざという時は警備隊にも\x01",
            "遅れを取らない自信がありますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_423F")

    label("loc_41B8")


    #C0156
    ChrTalk(
        0xFE,
        (
            "我々警護課の人間は\x01",
            "常に有事に備えて訓練している\x01",
            "実戦派ですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "いざという時は警備隊にも\x01",
            "遅れを取らない自信がありますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_423F")

    TalkEnd(0xFE)
    Return()

    # Function_21_40E3 end

    def Function_22_4243(): pass

    label("Function_22_4243")

    TalkBegin(0xFE)

    #C0158
    ChrTalk(
        0xFE,
        (
            "俺たちは普段、政府関連の\x01",
            "重要設備の警備や各種要人の\x01",
            "警護などを担当しているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "記念祭の時もそうだったが、\x01",
            "こういった国際行事の警備も\x01",
            "重要な仕事の１つってワケだな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_4243 end

    def Function_23_42FA(): pass

    label("Function_23_42FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_43F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4318")
    Call(0, 17)
    Jump("loc_43EB")

    label("loc_4318")


    #C0160
    ChrTalk(
        0xFE,
        (
            "ふむ、もしこのまま\x01",
            "休憩時間に現れないとなると、\x01",
            "残る山場は会議の後半とそれ以降か。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "ま、だが\x01",
            "あれこれ考えすぎても仕方ない。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "とにかく俺たちは、\x01",
            "その時その時において\x01",
            "最善を尽くせるよう備えるだけだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43EB")

    Jump("loc_4490")

    label("loc_43F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4490")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_440B")
    Call(0, 24)
    Jump("loc_4490")

    label("loc_440B")


    #C0163
    ChrTalk(
        0xFE,
        (
            "しかし、どうでもいいが\x01",
            "この部屋は２人だと持て余すな。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "何ていうか……\x01",
            "オルキスタワーってのは\x01",
            "何もかもスケールが桁違いだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4490")

    TalkEnd(0xFE)
    Return()

    # Function_23_42FA end

    def Function_24_4494(): pass

    label("Function_24_4494")

    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    TurnDirection(0x1A, 0x0, 500)
    TurnDirection(0x1B, 0x0, 500)

    #C0165
    ChrTalk(
        0x109,
        "#10100Fグラント一尉、お疲れ様です。\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x104,
        "#00300Fどうも、お疲れ様ッス。\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x1A,
        "シーカー曹長にオルランド軍曹か。\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x1A,
        (
            "いやすまない、\x01",
            "今はどちらも警備隊に\x01",
            "所属しているわけではなかったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x109,
        (
            "#10100Fいえ、確かに出向中ですが\x01",
            "呼びやすい形で結構ですので。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x104,
        "#00302Fはは、俺も別に何でもいいッスよ。\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#00000Fこちらは……\x01",
            "お２人だけなんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x1B,
        (
            "はい、各国首脳や報道陣の\x01",
            "手前がありますからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x1B,
        (
            "警備隊の露出は極力\x01",
            "避けるべきとの判断から、\x01",
            "最小限の配備となっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x102,
        "#00101Fそれはつまり……\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x109,
        (
            "#10101Fええ、２大国への配慮です。\x02\x03",

            "警備隊は自治州法により\x01",
            "軍備を制限されているものの\x01",
            "いわゆる軍に相当する機関……\x02\x03",

            "制限の範囲内とはいえ、\x01",
            "隊の維持や装備の拡充などに\x01",
            "多額の予算を使っています。\x02\x03",

            "#10108Fなので、このような\x01",
            "会議の場では槍玉に挙げられやすい\x01",
            "議題の１つなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x103,
        (
            "#00203Fなるほど……\x01",
            "だから極力目に入らないように\x01",
            "努めるわけですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x105,
        (
            "#10306Fやれやれ、外交というヤツは\x01",
            "本当に面倒だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x1A,
        (
            "まあ確かにそうなんだが、\x01",
            "あまりそう言ってくれるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x1A,
        (
            "それに、これはあくまで\x01",
            "体裁の話だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x1A,
        (
            "代わりに、直下のフロアには\x01",
            "一個中隊がいつでも出動出来る\x01",
            "状態で待機している。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x1A,
        (
            "万一の際にはすぐさま\x01",
            "事に当たるから心配は無用だぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        "#00001Fなるほど、了解です。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x102,
        "#00101Fいざという時はお願いします。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    SetScenarioFlags(0x1C1, 6)
    Call(0, 36)
    Return()

    # Function_24_4494 end

    def Function_25_4988(): pass

    label("Function_25_4988")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_4A1B")

    #C0184
    ChrTalk(
        0xFE,
        (
            "会議も半分が終わりましたが、\x01",
            "どうやら状況に変化はないようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "テロリストの動きは\x01",
            "何とか未然に察知したい所ですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B2D")

    label("loc_4A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4B2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A36")
    Call(0, 24)
    Jump("loc_4B2D")

    label("loc_4A36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AC9")
    TurnDirection(0xFE, 0x109, 0)

    #C0186
    ChrTalk(
        0xFE,
        (
            "ノエル曹長、今日はお互いの\x01",
            "出来ることを尽くしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        "フロアの警戒は任せました。\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x109,
        "#10100Fはい、了解です。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_4B2D")

    label("loc_4AC9")

    TurnDirection(0xFE, 0x109, 0)

    #C0189
    ChrTalk(
        0xFE,
        (
            "ノエル曹長、今日はお互いの\x01",
            "出来ることを尽くしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        "フロアの警戒は任せました。\x02",
    )

    CloseMessageWindow()

    label("loc_4B2D")

    TalkEnd(0xFE)
    Return()

    # Function_25_4988 end

    def Function_26_4B31(): pass

    label("Function_26_4B31")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_4B42")
    Jump("loc_4F36")

    label("loc_4B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4F36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B5D")
    Call(0, 27)
    Jump("loc_4F36")

    label("loc_4B5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E5D")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4BF8")
    Jump("loc_4C42")

    label("loc_4BF8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C18")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C42")

    label("loc_4C18")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C38")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C42")

    label("loc_4C38")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C42")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    #C0191
    ChrTalk(
        0x101,
        (
            "#00001Fそういえば副局長、\x01",
            "さっき仰っていた\x01",
            "アイツというのは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x102,
        (
            "#00100Fええ、私も気になりました。\x01",
            "まさか不審人物の情報でも？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xB,
        "ん？　私の家内がどう――\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    #C0194
    ChrTalk(
        0xB,
        (
            "って、お前たちには\x01",
            "関係のない話だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xB,
        "は、早く職務に戻りたまえ！\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        "#11P#00005Fは、はい、分かりました。\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x104,
        (
            "#00306F（まさか、奥さんのことを\x01",
            "  考えてたのかよ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x103,
        (
            "#00203F（確か恐妻家でしたからね。\x01",
            "  ……色々あるんでしょう。）\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#00106F（そうね……\x01",
            "  そっとしておきましょう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1C2, 0)
    SetChrSubChip(0xB, 0x0)
    Jump("loc_4F36")

    label("loc_4E5D")

    SetChrSubChip(0xB, 0x0)

    #C0200
    ChrTalk(
        0xB,
        "ぐぬぬ、どいつもこいつも……\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xB,
        "私だって、私だってなぁ……\x02",
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
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_4F36")

    TalkEnd(0xFE)
    Return()

    # Function_26_4B31 end

    def Function_27_4F3A(): pass

    label("Function_27_4F3A")

    EventBegin(0x0)
    Fade(500)
    OP_68(142170, 1500, 10600, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 142170, 0, 10600, 315)
    SetChrPos(0x102, 144770, 0, 10800, 270)
    SetChrPos(0x104, 143580, 0, 11190, 270)
    SetChrPos(0x103, 143590, 0, 10390, 315)
    SetChrPos(0x109, 143190, 0, 9390, 315)
    SetChrPos(0x105, 145000, 0, 9790, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0202
    ChrTalk(
        0xB,
        (
            "むむぅ、まさかアイツ……\x01",
            "いや、断じてそのようなことは……\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        (
            "#11P#00005F（ア、アイツって誰だ……？）\x02\x03",

            "#00000Fえっと、ピエール副局長？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0204
    ChrTalk(
        0xB,
        "はっ！？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x1)

    #C0205
    ChrTalk(
        0xB,
        "だ、誰かと思ったら特務支援課か。\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xB,
        "何か私に用事かね？\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x103,
        "#00200Fあの、副局長はこちらで何を？\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        "#5P#00005Fお、おい、ティオ――\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(500)

    #C0209
    ChrTalk(
        0xB,
        (
            "何をしているも何も……\x01",
            "私は警備対策室の室長だ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0210
    ChrTalk(
        0x104,
        "#00305Fへえ、そうだったんスか……\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x105,
        (
            "#10300Fそういえば、もらった資料に\x01",
            "名前が書いてあった気がするね。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x103,
        "#00203F……なるほど、勉強不足でした。\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xB,
        "き、貴様ら……！\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        "#00006Fはぁ、遅かったか……\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x102,
        (
            "#00106F前もって\x01",
            "教えておくべきだったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x109,
        "#12P#10106Fた、確かに……\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、でもその室長さんが\x01",
            "なぜ対策室に顔を出さないんだい？\x02\x03",

            "合間の休憩、にも見えないけど？\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xB,
        (
            "フ、フン……現場の指揮権は\x01",
            "全てダドリー君に委ねてあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xB,
        (
            "そんな状況で私が\x01",
            "でしゃばった所で、かえって\x01",
            "やりづらくなるというものだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xB,
        (
            "どう思おうが勝手だが……\x01",
            "その点、私は弁えた上司なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xB,
        (
            "と、とにかく……お前たち。\x01",
            "ダドリー君の足をくれぐれも\x01",
            "引っ張らんようになっ。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x101,
        "#11P#00006Fりょ、了解です。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x1C1, 7)
    Call(0, 36)
    EventEnd(0x5)
    Return()

    # Function_27_4F3A end

    def Function_28_549B(): pass

    label("Function_28_549B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_54AF")
    Call(0, 6)
    Jump("loc_5673")

    label("loc_54AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_566A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55CF")

    #C0223
    ChrTalk(
        0x8,
        (
            "#02203Fふむ、経緯はどうあれ\x01",
            "両首脳に呼ばれるなんてね。\x02\x03",

            "#02200F当然緊張するだろうが……\x01",
            "こんな機会は滅多にないことだ。\x02\x03",

            "２人のオーラを間近で受けるだけで\x01",
            "かなり良い勉強になると思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        "#00001Fはい、そうですね。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x102,
        "#00100Fそれでは先生、行って来ます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_5665")

    label("loc_55CF")


    #C0226
    ChrTalk(
        0x8,
        (
            "#02200F私も会議で感じたが、\x01",
            "２人のオーラを間近で受けるだけで\x01",
            "かなり良い勉強になるはずだ。\x02\x03",

            "余計なことは考えずに、\x01",
            "とにかくぶつかって来るといい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5665")

    Jump("loc_5673")

    label("loc_566A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5673")

    label("loc_5673")

    TalkEnd(0xFE)
    Return()

    # Function_28_549B end

    def Function_29_5677(): pass

    label("Function_29_5677")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_568B")
    Call(0, 6)
    Jump("loc_56A2")

    label("loc_568B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_5699")
    Jump("loc_56A2")

    label("loc_5699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_56A2")

    label("loc_56A2")

    TalkEnd(0xFE)
    Return()

    # Function_29_5677 end

    def Function_30_56A6(): pass

    label("Function_30_56A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_5731")

    #C0227
    ChrTalk(
        0xFE,
        (
            "よく分からないけど……\x01",
            "イアン先生をはじめ、妙に\x01",
            "オーラのある人が集まっているな。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        "ただならない雰囲気を感じるよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DD6")

    label("loc_5731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_57B9")

    #C0229
    ChrTalk(
        0xFE,
        (
            "そういえば、ピエール副局長は\x01",
            "どこにいったんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "なかなか帰ってこないけど、\x01",
            "対策本部の方にでも行ったのかな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DD6")

    label("loc_57B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5DD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_583F")

    #C0231
    ChrTalk(
        0xFE,
        (
            "ピエール副局長、\x01",
            "さっきから何かぶつぶつ\x01",
            "言ってるみたいけど大丈夫かなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        "……気になって仕方ないよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DD6")

    label("loc_583F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D5E")

    #C0233
    ChrTalk(
        0xFE,
        (
            "君たち、どうやらピエール副局長と\x01",
            "話をしていたみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        "調子は大丈夫そうだったかい？\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        "#00012Fえ、えっと……\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x104,
        (
            "#00306Fあれを大丈夫と言うかどうかは\x01",
            "難しい問題だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x103,
        (
            "#00203Fまあ、いつも通りと言えば\x01",
            "いつも通りでしたが。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x102,
        (
            "#00106Fでも前は、あそこまで\x01",
            "卑屈な人でもなかったような\x01",
            "気はするんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "なるほど、卑屈か……\x01",
            "まあ、それも仕方ないんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "何といっても、ウチには\x01",
            "副局長の肩書きを持つ人間が\x01",
            "２人いるわけだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "前局長の解任を受けて\x01",
            "新しい局長に任命されたのは\x01",
            "もう一方の副局長だったんだからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x101,
        (
            "#00001F確かにそうでしたね。\x02\x03",

            "俺たちとは\x01",
            "全然、接点のない方だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "で、その新局長なんだが……\x01",
            "実はピエール副局長の\x01",
            "後輩だってのを知ってるかい？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0244
    ChrTalk(
        0x101,
        "#00005F新局長が……副局長の後輩？\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x109,
        "#10106Fなるほど、それで……\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "とはいえ、ピエールさんが\x01",
            "局長ってのは俺でもいまいち\x01",
            "想像が付かないからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "はっきり言って\x01",
            "妥当な人事だとは思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "それでも、同じ副局長……\x01",
            "おまけにキャリアが下の人間に\x01",
            "抜かれたんじゃ堪えるよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、確かに\x01",
            "それが当然の感情だろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "まあ、というわけで\x01",
            "あの人も色々と大変なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "だから、君たちもあの人と\x01",
            "接する時は心を広くっていうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "たとえ小言を言われても、\x01",
            "逆に気遣うくらいの\x01",
            "気持ちでいるといいと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        "#00012Fそ、そうですね……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C2, 1)
    Jump("loc_5DD6")

    label("loc_5D5E")


    #C0254
    ChrTalk(
        0xFE,
        (
            "ピエール副局長も、\x01",
            "ああ見えて色々と大変なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "口やかましい人ではあるけど、\x01",
            "こちらも我慢してあげないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DD6")

    TalkEnd(0xFE)
    Return()

    # Function_30_56A6 end

    def Function_31_5DDA(): pass

    label("Function_31_5DDA")

    TalkBegin(0xFE)
    OP_4B(0xFE, 0xFF)

    #C0256
    ChrTalk(
        0xFE,
        (
            "いいかい、会議の前半が\x01",
            "終わったらすぐに記者会見だ。\x01",
            "会場の準備は迅速にね。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_31_5DDA end

    def Function_32_5E39(): pass

    label("Function_32_5E39")

    TalkBegin(0xFE)
    OP_4B(0xFE, 0xFF)

    #C0257
    ChrTalk(
        0xFE,
        (
            "分かりました……\x01",
            "迅速にそして確実に、ですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_32_5E39 end

    def Function_33_5E7B(): pass

    label("Function_33_5E7B")

    TalkBegin(0xFE)

    #C0258
    ChrTalk(
        0xFE,
        (
            "さて弁当弁当、と……\x01",
            "ふう、やっと飯にありつけるぜ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_5E7B end

    def Function_34_5EBB(): pass

    label("Function_34_5EBB")

    EventBegin(0x0)
    OP_4B(0xC, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)
    Fade(500)
    OP_68(334710, 1500, 220, 0)
    MoveCamera(43, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 334710, 0, 220, 45)
    SetChrPos(0x102, 333800, 0, 1230, 45)
    SetChrPos(0x104, 335830, 0, -620, 45)
    SetChrPos(0x103, 332180, 0, 160, 45)
    SetChrPos(0x109, 333080, 0, -440, 45)
    SetChrPos(0x105, 334230, 0, -1120, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0xC, 0xE1, 0x0)
    OP_93(0xE, 0xE1, 0x0)
    OP_93(0xD, 0xE1, 0x0)
    OP_0D()

    #C0259
    ChrTalk(
        0xD,
        "皆さん、お疲れ様です。\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xC,
        (
            "#02110F来たわね、ロイド君たち。\x02\x03",

            "#02102Fいや～、しっかし\x01",
            "ついに本会議が始まったわね～。\x02\x03",

            "クロスベル自治州と周辺４ヶ国の\x01",
            "代表者が一同に会する、\x01",
            "まさに前代未聞の国際会議……\x02\x03",

            "そしてそんなビックイベントが、\x01",
            "史上初の超高層ビルディング・\x01",
            "オルキスタワーで行われる……\x02\x03",

            "#02109Fあまりの興奮と緊張感に\x01",
            "お姉さんの心臓は\x01",
            "今にも爆発しちゃいそうよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x101,
        (
            "#12P#00012F興奮はともかく\x01",
            "とても緊張しているようには\x01",
            "見えないのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x103,
        (
            "#6P#00200Fええ、何の変哲もない\x01",
            "いつものグレイスさんかと。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xC, 0x103, 500)

    #C0263
    ChrTalk(
        0xC,
        (
            "#02105Fあら、ティオちゃん。\x01",
            "久しぶりなのにグイグイ来るわね。\x02\x03",

            "#02104Fま、確かにドキドキより\x01",
            "ワクワクが上回るのは認める\x01",
            "ところけど……それはともかく。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xE, 500)

    #C0264
    ChrTalk(
        0xC,
        (
            "#02100F紹介するわね、ノティシアさん。\x01",
            "彼らが特務支援課よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xE,
        (
            "なるほど、この子たちがね。\x01",
            "ふふ、写真で見るより素敵じゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xE,
        (
            "リベール通信のノティシアよ。\x01",
            "今日はよろしくお願いするわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xE1, 0x1F4)

    #C0267
    ChrTalk(
        0x101,
        "#12P#00000Fええ、こちらこそ。\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x102,
        (
            "#6P#00100Fリベール通信――王国で\x01",
            "最もメジャーな報道機関ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xD,
        (
            "ええ、それと業界内では\x01",
            "もう１つ熱い話題がありまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xD,
        (
            "去年フューリッツァ賞を取った記者が\x01",
            "在籍していることでも有名なんです。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_649B")

    #C0271
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、あのニールセンって人も\x01",
            "かつて受賞した栄誉ある賞だね。\x02\x03",

            "毎年最も優秀な\x01",
            "ジャーナリストに贈られるっていう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6508")

    label("loc_649B")


    #C0272
    ChrTalk(
        0x105,
        (
            "#12P#10300Fフューリッツァ賞……\x02\x03",

            "確か、毎年最も優秀な\x01",
            "ジャーナリストに贈られる\x01",
            "栄誉ある賞のことだっけ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6508")


    #C0273
    ChrTalk(
        0xE,
        "#5Pふふ、よく知っているわね。\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xE,
        (
            "#5Pちなみに受賞者の名前は\x01",
            "ナイアル・バーンズと\x01",
            "ドロシー・ハイアット。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xE,
        (
            "#5P我がリベール通信社が誇る、\x01",
            "エース記者と天才カメラマンよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x104,
        (
            "#12P#00302Fへえ、しかしリベールの記者が\x01",
            "去年受賞したってことは……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x109,
        (
            "#6P#10105Fもしかして、昨年起こった\x01",
            "リベールの異変に関する報道が\x01",
            "評価されたんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xE,
        "#5Pええ、ご明察の通りよ。\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xE,
        (
            "#5Pま、厳密にはそれ以前の\x01",
            "スクープも含めて総合的な判断で\x01",
            "評価されたみたいだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x103,
        (
            "#6P#00203Fなるほど……\x01",
            "随分凄い記者さんのようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xC,
        (
            "#02109Fそう、あたしたちも\x01",
            "負けていられないって話なのよ。\x02\x03",

            "#02103F記者ならば、誰もが\x01",
            "一度は憧れるフューリッツァ賞……\x02\x03",

            "明日の栄冠のためにも\x01",
            "日々の取材、特に今回の取材は\x01",
            "うんっと大事にしないと。\x02\x03",

            "#02110Fだからレインズ君、\x01",
            "周りに出し抜かれないように\x01",
            "張り切って行くわよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x0, 0x1F4)

    #C0282
    ChrTalk(
        0xD,
        "イ、イエス・マム！\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x101,
        (
            "#12P#00012F（う～ん、いつも以上に\x01",
            "  気合い十分って感じだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x102,
        (
            "#6P#00106F（とりあえず、\x01",
            "  大人しくしていてくれると\x01",
            "  いいんだけど……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_93(0xC, 0x5A, 0x0)
    OP_93(0xE, 0x10E, 0x0)
    OP_93(0xD, 0x0, 0x0)
    SetScenarioFlags(0x1C2, 4)
    Call(0, 36)
    EventEnd(0x5)
    Return()

    # Function_34_5EBB end

    def Function_35_691A(): pass

    label("Function_35_691A")

    Sound(160, 0, 100, 0)
    Return()

    # Function_35_691A end

    def Function_36_6921(): pass

    label("Function_36_6921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6949")
    SetScenarioFlags(0x146, 3)

    label("loc_6949")

    Return()

    # Function_36_6921 end

    def Function_37_694A(): pass

    label("Function_37_694A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    CreatePortrait(0, 16, 192, 528, 256, 0, 20, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis504.itp")
    OP_68(81000, 1000, 4000, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 81000, 0, 5500, 180)
    SetChrPos(0x102, 81000, 0, 5500, 180)
    SetChrPos(0x103, 81000, 0, 5500, 180)
    SetChrPos(0x104, 81000, 0, 5500, 180)
    SetChrPos(0x109, 81000, 0, 5500, 180)
    SetChrPos(0x105, 81000, 0, 5500, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 81000, 0, 5500, 180)
    OP_A7(0x20, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(79000, 1000, 300, 5000)
    SetCameraDistance(18500, 5000)
    BeginChrThread(0x101, 0, 0, 38)
    FadeToBright(1000, 0)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)

    def lambda_6B0A():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6B0A)
    Sleep(50)

    def lambda_6B1A():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6B1A)
    Sleep(50)

    def lambda_6B2A():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6B2A)
    Sleep(50)

    def lambda_6B3A():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6B3A)
    Sleep(50)

    def lambda_6B4A():
        OP_93(0x105, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6B4A)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0285
    ChrTalk(
        0x102,
        "#5P#00102F#10Aすごい……\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_68(79000, 1000, -2700, 2000)
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    Sleep(500)

    def lambda_6BB3():
        OP_97(0xFE, 0x12C, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6BB3)
    Sleep(300)

    def lambda_6BD0():
        OP_93(0xFE, 0xB4, 0x15E)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_6BD0)

    def lambda_6BDD():
        OP_97(0xFE, 0x12C, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6BDD)
    Sleep(300)

    def lambda_6BFA():
        OP_97(0xFE, 0x12C, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6BFA)
    Sleep(300)

    def lambda_6C17():
        OP_97(0xFE, 0x12C, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C17)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_694A end

    def Function_38_6C40(): pass

    label("Function_38_6C40")

    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    BeginChrThread(0x20, 3, 0, 39)
    Sleep(900)
    BeginChrThread(0x101, 3, 0, 40)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 41)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 42)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 43)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 44)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 45)
    Sleep(1300)
    Sound(107, 0, 100, 0)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    Return()

    # Function_38_6C40 end

    def Function_39_6CB0(): pass

    label("Function_39_6CB0")


    def lambda_6CB5():
        OP_95(0xFE, 81000, 0, 1500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6CB5)

    def lambda_6CCF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6CCF)
    WaitChrThread(0xFE, 1)

    def lambda_6CE4():
        OP_95(0xFE, 77500, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6CE4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_39_6CB0 end

    def Function_40_6D05(): pass

    label("Function_40_6D05")


    def lambda_6D0A():
        OP_95(0xFE, 81000, 0, 2000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6D0A)

    def lambda_6D24():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6D24)
    WaitChrThread(0xFE, 1)

    def lambda_6D39():
        OP_95(0xFE, 79200, 0, -400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6D39)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0286
    ChrTalk(
        0x101,
        "#5P#00005F#8Aあ……\x02",
    )
    #Auto

    CloseMessageWindow()
    Return()

    # Function_40_6D05 end

    def Function_41_6D95(): pass

    label("Function_41_6D95")


    def lambda_6D9A():
        OP_95(0xFE, 81000, 0, 2000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6D9A)

    def lambda_6DB4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6DB4)
    WaitChrThread(0xFE, 1)

    def lambda_6DC9():
        OP_95(0xFE, 78300, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6DC9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_41_6D95 end

    def Function_42_6DEA(): pass

    label("Function_42_6DEA")


    def lambda_6DEF():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6DEF)

    def lambda_6E09():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6E09)
    WaitChrThread(0xFE, 1)

    def lambda_6E1E():
        OP_95(0xFE, 80400, 0, -100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E1E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_42_6DEA end

    def Function_43_6E3F(): pass

    label("Function_43_6E3F")


    def lambda_6E44():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E44)

    def lambda_6E5E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6E5E)
    WaitChrThread(0xFE, 1)

    def lambda_6E73():
        OP_95(0xFE, 79500, 0, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E73)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_43_6E3F end

    def Function_44_6E94(): pass

    label("Function_44_6E94")


    def lambda_6E99():
        OP_95(0xFE, 81000, 0, 3000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E99)

    def lambda_6EB3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6EB3)
    WaitChrThread(0xFE, 1)

    def lambda_6EC8():
        OP_95(0xFE, 80800, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6EC8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_44_6E94 end

    def Function_45_6EE9(): pass

    label("Function_45_6EE9")


    def lambda_6EEE():
        OP_95(0xFE, 81000, 0, 3000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6EEE)

    def lambda_6F08():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6F08)
    WaitChrThread(0xFE, 1)

    def lambda_6F1D():
        OP_95(0xFE, 79900, 0, 2100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6F1D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_45_6EE9 end

    def Function_46_6F3E(): pass

    label("Function_46_6F3E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    OP_68(80600, 1000, -4200, 0)
    MoveCamera(30, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 79900, 0, -2500, 180)
    SetChrPos(0x102, 81500, 0, -2300, 180)
    SetChrPos(0x103, 79500, 0, -1500, 180)
    SetChrPos(0x104, 80400, 0, -100, 180)
    SetChrPos(0x109, 81100, 0, -1300, 180)
    SetChrPos(0x105, 78600, 0, -1000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 78200, 0, 1200, 180)
    OP_68(80600, 1000, -1200, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0287
    ChrTalk(
        0x109,
        "#10109F#5Pはああ～～っ……！\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x103,
        "#00202F#5Pすごい見晴らしですね……\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x104,
        "#00309F#5Pいや～、最高の光景だぜ。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x20,
        (
            "#02809F#5Pハハ、満足してもらえたようだね。\x02\x03",

            "#02800F──ここが３４Ｆ。\x01",
            "国際会議などが開かれた時、\x01",
            "関係者が待機するフロアになる。\x02\x03",

            "#02800Fそれでは、\x01",
            "ざっと見て回るとしようか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7162():
        TurnDirection(0x101, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7162)
    Sleep(50)

    def lambda_7172():
        TurnDirection(0x102, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7172)
    Sleep(50)

    def lambda_7182():
        TurnDirection(0x103, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7182)
    Sleep(50)

    def lambda_7192():
        TurnDirection(0x109, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7192)
    Sleep(50)

    def lambda_71A2():
        TurnDirection(0x105, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_71A2)
    Sleep(50)

    def lambda_71B2():
        TurnDirection(0x104, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_71B2)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)

    def lambda_71D7():

        label("loc_71D7")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_71D7")

    QueueWorkItem2(0x101, 2, lambda_71D7)

    def lambda_71E9():

        label("loc_71E9")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_71E9")

    QueueWorkItem2(0x102, 2, lambda_71E9)

    def lambda_71FB():

        label("loc_71FB")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_71FB")

    QueueWorkItem2(0x103, 2, lambda_71FB)

    def lambda_720D():

        label("loc_720D")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_720D")

    QueueWorkItem2(0x109, 2, lambda_720D)

    def lambda_721F():

        label("loc_721F")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_721F")

    QueueWorkItem2(0x105, 2, lambda_721F)

    def lambda_7231():

        label("loc_7231")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_7231")

    QueueWorkItem2(0x104, 2, lambda_7231)

    #C0291
    ChrTalk(
        0x101,
        "#12P#00002Fはい、お願いします。\x02",
    )

    CloseMessageWindow()
    OP_68(76600, 1000, -1200, 3500)
    BeginChrThread(0x20, 3, 0, 47)
    Sleep(1700)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)

    def lambda_729A():
        OP_97(0x105, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_729A)
    Sleep(100)

    def lambda_72B7():
        OP_97(0x103, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_72B7)
    Sleep(100)

    def lambda_72D4():
        OP_97(0x104, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_72D4)
    Sleep(100)

    def lambda_72F1():
        OP_97(0x101, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_72F1)
    Sleep(100)

    def lambda_730E():
        OP_97(0x109, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_730E)
    Sleep(100)

    def lambda_732B():
        OP_97(0x102, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_732B)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x20, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetChrPos(0x20, 35000, 0, -1000, 270)
    SetChrPos(0x27, 37600, -600, -1000, 270)
    SetChrPos(0x101, 37600, 0, -1400, 270)
    SetChrPos(0x102, 37600, 0, -100, 270)
    SetChrPos(0x103, 38900, 0, -1800, 270)
    SetChrPos(0x104, 38900, 0, -500, 270)
    SetChrPos(0x109, 40200, 0, -1600, 270)
    SetChrPos(0x105, 40200, 0, -300, 270)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6B(0x27)
    SetChrFlags(0x27, 0x20)
    SetChrFlags(0x27, 0x40)
    SetChrFlags(0x27, 0x8)
    SetChrFlags(0x27, 0x4)
    OP_68(35000, 900, -1000, 0)
    MoveCamera(60, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    MoveCamera(45, 19, 0, 11000)
    SetCameraDistance(18000, 11000)

    def lambda_7479():
        OP_95(0xFE, 8500, 0, -1000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_7479)

    def lambda_7493():
        OP_96(0xFE, 0x2968, 0xFFFFFDA8, 0xFFFFFC18, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_7493)

    def lambda_74AD():
        OP_97(0x101, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_74AD)
    Sleep(50)

    def lambda_74CA():
        OP_97(0x102, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_74CA)
    Sleep(50)

    def lambda_74E7():
        OP_97(0x103, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_74E7)
    Sleep(50)

    def lambda_7504():
        OP_97(0x104, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7504)
    Sleep(50)

    def lambda_7521():
        OP_97(0x109, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7521)
    Sleep(50)

    def lambda_753E():
        OP_97(0x105, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_753E)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_7564():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7564)
    Sleep(50)

    def lambda_7578():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7578)
    Sleep(500)

    def lambda_758C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_758C)
    Sleep(50)

    def lambda_75A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_75A0)
    OP_0D()
    WaitChrThread(0x20, 1)
    OP_93(0x20, 0x2D, 0x1F4)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_6B(0xFF)

    #C0292
    ChrTalk(
        0x20,
        (
            "#6P#02803Fそちらは、警備対策室に加えて\x01",
            "報道陣などの控え室が並んでいる。\x02\x03",

            "#02800Fテロリストが潜入した場合に備え、\x01",
            "一応、警備隊の一個中隊も\x01",
            "下のフロアに待機している状態だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x109,
        "#10104F#11P話は伺っています。\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x104,
        (
            "#00300F#11P警備隊でも選りすぐりが\x01",
            "集められてるみてぇだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x105,
        (
            "#10305F#11Pしかし報道陣ってことは、\x01",
            "グレイス女史も来るのかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x5A, 0x1F4)

    #C0296
    ChrTalk(
        0x20,
        (
            "#6P#02805Fああ、クロスベルタイムズの\x01",
            "女性記者だったかな？\x02\x03",

            "#02804Fリストにあったと思うから\x01",
            "多分、取材に来るだろう。\x02\x03",

            "#02800Fちなみに報道陣は\x01",
            "取材と記者会見の時以外は\x01",
            "このフロアから出さない予定だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x105,
        "#10302F#11Pなるほど、合理的だね。\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x102,
        (
            "#11P#00106Fたまに警備をすり抜けて\x01",
            "突撃インタビューをするような\x01",
            "乱暴な記者もいますものね……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x103,
        (
            "#12P#00211Fというかグレイスさんが\x01",
            "一番そんな感じですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        (
            "#12P#00006Fうーん、さすがに\x01",
            "見つけたら止めないとな。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x10E, 0x1F4)

    def lambda_78F7():
        OP_98(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_78F7)

    def lambda_7911():
        OP_97(0x101, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7911)
    Sleep(50)

    def lambda_792E():
        OP_97(0x102, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_792E)
    Sleep(50)

    def lambda_794B():
        OP_97(0x103, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_794B)
    Sleep(50)

    def lambda_7968():
        OP_97(0x104, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7968)
    Sleep(50)

    def lambda_7985():
        OP_97(0x109, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7985)
    Sleep(50)

    def lambda_79A2():
        OP_97(0x105, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_79A2)
    SetCameraDistance(21000, 5000)
    Sleep(5000)
    Fade(1000)
    EndChrThread(0x20, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetChrPos(0x20, -13000, 0, 3500, 0)
    SetChrPos(0x27, -13000, -500, 1400, 0)
    SetChrPos(0x101, -13800, 0, 1400, 0)
    SetChrPos(0x102, -12700, 0, 1400, 0)
    SetChrPos(0x103, -13400, 0, 100, 0)
    SetChrPos(0x104, -12300, 0, 100, 0)
    SetChrPos(0x109, -13600, 0, -1200, 0)
    SetChrPos(0x105, -12500, 0, -1200, 0)
    OP_6B(0x27)
    SetChrFlags(0x27, 0x20)
    SetChrFlags(0x27, 0x40)
    SetChrFlags(0x27, 0x8)
    SetChrFlags(0x27, 0x4)
    OP_68(-13000, 900, 1400, 0)
    MoveCamera(33, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    MoveCamera(49, 19, 0, 7000)
    SetCameraDistance(18000, 7000)

    def lambda_7ACA():
        OP_97(0xFE, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_7ACA)

    def lambda_7AE4():
        OP_98(0xFE, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_7AE4)

    def lambda_7AFE():
        OP_97(0x101, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7AFE)
    Sleep(50)

    def lambda_7B1B():
        OP_97(0x102, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7B1B)
    Sleep(50)

    def lambda_7B38():
        OP_97(0x103, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7B38)
    Sleep(50)

    def lambda_7B55():
        OP_97(0x104, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7B55)
    Sleep(50)

    def lambda_7B72():
        OP_97(0x109, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7B72)
    Sleep(50)

    def lambda_7B8F():
        OP_97(0x105, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7B8F)
    OP_0D()
    WaitChrThread(0x20, 1)
    OP_93(0x20, 0x10E, 0x1F4)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_6B(0xFF)

    #C0301
    ChrTalk(
        0x20,
        (
            "#02800F#11P一応、こちらの部屋も\x01",
            "案内しておこうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-14000, 1000, 17400, 1000)
    FadeToDark(1000, 0, -1)

    def lambda_7C11():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7C11)
    Sleep(50)

    def lambda_7C21():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7C21)

    def lambda_7C2E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7C2E)
    Sleep(50)

    def lambda_7C3E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7C3E)

    def lambda_7C4B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7C4B)
    Sleep(50)

    def lambda_7C5B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7C5B)
    OP_0D()
    SetChrPos(0x101, 142100, 0, 10100, 315)
    SetChrPos(0x102, 141200, 0, 8200, 270)
    SetChrPos(0x103, 142300, 0, 7000, 225)
    SetChrPos(0x104, 145600, 0, 10200, 0)
    SetChrPos(0x109, 144100, 0, 6300, 225)
    SetChrPos(0x105, 144100, 0, 11000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 147500, 0, 7000, 270)
    ClearMapObjFlags(0xB, 0x10)
    OP_70(0xB, 0x5)
    OP_68(142600, 1100, 500, 0)
    MoveCamera(33, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(21500, 0)
    OP_68(143600, 1100, 11500, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(143600, 1100, 8700, 0)
    MoveCamera(53, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    OP_0D()

    #C0302
    ChrTalk(
        0x105,
        "#11P#10302Fへえ……これは見事だね。\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        (
            "#11P#00002F休憩室みたいだけど\x01",
            "すごい開放感だな……\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x20,
        (
            "#02804Fここは会議の関係者に\x01",
            "用意されている休憩室だ。\x02\x03",

            "#02800F休憩時間などに\x01",
            "遠慮なく利用してくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7E61():
        TurnDirection(0x101, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7E61)
    Sleep(50)

    def lambda_7E71():
        TurnDirection(0x102, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7E71)
    Sleep(50)

    def lambda_7E81():
        TurnDirection(0x103, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7E81)
    Sleep(50)

    def lambda_7E91():
        TurnDirection(0x104, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7E91)
    Sleep(50)

    def lambda_7EA1():
        TurnDirection(0x109, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7EA1)
    Sleep(50)

    def lambda_7EB1():
        TurnDirection(0x105, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7EB1)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0305
    ChrTalk(
        0x101,
        "#6P#00004Fはい、遠慮なく。\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x102,
        (
            "#6P#00109Fふふ、後でお茶でも\x01",
            "一服しに来ましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x20,
        (
            "#02809Fさて、こんなところで\x01",
            "次のフロアに案内しようか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x20, -13000, 0, 11000, 180)
    SetChrPos(0x27, -13000, -500, 13100, 180)
    SetChrPos(0x101, -13800, 0, 13100, 180)
    SetChrPos(0x102, -12700, 0, 13100, 180)
    SetChrPos(0x103, -13400, 0, 14400, 180)
    SetChrPos(0x104, -12300, 0, 14400, 180)
    SetChrPos(0x109, -13600, 0, 15700, 180)
    SetChrPos(0x105, -12500, 0, 15700, 180)
    OP_6B(0x27)
    SetChrFlags(0x27, 0x20)
    SetChrFlags(0x27, 0x40)
    SetChrFlags(0x27, 0x8)
    SetChrFlags(0x27, 0x4)
    OP_68(-13000, 900, 14100, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    MoveCamera(53, 19, 0, 4000)
    SetCameraDistance(18500, 4000)

    def lambda_8057():
        OP_95(0xFE, -13000, 0, 1800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_8057)

    def lambda_8071():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_8071)

    def lambda_808B():
        OP_97(0x101, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_808B)
    Sleep(50)

    def lambda_80A8():
        OP_97(0x102, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_80A8)
    Sleep(50)

    def lambda_80C5():
        OP_97(0x103, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_80C5)
    Sleep(50)

    def lambda_80E2():
        OP_97(0x104, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_80E2)
    Sleep(50)

    def lambda_80FF():
        OP_97(0x109, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_80FF)
    Sleep(50)

    def lambda_811C():
        OP_97(0x105, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_811C)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x20, 1)

    def lambda_8144():
        OP_95(0xFE, -14800, 0, 0, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_8144)
    WaitChrThread(0x27, 1)
    OP_6B(0xFF)
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_817E():

        label("loc_817E")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_817E")

    QueueWorkItem2(0x101, 2, lambda_817E)
    WaitChrThread(0x102, 0)

    def lambda_8194():

        label("loc_8194")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_8194")

    QueueWorkItem2(0x102, 2, lambda_8194)
    WaitChrThread(0x103, 0)

    def lambda_81AA():

        label("loc_81AA")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_81AA")

    QueueWorkItem2(0x103, 2, lambda_81AA)
    WaitChrThread(0x104, 0)

    def lambda_81C0():

        label("loc_81C0")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_81C0")

    QueueWorkItem2(0x104, 2, lambda_81C0)
    WaitChrThread(0x20, 1)

    def lambda_81D6():
        OP_95(0xFE, -17600, 0, 0, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_81D6)
    Sleep(300)
    Sound(103, 0, 100, 0)

    def lambda_81F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_81F9)
    WaitChrThread(0x20, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    BeginChrThread(0x101, 3, 0, 48)
    Sleep(700)
    FadeToDark(2000, 0, -1)
    BeginChrThread(0x102, 3, 0, 48)
    Sleep(300)
    BeginChrThread(0x103, 3, 0, 48)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 48)
    Sleep(300)
    BeginChrThread(0x109, 3, 0, 48)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 48)
    OP_0D()
    EndChrThread(0x20, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    OP_A7(0x20, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x101, -48000, 0, -1000, 270)
    SetChrPos(0x102, -48000, 0, -1000, 270)
    SetChrPos(0x103, -48000, 0, -1000, 270)
    SetChrPos(0x104, -48000, 0, -1000, 270)
    SetChrPos(0x109, -48000, 0, -1000, 270)
    SetChrPos(0x105, -48000, 0, -1000, 270)
    SetChrPos(0x20, -54000, 0, 2000, 180)
    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0x0)
    ClearMapObjFlags(0x7, 0x10)
    OP_70(0x7, 0x3C)
    OP_68(-50000, 1100, -1000, 0)
    MoveCamera(49, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    OP_68(-54000, 1100, 1300, 4000)
    SetCameraDistance(19000, 4000)
    FadeToBright(1000, 0)
    ClearMapObjFlags(0xC, 0x10)
    OP_71(0xC, 0x0, 0x5, 0x0, 0x0)
    OP_79(0xC)
    BeginChrThread(0x101, 3, 0, 49)
    Sleep(600)
    BeginChrThread(0x102, 3, 0, 50)
    Sleep(600)
    BeginChrThread(0x103, 3, 0, 51)
    Sleep(600)
    BeginChrThread(0x104, 3, 0, 52)
    Sleep(600)
    BeginChrThread(0x109, 3, 0, 53)
    Sleep(600)
    BeginChrThread(0x105, 3, 0, 54)
    Sleep(1300)
    Sound(104, 0, 100, 0)
    OP_71(0xC, 0x5, 0x0, 0x0, 0x0)
    OP_79(0xC)
    SetMapObjFlags(0xC, 0x10)
    WaitChrThread(0x105, 3)

    #C0308
    ChrTalk(
        0x101,
        (
            "#12P#00005Fここは……\x01",
            "非常階段エリアですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x104,
        (
            "#00305F下への階段は\x01",
            "封鎖されてるみてぇだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x20,
        (
            "#02803F#5P本来なら階段を使って\x01",
            "１Ｆまで降りる事が出来る。\x02\x03",

            "#02801Fしかし今回の会議中は\x01",
            "３４Ｆ、３５Ｆ、３６Ｆ以外は\x01",
            "封鎖するようにしているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x109,
        (
            "#10101Fなるほど……\x01",
            "警備上の理由ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x105,
        (
            "#10305Fでも、もし地震なんかが\x01",
            "起きた時はどうするんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x20,
        (
            "#02806F#5Pその場合、自動的に\x01",
            "全ての非常階段が開放される。\x02\x03",

            "#02800Fまあ、完璧なセキュリティは\x01",
            "あり得ないということだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x101,
        (
            "#12P#00003Fなるほど……\x01",
            "気を付けておきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x103,
        (
            "#12P#00208F……ハッキング対策なども\x01",
            "考える必要がありそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x20,
        (
            "#02804F#5Pさて、せっかくだから\x01",
            "階段を使うとしようか。\x02\x03",

            "#02800F３５Ｆ──\x01",
            "国際会議場フロアだ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_46_6F3E end

    def Function_47_86E2(): pass

    label("Function_47_86E2")

    OP_92(0xFE, 0x128E0, 0x0, 0x1F4)

    def lambda_86F4():
        OP_95(0xFE, 76000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_86F4)
    WaitChrThread(0xFE, 1)

    def lambda_8712():
        OP_95(0xFE, 68000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8712)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_47_86E2 end

    def Function_48_872C(): pass

    label("Function_48_872C")


    def lambda_8731():
        OP_95(0xFE, -14800, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8731)
    WaitChrThread(0xFE, 1)

    def lambda_874F():
        OP_95(0xFE, -17600, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_874F)
    Sleep(300)

    def lambda_876C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_876C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_48_872C end

    def Function_49_877D(): pass

    label("Function_49_877D")


    def lambda_8782():
        OP_95(0xFE, -52000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8782)

    def lambda_879C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_879C)
    WaitChrThread(0xFE, 1)

    def lambda_87B1():
        OP_95(0xFE, -55000, 0, -100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_87B1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_49_877D end

    def Function_50_87D2(): pass

    label("Function_50_87D2")


    def lambda_87D7():
        OP_95(0xFE, -51000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_87D7)

    def lambda_87F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_87F1)
    WaitChrThread(0xFE, 1)

    def lambda_8806():
        OP_95(0xFE, -53500, 0, 400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8806)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_50_87D2 end

    def Function_51_8827(): pass

    label("Function_51_8827")


    def lambda_882C():
        OP_95(0xFE, -52000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_882C)

    def lambda_8846():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8846)
    WaitChrThread(0xFE, 1)

    def lambda_885B():
        OP_95(0xFE, -54500, 0, -1100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_885B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_51_8827 end

    def Function_52_887C(): pass

    label("Function_52_887C")


    def lambda_8881():
        OP_95(0xFE, -51000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8881)

    def lambda_889B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_889B)
    WaitChrThread(0xFE, 1)

    def lambda_88B0():
        OP_95(0xFE, -53000, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_88B0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_52_887C end

    def Function_53_88D1(): pass

    label("Function_53_88D1")


    def lambda_88D6():
        OP_95(0xFE, -51000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_88D6)

    def lambda_88F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_88F0)
    WaitChrThread(0xFE, 1)

    def lambda_8905():
        OP_95(0xFE, -51500, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8905)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_53_88D1 end

    def Function_54_8926(): pass

    label("Function_54_8926")


    def lambda_892B():
        OP_95(0xFE, -51000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_892B)

    def lambda_8945():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8945)
    WaitChrThread(0xFE, 1)

    def lambda_895A():
        OP_95(0xFE, -51500, 0, -900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_895A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_54_8926 end

    def Function_55_897B(): pass

    label("Function_55_897B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(73000, 1200, -1000, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 74500, 0, -1000, 270)
    SetChrPos(0x102, 73800, 0, 200, 225)
    SetChrPos(0x103, 73800, 0, -2200, 315)
    SetChrPos(0x104, 72200, 0, 200, 135)
    SetChrPos(0x109, 71500, 0, -1000, 90)
    SetChrPos(0x105, 72200, 0, -2200, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0317
    ChrTalk(
        0x101,
        (
            "#11P#00000Fよし……\x01",
            "これで一通り回ったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x109,
        (
            "#6P#10100F今のところは\x01",
            "特に問題なさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x104,
        (
            "#5P#00302Fああ、この調子でもう一度、\x01",
            "見て回るとしようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x102,
        (
            "#00104Fそうね……\x02\x03",

            "#00108F……会議の方は\x01",
            "どうなっているのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x101,
        (
            "#11P#00006Fそうだな、市長や議長が\x01",
            "頑張っているとは思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x103,
        (
            "#12P#00201F問題は《鉄血宰相》に\x01",
            "ロックスミス大統領ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x105,
        (
            "#12P#10302Fま、休憩時間になったら\x01",
            "誰かに聞けばいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 2)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_55_897B end

    def Function_56_8C13(): pass

    label("Function_56_8C13")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-55500, 1200, -1500, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -54000, 0, -1500, 270)
    SetChrPos(0x102, -54700, 0, -300, 225)
    SetChrPos(0x103, -54700, 0, -2700, 315)
    SetChrPos(0x104, -56300, 0, -300, 135)
    SetChrPos(0x109, -57000, 0, -1500, 90)
    SetChrPos(0x105, -56300, 0, -2700, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0324
    ChrTalk(
        0x101,
        (
            "#11P#00000Fよし……\x01",
            "これで一通り回ったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x109,
        (
            "#6P#10100F今のところは\x01",
            "特に問題なさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x104,
        (
            "#5P#00302Fああ、この調子でもう一度、\x01",
            "見て回るとしようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x102,
        (
            "#00104Fそうね……\x02\x03",

            "#00108F……会議の方は\x01",
            "どうなっているのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x101,
        (
            "#11P#00006Fそうだな、市長や議長が\x01",
            "頑張っているとは思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x103,
        (
            "#12P#00201F問題は《鉄血宰相》に\x01",
            "ロックスミス大統領ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x105,
        (
            "#12P#10302Fま、休憩時間になったら\x01",
            "誰かに聞けばいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 2)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_56_8C13 end

    def Function_57_8EAB(): pass

    label("Function_57_8EAB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("chr/ch03002.itc", 0x23)
    LoadChrToIndex("apl/ch50011.itc", 0x24)
    LoadChrToIndex("apl/ch51090.itc", 0x25)
    SoundLoad(803)
    SoundLoad(3455)
    SoundLoad(3456)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 142100, 50, 5800, 220)
    SetChrPos(0x102, 142700, 50, 4100, 275)
    SetChrPos(0x103, 142000, 50, 2500, 315)
    SetChrPos(0x104, 140450, 50, 1750, 5)
    SetChrPos(0x109, 138800, 50, 2500, 40)
    SetChrPos(0x105, 138200, 50, 4100, 95)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, 140450, 50, 6350, 185)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x28, 0x80)
    OP_78(0xD, 0x28)
    ClearChrFlags(0x29, 0x80)
    OP_78(0xE, 0x29)
    ClearChrFlags(0x2A, 0x80)
    OP_78(0xF, 0x2A)
    ClearChrFlags(0x2B, 0x80)
    OP_78(0x10, 0x2B)
    OP_49()
    SetChrPos(0x28, 142300, 0, 6000, 45)
    OP_D5(0x28, 0x0, 0xAFC8, 0x0, 0x0)
    SetChrPos(0x29, 138600, 0, 2300, 225)
    OP_D5(0x29, 0x0, 0x36EE8, 0x0, 0x0)
    SetChrPos(0x2A, 138600, 0, 6000, 315)
    OP_D5(0x2A, 0x0, 0x4CE78, 0x0, 0x0)
    SetChrPos(0x2B, 142200, 0, 2300, 135)
    OP_D5(0x2B, 0x0, 0x20F58, 0x0, 0x0)
    SetChrChipByIndex(0x2C, 0x25)
    SetChrSubChip(0x2C, 0x7)
    SetChrFlags(0x2C, 0x8000)
    SetChrPos(0x2C, 140450, 550, 5650, 0)
    ClearChrFlags(0x2C, 0x80)
    ClearChrBattleFlags(0x2C, 0x8000)
    SetChrName("")

    #A0331
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そして、ロイドたちは\x01",
            "先に休憩に入ったイアン弁護士と\x01",
            "改めて話をする機会が得られた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(140450, 900, 4100, 0)
    MoveCamera(35, 33, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(25500, 0)
    MoveCamera(65, 33, 0, 5000)
    SetCameraDistance(19500, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(140450, 1100, 4100, 0)
    MoveCamera(68, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_0D()
    Sleep(150)

    #C0332
    ChrTalk(
        0x8,
        (
            "#02205F#5Pなるほど……そんな事情で\x01",
            "君たちも警備に参加したのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x101,
        (
            "#11P#00002Fええ、正直気休め程度にしか\x01",
            "なっていないかもしれませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x8,
        (
            "#02210F#5Pいやいや、市長暗殺未遂事件で\x01",
            "大金星を上げた君たちだ。\x02\x03",

            "#02200Fこの場にいてくれるだけでも\x01",
            "私としては非常に心強いよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x102,
        "#11P#00104Fそう言って頂けると……\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x104,
        "#12P#00302Fハハ、ありがたいッスね。\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x103,
        (
            "#00200F#11Pそれで先生。\x01",
            "会議の方はどうなんですか？\x02\x03",

            "さほど荒れた雰囲気は\x01",
            "感じられませんでしたが。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        (
            "#02210F#5Pああ、今のところは順調だよ。\x02\x03",

            "幾つかの通商協定には\x01",
            "各国の同意も得られたし……\x02\x03",

            "#02200Fディーター市長の呼びかけも\x01",
            "無駄にならなかったようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        "#11P#00102Fふふ、そうですか……\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x109,
        "#12P#10109Fちょっと安心ですね。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x105,
        (
            "#6P#10300Fしかし“今のところ”って事は\x01",
            "何か懸念でもあるのかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(150)

    #C0342
    ChrTalk(
        0x102,
        "#11P#00105Fえ……\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        "#11P#00001F……そうなんですか？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x0)

    #C0344
    ChrTalk(
        0x8,
        (
            "#02203F#5Pふむ、オブザーバーである\x01",
            "私の口から言うのもなんだが……\x02\x03",

            "前半は、貿易や金融などの\x01",
            "経済的な議案が殆んどだったんだ。\x02\x03",

            "#02201F──しかし会議の後半は\x01",
            "各国首脳から提議される議案……\x02\x03",

            "しかもどうやら、クロスベルの\x01",
            "安全保障に関する話が出るらしい。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0345
    ChrTalk(
        0x101,
        "#11P#00013Fそれは……！\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x104,
        (
            "#12P#00301F……安全保障ってことは\x01",
            "軍事の話も入るってことか。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x109,
        (
            "#12P#10108Fでも、２年前に締結された\x01",
            "《不戦条約》もありますよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x8,
        (
            "#02203F#5Pあれはリベールの女王陛下が\x01",
            "当時のクロスベルの危機的状況を\x01",
            "抑えるために提案したものだ。\x02\x03",

            "レミフェリアは関わっていないし、\x01",
            "何よりクロスベルそのものが\x01",
            "《不戦条約》には関わっていない。\x02\x03",

            "#02201Fその意味で、それとは別の\x01",
            "新たな安全保障の枠組みが\x01",
            "求められているのは確かでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x102,
        (
            "#11P#00106F……確かに。\x01",
            "それは祖父も懸念していました。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x103,
        (
            "#00205F#11Pなら、クロスベルを交えた\x01",
            "新たな条約を結べばいいのでは？\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x109,
        (
            "#12P#10101Fそうですよ、不戦条約と同じ、\x01",
            "国家間の争いを武力で解決するのを\x01",
            "禁止するような枠組みを──\x02\x03",

            "#10105F───あ。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x101,
        (
            "#11P#00006Fそうか……\x01",
            "クロスベルは『国家』じゃない。\x02\x03",

            "#00008F帝国と共和国によって承認された\x01",
            "『自治州』でしかない……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x8,
        (
            "#02203F#5Pそう、それはつまり\x01",
            "『国際条約』を締結できるような\x01",
            "国家主権を持っていないという事だ。\x02\x03",

            "経済的な『協定』は結べても\x01",
            "対等な立場での『条約』は結べない。\x02\x03",

            "#02201Fそれが結果的に、この地の安全保障を\x01",
            "ひどく危うくさせてしまっている訳だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x104,
        (
            "#12P#00306Fややこしいが……\x01",
            "何となく判ってきたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x103,
        (
            "#00208F#11P……すみません。\x01",
            "ちょっといいですか？\x02\x03",

            "#00203Fクロスベル以外にも\x01",
            "自治州というのはあります。\x02\x03",

            "レマン自治州、オレド自治州、\x01",
            "ノーザンブリア自治州……\x02\x03",

            "#00200Fそれらの自治州も同じように\x01",
            "国際条約は結べないのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x8,
        (
            "#02210F#5Pいや、そんな事はない。\x02\x03",

            "#02200F確かにそれらの自治州も\x01",
            "それぞれの歴史的事情によって\x01",
            "国家としては成立していないが……\x02\x03",

            "『宗主国』から委譲される形で\x01",
            "同等の主権が認められている。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x109,
        "#12P#10105F宗主国……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(300)

    #C0358
    ChrTalk(
        0x102,
        (
            "#11P#00103Fそれらの自治州が決定的に\x01",
            "クロスベルと異なる点……\x02\x03",

            "#00101Fそれは成立を承認したのが\x01",
            "『アルテリア法国』という事なの。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x109, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrSubChip(0x101, 0x0)
    Sleep(1000)

    #C0359
    ChrTalk(
        0x103,
        "#00205F#11Pあ……\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x105,
        (
            "#6P#10305Fアルテリア法国というと\x01",
            "七耀教会の総本山だったっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x102,
        (
            "#11P#00104Fええ、国土は小さいけど\x01",
            "宗教的な権威は持っているから……\x02\x03",

            "#00100F自治州や自由都市の多くは\x01",
            "あそこに頼って成立しているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x101,
        (
            "#5P#00006Fだがクロスベルは、帝国と共和国に\x01",
            "承認されて成立する『自治州』……\x02\x03",

            "#00001Fいわば宗主国を２つも\x01",
            "持っている形になっているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x102,
        (
            "#11P#00108Fええ、そしてそれが歴史的に\x01",
            "様々なねじれ#6R㈲　㈲　㈲#と悲劇を生んだ……\x02\x03",

            "クロスベルに少しでも主権が\x01",
            "認められれば、もう少し状況は\x01",
            "変わるのでしょうけど……\x02\x03",

            "#00106F……それを２大国が認める事は\x01",
            "永遠にあり得ないでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x109,
        "#12P#10108F……そんな………\x02",
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x103,
        "#00206F#11P……溜息が出てしまいますね。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x8,
        (
            "#02203F#5P──話を戻すが、\x01",
            "どうやら宰相と大統領はそれぞれ、\x01",
            "安全保障に関する提案があるらしい。\x02\x03",

            "無論それは、対等な条約を\x01",
            "各国が結ぶというものではない。\x02\x03",

            "#02201F……今ごろ議長や市長たちは\x01",
            "警戒を強めている所だろうね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    #C0367
    ChrTalk(
        0x8,
        (
            "#02210F#5Pハハ、すまない。\x01",
            "不安にさせてしまったようだな。\x02\x03",

            "#02200Fまあ、マクダエル議長などは\x01",
            "このような状況は慣れっこだろう。\x02\x03",

            "それにディーター市長の方は\x01",
            "何やら策があるようでね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x105, 0x1)
    Sleep(150)

    #C0368
    ChrTalk(
        0x101,
        "#11P#00005F策、ですか？\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x102,
        "#11P#00105Fそれはどういう……\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x8,
        (
            "#02203F#5Pいや、詳しい話は\x01",
            "私も聞いていないんだが──\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x8, 0x1)
    SetChrSubChip(0x109, 0x0)

    #C0371
    ChrTalk(
        0x101,
        "#11P#00000F──失礼します。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    OP_24(0x323)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x9)
    Sleep(300)
    Sound(804, 0, 100, 0)
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0372
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00008F特務支援課、\x01",
            "ロイド・バニングスです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0373
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3455V#30W──バニングス。\x01",
            "こちらは記者会見が終わった。\x02\x03",

            "#3456V首脳たちは３６Ｆに引き上げたが、\x01",
            "お前たちはどこにいる？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD80)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0374
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fあ、はい。\x01",
            "３４Ｆの休憩室ですが……\x02\x03",

            "#00001F……何かありましたか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0375
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "実は、オズボーン宰相と\x01",
            "ロックスミス大統領から\x01",
            "それぞれ申し入れがあった。\x02\x03",

            "──休憩時間中、お前たちと\x01",
            "直接話がしてみたいそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    #Sound(2087, 255, 100, 0)    #voice#Lloyd
    SetMessageWindowPos(90, 130, -1, -1)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #A0376
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011F#4Sな──！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0377
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……相手が相手だ。\x01",
            "さすがに断ることもできん。\x02\x03",

            "休憩時間中に、３６Ｆにある\x01",
            "両首脳の部屋を訪ねるがいい。\x02\x03",

            "左翼の最奥が大統領、\x01",
            "右翼の最奥が宰相の部屋だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0378
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00006Fま、待ってください！\x01",
            "いったい何がどうして……\x02\x03",

            "#00011Fさすがに荷が重過ぎますよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0379
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──甘えるな、バニングス。\x02\x03",

            "両者の思惑をうかがえる\x01",
            "またとない機会だろうが？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0380
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F！\x02\x03",

            "#00003F……分かりました。\x01",
            "すぐに両首脳の所に向かいます。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0381
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いざという時はエリィ嬢に頼れ。\x01",
            "ＶＩＰ相手は慣れているはずだ。\x02\x03",

            "話が終わったら報告に来い。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0382
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001F了解です……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    VolumeBGM(0x64, 0x3E8)
    Sound(804, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    #C0383
    ChrTalk(
        0x102,
        "#11P#00101Fロイド、今のは……\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x104,
        (
            "#12P#00305Fおいおい、不穏なことを\x01",
            "言ってやがらなかったか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()

    #C0385
    ChrTalk(
        0x101,
        "#5P#00003Fああ……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0386
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《鉄血宰相》とロックスミス大統領に\x01",
            "それぞれ呼ばれたことを説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0387
    ChrTalk(
        0x109,
        "#12P#10111Fえええっ～！？\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x105,
        "#6P#10305Fへえ、マジかい？\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x103,
        (
            "#00206F#11Pどうやら冗談では\x01",
            "無さそうですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x8,
        (
            "#02205F#5Pいやはや……驚いたな。\x02\x03",

            "#02210Fどうやら思っていた以上に\x01",
            "特務支援課の名前は\x01",
            "知れ渡っているようだ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    #C0391
    ChrTalk(
        0x101,
        (
            "#11P#00006Fいや……両首脳のスタッフに\x01",
            "それぞれ知り合いがいるんです。\x02\x03",

            "#00008Fそれで興味を\x01",
            "持たれただけかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x104,
        (
            "#12P#00301Fなるほど……\x01",
            "そいつはありそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x102,
        (
            "#11P#00103F……だとしても\x01",
            "断るわけにはいかないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0394
    ChrTalk(
        0x101,
        (
            "#5P#00006Fああ、３６Ｆの\x01",
            "左翼と右翼の最奥の部屋だ。\x02\x03",

            "#00001Fさっそく訪ねてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x103,
        "#00201F#11P了解です。\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x109,
        "#12P#10101Fイ、イエス・サー！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x2C, 0x80)
    SetChrBattleFlags(0x2C, 0x8000)
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
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrPos(0x28, 156000, 0, 0, 0)
    SetChrPos(0x29, 156000, 0, 0, 0)
    SetChrPos(0x2A, 156000, 0, 0, 0)
    SetChrPos(0x2B, 156000, 0, 0, 0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 144700, 0, 4800, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x142, 1)
    OP_29(0xA4, 0x1, 0x2)
    OP_24(0x323)
    EventEnd(0x5)
    Return()

    # Function_57_8EAB end

    def Function_58_AEAF(): pass

    label("Function_58_AEAF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31250.itc", 0x1F)
    LoadChrToIndex("chr/ch31251.itc", 0x20)
    SoundLoad(145)
    SoundLoad(143)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -48500, 0, -1000, 270)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -48500, 0, -1000, 270)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -48500, 0, -1000, 270)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2D, 0x1F)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2D, 0x4)
    SetChrFlags(0x2D, 0x8000)
    OP_90(0x2D, -51500, -2000, 10000, 0)
    OP_A7(0x2D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2E, 0x1F)
    SetChrSubChip(0x2E, 0x0)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2E, 0x4)
    SetChrFlags(0x2E, 0x8000)
    OP_90(0x2E, -51500, -2000, 10000, 0)
    OP_A7(0x2E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2F, 0x1F)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x2F, 0x4)
    SetChrFlags(0x2F, 0x8000)
    OP_90(0x2F, -51500, -2000, 10000, 0)
    OP_A7(0x2F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x30, 0x1F)
    SetChrSubChip(0x30, 0x0)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x30, 0x4)
    SetChrFlags(0x30, 0x8000)
    OP_90(0x30, -51500, -2000, 10000, 0)
    OP_A7(0x30, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x6, 0x10)
    ClearMapObjFlags(0x7, 0x10)
    OP_70(0x6, 0x3C)
    OP_70(0x7, 0x3C)
    OP_68(-54000, 1100, 12500, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    FadeToBright(1000, 0)
    BeginChrThread(0x2D, 3, 0, 62)
    BeginChrThread(0x2E, 3, 0, 63)
    BeginChrThread(0x2F, 3, 0, 64)
    BeginChrThread(0x30, 3, 0, 65)
    OP_0D()
    OP_68(-51500, 1000, 2500, 3500)
    Sleep(1800)
    OP_71(0x7, 0x3C, 0x0, 0x0, 0x0)
    Sound(145, 2, 100, 0)
    Sleep(700)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0xC, 0x10)
    OP_71(0xC, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x5)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    BeginChrThread(0x9, 3, 0, 59)
    BeginChrThread(0xA, 3, 0, 60)
    BeginChrThread(0xB, 3, 0, 61)
    OP_79(0x7)
    Sound(143, 0, 70, 0)
    OP_24(0x91)
    WaitChrThread(0x2D, 3)

    #C0397
    ChrTalk(
        0x2D,
        "#6Pな、なんだこれは！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 3)

    #C0398
    ChrTalk(
        0xA,
        "#12Pど、どうしていきなり……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 3)

    #C0399
    ChrTalk(
        0xB,
        "#12Pなんだ、何が起こっている！？\x02",
    )

    CloseMessageWindow()
    OP_68(-49400, 1000, 400, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x3, 0x10)
    ClearMapObjFlags(0x4, 0x10)
    ClearMapObjFlags(0x5, 0x10)
    OP_70(0x3, 0x0)
    OP_70(0x4, 0x0)
    OP_70(0x5, 0x0)
    SetChrPos(0x9, 76600, 0, 2600, 0)
    SetChrPos(0xA, 74700, 0, 1800, 0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xC, 0x3)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 76500, 0, 200, 315)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 75800, 0, -1200, 0)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 74200, 0, -1000, 0)
    OP_4B(0xE, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 72400, 0, -200, 45)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 72700, 0, -1300, 45)
    OP_4B(0x10, 0xFF)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 71300, 0, 600, 90)
    OP_4B(0x11, 0xFF)
    OP_68(72700, 1000, 4450, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_68(75000, 1000, 2500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    TurnDirection(0x9, 0xA, 500)

    #C0400
    ChrTalk(
        0x9,
        (
            "#11Pだ、駄目です！\x01",
            "ボタンを押しても反応しません！\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xA,
        (
            "#5Pクッ……\x01",
            "何がどうなっている！？\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xC,
        (
            "#02105F#11Pちょっと、これじゃあ取材が\x01",
            "できないじゃないの！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    #C0403
    ChrTalk(
        0xC,
        "#02101F#5Pレインズ君、何とかしなさい！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)

    #C0404
    ChrTalk(
        0xD,
        "#12Pむ、無茶言わないでくださいよ～！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_24(0x91)
    SetScenarioFlags(0x142, 5)
    SetScenarioFlags(0x22, 4)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_58_AEAF end

    def Function_59_B41F(): pass

    label("Function_59_B41F")

    Sleep(600)

    def lambda_B427():
        OP_95(0xFE, -51000, 0, -1000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B427)

    def lambda_B441():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B441)
    WaitChrThread(0xFE, 1)

    def lambda_B456():
        OP_95(0xFE, -51100, 0, 700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B456)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_59_B41F end

    def Function_60_B477(): pass

    label("Function_60_B477")


    def lambda_B47C():
        OP_95(0xFE, -51000, 0, -1000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B47C)

    def lambda_B496():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B496)
    WaitChrThread(0xFE, 1)

    def lambda_B4AB():
        OP_95(0xFE, -52700, 0, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B4AB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_60_B477 end

    def Function_61_B4CC(): pass

    label("Function_61_B4CC")

    Sleep(1200)

    def lambda_B4D4():
        OP_95(0xFE, -52000, 0, -1000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B4D4)

    def lambda_B4EE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B4EE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_61_B4CC end

    def Function_62_B506(): pass

    label("Function_62_B506")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_B513():
        OP_95(0xFE, -51500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B513)

    def lambda_B52D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B52D)
    WaitChrThread(0xFE, 1)

    def lambda_B542():
        OP_95(0xFE, -55500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B542)
    WaitChrThread(0xFE, 1)

    def lambda_B560():
        OP_95(0xFE, -55500, 0, 2500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B560)
    WaitChrThread(0xFE, 1)

    def lambda_B57E():
        OP_95(0xFE, -53800, 0, 1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B57E)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(300)
    Return()

    # Function_62_B506 end

    def Function_63_B5AA(): pass

    label("Function_63_B5AA")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_B5BA():
        OP_95(0xFE, -51500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B5BA)

    def lambda_B5D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B5D4)
    WaitChrThread(0xFE, 1)

    def lambda_B5E9():
        OP_95(0xFE, -55500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B5E9)
    WaitChrThread(0xFE, 1)

    def lambda_B607():
        OP_95(0xFE, -55500, 0, 2500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B607)
    WaitChrThread(0xFE, 1)

    def lambda_B625():
        OP_95(0xFE, -54200, 0, -300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B625)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_63_B5AA end

    def Function_64_B64E(): pass

    label("Function_64_B64E")

    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_B65E():
        OP_95(0xFE, -51500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B65E)

    def lambda_B678():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B678)
    WaitChrThread(0xFE, 1)

    def lambda_B68D():
        OP_95(0xFE, -55500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B68D)
    WaitChrThread(0xFE, 1)

    def lambda_B6AB():
        OP_95(0xFE, -55500, 0, 2500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B6AB)
    WaitChrThread(0xFE, 1)

    def lambda_B6C9():
        OP_95(0xFE, -55100, 0, 700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B6C9)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_64_B64E end

    def Function_65_B6F2(): pass

    label("Function_65_B6F2")

    Sleep(1500)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_B702():
        OP_95(0xFE, -51500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B702)

    def lambda_B71C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B71C)
    WaitChrThread(0xFE, 1)

    def lambda_B731():
        OP_95(0xFE, -55500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B731)
    WaitChrThread(0xFE, 1)

    def lambda_B74F():
        OP_95(0xFE, -55500, 0, 2500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B74F)
    WaitChrThread(0xFE, 1)

    def lambda_B76D():
        OP_95(0xFE, -55800, 0, 1500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B76D)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_65_B6F2 end

    def Function_66_B796(): pass

    label("Function_66_B796")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02000.itp")
    CreatePortrait(1, 16, 192, 528, 256, 0, 20, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis519.itp")
    LoadChrToIndex("chr/ch27202.itc", 0x1E)
    LoadChrToIndex("chr/ch27302.itc", 0x1F)
    LoadChrToIndex("chr/ch32002.itc", 0x20)
    LoadChrToIndex("chr/ch32102.itc", 0x21)
    LoadChrToIndex("chr/ch05700.itc", 0x22)
    LoadChrToIndex("chr/ch44900.itc", 0x23)
    LoadChrToIndex("chr/ch00002.itc", 0x24)
    LoadChrToIndex("chr/ch00102.itc", 0x25)
    LoadChrToIndex("chr/ch00302.itc", 0x26)
    LoadChrToIndex("chr/ch02902.itc", 0x27)
    LoadChrToIndex("chr/ch03002.itc", 0x28)
    LoadChrToIndex("chr/ch00202.itc", 0x29)
    SetChrChipByIndex(0x25, 0x22)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 271000, 0, 13000, 180)
    SetChrChipByIndex(0x26, 0x23)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 275200, 0, 13800, 225)
    SetChrChipByIndex(0x21, 0x1E)
    SetChrSubChip(0x21, 0x2)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 272800, 100, 10900, 270)
    SetChrChipByIndex(0x22, 0x1F)
    SetChrSubChip(0x22, 0x2)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, 272800, 100, 8950, 270)
    SetChrChipByIndex(0x23, 0x20)
    SetChrSubChip(0x23, 0x2)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, 272800, 100, 7000, 270)
    SetChrChipByIndex(0x24, 0x21)
    SetChrSubChip(0x24, 0x2)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, 272800, 100, 5000, 270)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x1)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x2)
    SetChrChipByIndex(0x103, 0x29)
    SetChrSubChip(0x103, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 269200, 100, 10900, 90)
    SetChrPos(0x102, 269200, 100, 8950, 90)
    SetChrPos(0x103, 269200, 100, 7000, 90)
    SetChrPos(0x104, 269200, 100, 5000, 90)
    SetChrPos(0x109, 269200, 100, 2950, 90)
    SetChrPos(0x105, 272800, 100, 2950, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x11, 0x1000)
    OP_70(0x11, 0x1)
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0405
    AnonymousTalk(
        0x101,
        "#00011F《幻獣#4Rげんじゅう#》──ですか？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(271000, 900, 1000, 0)
    MoveCamera(35, 33, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(23000, 0)
    OP_68(271000, 900, 11000, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(3500)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_6F(0x79)
    Fade(500)
    OP_68(271000, 1300, 10000, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0406
    AnonymousTalk(
        0x25,
        (
            "──ええ、その通りよ。\x02\x03",

            "単なる魔獣とは言い難い、\x01",
            "大型で不可思議なモンスター……\x02\x03",

            "そんな存在が、クロスベル各地で\x01",
            "発見されるようになっているわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_93(0x26, 0x5A, 0x1F4)
    Sleep(500)
    OP_68(271300, 2000, 10320, 1500)
    MoveCamera(30, 11, 0, 1500)
    SetCameraDistance(20500, 1500)

    def lambda_BC1E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_BC1E)
    OP_6F(0x79)
    Sound(853, 0, 100, 0)
    OP_71(0x11, 0x1, 0xA, 0x0, 0x0)
    OP_79(0x11)

    def lambda_BC42():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_BC42)
    Sleep(100)
    OP_63(0x23, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x24, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0407
    ChrTalk(
        0x23,
        (
            "#11Pあ……\x01",
            "あたしらが見たヤツだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x24,
        (
            "#11P結局、止めを刺す前に\x01",
            "逃がしてしまったけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0409
    ChrTalk(
        0x109,
        "#10101F#12P#Nこんな魔獣が……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0410
    ChrTalk(
        0x103,
        (
            "#00206F#12P#Nそういった情報は\x01",
            "流れてはいましたが……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0411
    ChrTalk(
        0x26,
        (
            "#5P──それだけじゃない。\x01",
            "他のタイプも確認されている。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x26, 0x5A, 0x1F4)
    Sleep(500)
    Sound(853, 0, 100, 0)
    OP_71(0x11, 0xB, 0x14, 0x0, 0x0)
    OP_79(0x11)
    Sleep(1500)
    Sound(853, 0, 100, 0)
    OP_71(0x11, 0x15, 0x1E, 0x0, 0x0)
    OP_79(0x11)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0412
    ChrTalk(
        0x101,
        "#6P#N#00007Fこ、これは！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0413
    ChrTalk(
        0x102,
        "#6P#N#00101F旧鉱山に現れた……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0414
    ChrTalk(
        0x104,
        "#00307F#12P#Nおいおい、また出たのかよ！？\x02",
    )

    CloseMessageWindow()
    OP_93(0x26, 0xE1, 0x1F4)
    Sleep(150)

    #C0415
    ChrTalk(
        0x26,
        (
            "#5P先日、同じタイプのものが\x01",
            "北の山岳地帯に出現しやがってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x26,
        (
            "#5Pそちらのスコットたちに\x01",
            "既に退治されている。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(271560, 1300, 9270, 1200)
    MoveCamera(40, 19, 0, 1200)
    SetCameraDistance(21500, 1200)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    SetChrSubChip(0x102, 0x0)
    OP_6F(0x79)

    #C0417
    ChrTalk(
        0x101,
        "#6P#00006Fそうだったんですか……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0418
    ChrTalk(
        0x109,
        (
            "#10105F#12P#Nもしかしてお２人で\x01",
            "退治なさったんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x21, 0x1)
    Sleep(100)
    SetChrSubChip(0x22, 0x0)
    Sleep(200)

    #C0419
    ChrTalk(
        0x21,
        (
            "#5Pああ、不意を突いて\x01",
            "何とか倒すことができたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x21,
        (
            "#5Pこれも君たちの方から\x01",
            "情報が回っていたおかげだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x22,
        "#11Pただ、どうにも妙な手応えでな。\x02",
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x22,
        (
            "#11Pアーツの効き方が異なる上に\x01",
            "光るようにして消えてしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x102,
        "#6P#00108Fやはり……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0424
    ChrTalk(
        0x104,
        (
            "#00303F#6P#N……俺たちが戦った時と\x01",
            "まったく同じみてぇだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0425
    ChrTalk(
        0x105,
        (
            "#10303F#12P#Nしかし山岳地帯ということは……\x02\x03",

            "#10301F今度は“屋外”に現れたんだね？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C198():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_C198)
    Sleep(50)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x21, 0x2)
    Sleep(50)
    SetChrSubChip(0x22, 0x2)
    WaitChrThread(0x25, 2)
    Sleep(150)

    #C0426
    ChrTalk(
        0x25,
        (
            "#02006F#5Pええ、これまでにも\x01",
            "《塔》や《僧院》など\x01",
            "異常な場所は確認されているわ。\x02\x03",

            "どうやら何らかの理由で\x01",
            "“場の歪み”が発生していると\x01",
            "推測されているのだけど……\x02\x03",

            "#02001Fでも、これらの《幻獣》は\x01",
            "山岳地帯や湖沼地帯などにも\x01",
            "出現しているの。\x02\x03",

            "ひょっとしたら“場の歪み”が\x01",
            "そうした屋外にも\x01",
            "現れているのかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x109,
        "#10108F#12P#Nそ、そんな……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0428
    ChrTalk(
        0x23,
        "#11Pゾッとしない話だなぁ。\x02",
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x24,
        (
            "#11Pでは、私たちを\x01",
            "ここに呼んだ理由というのは？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(273530, 1300, 11920, 1500)
    MoveCamera(40, 14, 0, 1500)
    OP_6E(450, 1500)
    SetCameraDistance(22580, 1500)
    OP_71(0x11, 0x1F, 0x28, 0x0, 0x0)
    OP_79(0x11)
    OP_6F(0x79)

    #C0430
    ChrTalk(
        0x26,
        (
            "#5Pああ、これらの幻獣への対応を\x01",
            "ギルドと特務支援課の双方に\x01",
            "頼みたくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x26,
        (
            "#5P独立提唱がなされて以来、\x01",
            "ベルガード、タングラム両門で\x01",
            "やや緊張状態が続いている……\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x26,
        (
            "#5Pせめて住民投票が終わるまでは\x01",
            "そちらに集中しておきたいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x101,
        (
            "#6P#00003F#N……分かりました。\x01",
            "引き受けさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0434
    ChrTalk(
        0x21,
        (
            "#12P分担に関しては\x01",
            "こちらに任せてもらっても？\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x25,
        (
            "#02004F#5Pええ、データはお渡しするから\x01",
            "そちらにお任せするわ。\x02\x03",

            "#02001Fそれと……できれば\x01",
            "“原因”の特定も頼みたいの。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x21, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x22, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x23, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x24, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0436
    ChrTalk(
        0x103,
        (
            "#12P#N#00205F原因……？\x02\x03",

            "#00200Fなぜそうした《幻獣》が\x01",
            "いきなり現れたか、ですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0437
    ChrTalk(
        0x25,
        (
            "#02003F#5Pええ、魔獣の発生は\x01",
            "昔から一定のサイクルで\x01",
            "起きているけど……\x02\x03",

            "#02001Fこの《幻獣》に関しては\x01",
            "そこから外れた“異常事態”と\x01",
            "言っても過言ではないでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x26,
        (
            "#5P──間違いなく\x01",
            "何か原因があるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x26,
        (
            "#5P“場の歪み”を発生させて\x01",
            "常識外れの大型魔獣が\x01",
            "現れるだけの原因がな。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x104,
        "#00303F#6P#Nなるほど、確かにな。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0441
    ChrTalk(
        0x22,
        (
            "#11Pギルドの名に賭けて\x01",
            "必ずや突き止めてみせよう。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x103, 0x4)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 3)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_66_B796 end

    def Function_67_C8A5(): pass

    label("Function_67_C8A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC0A")
    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    OP_4B(0x16, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0xD, 0xFF)
    Fade(500)
    OP_68(32470, 1500, -1390, 0)
    MoveCamera(44, 24, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17510, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 30440, 0, -1390, 90)
    SetChrPos(0x1, 29160, 0, -2400, 90)
    SetChrPos(0x2, 29770, 0, 10, 90)
    SetChrPos(0x3, 28400, 0, -990, 90)
    SetChrPos(0x4, 27880, 0, 10, 90)
    SetChrPos(0x5, 28070, 0, -2600, 90)
    OP_0D()

    #C0442
    ChrTalk(
        0x9,
        (
            "ですから……\x01",
            "何度も言っているように\x01",
            "報道陣の皆さんは通せないんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x16,
        (
            "#12Pまあでも今は休憩中なわけだし……\x01",
            "そこを何とか、さ？\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x11,
        (
            "#6Pええ、写真を撮る以外のことは\x01",
            "何もしませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xD,
        "#6Pそうですよ、でないと先輩に……\x02",
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
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0446
    ChrTalk(
        0x101,
        (
            "#6P#00012Fダメだと分かっていても\x01",
            "行くんだな。\x02\x03",

            "#00003F流石に無理やり突破しようって\x01",
            "気はないみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x109,
        "#6P#10112Fこれも記者の性#2Rさが#なんでしょうか。\x02",
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x103,
        (
            "#6P#00206Fとりあえず……\x01",
            "ここは通れなさそうですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x9, 0xFF)
    OP_4C(0x16, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0xD, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1, 5)
    SetChrPos(0x0, 29470, 0, -1200, 270)
    EventEnd(0x5)
    Jump("loc_CC8A")

    label("loc_CC0A")

    EventBegin(0x1)
    SetChrName("")

    #A0449
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターフロア前に\x01",
            "記者たちが押しかけている。\x02\x03",

            "しばらくの間、\x01",
            "この場所は通れなさそうだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 29470, 0, -1200, 270)
    EventEnd(0x4)

    label("loc_CC8A")

    Return()

    # Function_67_C8A5 end

    def Function_68_CC8B(): pass

    label("Function_68_CC8B")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF08")
    SetChrName("")

    #A0450
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターのシャッターは\x01",
            "固く閉ざされている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0451
    ChrTalk(
        0x101,
        (
            "#00005Fそういえば、会議中は\x01",
            "手前のエレベーター以外は\x01",
            "使えないんだったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x102,
        (
            "#00100Fええ、確か警備上の理由で\x01",
            "そういう事になっていたわね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_END)), "loc_CE27")

    #C0453
    ChrTalk(
        0x103,
        (
            "#00200F非常階段同様、\x01",
            "ここも導力ネットによって\x01",
            "制御・管理されているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x101,
        (
            "#00003Fああ、そうらしいな。\x02\x03",

            "#00000Fまあいい、移動する時は\x01",
            "手前のエレベーターを使おう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF00")

    label("loc_CE27")


    #C0455
    ChrTalk(
        0x103,
        (
            "#00200Fちなみに、ロックの開閉は\x01",
            "導力ネットによって\x01",
            "制御・管理されているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x101,
        (
            "#00003Fああ、流石はオルキスターの\x01",
            "セキュリティってところだな。\x02\x03",

            "#00000Fまあいい、移動する時は\x01",
            "手前のエレベーターを使おう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF00")

    SetScenarioFlags(0x1C2, 2)
    Jump("loc_CF77")

    label("loc_CF08")

    SetChrName("")

    #A0457
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターのシャッターは\x01",
            "固く閉ざされている。\x02\x03",

            "会議中、このエレベーターは\x01",
            "使用できないようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_CF77")

    TalkEnd(0xFF)
    Return()

    # Function_68_CC8B end

    def Function_69_CF7B(): pass

    label("Function_69_CF7B")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D1A5")
    SetChrName("")

    #A0458
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "非常階段のシャッターは\x01",
            "固く閉ざされている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0459
    ChrTalk(
        0x101,
        "#00001Fこっちは３３階方面か。\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x102,
        (
            "#00100F会議中は完全に\x01",
            "封鎖するという話だったわね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_END)), "loc_D0E4")

    #C0461
    ChrTalk(
        0x103,
        (
            "#00200Fエレベーター同様、\x01",
            "こちらも導力ネットで\x01",
            "制御されているようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x101,
        (
            "#00003F完璧なセキュリティは\x01",
            "あり得ない――だったか。\x02\x03",

            "#00001F万が一の事態も\x01",
            "想定しておかないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D19D")

    label("loc_D0E4")


    #C0463
    ChrTalk(
        0x103,
        (
            "#00200Fシャッターのロックは\x01",
            "導力ネットによって\x01",
            "制御されているようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x101,
        (
            "#00003F完璧なセキュリティは\x01",
            "あり得ない――だったか。\x02\x03",

            "#00001F万が一の事態も\x01",
            "想定しておかないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D19D")

    SetScenarioFlags(0x1C2, 3)
    Jump("loc_D20E")

    label("loc_D1A5")

    SetChrName("")

    #A0465
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "非常階段のシャッターは\x01",
            "固く閉ざされている。\x02\x03",

            "会議中、この先の階へは\x01",
            "行き来できないようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D20E")

    TalkEnd(0xFF)
    Return()

    # Function_69_CF7B end

    def Function_70_D212(): pass

    label("Function_70_D212")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_70_D212 end

    SaveToFile()

Try(main)
