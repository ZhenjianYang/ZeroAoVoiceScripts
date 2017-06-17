from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e3400.bin",                # FileName
        "e3400",                    # MapName
        "e3400",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 1250, 22670, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e3400",                  # 0
        "太陽の姫",               # 1
        "月の姫",                 # 2
        "映りこみ太陽",           # 3
        "映りこみ月",             # 4
        "星の守護戦士",           # 5
        "放蕩者の王子",           # 6
        "女祭司長",               # 7
        "女占い師",               # 8
        "漂白民の少年",           # 9
        "ラの侍女",               # 10
        "ラの侍女",               # 11
        "ラの兵士",               # 12
        "ラの兵士",               # 13
        "ラの兵士",               # 14
        "ラの兵士",               # 15
        "映り守護戦士",           # 16
        "オブジェ用",             # 17
        "オブジェ用",             # 18
        "支配人バルサモ",         # 19
        "エマ捜査官",             # 20
        "ダドリー捜査官",         # 21
        "一課捜査官",             # 22
        "一課捜査官",             # 23
        "マクダエル市長",         # 24
        "秘書アーネスト",         # 25
        "セシル",                 # 26
        "SE制御",                 # 27
    ))

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(2380,    15199,   -7010,   360,  261,  0x0, 0,   2,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_5FC",          # 00, 0
        "Function_1_779",          # 01, 1
        "Function_2_77A",          # 02, 2
        "Function_3_871",          # 03, 3
        "Function_4_895",          # 04, 4
        "Function_5_93A",          # 05, 5
        "Function_6_9C4",          # 06, 6
        "Function_7_9F1",          # 07, 7
        "Function_8_A1E",          # 08, 8
        "Function_9_A35",          # 09, 9
        "Function_10_A4C",         # 0A, 10
        "Function_11_A55",         # 0B, 11
        "Function_12_A5E",         # 0C, 12
        "Function_13_A67",         # 0D, 13
        "Function_14_A70",         # 0E, 14
        "Function_15_A9D",         # 0F, 15
        "Function_16_ACA",         # 10, 16
        "Function_17_AE1",         # 11, 17
        "Function_18_AF8",         # 12, 18
        "Function_19_B17",         # 13, 19
        "Function_20_B36",         # 14, 20
        "Function_21_B55",         # 15, 21
        "Function_22_B74",         # 16, 22
        "Function_23_C36",         # 17, 23
        "Function_24_D18",         # 18, 24
        "Function_25_E7D",         # 19, 25
        "Function_26_148E",        # 1A, 26
        "Function_27_18EB",        # 1B, 27
        "Function_28_1936",        # 1C, 28
        "Function_29_19B8",        # 1D, 29
        "Function_30_1A3A",        # 1E, 30
        "Function_31_1A8B",        # 1F, 31
        "Function_32_1ADC",        # 20, 32
        "Function_33_1B2D",        # 21, 33
        "Function_34_1B98",        # 22, 34
        "Function_35_1BE1",        # 23, 35
        "Function_36_1C2A",        # 24, 36
        "Function_37_1C7F",        # 25, 37
        "Function_38_260D",        # 26, 38
        "Function_39_2641",        # 27, 39
        "Function_40_28EA",        # 28, 40
        "Function_41_2AA7",        # 29, 41
        "Function_42_2DBD",        # 2A, 42
        "Function_43_2E08",        # 2B, 43
        "Function_44_2ED8",        # 2C, 44
        "Function_45_30A4",        # 2D, 45
        "Function_46_3355",        # 2E, 46
        "Function_47_338E",        # 2F, 47
        "Function_48_33C7",        # 30, 48
        "Function_49_3B3F",        # 31, 49
        "Function_50_3B76",        # 32, 50
        "Function_51_3C00",        # 33, 51
        "Function_52_3DFB",        # 34, 52
        "Function_53_40B6",        # 35, 53
        "Function_54_41ED",        # 36, 54
        "Function_55_446D",        # 37, 55
        "Function_56_46B6",        # 38, 56
        "Function_57_4967",        # 39, 57
        "Function_58_4A00",        # 3A, 58
        "Function_59_4A99",        # 3B, 59
        "Function_60_4AE4",        # 3C, 60
        "Function_61_5161",        # 3D, 61
        "Function_62_518C",        # 3E, 62
        "Function_63_52EA",        # 3F, 63
        "Function_64_5448",        # 40, 64
        "Function_65_5518",        # 41, 65
        "Function_66_55E8",        # 42, 66
        "Function_67_56B8",        # 43, 67
        "Function_68_5788",        # 44, 68
        "Function_69_57D3",        # 45, 69
        "Function_70_5858",        # 46, 70
        "Function_71_5921",        # 47, 71
        "Function_72_5B81",        # 48, 72
        "Function_73_5DF9",        # 49, 73
        "Function_74_6474",        # 4A, 74
        "Function_75_6833",        # 4B, 75
        "Function_76_685C",        # 4C, 76
        "Function_77_76FC",        # 4D, 77
        "Function_78_7751",        # 4E, 78
        "Function_79_7765",        # 4F, 79
        "Function_80_77B0",        # 50, 80
        "Function_81_78A0",        # 51, 81
        "Function_82_78EB",        # 52, 82
        "Function_83_7B10",        # 53, 83
        "Function_84_7B2A",        # 54, 84
        "Function_85_7D4B",        # 55, 85
        "Function_86_7D65",        # 56, 86
        "Function_87_7D9C",        # 57, 87
        "Function_88_7EC9",        # 58, 88
        "Function_89_7F1C",        # 59, 89
        "Function_90_7F6F",        # 5A, 90
        "Function_91_8010",        # 5B, 91
        "Function_92_802F",        # 5C, 92
        "Function_93_804E",        # 5D, 93
        "Function_94_8128",        # 5E, 94
        "Function_95_8206",        # 5F, 95
        "Function_96_90DF",        # 60, 96
        "Function_97_9189",        # 61, 97
        "Function_98_9380",        # 62, 98
        "Function_99_994B",        # 63, 99
        "Function_100_9ACA",       # 64, 100
        "Function_101_A21B",       # 65, 101
        "Function_102_A27C",       # 66, 102
        "Function_103_A672",       # 67, 103
        "Function_104_A6BF",       # 68, 104
        "Function_105_A702",       # 69, 105
        "Function_106_A774",       # 6A, 106
        "Function_107_A958",       # 6B, 107
        "Function_108_A9CA",       # 6C, 108
        "Function_109_AC82",       # 6D, 109
        "Function_110_ACF4",       # 6E, 110
        "Function_111_AED8",       # 6F, 111
        "Function_112_B238",       # 70, 112
        "Function_113_B5B7",       # 71, 113
        "Function_114_B957",       # 72, 114
        "Function_115_BB51",       # 73, 115
        "Function_116_BD5D",       # 74, 116
        "Function_117_BFE3",       # 75, 117
        "Function_118_C101",       # 76, 118
        "Function_119_C13D",       # 77, 119
        "Function_120_C159",       # 78, 120
        "Function_121_C1CB",       # 79, 121
        "Function_122_D0AF",       # 7A, 122
        "Function_123_D0C9",       # 7B, 123
        "Function_124_D16E",       # 7C, 124
        "Function_125_D217",       # 7D, 125
        "Function_126_DA9D",       # 7E, 126
    ))


    def Function_0_5FC(): pass

    label("Function_0_5FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_610")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 102)
    Jump("loc_778")

    label("loc_610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_624")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 37)
    Jump("loc_778")

    label("loc_624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_638")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 106)
    Jump("loc_778")

    label("loc_638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 4)), scpexpr(EXPR_END)), "loc_64C")
    ClearScenarioFlags(0x5C, 4)
    Event(0, 108)
    Jump("loc_778")

    label("loc_64C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 5)), scpexpr(EXPR_END)), "loc_660")
    ClearScenarioFlags(0x5C, 5)
    Event(0, 110)
    Jump("loc_778")

    label("loc_660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 6)), scpexpr(EXPR_END)), "loc_674")
    ClearScenarioFlags(0x5C, 6)
    Event(0, 111)
    Jump("loc_778")

    label("loc_674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 7)), scpexpr(EXPR_END)), "loc_688")
    ClearScenarioFlags(0x5C, 7)
    Event(0, 112)
    Jump("loc_778")

    label("loc_688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 0)), scpexpr(EXPR_END)), "loc_69C")
    ClearScenarioFlags(0x5D, 0)
    Event(0, 113)
    Jump("loc_778")

    label("loc_69C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 1)), scpexpr(EXPR_END)), "loc_6B0")
    ClearScenarioFlags(0x5D, 1)
    Event(0, 114)
    Jump("loc_778")

    label("loc_6B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 2)), scpexpr(EXPR_END)), "loc_6C4")
    ClearScenarioFlags(0x5D, 2)
    Event(0, 115)
    Jump("loc_778")

    label("loc_6C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 3)), scpexpr(EXPR_END)), "loc_6D8")
    ClearScenarioFlags(0x5D, 3)
    Event(0, 116)
    Jump("loc_778")

    label("loc_6D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 4)), scpexpr(EXPR_END)), "loc_6EC")
    ClearScenarioFlags(0x5D, 4)
    Event(0, 48)
    Jump("loc_778")

    label("loc_6EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 5)), scpexpr(EXPR_END)), "loc_700")
    ClearScenarioFlags(0x5D, 5)
    Event(0, 60)
    Jump("loc_778")

    label("loc_700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 6)), scpexpr(EXPR_END)), "loc_714")
    ClearScenarioFlags(0x5D, 6)
    Event(0, 76)
    Jump("loc_778")

    label("loc_714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 7)), scpexpr(EXPR_END)), "loc_728")
    ClearScenarioFlags(0x5D, 7)
    Event(0, 100)
    Jump("loc_778")

    label("loc_728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E, 0)), scpexpr(EXPR_END)), "loc_73C")
    ClearScenarioFlags(0x5E, 0)
    Event(0, 121)
    Jump("loc_778")

    label("loc_73C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E, 1)), scpexpr(EXPR_END)), "loc_750")
    ClearScenarioFlags(0x5E, 1)
    Event(0, 95)
    Jump("loc_778")

    label("loc_750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E, 2)), scpexpr(EXPR_END)), "loc_764")
    ClearScenarioFlags(0x5E, 2)
    Event(0, 125)
    Jump("loc_778")

    label("loc_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_775")
    Event(0, 3)
    Jump("loc_778")

    label("loc_775")

    Event(0, 2)

    label("loc_778")

    Return()

    # Function_0_5FC end

    def Function_1_779(): pass

    label("Function_1_779")

    Return()

    # Function_1_779 end

    def Function_2_77A(): pass

    label("Function_2_77A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x80)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "一幕\x01",                # 0
            "二幕\x01",                # 1
            "三幕\x01",                # 2
            "四幕\x01",                # 3
            "フィナーレ\x01",          # 4
            "四幕中盤（仮）\x01",      # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7FF"),
        (1, "loc_810"),
        (2, "loc_821"),
        (3, "loc_832"),
        (4, "loc_843"),
        (5, "loc_854"),
        (SWITCH_DEFAULT, "loc_865"),
    )


    label("loc_7FF")

    SetScenarioFlags(0x5C, 2)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_865")

    label("loc_810")

    SetScenarioFlags(0x5D, 4)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_865")

    label("loc_821")

    SetScenarioFlags(0x5D, 5)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_865")

    label("loc_832")

    SetScenarioFlags(0x5D, 6)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_865")

    label("loc_843")

    SetScenarioFlags(0x5E, 1)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_865")

    label("loc_854")

    SetScenarioFlags(0x5D, 7)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_865")

    label("loc_865")

    FadeToDark(300, 0, -1)
    OP_0D()
    Return()

    # Function_2_77A end

    def Function_3_871(): pass

    label("Function_3_871")

    Call(0, 37)
    Call(0, 48)
    Call(0, 60)
    Call(0, 76)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    Call(0, 100)
    Return()

    # Function_3_871 end

    def Function_4_895(): pass

    label("Function_4_895")

    ClearChrFlags(0xFE, 0x1)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    OP_A7(0xFE, 0x0, 0x0, 0x0, 0x80, 0x0)
    OP_D3(0xFE, 0x41EB0, 0x4CE78, 0x0, 0x0)

    label("loc_8C7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_939")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_8C7")

    label("loc_939")

    Return()

    # Function_4_895 end

    def Function_5_93A(): pass

    label("Function_5_93A")

    ClearChrFlags(0xFE, 0x1)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    OP_A7(0xFE, 0x0, 0x0, 0x0, 0x80, 0x0)
    OP_D3(0xFE, 0x41EB0, 0x57E40, 0x0, 0x0)

    label("loc_96C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9C3")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IDIV), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_96C")

    label("loc_9C3")

    Return()

    # Function_5_93A end

    def Function_6_9C4(): pass

    label("Function_6_9C4")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_6_9C4 end

    def Function_7_9F1(): pass

    label("Function_7_9F1")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Sleep(33)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_7_9F1 end

    def Function_8_A1E(): pass

    label("Function_8_A1E")

    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_8_A1E end

    def Function_9_A35(): pass

    label("Function_9_A35")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(33)
    SetChrSubChip(0xFE, 0x1)
    Sleep(33)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_9_A35 end

    def Function_10_A4C(): pass

    label("Function_10_A4C")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_10_A4C end

    def Function_11_A55(): pass

    label("Function_11_A55")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_11_A55 end

    def Function_12_A5E(): pass

    label("Function_12_A5E")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_12_A5E end

    def Function_13_A67(): pass

    label("Function_13_A67")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_13_A67 end

    def Function_14_A70(): pass

    label("Function_14_A70")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_14_A70 end

    def Function_15_A9D(): pass

    label("Function_15_A9D")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    Sleep(33)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_15_A9D end

    def Function_16_ACA(): pass

    label("Function_16_ACA")

    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_ACA end

    def Function_17_AE1(): pass

    label("Function_17_AE1")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    Sleep(33)
    SetChrSubChip(0xFE, 0x1)
    Sleep(33)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_17_AE1 end

    def Function_18_AF8(): pass

    label("Function_18_AF8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B16")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_18_AF8")

    label("loc_B16")

    Return()

    # Function_18_AF8 end

    def Function_19_B17(): pass

    label("Function_19_B17")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B35")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(66)
    Jump("Function_19_B17")

    label("loc_B35")

    Return()

    # Function_19_B17 end

    def Function_20_B36(): pass

    label("Function_20_B36")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B54")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_20_B36")

    label("loc_B54")

    Return()

    # Function_20_B36 end

    def Function_21_B55(): pass

    label("Function_21_B55")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B73")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(66)
    Jump("Function_21_B55")

    label("loc_B73")

    Return()

    # Function_21_B55 end

    def Function_22_B74(): pass

    label("Function_22_B74")

    FadeToBright(500, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 0, 1300, 25500, 0, 0, 0, 1100, 1200, 1100, 0xFF, 0, 0, 0, 0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrPos(0x8, -3000, 1250, 26000, 90)
    OP_96(0x8, 0xFFFFF704, 0x4E2, 0x6590, 0x1770, 0x0)
    BeginChrThread(0x8, 1, 0, 27)
    BeginChrThread(0x8, 2, 0, 6)
    FadeToDark(1500, 0, -1)
    OP_9D(0x8, 0x8FC, 0x4E2, 0x6590, 0x5DC, 0x2BC)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 8)
    OP_96(0x8, 0x1388, 0x4E2, 0x6590, 0x1770, 0x0)
    Return()

    # Function_22_B74 end

    def Function_23_C36(): pass

    label("Function_23_C36")

    Fade(500)
    FadeToBright(0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 0, 1300, 25500, 0, 0, 0, 1100, 1200, 1100, 0xFF, 0, 0, 0, 0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetMapFlags(0x10)
    OP_11(0x0, 0x0, 0x0, 0xF, 0x11, 0x0)
    SetChrPos(0x8, 3000, 1250, 26000, 270)
    OP_96(0x8, 0x8FC, 0x4E2, 0x6590, 0x1770, 0x0)
    BeginChrThread(0x8, 1, 0, 27)
    BeginChrThread(0x8, 2, 0, 6)
    BeginChrThread(0x8, 3, 0, 18)
    FadeToDark(2000, 0, -1)
    OP_9D(0x8, 0xFFFFF704, 0x4E2, 0x6590, 0x5DC, 0x2BC)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 8)
    OP_96(0x8, 0xFFFFEC78, 0x4E2, 0x6590, 0x1770, 0x0)
    Return()

    # Function_23_C36 end

    def Function_24_D18(): pass

    label("Function_24_D18")

    BeginChrThread(0xA, 3, 0, 4)
    OP_68(-20, 2900, 25450, 0)
    MoveCamera(1, 17, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(18000, 0)
    FadeToBright(1500, 0)
    PlayEffect(0x1, 0xFF, 0x8, 0x40, 0, 100, 0, 0, 0, 0, 1100, 1200, 1100, 0xFF, 0, 0, 0, 0)
    OP_11(0x0, 0x0, 0x0, 0x11, 0x1E, 0x5DC)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0xFA0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x1388, 0xDAC)
    OP_C9(0x0, 0x1, 0x3E8, 0x44C, 0xDAC)
    BeginChrThread(0x8, 1, 0, 27)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    SetChrPos(0x8, 3000, 1250, 26000, 270)
    OP_9E(0x8, 0x0, 0x636A, 0x2BF20, 0x1770, 0x0)
    OP_9E(0x8, 0xFFFFFA24, 0x636A, 0x15F90, 0x1388, 0x0)
    BeginChrThread(0x8, 3, 0, 19)
    OP_9E(0x8, 0xFFFFFA24, 0x636A, 0xAFC8, 0xBB8, 0x0)
    OP_9E(0x8, 0xFFFFFA24, 0x636A, 0xAFC8, 0x5DC, 0x0)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x8, 0x2)
    Sleep(1000)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)
    EndChrThread(0x8, 0x3)
    OP_93(0x8, 0x87, 0x12C)
    Return()

    # Function_24_D18 end

    def Function_25_E7D(): pass

    label("Function_25_E7D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_148D")
    SetChrFlags(0x8, 0x4)
    BeginChrThread(0x8, 1, 0, 27)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    BeginChrThread(0x101, 1, 0, 28)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xC8, 0xC8, 0xC8, 0x0, 0x3E8)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 15000, 25500, 0, 180, 0, 830, 1500, 830, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1200, 25600, 0, 0, 0, 510, 1000, 510, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1300, 25600, 180, 0, 0, 570, 700, 570, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)
    OP_9D(0x8, 0xA, 0x4E2, 0x636A, 0xFA0, 0x3E8)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    BeginChrThread(0x8, 2, 0, 9)
    Sleep(50)
    BeginChrThread(0x8, 3, 0, 19)

    def lambda_FB7():
        OP_9E(0x8, 0x0, 0x5DC0, 0x927C0, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_FB7)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_FF9():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_FF9)
    Sleep(33)
    BeginChrThread(0x8, 1, 0, 27)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x8, 0x0)

    def lambda_1038():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1038)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_104E():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_104E)
    Sleep(33)
    BeginChrThread(0x8, 1, 0, 27)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x8, 0x0)

    def lambda_108D():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_108D)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_10C9():
        OP_9E(0x8, 0x0, 0x636A, 0xFFFA81C0, 0x2134, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_10C9)
    Sleep(33)
    BeginChrThread(0x8, 1, 0, 27)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x320)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x8, 0x0)

    def lambda_1132():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1132)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0x0, 0x4E2, 0x639C, 0x7D0, 0x7D0)
    BeginChrThread(0x8, 3, 0, 18)
    BeginChrThread(0x8, 2, 0, 9)
    OP_9D(0x8, 0x0, 0x4E2, 0x639C, 0xBB8, 0x9C4)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 1, 0, 27)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xC8, 0xC8, 0xC8, 0x0, 0x3E8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1200, 25600, 0, 0, 0, 510, 1000, 510, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1300, 25600, 180, 0, 0, 570, 700, 570, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)
    OP_9D(0x8, 0xA, 0x4E2, 0x636A, 0xFA0, 0x3E8)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    BeginChrThread(0x8, 2, 0, 9)
    Sleep(50)
    BeginChrThread(0x8, 3, 0, 19)

    def lambda_126B():
        OP_9E(0x8, 0x0, 0x5DC0, 0x927C0, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_126B)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_12AD():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_12AD)
    Sleep(33)
    BeginChrThread(0x8, 1, 0, 27)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x8, 0x0)

    def lambda_12EC():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_12EC)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_1302():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1302)
    Sleep(33)
    BeginChrThread(0x8, 1, 0, 27)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x8, 0x0)

    def lambda_1341():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1341)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_137D():
        OP_9E(0x8, 0x0, 0x636A, 0xFFFA81C0, 0x2134, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_137D)
    Sleep(33)
    BeginChrThread(0x8, 1, 0, 27)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x320)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x8, 0x0)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9D(0x8, 0x0, 0x4E2, 0x639C, 0x7D0, 0x7D0)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x101, 0x1)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xC8, 0xC8, 0xC8, 0x0, 0x3E8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1200, 25600, 0, 0, 0, 510, 1000, 510, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sleep(10000)
    Jump("Function_25_E7D")

    label("loc_148D")

    Return()

    # Function_25_E7D end

    def Function_26_148E(): pass

    label("Function_26_148E")

    BeginChrThread(0x101, 1, 0, 29)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xC8, 0xC8, 0xC8, 0x0, 0x3E8)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4430, 3300, 19500, 0, 90, 0, 300, 600, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4430, 3300, 19500, 0, 90, 0, 300, 600, 300, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1300, 25600, 180, 0, 0, 570, 700, 570, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)
    SetChrPos(0x8, 0, 1250, 25450, 140)
    BeginChrThread(0x8, 1, 0, 27)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9E(0x8, 0x0, 0x5FB4, 0x2BF20, 0xD48, 0x0)
    OP_9E(0x8, 0x0, 0x61A8, 0x2BF20, 0xD48, 0x0)
    OP_9E(0x8, 0x0, 0x5DC0, 0x2BF20, 0xD48, 0x0)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    Sleep(800)

    def lambda_15ED():
        OP_93(0x8, 0x12C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_15ED)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x1F)
    BeginChrThread(0x8, 1, 0, 27)

    def lambda_160E():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_160E)
    Sleep(520)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x9C4, 0x960)

    def lambda_1659():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1659)
    EndChrThread(0x8, 0x3)
    SetChrChipByIndex(0x8, 0x1F)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    Sleep(520)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x2)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x9C4, 0x960)

    def lambda_16B8():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_16B8)
    SetChrChipByIndex(0x8, 0x1F)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    Sleep(520)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x2)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x9C4, 0x960)
    EndChrThread(0x8, 0x3)

    def lambda_171D():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_171D)
    SetChrChipByIndex(0x8, 0x1F)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    Sleep(500)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x8, 0x1)
    Sleep(900)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 1, 0, 27)
    BeginChrThread(0x8, 3, 0, 19)
    OP_9E(0x8, 0x0, 0x5DC0, 0x2BF20, 0x1194, 0x0)
    OP_9E(0x8, 0x0, 0x61A8, 0x2BF20, 0x1194, 0x0)
    OP_9E(0x8, 0x0, 0x5FB4, 0x2BF20, 0x1194, 0x0)
    BeginChrThread(0x8, 3, 0, 18)
    Sleep(2550)

    def lambda_17C0():
        OP_93(0xFE, 0x73, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_17C0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xC8, 0xC8, 0xC8, 0x0, 0x3E8)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4430, 3300, 19500, 0, 90, 0, 300, 600, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4430, 3300, 19500, 0, 90, 0, 300, 600, 300, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1200, 25600, 0, 0, 0, 510, 1000, 510, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1300, 25600, 180, 0, 0, 570, 700, 570, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)
    EndChrThread(0x8, 0x1)
    Return()

    # Function_26_148E end

    def Function_27_18EB(): pass

    label("Function_27_18EB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1935")
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_27_18EB")

    label("loc_1935")

    Return()

    # Function_27_18EB end

    def Function_28_1936(): pass

    label("Function_28_1936")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19B7")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4230, 3300, 19500, 0, 90, 0, 300, 600, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4430, 3300, 19500, 0, 90, 0, 300, 600, 300, 0xFF, 0, 0, 0, 0)
    Sleep(1951)
    Jump("Function_28_1936")

    label("loc_19B7")

    Return()

    # Function_28_1936 end

    def Function_29_19B8(): pass

    label("Function_29_19B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A39")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4230, 3300, 19500, 0, 90, 0, 300, 600, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4430, 3300, 19500, 0, 90, 0, 300, 600, 300, 0xFF, 0, 0, 0, 0)
    Sleep(833)
    Jump("Function_29_19B8")

    label("loc_1A39")

    Return()

    # Function_29_19B8 end

    def Function_30_1A3A(): pass

    label("Function_30_1A3A")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)

    label("loc_1A44")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A8A")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_1A44")

    label("loc_1A8A")

    Return()

    # Function_30_1A3A end

    def Function_31_1A8B(): pass

    label("Function_31_1A8B")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)

    label("loc_1A95")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1ADB")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_1A95")

    label("loc_1ADB")

    Return()

    # Function_31_1A8B end

    def Function_32_1ADC(): pass

    label("Function_32_1ADC")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)

    label("loc_1AE6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B2C")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x2), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_1AE6")

    label("loc_1B2C")

    Return()

    # Function_32_1ADC end

    def Function_33_1B2D(): pass

    label("Function_33_1B2D")

    OP_70(0x0, 0x1E)
    OP_71(0x0, 0x1, 0x3C, 0x0, 0x8)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    Sleep(1000)
    OP_95(0xFE, 0, 2430, 30920, 1000, 0x0)
    BeginChrThread(0xE, 0, 0, 34)
    BeginChrThread(0x11, 0, 0, 35)
    BeginChrThread(0x12, 0, 0, 36)
    OP_95(0xFE, 0, 1520, 29550, 1000, 0x0)

    def lambda_1B8A():

        label("loc_1B8A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1B8A")

    QueueWorkItem2(0xFE, 2, lambda_1B8A)
    Return()

    # Function_33_1B2D end

    def Function_34_1B98(): pass

    label("Function_34_1B98")

    Sleep(1000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_95(0xFE, 0, 2430, 30920, 1000, 0x0)
    OP_95(0xFE, 800, 1910, 30140, 1000, 0x0)

    def lambda_1BD3():

        label("loc_1BD3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1BD3")

    QueueWorkItem2(0xFE, 2, lambda_1BD3)
    Return()

    # Function_34_1B98 end

    def Function_35_1BE1(): pass

    label("Function_35_1BE1")

    Sleep(3000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_95(0xFE, 0, 2430, 30920, 1000, 0x0)
    OP_95(0xFE, -970, 2200, 30570, 1000, 0x0)

    def lambda_1C1C():

        label("loc_1C1C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1C1C")

    QueueWorkItem2(0xFE, 2, lambda_1C1C)
    Return()

    # Function_35_1BE1 end

    def Function_36_1C2A(): pass

    label("Function_36_1C2A")

    Sleep(4000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_95(0xFE, 0, 2430, 30920, 1000, 0x0)
    OP_95(0xFE, -180, 2190, 30560, 1000, 0x0)

    def lambda_1C65():

        label("loc_1C65")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1C65")

    QueueWorkItem2(0xFE, 2, lambda_1C65)
    OP_71(0x0, 0x3C, 0x0, 0x0, 0x8)
    Return()

    # Function_36_1C2A end

    def Function_37_1C7F(): pass

    label("Function_37_1C7F")

    OP_F8(0x14D)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x101, 10, 1250, 30450, 140)
    LoadChrToIndex("apl/ch50250.itc", 0x1E)
    LoadChrToIndex("apl/ch50251.itc", 0x1F)
    LoadChrToIndex("apl/ch50252.itc", 0x20)
    LoadChrToIndex("apl/ch50253.itc", 0x21)
    LoadChrToIndex("apl/ch50254.itc", 0x22)
    LoadChrToIndex("chr/ch36700.itc", 0x34)
    LoadChrToIndex("chr/ch36900.itc", 0x36)
    LoadChrToIndex("chr/ch37200.itc", 0x3A)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x34)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x36)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x3A)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x3A)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0xC, 0, 2590, 31870, 180)
    SetChrPos(0xE, 0, 2590, 31870, 180)
    SetChrPos(0x11, 0, 2590, 31870, 180)
    SetChrPos(0x12, 0, 2590, 31870, 180)
    OP_A7(0xC, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_A7(0xE, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_A7(0x11, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_A7(0x12, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrPos(0x8, 10, 1250, 25450, 140)
    ClearChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x21)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x100)
    SetChrFlags(0xA, 0x800)
    SetChrPos(0xA, 10, 1250, 25450, 230)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x80, 0x0)
    OP_D3(0xA, 0x2BF20, 0x0, 0x0, 0x0)
    BeginChrThread(0xA, 3, 0, 5)
    OP_68(-20, 2900, 25450, 0)
    MoveCamera(1, 15, 0, 0)
    OP_6E(1140, 0)
    SetCameraDistance(26500, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    LoadEffect(0x2, "event\\ev290_01.eff")
    LoadEffect(0x6, "event\\ev290_02.eff")
    LoadEffect(0x1, "event\\ev290_03.eff")
    LoadEffect(0x3, "event\\ev290_00.eff")
    LoadEffect(0x5, "event\\ev293_02.eff")
    LoadEffect(0x0, "event\\ev290_05.eff")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    OP_7D(0x80, 0x80, 0x80, 0x0, 0x0)
    SoundLoad(872)
    SoundLoad(873)
    SoundLoad(874)
    BeginChrThread(0x22, 0, 0, 103)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Sound(871, 0, 100, 0)
    Sleep(3000)
    EndChrThread(0x22, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性の声")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "──皆様、お待たせしました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "これより、劇団アルカンシェルの新作\x01",
            "『金の太陽、銀の月』の\x01",
            "プレ公演の幕を上げさせて頂きます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "最後までごゆっくりお楽しみください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    BeginChrThread(0x22, 0, 0, 104)
    Sound(870, 0, 100, 0)
    OP_7D(0x0, 0x0, 0x0, 0x0, 0x7D0)
    Sleep(5000)
    OP_68(-20, 2900, 25450, 0)
    MoveCamera(1, 20, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(14500, 0)
    SetMapObjFlags(0x5, 0x4)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("男性の声")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──ここは『ラの国』。\x01",
            "天の女神の祝福と慈愛により\x01",
            "大いなる繁栄を誇った古の王国。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "古来より『ラ』では\x01",
            "『姫』と呼ばれる舞い手によって\x01",
            " 政#2Rまつりごと#が決定されてきた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『姫』は女神の意志を宿し、\x01",
            "星の祭殿において競い合うことで\x01",
            "その政の正しさを世に知らしめる……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "しかしそこには様々な思惑も絡み、\x01",
            "有力者たちは競うようにして\x01",
            "それぞれの『姫』を擁立するのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──そんな中。\x01",
            "《太陽の姫》と謳われる当代一の\x01",
            "舞い手の姿が、星の祭殿にあった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EndChrThread(0x22, 0x0)
    OP_E5()
    SetMapFlags(0x10)
    OP_11(0x0, 0x0, 0x0, 0xF, 0x11, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFFE2B40, 0xFFFB6C20, 0x0)
    OP_C9(0x0, 0x1, 0x5DC, 0xAF0, 0x0)
    Sleep(1000)
    PlayBGM("ed7500", 1)
    Sleep(4000)
    Sleep(450)
    BeginChrThread(0x101, 0, 0, 22)
    Sleep(550)
    Sleep(5000)
    BeginChrThread(0x101, 0, 0, 23)
    Sleep(150)
    Sleep(850)
    Sleep(4000)
    Sleep(1000)
    Sleep(200)
    Fade(100)
    BeginChrThread(0x101, 0, 0, 24)
    Sleep(800)
    Sleep(1000)
    Sleep(1000)
    Sleep(1000)
    Sleep(4000)
    Sleep(300)
    Fade(150)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x1)
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    FadeToBright(500, 0)
    OP_7D(0xFF, 0xFF, 0xC8, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFA2400, 0x1F4)
    OP_C9(0x0, 0x1, 0xBB8, 0xFA0, 0x1F4)
    OP_11(0x0, 0x0, 0x0, 0x1E, 0x64, 0x1388)
    Sleep(150)
    BeginChrThread(0x101, 3, 0, 25)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 15, 0, 0, 1100, 1200, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 1000, 15000, 15, 0, 0, 1100, 1200, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(130, 3700, 25170, 10000)
    MoveCamera(1, 7, 0, 30000)
    OP_6E(760, 10000)
    SetCameraDistance(16000, 20000)
    BeginChrThread(0x22, 1, 0, 38)
    Sleep(350)
    Sleep(5000)
    Sleep(10000)
    Sleep(10000)
    Sleep(6000)
    BeginChrThread(0x101, 3, 0, 26)
    BeginChrThread(0xC, 0, 0, 33)
    OP_68(-50, 2900, 25220, 10000)
    MoveCamera(1, 18, 0, 10000)
    OP_6E(760, 10000)
    SetCameraDistance(16000, 10000)
    Sleep(4000)
    Sleep(10000)
    Sleep(3000)
    FadeToDark(3000, 0, -1)
    Sleep(100)

    def lambda_24E9():
        OP_96(0xFE, 0xE6, 0x4E2, 0x6978, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_24E9)
    Sleep(500)

    def lambda_2506():
        OP_96(0xFE, 0x528, 0x4E2, 0x6540, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_2506)
    Sleep(400)

    def lambda_2523():
        OP_96(0xFE, 0xE6, 0x4E2, 0x6978, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2523)
    Sleep(500)

    def lambda_2540():
        OP_96(0xFE, 0xE6, 0x4E2, 0x6978, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_2540)
    OP_0D()
    StopBGM(0x1388)
    WaitChrThread(0x22, 1)
    WaitBGM()
    OP_E6()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_25EE")
    EndChrThread(0x101, 0xFF)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x4)
    EndChrThread(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x1000)
    SetChrFlags(0xA, 0x1)
    SetChrFlags(0xA, 0x4)
    EndChrThread(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    EndChrThread(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    EndChrThread(0xE, 0xFF)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    EndChrThread(0x11, 0xFF)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    EndChrThread(0x12, 0xFF)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    OP_24(0x369)
    Return()

    label("loc_25EE")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x211), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    VolumeBGM(0x32, 0x64)
    OP_24(0x369)
    SetScenarioFlags(0x5C, 3)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_1C7F end

    def Function_38_260D(): pass

    label("Function_38_260D")

    Sleep(700)
    Sound(873, 2, 100, 0)
    Sound(872, 0, 100, 0)
    Sleep(15500)
    Sound(874, 0, 100, 0)
    Sleep(5000)
    Sleep(10000)
    Sound(872, 0, 100, 0)
    Sleep(18000)
    OP_24(0x369)
    Sound(872, 0, 100, 0)
    Sleep(2000)
    Return()

    # Function_38_260D end

    def Function_39_2641(): pass

    label("Function_39_2641")

    OP_68(10, 2900, 23030, 10000)
    MoveCamera(0, 19, 0, 10000)
    OP_6E(570, 10000)
    SetCameraDistance(19500, 10000)
    SetChrPos(0x9, 0, 9500, 23220, 270)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 21)
    OP_A7(0x9, 0x0, 0x0, 0x0, 0xFF, 0x0)

    def lambda_269C():
        OP_96(0x9, 0x0, 0x4E2, 0x5AB4, 0x44C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_269C)
    Sleep(3000)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0xBB8)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0xBB8)
    OP_7D(0x8C, 0x8C, 0xFF, 0x0, 0xBB8)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
    WaitChrThread(0x9, 0)
    BeginChrThread(0x9, 1, 0, 43)
    Sleep(1500)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1F)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    OP_95(0x9, -2110, 1250, 20950, 4500, 0x0)
    BeginChrThread(0x9, 2, 0, 7)

    def lambda_2724():
        OP_9E(0x9, 0x0, 0x5AB4, 0xFFFEA070, 0x898, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2724)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    Sleep(1)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x578, 0x2BC)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1E)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    Sleep(700)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x7D0, 0x2BC)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1F)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)

    def lambda_27AD():
        OP_93(0x9, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_27AD)
    BeginChrThread(0x9, 2, 0, 7)
    OP_9D(0x9, 0xFFFFF9FC, 0x4E2, 0x5E38, 0xBB8, 0x4B0)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x1)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1E)
    BeginChrThread(0x9, 2, 0, 7)

    def lambda_27ED():
        OP_93(0x9, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_27ED)
    OP_9D(0x9, 0xFFFFF3C6, 0x4E2, 0x62F2, 0x3E8, 0x6A4)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x2)
    Sleep(1500)

    def lambda_281C():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_281C)
    BeginChrThread(0x9, 2, 0, 7)
    OP_9D(0x9, 0xFFFFFA74, 0x4E2, 0x6496, 0x7D0, 0xA28)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0x58C, 0x4E2, 0x6496, 0x7D0, 0xA28)
    BeginChrThread(0x9, 2, 0, 10)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xF28, 0x4E2, 0x6496, 0x7D0, 0xA28)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x2)
    Sleep(500)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    OP_9E(0x9, 0xF28, 0x55F0, 0xFFFEA070, 0xBB8, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x2)
    BeginChrThread(0x9, 3, 0, 21)
    Sleep(700)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)
    Sleep(1800)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x1)
    Return()

    # Function_39_2641 end

    def Function_40_28EA(): pass

    label("Function_40_28EA")

    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 21)
    OP_96(0x9, 0xFFFFECF0, 0x4E2, 0x5BC2, 0x5DC, 0x0)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)

    def lambda_2917():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2917)
    Sleep(1000)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x1F)
    OP_95(0x9, -2300, 1250, 23490, 4000, 0x0)
    BeginChrThread(0x9, 2, 0, 7)

    def lambda_294F():
        OP_9D(0x9, 0x974, 0x4E2, 0x5BC2, 0xDAC, 0x44C)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_294F)
    Sleep(1000)
    BeginChrThread(0x9, 3, 0, 20)
    WaitChrThread(0x9, 0)

    def lambda_2979():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2979)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 2, 0, 10)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0x1310, 0x4E2, 0x5BCC, 0x5DC, 0x7D0)
    EndChrThread(0x9, 0x3)
    OP_93(0x9, 0x5A, 0x0)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x2)
    Sleep(500)

    def lambda_29C9():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_29C9)
    Sleep(800)
    SetChrChipByIndex(0x9, 0x1F)
    OP_95(0x9, 1420, 1250, 23490, 4500, 0x0)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)

    def lambda_2A07():
        OP_9D(0x9, 0xFFFFF894, 0x4E2, 0x5BC2, 0x7D0, 0xB54)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2A07)
    WaitChrThread(0x9, 0)
    BeginChrThread(0x9, 2, 0, 46)

    def lambda_2A2E():
        OP_9D(0x9, 0xFFFFECF0, 0x4E2, 0x5BC2, 0xDAC, 0x2BC)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2A2E)
    Sleep(1000)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)
    WaitChrThread(0x9, 0)

    def lambda_2A5E():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2A5E)
    Sleep(800)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 21)
    OP_9E(0x9, 0xFFFFF0D8, 0x4C2C, 0x15F90, 0x7D0, 0x0)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x1)

    def lambda_2A97():
        OP_93(0x9, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2A97)
    Sleep(1500)
    SetChrSubChip(0x9, 0x0)
    Return()

    # Function_40_28EA end

    def Function_41_2AA7(): pass

    label("Function_41_2AA7")

    OP_68(10, 3500, 23030, 10000)
    MoveCamera(0, 7, 0, 10000)
    OP_6E(580, 10000)
    SetCameraDistance(19500, 10000)

    def lambda_2ADA():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2ADA)
    BeginChrThread(0x9, 2, 0, 7)
    OP_9D(0x9, 0xA, 0x4E2, 0x48E4, 0x7D0, 0xBB8)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xFFFFFA24, 0x4E2, 0x4E84, 0x7D0, 0xBB8)
    BeginChrThread(0x9, 2, 0, 11)
    BeginChrThread(0x9, 3, 0, 18)
    OP_9D(0x9, 0x5DC, 0x4E2, 0x50BE, 0x7D0, 0xBB8)

    def lambda_2B4A():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2B4A)
    BeginChrThread(0x9, 2, 0, 7)
    OP_9D(0x9, 0xFFFFFA24, 0x4E2, 0x587A, 0xDAC, 0x640)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0x5DC, 0x4E2, 0x5DE8, 0x7D0, 0xC1C)
    BeginChrThread(0x9, 2, 0, 7)
    OP_9D(0x9, 0xFFFFFA24, 0x4E2, 0x6446, 0x7D0, 0xC1C)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0x5DC, 0x4E2, 0x5DE8, 0x7D0, 0xC80)

    def lambda_2BD7():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2BD7)
    BeginChrThread(0x9, 2, 0, 11)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xFFFFFA24, 0x4E2, 0x587A, 0x7D0, 0xC80)
    EndChrThread(0x9, 0x3)
    BeginChrThread(0x9, 2, 0, 7)
    OP_9D(0x9, 0x5DC, 0x4E2, 0x50BE, 0xDAC, 0x514)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xFFFFFA24, 0x4E2, 0x4E84, 0x7D0, 0xC80)

    def lambda_2C4B():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2C4B)
    BeginChrThread(0x9, 2, 0, 10)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xA, 0x4E2, 0x48E4, 0x7D0, 0xC80)
    EndChrThread(0x9, 0x3)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x2)
    Sleep(733)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x1F)
    OP_95(0x9, 10, 1250, 23320, 1600, 0x0)
    OP_68(40, 7920, 29870, 2000)
    MoveCamera(0, -12, 0, 2000)
    OP_6E(800, 3000)
    SetCameraDistance(13500, 3000)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 2, 0, 7)

    def lambda_2CEE():
        OP_9D(0x9, 0x1E, 0x187E, 0x753A, 0x1D4C, 0x258)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2CEE)
    Sleep(1000)

    def lambda_2D0E():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2D0E)
    OP_A7(0x9, 0x50, 0x50, 0x50, 0xFF, 0x12C)
    WaitChrThread(0x9, 0)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x2)
    Sleep(1700)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)

    def lambda_2D45():
        OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2D45)
    OP_68(100, 4000, 25480, 8000)
    MoveCamera(0, 7, 0, 8000)
    OP_6E(780, 8000)
    SetCameraDistance(19000, 8000)
    BeginChrThread(0x9, 0, 0, 42)
    OP_9F(0x0, 0x9)
    OP_9F(0x1, -3580, 6000, 21170)
    OP_9F(0x1, 3580, 6000, 21170)
    OP_9F(0x1, 100, 3500, 25480)
    OP_9F(0x2, 0x9, 1700, 0x0)
    Return()

    # Function_41_2AA7 end

    def Function_42_2DBD(): pass

    label("Function_42_2DBD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E07")
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, -300, 0, 0, 180, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_42_2DBD")

    label("loc_2E07")

    Return()

    # Function_42_2DBD end

    def Function_43_2E08(): pass

    label("Function_43_2E08")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2ED7")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2EB4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2EB4")
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    label("loc_2EB4")

    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_43_2E08")

    label("loc_2ED7")

    Return()

    # Function_43_2E08 end

    def Function_44_2ED8(): pass

    label("Function_44_2ED8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30A3")
    Sleep(2166)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 5920, 1700, 21450, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 6690, 1700, 27650, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, -5920, 1700, 21450, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, -6690, 1700, 27650, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 5920, 1000, 21450, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 6690, 1000, 27650, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -5920, 1000, 21450, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -6690, 1000, 27650, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    Jump("Function_44_2ED8")

    label("loc_30A3")

    Return()

    # Function_44_2ED8 end

    def Function_45_30A4(): pass

    label("Function_45_30A4")

    Sleep(530)

    label("loc_30A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3354")
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 5920, 1700, 21450, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -5920, 1700, 21450, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 5920, 1000, 21450, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -5920, 1000, 21450, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    Sleep(722)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 6690, 1700, 27650, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -6690, 1700, 27650, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 6690, 1000, 27650, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -6690, 1000, 27650, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    Sleep(722)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 6690, 1700, 27650, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -6690, 1700, 27650, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 6690, 1000, 27650, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -6690, 1000, 27650, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    Sleep(722)
    Jump("loc_30A7")

    label("loc_3354")

    Return()

    # Function_45_30A4 end

    def Function_46_3355(): pass

    label("Function_46_3355")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_D3(0xFE, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x100)
    OP_D3(0xFE, 0x0, 0x0, 0x57E40, 0x3E8)
    SetChrFlags(0xFE, 0x100)
    Return()

    # Function_46_3355 end

    def Function_47_338E(): pass

    label("Function_47_338E")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    OP_D3(0xFE, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x100)
    OP_D3(0xFE, 0x0, 0x0, 0xFFFA81C0, 0x3E8)
    SetChrFlags(0xFE, 0x100)
    Return()

    # Function_47_338E end

    def Function_48_33C7(): pass

    label("Function_48_33C7")

    OP_F8(0x14D)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "yuka", 0x0, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    LoadChrToIndex("apl/ch50265.itc", 0x1E)
    LoadChrToIndex("apl/ch50266.itc", 0x1F)
    LoadChrToIndex("apl/ch50267.itc", 0x20)
    LoadChrToIndex("apl/ch50268.itc", 0x21)
    LoadChrToIndex("apl/ch50269.itc", 0x22)
    LoadChrToIndex("apl/ch50270.itc", 0x23)
    LoadChrToIndex("chr/ch36600.itc", 0x35)
    LoadChrToIndex("chr/ch37000.itc", 0x37)
    LoadChrToIndex("chr/ch37100.itc", 0x39)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x35)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x37)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x39)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x39)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x39)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x39)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrPos(0xD, 0, 2200, 29540, 180)
    SetChrPos(0xF, 1100, 1800, 28360, 180)
    SetChrPos(0x13, -2170, 1800, 30000, 180)
    SetChrPos(0x14, 2170, 1800, 30000, 180)
    SetChrPos(0x15, -6200, 1250, 24300, 135)
    SetChrPos(0x16, 6200, 1250, 24300, 225)
    OP_A7(0xD, 0xA0, 0xA0, 0xA0, 0xFF, 0x0)
    OP_A7(0xF, 0xA0, 0xA0, 0xA0, 0xFF, 0x0)
    OP_A7(0x13, 0xA0, 0xA0, 0xA0, 0xFF, 0x0)
    OP_A7(0x14, 0xA0, 0xA0, 0xA0, 0xFF, 0x0)
    OP_A7(0x15, 0xA0, 0xA0, 0xA0, 0xFF, 0x0)
    OP_A7(0x16, 0xA0, 0xA0, 0xA0, 0xFF, 0x0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 10, 1250, 25450, 360)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x100)
    SetChrPos(0xB, 10, 1250, 25450, 230)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_D3(0xB, 0x2BF20, 0x0, 0x0, 0x0)
    BeginChrThread(0xB, 3, 0, 30)
    OP_68(10, 3200, 25450, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(1020, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 10, 1250, 25450, 360)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    OP_7D(0x0, 0x0, 0x0, 0x0, 0x0)
    SoundLoad(872)
    SoundLoad(873)
    SoundLoad(875)
    Sound(877, 0, 100, 0)
    Sleep(4000)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性の声")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "こうして《陽の一族》が擁立する\x01",
            "《太陽の姫》に対抗すべく……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "新たなる姫が名乗りを上げたのです。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "その姫の名は《月の姫》……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "『ラ』の国の勢力を二分する、\x01",
            "《夜の一族》の擁立した舞い手でした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_E5()
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0xBB8)
    OP_68(-80, 7300, 29380, 0)
    MoveCamera(0, -10, 0, 0)
    OP_6E(960, 0)
    SetCameraDistance(13000, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFFFF, 0x1, "cv_eff01.itp")
    OP_7D(0x80, 0x80, 0xFF, 0x0, 0x1F4)
    OP_A7(0x9, 0x50, 0x50, 0x50, 0xFF, 0x0)
    LoadEffect(0x3, "event\\ev294_00.eff")
    LoadEffect(0x2, "event\\ev291_03.eff")
    LoadEffect(0x1, "event\\ev291_04.eff")
    LoadEffect(0x6, "event\\ev291_00.eff")
    LoadEffect(0x4, "event\\ev291_01.eff")
    LoadEffect(0x5, "event\\ev292_00.eff")
    LoadEffect(0x7, "event\\ev291_05.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_38AF")
    LoadEffect(0x0, "event\\evanull.eff")

    label("loc_38AF")

    SetChrPos(0x9, 50, 9540, 23220, 360)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    ClearChrFlags(0x9, 0x1)
    OP_C9(0x0, 0x0, 0xFFFE2B40, 0xFFFD40E0, 0x0)
    OP_C9(0x0, 0x1, 0x5DC, 0x7D0, 0x0)
    OP_7D(0xC8, 0xC8, 0xFF, 0x0, 0x0)
    Sleep(1000)
    FadeToBright(2000, 0)
    Sleep(1000)
    PlayBGM("ed7501", 1)
    BeginChrThread(0x101, 3, 0, 39)
    Sleep(26000)
    BeginChrThread(0x101, 2, 0, 45)
    Sleep(800)
    BeginChrThread(0x101, 3, 0, 40)
    Sleep(1200)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFA2400, 0x7D0)
    OP_C9(0x0, 0x1, 0xBB8, 0xFA0, 0x7D0)
    Sleep(15000)
    EndChrThread(0x101, 0x2)
    Sleep(5700)
    BeginChrThread(0x101, 2, 0, 44)
    Sleep(2166)
    BeginChrThread(0x101, 3, 0, 41)
    BeginChrThread(0x22, 1, 0, 49)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFA2400, 0x3E8)
    OP_C9(0x0, 0x1, 0xBB8, 0xFA0, 0x3E8)
    OP_7D(0xC8, 0xC8, 0xFF, 0x0, 0x3E8)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 15, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 1000, 15000, 15, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_39FB():
        OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_39FB)

    def lambda_3A0C():
        OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_3A0C)

    def lambda_3A1D():
        OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_3A1D)

    def lambda_3A2E():
        OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_3A2E)

    def lambda_3A3F():
        OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_3A3F)

    def lambda_3A50():
        OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_3A50)
    WaitChrThread(0x101, 3)
    Sleep(2000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_3B21")
    StopBGM(0x1388)
    WaitChrThread(0x22, 1)
    WaitBGM()
    EndChrThread(0x101, 0xFF)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x4)
    EndChrThread(0x9, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xB, 0x20)
    ClearChrFlags(0xB, 0x1000)
    SetChrFlags(0xB, 0x1)
    SetChrFlags(0xB, 0x4)
    EndChrThread(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    EndChrThread(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    EndChrThread(0xF, 0xFF)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    EndChrThread(0x13, 0xFF)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    EndChrThread(0x14, 0xFF)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    EndChrThread(0x15, 0xFF)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    EndChrThread(0x16, 0xFF)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    OP_24(0x369)
    Return()

    label("loc_3B21")

    WaitChrThread(0x22, 1)
    OP_E6()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1F5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x369)
    SetScenarioFlags(0x5D, 5)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_48_33C7 end

    def Function_49_3B3F(): pass

    label("Function_49_3B3F")

    Sleep(15000)
    Sound(875, 0, 80, 0)
    Sound(877, 0, 100, 0)
    Sleep(3000)
    Sound(872, 0, 90, 0)
    Sound(873, 2, 100, 0)
    Sleep(4000)
    Sleep(4000)
    Sleep(5000)
    Sound(872, 0, 100, 0)
    Sleep(1000)
    OP_24(0x369)
    Sleep(5000)
    Return()

    # Function_49_3B3F end

    def Function_50_3B76(): pass

    label("Function_50_3B76")

    SetMapFlags(0x10)
    OP_11(0x0, 0x0, 0x0, 0x14, 0x15, 0x0)
    OP_A8(0x9, 0x14, 0x14, 0x0, 0x0)
    BeginChrThread(0x9, 1, 0, 59)
    OP_C9(0x0, 0x0, 0xFFFC5680, 0xFFFB6C20, 0x0)
    OP_C9(0x0, 0x1, 0x5DC, 0xAF0, 0x0)
    OP_C9(0x0, 0x0, 0xFFFDB610, 0xFFFB6C20, 0xFA0)
    SetChrChipByIndex(0x9, 0x28)
    OP_95(0x9, -3460, 1250, 25450, 800, 0x0)
    SetChrChipByIndex(0x9, 0x2D)
    OP_93(0x9, 0x87, 0x190)
    Sleep(1000)
    OP_93(0x9, 0xE1, 0x190)
    Sleep(1000)
    OP_93(0x9, 0x5A, 0x190)
    Return()

    # Function_50_3B76 end

    def Function_51_3C00(): pass

    label("Function_51_3C00")

    PlayEffect(0x5, 0x2, 0xFF, 0x0, 0, 1000, 25000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x8, 0x23)

    def lambda_3C40():

        label("loc_3C40")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_3C40")

    QueueWorkItem2(0x8, 3, lambda_3C40)
    OP_A7(0x8, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x8, -690, 1250, 22710, 90)
    OP_A7(0x8, 0x0, 0x0, 0x0, 0xFF, 0x64)
    OP_68(-1890, 2900, 22370, 2000)
    MoveCamera(0, 16, 0, 2000)
    OP_6E(620, 2000)
    SetCameraDistance(17000, 2000)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -1370, 2000, 23670, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(900)

    def lambda_3CE1():

        label("loc_3CE1")

        TurnDirection(0x9, 0x8, 500)
        Yield()
        Jump("loc_3CE1")

    QueueWorkItem2(0x9, 3, lambda_3CE1)
    Sleep(1500)
    PlayEffect(0x1, 0xFF, 0x8, 0x40, 0, 100, 0, 0, 0, 0, 1100, 1800, 1100, 0xFF, 0, 0, 0, 0)
    OP_C9(0x0, 0x0, 0xFFFC5680, 0xFFFB6C20, 0xC8)
    OP_C9(0x0, 0x1, 0x7D0, 0xAF0, 0xC8)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    OP_A8(0x8, 0x14, 0x14, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    Sleep(1000)
    OP_96(0x9, 0xFFFFF5D8, 0x4E2, 0x5BCC, 0x5DC, 0x0)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x8, 0x40, 0, 100, 0, 0, 0, 0, 1100, 1800, 1100, 0xFF, 0, 0, 0, 0)
    OP_96(0x9, 0xFFFFF5D8, 0x4E2, 0x558C, 0x7D0, 0x0)
    Sleep(500)

    def lambda_3DD1():
        OP_96(0x9, 0xFFFFF092, 0x4E2, 0x5C76, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3DD1)
    OP_A8(0x8, 0x0, 0x0, 0x0, 0x3E8)
    OP_A8(0x9, 0x0, 0x0, 0x0, 0x3E8)
    Return()

    # Function_51_3C00 end

    def Function_52_3DFB(): pass

    label("Function_52_3DFB")

    BeginChrThread(0x8, 1, 0, 57)
    EndChrThread(0x9, 0x1)
    OP_68(-2440, 2900, 24920, 4000)
    MoveCamera(0, 19, 0, 4000)
    OP_6E(680, 4000)
    SetCameraDistance(17000, 4000)
    OP_11(0x0, 0x0, 0x0, 0x14, 0x32, 0xBB8)
    OP_C9(0x0, 0x0, 0xFFFA81C0, 0xFFFBBA40, 0xBB8)
    OP_C9(0x0, 0x1, 0x9C4, 0xBB8, 0xBB8)
    OP_7D(0xFF, 0xFF, 0xC8, 0x0, 0xBB8)
    EndChrThread(0x8, 0x3)
    SetChrChipByIndex(0x8, 0x1F)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    OP_95(0x8, -3550, 1250, 22010, 2400, 0x0)
    BeginChrThread(0x8, 2, 0, 7)

    def lambda_3E9B():
        OP_9E(0x8, 0xFFFFF858, 0x625C, 0xFFFF63C0, 0x4B0, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3E9B)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    Sleep(1)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x7D0, 0x3E8)
    EndChrThread(0x8, 0x3)
    SetChrChipByIndex(0x8, 0x1F)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    WaitChrThread(0x8, 0)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x7D0, 0x384)
    EndChrThread(0x8, 0x3)
    SetChrChipByIndex(0x8, 0x1F)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)

    def lambda_3F25():
        OP_93(0x8, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3F25)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFF614, 0x4E2, 0x622A, 0xBB8, 0x2BC)
    BeginChrThread(0x8, 2, 0, 7)

    def lambda_3F55():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3F55)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x4B0, 0x1F4)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)
    EndChrThread(0x8, 0x3)
    SetChrSubChip(0x8, 0x2)
    Sleep(1100)

    def lambda_3F8C():
        OP_93(0x8, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3F8C)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFF394, 0x4E2, 0x65EA, 0x7D0, 0x578)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9D(0x8, 0xFFFFF902, 0x4E2, 0x65EA, 0x7D0, 0x578)
    BeginChrThread(0x8, 2, 0, 7)

    def lambda_3FDF():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3FDF)
    OP_9D(0x8, 0xFFFFFD9E, 0x4E2, 0x65EA, 0x7D0, 0x578)
    EndChrThread(0x8, 0x3)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    Sleep(500)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_9E(0x8, 0x3E8, 0x59D8, 0xFFFF15A0, 0x9C4, 0x1)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    BeginChrThread(0x8, 3, 0, 19)
    Sleep(700)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    Sleep(500)
    EndChrThread(0x8, 0x3)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)
    Sleep(800)
    EndChrThread(0x8, 0x1)
    Sleep(800)

    def lambda_406F():

        label("loc_406F")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_406F")

    QueueWorkItem2(0x8, 3, lambda_406F)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFF844, 0x4E2, 0x6004, 0x5DC, 0x7D0)
    Sleep(500)
    SetChrSubChip(0x8, 0x1)
    Sleep(60)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    Return()

    # Function_52_3DFB end

    def Function_53_40B6(): pass

    label("Function_53_40B6")

    BeginChrThread(0x8, 1, 0, 57)

    def lambda_40C1():
        OP_93(0x8, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_40C1)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFF902, 0x4E2, 0x639C, 0x7D0, 0x578)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9D(0x8, 0xFFFFF394, 0x4E2, 0x639C, 0x7D0, 0x578)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFEE30, 0x4E2, 0x639C, 0x7D0, 0x578)

    def lambda_412B():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_412B)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    Sleep(500)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_9E(0x8, 0xFFFFEE44, 0x54B0, 0xBB80, 0x7D0, 0x1)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    BeginChrThread(0x8, 3, 0, 19)
    Sleep(700)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    Sleep(400)

    def lambda_418A():

        label("loc_418A")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_418A")

    QueueWorkItem2(0x8, 3, lambda_418A)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)
    Sleep(1200)

    def lambda_41A7():

        label("loc_41A7")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_41A7")

    QueueWorkItem2(0x8, 3, lambda_41A7)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x8, 0x4)
    Sleep(1100)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x8, 0x1F)
    BeginChrThread(0x8, 0, 0, 55)
    Sleep(700)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x9, 0x29)
    BeginChrThread(0x9, 0, 0, 56)
    Return()

    # Function_53_40B6 end

    def Function_54_41ED(): pass

    label("Function_54_41ED")

    BeginChrThread(0x9, 1, 0, 58)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x28)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    OP_95(0x9, -3550, 1250, 22010, 2000, 0x0)
    BeginChrThread(0x9, 2, 0, 15)

    def lambda_4224():
        OP_9E(0x9, 0xFFFFF858, 0x625C, 0xFFFF63C0, 0x4B0, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_4224)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    Sleep(1)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x7D0, 0x3E8)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x29)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    WaitChrThread(0x9, 0)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x7D0, 0x384)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x29)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)

    def lambda_42AE():
        OP_93(0x9, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_42AE)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9D(0x9, 0xFFFFEE30, 0x4E2, 0x659A, 0xBB8, 0x2BC)
    BeginChrThread(0x9, 2, 0, 15)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 7)

    def lambda_42E8():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_42E8)

    def lambda_42F5():
        OP_9D(0x8, 0xFFFFFFBA, 0x4E2, 0x61DA, 0x4B0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_42F5)

    def lambda_4312():

        label("loc_4312")

        TurnDirection(0x9, 0x8, 500)
        Yield()
        Jump("loc_4312")

    QueueWorkItem2(0x9, 3, lambda_4312)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x4B0, 0x1F4)

    def lambda_433B():

        label("loc_433B")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_433B")

    QueueWorkItem2(0x8, 3, lambda_433B)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x1)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x28)
    OP_95(0x9, -4560, 1250, 26010, 3000, 0x0)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x2)
    Sleep(1100)
    BeginChrThread(0x101, 2, 0, 53)

    def lambda_438A():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_438A)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9D(0x9, 0xFFFFF394, 0x4E2, 0x65EA, 0x7D0, 0x578)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xFFFFF902, 0x4E2, 0x65EA, 0x7D0, 0x578)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9D(0x9, 0xFFFFFD9E, 0x4E2, 0x65EA, 0x7D0, 0x578)

    def lambda_43F4():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_43F4)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x2)
    Sleep(500)
    SetChrChipByIndex(0x9, 0x29)
    SetChrSubChip(0x9, 0x0)
    OP_9E(0x9, 0xFFFFFE0C, 0x59D8, 0xFFFF15A0, 0x7D0, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x2)
    BeginChrThread(0x9, 3, 0, 21)
    Sleep(700)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    Sleep(400)
    EndChrThread(0x9, 0x3)

    def lambda_4457():

        label("loc_4457")

        TurnDirection(0x9, 0x8, 500)
        Yield()
        Jump("loc_4457")

    QueueWorkItem2(0x9, 3, lambda_4457)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x1)
    Return()

    # Function_54_41ED end

    def Function_55_446D(): pass

    label("Function_55_446D")

    EndChrThread(0xFE, 0x3)
    OP_9E(0xFE, 0xFFFFFAD8, 0x59D8, 0x2BF20, 0x1194, 0x1)
    OP_9E(0xFE, 0xFFFFF8EE, 0x5BCC, 0x2BF20, 0x1194, 0x1)
    BeginChrThread(0xFE, 2, 0, 9)
    BeginChrThread(0xFE, 3, 0, 18)
    OP_9D(0xFE, 0xFFFFF786, 0x4E2, 0x53F2, 0xBB8, 0x3E8)
    EndChrThread(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 0x1F)
    OP_9E(0xFE, 0xFFFFF8EE, 0x5BCC, 0x2BF20, 0x1770, 0x1)
    OP_96(0xFE, 0x582, 0x4E2, 0x67F2, 0x1770, 0x0)
    BeginChrThread(0xFE, 2, 0, 6)
    OP_9D(0xFE, 0xD7A, 0x125C, 0x6C16, 0x12C0, 0x7D0)

    def lambda_4511():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4511)
    BeginChrThread(0xFE, 2, 0, 7)
    OP_9D(0xFE, 0x1158, 0x125C, 0x655E, 0x7D0, 0x578)
    BeginChrThread(0xFE, 2, 0, 9)
    BeginChrThread(0xFE, 3, 0, 18)
    OP_9D(0xFE, 0x15FE, 0x125C, 0x6B8A, 0x7D0, 0x578)

    def lambda_455E():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_455E)
    BeginChrThread(0xFE, 2, 0, 7)
    OP_9D(0xFE, 0xD7A, 0x125C, 0x6C16, 0x7D0, 0x578)
    BeginChrThread(0xFE, 2, 0, 9)
    BeginChrThread(0xFE, 3, 0, 18)
    OP_9D(0xFE, 0x1158, 0x125C, 0x655E, 0x7D0, 0x578)
    SetChrChipByIndex(0xFE, 0x1F)
    EndChrThread(0xFE, 0x3)
    OP_9E(0xFE, 0xD7A, 0x6C16, 0xFFFD8F00, 0x1388, 0x1)
    OP_9D(0xFE, 0xFFFFF02E, 0x1F0E, 0x6F86, 0x1388, 0x7D0)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    TurnDirection(0xFE, 0x9, 500)
    Sleep(500)
    Sleep(500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1700)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    BeginChrThread(0xFE, 2, 0, 6)
    ClearChrFlags(0xFE, 0x1)
    OP_9D(0xFE, 0xFFFFFC18, 0x20D0, 0x6978, 0x5DC, 0x320)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x2)
    BeginChrThread(0xFE, 3, 0, 18)

    def lambda_4638():
        OP_9E(0xFE, 0xFFFFFC18, 0x61A8, 0x1A3EC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4638)
    Sleep(1)

    def lambda_4656():
        OP_96(0xFE, 0xFDB, 0x4E2, 0x6554, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4656)
    Sleep(300)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_55_446D end

    def Function_56_46B6(): pass

    label("Function_56_46B6")

    EndChrThread(0xFE, 0x3)
    OP_9E(0xFE, 0xFFFFF84E, 0x59B0, 0x2BF20, 0xFA0, 0x1)
    BeginChrThread(0xFE, 2, 0, 17)
    BeginChrThread(0xFE, 3, 0, 20)
    OP_9D(0xFE, 0xFFFFF9CA, 0x4E2, 0x636A, 0xBB8, 0x3E8)

    def lambda_46F7():
        OP_96(0xFE, 0xFFFFFAD8, 0x4E2, 0x6978, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_46F7)

    def lambda_4711():

        label("loc_4711")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_4711")

    QueueWorkItem2(0x10, 1, lambda_4711)
    EndChrThread(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 0x29)
    OP_95(0xFE, 1410, 1250, 26610, 5000, 0x0)
    OP_68(-1000, 7000, 26030, 3000)
    MoveCamera(0, 12, 0, 3000)
    OP_6E(620, 3000)
    SetCameraDistance(17000, 3000)
    BeginChrThread(0xFE, 2, 0, 14)
    OP_9D(0xFE, 0xD7A, 0x125C, 0x6C16, 0x12C0, 0x7D0)

    def lambda_478A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_478A)
    BeginChrThread(0xFE, 2, 0, 15)
    OP_9D(0xFE, 0x1158, 0x125C, 0x655E, 0x7D0, 0x578)
    BeginChrThread(0xFE, 2, 0, 17)
    BeginChrThread(0xFE, 3, 0, 20)
    OP_9D(0xFE, 0x15FE, 0x125C, 0x6B8A, 0x7D0, 0x578)

    def lambda_47D7():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_47D7)
    BeginChrThread(0xFE, 2, 0, 15)
    OP_9D(0xFE, 0xD7A, 0x125C, 0x6C16, 0x7D0, 0x578)
    BeginChrThread(0xFE, 2, 0, 17)
    BeginChrThread(0xFE, 3, 0, 20)
    OP_9D(0xFE, 0x1158, 0x125C, 0x655E, 0x7D0, 0x578)
    SetChrChipByIndex(0xFE, 0x29)
    EndChrThread(0xFE, 0x3)
    OP_9E(0xFE, 0xD7A, 0x6C16, 0xFFFD8F00, 0x1388, 0x1)
    BeginChrThread(0xFE, 2, 0, 14)
    OP_9D(0xFE, 0xFFFFF02E, 0x1F0E, 0x6F86, 0x1388, 0x7D0)
    SetChrChipByIndex(0xFE, 0x28)
    OP_95(0xFE, -5770, 7950, 27760, 2000, 0x0)
    OP_95(0xFE, -6170, 7950, 26370, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Sleep(500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(500)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    BeginChrThread(0xFE, 2, 0, 14)
    ClearChrFlags(0xFE, 0x1)
    OP_9D(0xFE, 0xFFFFFC18, 0x20D0, 0x59D8, 0x5DC, 0x320)
    OP_68(-1000, 4000, 26030, 8000)
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x2)
    BeginChrThread(0xFE, 3, 0, 20)

    def lambda_48E9():
        OP_9E(0xFE, 0xFFFFFC18, 0x61A8, 0xFFE5C140, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_48E9)
    Sleep(1)

    def lambda_4907():
        OP_96(0xFE, 0xFDB, 0x4E2, 0x6554, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4907)
    Sleep(300)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_56_46B6 end

    def Function_57_4967(): pass

    label("Function_57_4967")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49FF")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_49DC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_49DC")
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    label("loc_49DC")

    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_57_4967")

    label("loc_49FF")

    Return()

    # Function_57_4967 end

    def Function_58_4A00(): pass

    label("Function_58_4A00")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A98")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4A75")
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A75")
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    label("loc_4A75")

    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_58_4A00")

    label("loc_4A98")

    Return()

    # Function_58_4A00 end

    def Function_59_4A99(): pass

    label("Function_59_4A99")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AE3")
    PlayEffect(0x1, 0xFF, 0xFE, 0x40, 0, 100, 0, 0, 0, 0, 1100, 1800, 1100, 0xFF, 0, 0, 0, 0)
    Sleep(3200)
    Jump("Function_59_4A99")

    label("loc_4AE3")

    Return()

    # Function_59_4A99 end

    def Function_60_4AE4(): pass

    label("Function_60_4AE4")

    OP_F8(0x14D)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    LoadChrToIndex("apl/ch50280.itc", 0x1E)
    LoadChrToIndex("apl/ch50281.itc", 0x1F)
    LoadChrToIndex("apl/ch50282.itc", 0x20)
    LoadChrToIndex("apl/ch50283.itc", 0x21)
    LoadChrToIndex("apl/ch50284.itc", 0x22)
    LoadChrToIndex("chr/ch09900.itc", 0x23)
    LoadChrToIndex("apl/ch50265.itc", 0x28)
    LoadChrToIndex("apl/ch50266.itc", 0x29)
    LoadChrToIndex("apl/ch50267.itc", 0x2A)
    LoadChrToIndex("apl/ch50268.itc", 0x2B)
    LoadChrToIndex("apl/ch50269.itc", 0x2C)
    LoadChrToIndex("chr/ch09800.itc", 0x2D)
    LoadChrToIndex("chr/ch36800.itc", 0x38)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x38)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x10, -9000, 1250, 25450, 270)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x2D)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-2580, 2900, 24350, 0)
    MoveCamera(0, 16, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x9, -6960, 1250, 25450, 90)
    SetChrPos(0x8, 3890, 4700, 27480, 225)
    SetChrPos(0x101, 10, 1250, 25450, 360)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SoundLoad(872)
    SoundLoad(873)
    SoundLoad(874)
    SoundLoad(876)
    Sound(877, 0, 100, 0)
    Sleep(4000)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("男性の声")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──女神の気まぐれか、\x01",
            "それとも悪戯によるものか……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《太陽の姫》は、《月の姫》が\x01",
            "生き別れた実の妹である事を知る。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "しかし《月の姫》はその事を知らず、\x01",
            "氷のような敵対心を向けてくるのみ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "思い悩んだ《太陽の姫》は\x01",
            "白装束と面で正体を隠した上で\x01",
            "森の廃墟に《月の姫》を呼び出す……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そこはかつて幼き姉妹が\x01",
            "仲睦まじく遊んだ秘密の場所であった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_E5()
    Sleep(1000)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFFFF, 0x1, "cv_eff01.itp")
    OP_7D(0xC8, 0xC8, 0xFF, 0x0, 0x1F4)
    FadeToBright(1000, 0)
    PlayBGM("ed7502", 1)
    LoadEffect(0x1, "event\\ev290_03.eff")
    LoadEffect(0x5, "event\\ev292_01.eff")
    LoadEffect(0x2, "event\\ev292_02.eff")
    LoadEffect(0x3, "event\\ev292_03.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_4F0C")
    LoadEffect(0x0, "event\\evanull.eff")
    LoadEffect(0x4, "event\\evanull.eff")
    LoadEffect(0x6, "event\\evanull.eff")
    LoadEffect(0x7, "event\\evanull.eff")

    label("loc_4F0C")

    BeginChrThread(0x101, 0, 0, 50)
    Sleep(8810)
    BeginChrThread(0x101, 1, 0, 51)
    Sleep(8900)
    BeginChrThread(0x101, 0, 0, 52)
    Sleep(8900)
    Sleep(8900)
    BeginChrThread(0x101, 1, 0, 54)
    Sleep(8900)
    Sleep(8900)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFA2400, 0x3E8)
    OP_C9(0x0, 0x1, 0xBB8, 0xFA0, 0x3E8)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 12000, 25000, 0, 180, 0, 1000, 1100, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 12000, 25000, 0, 180, 0, 1000, 1100, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 90, 0, 0, 1500, 1100, 1500, 0xFF, 0, 0, 0, 0)
    StopEffect(0x2, 0x2)
    BeginChrThread(0x22, 1, 0, 61)
    OP_7D(0xFF, 0xB4, 0xB4, 0x0, 0x22C4)
    Sleep(8900)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 12000, 25000, 0, 180, 0, 1000, 1100, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(4000)
    OP_7D(0x0, 0xFF, 0xFF, 0x0, 0x22C4)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 12000, 25000, 0, 180, 0, 1000, 1100, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 12000, 25000, 0, 180, 0, 1000, 1100, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(4900)
    FadeToDark(3000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_5143")
    StopBGM(0x1388)
    WaitChrThread(0x22, 1)
    WaitBGM()
    EndChrThread(0x101, 0xFF)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x4)
    EndChrThread(0x9, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x4)
    EndChrThread(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    EndChrThread(0x10, 0xFF)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    OP_24(0x369)
    Return()

    label("loc_5143")

    WaitChrThread(0x22, 1)
    OP_E6()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1F6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x369)
    SetScenarioFlags(0x5D, 6)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_60_4AE4 end

    def Function_61_5161(): pass

    label("Function_61_5161")

    Sleep(2500)
    Sound(876, 0, 100, 0)
    Sound(873, 2, 100, 0)
    Sleep(6500)
    Sound(874, 0, 100, 0)
    Sleep(8000)
    Sound(872, 0, 100, 0)
    Sleep(1000)
    OP_24(0x369)
    Sleep(3000)
    Return()

    # Function_61_5161 end

    def Function_62_518C(): pass

    label("Function_62_518C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52E9")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4410, 3700, 20000, 0, 90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4410, 3700, 20000, 0, 90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4100, 4800, 31100, 0, 90, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4000, 4800, 31100, 0, 90, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -4160, -2000, 31100, 0, -90, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 4160, -2000, 31100, 0, -90, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    Sleep(833)
    Jump("Function_62_518C")

    label("loc_52E9")

    Return()

    # Function_62_518C end

    def Function_63_52EA(): pass

    label("Function_63_52EA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5447")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4410, 3700, 20000, 0, 90, 0, 400, 600, 400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4410, 3700, 20000, 0, 90, 0, 400, 600, 400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4100, 4800, 31100, 0, 90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4000, 4800, 31100, 0, 90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -4160, -2000, 31100, 0, -90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 4160, -2000, 31100, 0, -90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sleep(833)
    Jump("Function_63_52EA")

    label("loc_5447")

    Return()

    # Function_63_52EA end

    def Function_64_5448(): pass

    label("Function_64_5448")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5517")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_54F4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_54F4")
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    label("loc_54F4")

    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_64_5448")

    label("loc_5517")

    Return()

    # Function_64_5448 end

    def Function_65_5518(): pass

    label("Function_65_5518")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_55E7")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_55C4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_55C4")
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    label("loc_55C4")

    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_65_5518")

    label("loc_55E7")

    Return()

    # Function_65_5518 end

    def Function_66_55E8(): pass

    label("Function_66_55E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56B7")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5694")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5694")
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(250)

    label("loc_5694")

    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_66_55E8")

    label("loc_56B7")

    Return()

    # Function_66_55E8 end

    def Function_67_56B8(): pass

    label("Function_67_56B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5787")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5764")
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5764")
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(250)

    label("loc_5764")

    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_67_56B8")

    label("loc_5787")

    Return()

    # Function_67_56B8 end

    def Function_68_5788(): pass

    label("Function_68_5788")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_57D2")
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_68_5788")

    label("loc_57D2")

    Return()

    # Function_68_5788 end

    def Function_69_57D3(): pass

    label("Function_69_57D3")


    def lambda_57D8():

        label("loc_57D8")

        TurnDirection(0xC, 0x8, 500)
        Yield()
        Jump("loc_57D8")

    QueueWorkItem2(0xC, 1, lambda_57D8)
    OP_95(0x8, -2000, 1250, 24200, 1000, 0x0)
    Sleep(1000)
    TurnDirection(0x8, 0xC, 500)
    Sleep(500)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x1)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x1)
    Sleep(90)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0x8, 0x0)
    Sleep(1500)
    SetChrSubChip(0xA, 0x1)
    SetChrSubChip(0x8, 0x1)
    Sleep(90)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    Sleep(1000)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    OP_93(0x8, 0x5A, 0x1F4)
    Sleep(13333)
    Sleep(3000)
    Return()

    # Function_69_57D3 end

    def Function_70_5858(): pass

    label("Function_70_5858")


    def lambda_585D():

        label("loc_585D")

        TurnDirection(0xC, 0x9, 500)
        Yield()
        Jump("loc_585D")

    QueueWorkItem2(0xC, 1, lambda_585D)
    OP_95(0x9, 2000, 1250, 24200, 1000, 0x0)
    Sleep(1000)
    TurnDirection(0x9, 0xC, 500)
    Sleep(500)
    SetChrChipByIndex(0xB, 0x2A)
    SetChrSubChip(0xB, 0x1)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x1)
    Sleep(90)
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0x9, 0x0)
    Sleep(1500)
    SetChrSubChip(0x9, 0x1)
    SetChrSubChip(0xB, 0x0)
    Sleep(90)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    Sleep(1000)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x2)
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(1000)
    EndChrThread(0xC, 0x1)
    OP_93(0xC, 0xB4, 0x1F4)
    BeginChrThread(0xC, 0, 0, 75)
    SetChrSubChip(0x8, 0x2)
    SetChrSubChip(0x9, 0x2)
    OP_68(50, 3500, 23770, 5000)
    MoveCamera(0, 15, 0, 5000)
    OP_6E(720, 5000)
    SetCameraDistance(15000, 5000)
    Return()

    # Function_70_5858 end

    def Function_71_5921(): pass

    label("Function_71_5921")

    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 2, 0, 15)

    def lambda_5936():
        OP_9D(0x9, 0xFA, 0xCB2, 0x5C58, 0x7D0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5936)
    Sleep(200)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    WaitChrThread(0x9, 1)
    OP_9D(0x9, 0x726, 0x4E2, 0x5C58, 0x1F4, 0x5DC)
    EndChrThread(0x9, 0x3)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x29)
    OP_9E(0x9, 0x0, 0x5DC0, 0x20F58, 0x1770, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)

    def lambda_59AE():
        OP_9E(0x9, 0x0, 0x5DC0, 0x1B7740, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_59AE)
    Sleep(33)

    def lambda_59CC():

        label("loc_59CC")

        TurnDirection(0x9, 0x8, 0)
        Yield()
        Jump("loc_59CC")

    QueueWorkItem2(0x9, 3, lambda_59CC)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x7D0, 0x7D0)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x7D0, 0x7D0)
    BeginChrThread(0x9, 3, 0, 20)
    BeginChrThread(0x9, 2, 0, 17)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xBB8, 0x3E8)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x29)
    EndChrThread(0x9, 0x1)
    EndChrThread(0x9, 0x3)
    BeginChrThread(0x9, 0, 0, 67)
    OP_9E(0x9, 0x0, 0x5DC0, 0x50910, 0x1388, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 2, 0, 14)

    def lambda_5A7C():

        label("loc_5A7C")

        TurnDirection(0x9, 0x8, 500)
        Yield()
        Jump("loc_5A7C")

    QueueWorkItem2(0x9, 3, lambda_5A7C)
    OP_9D(0x9, 0xFFFFEFF2, 0x4E2, 0x5DDE, 0xBB8, 0x3E8)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    Sleep(150)
    SetChrSubChip(0x9, 0x1)
    Sleep(150)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x0)
    Sleep(900)
    SetChrChipByIndex(0x9, 0x29)
    OP_95(0x9, -1420, 1250, 24000, 6000, 0x0)
    BeginChrThread(0x9, 2, 0, 13)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0x384, 0x4E2, 0x5BC2, 0x7D0, 0xDAC)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 2, 0, 47)

    def lambda_5B11():
        OP_9D(0x9, 0xF28, 0x4E2, 0x5BC2, 0xDAC, 0x384)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5B11)
    Sleep(1000)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    WaitChrThread(0x9, 1)

    def lambda_5B41():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_5B41)
    Sleep(700)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x1)
    Sleep(100)
    SetChrSubChip(0x9, 0x0)
    Sleep(600)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x29)
    OP_95(0x9, 500, 1250, 23750, 7000, 0x0)
    Return()

    # Function_71_5921 end

    def Function_72_5B81(): pass

    label("Function_72_5B81")

    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 2, 0, 7)

    def lambda_5B96():
        OP_9D(0x8, 0xFFFFFF06, 0xCB2, 0x5C58, 0x7D0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5B96)
    Sleep(200)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    WaitChrThread(0x8, 1)
    OP_9D(0x8, 0xFFFFF8DA, 0x4E2, 0x5C58, 0x1F4, 0x5DC)
    EndChrThread(0x8, 0x3)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x1F)
    OP_9E(0x8, 0x0, 0x5DC0, 0x20F58, 0x1770, 0x1)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 3, 0, 18)

    def lambda_5C14():
        OP_9E(0x8, 0x0, 0x5DC0, 0x1B7740, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5C14)
    Sleep(33)

    def lambda_5C32():

        label("loc_5C32")

        TurnDirection(0x8, 0x9, 0)
        Yield()
        Jump("loc_5C32")

    QueueWorkItem2(0x8, 3, lambda_5C32)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x7D0, 0x7D0)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x7D0, 0x7D0)
    BeginChrThread(0x8, 3, 0, 18)
    BeginChrThread(0x8, 2, 0, 9)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xBB8, 0x3E8)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x1F)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 0, 0, 66)
    OP_9E(0x8, 0x0, 0x5DC0, 0x50910, 0x1388, 0x1)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 2, 0, 6)

    def lambda_5CE2():

        label("loc_5CE2")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_5CE2")

    QueueWorkItem2(0x8, 3, lambda_5CE2)
    OP_9D(0x8, 0x100E, 0x4E2, 0x5DDE, 0xBB8, 0x3E8)
    EndChrThread(0x8, 0x3)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(150)
    SetChrSubChip(0x8, 0x1)
    Sleep(150)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sleep(900)
    SetChrChipByIndex(0x8, 0x1F)
    OP_95(0x8, 1420, 1250, 23000, 6000, 0x0)
    BeginChrThread(0x8, 2, 0, 10)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9D(0x8, 0xFFFFFC7C, 0x4E2, 0x5BC2, 0x7D0, 0xDAC)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 2, 0, 46)

    def lambda_5D77():
        OP_9D(0x8, 0xFFFFF0D8, 0x4E2, 0x5BC2, 0xDAC, 0x384)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5D77)
    Sleep(1000)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    WaitChrThread(0x8, 1)

    def lambda_5DA7():
        OP_93(0x8, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_5DA7)
    Sleep(700)

    def lambda_5DB7():

        label("loc_5DB7")

        TurnDirection(0x8, 0x9, 0)
        Yield()
        Jump("loc_5DB7")

    QueueWorkItem2(0x8, 3, lambda_5DB7)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x1)
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(600)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x1F)
    OP_95(0x8, -500, 1250, 23750, 7000, 0x0)
    Return()

    # Function_72_5B81 end

    def Function_73_5DF9(): pass

    label("Function_73_5DF9")

    OP_68(10, 7180, 26650, 3000)
    MoveCamera(0, 18, 0, 3000)
    OP_6E(720, 3000)
    SetCameraDistance(18500, 3000)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0x1720, 0x16A8, 0x605E, 0x157C, 0x7D0)
    EndChrThread(0x9, 0x3)
    OP_93(0x9, 0x10E, 0x0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x1)
    Sleep(30)
    SetChrSubChip(0x9, 0x0)
    Sleep(1000)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9D(0x9, 0x14F0, 0x1DB0, 0x67F2, 0x9C4, 0x5DC)
    SetChrChipByIndex(0x9, 0x29)
    OP_95(0x9, 3810, 7600, 30020, 6000, 0x0)
    OP_95(0x9, 2080, 7600, 30770, 6000, 0x0)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    TurnDirection(0x9, 0x8, 0)
    OP_68(0, 8920, 31090, 6000)
    MoveCamera(0, 0, 0, 6000)
    OP_6E(720, 6000)
    SetCameraDistance(18500, 6000)
    BeginChrThread(0x9, 0, 0, 68)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xFFFFF7E0, 0x1DB0, 0x7832, 0x9C4, 0xBB8)
    EndChrThread(0x9, 0x3)
    BeginChrThread(0x9, 2, 0, 16)
    Sleep(500)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9D(0x9, 0x820, 0x1DB0, 0x7832, 0x1F4, 0x7D0)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xFFFFF7E0, 0x1DB0, 0x7832, 0x9C4, 0xBB8)
    EndChrThread(0x9, 0x3)
    BeginChrThread(0x9, 2, 0, 16)
    Sleep(200)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9D(0x9, 0x820, 0x1DB0, 0x7832, 0x1F4, 0x7D0)
    Sleep(300)
    OP_9D(0x9, 0xFFFFF7E0, 0x1DB0, 0x7832, 0x1F4, 0x7D0)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0x820, 0x1DB0, 0x7832, 0xBB8, 0xBB8)
    EndChrThread(0x9, 0x3)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xFA, 0x2580, 0x7832, 0x834, 0xBB8)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 9900, 30800, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 9900, 30800, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 9900, 30800, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_9D(0x9, 0x7D0, 0x1DB0, 0x7832, 0x64, 0x1388)

    def lambda_60B4():

        label("loc_60B4")

        TurnDirection(0x9, 0x8, 0)
        Yield()
        Jump("loc_60B4")

    QueueWorkItem2(0x9, 3, lambda_60B4)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x1)
    Sleep(30)
    SetChrSubChip(0x9, 0x0)
    Sleep(250)
    BeginChrThread(0x9, 2, 0, 17)
    OP_9D(0x9, 0xFA, 0x2198, 0x7832, 0x44C, 0xBB8)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 8900, 30800, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 8900, 30800, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 8900, 30800, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_9D(0x9, 0x7D0, 0x1C84, 0x7832, 0x64, 0xBB8)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x1)
    Sleep(30)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    Sleep(500)
    SetChrChipByIndex(0x9, 0x28)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    OP_96(0x9, 0x10FE, 0x1C84, 0x76B6, 0x5DC, 0x0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x1)
    Sleep(30)
    SetChrSubChip(0x9, 0x0)
    Sleep(800)
    BeginChrThread(0x9, 2, 0, 13)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0x7D0, 0x1DB0, 0x7832, 0x7D0, 0x1388)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xFA, 0x2134, 0x7832, 0x5DC, 0x1388)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 8900, 30800, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 8900, 30800, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 8900, 30800, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 8900, 30800, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_68(10, 2900, 23870, 5000)
    MoveCamera(0, 20, 0, 5000)
    OP_6E(720, 5000)
    SetCameraDistance(18500, 5000)
    FadeToDark(0, 16777215, -1)
    FadeToBright(200, 16777215)
    BeginChrThread(0x9, 0, 0, 68)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 3, 0, 21)
    OP_96(0x9, 0x190, 0x1B58, 0x61A8, 0xBB8, 0x0)

    def lambda_6388():
        OP_9E(0x9, 0x0, 0x61A8, 0x20F580, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6388)
    Sleep(33)
    OP_96(0x9, 0xFA, 0x4E2, 0x61A8, 0x4B0, 0x0)
    BeginChrThread(0x9, 0, 0, 67)
    BeginChrThread(0x9, 3, 0, 20)
    Sleep(800)
    OP_96(0x9, 0x6EA, 0x4E2, 0x5226, 0x3E8, 0x0)
    Sleep(1033)
    EndChrThread(0x9, 0x3)
    OP_93(0x9, 0xE1, 0x0)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x2)
    Sleep(1500)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9C(0x9, 0x3E8, 0x0, 0x0, 0x44C, 0x578)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x1)
    Sleep(2000)
    BeginChrThread(0x9, 2, 0, 14)
    OP_9C(0x9, 0x0, 0xBB8, 0x0, 0x1004, 0x3E8)
    BeginChrThread(0x9, 0, 0, 68)
    OP_9F(0x0, 0x9)
    OP_9F(0x1, -1510, 5250, 25740)
    OP_9F(0x1, 1510, 7250, 25740)
    OP_9F(0x1, 600, 8250, 20580)
    OP_9F(0x2, 0x9, 4000, 0x2)
    Return()

    # Function_73_5DF9 end

    def Function_74_6474(): pass

    label("Function_74_6474")

    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9D(0x8, 0xFFFFE8E0, 0x16A8, 0x605E, 0x157C, 0x7D0)
    EndChrThread(0x8, 0x3)
    OP_93(0x8, 0x5A, 0x0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x1)
    Sleep(30)
    SetChrSubChip(0x8, 0x0)
    Sleep(1000)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFEB10, 0x1DB0, 0x67F2, 0x9C4, 0x5DC)
    SetChrChipByIndex(0x8, 0x1F)
    OP_95(0x8, -3810, 7600, 30020, 6000, 0x0)
    OP_95(0x8, -2080, 7600, 30770, 6000, 0x0)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    TurnDirection(0x8, 0x9, 0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)
    BeginChrThread(0x8, 0, 0, 68)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0x820, 0x1DB0, 0x7832, 0x1F4, 0x7D0)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9D(0x8, 0xFFFFF7E0, 0x1DB0, 0x7832, 0x9C4, 0xBB8)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 8)
    Sleep(500)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFF3F8, 0x1DB0, 0x7832, 0x1F4, 0x7D0)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    Sleep(100)
    OP_9D(0x8, 0xFFFFF7E0, 0x1DB0, 0x7832, 0xC8, 0xBB8)
    BeginChrThread(0x8, 2, 0, 10)
    BeginChrThread(0x8, 3, 0, 20)
    OP_9D(0x8, 0x820, 0x1DB0, 0x7832, 0xBB8, 0xBB8)
    BeginChrThread(0x8, 2, 0, 8)
    EndChrThread(0x8, 0x3)
    Sleep(500)
    OP_9D(0x8, 0xFFFFF7E0, 0x1DB0, 0x7832, 0x1F4, 0x7D0)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9D(0x8, 0xFFFFFF06, 0x2580, 0x7832, 0x834, 0xBB8)
    OP_9D(0x8, 0xFFFFF830, 0x1DB0, 0x7832, 0x64, 0x1388)

    def lambda_6635():

        label("loc_6635")

        TurnDirection(0x8, 0x9, 0)
        Yield()
        Jump("loc_6635")

    QueueWorkItem2(0x8, 3, lambda_6635)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x1)
    Sleep(30)
    SetChrSubChip(0x8, 0x0)
    Sleep(250)
    BeginChrThread(0x8, 2, 0, 9)
    OP_9D(0x8, 0xFFFFFF06, 0x2198, 0x7832, 0x44C, 0xBB8)
    OP_9D(0x8, 0xFFFFF830, 0x1C84, 0x7832, 0x64, 0xBB8)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x1)
    Sleep(30)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    Sleep(500)
    SetChrChipByIndex(0x8, 0x1E)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    OP_96(0x8, 0xFFFFEF02, 0x1C84, 0x76B6, 0x5DC, 0x0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x1)
    Sleep(30)
    SetChrSubChip(0x8, 0x0)
    Sleep(800)
    BeginChrThread(0x8, 2, 0, 10)
    BeginChrThread(0x8, 3, 0, 20)
    OP_9D(0x8, 0xFFFFF830, 0x1DB0, 0x7832, 0x7D0, 0x1388)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9D(0x8, 0xFFFFFF06, 0x2134, 0x7832, 0x5DC, 0x1388)
    BeginChrThread(0x8, 0, 0, 68)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 3, 0, 19)
    OP_96(0x8, 0xFFFFFE70, 0x1B58, 0x61A8, 0xBB8, 0x0)

    def lambda_6747():
        OP_9E(0x8, 0x0, 0x61A8, 0x20F580, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6747)
    Sleep(33)
    OP_96(0x8, 0xFFFFFF06, 0x4E2, 0x61A8, 0x4B0, 0x0)
    BeginChrThread(0x8, 0, 0, 66)
    BeginChrThread(0x8, 3, 0, 18)
    Sleep(800)
    OP_96(0x8, 0xFFFFF916, 0x4E2, 0x5226, 0x3E8, 0x0)
    Sleep(1033)
    EndChrThread(0x8, 0x3)
    OP_93(0x8, 0x87, 0x0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    Sleep(1500)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9C(0x8, 0xFFFFFC18, 0x0, 0x0, 0x44C, 0x578)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)
    Sleep(2000)
    BeginChrThread(0x8, 2, 0, 6)
    OP_9C(0x8, 0x0, 0xBB8, 0x0, 0x1004, 0x3E8)
    BeginChrThread(0x8, 0, 0, 68)
    OP_9F(0x0, 0x8)
    OP_9F(0x1, 1510, 5250, 25740)
    OP_9F(0x1, -1510, 7250, 25740)
    OP_9F(0x1, -600, 8250, 20580)
    OP_9F(0x2, 0x8, 4000, 0x2)
    Return()

    # Function_74_6474 end

    def Function_75_6833(): pass

    label("Function_75_6833")

    OP_96(0xC, 0xA, 0x4E2, 0x7044, 0x3E8, 0x0)
    OP_96(0xC, 0x0, 0x8F2, 0x7486, 0x3E8, 0x0)
    Return()

    # Function_75_6833 end

    def Function_76_685C(): pass

    label("Function_76_685C")

    OP_F8(0x14D)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "yuka", 0x0, 0x1)
    SetMapObjFrame(0x3, "ball", 0x0, 0x1)
    SetMapObjFrame(0x3, "04Bback", 0x0, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    LoadChrToIndex("apl/ch50250.itc", 0x1E)
    LoadChrToIndex("apl/ch50251.itc", 0x1F)
    LoadChrToIndex("apl/ch50252.itc", 0x20)
    LoadChrToIndex("apl/ch50253.itc", 0x21)
    LoadChrToIndex("apl/ch50254.itc", 0x22)
    LoadChrToIndex("apl/ch50255.itc", 0x23)
    LoadChrToIndex("apl/ch50265.itc", 0x28)
    LoadChrToIndex("apl/ch50266.itc", 0x29)
    LoadChrToIndex("apl/ch50267.itc", 0x2A)
    LoadChrToIndex("apl/ch50268.itc", 0x2B)
    LoadChrToIndex("apl/ch50269.itc", 0x2C)
    LoadChrToIndex("apl/ch50270.itc", 0x2D)
    LoadChrToIndex("chr/ch36700.itc", 0x34)
    LoadChrToIndex("chr/ch36600.itc", 0x35)
    LoadChrToIndex("chr/ch36900.itc", 0x36)
    LoadChrToIndex("chr/ch37000.itc", 0x37)
    LoadChrToIndex("chr/ch36800.itc", 0x38)
    LoadChrToIndex("chr/ch37100.itc", 0x39)
    LoadChrToIndex("chr/ch37200.itc", 0x3A)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x34)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x35)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x36)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x37)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x38)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x3A)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x3A)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x39)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x39)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x39)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x39)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrPos(0xC, 10, 1250, 26300, 180)
    SetChrPos(0xE, -2920, 1800, 28680, 135)
    SetChrPos(0x10, -3610, 1800, 27530, 135)
    SetChrPos(0x11, -4670, 1800, 28800, 132)
    SetChrPos(0x12, -4830, 1800, 27400, 132)
    SetChrPos(0xD, 2920, 1800, 28680, 225)
    SetChrPos(0xF, 3610, 1800, 27530, 225)
    SetChrPos(0x13, 4670, 1800, 28800, 225)
    SetChrPos(0x14, 4830, 1800, 27400, 225)
    SetChrPos(0x15, -6200, 1250, 24300, 135)
    SetChrPos(0x16, 6200, 1250, 24300, 225)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, -6450, 1250, 24260, 90)
    SetChrPos(0x9, 6450, 1250, 24260, 90)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x2B)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x100)
    SetChrPos(0xB, 10, 1250, 25450, 230)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_D3(0xB, 0x2BF20, 0x0, 0x0, 0x0)
    BeginChrThread(0xB, 3, 0, 30)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x21)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x100)
    SetChrPos(0xA, 10, 1250, 25450, 230)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_D3(0xA, 0x2BF20, 0x0, 0x0, 0x0)
    BeginChrThread(0xA, 3, 0, 31)
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x17, 0x34)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x100)
    SetChrPos(0x17, 10, 1250, 25450, 230)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_D3(0x17, 0x2BF20, 0x0, 0x0, 0x0)
    BeginChrThread(0x17, 3, 0, 32)
    OP_68(10, 3830, 24760, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(860, 0)
    SetCameraDistance(15000, 0)
    OP_7D(0xC8, 0xC8, 0xC8, 0x0, 0x1F4)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFA2400, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xFA0, 0x0)
    SetChrPos(0x101, 10, 1250, 28450, 360)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    LoadEffect(0x0, "event\\ev290_01.eff")
    LoadEffect(0x1, "event\\ev291_04.eff")
    LoadEffect(0x2, "event\\ev291_03.eff")
    LoadEffect(0x3, "event\\ev290_00.eff")
    LoadEffect(0x4, "event\\ev293_01.eff")
    LoadEffect(0x5, "event\\ev293_02.eff")
    LoadEffect(0x6, "event\\ev292_04.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_6DDB")
    LoadEffect(0x7, "event\\evanull.eff")

    label("loc_6DDB")

    SoundLoad(872)
    SoundLoad(873)
    SoundLoad(874)
    SoundLoad(876)
    Sound(877, 0, 100, 0)
    Sleep(4000)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性の声")

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "──かつて幼き姉妹を\x01",
            "離れ離れにした恐るべき陰謀劇……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "その真相を知りながらも結局、\x01",
            "姉妹は相争うことになりました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "なぜならば彼女たちは『姫』……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "舞いこそが彼女たちの全てであり、\x01",
            "女神の意志を宿せる『巫女姫』は\x01",
            "たった１人しかいなかったからです。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "互いへの思慕の念、そして同じ相手を\x01",
            "好きになってしまった葛藤……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "それ以上に、得がたきライバルへの\x01",
            "熱い共感と燃えるような対抗意識……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0024
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "その全てを胸に秘めた二人の姫が、\x01",
            "今宵、『星の祭殿』に降り立ちました──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_E5()
    Sleep(1000)
    PlayBGM("ed7503", 1)
    FadeToBright(1000, 0)
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 62)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4410, 3700, 20000, 0, 90, 0, 400, 600, 400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4410, 3700, 20000, 0, 90, 0, 400, 600, 400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4100, 4800, 31100, 0, 90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4000, 4800, 31100, 0, 90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -4160, -2000, 31100, 0, -90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 4160, -2000, 31100, 0, -90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    OP_7D(0xFF, 0xFF, 0xDC, 0x0, 0x0)
    OP_7D(0xC8, 0xC8, 0xC8, 0x0, 0x3E8)
    BeginChrThread(0x8, 0, 0, 64)
    BeginChrThread(0x101, 0, 0, 69)
    Sleep(10333)
    BeginChrThread(0x9, 0, 0, 65)
    BeginChrThread(0x101, 1, 0, 70)
    Sleep(3000)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4410, 3700, 20000, 0, 90, 0, 400, 600, 400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4410, 3700, 20000, 0, 90, 0, 400, 600, 400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4100, 4800, 31100, 0, 90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4000, 4800, 31100, 0, 90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -4160, -2000, 31100, 0, -90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 4160, -2000, 31100, 0, -90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    OP_7D(0xFF, 0xFF, 0xDC, 0x0, 0x0)
    OP_7D(0xC8, 0xC8, 0xC8, 0x0, 0x3E8)
    Sleep(15000)
    BeginChrThread(0x101, 0, 0, 72)
    BeginChrThread(0x101, 1, 0, 71)
    Sleep(500)
    BeginChrThread(0x22, 1, 0, 77)
    FadeToDark(0, 16777215, -1)
    FadeToBright(200, 16777215)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 3900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 3900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 3900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 3900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_C9(0x0, 0x0, 0xFFF6D840, 0xFFFA2400, 0x1F4)
    OP_C9(0x0, 0x1, 0xDAC, 0xFA0, 0x1F4)
    OP_7D(0xE6, 0xDC, 0xFF, 0x0, 0x1F4)
    BeginChrThread(0x101, 3, 0, 63)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 15, 0, 0, 1100, 1200, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 1000, 15000, 15, 0, 0, 1100, 1200, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 90, 0, 0, 1500, 1600, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(15000)
    FadeToDark(0, 16777215, -1)
    FadeToBright(200, 16777215)
    BeginChrThread(0x101, 0, 0, 74)
    BeginChrThread(0x101, 1, 0, 73)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 1900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 1900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(35000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    WaitChrThread(0x22, 1)
    WaitBGM()
    OP_E6()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_76EC")
    EndChrThread(0x101, 0xFF)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x4)
    EndChrThread(0x9, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xB, 0x20)
    ClearChrFlags(0xB, 0x1000)
    SetChrFlags(0xB, 0x1)
    SetChrFlags(0xB, 0x4)
    EndChrThread(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x4)
    EndChrThread(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x1000)
    SetChrFlags(0xA, 0x1)
    SetChrFlags(0xA, 0x4)
    EndChrThread(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xC, 0x20)
    ClearChrFlags(0xC, 0x1000)
    SetChrFlags(0xC, 0x1)
    SetChrFlags(0xC, 0x4)
    EndChrThread(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x17, 0x20)
    ClearChrFlags(0x17, 0x1000)
    SetChrFlags(0x17, 0x1)
    SetChrFlags(0x17, 0x4)
    EndChrThread(0x17, 0xFF)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    EndChrThread(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    EndChrThread(0xE, 0xFF)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    EndChrThread(0xF, 0xFF)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    EndChrThread(0x10, 0xFF)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    EndChrThread(0x11, 0xFF)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    EndChrThread(0x12, 0xFF)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    EndChrThread(0x13, 0xFF)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    EndChrThread(0x14, 0xFF)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    EndChrThread(0x15, 0xFF)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    EndChrThread(0x16, 0xFF)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    OP_24(0x369)
    Return()

    label("loc_76EC")

    OP_24(0x369)
    SetScenarioFlags(0x5D, 7)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_76_685C end

    def Function_77_76FC(): pass

    label("Function_77_76FC")

    Sleep(500)
    Sound(874, 0, 100, 0)
    Sound(876, 0, 100, 0)
    Sound(873, 2, 100, 0)
    Sleep(14500)
    Sound(872, 0, 100, 0)
    Sleep(15000)
    Sound(872, 0, 100, 0)
    Sleep(8000)
    Sound(874, 0, 100, 0)
    Sleep(2000)
    Sound(872, 0, 100, 0)
    Sleep(2000)
    Sound(876, 0, 100, 0)
    Sleep(7000)
    Sound(874, 0, 100, 0)
    Sleep(1000)
    OP_24(0x369)
    Sleep(1000)
    Return()

    # Function_77_76FC end

    def Function_78_7751(): pass

    label("Function_78_7751")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7764")
    Sleep(4138)
    Jump("Function_78_7751")

    label("loc_7764")

    Return()

    # Function_78_7751 end

    def Function_79_7765(): pass

    label("Function_79_7765")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_77AF")
    PlayEffect(0x7, 0xFF, 0xFE, 0x100, -500, -800, 0, 0, 180, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Jump("Function_79_7765")

    label("loc_77AF")

    Return()

    # Function_79_7765 end

    def Function_80_77B0(): pass

    label("Function_80_77B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_789F")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4410, 3700, 20000, 0, 90, 0, 300, 400, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4410, 3700, 20000, 0, 90, 0, 300, 400, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4100, 4800, 31100, 0, 90, 0, 200, 300, 200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4000, 4800, 31100, 0, 90, 0, 200, 300, 200, 0xFF, 0, 0, 0, 0)
    Sleep(833)
    Jump("Function_80_77B0")

    label("loc_789F")

    Return()

    # Function_80_77B0 end

    def Function_81_78A0(): pass

    label("Function_81_78A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_78EA")
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_81_78A0")

    label("loc_78EA")

    Return()

    # Function_81_78A0 end

    def Function_82_78EB(): pass

    label("Function_82_78EB")

    SetChrFlags(0x8, 0x4)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    OP_9D(0x8, 0xA, 0x2E18, 0x61A8, 0xFA0, 0x3E8)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    BeginChrThread(0x8, 2, 0, 9)
    Sleep(50)
    BeginChrThread(0x8, 3, 0, 19)

    def lambda_792F():
        OP_9E(0x8, 0xFFFFFA24, 0x61A8, 0x927C0, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_792F)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_7971():
        OP_9E(0x8, 0x0, 0x61A8, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_7971)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x8, 0x0)

    def lambda_79AA():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_79AA)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_79C0():
        OP_9E(0x8, 0x0, 0x61A8, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_79C0)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x8, 0x0)

    def lambda_79F9():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_79F9)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_7A35():
        OP_9E(0x8, 0x0, 0x61A8, 0xFFFA81C0, 0x2134, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_7A35)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x320)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x8, 0x0)

    def lambda_7A98():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_7A98)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFFE0C, 0x319C, 0x61A8, 0x7D0, 0xBB8)

    def lambda_7AC2():
        OP_9E(0x8, 0x0, 0x61A8, 0xFFF50380, 0x1194, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_7AC2)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 9)
    Sleep(1)
    OP_9D(0x8, 0xFFFFFE0C, 0x332C, 0x61A8, 0xBB8, 0x4B0)
    EndChrThread(0x8, 0x3)
    OP_93(0x8, 0xB4, 0x0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Return()

    # Function_82_78EB end

    def Function_83_7B10(): pass

    label("Function_83_7B10")

    Sleep(600)
    SetChrSubChip(0x8, 0x1)
    Sleep(100)
    OP_93(0x8, 0x87, 0x0)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x1)
    Return()

    # Function_83_7B10 end

    def Function_84_7B2A(): pass

    label("Function_84_7B2A")

    SetChrFlags(0x9, 0x4)
    BeginChrThread(0x9, 2, 0, 14)
    Sleep(100)
    OP_9D(0x9, 0xA, 0x2E18, 0x61A8, 0xFA0, 0x3E8)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    Sleep(100)
    BeginChrThread(0x9, 2, 0, 17)
    Sleep(50)
    BeginChrThread(0x9, 3, 0, 21)

    def lambda_7B6E():
        OP_9E(0x9, 0x5DC, 0x61A8, 0x927C0, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_7B6E)
    Sleep(33)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    EndChrThread(0x9, 0x3)
    BeginChrThread(0x9, 2, 0, 14)
    Sleep(100)

    def lambda_7BB0():
        OP_9E(0x9, 0x0, 0x61A8, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_7BB0)
    Sleep(33)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x9, 0x0)

    def lambda_7BE9():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_7BE9)
    BeginChrThread(0x9, 2, 0, 14)
    Sleep(100)

    def lambda_7BFF():
        OP_9E(0x9, 0x0, 0x61A8, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_7BFF)
    Sleep(33)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x9, 0x0)

    def lambda_7C38():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_7C38)
    BeginChrThread(0x9, 2, 0, 14)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    BeginChrThread(0x9, 2, 0, 14)
    Sleep(100)

    def lambda_7C74():
        OP_9E(0x9, 0x0, 0x61A8, 0xFFFA81C0, 0x2134, 0x2)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_7C74)
    Sleep(33)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xFA0, 0x320)
    BeginChrThread(0x9, 2, 0, 14)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    EndChrThread(0x9, 0x3)
    EndChrThread(0x9, 0x0)

    def lambda_7CD7():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_7CD7)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9D(0x9, 0x1F4, 0x319C, 0x61A8, 0x7D0, 0xBB8)

    def lambda_7D01():
        OP_9E(0x9, 0x0, 0x61A8, 0xFFF50380, 0x1194, 0x2)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_7D01)
    EndChrThread(0x9, 0x3)
    BeginChrThread(0x9, 2, 0, 17)
    Sleep(1)
    OP_9D(0x9, 0x1F4, 0x332C, 0x61A8, 0xBB8, 0x4B0)
    OP_93(0x9, 0xB4, 0x0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    Return()

    # Function_84_7B2A end

    def Function_85_7D4B(): pass

    label("Function_85_7D4B")

    Sleep(600)
    SetChrSubChip(0x9, 0x1)
    Sleep(100)
    OP_93(0x9, 0xE1, 0x0)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x1)
    Return()

    # Function_85_7D4B end

    def Function_86_7D65(): pass

    label("Function_86_7D65")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D9B")
    OP_D3(0x18, 0x0, 0x36EE80, 0x0, 0xEA60)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    Jump("Function_86_7D65")

    label("loc_7D9B")

    Return()

    # Function_86_7D65 end

    def Function_87_7D9C(): pass

    label("Function_87_7D9C")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_95(0xFE, 2610, 1250, 24750, 4000, 0x0)
    Sleep(500)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x2BC, 0xBB8)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x2BC, 0xBB8)
    Sleep(800)
    OP_93(0xFE, 0x5A, 0x2BC)
    Sleep(100)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(300)
    OP_93(0xFE, 0xC8, 0x2BC)
    OP_9E(0xFE, 0x0, 0x61A8, 0x99CF0, 0x1770, 0x1)
    OP_9E(0xFE, 0x0, 0x66BC, 0x29810, 0x1770, 0x1)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x2)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    SetChrSubChip(0xFE, 0x2)
    Sleep(1000)

    label("loc_7E62")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7EC8")
    OP_A1(0xFE, 0x7D0, 0x4, 0x2, 0x3, 0x2, 0x4)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E9A")
    Sleep(1500)
    Jump("loc_7EC3")

    label("loc_7E9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7EB1")
    Sleep(800)
    Jump("loc_7EC3")

    label("loc_7EB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7EC3")
    Sleep(100)

    label("loc_7EC3")

    Jump("loc_7E62")

    label("loc_7EC8")

    Return()

    # Function_87_7D9C end

    def Function_88_7EC9(): pass

    label("Function_88_7EC9")

    Sleep(4000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_95(0xFE, 2610, 1250, 24750, 5000, 0x0)
    OP_9E(0xFE, 0x0, 0x61A8, 0x8ED28, 0x1388, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x10, 500)
    Sleep(1000)
    OP_99(0xFE, 0x10, 0x3E8, 0x1F4, 0x0)
    Return()

    # Function_88_7EC9 end

    def Function_89_7F1C(): pass

    label("Function_89_7F1C")

    Sleep(4500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_95(0xFE, 2610, 1250, 24750, 5000, 0x0)
    OP_9E(0xFE, 0x0, 0x61A8, 0x83D60, 0x1388, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x10, 500)
    Sleep(1000)
    OP_99(0xFE, 0x10, 0x4B0, 0x1F4, 0x0)
    Return()

    # Function_89_7F1C end

    def Function_90_7F6F(): pass

    label("Function_90_7F6F")

    OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xBB8, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x7D0, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFE0C, 0x0, 0x5DC, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFE0C, 0x0, 0x3E8, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFE0C, 0x0, 0x320, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFE0C, 0x0, 0x28A, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0x1F4, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x12C, 0x0)
    Return()

    # Function_90_7F6F end

    def Function_91_8010(): pass

    label("Function_91_8010")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_802E")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_91_8010")

    label("loc_802E")

    Return()

    # Function_91_8010 end

    def Function_92_802F(): pass

    label("Function_92_802F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_804D")
    OP_A1(0xFE, 0x7D0, 0x8, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3, 0x0, 0x1)
    Jump("Function_92_802F")

    label("loc_804D")

    Return()

    # Function_92_802F end

    def Function_93_804E(): pass

    label("Function_93_804E")

    OP_9D(0x8, 0xFFFFFA06, 0x109A, 0x578A, 0x7D0, 0x7D0)
    SetChrChipByIndex(0x8, 0x1E)
    BeginChrThread(0x8, 2, 0, 91)
    Sleep(5200)
    SetChrChipByIndex(0x8, 0x1F)
    Sleep(2000)
    EndChrThread(0x8, 0x2)
    OP_93(0x8, 0x87, 0x0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    OP_9D(0x8, 0xFFFFFE0C, 0x157C, 0x61A8, 0xBB8, 0x4B0)

    def lambda_80A8():

        label("loc_80A8")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0x320, 0x3)
        Yield()
        Jump("loc_80A8")

    QueueWorkItem2(0x8, 2, lambda_80A8)
    Sleep(1)
    OP_96(0x8, 0xFFFFFE0C, 0x2BC0, 0x61A8, 0x12C, 0x0)
    EndChrThread(0x8, 0x2)
    BeginChrThread(0x8, 2, 0, 7)
    ClearChrFlags(0x8, 0x1)
    OP_9D(0x8, 0xFFFFFE0C, 0x300C, 0x61A8, 0x7D0, 0x7D0)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x24)

    label("loc_8109")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8127")
    OP_A1(0x8, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("loc_8109")

    label("loc_8127")

    Return()

    # Function_93_804E end

    def Function_94_8128(): pass

    label("Function_94_8128")

    OP_9D(0x9, 0x5FA, 0x109A, 0x578A, 0x7D0, 0x7D0)
    SetChrChipByIndex(0x9, 0x28)
    BeginChrThread(0x9, 2, 0, 92)
    Sleep(5200)
    SetChrChipByIndex(0x9, 0x29)
    Sleep(2000)
    EndChrThread(0x9, 0x2)
    OP_93(0x9, 0xE1, 0x0)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x2)
    OP_9D(0x9, 0x1F4, 0x157C, 0x61A8, 0xBB8, 0x4B0)

    def lambda_8182():

        label("loc_8182")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0x320, 0x3)
        Yield()
        Jump("loc_8182")

    QueueWorkItem2(0x9, 2, lambda_8182)
    Sleep(1)
    OP_96(0x9, 0x1F4, 0x2BC0, 0x61A8, 0x12C, 0x0)
    EndChrThread(0x9, 0x2)
    BeginChrThread(0x9, 2, 0, 15)
    ClearChrFlags(0x9, 0x1)
    OP_9D(0x9, 0x1F4, 0x2EE0, 0x61A8, 0x7D0, 0x7D0)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x2E)
    SetChrSubChip(0x9, 0x6)

    label("loc_81E7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8205")
    OP_A1(0x9, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("loc_81E7")

    label("loc_8205")

    Return()

    # Function_94_8128 end

    def Function_95_8206(): pass

    label("Function_95_8206")

    OP_F8(0x14D)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    LoadChrToIndex("apl/ch50250.itc", 0x1E)
    LoadChrToIndex("apl/ch50251.itc", 0x1F)
    LoadChrToIndex("apl/ch50252.itc", 0x20)
    LoadChrToIndex("apl/ch50253.itc", 0x21)
    LoadChrToIndex("apl/ch50254.itc", 0x22)
    LoadChrToIndex("apl/ch50255.itc", 0x23)
    LoadChrToIndex("apl/ch50256.itc", 0x24)
    LoadChrToIndex("apl/ch50265.itc", 0x28)
    LoadChrToIndex("apl/ch50266.itc", 0x29)
    LoadChrToIndex("apl/ch50267.itc", 0x2A)
    LoadChrToIndex("apl/ch50268.itc", 0x2B)
    LoadChrToIndex("apl/ch50269.itc", 0x2C)
    LoadChrToIndex("apl/ch50270.itc", 0x2D)
    LoadChrToIndex("apl/ch50271.itc", 0x2E)
    LoadChrToIndex("chr/ch00102.itc", 0x2F)
    LoadChrToIndex("apl/ch50234.itc", 0x30)
    LoadChrToIndex("chr/ch25800.itc", 0x31)
    LoadChrToIndex("apl/ch50294.itc", 0x32)
    LoadChrToIndex("chr/ch36700.itc", 0x34)
    LoadChrToIndex("chr/ch36600.itc", 0x35)
    LoadChrToIndex("chr/ch36900.itc", 0x36)
    LoadChrToIndex("chr/ch37000.itc", 0x37)
    LoadChrToIndex("chr/ch36800.itc", 0x38)
    LoadChrToIndex("apl/ch50289.itc", 0x39)
    LoadChrToIndex("chr/ch37200.itc", 0x3A)
    LoadChrToIndex("apl/ch50290.itc", 0x3D)
    LoadChrToIndex("apl/ch50291.itc", 0x3C)
    LoadChrToIndex("apl/ch50292.itc", 0x3E)
    LoadChrToIndex("apl/ch50293.itc", 0x3F)
    SetChrPos(0x10, 7930, 1250, 24860, 270)
    SetChrPos(0x11, 7930, 1250, 24860, 270)
    SetChrPos(0x12, 7930, 1250, 24860, 270)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x34)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x35)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x36)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x37)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x38)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x3A)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x3A)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x39)
    SetChrSubChip(0x13, 0x1)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x39)
    SetChrSubChip(0x14, 0x1)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x39)
    SetChrSubChip(0x15, 0x1)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x39)
    SetChrSubChip(0x16, 0x1)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x13, 0x2)
    SetChrFlags(0x14, 0x2)
    SetChrFlags(0x15, 0x2)
    SetChrFlags(0x16, 0x2)
    SetChrPos(0x13, -5940, 5800, 24600, 180)
    SetChrPos(0x14, 5940, 5800, 24600, 180)
    SetChrPos(0x15, -5680, 7600, 26590, 180)
    SetChrPos(0x16, 5680, 7600, 26590, 180)
    SetChrPos(0xC, 7500, 1500, 25000, 225)
    SetChrPos(0xD, -7500, 1500, 25000, 225)
    SetChrPos(0xE, 7500, 1500, 25000, 135)
    SetChrPos(0xF, -7500, 1500, 25000, 135)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xE, 0x1)
    ClearChrFlags(0xF, 0x1)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, -6450, 1250, 24260, 90)
    SetChrPos(0x9, 6450, 1250, 24260, 90)
    LoadEffect(0x0, "event\\ev290_02.eff")
    LoadEffect(0x1, "event\\ev290_01.eff")
    LoadEffect(0x3, "event\\ev290_00.eff")
    LoadEffect(0x4, "event\\ev295_00.eff")
    LoadEffect(0x5, "event\\ev293_02.eff")
    LoadEffect(0x6, "event\\ev290_05.eff")
    LoadEffect(0x7, "event\\ev294_00.eff")
    SetChrPos(0x101, 10, 1250, 25450, 360)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    ClearMapObjFlags(0x4, 0x4)
    OP_78(0x4, 0x18)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    OP_49()
    SetMapObjFrame(0x3, "04moon_add", 0x0, 0x1)
    SetMapObjFrame(0x3, "02water01", 0x0, 0x1)
    SetMapObjFrame(0x3, "02water02_add", 0x0, 0x1)
    SetMapObjFrame(0x3, "04Aback", 0x0, 0x1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFA2400, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xFA0, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x1)
    LoadChrToIndex("chr/ch05800.itc", 0x3B)
    SetChrChipByIndex(0x1F, 0x1E)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -27000, 15200, 8500, 270)
    SetMapFlags(0x10)
    OP_11(0x0, 0x0, 0x0, 0x17, 0x1E, 0x0)
    SoundLoad(872)
    SoundLoad(874)
    SoundLoad(875)
    SoundLoad(876)
    SoundLoad(880)
    SoundLoad(881)
    OP_E5()
    PlayBGM("ed7506", 1)
    BeginChrThread(0x22, 1, 0, 96)
    BeginChrThread(0x101, 3, 0, 80)
    BeginChrThread(0x101, 2, 0, 78)
    FadeToBright(6000, 0)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    SetChrPos(0x18, 0, 12000, 25000, 0)
    OP_68(10, 5680, 25450, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(15500, 0)
    OP_68(10, 13680, 25450, 12000)
    MoveCamera(0, -1, 0, 12000)
    OP_6E(640, 12000)
    SetCameraDistance(18000, 12000)
    BeginChrThread(0x18, 0, 0, 97)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 4000, 15000, 15, 0, 0, 1100, 1200, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 90, 0, 0, 1500, 1600, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(5000)
    BeginChrThread(0x8, 1, 0, 81)
    BeginChrThread(0x9, 1, 0, 81)
    BeginChrThread(0x101, 0, 0, 82)
    BeginChrThread(0x101, 1, 0, 84)
    WaitChrThread(0x101, 0)
    OP_11(0x0, 0x0, 0x0, 0x1E, 0x32, 0x1388)
    OP_C9(0x0, 0x0, 0xFFF6D840, 0xFFFA2400, 0x0)
    OP_C9(0x0, 0x1, 0xDAC, 0xFA0, 0x0)
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)
    EndChrThread(0x18, 0xFF)
    SetChrPos(0x18, 0, 12000, 25000, 0)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    PlayEffect(0x4, 0xFF, 0x14, 0x40, 0, 800, -300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x13, 0x40, 0, 800, 300, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x15, 0x40, 0, 1000, -350, -90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x15, 0x40, 0, 1000, -350, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x16, 0x40, 0, 1100, -350, -90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x16, 0x40, 0, 1100, -350, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x101, 0, 0, 83)
    BeginChrThread(0x101, 1, 0, 85)
    OP_68(10, 2900, 25450, 12000)
    MoveCamera(0, 30, 0, 12000)
    OP_6E(740, 12000)
    SetCameraDistance(18500, 12000)
    BeginChrThread(0x8, 0, 0, 90)
    BeginChrThread(0x9, 0, 0, 90)
    BeginChrThread(0x18, 1, 0, 90)

    def lambda_8B4E():
        OP_95(0xF, 0, 1500, 28500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_8B4E)
    Sleep(7000)

    def lambda_8B6B():
        OP_95(0xE, 0, 1500, 21500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_8B6B)
    Sleep(1000)

    def lambda_8B88():
        OP_95(0xD, -3500, 1500, 25000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_8B88)
    Sleep(1000)

    def lambda_8BA5():
        OP_95(0xC, 3500, 1500, 25000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_8BA5)
    WaitChrThread(0xE, 0)
    OP_93(0xE, 0x0, 0x1F4)
    WaitChrThread(0x18, 1)
    OP_82(0x0, 0xC8, 0x7D0, 0xC8)
    BeginChrThread(0x8, 0, 0, 93)
    BeginChrThread(0x9, 0, 0, 94)
    Sleep(1200)
    OP_D3(0x18, 0x0, 0xAFC8, 0x0, 0x1388)
    OP_D3(0x18, 0x0, 0x16B48, 0x0, 0x7D0)

    def lambda_8C14():
        OP_96(0xC, 0xDAC, 0x1D4C, 0x61A8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_8C14)

    def lambda_8C2E():
        OP_96(0xD, 0xFFFFF254, 0x1D4C, 0x61A8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_8C2E)

    def lambda_8C48():
        OP_96(0xE, 0x0, 0x1D4C, 0x53FC, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_8C48)

    def lambda_8C62():
        OP_96(0xF, 0x0, 0x1D4C, 0x6F54, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_8C62)

    def lambda_8C7C():

        label("loc_8C7C")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0xDF2, 0x1)
        Yield()
        Jump("loc_8C7C")

    QueueWorkItem2(0xC, 2, lambda_8C7C)

    def lambda_8C9C():

        label("loc_8C9C")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0xDF2, 0x1)
        Yield()
        Jump("loc_8C9C")

    QueueWorkItem2(0xD, 2, lambda_8C9C)

    def lambda_8CBC():

        label("loc_8CBC")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0xDF2, 0x1)
        Yield()
        Jump("loc_8CBC")

    QueueWorkItem2(0xE, 2, lambda_8CBC)

    def lambda_8CDC():

        label("loc_8CDC")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0xDF2, 0x1)
        Yield()
        Jump("loc_8CDC")

    QueueWorkItem2(0xF, 2, lambda_8CDC)
    BeginChrThread(0xC, 1, 0, 79)
    BeginChrThread(0xD, 1, 0, 79)
    BeginChrThread(0xE, 1, 0, 79)
    BeginChrThread(0xF, 1, 0, 79)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xC, 0x1000)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xD, 0x1000)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xE, 0x1000)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0xF, 0x1000)
    SetChrChipByIndex(0xC, 0x3C)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x3D)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x3E)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x3F)
    SetChrSubChip(0xF, 0x0)

    def lambda_8D5C():
        OP_96(0x18, 0x0, 0x2710, 0x61A8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_8D5C)
    BeginChrThread(0x18, 1, 0, 86)
    Sleep(2000)
    OP_68(0, 9500, 22670, 30000)
    SetCameraDistance(18000, 25000)
    BeginChrThread(0x10, 0, 0, 87)
    BeginChrThread(0x11, 0, 0, 88)
    BeginChrThread(0x12, 0, 0, 89)
    Sleep(13000)
    OP_68(0, 12000, 22670, 8000)
    MoveCamera(0, 10, 0, 13000)
    OP_6E(640, 14000)
    SetCameraDistance(13000, 14000)
    Sleep(12000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x101, 0x2)
    OP_68(-27390, 16850, 6230, 0)
    MoveCamera(55, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9500, 0)
    OP_11(0x0, 0x0, 0x0, 0x28, 0x96, 0x0)
    SetChrPos(0x101, -27230, 15100, 7870, 300)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xA, 0x0)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, -26230, 15050, 6870, 300)
    SetChrChipByIndex(0x102, 0x2F)
    SetChrSubChip(0x102, 0x2)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    SetChrPos(0x1F, -26700, 15200, 6600, 0)
    SetChrFlags(0x1F, 0x2)
    SetChrChipByIndex(0x1F, 0x30)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1A, -24860, 15200, 3960, 290)
    SetChrChipByIndex(0x1A, 0x31)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_E6()

    #C0025
    ChrTalk(
        0x102,
        "#0108F#12P#40W……すごい…………\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x1F, 0x1)
    Sleep(1000)
    Fade(500)
    SetChrSubChip(0x1F, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(500)

    #N0026
    NpcTalk(
        0x1F,
        "老人の声",
        "#6P#50Wふふ……大したものだ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x102, 0x0)

    #C0027
    ChrTalk(
        0x102,
        (
            "#0105F#11Pお、おじいさま！\x02\x03",

            "#0102Fよかった……\x01",
            "気付かれたんですね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x1F,
        (
            "#2503F#6P#40Wああ……大した事はない。\x02\x03",

            "#2500F大変なことが起こったが……\x01",
            "今はこのまま舞台を見届けよう……\x02\x03",

            "それがアルカンシェルの諸君に対する\x01",
            "私なりの礼儀だからね……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        "#0106F#11Pおじいさま……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x1A,
        "もったいないお言葉です……\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(10000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sound(881, 0, 100, 0)
    Sleep(1000)
    OP_24(0x370)
    StopBGM(0x1F40)
    WaitBGM()
    EndChrThread(0x22, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_90CF")
    ClearScenarioFlags(0x5B, 0)
    OP_24(0x370)
    OP_B7(0x0)
    Return()

    label("loc_90CF")

    OP_24(0x370)
    SetScenarioFlags(0x5D, 2)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_95_8206 end

    def Function_96_90DF(): pass

    label("Function_96_90DF")

    Sleep(500)
    Sound(875, 0, 100, 0)
    Sleep(500)
    Sound(880, 2, 0, 0)
    Sleep(200)
    OP_25(0x370, 0xA)
    Sleep(200)
    OP_25(0x370, 0x14)
    Sleep(200)
    OP_25(0x370, 0x1E)
    Sleep(200)
    OP_25(0x370, 0x28)
    Sleep(200)
    OP_25(0x370, 0x32)
    Sleep(200)
    OP_25(0x370, 0x3C)
    Sleep(200)
    OP_25(0x370, 0x46)
    Sleep(200)
    OP_25(0x370, 0x50)
    Sleep(200)
    OP_25(0x370, 0x5A)
    Sleep(200)
    OP_25(0x370, 0x64)
    Sleep(8000)
    Sound(874, 0, 100, 0)
    Sleep(1000)
    Sound(875, 0, 100, 0)
    Sleep(7000)
    Sound(874, 0, 100, 0)
    Sleep(1000)
    Sound(875, 0, 100, 0)
    Sleep(12000)
    Sound(876, 0, 100, 0)
    Sleep(8000)
    Sound(874, 0, 100, 0)
    Sleep(1000)
    Sound(875, 0, 100, 0)
    Sleep(19500)
    Sound(881, 0, 100, 0)
    Sleep(4000)
    Sound(876, 0, 100, 0)
    Return()

    # Function_96_90DF end

    def Function_97_9189(): pass

    label("Function_97_9189")

    SetChrPos(0x18, 0, 12000, 25000, 0)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)

    label("loc_91AD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_937F")

    def lambda_91BD():
        OP_96(0xFE, 0xFFFFFA24, 0x2E18, 0x61A8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_91BD)
    OP_D3(0x18, 0x0, 0x0, 0xFFFFF830, 0x3E8)

    def lambda_91EA():
        OP_96(0xFE, 0xFFFFFA24, 0x2E7C, 0x61A8, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_91EA)
    OP_D3(0x18, 0x0, 0x0, 0xFFFFF63C, 0x1F4)

    def lambda_9217():
        OP_96(0xFE, 0xFFFFFA24, 0x2E7C, 0x61A8, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9217)
    OP_D3(0x18, 0x0, 0x0, 0xFFFFF5D8, 0xFA)

    def lambda_9244():
        OP_96(0xFE, 0x0, 0x2E18, 0x61A8, 0xFA, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9244)
    OP_D3(0x18, 0x0, 0x0, 0xFFFFF7CC, 0xFA)

    def lambda_9271():
        OP_96(0xFE, 0x0, 0x2DB4, 0x61A8, 0x15E, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9271)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x2EE)

    def lambda_929E():
        OP_96(0xFE, 0x5DC, 0x2E18, 0x61A8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_929E)
    OP_D3(0x18, 0x0, 0x0, 0x7D0, 0x3E8)

    def lambda_92CB():
        OP_96(0xFE, 0x5DC, 0x2E7C, 0x61A8, 0xAA, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_92CB)
    OP_D3(0x18, 0x0, 0x0, 0x9C4, 0x1F4)

    def lambda_92F8():
        OP_96(0xFE, 0x5DC, 0x2E7C, 0x61A8, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_92F8)
    OP_D3(0x18, 0x0, 0x0, 0x834, 0xFA)

    def lambda_9325():
        OP_96(0xFE, 0x0, 0x2E18, 0x61A8, 0xFA, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9325)
    OP_D3(0x18, 0x0, 0x0, 0x834, 0xFA)

    def lambda_9352():
        OP_96(0xFE, 0x0, 0x2DB4, 0x61A8, 0x15E, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9352)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x2EE)
    Jump("loc_91AD")

    label("loc_937F")

    Return()

    # Function_97_9189 end

    def Function_98_9380(): pass

    label("Function_98_9380")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_994A")
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    BeginChrThread(0x8, 1, 0, 68)
    OP_9D(0x8, 0xFFFFFE0C, 0x2EE0, 0x61A8, 0x7D0, 0x1388)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_9F(0x0, 0x8)
    OP_9F(0x1, -4000, 12000, 23000)
    OP_9F(0x1, -4000, 12000, 27000)
    OP_9F(0x1, -500, 12000, 25000)
    OP_9F(0x2, 0x8, 10000, 0x0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_9E(0x8, 0xFFFFF830, 0x61A8, 0x57E40, 0x2EE0, 0x0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_9F(0x0, 0x8)
    OP_9F(0x1, -3000, 14000, 25000)
    OP_9F(0x1, -3000, 10000, 25000)
    OP_9F(0x1, -500, 12000, 25000)
    OP_9F(0x2, 0x8, 10000, 0x0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_9E(0x8, 0xFFFFF830, 0x61A8, 0x2BF20, 0x2328, 0x0)
    OP_9E(0x8, 0x0, 0x61A8, 0x57E40, 0x1770, 0x0)
    OP_9E(0x8, 0xFFFFEC78, 0x61A8, 0xFFFA81C0, 0x1B58, 0x0)
    OP_9E(0x8, 0xFFFFEC78, 0x61A8, 0xFFFBE150, 0x2328, 0x0)
    OP_96(0x8, 0xFFFFFE0C, 0x2EE0, 0x61A8, 0x2328, 0x0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_9D(0x8, 0xFFFFEC0A, 0x34BC, 0x70E4, 0xBB8, 0xBB8)
    EndChrThread(0x8, 0x3)
    TurnDirection(0x8, 0x9, 0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    Sleep(500)
    SetChrChipByIndex(0x8, 0x1F)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    OP_9E(0x8, 0x0, 0x61A8, 0xABE0, 0x1B58, 0x1)
    Jump("Function_98_9380")

    label("loc_994A")

    Return()

    # Function_98_9380 end

    def Function_99_994B(): pass

    label("Function_99_994B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9AC9")
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    BeginChrThread(0x9, 1, 0, 68)
    OP_9D(0x9, 0x1F4, 0x2EE0, 0x61A8, 0x7D0, 0x1388)
    OP_9F(0x0, 0x9)
    OP_9F(0x1, 4000, 12000, 23000)
    OP_9F(0x1, 4000, 12000, 27000)
    OP_9F(0x1, 500, 12000, 25000)
    OP_9F(0x2, 0x9, 10000, 0x0)
    OP_9E(0x9, 0x7D0, 0x61A8, 0x57E40, 0x2EE0, 0x0)
    OP_9F(0x0, 0x9)
    OP_9F(0x1, 3000, 10000, 25000)
    OP_9F(0x1, 3000, 14000, 25000)
    OP_9F(0x1, 500, 12000, 25000)
    OP_9F(0x2, 0x9, 10000, 0x0)
    OP_9E(0x9, 0x7D0, 0x61A8, 0x2BF20, 0x2328, 0x0)
    OP_9E(0x9, 0x0, 0x61A8, 0x57E40, 0x1770, 0x0)
    OP_9E(0x9, 0x1388, 0x61A8, 0xFFFA81C0, 0x1B58, 0x0)
    OP_9E(0x9, 0x1388, 0x61A8, 0xFFFBE150, 0x2328, 0x0)
    OP_96(0x9, 0x1F4, 0x2EE0, 0x61A8, 0x2328, 0x0)
    OP_9D(0x9, 0x13F6, 0x34BC, 0x70E4, 0xBB8, 0xBB8)
    EndChrThread(0x9, 0x3)
    TurnDirection(0x9, 0x8, 0)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x2)
    Sleep(500)
    SetChrChipByIndex(0x9, 0x29)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    OP_9E(0x9, 0x0, 0x61A8, 0xFFFF5420, 0x1B58, 0x1)
    Jump("Function_99_994B")

    label("loc_9AC9")

    Return()

    # Function_99_994B end

    def Function_100_9ACA(): pass

    label("Function_100_9ACA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50250.itc", 0x1E)
    LoadChrToIndex("apl/ch50251.itc", 0x1F)
    LoadChrToIndex("apl/ch50252.itc", 0x20)
    LoadChrToIndex("apl/ch50253.itc", 0x21)
    LoadChrToIndex("apl/ch50254.itc", 0x22)
    LoadChrToIndex("apl/ch50265.itc", 0x28)
    LoadChrToIndex("apl/ch50266.itc", 0x29)
    LoadChrToIndex("apl/ch50267.itc", 0x2A)
    LoadChrToIndex("apl/ch50268.itc", 0x2B)
    LoadChrToIndex("apl/ch50269.itc", 0x2C)
    LoadChrToIndex("chr/ch27802.itc", 0x33)
    LoadChrToIndex("chr/ch27902.itc", 0x34)
    LoadChrToIndex("chr/ch33002.itc", 0x35)
    LoadChrToIndex("chr/ch33302.itc", 0x36)
    LoadChrToIndex("chr/ch27702.itc", 0x37)
    LoadChrToIndex("chr/ch27602.itc", 0x38)
    LoadChrToIndex("chr/ch33202.itc", 0x39)
    LoadChrToIndex("chr/ch33102.itc", 0x3A)
    SoundLoad(873)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, -5110, 13500, 28900, 90)
    SetChrPos(0x9, 5110, 13500, 28900, 270)
    LoadEffect(0x0, "event\\ev290_01.eff")
    LoadEffect(0x5, "event\\ev293_02.eff")
    LoadEffect(0x7, "event\\ev290_05.eff")
    LoadEffect(0x6, "event\\ev292_04.eff")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFA2400, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xFA0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x1000)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFrame(0x3, "04moon_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "yuka", 0x0, 0x1)
    SetMapObjFrame(0x3, "ball", 0x0, 0x1)
    SetMapObjFrame(0x3, "04Bback", 0x0, 0x1)
    SetMapObjFrame(0x3, "02water01", 0x0, 0x1)
    SetMapObjFrame(0x3, "02water02_add", 0x0, 0x1)
    SetMapObjFlags(0x4, 0x1000)
    ClearMapObjFlags(0x4, 0x4)
    OP_78(0x4, 0x18)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    OP_49()
    SetChrPos(0x18, 0, 17500, 25000, 0)
    SetMapFlags(0x10)
    OP_11(0x0, 0x0, 0x0, 0x1A, 0x64, 0x0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 6500, 25000, 15, 0, 0, 1100, 1400, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 6500, 15000, 15, 0, 0, 1100, 1400, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 90, 0, 0, 1500, 1600, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, 20000, 25000, 90, 180, 0, 1500, 1600, 1500, 0xFF, 0, 0, 0, 0)
    OP_68(0, 8300, 22670, 0)
    MoveCamera(0, -5, 30, 0)
    OP_6E(540, 0)
    SetCameraDistance(22000, 0)
    OP_68(0, 14100, 22670, 14000)
    MoveCamera(0, -12, 20, 18000)
    OP_6E(540, 14000)
    SetCameraDistance(17000, 18000)
    BeginChrThread(0x101, 0, 0, 99)
    BeginChrThread(0x101, 1, 0, 98)
    PlayBGM("ed7504", 1)
    BeginChrThread(0x22, 1, 0, 101)
    FadeToBright(5000, 0)
    OP_0D()
    Sleep(4000)
    SetChrChipByIndex(0xC, 0x33)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -6740, 15250, -5800, 6)
    SetChrChipByIndex(0xD, 0x34)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -7950, 15250, -3430, 18)
    SetChrChipByIndex(0xE, 0x35)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -5820, 15250, -5920, 8)
    SetChrChipByIndex(0xF, 0x36)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -3960, 15250, -3940, 8)
    SetChrChipByIndex(0x10, 0x37)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -2930, 15250, -4190, 8)
    SetChrChipByIndex(0x11, 0x38)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -2140, 15250, -4280, 8)
    SetChrChipByIndex(0x12, 0x39)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 2140, 15250, -4280, 6)
    SetChrChipByIndex(0x13, 0x3A)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 2930, 15250, -4190, 6)
    SetChrChipByIndex(0x14, 0x33)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 6870, 15250, -3670, 348)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 7840, 15250, -3470, 348)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    OP_11(0x0, 0x0, 0x0, 0x32, 0x78, 0x0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    LoadChrToIndex("chr/ch00900.itc", 0x32)
    SetChrChipByIndex(0x1C, 0x32)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -50, 15200, -6400, 0)
    SetChrPos(0x101, 13000, 15200, -8300, 0)
    SetChrPos(0x102, 13000, 15200, -8700, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    BeginChrThread(0x18, 2, 0, 120)
    OP_68(-290, 11930, 27720, 0)
    MoveCamera(347, 9, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(52500, 0)
    SetCameraDistance(57500, 3500)
    Fade(500)
    Sleep(1000)

    def lambda_A13C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A13C)

    def lambda_A14D():
        OP_95(0xFE, -13000, 15200, -8300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A14D)
    Sleep(500)
    MoveCamera(8, 9, 4, 6000)

    def lambda_A175():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A175)

    def lambda_A186():
        OP_95(0xFE, -13000, 15200, -8700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_A186)
    Sleep(2000)
    OP_63(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_A1BE():

        label("loc_A1BE")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_A1BE")

    QueueWorkItem2(0x1C, 0, lambda_A1BE)
    Sleep(1000)

    #C0031
    ChrTalk(
        0x1C,
        "#0605F#11P#10Aな……！？\x02",
    )
    #Auto

    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x22, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1F8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x369)
    SetScenarioFlags(0x5E, 0)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_100_9ACA end

    def Function_101_A21B(): pass

    label("Function_101_A21B")

    Sleep(500)
    Sound(873, 2, 100, 0)
    Sleep(2000)
    Sound(872, 0, 100, 0)
    Sleep(4500)
    Sound(874, 0, 100, 0)
    Sleep(8000)
    OP_25(0x369, 0x5A)
    Sleep(100)
    OP_25(0x369, 0x50)
    Sleep(100)
    OP_25(0x369, 0x46)
    Sleep(100)
    OP_25(0x369, 0x3C)
    Sleep(100)
    OP_25(0x369, 0x32)
    Sleep(100)
    OP_25(0x369, 0x28)
    Sleep(100)
    OP_25(0x369, 0x1E)
    Sleep(100)
    OP_25(0x369, 0x14)
    Sleep(100)
    OP_25(0x369, 0xA)
    Sleep(100)
    OP_24(0x369)
    Return()

    # Function_101_A21B end

    def Function_102_A27C(): pass

    label("Function_102_A27C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30500.itc", 0x1E)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    LoadChrToIndex("chr/ch30200.itc", 0x20)
    LoadChrToIndex("chr/ch30300.itc", 0x21)
    LoadChrToIndex("chr/ch27802.itc", 0x33)
    LoadChrToIndex("chr/ch27902.itc", 0x34)
    LoadChrToIndex("chr/ch33002.itc", 0x35)
    LoadChrToIndex("chr/ch33302.itc", 0x36)
    LoadChrToIndex("chr/ch27702.itc", 0x37)
    LoadChrToIndex("chr/ch27602.itc", 0x38)
    LoadChrToIndex("chr/ch33202.itc", 0x39)
    LoadChrToIndex("chr/ch33102.itc", 0x3A)
    SoundLoad(869)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1B, -7310, 0, 18690, 156)
    SetChrPos(0x1D, -6330, 2700, 910, 21)
    SetChrPos(0x1E, 2650, 2700, 150, 336)
    SetChrPos(0x1C, 10390, 15200, -1250, 333)
    SetChrChipByIndex(0xC, 0x33)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -6740, 15250, -5800, 6)
    SetChrChipByIndex(0xD, 0x34)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -7950, 15250, -3430, 18)
    SetChrChipByIndex(0xE, 0x35)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -5820, 15250, -5920, 8)
    SetChrChipByIndex(0xF, 0x36)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -3960, 15250, -3940, 8)
    SetChrChipByIndex(0x10, 0x37)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -2930, 15250, -4190, 8)
    SetChrChipByIndex(0x11, 0x38)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -2140, 15250, -4280, 8)
    SetChrChipByIndex(0x12, 0x39)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 2140, 15250, -4280, 6)
    SetChrChipByIndex(0x13, 0x3A)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 2930, 15250, -4190, 6)
    SetChrChipByIndex(0x14, 0x33)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 6870, 15250, -3670, 348)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 7840, 15250, -3470, 348)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    OP_68(-5940, 2550, 10180, 0)
    MoveCamera(21, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22000, 0)
    OP_68(830, 4340, 340, 8000)
    MoveCamera(345, 19, 0, 8000)
    OP_6E(510, 8000)
    SetCameraDistance(22000, 8000)
    BeginChrThread(0x22, 0, 0, 103)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    EndChrThread(0x22, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(7600, 14840, -2520, 0)
    MoveCamera(4, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    OP_68(9650, 16290, -2200, 8000)
    MoveCamera(18, 21, 0, 8000)
    OP_6E(500, 8000)
    SetCameraDistance(20500, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3000)
    BeginChrThread(0x22, 0, 0, 104)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x22, 0)
    OP_24(0x365)
    SetScenarioFlags(0x5C, 2)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_102_A27C end

    def Function_103_A672(): pass

    label("Function_103_A672")

    Sound(869, 2, 0, 0)
    Sleep(100)
    OP_25(0x365, 0xA)
    Sleep(100)
    OP_25(0x365, 0x14)
    Sleep(100)
    OP_25(0x365, 0x1E)
    Sleep(100)
    OP_25(0x365, 0x28)
    Sleep(100)
    OP_25(0x365, 0x32)
    Sleep(100)
    OP_25(0x365, 0x3C)
    Sleep(100)
    OP_25(0x365, 0x46)
    Sleep(100)
    OP_25(0x365, 0x50)
    Sleep(100)
    OP_25(0x365, 0x5A)
    Sleep(100)
    OP_25(0x365, 0x64)
    Return()

    # Function_103_A672 end

    def Function_104_A6BF(): pass

    label("Function_104_A6BF")

    OP_25(0x365, 0x5A)
    Sleep(100)
    OP_25(0x365, 0x50)
    Sleep(100)
    OP_25(0x365, 0x46)
    Sleep(100)
    OP_25(0x365, 0x3C)
    Sleep(100)
    OP_25(0x365, 0x32)
    Sleep(100)
    OP_25(0x365, 0x28)
    Sleep(100)
    OP_25(0x365, 0x1E)
    Sleep(100)
    OP_25(0x365, 0x14)
    Sleep(100)
    OP_25(0x365, 0xA)
    Sleep(100)
    OP_24(0x365)
    Return()

    # Function_104_A6BF end

    def Function_105_A702(): pass

    label("Function_105_A702")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A773")
    OP_7D(0xFF, 0xFF, 0xC8, 0x0, 0x64)
    Sleep(200)
    OP_7D(0xC8, 0xC8, 0xC8, 0x0, 0xC8)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A745")
    Sleep(500)
    Jump("loc_A76E")

    label("loc_A745")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A75C")
    Sleep(300)
    Jump("loc_A76E")

    label("loc_A75C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A76E")
    Sleep(100)

    label("loc_A76E")

    Jump("Function_105_A702")

    label("loc_A773")

    Return()

    # Function_105_A702 end

    def Function_106_A774(): pass

    label("Function_106_A774")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    BeginChrThread(0x101, 2, 0, 105)
    LoadChrToIndex("chr/ch30500.itc", 0x1E)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    LoadChrToIndex("chr/ch30200.itc", 0x20)
    LoadChrToIndex("chr/ch30300.itc", 0x21)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1B, -7310, 0, 18690, 156)
    SetChrPos(0x1D, -6330, 2700, 910, 21)
    SetChrPos(0x1E, 2650, 2700, 150, 336)
    SetChrPos(0x1C, 10390, 15200, -1250, 333)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    OP_68(-14360, 3000, 14280, 0)
    MoveCamera(24, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(22000, 0)
    OP_68(-5170, 3000, 8070, 5000)
    MoveCamera(49, 25, 0, 5000)
    OP_6E(650, 5000)
    SetCameraDistance(22000, 5000)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A94E")
    SetScenarioFlags(0x5C, 4)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_A957")

    label("loc_A94E")

    NewScene("c0410", 101, 0, 0)
    IdleLoop()

    label("loc_A957")

    Return()

    # Function_106_A774 end

    def Function_107_A958(): pass

    label("Function_107_A958")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A9C9")
    OP_7D(0xC8, 0xFF, 0xFF, 0x0, 0x64)
    Sleep(200)
    OP_7D(0xA0, 0xC8, 0xC8, 0x0, 0xC8)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A99B")
    Sleep(500)
    Jump("loc_A9C4")

    label("loc_A99B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9B2")
    Sleep(300)
    Jump("loc_A9C4")

    label("loc_A9B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9C4")
    Sleep(100)

    label("loc_A9C4")

    Jump("Function_107_A958")

    label("loc_A9C9")

    Return()

    # Function_107_A958 end

    def Function_108_A9CA(): pass

    label("Function_108_A9CA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    BeginChrThread(0x101, 2, 0, 107)
    LoadChrToIndex("chr/ch30500.itc", 0x1E)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    LoadChrToIndex("chr/ch30200.itc", 0x20)
    LoadChrToIndex("chr/ch30300.itc", 0x21)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1B, -7310, 0, 18690, 156)
    SetChrPos(0x1D, -6330, 2700, 910, 21)
    SetChrPos(0x1E, 2650, 2700, 150, 336)
    SetChrPos(0x1C, 10390, 15200, -1250, 333)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    LoadEffect(0x6, "event\\ev291_00.eff")
    LoadEffect(0x4, "event\\ev291_01.eff")
    LoadEffect(0x5, "event\\ev292_00.eff")
    LoadEffect(0x7, "event\\ev291_05.eff")
    SetMapObjFrame(0xFF, "yuka", 0x0, 0x1)
    BeginChrThread(0x101, 2, 0, 45)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 15, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 1000, 15000, 15, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(-260, 3900, 3530, 0)
    MoveCamera(353, 33, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15000, 0)
    OP_68(-260, 3900, 2530, 8000)
    MoveCamera(377, 28, 0, 8000)
    OP_6E(700, 8000)
    SetCameraDistance(15000, 8000)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC78")
    SetScenarioFlags(0x5C, 5)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_AC81")

    label("loc_AC78")

    NewScene("c0410", 101, 0, 0)
    IdleLoop()

    label("loc_AC81")

    Return()

    # Function_108_A9CA end

    def Function_109_AC82(): pass

    label("Function_109_AC82")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ACF3")
    OP_7D(0xC8, 0xFF, 0xC8, 0x0, 0x64)
    Sleep(200)
    OP_7D(0x8C, 0xC8, 0x8C, 0x0, 0xC8)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ACC5")
    Sleep(500)
    Jump("loc_ACEE")

    label("loc_ACC5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ACDC")
    Sleep(300)
    Jump("loc_ACEE")

    label("loc_ACDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ACEE")
    Sleep(100)

    label("loc_ACEE")

    Jump("Function_109_AC82")

    label("loc_ACF3")

    Return()

    # Function_109_AC82 end

    def Function_110_ACF4(): pass

    label("Function_110_ACF4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    BeginChrThread(0x101, 2, 0, 109)
    LoadChrToIndex("chr/ch30500.itc", 0x1E)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    LoadChrToIndex("chr/ch30200.itc", 0x20)
    LoadChrToIndex("chr/ch30300.itc", 0x21)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1B, -7310, 0, 18690, 156)
    SetChrPos(0x1D, -6330, 2700, 910, 21)
    SetChrPos(0x1E, 2650, 2700, 150, 336)
    SetChrPos(0x1C, 10390, 15200, -1250, 333)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    OP_68(-1740, 1780, 22680, 0)
    MoveCamera(38, 20, 0, 0)
    OP_6E(690, 0)
    SetCameraDistance(35500, 0)
    OP_68(-1740, 1780, 22680, 8000)
    MoveCamera(28, 20, 0, 8000)
    OP_6E(690, 8000)
    SetCameraDistance(35500, 8000)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AECE")
    SetScenarioFlags(0x5C, 6)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_AED7")

    label("loc_AECE")

    NewScene("c0410", 101, 0, 0)
    IdleLoop()

    label("loc_AED7")

    Return()

    # Function_110_ACF4 end

    def Function_111_AED8(): pass

    label("Function_111_AED8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch27802.itc", 0x33)
    LoadChrToIndex("chr/ch27902.itc", 0x34)
    LoadChrToIndex("chr/ch33002.itc", 0x35)
    LoadChrToIndex("chr/ch33302.itc", 0x36)
    LoadChrToIndex("chr/ch27702.itc", 0x37)
    LoadChrToIndex("chr/ch27602.itc", 0x38)
    LoadChrToIndex("chr/ch33202.itc", 0x39)
    LoadChrToIndex("chr/ch33102.itc", 0x3A)
    SetChrChipByIndex(0xC, 0x33)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -6740, 15250, -5800, 6)
    SetChrChipByIndex(0xD, 0x34)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -7950, 15250, -3430, 18)
    SetChrChipByIndex(0xE, 0x35)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -5820, 15250, -5920, 8)
    SetChrChipByIndex(0xF, 0x36)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -3960, 15250, -3940, 8)
    SetChrChipByIndex(0x10, 0x37)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -2930, 15250, -4190, 8)
    SetChrChipByIndex(0x11, 0x38)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -2140, 15250, -4280, 8)
    SetChrChipByIndex(0x12, 0x39)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 2140, 15250, -4280, 6)
    SetChrChipByIndex(0x13, 0x3A)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 2930, 15250, -4190, 6)
    SetChrChipByIndex(0x14, 0x33)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 6870, 15250, -3670, 348)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 7840, 15250, -3470, 348)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 860, 15200, -9740, 357)
    SetChrFlags(0x1C, 0x8000)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    OP_7D(0xC8, 0xC8, 0x8C, 0x0, 0x0)
    OP_68(-3760, 16850, -7210, 0)
    MoveCamera(59, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    OP_68(3700, 16850, -6690, 5000)
    MoveCamera(59, 18, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(17500, 5000)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B20E")
    SetScenarioFlags(0x5C, 7)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_B237")

    label("loc_B20E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_B225")
    NewScene("c0410", 106, 0, 0)
    IdleLoop()
    Jump("loc_B237")

    label("loc_B225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_B237")
    NewScene("c0410", 108, 0, 0)
    IdleLoop()

    label("loc_B237")

    Return()

    # Function_111_AED8 end

    def Function_112_B238(): pass

    label("Function_112_B238")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch27802.itc", 0x33)
    LoadChrToIndex("chr/ch27902.itc", 0x34)
    LoadChrToIndex("chr/ch33002.itc", 0x35)
    LoadChrToIndex("chr/ch33302.itc", 0x36)
    LoadChrToIndex("chr/ch27702.itc", 0x37)
    LoadChrToIndex("chr/ch27602.itc", 0x38)
    LoadChrToIndex("chr/ch33202.itc", 0x39)
    LoadChrToIndex("chr/ch33102.itc", 0x3A)
    SetChrChipByIndex(0xC, 0x33)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -6740, 15250, -5800, 6)
    SetChrChipByIndex(0xD, 0x34)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -7950, 15250, -3430, 18)
    SetChrChipByIndex(0xE, 0x35)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -5820, 15250, -5920, 8)
    SetChrChipByIndex(0xF, 0x36)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -3960, 15250, -3940, 8)
    SetChrChipByIndex(0x10, 0x37)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -2930, 15250, -4190, 8)
    SetChrChipByIndex(0x11, 0x38)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -2140, 15250, -4280, 8)
    SetChrChipByIndex(0x12, 0x39)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 2140, 15250, -4280, 6)
    SetChrChipByIndex(0x13, 0x3A)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 2930, 15250, -4190, 6)
    SetChrChipByIndex(0x14, 0x33)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 6870, 15250, -3670, 348)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 7840, 15250, -3470, 348)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 60, 15200, -8580, 360)
    SetChrFlags(0x1C, 0x8000)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    OP_7D(0x8C, 0xC8, 0xFF, 0x0, 0x0)
    OP_68(3520, 17240, -8490, 0)
    MoveCamera(0, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    OP_68(-3560, 17240, -8490, 5000)
    MoveCamera(0, 14, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(20500, 5000)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    OP_93(0x1C, 0x50, 0x1F4)
    Sleep(400)
    OP_93(0x1C, 0x118, 0x1F4)
    OP_93(0x1C, 0x50, 0x1F4)
    Sleep(2000)
    OP_93(0x1C, 0x118, 0x1F4)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B58D")
    SetScenarioFlags(0x5D, 0)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_B5B6")

    label("loc_B58D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_B5A4")
    NewScene("c0410", 106, 0, 0)
    IdleLoop()
    Jump("loc_B5B6")

    label("loc_B5A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_B5B6")
    NewScene("c0410", 108, 0, 0)
    IdleLoop()

    label("loc_B5B6")

    Return()

    # Function_112_B238 end

    def Function_113_B5B7(): pass

    label("Function_113_B5B7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-40, 15800, -7080, 0)
    MoveCamera(48, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    LoadChrToIndex("chr/ch27802.itc", 0x33)
    LoadChrToIndex("chr/ch27902.itc", 0x34)
    LoadChrToIndex("chr/ch33002.itc", 0x35)
    LoadChrToIndex("chr/ch33302.itc", 0x36)
    LoadChrToIndex("chr/ch27702.itc", 0x37)
    LoadChrToIndex("chr/ch27602.itc", 0x38)
    LoadChrToIndex("chr/ch33202.itc", 0x39)
    LoadChrToIndex("chr/ch33102.itc", 0x3A)
    SetChrChipByIndex(0xC, 0x33)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -6740, 15250, -5800, 6)
    SetChrChipByIndex(0xD, 0x34)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -7950, 15250, -3430, 18)
    SetChrChipByIndex(0xE, 0x35)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -5820, 15250, -5920, 8)
    SetChrChipByIndex(0xF, 0x36)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -3960, 15250, -3940, 8)
    SetChrChipByIndex(0x10, 0x37)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -2930, 15250, -4190, 8)
    SetChrChipByIndex(0x11, 0x38)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -2140, 15250, -4280, 8)
    SetChrChipByIndex(0x12, 0x39)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 2140, 15250, -4280, 6)
    SetChrChipByIndex(0x13, 0x3A)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 2930, 15250, -4190, 6)
    SetChrChipByIndex(0x14, 0x33)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 6870, 15250, -3670, 348)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 7840, 15250, -3470, 348)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 1080, 15200, -7180, 358)
    SetChrFlags(0x1C, 0x8000)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    OP_7D(0x8C, 0xC8, 0xC8, 0x0, 0x0)
    OP_68(930, 16850, -7260, 0)
    MoveCamera(28, 12, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)
    OP_68(930, 16850, -7260, 5000)
    MoveCamera(37, 12, 0, 5000)
    OP_6E(380, 5000)
    SetCameraDistance(20500, 5000)
    OP_63(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B92D")
    SetScenarioFlags(0x5D, 1)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_B956")

    label("loc_B92D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_B944")
    NewScene("c0410", 106, 0, 0)
    IdleLoop()
    Jump("loc_B956")

    label("loc_B944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_B956")
    NewScene("c0410", 108, 0, 0)
    IdleLoop()

    label("loc_B956")

    Return()

    # Function_113_B5B7 end

    def Function_114_B957(): pass

    label("Function_114_B957")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05800.itc", 0x1E)
    LoadChrToIndex("chr/ch02300.itc", 0x1F)
    LoadChrToIndex("chr/ch30000.itc", 0x20)
    SetChrChipByIndex(0x1F, 0x1E)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -25480, 15200, 9430, 62)
    SetChrChipByIndex(0x20, 0x1F)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrPos(0x20, -27330, 15200, 9810, 69)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, -24350, 15200, 2810, 1)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xC8, 0xC8, 0x8C, 0x0, 0x0)
    OP_68(-25840, 16850, 6000, 0)
    MoveCamera(100, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_68(-26000, 16850, 8000, 6000)
    MoveCamera(75, 24, 0, 6000)
    OP_6E(500, 6000)
    SetCameraDistance(19500, 6000)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB47")
    SetScenarioFlags(0x5D, 2)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_BB50")

    label("loc_BB47")

    NewScene("c0410", 115, 0, 0)
    IdleLoop()

    label("loc_BB50")

    Return()

    # Function_114_B957 end

    def Function_115_BB51(): pass

    label("Function_115_BB51")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05800.itc", 0x1E)
    LoadChrToIndex("chr/ch02300.itc", 0x1F)
    LoadChrToIndex("chr/ch30000.itc", 0x20)
    SetChrChipByIndex(0x1F, 0x1E)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -25480, 15200, 9430, 62)
    SetChrChipByIndex(0x20, 0x1F)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrPos(0x20, -27330, 15200, 9810, 69)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, -24260, 15200, 4830, 45)
    OP_63(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0x8C, 0xC8, 0xFF, 0x0, 0x0)
    OP_68(-26720, 16850, 8400, 0)
    MoveCamera(68, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_68(-25060, 16850, 5820, 8000)
    MoveCamera(56, 24, 0, 8000)
    OP_6E(500, 8000)
    SetCameraDistance(19500, 8000)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD53")
    SetScenarioFlags(0x5D, 3)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_BD5C")

    label("loc_BD53")

    NewScene("c0410", 115, 0, 0)
    IdleLoop()

    label("loc_BD5C")

    Return()

    # Function_115_BB51 end

    def Function_116_BD5D(): pass

    label("Function_116_BD5D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-25620, 15800, 6780, 0)
    MoveCamera(28, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    LoadChrToIndex("chr/ch05800.itc", 0x1E)
    LoadChrToIndex("chr/ch02300.itc", 0x1F)
    LoadChrToIndex("chr/ch30000.itc", 0x20)
    SetChrChipByIndex(0x1F, 0x1E)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -25480, 15200, 9430, 62)
    SetChrChipByIndex(0x20, 0x1F)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrPos(0x20, -27330, 15200, 9810, 69)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, -21760, 15200, 6080, 45)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_63(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_7D(0x8C, 0xC8, 0xC8, 0x0, 0x0)
    LoadEffect(0x3, "event\\ev292_03.eff")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 90, 0, 0, 1500, 1100, 1500, 0xFF, 0, 0, 0, 0)
    OP_68(-25230, 16850, 7010, 0)
    MoveCamera(57, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_68(-25230, 16850, 7010, 10000)
    MoveCamera(56, 10, 0, 10000)
    OP_6E(500, 10000)
    SetCameraDistance(16500, 10000)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFD9")
    SetScenarioFlags(0x5D, 4)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_BFE2")

    label("loc_BFD9")

    NewScene("c0410", 115, 0, 0)
    IdleLoop()

    label("loc_BFE2")

    Return()

    # Function_116_BD5D end

    def Function_117_BFE3(): pass

    label("Function_117_BFE3")

    SetChrChipByIndex(0xFE, 0x33)
    Sound(808, 0, 100, 0)
    OP_96(0xFE, 0xFFFF95F2, 0x3B60, 0x1662, 0x2710, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    Sound(533, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)

    def lambda_C024():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C024)
    OP_96(0xFE, 0xFFFF95F2, 0x3B60, 0x1A4A, 0x1F40, 0x0)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    PlayEffect(0x5, 0xFF, 0xFE, 0x40, -1300, 2000, 0, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    Sound(511, 0, 100, 0)
    Sound(830, 0, 100, 0)
    Sound(1876, 255, 100, 1)    #voice#Earnest
    BeginChrThread(0x18, 0, 0, 118)
    SetChrFlags(0x20, 0x20)
    SetChrFlags(0x20, 0x1000)

    def lambda_C0AF():
        OP_96(0xFE, 0xFFFF969C, 0x3B60, 0x23A0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_C0AF)
    SetChrChipByIndex(0x20, 0x2F)
    SetChrSubChip(0x20, 0x0)
    OP_96(0xFE, 0xFFFF95F2, 0x3B60, 0x1A4A, 0x1388, 0x0)
    Sound(532, 0, 100, 0)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x32)

    def lambda_C0F3():

        label("loc_C0F3")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_C0F3")

    QueueWorkItem2(0xFE, 2, lambda_C0F3)
    Return()

    # Function_117_BFE3 end

    def Function_118_C101(): pass

    label("Function_118_C101")

    SetChrFlags(0x18, 0x4)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    BeginChrThread(0x18, 3, 0, 18)
    OP_9D(0x18, 0xFFFF8D64, 0x38A4, 0x292C, 0xBB8, 0xBB8)
    Sound(878, 0, 100, 0)
    SetChrFlags(0x18, 0x2)
    SetChrSubChip(0x18, 0x4)
    Return()

    # Function_118_C101 end

    def Function_119_C13D(): pass

    label("Function_119_C13D")

    OP_95(0xFE, -25200, 15200, 6000, 5000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_119_C13D end

    def Function_120_C159(): pass

    label("Function_120_C159")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C1CA")
    OP_7D(0x50, 0xFF, 0xFF, 0x0, 0x64)
    Sleep(200)
    OP_7D(0x50, 0xC8, 0xC8, 0x0, 0xC8)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C19C")
    Sleep(500)
    Jump("loc_C1C5")

    label("loc_C19C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C1B3")
    Sleep(300)
    Jump("loc_C1C5")

    label("loc_C1B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C1C5")
    Sleep(100)

    label("loc_C1C5")

    Jump("Function_120_C159")

    label("loc_C1CA")

    Return()

    # Function_120_C159 end

    def Function_121_C1CB(): pass

    label("Function_121_C1CB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    LoadChrToIndex("chr/ch05800.itc", 0x1F)
    LoadChrToIndex("chr/ch02300.itc", 0x20)
    LoadChrToIndex("apl/ch50241.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    LoadChrToIndex("chr/ch00951.itc", 0x23)
    LoadChrToIndex("apl/ch50223.itc", 0x28)
    LoadChrToIndex("apl/ch50234.itc", 0x29)
    LoadChrToIndex("apl/ch50225.itc", 0x2A)
    LoadChrToIndex("apl/ch50226.itc", 0x2B)
    LoadChrToIndex("apl/ch50240.itc", 0x2C)
    LoadChrToIndex("apl/ch50228.itc", 0x2D)
    LoadChrToIndex("apl/ch50229.itc", 0x2E)
    LoadChrToIndex("apl/ch50230.itc", 0x2F)
    LoadChrToIndex("chr/ch00050.itc", 0x32)
    LoadChrToIndex("chr/ch00051.itc", 0x33)
    LoadChrToIndex("chr/ch00052.itc", 0x34)
    LoadChrToIndex("chr/ch00150.itc", 0x37)
    LoadChrToIndex("chr/ch00156.itc", 0x38)
    BeginChrThread(0x18, 2, 0, 120)
    LoadEffect(0x7, "event\\ev290_05.eff")
    LoadEffect(0x6, "event\\ev292_04.eff")
    LoadEffect(0x5, "event\\eva01_01.eff")
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 90, 0, 0, 1500, 1600, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, 20000, 25000, 90, 180, 0, 1500, 1600, 1500, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x18, 0x2B)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, -27150, 15700, 8660, 225)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrSubChip(0x1C, 0x0)
    SetChrPos(0x1C, -27900, 15200, 2620, 0)
    SetChrFlags(0x1F, 0x2)
    SetChrChipByIndex(0x1F, 0x2A)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -28000, 15200, 8400, 270)
    SetChrChipByIndex(0x20, 0x28)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrPos(0x20, -27000, 15200, 8500, 270)
    SetChrPos(0x101, -26770, 15200, 920, 0)
    SetChrPos(0x102, -25520, 15200, 650, 0)

    def lambda_C417():
        OP_96(0xFE, 0xFFFF976E, 0x3B60, 0xB68, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C417)

    def lambda_C431():
        OP_96(0xFE, 0xFFFF9C50, 0x3B60, 0xA5A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C431)
    OP_68(-26750, 16850, 3330, 0)
    MoveCamera(30, 28, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(19500, 0)
    OP_68(-27740, 16440, 8450, 2000)
    MoveCamera(30, 28, 0, 2000)
    OP_6E(320, 2000)
    SetCameraDistance(23500, 2000)
    FadeToBright(2000, 0)
    Sleep(1000)
    Sleep(400)
    SetChrSubChip(0x20, 0x2)
    Sound(804, 0, 100, 0)
    Sound(540, 0, 80, 0)
    Sleep(500)
    OP_0D()

    #C0032
    ChrTalk(
        0x102,
        "#0110Fっ……！？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x20, 0x3)
    Sleep(300)

    #C0033
    ChrTalk(
        0x20,
        "#2611F#5Pむっ……！？\x02",
    )

    CloseMessageWindow()
    Sound(1091, 255, 100, 0)    #voice#Lloyd
    Sleep(1000)
    Sound(1011, 255, 100, 0)    #voice#Lloyd
    SetCameraDistance(28500, 2000)
    BeginChrThread(0x101, 0, 0, 117)
    WaitChrThread(0x101, 0)
    Sleep(300)

    #C0034
    ChrTalk(
        0x20,
        "#2614Fくっ……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x20, 0xB4, 0x0)
    SetChrPos(0x20, -27250, 15200, 8650, 225)
    Sleep(200)
    Fade(500)
    SetChrPos(0x20, -27500, 15200, 8800, 270)
    SetChrChipByIndex(0x20, 0x20)
    Sound(804, 0, 100, 0)
    OP_93(0x20, 0xB4, 0x0)
    ClearChrFlags(0x1F, 0x2)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    OP_93(0x1F, 0x0, 0x0)
    Sleep(300)
    OP_68(-27030, 16850, 8000, 4000)
    MoveCamera(47, 22, 0, 4000)
    OP_6E(460, 4000)
    SetCameraDistance(20500, 4000)

    def lambda_C5C4():
        OP_9D(0xFE, 0xFFFF9494, 0x3B60, 0x2968, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_C5C4)

    def lambda_C5E1():
        OP_9D(0xFE, 0xFFFF92A0, 0x3B60, 0x27D8, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_C5E1)
    Sound(814, 0, 100, 0)
    BeginChrThread(0x102, 0, 0, 119)
    WaitChrThread(0x20, 0)
    SetChrChipByIndex(0x20, 0x2D)
    SetChrSubChip(0x20, 0x0)
    Sound(531, 0, 100, 0)
    SetChrFlags(0x20, 0x2)
    SetChrChipByIndex(0x1F, 0x2C)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x20)
    SetChrFlags(0x1F, 0x2)

    #C0035
    ChrTalk(
        0x102,
        "#0107Fおじいさま……！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#0007Fくそっ……拳銃#4Rそんなもの#まで！？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    OP_95(0x1C, -28330, 15200, 5500, 5000, 0x0)
    OP_93(0x1C, 0x0, 0x320)
    OP_63(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0037
    ChrTalk(
        0x1C,
        (
            "#0607Fこ、これは……\x01",
            "一体どういうことだ！？\x02",
        )
    )

    CloseMessageWindow()
    MoveCamera(24, 31, 0, 30000)

    #C0038
    ChrTalk(
        0x20,
        (
            "#2613Fクク、まさか君たちが\x01",
            "こんな場所に現れるとは……\x02\x03",

            "#2610Fやれやれ……\x01",
            "とんだ女神の巡り合わせだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#0108Fアーネストさん……\x01",
            "いったいどうして……！\x02\x03",

            "#0107Fあれほど、おじいさまを尊敬して\x01",
            "支えてくれた貴方がどうして……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1899, 255, 100, 0)    #voice#Earnest
    Sleep(1000)

    #C0040
    ChrTalk(
        0x20,
        (
            "#2613F……エリィ、君と同じだよ。\x02\x03",

            "私もいいかげん、この状況には\x01",
            "ウンザリとしていたんだ……\x02\x03",

            "#2611F結局、何かを変えるためには\x01",
            "より強い者に従うしかない……\x02\x03",

            "#2614Fだからこそ私は行動したんだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#0003Fそのために《銀#2Rイン#》の名を騙り\x01",
            "イリアさんに脅迫状を送って……\x02\x03",

            "#0013F《銀》が現れると思い込ませて\x01",
            "市長の抹殺を図ったのか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x1C,
        (
            "#0603F……クッ、そういう事か。\x02\x03",

            "#0610Fずいぶんと舐めた真似を\x01",
            "してくれるじゃないか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x20,
        (
            "#2613Fハハ、捜査一課といっても\x01",
            "所詮は無能な警察官にしかすぎん。\x02\x03",

            "ルバーチェも、黒月も\x01",
            "本物の《銀#2Rイン#》とやらも……\x02\x03",

            "#2610F全員、私の掌の上で\x01",
            "踊っていたにすぎんのだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x1C,
        "#0601Fくっ……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    EndChrThread(0x1C, 0x2)
    SetChrFlags(0x1C, 0x20)
    SetChrFlags(0x1C, 0x2)
    SetChrChipByIndex(0x1C, 0x21)
    SetChrSubChip(0x1C, 0x0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sound(1560, 255, 100, 0)    #voice#Dudley
    Sleep(1000)

    #C0045
    ChrTalk(
        0x1C,
        (
            "#0603F──大人しく\x01",
            "銃を捨ててもらおう。\x02\x03",

            "#0601F今ならまだ、未遂で済む。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x20,
        (
            "#2613F#5Pクク、それはこちらの台詞だ。\x02\x03",

            "#2610F自治州代表の一人でもある\x01",
            "この老いぼれの命……\x02\x03",

            "お前たちの目の前で\x01",
            "散らしてやってもいいんだぞ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        "#0106Fやめてっ……！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x1C,
        "#0610Fチッ……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x20,
        (
            "#2610F#5P実の祖父がくたばる瞬間を\x01",
            "その孫娘に見せたくはあるまい？\x02\x03",

            "そちらの壁際まで移動して\x01",
            "道を空けてもらおうか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#0003F……どうするつもりだ。\x02\x03",

            "#0001Fこの場を逃れたところで\x01",
            "あんたに逃げ場はないぞ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0051
    ChrTalk(
        0x20,
        (
            "#2614F#5P#4Sうるさいっ！\x01",
            "いいから言うとおりにしろ！\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#0013Fくっ……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-27030, 16850, 6000, 4000)

    def lambda_CCF3():

        label("loc_CCF3")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_CCF3")

    QueueWorkItem2(0x101, 2, lambda_CCF3)

    def lambda_CD05():

        label("loc_CD05")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_CD05")

    QueueWorkItem2(0x102, 2, lambda_CD05)

    def lambda_CD17():

        label("loc_CD17")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_CD17")

    QueueWorkItem2(0x1C, 2, lambda_CD17)
    ClearChrFlags(0x1C, 0x20)
    ClearChrFlags(0x1C, 0x2)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrSubChip(0x1C, 0x0)
    Sound(531, 0, 100, 0)

    def lambda_CD41():
        OP_96(0xFE, 0xFFFF9D90, 0x3B60, 0xE74, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_CD41)
    Sleep(500)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0xFF)
    Sound(804, 0, 100, 0)

    def lambda_CD72():
        OP_96(0xFE, 0xFFFF9B9C, 0x3B60, 0x14B4, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CD72)
    Sleep(500)

    def lambda_CD8F():
        OP_96(0xFE, 0xFFFFA04C, 0x3B60, 0x16A8, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CD8F)
    WaitChrThread(0x1C, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7505", 0)

    #C0053
    ChrTalk(
        0x20,
        "#2613F#5P#N……いいだろう。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x1F, 0x20)
    SetChrFlags(0x1F, 0x1000)

    def lambda_CDE0():

        label("loc_CDE0")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_CDE0")

    QueueWorkItem2(0x20, 1, lambda_CDE0)

    def lambda_CDF2():
        OP_97(0x20, 0x0, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_CDF2)

    def lambda_CE0C():
        OP_98(0x1F, 0x0, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_CE0C)
    WaitChrThread(0x20, 0)
    EndChrThread(0x20, 0x1)
    TurnDirection(0x20, 0x101, 500)

    #C0054
    ChrTalk(
        0x20,
        "#2614F#5Pそれでは返してやる！\x02",
    )

    CloseMessageWindow()
    OP_68(-26670, 16850, 3880, 1000)
    MoveCamera(68, 27, 0, 1000)
    OP_6E(500, 1000)
    SetCameraDistance(19500, 1000)
    EndChrThread(0x101, 0xFF)
    SetChrSubChip(0x1F, 0x1)
    Sound(804, 0, 100, 0)
    OP_96(0x1F, 0xFFFF998A, 0x3B60, 0x16BC, 0x1F40, 0x0)

    def lambda_CEA8():
        OP_96(0x1F, 0xFFFF9B9C, 0x3B60, 0x15E0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_CEA8)
    BeginChrThread(0x1F, 3, 0, 122)
    ClearChrFlags(0x20, 0x2)
    ClearChrFlags(0x20, 0x20)
    ClearChrFlags(0x20, 0x1000)
    SetChrChipByIndex(0x20, 0x2E)
    Sound(1904, 255, 100, 0)    #voice#Earnest

    def lambda_CEE1():
        OP_95(0x20, -26690, 15200, 2410, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_CEE1)
    Sound(819, 0, 100, 0)
    OP_96(0x101, 0xFFFF9C00, 0x3B60, 0x1388, 0xFA0, 0x0)
    WaitChrThread(0x20, 0)

    def lambda_CF19():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_CF19)

    def lambda_CF2A():
        OP_95(0xFE, -26690, 15200, 1000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_CF2A)
    WaitChrThread(0x20, 0)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x1C, 0xFF)
    OP_95(0x102, -25230, 15200, 5870, 3000, 0x0)
    Fade(500)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, -25230, 15100, 5870, 300)
    SetChrFlags(0x1F, 0x2)
    SetChrChipByIndex(0x1F, 0x29)
    SetChrSubChip(0x1F, 0x0)
    Sound(820, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x38)
    SetChrSubChip(0x102, 0x0)

    #C0055
    ChrTalk(
        0x102,
        "#0107F#11Pおじいさま……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x20, 700)

    #C0056
    ChrTalk(
        0x101,
        "#0007F#5P待て……！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0x32)
    Sound(808, 0, 100, 0)
    OP_95(0x101, -26690, 15200, 2410, 6000, 0x0)

    def lambda_D002():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D002)

    def lambda_D013():
        OP_95(0xFE, -26690, 15200, 1000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D013)

    #C0057
    ChrTalk(
        0x1C,
        "#0607F#5P逃がすか……！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x1C, 0x23)
    Sound(531, 0, 100, 0)
    OP_95(0x1C, -26690, 15200, 2410, 6000, 0x0)

    def lambda_D068():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_D068)

    def lambda_D079():
        OP_95(0xFE, -26690, 15200, 1000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_D079)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1F9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5E, 1)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_121_C1CB end

    def Function_122_D0AF(): pass

    label("Function_122_D0AF")

    WaitChrThread(0xFE, 0)
    SetChrSubChip(0x1F, 0x2)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    Return()

    # Function_122_D0AF end

    def Function_123_D0C9(): pass

    label("Function_123_D0C9")

    OP_93(0x8, 0x87, 0x0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    SetChrPos(0x8, -500, 5500, 25000, 135)

    def lambda_D0EE():

        label("loc_D0EE")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0x320, 0x3)
        Yield()
        Jump("loc_D0EE")

    QueueWorkItem2(0x8, 2, lambda_D0EE)
    Sleep(1)
    OP_96(0x8, 0xFFFFFE0C, 0x2BC0, 0x61A8, 0x12C, 0x0)
    EndChrThread(0x8, 0x2)
    BeginChrThread(0x8, 2, 0, 7)
    ClearChrFlags(0x8, 0x1)
    OP_9D(0x8, 0xFFFFFE0C, 0x300C, 0x61A8, 0x7D0, 0x7D0)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x24)

    label("loc_D14F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D16D")
    OP_A1(0x8, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("loc_D14F")

    label("loc_D16D")

    Return()

    # Function_123_D0C9 end

    def Function_124_D16E(): pass

    label("Function_124_D16E")

    OP_93(0x9, 0xE1, 0x0)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x2)
    SetChrPos(0x9, 500, 5500, 25000, 225)

    def lambda_D193():

        label("loc_D193")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0x320, 0x3)
        Yield()
        Jump("loc_D193")

    QueueWorkItem2(0x9, 2, lambda_D193)
    Sleep(1)
    OP_96(0x9, 0x1F4, 0x2BC0, 0x61A8, 0x12C, 0x0)
    EndChrThread(0x9, 0x2)
    BeginChrThread(0x9, 2, 0, 15)
    ClearChrFlags(0x9, 0x1)
    OP_9D(0x9, 0x1F4, 0x2EE0, 0x61A8, 0x7D0, 0x7D0)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x2E)
    SetChrSubChip(0x9, 0x6)

    label("loc_D1F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D216")
    OP_A1(0x9, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("loc_D1F8")

    label("loc_D216")

    Return()

    # Function_124_D16E end

    def Function_125_D217(): pass

    label("Function_125_D217")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_F8(0x14D)
    LoadChrToIndex("chr/ch00002.itc", 0x25)
    LoadChrToIndex("chr/ch07502.itc", 0x26)
    LoadChrToIndex("chr/ch21802.itc", 0x33)
    LoadChrToIndex("chr/ch21902.itc", 0x34)
    LoadChrToIndex("chr/ch22002.itc", 0x35)
    LoadChrToIndex("chr/ch22302.itc", 0x36)
    LoadChrToIndex("chr/ch22102.itc", 0x37)
    LoadChrToIndex("chr/ch33202.itc", 0x38)
    LoadChrToIndex("chr/ch27702.itc", 0x39)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 7850, 15250, -3320, 345)
    SetChrChipByIndex(0x21, 0x26)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrPos(0x21, 7000, 15250, -3560, 345)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0xC, 0x33)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 6400, 15250, -5600, 345)
    SetChrChipByIndex(0xD, 0x38)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 4800, 15250, -5840, 345)
    SetChrChipByIndex(0xE, 0x34)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 5600, 15250, -5720, 345)
    SetChrChipByIndex(0xF, 0x35)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 3600, 15250, -4000, 355)
    SetChrChipByIndex(0x10, 0x36)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 2700, 15250, -4090, 355)
    SetChrChipByIndex(0x11, 0x37)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 1900, 15250, -4180, 355)
    SetChrChipByIndex(0x12, 0x39)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 8700, 15250, -3080, 345)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    LoadEffect(0x0, "event\\ev290_02.eff")
    LoadEffect(0x1, "event\\ev290_01.eff")
    LoadEffect(0x3, "event\\ev290_00.eff")
    LoadEffect(0x4, "event\\ev295_00.eff")
    LoadEffect(0x5, "event\\ev293_02.eff")
    LoadEffect(0x6, "event\\ev290_05.eff")
    LoadEffect(0x7, "event\\ev294_00.eff")
    SetMapObjFrame(0x3, "04moon_add", 0x0, 0x1)
    SetMapObjFrame(0x3, "02water01", 0x0, 0x1)
    SetMapObjFrame(0x3, "02water02_add", 0x0, 0x1)
    SetMapObjFrame(0x3, "04Aback", 0x0, 0x1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFA2400, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xFA0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    ClearMapObjFlags(0x4, 0x4)
    OP_78(0x4, 0x18)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    OP_49()
    LoadChrToIndex("apl/ch50250.itc", 0x1E)
    LoadChrToIndex("apl/ch50251.itc", 0x1F)
    LoadChrToIndex("apl/ch50252.itc", 0x20)
    LoadChrToIndex("apl/ch50253.itc", 0x21)
    LoadChrToIndex("apl/ch50254.itc", 0x22)
    LoadChrToIndex("apl/ch50255.itc", 0x23)
    LoadChrToIndex("apl/ch50256.itc", 0x24)
    LoadChrToIndex("apl/ch50265.itc", 0x28)
    LoadChrToIndex("apl/ch50266.itc", 0x29)
    LoadChrToIndex("apl/ch50267.itc", 0x2A)
    LoadChrToIndex("apl/ch50268.itc", 0x2B)
    LoadChrToIndex("apl/ch50269.itc", 0x2C)
    LoadChrToIndex("apl/ch50270.itc", 0x2D)
    LoadChrToIndex("apl/ch50271.itc", 0x2E)
    LoadChrToIndex("apl/ch50289.itc", 0x2F)
    SoundLoad(880)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x2F)
    SetChrSubChip(0x13, 0x1)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x2F)
    SetChrSubChip(0x14, 0x1)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x1)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x2F)
    SetChrSubChip(0x16, 0x1)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x13, 0x2)
    SetChrFlags(0x14, 0x2)
    SetChrFlags(0x15, 0x2)
    SetChrFlags(0x16, 0x2)
    SetChrPos(0x13, -5940, 5800, 24600, 180)
    SetChrPos(0x14, 5940, 5800, 24600, 180)
    SetChrPos(0x15, -5680, 7600, 26590, 180)
    SetChrPos(0x16, 5680, 7600, 26590, 180)
    PlayEffect(0x4, 0xFF, 0x14, 0x40, 0, 800, -300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x13, 0x40, 0, 800, 300, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x15, 0x40, 0, 1000, -350, -90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x15, 0x40, 0, 1000, -350, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x16, 0x40, 0, 1100, -350, -90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x16, 0x40, 0, 1100, -350, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, -6450, 1250, 24260, 90)
    SetChrPos(0x9, 6450, 1250, 24260, 90)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x1)
    BeginChrThread(0x101, 3, 0, 80)
    BeginChrThread(0x101, 2, 0, 78)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    SetChrPos(0x18, 0, 12000, 25000, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 90, 0, 0, 1500, 1600, 1500, 0xFF, 0, 0, 0, 0)
    OP_C9(0x0, 0x0, 0xFFF6D840, 0xFFFA2400, 0x0)
    OP_C9(0x0, 0x1, 0xDAC, 0xFA0, 0x0)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    OP_E5()
    SetMapObjFlags(0x5, 0x1000)
    ClearMapObjFlags(0x5, 0x4)
    OP_78(0x5, 0x19)
    SetChrPos(0x19, 0, 18000, 24000, 0)
    OP_D3(0x19, 0x0, 0x0, 0x0, 0x0)
    OP_49()
    SetChrPos(0x8, -500, 5100, 25000, 0)
    SetChrPos(0x9, 500, 5100, 25000, 0)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x18, 0, 4000, 25000, 0)
    BeginChrThread(0x8, 0, 0, 123)
    BeginChrThread(0x9, 0, 0, 124)

    def lambda_D958():
        OP_96(0x18, 0x0, 0x2710, 0x61A8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_D958)
    BeginChrThread(0x18, 1, 0, 86)
    OP_EE(0x0, 0x5)
    PlayBGM("ed7532", 0)
    FadeToBright(1000, 0)
    BeginChrThread(0x22, 1, 0, 126)
    OP_68(7870, 17900, -3420, 0)
    MoveCamera(102, 7, 0, 0)
    OP_6E(1180, 0)
    SetCameraDistance(7000, 0)
    OP_68(7870, 17010, -3420, 5000)
    MoveCamera(102, 23, 0, 5000)
    OP_6E(1180, 5000)
    SetCameraDistance(7000, 5000)
    Sleep(3000)
    Fade(1500)
    OP_68(10, 8620, 25430, 0)
    MoveCamera(350, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(40140, 0)
    OP_68(10, 10610, 25430, 15000)
    MoveCamera(350, 13, 0, 15000)
    OP_6E(380, 10000)
    SetCameraDistance(52000, 10000)
    Sleep(16000)

    def lambda_DA52():
        OP_96(0x19, 0x0, 0x546, 0x5DC0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_DA52)
    Sleep(5000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    StopBGM(0x1770)
    WaitBGM()
    OP_EE(0x0, 0xA)
    OP_E6()
    OP_24(0x370)
    SetScenarioFlags(0x5C, 1)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_125_D217 end

    def Function_126_DA9D(): pass

    label("Function_126_DA9D")

    Sleep(1500)
    Sound(880, 2, 0, 0)
    Sleep(50)
    OP_25(0x370, 0xA)
    Sleep(50)
    OP_25(0x370, 0x14)
    Sleep(50)
    OP_25(0x370, 0x1E)
    Sleep(50)
    OP_25(0x370, 0x28)
    Sleep(50)
    OP_25(0x370, 0x32)
    Sleep(50)
    OP_25(0x370, 0x3C)
    Sleep(50)
    OP_25(0x370, 0x46)
    Sleep(50)
    OP_25(0x370, 0x50)
    Sleep(50)
    OP_25(0x370, 0x5A)
    Sleep(50)
    OP_25(0x370, 0x64)
    Sleep(17500)
    Sound(876, 0, 100, 0)
    Sleep(3000)
    Sound(875, 0, 100, 0)
    Sleep(2000)
    OP_25(0x370, 0x64)
    Sleep(50)
    OP_25(0x370, 0x5A)
    Sleep(50)
    OP_25(0x370, 0x50)
    Sleep(50)
    OP_25(0x370, 0x46)
    Sleep(50)
    OP_25(0x370, 0x3C)
    Sleep(50)
    OP_25(0x370, 0x32)
    Sleep(50)
    OP_25(0x370, 0x28)
    Sleep(50)
    OP_25(0x370, 0x1E)
    Sleep(50)
    OP_25(0x370, 0x14)
    Sleep(50)
    OP_25(0x370, 0xA)
    Sleep(50)
    OP_24(0x370)
    Return()

    # Function_126_DA9D end

    SaveToFile()

Try(main)
