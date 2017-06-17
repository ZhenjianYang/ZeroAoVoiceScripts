from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t112b.bin",                # FileName
        "t112b",                    # MapName
        "t112b",                    # Location
        0x0048,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 72, 0, 9, 0, 10],
    )

    BuildStringList((
        "t112b",                  # 0
        "雷纳德管家",             # 1
        "罗克萨努",               # 2
        "布伦达",                 # 3
        "伊丽莎白",               # 4
        "雷克特",                 # 5
        "向导巴克雷",             # 6
        "玛丽亚贝尔",             # 7
        "雾香",                   # 8
        "伊梅尔达夫人",           # 9
        "尼基塔",                 # 10
        "黑衣人",                 # 11
        "黑衣人",                 # 12
        "客人",                   # 13
        "客人",                   # 14
        "客人",                   # 15
        "客人",                   # 16
        "客人",                   # 17
        "客人",                   # 18
        "客人",                   # 19
        "客人",                   # 20
        "客人",                   # 21
        "客人",                   # 22
        "客人",                   # 23
        "客人",                   # 24
        "客人",                   # 25
        "客人",                   # 26
        "客人",                   # 27
        "客人",                   # 28
        "客人",                   # 29
        "马尔克尼会长",           # 30
        "哈尔特曼议长",           # 31
        "玛丽亚贝尔",             # 32
    ))

    AddCharChip((
        "chr/ch27500.itc",                   # 00
        "chr/ch34500.itc",                   # 01
        "chr/ch25700.itc",                   # 02
        "chr/ch39100.itc",                   # 03
        "chr/ch07400.itc",                   # 04
        "chr/ch27902.itc",                   # 05
        "chr/ch25800.itc",                   # 06
        "chr/ch33202.itc",                   # 07
        "chr/ch33002.itc",                   # 08
        "chr/ch05502.itc",                   # 09
        "chr/ch36200.itc",                   # 0A
        "chr/ch36100.itc",                   # 0B
        "chr/ch07302.itc",                   # 0C
        "chr/ch09002.itc",                   # 0D
        "chr/ch27702.itc",                   # 0E
        "chr/ch21602.itc",                   # 0F
        "chr/ch26902.itc",                   # 10
        "chr/ch21802.itc",                   # 11
        "chr/ch26802.itc",                   # 12
        "chr/ch21902.itc",                   # 13
        "chr/ch33002.itc",                   # 14
        "chr/ch21700.itc",                   # 15
        "chr/ch22002.itc",                   # 16
        "chr/ch32402.itc",                   # 17
        "chr/ch33302.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(-2670,   0,       22700,   270,  385,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-1340,   0,       7380,    90,   385,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-39,     1000,    28479,   180,  385,  0x0, 0,   2,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(9770,    4000,    5820,    180,  385,  0x0, 0,   3,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(9090,    4000,    20329,   225,  385,  0x0, 0,   4,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-6099,   0,       3190,    90,   385,  0x0, 0,   6,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(2400,    150,     6599,    0,    469,  0x0, 0,   9,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(-2400,   150,     11600,   0,    385,  0x0, 0,   12,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(4000,    150,     19100,   0,    469,  0x0, 0,   13,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(-2400,   150,     9100,    0,    469,  0x0, 0,   18,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(-3660,   0,       1009,    0,    385,  0x0, 0,   10,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(3819,    0,       1009,    0,    385,  0x0, 0,   11,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-4000,   150,     19100,   0,    469,  0x0, 0,   7,   0,   255, 255, 0,   24,  255,  0)
    DeclNpc(-2400,   150,     19100,   0,    469,  0x0, 0,   8,   0,   255, 255, 0,   25,  255,  0)
    DeclNpc(5550,    150,     11600,   0,    469,  0x0, 0,   8,   0,   255, 255, 0,   26,  255,  0)
    DeclNpc(2400,    150,     11600,   0,    469,  0x0, 0,   5,   0,   255, 255, 0,   27,  255,  0)
    DeclNpc(2400,    150,     16600,   0,    469,  0x0, 0,   14,  0,   255, 255, 0,   28,  255,  0)
    DeclNpc(5550,    150,     16600,   0,    469,  0x0, 0,   15,  0,   255, 255, 0,   29,  255,  0)
    DeclNpc(-5599,   150,     16600,   0,    469,  0x0, 0,   24,  0,   255, 255, 0,   30,  255,  0)
    DeclNpc(-4000,   150,     16600,   0,    469,  0x0, 0,   23,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(-5599,   150,     6599,    0,    469,  0x0, 0,   8,   0,   255, 255, 0,   32,  255,  0)
    DeclNpc(-5599,   150,     11600,   0,    469,  0x0, 0,   17,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(4000,    150,     9100,    0,    469,  0x0, 0,   17,  0,   255, 255, 0,   34,  255,  0)
    DeclNpc(5550,    150,     9100,    0,    469,  0x0, 0,   19,  0,   255, 255, 0,   35,  255,  0)
    DeclNpc(-4000,   150,     14100,   0,    469,  0x0, 0,   20,  0,   255, 255, 0,   36,  255,  0)
    DeclNpc(-2400,   150,     14100,   0,    469,  0x0, 0,   21,  0,   255, 255, 0,   37,  255,  0)
    DeclNpc(-4000,   150,     9100,    0,    469,  0x0, 0,   22,  0,   255, 255, 0,   38,  255,  0)
    DeclNpc(2400,    150,     14100,   0,    469,  0x0, 0,   8,   0,   255, 255, 0,   39,  255,  0)
    DeclNpc(4000,    150,     14100,   0,    469,  0x0, 0,   16,  0,   255, 255, 0,   40,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(2400,    -150,    6599,    0,    469,  0x0, 0,   9,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_588",          # 00, 0
        "Function_1_640",          # 01, 1
        "Function_2_641",          # 02, 2
        "Function_3_832",          # 03, 3
        "Function_4_85D",          # 04, 4
        "Function_5_888",          # 05, 5
        "Function_6_8E9",          # 06, 6
        "Function_7_9CB",          # 07, 7
        "Function_8_A5D",          # 08, 8
        "Function_9_AEF",          # 09, 9
        "Function_10_BF9",         # 0A, 10
        "Function_11_C16",         # 0B, 11
        "Function_12_DDB",         # 0C, 12
        "Function_13_FC3",         # 0D, 13
        "Function_14_10AC",        # 0E, 14
        "Function_15_118C",        # 0F, 15
        "Function_16_1202",        # 10, 16
        "Function_17_164C",        # 11, 17
        "Function_18_1698",        # 12, 18
        "Function_19_1859",        # 13, 19
        "Function_20_1B9E",        # 14, 20
        "Function_21_1DC2",        # 15, 21
        "Function_22_1E12",        # 16, 22
        "Function_23_1F3F",        # 17, 23
        "Function_24_1FCE",        # 18, 24
        "Function_25_2124",        # 19, 25
        "Function_26_23AA",        # 1A, 26
        "Function_27_254E",        # 1B, 27
        "Function_28_26D8",        # 1C, 28
        "Function_29_284E",        # 1D, 29
        "Function_30_2982",        # 1E, 30
        "Function_31_2ADD",        # 1F, 31
        "Function_32_2CA5",        # 20, 32
        "Function_33_2E2F",        # 21, 33
        "Function_34_2FB2",        # 22, 34
        "Function_35_31F0",        # 23, 35
        "Function_36_3444",        # 24, 36
        "Function_37_3594",        # 25, 37
        "Function_38_36E5",        # 26, 38
        "Function_39_3858",        # 27, 39
        "Function_40_3A11",        # 28, 40
        "Function_41_3B60",        # 29, 41
        "Function_42_3E75",        # 2A, 42
        "Function_43_4D1C",        # 2B, 43
        "Function_44_4D59",        # 2C, 44
        "Function_45_559D",        # 2D, 45
        "Function_46_55E6",        # 2E, 46
        "Function_47_562F",        # 2F, 47
        "Function_48_5678",        # 30, 48
        "Function_49_56C1",        # 31, 49
        "Function_50_570A",        # 32, 50
        "Function_51_5753",        # 33, 51
        "Function_52_579C",        # 34, 52
        "Function_53_57E5",        # 35, 53
        "Function_54_582E",        # 36, 54
        "Function_55_5877",        # 37, 55
        "Function_56_58C0",        # 38, 56
        "Function_57_5909",        # 39, 57
        "Function_58_5952",        # 3A, 58
        "Function_59_599B",        # 3B, 59
        "Function_60_59E4",        # 3C, 60
        "Function_61_5A2D",        # 3D, 61
        "Function_62_5A76",        # 3E, 62
    ))


    def Function_0_588(): pass

    label("Function_0_588")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5C8"),
        (1, "loc_5D4"),
        (2, "loc_5E0"),
        (3, "loc_5EC"),
        (4, "loc_5F8"),
        (5, "loc_604"),
        (6, "loc_610"),
        (SWITCH_DEFAULT, "loc_61C"),
    )


    label("loc_5C8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_5D4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_5E0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_5EC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_5F8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_604")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_610")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_61C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_628")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_63F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_63F")

    Return()

    # Function_0_588 end

    def Function_1_640(): pass

    label("Function_1_640")

    Return()

    # Function_1_640 end

    def Function_2_641(): pass

    label("Function_2_641")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_831")
    OP_95(0xFE, -1340, 0, 9870, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -1340, 0, 12360, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -1340, 0, 15020, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -1340, 0, 17340, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -1340, 0, 19800, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, 1200, 0, 19800, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 1200, 0, 17340, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 1200, 0, 15020, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 1200, 0, 12360, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 1200, 0, 9870, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 1200, 0, 7380, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -1340, 0, 7380, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    Jump("Function_2_641")

    label("loc_831")

    Return()

    # Function_2_641 end

    def Function_3_832(): pass

    label("Function_3_832")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_85C")
    OP_94(0xFE, 0xFFFFF3F8, 0x6A5E, 0xAB4, 0x73FA, 0x3E8)
    Sleep(300)
    Jump("Function_3_832")

    label("loc_85C")

    Return()

    # Function_3_832 end

    def Function_4_85D(): pass

    label("Function_4_85D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_887")
    OP_94(0xFE, 0x20E4, 0xD84, 0x2AC6, 0x1F72, 0x3E8)
    Sleep(300)
    Jump("Function_4_85D")

    label("loc_887")

    Return()

    # Function_4_85D end

    def Function_5_888(): pass

    label("Function_5_888")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8E8")
    OP_95(0xFE, 5570, 0, 3190, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -6100, 0, 3190, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    Jump("Function_5_888")

    label("loc_8E8")

    Return()

    # Function_5_888 end

    def Function_6_8E9(): pass

    label("Function_6_8E9")

    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -4990, 0, 24290, 135)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 3140, 0, 31200, 45)
    ClearChrFlags(0xA, 0x80)
    BeginChrThread(0xA, 0, 0, 3)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 8680, 4000, 20780, 225)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 8140, 4000, 20220, 315)
    ClearChrFlags(0xD, 0x80)
    BeginChrThread(0xD, 0, 0, 5)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    Return()

    # Function_6_8E9 end

    def Function_7_9CB(): pass

    label("Function_7_9CB")

    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x8000)
    Return()

    # Function_7_9CB end

    def Function_8_A5D(): pass

    label("Function_8_A5D")

    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x8000)
    ClearChrFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x8000)
    Return()

    # Function_8_A5D end

    def Function_9_AEF(): pass

    label("Function_9_AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B05")
    Event(0, 41)
    Jump("loc_B16")

    label("loc_B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B16")
    Event(0, 42)

    label("loc_B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_B25")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 44)

    label("loc_B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_B33")
    Jump("loc_BF5")

    label("loc_B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_B6C")
    Call(0, 6)
    SetChrPos(0x9, -3480, 1000, 29970, 135)
    SetChrPos(0xA, -2430, 1000, 30860, 135)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_BF5")

    label("loc_B6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_BA2")
    SetChrPos(0x9, -3480, 1000, 29970, 135)
    SetChrPos(0xA, -2430, 1000, 30860, 135)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_BF5")

    label("loc_BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_BF5")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0xA, 0x80)
    BeginChrThread(0xA, 0, 0, 3)
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 6)), scpexpr(EXPR_END)), "loc_BEF")
    SetChrPos(0xB, 8250, 4000, 19670, 45)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_BF5")

    label("loc_BEF")

    BeginChrThread(0xB, 0, 0, 4)

    label("loc_BF5")

    Call(0, 7)
    Return()

    # Function_9_AEF end

    def Function_10_BF9(): pass

    label("Function_10_BF9")

    SoundDistance(0x7C, 0xFFFFFFF6, 0x3E8, 0x9F7E, 0x2710, 0x186A0, 0x64, 0x0)
    Return()

    # Function_10_BF9 end

    def Function_11_C16(): pass

    label("Function_11_C16")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_C27")
    Jump("loc_DD7")

    label("loc_C27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_CF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB4")
    OP_93(0xFE, 0x87, 0x0)

    #C0001
    ChrTalk(
        0xFE,
        (
            "拍卖品清单……准备完毕。\x01",
            "木槌……准备完毕。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 400)

    #C0002
    ChrTalk(
        0xFE,
        (
            "哎呀，您要上二楼席位吗？\x01",
            "请从这边的楼梯上去。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CF0")

    label("loc_CB4")


    #C0003
    ChrTalk(
        0xFE,
        (
            "在二楼席位也可以\x01",
            "正常参加竞拍哦，\x01",
            "请从这边的楼梯上去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF0")

    Jump("loc_DD7")

    label("loc_CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_D03")
    Jump("loc_DD7")

    label("loc_D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_DD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D87")

    #C0004
    ChrTalk(
        0xFE,
        (
            "哎呀，客人……\x01",
            "距离竞拍会开始\x01",
            "还有一点时间哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "会场正在进行准备，\x01",
            "目前谢绝客人入内，请您谅解。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DD7")

    label("loc_D87")


    #C0006
    ChrTalk(
        0xFE,
        (
            "距离竞拍会开始\x01",
            "还有一点时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "在西南大间的客厅里\x01",
            "消磨一下时间如何呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD7")

    TalkEnd(0xFE)
    Return()

    # Function_11_C16 end

    def Function_12_DDB(): pass

    label("Function_12_DDB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_DEC")
    Jump("loc_FBF")

    label("loc_DEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_EF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E73")

    #C0008
    ChrTalk(
        0xFE,
        (
            "伊丽莎白真是的，\x01",
            "似乎很喜欢粘着\x01",
            "来宾雷克特先生呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "那小家伙\x01",
            "平时不太亲近人的……\x01",
            "真是不可思议呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_EF2")

    label("loc_E73")


    #C0010
    ChrTalk(
        0xFE,
        (
            "说起来，雷克特先生\x01",
            "擅自就给伊丽莎白\x01",
            "起了个『小黑』这样的名字。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "要是以后叫它『伊丽莎白』\x01",
            "也不听的话，可该怎么办呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF2")

    Jump("loc_FBF")

    label("loc_EF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_F05")
    Jump("loc_FBF")

    label("loc_F05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_FBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F78")

    #C0012
    ChrTalk(
        0xFE,
        (
            "老爷养的猫伊丽莎白\x01",
            "不知道跑到哪里去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "唔唔……真担心它\x01",
            "会对各位来宾失礼啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_FBF")

    label("loc_F78")


    #C0014
    ChrTalk(
        0xFE,
        "二位有没有见到一只黑猫？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "伊丽莎白真是的……\x01",
            "躲到哪里去了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FBF")

    TalkEnd(0xFE)
    Return()

    # Function_12_DDB end

    def Function_13_FC3(): pass

    label("Function_13_FC3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_FD4")
    Jump("loc_10A8")

    label("loc_FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_1027")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FEF")
    Call(0, 14)
    Jump("loc_1022")

    label("loc_FEF")


    #C0016
    ChrTalk(
        0xFE,
        (
            "台上也检查完毕了……\x01",
            "之后就等拍卖品搬进来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1022")

    Jump("loc_10A8")

    label("loc_1027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_1035")
    Jump("loc_10A8")

    label("loc_1035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_10A8")

    #C0017
    ChrTalk(
        0xFE,
        (
            "很抱歉，客人……\x01",
            "请不要\x01",
            "到台上来。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "这里是展示拍卖品的地方，\x01",
            "为了以防万一，\x01",
            "我正在进行严格检查。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A8")

    TalkEnd(0xFE)
    Return()

    # Function_13_FC3 end

    def Function_14_10AC(): pass

    label("Function_14_10AC")


    #C0019
    ChrTalk(
        0xFE,
        (
            "台上的检查\x01",
            "终于结束了。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "在角落里找到了这本书……\x01",
            "大概是去年的宾客忘在这里的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "那位客人今年\x01",
            "好像没来……\x01",
            "不介意的话，就送给各位吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '黑市医生格伦　10卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('黑市医生格伦　10卷', 1)
    SetScenarioFlags(0x9D, 1)
    Return()

    # Function_14_10AC end

    def Function_15_118C(): pass

    label("Function_15_118C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_119D")
    Jump("loc_11FE")

    label("loc_119D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_11BB")

    #C0023
    ChrTalk(
        0xFE,
        "喵呜呜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_11FE")

    label("loc_11BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_11C9")
    Jump("loc_11FE")

    label("loc_11C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_11FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 6)), scpexpr(EXPR_END)), "loc_11EE")

    #C0024
    ChrTalk(
        0xFE,
        "喵啊～～\x02",
    )

    CloseMessageWindow()
    Jump("loc_11FE")

    label("loc_11EE")


    #C0025
    ChrTalk(
        0xFE,
        "喵～～咕。\x02",
    )

    CloseMessageWindow()

    label("loc_11FE")

    TalkEnd(0xFE)
    Return()

    # Function_15_118C end

    def Function_16_1202(): pass

    label("Function_16_1202")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_1213")
    Jump("loc_1648")

    label("loc_1213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_14E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1426")
    OP_4B(0xB, 0xFF)

    #C0026
    ChrTalk(
        0x101,
        (
            "#5105F雷克特先生……\x01",
            "你在这种地方啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xC,
        (
            "#3509F是啊，小黑很亲近我嘛，\x01",
            "都不让我走呢。\x02\x03",

            "#3502F哎呀呀，受欢迎的男人真辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 400)

    #C0028
    ChrTalk(
        0xB,
        "喵呜？\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x151,
        "#5709F啊哈哈，真是位有趣的先生啊。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xC,
        (
            "#3504F……话说，拍卖会差不多\x01",
            "快开始了……\x02\x03",

            "#3501F怎么，你们不参加吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#5103F是、是的。\x02\x03",

            "#5100F因为有点要事，\x01",
            "所以打算稍微离席一阵。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xC,
        (
            "#3507F哦哦，走吧。\x01",
            "竞争对手减少，我会更轻松嘛。\x02\x03",

            "#3504F嗯，虽然不知道你们有什么要事……\x01",
            "但要努力做好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#5101F好、好的……\x01",
            "（难道他察觉到了什么吗……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_14DC")

    label("loc_1426")


    #C0034
    ChrTalk(
        0xC,
        (
            "#3510F我既然是作为老头子的代理人过来，\x01",
            "总得拍点什么回去才行。\x02\x03",

            "#3509F好～就算是为了小黑，\x01",
            "在黄金色的猫食展出之前，\x01",
            "要坚持到底！\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#5112F（我想应该不会\x01",
            "  有那种东西展出……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14DC")

    Jump("loc_1648")

    label("loc_14E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_14EF")
    Jump("loc_1648")

    label("loc_14EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1648")
    OP_4B(0xB, 0xFF)
    TurnDirection(0xFE, 0xB, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F3")

    #C0036
    ChrTalk(
        0xC,
        (
            "#3500F小黑，我给你\x01",
            "钓到晚饭了哦。\x02\x03",

            "#3504F心怀感激地收下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xB,
        "喵呜～～？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xB,
        "（大吃大嚼……）\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xC,
        (
            "#3509F哦～哦～！\x01",
            "在吃了在吃了！\x02\x03",

            "#3500F哎呀，原来这种鱼\x01",
            "是可以吃的啊，\x01",
            "我之前都不知道呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#5106F（喂喂……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1644")

    label("loc_15F3")


    #C0041
    ChrTalk(
        0xB,
        "（大吃大嚼……）\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xC,
        (
            "#3500F小黑，要细嚼慢咽，不要急哦。\x01",
            "鱼身还剩下很多呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1644")

    OP_4C(0xB, 0xFF)

    label("loc_1648")

    TalkEnd(0xFE)
    Return()

    # Function_16_1202 end

    def Function_17_164C(): pass

    label("Function_17_164C")

    TalkBegin(0xFE)

    #C0043
    ChrTalk(
        0xFE,
        "哎呀……各位客人，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "竞拍即将开始，\x01",
            "请尽快就坐等候。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_164C end

    def Function_18_1698(): pass

    label("Function_18_1698")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_172C")
    Jump("loc_1776")

    label("loc_172C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_174C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1776")

    label("loc_174C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_176C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1776")

    label("loc_176C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1776")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1814")

    #C0045
    ChrTalk(
        0xE,
        (
            "#2904F我就在这里\x01",
            "观看竞拍会的\x01",
            "拍卖物吧。\x02\x03",

            "#2902F虽然不知道发生了什么事……\x01",
            "不过你们要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1851")

    label("loc_1814")


    #C0046
    ChrTalk(
        0xE,
        (
            "#2902F虽然不知道发生了什么事……\x01",
            "不过你们要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1851")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_18_1698 end

    def Function_19_1859(): pass

    label("Function_19_1859")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_18ED")
    Jump("loc_1937")

    label("loc_18ED")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_190D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1937")

    label("loc_190D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_192D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1937")

    label("loc_192D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1937")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B19")

    #C0047
    ChrTalk(
        0xF,
        (
            "#3400F你们几个……\x01",
            "遇到什么事了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#5105F……哎！？\x01",
            "您怎么会知道……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xF,
        (
            "#3404F拍卖会\x01",
            "即将开始的时候，\x01",
            "你们就离开了席位……\x02\x03",

            "#3402F肯定是因为发生了什么事——\x01",
            "这样想是很自然的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x151,
        (
            "#5705F……真是位洞察力优秀的\x01",
            "姐姐啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xF,
        "#3404F……呵呵。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#5103F虽然这话不能大声说……\x01",
            "不过，在这幢宅邸里即将\x01",
            "发生非同寻常的大事。\x02\x03",

            "#5101F雾香小姐，\x01",
            "您也请多加小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xF,
        (
            "#3400F……明白了。\x01",
            "我就老实待在会场里，\x01",
            "不出去了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1B96")

    label("loc_1B19")


    #C0054
    ChrTalk(
        0xF,
        (
            "#3404F比起观看竞拍会，\x01",
            "你们竟然会优先处理那件事……\x01",
            "看来一定是很不寻常的事件吧。\x02\x03",

            "#3400F我会老实待在会场里，\x01",
            "不出去的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B96")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_1859 end

    def Function_20_1B9E(): pass

    label("Function_20_1B9E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C32")
    Jump("loc_1C7C")

    label("loc_1C32")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C52")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C7C")

    label("loc_1C52")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C72")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C7C")

    label("loc_1C72")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C7C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D41")

    #C0055
    ChrTalk(
        0xFE,
        (
            "罗赞贝尔克工房制造的人偶\x01",
            "就算会展出拍卖，大概也得\x01",
            "等到最后才能出现吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "那么，到底会拍到怎样的价格呢……\x01",
            "我开始期待了呢。\x01",
            "嘻哈哈……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1DBA")

    label("loc_1D41")


    #C0057
    ChrTalk(
        0xFE,
        (
            "罗赞贝尔克工房制造的人偶\x01",
            "就算会参加拍卖，展出顺序\x01",
            "大概也是在最后吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "在此之前，要不要先小睡片刻呢。\x01",
            "嘻哈哈……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DBA")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_1B9E end

    def Function_21_1DC2(): pass

    label("Function_21_1DC2")

    TalkBegin(0xFE)
    SetChrSubChip(0xFE, 0x1)

    #C0059
    ChrTalk(
        0x11,
        (
            "呵呵……\x01",
            "今天可要为我\x01",
            "拍下宝石哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x22,
        (
            "呼……\x01",
            "小事一桩啦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_1DC2 end

    def Function_22_1E12(): pass

    label("Function_22_1E12")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F12")
    OP_93(0xFE, 0x0, 0x0)

    #C0061
    ChrTalk(
        0xFE,
        (
            "嘁……那些家伙在干什么啊。\x01",
            "怎么过了这么久，\x01",
            "还没把商品搬进来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "这可事关会长的脸面。\x01",
            "要是耽误了开场，\x01",
            "后果可是会很严重啊……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 400)

    #C0063
    ChrTalk(
        0xFE,
        "……啊，失礼。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "请不必担心，\x01",
            "竞拍会将按照预定进行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_1F3B")

    label("loc_1F12")


    #C0065
    ChrTalk(
        0xFE,
        (
            "请不必担心，\x01",
            "竞拍会将按照预定进行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F3B")

    TalkEnd(0xFE)
    Return()

    # Function_22_1E12 end

    def Function_23_1F3F(): pass

    label("Function_23_1F3F")

    TalkBegin(0xFE)

    #C0066
    ChrTalk(
        0xFE,
        (
            "刚才，我们的上司\x01",
            "好像感觉到了也许有\x01",
            "可疑人物混了进来……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "但目前还没有接到\x01",
            "宾客中存在可疑人物\x01",
            "的报告。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        "请放心享受竞拍会。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_1F3F end

    def Function_24_1FCE(): pass

    label("Function_24_1FCE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2062")
    Jump("loc_20AC")

    label("loc_2062")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2082")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20AC")

    label("loc_2082")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_20A2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20AC")

    label("loc_20A2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20AC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0069
    ChrTalk(
        0xFE,
        "竞拍终于要开始了呢。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "出价就交给我先生了，\x01",
            "我得先习惯这种气氛……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_1FCE end

    def Function_25_2124(): pass

    label("Function_25_2124")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_21B8")
    Jump("loc_2202")

    label("loc_21B8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_21D8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2202")

    label("loc_21D8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21F8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2202")

    label("loc_21F8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2202")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    OP_52(0x14, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x14, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_22BB")
    Jump("loc_2305")

    label("loc_22BB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_22DB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2305")

    label("loc_22DB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22FB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2305")

    label("loc_22FB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2305")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0071
    ChrTalk(
        0xFE,
        (
            "哈哈哈……不必紧张。\x01",
            "就像平常购物时一样，\x01",
            "放松点就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "没什么啦，当是\x01",
            "买点价格稍高的\x01",
            "爱好品不就好了嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_2124 end

    def Function_26_23AA(): pass

    label("Function_26_23AA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_243E")
    Jump("loc_2488")

    label("loc_243E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_245E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2488")

    label("loc_245E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_247E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2488")

    label("loc_247E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2488")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0073
    ChrTalk(
        0xFE,
        (
            "在客厅里听马尔克尼会长的口气，\x01",
            "好像除了传闻中的拍卖品以外，\x01",
            "还有很值得期待的好东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "为了避免中意的商品出现时没钱拍，\x01",
            "可得保留一些米拉才好。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_23AA end

    def Function_27_254E(): pass

    label("Function_27_254E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25E2")
    Jump("loc_262C")

    label("loc_25E2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2602")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_262C")

    label("loc_2602")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2622")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_262C")

    label("loc_2622")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_262C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0075
    ChrTalk(
        0xFE,
        (
            "参加竞拍时，如何在初期阶段\x01",
            "展示自己的资金实力……\x01",
            "将成为决定胜负的关键。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "为了让别人不敢轻易抬价，\x01",
            "必须要强硬地出价。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_27_254E end

    def Function_28_26D8(): pass

    label("Function_28_26D8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_276C")
    Jump("loc_27B6")

    label("loc_276C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_278C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_27B6")

    label("loc_278C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27AC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_27B6")

    label("loc_27AC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27B6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0077
    ChrTalk(
        0xFE,
        (
            "今天结识了\x01",
            "哈尔特曼议长，\x01",
            "最大的目的已经达到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "之后就是再拍点高额的物品，\x01",
            "继续表现一下自己吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_28_26D8 end

    def Function_29_284E(): pass

    label("Function_29_284E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_28E2")
    Jump("loc_292C")

    label("loc_28E2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2902")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_292C")

    label("loc_2902")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2922")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_292C")

    label("loc_2922")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_292C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0079
    ChrTalk(
        0xFE,
        (
            "哈哈哈……\x01",
            "今年要带点什么回去呢……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_29_284E end

    def Function_30_2982(): pass

    label("Function_30_2982")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A16")
    Jump("loc_2A60")

    label("loc_2A16")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2A36")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A60")

    label("loc_2A36")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A56")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A60")

    label("loc_2A56")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A60")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0080
    ChrTalk(
        0xFE,
        (
            "去年拍下过\x01",
            "七耀石戒指……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "祈祷今年的展品中会有\x01",
            "比它更加珍贵的物品吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_2982 end

    def Function_31_2ADD(): pass

    label("Function_31_2ADD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B71")
    Jump("loc_2BBB")

    label("loc_2B71")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B91")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BBB")

    label("loc_2B91")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BB1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BBB")

    label("loc_2BB1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BBB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0082
    ChrTalk(
        0xFE,
        (
            "去年为了著名画家\x01",
            "拉迪·雷纳尔德的名画，\x01",
            "我一直和别人竞争到最后。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "当我喊出决定性的落槌价格之后，\x01",
            "竞争对手那懊恼的表情……\x01",
            "真是令人兴奋不已啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "希望今年也能\x01",
            "体会到那种兴奋呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_2ADD end

    def Function_32_2CA5(): pass

    label("Function_32_2CA5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D39")
    Jump("loc_2D83")

    label("loc_2D39")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D59")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D83")

    label("loc_2D59")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D79")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D83")

    label("loc_2D79")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D83")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0085
    ChrTalk(
        0xFE,
        (
            "在竞拍会上展出的拍卖品\x01",
            "都是在别处无法买到的贵重物品。\x01",
            "我也很期待。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "……虽然很不爽大量的米拉\x01",
            "将要流进马尔克尼的商会。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_2CA5 end

    def Function_33_2E2F(): pass

    label("Function_33_2E2F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2EC3")
    Jump("loc_2F0D")

    label("loc_2EC3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2EE3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F0D")

    label("loc_2EE3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F03")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F0D")

    label("loc_2F03")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F0D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0087
    ChrTalk(
        0xFE,
        (
            "和大人物们都打过招呼了，\x01",
            "接下来就只需享受拍卖会了。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "……你是不是有点紧张？\x01",
            "哈哈哈，绷那么紧可不好哦，年轻人。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_2E2F end

    def Function_34_2FB2(): pass

    label("Function_34_2FB2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3046")
    Jump("loc_3090")

    label("loc_3046")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3066")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3090")

    label("loc_3066")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3086")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3090")

    label("loc_3086")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3090")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3164")

    #C0089
    ChrTalk(
        0xFE,
        (
            "……仔细一看，\x01",
            "那位金发的小姐……\x01",
            "不是ＩＢＣ的千金吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "我记得她也是\x01",
            "罗赞贝尔克工房人偶的\x01",
            "狂热爱好者……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "……糟糕了，\x01",
            "人偶说不定会被她拍下……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_31E8")

    label("loc_3164")


    #C0092
    ChrTalk(
        0xFE,
        (
            "那位小姐\x01",
            "如果是ＩＢＣ的千金……\x01",
            "那可就太难对付了。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "不、不行，我可不能示弱。\x01",
            "我也算是个贵族……\x01",
            "资金上的实力应该不会输的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31E8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_34_2FB2 end

    def Function_35_31F0(): pass

    label("Function_35_31F0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3284")
    Jump("loc_32CE")

    label("loc_3284")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_32A4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32CE")

    label("loc_32A4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32C4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32CE")

    label("loc_32C4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32CE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    OP_52(0x1E, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x1E, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3387")
    Jump("loc_33D1")

    label("loc_3387")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_33A7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_33D1")

    label("loc_33A7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33C7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_33D1")

    label("loc_33C7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_33D1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0094
    ChrTalk(
        0xFE,
        (
            "喂喂，不要太激动。\x01",
            "要是冲动起来，\x01",
            "本来能赢的竞争都赢不了啦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_35_31F0 end

    def Function_36_3444(): pass

    label("Function_36_3444")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_34D8")
    Jump("loc_3522")

    label("loc_34D8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_34F8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3522")

    label("loc_34F8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3518")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3522")

    label("loc_3518")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3522")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0095
    ChrTalk(
        0xFE,
        (
            "黑手党举办的竞拍会\x01",
            "究竟是怎样的东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        "就亲眼确认一下吧。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_36_3444 end

    def Function_37_3594(): pass

    label("Function_37_3594")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3628")
    Jump("loc_3672")

    label("loc_3628")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3648")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3672")

    label("loc_3648")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3668")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3672")

    label("loc_3668")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3672")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0097
    ChrTalk(
        0xFE,
        (
            "放眼望去，\x01",
            "这里都没有踏实\x01",
            "做生意的人啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        "感觉有点可怕呢。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_37_3594 end

    def Function_38_36E5(): pass

    label("Function_38_36E5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3779")
    Jump("loc_37C3")

    label("loc_3779")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3799")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37C3")

    label("loc_3799")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37B9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37C3")

    label("loc_37B9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37C3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0099
    ChrTalk(
        0xFE,
        (
            "（只要带着这个女人，\x01",
            "　看起来就很有面子了吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "（相比之下，\x01",
            "　宝石礼物什么的已经算便宜了。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_38_36E5 end

    def Function_39_3858(): pass

    label("Function_39_3858")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_38EC")
    Jump("loc_3936")

    label("loc_38EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_390C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3936")

    label("loc_390C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_392C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3936")

    label("loc_392C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3936")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0101
    ChrTalk(
        0x23,
        (
            "哇哈哈哈，\x01",
            "终于要开始了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x23,
        (
            "女儿啊，你知道在今天竞拍中，\x01",
            "能拍下众多商品的是谁吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x24,
        (
            "那就是米拉最多的人……\x01",
            "也就是父亲您。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x23,
        (
            "哇哈哈，一点也不错。\x01",
            "你果然懂事。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_39_3858 end

    def Function_40_3A11(): pass

    label("Function_40_3A11")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3AA5")
    Jump("loc_3AEF")

    label("loc_3AA5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3AC5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3AEF")

    label("loc_3AC5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3AE5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3AEF")

    label("loc_3AE5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3AEF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0105
    ChrTalk(
        0xFE,
        (
            "呵呵……父亲\x01",
            "真是个直爽\x01",
            "又自信的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        "男人就要这样才行。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_40_3A11 end

    def Function_41_3B60(): pass

    label("Function_41_3B60")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 7)
    SetChrPos(0x101, -600, 0, -1150, 0)
    SetChrPos(0xEF, 600, 0, -1150, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-4910, 2700, 9100, 0)
    MoveCamera(343, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(28640, 0)
    FadeToBright(1000, 0)
    OP_68(-560, 2700, 10410, 8000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(0, 3800, 4200, 0)
    MoveCamera(0, 8, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(16110, 0)
    OP_68(0, 2300, 4200, 4000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_3C51():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C51)
    Sleep(200)

    def lambda_3C69():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3C69)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_6F(0x1)
    OP_0D()

    #C0107
    ChrTalk(
        0x101,
        (
            "#5105F#5P看来，这里\x01",
            "好像就是竞拍会场……\x02\x03",

            "#5106F这种豪华程度真是让人叹为观止啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3D3C")

    #C0108
    ChrTalk(
        0x102,
        (
            "#5306F#11P里面好像\x01",
            "还有小型瀑布……\x02\x03",

            "#5301F老实说，感觉真是\x01",
            "极尽奢华之能事啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DF0")

    label("loc_3D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3D9A")

    #C0109
    ChrTalk(
        0x103,
        (
            "#5406F#11P里面好像\x01",
            "还有小型瀑布……\x02\x03",

            "#5411F这里真的……\x01",
            "是在建筑物内部吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DF0")

    label("loc_3D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3DF0")

    #C0110
    ChrTalk(
        0x104,
        (
            "#5606F#11P那里面好像\x01",
            "还有小型瀑布……\x02\x03",

            "#5601F我们真的是在建筑物内部吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DF0")

    TurnDirection(0x101, 0xEF, 500)

    #C0111
    ChrTalk(
        0x101,
        (
            "#5103F#5P总、总之，\x01",
            "也去别的地方看看吧。\x02\x03",

            "#5101F而且也想确认一下\x01",
            "与会宾客都是些什么样的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, -2900, 180)
    SetScenarioFlags(0xA5, 1)
    EventEnd(0x5)
    Call(0, 7)
    Return()

    # Function_41_3B60 end

    def Function_42_3E75(): pass

    label("Function_42_3E75")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08102.itc", 0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3E9B")
    LoadChrToIndex("chr/ch07702.itc", 0x1F)
    Jump("loc_3EBE")

    label("loc_3E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3EAF")
    LoadChrToIndex("chr/ch07802.itc", 0x1F)
    Jump("loc_3EBE")

    label("loc_3EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3EBE")
    LoadChrToIndex("chr/ch07902.itc", 0x1F)

    label("loc_3EBE")

    LoadChrToIndex("chr/ch05502.itc", 0x20)
    AddParty(0x50, 0xFF, 0xFF)
    SetChrPos(0x101, 600, 0, -2250, 0)
    SetChrPos(0xEF, -600, 0, -2250, 0)
    SetChrPos(0x138, 0, 0, -1450, 0)
    SetChrPos(0x151, 0, 0, -3000, 0)
    OP_A7(0x151, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Call(0, 6)
    OP_4B(0xD, 0xFF)
    SetChrPos(0xD, 0, 0, 16500, 180)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrPos(0x9, 2870, 1000, 31060, 45)
    Call(0, 7)
    OP_68(0, 1600, 30250, 0)
    MoveCamera(0, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(27500, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1600, 9250, 12000)
    Sleep(7500)

    def lambda_3FA8():
        OP_95(0xFE, 600, 0, 3250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FA8)

    def lambda_3FC2():
        OP_95(0xFE, -600, 0, 3250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3FC2)

    def lambda_3FDC():
        OP_95(0xFE, 0, 0, 4450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_3FDC)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x138, 1)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(-890, 1800, 4510, 0)
    MoveCamera(50, 13, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetCameraDistance(17000, 2500)
    OP_6F(0x10)
    OP_0D()

    #C0112
    ChrTalk(
        0x101,
        "#5108F#2P真是好热闹啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_40AB")

    #C0113
    ChrTalk(
        0x102,
        (
            "#5301F#12P嗯……看来会有相当多的\x01",
            "米拉流入主办方的口袋呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4144")

    label("loc_40AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_40FC")

    #C0114
    ChrTalk(
        0x103,
        (
            "#5401F#12P看这样子，似乎会有\x01",
            "相当多的米拉流入主办方的口袋……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4144")

    label("loc_40FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4144")

    #C0115
    ChrTalk(
        0x104,
        (
            "#5601F#12P嗯……看来会有相当多的\x01",
            "米拉流进主办方的口袋啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4144")

    OP_68(-890, 1800, 5010, 2000)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_4165():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4165)
    WaitChrThread(0xD, 1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4193():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4193)
    WaitChrThread(0xD, 1)

    #C0116
    ChrTalk(
        0xD,
        (
            "#5P玛丽亚贝尔小姐，\x01",
            "我们恭候多时了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x10E, 0x12C)
    Sleep(300)
    OP_93(0xD, 0x5A, 0x1F4)
    Sleep(500)
    OP_93(0xD, 0xB4, 0x12C)

    #C0117
    ChrTalk(
        0xD,
        "#5P这边的席位可以吗？\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x138,
        "#2902F#2P嗯，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_93(0x138, 0xB4, 0x1F4)

    #C0119
    ChrTalk(
        0x138,
        (
            "#2900F#5P──来，\x01",
            "坐下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        "#5102F#2P嗯，好的……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4297")

    #C0121
    ChrTalk(
        0x102,
        (
            "#5306F#12P终究还是有点\x01",
            "紧张呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42F6")

    label("loc_4297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_42C8")

    #C0122
    ChrTalk(
        0x103,
        (
            "#5406F#12P终究是有点\x01",
            "紧张……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42F6")

    label("loc_42C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_42F6")

    #C0123
    ChrTalk(
        0x104,
        (
            "#5606F#12P到底是有点\x01",
            "紧张啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42F6")

    OP_93(0x138, 0x0, 0x1F4)
    Sleep(100)

    def lambda_4305():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4305)
    Sleep(300)
    BeginChrThread(0x138, 3, 0, 43)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 43)
    Sleep(700)
    BeginChrThread(0xEF, 3, 0, 43)
    WaitChrThread(0xD, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    EndChrThread(0x138, 0x1)
    EndChrThread(0x101, 0x3)
    EndChrThread(0xEF, 0x3)
    EndChrThread(0x138, 0x3)
    FadeToBright(1000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x10)
    SetChrPos(0x101, 4000, 150, 6600, 0)
    SetChrChipByIndex(0xEF, 0x1F)
    SetChrSubChip(0xEF, 0x0)
    SetChrFlags(0xEF, 0x4)
    SetChrFlags(0xEF, 0x10)
    SetChrPos(0xEF, 5550, 150, 6600, 0)
    SetChrChipByIndex(0x138, 0x20)
    SetChrSubChip(0x138, 0x0)
    SetChrFlags(0x138, 0x4)
    SetChrFlags(0x138, 0x40)
    SetChrPos(0x138, 2400, 50, 6600, 0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x151, 0x80)
    ClearChrBattleFlags(0x151, 0x8000)
    OP_A7(0x151, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(2110, 2200, 6880, 0)
    MoveCamera(38, 13, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17670, 0)
    OP_68(2110, 1300, 6880, 3500)
    Sleep(2000)

    def lambda_4430():
        OP_95(0xFE, 0, 0, 3350, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4430)
    WaitChrThread(0x151, 1)
    OP_63(0x151, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x151, 0x101, 500)
    #Sound(1438, 255, 90, 0)    #voice#Lazy

    #C0124
    ChrTalk(
        0x151,
        "#5P#5702F啊，你们在这里啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x138, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(100)
    SetChrSubChip(0xEF, 0x1)
    Sleep(100)
    SetChrSubChip(0x138, 0x1)
    OP_68(3600, 1300, 8380, 3000)

    def lambda_44ED():
        OP_95(0xFE, 1610, 0, 7750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_44ED)
    WaitChrThread(0x151, 1)
    OP_93(0x151, 0x87, 0x1F4)
    OP_6F(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4539")

    #C0125
    ChrTalk(
        0x102,
        "#5305F#11P哎呀，瓦吉。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4588")

    label("loc_4539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4563")

    #C0126
    ChrTalk(
        0x103,
        "#5405F#11P瓦吉先生……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4588")

    label("loc_4563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4588")

    #C0127
    ChrTalk(
        0x104,
        "#5605F#11P哦，是你啊。\x02",
    )

    CloseMessageWindow()

    label("loc_4588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 2)), scpexpr(EXPR_END)), "loc_4627")

    #C0128
    ChrTalk(
        0x101,
        (
            "#5100F#11P我们刚才看到的\x01",
            "那对夫妇……\x02\x03",

            "他们好像已经顺利和好了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x151,
        (
            "#5704F#5P呵呵，似乎是呢。\x02\x03",

            "#5702F这样一来，我也终于\x01",
            "可以光荣卸任了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46D7")

    label("loc_4627")


    #C0130
    ChrTalk(
        0x101,
        (
            "#5105F#11P你好像独自一人……\x02\x03",

            "#5101F刚才的那场夫妇吵架，\x01",
            "结果怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x151,
        (
            "#5704F#5P呵呵，说来说去，\x01",
            "似乎总算是物归原主了呢。\x02\x03",

            "#5702F这样一来，我也终于\x01",
            "可以光荣卸任了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46D7")


    #C0132
    ChrTalk(
        0x101,
        "#5102F#11P是吗……太好了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4723")

    #C0133
    ChrTalk(
        0x102,
        "#5302F#11P呵呵，辛苦了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_477B")

    label("loc_4723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_474D")

    #C0134
    ChrTalk(
        0x103,
        "#5402F#11P……辛苦了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_477B")

    label("loc_474D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_477B")

    #C0135
    ChrTalk(
        0x104,
        (
            "#5602F#11P哈哈……\x01",
            "辛苦你了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_477B")


    #C0136
    ChrTalk(
        0x138,
        (
            "#2902F#12P呵呵，你们似乎认识\x01",
            "这位有趣的人啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#5105F#11P啊……\x01",
            "那个，这位是──\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x151,
        (
            "#5703F#5P我叫瓦吉，\x01",
            "瓦吉·赫米斯菲亚。\x02\x03",

            "#5700F您是ＩＢＣ总裁的千金，\x01",
            "玛丽亚贝尔·库罗伊斯小姐吧？\x02\x03",

            "见到您非常荣幸。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x138,
        (
            "#2909F#12P哎呀，呵呵。\x01",
            "被抢占先机了呢。\x02\x03",

            "#2900F是瓦吉先生吗，\x01",
            "不嫌弃的话，\x01",
            "要给你准备个附近的席位吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x151,
        (
            "#5704F#5P不，那倒不用。\x02\x03",

            "#5700F其实我有些事\x01",
            "想告诉他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#5105F#11P哎……\x02",
    )

    CloseMessageWindow()

    def lambda_4912():
        OP_95(0xFE, 4200, 0, 7750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4912)
    Sleep(300)
    SetChrSubChip(0x138, 0x0)
    Sleep(300)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x151, 1)
    OP_93(0x151, 0xB4, 0x1F4)

    #C0142
    ChrTalk(
        0x151,
        (
            "#5701F#5P（……我从窗子往后院看去，\x01",
            "  发现有好几条狗睡着了。）\x02\x03",

            "（你有没有什么头绪？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0143
    ChrTalk(
        0x101,
        "#5113F#11P（……真的吗？）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4A53")

    #C0144
    ChrTalk(
        0x102,
        (
            "#5305F#11P（说到狗……\x01",
            "  也就是那些军犬吧。）\x02\x03",

            "#5301F（可是，竟然会睡着……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B10")

    label("loc_4A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4AB2")

    #C0145
    ChrTalk(
        0x103,
        (
            "#5405F#11P（说到狗……\x01",
            "  就是那些军犬吧。）\x02\x03",

            "#5401F（可是，竟然睡着了……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B10")

    label("loc_4AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4B10")

    #C0146
    ChrTalk(
        0x104,
        (
            "#5605F#11P（说到狗～\x01",
            "  大概就是那些军犬吧。）\x02\x03",

            "#5601F（不过，竟然会睡着啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B10")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0147
    ChrTalk(
        0x101,
        (
            "#5103F#11P──玛丽亚贝尔小姐。\x02\x03",

            "#5100F非常抱歉，\x01",
            "我们要稍微离席一下。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x138, 0x2)

    #C0148
    ChrTalk(
        0x138,
        (
            "#2904F#6P呵呵，事情似乎\x01",
            "变得有趣起来了呢。\x02\x03",

            "#2902F不必介意我。\x02\x03",

            "我会代替你们，\x01",
            "把竞拍会的拍卖品\x01",
            "欣赏到最后一刻的。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        "#5102F#11P……十分感谢。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4C40")

    #C0150
    ChrTalk(
        0x102,
        "#5302F#11P谢谢了，贝尔。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C8F")

    label("loc_4C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4C6C")

    #C0151
    ChrTalk(
        0x103,
        "#5402F#11P那就拜托您了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C8F")

    label("loc_4C6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4C8F")

    #C0152
    ChrTalk(
        0x104,
        "#5609F#11P多谢啦～！\x02",
    )

    CloseMessageWindow()

    label("loc_4C8F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0xD, -6100, 0, 3190, 90)
    OP_4C(0xD, 0xFF)
    SetChrPos(0x9, 3140, 0, 31200, 45)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x10)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrSubChip(0xEF, 0x0)
    ClearChrFlags(0x138, 0x4)
    ClearChrFlags(0x138, 0x10)
    ClearChrFlags(0x138, 0x40)
    SetChrChipByIndex(0x138, 0xFF)
    SetChrSubChip(0x138, 0x0)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    RemoveParty(0x37, 0x0)
    SetScenarioFlags(0x5C, 1)
    NewScene("t111B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_3E75 end

    def Function_43_4D1C(): pass

    label("Function_43_4D1C")


    def lambda_4D21():
        OP_95(0xFE, 0, 0, 7450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4D21)
    WaitChrThread(0xFE, 1)

    def lambda_4D3F():
        OP_95(0xFE, 5450, 0, 7450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4D3F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_43_4D1C end

    def Function_44_4D59(): pass

    label("Function_44_4D59")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06200.itc", 0x1E)
    LoadChrToIndex("chr/ch06500.itc", 0x1F)
    LoadChrToIndex("chr/ch33200.itc", 0x20)
    LoadChrToIndex("chr/ch33000.itc", 0x21)
    LoadChrToIndex("chr/ch27700.itc", 0x22)
    LoadChrToIndex("chr/ch21600.itc", 0x23)
    LoadChrToIndex("chr/ch33300.itc", 0x24)
    LoadChrToIndex("chr/ch21800.itc", 0x25)
    LoadChrToIndex("chr/ch21900.itc", 0x26)
    LoadChrToIndex("chr/ch20800.itc", 0x28)
    LoadChrToIndex("chr/ch20900.itc", 0x29)
    LoadChrToIndex("chr/ch22000.itc", 0x2A)
    SetChrPos(0x0, 0, 0, 0, 0)
    SetChrPos(0x1, 0, 0, 0, 0)
    SetChrPos(0x2, 0, 0, 0, 0)
    SetChrPos(0x3, 0, 0, 0, 0)
    SetChrPos(0x4, 0, 0, 0, 0)
    SetChrPos(0x5, 0, 0, 0, 0)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x25, 0x1E)
    SetChrSubChip(0x25, 0x0)
    SetChrChipByIndex(0x26, 0x1F)
    SetChrSubChip(0x26, 0x0)
    SetChrPos(0x25, 0, 1000, 26500, 180)
    SetChrPos(0x26, -1400, 1000, 29000, 180)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    Call(0, 6)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    OP_93(0x12, 0x0, 0x0)
    OP_93(0x13, 0x0, 0x0)
    Call(0, 7)
    FadeToBright(1000, 0)
    OP_68(0, 2400, 21500, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(33400, 0)
    OP_68(0, 100, 21500, 6000)
    OP_63(0x25, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x14, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x18, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x22, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x1E, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_63(0x16, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x1B, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x24, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x20, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_63(0x17, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x1A, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x1D, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x1F, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_63(0x14, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x18, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x22, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x1E, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_63(0x16, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x1B, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x24, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x20, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_63(0x17, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x1A, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x1D, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x1F, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x1)
    OP_64(0x25)
    OP_0D()
    Fade(1000)
    OP_68(-90, 2100, 22700, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(22140, 0)
    SetCameraDistance(20140, 3000)
    OP_6F(0x10)
    OP_0D()

    #C0153
    ChrTalk(
        0x25,
        (
            "#3005F#5P各、各位，请肃静！\x02\x03",

            "#3000F虽然发生了一点小小的意外，\x01",
            "但竞拍会将照常举行──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0154
    ChrTalk(
        0x15,
        (
            "#5P比起这个，刚才的枪声\x01",
            "到底是怎么回事啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0155
    ChrTalk(
        0x18,
        "#5P你、你以为我们是什么人啊！\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0156
    ChrTalk(
        0x1B,
        (
            "#11P视、视情况，我会向\x01",
            "自治州政府提出抗议哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x25, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0157
    ChrTalk(
        0x25,
        "#3005F#5P请、请大家冷静一下……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(-700, 2100, 30550, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(20740, 0)
    SetCameraDistance(19240, 2500)
    OP_6F(0x79)
    OP_0D()

    #C0158
    ChrTalk(
        0x26,
        (
            "#2703F#5P哼，一帮废物……\x02\x03",

            "#2701F……竟敢\x01",
            "给我的脸上抹黑……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x26, 0x10E, 0x190)

    def lambda_53D9():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_53D9)
    Sleep(500)
    OP_63(0x25, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x25, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x25, 0x26, 500)

    #C0159
    ChrTalk(
        0x25,
        (
            "#3005F#12P哈、哈尔特曼议长！？\x02\x03",

            "#3007F您要去哪里……\x01",
            "请、请等一下！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    WaitChrThread(0x26, 1)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    Fade(1000)
    SetChrSubChip(0xE, 0x1)
    OP_68(0, 2400, 21500, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(33400, 0)
    OP_68(0, 100, 21500, 9000)
    BeginChrThread(0x8, 3, 0, 62)
    OP_6F(0x1)
    OP_0D()
    Fade(500)
    OP_68(1900, 100, 18300, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(23770, 0)
    OP_0D()
    Sleep(300)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    SetChrFlags(0x27, 0x8)

    #N0160
    NpcTalk(
        0x27,
        "玛丽亚贝尔",
        (
            "#2904F#11P呵呵……\x01",
            "竞拍会泡汤了呢。\x02\x03",

            "#2902F虽然原定目标落空了……\x01",
            "不过看到了有趣的场面，\x01",
            "也就算了吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("t101B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_4D59 end

    def Function_45_559D(): pass

    label("Function_45_559D")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_55B1():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_55B1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_55D1():
        OP_9B(0x0, 0xFE, 0x0, 0x526C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_55D1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_45_559D end

    def Function_46_55E6(): pass

    label("Function_46_55E6")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_55FA():
        OP_9B(0x0, 0xFE, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_55FA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_561A():
        OP_9B(0x0, 0xFE, 0x0, 0x526C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_561A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_46_55E6 end

    def Function_47_562F(): pass

    label("Function_47_562F")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_5643():
        OP_9B(0x0, 0xFE, 0x0, 0x15AE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5643)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_5663():
        OP_9B(0x0, 0xFE, 0x0, 0x3520, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5663)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_47_562F end

    def Function_48_5678(): pass

    label("Function_48_5678")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_568C():
        OP_9B(0x0, 0xFE, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_568C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_56AC():
        OP_9B(0x0, 0xFE, 0x0, 0x3520, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_56AC)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_48_5678 end

    def Function_49_56C1(): pass

    label("Function_49_56C1")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_56D5():
        OP_9B(0x0, 0xFE, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_56D5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_56F5():
        OP_9B(0x0, 0xFE, 0x0, 0x48A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_56F5)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_49_56C1 end

    def Function_50_570A(): pass

    label("Function_50_570A")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_571E():
        OP_9B(0x0, 0xFE, 0x0, 0x15AE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_571E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_573E():
        OP_9B(0x0, 0xFE, 0x0, 0x48A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_573E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_50_570A end

    def Function_51_5753(): pass

    label("Function_51_5753")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_5767():
        OP_9B(0x0, 0xFE, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5767)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_5787():
        OP_9B(0x0, 0xFE, 0x0, 0x48A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5787)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_51_5753 end

    def Function_52_579C(): pass

    label("Function_52_579C")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_57B0():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_57B0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_57D0():
        OP_9B(0x0, 0xFE, 0x0, 0x48A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_57D0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_52_579C end

    def Function_53_57E5(): pass

    label("Function_53_57E5")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_57F9():
        OP_9B(0x0, 0xFE, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_57F9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_5819():
        OP_9B(0x0, 0xFE, 0x0, 0x2198, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5819)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_53_57E5 end

    def Function_54_582E(): pass

    label("Function_54_582E")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_5842():
        OP_9B(0x0, 0xFE, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5842)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_5862():
        OP_9B(0x0, 0xFE, 0x0, 0x3520, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5862)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_54_582E end

    def Function_55_5877(): pass

    label("Function_55_5877")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_588B():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_588B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_58AB():
        OP_9B(0x0, 0xFE, 0x0, 0x2B5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_58AB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_55_5877 end

    def Function_56_58C0(): pass

    label("Function_56_58C0")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_58D4():
        OP_9B(0x0, 0xFE, 0x0, 0x15AE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_58D4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_58F4():
        OP_9B(0x0, 0xFE, 0x0, 0x2B5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_58F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_56_58C0 end

    def Function_57_5909(): pass

    label("Function_57_5909")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_591D():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_591D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_593D():
        OP_9B(0x0, 0xFE, 0x0, 0x3EE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_593D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_57_5909 end

    def Function_58_5952(): pass

    label("Function_58_5952")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_5966():
        OP_9B(0x0, 0xFE, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5966)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_5986():
        OP_9B(0x0, 0xFE, 0x0, 0x3EE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5986)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_58_5952 end

    def Function_59_599B(): pass

    label("Function_59_599B")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_59AF():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_59AF)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_59CF():
        OP_9B(0x0, 0xFE, 0x0, 0x2B5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_59CF)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_59_599B end

    def Function_60_59E4(): pass

    label("Function_60_59E4")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_59F8():
        OP_9B(0x0, 0xFE, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_59F8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_5A18():
        OP_9B(0x0, 0xFE, 0x0, 0x3EE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5A18)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_60_59E4 end

    def Function_61_5A2D(): pass

    label("Function_61_5A2D")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_5A41():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5A41)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_5A61():
        OP_9B(0x0, 0xFE, 0x0, 0x3EE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5A61)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_61_5A2D end

    def Function_62_5A76(): pass

    label("Function_62_5A76")

    BeginChrThread(0x15, 3, 0, 46)
    BeginChrThread(0x18, 3, 0, 49)
    BeginChrThread(0x1E, 3, 0, 55)
    Sleep(6000)
    BeginChrThread(0x19, 3, 0, 50)
    BeginChrThread(0x21, 3, 0, 58)
    BeginChrThread(0x1C, 3, 0, 53)
    Sleep(6000)
    BeginChrThread(0x14, 3, 0, 45)
    BeginChrThread(0x23, 3, 0, 60)
    BeginChrThread(0x17, 3, 0, 48)
    Sleep(6000)
    BeginChrThread(0x1B, 3, 0, 52)
    BeginChrThread(0x24, 3, 0, 61)
    BeginChrThread(0x1F, 3, 0, 56)
    Sleep(6000)
    BeginChrThread(0x1A, 3, 0, 51)
    BeginChrThread(0x20, 3, 0, 57)
    Return()

    # Function_62_5A76 end

    SaveToFile()

Try(main)
