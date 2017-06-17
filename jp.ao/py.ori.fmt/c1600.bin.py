from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1600.bin",                # FileName
        "c1600",                    # MapName
        "c1600",                    # Location
        0x00B2,                     # MapIndex
        "ed7550",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x01',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 178, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1600",                  # 0
        "ジョーイ",               # 1
        "シズク",                 # 2
        "ヨナ",                   # 3
        "ロバーツ主任",           # 4
        "ディーター市長",         # 5
        "戦鬼シグムント",         # 6
        "シャーリィ",             # 7
        "ヴァルド",               # 8
        "キーア",                 # 9
        "マリアベル",             # 10
        "アリアンロード",         # 11
        "ノバルティス博士",       # 12
        "道化師カンパネルラ",     # 13
        "セルゲイ課長",           # 14
        "飛空挺",                 # 15
        "飛空挺",                 # 16
        "飛空挺影",               # 17
        "飛空挺影",               # 18
        "帝国系テロリスト",       # 19
        "帝国系テロリスト",       # 20
        "帝国系テロリスト",       # 21
        "帝国系テロリスト",       # 22
        "帝国系テロリスト",       # 23
        "帝国系テロリスト",       # 24
        "帝国系テロリスト",       # 25
        "共和国系テロリスト",     # 26
        "共和国系テロリスト",     # 27
        "共和国系テロリスト",     # 28
        "共和国系テロリスト",     # 29
        "共和国系テロリスト",     # 30
        "共和国系テロリスト",     # 31
        "共和国系テロリスト",     # 32
        "アイオーン",             # 33
        "アイオーン",             # 34
        "アイオーン",             # 35
        "メルカバ",               # 36
        "映像",                   # 37
        "映像",                   # 38
        "映像",                   # 39
        "映像",                   # 40
        "映像",                   # 41
        "映像",                   # 42
        "SE制御",                 # 43
        "bc1600",                 # 44
    ))

    ATBonus("ATBonus_6D4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_794", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_798", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_79C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7B0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_774", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_778", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_77C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_780", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_784", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_788", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_78C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_790", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_7B4", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bc1600", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_794", "MonsterBattlePostion_774", "ed7554", "ed7554", "ATBonus_6D4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch27600.itc",                   # 02
        "apl/ch51731.itc",                   # 03
        "chr/ch05410.itc",                   # 04
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

    DeclNpc(-119,    0,       22069,   0,    389,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(8680,    0,       -16479,  135,  389,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(32200,   -4400,   -27850,  75,   453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(28399,   -4400,   -27750,  45,   453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 34,  22.0,                  -23.0,                 -5.400000095367432,    625.0,                 [0.14142131805419922,  0.07071070373058319,   -0.0,                  0.0,                   -0.14142140746116638,  0.07071065902709961,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -6.363961219787598,    0.07070967555046082,   1.0800000429153442,    1.0])
    DeclEvent(0x0000, 0, 62,  0.0,                   -22.0,                 -1.0,                  156.25,                [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  4.400000095367432,     0.20000000298023224,   1.0])

    DeclActor(0,       0,       0,       1500,    0,       1500,    0,       0x007C, 0,  93, 0x0000)

    ChipFrameInfo(2420, 0)                                       # 0

    ScpFunction((
        "Function_0_974",          # 00, 0
        "Function_1_A24",          # 01, 1
        "Function_2_B80",          # 02, 2
        "Function_3_D5F",          # 03, 3
        "Function_4_1334",         # 04, 4
        "Function_5_1597",         # 05, 5
        "Function_6_16E2",         # 06, 6
        "Function_7_1960",         # 07, 7
        "Function_8_2075",         # 08, 8
        "Function_9_23BF",         # 09, 9
        "Function_10_2FD3",        # 0A, 10
        "Function_11_3028",        # 0B, 11
        "Function_12_307D",        # 0C, 12
        "Function_13_30D2",        # 0D, 13
        "Function_14_3142",        # 0E, 14
        "Function_15_3197",        # 0F, 15
        "Function_16_31EC",        # 10, 16
        "Function_17_321C",        # 11, 17
        "Function_18_3284",        # 12, 18
        "Function_19_32C1",        # 13, 19
        "Function_20_3305",        # 14, 20
        "Function_21_3349",        # 15, 21
        "Function_22_338D",        # 16, 22
        "Function_23_33D1",        # 17, 23
        "Function_24_3415",        # 18, 24
        "Function_25_3459",        # 19, 25
        "Function_26_349D",        # 1A, 26
        "Function_27_3A24",        # 1B, 27
        "Function_28_3A84",        # 1C, 28
        "Function_29_3AE4",        # 1D, 29
        "Function_30_3C07",        # 1E, 30
        "Function_31_3D13",        # 1F, 31
        "Function_32_3DE2",        # 20, 32
        "Function_33_3EB1",        # 21, 33
        "Function_34_429F",        # 22, 34
        "Function_35_59C8",        # 23, 35
        "Function_36_5AC0",        # 24, 36
        "Function_37_5ADF",        # 25, 37
        "Function_38_5AFE",        # 26, 38
        "Function_39_5B5D",        # 27, 39
        "Function_40_5B7C",        # 28, 40
        "Function_41_5BC4",        # 29, 41
        "Function_42_5C11",        # 2A, 42
        "Function_43_70D9",        # 2B, 43
        "Function_44_73F6",        # 2C, 44
        "Function_45_74AA",        # 2D, 45
        "Function_46_74FA",        # 2E, 46
        "Function_47_7550",        # 2F, 47
        "Function_48_760A",        # 30, 48
        "Function_49_76B3",        # 31, 49
        "Function_50_779E",        # 32, 50
        "Function_51_77DE",        # 33, 51
        "Function_52_7861",        # 34, 52
        "Function_53_80CC",        # 35, 53
        "Function_54_8859",        # 36, 54
        "Function_55_8970",        # 37, 55
        "Function_56_91CA",        # 38, 56
        "Function_57_933E",        # 39, 57
        "Function_58_937D",        # 3A, 58
        "Function_59_9815",        # 3B, 59
        "Function_60_9844",        # 3C, 60
        "Function_61_98E1",        # 3D, 61
        "Function_62_98F8",        # 3E, 62
        "Function_63_C2C9",        # 3F, 63
        "Function_64_C2F7",        # 40, 64
        "Function_65_C358",        # 41, 65
        "Function_66_C3B9",        # 42, 66
        "Function_67_C3DE",        # 43, 67
        "Function_68_CEBE",        # 44, 68
        "Function_69_CED1",        # 45, 69
        "Function_70_CF06",        # 46, 70
        "Function_71_11240",       # 47, 71
        "Function_72_11265",       # 48, 72
        "Function_73_112CC",       # 49, 73
        "Function_74_11333",       # 4A, 74
        "Function_75_1139A",       # 4B, 75
        "Function_76_11401",       # 4C, 76
        "Function_77_11468",       # 4D, 77
        "Function_78_114AA",       # 4E, 78
        "Function_79_114CC",       # 4F, 79
        "Function_80_114E8",       # 50, 80
        "Function_81_11504",       # 51, 81
        "Function_82_11520",       # 52, 82
        "Function_83_1153C",       # 53, 83
        "Function_84_11558",       # 54, 84
        "Function_85_1157C",       # 55, 85
        "Function_86_11587",       # 56, 86
        "Function_87_11592",       # 57, 87
        "Function_88_1159D",       # 58, 88
        "Function_89_115A8",       # 59, 89
        "Function_90_115B3",       # 5A, 90
        "Function_91_115BE",       # 5B, 91
        "Function_92_11639",       # 5C, 92
        "Function_93_11651",       # 5D, 93
        "Function_94_116B2",       # 5E, 94
    ))


    def Function_0_974(): pass

    label("Function_0_974")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_9AC"),
        (1, "loc_9B8"),
        (2, "loc_9C4"),
        (3, "loc_9D0"),
        (4, "loc_9DC"),
        (5, "loc_9E8"),
        (6, "loc_9F4"),
        (SWITCH_DEFAULT, "loc_A00"),
    )


    label("loc_9AC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9B8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9C4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9D0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9DC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9E8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_A00")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_A0C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A23")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_A23")

    Return()

    # Function_0_974 end

    def Function_1_A24(): pass

    label("Function_1_A24")

    SetMapObjFlags(0x5, 0x2000000)
    SetMapObjFlags(0x14, 0x2000000)
    SetMapObjFlags(0x9, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0x13, 0x2000000)
    SetMapObjFlags(0x15, 0x2000000)
    SetMapObjFlags(0x17, 0x2000000)
    SetMapObjFlags(0x6, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0x16, 0x2000000)
    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)
    SetMapObjFlags(0xF, 0x2000000)
    SetMapObjFlags(0x10, 0x2000000)
    SetMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0x12, 0x2000000)
    SetMapObjFlags(0x18, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_AB7")
    ClearMapObjFlags(0x6, 0x2000000)
    ClearMapObjFlags(0x7, 0x2000000)
    ClearMapObjFlags(0xB, 0x2000000)
    ClearMapObjFlags(0xC, 0x2000000)

    label("loc_AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_AC6")
    ClearMapObjFlags(0x5, 0x2000000)

    label("loc_AC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_AE1")
    ClearMapObjFlags(0x5, 0x2000000)
    ClearMapObjFlags(0x9, 0x2000000)
    ClearMapObjFlags(0xA, 0x2000000)

    label("loc_AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_AF0")
    ClearMapObjFlags(0x5, 0x2000000)

    label("loc_AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_B0B")
    ClearMapObjFlags(0x5, 0x2000000)
    ClearMapObjFlags(0x9, 0x2000000)
    ClearMapObjFlags(0x13, 0x2000000)

    label("loc_B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2B")
    ClearMapObjFlags(0x5, 0x2000000)
    ClearMapObjFlags(0x14, 0x2000000)
    ClearMapObjFlags(0x18, 0x2000000)

    label("loc_B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_B70")
    ClearMapObjFlags(0xD, 0x2000000)
    ClearMapObjFlags(0xE, 0x2000000)
    ClearMapObjFlags(0xF, 0x2000000)
    ClearMapObjFlags(0x10, 0x2000000)
    ClearMapObjFlags(0x11, 0x2000000)
    ClearMapObjFlags(0x12, 0x2000000)
    ClearMapObjFlags(0x15, 0x2000000)
    ClearMapObjFlags(0x17, 0x2000000)
    ClearMapObjFlags(0x16, 0x2000000)
    SetMapObjFlags(0x18, 0x2000000)

    label("loc_B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_B7F")
    ClearMapObjFlags(0x16, 0x2000000)

    label("loc_B7F")

    Return()

    # Function_1_A24 end

    def Function_2_B80(): pass

    label("Function_2_B80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BC5")
    SetChrChipByIndex(0xC, 0x3)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, 0, 180)
    OP_8E(0xC, "ディーター大統領")

    label("loc_BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_BDD")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    Jump("loc_C43")

    label("loc_BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_BF5")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    Jump("loc_C43")

    label("loc_BF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C03")
    Jump("loc_C43")

    label("loc_C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C11")
    Jump("loc_C43")

    label("loc_C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C29")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    Jump("loc_C43")

    label("loc_C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C43")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_93(0x8, 0x13B, 0x0)

    label("loc_C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_C57")
    ClearScenarioFlags(0x22, 0)
    Event(0, 8)
    Jump("loc_D48")

    label("loc_C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_C6B")
    ClearScenarioFlags(0x22, 1)
    Event(0, 9)
    Jump("loc_D48")

    label("loc_C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_C7F")
    ClearScenarioFlags(0x22, 2)
    Event(0, 26)
    Jump("loc_D48")

    label("loc_C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_C96")
    ClearScenarioFlags(0x22, 3)
    SetScenarioFlags(0x0, 5)
    Event(0, 42)
    Jump("loc_D48")

    label("loc_C96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_CAA")
    ClearScenarioFlags(0x22, 4)
    Event(0, 52)
    Jump("loc_D48")

    label("loc_CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_CBE")
    ClearScenarioFlags(0x22, 5)
    Event(0, 53)
    Jump("loc_D48")

    label("loc_CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_CD2")
    ClearScenarioFlags(0x22, 6)
    Event(0, 54)
    Jump("loc_D48")

    label("loc_CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_CE6")
    ClearScenarioFlags(0x22, 7)
    Event(0, 55)
    Jump("loc_D48")

    label("loc_CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_CFA")
    ClearScenarioFlags(0x23, 0)
    Event(0, 56)
    Jump("loc_D48")

    label("loc_CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_D0E")
    ClearScenarioFlags(0x23, 1)
    Event(0, 58)
    Jump("loc_D48")

    label("loc_D0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_D22")
    ClearScenarioFlags(0x23, 2)
    Event(0, 67)
    Jump("loc_D48")

    label("loc_D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_D39")
    ClearScenarioFlags(0x23, 3)
    SetScenarioFlags(0x0, 4)
    Event(0, 70)
    Jump("loc_D48")

    label("loc_D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_D48")
    ClearScenarioFlags(0x23, 4)
    Event(0, 94)

    label("loc_D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5E")
    SetMapFlags(0x10000000)
    Event(0, 33)

    label("loc_D5E")

    Return()

    # Function_2_B80 end

    def Function_3_D5F(): pass

    label("Function_3_D5F")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x4B0)
    OP_F3(100000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D9C")
    SetMapObjFrame(0xFF, "CS00", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CS01", 0x1, 0x2)
    Jump("loc_DA8")

    label("loc_D9C")

    SetMapObjFrame(0xFF, "CS02", 0x1, 0x2)

    label("loc_DA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_DBF")
    Sound(132, 1, 50, 0)
    ClearScenarioFlags(0x0, 5)
    Jump("loc_DDE")

    label("loc_DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD8")
    Sound(132, 1, 50, 0)
    Jump("loc_DDE")

    label("loc_DD8")

    Sound(132, 1, 100, 0)

    label("loc_DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_DF8")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 4)
    Jump("loc_E26")

    label("loc_DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E14")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E26")

    label("loc_E14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E26")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E26")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E3E")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_E3E")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E56")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_E56")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB8")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x0, 0x1)

    label("loc_EB8")

    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1012")
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "open")
    OP_70(0x1, 0x12D)
    OP_70(0x2, 0x12D)
    OP_70(0x3, 0x12D)
    OP_70(0x4, 0x12D)
    Jump("loc_1136")

    label("loc_1012")

    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "close")
    OP_70(0x1, 0x0)
    OP_70(0x2, 0x0)
    OP_70(0x3, 0x0)
    OP_70(0x4, 0x0)

    label("loc_1136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1159")
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x8, 0x20)
    OP_70(0x8, 0x2)
    Jump("loc_115F")

    label("loc_1159")

    SetMapObjFlags(0x8, 0x4)

    label("loc_115F")

    SetMapObjFrame(0xFF, "last", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1235")
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    SetChrPos(0x28, 0, 0, 6500, 180)
    OP_D5(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x42E)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    OP_78(0x14, 0x29)
    SetChrPos(0x29, 0, 0, 6500, 180)
    OP_D5(0x29, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x14, 0x1000)
    SetMapObjFlags(0x14, 0x4)
    OP_74(0x14, 0x1E)
    OP_70(0x14, 0x42E)
    SetChrFlags(0x29, 0x1)
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12CF")
    LoadEffect(0x9, "map/mprain01.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "sky00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)

    label("loc_12CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1333")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x12C, 0x384, 0x0)
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)

    label("loc_1333")

    Return()

    # Function_3_D5F end

    def Function_4_1334(): pass

    label("Function_4_1334")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1345")
    Jump("loc_1593")

    label("loc_1345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_14F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1469")

    #C0001
    ChrTalk(
        0xFE,
        (
            "ふう……やっぱり\x01",
            "この場所は何度来てもいいなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "今日はここで本を読もうと\x01",
            "思っていたけど、この景色だけで\x01",
            "胸が一杯になってしまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "よかったらこの本、\x01",
            "君たちが呼んでくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2F7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2F7, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x189, 1)
    Jump("loc_14EC")

    label("loc_1469")


    #C0005
    ChrTalk(
        0xFE,
        (
            "ふう……やっぱり\x01",
            "この場所は何度来てもいいなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "ここで景色をみていると、\x01",
            "あの襲撃事件の恐怖も\x01",
            "落ち着いてくる気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14EC")

    Jump("loc_1593")

    label("loc_14F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1593")

    #C0007
    ChrTalk(
        0xFE,
        (
            "ここからじゃ全然見えないけど、\x01",
            "あっちの方角では今まさに警備隊が\x01",
            "戦っているんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "こんなに美しい景色だってのに……\x01",
            "ホント悲しいことだよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1593")

    TalkEnd(0xFE)
    Return()

    # Function_4_1334 end

    def Function_5_1597(): pass

    label("Function_5_1597")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_164D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B9")
    TalkEnd(0xFE)
    Call(0, 7)
    Return()

    label("loc_15B9")


    #C0009
    ChrTalk(
        0x9,
        (
            "#11223F……皆さんなら、\x01",
            "きっと大丈夫だと思います。\x02\x03",

            "#11222Fどうか、キーアちゃんを……\x01",
            "わたしの大切なお友達を、\x01",
            "よろしくお願いします……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16DE")

    label("loc_164D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_16DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1668")
    Call(0, 6)
    Jump("loc_16DE")

    label("loc_1668")


    #C0010
    ChrTalk(
        0x9,
        (
            "#11228F皆さん、どうかお父さんを……\x01",
            "キーアちゃんを\x01",
            "よろしくお願いします。\x02\x03",

            "#11223Fわたし、ここで待ってますから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DE")

    TalkEnd(0xFE)
    Return()

    # Function_5_1597 end

    def Function_6_16E2(): pass

    label("Function_6_16E2")

    OP_93(0x9, 0x87, 0x0)

    #C0011
    ChrTalk(
        0x9,
        "#11221Fお父さん、キーアちゃん……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00005Fシズクちゃん……\x01",
            "こんな所にいたのか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x0, 500)

    #C0013
    ChrTalk(
        0x9,
        (
            "#11220Fみなさん……\x01",
            "はい、あの《大樹》を\x01",
            "見ていたんです。\x02\x03",

            "#11230Fお父さんとキーアちゃんは、\x01",
            "本当にあんな所に……？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x103,
        "#00203F……ええ、間違いありません。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        (
            "#00108F《大樹》のどこにいるかは\x01",
            "まだ分からないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        "#11223Fそうですか………………\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#00003F……シズクちゃん、待っててくれ。\x02\x03",

            "#00001Fアリオスさんとキーアは、\x01",
            "絶対に俺たちが連れ戻してみせる。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x104,
        "#00302Fああ、だから心配すんな。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        (
            "#11223F……はい。\x02\x03",

            "#11221F皆さん、どうかお父さんを……\x01",
            "キーアちゃんを\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x87, 0x0)
    SetScenarioFlags(0x1AF, 2)
    Return()

    # Function_6_16E2 end

    def Function_7_1960(): pass

    label("Function_7_1960")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x9, 0xFF)
    OP_68(7690, 1100, -15570, 0)
    MoveCamera(110, 28, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9990, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 7530, 0, -15000, 135)
    SetChrPos(0x1, 9360, 0, -14520, 180)
    SetChrPos(0x2, 6860, 0, -16500, 90)
    SetChrPos(0x3, 8570, 0, -13930, 180)
    SetChrPos(0x4, 5900, 0, -15300, 110)
    SetChrPos(0x5, 7050, 0, -13540, 155)
    OP_93(0x9, 0x13B, 0x0)
    SetChrName("")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちは、\x01",
            "アリオスを打倒したこと……\x02\x03",

            "そして、ガイ殺害の真犯人が\x01",
            "アリオスではなかったことを\x01",
            "シズクに説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(1000, 0)
    OP_0D()

    #C0021
    ChrTalk(
        0x9,
        "#11225F……そうですか……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#6P#00004F……ああ。\x02\x03",

            "#00000Fアリオスさんも、後で必ず\x01",
            "シズクちゃんの元に……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x9,
        "#11233F……う……ぐすっ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0024
    ChrTalk(
        0x9,
        (
            "#11234Fううっ……良かったです……\x02\x03",

            "#11233Fお父さんが、大切な友達を……\x01",
            "ロイドさんのお兄さんを\x01",
            "手に掛けたわけじゃなくて……\x02\x03",

            "#11234Fもし、本当にそうだったら、\x01",
            "お父さん、もう絶対に後戻りなんか\x01",
            "できないんじゃないかって……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        "#6P#00108Fシズクちゃん……\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#6P#00002Fはは……言ったろう？\x01",
            "後戻り出来ないなんて、\x01",
            "そんなことはないってさ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D63")

    #C0027
    ChrTalk(
        0x10A,
        (
            "#6P#00602F……待っていろ。\x01",
            "マクレインは後で必ず\x01",
            "連れて戻ると約束する。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E12")

    label("loc_1D63")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DBC")

    #C0028
    ChrTalk(
        0x109,
        (
            "#6P#10102F待っててね。\x01",
            "アリオスさんは後で必ず\x01",
            "連れて戻るから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E12")

    label("loc_1DBC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E12")

    #C0029
    ChrTalk(
        0x105,
        (
            "#6P#10402Fアリオスさんは\x01",
            "後で必ず連れて戻る。\x01",
            "フフ、約束するよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E12")


    #C0030
    ChrTalk(
        0x9,
        "#11222Fぐすっ……はいっ……！！\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x103,
        (
            "#12P#00202F……これで後は、\x01",
            "キーアを取り戻すだけですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#6P#00309Fおう、シズクちゃんを\x01",
            "笑顔にするためにもな！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F04")

    #C0033
    ChrTalk(
        0x105,
        (
            "#6P#10409Fフフ、こうなったら\x01",
            "何が何でも成し遂げなきゃね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FAC")

    label("loc_1F04")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F54")

    #C0034
    ChrTalk(
        0x109,
        (
            "#6P#10109Fこうなったら、\x01",
            "何が何でも成し遂げましょう！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FAC")

    label("loc_1F54")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FAC")

    #C0035
    ChrTalk(
        0x106,
        (
            "#6P#10709Fこうなったら、\x01",
            "何が何でも成し遂げなければ\x01",
            "いけませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FAC")


    #C0036
    ChrTalk(
        0x9,
        (
            "#11223F……お父さんに勝った皆さんなら、\x01",
            "きっと大丈夫だと思います。\x02\x03",

            "#11227Fどうか、キーアちゃんを……\x01",
            "わたしの大切なお友達を、\x01",
            "よろしくお願いします……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_93(0x9, 0x87, 0x0)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x1AF, 1)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_7_1960 end

    def Function_8_2075(): pass

    label("Function_8_2075")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    OP_68(23800, -43600, 6100, 0)
    MoveCamera(305, 17, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(12000, 0)
    SetChrPos(0x101, 23800, -44600, 6100, 90)
    SetChrPos(0x102, 23800, -44600, 7200, 90)
    SetChrPos(0x109, 23000, -44600, 7000, 90)
    SetChrPos(0x103, 23000, -44600, 5900, 90)
    SetChrPos(0x104, 22200, -44600, 5700, 90)
    SetChrPos(0x105, 23600, -44600, 5100, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 20800, -44600, 7500, 90)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1500, 0)
    MoveCamera(305, 23, 0, 6000)
    OP_6E(1100, 6000)
    SetCameraDistance(82000, 6000)
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(0, -53600, -25000, 0)
    MoveCamera(315, -15, 15, 0)
    OP_6E(1100, 0)
    SetCameraDistance(80000, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrFlags(0xC, 0x8)
    OP_68(0, -73600, -75000, 11000)
    MoveCamera(215, 30, 15, 11000)
    SetCameraDistance(180000, 11000)
    OP_6F(0x79)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("c1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_2075 end

    def Function_9_23BF(): pass

    label("Function_9_23BF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    LoadChrToIndex("apl/ch51259.itc", 0x1F)
    SoundLoad(803)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    SetChrPos(0x101, -19000, -6000, 0, 270)
    SetChrPos(0x102, -19000, -6000, 0, 270)
    SetChrPos(0x103, -19000, -6000, 0, 270)
    SetChrPos(0x104, -19000, -6000, 0, 270)
    SetChrPos(0x109, -19000, -6000, 0, 270)
    SetChrPos(0x105, -19000, -6000, 0, 270)
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
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -19000, -6000, 0, 270)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-20000, -5000, 0, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_68(-23000, -5000, 0, 6000)
    SetCameraDistance(16000, 6000)
    BeginChrThread(0xC, 3, 0, 16)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 10)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 11)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 15)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 14)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 12)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 13)
    WaitChrThread(0x109, 3)

    #C0037
    ChrTalk(
        0x109,
        "#11P#10109Fわああっ……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 3)

    #C0038
    ChrTalk(
        0x105,
        (
            "#11P#10302Fこれは……\x01",
            "さすがに見事だねぇ。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    OP_68(0, 0, 0, 9000)
    MoveCamera(225, 13, 0, 9000)
    OP_6E(900, 9000)
    SetCameraDistance(130000, 9000)
    BeginChrThread(0xC, 3, 0, 17)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 17)
    Sleep(900)
    BeginChrThread(0x109, 3, 0, 17)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 17)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 17)
    OP_6F(0x79)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetChrPos(0x101, -19700, -4400, -20300, 180)
    SetChrPos(0x102, -20300, -4400, -19700, 180)
    SetChrPos(0x103, -20000, -4400, -20000, 180)
    SetChrPos(0x104, -19700, -4400, -20300, 180)
    SetChrPos(0x109, -20300, -4400, -19700, 180)
    SetChrPos(0x105, -20000, -4400, -20000, 180)
    SetChrPos(0xC, -20000, -4400, -20000, 180)
    BeginChrThread(0x101, 0, 0, 18)
    Sleep(1000)
    Fade(1000)
    OP_68(-29000, -3900, -29000, 0)
    MoveCamera(225, 17, 0, 0)
    OP_6E(1100, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    OP_68(-24400, -3900, -38800, 6000)
    MoveCamera(205, 19, 0, 6000)
    SetCameraDistance(23500, 6000)
    OP_6F(0x79)
    WaitChrThread(0x109, 3)

    #C0039
    ChrTalk(
        0x101,
        (
            "#00004F#11Pはは……\x01",
            "言葉も出ないな……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x102,
        "#00102F#11Pええ、そうね……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)

    #C0041
    ChrTalk(
        0x103,
        (
            "#00202F#11P……街がまるで\x01",
            "模型#4Rミニチュア#みたいに見えますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#00309F#11Pいや～、夜はさぞかし\x01",
            "すげぇ景色なんだろうな！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-28800, -3300, -31300, 0)
    MoveCamera(205, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    OP_0D()

    #C0043
    ChrTalk(
        0xC,
        (
            "#12P#02809Fハハ、いずれこの場所は\x01",
            "展望台として市民に\x01",
            "開放しようと考えている。\x02\x03",

            "#02800F政府関係者だけが独占するのは\x01",
            "あまりにも勿体ないからね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28EF():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_28EF)
    Sleep(50)

    def lambda_28FF():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_28FF)
    Sleep(50)

    def lambda_290F():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_290F)
    Sleep(50)

    def lambda_291F():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_291F)
    Sleep(50)

    def lambda_292F():
        TurnDirection(0x105, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_292F)
    Sleep(50)

    def lambda_293F():
        TurnDirection(0x109, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_293F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    def lambda_2964():

        label("loc_2964")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2964")

    QueueWorkItem2(0x101, 2, lambda_2964)

    def lambda_2976():

        label("loc_2976")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2976")

    QueueWorkItem2(0x102, 2, lambda_2976)

    def lambda_2988():

        label("loc_2988")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2988")

    QueueWorkItem2(0x103, 2, lambda_2988)

    def lambda_299A():

        label("loc_299A")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_299A")

    QueueWorkItem2(0x109, 2, lambda_299A)

    def lambda_29AC():

        label("loc_29AC")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_29AC")

    QueueWorkItem2(0x105, 2, lambda_29AC)

    def lambda_29BE():

        label("loc_29BE")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_29BE")

    QueueWorkItem2(0x104, 2, lambda_29BE)

    #C0044
    ChrTalk(
        0x101,
        "#00002F#5Pああ、それはいいですね。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        (
            "#00109F#5Pふふ、キーアちゃんも\x01",
            "ここに連れて来たいわね。\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(500)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0046
    ChrTalk(
        0xC,
        "#12P#02805Fおっと、失礼。\x02",
    )

    CloseMessageWindow()
    OP_93(0xC, 0x5A, 0x1F4)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x10)
    OP_0D()
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    Sleep(300)
    SetChrSubChip(0xC, 0x1)
    Sleep(300)

    #C0047
    ChrTalk(
        0xC,
        (
            "#11P#02801Fああ、私だ。\x02\x03",

            "#02803F……そうか、分かった。\x01",
            "すぐにそちらに向かおう。\x02",
        )
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    SetChrSubChip(0xC, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x2)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    #C0048
    ChrTalk(
        0xC,
        (
            "#12P#02800Fどうやら首脳たちが\x01",
            "タワーに到着したようだ。\x02\x03",

            "申しわけないが\x01",
            "これで失礼させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#00004F#5Pそうですか……\x01",
            "本当にありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x103,
        "#00204F#5Pどうもです。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        "#00309F#5Pいや～、マジ楽しかったッス。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x109,
        "#10102F#5Pいい経験をさせて頂きました！\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xC,
        (
            "#12P#02804Fはは、こちらこそ\x01",
            "いい気分転換をさせてもらったよ。\x02\x03",

            "#02800Fそれでは、また後で。\x01",
            "警備の方は頑張ってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        "#00000F#5Pはい、お任せください。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x105,
        (
            "#10302F#5Pま、推薦分くらいは\x01",
            "頑張らせてもらおうかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        (
            "#00104F#5P──女神#4Rエイドス#のご加護を。\x01",
            "会議の成功、お祈りしてます。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xC,
        "#12P#02809Fハハ、私も祈っているよ。\x02",
    )

    CloseMessageWindow()
    OP_92(0xC, 0xFFFFADF8, 0xFFFFADF8, 0x1F4)
    OP_68(-25800, -3300, -28300, 5000)
    SetCameraDistance(17500, 5000)

    def lambda_2DB9():
        OP_95(0xFE, -21000, -4400, -21000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2DB9)
    WaitChrThread(0xC, 1)
    OP_6F(0x79)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0xC, 0x80)
    Fade(500)
    OP_68(-28350, -3300, -32000, 0)
    MoveCamera(205, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    #C0058
    ChrTalk(
        0x101,
        (
            "#00000F#5Pさてと、俺たちも\x01",
            "ダドリーさんの所に行くか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2E6F():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2E6F)
    Sleep(50)

    def lambda_2E7F():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2E7F)
    Sleep(50)

    def lambda_2E8F():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2E8F)
    Sleep(50)

    def lambda_2E9F():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2E9F)
    Sleep(50)

    def lambda_2EAF():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2EAF)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    #C0059
    ChrTalk(
        0x103,
        (
            "#12P#00202Fたしか３４Ｆの\x01",
            "警備対策室でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        (
            "#6P#00306Fしかし、このまま\x01",
            "何も起きなきゃいいんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x109,
        "#6P#10108Fそうですね、本当に……\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    StopSound(132, 1000, 100)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x323)
    SetScenarioFlags(0x22, 1)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_23BF end

    def Function_10_2FD3(): pass

    label("Function_10_2FD3")


    def lambda_2FD8():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FD8)

    def lambda_2FF2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FF2)
    WaitChrThread(0xFE, 1)

    def lambda_3007():
        OP_95(0xFE, -23500, -6000, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3007)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_10_2FD3 end

    def Function_11_3028(): pass

    label("Function_11_3028")


    def lambda_302D():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_302D)

    def lambda_3047():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3047)
    WaitChrThread(0xFE, 1)

    def lambda_305C():
        OP_95(0xFE, -23500, -6000, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_305C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_11_3028 end

    def Function_12_307D(): pass

    label("Function_12_307D")


    def lambda_3082():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3082)

    def lambda_309C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_309C)
    WaitChrThread(0xFE, 1)

    def lambda_30B1():
        OP_95(0xFE, -21500, -6000, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_30B1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_12_307D end

    def Function_13_30D2(): pass

    label("Function_13_30D2")


    def lambda_30D7():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_30D7)

    def lambda_30F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_30F1)
    WaitChrThread(0xFE, 1)

    def lambda_3106():
        OP_95(0xFE, -21500, -6000, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3106)
    WaitChrThread(0xFE, 1)
    Sound(107, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    Return()

    # Function_13_30D2 end

    def Function_14_3142(): pass

    label("Function_14_3142")


    def lambda_3147():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3147)

    def lambda_3161():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3161)
    WaitChrThread(0xFE, 1)

    def lambda_3176():
        OP_95(0xFE, -22500, -6000, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3176)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_14_3142 end

    def Function_15_3197(): pass

    label("Function_15_3197")


    def lambda_319C():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_319C)

    def lambda_31B6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_31B6)
    WaitChrThread(0xFE, 1)

    def lambda_31CB():
        OP_95(0xFE, -22500, -6000, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31CB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_15_3197 end

    def Function_16_31EC(): pass

    label("Function_16_31EC")


    def lambda_31F1():
        OP_95(0xFE, -25000, -6000, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31F1)

    def lambda_320B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_320B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_16_31EC end

    def Function_17_321C(): pass

    label("Function_17_321C")

    OP_92(0xFE, 0xFFFF9FE8, 0xFFFFD8F0, 0x1F4)

    def lambda_322E():
        OP_95(0xFE, -24600, -6000, -10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_322E)
    WaitChrThread(0xFE, 1)

    def lambda_324C():
        OP_95(0xFE, -21000, -4400, -18600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_324C)
    WaitChrThread(0xFE, 1)

    def lambda_326A():
        OP_95(0xFE, -21000, -4400, -21000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_326A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_17_321C end

    def Function_18_3284(): pass

    label("Function_18_3284")

    BeginChrThread(0xC, 3, 0, 25)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 19)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 20)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 23)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 22)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 24)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 21)
    Return()

    # Function_18_3284 end

    def Function_19_32C1(): pass

    label("Function_19_32C1")


    def lambda_32C6():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32C6)
    WaitChrThread(0xFE, 1)

    def lambda_32E4():
        OP_95(0xFE, -28000, -4400, -32600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32E4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_19_32C1 end

    def Function_20_3305(): pass

    label("Function_20_3305")


    def lambda_330A():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_330A)
    WaitChrThread(0xFE, 1)

    def lambda_3328():
        OP_95(0xFE, -29800, -4400, -32800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3328)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_20_3305 end

    def Function_21_3349(): pass

    label("Function_21_3349")


    def lambda_334E():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_334E)
    WaitChrThread(0xFE, 1)

    def lambda_336C():
        OP_95(0xFE, -28700, -4400, -31400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_336C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_21_3349 end

    def Function_22_338D(): pass

    label("Function_22_338D")


    def lambda_3392():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3392)
    WaitChrThread(0xFE, 1)

    def lambda_33B0():
        OP_95(0xFE, -26400, -4400, -31800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33B0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_22_338D end

    def Function_23_33D1(): pass

    label("Function_23_33D1")


    def lambda_33D6():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33D6)
    WaitChrThread(0xFE, 1)

    def lambda_33F4():
        OP_95(0xFE, -30700, -4400, -31900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33F4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xBE, 0x1F4)
    Return()

    # Function_23_33D1 end

    def Function_24_3415(): pass

    label("Function_24_3415")


    def lambda_341A():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_341A)
    WaitChrThread(0xFE, 1)

    def lambda_3438():
        OP_95(0xFE, -27100, -4400, -30600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3438)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_24_3415 end

    def Function_25_3459(): pass

    label("Function_25_3459")


    def lambda_345E():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_345E)
    WaitChrThread(0xFE, 1)

    def lambda_347C():
        OP_95(0xFE, -29400, -4400, -28800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_347C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_25_3459 end

    def Function_26_349D(): pass

    label("Function_26_349D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, 0, -33620, 0, 0)
    SetChrPos(0x1, 0, -33620, 0, 0)
    SetChrPos(0x2, 0, -33620, 0, 0)
    SetChrPos(0x3, 0, -33620, 0, 0)
    LoadChrToIndex("chr/ch42250.itc", 0x1E)
    LoadChrToIndex("chr/ch42251.itc", 0x1F)
    LoadChrToIndex("chr/ch42350.itc", 0x20)
    LoadChrToIndex("chr/ch42351.itc", 0x21)
    LoadChrToIndex("chr/ch42550.itc", 0x22)
    LoadChrToIndex("chr/ch42551.itc", 0x23)
    SoundLoad(497)
    SetChrChipByIndex(0x1A, 0x21)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x21, 0x23)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -10600, 3300, -3000, 270)
    OP_A7(0x21, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x22, 0x23)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -10600, 3300, -3000, 270)
    OP_A7(0x22, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x23, 0x23)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -10600, 3300, -3000, 270)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x24, 0x23)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -10600, 3300, -3000, 270)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x25, 0x23)
    SetChrSubChip(0x25, 0x0)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, -10600, 3300, -3000, 270)
    OP_A7(0x25, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x26, 0x23)
    SetChrSubChip(0x26, 0x0)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, -10600, 3300, -3000, 270)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x27, 0x23)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, -10600, 3300, -3000, 270)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x16, 0x80)
    OP_78(0x7, 0x16)
    OP_49()
    SetChrPos(0x16, 11000, 60000, 0, 170)
    OP_D5(0x16, 0x0, 0x29810, 0x0, 0x0)
    SetMapObjFlags(0x7, 0x1000)
    OP_74(0x7, 0x1E)
    OP_70(0x7, 0x3D)
    OP_71(0x7, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x6, 0x17)
    OP_49()
    SetChrPos(0x17, -11000, 62000, 0, 190)
    OP_D5(0x17, 0x0, 0x2E630, 0x0, 0x0)
    SetMapObjFlags(0x6, 0x1000)
    OP_74(0x6, 0x1E)
    OP_70(0x6, 0x3D)
    OP_71(0x6, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_78(0xC, 0x18)
    OP_78(0xB, 0x19)
    OP_49()
    SetChrPos(0x18, 10000, 100, 0, 170)
    OP_D5(0x18, 0x0, 0x29810, 0x0, 0x0)
    SetChrPos(0x19, -10000, 100, 0, 190)
    OP_D5(0x19, 0x0, 0x2E630, 0x0, 0x0)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFlags(0xB, 0x1000)
    OP_68(0, 28000, 0, 0)
    MoveCamera(165, -35, 0, 0)
    OP_6E(1100, 0)
    SetCameraDistance(190000, 0)

    def lambda_382F():
        OP_96(0xFE, 0x2AF8, 0x9C40, 0x0, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_382F)

    def lambda_3849():
        OP_96(0xFE, 0xFFFFD508, 0xA410, 0x0, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3849)
    Sound(497, 2, 100, 0)
    MoveCamera(15, -35, 0, 9000)
    SetCameraDistance(110000, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    EndChrThread(0x16, 0xFF)
    EndChrThread(0x17, 0xFF)
    SetChrPos(0x17, -10000, 22000, 0, 190)
    SetChrPos(0x16, 10000, 20000, 0, 170)
    BeginChrThread(0x16, 3, 0, 31)
    BeginChrThread(0x17, 3, 0, 32)
    OP_68(0, 9000, 0, 0)
    MoveCamera(45, 40, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(45000, 0)
    OP_68(0, 2000, 0, 5000)
    MoveCamera(35, 17, 0, 5000)
    SetCameraDistance(35000, 5000)
    Sleep(1500)
    Sound(942, 0, 100, 0)
    WaitChrThread(0x16, 3)
    OP_82(0xC8, 0xC8, 0xBB8, 0x12C)
    Sound(495, 0, 100, 0)
    Sound(833, 0, 50, 0)
    WaitChrThread(0x17, 3)
    OP_82(0xC8, 0xC8, 0xBB8, 0x12C)
    Sound(495, 0, 100, 0)
    Sound(833, 0, 50, 0)
    StopSound(497, 1000, 100)
    Sleep(300)
    Sound(105, 0, 100, 0)
    OP_71(0x6, 0x12D, 0x168, 0x0, 0x0)
    Sleep(500)
    BeginChrThread(0x17, 3, 0, 27)
    Sleep(1500)
    BeginChrThread(0x16, 3, 0, 28)
    Sleep(2500)
    Fade(500)
    OP_68(0, -1500, 0, 0)
    MoveCamera(0, 7, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(35000, 0)
    OP_0D()
    OP_68(0, -5000, 0, 10000)
    MoveCamera(90, 3, 0, 10000)
    SetCameraDistance(39000, 10000)
    Sleep(7000)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_6F(0x79)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x1F1)
    SetScenarioFlags(0x22, 6)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_26_349D end

    def Function_27_3A24(): pass

    label("Function_27_3A24")

    ClearChrFlags(0x21, 0x80)
    BeginChrThread(0x21, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x22, 0x80)
    BeginChrThread(0x22, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x23, 0x80)
    BeginChrThread(0x23, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x24, 0x80)
    BeginChrThread(0x24, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x25, 0x80)
    BeginChrThread(0x25, 3, 0, 29)
    Sleep(4000)
    ClearChrFlags(0x26, 0x80)
    BeginChrThread(0x26, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x27, 0x80)
    BeginChrThread(0x27, 3, 0, 29)
    Return()

    # Function_27_3A24 end

    def Function_28_3A84(): pass

    label("Function_28_3A84")

    ClearChrFlags(0x1A, 0x80)
    BeginChrThread(0x1A, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x1B, 0x80)
    BeginChrThread(0x1B, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x1C, 0x80)
    BeginChrThread(0x1C, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x1D, 0x80)
    BeginChrThread(0x1D, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x1E, 0x80)
    BeginChrThread(0x1E, 3, 0, 30)
    Sleep(2500)
    ClearChrFlags(0x1F, 0x80)
    BeginChrThread(0x1F, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x20, 0x80)
    BeginChrThread(0x20, 3, 0, 30)
    Return()

    # Function_28_3A84 end

    def Function_29_3AE4(): pass

    label("Function_29_3AE4")


    def lambda_3AE9():
        OP_95(0xFE, -12600, 3300, -3000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AE9)

    def lambda_3B03():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3B03)
    WaitChrThread(0xFE, 1)

    def lambda_3B18():
        OP_95(0xFE, -12000, 3300, -4800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B18)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 30, 0)

    def lambda_3B47():
        OP_9D(0xFE, 0xFFFFD440, 0x0, 0xFFFFDA80, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B47)
    WaitChrThread(0xFE, 1)
    Sound(326, 0, 40, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3B79():
        OP_95(0xFE, 0, 0, -18500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B79)
    WaitChrThread(0xFE, 1)

    def lambda_3B97():
        OP_95(0xFE, 0, 0, -22000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B97)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_3BBA():
        OP_9E(0xFE, 0x0, 0x0, 0x15F90, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BBA)
    WaitChrThread(0xFE, 1)

    def lambda_3BD9():
        OP_95(0xFE, -18000, -6000, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BD9)
    Sleep(500)

    def lambda_3BF6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3BF6)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_3AE4 end

    def Function_30_3C07(): pass

    label("Function_30_3C07")


    def lambda_3C0C():
        OP_95(0xFE, 8400, 4000, 4400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C0C)
    WaitChrThread(0xFE, 1)

    def lambda_3C2A():
        OP_95(0xFE, 6800, 4000, -1300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C2A)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3C53():
        OP_9D(0xFE, 0x11F8, 0x0, 0xFFFFE890, 0xBE, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C53)
    WaitChrThread(0xFE, 1)
    Sound(326, 0, 40, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3C85():
        OP_95(0xFE, 0, 0, -18500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C85)
    WaitChrThread(0xFE, 1)

    def lambda_3CA3():
        OP_95(0xFE, 0, 0, -22000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CA3)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_3CC6():
        OP_9E(0xFE, 0x0, 0x0, 0x15F90, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CC6)
    WaitChrThread(0xFE, 1)

    def lambda_3CE5():
        OP_95(0xFE, -18000, -6000, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CE5)
    Sleep(500)

    def lambda_3D02():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3D02)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_30_3C07 end

    def Function_31_3D13(): pass

    label("Function_31_3D13")


    def lambda_3D18():
        OP_D5(0xFE, 0x0, 0x2E630, 0x0, 0xED8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3D18)

    def lambda_3D31():
        OP_D5(0xFE, 0x0, 0x2E630, 0x0, 0xED8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_3D31)

    def lambda_3D4A():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D4A)
    Sleep(2800)

    def lambda_3D67():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D67)
    Sleep(300)

    def lambda_3D84():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D84)
    Sleep(300)

    def lambda_3DA1():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DA1)
    Sleep(300)

    def lambda_3DBE():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DBE)
    WaitChrThread(0xFE, 1)
    ClearMapObjFlags(0x7, 0x20)
    OP_74(0x7, 0x0)
    Return()

    # Function_31_3D13 end

    def Function_32_3DE2(): pass

    label("Function_32_3DE2")


    def lambda_3DE7():
        OP_D5(0xFE, 0x0, 0x29810, 0x0, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3DE7)

    def lambda_3E00():
        OP_D5(0xFE, 0x0, 0x29810, 0x0, 0xDAC)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3E00)

    def lambda_3E19():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E19)
    Sleep(2500)

    def lambda_3E36():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E36)
    Sleep(300)

    def lambda_3E53():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E53)
    Sleep(300)

    def lambda_3E70():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E70)
    Sleep(300)

    def lambda_3E8D():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E8D)
    WaitChrThread(0xFE, 1)
    ClearMapObjFlags(0x6, 0x20)
    OP_74(0x6, 0x0)
    Return()

    # Function_32_3DE2 end

    def Function_33_3EB1(): pass

    label("Function_33_3EB1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -19000, -6000, 0, 270)
    SetChrPos(0x102, -19000, -6000, 0, 270)
    SetChrPos(0x103, -19000, -6000, 0, 270)
    SetChrPos(0x104, -19000, -6000, 0, 270)
    SetChrPos(0x109, -19000, -6000, 0, 270)
    SetChrPos(0x105, -19000, -6000, 0, 270)
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
    ClearMapFlags(0x10000000)
    OP_68(-20000, -5000, 0, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_68(-23000, -5000, 0, 6000)
    SetCameraDistance(16000, 6000)
    BeginChrThread(0x101, 3, 0, 10)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 11)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 15)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 14)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 12)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 13)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0062
    ChrTalk(
        0x102,
        "#11P#00105Fあら……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 3)
    OP_68(-25000, -4500, 0, 2500)
    MoveCamera(335, 17, 0, 2500)
    SetCameraDistance(14500, 2500)
    OP_6F(0x79)
    Sleep(300)

    #C0063
    ChrTalk(
        0x109,
        (
            "#12P#10102Fちょっと雨が\x01",
            "止んできたみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        (
            "#00309Fああ……それにしても\x01",
            "相変わらずスゲェ景色だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#12P#00002Fああ、晴れた日だと\x01",
            "更に絶景なんだろうけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(700)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(400)

    #C0066
    ChrTalk(
        0x101,
        (
            "#11P#00005Fヨナと主任は\x01",
            "どこにいるんだろう？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_41B0():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_41B0)
    Sleep(50)

    def lambda_41C0():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_41C0)
    Sleep(50)

    def lambda_41D0():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_41D0)
    Sleep(50)

    def lambda_41E0():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_41E0)
    Sleep(50)

    def lambda_41F0():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_41F0)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    #C0067
    ChrTalk(
        0x103,
        (
            "#12P#00204F多分、屋上の一角に\x01",
            "いるのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x105,
        "#10300F探してみようか。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -22000, -6000, 0, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x164, 7)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_33_3EB1 end

    def Function_34_429F(): pass

    label("Function_34_429F")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00254.itc", 0x1F)
    LoadChrToIndex("apl/ch51405.itc", 0x20)
    LoadChrToIndex("chr/ch29300.itc", 0x21)
    SoundLoad(2280)
    SoundLoad(2683)
    SoundLoad(2281)
    SoundLoad(943)
    SoundLoad(938)
    SoundLoad(852)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    LoadEffect(0x2, "event/ev14010.eff")
    LoadEffect(0x3, "event/ev14026.eff")
    LoadEffect(0x4, "event/ev14027.eff")
    LoadEffect(0x5, "event/ev14028.eff")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis328.itp")
    CreatePortrait(1, 308, 154, 340, 186, 0, 0, 32, 36, 0, 0, 32, 32, 0xFFFFFF, 0x0, "c_vis329.itp")
    SetChrPos(0x101, 22400, -4400, -22300, 135)
    SetChrPos(0x103, 21700, -4400, -23000, 135)
    SetChrPos(0x102, 20700, -4400, -22300, 135)
    SetChrPos(0x104, 21700, -4400, -21300, 135)
    SetChrPos(0x109, 19700, -4400, -21900, 135)
    SetChrPos(0x105, 20700, -4400, -20900, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 28400, -4400, -27750, 45)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x20)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, 31900, -4400, -27650, 75)
    BeginChrThread(0xA, 2, 0, 36)
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x1000)
    OP_74(0x8, 0x1E)
    OP_70(0x8, 0x2)
    OP_68(21700, -3200, -22650, 0)
    MoveCamera(350, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15000, 1200)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_44F5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_44F5)

    #N0069
    NpcTalk(
        0xB,
        "ロバーツ主任の声",
        "やあ、待ってたよ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    BeginChrThread(0x32, 1, 0, 41)
    OP_68(29300, -3200, -26900, 2000)
    MoveCamera(15, 17, 0, 2000)
    SetCameraDistance(13500, 2000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(27740, -3200, -26940, 0)
    MoveCamera(350, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0xA, 32200, -4400, -27850, 75)

    def lambda_4614():
        OP_97(0x101, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4614)
    Sleep(100)

    def lambda_4631():
        OP_97(0x103, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4631)
    Sleep(100)

    def lambda_464E():
        OP_97(0x104, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_464E)
    Sleep(100)

    def lambda_466B():
        OP_97(0x102, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_466B)
    Sleep(100)

    def lambda_4688():
        OP_97(0x105, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4688)
    Sleep(100)

    def lambda_46A5():
        OP_97(0x109, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_46A5)
    WaitChrThread(0x109, 0)

    #C0070
    ChrTalk(
        0x101,
        (
            "#00002F#5Pこれがアラート信号を\x01",
            "感知するための装置ですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xB,
        (
            "#12Pああ、ただしこのままじゃあ\x01",
            "半径１０セルジュの範囲内しか\x01",
            "感知することができない。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xB,
        "#12Pそこでティオ君の出番ってわけだ。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x103,
        (
            "#5P#00204Fこちらの方は問題ありません。\x02\x03",

            "#00200Fしかし……\x01",
            "雨の影響は大丈夫ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xB,
        (
            "#12Pまあ、かなり小雨になったし\x01",
            "あんまり影響はないと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xB,
        (
            "#12Pしかしティオ君をこのまま\x01",
            "雨風に晒すのは忍びないな……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xB,
        (
            "#12Pそうだ、ティオ君が\x01",
            "センサーを起動している間は\x01",
            "僕が傘を差して──\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x103,
        (
            "#5P#00203F結構です。\x01",
            "逆に気が散りますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xB,
        "#12Pしゅん……\x02",
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
    EndChrThread(0xA, 0x2)
    StopSound(938, 500, 40)

    #C0079
    ChrTalk(
        0xA,
        (
            "#02303F#5P──よしっと。\x01",
            "こっちも準備ＯＫだぜ。\x02\x03",

            "#02300Fいつでもエイオンを\x01",
            "起動させて大丈夫だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x103,
        (
            "#5P#00204Fそれでは始めましょう。\x02\x03",

            "#00200FリンさんたちのエニグマⅡの\x01",
            "固体番号は入力済みですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xB,
        (
            "#12Pああ、ギルドからちゃんと\x01",
            "番号は聞いておいたからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xB,
        "#12P既に測定器に入力してるよ。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x103,
        "#5P#00202F了解しました。\x02",
    )

    CloseMessageWindow()

    def lambda_4AC2():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4AC2)
    Sleep(50)

    def lambda_4AD2():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4AD2)
    Sleep(50)

    def lambda_4AE2():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4AE2)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    def lambda_4AFE():

        label("loc_4AFE")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4AFE")

    QueueWorkItem2(0x101, 2, lambda_4AFE)

    def lambda_4B10():

        label("loc_4B10")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4B10")

    QueueWorkItem2(0x102, 2, lambda_4B10)

    def lambda_4B22():

        label("loc_4B22")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4B22")

    QueueWorkItem2(0x109, 2, lambda_4B22)

    def lambda_4B34():

        label("loc_4B34")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4B34")

    QueueWorkItem2(0x105, 2, lambda_4B34)

    def lambda_4B46():

        label("loc_4B46")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4B46")

    QueueWorkItem2(0x104, 2, lambda_4B46)

    def lambda_4B58():

        label("loc_4B58")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4B58")

    QueueWorkItem2(0xB, 2, lambda_4B58)
    Sleep(150)

    #C0084
    ChrTalk(
        0x101,
        "#11P#00001Fティオ、よろしく頼む。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        (
            "#00108F#5Pリンさんたちの居場所、\x01",
            "どうか突き止めてあげて。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x15E, 0x1F4)
    Sleep(100)

    #C0086
    ChrTalk(
        0x103,
        "#6P#00202Fはい、それでは──\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    OP_92(0x103, 0x6C98, 0xFFFF8C60, 0x1F4)
    OP_68(28160, -3400, -29390, 2000)

    def lambda_4C25():
        OP_95(0xFE, 27800, -4400, -29600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4C25)
    WaitChrThread(0x103, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0xB, 0x2)
    OP_93(0x103, 0x87, 0x1F4)
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_0D()

    def lambda_4C76():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4C76)
    Sleep(500)
    #Sound(2280, 255, 100, 0)    #voice#Tio

    #C0087
    ChrTalk(
        0x103,
        (
            "#5P#00203F#30W──エイオンシステム起動。\x02\x03",

            "#00201F#30Wマトリクス方式による\x01",
            "測定器との連動#4Rリンク#を開始……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x8E8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7352", 0)
    MoveCamera(346, 20, 0, 18000)
    SetCameraDistance(15950, 18000)
    Sound(852, 2, 100, 0)
    Sound(943, 2, 100, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x5, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_71(0x8, 0xA, 0x29, 0x0, 0x0)
    OP_79(0x8)
    OP_24(0x3AF)
    Sound(143, 0, 50, 0)
    Sound(938, 2, 50, 0)
    BeginChrThread(0xA, 2, 0, 36)

    #C0088
    ChrTalk(
        0xA,
        (
            "#02304F#6P──連動#4Rリンク#を確認。\x02\x03",

            "#02302Fそのままイッちまっても\x01",
            "問題なさそうだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xB,
        (
            "#5P測定器への導力供給も\x01",
            "高レベルで安定できそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xB,
        "#5Pティオ君、よろしく頼むよ。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x103,
        (
            "#5P#00203Fはい──\x01",
            "それでは行きます。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0092
    ChrTalk(
        0x103,
        "#5P#00201F#2683V#40W#20Aセンサー機能解放……\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(1000)

    #C0093
    ChrTalk(
        0x103,
        (
            "#5P#00203F#20A#40Wエイオンシステム─#800W─\x01",
            "#30W#00207F#4S制限解除#8Rリミットブレイク#！\x02",
        )
    )
    #Auto

    Sleep(1200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    MoveCamera(333, 19, -5, 4000)
    SetCameraDistance(22000, 4000)
    BeginChrThread(0x101, 3, 0, 38)
    BeginChrThread(0x103, 3, 0, 39)
    Sound(357, 0, 100, 0)
    PlayEffect(0x0, 0x0, 0x103, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    EndChrThread(0xA, 0x2)
    Fade(500)
    OP_68(27800, -3300, -29600, 0)
    MoveCamera(100, 20, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12000, 0)
    BeginChrThread(0xA, 2, 0, 37)
    OP_68(34800, -2800, -36600, 7000)
    MoveCamera(100, 10, -15, 7000)
    SetCameraDistance(36000, 7000)
    BeginChrThread(0xB, 3, 0, 35)
    OP_6F(0x79)
    WaitChrThread(0xB, 3)

    #C0094
    ChrTalk(
        0x104,
        "#00305F#6Pおおっ……！\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x109,
        "#6P#10111Fい、今のは……\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x105,
        (
            "#10305F#6P何か“波”みたいなのが\x01",
            "広がっていったみたいだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0xA, 0x2)
    Fade(500)
    OP_68(28060, -3400, -29350, 0)
    MoveCamera(350, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    BeginChrThread(0xA, 2, 0, 36)
    OP_0D()
    OP_71(0x8, 0x5A, 0x64, 0x0, 0x0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopSound(852, 500, 90)
    StopSound(943, 500, 40)
    EndChrThread(0x103, 0x3)
    Sleep(500)
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    StopBGM(0x1770)
    Sleep(500)

    #C0097
    ChrTalk(
        0x103,
        "#6P#00206F……ふう。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xB,
        "#5Pうんうん、成功みたいだねぇ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(27400, -3200, -27000, 1200)

    def lambda_51D8():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_51D8)
    Sleep(50)

    def lambda_51E8():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_51E8)
    Sleep(50)

    def lambda_51F8():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_51F8)
    Sleep(50)

    def lambda_5208():
        TurnDirection(0x109, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5208)
    Sleep(50)

    def lambda_5218():
        TurnDirection(0x105, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5218)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    #C0099
    ChrTalk(
        0x101,
        "#5P#00007F本当ですか……！？\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        (
            "#00101F#5Pリンさんたちの居場所が\x01",
            "分かったんですか！？\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)
    TurnDirection(0xB, 0x101, 500)

    #C0101
    ChrTalk(
        0xB,
        (
            "#12Pうん、まあ正確には\x01",
            "エニグマⅡの場所だけどね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0102
    ChrTalk(
        0x103,
        (
            "#6P#00203F２つのアラート信号を\x01",
            "わたしの方でも感知しました。\x02\x03",

            "#00201Fここからかなり南の方ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "#02302F#6Pんで、入ってきた情報を解析して\x01",
            "マップ情報に出力すると……\x02\x03",

            "#02309F（カタカタ）──ホラ、出てきたぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    EndChrThread(0xA, 0x2)
    StopSound(938, 500, 40)
    BeginChrThread(0x101, 3, 0, 40)
    Sleep(2000)
    SetMessageWindowPos(10, 40, -1, -1)

    #A0104
    AnonymousTalk(
        0x101,
        "#00005Fえ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(30, 80, -1, -1)

    #A0105
    AnonymousTalk(
        0x109,
        (
            "#10101Fここは……\x01",
            "エルム湖の南側……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 20, -1, -1)

    #A0106
    AnonymousTalk(
        0x104,
        (
            "#00301Fなんだこりゃ……\x01",
            "こんな所に何かあったか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(20, 80, -1, -1)

    #A0107
    AnonymousTalk(
        0x102,
        (
            "#00108Fわ、私の知る限り\x01",
            "人の手が入ったことすらない\x01",
            "湿原地帯だと思うけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(80, 20, -1, -1)

    #A0108
    AnonymousTalk(
        0x105,
        (
            "#10301Fそんな場所に、あの遊撃士の\x01",
            "お姉さんたちが居るわけか……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(220, 180, -1, -1)

    #A0109
    AnonymousTalk(
        0xA,
        (
            "#02305Fよくわかんねーけど、\x01",
            "タダ事じゃないんじゃねえの？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(220, 60, -1, -1)

    #A0110
    AnonymousTalk(
        0xB,
        "うーん、さすがに心配だねぇ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(120, 120, -1, -1)

    #A0111
    AnonymousTalk(
        0x103,
        "#00208Fロイドさん……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(10, 40, -1, -1)

    #A0112
    AnonymousTalk(
        0x101,
        "#00008F………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x101, 0x3)
    OP_68(31000, -3300, -28800, 0)
    MoveCamera(13, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x101, 30300, -4400, -29500, 55)
    SetChrPos(0x103, 30800, -4400, -30900, 15)
    SetChrPos(0x102, 29600, -4400, -28800, 55)
    SetChrPos(0x104, 28600, -4400, -28300, 100)
    SetChrPos(0x109, 28600, -4400, -30000, 55)
    SetChrPos(0x105, 29300, -4400, -30700, 55)
    SetChrPos(0xB, 30400, -4400, -26800, 100)
    SetChrPos(0xA, 31900, -4400, -27650, 75)
    OP_70(0x8, 0x2)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_93(0x101, 0xF0, 0x1F4)

    #C0113
    ChrTalk(
        0x101,
        (
            "#11P#00003F──とりあえず一旦\x01",
            "ミシェルさんの所に戻ろう。\x02\x03",

            "#00001Fそれと、念のため警察本部に\x01",
            "ボートを手配してもらった方が\x01",
            "いいかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5795():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5795)
    Sleep(50)

    def lambda_57A5():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_57A5)
    Sleep(50)

    def lambda_57B5():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_57B5)
    Sleep(50)

    def lambda_57C5():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_57C5)
    Sleep(50)

    def lambda_57D5():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_57D5)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0114
    ChrTalk(
        0x102,
        "#00106F#5Pそうね……\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x109,
        (
            "#6P#10101Fええ、状況を考えると\x01",
            "急いだ方が良さそうです！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5850():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5850)
    Sleep(50)

    def lambda_5860():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5860)
    Sleep(50)

    def lambda_5870():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5870)
    Sleep(50)

    def lambda_5880():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5880)
    Sleep(50)

    def lambda_5890():
        TurnDirection(0x109, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5890)
    Sleep(50)

    def lambda_58A0():
        TurnDirection(0x105, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_58A0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0116
    ChrTalk(
        0x101,
        (
            "#6P#00000Fロバーツ主任にヨナも\x01",
            "協力ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5906():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_5906)
    Sleep(50)

    def lambda_5916():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_5916)
    Sleep(50)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xA, 0)

    #C0117
    ChrTalk(
        0xB,
        (
            "#5Pなんのなんの。\x01",
            "後片付けは任せてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        "#02302F#11Pま、せいぜい気を付けろよな～。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15500, 2000)
    StopSound(132, 2000, 90)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x3AF)
    OP_24(0x3AA)
    OP_24(0x354)
    SetScenarioFlags(0x22, 1)
    NewScene("c1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_429F end

    def Function_35_59C8(): pass

    label("Function_35_59C8")

    Sleep(2600)
    StopEffect(0x2, 0x2)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 29400, -2900, -26600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(1014, 0, 100, 0)
    Sleep(1000)
    Sound(895, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x103, 0x1, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Sound(998, 0, 100, 0)
    Sound(922, 0, 100, 0)
    Sound(833, 0, 40, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    PlayEffect(0x2, 0xFF, 0x103, 0x1, 0, 2000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(1000)
    CancelBlur(1500)
    Sleep(2000)
    Return()

    # Function_35_59C8 end

    def Function_36_5AC0(): pass

    label("Function_36_5AC0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5ADE")
    SetChrSubChip(0xFE, 0x4)
    Sleep(90)
    SetChrSubChip(0xFE, 0x5)
    Sleep(90)
    Jump("Function_36_5AC0")

    label("loc_5ADE")

    Return()

    # Function_36_5AC0 end

    def Function_37_5ADF(): pass

    label("Function_37_5ADF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5AFD")
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    Jump("Function_37_5ADF")

    label("loc_5AFD")

    Return()

    # Function_37_5ADF end

    def Function_38_5AFE(): pass

    label("Function_38_5AFE")

    Sound(943, 2, 50, 0)
    OP_71(0x8, 0x29, 0x32, 0x0, 0x0)
    OP_79(0x8)
    Sound(311, 0, 50, 0)
    PlayEffect(0x3, 0x2, 0xFF, 0x0, 29400, -4400, -26600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_71(0x8, 0x32, 0x59, 0x0, 0x20)
    Return()

    # Function_38_5AFE end

    def Function_39_5B5D(): pass

    label("Function_39_5B5D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5B7B")
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_39_5B5D")

    label("loc_5B7B")

    Return()

    # Function_39_5B5D end

    def Function_40_5B7C(): pass

    label("Function_40_5B7C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BC3")
    Sound(1021, 0, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Jump("Function_40_5B7C")

    label("loc_5BC3")

    Return()

    # Function_40_5B7C end

    def Function_41_5BC4(): pass

    label("Function_41_5BC4")

    Sound(938, 2, 0, 0)
    Sleep(200)
    OP_25(0x3AA, 0x5)
    Sleep(200)
    OP_25(0x3AA, 0xA)
    Sleep(200)
    OP_25(0x3AA, 0xF)
    Sleep(200)
    OP_25(0x3AA, 0x14)
    Sleep(200)
    OP_25(0x3AA, 0x19)
    Sleep(200)
    OP_25(0x3AA, 0x1E)
    Sleep(200)
    OP_25(0x3AA, 0x23)
    Sleep(200)
    OP_25(0x3AA, 0x28)
    Sleep(200)
    OP_25(0x3AA, 0x2D)
    Sleep(200)
    OP_25(0x3AA, 0x32)
    Return()

    # Function_41_5BC4 end

    def Function_42_5C11(): pass

    label("Function_42_5C11")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05620.itc", 0x1E)
    LoadChrToIndex("chr/ch03700.itc", 0x1F)
    LoadChrToIndex("apl/ch51545.itc", 0x20)
    LoadChrToIndex("chr/ch03300.itc", 0x21)
    LoadChrToIndex("chr/ch03400.itc", 0x22)
    LoadChrToIndex("chr/ch02100.itc", 0x23)
    LoadChrToIndex("chr/ch13400.itc", 0x24)
    LoadChrToIndex("chr/ch03600.itc", 0x25)
    LoadChrToIndex("chr/ch03500.itc", 0x26)
    LoadChrToIndex("apl/ch51548.itc", 0x27)
    LoadChrToIndex("apl/ch51543.itc", 0x28)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12300.itp")
    LoadEffect(0x0, "event/ev500_00.eff")
    LoadEffect(0x1, "event/ev10005.eff")
    LoadEffect(0x2, "event/ev10001.eff")
    LoadEffect(0x4, "event/ev15071.eff")
    LoadEffect(0x5, "event/ev17022.eff")
    LoadEffect(0x6, "event/ev10008.eff")
    LoadEffect(0x7, "event/eva03_01.eff")
    SoundLoad(832)
    SoundLoad(852)
    SetChrPos(0x0, 0, -33620, 0, 0)
    SetChrPos(0x1, 0, -33620, 0, 0)
    SetChrPos(0x2, 0, -33620, 0, 0)
    SetChrPos(0x3, 0, -33620, 0, 0)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, -1000, 180)
    OP_8E(0xC, "ディーター大統領")
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 1600, 0, -5000, 0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 0, 300, -5000, 0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x10, 1, 0, 0)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -1200, 0, 400, 180)
    SetChrChipByIndex(0xE, 0x22)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -2400, 0, 400, 180)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 400, 0, 1000, 180)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -4000, 0, -4300, 90)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -5000, 0, -2900, 90)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -5500, 0, -5000, 90)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "open")
    OP_70(0x1, 0x12D)
    OP_70(0x2, 0x12D)
    OP_70(0x3, 0x12D)
    OP_70(0x4, 0x12D)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    OP_D5(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFlags(0x5, 0x4)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x0)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    OP_78(0x9, 0x29)
    OP_D5(0x29, 0x0, 0x20F58, 0x0, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFlags(0x9, 0x4)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    SetChrFlags(0x29, 0x1)
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    OP_78(0xA, 0x2A)
    OP_D5(0x2A, 0x0, 0x36EE8, 0x0, 0x0)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFlags(0xA, 0x4)
    OP_74(0xA, 0x1E)
    OP_70(0xA, 0x0)
    SetChrFlags(0x2A, 0x1)
    OP_52(0x2A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 0, 0, 0)
    MoveCamera(180, 25, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(100000, 0)
    MoveCamera(45, 15, 0, 10000)
    OP_68(0, 1000, 0, 10000)
    SetCameraDistance(12000, 10000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 1300, -3000, 0)
    MoveCamera(120, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12000, 0)
    SetCameraDistance(14000, 5000)
    OP_0D()
    BeginChrThread(0x32, 1, 0, 50)
    BeginChrThread(0x10, 3, 0, 45)
    Sleep(700)
    BeginChrThread(0x11, 3, 0, 45)
    Sleep(1100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    Sleep(1)
    CancelBlur(1500)
    WaitChrThread(0x10, 3)
    Sound(852, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x10, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x11, 3)
    OP_6F(0x79)

    #C0119
    ChrTalk(
        0xC,
        "#11302F#6Pおお……！\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xD,
        "#04500F#6Pほう……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xF,
        "#01605F#6Pチビ、おめぇ……\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xE,
        (
            "#04602F#6P#Nへえ～。\x01",
            "なんかスゴそうだね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(190, 1300, -3970, 1500)
    OP_95(0xC, -60, 0, -2170, 1200, 0x0)
    OP_6F(0x79)

    #C0123
    ChrTalk(
        0xC,
        (
            "#11304F#6Pキーア君──いや、\x01",
            "教団にならって《御子#4Rみ こ#》殿と\x01",
            "呼ばせてもらおう。\x02\x03",

            "#11302Fよくぞ再び、\x01",
            "この世界に顕#2Rあらわ#れてくれた。\x02\x03",

            "クロイス家の現当主として\x01",
            "お迎えできて光栄だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0124
    AnonymousTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#30W…………うん。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0125
    ChrTalk(
        0x11,
        (
            "#10804F#11Pフフ、お父様。\x01",
            "挨拶はそのくらいで。\x02\x03",

            "#10802Fそろそろ彼らからの\x01",
            "贈り物を受け取りませんと。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xC,
        "#11305F#6Pおお、そうだったな。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 170, -1, -1)
    SetChrName("男の声")

    #A0127
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フフ、ようやく私の努力も\x01",
            "実を結ぶようだねぇ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-2000, 1300, -4300, 2000)
    MoveCamera(45, 13, 0, 2000)
    SetCameraDistance(13000, 2000)
    Sleep(1000)
    Sound(977, 0, 100, 0)
    Sound(832, 2, 100, 0)
    BeginChrThread(0x13, 3, 0, 46)
    Sleep(500)
    Sound(977, 0, 50, 0)
    BeginChrThread(0x14, 3, 0, 46)
    Sleep(500)
    Sound(977, 0, 50, 0)
    BeginChrThread(0x12, 3, 0, 46)

    def lambda_662C():
        TurnDirection(0xC, 0x14, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_662C)
    Sleep(50)

    def lambda_663C():
        TurnDirection(0x11, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_663C)
    Sleep(50)

    def lambda_664C():
        TurnDirection(0x10, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_664C)
    Sleep(50)

    def lambda_665C():
        TurnDirection(0xD, 0x14, 500)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_665C)
    Sleep(50)

    def lambda_666C():
        TurnDirection(0xE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_666C)
    Sleep(50)

    def lambda_667C():
        TurnDirection(0xF, 0x14, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_667C)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x10, 0)
    WaitChrThread(0xD, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)
    OP_6F(0x79)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    Sleep(1)
    CancelBlur(1500)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x12, 3)
    OP_68(-2500, 1300, -4300, 1700)
    Sleep(1700)
    SetChrChipByIndex(0x14, 0x28)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x14, 0x2)
    Sleep(120)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0x14, 0x1)
    Sleep(400)
    OP_6F(0x79)
    StopSound(832, 500, 100)
    Sleep(300)

    #C0128
    ChrTalk(
        0x12,
        (
            "#6P#04900F#3C大いなる至宝を継ぐ者よ……\x02\x03",

            "《身喰らう蛇》の盟主に代わり\x01",
            "御身の顕現を寿#2Rことほ#がせて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x13,
        (
            "#04704F#6Pフフ、ささやかながら\x01",
            "“献上品”を用意しました。\x02\x03",

            "#04700Fどうかお受け取りあれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12302F#11P……ありがとう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x0, 0x1F4)
    Fade(500)
    OP_68(0, 1700, -5000, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(11000, 0)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x20)
    ClearChrFlags(0x14, 0x10)
    ClearChrFlags(0x14, 0x2)
    Sound(812, 0, 100, 0)
    OP_4B(0x10, 0xFF)
    SetChrChipByIndex(0x10, 0x27)
    SetChrSubChip(0x10, 0x1)
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(10500, 800)

    def lambda_6877():
        TurnDirection(0xC, 0x10, 0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_6877)
    Sleep(0)

    def lambda_6887():
        TurnDirection(0xD, 0x10, 0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_6887)
    Sleep(0)

    def lambda_6897():
        TurnDirection(0xE, 0x10, 0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_6897)
    Sleep(0)

    def lambda_68A7():
        TurnDirection(0xF, 0x10, 0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_68A7)
    Sleep(0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    OP_68(0, 7000, -5000, 4000)
    MoveCamera(0, -5, 0, 4000)
    Sleep(2000)
    StopSound(132, 2000, 40)
    StopSound(852, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x340)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_06.pmf", 0x229, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_93(0xC, 0x0, 0x1F4)
    OP_93(0xF, 0x2D, 0x1F4)
    OP_93(0xD, 0x13B, 0x1F4)
    OP_93(0xE, 0x13B, 0x1F4)
    OP_93(0x11, 0x0, 0x1F4)
    OP_93(0x13, 0x0, 0x1F4)
    OP_93(0x14, 0x0, 0x1F4)
    OP_93(0x12, 0x0, 0x1F4)
    BeginChrThread(0x28, 3, 0, 47)
    BeginChrThread(0x29, 3, 0, 48)
    BeginChrThread(0x2A, 3, 0, 49)
    OP_68(0, 19000, 1000, 0)
    MoveCamera(215, 40, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(25000, 0)
    OP_68(0, 3000, 1000, 8500)
    MoveCamera(135, 27, 0, 8500)
    SetCameraDistance(20000, 8500)
    SoundLoad(979)
    Sound(852, 2, 100, 0)
    Sound(132, 2, 100, 0)
    Sound(979, 2, 100, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x10, 3, 0, 51)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x7, 0x3, 0xFF, 0x0, 0, 30000, 0, 0, 270, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x4, 0xFF, 0x0, 0, 30000, 0, 0, 270, 0, 2000, 1000, 2000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(6500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    StopEffect(0x3, 0x0)
    StopEffect(0x4, 0x0)
    CancelBlur(0)
    Fade(500)
    OP_68(0, 4500, 6500, 0)
    MoveCamera(0, -23, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(9500, 0)
    SetChrFlags(0xF, 0x8)
    OP_68(0, 3000, 6500, 1500)
    MoveCamera(0, -13, 0, 1500)
    SetCameraDistance(10500, 1500)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 3000, 6500, 0)
    MoveCamera(23, 13, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13000, 0)
    ClearChrFlags(0xF, 0x8)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4C(0x10, 0xFF)
    OP_68(0, 1900, 3000, 4000)
    MoveCamera(33, 9, 0, 4000)
    OP_6E(800, 4000)
    SetCameraDistance(21000, 4000)
    OP_6F(0x79)
    WaitChrThread(0x2A, 3)
    Sleep(300)

    #C0131
    ChrTalk(
        0xF,
        "#01607F#6Pこ、こいつは……！\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xE,
        (
            "#04612F#12Pうわあああっ！\x01",
            "カッコイイじゃん！\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xD,
        (
            "#04502F#12Pクク……\x01",
            "なかなかのオモチャだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x11,
        (
            "#10804F#12P#N『神機アイオーン』……\x02\x03",

            "#10800F《至宝》が奇蹟を振るうための\x01",
            "３体のインターフェイス……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(800)
    OP_68(0, 1000, -1000, 0)
    MoveCamera(24, 12, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(15000, 1500)
    OP_6F(0x79)
    OP_0D()

    #C0135
    ChrTalk(
        0xC,
        "#11P#11304F#12P……予想以上の仕上がりだ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x13, 500)

    #C0136
    ChrTalk(
        0xC,
        (
            "#11P#11300F《結社》の諸君。\x01",
            "借りを作ってしまったようだね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6D73():
        TurnDirection(0x13, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_6D73)
    Sleep(50)

    def lambda_6D83():
        TurnDirection(0x12, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_6D83)
    Sleep(50)

    def lambda_6D93():
        TurnDirection(0x14, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_6D93)
    Sleep(50)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x14, 0)

    def lambda_6DAF():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6DAF)

    #C0137
    ChrTalk(
        0x13,
        (
            "#5P#04709F#6Pハハ、こちらも資金面で\x01",
            "いつも助けてもらっているからね。\x02\x03",

            "#04702Fゴルディアス級の運用データが\x01",
            "そっくり使えたのも大きかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x12,
        (
            "#04900F#3C#6P#Nそれに今回の件については\x01",
            "《盟主》の意にも適#2Rかな#うこと……\x02\x03",

            "借りに思う必要はありません。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0139
    ChrTalk(
        0x11,
        (
            "#10809F#11Pうふふ……\x01",
            "なかなかの太っ腹ですわね。\x02\x03",

            "#10802F──キーアさん。\x01",
            "それではお願いできますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12301F#12Pうん……わかった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Fade(250)
    Sound(802, 0, 50, 0)
    OP_4B(0x10, 0x1)
    SetChrChipByIndex(0x10, 0x27)
    SetChrSubChip(0x10, 0x2)
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(500)
    OP_68(0, 1900, 3000, 2000)
    MoveCamera(33, 9, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(21000, 2000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(273, 0, 70, 0)
    PlayEffect(0x4, 0x1, 0xFF, 0x0, -7000, 5000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0xFF, 0x0, 9000, 5000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_7028():
        OP_93(0xC, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_7028)
    Sleep(50)

    def lambda_7038():
        OP_93(0x11, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_7038)
    Sleep(50)

    def lambda_7048():
        OP_93(0x13, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_7048)
    Sleep(50)

    def lambda_7058():
        OP_93(0x12, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_7058)
    Sleep(50)

    def lambda_7068():
        OP_93(0x14, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_7068)
    Sleep(50)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x14, 0)
    Sleep(2000)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    BeginChrThread(0x29, 3, 0, 43)
    BeginChrThread(0x2A, 3, 0, 44)
    WaitChrThread(0x29, 3)
    Sleep(2000)
    StopSound(979, 2000, 100)
    StopSound(132, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    CancelBlur(0)
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x229), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x24, 3)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_5C11 end

    def Function_43_70D9(): pass

    label("Function_43_70D9")

    OP_68(0, 2900, 3000, 1500)
    SetCameraDistance(23000, 1500)
    Sound(935, 0, 100, 0)

    def lambda_70FE():
        OP_96(0xFE, 0xFFFFE4A8, 0x7D0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_70FE)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x14A, 0x15E, 0x0, 0x0)
    OP_79(0x9)
    OP_74(0x9, 0xA)
    OP_71(0x9, 0xA, 0x32, 0x0, 0x20)
    WaitChrThread(0x29, 1)
    OP_6F(0x79)
    Sound(905, 0, 100, 0)
    OP_71(0x9, 0x65, 0x6E, 0x15E, 0x0)
    OP_79(0x9)
    OP_71(0x9, 0x6F, 0x96, 0x0, 0x20)
    OP_68(0, 3900, -3000, 2500)
    MoveCamera(60, 7, 15, 2500)
    SetCameraDistance(40000, 6500)
    BlurSwitch(0x3E8, 0x77FFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, 10000, -7000, 90, 0, 0, 500, 3000, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, 10000, -7000, 90, 0, 0, 1000, 3000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, 10000, -7000, 90, 0, 0, 1500, 3000, 1500, 0xFF, 0, 0, 0, 0)
    Sound(833, 0, 50, 0)
    Sound(499, 0, 100, 0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_r0 (66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_r1(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_r2(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_l0(69)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_l1(70)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_l2(71)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_9F(0x0, 0x29)
    OP_9F(0x1, 8000, 3000, -4000)
    OP_9F(0x1, 20000, 4000, -7000)
    OP_9F(0x1, 500000, 7000, -8000)

    def lambda_73C9():
        OP_9F(0x2, 0x29, 20000, 0x6)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_73C9)
    Sleep(1000)

    def lambda_73DB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_73DB)
    Sleep(300)

    def lambda_73EB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_73EB)
    OP_6F(0x41)
    Return()

    # Function_43_70D9 end

    def Function_44_73F6(): pass

    label("Function_44_73F6")

    Sound(978, 0, 50, 0)
    OP_25(0x3D3, 0x64)
    OP_71(0xA, 0x5A, 0x33, 0x0, 0x0)

    def lambda_7411():
        OP_96(0xFE, 0x2328, 0x3E8, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_7411)
    WaitChrThread(0x2A, 1)
    OP_79(0xA)
    OP_71(0xA, 0xA, 0x32, 0x0, 0x20)
    Sleep(2000)
    OP_9F(0x0, 0x2A)
    OP_9F(0x1, -5000, 3000, -3000)
    OP_9F(0x1, -20000, 4000, -6000)
    OP_9F(0x1, -200000, 7000, -7000)

    def lambda_746F():
        OP_9F(0x2, 0x2A, 10000, 0x6)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_746F)
    Sleep(1000)

    def lambda_7481():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_7481)
    Sleep(100)

    def lambda_7491():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7491)
    Sleep(100)

    def lambda_74A1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_74A1)
    Return()

    # Function_44_73F6 end

    def Function_45_74AA(): pass

    label("Function_45_74AA")

    PlayEffect(0x1, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1800)

    def lambda_74E9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_74E9)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_45_74AA end

    def Function_46_74FA(): pass

    label("Function_46_74FA")

    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(936, 0, 80, 0)

    def lambda_753F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_753F)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_46_74FA end

    def Function_47_7550(): pass

    label("Function_47_7550")

    SetChrPos(0x28, 0, 20000, 7000, 180)
    OP_71(0x5, 0x5B, 0x82, 0x0, 0x20)

    def lambda_7572():
        OP_96(0xFE, 0x0, 0x1F4, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7572)
    WaitChrThread(0xFE, 1)
    OP_71(0x5, 0x83, 0x96, 0x0, 0x0)

    def lambda_759C():
        OP_96(0xFE, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_759C)
    WaitChrThread(0xFE, 1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0x1F4, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sound(902, 0, 100, 0)
    Sound(833, 0, 70, 0)
    OP_79(0x5)
    OP_71(0x5, 0x406, 0x42E, 0x0, 0x20)
    CancelBlur(500)
    Sleep(500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_47_7550 end

    def Function_48_760A(): pass

    label("Function_48_760A")

    SetChrPos(0x29, -7000, 25000, 2000, 135)
    OP_71(0x9, 0xB, 0x32, 0x0, 0x20)

    def lambda_762C():
        OP_96(0xFE, 0xFFFFE4A8, 0x0, 0x7D0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_762C)
    Sleep(13000)
    Sound(905, 0, 70, 0)
    OP_71(0x9, 0x122, 0x136, 0x0, 0x0)
    OP_79(0x9)
    OP_74(0x9, 0xF)
    OP_71(0x9, 0x136, 0x14A, 0x0, 0x20)
    WaitChrThread(0xFE, 1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0xFA, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sound(902, 0, 100, 0)
    Sound(833, 0, 70, 0)
    CancelBlur(500)
    Sleep(500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_48_760A end

    def Function_49_76B3(): pass

    label("Function_49_76B3")

    SetChrPos(0x2A, 9000, 28000, 2000, 225)
    OP_71(0xA, 0xA, 0x32, 0x0, 0x20)

    def lambda_76D5():
        OP_96(0xFE, 0x2328, 0x3E8, 0x7D0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_76D5)
    WaitChrThread(0xFE, 1)
    OP_71(0xA, 0x33, 0x5A, 0x0, 0x0)

    def lambda_76FF():
        OP_96(0xFE, 0x2328, 0x0, 0x7D0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_76FF)
    WaitChrThread(0xFE, 1)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_25(0x3D3, 0x1E)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 9000, 0, 2000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0x2BC, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_79(0xA)
    OP_71(0xA, 0x172, 0x19A, 0x3E8, 0x20)
    CancelBlur(500)
    Sleep(1000)
    Return()

    # Function_49_76B3 end

    def Function_50_779E(): pass

    label("Function_50_779E")

    Sound(921, 0, 100, 0)
    Sound(922, 0, 50, 0)
    Sound(977, 0, 80, 0)
    Sound(832, 2, 100, 0)
    Sleep(700)
    Sound(922, 0, 40, 0)
    Sound(977, 0, 60, 0)
    Sleep(800)
    Sound(936, 0, 80, 0)
    Sleep(1000)
    Sound(936, 0, 80, 0)
    StopSound(832, 1000, 100)
    Return()

    # Function_50_779E end

    def Function_51_77DE(): pass

    label("Function_51_77DE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7860")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_780E")
    OP_82(0x0, 0xF, 0xBB8, 0x1F4)
    Jump("loc_7858")

    label("loc_780E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7833")
    OP_82(0x4B, 0x96, 0x1388, 0x1F4)
    Jump("loc_7858")

    label("loc_7833")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7858")
    OP_82(0x19, 0x32, 0x1388, 0x1F4)
    Jump("loc_7858")

    label("loc_7858")

    Sleep(500)
    Jump("Function_51_77DE")

    label("loc_7860")

    Return()

    # Function_51_77DE end

    def Function_52_7861(): pass

    label("Function_52_7861")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05620.itc", 0x1E)
    LoadChrToIndex("chr/ch03700.itc", 0x1F)
    LoadChrToIndex("apl/ch51545.itc", 0x20)
    LoadChrToIndex("chr/ch03300.itc", 0x21)
    LoadChrToIndex("chr/ch03400.itc", 0x22)
    LoadChrToIndex("chr/ch02100.itc", 0x23)
    LoadChrToIndex("chr/ch13400.itc", 0x24)
    LoadChrToIndex("chr/ch03600.itc", 0x25)
    LoadChrToIndex("chr/ch03500.itc", 0x26)
    LoadChrToIndex("apl/ch51532.itc", 0x27)
    LoadEffect(0x0, "event/ev500_00.eff")
    SoundLoad(852)
    SoundLoad(3978)
    SetChrPos(0x0, 0, -33620, 0, 0)
    SetChrPos(0x1, 0, -33620, 0, 0)
    SetChrPos(0x2, 0, -33620, 0, 0)
    SetChrPos(0x3, 0, -33620, 0, 0)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -1500, 0, -2000, 270)
    OP_8E(0xC, "ディーター大統領")
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -600, 0, -6300, 270)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x2)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 0, 300, -4900, 270)
    OP_52(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x10, 1, 0, 0)
    PlayEffect(0x0, 0x0, 0x10, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -3700, 0, -700, 270)
    SetChrChipByIndex(0xE, 0x22)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -4100, 0, 400, 270)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -1900, 0, -200, 270)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -4000, 0, -4300, 270)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -5000, 0, -3300, 270)
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -5500, 0, -5000, 270)
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "open")
    OP_70(0x1, 0x12D)
    OP_70(0x2, 0x12D)
    OP_70(0x3, 0x12D)
    OP_70(0x4, 0x12D)
    OP_68(-7500, 2200, -4000, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14500, 0)
    Sound(852, 2, 100, 0)
    OP_68(-2800, 1200, -3040, 3000)
    SetCameraDistance(13500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0141
    ChrTalk(
        0xE,
        "#04612F#3978V#5S#11P#13Aひゃっほう！！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    #C0142
    ChrTalk(
        0xF,
        "#11P#01611F……な、なんだありゃ……\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x14,
        (
            "#12P#04809Fアハハ、こりゃ凄いや！\x02\x03",

            "#04802F《零#2Rゼロ#の至宝》……\x01",
            "よくぞ言ったもんだね！\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x13,
        (
            "#12P#04702Fクク、ゴルディアス級最終型を\x01",
            "３体も同時に……！\x02\x03",

            "しかも《奇蹟》の代行者として\x01",
            "自律行動させられるとは……！\x02\x03",

            "#04709Fハハ、これはあの方にも\x01",
            "良い報告が出来そうだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x12,
        "#12P#04900F#3C#30W………………………………\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xD,
        (
            "#11P#04504Fフン……\x01",
            "確かに大したもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x11,
        (
            "#12P#10811Fフフ、まあ最初ですと\x01",
            "こんなものかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12312F#40W………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x320)

    #C0149
    ChrTalk(
        0xC,
        (
            "#11P#11309Fフフフ……\x01",
            "#4Sハハハハハハハハハハッ！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1650, 1200, -2100, 1500)
    MoveCamera(90, 21, 0, 1500)
    SetCameraDistance(13000, 1500)
    OP_6F(0x79)
    SetCameraDistance(12000, 10000)
    SetChrChipByIndex(0xC, 0x27)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    Sleep(110)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0xC, 0x1)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0150
    ChrTalk(
        0xC,
        (
            "#11304F#30W──今、この瞬間をもって\x01",
            "クロスベルは《聖地》となった！\x02\x03",

            "#11302F帝国と共和国という列強を退け、\x01",
            "大陸全土に新たな秩序を\x01",
            "もたらすための拠点に……！\x02\x03",

            "我がクロイス家の理想と正義を\x01",
            "世界に広めるための中心に……！\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    SetCameraDistance(23000, 5000)
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0xBB8)

    #C0151
    ChrTalk(
        0xC,
        "#11309F#5S#40W#30Aハーッハッハッハッハッハッ！\x02",
    )
    #Auto

    Sleep(2000)
    StopSound(132, 2000, 100)
    StopSound(852, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 3)
    NewScene("t1490", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_52_7861 end

    def Function_53_80CC(): pass

    label("Function_53_80CC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11600.itc", 0x1E)
    LoadChrToIndex("chr/ch13400.itc", 0x1F)
    LoadChrToIndex("chr/ch03600.itc", 0x20)
    LoadChrToIndex("chr/ch04200.itc", 0x21)
    LoadEffect(0x0, "event\\ev500_00.eff")
    SetChrPos(0x0, 0, -33620, 0, 0)
    SetChrPos(0x1, 0, -33620, 0, 0)
    SetChrPos(0x2, 0, -33620, 0, 0)
    SetChrPos(0x3, 0, -33620, 0, 0)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 12300, -33620, 23500, 0)
    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x0, 0xFF, 0x10, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 6900, 0, -14700, 135)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 5700, 0, -15500, 135)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 7500, 0, -16200, 135)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    SetChrPos(0x28, 0, 0, 0, 180)
    OP_D5(0x28, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x406)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "open")
    OP_70(0x1, 0x12D)
    OP_70(0x2, 0x12D)
    OP_70(0x3, 0x12D)
    OP_70(0x4, 0x12D)
    OP_68(0, 6500, 0, 0)
    MoveCamera(147, -3, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(16500, 0)
    OP_F0(0x0, 0x1)
    OP_68(0, 3500, 0, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    OP_68(6800, 1200, -16300, 4000)
    MoveCamera(90, 13, 0, 4000)
    SetCameraDistance(12500, 4000)
    OP_6F(0x79)
    SetCameraDistance(11500, 30000)
    Sleep(300)

    #C0152
    ChrTalk(
        0x14,
        (
            "#6P#04804Fさてと、既に『幻焔#4Rげんえん#計画』は\x01",
            "帝国の方に舞台を移したし……\x02\x03",

            "#04802Fここからは予定通り、\x01",
            "しばらく様子見ってわけかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x12,
        (
            "#04923Fええ、そうなりますね。\x02\x03",

            "#04921F帝国方面の段階が進むまでは\x01",
            "付き合わせてもらいましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x13,
        (
            "#04704F#5Pフフ、現時点で《零の至宝》の力は\x01",
            "消えた《幻の至宝》に匹敵している。\x02\x03",

            "更に、オリジナルが持っていなかった\x01",
            "潜在能力すら垣間#4Rかい ま #見せつつある……\x02\x03",

            "#04702Fクク、どこまで進化させられるか、\x01",
            "クロイス家のお手並みを拝見しようか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x13, 500)
    Sleep(100)

    #C0155
    ChrTalk(
        0x14,
        (
            "#12P#04809Fウフフ……\x01",
            "博士、ノリノリだねぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x14, 0x87, 0x1F4)

    #C0156
    ChrTalk(
        0x14,
        (
            "#6P#04805Fそういえば“彼ら”の方も\x01",
            "やっと動き出したみたいだけど？\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x12,
        (
            "#04924Fむしろ好機でありましょう。\x02\x03",

            "#04922F我らとの立ち位置の違い……\x01",
            "今後のためにも明確にすべきかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x13,
        (
            "#04700F#5Pフフ、それは君たちに任せるよ。\x02\x03",

            "#04704F私はここで、《零の至宝》の\x01",
            "データを取り続けさせてもらう……\x02\x03",

            "#04702F──人と神を繋ぐ究極の\x01",
            "インターフェイスたり得るかをね！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(6800, -800, -16300, 3000)
    StopSound(132, 2000, 90)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_68(12300, -32820, 23400, 0)
    MoveCamera(150, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(35000, 0)
    SetCameraDistance(15000, 9000)
    Sound(132, 2, 50, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    StopSound(132, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("e4020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_53_80CC end

    def Function_54_8859(): pass

    label("Function_54_8859")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11600.itc", 0x1E)
    LoadChrToIndex("chr/ch04200.itc", 0x1F)
    LoadEffect(0x0, "event\\ev500_00.eff")
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 17450, 0, -5600, 225)
    PlayEffect(0x0, 0xFF, 0x10, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 16250, 0, -8350, 45)
    OP_68(17260, 1000, -7120, 0)
    MoveCamera(68, 17, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_894F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8962")
    Sleep(1)
    Jump("loc_894F")

    label("loc_8962")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_54_8859 end

    def Function_55_8970(): pass

    label("Function_55_8970")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12300.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02900.itp")
    LoadChrToIndex("chr/ch05500.itc", 0x1E)
    LoadChrToIndex("chr/ch11600.itc", 0x1F)
    LoadEffect(0x0, "event\\ev500_00.eff")
    SoundLoad(3634)
    SoundLoad(3635)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -22000, -4400, -22000, 225)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -27500, -4400, -32600, 150)
    PlayEffect(0x0, 0xFF, 0x10, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xAF, 0x9B, 0x12C, 0x384, 0x0)
    SetMapObjFrame(0xFF, "sky00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)
    OP_68(-22300, -3300, -44000, 0)
    MoveCamera(195, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(28000, 0)
    OP_68(-27500, -3300, -32600, 7000)
    SetCameraDistance(14000, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0159
    AnonymousTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#30W………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    ClearChrFlags(0x11, 0x80)

    #N0160
    NpcTalk(
        0x11,
        "マリアベルの声",
        (
            "フフ……\x01",
            "してやられましたわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-24000, -3300, -24000, 0)
    MoveCamera(180, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_68(-27350, -3300, -31200, 5000)
    MoveCamera(150, 17, 0, 5000)
    SetCameraDistance(13500, 5000)

    def lambda_8C7F():
        OP_95(0xFE, -26500, -4400, -26500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8C7F)
    WaitChrThread(0x11, 1)

    def lambda_8C9D():
        OP_95(0xFE, -27000, -4400, -29500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8C9D)
    WaitChrThread(0x11, 1)
    TurnDirection(0x10, 0x11, 400)
    OP_6F(0x79)
    SetCameraDistance(11500, 50000)
    Sleep(150)

    #C0161
    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12300Fベル……\x02\x03",

            "#12308Fディーターが捜してるみたいだけど\x01",
            "行かなくてもいいの？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0162
    AnonymousTalk(
        0x11,
        (
            "うふふ、お父様にはもう少し\x01",
            "焦っていただきましょう。\x02\x03",

            "やはり《鐘》の共鳴がないと\x01",
            "《結界》の展開は難しいですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    #C0163
    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12303F#30W……うん、今のままだと。\x02\x03",

            "#12308Fあの子#6Rアイオーン#たちは動けるけど\x01",
            "《空》の力は使えないかな……\x02\x03",

            "#12315F──ロイドたち、来るよ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x11,
        (
            "#6P#02913Fフフ、困りましたわね。\x02\x03",

            "これでは予定通り動くしか\x01",
            "無くなってしまいますわ。\x02\x03",

            "#02911F“彼”のプラン通りに。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12303F#30W………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x11,
        (
            "#6P#02902F全てはキーアさん次第……\x01",
            "わたくし達は従うだけです。\x02\x03",

            "#02903Fここで降りるか──\x01",
            "それとも全てを叶えるか#14R㈲　㈲　㈲　㈲　㈲　㈲　㈲#。\x02\x03",

            "#02912Fそろそろ選ぶ時ですわよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12304F#40W…………うん。\x02\x03",

            "#12302F最初から、他に道が無いのは\x01",
            "キーアにも分かってたから……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x73, 0x1F4)
    Sleep(300)
    OP_63(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)
    Sleep(800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, -1, -1, -1)

    #C0168
    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12304F#3634V#40W#59Aロイドやエリィ、ティオやランディ、\x01",
            "シズクやみんなのためにも……\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(11000, 2000)
    StopSound(132, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0169
    AnonymousTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3635V#40W#32A──きっと全てを叶えてみせる。\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    StopBGM(0x1770)
    WaitBGM()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("e302B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_55_8970 end

    def Function_56_91CA(): pass

    label("Function_56_91CA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev17031.eff")
    SoundLoad(980)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x5, 0x28)
    OP_49()
    SetChrPos(0x28, 0, 0, 0, 0)
    OP_93(0x28, 0xB4, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB, 0x32, 0x0, 0x20)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1194), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-570, 2100, -8640, 0)
    MoveCamera(144, 45, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(130610, 0)
    Sound(980, 2, 20, 0)
    FadeToBright(1000, 0)
    OP_68(3650, 11100, 4520, 10000)
    MoveCamera(133, -7, 0, 10000)
    OP_6E(800, 10000)
    SetCameraDistance(54000, 10000)
    BeginChrThread(0x29, 0, 0, 57)
    OP_0D()
    Sleep(7000)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 200000, 45500, -200000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    Sleep(1000)
    StopSound(980, 1000, 10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopEffect(0x0, 0x2)
    SetScenarioFlags(0x23, 2)
    NewScene("e4310", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_56_91CA end

    def Function_57_933E(): pass

    label("Function_57_933E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_937C")
    Sleep(600)
    OP_98(0xFE, 0x0, 0xFFFFF8F8, 0x0, 0x258, 0x1)
    Sleep(600)
    OP_98(0xFE, 0x0, 0x708, 0x0, 0x258, 0x1)
    Jump("Function_57_933E")

    label("loc_937C")

    Return()

    # Function_57_933E end

    def Function_58_937D(): pass

    label("Function_58_937D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_F3(200000)
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x1, 0x0)
    LoadEffect(0x0, "event/ev17031.eff")
    LoadEffect(0x7, "event/ev17022.eff")
    LoadEffect(0x8, "event/eva03_01.eff")
    SoundLoad(980)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x5, 0x28)
    OP_49()
    SetChrPos(0x28, 0, 0, 0, 0)
    OP_93(0x28, 0xB4, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB, 0x32, 0x0, 0x20)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1194), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x29, 0x80)
    OP_78(0x9, 0x29)
    OP_49()
    SetChrPos(0x29, -15000, 10200, 60080, 0)
    OP_93(0x29, 0xB4, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0xDD)
    SetChrFlags(0x29, 0x1)
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_87(0x7, 0xFF, 0x9, "Null_wing_r0 (66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x9, "Null_wing_r1(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x9, "Null_wing_r2(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x9, "Null_wing_l0(69)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x9, "Null_wing_l1(70)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x9, "Null_wing_l2(71)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    ClearChrFlags(0x2B, 0x80)
    OP_78(0x13, 0x2B)
    OP_49()
    SetChrPos(0x2B, 200000, 45000, -200000, 0)
    OP_93(0x2B, 0x13B, 0x0)
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_74(0x13, 0x1E)
    OP_71(0x13, 0x1, 0x78, 0x0, 0x20)
    OP_FF(0x13, 0x96, 0x96, 0x96)
    OP_75(0x13, 0x1, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 200000, 45500, -200000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(980, 2, 20, 0)
    FadeToBright(1000, 0)
    OP_68(5000, 9900, 1500, 0)
    MoveCamera(154, 2, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(42350, 0)
    OP_68(5000, 9900, 1500, 5000)
    MoveCamera(136, 3, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(42350, 5000)
    OP_0D()
    Sleep(1500)
    OP_75(0x13, 0x2, 0x0)
    OP_93(0x29, 0xA1, 0x28)
    EndChrThread(0x29, 0x0)
    BeginChrThread(0x29, 0, 0, 60)
    BeginChrThread(0x29, 1, 0, 61)
    Sleep(500)
    Sound(499, 0, 100, 0)
    Sound(998, 0, 100, 0)
    Sleep(4000)
    OP_6F(0x79)
    OP_FF(0x13, 0x3E8, 0x3E8, 0x3E8)
    SetMapObjFlags(0x13, 0x4)
    PlayEffect(0x8, 0xFF, 0x29, 0x5, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0xFF, 0x29, 0x5, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(999, 0, 100, 0)
    OP_68(133720, 25300, -151690, 0)
    MoveCamera(323, 6, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(107240, 0)
    Fade(500)
    OP_0D()
    BlurSwitch(0x3E8, 0x77FFFFFF, 0x0, 0x1, 0xA)
    Sleep(1500)
    EndChrThread(0x29, 0x0)
    OP_6F(0x79)
    StopSound(980, 1000, 10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 3)
    NewScene("e4310", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_58_937D end

    def Function_59_9815(): pass

    label("Function_59_9815")

    ClearMapObjFlags(0x9, 0x20)
    OP_79(0x9)
    Sound(982, 0, 100, 0)
    Sound(905, 0, 100, 0)
    OP_71(0x9, 0xC9, 0xDC, 0x0, 0x0)
    Sleep(300)
    Sleep(1000)
    OP_79(0x9)
    OP_70(0x9, 0xDD)
    Return()

    # Function_59_9815 end

    def Function_60_9844(): pass

    label("Function_60_9844")

    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x1F40, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x2EE0, 0x1)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 5500, 10200, 3080)
    OP_9F(0x1, 50000, 10200, -120000)
    OP_9F(0x1, 72000, 14200, -155000)
    OP_9F(0x1, 95000, 18200, -180000)
    OP_9F(0x1, 120000, 22200, -200000)
    OP_9F(0x1, 150000, 25200, -215000)
    OP_9F(0x1, 203000, 33200, -225000)
    OP_9F(0x2, 0xFE, 65000, 0x2)
    Return()

    # Function_60_9844 end

    def Function_61_98E1(): pass

    label("Function_61_98E1")

    Sleep(2000)
    OP_74(0x9, 0x3)
    OP_71(0x9, 0x104, 0x103, 0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_61_98E1 end

    def Function_62_98F8(): pass

    label("Function_62_98F8")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 64)
    Call(0, 65)
    LoadEffect(0x0, "event/ev17050.eff")
    LoadEffect(0x1, "event/ev17051.eff")
    SoundLoad(943)
    SoundLoad(933)
    SoundLoad(927)
    SoundLoad(950)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11300.itp")
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    OP_49()
    SetChrPos(0x28, 0, 0, 6500, 180)
    OP_D5(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x42E)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 0x3)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, 0, 180)
    OP_8E(0xC, "ディーター大統領")
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, -600, 0, -20000, 0)
    SetChrPos(0x102, 600, 0, -20000, 0)
    SetChrPos(0x103, -1100, 0, -21100, 0)
    SetChrPos(0x104, 1100, 0, -21100, 0)
    SetChrPos(0xF4, -600, 0, -22200, 0)
    SetChrPos(0xF5, 600, 0, -22200, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(0, 1100, -20000, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    FadeToBright(500, 0)
    OP_0D()

    #N0170
    NpcTalk(
        0xC,
        "男性の声",
        (
            "……やれやれ。\x01",
            "招かれざる客がここまで\x01",
            "辿りついてしまうとは。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    PlayBGM("ed7356", 0)
    OP_68(0, 2500, -2000, 3000)
    MoveCamera(0, 9, 0, 3000)
    SetCameraDistance(13000, 3000)
    OP_6F(0x79)
    Sleep(500)

    #C0171
    ChrTalk(
        0x102,
        "#2P#00107F#N……おじさま……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0172
    ChrTalk(
        0x101,
        "#1P#00007F#Nディーターさん……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1300, -5000, 0)
    MoveCamera(34, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -500, 0, -15500, 0)
    SetChrPos(0x102, 500, 0, -15500, 0)
    SetChrPos(0x103, -1000, 0, -17000, 0)
    SetChrPos(0x104, 1000, 0, -17000, 0)
    SetChrPos(0xF4, 0, 0, -16700, 0)
    SetChrPos(0xF5, 0, 0, -17700, 0)
    SetCameraDistance(18000, 2000)

    def lambda_9D04():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFDECC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9D04)
    Sleep(50)

    def lambda_9D21():
        OP_96(0xFE, 0x320, 0x0, 0xFFFFDECC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9D21)
    Sleep(50)

    def lambda_9D3E():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFDA1C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_9D3E)
    Sleep(50)

    def lambda_9D5B():
        OP_96(0xFE, 0xFFFFF95C, 0x0, 0xFFFFD8F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9D5B)

    def lambda_9D75():
        OP_96(0xFE, 0x6A4, 0x0, 0xFFFFD8F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9D75)

    def lambda_9D8F():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFD5D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_9D8F)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    SetCameraDistance(17000, 30000)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0173
    AnonymousTalk(
        0xC,
        (
            "フフ……\x01",
            "久しぶりだね、諸君。\x02\x03",

            "しかし昼食#4Rランチ#の約束をした\x01",
            "覚えはないのだが……\x02\x03",

            "ひょっとして日時を\x01",
            "間違えてはいないかね？\x02",
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

    #C0174
    ChrTalk(
        0x101,
        (
            "#00003F#12Pアポイント無しの訪問、\x01",
            "申し訳ありません。\x02\x03",

            "#00001F──ですがこちらにも\x01",
            "譲れない事情がありまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x103,
        (
            "#12P#N#00206F独立国の取り消し、\x01",
            "それに市内の魔導兵など\x01",
            "色々ありますが……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0176
    ChrTalk(
        0x104,
        (
            "#00307F#12Pまずはとっとと\x01",
            "キー坊を返してもらおうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xC,
        "#5P#11304Fああ、構わないよ？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0178
    ChrTalk(
        0x101,
        "#00011F#12Pな……\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xC,
        (
            "#5P#11300Fフフ、君たちは何か、\x01",
            "勘違いをしているようだね。\x02\x03",

            "我々は別に、キーア君に無理矢理、\x01",
            "協力してもらっているわけでない。\x02\x03",

            "#11303Fこのクロスベルを取り巻いている、\x01",
            "途方もない困難……\x02\x03",

            "#11301Fそれを解決するために\x01",
            "彼女は進んで協力してくれたのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x103,
        "#12P#N#00208Fそれは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0181
    ChrTalk(
        0x102,
        (
            "#00106F#12P──そう仕向けたのもまた、\x01",
            "おじさま達のはずです。\x02\x03",

            "#00108F猟兵団を影で操り、\x01",
            "クロスベル市を襲撃させることで、\x01",
            "市民の独立の気運を煽り……\x02\x03",

            "#00101F帝国と共和国の資産を凍結することで\x01",
            "自治州存亡の危機を演出した……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2D9")

    #C0182
    ChrTalk(
        0x10A,
        (
            "#00606F#12P#N……真偽はともかく、\x01",
            "許される所業ではありませんな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A386")

    label("loc_A2D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A332")

    #C0183
    ChrTalk(
        0x105,
        (
            "#10404F#12P#Nまあ、マッチポンプ、\x01",
            "ここに極まれりって感じだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A386")

    label("loc_A332")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A386")

    #C0184
    ChrTalk(
        0x109,
        (
            "#10106F#12P#N……真偽はともかく、\x01",
            "やはり許されないと思います。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A386")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A3EB")

    #C0185
    ChrTalk(
        0x106,
        (
            "#10708F#12P#Nそしてその状況を\x01",
            "キーアちゃんに突きつけて\x01",
            "決断を迫った……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A4B0")

    label("loc_A3EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A455")

    #C0186
    ChrTalk(
        0x109,
        (
            "#10108F#12P#Nそしてその状況を\x01",
            "キーアちゃんに突きつけて\x01",
            "決断を迫ったんですね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A4B0")

    label("loc_A455")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4B0")

    #C0187
    ChrTalk(
        0x105,
        (
            "#10408F#12P#Nそしてその状況を\x01",
            "あの子に突きつけて\x01",
            "決断を迫ったわけだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A4B0")

    OP_57(0x0)
    OP_5A()

    #C0188
    ChrTalk(
        0x104,
        (
            "#00301F#12P白い歯が売りのナイスミドルにしちゃ\x01",
            "エゲツなさすぎやしねぇか？\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x101,
        (
            "#00006F#12Pディーター大統領……\x01",
            "いえ、ディーターさんと\x01",
            "呼ばせてもらいます。\x02\x03",

            "#00013Fそれが貴方の“正義”ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xC,
        "#5P#11304Fああ──その通りだ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(0, 1200, 10, 0)
    MoveCamera(57, 7, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    MoveCamera(37, 11, 0, 50000)
    SetCameraDistance(19000, 50000)
    OP_0D()
    Sleep(150)

    #C0191
    ChrTalk(
        0xC,
        (
            "#5P#11303F現実の政治は\x01",
            "奇麗事ばかりではない。\x02\x03",

            "あの程度の政治工作ならば\x01",
            "むしろ手ぬるいくらいだろう。\x02\x03",

            "#11301F１２年前、帝国がリベールに\x01",
            "侵攻する時に起こした悲劇を\x01",
            "君たちは知っているかね？\x02\x03",

            "もしくは共和国が民主化する時に\x01",
            "断行された血塗られた粛清は？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x101,
        "#00007F#12P#Nだ、だからといって……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0193
    ChrTalk(
        0x102,
        (
            "#00108F#12P#Nおじさま達のしている事が\x01",
            "正当化されるとでも……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0194
    ChrTalk(
        0xC,
        (
            "#11304F正当化は“される”ものではない。\x01",
            "力と意志をもって“する”ものだよ。\x02\x03",

            "#11300F私はクロイス家の当主だが、\x01",
            "元々、一族の使命については\x01",
            "さほど熱心なわけでは無かった。\x02\x03",

            "そのあたりはむしろ、\x01",
            "娘の方が詳しいくらいだからね。\x02\x03",

            "#11303F──だが、始祖が夢見た\x01",
            "新たなる《至宝》の誕生が\x01",
            "実現可能だと判った時……\x02\x03",

            "私は狂喜し、クロイス家に\x01",
            "生まれたことに感謝したものだよ。\x02\x03",

            "#11302Fこの激動の時代を治め、\x01",
            "《正義》を広められるだけの力を\x01",
            "手に入れられるのだからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x103,
        "#00205F#12P#N《正義》……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0196
    ChrTalk(
        0x101,
        (
            "#00011F#12P#Nそれでは、貴方は……\x02\x03",

            "#00006F自らの利益のためでも、\x01",
            "支配欲のためでもなく……\x02\x03",

            "#00010F《正義》を実現するために\x01",
            "ここまでの事をしたと……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0197
    ChrTalk(
        0xC,
        (
            "#11309Fハハ、それ以外に\x01",
            "どんな理由があると言うのだね？\x02\x03",

            "#11300F１０年前、ＩＢＣの資産が\x01",
            "大陸一を達成した時点で\x01",
            "富を求める必要も無くなった。\x02\x03",

            "大陸全土を支配するという、\x01",
            "時代錯誤な幻想にも興味はない。\x02\x03",

            "#11306F私はね──我慢がならないのだよ。\x02\x03",

            "“国家”という枠組みに囚われて\x01",
            "無益な争いを繰り広げるこの世界に。\x02\x03",

            "#11303Fその意味では“独立国”という\x01",
            "形式に拘っているわけでもない。\x02\x03",

            "マクダエル議長の宣言通り、\x01",
            "無効とされても構わないのさ。\x02\x03",

            "#11301F──私が理想とする《正義》が\x01",
            "世界に遍#2Rあまね#く広まるのであれば……\x02\x03",

            "#11302Fその《正義》によって秩序が保たれ、\x01",
            "平和な世界が築かれるのであれば！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ACF7")

    #C0198
    ChrTalk(
        0x10A,
        "#00610F#12P#N……馬鹿な。\x02",
    )

    CloseMessageWindow()

    label("loc_ACF7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD28")

    #C0199
    ChrTalk(
        0x105,
        "#10401F#12P#N本気かい……？\x02",
    )

    CloseMessageWindow()

    label("loc_AD28")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD72")

    #C0200
    ChrTalk(
        0x109,
        (
            "#10106F#12P#Nきょ、共感できなくは\x01",
            "ありませんけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD72")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ADC3")

    #C0201
    ChrTalk(
        0x106,
        (
            "#10706F#12P#N……私にはただの\x01",
            "絵空事にしか聞こえません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADC3")

    OP_57(0x0)
    OP_5A()

    #C0202
    ChrTalk(
        0x104,
        (
            "#00306F#12P#Nなんつーか……ここまで\x01",
            "ガチだとは思わなかったぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0203
    ChrTalk(
        0x103,
        (
            "#00208F#12P#N……ですがその《正義》の幻想も\x01",
            "ある程度は実現できてしまう……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0204
    ChrTalk(
        0x102,
        (
            "#00106F#12P#Nそうね、キーアちゃんという\x01",
            "《零の至宝》があれば……\x02\x03",

            "#00108F……既存の政治思想にはない、\x01",
            "反則とでも言うべき状況設定だわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0205
    ChrTalk(
        0x101,
        "#00008F#12P#N#30W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1100, -5000, 0)
    MoveCamera(147, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    SetMapObjFlags(0x5, 0x4)
    SetChrPos(0xF4, 500, 0, -9700, 0)
    SetChrPos(0xF5, -500, 0, -10700, 0)
    MoveCamera(151, 13, 0, 30000)
    SetCameraDistance(19000, 30000)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0206
    ChrTalk(
        0x101,
        (
            "#00006F#11P──ディーターさん。\x02\x03",

            "俺は……貴方の考えには\x01",
            "色々と勉強させてもらいました。\x02\x03",

            "#00001Fですが貴方の《正義》については……\x01",
            "少し過大評価をしていたようです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0207
    ChrTalk(
        0xC,
        "#6P#11301F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        (
            "#00008F俺たちは警察官で、\x01",
            "しかも特務支援課の所属です。\x02\x03",

            "#00003F法というルールに則りながら、\x01",
            "市民に寄り添う形で《正義》を体現する。\x02\x03",

            "#00001Fですが……\x01",
            "必ずしも正解があるとは限りませんし、\x01",
            "迷ったりする事も多くあります。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1E2")

    #C0209
    ChrTalk(
        0x10A,
        (
            "#11P#00603F……当然だ。\x01",
            "治安維持や安全保障なども\x01",
            "正解というものがある訳ではない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1E2")


    #C0210
    ChrTalk(
        0x102,
        (
            "#11P#00106F……そうね。\x01",
            "立場が異なれば《正義》の在り方も\x01",
            "変わってくるものだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x103,
        (
            "#11P#00204F迷いながら、時には失敗しつつも\x01",
            "《正義》を追い求めていく……\x02\x03",

            "#00202Fかつてディーターさんに\x01",
            "言われた事でもありますよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x104,
        (
            "#5P#00302Fなんつーか、あの時の演説と\x01",
            "全然違うような気がするんだが？\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xC,
        (
            "#6P#11303F……あれは力と意志が\x01",
            "足りていない状況においての\x01",
            "方法論について語ったまでだ。\x02\x03",

            "その双方が揃っている状況で\x01",
            "《正義》を行使しないこと……\x02\x03",

            "#11301Fそれは“怠惰”ではないのかね？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0214
    ChrTalk(
        0x101,
        "#00013F#4S#11P──違う！\x02",
    )

    CloseMessageWindow()

    def lambda_B3FD():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFE2B4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B3FD)
    WaitChrThread(0x101, 1)
    Sleep(150)

    #C0215
    ChrTalk(
        0x101,
        (
            "#00003F#11P《正義》は移ろいやすく、\x01",
            "形の定まらないものだ……！\x02\x03",

            "それを追い求め続ける事にこそ、\x01",
            "皆にとっての価値がある……！\x02\x03",

            "#00007F貴方のしようとしている事は\x01",
            "《正義》を型にはめて画一化し、\x01",
            "押し付ける事でしかない……！\x02\x03",

            "そんなものが本当に\x01",
            "貴方の求める《正義》なのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xC,
        (
            "#6P#11310Fぐっ……\x02\x03",

            "#11307F現に私は\x01",
            "クロスベルの政治状況に風穴を開けて\x01",
            "幾つもの改革を成し遂げた！\x02\x03",

            "その成果を否定するというのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x102,
        (
            "#11P#00106F……それとこれとは話が別です。\x02\x03",

            "#00108Fおじさまの全てを\x01",
            "否定するつもりはありませんし、\x01",
            "学ぶ所が多かったのは確かです。\x02\x03",

            "#00101Fだからこそ……その欺瞞#4R ぎ まん#と\x01",
            "勘違いを指摘せざるを得ません。\x02\x03",

            "#00107F貴方を尊敬していた者として……\x01",
            "間違いに気付いて欲しい意味でも！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0218
    ChrTalk(
        0xC,
        "#6P#11302F#4Sいいだろう！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1100, 2000, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    ClearMapObjFlags(0x5, 0x4)
    SetChrPos(0xF4, -500, 0, -9700, 0)
    SetChrPos(0xF5, 500, 0, -10700, 0)
    OP_0D()
    Sleep(150)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xC, 0x1)
    Sleep(70)
    SetChrSubChip(0xC, 0x2)
    OP_68(0, 1100, -4000, 1500)
    MoveCamera(0, 21, 0, 1500)
    SetCameraDistance(27000, 1500)
    OP_6F(0x79)
    Fade(500)
    BeginChrThread(0x32, 1, 0, 66)
    SetMapObjFrame(0xFF, "futa03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "move")
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_B85A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B85A)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_B87F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B87F)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0219
    ChrTalk(
        0x101,
        "#6P#00005F……！？\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x104,
        "#00307F#6P#Nな、なんだぁ！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(10, 1300, 0, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)
    OP_93(0x103, 0x0, 0x0)
    OP_93(0x104, 0x0, 0x0)
    MoveCamera(45, 13, 0, 10000)
    SetCameraDistance(13500, 10000)
    OP_0D()
    SetMessageWindowPos(250, 250, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B99A")

    #A0221
    AnonymousTalk(
        0x105,
        (
            "#10407Fこれは……\x01",
            "《魔導》の力……！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA19")

    label("loc_B99A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B9DB")

    #A0222
    AnonymousTalk(
        0x106,
        (
            "#10707Fこれは……\x01",
            "《魔導》の力……！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA19")

    label("loc_B9DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BA19")

    #A0223
    AnonymousTalk(
        0x109,
        (
            "#10107F導力魔法……\x01",
            "──ううん、違う！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA19")

    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(0, 250, -1, -1)

    #A0224
    AnonymousTalk(
        0x103,
        (
            "#00201F気を付けてください！\x02\x03",

            "オルキスタワーから\x01",
            "彼を中心に膨大な霊力が\x01",
            "集まり始めています……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    #C0225
    ChrTalk(
        0xC,
        (
            "#11304Fフフ、ベルほどではないが\x01",
            "クロイス家の当主として\x01",
            "この程度は嗜#2Rたしな#んでいてね……\x02\x03",

            "#11300Fそして、このオルキスタワーの\x01",
            "“霊子変換機能”を利用すれば──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0226
    ChrTalk(
        0xC,
        "#11307F#4S#38Aこんな事も可能になるのだよ！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_6F(0x79)
    Sound(950, 2, 40, 0)
    Sound(935, 0, 100, 0)
    PlayEffect(0x1, 0x1, 0xC, 0x5, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_BBCE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_BBCE)
    StopEffect(0x0, 0x2)
    WaitChrThread(0xC, 2)
    OP_68(0, 4000, 5000, 3000)
    SetChrFlags(0xC, 0x20)

    def lambda_BBFC():
        OP_96(0xFE, 0x0, 0xFA0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_BBFC)
    WaitChrThread(0xC, 1)
    StopEffect(0x1, 0x2)
    Sound(930, 0, 100, 0)
    StopSound(933, 1000, 100)
    StopSound(950, 1000, 40)
    OP_6F(0x79)
    Sleep(1500)
    StopSound(927, 1000, 100)

    #C0227
    ChrTalk(
        0x102,
        "#00105Fあ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC82")

    #C0228
    ChrTalk(
        0x10A,
        "#00605F吸い込まれただと……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_BCED")

    label("loc_BC82")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BCBC")

    #C0229
    ChrTalk(
        0x109,
        "#10111Fす、吸い込まれた……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_BCED")

    label("loc_BCBC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BCED")

    #C0230
    ChrTalk(
        0x106,
        "#10712F吸い込まれた……！？\x02",
    )

    CloseMessageWindow()

    label("loc_BCED")

    OP_68(0, 4000, 5000, 6000)
    MoveCamera(0, -5, 0, 6000)
    SetCameraDistance(12500, 6000)
    Sound(140, 0, 100, 0)
    Sound(859, 0, 50, 0)
    OP_71(0x5, 0x406, 0x42E, 0x0, 0x20)
    Sleep(1000)
    BeginChrThread(0x28, 3, 0, 63)
    Sleep(2000)
    OP_6F(0x79)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("男性の声")

    #A0231
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30Wふむ……視界と制御も良好だ。\x02",
        )
    )

    CloseMessageWindow()

    #A0232
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W《至宝》の力を受けつつ\x01",
            "自在に操る事が出来そうだな。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    WaitChrThread(0x28, 3)
    StopBGM(0xBB8)
    OP_68(0, 2500, -7500, 2500)
    MoveCamera(0, 5, 0, 2500)
    SetCameraDistance(11000, 2500)
    Sleep(2000)

    def lambda_BDFC():
        OP_97(0x101, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BDFC)
    Sleep(50)

    def lambda_BE19():
        OP_97(0x102, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BE19)
    Sleep(50)

    def lambda_BE36():
        OP_97(0x103, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BE36)
    Sleep(50)

    def lambda_BE53():
        OP_97(0x104, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BE53)
    Sleep(50)

    def lambda_BE70():
        OP_97(0xF4, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_BE70)
    Sleep(50)

    def lambda_BE8D():
        OP_97(0xF5, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_BE8D)
    OP_6F(0x79)
    WaitChrThread(0xF5, 0)
    Sleep(300)

    #C0233
    ChrTalk(
        0x102,
        "#00107F#12P#Nお、おじさま……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #N0234
    NpcTalk(
        0x101,
        "ティオ",
        (
            "#00207F#6P#N霊的な位相空間から人形兵器を\x01",
            "コントロールしている……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0235
    ChrTalk(
        0x104,
        "#00310F#12P#Nオイオイ、そんなのありかよ！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7554", 0)
    Fade(250)
    OP_68(0, 4000, 5000, 0)
    MoveCamera(0, 5, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -800, 0, -5500, 0)
    SetChrPos(0x102, 800, 0, -5500, 0)
    SetChrPos(0x103, -1700, 0, -7000, 0)
    SetChrPos(0x104, 1700, 0, -7000, 0)
    SetChrPos(0xF4, 0, 0, -6700, 0)
    SetChrPos(0xF5, 0, 0, -7800, 0)
    SetCameraDistance(14500, 1000)
    OP_0D()
    OP_71(0x5, 0x492, 0x4BA, 0x0, 0x0)
    Sleep(200)
    Sound(905, 0, 100, 0)
    OP_79(0x5)
    OP_71(0x5, 0x4BA, 0x4CE, 0x0, 0x20)
    Sound(951, 0, 100, 0)
    Sleep(100)
    Sound(833, 0, 100, 0)
    Sound(859, 0, 100, 0)
    OP_6F(0x79)
    OP_68(0, 2000, -1000, 12000)
    MoveCamera(35, 5, 0, 12000)
    SetCameraDistance(17000, 12000)
    Sleep(1000)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("ディーターの声")

    #A0236
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#80Aハハ、これぞ《正義》を体現し、\x01",
            "世に知らしめるための白き機体……\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sound(905, 0, 100, 0)
    OP_71(0x5, 0x4CE, 0x4E2, 0x0, 0x0)
    OP_79(0x5)
    Sound(951, 0, 100, 0)
    OP_71(0x5, 0x335, 0x348, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x349, 0x352, 0x0, 0x20)
    Sound(833, 0, 100, 0)
    Sleep(800)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("ディーターの声")

    #A0237
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#36Aさあ──\x01",
            "“証明”してみるとしようか。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("ディーターの声")

    #A0238
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#80A私の《正義》と君たちの《正義》……\x01",
            "果たしてどちらが正しいのかを！\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_6F(0x79)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x24)
    SetChrSubChip(0xF5, 0x0)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C233")
    Sound(540, 0, 50, 0)

    label("loc_C233")

    OP_0D()
    Sleep(300)

    #C0239
    ChrTalk(
        0x101,
        "#00010F#12P#Nくっ……望むところだ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0240
    ChrTalk(
        0x102,
        (
            "#00107F#12P#N全力をもって\x01",
            "挑ませてもらいます……！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x3B6)
    OP_24(0x39F)
    OP_24(0x3A5)
    OP_24(0x3AF)
    Battle("BattleInfo_7B4", 0x30200011, 0x0, 0x100, 0x11, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 67)
    Return()

    # Function_62_98F8 end

    def Function_63_C2C9(): pass

    label("Function_63_C2C9")

    OP_71(0x5, 0x442, 0x492, 0x0, 0x0)
    Sleep(200)
    Sound(905, 0, 100, 0)
    Sleep(1000)
    Sound(905, 0, 100, 0)
    OP_79(0x5)
    OP_71(0x5, 0x406, 0x42E, 0x0, 0x20)
    Return()

    # Function_63_C2C9 end

    def Function_64_C2F7(): pass

    label("Function_64_C2F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C30F")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_C30F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C327")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_C327")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C33F")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_C33F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C357")
    LoadChrToIndex("chr/ch00950.itc", 0x23)

    label("loc_C357")

    Return()

    # Function_64_C2F7 end

    def Function_65_C358(): pass

    label("Function_65_C358")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C370")
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_C370")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C388")
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_C388")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C3A0")
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_C3A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C3B8")
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_C3B8")

    Return()

    # Function_65_C358 end

    def Function_66_C3B9(): pass

    label("Function_66_C3B9")

    Sound(922, 0, 100, 0)
    Sound(927, 2, 100, 0)
    Sound(933, 2, 100, 0)
    Sound(943, 2, 100, 0)
    Sleep(1000)
    OP_24(0x3AF)
    Sound(143, 0, 50, 0)
    Return()

    # Function_66_C3B9 end

    def Function_67_C3DE(): pass

    label("Function_67_C3DE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51769.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 64)
    Call(0, 65)
    LoadEffect(0x0, "event/ev17052.eff")
    LoadEffect(0x1, "event/ev17051.eff")
    SoundLoad(933)
    SoundLoad(927)
    SoundLoad(943)
    SoundLoad(950)
    SoundLoad(579)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x5)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 2000, 5500, 180)
    OP_8E(0xC, "ディーター大統領")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x24)
    SetChrSubChip(0xF5, 0x0)
    SetChrPos(0x101, -800, 0, -5500, 0)
    SetChrPos(0x102, 800, 0, -5500, 0)
    SetChrPos(0x103, -1700, 0, -7000, 0)
    SetChrPos(0x104, 1700, 0, -7000, 0)
    SetChrPos(0xF4, 0, 0, -6700, 0)
    SetChrPos(0xF5, 0, 0, -7800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    SetChrPos(0x28, 0, 0, 6500, 180)
    OP_D5(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x3A2)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    SetMapObjFrame(0xFF, "futa03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "open")
    OP_68(0, 3500, -1000, 0)
    MoveCamera(35, 5, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    BeginChrThread(0x32, 1, 0, 69)
    OP_68(0, 1500, -1000, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0241
    ChrTalk(
        0x101,
        "#00000F#12Pや、やったか……！\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x104,
        "#00300F#12Pこれで何とか……！\x02",
    )

    CloseMessageWindow()
    PlayBGM("ed7554", 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 6500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(930, 0, 80, 0)
    Sound(933, 2, 100, 0)
    Sound(927, 2, 100, 0)
    EndChrThread(0x32, 0x1)
    Sleep(1000)
    SetMapObjFlags(0x18, 0x4)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0243
    ChrTalk(
        0x103,
        (
            "#00207F#12P霊子エネルギー、\x01",
            "再び充填されています！\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x102,
        "#00110F#12Pそんな……！\x02",
    )

    CloseMessageWindow()
    OP_68(0, 2000, -1000, 2000)
    Sound(905, 0, 100, 0)
    OP_74(0x5, 0xF)
    OP_71(0x5, 0x3A3, 0x3CA, 0x0, 0x0)
    Sleep(2000)
    Sound(902, 0, 70, 0)
    OP_79(0x5)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB, 0x32, 0x0, 0x20)
    Sound(951, 0, 100, 0)
    OP_6F(0x79)
    Sleep(800)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(10, 70, -1, -1)
    SetChrName("ディーターの声")

    #A0245
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30Wフフ、《零の至宝》より\x01",
            "この機体は無制限の力を得ている。\x02",
        )
    )

    CloseMessageWindow()

    #A0246
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W決定的に破壊されない限り、\x01",
            "敗北はあり得ないというわけだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0247
    ChrTalk(
        0x101,
        "#00010F#12P#Nくっ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C908")

    #C0248
    ChrTalk(
        0x10A,
        "#00610F#12P#Nそういう事か……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_C908")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C946")

    #C0249
    ChrTalk(
        0x105,
        "#10410F#12P#Nさすがに反則すぎるね……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_C946")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C984")

    #C0250
    ChrTalk(
        0x109,
        "#10110F#12P#Nくっ……何か手立ては……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_C984")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C9C8")

    #C0251
    ChrTalk(
        0x106,
        "#10708F#12P#N（……勝機を探さないと……！）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_C9C8")

    Sleep(500)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(10, 70, -1, -1)
    SetChrName("ディーターの声")

    #A0252
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30Wフフ、君たちの命を\x01",
            "奪うつもりは毛頭ないさ。\x02",
        )
    )

    CloseMessageWindow()

    #A0253
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W大人しく降伏して、\x01",
            "私の理想に協力してくれれば──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xFA0)
    Sound(954, 0, 100, 0)
    Sound(922, 0, 100, 0)
    StopSound(933, 1000, 100)
    StopSound(927, 1000, 100)
    Fade(250)
    ClearMapObjFlags(0x5, 0x20)
    OP_70(0x5, 0xB)
    OP_0D()
    StopEffect(0x0, 0x2)
    Sleep(1500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(10, 70, -1, -1)
    SetChrName("ディーターの声")

    #A0254
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S　 ！？\x02",
        )
    )

    CloseMessageWindow()
    Sound(955, 0, 100, 0)

    #A0255
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "な、なんだ……？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    OP_70(0x14, 0xB)
    Fade(1000)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    Sleep(1500)

    #C0256
    ChrTalk(
        0x104,
        "#00301F#12P#Nど、どうしたってんだ？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0257
    ChrTalk(
        0x103,
        (
            "#00205F#12P#N霊子エネルギーの供給が\x01",
            "途絶えた……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_71(0x14, 0x564, 0x58C, 0x0, 0x0)
    Sound(905, 0, 100, 0)
    Sound(954, 0, 100, 0)
    OP_79(0x14)
    Sound(902, 0, 100, 0)
    OP_68(0, 1000, -1000, 2000)
    MoveCamera(35, 19, 0, 2000)
    SetCameraDistance(35000, 2000)
    Sleep(1500)
    Fade(500)
    BeginChrThread(0x32, 1, 0, 68)
    Sound(927, 2, 100, 0)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    OP_0D()
    SetMapObjFrame(0xFF, "futa00", 0x2, "move2")
    Sleep(1300)
    Fade(500)
    OP_68(50000, -4500, -50000, 0)
    MoveCamera(340, 21, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(50000, 0)
    OP_68(0, -4500, -10000, 9000)
    MoveCamera(0, 33, 0, 9000)
    SetCameraDistance(115000, 9000)
    OP_71(0x1, 0x12C, 0x0, 0x0, 0x0)
    OP_71(0x2, 0x12C, 0x0, 0x0, 0x0)
    OP_71(0x3, 0x12C, 0x0, 0x0, 0x0)
    OP_71(0x4, 0x12C, 0x0, 0x0, 0x0)
    Sleep(2000)
    Sound(579, 2, 30, 0)
    OP_79(0x1)
    OP_79(0x2)
    OP_79(0x3)
    OP_79(0x4)
    StopSound(927, 500, 100)
    StopSound(579, 500, 20)
    Sound(954, 0, 100, 0)
    Sound(143, 0, 30, 0)
    SetMapObjFrame(0xFF, "futa01", 0x2, "move2")
    OP_6F(0x79)
    Fade(500)
    SetMapObjFrame(0xFF, "futa02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x0, 0x1)
    Sleep(1500)
    Fade(500)
    OP_68(0, 2000, 5500, 0)
    MoveCamera(25, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    OP_68(0, 2000, 3500, 3500)
    MoveCamera(35, 11, 0, 3500)
    SetCameraDistance(17000, 3500)
    Sound(930, 0, 100, 0)
    Sound(950, 2, 40, 0)
    Sound(933, 2, 100, 0)
    PlayEffect(0x1, 0x1, 0xC, 0x5, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_CE1F():
        OP_96(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_CE1F)
    WaitChrThread(0xC, 1)

    def lambda_CE3D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_CE3D)
    WaitChrThread(0xC, 2)
    StopEffect(0x1, 0x2)
    StopSound(950, 1000, 30)
    StopSound(933, 1000, 100)
    Sound(935, 0, 100, 0)
    OP_6F(0x79)
    Sleep(800)

    #C0258
    ChrTalk(
        0xC,
        "#11310F#5Pば、馬鹿な……！\x02",
    )

    CloseMessageWindow()
    StopSound(132, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x3A5)
    OP_24(0x39F)
    OP_24(0x3B6)
    OP_24(0x243)
    OP_24(0x3AF)
    SetScenarioFlags(0x24, 1)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_67_C3DE end

    def Function_68_CEBE(): pass

    label("Function_68_CEBE")

    Sound(943, 2, 50, 0)
    Sleep(1500)
    OP_24(0x3AF)
    Sound(143, 0, 60, 0)
    Return()

    # Function_68_CEBE end

    def Function_69_CED1(): pass

    label("Function_69_CED1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CF05")
    Sound(203, 0, 50, 0)
    Sleep(900)
    Sound(203, 0, 60, 0)
    Sleep(1100)
    Sound(203, 0, 50, 0)
    Sleep(800)
    Sound(203, 0, 40, 0)
    Sleep(1000)
    Jump("Function_69_CED1")

    label("loc_CF05")

    Return()

    # Function_69_CED1 end

    def Function_70_CF06(): pass

    label("Function_70_CF06")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrChipPat(0x4, 0x1, 0x1F)
    SetChrChipPat(0x5, 0x1, 0x20)
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF44")
    AddParty(0x8, 0xFF, 0xFF)
    SetScenarioFlags(0x0, 0)

    label("loc_CF44")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF5C")
    AddParty(0x4, 0xFF, 0xFF)
    SetScenarioFlags(0x0, 1)

    label("loc_CF5C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF74")
    AddParty(0x5, 0xFF, 0xFF)
    SetScenarioFlags(0x0, 2)

    label("loc_CF74")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF8C")
    AddParty(0x9, 0xFF, 0xFF)
    SetScenarioFlags(0x0, 3)

    label("loc_CF8C")

    LoadChrToIndex("chr/ch05620.itc", 0x1E)
    LoadChrToIndex("chr/ch13400.itc", 0x1F)
    LoadChrToIndex("chr/ch02500.itc", 0x20)
    LoadChrToIndex("apl/ch51732.itc", 0x21)
    LoadChrToIndex("apl/ch51113.itc", 0x22)
    LoadChrToIndex("apl/ch51734.itc", 0x23)
    LoadEffect(0x0, "event/ev10000.eff")
    LoadEffect(0x1, "event/ev10001.eff")
    LoadEffect(0x2, "event/ev17054.eff")
    SoundLoad(3787)
    SoundLoad(112)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04700.itp")
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, 0, 0)
    OP_8E(0xC, "ディーター大統領")
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 10000, 0, 1500, 270)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x101, -800, 0, -5500, 0)
    SetChrPos(0x102, 800, 0, -5500, 0)
    SetChrPos(0x103, -1700, 0, -7000, 0)
    SetChrPos(0x104, 1700, 0, -7000, 0)
    SetChrPos(0xF4, 100, 0, -6700, 0)
    SetChrPos(0xF5, -100, 0, -7800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    SetChrPos(0x28, 0, 0, 6500, 180)
    OP_D5(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFlags(0x14, 0x4)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x58C)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    OP_78(0x14, 0x29)
    SetChrPos(0x29, 0, 0, 6500, 180)
    OP_D5(0x29, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x14, 0x1000)
    ClearMapObjFlags(0x14, 0x4)
    OP_74(0x14, 0x1E)
    OP_70(0x14, 0x58C)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "close")
    OP_70(0x1, 0x0)
    OP_70(0x2, 0x0)
    OP_70(0x3, 0x0)
    OP_70(0x4, 0x0)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    OP_78(0xD, 0x2C)
    OP_78(0xE, 0x2D)
    OP_78(0xF, 0x2E)
    OP_78(0x10, 0x2F)
    OP_78(0x11, 0x30)
    OP_78(0x12, 0x31)
    OP_49()
    SetChrPos(0x2C, 15000, 6000, -3000, 0)
    SetChrPos(0x2D, 15100, 7000, -7500, 0)
    SetChrPos(0x2E, 15100, 7000, 1500, 0)
    SetChrPos(0x2F, 15200, 5000, 5000, 0)
    SetChrPos(0x30, 15200, 5000, -11000, 0)
    SetChrPos(0x31, 15000, 6000, -3000, 0)
    OP_D5(0x2C, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x2D, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x2E, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x2F, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x30, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x31, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFlags(0xE, 0x1000)
    SetMapObjFlags(0xF, 0x1000)
    SetMapObjFlags(0x10, 0x1000)
    SetMapObjFlags(0x11, 0x1000)
    SetMapObjFlags(0x12, 0x1000)
    OP_FF(0xD, 0x168, 0x168, 0x168)
    OP_FF(0xE, 0x140, 0x140, 0x140)
    OP_FF(0xF, 0x140, 0x140, 0x140)
    OP_FF(0x10, 0x140, 0x140, 0x140)
    OP_FF(0x11, 0x140, 0x140, 0x140)
    OP_FF(0x12, 0x17C, 0x17C, 0x17C)
    ClearChrFlags(0x2B, 0x80)
    OP_78(0x15, 0x2B)
    OP_49()
    SetChrPos(0x2B, 0, 15000, 6000, 180)
    OP_D5(0x2B, 0x1388, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x15, 0x1000)
    OP_74(0x15, 0x1E)
    OP_71(0x15, 0x1, 0x78, 0x0, 0x20)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x17, 0x18)
    OP_49()
    SetChrPos(0x18, 0, 15000, 6000, 180)
    OP_D5(0x18, 0x1388, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x1000)
    OP_68(210, 2500, 5500, 0)
    MoveCamera(35, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18050, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(210, 1500, 5500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0259
    ChrTalk(
        0xC,
        (
            "#12P#11307Fど、どういう事だ！？\x02\x03",

            "どうして《至宝》からの供給が\x01",
            "いきなり止まるのだ……！？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(240, 40, -1, -1)
    SetChrName("不気味な声")

    #A0260
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "まぁ、余計な事をしている暇が\x01",
            "無くなったからだろうねぇ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7580", 0)
    SetChrFlags(0x102, 0x8)
    OP_68(10000, 1000, 1500, 2000)
    SetCameraDistance(14000, 2000)
    TurnDirection(0xC, 0x13, 500)
    TurnDirection(0x101, 0x13, 0)
    TurnDirection(0x102, 0x13, 0)
    TurnDirection(0x103, 0x13, 0)
    TurnDirection(0x104, 0x13, 0)
    TurnDirection(0xF4, 0x13, 0)
    TurnDirection(0xF5, 0x13, 0)
    OP_6F(0x79)
    ClearChrFlags(0x102, 0x8)
    SetCameraDistance(13000, 2000)
    Sound(223, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 10000, 0, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(936, 0, 100, 0)
    ClearChrFlags(0x13, 0x80)

    def lambda_D70C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_D70C)
    WaitChrThread(0x13, 2)
    Sleep(1000)

    #C0261
    ChrTalk(
        0x101,
        "#00013F《結社》の……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D77B")

    #C0262
    ChrTalk(
        0x105,
        (
            "#10407F《十三工房》\x01",
            "Ｆ・ノバルティス……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D79E")

    label("loc_D77B")


    #C0263
    ChrTalk(
        0x103,
        "#00207Fノバルティス博士……！\x02",
    )

    CloseMessageWindow()

    label("loc_D79E")

    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(5960, 1000, 1210, 0)
    MoveCamera(55, 11, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    Sleep(150)

    #C0264
    ChrTalk(
        0xC,
        (
            "#6P#11310Fノバルティス博士……\x01",
            "一体、どういうことだ！？\x02\x03",

            "まさか《結社》が機体に\x01",
            "何かを仕掛けていたのか！？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0265
    AnonymousTalk(
        0x13,
        (
            "フフ、前にも言ったように\x01",
            "あくまで今回は手伝いでね。\x02\x03",

            "良いデータも取れたことだし、\x01",
            "そろそろ私も失礼させてもらうよ。\x02\x03",

            "契約通り、そちらの最終型と共にね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    Sleep(200)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0266
    ChrTalk(
        0xC,
        (
            "#6P#11307F契約だと……！？\x02\x03",

            "馬鹿な、この機体はこちらが\x01",
            "《結社》から買い上げたものだ！\x02\x03",

            "持って行かれる道理などない！\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x13,
        (
            "#11P#04704Fいやいや、実は契約内容に\x01",
            "ちょっとした変更があってね。\x02\x03",

            "用済みになった機体を\x01",
            "こちらに回収させてもらうよう、\x01",
            "取り計らってくれたのだよ。\x02\x03",

            "#04702F──閣下のご令嬢、\x01",
            "マリアベル・クロイス嬢がね。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xC,
        "#6P#11305Fな……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(260, 10, -1, -1)
    SetChrName("娘の声")

    #A0269
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3787V#30W#37Aウフフ……その通りですわ。\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0270
    ChrTalk(
        0x101,
        "#5P#00011F#6P#Nこ、この声は……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0271
    ChrTalk(
        0x102,
        "#00107Fベル#6P#N……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7572", 0)
    Fade(500)
    OP_68(15000, 5500, -3000, 0)
    MoveCamera(62, 0, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14000, 0)
    OP_93(0xC, 0x5A, 0x0)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x102, 0x5A, 0x0)
    OP_93(0x103, 0x5A, 0x0)
    OP_93(0x104, 0x5A, 0x0)
    OP_93(0xF4, 0x5A, 0x0)
    OP_93(0xF5, 0x5A, 0x0)
    SetCameraDistance(16000, 3000)
    Sleep(500)
    Sound(922, 0, 100, 0)
    BeginChrThread(0x2C, 3, 0, 79)
    OP_6F(0x79)
    Sleep(500)

    #C0272
    ChrTalk(
        0xC,
        (
            "#11310F#6P#Nベル……これは一体……？\x02\x03",

            "#11307Fそれに一体、どこにいるんだ！？\x02\x03",

            "オルキスタワーではないのか！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 160, -1, -1)

    #A0273
    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フフ、わたくしはとっくに\x01",
            "そちらを後にしていますわ。\x02\x03",

            "キーアさんたちと一緒に。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0274
    ChrTalk(
        0x101,
        "#00005F#6P#Nな……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0275
    ChrTalk(
        0x102,
        (
            "#00101F#6P#Nた、確かにどのフロアにも\x01",
            "居なかったみたいだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(57, -5, 0, 3000)
    SetCameraDistance(19500, 3000)
    Sound(922, 0, 100, 0)
    BeginChrThread(0x2D, 3, 0, 80)
    Sleep(500)
    Sound(922, 0, 100, 0)
    BeginChrThread(0x2E, 3, 0, 81)
    Sleep(500)
    Sound(922, 0, 100, 0)
    BeginChrThread(0x2F, 3, 0, 82)
    Sleep(500)
    Sound(922, 0, 100, 0)
    BeginChrThread(0x30, 3, 0, 83)
    OP_6F(0x79)
    Sleep(300)

    #C0276
    ChrTalk(
        0x101,
        "#00007F#6P#Nアリオスさん……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE9D")

    #C0277
    ChrTalk(
        0x10A,
        "#00610F#6P#Nマクレイン……！\x02",
    )

    CloseMessageWindow()

    label("loc_DE9D")


    #C0278
    ChrTalk(
        0x104,
        (
            "#00307F#6P#N叔父貴……！\x01",
            "シャーリィ……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF0A")

    #C0279
    ChrTalk(
        0x106,
        "#10701F#6P#N《血染めのシャーリィ》……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_DF0A")


    #C0280
    ChrTalk(
        0x103,
        "#00201F#6P#Nヴァルドさんまで……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF6E")

    #C0281
    ChrTalk(
        0x105,
        "#10401F#6P#Nやはり彼らと一緒だったか……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_DF6E")

    Sleep(150)
    SetMessageWindowPos(240, 110, -1, -1)
    SetChrName("アリオス")

    #A0282
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(120, 120, -1, -1)

    #A0283
    AnonymousTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クク……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(30, 160, -1, -1)

    #A0284
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "うーん！\x01",
            "盛り上がってきたねぇ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(370, 160, -1, -1)

    #A0285
    AnonymousTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ケッ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0286
    ChrTalk(
        0xC,
        (
            "#11310F#6P#Nど、どういう事だ……\x02\x03",

            "#11307F君たちは……\x01",
            "私を裏切ったというのか！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 110, -1, -1)
    SetChrName("アリオス")

    #A0287
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……大統領、申し訳ありません。\x02\x03",

            "しかし私は元々、貴方の計画に\x01",
            "協力していたわけではありません。\x02\x03",

            "“先生”とマリアベル嬢の計画に\x01",
            "協力していただけです。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0288
    ChrTalk(
        0xC,
        (
            "#11305F#30W#6P#N“先生”……\x02\x03",

            "#11310Fま……まさか……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("男性の声")

    #A0289
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ──その通りだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(250)
    OP_68(15000, 5500, -3000, 0)
    MoveCamera(90, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14500, 0)
    OP_FF(0xD, 0x140, 0x140, 0x140)
    SetChrPos(0x2C, 15100, 5000, -7000, 0)
    SetChrPos(0x2D, 15200, 7500, -10000, 0)
    SetChrPos(0x30, 15300, 4000, -12000, 0)
    SetChrPos(0x2E, 15100, 7500, 2000, 0)
    SetChrPos(0x2F, 15200, 4000, 4000, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_0D()
    Sound(922, 0, 100, 0)
    BeginChrThread(0x31, 3, 0, 84)
    Sleep(500)
    CancelBlur(1000)
    SetCameraDistance(17500, 1000)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2B4")
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0290
    ChrTalk(
        0x101,
        "#00007F#4S#12P#N……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E2B4")


    #C0291
    ChrTalk(
        0x102,
        "#00105F#12P#N………ぁ…………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0292
    ChrTalk(
        0x103,
        "#00205F#12P#N……え…………？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0293
    ChrTalk(
        0x104,
        "#00305F#12P#N……う、嘘だろ………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E360")

    #C0294
    ChrTalk(
        0x10A,
        "#00605F#12P#Nイ、イアン先生……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E38E")

    #C0295
    ChrTalk(
        0x109,
        "#10111F#12P#Nそ、そんな……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E38E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3C8")

    #C0296
    ChrTalk(
        0x105,
        "#10410F#12P#Nまさか……そう来るとはね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_END)), "loc_E5BD")

    #C0297
    ChrTalk(
        0x101,
        "#00013F#12P#N…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("イアン弁護士")

    #A0298
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ふむ、その様子では\x01",
            "ロイド君は私の関与に\x01",
            "気付いていたのかな……？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0299
    ChrTalk(
        0x101,
        (
            "#00006F#12P#N……ええ。\x01",
            "ニールセンという記者の方が\x01",
            "ヒントをくれましたから。\x02\x03",

            "#00008Fそれとピート君や墓守のご老人……\x01",
            "キリカさんやレクターさんの指摘……\x02\x03",

            "#00013F全ての断片#4Rフラグメント#が最終的に\x01",
            "貴方の関与を指し示していました。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("イアン弁護士")

    #A0300
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ふふ、どうやら完全に\x01",
            "ガイ君に追いついたようだね。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_E5BD")

    Fade(500)
    OP_68(8000, 3000, -3000, 0)
    MoveCamera(50, 3, 0, 0)
    SetCameraDistance(23000, 0)
    OP_0D()
    Sleep(300)

    #C0301
    ChrTalk(
        0xC,
        (
            "#6P#11310F#Nグリムウッド先生……\x01",
            "これはどういう事ですか……！？\x02\x03",

            "た、確かに先生には色々と\x01",
            "相談に乗ってもらいはしたが……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(190, 100, -1, -1)
    SetChrName("イアン弁護士")

    #A0302
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ……君は本当に\x01",
            "教え甲斐のある生徒だったよ。\x02\x03",

            "経営者としては超一流だし、\x01",
            "政治家としても悪くはなかった。\x02\x03",

            "夢想家すぎる#12R㈲　㈲　㈲　㈲　㈲　㈲#という、\x01",
            "致命的な欠点を除けばね。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(50)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0303
    ChrTalk(
        0xC,
        "#6P#11305F#N……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(270, 110, -1, -1)

    #A0304
    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フフ、お父様はご自分の考えで\x01",
            "全てが上手く運んだと\x01",
            "思ってらっしゃるようですが……\x02\x03",

            "その実、先生の用意した筋書#4Rシナリオ#に\x01",
            "誘導されていただけですわ。\x02\x03",

            "教団の扱い、通商会議の段取り、\x01",
            "クロスベル市襲撃から独立宣言まで……\x02\x03",

            "そのアイデアの元を、最初にお父様に\x01",
            "囁いたのはどなたでしたかしら？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0305
    ChrTalk(
        0xC,
        "#6P#11310F#30W#N………ぁ……………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(190, 100, -1, -1)
    SetChrName("イアン弁護士")

    #A0306
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "このまま君が上手くやれば\x01",
            "表に出るつもりは無かったが……\x02\x03",

            "どうやら黒幕#4Rフィクサー#としてのみ、\x01",
            "留まってはいられないようだ。\x02\x03",

            "『碧き零の計画』、\x01",
            "このまま遂行させてもらうよ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0307
    ChrTalk(
        0xC,
        "#6P#11310F#N碧#2Rあお#き……零#2Rゼロ#……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0308
    ChrTalk(
        0x101,
        "#00007F#6P#Nな、なんだそれは！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(270, 110, -1, -1)

    #A0309
    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フフ、《零の至宝》の完成形……\x02\x03",

            "時空を支配し、因果律を組み替える\x01",
            "《碧の大樹》……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(270, 110, -1, -1)

    #A0310
    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4Sその新たなる誕生ですわ……！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(929, 0, 40, 0)
    Sound(934, 0, 40, 0)
    Sound(112, 2, 100, 0)
    PlayEffect(0x2, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0x1388)
    OP_68(8000, 3000, -6000, 1000)
    SetCameraDistance(24000, 1000)

    def lambda_EBF7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_EBF7)

    def lambda_EC04():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_EC04)

    def lambda_EC11():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_EC11)
    Sleep(50)

    def lambda_EC21():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_EC21)
    Sleep(50)

    def lambda_EC31():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_EC31)
    Sleep(50)

    def lambda_EC41():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_EC41)
    Sleep(50)

    def lambda_EC51():
        OP_93(0xF4, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_EC51)
    Sleep(50)

    def lambda_EC61():
        OP_93(0xF5, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_EC61)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    #C0311
    ChrTalk(
        0x104,
        "#00305F#5Pこの光は……！？\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x102,
        "#00105F#5P碧い光……！？\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x103,
        (
            "#00207F#5P……南南西！\x01",
            "湿地帯のあたりです！\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x101,
        "#00010F#5Pあれは──\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7555", 0)
    OP_68(8000, 3000, -7000, 2000)
    SetCameraDistance(24500, 2000)
    StopSound(132, 1000, 40)
    StopSound(112, 1000, 90)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_07a.pmf", 0x22B, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    ClearMapObjFlags(0x16, 0x4)
    StopEffect(0x0, 0x0)
    OP_68(0, 2000, -20000, 0)
    MoveCamera(150, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18500, 0)
    Sound(132, 2, 50, 0)
    Sound(112, 2, 80, 0)
    OP_68(0, 2000, -13000, 4000)
    MoveCamera(145, 9, 0, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0x7D0)

    #C0315
    ChrTalk(
        0x101,
        "#5P#00010F#6P#N…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE5D")

    #C0316
    ChrTalk(
        0x109,
        "#5P#10111F#6P#Nなああああっ……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_EE5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE8D")

    #C0317
    ChrTalk(
        0x105,
        "#5P#10410F#6P#Nこ、これは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_EE8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EEBD")

    #C0318
    ChrTalk(
        0x10A,
        "#5P#00610F#6P#N……馬鹿な……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_EEBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EEED")

    #C0319
    ChrTalk(
        0x106,
        "#5P#10701F#6P#N……大樹……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_EEED")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7571", 0)
    Sleep(500)

    #N0320
    NpcTalk(
        0x104,
        "ノバルティス博士",
        (
            "#04702F#5P#Nクク──素晴らしい！\x02\x03",

            "まさに特異点の産物……\x01",
            "かの《塩の杭》を遥かに超える\x01",
            "“予定外の奇蹟”と言うべきか！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0321
    ChrTalk(
        0xC,
        "#11305F#6P#N…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(112, 2000, 70)
    Fade(500)
    OP_68(8000, 3000, -3000, 0)
    MoveCamera(50, 3, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(23000, 0)
    OP_0D()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0322
    ChrTalk(
        0x101,
        (
            "#00007F#4S#6P#Nま、待ってくれ！\x02\x03",

            "#00010F#3Sあの巨大な樹が\x01",
            "《零の至宝》の完成形って……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_F06E():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F06E)
    Sleep(30)

    def lambda_F07E():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F07E)
    Sleep(30)

    def lambda_F08E():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F08E)
    Sleep(30)

    def lambda_F09E():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_F09E)
    Sleep(30)

    def lambda_F0AE():
        OP_93(0xF5, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_F0AE)
    Sleep(30)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    #C0323
    ChrTalk(
        0x102,
        (
            "#00107F#6P#Nキーアちゃんは……\x01",
            "……あの子は一体どこに！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(270, 110, -1, -1)

    #A0324
    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フフ、何を言っているのかしら。\x02\x03",

            "キーアさんならほら、\x01",
            "そこからも見えているでしょう？\x02\x03",

            "あの《碧の大樹》こそ\x01",
            "キーアさんそのもの#8R㈲　㈲　㈲　㈲#ですわ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sleep(300)
    SetMessageWindowPos(300, 70, -1, -1)
    SetChrName("アリオス")

    #A0325
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……彼女の心と身体が\x01",
            "失われたというわけではない。\x02\x03",

            "そのあたりは安心するがいい。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(190, 100, -1, -1)
    SetChrName("イアン弁護士")

    #A0326
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "だが、これより彼女は\x01",
            "全ての“調停者”となる──\x02\x03",

            "彼女にとっても、君たちにとっても\x01",
            "悪い結果にはならないはずだ。\x02\x03",

            "できれば見守ってあげて欲しい。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0327
    ChrTalk(
        0x103,
        "#00206F#6P#Nい、いったい何を……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0328
    ChrTalk(
        0x104,
        "#00310F#6P#Nワケ判らなさすぎだぜ……\x02",
    )

    CloseMessageWindow()
    OP_68(15000, 5000, -5000, 1600)
    MoveCamera(69, -5, 0, 1600)
    SetCameraDistance(19500, 1600)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4AF")
    SetMessageWindowPos(0, 170, -1, -1)

    #A0329
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ホントそうだよねー。\x02\x03",

            "でも楽しければ\x01",
            "それでいいんじゃない？\x02\x03",

            "ね、リーシャ㈱\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0330
    ChrTalk(
        0x106,
        "#10701F#6P#N…………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_F509")

    label("loc_F4AF")

    SetMessageWindowPos(0, 170, -1, -1)

    #A0331
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ホントそうだよねー。\x02\x03",

            "でも楽しければ\x01",
            "それでいいんじゃない？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_F509")

    SetMessageWindowPos(10, 110, -1, -1)

    #A0332
    AnonymousTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クク、まあ邪魔するつもりなら\x01",
            "遠慮なく相手をしてやろう。\x02\x03",

            "これも契約の内だからな。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F638")
    SetMessageWindowPos(370, 160, -1, -1)

    #A0333
    AnonymousTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……こいつらの企みは\x01",
            "知ったこっちゃないが……\x02\x03",

            "来るんなら今度こそ\x01",
            "徹底的に潰してやるぜ……\x02\x03",

            "なあ、ワジぃ……？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0334
    ChrTalk(
        0x105,
        "#10401F#6P#N……ヴァルド。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_F6B3")

    label("loc_F638")

    SetMessageWindowPos(370, 160, -1, -1)

    #A0335
    AnonymousTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……こいつらの企みは\x01",
            "知ったこっちゃないが……\x02\x03",

            "来るんなら今度こそ\x01",
            "徹底的に潰してやるぜ……？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_F6B3")

    SetMessageWindowPos(160, 150, -1, -1)

    #A0336
    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ウフフ……\x01",
            "それでは皆さん、御機嫌よう。\x02\x03",

            "──それとお父様。\x01",
            "今までお世話になりましたわ。\x02\x03",

            "単純で、ロマンチストで\x01",
            "愚かしくはありましたけれど……\x02\x03",

            "わたくし、お父様のことが\x01",
            "決して嫌いではありませんでした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(977, 0, 100, 0)
    BeginChrThread(0x31, 3, 0, 90)
    Sleep(200)
    BeginChrThread(0x2C, 3, 0, 85)
    Sleep(200)
    BeginChrThread(0x2D, 3, 0, 86)
    Sleep(200)
    Sound(977, 0, 50, 0)
    BeginChrThread(0x2E, 3, 0, 87)
    Sleep(200)
    BeginChrThread(0x2F, 3, 0, 88)
    Sleep(200)
    BeginChrThread(0x30, 3, 0, 89)
    WaitChrThread(0x30, 3)
    Fade(500)
    OP_68(5000, 1500, -1000, 0)
    MoveCamera(35, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(19000, 0)
    OP_93(0xC, 0x5A, 0x0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(2000, 1500, -1000, 3000)
    OP_0D()
    OP_6F(0x79)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)

    #C0337
    ChrTalk(
        0xC,
        "#5P#11311F#40W…………ベル……………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x0)
    Sleep(1000)

    def lambda_F8F3():
        OP_A6(0xFE, 0x0, 0x1E, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_F8F3)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xC, 0x1)
    Sleep(130)
    SetChrSubChip(0xC, 0x2)
    Sleep(130)
    SetChrSubChip(0xC, 0x3)
    Sleep(500)
    TurnDirection(0x13, 0xC, 500)

    #C0338
    ChrTalk(
        0x13,
        (
            "#04704Fフフ、役目が無ければ\x01",
            "私も最後まで付き合うんだが……\x02\x03",

            "#04700Fまあ、せいぜい遠くの地で\x01",
            "続報を聞かせてもらうとしよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    Sound(901, 0, 100, 0)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    Sleep(500)
    Fade(1000)
    SetMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    OP_0D()
    OP_68(0, 2000, -1000, 2000)
    MoveCamera(31, 5, 0, 2000)
    SetCameraDistance(18000, 2000)
    Sound(980, 2, 30, 0)
    BeginChrThread(0x28, 3, 0, 77)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_FAAC():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FAAC)
    Sleep(50)

    def lambda_FABC():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FABC)
    Sleep(50)

    def lambda_FACC():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_FACC)
    Sleep(50)

    def lambda_FADC():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FADC)
    Sleep(50)

    def lambda_FAEC():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_FAEC)
    Sleep(50)

    def lambda_FAFC():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_FAFC)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    #C0339
    ChrTalk(
        0x101,
        "#00007F#12P#N……あ………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x28, 3)
    BeginChrThread(0x28, 3, 0, 78)
    Sound(223, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 10000, 0, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(936, 0, 100, 0)

    def lambda_FB92():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_FB92)
    WaitChrThread(0x13, 2)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    OP_D3(0x13, 0x5, "Null_hand_l(63)")
    OP_93(0x13, 0x0, 0x0)
    ClearChrFlags(0x13, 0x1)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(310, 4200, 5930, 2000)
    MoveCamera(31, 7, 0, 2000)
    SetCameraDistance(15000, 2000)
    Sleep(500)
    Sound(223, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 1900, 3900, 4750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_FC42():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_FC42)
    WaitChrThread(0x13, 2)
    Sound(936, 0, 100, 0)
    Sleep(1200)

    #C0340
    ChrTalk(
        0x13,
        (
            "#5P#04709Fハハ、それでは失礼するよ。\x02\x03",

            "#04704F無駄だとは思うが\x01",
            "せいぜい足掻いてみたまえ。\x02\x03",

            "#04702F有意義なデータを\x01",
            "残してもらう意味でもねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(955, 0, 100, 0)
    Sleep(1000)
    OP_68(0, 4900, 6000, 700)
    Sound(905, 0, 100, 0)
    OP_71(0x5, 0x51E, 0x532, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x532, 0x55A, 0x0, 0x20)
    OP_6F(0x79)
    MoveCamera(25, 15, 0, 3000)
    SetCameraDistance(22000, 3000)
    Sound(223, 0, 100, 0)
    Sound(919, 0, 70, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 0, 0, 6500, 0, 0, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(936, 0, 100, 0)
    StopSound(980, 1000, 30)
    OP_75(0x5, 0x1, 0x1F4)

    def lambda_FD9F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_FD9F)

    def lambda_FDB0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_FDB0)
    WaitChrThread(0x13, 2)
    SetChrFlags(0x13, 0x80)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 2000, -1000, 0)
    MoveCamera(31, 5, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18500, 0)
    OP_0D()

    #C0341
    ChrTalk(
        0x103,
        "#00201F#30W#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x104,
        (
            "#00310F#30W#11P引っ掻き回すだけ引っ掻き回して\x01",
            "トンズラかよ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x6, 0, 0, -21000, 0)
    SetChrPos(0x7, 0, 0, -22000, 0)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    StopBGM(0x1770)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_FEDF")

    #N0343
    NpcTalk(
        0x105,
        "ワジの声",
        "みんな、無事かい……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF40")

    label("loc_FEDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FF16")

    #N0344
    NpcTalk(
        0x109,
        "ノエルの声",
        "皆さん……無事ですか！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF40")

    label("loc_FF16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_FF40")

    #N0345
    NpcTalk(
        0x10A,
        "ダドリーの声",
        "無事か……！？\x02",
    )

    CloseMessageWindow()

    label("loc_FF40")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(0, 1200, -10000, 2250)
    MoveCamera(55, 13, 0, 2250)
    OP_6E(600, 2250)
    SetCameraDistance(15000, 2250)

    def lambda_FFE8():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FFE8)
    Sleep(50)

    def lambda_FFF8():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FFF8)
    Sleep(50)

    def lambda_10008():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10008)
    Sleep(50)

    def lambda_10018():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10018)
    Sleep(50)

    def lambda_10028():
        OP_93(0xF4, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_10028)
    Sleep(50)

    def lambda_10038():
        OP_93(0xF5, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_10038)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    def lambda_1005D():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFCF2C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x6, 1, lambda_1005D)
    Sleep(200)

    def lambda_1007A():
        OP_96(0xFE, 0x320, 0x0, 0xFFFFCF2C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x7, 1, lambda_1007A)
    WaitChrThread(0x6, 1)
    WaitChrThread(0x7, 1)
    OP_6F(0x79)

    #C0346
    ChrTalk(
        0x101,
        "#00008F２人とも……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_10111")

    #C0347
    ChrTalk(
        0x106,
        (
            "#10708F#12P今のは一体……\x02\x03",

            "#10707Fそれにあの巨大な\x01",
            "樹のようなものは……！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101D8")

    label("loc_10111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_10176")

    #C0348
    ChrTalk(
        0x10A,
        (
            "#00610F#12P今のは一体……\x02\x03",

            "#00607Fそれにあの巨大な樹の\x01",
            "ようなものはなんだ……！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101D8")

    label("loc_10176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_101D8")

    #C0349
    ChrTalk(
        0x109,
        (
            "#10108F#12Pい、今のは一体……\x02\x03",

            "#10107Fそ、それにあの巨大な\x01",
            "樹のようなものは……！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_101D8")


    #C0350
    ChrTalk(
        0x102,
        "#5P#00106Fそ、それが……\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x103,
        "#5P#00206F何と言ったらいいか……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x4)
    SetChrPos(0x15, -8500, -2000, -20000, 90)

    #N0352
    NpcTalk(
        0x15,
        "セルゲイの声",
        (
            "……どうやらまだ\x01",
            "終わりじゃないみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7567", 0)
    Fade(500)
    OP_68(0, 1000, -21800, 0)
    MoveCamera(145, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x6, -1200, 0, -12500, 0)
    SetChrPos(0x7, 1200, 0, -12500, 0)

    def lambda_10370():
        OP_95(0xFE, -2200, 0, -21800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_10370)
    Sleep(500)
    Sound(112, 2, 50, 0)
    WaitChrThread(0x15, 1)

    def lambda_10397():
        OP_95(0xFE, 0, 0, -21800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_10397)
    WaitChrThread(0x15, 1)
    OP_68(0, 1000, -10000, 4000)
    MoveCamera(145, 15, 0, 4000)

    def lambda_103D1():
        OP_95(0xFE, 0, 0, -11500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_103D1)
    WaitChrThread(0x15, 1)
    OP_6F(0x79)

    #C0353
    ChrTalk(
        0x101,
        "#6P#00005F課長……！\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x104,
        "#00301F#6P下の方は大丈夫なんスか？\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x15,
        (
            "#11P#01003Fああ、魔導兵どもが消えたんで\x01",
            "無事タワーに乗り込めた。\x02\x03",

            "#01001Fしかし……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0xB4, 0x1F4)
    Sleep(900)
    OP_68(-450, 1500, -5360, 1500)
    SetCameraDistance(18700, 1500)
    OP_93(0x15, 0x0, 0x1F4)
    OP_6F(0x79)
    Sleep(500)

    #C0356
    ChrTalk(
        0xC,
        "#11311F#40W#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x15,
        (
            "#11P#01006F……いったい、\x01",
            "何がどうなってやがる？\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x102,
        "#00108F#6Pはい……\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        "#6P#00006F#6P……それが……\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18200, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    SetChrPos(0x101, -450, 0, -9600, 180)
    SetChrPos(0x102, 450, 0, -9100, 180)
    SetChrPos(0x103, -1500, 0, -9600, 135)
    SetChrPos(0x104, 1500, 0, -9600, 225)
    SetChrPos(0xF4, -1050, 0, -8000, 180)
    SetChrPos(0xF5, 1050, 0, -8000, 180)
    SetChrPos(0x6, -1750, 0, -11400, 45)
    SetChrPos(0x7, 1750, 0, -11400, 315)
    SetChrPos(0x15, 0, 0, -12900, 0)
    OP_68(-120, 1100, -11660, 0)
    MoveCamera(143, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    SetChrName("")

    #A0360
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちは課長に一通りの経緯を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(14500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_106EA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_106C3")

    #C0361
    ChrTalk(
        0x106,
        "#11P#10712Fそ、そんな事が……\x02",
    )

    Jump("loc_106E4")

    label("loc_106C3")


    #C0362
    ChrTalk(
        0x106,
        "#5P#10712Fそ、そんな事が……\x02",
    )


    label("loc_106E4")

    CloseMessageWindow()
    Jump("loc_107C7")

    label("loc_106EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10757")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1072E")

    #C0363
    ChrTalk(
        0x109,
        "#11P#10106Fそ、そんな事って……\x02",
    )

    Jump("loc_10751")

    label("loc_1072E")


    #C0364
    ChrTalk(
        0x106,
        "#5P#10706Fそ、そんな事って……\x02",
    )


    label("loc_10751")

    CloseMessageWindow()
    Jump("loc_107C7")

    label("loc_10757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_107C7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1079F")

    #C0365
    ChrTalk(
        0x105,
        "#11P#10406Fさすがにビックリだね……\x02",
    )

    Jump("loc_107C6")

    label("loc_1079F")


    #C0366
    ChrTalk(
        0x105,
        "#5P#10406Fさすがにビックリだね……\x02",
    )


    label("loc_107C6")

    CloseMessageWindow()

    label("loc_107C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_10862")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10822")

    #C0367
    ChrTalk(
        0x10A,
        (
            "#11P#00608Fまさかイアン先生が\x01",
            "黒幕の１人だったとは……\x02",
        )
    )

    Jump("loc_1085C")

    label("loc_10822")


    #C0368
    ChrTalk(
        0x10A,
        (
            "#5P#00608Fまさかイアン先生が\x01",
            "黒幕の１人だったとは……\x02",
        )
    )


    label("loc_1085C")

    CloseMessageWindow()
    Jump("loc_1098B")

    label("loc_10862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_108F5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_108B9")

    #C0369
    ChrTalk(
        0x105,
        (
            "#11P#10403Fあの熊ヒゲ先生が\x01",
            "黒幕の１人とはねぇ……\x02",
        )
    )

    Jump("loc_108EF")

    label("loc_108B9")


    #C0370
    ChrTalk(
        0x105,
        (
            "#5P#10403Fあの熊ヒゲ先生が\x01",
            "黒幕の１人とはねぇ……\x02",
        )
    )


    label("loc_108EF")

    CloseMessageWindow()
    Jump("loc_1098B")

    label("loc_108F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1098B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10950")

    #C0371
    ChrTalk(
        0x109,
        (
            "#11P#10108Fあのイアン先生が\x01",
            "黒幕の１人だったなんて……\x02",
        )
    )

    Jump("loc_1098A")

    label("loc_10950")


    #C0372
    ChrTalk(
        0x109,
        (
            "#5P#10108Fあのイアン先生が\x01",
            "黒幕の１人だったなんて……\x02",
        )
    )


    label("loc_1098A")

    CloseMessageWindow()

    label("loc_1098B")


    #C0373
    ChrTalk(
        0x15,
        (
            "#11P#01006F……なるほどな。\x02\x03",

            "#01001F政財界に国際情勢、警察にギルド、\x01",
            "様々な裏事情にも通じている人物か。\x02\x03",

            "#01003Fあの先生がその気になれば\x01",
            "確かに全てを段取れただろう。\x02\x03",

            "#01000F問題は動機だが……\x01",
            "今はそれどころじゃなさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x101,
        "#00006F#6Pはい……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(200)
    SetChrName("")
    BeginChrThread(0x101, 0, 0, 74)
    WaitChrThread(0x101, 0)

    #C0375
    ChrTalk(
        0x101,
        (
            "#13P#00001F──ワジ。\x01",
            "メルカバを呼んでもらえるか？\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x105, 0, 0, 73)
    WaitChrThread(0x105, 0)

    #C0376
    ChrTalk(
        0x105,
        "#13P#10402Fフフ、そう言うと思ったよ。\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_93(0x105, 0x10E, 0x1F4)
    Sleep(300)
    Fade(250)
    Sound(802, 0, 80, 0)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x4)
    SetChrFlags(0x105, 0x10)
    SetChrFlags(0x105, 0x2)
    SetChrFlags(0x105, 0x20)
    Sleep(500)
    SetChrSubChip(0x105, 0x5)
    Sound(804, 0, 100, 0)
    Sleep(500)

    #C0377
    ChrTalk(
        0x15,
        "#11P#01000F……行くのか？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B88")

    def lambda_10B80():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x6, 2, lambda_10B80)

    label("loc_10B88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10BA7")

    def lambda_10B9F():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x7, 2, lambda_10B9F)

    label("loc_10BA7")

    OP_93(0x101, 0xB4, 0x1F4)

    #C0378
    ChrTalk(
        0x101,
        (
            "#00003F#6Pええ、もはや警察の仕事とは\x01",
            "言えないかもしれません……\x02\x03",

            "#00013Fですが、キーアと全ての真実が\x01",
            "あそこで待っている以上、\x01",
            "俺には放っておけません。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x102,
        (
            "#00101F#6P……私もです。\x01",
            "ベルを止めないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x103,
        (
            "#00204F#6Pまあ、ここまで来たら\x01",
            "一蓮托生は当然かと。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x104,
        (
            "#00302F#6P叔父貴たちも手ぐすねひいて\x01",
            "待ってるみてぇだしな。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x109, 0, 0, 72)
    WaitChrThread(0x109, 0)

    #C0382
    ChrTalk(
        0x109,
        (
            "#6P#10107Fあたしも……\x01",
            "付き合わせてもらいます！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrSubChip(0x105, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(300)
    Fade(250)
    Sound(802, 0, 80, 0)
    SetChrChipByIndex(0x105, 0xFF)
    ClearChrFlags(0x105, 0x10)
    ClearChrFlags(0x105, 0x2)
    ClearChrFlags(0x105, 0x20)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Sleep(150)
    TurnDirection(0x105, 0x15, 500)
    BeginChrThread(0x105, 0, 0, 73)
    WaitChrThread(0x105, 0)

    #C0383
    ChrTalk(
        0x105,
        (
            "#6P#10404Fま、メルカバを提供するんだし、\x01",
            "僕も付き合わせてもらうよ。\x02\x03",

            "#10400Fヴァルドとの決着も\x01",
            "付ける必要がありそうだしね。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x106, 0, 0, 75)
    WaitChrThread(0x106, 0)

    #C0384
    ChrTalk(
        0x106,
        (
            "#6P#10703F……私も“彼女”と\x01",
            "決着を付ける必要があります。\x02\x03",

            "#10708F私自身のけじめのためにも……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x10A, 0, 0, 76)
    WaitChrThread(0x10A, 0)

    #C0385
    ChrTalk(
        0x10A,
        (
            "#6P#00603F……マクレインと\x01",
            "イアン先生の両名については\x01",
            "詳しい事情聴取の必要もあります。\x02\x03",

            "#00601F私も同行するつもりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x15,
        (
            "#11P#01004Fクク……\x01",
            "止めても無駄そうだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x32, 1, 0, 91)
    OP_68(1020, 1900, -13060, 3000)
    MoveCamera(143, 12, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(18500, 3000)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrPos(0x2B, 0, 60000, -10000, 0)
    OP_D5(0x2B, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x15, 0x4)

    def lambda_10F99():
        OP_96(0x2B, 0x0, 0x2710, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_10F99)
    BeginChrThread(0x2B, 3, 0, 71)
    OP_68(0, 45000, 0, 0)
    MoveCamera(231, -60, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(55000, 0)
    MoveCamera(211, -30, 0, 7000)
    SetCameraDistance(45000, 7000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    SetChrPos(0x18, 11000, 0, -2000, 200)
    OP_D5(0x18, 0x0, 0x30D40, 0x0, 0x0)
    OP_75(0x17, 0x2, 0xBB8)
    OP_68(1020, 1900, -13060, 0)
    MoveCamera(143, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_68(-240, 1100, -11750, 3000)
    MoveCamera(143, 17, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0387
    ChrTalk(
        0x15,
        (
            "#11P#01003F──大統領の身柄も含めて、\x01",
            "市内とタワーの方は任せておけ。\x02\x03",

            "#01001Fお前たちはお前たちで\x01",
            "納得できるまでやって来い。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0x7D0, 0xC8)

    #C0388
    ChrTalk(
        0x15,
        (
            "#01007F#11P『特務支援課』として……\x01",
            "何よりもお前たち自身として！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("ロイドたち")

    #A0389
    AnonymousTalk(
        0xFF,
        "#4Sはい……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 3000)
    StopSound(132, 490, 40)
    StopSound(112, 490, 40)
    FadeToDark(2000, 0, -1)
    Sleep(500)
    StopSound(497, 1500, 50)
    StopSound(496, 1500, 50)
    OP_0D()
    EndChrThread(0x2B, 0xFF)
    OP_6F(0x79)
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x84)
    OP_24(0x70)
    Sleep(2000)
    OP_29(0xB1, 0x1, 0xF)
    OP_29(0xB1, 0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_END)), "loc_11231")
    OP_E0(0x33, 0x0)
    OP_E0(0x80, 0x0)
    Sleep(500)

    label("loc_11231")

    OP_E5(0x3)
    SetScenarioFlags(0x23, 6)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_70_CF06 end

    def Function_71_11240(): pass

    label("Function_71_11240")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11264")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_71_11240")

    label("loc_11264")

    Return()

    # Function_71_11240 end

    def Function_72_11265(): pass

    label("Function_72_11265")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1127F")
    OP_FC(0x1)
    Jump("loc_112C8")

    label("loc_1127F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11299")
    OP_FC(0x2)
    Jump("loc_112C8")

    label("loc_11299")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_112B3")
    OP_FC(0x1)
    Jump("loc_112C8")

    label("loc_112B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_112C8")
    OP_FC(0x2)

    label("loc_112C8")

    Sleep(1)
    Return()

    # Function_72_11265 end

    def Function_73_112CC(): pass

    label("Function_73_112CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_112E6")
    OP_FC(0x6)
    Jump("loc_1132F")

    label("loc_112E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11300")
    OP_FC(0x6)
    Jump("loc_1132F")

    label("loc_11300")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1131A")
    OP_FC(0xB)
    Jump("loc_1132F")

    label("loc_1131A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1132F")
    OP_FC(0x5)

    label("loc_1132F")

    Sleep(1)
    Return()

    # Function_73_112CC end

    def Function_74_11333(): pass

    label("Function_74_11333")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1134D")
    OP_FC(0xB)
    Jump("loc_11396")

    label("loc_1134D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11367")
    OP_FC(0xB)
    Jump("loc_11396")

    label("loc_11367")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11381")
    OP_FC(0x6)
    Jump("loc_11396")

    label("loc_11381")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11396")
    OP_FC(0x6)

    label("loc_11396")

    Sleep(1)
    Return()

    # Function_74_11333 end

    def Function_75_1139A(): pass

    label("Function_75_1139A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_113B4")
    OP_FC(0x1)
    Jump("loc_113FD")

    label("loc_113B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_113CE")
    OP_FC(0x2)
    Jump("loc_113FD")

    label("loc_113CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_113E8")
    OP_FC(0x1)
    Jump("loc_113FD")

    label("loc_113E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_113FD")
    OP_FC(0x2)

    label("loc_113FD")

    Sleep(1)
    Return()

    # Function_75_1139A end

    def Function_76_11401(): pass

    label("Function_76_11401")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1141B")
    OP_FC(0x1)
    Jump("loc_11464")

    label("loc_1141B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11435")
    OP_FC(0x2)
    Jump("loc_11464")

    label("loc_11435")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1144F")
    OP_FC(0x1)
    Jump("loc_11464")

    label("loc_1144F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11464")
    OP_FC(0x2)

    label("loc_11464")

    Sleep(1)
    Return()

    # Function_76_11401 end

    def Function_77_11468(): pass

    label("Function_77_11468")

    Sound(905, 0, 100, 0)
    Sound(904, 2, 100, 0)
    OP_74(0x5, 0xF)
    OP_71(0x5, 0x3A3, 0x3CA, 0x0, 0x0)
    Sleep(2000)
    Sound(902, 0, 70, 0)
    OP_79(0x5)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB, 0x32, 0x0, 0x0)
    Sound(951, 0, 100, 0)
    OP_24(0x388)
    Return()

    # Function_77_11468 end

    def Function_78_114AA(): pass

    label("Function_78_114AA")

    Sound(905, 0, 100, 0)
    OP_71(0x5, 0x4E2, 0x4F6, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x4F6, 0x51E, 0x0, 0x20)
    Return()

    # Function_78_114AA end

    def Function_79_114CC(): pass

    label("Function_79_114CC")

    OP_71(0xD, 0x0, 0x64, 0x0, 0x8)
    OP_79(0xD)
    OP_71(0xD, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_79_114CC end

    def Function_80_114E8(): pass

    label("Function_80_114E8")

    OP_71(0xE, 0x0, 0x64, 0x0, 0x8)
    OP_79(0xE)
    OP_71(0xE, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_80_114E8 end

    def Function_81_11504(): pass

    label("Function_81_11504")

    OP_71(0xF, 0x0, 0x64, 0x0, 0x8)
    OP_79(0xF)
    OP_71(0xF, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_81_11504 end

    def Function_82_11520(): pass

    label("Function_82_11520")

    OP_71(0x10, 0x0, 0x64, 0x0, 0x8)
    OP_79(0x10)
    OP_71(0x10, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_82_11520 end

    def Function_83_1153C(): pass

    label("Function_83_1153C")

    OP_71(0x11, 0x0, 0x64, 0x0, 0x8)
    OP_79(0x11)
    OP_71(0x11, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_83_1153C end

    def Function_84_11558(): pass

    label("Function_84_11558")

    OP_74(0x12, 0xF)
    OP_71(0x12, 0x0, 0x64, 0x0, 0x8)
    OP_79(0x12)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_84_11558 end

    def Function_85_1157C(): pass

    label("Function_85_1157C")

    OP_75(0xD, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_85_1157C end

    def Function_86_11587(): pass

    label("Function_86_11587")

    OP_75(0xE, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_86_11587 end

    def Function_87_11592(): pass

    label("Function_87_11592")

    OP_75(0xF, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_87_11592 end

    def Function_88_1159D(): pass

    label("Function_88_1159D")

    OP_75(0x10, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_88_1159D end

    def Function_89_115A8(): pass

    label("Function_89_115A8")

    OP_75(0x11, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_89_115A8 end

    def Function_90_115B3(): pass

    label("Function_90_115B3")

    OP_75(0x12, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_90_115B3 end

    def Function_91_115BE(): pass

    label("Function_91_115BE")

    Sound(497, 2, 0, 0)
    Sound(496, 2, 0, 0)
    Sleep(200)
    OP_25(0x1F1, 0x5)
    OP_25(0x1F0, 0x5)
    Sleep(200)
    OP_25(0x1F1, 0xA)
    OP_25(0x1F0, 0xA)
    Sleep(200)
    OP_25(0x1F1, 0xF)
    OP_25(0x1F0, 0xF)
    Sleep(200)
    OP_25(0x1F1, 0x14)
    OP_25(0x1F0, 0x14)
    Sleep(200)
    OP_25(0x1F1, 0x19)
    OP_25(0x1F0, 0x19)
    Sleep(200)
    OP_25(0x1F1, 0x1E)
    OP_25(0x1F0, 0x1E)
    Sleep(200)
    OP_25(0x1F1, 0x23)
    OP_25(0x1F0, 0x23)
    Sleep(200)
    OP_25(0x1F1, 0x28)
    OP_25(0x1F0, 0x28)
    Sleep(200)
    OP_25(0x1F1, 0x2D)
    OP_25(0x1F0, 0x2D)
    Sleep(200)
    OP_25(0x1F1, 0x32)
    OP_25(0x1F0, 0x32)
    Return()

    # Function_91_115BE end

    def Function_92_11639(): pass

    label("Function_92_11639")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    EventEnd(0x5)
    SetCameraDistance(13000, 0)
    Return()

    # Function_92_11639 end

    def Function_93_11651(): pass

    label("Function_93_11651")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    StopEffect(0x9, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0390
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x394),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x394, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x18A, 0)
    OP_65(0x0, 0x1)
    EventEnd(0x3)
    Return()

    # Function_93_11651 end

    def Function_94_116B2(): pass

    label("Function_94_116B2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05620.itc", 0x1E)
    LoadChrToIndex("chr/ch30000.itc", 0x1F)
    LoadChrToIndex("chr/ch02500.itc", 0x20)
    SetChrPos(0x0, 0, -33620, 0, 0)
    SetChrPos(0x1, 0, -33620, 0, 0)
    SetChrPos(0x2, 0, -33620, 0, 0)
    SetChrPos(0x3, 0, -33620, 0, 0)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, -800, 0, -16900, 180)
    SetChrChipByIndex(0x1B, 0x1F)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1B, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 800, 0, -16900, 180)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -1800, 0, -19500, 45)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1D, 0x4)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 3700, 0, -17500, 270)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, -17000, 180)
    ClearMapObjFlags(0x16, 0x4)
    OP_68(0, 900, -19000, 0)
    MoveCamera(140, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Return()

    # Function_94_116B2 end

    SaveToFile()

Try(main)
