from ZeroScenarioHelper import *

def main():
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
        "太阳之姬",               # 1
        "月之姬",                 # 2
        "映射太阳",               # 3
        "映射月亮",               # 4
        "星之守护战士",           # 5
        "放荡的王子",             # 6
        "女祭司长",               # 7
        "女占卜师",               # 8
        "流民少年",               # 9
        "乐的侍女",               # 10
        "乐的侍女",               # 11
        "乐的士兵",               # 12
        "乐的士兵",               # 13
        "乐的士兵",               # 14
        "乐的士兵",               # 15
        "映射守护战士",           # 16
        "Objects用",              # 17
        "Objects用",              # 18
        "巴尔萨摩经理",           # 19
        "艾玛搜查官",             # 20
        "达德利搜查官",           # 21
        "一科搜查官",             # 22
        "一科搜查官",             # 23
        "麦克道尔市长",           # 24
        "阿奈斯特秘书",           # 25
        "塞茜尔",                 # 26
        "SE控制",                 # 27
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
        "Function_3_875",          # 03, 3
        "Function_4_899",          # 04, 4
        "Function_5_93E",          # 05, 5
        "Function_6_9C8",          # 06, 6
        "Function_7_9F5",          # 07, 7
        "Function_8_A22",          # 08, 8
        "Function_9_A39",          # 09, 9
        "Function_10_A50",         # 0A, 10
        "Function_11_A59",         # 0B, 11
        "Function_12_A62",         # 0C, 12
        "Function_13_A6B",         # 0D, 13
        "Function_14_A74",         # 0E, 14
        "Function_15_AA1",         # 0F, 15
        "Function_16_ACE",         # 10, 16
        "Function_17_AE5",         # 11, 17
        "Function_18_AFC",         # 12, 18
        "Function_19_B1B",         # 13, 19
        "Function_20_B3A",         # 14, 20
        "Function_21_B59",         # 15, 21
        "Function_22_B78",         # 16, 22
        "Function_23_C3A",         # 17, 23
        "Function_24_D1C",         # 18, 24
        "Function_25_E81",         # 19, 25
        "Function_26_1492",        # 1A, 26
        "Function_27_18EF",        # 1B, 27
        "Function_28_193A",        # 1C, 28
        "Function_29_19BC",        # 1D, 29
        "Function_30_1A3E",        # 1E, 30
        "Function_31_1A8F",        # 1F, 31
        "Function_32_1AE0",        # 20, 32
        "Function_33_1B31",        # 21, 33
        "Function_34_1B9C",        # 22, 34
        "Function_35_1BE5",        # 23, 35
        "Function_36_1C2E",        # 24, 36
        "Function_37_1C83",        # 25, 37
        "Function_38_25C2",        # 26, 38
        "Function_39_25F6",        # 27, 39
        "Function_40_289F",        # 28, 40
        "Function_41_2A5C",        # 29, 41
        "Function_42_2D72",        # 2A, 42
        "Function_43_2DBD",        # 2B, 43
        "Function_44_2E8D",        # 2C, 44
        "Function_45_3059",        # 2D, 45
        "Function_46_330A",        # 2E, 46
        "Function_47_3343",        # 2F, 47
        "Function_48_337C",        # 30, 48
        "Function_49_3AEC",        # 31, 49
        "Function_50_3B23",        # 32, 50
        "Function_51_3BAD",        # 33, 51
        "Function_52_3DA8",        # 34, 52
        "Function_53_4063",        # 35, 53
        "Function_54_419A",        # 36, 54
        "Function_55_441A",        # 37, 55
        "Function_56_4663",        # 38, 56
        "Function_57_4914",        # 39, 57
        "Function_58_49AD",        # 3A, 58
        "Function_59_4A46",        # 3B, 59
        "Function_60_4A91",        # 3C, 60
        "Function_61_5100",        # 3D, 61
        "Function_62_512B",        # 3E, 62
        "Function_63_5289",        # 3F, 63
        "Function_64_53E7",        # 40, 64
        "Function_65_54B7",        # 41, 65
        "Function_66_5587",        # 42, 66
        "Function_67_5657",        # 43, 67
        "Function_68_5727",        # 44, 68
        "Function_69_5772",        # 45, 69
        "Function_70_57F7",        # 46, 70
        "Function_71_58C0",        # 47, 71
        "Function_72_5B20",        # 48, 72
        "Function_73_5D98",        # 49, 73
        "Function_74_6413",        # 4A, 74
        "Function_75_67D2",        # 4B, 75
        "Function_76_67FB",        # 4C, 76
        "Function_77_7665",        # 4D, 77
        "Function_78_76BA",        # 4E, 78
        "Function_79_76CE",        # 4F, 79
        "Function_80_7719",        # 50, 80
        "Function_81_7809",        # 51, 81
        "Function_82_7854",        # 52, 82
        "Function_83_7A79",        # 53, 83
        "Function_84_7A93",        # 54, 84
        "Function_85_7CB4",        # 55, 85
        "Function_86_7CCE",        # 56, 86
        "Function_87_7D05",        # 57, 87
        "Function_88_7E32",        # 58, 88
        "Function_89_7E85",        # 59, 89
        "Function_90_7ED8",        # 5A, 90
        "Function_91_7F79",        # 5B, 91
        "Function_92_7F98",        # 5C, 92
        "Function_93_7FB7",        # 5D, 93
        "Function_94_8091",        # 5E, 94
        "Function_95_816F",        # 5F, 95
        "Function_96_902E",        # 60, 96
        "Function_97_90D8",        # 61, 97
        "Function_98_92CF",        # 62, 98
        "Function_99_989A",        # 63, 99
        "Function_100_9A19",       # 64, 100
        "Function_101_A16C",       # 65, 101
        "Function_102_A1CD",       # 66, 102
        "Function_103_A5C3",       # 67, 103
        "Function_104_A610",       # 68, 104
        "Function_105_A653",       # 69, 105
        "Function_106_A6C5",       # 6A, 106
        "Function_107_A8A9",       # 6B, 107
        "Function_108_A91B",       # 6C, 108
        "Function_109_ABD3",       # 6D, 109
        "Function_110_AC45",       # 6E, 110
        "Function_111_AE29",       # 6F, 111
        "Function_112_B189",       # 70, 112
        "Function_113_B508",       # 71, 113
        "Function_114_B8A8",       # 72, 114
        "Function_115_BAA2",       # 73, 115
        "Function_116_BCAE",       # 74, 116
        "Function_117_BF34",       # 75, 117
        "Function_118_C052",       # 76, 118
        "Function_119_C08E",       # 77, 119
        "Function_120_C0AA",       # 78, 120
        "Function_121_C11C",       # 79, 121
        "Function_122_CF74",       # 7A, 122
        "Function_123_CF8E",       # 7B, 123
        "Function_124_D033",       # 7C, 124
        "Function_125_D0DC",       # 7D, 125
        "Function_126_D962",       # 7E, 126
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
            "第一幕\x01",                # 0
            "第二幕\x01",                # 1
            "第三幕\x01",                # 2
            "第四幕\x01",                # 3
            "终幕\x01",                  # 4
            "第四幕中场（假）\x01",      # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_803"),
        (1, "loc_814"),
        (2, "loc_825"),
        (3, "loc_836"),
        (4, "loc_847"),
        (5, "loc_858"),
        (SWITCH_DEFAULT, "loc_869"),
    )


    label("loc_803")

    SetScenarioFlags(0x5C, 2)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_869")

    label("loc_814")

    SetScenarioFlags(0x5D, 4)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_869")

    label("loc_825")

    SetScenarioFlags(0x5D, 5)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_869")

    label("loc_836")

    SetScenarioFlags(0x5D, 6)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_869")

    label("loc_847")

    SetScenarioFlags(0x5E, 1)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_869")

    label("loc_858")

    SetScenarioFlags(0x5D, 7)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_869")

    label("loc_869")

    FadeToDark(300, 0, -1)
    OP_0D()
    Return()

    # Function_2_77A end

    def Function_3_875(): pass

    label("Function_3_875")

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

    # Function_3_875 end

    def Function_4_899(): pass

    label("Function_4_899")

    ClearChrFlags(0xFE, 0x1)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    OP_A7(0xFE, 0x0, 0x0, 0x0, 0x80, 0x0)
    OP_D3(0xFE, 0x41EB0, 0x4CE78, 0x0, 0x0)

    label("loc_8CB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_93D")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_8CB")

    label("loc_93D")

    Return()

    # Function_4_899 end

    def Function_5_93E(): pass

    label("Function_5_93E")

    ClearChrFlags(0xFE, 0x1)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    OP_A7(0xFE, 0x0, 0x0, 0x0, 0x80, 0x0)
    OP_D3(0xFE, 0x41EB0, 0x57E40, 0x0, 0x0)

    label("loc_970")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9C7")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IDIV), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_970")

    label("loc_9C7")

    Return()

    # Function_5_93E end

    def Function_6_9C8(): pass

    label("Function_6_9C8")

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

    # Function_6_9C8 end

    def Function_7_9F5(): pass

    label("Function_7_9F5")

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

    # Function_7_9F5 end

    def Function_8_A22(): pass

    label("Function_8_A22")

    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_8_A22 end

    def Function_9_A39(): pass

    label("Function_9_A39")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(33)
    SetChrSubChip(0xFE, 0x1)
    Sleep(33)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_9_A39 end

    def Function_10_A50(): pass

    label("Function_10_A50")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_10_A50 end

    def Function_11_A59(): pass

    label("Function_11_A59")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_11_A59 end

    def Function_12_A62(): pass

    label("Function_12_A62")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_12_A62 end

    def Function_13_A6B(): pass

    label("Function_13_A6B")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_13_A6B end

    def Function_14_A74(): pass

    label("Function_14_A74")

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

    # Function_14_A74 end

    def Function_15_AA1(): pass

    label("Function_15_AA1")

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

    # Function_15_AA1 end

    def Function_16_ACE(): pass

    label("Function_16_ACE")

    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_ACE end

    def Function_17_AE5(): pass

    label("Function_17_AE5")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    Sleep(33)
    SetChrSubChip(0xFE, 0x1)
    Sleep(33)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_17_AE5 end

    def Function_18_AFC(): pass

    label("Function_18_AFC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B1A")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_18_AFC")

    label("loc_B1A")

    Return()

    # Function_18_AFC end

    def Function_19_B1B(): pass

    label("Function_19_B1B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B39")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(66)
    Jump("Function_19_B1B")

    label("loc_B39")

    Return()

    # Function_19_B1B end

    def Function_20_B3A(): pass

    label("Function_20_B3A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B58")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_20_B3A")

    label("loc_B58")

    Return()

    # Function_20_B3A end

    def Function_21_B59(): pass

    label("Function_21_B59")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B77")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(66)
    Jump("Function_21_B59")

    label("loc_B77")

    Return()

    # Function_21_B59 end

    def Function_22_B78(): pass

    label("Function_22_B78")

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

    # Function_22_B78 end

    def Function_23_C3A(): pass

    label("Function_23_C3A")

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

    # Function_23_C3A end

    def Function_24_D1C(): pass

    label("Function_24_D1C")

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

    # Function_24_D1C end

    def Function_25_E81(): pass

    label("Function_25_E81")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1491")
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

    def lambda_FBB():
        OP_9E(0x8, 0x0, 0x5DC0, 0x927C0, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_FBB)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_FFD():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_FFD)
    Sleep(33)
    BeginChrThread(0x8, 1, 0, 27)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x8, 0x0)

    def lambda_103C():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_103C)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_1052():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1052)
    Sleep(33)
    BeginChrThread(0x8, 1, 0, 27)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x8, 0x0)

    def lambda_1091():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1091)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_10CD():
        OP_9E(0x8, 0x0, 0x636A, 0xFFFA81C0, 0x2134, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_10CD)
    Sleep(33)
    BeginChrThread(0x8, 1, 0, 27)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x320)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x8, 0x0)

    def lambda_1136():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1136)
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

    def lambda_126F():
        OP_9E(0x8, 0x0, 0x5DC0, 0x927C0, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_126F)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_12B1():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_12B1)
    Sleep(33)
    BeginChrThread(0x8, 1, 0, 27)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x8, 0x0)

    def lambda_12F0():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_12F0)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_1306():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1306)
    Sleep(33)
    BeginChrThread(0x8, 1, 0, 27)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x8, 0x0)

    def lambda_1345():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1345)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_1381():
        OP_9E(0x8, 0x0, 0x636A, 0xFFFA81C0, 0x2134, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1381)
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
    Jump("Function_25_E81")

    label("loc_1491")

    Return()

    # Function_25_E81 end

    def Function_26_1492(): pass

    label("Function_26_1492")

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

    def lambda_15F1():
        OP_93(0x8, 0x12C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_15F1)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x1F)
    BeginChrThread(0x8, 1, 0, 27)

    def lambda_1612():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1612)
    Sleep(520)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x9C4, 0x960)

    def lambda_165D():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_165D)
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

    def lambda_16BC():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_16BC)
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

    def lambda_1721():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1721)
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

    def lambda_17C4():
        OP_93(0xFE, 0x73, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_17C4)
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

    # Function_26_1492 end

    def Function_27_18EF(): pass

    label("Function_27_18EF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1939")
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_27_18EF")

    label("loc_1939")

    Return()

    # Function_27_18EF end

    def Function_28_193A(): pass

    label("Function_28_193A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19BB")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4230, 3300, 19500, 0, 90, 0, 300, 600, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4430, 3300, 19500, 0, 90, 0, 300, 600, 300, 0xFF, 0, 0, 0, 0)
    Sleep(1951)
    Jump("Function_28_193A")

    label("loc_19BB")

    Return()

    # Function_28_193A end

    def Function_29_19BC(): pass

    label("Function_29_19BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A3D")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4230, 3300, 19500, 0, 90, 0, 300, 600, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4430, 3300, 19500, 0, 90, 0, 300, 600, 300, 0xFF, 0, 0, 0, 0)
    Sleep(833)
    Jump("Function_29_19BC")

    label("loc_1A3D")

    Return()

    # Function_29_19BC end

    def Function_30_1A3E(): pass

    label("Function_30_1A3E")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)

    label("loc_1A48")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A8E")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_1A48")

    label("loc_1A8E")

    Return()

    # Function_30_1A3E end

    def Function_31_1A8F(): pass

    label("Function_31_1A8F")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)

    label("loc_1A99")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1ADF")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_1A99")

    label("loc_1ADF")

    Return()

    # Function_31_1A8F end

    def Function_32_1AE0(): pass

    label("Function_32_1AE0")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)

    label("loc_1AEA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B30")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x2), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_1AEA")

    label("loc_1B30")

    Return()

    # Function_32_1AE0 end

    def Function_33_1B31(): pass

    label("Function_33_1B31")

    OP_70(0x0, 0x1E)
    OP_71(0x0, 0x1, 0x3C, 0x0, 0x8)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    Sleep(1000)
    OP_95(0xFE, 0, 2430, 30920, 1000, 0x0)
    BeginChrThread(0xE, 0, 0, 34)
    BeginChrThread(0x11, 0, 0, 35)
    BeginChrThread(0x12, 0, 0, 36)
    OP_95(0xFE, 0, 1520, 29550, 1000, 0x0)

    def lambda_1B8E():

        label("loc_1B8E")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1B8E")

    QueueWorkItem2(0xFE, 2, lambda_1B8E)
    Return()

    # Function_33_1B31 end

    def Function_34_1B9C(): pass

    label("Function_34_1B9C")

    Sleep(1000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_95(0xFE, 0, 2430, 30920, 1000, 0x0)
    OP_95(0xFE, 800, 1910, 30140, 1000, 0x0)

    def lambda_1BD7():

        label("loc_1BD7")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1BD7")

    QueueWorkItem2(0xFE, 2, lambda_1BD7)
    Return()

    # Function_34_1B9C end

    def Function_35_1BE5(): pass

    label("Function_35_1BE5")

    Sleep(3000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_95(0xFE, 0, 2430, 30920, 1000, 0x0)
    OP_95(0xFE, -970, 2200, 30570, 1000, 0x0)

    def lambda_1C20():

        label("loc_1C20")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1C20")

    QueueWorkItem2(0xFE, 2, lambda_1C20)
    Return()

    # Function_35_1BE5 end

    def Function_36_1C2E(): pass

    label("Function_36_1C2E")

    Sleep(4000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_95(0xFE, 0, 2430, 30920, 1000, 0x0)
    OP_95(0xFE, -180, 2190, 30560, 1000, 0x0)

    def lambda_1C69():

        label("loc_1C69")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1C69")

    QueueWorkItem2(0xFE, 2, lambda_1C69)
    OP_71(0x0, 0x3C, 0x0, 0x0, 0x8)
    Return()

    # Function_36_1C2E end

    def Function_37_1C83(): pass

    label("Function_37_1C83")

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
    SetChrName("女性的声音")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "──尊敬的观众，让各位久等了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "接下来，彩虹剧团的新剧\x01",
            "『金之太阳、银之月』\x01",
            "即将正式拉开帷幕。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "希望您能一直享受到最后。\x07\x00\x02",
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
    SetChrName("男性的声音")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──这里是『乐之国』。\x01",
            "深受天之女神的祝福与慈爱，\x01",
            "繁荣昌盛的古代王国。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "自古以来，『乐之国』\x01",
            "都遵从名为『舞姬』的\x01",
            "舞者，来决定一切政治行动。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『舞姬』们继承了女神的意志，\x01",
            "在星之神殿中比拼舞技，\x01",
            "将正确的政略告知于世人……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "可是，在各种利益与诡计的交织之下，\x01",
            "当权者们相互展开争斗，\x01",
            "各自拥护了不同的『舞姬』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──在此背景下，\x01",
            "一位拥有当代第一舞技，被誉为『太阳之姬』\x01",
            "的绝世舞者，降临到了星之神殿。\x07\x00\x02",
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

    def lambda_249E():
        OP_96(0xFE, 0xE6, 0x4E2, 0x6978, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_249E)
    Sleep(500)

    def lambda_24BB():
        OP_96(0xFE, 0x528, 0x4E2, 0x6540, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_24BB)
    Sleep(400)

    def lambda_24D8():
        OP_96(0xFE, 0xE6, 0x4E2, 0x6978, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_24D8)
    Sleep(500)

    def lambda_24F5():
        OP_96(0xFE, 0xE6, 0x4E2, 0x6978, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_24F5)
    OP_0D()
    StopBGM(0x1388)
    WaitChrThread(0x22, 1)
    WaitBGM()
    OP_E6()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_25A3")
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

    label("loc_25A3")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x211), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    VolumeBGM(0x32, 0x64)
    OP_24(0x369)
    SetScenarioFlags(0x5C, 3)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_1C83 end

    def Function_38_25C2(): pass

    label("Function_38_25C2")

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

    # Function_38_25C2 end

    def Function_39_25F6(): pass

    label("Function_39_25F6")

    OP_68(10, 2900, 23030, 10000)
    MoveCamera(0, 19, 0, 10000)
    OP_6E(570, 10000)
    SetCameraDistance(19500, 10000)
    SetChrPos(0x9, 0, 9500, 23220, 270)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 21)
    OP_A7(0x9, 0x0, 0x0, 0x0, 0xFF, 0x0)

    def lambda_2651():
        OP_96(0x9, 0x0, 0x4E2, 0x5AB4, 0x44C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2651)
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

    def lambda_26D9():
        OP_9E(0x9, 0x0, 0x5AB4, 0xFFFEA070, 0x898, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_26D9)
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

    def lambda_2762():
        OP_93(0x9, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2762)
    BeginChrThread(0x9, 2, 0, 7)
    OP_9D(0x9, 0xFFFFF9FC, 0x4E2, 0x5E38, 0xBB8, 0x4B0)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x1)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1E)
    BeginChrThread(0x9, 2, 0, 7)

    def lambda_27A2():
        OP_93(0x9, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_27A2)
    OP_9D(0x9, 0xFFFFF3C6, 0x4E2, 0x62F2, 0x3E8, 0x6A4)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x2)
    Sleep(1500)

    def lambda_27D1():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_27D1)
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

    # Function_39_25F6 end

    def Function_40_289F(): pass

    label("Function_40_289F")

    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 21)
    OP_96(0x9, 0xFFFFECF0, 0x4E2, 0x5BC2, 0x5DC, 0x0)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)

    def lambda_28CC():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_28CC)
    Sleep(1000)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x1F)
    OP_95(0x9, -2300, 1250, 23490, 4000, 0x0)
    BeginChrThread(0x9, 2, 0, 7)

    def lambda_2904():
        OP_9D(0x9, 0x974, 0x4E2, 0x5BC2, 0xDAC, 0x44C)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2904)
    Sleep(1000)
    BeginChrThread(0x9, 3, 0, 20)
    WaitChrThread(0x9, 0)

    def lambda_292E():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_292E)
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

    def lambda_297E():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_297E)
    Sleep(800)
    SetChrChipByIndex(0x9, 0x1F)
    OP_95(0x9, 1420, 1250, 23490, 4500, 0x0)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)

    def lambda_29BC():
        OP_9D(0x9, 0xFFFFF894, 0x4E2, 0x5BC2, 0x7D0, 0xB54)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_29BC)
    WaitChrThread(0x9, 0)
    BeginChrThread(0x9, 2, 0, 46)

    def lambda_29E3():
        OP_9D(0x9, 0xFFFFECF0, 0x4E2, 0x5BC2, 0xDAC, 0x2BC)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_29E3)
    Sleep(1000)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)
    WaitChrThread(0x9, 0)

    def lambda_2A13():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2A13)
    Sleep(800)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 21)
    OP_9E(0x9, 0xFFFFF0D8, 0x4C2C, 0x15F90, 0x7D0, 0x0)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x1)

    def lambda_2A4C():
        OP_93(0x9, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2A4C)
    Sleep(1500)
    SetChrSubChip(0x9, 0x0)
    Return()

    # Function_40_289F end

    def Function_41_2A5C(): pass

    label("Function_41_2A5C")

    OP_68(10, 3500, 23030, 10000)
    MoveCamera(0, 7, 0, 10000)
    OP_6E(580, 10000)
    SetCameraDistance(19500, 10000)

    def lambda_2A8F():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2A8F)
    BeginChrThread(0x9, 2, 0, 7)
    OP_9D(0x9, 0xA, 0x4E2, 0x48E4, 0x7D0, 0xBB8)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xFFFFFA24, 0x4E2, 0x4E84, 0x7D0, 0xBB8)
    BeginChrThread(0x9, 2, 0, 11)
    BeginChrThread(0x9, 3, 0, 18)
    OP_9D(0x9, 0x5DC, 0x4E2, 0x50BE, 0x7D0, 0xBB8)

    def lambda_2AFF():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2AFF)
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

    def lambda_2B8C():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2B8C)
    BeginChrThread(0x9, 2, 0, 11)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xFFFFFA24, 0x4E2, 0x587A, 0x7D0, 0xC80)
    EndChrThread(0x9, 0x3)
    BeginChrThread(0x9, 2, 0, 7)
    OP_9D(0x9, 0x5DC, 0x4E2, 0x50BE, 0xDAC, 0x514)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xFFFFFA24, 0x4E2, 0x4E84, 0x7D0, 0xC80)

    def lambda_2C00():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2C00)
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

    def lambda_2CA3():
        OP_9D(0x9, 0x1E, 0x187E, 0x753A, 0x1D4C, 0x258)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2CA3)
    Sleep(1000)

    def lambda_2CC3():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2CC3)
    OP_A7(0x9, 0x50, 0x50, 0x50, 0xFF, 0x12C)
    WaitChrThread(0x9, 0)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x2)
    Sleep(1700)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)

    def lambda_2CFA():
        OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2CFA)
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

    # Function_41_2A5C end

    def Function_42_2D72(): pass

    label("Function_42_2D72")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DBC")
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, -300, 0, 0, 180, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_42_2D72")

    label("loc_2DBC")

    Return()

    # Function_42_2D72 end

    def Function_43_2DBD(): pass

    label("Function_43_2DBD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E8C")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E69")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E69")
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    label("loc_2E69")

    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_43_2DBD")

    label("loc_2E8C")

    Return()

    # Function_43_2DBD end

    def Function_44_2E8D(): pass

    label("Function_44_2E8D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3058")
    Sleep(2166)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 5920, 1700, 21450, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 6690, 1700, 27650, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, -5920, 1700, 21450, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, -6690, 1700, 27650, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 5920, 1000, 21450, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 6690, 1000, 27650, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -5920, 1000, 21450, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -6690, 1000, 27650, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    Jump("Function_44_2E8D")

    label("loc_3058")

    Return()

    # Function_44_2E8D end

    def Function_45_3059(): pass

    label("Function_45_3059")

    Sleep(530)

    label("loc_305C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3309")
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
    Jump("loc_305C")

    label("loc_3309")

    Return()

    # Function_45_3059 end

    def Function_46_330A(): pass

    label("Function_46_330A")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_D3(0xFE, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x100)
    OP_D3(0xFE, 0x0, 0x0, 0x57E40, 0x3E8)
    SetChrFlags(0xFE, 0x100)
    Return()

    # Function_46_330A end

    def Function_47_3343(): pass

    label("Function_47_3343")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    OP_D3(0xFE, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x100)
    OP_D3(0xFE, 0x0, 0x0, 0xFFFA81C0, 0x3E8)
    SetChrFlags(0xFE, 0x100)
    Return()

    # Function_47_3343 end

    def Function_48_337C(): pass

    label("Function_48_337C")

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
    SetChrName("女性的声音")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "如此一来，为了对抗拥护\x01",
            "『太阳之姬』的『阳之一族』……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "另一位新的舞姬也现身于世人面前。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "这位舞姬的名字是『月之姬』……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "她便是『乐之国』的另一大势力——\x01",
            "『夜之一族』所拥护的舞者。\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_385C")
    LoadEffect(0x0, "event\\evanull.eff")

    label("loc_385C")

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

    def lambda_39A8():
        OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_39A8)

    def lambda_39B9():
        OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_39B9)

    def lambda_39CA():
        OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_39CA)

    def lambda_39DB():
        OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_39DB)

    def lambda_39EC():
        OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_39EC)

    def lambda_39FD():
        OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_39FD)
    WaitChrThread(0x101, 3)
    Sleep(2000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_3ACE")
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

    label("loc_3ACE")

    WaitChrThread(0x22, 1)
    OP_E6()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1F5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x369)
    SetScenarioFlags(0x5D, 5)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_48_337C end

    def Function_49_3AEC(): pass

    label("Function_49_3AEC")

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

    # Function_49_3AEC end

    def Function_50_3B23(): pass

    label("Function_50_3B23")

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

    # Function_50_3B23 end

    def Function_51_3BAD(): pass

    label("Function_51_3BAD")

    PlayEffect(0x5, 0x2, 0xFF, 0x0, 0, 1000, 25000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x8, 0x23)

    def lambda_3BED():

        label("loc_3BED")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_3BED")

    QueueWorkItem2(0x8, 3, lambda_3BED)
    OP_A7(0x8, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x8, -690, 1250, 22710, 90)
    OP_A7(0x8, 0x0, 0x0, 0x0, 0xFF, 0x64)
    OP_68(-1890, 2900, 22370, 2000)
    MoveCamera(0, 16, 0, 2000)
    OP_6E(620, 2000)
    SetCameraDistance(17000, 2000)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -1370, 2000, 23670, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(900)

    def lambda_3C8E():

        label("loc_3C8E")

        TurnDirection(0x9, 0x8, 500)
        Yield()
        Jump("loc_3C8E")

    QueueWorkItem2(0x9, 3, lambda_3C8E)
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

    def lambda_3D7E():
        OP_96(0x9, 0xFFFFF092, 0x4E2, 0x5C76, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3D7E)
    OP_A8(0x8, 0x0, 0x0, 0x0, 0x3E8)
    OP_A8(0x9, 0x0, 0x0, 0x0, 0x3E8)
    Return()

    # Function_51_3BAD end

    def Function_52_3DA8(): pass

    label("Function_52_3DA8")

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

    def lambda_3E48():
        OP_9E(0x8, 0xFFFFF858, 0x625C, 0xFFFF63C0, 0x4B0, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3E48)
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

    def lambda_3ED2():
        OP_93(0x8, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3ED2)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFF614, 0x4E2, 0x622A, 0xBB8, 0x2BC)
    BeginChrThread(0x8, 2, 0, 7)

    def lambda_3F02():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3F02)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x4B0, 0x1F4)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)
    EndChrThread(0x8, 0x3)
    SetChrSubChip(0x8, 0x2)
    Sleep(1100)

    def lambda_3F39():
        OP_93(0x8, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3F39)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFF394, 0x4E2, 0x65EA, 0x7D0, 0x578)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9D(0x8, 0xFFFFF902, 0x4E2, 0x65EA, 0x7D0, 0x578)
    BeginChrThread(0x8, 2, 0, 7)

    def lambda_3F8C():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3F8C)
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

    def lambda_401C():

        label("loc_401C")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_401C")

    QueueWorkItem2(0x8, 3, lambda_401C)
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

    # Function_52_3DA8 end

    def Function_53_4063(): pass

    label("Function_53_4063")

    BeginChrThread(0x8, 1, 0, 57)

    def lambda_406E():
        OP_93(0x8, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_406E)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFF902, 0x4E2, 0x639C, 0x7D0, 0x578)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9D(0x8, 0xFFFFF394, 0x4E2, 0x639C, 0x7D0, 0x578)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFEE30, 0x4E2, 0x639C, 0x7D0, 0x578)

    def lambda_40D8():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_40D8)
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

    def lambda_4137():

        label("loc_4137")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_4137")

    QueueWorkItem2(0x8, 3, lambda_4137)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)
    Sleep(1200)

    def lambda_4154():

        label("loc_4154")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_4154")

    QueueWorkItem2(0x8, 3, lambda_4154)
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

    # Function_53_4063 end

    def Function_54_419A(): pass

    label("Function_54_419A")

    BeginChrThread(0x9, 1, 0, 58)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x28)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    OP_95(0x9, -3550, 1250, 22010, 2000, 0x0)
    BeginChrThread(0x9, 2, 0, 15)

    def lambda_41D1():
        OP_9E(0x9, 0xFFFFF858, 0x625C, 0xFFFF63C0, 0x4B0, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_41D1)
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

    def lambda_425B():
        OP_93(0x9, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_425B)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9D(0x9, 0xFFFFEE30, 0x4E2, 0x659A, 0xBB8, 0x2BC)
    BeginChrThread(0x9, 2, 0, 15)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 7)

    def lambda_4295():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_4295)

    def lambda_42A2():
        OP_9D(0x8, 0xFFFFFFBA, 0x4E2, 0x61DA, 0x4B0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_42A2)

    def lambda_42BF():

        label("loc_42BF")

        TurnDirection(0x9, 0x8, 500)
        Yield()
        Jump("loc_42BF")

    QueueWorkItem2(0x9, 3, lambda_42BF)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x4B0, 0x1F4)

    def lambda_42E8():

        label("loc_42E8")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_42E8")

    QueueWorkItem2(0x8, 3, lambda_42E8)
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

    def lambda_4337():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_4337)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9D(0x9, 0xFFFFF394, 0x4E2, 0x65EA, 0x7D0, 0x578)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xFFFFF902, 0x4E2, 0x65EA, 0x7D0, 0x578)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9D(0x9, 0xFFFFFD9E, 0x4E2, 0x65EA, 0x7D0, 0x578)

    def lambda_43A1():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_43A1)
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

    def lambda_4404():

        label("loc_4404")

        TurnDirection(0x9, 0x8, 500)
        Yield()
        Jump("loc_4404")

    QueueWorkItem2(0x9, 3, lambda_4404)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x1)
    Return()

    # Function_54_419A end

    def Function_55_441A(): pass

    label("Function_55_441A")

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

    def lambda_44BE():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_44BE)
    BeginChrThread(0xFE, 2, 0, 7)
    OP_9D(0xFE, 0x1158, 0x125C, 0x655E, 0x7D0, 0x578)
    BeginChrThread(0xFE, 2, 0, 9)
    BeginChrThread(0xFE, 3, 0, 18)
    OP_9D(0xFE, 0x15FE, 0x125C, 0x6B8A, 0x7D0, 0x578)

    def lambda_450B():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_450B)
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

    def lambda_45E5():
        OP_9E(0xFE, 0xFFFFFC18, 0x61A8, 0x1A3EC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_45E5)
    Sleep(1)

    def lambda_4603():
        OP_96(0xFE, 0xFDB, 0x4E2, 0x6554, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4603)
    Sleep(300)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_55_441A end

    def Function_56_4663(): pass

    label("Function_56_4663")

    EndChrThread(0xFE, 0x3)
    OP_9E(0xFE, 0xFFFFF84E, 0x59B0, 0x2BF20, 0xFA0, 0x1)
    BeginChrThread(0xFE, 2, 0, 17)
    BeginChrThread(0xFE, 3, 0, 20)
    OP_9D(0xFE, 0xFFFFF9CA, 0x4E2, 0x636A, 0xBB8, 0x3E8)

    def lambda_46A4():
        OP_96(0xFE, 0xFFFFFAD8, 0x4E2, 0x6978, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_46A4)

    def lambda_46BE():

        label("loc_46BE")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_46BE")

    QueueWorkItem2(0x10, 1, lambda_46BE)
    EndChrThread(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 0x29)
    OP_95(0xFE, 1410, 1250, 26610, 5000, 0x0)
    OP_68(-1000, 7000, 26030, 3000)
    MoveCamera(0, 12, 0, 3000)
    OP_6E(620, 3000)
    SetCameraDistance(17000, 3000)
    BeginChrThread(0xFE, 2, 0, 14)
    OP_9D(0xFE, 0xD7A, 0x125C, 0x6C16, 0x12C0, 0x7D0)

    def lambda_4737():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4737)
    BeginChrThread(0xFE, 2, 0, 15)
    OP_9D(0xFE, 0x1158, 0x125C, 0x655E, 0x7D0, 0x578)
    BeginChrThread(0xFE, 2, 0, 17)
    BeginChrThread(0xFE, 3, 0, 20)
    OP_9D(0xFE, 0x15FE, 0x125C, 0x6B8A, 0x7D0, 0x578)

    def lambda_4784():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4784)
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

    def lambda_4896():
        OP_9E(0xFE, 0xFFFFFC18, 0x61A8, 0xFFE5C140, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4896)
    Sleep(1)

    def lambda_48B4():
        OP_96(0xFE, 0xFDB, 0x4E2, 0x6554, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_48B4)
    Sleep(300)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_56_4663 end

    def Function_57_4914(): pass

    label("Function_57_4914")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49AC")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4989")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4989")
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    label("loc_4989")

    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_57_4914")

    label("loc_49AC")

    Return()

    # Function_57_4914 end

    def Function_58_49AD(): pass

    label("Function_58_49AD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A45")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4A22")
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A22")
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    label("loc_4A22")

    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_58_49AD")

    label("loc_4A45")

    Return()

    # Function_58_49AD end

    def Function_59_4A46(): pass

    label("Function_59_4A46")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A90")
    PlayEffect(0x1, 0xFF, 0xFE, 0x40, 0, 100, 0, 0, 0, 0, 1100, 1800, 1100, 0xFF, 0, 0, 0, 0)
    Sleep(3200)
    Jump("Function_59_4A46")

    label("loc_4A90")

    Return()

    # Function_59_4A46 end

    def Function_60_4A91(): pass

    label("Function_60_4A91")

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
    SetChrName("男性的声音")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──这究竟是女神的心血来潮，\x01",
            "还是恶作剧呢……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『太阳之姬』得知，『月之姬』\x01",
            "竟然是自己失散多年的亲妹妹。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "但『月之姬』却对此一无所知，\x01",
            "始终对太阳之姬抱着一颗冷如冰霜的敌对心。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "烦恼不已的『太阳之姬』\x01",
            "将真实面目隐藏于白衣与面纱之下，\x01",
            "将『月之姬』约到了森林中的废墟……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "那是姐妹两人在幼年时期\x01",
            "经常一起开心玩耍的秘密场所。\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_4EAB")
    LoadEffect(0x0, "event\\evanull.eff")
    LoadEffect(0x4, "event\\evanull.eff")
    LoadEffect(0x6, "event\\evanull.eff")
    LoadEffect(0x7, "event\\evanull.eff")

    label("loc_4EAB")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_50E2")
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

    label("loc_50E2")

    WaitChrThread(0x22, 1)
    OP_E6()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1F6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x369)
    SetScenarioFlags(0x5D, 6)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_60_4A91 end

    def Function_61_5100(): pass

    label("Function_61_5100")

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

    # Function_61_5100 end

    def Function_62_512B(): pass

    label("Function_62_512B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5288")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4410, 3700, 20000, 0, 90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4410, 3700, 20000, 0, 90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4100, 4800, 31100, 0, 90, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4000, 4800, 31100, 0, 90, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -4160, -2000, 31100, 0, -90, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 4160, -2000, 31100, 0, -90, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    Sleep(833)
    Jump("Function_62_512B")

    label("loc_5288")

    Return()

    # Function_62_512B end

    def Function_63_5289(): pass

    label("Function_63_5289")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53E6")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4410, 3700, 20000, 0, 90, 0, 400, 600, 400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4410, 3700, 20000, 0, 90, 0, 400, 600, 400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4100, 4800, 31100, 0, 90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4000, 4800, 31100, 0, 90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -4160, -2000, 31100, 0, -90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 4160, -2000, 31100, 0, -90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sleep(833)
    Jump("Function_63_5289")

    label("loc_53E6")

    Return()

    # Function_63_5289 end

    def Function_64_53E7(): pass

    label("Function_64_53E7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54B6")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5493")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5493")
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    label("loc_5493")

    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_64_53E7")

    label("loc_54B6")

    Return()

    # Function_64_53E7 end

    def Function_65_54B7(): pass

    label("Function_65_54B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5586")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5563")
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5563")
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    label("loc_5563")

    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_65_54B7")

    label("loc_5586")

    Return()

    # Function_65_54B7 end

    def Function_66_5587(): pass

    label("Function_66_5587")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5656")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5633")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5633")
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(250)

    label("loc_5633")

    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_66_5587")

    label("loc_5656")

    Return()

    # Function_66_5587 end

    def Function_67_5657(): pass

    label("Function_67_5657")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5726")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5703")
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5703")
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(250)

    label("loc_5703")

    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_67_5657")

    label("loc_5726")

    Return()

    # Function_67_5657 end

    def Function_68_5727(): pass

    label("Function_68_5727")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5771")
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_68_5727")

    label("loc_5771")

    Return()

    # Function_68_5727 end

    def Function_69_5772(): pass

    label("Function_69_5772")


    def lambda_5777():

        label("loc_5777")

        TurnDirection(0xC, 0x8, 500)
        Yield()
        Jump("loc_5777")

    QueueWorkItem2(0xC, 1, lambda_5777)
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

    # Function_69_5772 end

    def Function_70_57F7(): pass

    label("Function_70_57F7")


    def lambda_57FC():

        label("loc_57FC")

        TurnDirection(0xC, 0x9, 500)
        Yield()
        Jump("loc_57FC")

    QueueWorkItem2(0xC, 1, lambda_57FC)
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

    # Function_70_57F7 end

    def Function_71_58C0(): pass

    label("Function_71_58C0")

    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 2, 0, 15)

    def lambda_58D5():
        OP_9D(0x9, 0xFA, 0xCB2, 0x5C58, 0x7D0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_58D5)
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

    def lambda_594D():
        OP_9E(0x9, 0x0, 0x5DC0, 0x1B7740, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_594D)
    Sleep(33)

    def lambda_596B():

        label("loc_596B")

        TurnDirection(0x9, 0x8, 0)
        Yield()
        Jump("loc_596B")

    QueueWorkItem2(0x9, 3, lambda_596B)
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

    def lambda_5A1B():

        label("loc_5A1B")

        TurnDirection(0x9, 0x8, 500)
        Yield()
        Jump("loc_5A1B")

    QueueWorkItem2(0x9, 3, lambda_5A1B)
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

    def lambda_5AB0():
        OP_9D(0x9, 0xF28, 0x4E2, 0x5BC2, 0xDAC, 0x384)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5AB0)
    Sleep(1000)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    WaitChrThread(0x9, 1)

    def lambda_5AE0():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_5AE0)
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

    # Function_71_58C0 end

    def Function_72_5B20(): pass

    label("Function_72_5B20")

    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 2, 0, 7)

    def lambda_5B35():
        OP_9D(0x8, 0xFFFFFF06, 0xCB2, 0x5C58, 0x7D0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5B35)
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

    def lambda_5BB3():
        OP_9E(0x8, 0x0, 0x5DC0, 0x1B7740, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5BB3)
    Sleep(33)

    def lambda_5BD1():

        label("loc_5BD1")

        TurnDirection(0x8, 0x9, 0)
        Yield()
        Jump("loc_5BD1")

    QueueWorkItem2(0x8, 3, lambda_5BD1)
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

    def lambda_5C81():

        label("loc_5C81")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_5C81")

    QueueWorkItem2(0x8, 3, lambda_5C81)
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

    def lambda_5D16():
        OP_9D(0x8, 0xFFFFF0D8, 0x4E2, 0x5BC2, 0xDAC, 0x384)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5D16)
    Sleep(1000)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    WaitChrThread(0x8, 1)

    def lambda_5D46():
        OP_93(0x8, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_5D46)
    Sleep(700)

    def lambda_5D56():

        label("loc_5D56")

        TurnDirection(0x8, 0x9, 0)
        Yield()
        Jump("loc_5D56")

    QueueWorkItem2(0x8, 3, lambda_5D56)
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

    # Function_72_5B20 end

    def Function_73_5D98(): pass

    label("Function_73_5D98")

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

    def lambda_6053():

        label("loc_6053")

        TurnDirection(0x9, 0x8, 0)
        Yield()
        Jump("loc_6053")

    QueueWorkItem2(0x9, 3, lambda_6053)
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

    def lambda_6327():
        OP_9E(0x9, 0x0, 0x61A8, 0x20F580, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6327)
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

    # Function_73_5D98 end

    def Function_74_6413(): pass

    label("Function_74_6413")

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

    def lambda_65D4():

        label("loc_65D4")

        TurnDirection(0x8, 0x9, 0)
        Yield()
        Jump("loc_65D4")

    QueueWorkItem2(0x8, 3, lambda_65D4)
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

    def lambda_66E6():
        OP_9E(0x8, 0x0, 0x61A8, 0x20F580, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_66E6)
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

    # Function_74_6413 end

    def Function_75_67D2(): pass

    label("Function_75_67D2")

    OP_96(0xC, 0xA, 0x4E2, 0x7044, 0x3E8, 0x0)
    OP_96(0xC, 0x0, 0x8F2, 0x7486, 0x3E8, 0x0)
    Return()

    # Function_75_67D2 end

    def Function_76_67FB(): pass

    label("Function_76_67FB")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_6D7A")
    LoadEffect(0x7, "event\\evanull.eff")

    label("loc_6D7A")

    SoundLoad(872)
    SoundLoad(873)
    SoundLoad(874)
    SoundLoad(876)
    Sound(877, 0, 100, 0)
    Sleep(4000)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "──将幼年的姐妹生生拆散的，\x01",
            "竟是一场人为策划的可怕阴谋……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "然而，即使明白了这个真相，\x01",
            "姐妹二人还是不得不互相争斗。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "要问为何，只因她们是『舞姬』……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "对她们而言，舞蹈就是生命的全部。\x01",
            "但可以继承女神之意志的\x01",
            "『巫女姬』，却只能有一人。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "对彼此的思念之情，\x01",
            "爱慕上同一对象的纠葛……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "以及，惺惺相惜的对手之间燃起的\x01",
            "共鸣与对抗意识……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0024
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "将各种情绪深埋于心中，\x01",
            "今夜，两位舞姬将降临于这座『星之神殿』──\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_7655")
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

    label("loc_7655")

    OP_24(0x369)
    SetScenarioFlags(0x5D, 7)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_76_67FB end

    def Function_77_7665(): pass

    label("Function_77_7665")

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

    # Function_77_7665 end

    def Function_78_76BA(): pass

    label("Function_78_76BA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_76CD")
    Sleep(4138)
    Jump("Function_78_76BA")

    label("loc_76CD")

    Return()

    # Function_78_76BA end

    def Function_79_76CE(): pass

    label("Function_79_76CE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7718")
    PlayEffect(0x7, 0xFF, 0xFE, 0x100, -500, -800, 0, 0, 180, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Jump("Function_79_76CE")

    label("loc_7718")

    Return()

    # Function_79_76CE end

    def Function_80_7719(): pass

    label("Function_80_7719")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7808")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4410, 3700, 20000, 0, 90, 0, 300, 400, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4410, 3700, 20000, 0, 90, 0, 300, 400, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4100, 4800, 31100, 0, 90, 0, 200, 300, 200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4000, 4800, 31100, 0, 90, 0, 200, 300, 200, 0xFF, 0, 0, 0, 0)
    Sleep(833)
    Jump("Function_80_7719")

    label("loc_7808")

    Return()

    # Function_80_7719 end

    def Function_81_7809(): pass

    label("Function_81_7809")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7853")
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_81_7809")

    label("loc_7853")

    Return()

    # Function_81_7809 end

    def Function_82_7854(): pass

    label("Function_82_7854")

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

    def lambda_7898():
        OP_9E(0x8, 0xFFFFFA24, 0x61A8, 0x927C0, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_7898)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_78DA():
        OP_9E(0x8, 0x0, 0x61A8, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_78DA)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x8, 0x0)

    def lambda_7913():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_7913)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_7929():
        OP_9E(0x8, 0x0, 0x61A8, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_7929)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x8, 0x0)

    def lambda_7962():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_7962)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_799E():
        OP_9E(0x8, 0x0, 0x61A8, 0xFFFA81C0, 0x2134, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_799E)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x320)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x8, 0x0)

    def lambda_7A01():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_7A01)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFFE0C, 0x319C, 0x61A8, 0x7D0, 0xBB8)

    def lambda_7A2B():
        OP_9E(0x8, 0x0, 0x61A8, 0xFFF50380, 0x1194, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_7A2B)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 9)
    Sleep(1)
    OP_9D(0x8, 0xFFFFFE0C, 0x332C, 0x61A8, 0xBB8, 0x4B0)
    EndChrThread(0x8, 0x3)
    OP_93(0x8, 0xB4, 0x0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Return()

    # Function_82_7854 end

    def Function_83_7A79(): pass

    label("Function_83_7A79")

    Sleep(600)
    SetChrSubChip(0x8, 0x1)
    Sleep(100)
    OP_93(0x8, 0x87, 0x0)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x1)
    Return()

    # Function_83_7A79 end

    def Function_84_7A93(): pass

    label("Function_84_7A93")

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

    def lambda_7AD7():
        OP_9E(0x9, 0x5DC, 0x61A8, 0x927C0, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_7AD7)
    Sleep(33)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    EndChrThread(0x9, 0x3)
    BeginChrThread(0x9, 2, 0, 14)
    Sleep(100)

    def lambda_7B19():
        OP_9E(0x9, 0x0, 0x61A8, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_7B19)
    Sleep(33)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x9, 0x0)

    def lambda_7B52():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_7B52)
    BeginChrThread(0x9, 2, 0, 14)
    Sleep(100)

    def lambda_7B68():
        OP_9E(0x9, 0x0, 0x61A8, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_7B68)
    Sleep(33)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x9, 0x0)

    def lambda_7BA1():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_7BA1)
    BeginChrThread(0x9, 2, 0, 14)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    BeginChrThread(0x9, 2, 0, 14)
    Sleep(100)

    def lambda_7BDD():
        OP_9E(0x9, 0x0, 0x61A8, 0xFFFA81C0, 0x2134, 0x2)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_7BDD)
    Sleep(33)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xFA0, 0x320)
    BeginChrThread(0x9, 2, 0, 14)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    EndChrThread(0x9, 0x3)
    EndChrThread(0x9, 0x0)

    def lambda_7C40():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_7C40)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9D(0x9, 0x1F4, 0x319C, 0x61A8, 0x7D0, 0xBB8)

    def lambda_7C6A():
        OP_9E(0x9, 0x0, 0x61A8, 0xFFF50380, 0x1194, 0x2)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_7C6A)
    EndChrThread(0x9, 0x3)
    BeginChrThread(0x9, 2, 0, 17)
    Sleep(1)
    OP_9D(0x9, 0x1F4, 0x332C, 0x61A8, 0xBB8, 0x4B0)
    OP_93(0x9, 0xB4, 0x0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    Return()

    # Function_84_7A93 end

    def Function_85_7CB4(): pass

    label("Function_85_7CB4")

    Sleep(600)
    SetChrSubChip(0x9, 0x1)
    Sleep(100)
    OP_93(0x9, 0xE1, 0x0)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x1)
    Return()

    # Function_85_7CB4 end

    def Function_86_7CCE(): pass

    label("Function_86_7CCE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D04")
    OP_D3(0x18, 0x0, 0x36EE80, 0x0, 0xEA60)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    Jump("Function_86_7CCE")

    label("loc_7D04")

    Return()

    # Function_86_7CCE end

    def Function_87_7D05(): pass

    label("Function_87_7D05")

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

    label("loc_7DCB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7E31")
    OP_A1(0xFE, 0x7D0, 0x4, 0x2, 0x3, 0x2, 0x4)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E03")
    Sleep(1500)
    Jump("loc_7E2C")

    label("loc_7E03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E1A")
    Sleep(800)
    Jump("loc_7E2C")

    label("loc_7E1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E2C")
    Sleep(100)

    label("loc_7E2C")

    Jump("loc_7DCB")

    label("loc_7E31")

    Return()

    # Function_87_7D05 end

    def Function_88_7E32(): pass

    label("Function_88_7E32")

    Sleep(4000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_95(0xFE, 2610, 1250, 24750, 5000, 0x0)
    OP_9E(0xFE, 0x0, 0x61A8, 0x8ED28, 0x1388, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x10, 500)
    Sleep(1000)
    OP_99(0xFE, 0x10, 0x3E8, 0x1F4, 0x0)
    Return()

    # Function_88_7E32 end

    def Function_89_7E85(): pass

    label("Function_89_7E85")

    Sleep(4500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_95(0xFE, 2610, 1250, 24750, 5000, 0x0)
    OP_9E(0xFE, 0x0, 0x61A8, 0x83D60, 0x1388, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x10, 500)
    Sleep(1000)
    OP_99(0xFE, 0x10, 0x4B0, 0x1F4, 0x0)
    Return()

    # Function_89_7E85 end

    def Function_90_7ED8(): pass

    label("Function_90_7ED8")

    OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xBB8, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x7D0, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFE0C, 0x0, 0x5DC, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFE0C, 0x0, 0x3E8, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFE0C, 0x0, 0x320, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFE0C, 0x0, 0x28A, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0x1F4, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x12C, 0x0)
    Return()

    # Function_90_7ED8 end

    def Function_91_7F79(): pass

    label("Function_91_7F79")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7F97")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_91_7F79")

    label("loc_7F97")

    Return()

    # Function_91_7F79 end

    def Function_92_7F98(): pass

    label("Function_92_7F98")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7FB6")
    OP_A1(0xFE, 0x7D0, 0x8, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3, 0x0, 0x1)
    Jump("Function_92_7F98")

    label("loc_7FB6")

    Return()

    # Function_92_7F98 end

    def Function_93_7FB7(): pass

    label("Function_93_7FB7")

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

    def lambda_8011():

        label("loc_8011")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0x320, 0x3)
        Yield()
        Jump("loc_8011")

    QueueWorkItem2(0x8, 2, lambda_8011)
    Sleep(1)
    OP_96(0x8, 0xFFFFFE0C, 0x2BC0, 0x61A8, 0x12C, 0x0)
    EndChrThread(0x8, 0x2)
    BeginChrThread(0x8, 2, 0, 7)
    ClearChrFlags(0x8, 0x1)
    OP_9D(0x8, 0xFFFFFE0C, 0x300C, 0x61A8, 0x7D0, 0x7D0)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x24)

    label("loc_8072")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8090")
    OP_A1(0x8, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("loc_8072")

    label("loc_8090")

    Return()

    # Function_93_7FB7 end

    def Function_94_8091(): pass

    label("Function_94_8091")

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

    def lambda_80EB():

        label("loc_80EB")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0x320, 0x3)
        Yield()
        Jump("loc_80EB")

    QueueWorkItem2(0x9, 2, lambda_80EB)
    Sleep(1)
    OP_96(0x9, 0x1F4, 0x2BC0, 0x61A8, 0x12C, 0x0)
    EndChrThread(0x9, 0x2)
    BeginChrThread(0x9, 2, 0, 15)
    ClearChrFlags(0x9, 0x1)
    OP_9D(0x9, 0x1F4, 0x2EE0, 0x61A8, 0x7D0, 0x7D0)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x2E)
    SetChrSubChip(0x9, 0x6)

    label("loc_8150")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_816E")
    OP_A1(0x9, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("loc_8150")

    label("loc_816E")

    Return()

    # Function_94_8091 end

    def Function_95_816F(): pass

    label("Function_95_816F")

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

    def lambda_8AB7():
        OP_95(0xF, 0, 1500, 28500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_8AB7)
    Sleep(7000)

    def lambda_8AD4():
        OP_95(0xE, 0, 1500, 21500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_8AD4)
    Sleep(1000)

    def lambda_8AF1():
        OP_95(0xD, -3500, 1500, 25000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_8AF1)
    Sleep(1000)

    def lambda_8B0E():
        OP_95(0xC, 3500, 1500, 25000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_8B0E)
    WaitChrThread(0xE, 0)
    OP_93(0xE, 0x0, 0x1F4)
    WaitChrThread(0x18, 1)
    OP_82(0x0, 0xC8, 0x7D0, 0xC8)
    BeginChrThread(0x8, 0, 0, 93)
    BeginChrThread(0x9, 0, 0, 94)
    Sleep(1200)
    OP_D3(0x18, 0x0, 0xAFC8, 0x0, 0x1388)
    OP_D3(0x18, 0x0, 0x16B48, 0x0, 0x7D0)

    def lambda_8B7D():
        OP_96(0xC, 0xDAC, 0x1D4C, 0x61A8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_8B7D)

    def lambda_8B97():
        OP_96(0xD, 0xFFFFF254, 0x1D4C, 0x61A8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_8B97)

    def lambda_8BB1():
        OP_96(0xE, 0x0, 0x1D4C, 0x53FC, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_8BB1)

    def lambda_8BCB():
        OP_96(0xF, 0x0, 0x1D4C, 0x6F54, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_8BCB)

    def lambda_8BE5():

        label("loc_8BE5")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0xDF2, 0x1)
        Yield()
        Jump("loc_8BE5")

    QueueWorkItem2(0xC, 2, lambda_8BE5)

    def lambda_8C05():

        label("loc_8C05")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0xDF2, 0x1)
        Yield()
        Jump("loc_8C05")

    QueueWorkItem2(0xD, 2, lambda_8C05)

    def lambda_8C25():

        label("loc_8C25")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0xDF2, 0x1)
        Yield()
        Jump("loc_8C25")

    QueueWorkItem2(0xE, 2, lambda_8C25)

    def lambda_8C45():

        label("loc_8C45")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0xDF2, 0x1)
        Yield()
        Jump("loc_8C45")

    QueueWorkItem2(0xF, 2, lambda_8C45)
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

    def lambda_8CC5():
        OP_96(0x18, 0x0, 0x2710, 0x61A8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_8CC5)
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
        "#0108F#12P#40W……好厉害…………\x02",
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
        "老人的声音",
        "#6P#50W呵呵……真是了不起……\x02",
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
            "#0105F#11P外、外公！\x02\x03",

            "#0102F太好了……\x01",
            "您已经恢复意识了啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x1F,
        (
            "#2503F#6P#40W嗯……没什么大不了的。\x02\x03",

            "#2500F虽然发生了这样的事情……\x01",
            "但现在还是让我继续将这场表演欣赏到最后吧……\x02\x03",

            "这也是我对彩虹剧团的各位\x01",
            "所应尽的礼仪啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        "#0106F#11P外公……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x1A,
        "这真是最高的赞誉了……\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_901E")
    ClearScenarioFlags(0x5B, 0)
    OP_24(0x370)
    OP_B7(0x0)
    Return()

    label("loc_901E")

    OP_24(0x370)
    SetScenarioFlags(0x5D, 2)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_95_816F end

    def Function_96_902E(): pass

    label("Function_96_902E")

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

    # Function_96_902E end

    def Function_97_90D8(): pass

    label("Function_97_90D8")

    SetChrPos(0x18, 0, 12000, 25000, 0)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)

    label("loc_90FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_92CE")

    def lambda_910C():
        OP_96(0xFE, 0xFFFFFA24, 0x2E18, 0x61A8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_910C)
    OP_D3(0x18, 0x0, 0x0, 0xFFFFF830, 0x3E8)

    def lambda_9139():
        OP_96(0xFE, 0xFFFFFA24, 0x2E7C, 0x61A8, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9139)
    OP_D3(0x18, 0x0, 0x0, 0xFFFFF63C, 0x1F4)

    def lambda_9166():
        OP_96(0xFE, 0xFFFFFA24, 0x2E7C, 0x61A8, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9166)
    OP_D3(0x18, 0x0, 0x0, 0xFFFFF5D8, 0xFA)

    def lambda_9193():
        OP_96(0xFE, 0x0, 0x2E18, 0x61A8, 0xFA, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9193)
    OP_D3(0x18, 0x0, 0x0, 0xFFFFF7CC, 0xFA)

    def lambda_91C0():
        OP_96(0xFE, 0x0, 0x2DB4, 0x61A8, 0x15E, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_91C0)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x2EE)

    def lambda_91ED():
        OP_96(0xFE, 0x5DC, 0x2E18, 0x61A8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_91ED)
    OP_D3(0x18, 0x0, 0x0, 0x7D0, 0x3E8)

    def lambda_921A():
        OP_96(0xFE, 0x5DC, 0x2E7C, 0x61A8, 0xAA, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_921A)
    OP_D3(0x18, 0x0, 0x0, 0x9C4, 0x1F4)

    def lambda_9247():
        OP_96(0xFE, 0x5DC, 0x2E7C, 0x61A8, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9247)
    OP_D3(0x18, 0x0, 0x0, 0x834, 0xFA)

    def lambda_9274():
        OP_96(0xFE, 0x0, 0x2E18, 0x61A8, 0xFA, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9274)
    OP_D3(0x18, 0x0, 0x0, 0x834, 0xFA)

    def lambda_92A1():
        OP_96(0xFE, 0x0, 0x2DB4, 0x61A8, 0x15E, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_92A1)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x2EE)
    Jump("loc_90FC")

    label("loc_92CE")

    Return()

    # Function_97_90D8 end

    def Function_98_92CF(): pass

    label("Function_98_92CF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9899")
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
    Jump("Function_98_92CF")

    label("loc_9899")

    Return()

    # Function_98_92CF end

    def Function_99_989A(): pass

    label("Function_99_989A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9A18")
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
    Jump("Function_99_989A")

    label("loc_9A18")

    Return()

    # Function_99_989A end

    def Function_100_9A19(): pass

    label("Function_100_9A19")

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

    def lambda_A08B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A08B)

    def lambda_A09C():
        OP_95(0xFE, -13000, 15200, -8300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A09C)
    Sleep(500)
    MoveCamera(8, 9, 4, 6000)

    def lambda_A0C4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A0C4)

    def lambda_A0D5():
        OP_95(0xFE, -13000, 15200, -8700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_A0D5)
    Sleep(2000)
    OP_63(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_A10D():

        label("loc_A10D")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_A10D")

    QueueWorkItem2(0x1C, 0, lambda_A10D)
    Sleep(1000)

    #C0031
    ChrTalk(
        0x1C,
        "#0605F#11P#10A什么……！？\x02",
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

    # Function_100_9A19 end

    def Function_101_A16C(): pass

    label("Function_101_A16C")

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

    # Function_101_A16C end

    def Function_102_A1CD(): pass

    label("Function_102_A1CD")

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

    # Function_102_A1CD end

    def Function_103_A5C3(): pass

    label("Function_103_A5C3")

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

    # Function_103_A5C3 end

    def Function_104_A610(): pass

    label("Function_104_A610")

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

    # Function_104_A610 end

    def Function_105_A653(): pass

    label("Function_105_A653")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A6C4")
    OP_7D(0xFF, 0xFF, 0xC8, 0x0, 0x64)
    Sleep(200)
    OP_7D(0xC8, 0xC8, 0xC8, 0x0, 0xC8)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A696")
    Sleep(500)
    Jump("loc_A6BF")

    label("loc_A696")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A6AD")
    Sleep(300)
    Jump("loc_A6BF")

    label("loc_A6AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A6BF")
    Sleep(100)

    label("loc_A6BF")

    Jump("Function_105_A653")

    label("loc_A6C4")

    Return()

    # Function_105_A653 end

    def Function_106_A6C5(): pass

    label("Function_106_A6C5")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A89F")
    SetScenarioFlags(0x5C, 4)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_A8A8")

    label("loc_A89F")

    NewScene("c0410", 101, 0, 0)
    IdleLoop()

    label("loc_A8A8")

    Return()

    # Function_106_A6C5 end

    def Function_107_A8A9(): pass

    label("Function_107_A8A9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A91A")
    OP_7D(0xC8, 0xFF, 0xFF, 0x0, 0x64)
    Sleep(200)
    OP_7D(0xA0, 0xC8, 0xC8, 0x0, 0xC8)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A8EC")
    Sleep(500)
    Jump("loc_A915")

    label("loc_A8EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A903")
    Sleep(300)
    Jump("loc_A915")

    label("loc_A903")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A915")
    Sleep(100)

    label("loc_A915")

    Jump("Function_107_A8A9")

    label("loc_A91A")

    Return()

    # Function_107_A8A9 end

    def Function_108_A91B(): pass

    label("Function_108_A91B")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABC9")
    SetScenarioFlags(0x5C, 5)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_ABD2")

    label("loc_ABC9")

    NewScene("c0410", 101, 0, 0)
    IdleLoop()

    label("loc_ABD2")

    Return()

    # Function_108_A91B end

    def Function_109_ABD3(): pass

    label("Function_109_ABD3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC44")
    OP_7D(0xC8, 0xFF, 0xC8, 0x0, 0x64)
    Sleep(200)
    OP_7D(0x8C, 0xC8, 0x8C, 0x0, 0xC8)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC16")
    Sleep(500)
    Jump("loc_AC3F")

    label("loc_AC16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC2D")
    Sleep(300)
    Jump("loc_AC3F")

    label("loc_AC2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC3F")
    Sleep(100)

    label("loc_AC3F")

    Jump("Function_109_ABD3")

    label("loc_AC44")

    Return()

    # Function_109_ABD3 end

    def Function_110_AC45(): pass

    label("Function_110_AC45")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE1F")
    SetScenarioFlags(0x5C, 6)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_AE28")

    label("loc_AE1F")

    NewScene("c0410", 101, 0, 0)
    IdleLoop()

    label("loc_AE28")

    Return()

    # Function_110_AC45 end

    def Function_111_AE29(): pass

    label("Function_111_AE29")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B15F")
    SetScenarioFlags(0x5C, 7)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_B188")

    label("loc_B15F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_B176")
    NewScene("c0410", 106, 0, 0)
    IdleLoop()
    Jump("loc_B188")

    label("loc_B176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_B188")
    NewScene("c0410", 108, 0, 0)
    IdleLoop()

    label("loc_B188")

    Return()

    # Function_111_AE29 end

    def Function_112_B189(): pass

    label("Function_112_B189")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4DE")
    SetScenarioFlags(0x5D, 0)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_B507")

    label("loc_B4DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_B4F5")
    NewScene("c0410", 106, 0, 0)
    IdleLoop()
    Jump("loc_B507")

    label("loc_B4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_B507")
    NewScene("c0410", 108, 0, 0)
    IdleLoop()

    label("loc_B507")

    Return()

    # Function_112_B189 end

    def Function_113_B508(): pass

    label("Function_113_B508")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B87E")
    SetScenarioFlags(0x5D, 1)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_B8A7")

    label("loc_B87E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_B895")
    NewScene("c0410", 106, 0, 0)
    IdleLoop()
    Jump("loc_B8A7")

    label("loc_B895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_B8A7")
    NewScene("c0410", 108, 0, 0)
    IdleLoop()

    label("loc_B8A7")

    Return()

    # Function_113_B508 end

    def Function_114_B8A8(): pass

    label("Function_114_B8A8")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA98")
    SetScenarioFlags(0x5D, 2)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_BAA1")

    label("loc_BA98")

    NewScene("c0410", 115, 0, 0)
    IdleLoop()

    label("loc_BAA1")

    Return()

    # Function_114_B8A8 end

    def Function_115_BAA2(): pass

    label("Function_115_BAA2")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCA4")
    SetScenarioFlags(0x5D, 3)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_BCAD")

    label("loc_BCA4")

    NewScene("c0410", 115, 0, 0)
    IdleLoop()

    label("loc_BCAD")

    Return()

    # Function_115_BAA2 end

    def Function_116_BCAE(): pass

    label("Function_116_BCAE")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF2A")
    SetScenarioFlags(0x5D, 4)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_BF33")

    label("loc_BF2A")

    NewScene("c0410", 115, 0, 0)
    IdleLoop()

    label("loc_BF33")

    Return()

    # Function_116_BCAE end

    def Function_117_BF34(): pass

    label("Function_117_BF34")

    SetChrChipByIndex(0xFE, 0x33)
    Sound(808, 0, 100, 0)
    OP_96(0xFE, 0xFFFF95F2, 0x3B60, 0x1662, 0x2710, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    Sound(533, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)

    def lambda_BF75():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BF75)
    OP_96(0xFE, 0xFFFF95F2, 0x3B60, 0x1A4A, 0x1F40, 0x0)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    PlayEffect(0x5, 0xFF, 0xFE, 0x40, -1300, 2000, 0, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    Sound(511, 0, 100, 0)
    Sound(830, 0, 100, 0)
    Sound(1876, 255, 100, 1)    #voice#Earnest
    BeginChrThread(0x18, 0, 0, 118)
    SetChrFlags(0x20, 0x20)
    SetChrFlags(0x20, 0x1000)

    def lambda_C000():
        OP_96(0xFE, 0xFFFF969C, 0x3B60, 0x23A0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_C000)
    SetChrChipByIndex(0x20, 0x2F)
    SetChrSubChip(0x20, 0x0)
    OP_96(0xFE, 0xFFFF95F2, 0x3B60, 0x1A4A, 0x1388, 0x0)
    Sound(532, 0, 100, 0)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x32)

    def lambda_C044():

        label("loc_C044")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_C044")

    QueueWorkItem2(0xFE, 2, lambda_C044)
    Return()

    # Function_117_BF34 end

    def Function_118_C052(): pass

    label("Function_118_C052")

    SetChrFlags(0x18, 0x4)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    BeginChrThread(0x18, 3, 0, 18)
    OP_9D(0x18, 0xFFFF8D64, 0x38A4, 0x292C, 0xBB8, 0xBB8)
    Sound(878, 0, 100, 0)
    SetChrFlags(0x18, 0x2)
    SetChrSubChip(0x18, 0x4)
    Return()

    # Function_118_C052 end

    def Function_119_C08E(): pass

    label("Function_119_C08E")

    OP_95(0xFE, -25200, 15200, 6000, 5000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_119_C08E end

    def Function_120_C0AA(): pass

    label("Function_120_C0AA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C11B")
    OP_7D(0x50, 0xFF, 0xFF, 0x0, 0x64)
    Sleep(200)
    OP_7D(0x50, 0xC8, 0xC8, 0x0, 0xC8)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C0ED")
    Sleep(500)
    Jump("loc_C116")

    label("loc_C0ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C104")
    Sleep(300)
    Jump("loc_C116")

    label("loc_C104")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C116")
    Sleep(100)

    label("loc_C116")

    Jump("Function_120_C0AA")

    label("loc_C11B")

    Return()

    # Function_120_C0AA end

    def Function_121_C11C(): pass

    label("Function_121_C11C")

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

    def lambda_C368():
        OP_96(0xFE, 0xFFFF976E, 0x3B60, 0xB68, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C368)

    def lambda_C382():
        OP_96(0xFE, 0xFFFF9C50, 0x3B60, 0xA5A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C382)
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
        "#0110F啊……！？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x20, 0x3)
    Sleep(300)

    #C0033
    ChrTalk(
        0x20,
        "#2611F#5P唔……！？\x02",
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
        "#2614F呜……！\x02",
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

    def lambda_C511():
        OP_9D(0xFE, 0xFFFF9494, 0x3B60, 0x2968, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_C511)

    def lambda_C52E():
        OP_9D(0xFE, 0xFFFF92A0, 0x3B60, 0x27D8, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_C52E)
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
        "#0107F外公……！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#0007F可恶……竟然连手枪这种东西都用上了！？\x02",
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
            "#0607F这、这是……\x01",
            "这究竟是怎么回事！？\x02",
        )
    )

    CloseMessageWindow()
    MoveCamera(24, 31, 0, 30000)

    #C0038
    ChrTalk(
        0x20,
        (
            "#2613F呵呵，真是没想到，\x01",
            "你们竟然会出现在这种地方……\x02\x03",

            "#2610F哎呀呀……\x01",
            "女神可真爱和人开玩笑啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#0108F阿奈斯特先生……\x01",
            "你到底为什么要这样做……！\x02\x03",

            "#0107F一直都那样尊敬外公，\x01",
            "支持着外公的你，为什么会……！\x02",
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
            "#2613F……艾莉，我和你一样啊。\x02\x03",

            "我也早已经对这种现状\x01",
            "感到厌烦，不想再继续忍受了……\x02\x03",

            "#2611F说到底，要想改变现状，\x01",
            "就只有归顺更强的人……\x02\x03",

            "#2614F所以，我才会采取这种行动！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#0003F所以你才盗用『银』的名号，\x01",
            "给伊莉娅小姐发送了恐吓信……\x02\x03",

            "#0013F让我们都以为『银』会出现，\x01",
            "而你就借此机会来谋杀市长……！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x1C,
        (
            "#0603F……哼，原来是这么回事吗。\x02\x03",

            "#0610F不过你这家伙未免也\x01",
            "太小看我们了吧……！\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x20,
        (
            "#2613F哈哈，就算是搜查一科，\x01",
            "也不过只是群无能的警官罢了。\x02\x03",

            "鲁巴彻也好，黑月也好，\x01",
            "真正的『银』也好……\x02\x03",

            "#2610F全都只是在我的掌心上\x01",
            "跳舞的木偶而已！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x1C,
        "#0601F唔……\x02",
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
            "#0603F──老老实实\x01",
            "把枪扔掉吧。\x02\x03",

            "#0601F现在收手的话，还可以算你是未遂。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x20,
        (
            "#2613F#5P呵呵，那是我的台词啊。\x02\x03",

            "#2610F自治州的代表之一，\x01",
            "这个老东西的命……\x02\x03",

            "将会在你们的眼前被我\x01",
            "夺走，这也无所谓吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        "#0106F住手啊……！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x1C,
        "#0610F嘁……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x20,
        (
            "#2610F#5P你们不希望让孙女\x01",
            "亲眼目睹外公死掉的瞬间吧？\x02\x03",

            "这样的话，就请各位都退到那边的\x01",
            "墙角，给我空出来一条路来如何……？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#0003F……你打算做什么？\x02\x03",

            "#0001F就算你逃得了一时\x01",
            "也逃不了一世。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0051
    ChrTalk(
        0x20,
        (
            "#2614F#5P#4S吵死了！住嘴！\x01",
            "你们只需要照我说的去做就行了！\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#0013F呜……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-27030, 16850, 6000, 4000)

    def lambda_CBC2():

        label("loc_CBC2")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_CBC2")

    QueueWorkItem2(0x101, 2, lambda_CBC2)

    def lambda_CBD4():

        label("loc_CBD4")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_CBD4")

    QueueWorkItem2(0x102, 2, lambda_CBD4)

    def lambda_CBE6():

        label("loc_CBE6")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_CBE6")

    QueueWorkItem2(0x1C, 2, lambda_CBE6)
    ClearChrFlags(0x1C, 0x20)
    ClearChrFlags(0x1C, 0x2)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrSubChip(0x1C, 0x0)
    Sound(531, 0, 100, 0)

    def lambda_CC10():
        OP_96(0xFE, 0xFFFF9D90, 0x3B60, 0xE74, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_CC10)
    Sleep(500)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0xFF)
    Sound(804, 0, 100, 0)

    def lambda_CC41():
        OP_96(0xFE, 0xFFFF9B9C, 0x3B60, 0x14B4, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CC41)
    Sleep(500)

    def lambda_CC5E():
        OP_96(0xFE, 0xFFFFA04C, 0x3B60, 0x16A8, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CC5E)
    WaitChrThread(0x1C, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7505", 0)

    #C0053
    ChrTalk(
        0x20,
        "#2613F#5P#N……很好。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x1F, 0x20)
    SetChrFlags(0x1F, 0x1000)

    def lambda_CCA9():

        label("loc_CCA9")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_CCA9")

    QueueWorkItem2(0x20, 1, lambda_CCA9)

    def lambda_CCBB():
        OP_97(0x20, 0x0, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_CCBB)

    def lambda_CCD5():
        OP_98(0x1F, 0x0, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_CCD5)
    WaitChrThread(0x20, 0)
    EndChrThread(0x20, 0x1)
    TurnDirection(0x20, 0x101, 500)

    #C0054
    ChrTalk(
        0x20,
        "#2614F#5P那就还给你们吧！\x02",
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

    def lambda_CD6D():
        OP_96(0x1F, 0xFFFF9B9C, 0x3B60, 0x15E0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_CD6D)
    BeginChrThread(0x1F, 3, 0, 122)
    ClearChrFlags(0x20, 0x2)
    ClearChrFlags(0x20, 0x20)
    ClearChrFlags(0x20, 0x1000)
    SetChrChipByIndex(0x20, 0x2E)
    Sound(1904, 255, 100, 0)    #voice#Earnest

    def lambda_CDA6():
        OP_95(0x20, -26690, 15200, 2410, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_CDA6)
    Sound(819, 0, 100, 0)
    OP_96(0x101, 0xFFFF9C00, 0x3B60, 0x1388, 0xFA0, 0x0)
    WaitChrThread(0x20, 0)

    def lambda_CDDE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_CDDE)

    def lambda_CDEF():
        OP_95(0xFE, -26690, 15200, 1000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_CDEF)
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
        "#0107F#11P外公……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x20, 700)

    #C0056
    ChrTalk(
        0x101,
        "#0007F#5P站住……！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0x32)
    Sound(808, 0, 100, 0)
    OP_95(0x101, -26690, 15200, 2410, 6000, 0x0)

    def lambda_CEC1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CEC1)

    def lambda_CED2():
        OP_95(0xFE, -26690, 15200, 1000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CED2)

    #C0057
    ChrTalk(
        0x1C,
        "#0607F#5P怎么会让你逃掉……！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x1C, 0x23)
    Sound(531, 0, 100, 0)
    OP_95(0x1C, -26690, 15200, 2410, 6000, 0x0)

    def lambda_CF2D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_CF2D)

    def lambda_CF3E():
        OP_95(0xFE, -26690, 15200, 1000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_CF3E)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1F9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5E, 1)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_121_C11C end

    def Function_122_CF74(): pass

    label("Function_122_CF74")

    WaitChrThread(0xFE, 0)
    SetChrSubChip(0x1F, 0x2)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    Return()

    # Function_122_CF74 end

    def Function_123_CF8E(): pass

    label("Function_123_CF8E")

    OP_93(0x8, 0x87, 0x0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    SetChrPos(0x8, -500, 5500, 25000, 135)

    def lambda_CFB3():

        label("loc_CFB3")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0x320, 0x3)
        Yield()
        Jump("loc_CFB3")

    QueueWorkItem2(0x8, 2, lambda_CFB3)
    Sleep(1)
    OP_96(0x8, 0xFFFFFE0C, 0x2BC0, 0x61A8, 0x12C, 0x0)
    EndChrThread(0x8, 0x2)
    BeginChrThread(0x8, 2, 0, 7)
    ClearChrFlags(0x8, 0x1)
    OP_9D(0x8, 0xFFFFFE0C, 0x300C, 0x61A8, 0x7D0, 0x7D0)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x24)

    label("loc_D014")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D032")
    OP_A1(0x8, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("loc_D014")

    label("loc_D032")

    Return()

    # Function_123_CF8E end

    def Function_124_D033(): pass

    label("Function_124_D033")

    OP_93(0x9, 0xE1, 0x0)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x2)
    SetChrPos(0x9, 500, 5500, 25000, 225)

    def lambda_D058():

        label("loc_D058")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0x320, 0x3)
        Yield()
        Jump("loc_D058")

    QueueWorkItem2(0x9, 2, lambda_D058)
    Sleep(1)
    OP_96(0x9, 0x1F4, 0x2BC0, 0x61A8, 0x12C, 0x0)
    EndChrThread(0x9, 0x2)
    BeginChrThread(0x9, 2, 0, 15)
    ClearChrFlags(0x9, 0x1)
    OP_9D(0x9, 0x1F4, 0x2EE0, 0x61A8, 0x7D0, 0x7D0)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x2E)
    SetChrSubChip(0x9, 0x6)

    label("loc_D0BD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D0DB")
    OP_A1(0x9, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("loc_D0BD")

    label("loc_D0DB")

    Return()

    # Function_124_D033 end

    def Function_125_D0DC(): pass

    label("Function_125_D0DC")

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

    def lambda_D81D():
        OP_96(0x18, 0x0, 0x2710, 0x61A8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_D81D)
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

    def lambda_D917():
        OP_96(0x19, 0x0, 0x546, 0x5DC0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_D917)
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

    # Function_125_D0DC end

    def Function_126_D962(): pass

    label("Function_126_D962")

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

    # Function_126_D962 end

    SaveToFile()

Try(main)
