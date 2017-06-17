from ScenarioHelper import *

def main():
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
        "伊安律师",               # 1
        "警官",                   # 2
        "警官",                   # 3
        "皮埃尔副局长",           # 4
        "格蕾丝",                 # 5
        "雷因兹",                 # 6
        "记者诺蒂亚",             # 7
        "记者克劳德",             # 8
        "记者帕卡",               # 9
        "帝国时报社记者",         # 10
        "警官",                   # 11
        "警官",                   # 12
        "警官",                   # 13
        "记者汤普森",             # 14
        "泰瑞尔通讯社记者",       # 15
        "达德利搜查官",           # 16
        "搜查官",                 # 17
        "搜查官",                 # 18
        "古兰特一尉",             # 19
        "吉赛尔上士",             # 20
        "市政府职员",             # 21
        "市政府职员",             # 22
        "市政府职员",             # 23
        "雷克特书记官",           # 24
        "迪塔市长",               # 25
        "游击士斯克特",           # 26
        "游击士温蔡尔",           # 27
        "游击士林",               # 28
        "游击士艾欧莉娅",         # 29
        "索妮亚司令",             # 30
        "道格拉斯副司令",         # 31
        "假",                     # 32
        "椅子",                   # 33
        "椅子",                   # 34
        "椅子",                   # 35
        "椅子",                   # 36
        "餐具",                   # 37
        "警备队员",               # 38
        "警备队员",               # 39
        "警备队员",               # 40
        "警备队员",               # 41
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
        "Function_4_133F",         # 04, 4
        "Function_5_169F",         # 05, 5
        "Function_6_1963",         # 06, 6
        "Function_7_20AC",         # 07, 7
        "Function_8_2250",         # 08, 8
        "Function_9_231D",         # 09, 9
        "Function_10_2455",        # 0A, 10
        "Function_11_2566",        # 0B, 11
        "Function_12_28BF",        # 0C, 12
        "Function_13_2A3D",        # 0D, 13
        "Function_14_2B8B",        # 0E, 14
        "Function_15_2D37",        # 0F, 15
        "Function_16_2E36",        # 10, 16
        "Function_17_328A",        # 11, 17
        "Function_18_3383",        # 12, 18
        "Function_19_3636",        # 13, 19
        "Function_20_3743",        # 14, 20
        "Function_21_391F",        # 15, 21
        "Function_22_3A57",        # 16, 22
        "Function_23_3AE4",        # 17, 23
        "Function_24_3C5C",        # 18, 24
        "Function_25_40B6",        # 19, 25
        "Function_26_4219",        # 1A, 26
        "Function_27_45D6",        # 1B, 27
        "Function_28_4AAB",        # 1C, 28
        "Function_29_4C5F",        # 1D, 29
        "Function_30_4C8E",        # 1E, 30
        "Function_31_5246",        # 1F, 31
        "Function_32_52A1",        # 20, 32
        "Function_33_52D7",        # 21, 33
        "Function_34_5309",        # 22, 34
        "Function_35_5BF6",        # 23, 35
        "Function_36_5BFD",        # 24, 36
        "Function_37_5C26",        # 25, 37
        "Function_38_5F1C",        # 26, 38
        "Function_39_5F8C",        # 27, 39
        "Function_40_5FE1",        # 28, 40
        "Function_41_6071",        # 29, 41
        "Function_42_60C6",        # 2A, 42
        "Function_43_611B",        # 2B, 43
        "Function_44_6170",        # 2C, 44
        "Function_45_61C5",        # 2D, 45
        "Function_46_621A",        # 2E, 46
        "Function_47_7916",        # 2F, 47
        "Function_48_7960",        # 30, 48
        "Function_49_79B1",        # 31, 49
        "Function_50_7A06",        # 32, 50
        "Function_51_7A5B",        # 33, 51
        "Function_52_7AB0",        # 34, 52
        "Function_53_7B05",        # 35, 53
        "Function_54_7B5A",        # 36, 54
        "Function_55_7BAF",        # 37, 55
        "Function_56_7E11",        # 38, 56
        "Function_57_8073",        # 39, 57
        "Function_58_9DFD",        # 3A, 58
        "Function_59_A331",        # 3B, 59
        "Function_60_A389",        # 3C, 60
        "Function_61_A3DE",        # 3D, 61
        "Function_62_A418",        # 3E, 62
        "Function_63_A4BC",        # 3F, 63
        "Function_64_A560",        # 40, 64
        "Function_65_A604",        # 41, 65
        "Function_66_A6A8",        # 42, 66
        "Function_67_B687",        # 43, 67
        "Function_68_BA19",        # 44, 68
        "Function_69_BC87",        # 45, 69
        "Function_70_BEF4",        # 46, 70
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_11F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118A")

    #C0001
    ChrTalk(
        0xFE,
        (
            "那些记者们终于放弃，\x01",
            "不再试图上楼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "唉……说起来，\x01",
            "那就是所谓的职业病吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "不管是哪个国家的记者，\x01",
            "好像都很擅长死缠烂打啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_11EC")

    label("loc_118A")


    #C0004
    ChrTalk(
        0xFE,
        (
            "唉……说起来，\x01",
            "那就是所谓的职业病吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "不管是哪个国家的记者，\x01",
            "好像都很擅长死缠烂打啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11EC")

    Jump("loc_133B")

    label("loc_11F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_11FF")
    Jump("loc_133B")

    label("loc_11FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_133B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12C2")

    #C0006
    ChrTalk(
        0xFE,
        (
            "这里是用来招待各国\x01",
            "新闻记者的休息室。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "按照规定，在会议进行过程中，\x01",
            "这些前来采访的记者是\x01",
            "绝对不能离开休息室的。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "各国记者都在里面，\x01",
            "请你们进去确认一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_133B")

    label("loc_12C2")


    #C0009
    ChrTalk(
        0xFE,
        (
            "这里是用来招待各国\x01",
            "新闻记者的休息室。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "按照规定，在会议进行过程中，\x01",
            "这些前来采访的记者是\x01",
            "绝对不能离开休息室的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133B")

    TalkEnd(0xFE)
    Return()

    # Function_3_10DF end

    def Function_4_133F(): pass

    label("Function_4_133F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_1353")
    Call(0, 6)
    Jump("loc_169B")

    label("loc_1353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_1679")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1609")

    #C0011
    ChrTalk(
        0xC,
        (
            "#02100F哎呀，罗伊德，是你们啊。\x01",
            "警备方面如何啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00002F嗯，暂时没发现什么问题。\x02\x03",

            "格蕾丝小姐，您的联合\x01",
            "采访工作还顺利吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xC,
        (
            "#02102F呵呵，这个嘛～\x01",
            "托各位的福，收获不少呢。\x02\x03",

            "看来能写出一篇比我\x01",
            "预料中还要正面的报道。\x02\x03",

            "#02109F接下来，要是能挖掘到一些\x01",
            "群众喜闻乐见的八卦消息就更好了～\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#00006F那个……我想您应该很清楚……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        (
            "#00106F千万别闯到\x01",
            "不该进的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xC,
        (
            "#02104F放心吧，那方面的事情\x01",
            "只要让雷因兹……\x02\x03",

            "#02101F啊，不对不对，\x01",
            "我一定会遵守规定的。\x02\x03",

            "#02109F你们根本不必\x01",
            "担心姐姐我哦～\x02",
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
        "#00006F（唉，真让人不放心啊……）\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        "#00106F（是啊……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 1)
    Jump("loc_1674")

    label("loc_1609")


    #C0019
    ChrTalk(
        0xC,
        (
            "#02109F我一定会遵守规定的，\x01",
            "你们就放心吧～\x02\x03",

            "#02100F接下来，\x01",
            "先和通讯社联系一下，\x01",
            "然后去休息室看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1674")

    Jump("loc_169B")

    label("loc_1679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_169B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1698")
    TalkEnd(0xFE)
    Call(0, 34)
    Return()

    label("loc_1698")

    Call(0, 5)

    label("loc_169B")

    TalkEnd(0xFE)
    Return()

    # Function_4_133F end

    def Function_5_169F(): pass

    label("Function_5_169F")

    OP_4B(0xC, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1887")

    #C0020
    ChrTalk(
        0xC,
        (
            "#02100F也就是说，奈尔先生\x01",
            "他们没有来这里吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xE,
        (
            "是的，他们正忙着在\x01",
            "共和国那边取材，\x01",
            "抽不出时间来这里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xE,
        (
            "听说那边的状况\x01",
            "也不太好。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xC,
        (
            "#02103F这样啊，你是指那群\x01",
            "民族主义的激进分子吧？\x02\x03",

            "#02101F我听到过一些传闻，\x01",
            "据说他们可能会在这次的\x01",
            "通商会议上展开行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xE,
        (
            "呵呵，看来你也没有\x01",
            "白干记者这一行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xE,
        (
            "的确有这方面的传言，\x01",
            "但目前还没有确凿证据。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#00001F（格蕾丝小姐也得到了\x01",
            "  那种情报……）\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#00303F（总之，\x01",
            "  我们必须继续保持警戒。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_195A")

    label("loc_1887")


    #C0028
    ChrTalk(
        0xC,
        (
            "#02100F对了，诺蒂亚小姐。\x01",
            "你下次见到奈尔先生时，\x01",
            "可以帮我转告他一句话吗？\x02\x03",

            "『恭喜你拿到了\x01",
            "  菲利策奖，但下次的\x01",
            "  获奖者一定是我。』\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xE,
        (
            "呵呵，说起来，\x01",
            "听说你也认识\x01",
            "奈尔呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xE,
        "没问题，我一定会转告他的。\x02",
    )

    CloseMessageWindow()

    label("loc_195A")

    OP_4C(0xC, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_5_169F end

    def Function_6_1963(): pass

    label("Function_6_1963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B02")

    #C0031
    ChrTalk(
        0x1F,
        (
            "#11505F原来如此，大胡子熊律师\x01",
            "喜欢喝咖啡啊。\x02\x03",

            "#11500F您说不定会和宰相阁下挺合得来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "#02200F哦？宰相阁下也喜欢咖啡吗？\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x1F,
        (
            "#11503F是啊，尤其喜欢黑咖啡。\x02\x03",

            "#11502F也许正是因为这样，\x01",
            "他才会一直\x01",
            "目露寒光呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0034
    ChrTalk(
        0x8,
        "#02202F原、原来如此……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xC,
        "#02109F呵呵，说不定还真是这样。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#00005F（真、真是奇怪的\x01",
            "  组合啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        (
            "#00206F（是啊……\x01",
            "  好像还挺聊得来呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 2)
    Jump("loc_20AB")

    label("loc_1B02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DE6")

    #C0038
    ChrTalk(
        0xC,
        (
            "#02104F嗯嗯，我得记下来，\x01",
            "奥斯本宰相喜欢咖啡……\x02\x03",

            "#02100F那雷克特先生呢？你喜欢红茶还是咖啡？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x1F,
        (
            "#11510F唔～我还是\x01",
            "比较喜欢红茶。\x02\x03",

            "#11500F不过我只是个二等书记官，\x01",
            "打听我的嗜好有什么用呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xC,
        (
            "#02109F哎呀～因为你实在是\x01",
            "太英俊了嘛，\x01",
            "所以我打算先下手为强。\x02\x03",

            "#02102F毕竟帅哥美女可以\x01",
            "给报道锦上添花呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x1F,
        (
            "#11509F哈哈，原来如此，\x01",
            "多谢夸奖了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 0)), scpexpr(EXPR_END)), "loc_1D29")

    #C0042
    ChrTalk(
        0x101,
        (
            "#00006F（唔……非常明显的\x01",
            "  场面话啊。）\x02\x03",

            "#00001F（看来格蕾丝小姐\x01",
            "  也对雷克特先生的情况\x01",
            "  有一定程度的掌握……）\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x105,
        (
            "#10302F（呵呵，这就是所谓的\x01",
            "  虚虚实实，相互试探吧？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DDE")

    label("loc_1D29")


    #C0044
    ChrTalk(
        0x101,
        (
            "#00006F（唔……非常明显的\x01",
            "  场面话啊。）\x02\x03",

            "#00001F（格蕾丝小姐肯定知道\x01",
            "  雷克特先生并不只是一个\x01",
            "  普通的书记官……）\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x105,
        (
            "#10302F（呵呵，这就是所谓的\x01",
            "  虚虚实实，相互试探吧？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DDE")

    SetScenarioFlags(0x1C1, 3)
    Jump("loc_20AB")

    label("loc_1DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF5")

    #C0046
    ChrTalk(
        0x1F,
        (
            "#11501F对了，大胡子熊律师，\x01",
            "其实我有一件事想向您\x01",
            "咨询一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        "#02205F哦？是什么事？\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x1F,
        (
            "#11506F该怎么说呢～其实我\x01",
            "正在为职场的事而烦恼。\x02\x03",

            "所以很想请教一下\x01",
            "您这位在人权问题上\x01",
            "极富盛名的律师……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "#02202F这样啊……\x01",
            "但今天的时间实在不充裕。\x02\x03",

            "如果你方便的话，\x01",
            "改日来我的事务所好了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0050
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "伊安律师将名片递给了\x01",
            "雷克特书记官。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0051
    ChrTalk(
        0x1F,
        "#11509F哎呀，真是太感谢了。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#00001F（原来如此，他就是用这种方法\x01",
            "  来扩充人脉的啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        (
            "#00103F（对于谍报人员来说，\x01",
            "  这种外向的性格\x01",
            "  也是必要的技能啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 4)
    Jump("loc_20AB")

    label("loc_1FF5")


    #C0054
    ChrTalk(
        0x1F,
        "#11500F另外，大胡子熊律师……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        "#02202F没错，那其实是……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xC,
        "#02100F嗯嗯，原来如此……\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#00003F（……总不能一直偷听\x01",
            "  他们三人的谈话。）\x02\x03",

            "（还是不要\x01",
            "  逗留在这里了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20AB")

    Return()

    # Function_6_1963 end

    def Function_7_20AC(): pass

    label("Function_7_20AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_210F")

    #C0058
    ChrTalk(
        0xFE,
        (
            "唉，ＶＩＰ楼层果然不是\x01",
            "可以轻易潜入的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "……话说回来，前辈\x01",
            "去哪里了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_224C")

    label("loc_210F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_211D")
    Jump("loc_224C")

    label("loc_211D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_224C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_213C")
    TalkEnd(0xFE)
    Call(0, 34)
    Return()

    label("loc_213C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E4")

    #C0060
    ChrTalk(
        0xFE,
        (
            "利贝尔通讯社的天才摄影师，\x01",
            "朵洛希·海娅特……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "她拍摄的照片\x01",
            "全都栩栩如生，\x01",
            "有种可以吸引他人目光的魅力。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "身为摄影师，真想\x01",
            "和她聊聊啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_224C")

    label("loc_21E4")


    #C0063
    ChrTalk(
        0xFE,
        (
            "唔……下次去利贝尔\x01",
            "旅行的时候，\x01",
            "抽空去一趟通讯社吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "我记得从卢安\x01",
            "到王都也用不了\x01",
            "多少时间……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_224C")

    TalkEnd(0xFE)
    Return()

    # Function_7_20AC end

    def Function_8_2250(): pass

    label("Function_8_2250")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_22F7")

    #C0065
    ChrTalk(
        0xFE,
        (
            "两大国的意图暂且不提，\x01",
            "会议前半程的成果还是\x01",
            "很令人惊喜的。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "大陆的经济如果能进一步繁盛，\x01",
            "对利贝尔和雷米菲利亚来说，\x01",
            "也是一件值得高兴的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2319")

    label("loc_22F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2319")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2316")
    TalkEnd(0xFE)
    Call(0, 34)
    Return()

    label("loc_2316")

    Call(0, 5)

    label("loc_2319")

    TalkEnd(0xFE)
    Return()

    # Function_8_2250 end

    def Function_9_231D(): pass

    label("Function_9_231D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_23B7")

    #C0067
    ChrTalk(
        0xFE,
        (
            "虽然归根结底，\x01",
            "自治州的利益\x01",
            "也直接牵扯到两大国的利益……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "但没想到两大国竟然会对自治州的提案\x01",
            "做出如此程度的让步，还真是稀奇啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2451")

    label("loc_23B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2451")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23D2")
    Call(0, 10)
    Jump("loc_2451")

    label("loc_23D2")


    #C0069
    ChrTalk(
        0xFE,
        (
            "说起来，这座兰花塔\x01",
            "真是一栋无比壮观的建筑。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "雷米菲利亚离这里实在太远，\x01",
            "但在共和国的阿尔泰尔市\x01",
            "应该能清楚地看到它吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2451")

    TalkEnd(0xFE)
    Return()

    # Function_9_231D end

    def Function_10_2455(): pass

    label("Function_10_2455")


    #C0071
    ChrTalk(
        0x15,
        (
            "自我介绍一下，我是\x01",
            "『热点报道』的汤普森。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x15,
        (
            "你是泰瑞尔通讯社的\x01",
            "摄影师吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x16,
        "是啊，不过我还只是个新手。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x16,
        (
            "既然在『热点报道』工作，\x01",
            "那您应该是雷米菲利亚的人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x16,
        (
            "国籍不同便没有竞争……\x01",
            "今天就让我们并肩作战好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x15,
        (
            "哈哈，说得没错。\x01",
            "劳烦你多多关照了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_10_2455 end

    def Function_11_2566(): pass

    label("Function_11_2566")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_2656")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2601")

    #C0077
    ChrTalk(
        0xFE,
        (
            "唔，会议前半程的内容\x01",
            "总算是整理得差不多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "不过，后半程应该\x01",
            "会有更敏感的问题\x01",
            "被摆上台面……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        "好戏还在后头呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2651")

    label("loc_2601")


    #C0080
    ChrTalk(
        0xFE,
        (
            "在会议的后半程，\x01",
            "应该会有更敏感的问题\x01",
            "被摆上台面……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        "好戏还在后头呢。\x02",
    )

    CloseMessageWindow()

    label("loc_2651")

    Jump("loc_28BB")

    label("loc_2656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2813")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27A1")
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0082
    ChrTalk(
        0xFE,
        (
            "是的，关于这个问题，\x01",
            "各国的想法已经达成一致……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        "请把具体内容汇报给总部……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#00000F（他正在用艾尼格玛\x01",
            "  和什么人通话呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        (
            "#00100F（估计在塔外也有\x01",
            "  记者同事吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x105,
        (
            "#10302F（呵呵，这是在争分夺秒地\x01",
            "  传达通商会议的情报吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        "#00303F（还真是辛苦啊。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_280E")

    label("loc_27A1")

    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0088
    ChrTalk(
        0xFE,
        (
            "是的，关于这个问题，\x01",
            "各国的想法已经达成一致……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        "请把具体内容汇报给总部……\x02",
    )

    CloseMessageWindow()

    label("loc_280E")

    Jump("loc_28BB")

    label("loc_2813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_28BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_282E")
    Call(0, 12)
    Jump("loc_28BB")

    label("loc_282E")


    #C0090
    ChrTalk(
        0xFE,
        (
            "呵呵，说起来，\x01",
            "洛克史密斯总统也是如此啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        "百闻不如一见……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "和泰瑞尔通讯社平时\x01",
            "在报道中描述的形象相比，\x01",
            "他本人更显威严庄重呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28BB")

    TalkEnd(0xFE)
    Return()

    # Function_11_2566 end

    def Function_12_28BF(): pass

    label("Function_12_28BF")

    OP_4B(0x10, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0093
    ChrTalk(
        0x10,
        (
            "哎呀～话说回来，\x01",
            "这次的会议在各方面\x01",
            "都超乎想象呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x10,
        (
            "两国间的会议倒还常见，\x01",
            "但此次却汇集了自治州与周边四国……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x10,
        (
            "而且奥斯本宰相\x01",
            "和洛克史密斯总统还会\x01",
            "进行直接会谈。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xF,
        (
            "不管怎么说，\x01",
            "这还是他们两人第一次\x01",
            "当面谈话呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xF,
        (
            "今天一定会成为\x01",
            "历史性的一日。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x10,
        "是啊，说得没错。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x10,
        (
            "这里聚集了包括你们\x01",
            "帝国时报在内的各国记者，\x01",
            "咱们一起竭尽全力认真取材吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_12_28BF end

    def Function_13_2A3D(): pass

    label("Function_13_2A3D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_2AC9")

    #C0100
    ChrTalk(
        0xFE,
        (
            "无法到ＶＩＰ楼层采访\x01",
            "各位首脑，的确有些遗憾……\x01",
            "不过以后还有采访的机会。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "我得赶快再研究一下\x01",
            "记者问答的纲要才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B87")

    label("loc_2AC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2AD7")
    Jump("loc_2B87")

    label("loc_2AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2B87")

    #C0102
    ChrTalk(
        0xFE,
        (
            "虽然克洛斯贝尔的警察时常\x01",
            "被评价为无能之辈……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "但从大楼内的警备情况来看，\x01",
            "感觉他们十分优秀呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "可见问题的核心并不在于警察……\x01",
            "而是自治州本身的特殊性啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B87")

    TalkEnd(0xFE)
    Return()

    # Function_13_2A3D end

    def Function_14_2B8B(): pass

    label("Function_14_2B8B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_2BEA")

    #C0105
    ChrTalk(
        0xFE,
        (
            "好了，闲逛了一圈，\x01",
            "休息时间也要结束了。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "该为后半程会议\x01",
            "做些准备了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D33")

    label("loc_2BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2CA8")

    #C0107
    ChrTalk(
        0xFE,
        (
            "在有关经济的协议方面，\x01",
            "取得的成果可真是让人大吃一惊。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "这多亏了同时\x01",
            "兼任ＩＢＣ总裁的\x01",
            "提案者迪塔市长啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "经济发展将促进大陆和平……\x01",
            "看来这并不是不切实际的空谈呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D33")

    label("loc_2CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2D33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CC3")
    Call(0, 12)
    Jump("loc_2D33")

    label("loc_2CC3")


    #C0110
    ChrTalk(
        0xFE,
        (
            "话说回来……\x01",
            "奥斯本宰相的气势真是非同小可。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "真人和照片的感觉完全不同。\x01",
            "现在我觉得很多疑问都有解答了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D33")

    TalkEnd(0xFE)
    Return()

    # Function_14_2B8B end

    def Function_15_2D37(): pass

    label("Function_15_2D37")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_2D79")

    #C0112
    ChrTalk(
        0xFE,
        (
            "休息时间快要结束了……\x01",
            "趁现在去买点饮料吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E32")

    label("loc_2D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2D87")
    Jump("loc_2E32")

    label("loc_2D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2E32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DA2")
    Call(0, 10)
    Jump("loc_2E32")

    label("loc_2DA2")


    #C0113
    ChrTalk(
        0xFE,
        (
            "是啊，天气晴朗的时候，\x01",
            "看得非常清楚。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "拜其所赐，来阿尔泰尔市\x01",
            "观光的游客数量\x01",
            "也有所增加呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "兰花塔带来的经济效益\x01",
            "真是相当了得啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E32")

    TalkEnd(0xFE)
    Return()

    # Function_15_2D37 end

    def Function_16_2E36(): pass

    label("Function_16_2E36")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2EC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E54")
    Call(0, 17)
    Jump("loc_2EC2")

    label("loc_2E54")


    #C0116
    ChrTalk(
        0x17,
        (
            "#00600F啊，是你们啊。\x02\x03",

            "虽说现在还有时间，\x01",
            "但你们还是尽快前往\x01",
            "两国首脑的房间吧。\x02\x03",

            "总不能让他们\x01",
            "等得太久。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC2")

    Jump("loc_3286")

    label("loc_2EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_3286")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3210")

    #C0117
    ChrTalk(
        0x17,
        (
            "#00600F是你们啊。\x02\x03",

            "有什么异常状况吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        "#00000F目前还没有。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x102,
        (
            "#00100F通过这些监视器，\x01",
            "可以俯瞰所有区域的警备状态吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x17,
        (
            "#00603F嗯，不仅是会议现场，\x01",
            "也能对兰花塔中的\x01",
            "其它重要场所进行实时监控。\x02\x03",

            "#00600F设置在这栋大楼内的可是\x01",
            "最新型的监控摄像系统。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x103,
        (
            "#00203F监控摄像……就是ＩＢＣ\x01",
            "和导力商店也在使用的\x01",
            "那种技术吧？\x02\x03",

            "#00200F但设置的摄像机台数\x01",
            "和这里相比就差得太远了。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x104,
        (
            "#00306F虽然说得平淡无奇，\x01",
            "但好像是很厉害的技术啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，将来说不定还会\x01",
            "用这种技术去监视外面的情况呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x109,
        (
            "#10106F唔～但不知道市民们\x01",
            "会不会同意那种做法。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x17,
        (
            "#00603F……总之，现在我们必须\x01",
            "最大限度地利用一切可用之物。\x02\x03",

            "#00601F既然无法掌握恐怖分子的动向，\x01",
            "那就只能在他们即将行动时\x01",
            "或行动之后迅速击溃他们。\x02\x03",

            "为此，哪怕是微不足道的情报\x01",
            "也绝不能放过。\x02\x03",

            "如果有什么情况，一定要立刻联系我。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        "#00001F好的，我明白了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 5)
    Call(0, 36)
    Jump("loc_3286")

    label("loc_3210")


    #C0127
    ChrTalk(
        0x17,
        (
            "#00603F我们一直和各界保持着联系，\x01",
            "目前还没发现任何值得注意的问题。\x02\x03",

            "#00600F你们就继续进行\x01",
            "相关楼层的警备工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3286")

    TalkEnd(0xFE)
    Return()

    # Function_16_2E36 end

    def Function_17_328A(): pass

    label("Function_17_328A")

    OP_4B(0x17, 0xFF)
    OP_4B(0x1A, 0xFF)

    #C0128
    ChrTalk(
        0x17,
        (
            "#00600F古兰特一尉，那支中队\x01",
            "现在的状况如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x1A,
        (
            "没问题，大家都保持着警觉，\x01",
            "正在待命之中。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x1A,
        (
            "毕竟我们的职责就是\x01",
            "做好随时出动的准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x17,
        (
            "#00603F是吗，真是可靠啊。\x02\x03",

            "#00601F那么，关于后半程会议的\x01",
            "警备队安排……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x17, 0xFF)
    OP_4C(0x1A, 0xFF)
    ClearChrFlags(0x17, 0x10)
    ClearChrFlags(0x1A, 0x10)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_17_328A end

    def Function_18_3383(): pass

    label("Function_18_3383")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_34D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3449")

    #C0132
    ChrTalk(
        0xFE,
        (
            "现阶段，市内外\x01",
            "都没出现任何问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "根据监视人员的报告，\x01",
            "『赤色星座』和『黑月』\x01",
            "都还没有任何行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "这就是暴风雨之前的平静吗……\x01",
            "说实话，真让人忐忑不安啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_34CE")

    label("loc_3449")


    #C0135
    ChrTalk(
        0xFE,
        (
            "根据监视人员的报告，\x01",
            "『赤色星座』和『黑月』\x01",
            "目前都还没有任何行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "这就是暴风雨之前的平静吗……\x01",
            "说实话，真让人忐忑不安啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34CE")

    Jump("loc_3632")

    label("loc_34D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_3632")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35AC")

    #C0137
    ChrTalk(
        0xFE,
        (
            "如今的体制可以使\x01",
            "各方面的情报迅速汇集到\x01",
            "警备对策室。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "另外，这里的导力终端虽然\x01",
            "功能受限，但可以直接连接到\x01",
            "警察总部的数据库。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "如有必要，\x01",
            "我们随时可以在这里\x01",
            "调查可疑人物的身份。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_3632")

    label("loc_35AC")


    #C0140
    ChrTalk(
        0xFE,
        (
            "能做出这么周全的安排，\x01",
            "多亏了迪塔市长的\x01",
            "全面协助啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "这次的警备体制可谓\x01",
            "集结了克洛斯贝尔的全部力量……\x01",
            "因此我们绝不能失败。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3632")

    TalkEnd(0xFE)
    Return()

    # Function_18_3383 end

    def Function_19_3636(): pass

    label("Function_19_3636")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_36AF")

    #C0142
    ChrTalk(
        0xFE,
        (
            "都已经展开了那么多的警戒活动，\x01",
            "却还是没能获取任何情报……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "那些恐怖分子到底\x01",
            "潜伏在什么地方呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_373F")

    label("loc_36AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_373F")

    #C0144
    ChrTalk(
        0xFE,
        (
            "到目前为止，那些恐怖分子\x01",
            "丝毫没有露出尾巴。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "难道是这完美的警备体制\x01",
            "使他们放弃了吗……\x01",
            "但还是不能有这种乐观的想法啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0x19, 0x2)
    Return()

    label("loc_373F")

    TalkEnd(0xFE)
    Return()

    # Function_19_3636 end

    def Function_20_3743(): pass

    label("Function_20_3743")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_389F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3819")

    #C0146
    ChrTalk(
        0xFE,
        (
            "无论是休息时间还是会议期间，\x01",
            "我们都不会放松警戒。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "警备体制如此完善，\x01",
            "那些恐怖分子到底打算\x01",
            "从哪里突破呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "我们已经预想了好几种方案，\x01",
            "但一旦发生问题，还是得随机应变啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_389A")

    label("loc_3819")


    #C0149
    ChrTalk(
        0xFE,
        (
            "警备体制如此完善，\x01",
            "那些恐怖分子到底打算\x01",
            "从哪里突破呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "我们已经预想了好几种方案，\x01",
            "但一旦发生问题，还是得随机应变啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_389A")

    Jump("loc_391B")

    label("loc_389F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_391B")

    #C0151
    ChrTalk(
        0xFE,
        (
            "看看监视器中的影像，\x01",
            "就知道大家的警戒\x01",
            "非常严密认真。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "恐怖分子吗……\x01",
            "真希望这只是我们多余的担心。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0xA, 0x1)
    Return()

    label("loc_391B")

    TalkEnd(0xFE)
    Return()

    # Function_20_3743 end

    def Function_21_391F(): pass

    label("Function_21_391F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39D6")

    #C0153
    ChrTalk(
        0xFE,
        (
            "我们警卫科所有人\x01",
            "都出动参与了\x01",
            "兰花塔的警备。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "我们都是实战派，为了预防万一，\x01",
            "平时一直在经受严格的训练。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "一旦出现什么问题，\x01",
            "我们是不会输给警备队的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3A53")

    label("loc_39D6")


    #C0156
    ChrTalk(
        0xFE,
        (
            "我们警备科的成员都是实战派，\x01",
            "为了预防万一，\x01",
            "平时一直在经受严格的训练。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "一旦出现什么问题，\x01",
            "我们是不会输给警备队的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A53")

    TalkEnd(0xFE)
    Return()

    # Function_21_391F end

    def Function_22_3A57(): pass

    label("Function_22_3A57")

    TalkBegin(0xFE)

    #C0158
    ChrTalk(
        0xFE,
        (
            "我们平时主要负责保护\x01",
            "政府的重要设施以及\x01",
            "各界要人。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "这种国际盛会的警备任务\x01",
            "也属于我们的重要工作之一，\x01",
            "在纪念庆典时也是如此。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_3A57 end

    def Function_23_3AE4(): pass

    label("Function_23_3AE4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_3BD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B02")
    Call(0, 17)
    Jump("loc_3BCF")

    label("loc_3B02")


    #C0160
    ChrTalk(
        0xFE,
        (
            "唔，如果在这次休息时间里，\x01",
            "恐怖分子还是没有出现，\x01",
            "那危险期就在后半程会议及会议结束之后了。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "算了，考虑太多\x01",
            "也没用。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "总之，我们要全力保持警戒，\x01",
            "以便在发生特殊状况时\x01",
            "立刻采取最妥善的应对措施。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BCF")

    Jump("loc_3C58")

    label("loc_3BD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_3C58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BEF")
    Call(0, 24)
    Jump("loc_3C58")

    label("loc_3BEF")


    #C0163
    ChrTalk(
        0xFE,
        (
            "话说回来，这房间只有\x01",
            "两个人，还真是太空旷了。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "该怎么说呢……\x01",
            "兰花塔各方面的规格\x01",
            "都超出常规啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C58")

    TalkEnd(0xFE)
    Return()

    # Function_23_3AE4 end

    def Function_24_3C5C(): pass

    label("Function_24_3C5C")

    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    TurnDirection(0x1A, 0x0, 500)
    TurnDirection(0x1B, 0x0, 500)

    #C0165
    ChrTalk(
        0x109,
        "#10100F古兰特一尉，您辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x104,
        "#00300F辛苦啦。\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x1A,
        "是希卡上士和奥兰多下士啊。\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x1A,
        (
            "啊，不对，\x01",
            "你们现在已经\x01",
            "不属于警备队了。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x109,
        (
            "#10100F没关系，虽说我正在外派之中，\x01",
            "但您还是可以用习惯的方式来称呼我。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x104,
        "#00302F哈哈，我也不在意这些哦。\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#00000F这里……\x01",
            "只有您二位负责警戒吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x1B,
        (
            "是的，毕竟各国首脑和\x01",
            "记者都在这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x1B,
        (
            "上级认为警备队应该尽量\x01",
            "避免露面，所以只安排了\x01",
            "最低限度的警备人员。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x102,
        "#00101F您的意思是……\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x109,
        (
            "#10101F嗯，因为对两大国有顾虑。\x02\x03",

            "虽说自治州法已经限制了\x01",
            "警备队的军备规模，\x01",
            "但它始终还是一个相当于军队的组织……\x02\x03",

            "即使被限制了规模，\x01",
            "也依然投入了大量资金来\x01",
            "维持部队、扩充装备。\x02\x03",

            "#10108F因此，在这种大型会议上，\x01",
            "警备队这个议题很容易被\x01",
            "当作发难点而摆上台面。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x103,
        (
            "#00203F原来如此……\x01",
            "所以才尽力不让警备队\x01",
            "进入两大国的视线。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x105,
        (
            "#10306F哎呀呀，外交这种东西\x01",
            "还真是麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x1A,
        (
            "话虽如此，\x01",
            "但最好还是不要随便说出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x1A,
        (
            "而且这只是表面上的\x01",
            "安排而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x1A,
        (
            "其实在下面的楼层，\x01",
            "备有一支正在待命的中队，\x01",
            "他们随时可以出动。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x1A,
        (
            "不必担心，万一出现问题，\x01",
            "我们也可以立刻处理。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        "#00001F原来如此，我明白了。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x102,
        "#00101F如果有什么万一，就拜托各位了。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    SetScenarioFlags(0x1C1, 6)
    Call(0, 36)
    Return()

    # Function_24_3C5C end

    def Function_25_40B6(): pass

    label("Function_25_40B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_4127")

    #C0184
    ChrTalk(
        0xFE,
        (
            "会议前半程已经结束，\x01",
            "状况依然没有什么变化。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "真希望能在事前\x01",
            "掌握到恐怖分子的动向啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4215")

    label("loc_4127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4215")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4142")
    Call(0, 24)
    Jump("loc_4215")

    label("loc_4142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41C3")
    TurnDirection(0xFE, 0x109, 0)

    #C0186
    ChrTalk(
        0xFE,
        (
            "诺艾尔上士，今天我们\x01",
            "都要尽力而为。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        "相关楼层的警备就交给你们了。\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x109,
        "#10100F好的，我明白了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_4215")

    label("loc_41C3")

    TurnDirection(0xFE, 0x109, 0)

    #C0189
    ChrTalk(
        0xFE,
        (
            "诺艾尔上士，今天我们\x01",
            "都要尽力而为。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        "相关楼层的警备就交给你们了。\x02",
    )

    CloseMessageWindow()

    label("loc_4215")

    TalkEnd(0xFE)
    Return()

    # Function_25_40B6 end

    def Function_26_4219(): pass

    label("Function_26_4219")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_422A")
    Jump("loc_45D2")

    label("loc_422A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_45D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4245")
    Call(0, 27)
    Jump("loc_45D2")

    label("loc_4245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4501")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_42E0")
    Jump("loc_432A")

    label("loc_42E0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4300")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_432A")

    label("loc_4300")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4320")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_432A")

    label("loc_4320")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_432A")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    #C0191
    ChrTalk(
        0x101,
        (
            "#00001F对了，副局长，\x01",
            "您刚刚提到的\x01",
            "『那家伙』是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x102,
        (
            "#00100F嗯，我也十分在意，\x01",
            "难道是什么可疑人物的情报吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xB,
        "嗯？我妻子她……\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    #C0194
    ChrTalk(
        0xB,
        (
            "不对！这和你们\x01",
            "完全无关。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xB,
        "赶、赶紧回到自己的岗位上去！\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        "#11P#00005F好、好的，明白了。\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x104,
        (
            "#00306F（难道他刚才\x01",
            "  在想自己的老婆？）\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x103,
        (
            "#00203F（他是出名的怕老婆呢。\x01",
            "  ……肯定有不少问题吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#00106F（是啊……\x01",
            "  就让他一个人静静吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1C2, 0)
    SetChrSubChip(0xB, 0x0)
    Jump("loc_45D2")

    label("loc_4501")

    SetChrSubChip(0xB, 0x0)

    #C0200
    ChrTalk(
        0xB,
        "可恶，每个人都和我过不去……\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xB,
        "既然如此，我就……\x02",
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

    label("loc_45D2")

    TalkEnd(0xFE)
    Return()

    # Function_26_4219 end

    def Function_27_45D6(): pass

    label("Function_27_45D6")

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
            "可恶，难道那家伙……\x01",
            "不对，绝对不可能有那种事……\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        (
            "#11P#00005F（那、那家伙是指……？）\x02\x03",

            "#00000F请问……皮埃尔副局长？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0204
    ChrTalk(
        0xB,
        "哇！？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x1)

    #C0205
    ChrTalk(
        0xB,
        "还、还以为是谁呢，原来是你们支援科啊。\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xB,
        "找我有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x103,
        "#00200F那个……副局长，您在这里做什么？\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        "#5P#00005F喂喂，缇欧……\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(500)

    #C0209
    ChrTalk(
        0xB,
        (
            "竟然问我在这里做什么……\x01",
            "我可是警备对策室的室长啊！\x02",
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
        "#00305F哎，是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x105,
        (
            "#10300F我想起来了，我们拿到的\x01",
            "资料上的确有他的名字。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x103,
        "#00203F……原来如此，是我了解不足。\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xB,
        "你、你们……！\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        "#00006F唉，太迟了吗……\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x102,
        (
            "#00106F应该事先\x01",
            "提醒他们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x109,
        "#12P#10106F的、的确啊……\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，但身为室长，\x01",
            "为何不待在对策室里呢？\x02\x03",

            "现在好像也不是休息时间啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xB,
        (
            "哼、哼……我已经将现场指挥工作\x01",
            "全权委托给达德利了。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xB,
        (
            "既然如此，\x01",
            "我要是待在那里，\x01",
            "他们反而会不好办事。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xB,
        (
            "不管你们怎么想……\x01",
            "但在这方面，我可是个通情达理的上司。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xB,
        (
            "总、总之……\x01",
            "你们听好了，可不要拖\x01",
            "达德利的后腿啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x101,
        "#11P#00006F知、知道了。\x02",
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

    # Function_27_45D6 end

    def Function_28_4AAB(): pass

    label("Function_28_4AAB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_4ABF")
    Call(0, 6)
    Jump("loc_4C5B")

    label("loc_4ABF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_4C52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BC9")

    #C0223
    ChrTalk(
        0x8,
        (
            "#02203F唔，真没想到\x01",
            "两国首脑会同时召见你们。\x02\x03",

            "#02200F你们肯定很紧张吧……\x01",
            "但这可是个千载难逢的机会。\x02\x03",

            "哪怕只是近距离感受一下他们两人的气场，\x01",
            "也能让你们学到不少东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        "#00001F嗯，您说得没错。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x102,
        "#00100F伊安律师，我们这就过去了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_4C4D")

    label("loc_4BC9")


    #C0226
    ChrTalk(
        0x8,
        (
            "#02200F我在会议上也有所体会，\x01",
            "哪怕只是近距离感受一下他们两人的气场，\x01",
            "也能让人学到不少东西。\x02\x03",

            "你们别想太多，\x01",
            "坦然地去见他们吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C4D")

    Jump("loc_4C5B")

    label("loc_4C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4C5B")

    label("loc_4C5B")

    TalkEnd(0xFE)
    Return()

    # Function_28_4AAB end

    def Function_29_4C5F(): pass

    label("Function_29_4C5F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_4C73")
    Call(0, 6)
    Jump("loc_4C8A")

    label("loc_4C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_4C81")
    Jump("loc_4C8A")

    label("loc_4C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4C8A")

    label("loc_4C8A")

    TalkEnd(0xFE)
    Return()

    # Function_29_4C5F end

    def Function_30_4C8E(): pass

    label("Function_30_4C8E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_4D13")

    #C0227
    ChrTalk(
        0xFE,
        (
            "不知该怎么形容……\x01",
            "包括伊安律师在内，一群散发着\x01",
            "独特感觉的人聚集在休息室里。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        "总觉得让人有种很奇妙的感觉。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5242")

    label("loc_4D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_4D6B")

    #C0229
    ChrTalk(
        0xFE,
        (
            "对了，皮埃尔副局长\x01",
            "在哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "他一直没回来，\x01",
            "是去对策总部了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5242")

    label("loc_4D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5242")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DDD")

    #C0231
    ChrTalk(
        0xFE,
        (
            "皮埃尔副局长\x01",
            "从刚才起就一直\x01",
            "低声念叨着什么，他没事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        "……实在是让人很在意啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5242")

    label("loc_4DDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51F0")

    #C0233
    ChrTalk(
        0xFE,
        (
            "你们刚才和皮埃尔副局长\x01",
            "聊了几句吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        "他的状态还好吗？\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        "#00012F这……该怎么说呢……\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x104,
        (
            "#00306F那种状态究竟算好还是不好？\x01",
            "实在是不好判断啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x103,
        (
            "#00203F总之，还算是\x01",
            "平时的老样子吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x102,
        (
            "#00106F但我记得\x01",
            "他以前并不会\x01",
            "那么低声下气啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "原来如此，低声下气吗……\x01",
            "这也是没办法的事啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "我们警察局\x01",
            "原本有两位\x01",
            "副局长……\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "但在前任局长下台之后，\x01",
            "被任命为新局长的\x01",
            "却是另一位副局长。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x101,
        (
            "#00001F我也听说过。\x02\x03",

            "不过我们和另一位副局长\x01",
            "完全没有交流过……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "另外，你们知道吗……\x01",
            "其实那位新局长\x01",
            "是皮埃尔副局长的后辈哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0244
    ChrTalk(
        0x101,
        "#00005F新局长是……皮埃尔副局长的后辈？\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x109,
        "#10106F原来如此，所以他才……\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "但话说回来，我还真\x01",
            "无法想象皮埃尔副局长\x01",
            "当上局长的样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "说实话，我觉得这种\x01",
            "人事安排很妥当。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "但对副局长来说……\x01",
            "被同为副局长，并且资历不如\x01",
            "自己的人超越，肯定很难受吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，这的确是\x01",
            "人之常情。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "总之，他现在\x01",
            "遇到了很多问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "所以你们在和他接触的时候，\x01",
            "尽量大度一些为好……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "如果被他唠叨了几句，\x01",
            "就理解为他在\x01",
            "担心你们好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        "#00012F好、好的……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C2, 1)
    Jump("loc_5242")

    label("loc_51F0")


    #C0254
    ChrTalk(
        0xFE,
        (
            "皮埃尔副局长现在\x01",
            "遇到了很多问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "虽然他很爱唠叨，\x01",
            "但我们还是要多忍耐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5242")

    TalkEnd(0xFE)
    Return()

    # Function_30_4C8E end

    def Function_31_5246(): pass

    label("Function_31_5246")

    TalkBegin(0xFE)
    OP_4B(0xFE, 0xFF)

    #C0256
    ChrTalk(
        0xFE,
        (
            "听好，会议前半程结束之后，\x01",
            "立刻就会召开记者招待会。\x01",
            "要迅速准备好会场。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_31_5246 end

    def Function_32_52A1(): pass

    label("Function_32_52A1")

    TalkBegin(0xFE)
    OP_4B(0xFE, 0xFF)

    #C0257
    ChrTalk(
        0xFE,
        (
            "明白了……\x01",
            "要做得又快又好，对吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_32_52A1 end

    def Function_33_52D7(): pass

    label("Function_33_52D7")

    TalkBegin(0xFE)

    #C0258
    ChrTalk(
        0xFE,
        (
            "好，盒饭盒饭……\x01",
            "呼，终于可以吃饭了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_52D7 end

    def Function_34_5309(): pass

    label("Function_34_5309")

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
        "真是辛苦各位了。\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xC,
        (
            "#02110F罗伊德，你们来了啊。\x02\x03",

            "#02102F哎呀～\x01",
            "正式会议终于召开了～\x02\x03",

            "克洛斯贝尔自治州与周边四国的\x01",
            "代表人物齐聚一堂……\x01",
            "这真是一场前所未有的国际会议啊……\x02\x03",

            "而且这场空前的盛会还是在\x01",
            "史上首座超高层建筑物——\x01",
            "兰花塔中举行的……\x02\x03",

            "#02109F姐姐我已经快承受不住\x01",
            "这种强烈的兴奋与紧张了，\x01",
            "好像连心脏都要爆炸了呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x101,
        (
            "#12P#00012F兴奋暂且不说，\x01",
            "但我完全看不出\x01",
            "您在紧张啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x103,
        (
            "#6P#00200F是啊，看起来和平时的\x01",
            "格蕾丝小姐没什么不同。\x02",
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
            "#02105F哎呀，小缇欧，\x01",
            "久别重逢，竟然说得这么不留情面。\x02\x03",

            "#02104F当然，我也承认心中的\x01",
            "兴奋之情要远比紧张更强……\x01",
            "好了，先不说这些了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xE, 500)

    #C0264
    ChrTalk(
        0xC,
        (
            "#02100F诺蒂亚小姐，我给你介绍一下，\x01",
            "他们就是特别任务支援科哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xE,
        (
            "啊，就是这些孩子吗？\x01",
            "呵呵，真人比照片上更精神呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xE,
        (
            "我是利贝尔通讯社的诺蒂亚，\x01",
            "今天很高兴见到大家，请多关照。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xE1, 0x1F4)

    #C0267
    ChrTalk(
        0x101,
        "#12P#00000F啊，彼此彼此。\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x102,
        (
            "#6P#00100F利贝尔通讯社……\x01",
            "就是王国最大的新闻机构吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xD,
        (
            "是啊，关于利贝尔通讯社，\x01",
            "在业界内还有另一个热门话题呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xD,
        (
            "去年的菲利策奖获得者\x01",
            "就是利贝尔通讯社的记者。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5851")

    #C0271
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，就是尼尔森先生\x01",
            "也曾拿到过的那个大奖吧？\x02\x03",

            "据说是每年颁发给\x01",
            "年度最优秀新闻工作者的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58A2")

    label("loc_5851")


    #C0272
    ChrTalk(
        0x105,
        (
            "#12P#10300F菲利策奖……\x02\x03",

            "我记得是颁发给年度\x01",
            "最优秀新闻工作者的\x01",
            "荣誉大奖吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58A2")


    #C0273
    ChrTalk(
        0xE,
        "#5P呵呵，你还挺清楚的嘛。\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xE,
        (
            "#5P顺便一提，获奖者是\x01",
            "奈尔·班兹和\x01",
            "朵洛希·海娅特。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xE,
        (
            "#5P他们是利贝尔通讯社引以为豪的\x01",
            "王牌记者和天才摄影师。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x104,
        (
            "#12P#00302F对了……利贝尔的记者\x01",
            "在去年获奖……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x109,
        (
            "#6P#10105F莫非是那期\x01",
            "关于利贝尔异变的报道\x01",
            "获得了高度评价吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xE,
        "#5P嗯，正是。\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xE,
        (
            "#5P但严格来说，\x01",
            "这是结合了以前那些特辑\x01",
            "而做出的综合评价。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x103,
        (
            "#6P#00203F原来如此……\x01",
            "看来真是很厉害的记者啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xC,
        (
            "#02109F是啊，我们也\x01",
            "绝对不能输给他们。\x02\x03",

            "#02103F每一名记者\x01",
            "都对菲利策奖憧憬不已……\x02\x03",

            "为了有朝一日摘取桂冠，\x01",
            "对待每一次取材，都必须要\x01",
            "全力以赴才行，这次就更不用说了。\x02\x03",

            "#02110F所以说，雷因兹，\x01",
            "我们绝不能被别人抢先，\x01",
            "加油干吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x0, 0x1F4)

    #C0282
    ChrTalk(
        0xD,
        "是、是的！前辈！\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x101,
        (
            "#12P#00012F（嗯～她好像\x01",
            "  比平时还要有干劲啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x102,
        (
            "#6P#00106F（不管怎么说，\x01",
            "  但愿她能老老实实地\x01",
            "  遵守规则……）\x02",
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

    # Function_34_5309 end

    def Function_35_5BF6(): pass

    label("Function_35_5BF6")

    Sound(160, 0, 100, 0)
    Return()

    # Function_35_5BF6 end

    def Function_36_5BFD(): pass

    label("Function_36_5BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C25")
    SetScenarioFlags(0x146, 3)

    label("loc_5C25")

    Return()

    # Function_36_5BFD end

    def Function_37_5C26(): pass

    label("Function_37_5C26")

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

    def lambda_5DE6():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5DE6)
    Sleep(50)

    def lambda_5DF6():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5DF6)
    Sleep(50)

    def lambda_5E06():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5E06)
    Sleep(50)

    def lambda_5E16():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5E16)
    Sleep(50)

    def lambda_5E26():
        OP_93(0x105, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5E26)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0285
    ChrTalk(
        0x102,
        "#5P#00102F#10A好壮观……\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_68(79000, 1000, -2700, 2000)
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    Sleep(500)

    def lambda_5E8F():
        OP_97(0xFE, 0x12C, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E8F)
    Sleep(300)

    def lambda_5EAC():
        OP_93(0xFE, 0xB4, 0x15E)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_5EAC)

    def lambda_5EB9():
        OP_97(0xFE, 0x12C, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5EB9)
    Sleep(300)

    def lambda_5ED6():
        OP_97(0xFE, 0x12C, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5ED6)
    Sleep(300)

    def lambda_5EF3():
        OP_97(0xFE, 0x12C, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5EF3)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_5C26 end

    def Function_38_5F1C(): pass

    label("Function_38_5F1C")

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

    # Function_38_5F1C end

    def Function_39_5F8C(): pass

    label("Function_39_5F8C")


    def lambda_5F91():
        OP_95(0xFE, 81000, 0, 1500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5F91)

    def lambda_5FAB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5FAB)
    WaitChrThread(0xFE, 1)

    def lambda_5FC0():
        OP_95(0xFE, 77500, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5FC0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_39_5F8C end

    def Function_40_5FE1(): pass

    label("Function_40_5FE1")


    def lambda_5FE6():
        OP_95(0xFE, 81000, 0, 2000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5FE6)

    def lambda_6000():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6000)
    WaitChrThread(0xFE, 1)

    def lambda_6015():
        OP_95(0xFE, 79200, 0, -400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6015)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0286
    ChrTalk(
        0x101,
        "#5P#00005F#8A啊……\x02",
    )
    #Auto

    CloseMessageWindow()
    Return()

    # Function_40_5FE1 end

    def Function_41_6071(): pass

    label("Function_41_6071")


    def lambda_6076():
        OP_95(0xFE, 81000, 0, 2000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6076)

    def lambda_6090():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6090)
    WaitChrThread(0xFE, 1)

    def lambda_60A5():
        OP_95(0xFE, 78300, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_60A5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_41_6071 end

    def Function_42_60C6(): pass

    label("Function_42_60C6")


    def lambda_60CB():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_60CB)

    def lambda_60E5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_60E5)
    WaitChrThread(0xFE, 1)

    def lambda_60FA():
        OP_95(0xFE, 80400, 0, -100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_60FA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_42_60C6 end

    def Function_43_611B(): pass

    label("Function_43_611B")


    def lambda_6120():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6120)

    def lambda_613A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_613A)
    WaitChrThread(0xFE, 1)

    def lambda_614F():
        OP_95(0xFE, 79500, 0, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_614F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_43_611B end

    def Function_44_6170(): pass

    label("Function_44_6170")


    def lambda_6175():
        OP_95(0xFE, 81000, 0, 3000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6175)

    def lambda_618F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_618F)
    WaitChrThread(0xFE, 1)

    def lambda_61A4():
        OP_95(0xFE, 80800, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61A4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_44_6170 end

    def Function_45_61C5(): pass

    label("Function_45_61C5")


    def lambda_61CA():
        OP_95(0xFE, 81000, 0, 3000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61CA)

    def lambda_61E4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_61E4)
    WaitChrThread(0xFE, 1)

    def lambda_61F9():
        OP_95(0xFE, 79900, 0, 2100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61F9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_45_61C5 end

    def Function_46_621A(): pass

    label("Function_46_621A")

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
        "#10109F#5P啊啊啊～！\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x103,
        "#00202F#5P好漂亮的风景……\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x104,
        "#00309F#5P哎呀～真是至高绝景啊。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x20,
        (
            "#02809F#5P哈哈，看来你们相当满意呢。\x02\x03",

            "#02800F……这里是三十四层。\x01",
            "在召开国际会议等大型会议时，\x01",
            "将把这个楼层提供给相关人员待命。\x02\x03",

            "#02800F接下来，\x01",
            "我们就在这个楼层随便逛逛吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_642C():
        TurnDirection(0x101, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_642C)
    Sleep(50)

    def lambda_643C():
        TurnDirection(0x102, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_643C)
    Sleep(50)

    def lambda_644C():
        TurnDirection(0x103, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_644C)
    Sleep(50)

    def lambda_645C():
        TurnDirection(0x109, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_645C)
    Sleep(50)

    def lambda_646C():
        TurnDirection(0x105, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_646C)
    Sleep(50)

    def lambda_647C():
        TurnDirection(0x104, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_647C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)

    def lambda_64A1():

        label("loc_64A1")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_64A1")

    QueueWorkItem2(0x101, 2, lambda_64A1)

    def lambda_64B3():

        label("loc_64B3")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_64B3")

    QueueWorkItem2(0x102, 2, lambda_64B3)

    def lambda_64C5():

        label("loc_64C5")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_64C5")

    QueueWorkItem2(0x103, 2, lambda_64C5)

    def lambda_64D7():

        label("loc_64D7")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_64D7")

    QueueWorkItem2(0x109, 2, lambda_64D7)

    def lambda_64E9():

        label("loc_64E9")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_64E9")

    QueueWorkItem2(0x105, 2, lambda_64E9)

    def lambda_64FB():

        label("loc_64FB")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_64FB")

    QueueWorkItem2(0x104, 2, lambda_64FB)

    #C0291
    ChrTalk(
        0x101,
        "#12P#00002F好的，麻烦您了。\x02",
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

    def lambda_6560():
        OP_97(0x105, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6560)
    Sleep(100)

    def lambda_657D():
        OP_97(0x103, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_657D)
    Sleep(100)

    def lambda_659A():
        OP_97(0x104, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_659A)
    Sleep(100)

    def lambda_65B7():
        OP_97(0x101, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_65B7)
    Sleep(100)

    def lambda_65D4():
        OP_97(0x109, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_65D4)
    Sleep(100)

    def lambda_65F1():
        OP_97(0x102, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_65F1)
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

    def lambda_673F():
        OP_95(0xFE, 8500, 0, -1000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_673F)

    def lambda_6759():
        OP_96(0xFE, 0x2968, 0xFFFFFDA8, 0xFFFFFC18, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_6759)

    def lambda_6773():
        OP_97(0x101, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6773)
    Sleep(50)

    def lambda_6790():
        OP_97(0x102, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6790)
    Sleep(50)

    def lambda_67AD():
        OP_97(0x103, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_67AD)
    Sleep(50)

    def lambda_67CA():
        OP_97(0x104, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_67CA)
    Sleep(50)

    def lambda_67E7():
        OP_97(0x109, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_67E7)
    Sleep(50)

    def lambda_6804():
        OP_97(0x105, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6804)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_682A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_682A)
    Sleep(50)

    def lambda_683E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_683E)
    Sleep(500)

    def lambda_6852():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6852)
    Sleep(50)

    def lambda_6866():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6866)
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
            "#6P#02803F这一排房间是警备对策室和\x01",
            "记者们所使用的休息室。\x02\x03",

            "#02800F为了应对恐怖分子潜入大楼的情况，\x01",
            "特意安排了警备队的一个中队\x01",
            "在下面的楼层待命。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x109,
        "#10104F#11P我也听说过这件事。\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x104,
        (
            "#00300F#11P据说那些队员都是从警备队\x01",
            "严格筛选出来的精英。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x105,
        (
            "#10305F#11P说起记者……\x01",
            "格蕾丝小姐也来了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x5A, 0x1F4)

    #C0296
    ChrTalk(
        0x20,
        (
            "#6P#02805F哦，你是说克洛斯贝尔时代周刊的\x01",
            "那个女记者吗？\x02\x03",

            "#02804F名单上有她的名字，\x01",
            "我想她应该也会来采访吧。\x02\x03",

            "#02800F顺便一提，\x01",
            "除了记者招待会时间之外，\x01",
            "新闻人员是不能离开这个楼层的。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x105,
        "#10302F#11P原来如此，很合理的安排呢。\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x102,
        (
            "#11P#00106F毕竟有些记者喜欢乱来，\x01",
            "会趁警备人员不注意时\x01",
            "进行突击采访……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x103,
        (
            "#12P#00211F说起这个，最有可能那么做的人\x01",
            "恐怕就是格蕾丝小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        (
            "#12P#00006F唔……如果真的发现她那样做，\x01",
            "我们可得阻止她。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x10E, 0x1F4)

    def lambda_6B77():
        OP_98(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_6B77)

    def lambda_6B91():
        OP_97(0x101, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6B91)
    Sleep(50)

    def lambda_6BAE():
        OP_97(0x102, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6BAE)
    Sleep(50)

    def lambda_6BCB():
        OP_97(0x103, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6BCB)
    Sleep(50)

    def lambda_6BE8():
        OP_97(0x104, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6BE8)
    Sleep(50)

    def lambda_6C05():
        OP_97(0x109, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6C05)
    Sleep(50)

    def lambda_6C22():
        OP_97(0x105, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6C22)
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

    def lambda_6D4A():
        OP_97(0xFE, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_6D4A)

    def lambda_6D64():
        OP_98(0xFE, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_6D64)

    def lambda_6D7E():
        OP_97(0x101, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6D7E)
    Sleep(50)

    def lambda_6D9B():
        OP_97(0x102, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6D9B)
    Sleep(50)

    def lambda_6DB8():
        OP_97(0x103, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6DB8)
    Sleep(50)

    def lambda_6DD5():
        OP_97(0x104, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6DD5)
    Sleep(50)

    def lambda_6DF2():
        OP_97(0x109, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6DF2)
    Sleep(50)

    def lambda_6E0F():
        OP_97(0x105, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6E0F)
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
            "#02800F#11P接下来，就带你们\x01",
            "看看这个房间吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-14000, 1000, 17400, 1000)
    FadeToDark(1000, 0, -1)

    def lambda_6E8B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6E8B)
    Sleep(50)

    def lambda_6E9B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6E9B)

    def lambda_6EA8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6EA8)
    Sleep(50)

    def lambda_6EB8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6EB8)

    def lambda_6EC5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6EC5)
    Sleep(50)

    def lambda_6ED5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6ED5)
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
        "#11P#10302F嘿……这房间可真棒。\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        (
            "#11P#00002F这里应该是休息室吧？\x01",
            "可真够宽敞的啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x20,
        (
            "#02804F这是为会议相关人员\x01",
            "准备的休息室。\x02\x03",

            "#02800F在休息时间，\x01",
            "你们可以随意使用这里。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_70C3():
        TurnDirection(0x101, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_70C3)
    Sleep(50)

    def lambda_70D3():
        TurnDirection(0x102, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_70D3)
    Sleep(50)

    def lambda_70E3():
        TurnDirection(0x103, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_70E3)
    Sleep(50)

    def lambda_70F3():
        TurnDirection(0x104, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_70F3)
    Sleep(50)

    def lambda_7103():
        TurnDirection(0x109, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7103)
    Sleep(50)

    def lambda_7113():
        TurnDirection(0x105, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7113)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0305
    ChrTalk(
        0x101,
        "#6P#00004F好，那我们就不客气了。\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x102,
        (
            "#6P#00109F呵呵，待会到这里\x01",
            "喝杯茶吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x20,
        (
            "#02809F好了，这个楼层大致就是这样。\x01",
            "我带你们去参观下一层吧。\x02",
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

    def lambda_72B7():
        OP_95(0xFE, -13000, 0, 1800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_72B7)

    def lambda_72D1():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_72D1)

    def lambda_72EB():
        OP_97(0x101, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_72EB)
    Sleep(50)

    def lambda_7308():
        OP_97(0x102, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7308)
    Sleep(50)

    def lambda_7325():
        OP_97(0x103, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7325)
    Sleep(50)

    def lambda_7342():
        OP_97(0x104, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7342)
    Sleep(50)

    def lambda_735F():
        OP_97(0x109, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_735F)
    Sleep(50)

    def lambda_737C():
        OP_97(0x105, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_737C)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x20, 1)

    def lambda_73A4():
        OP_95(0xFE, -14800, 0, 0, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_73A4)
    WaitChrThread(0x27, 1)
    OP_6B(0xFF)
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_73DE():

        label("loc_73DE")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_73DE")

    QueueWorkItem2(0x101, 2, lambda_73DE)
    WaitChrThread(0x102, 0)

    def lambda_73F4():

        label("loc_73F4")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_73F4")

    QueueWorkItem2(0x102, 2, lambda_73F4)
    WaitChrThread(0x103, 0)

    def lambda_740A():

        label("loc_740A")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_740A")

    QueueWorkItem2(0x103, 2, lambda_740A)
    WaitChrThread(0x104, 0)

    def lambda_7420():

        label("loc_7420")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_7420")

    QueueWorkItem2(0x104, 2, lambda_7420)
    WaitChrThread(0x20, 1)

    def lambda_7436():
        OP_95(0xFE, -17600, 0, 0, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_7436)
    Sleep(300)
    Sound(103, 0, 100, 0)

    def lambda_7459():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_7459)
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
            "#12P#00005F这是……\x01",
            "疏散楼梯吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x104,
        (
            "#00305F下楼的楼梯\x01",
            "已经被封锁了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x20,
        (
            "#02803F#5P原本可以经由\x01",
            "这个楼梯抵达一楼。\x02\x03",

            "#02801F但在本次会议期间，\x01",
            "除了三十四、三十五和三十六层之外，\x01",
            "其它楼层都已被完全封锁了。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x109,
        (
            "#10101F原来如此……\x01",
            "是出于警备方面的考虑吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x105,
        (
            "#10305F可是，如果万一发生了地震\x01",
            "之类的突发状况，又该怎么办呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x20,
        (
            "#02806F#5P如果发生了那种情况，\x01",
            "疏散楼梯的全部封锁都会自动解除。\x02\x03",

            "#02800F没办法，安全措施是不可能\x01",
            "做到完美无缺的。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x101,
        (
            "#12P#00003F原来如此……\x01",
            "我们会注意这方面的。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x103,
        (
            "#12P#00208F……看来也有必要考虑一下\x01",
            "该如何防犯网络入侵呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x20,
        (
            "#02804F#5P既然都到这里来了，\x01",
            "我们就走楼梯上去吧。\x02\x03",

            "#02800F三十五层是\x01",
            "国际会议专用楼层。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_46_621A end

    def Function_47_7916(): pass

    label("Function_47_7916")

    OP_92(0xFE, 0x128E0, 0x0, 0x1F4)

    def lambda_7928():
        OP_95(0xFE, 76000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7928)
    WaitChrThread(0xFE, 1)

    def lambda_7946():
        OP_95(0xFE, 68000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7946)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_47_7916 end

    def Function_48_7960(): pass

    label("Function_48_7960")


    def lambda_7965():
        OP_95(0xFE, -14800, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7965)
    WaitChrThread(0xFE, 1)

    def lambda_7983():
        OP_95(0xFE, -17600, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7983)
    Sleep(300)

    def lambda_79A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_79A0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_48_7960 end

    def Function_49_79B1(): pass

    label("Function_49_79B1")


    def lambda_79B6():
        OP_95(0xFE, -52000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_79B6)

    def lambda_79D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_79D0)
    WaitChrThread(0xFE, 1)

    def lambda_79E5():
        OP_95(0xFE, -55000, 0, -100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_79E5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_49_79B1 end

    def Function_50_7A06(): pass

    label("Function_50_7A06")


    def lambda_7A0B():
        OP_95(0xFE, -51000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7A0B)

    def lambda_7A25():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7A25)
    WaitChrThread(0xFE, 1)

    def lambda_7A3A():
        OP_95(0xFE, -53500, 0, 400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7A3A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_50_7A06 end

    def Function_51_7A5B(): pass

    label("Function_51_7A5B")


    def lambda_7A60():
        OP_95(0xFE, -52000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7A60)

    def lambda_7A7A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7A7A)
    WaitChrThread(0xFE, 1)

    def lambda_7A8F():
        OP_95(0xFE, -54500, 0, -1100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7A8F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_51_7A5B end

    def Function_52_7AB0(): pass

    label("Function_52_7AB0")


    def lambda_7AB5():
        OP_95(0xFE, -51000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7AB5)

    def lambda_7ACF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7ACF)
    WaitChrThread(0xFE, 1)

    def lambda_7AE4():
        OP_95(0xFE, -53000, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7AE4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_52_7AB0 end

    def Function_53_7B05(): pass

    label("Function_53_7B05")


    def lambda_7B0A():
        OP_95(0xFE, -51000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B0A)

    def lambda_7B24():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7B24)
    WaitChrThread(0xFE, 1)

    def lambda_7B39():
        OP_95(0xFE, -51500, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B39)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_53_7B05 end

    def Function_54_7B5A(): pass

    label("Function_54_7B5A")


    def lambda_7B5F():
        OP_95(0xFE, -51000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B5F)

    def lambda_7B79():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7B79)
    WaitChrThread(0xFE, 1)

    def lambda_7B8E():
        OP_95(0xFE, -51500, 0, -900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B8E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_54_7B5A end

    def Function_55_7BAF(): pass

    label("Function_55_7BAF")

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
            "#11P#00000F好，我们已经\x01",
            "巡视过所有区域了。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x109,
        (
            "#6P#10100F看来现阶段\x01",
            "并没有什么问题呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x104,
        (
            "#5P#00302F是啊，那我们就\x01",
            "再去巡逻一圈吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x102,
        (
            "#00104F好……\x02\x03",

            "#00108F……不知会议的\x01",
            "进展状况如何了。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x101,
        (
            "#11P#00006F嗯，我想市长和议长\x01",
            "应该都在努力吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x103,
        (
            "#12P#00201F但关键问题还是在于\x01",
            "『铁血宰相』和洛克史密斯总统。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x105,
        (
            "#12P#10302F好啦，休息时间到了之后，\x01",
            "找个人问问不就好了。\x02",
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

    # Function_55_7BAF end

    def Function_56_7E11(): pass

    label("Function_56_7E11")

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
            "#11P#00000F好，我们已经\x01",
            "巡视过所有地方了。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x109,
        (
            "#6P#10100F看来现阶段\x01",
            "并没有什么问题呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x104,
        (
            "#5P#00302F是啊，那我们就\x01",
            "再去巡逻一圈吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x102,
        (
            "#00104F好……\x02\x03",

            "#00108F……不知会议的\x01",
            "进展状况如何了。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x101,
        (
            "#11P#00006F嗯，我想市长和议长\x01",
            "应该都在努力吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x103,
        (
            "#12P#00201F但关键问题还是在于\x01",
            "『铁血宰相』和洛克史密斯总统。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x105,
        (
            "#12P#10302F好啦，休息时间到了之后，\x01",
            "找个人问问不就好了。\x02",
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

    # Function_56_7E11 end

    def Function_57_8073(): pass

    label("Function_57_8073")

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
            "就这样，罗伊德等人得到机会，\x01",
            "和提前退场休息的伊安律师\x01",
            "展开了交谈。\x07\x00\x02",
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
            "#02205F#5P原来如此……由于那种原因，\x01",
            "你们也参与警备工作了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x101,
        (
            "#11P#00002F是的，但说实话，让我们加入，\x01",
            "其实也就是象征性地加一道保险而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x8,
        (
            "#02210F#5P不必谦虚，你们可是阻止了\x01",
            "暗杀市长事件的头号功劳者啊。\x02\x03",

            "#02200F只要看到你们在这里，\x01",
            "我就能感到非常安心。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x102,
        "#11P#00104F您真是太过奖了……\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x104,
        "#12P#00302F哈哈，谢谢夸奖。\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x103,
        (
            "#00200F#11P对了，律师，\x01",
            "会议情况如何？\x02\x03",

            "好像并没有感觉到\x01",
            "太过险恶的气氛。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        (
            "#02210F#5P嗯，目前还算顺利。\x02\x03",

            "好几项通商协议都\x01",
            "得到了各国的同意……\x02\x03",

            "#02200F看来迪塔市长特意举办\x01",
            "这场会议，并没有白费功夫……\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        "#11P#00102F呵呵，这样啊……\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x109,
        "#12P#10109F总算是放心一些了。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x105,
        (
            "#6P#10300F但您说『目前』，\x01",
            "这就代表您还有某些忧虑吧？\x02",
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
        "#11P#00105F哎……？\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        "#11P#00001F……是这样吗？\x02",
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
            "#02203F#5P唔，我作为旁听人，\x01",
            "本不该谈及这个问题……\x02\x03",

            "但在会议前半程，谈论的几乎都是\x01",
            "贸易、金融等方面的经济类提案。\x02\x03",

            "#02201F……而到了会议的后半程，\x01",
            "就会开始讨论各国首脑提出的议案……\x02\x03",

            "恐怕还会出现有关克洛斯贝尔的\x01",
            "安全保障问题的议案。\x02",
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
        "#11P#00013F这……！\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x104,
        (
            "#12P#00301F……安全保障……\x01",
            "也就是说，会涉及军事问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x109,
        (
            "#12P#10108F但总要顾虑到两年前\x01",
            "签订的《互不侵犯条约》吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x8,
        (
            "#02203F#5P那只是利贝尔的女王陛下\x01",
            "为了控制克洛斯贝尔当时的危机\x01",
            "而提出的条约。\x02\x03",

            "与雷米菲利亚完全无关，\x01",
            "而且克洛斯贝尔自身也与\x01",
            "《互不侵犯条约》毫无关系可言。\x02\x03",

            "#02201F正因如此，\x01",
            "我们十分需要一个全新的\x01",
            "安全保障方案。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x102,
        (
            "#11P#00106F……的确，\x01",
            "外公也一直在为这件事挂心。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x103,
        (
            "#00205F#11P也就是说，只要签订一项把克洛斯贝尔\x01",
            "包含在内的新条约就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x109,
        (
            "#12P#10101F是啊，重新签署一项和\x01",
            "《互不侵犯条约》类似的，\x01",
            "禁止以武力解决国家间纷争的新条约……\x02\x03",

            "#10105F……啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x101,
        (
            "#11P#00006F原来如此……\x01",
            "克洛斯贝尔并不是『国家』。\x02\x03",

            "#00008F只是一个被帝国和共和国\x01",
            "认可的『自治州』而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x8,
        (
            "#02203F#5P没错，这就意味着\x01",
            "克洛斯贝尔并没有签署\x01",
            "『国际条约』的国家主权。\x02\x03",

            "虽然可以签订经济方面的『协议』，\x01",
            "但却不能站在对等的立场签署『条约』。\x02\x03",

            "#02201F归根结底，就是因为这样，\x01",
            "才导致这片土地的安全得不到保障。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x104,
        (
            "#12P#00306F事情真是复杂……\x01",
            "不过我总算大致理解了。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x103,
        (
            "#00208F#11P……抱歉，\x01",
            "我可以提个问题吗？\x02\x03",

            "#00203F除了克洛斯贝尔之外，\x01",
            "还有其它的自治州。\x02\x03",

            "比如列曼自治州、奥雷德自治州、\x01",
            "诺桑普里亚自治州……\x02\x03",

            "#00200F这些自治州也和我们一样，\x01",
            "无法缔结国际条约吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x8,
        (
            "#02210F#5P不，它们是可以的。\x02\x03",

            "#02200F虽然其它自治州也\x01",
            "因为自身的历史问题，\x01",
            "没有成立为国家……\x02\x03",

            "但『宗主国』将权力转交给了它们，\x01",
            "承认它们拥有同等的主权。\x02",
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
            "#11P#00103F其它自治州与\x01",
            "克洛斯贝尔的最大不同……\x02\x03",

            "#00101F就在于它们的宗主国『亚尔特利亚法典国』\x01",
            "承认了它们的主权。\x02",
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
        "#00205F#11P啊……\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x105,
        (
            "#6P#10305F说到亚尔特利亚法典国，\x01",
            "就是七耀教会的总部吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x102,
        (
            "#11P#00104F没错，虽然国土狭小，\x01",
            "但却拥有宗教上的权威……\x02\x03",

            "#00100F大多数自治州和自由都市\x01",
            "都是倚仗那里才得以成立。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x101,
        (
            "#5P#00006F但克洛斯贝尔却是在帝国和\x01",
            "共和国的认可下而成立的『自治州』……\x02\x03",

            "#00001F也就是说，克洛斯贝尔\x01",
            "拥有两个宗主国。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x102,
        (
            "#11P#00108F没错，从历史角度来看，\x01",
            "这也引发了许多扭曲的事态与悲剧……\x02\x03",

            "如果克洛斯贝尔\x01",
            "能拥有些许主权，\x01",
            "状况也许就会有所不同了……\x02\x03",

            "#00106F……但两大国恐怕永远都不会\x01",
            "承认克洛斯贝尔的主权。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x109,
        "#12P#10108F……怎么会这样………\x02",
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x103,
        "#00206F#11P……真让人沮丧啊。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x8,
        (
            "#02203F#5P……回到原来的话题吧，\x01",
            "宰相和总统似乎对\x01",
            "安全保障问题都有着各自的提案。\x02\x03",

            "当然了，那绝对不是与\x01",
            "各国缔结平等条约这种好事。\x02\x03",

            "#02201F……议长和市长肯定\x01",
            "也在加强戒备吧。\x02",
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
            "#02210F#5P哈哈，抱歉，\x01",
            "我好像让你们感到不安了。\x02\x03",

            "#02200F不过，麦克道尔议长他们\x01",
            "肯定早就习惯这种状况了。\x02\x03",

            "而且迪塔市长似乎\x01",
            "有什么对策呢。\x02",
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
        "#11P#00005F对策吗？\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x102,
        "#11P#00105F那到底是什么……？\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x8,
        (
            "#02203F#5P这个嘛，我也没有听说\x01",
            "具体内容……\x02",
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
        "#11P#00000F……不好意思。\x02",
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
            "#00008F我是特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0373
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3455V#30W……班宁斯，\x01",
            "这边的记者招待会已经结束了。\x02\x03",

            "#3456V各国首脑们已经回到三十六层，\x01",
            "你们现在在哪里？\x02",
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
            "#00005F啊……我们正在\x01",
            "三十四层的休息室……\x02\x03",

            "#00001F……发生了什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0375
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是这样的，奥斯本宰相和\x01",
            "洛克史密斯总统\x01",
            "都提出了要求。\x02\x03",

            "他们想利用休息时间，\x01",
            "与你们当面会谈。\x02",
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
            "#00011F#4S什么……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0377
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……毕竟对方都是大人物，\x01",
            "实在无法拒绝他们的要求。\x02\x03",

            "你们就趁着休息时间，去两位首脑\x01",
            "位于三十六层的休息室拜访吧。\x02\x03",

            "总统的房间在左侧最里面，\x01",
            "宰相的房间在右侧最里面。\x02",
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
            "#00006F请、请等一下！\x01",
            "这究竟是为什么……\x02\x03",

            "#00011F而且这责任未免也太重大了！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0379
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……别啰嗦了，班宁斯。\x02\x03",

            "这可是一个能够试探\x01",
            "双方想法的绝佳机会。\x02",
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

            "#00003F……我明白了，\x01",
            "我们会立刻前往两位首脑的房间。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0381
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有问题的时候，就交给艾莉大小姐吧，\x01",
            "她应该习惯面对这些大人物了。\x02\x03",

            "谈话结束之后，记得向我汇报。\x02",
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
            "#00001F好的……！\x02",
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
        "#11P#00101F罗伊德，刚才那是……\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x104,
        (
            "#12P#00305F喂喂，你刚才是不是\x01",
            "听到了什么很惊人的消息？\x02",
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
        "#5P#00003F是这样的……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0386
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德向众人说明了『铁血宰相』和\x01",
            "洛克史密斯总统召见他们的事情。\x07\x00\x02",
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
        "#12P#10111F什么～！？\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x105,
        "#6P#10305F哇，真的假的？\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x103,
        (
            "#00206F#11P看样子，好像不是\x01",
            "在开玩笑啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x8,
        (
            "#02205F#5P哎呀呀……真让我吃惊。\x02\x03",

            "#02210F看来特别任务支援科的\x01",
            "名气比我想象中的\x01",
            "还要大呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    #C0391
    ChrTalk(
        0x101,
        (
            "#11P#00006F不……只是两位首脑身边\x01",
            "都有我们认识的人。\x02\x03",

            "#00008F说不定正是因为这样，\x01",
            "他们才会对我们产生兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x104,
        (
            "#12P#00301F原来如此……\x01",
            "很有可能啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x102,
        (
            "#11P#00103F……不管怎么说，\x01",
            "我们总不能拒绝他们。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0394
    ChrTalk(
        0x101,
        (
            "#5P#00006F是啊，他们就在三十六层\x01",
            "左侧和右侧最里面的房间。\x02\x03",

            "#00001F马上过去拜访他们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x103,
        "#00201F#11P明白了。\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x109,
        "#12P#10101F是、是的！队长！\x02",
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

    # Function_57_8073 end

    def Function_58_9DFD(): pass

    label("Function_58_9DFD")

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
        "#6P这、这是怎么回事！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 3)

    #C0398
    ChrTalk(
        0xA,
        "#12P为、为何突然……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 3)

    #C0399
    ChrTalk(
        0xB,
        "#12P怎么回事！发生了什么事！？\x02",
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
            "#11P不、不行！\x01",
            "按下按钮也没有反应！！\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xA,
        (
            "#5P可恶……\x01",
            "到底发生了什么事！？\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xC,
        (
            "#02105F#11P喂喂，这下不就\x01",
            "没法采访了吗！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    #C0403
    ChrTalk(
        0xC,
        "#02101F#5P雷因兹，赶快想想办法啊！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)

    #C0404
    ChrTalk(
        0xD,
        "#12P别、别难为我了～！\x02",
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

    # Function_58_9DFD end

    def Function_59_A331(): pass

    label("Function_59_A331")

    Sleep(600)

    def lambda_A339():
        OP_95(0xFE, -51000, 0, -1000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A339)

    def lambda_A353():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A353)
    WaitChrThread(0xFE, 1)

    def lambda_A368():
        OP_95(0xFE, -51100, 0, 700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A368)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_59_A331 end

    def Function_60_A389(): pass

    label("Function_60_A389")


    def lambda_A38E():
        OP_95(0xFE, -51000, 0, -1000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A38E)

    def lambda_A3A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A3A8)
    WaitChrThread(0xFE, 1)

    def lambda_A3BD():
        OP_95(0xFE, -52700, 0, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A3BD)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_60_A389 end

    def Function_61_A3DE(): pass

    label("Function_61_A3DE")

    Sleep(1200)

    def lambda_A3E6():
        OP_95(0xFE, -52000, 0, -1000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A3E6)

    def lambda_A400():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A400)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_61_A3DE end

    def Function_62_A418(): pass

    label("Function_62_A418")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_A425():
        OP_95(0xFE, -51500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A425)

    def lambda_A43F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A43F)
    WaitChrThread(0xFE, 1)

    def lambda_A454():
        OP_95(0xFE, -55500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A454)
    WaitChrThread(0xFE, 1)

    def lambda_A472():
        OP_95(0xFE, -55500, 0, 2500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A472)
    WaitChrThread(0xFE, 1)

    def lambda_A490():
        OP_95(0xFE, -53800, 0, 1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A490)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(300)
    Return()

    # Function_62_A418 end

    def Function_63_A4BC(): pass

    label("Function_63_A4BC")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_A4CC():
        OP_95(0xFE, -51500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A4CC)

    def lambda_A4E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A4E6)
    WaitChrThread(0xFE, 1)

    def lambda_A4FB():
        OP_95(0xFE, -55500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A4FB)
    WaitChrThread(0xFE, 1)

    def lambda_A519():
        OP_95(0xFE, -55500, 0, 2500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A519)
    WaitChrThread(0xFE, 1)

    def lambda_A537():
        OP_95(0xFE, -54200, 0, -300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A537)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_63_A4BC end

    def Function_64_A560(): pass

    label("Function_64_A560")

    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_A570():
        OP_95(0xFE, -51500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A570)

    def lambda_A58A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A58A)
    WaitChrThread(0xFE, 1)

    def lambda_A59F():
        OP_95(0xFE, -55500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A59F)
    WaitChrThread(0xFE, 1)

    def lambda_A5BD():
        OP_95(0xFE, -55500, 0, 2500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A5BD)
    WaitChrThread(0xFE, 1)

    def lambda_A5DB():
        OP_95(0xFE, -55100, 0, 700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A5DB)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_64_A560 end

    def Function_65_A604(): pass

    label("Function_65_A604")

    Sleep(1500)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_A614():
        OP_95(0xFE, -51500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A614)

    def lambda_A62E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A62E)
    WaitChrThread(0xFE, 1)

    def lambda_A643():
        OP_95(0xFE, -55500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A643)
    WaitChrThread(0xFE, 1)

    def lambda_A661():
        OP_95(0xFE, -55500, 0, 2500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A661)
    WaitChrThread(0xFE, 1)

    def lambda_A67F():
        OP_95(0xFE, -55800, 0, 1500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A67F)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_65_A604 end

    def Function_66_A6A8(): pass

    label("Function_66_A6A8")

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
        "#00011F『幻兽』吗……？\x02",
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
            "……嗯，正是。\x02\x03",

            "那是一种与普通魔兽完全不同，\x01",
            "非常不可思议的大型怪物……\x02\x03",

            "目前已在克洛斯贝尔的多处地点\x01",
            "发现了那种怪物的踪迹。\x02",
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

    def lambda_AB0C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_AB0C)
    OP_6F(0x79)
    Sound(853, 0, 100, 0)
    OP_71(0x11, 0x1, 0xA, 0x0, 0x0)
    OP_79(0x11)

    def lambda_AB30():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_AB30)
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
            "#11P啊……\x01",
            "这是我们见过的那个怪物！\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x24,
        (
            "#11P可惜最后没能干掉它，\x01",
            "让它逃走了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0409
    ChrTalk(
        0x109,
        "#10101F#12P#N居然有这种魔兽……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0410
    ChrTalk(
        0x103,
        (
            "#00206F#12P#N我也听说过\x01",
            "这方面的情报……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0411
    ChrTalk(
        0x26,
        (
            "#5P……不仅如此，\x01",
            "现在还发现了其它种类。\x02",
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
        "#6P#N#00007F这、这是……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0413
    ChrTalk(
        0x102,
        "#6P#N#00101F当时在旧矿山出现的……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0414
    ChrTalk(
        0x104,
        "#00307F#12P#N喂喂，又出现了吗！？\x02",
    )

    CloseMessageWindow()
    OP_93(0x26, 0xE1, 0x1F4)
    Sleep(150)

    #C0415
    ChrTalk(
        0x26,
        (
            "#5P前几天，在北部的山岳地带\x01",
            "出现了类型与之相同的怪物。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x26,
        (
            "#5P斯克特和温蔡尔\x01",
            "已经把它消灭了。\x02",
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
        "#6P#00006F这样啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0418
    ChrTalk(
        0x109,
        (
            "#10105F#12P#N难道两个人就\x01",
            "把它消灭了吗？\x02",
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
            "#5P是的，我们出其不意地\x01",
            "发动袭击，好不容易才打倒了它。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x21,
        (
            "#5P这也多亏了你们\x01",
            "之前提供的情报啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x22,
        "#11P不过，当时的手感实在是很奇怪。\x02",
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x22,
        (
            "#11P魔法攻击的有效率与其它魔兽大不相同，\x01",
            "而且它最后还变成一道光消失了。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x102,
        "#6P#00108F果然……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0424
    ChrTalk(
        0x104,
        (
            "#00303F#6P#N……和我们当时遇到的\x01",
            "情况完全相同啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0425
    ChrTalk(
        0x105,
        (
            "#10303F#12P#N说到山岳地带……\x02\x03",

            "#10301F也就是说，这次出现在『野外』了吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B022():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_B022)
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
            "#02006F#5P是的，以前只\x01",
            "出现在『塔』和『僧院』\x01",
            "这类异常场所。\x02\x03",

            "据我们推测，\x01",
            "似乎是由于某种原因，\x01",
            "使那些地方发生了『力场扭曲』……\x02\x03",

            "#02001F可是，这次的『幻兽』\x01",
            "却出现在了山岳地带\x01",
            "和湖沼地带。\x02\x03",

            "说不定连野外地区\x01",
            "都已经出现了\x01",
            "『力场扭曲』现象。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x109,
        "#10108F#12P#N怎、怎么会……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0428
    ChrTalk(
        0x23,
        "#11P这可不是开玩笑的啊。\x02",
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x24,
        (
            "#11P那么，把我们召集到\x01",
            "这里的理由就是……？\x02",
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
            "#5P是的，我们想拜托协会和\x01",
            "特别任务支援科一起负责\x01",
            "处理这些幻兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x26,
        (
            "#5P自从发表独立提案以来，\x01",
            "贝尔加德门和唐古拉姆门\x01",
            "都持续着紧张状态……\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x26,
        (
            "#5P至少在居民投票结束之前，我想让警备队\x01",
            "集中精力，专心完成边境大门的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x101,
        (
            "#6P#00003F#N……明白了，\x01",
            "我们接受这个任务。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0434
    ChrTalk(
        0x21,
        (
            "#12P分工方面，\x01",
            "可以让我们自己安排吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x25,
        (
            "#02004F#5P没问题，我会把资料交给你们，\x01",
            "接下来就全权交由你们负责了。\x02\x03",

            "#02001F还有……我希望你们\x01",
            "尽可能地查明『原因』。\x02",
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

            "#00200F是要查明这些『幻兽』\x01",
            "突然出现的原因吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0437
    ChrTalk(
        0x25,
        (
            "#02003F#5P没错，虽说魔兽\x01",
            "本来就会\x01",
            "周期性地行动……\x02\x03",

            "#02001F但这些『幻兽』与\x01",
            "寻常魔兽不同，可以说是\x01",
            "超乎想象的『异常事态』。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x26,
        (
            "#5P我相信这肯定是由于\x01",
            "什么原因而引起的。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x26,
        (
            "#5P那个原因足以引发『力场扭曲』，\x01",
            "并且可以导致那群超乎想象的\x01",
            "大型魔兽出现。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x104,
        "#00303F#6P#N嗯，确实有可能。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0441
    ChrTalk(
        0x22,
        (
            "#11P赌上协会之名，\x01",
            "我们一定会查明一切的。\x02",
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

    # Function_66_A6A8 end

    def Function_67_B687(): pass

    label("Function_67_B687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9B2")
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
            "喂喂……\x01",
            "我已经说过很多次了，\x01",
            "现在不能让各位记者通过。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x16,
        (
            "#12P但现在是休息时间啊……\x01",
            "拜托了，你就通融一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x11,
        (
            "#6P是啊，我们只是拍拍照片而已，\x01",
            "绝不会做别的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xD,
        "#6P就是啊，不然我会被前辈……\x02",
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
            "#6P#00012F明知道不可能，\x01",
            "他们却还是行动了啊。\x02\x03",

            "#00003F但他们似乎还没有大胆到\x01",
            "敢于强行突破的程度……\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x109,
        "#6P#10112F这也算是记者的特质吧。\x02",
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x103,
        (
            "#6P#00206F总之……\x01",
            "看来没法从这里通行了。\x02",
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
    Jump("loc_BA18")

    label("loc_B9B2")

    EventBegin(0x1)
    SetChrName("")

    #A0449
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力梯前的大厅被记者们\x01",
            "堵得水泄不通。\x02\x03",

            "看来暂时无法\x01",
            "从这里通行了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 29470, 0, -1200, 270)
    EventEnd(0x4)

    label("loc_BA18")

    Return()

    # Function_67_B687 end

    def Function_68_BA19(): pass

    label("Function_68_BA19")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC34")
    SetChrName("")

    #A0450
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力梯前的卷帘门\x01",
            "紧紧关闭着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0451
    ChrTalk(
        0x101,
        (
            "#00005F说起来，在会议期间，\x01",
            "好像只能使用\x01",
            "最前面的导力梯吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x102,
        (
            "#00100F嗯，好像是出于警备上的考虑，\x01",
            "做出了这样安排。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_END)), "loc_BB7F")

    #C0453
    ChrTalk(
        0x103,
        (
            "#00200F这里似乎和疏散楼梯一样，\x01",
            "也是通过导力网络\x01",
            "进行控制和管理的。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x101,
        (
            "#00003F嗯，好像是这样。\x02\x03",

            "#00000F总之，如果要去其它楼层，\x01",
            "我们就乘坐最前面的导力梯吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC2C")

    label("loc_BB7F")


    #C0455
    ChrTalk(
        0x103,
        (
            "#00200F顺便一说，锁定开关\x01",
            "似乎是通过导力网络\x01",
            "来控制和管理的。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x101,
        (
            "#00003F嗯，不愧是兰花塔的\x01",
            "安保系统啊。\x02\x03",

            "#00000F总之，如果要去其它楼层，\x01",
            "我们就乘坐最前面的导力梯吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC2C")

    SetScenarioFlags(0x1C2, 2)
    Jump("loc_BC83")

    label("loc_BC34")

    SetChrName("")

    #A0457
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力梯前的卷帘门\x01",
            "紧紧关闭着。\x02\x03",

            "在会议期间，\x01",
            "无法使用这部导力梯。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_BC83")

    TalkEnd(0xFF)
    Return()

    # Function_68_BA19 end

    def Function_69_BC87(): pass

    label("Function_69_BC87")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE9B")
    SetChrName("")

    #A0458
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "疏散楼梯前的卷帘门\x01",
            "紧紧关闭着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0459
    ChrTalk(
        0x101,
        "#00001F这边是通往三十三楼吧。\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x102,
        (
            "#00100F嗯，在会议期间，\x01",
            "这里将会完全封锁呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_END)), "loc_BDDE")

    #C0461
    ChrTalk(
        0x103,
        (
            "#00200F这里似乎和导力梯一样，\x01",
            "也是通过导力网络\x01",
            "进行控制的……\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x101,
        (
            "#00003F迪塔先生说过，不存在完美无缺的\x01",
            "安全防护系统……\x02\x03",

            "#00001F得好好考虑一下，\x01",
            "如果真有什么万一，应该如何应对。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE93")

    label("loc_BDDE")


    #C0463
    ChrTalk(
        0x103,
        (
            "#00200F卷帘门的锁定开关\x01",
            "似乎是通过导力网络\x01",
            "进行控制的……\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x101,
        (
            "#00003F迪塔先生说过，不存在完美无缺的\x01",
            "安全防护系统……\x02\x03",

            "#00001F得好好考虑一下，\x01",
            "如果真有什么万一，应该如何应对。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE93")

    SetScenarioFlags(0x1C2, 3)
    Jump("loc_BEF0")

    label("loc_BE9B")

    SetChrName("")

    #A0465
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "疏散楼梯前的卷帘门\x01",
            "紧紧关闭着。\x02\x03",

            "在会议过程中，\x01",
            "下方楼层是禁止通行的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_BEF0")

    TalkEnd(0xFF)
    Return()

    # Function_69_BC87 end

    def Function_70_BEF4(): pass

    label("Function_70_BEF4")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_70_BEF4 end

    SaveToFile()

Try(main)
