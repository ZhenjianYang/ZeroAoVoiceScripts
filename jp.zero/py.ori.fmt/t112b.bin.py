from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "執事レナード",           # 1
        "ロクサーヌ",             # 2
        "ブレンダ",               # 3
        "エリザベート",           # 4
        "レクター",               # 5
        "案内人バークレイ",       # 6
        "マリアベル",             # 7
        "キリカ",                 # 8
        "イメルダ夫人",           # 9
        "ニキータ",               # 10
        "黒服",                   # 11
        "黒服",                   # 12
        "招待客",                 # 13
        "招待客",                 # 14
        "招待客",                 # 15
        "招待客",                 # 16
        "招待客",                 # 17
        "招待客",                 # 18
        "招待客",                 # 19
        "招待客",                 # 20
        "招待客",                 # 21
        "招待客",                 # 22
        "招待客",                 # 23
        "招待客",                 # 24
        "招待客",                 # 25
        "招待客",                 # 26
        "招待客",                 # 27
        "招待客",                 # 28
        "招待客",                 # 29
        "マルコーニ会長",         # 30
        "ハルトマン議長",         # 31
        "マリアベル",             # 32
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
        "Function_12_E2D",         # 0C, 12
        "Function_13_109B",        # 0D, 13
        "Function_14_11C8",        # 0E, 14
        "Function_15_12F0",        # 0F, 15
        "Function_16_1370",        # 10, 16
        "Function_17_188C",        # 11, 17
        "Function_18_18F8",        # 12, 18
        "Function_19_1AE7",        # 13, 19
        "Function_20_1E98",        # 14, 20
        "Function_21_20CA",        # 15, 21
        "Function_22_212C",        # 16, 22
        "Function_23_228F",        # 17, 23
        "Function_24_2366",        # 18, 24
        "Function_25_24D0",        # 19, 25
        "Function_26_2772",        # 1A, 26
        "Function_27_2910",        # 1B, 27
        "Function_28_2AB0",        # 1C, 28
        "Function_29_2C42",        # 1D, 29
        "Function_30_2D7E",        # 1E, 30
        "Function_31_2EE9",        # 1F, 31
        "Function_32_30DB",        # 20, 32
        "Function_33_327D",        # 21, 33
        "Function_34_3414",        # 22, 34
        "Function_35_369A",        # 23, 35
        "Function_36_38FC",        # 24, 36
        "Function_37_3A68",        # 25, 37
        "Function_38_3BD3",        # 26, 38
        "Function_39_3D5E",        # 27, 39
        "Function_40_3F47",        # 28, 40
        "Function_41_40B8",        # 29, 41
        "Function_42_4421",        # 2A, 42
        "Function_43_543C",        # 2B, 43
        "Function_44_5479",        # 2C, 44
        "Function_45_5D2D",        # 2D, 45
        "Function_46_5D76",        # 2E, 46
        "Function_47_5DBF",        # 2F, 47
        "Function_48_5E08",        # 30, 48
        "Function_49_5E51",        # 31, 49
        "Function_50_5E9A",        # 32, 50
        "Function_51_5EE3",        # 33, 51
        "Function_52_5F2C",        # 34, 52
        "Function_53_5F75",        # 35, 53
        "Function_54_5FBE",        # 36, 54
        "Function_55_6007",        # 37, 55
        "Function_56_6050",        # 38, 56
        "Function_57_6099",        # 39, 57
        "Function_58_60E2",        # 3A, 58
        "Function_59_612B",        # 3B, 59
        "Function_60_6174",        # 3C, 60
        "Function_61_61BD",        # 3D, 61
        "Function_62_6206",        # 3E, 62
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
    Jump("loc_E29")

    label("loc_C27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_D09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB8")
    OP_93(0xFE, 0x87, 0x0)

    #C0001
    ChrTalk(
        0xFE,
        (
            "出品物リスト……よし。\x01",
            "木槌……よし。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 400)

    #C0002
    ChrTalk(
        0xFE,
        (
            "おや、２階席へ行かれますかな？\x01",
            "そちらの階段からどうぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D04")

    label("loc_CB8")


    #C0003
    ChrTalk(
        0xFE,
        (
            "２階席からでも問題なく\x01",
            "競売に参加できますよ。\x01",
            "そちらの階段からどうぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D04")

    Jump("loc_E29")

    label("loc_D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_D17")
    Jump("loc_E29")

    label("loc_D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_E29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB7")

    #C0004
    ChrTalk(
        0xFE,
        (
            "おや、お客様……\x01",
            "オークション開始までは\x01",
            "まだ少し時間がございますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "会場は整備中ですので、\x01",
            "立入はご遠慮願えると幸いです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E29")

    label("loc_DB7")


    #C0006
    ChrTalk(
        0xFE,
        (
            "オークション開始までは\x01",
            "まだ少し時間がございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "南西大部屋のサロンで\x01",
            "時間を潰されてはいかがでしょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E29")

    TalkEnd(0xFE)
    Return()

    # Function_11_C16 end

    def Function_12_E2D(): pass

    label("Function_12_E2D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_E3E")
    Jump("loc_1097")

    label("loc_E3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_F9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF1")

    #C0008
    ChrTalk(
        0xFE,
        (
            "エリザベートったら\x01",
            "招待客のレクター様に\x01",
            "随分懐いてしまったみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "あの子はあまり\x01",
            "人に懐かないのですが……\x01",
            "不思議なこともあるものですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_F96")

    label("loc_EF1")


    #C0010
    ChrTalk(
        0xFE,
        (
            "そういえばレクター様、\x01",
            "エリザベートのことを勝手に\x01",
            "“クロ”なんて名前で呼んでましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "“エリザベート”って呼んでも\x01",
            "来なくなっちゃったらどうしましょう……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F96")

    Jump("loc_1097")

    label("loc_F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_FA9")
    Jump("loc_1097")

    label("loc_FA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1097")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1042")

    #C0012
    ChrTalk(
        0xFE,
        (
            "旦那様の飼い猫のエリザベートが\x01",
            "どこかへ行ってしまったのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "うぅん……招待客の皆様に\x01",
            "粗相をしていないか心配です。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1097")

    label("loc_1042")


    #C0014
    ChrTalk(
        0xFE,
        "黒い猫を見ませんでしたか？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "エリザベートったら……\x01",
            "どこに隠れてるのかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1097")

    TalkEnd(0xFE)
    Return()

    # Function_12_E2D end

    def Function_13_109B(): pass

    label("Function_13_109B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_10AC")
    Jump("loc_11C4")

    label("loc_10AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_1113")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C7")
    Call(0, 14)
    Jump("loc_110E")

    label("loc_10C7")


    #C0016
    ChrTalk(
        0xFE,
        (
            "ステージチェックも終わり……\x01",
            "あとは出品物の搬入を待つばかりです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_110E")

    Jump("loc_11C4")

    label("loc_1113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_1121")
    Jump("loc_11C4")

    label("loc_1121")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_11C4")

    #C0017
    ChrTalk(
        0xFE,
        (
            "すみません、お客様……\x01",
            "ステージ上には上がらないで\x01",
            "くださいまし。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "出品物をお披露目する場所ですから\x01",
            "万が一に備えて\x01",
            "厳重にチェックしているのです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C4")

    TalkEnd(0xFE)
    Return()

    # Function_13_109B end

    def Function_14_11C8(): pass

    label("Function_14_11C8")


    #C0019
    ChrTalk(
        0xFE,
        (
            "ステージのチェックも\x01",
            "ようやく終わりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "陰から本が出てきたのですが……\x01",
            "多分、去年の招待客様の忘れ物でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "今年はいらっしゃってない\x01",
            "お客様のようですし……\x01",
            "よろしければ、皆様に差し上げますわ。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2CF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2CF, 1)
    SetScenarioFlags(0x9D, 1)
    Return()

    # Function_14_11C8 end

    def Function_15_12F0(): pass

    label("Function_15_12F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_1301")
    Jump("loc_136C")

    label("loc_1301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_1323")

    #C0023
    ChrTalk(
        0xFE,
        "ふみゃああ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_136C")

    label("loc_1323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_1331")
    Jump("loc_136C")

    label("loc_1331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_136C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 6)), scpexpr(EXPR_END)), "loc_135A")

    #C0024
    ChrTalk(
        0xFE,
        "にゃあ～～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_136C")

    label("loc_135A")


    #C0025
    ChrTalk(
        0xFE,
        "にゃ～～ご。\x02",
    )

    CloseMessageWindow()

    label("loc_136C")

    TalkEnd(0xFE)
    Return()

    # Function_15_12F0 end

    def Function_16_1370(): pass

    label("Function_16_1370")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_1381")
    Jump("loc_1888")

    label("loc_1381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_16E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1604")
    OP_4B(0xB, 0xFF)

    #C0026
    ChrTalk(
        0x101,
        (
            "#5105Fレクターさん……\x01",
            "こんな所にいたんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xC,
        (
            "#3509Fおう、クロに懐かれちまってな。\x01",
            "なかなか放してくれねぇのさ。\x02\x03",

            "#3502Fいやはや、モテる男はツラいぜ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 400)

    #C0028
    ChrTalk(
        0xB,
        "みゃおん？\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x151,
        "#5709Fあはは、おもしろい御仁だね。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xC,
        (
            "#3504F……で、そろそろオークションが\x01",
            "始まるわけだが……\x02\x03",

            "#3501F何、お前ら参加しないの？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#5103Fえ、えぇ。\x02\x03",

            "#5100F用事が出来てしまったので\x01",
            "少しの間、席を離れるつもりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xC,
        (
            "#3507Fおうおう、行ってしまえ。\x01",
            "競争相手が減ればラクってもんだぜ。\x02\x03",

            "#3504Fま、用事とやらが何か知らねぇけど……\x01",
            "せいぜい上手く立ち回るんだなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#5101Fは、はぁ……\x01",
            "（何か気付いているのか……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_16DE")

    label("loc_1604")


    #C0034
    ChrTalk(
        0xC,
        (
            "#3510F俺もオッサンの代理で来てる以上、\x01",
            "何か落札して帰らねぇとなァ。\x02\x03",

            "#3509Fよーし、いっちょクロのために\x01",
            "黄金色のキャットフードが出るまで\x01",
            "粘ってみるか！\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#5112F（多分そんなものは\x01",
            "  出品されないと思うけど……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DE")

    Jump("loc_1888")

    label("loc_16E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_16F1")
    Jump("loc_1888")

    label("loc_16F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1888")
    OP_4B(0xB, 0xFF)
    TurnDirection(0xFE, 0xB, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1825")

    #C0036
    ChrTalk(
        0xC,
        (
            "#3500Fクロ、お前の晩メシを\x01",
            "釣ってきてやったぜ。\x02\x03",

            "#3504Fありがたく受け取るがよい。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xB,
        "にゃぁお～～ん？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xB,
        "（がつがつ……）\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xC,
        (
            "#3509Fお～お～！\x01",
            "食っとる食っとる！\x02\x03",

            "#3500Fいやぁ、この魚って\x01",
            "食っても大丈夫なんだなァ。\x01",
            "初めて知ったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#5106F（おいおい……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1884")

    label("loc_1825")


    #C0041
    ChrTalk(
        0xB,
        "（がつがつ……）\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xC,
        (
            "#3500Fほれ、良く噛んで食えよクロ。\x01",
            "まだまだ身はたっぷり残ってるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1884")

    OP_4C(0xB, 0xFF)

    label("loc_1888")

    TalkEnd(0xFE)
    Return()

    # Function_16_1370 end

    def Function_17_188C(): pass

    label("Function_17_188C")

    TalkBegin(0xFE)

    #C0043
    ChrTalk(
        0xFE,
        "おや……いかがなさいましたか？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "間もなく競売が始まります。\x01",
            "早めに席についてお待ちください。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_188C end

    def Function_18_18F8(): pass

    label("Function_18_18F8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_198C")
    Jump("loc_19D6")

    label("loc_198C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19AC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19D6")

    label("loc_19AC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19CC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19D6")

    label("loc_19CC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19D6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A98")

    #C0045
    ChrTalk(
        0xE,
        (
            "#2904Fわたくしはここで\x01",
            "オークションの出品物を\x01",
            "見届けておきますわ。\x02\x03",

            "#2902F何が起きているかは知りませんけど……\x01",
            "くれぐれも気をつけて。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1ADF")

    label("loc_1A98")


    #C0046
    ChrTalk(
        0xE,
        (
            "#2902F何が起きているかは知りませんけど……\x01",
            "くれぐれも気をつけて。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ADF")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_18_18F8 end

    def Function_19_1AE7(): pass

    label("Function_19_1AE7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B7B")
    Jump("loc_1BC5")

    label("loc_1B7B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1B9B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BC5")

    label("loc_1B9B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BBB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BC5")

    label("loc_1BBB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BC5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E01")

    #C0047
    ChrTalk(
        0xF,
        (
            "#3400Fあなた達……\x01",
            "何かあったのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#5105F……え！？\x01",
            "どうしてそれを……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xF,
        (
            "#3404Fオークションが\x01",
            "今まさに始まろうとしている時に\x01",
            "あなた達が席を立った……\x02\x03",

            "#3402F何かあったと見るのが\x01",
            "自然でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x151,
        (
            "#5705F……なかなか洞察眼に優れた\x01",
            "お姉さんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xF,
        "#3404F……フフ。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#5103Fあまり大きな声では言えませんけど……\x01",
            "この屋敷でただならないことが\x01",
            "起きようとしているみたいです。\x02\x03",

            "#5101Fキリカさんも\x01",
            "充分気をつけてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xF,
        (
            "#3400F……分かったわ。\x01",
            "会場内から出ないように\x01",
            "大人しくしておきましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1E90")

    label("loc_1E01")


    #C0054
    ChrTalk(
        0xF,
        (
            "#3404Fあなた達が競売会を見ることより\x01",
            "優先すべきこと……\x01",
            "よほどのことが起こったようね。\x02\x03",

            "#3400F会場内から出ないように\x01",
            "大人しくしておくわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E90")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_1AE7 end

    def Function_20_1E98(): pass

    label("Function_20_1E98")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F2C")
    Jump("loc_1F76")

    label("loc_1F2C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F4C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F76")

    label("loc_1F4C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F6C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F76")

    label("loc_1F6C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F76")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2043")

    #C0055
    ChrTalk(
        0xFE,
        (
            "ローゼンベルク工房製の人形は\x01",
            "出品されるにしても\x01",
            "最後の方だろうねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "さて、如何ほどの値がつくやら……\x01",
            "楽しみになってきたよ。\x01",
            "ヒヒャヒャ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_20C2")

    label("loc_2043")


    #C0057
    ChrTalk(
        0xFE,
        (
            "ローゼンベルク工房製の人形は\x01",
            "出品されるにしても\x01",
            "最後の方だろうねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "それまでは居眠りでもしてるかね。\x01",
            "ヒヒャヒャ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20C2")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_1E98 end

    def Function_21_20CA(): pass

    label("Function_21_20CA")

    TalkBegin(0xFE)
    SetChrSubChip(0xFE, 0x1)

    #C0059
    ChrTalk(
        0x11,
        (
            "うふふ……\x01",
            "今日は私のために\x01",
            "宝石を落札してね。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x22,
        (
            "ふっ……\x01",
            "お安い御用だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_20CA end

    def Function_22_212C(): pass

    label("Function_22_212C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2256")
    OP_93(0xFE, 0x0, 0x0)

    #C0061
    ChrTalk(
        0xFE,
        (
            "チ……何やってんだあいつら。\x01",
            "いつまでたっても商品が\x01",
            "運び込まれてこねぇじゃねぇか。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "会長の面目がかかってんだ。\x01",
            "開始時間が遅れたら\x01",
            "ただじゃすまねぇぞ……\x02",
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
        "……おっと、失礼。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "ご心配なく。\x01",
            "予定通りことは進んでおりますので。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_228B")

    label("loc_2256")


    #C0065
    ChrTalk(
        0xFE,
        (
            "ご心配なく。\x01",
            "予定通りことは進んでおりますので。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_228B")

    TalkEnd(0xFE)
    Return()

    # Function_22_212C end

    def Function_23_228F(): pass

    label("Function_23_228F")

    TalkBegin(0xFE)

    #C0066
    ChrTalk(
        0xFE,
        (
            "先程、私どもの上司が\x01",
            "不審人物の紛れている可能性を\x01",
            "感じていたようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "今のところ招待客の皆さんに\x01",
            "怪しい人物がまぎれているという\x01",
            "報告はありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        "安心してオークションをお楽しみください。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_228F end

    def Function_24_2366(): pass

    label("Function_24_2366")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23FA")
    Jump("loc_2444")

    label("loc_23FA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_241A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2444")

    label("loc_241A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_243A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2444")

    label("loc_243A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2444")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0069
    ChrTalk(
        0xFE,
        "いよいよ競売が始まるわね。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "入札は主人に任せてみるわ。\x01",
            "まずはこの空気に馴れないと……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_2366 end

    def Function_25_24D0(): pass

    label("Function_25_24D0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2564")
    Jump("loc_25AE")

    label("loc_2564")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2584")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25AE")

    label("loc_2584")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25A4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25AE")

    label("loc_25A4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25AE")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2667")
    Jump("loc_26B1")

    label("loc_2667")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2687")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_26B1")

    label("loc_2687")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26A7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_26B1")

    label("loc_26A7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26B1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0071
    ChrTalk(
        0xFE,
        (
            "ははは……緊張することはない。\x01",
            "普通の買い物と同じように\x01",
            "楽しめばいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "なぁに、ちょっと値段が高い\x01",
            "趣味の物を買うと\x01",
            "思えばいいのだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_24D0 end

    def Function_26_2772(): pass

    label("Function_26_2772")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2806")
    Jump("loc_2850")

    label("loc_2806")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2826")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2850")

    label("loc_2826")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2846")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2850")

    label("loc_2846")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2850")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0073
    ChrTalk(
        0xFE,
        (
            "サロンでのマルコーニ会長の口ぶりだと\x01",
            "噂になっている出品物以外にも\x01",
            "期待できそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "欲しい商品が出たときのために\x01",
            "ミラを温存しなければ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_2772 end

    def Function_27_2910(): pass

    label("Function_27_2910")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_29A4")
    Jump("loc_29EE")

    label("loc_29A4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29C4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29EE")

    label("loc_29C4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29E4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29EE")

    label("loc_29E4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29EE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0075
    ChrTalk(
        0xFE,
        (
            "オークションでは序盤の方で\x01",
            "いかに資金力を見せつけるか……\x01",
            "それが決め手になるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "下手に釣り上げられないためにも\x01",
            "強気で入札していかないと。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_27_2910 end

    def Function_28_2AB0(): pass

    label("Function_28_2AB0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B44")
    Jump("loc_2B8E")

    label("loc_2B44")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B64")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B8E")

    label("loc_2B64")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B84")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B8E")

    label("loc_2B84")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B8E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0077
    ChrTalk(
        0xFE,
        (
            "今日はハルトマン議長との\x01",
            "繋がりが出来た。\x01",
            "大方の目的は達成したわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "あとは高額の商品を落札して\x01",
            "さらにアピールといくかのう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_28_2AB0 end

    def Function_29_2C42(): pass

    label("Function_29_2C42")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2CD6")
    Jump("loc_2D20")

    label("loc_2CD6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2CF6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D20")

    label("loc_2CF6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D16")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D20")

    label("loc_2D16")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D20")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0079
    ChrTalk(
        0xFE,
        (
            "はっはっは……\x01",
            "今年は何を持ち帰れるかのう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_29_2C42 end

    def Function_30_2D7E(): pass

    label("Function_30_2D7E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E12")
    Jump("loc_2E5C")

    label("loc_2E12")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E32")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E5C")

    label("loc_2E32")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E52")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E5C")

    label("loc_2E52")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E5C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0080
    ChrTalk(
        0xFE,
        (
            "去年落札したような\x01",
            "七耀石の指輪……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "あれ以上のレヴェルのものが\x01",
            "あることを祈りますわ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_2D7E end

    def Function_31_2EE9(): pass

    label("Function_31_2EE9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F7D")
    Jump("loc_2FC7")

    label("loc_2F7D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F9D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FC7")

    label("loc_2F9D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FBD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FC7")

    label("loc_2FBD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2FC7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0082
    ChrTalk(
        0xFE,
        (
            "去年はかの著名な画家\x01",
            "ラディ・レイナルドの絵を賭けて\x01",
            "最後まで落札を争ったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "決定的な落札額を言い放った時の\x01",
            "競争相手の悔しそうな顔ときたら……\x01",
            "それはもうゾクゾクきたものよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "今年もあんな興奮が\x01",
            "味わえるといいわね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_2EE9 end

    def Function_32_30DB(): pass

    label("Function_32_30DB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_316F")
    Jump("loc_31B9")

    label("loc_316F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_318F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31B9")

    label("loc_318F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31AF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31B9")

    label("loc_31AF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31B9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0085
    ChrTalk(
        0xFE,
        (
            "オークションの出品物は\x01",
            "他では手に入らない貴重な物ばかり。\x01",
            "わしも楽しみにしておった。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "……マルコーニの商会に\x01",
            "ミラが流れるのは気に食わんがな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_30DB end

    def Function_33_327D(): pass

    label("Function_33_327D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3311")
    Jump("loc_335B")

    label("loc_3311")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3331")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_335B")

    label("loc_3331")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3351")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_335B")

    label("loc_3351")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_335B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0087
    ChrTalk(
        0xFE,
        (
            "お偉方への顔通しも終わったし\x01",
            "あとはオークションを楽しむだけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "……何か緊張していないか？\x01",
            "はっはっは、気張るのはよくないよキミ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_327D end

    def Function_34_3414(): pass

    label("Function_34_3414")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_34A8")
    Jump("loc_34F2")

    label("loc_34A8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_34C8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_34F2")

    label("loc_34C8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34E8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_34F2")

    label("loc_34E8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_34F2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35F6")

    #C0089
    ChrTalk(
        0xFE,
        (
            "……よく見てみたら\x01",
            "あの金髪のお嬢さん……\x01",
            "ＩＢＣのご令嬢じゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "たしか彼女も熱狂的な\x01",
            "ローゼンベルク工房製人形の\x01",
            "ファンだったはず……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "……まずいな。\x01",
            "もしかしたら落札されてしまうかも……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3692")

    label("loc_35F6")


    #C0092
    ChrTalk(
        0xFE,
        (
            "あのお嬢さんが\x01",
            "ＩＢＣのご令嬢だとしたら……\x01",
            "相手が悪すぎるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "い、いや、弱気になってはダメだ。\x01",
            "私も貴族の端くれ……\x01",
            "資金力では負けてないはずだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3692")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_34_3414 end

    def Function_35_369A(): pass

    label("Function_35_369A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_372E")
    Jump("loc_3778")

    label("loc_372E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_374E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3778")

    label("loc_374E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_376E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3778")

    label("loc_376E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3778")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3831")
    Jump("loc_387B")

    label("loc_3831")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3851")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_387B")

    label("loc_3851")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3871")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_387B")

    label("loc_3871")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_387B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0094
    ChrTalk(
        0xFE,
        (
            "ほらほら、熱くならないの。\x01",
            "カッとなってちゃ、\x01",
            "勝てる勝負にも勝てないわよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_35_369A end

    def Function_36_38FC(): pass

    label("Function_36_38FC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3990")
    Jump("loc_39DA")

    label("loc_3990")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_39B0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39DA")

    label("loc_39B0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39D0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39DA")

    label("loc_39D0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39DA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0095
    ChrTalk(
        0xFE,
        (
            "マフィアが運営する競売とやらが\x01",
            "どのようなものか……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        "この目で確かめてみるとするかのう。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_36_38FC end

    def Function_37_3A68(): pass

    label("Function_37_3A68")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3AFC")
    Jump("loc_3B46")

    label("loc_3AFC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B1C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B46")

    label("loc_3B1C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B3C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B46")

    label("loc_3B3C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B46")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0097
    ChrTalk(
        0xFE,
        (
            "どこを見渡しても\x01",
            "堅気の商売をしている人は\x01",
            "見当たらないわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        "なんだか少し怖いわねぇ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_37_3A68 end

    def Function_38_3BD3(): pass

    label("Function_38_3BD3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C67")
    Jump("loc_3CB1")

    label("loc_3C67")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C87")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3CB1")

    label("loc_3C87")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CA7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3CB1")

    label("loc_3CA7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3CB1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0099
    ChrTalk(
        0xFE,
        (
            "（この女性を連れていれば\x01",
            "　とりあえず貫禄は出せるだろう。）\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "（それに比べたら\x01",
            "　宝石のプレゼントなんて安いものだよ。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_38_3BD3 end

    def Function_39_3D5E(): pass

    label("Function_39_3D5E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3DF2")
    Jump("loc_3E3C")

    label("loc_3DF2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3E12")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E3C")

    label("loc_3E12")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E32")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E3C")

    label("loc_3E32")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E3C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0101
    ChrTalk(
        0x23,
        (
            "がっはっはっは。\x01",
            "いよいよじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x23,
        (
            "娘よ、今日の競売で多くの商品を\x01",
            "落札できるのはだれか分かるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x24,
        (
            "それはより多くのミラを持つもの……\x01",
            "つまりお父様ですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x23,
        (
            "がっはっは、その通りじゃ。\x01",
            "よく分かっておるのう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_39_3D5E end

    def Function_40_3F47(): pass

    label("Function_40_3F47")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FDB")
    Jump("loc_4025")

    label("loc_3FDB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3FFB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4025")

    label("loc_3FFB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_401B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4025")

    label("loc_401B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4025")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0105
    ChrTalk(
        0xFE,
        (
            "オホホ……お父様ったら\x01",
            "気持ちのいいほどの\x01",
            "自信家でらっしゃるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        "男の方はこうでなくてはね。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_40_3F47 end

    def Function_41_40B8(): pass

    label("Function_41_40B8")

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

    def lambda_41A9():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41A9)
    Sleep(200)

    def lambda_41C1():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_41C1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_6F(0x1)
    OP_0D()

    #C0107
    ChrTalk(
        0x101,
        (
            "#5105F#5Pどうやらここが\x01",
            "オークション会場みたいだけど……\x02\x03",

            "#5106F何かもう、溜息しか出て来ないな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_42BE")

    #C0108
    ChrTalk(
        0x102,
        (
            "#5306F#11P何だか奥の方に\x01",
            "水が流れているけど……\x02\x03",

            "#5301F正直、あり得ないくらい\x01",
            "贅を尽くしている感じだわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_438E")

    label("loc_42BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4330")

    #C0109
    ChrTalk(
        0x103,
        (
            "#5406F#11P何だか奥の方に\x01",
            "水が流れてますけど……\x02\x03",

            "#5411F本当にここ……\x01",
            "建物の中なんでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_438E")

    label("loc_4330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_438E")

    #C0110
    ChrTalk(
        0x104,
        (
            "#5606F#11Pなんか奥の方に\x01",
            "水が流れてるんだが……\x02\x03",

            "#5601F本当に建物の中なのかよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_438E")

    TurnDirection(0x101, 0xEF, 500)

    #C0111
    ChrTalk(
        0x101,
        (
            "#5103F#5Pと、とにかく\x01",
            "他の場所も回ってみよう。\x02\x03",

            "#5101Fどんな招待客がいるのか\x01",
            "一通り確かめておきたいしな。\x02",
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

    # Function_41_40B8 end

    def Function_42_4421(): pass

    label("Function_42_4421")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08102.itc", 0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4447")
    LoadChrToIndex("chr/ch07702.itc", 0x1F)
    Jump("loc_446A")

    label("loc_4447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_445B")
    LoadChrToIndex("chr/ch07802.itc", 0x1F)
    Jump("loc_446A")

    label("loc_445B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_446A")
    LoadChrToIndex("chr/ch07902.itc", 0x1F)

    label("loc_446A")

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

    def lambda_4554():
        OP_95(0xFE, 600, 0, 3250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4554)

    def lambda_456E():
        OP_95(0xFE, -600, 0, 3250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_456E)

    def lambda_4588():
        OP_95(0xFE, 0, 0, 4450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_4588)
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
        "#5108F#2Pかなりの盛況ぶりだな……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4651")

    #C0113
    ChrTalk(
        0x102,
        (
            "#5301F#12Pええ……\x01",
            "相当なミラが動きそうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46D4")

    label("loc_4651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4698")

    #C0114
    ChrTalk(
        0x103,
        (
            "#5401F#12Pこの様子だと相当なミラが\x01",
            "動きそうです……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46D4")

    label("loc_4698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_46D4")

    #C0115
    ChrTalk(
        0x104,
        (
            "#5601F#12Pああ……\x01",
            "相当なミラが動きそうだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46D4")

    OP_68(-890, 1800, 5010, 2000)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_46F5():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_46F5)
    WaitChrThread(0xD, 1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4723():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4723)
    WaitChrThread(0xD, 1)

    #C0116
    ChrTalk(
        0xD,
        (
            "#5Pマリアベル様、\x01",
            "お待ちしておりました。\x02",
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
        "#5Pこちらの席で宜しいですか？\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x138,
        "#2902F#2Pええ、ありがとう。\x02",
    )

    CloseMessageWindow()
    OP_93(0x138, 0xB4, 0x1F4)

    #C0119
    ChrTalk(
        0x138,
        (
            "#2900F#5P──さあ、\x01",
            "座ってしまいましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        "#5102F#2Pえ、ええ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4859")

    #C0121
    ChrTalk(
        0x102,
        (
            "#5306F#12Pさすがにちょっと\x01",
            "緊張してきたわね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48D4")

    label("loc_4859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4898")

    #C0122
    ChrTalk(
        0x103,
        (
            "#5406F#12Pさすがに少し\x01",
            "緊張してきました……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48D4")

    label("loc_4898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_48D4")

    #C0123
    ChrTalk(
        0x104,
        (
            "#5606F#12Pさすがにちょいと\x01",
            "緊張してきたな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48D4")

    OP_93(0x138, 0x0, 0x1F4)
    Sleep(100)

    def lambda_48E3():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_48E3)
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
    SetChrPos(0x138, 2400, 150, 6600, 0)
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

    def lambda_4A0E():
        OP_95(0xFE, 0, 0, 3350, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4A0E)
    WaitChrThread(0x151, 1)
    OP_63(0x151, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x151, 0x101, 500)
    #Sound(1438, 255, 90, 0)    #voice#Lazy

    #C0124
    ChrTalk(
        0x151,
        "#5P#5702Fああ、ここにいたのか。\x02",
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

    def lambda_4ACF():
        OP_95(0xFE, 1610, 0, 7750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4ACF)
    WaitChrThread(0x151, 1)
    OP_93(0x151, 0x87, 0x1F4)
    OP_6F(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4B1D")

    #C0125
    ChrTalk(
        0x102,
        "#5305F#11Pあら、ワジ君。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B6E")

    label("loc_4B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4B47")

    #C0126
    ChrTalk(
        0x103,
        "#5405F#11Pワジさん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B6E")

    label("loc_4B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4B6E")

    #C0127
    ChrTalk(
        0x104,
        "#5605F#11Pおお、お前か。\x02",
    )

    CloseMessageWindow()

    label("loc_4B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 2)), scpexpr(EXPR_END)), "loc_4C25")

    #C0128
    ChrTalk(
        0x101,
        (
            "#5100F#11P先ほどの\x01",
            "ご夫婦を見かけたけど……\x02\x03",

            "無事、仲直りできたみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x151,
        (
            "#5704F#5Pフフ、そうみたいだね。\x02\x03",

            "#5702Fこれで僕も晴れて\x01",
            "お役御免になったところさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CE9")

    label("loc_4C25")


    #C0130
    ChrTalk(
        0x101,
        (
            "#5105F#11P一人みたいだけど……\x02\x03",

            "#5101Fさっきのケンカは\x01",
            "結局、どうなったんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x151,
        (
            "#5704F#5Pフフ、何だかんだで\x01",
            "元の鞘に収まったみたいだね。\x02\x03",

            "#5702Fそれで僕も晴れて\x01",
            "お役御免になったところさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CE9")


    #C0132
    ChrTalk(
        0x101,
        "#5102F#11Pそうか……よかった。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4D3B")

    #C0133
    ChrTalk(
        0x102,
        "#5302F#11Pふふ、お疲れ様。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DA1")

    label("loc_4D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4D6B")

    #C0134
    ChrTalk(
        0x103,
        "#5402F#11P……お疲れ様です。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DA1")

    label("loc_4D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4DA1")

    #C0135
    ChrTalk(
        0x104,
        (
            "#5602F#11Pはは……\x01",
            "ご苦労さんだったな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DA1")


    #C0136
    ChrTalk(
        0x138,
        (
            "#2902F#12Pふふ、面白い方と\x01",
            "お知り合いみたいですわね？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#5105F#11Pああ……\x01",
            "えっと、こちらの彼は──\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x151,
        (
            "#5703F#5P僕の名前はワジ。\x01",
            "ワジ・ヘミスフィアだよ。\x02\x03",

            "#5700FＩＢＣ総裁のご令嬢、\x01",
            "マリアベル・クロイスさんだね？\x02\x03",

            "お会いできて光栄だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x138,
        (
            "#2909F#12Pあら、うふふ。\x01",
            "機先を制されてしまったわね。\x02\x03",

            "#2900Fワジさんと言ったかしら。\x01",
            "よかったら近くに席を\x01",
            "用意してもらいましょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x151,
        (
            "#5704F#5Pいや、それには及ばない。\x02\x03",

            "#5700F実は少々、そちらの彼らに\x01",
            "伝えたいことがあってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#5105F#11Pえ……\x02",
    )

    CloseMessageWindow()

    def lambda_4F9E():
        OP_95(0xFE, 4200, 0, 7750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4F9E)
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
            "#5701F#5P（……窓から裏庭を見下ろしたら\x01",
            "  犬が何匹も眠っていた。）\x02\x03",

            "（何か心当たりはあるかい？）\x02",
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
        "#5113F#11P（……本当か？）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_50F7")

    #C0144
    ChrTalk(
        0x102,
        (
            "#5305F#11P（犬というと……\x01",
            "  例の軍用犬の事みたいね。）\x02\x03",

            "#5301F（でも、眠っていたって……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51DA")

    label("loc_50F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_516C")

    #C0145
    ChrTalk(
        0x103,
        (
            "#5405F#11P（犬というと……\x01",
            "  例の軍用犬みたいですね。）\x02\x03",

            "#5401F（でも、眠っていたというのは……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51DA")

    label("loc_516C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_51DA")

    #C0146
    ChrTalk(
        0x104,
        (
            "#5605F#11P（犬ってーと、\x01",
            "  例の軍用犬の事みてぇだな。）\x02\x03",

            "#5601F（だが、眠っていたってのは……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51DA")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0147
    ChrTalk(
        0x101,
        (
            "#5103F#11P──マリアベルさん。\x02\x03",

            "#5100F申し訳ないですけど\x01",
            "少しばかり席を外します。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x138, 0x2)

    #C0148
    ChrTalk(
        0x138,
        (
            "#2904F#6Pフフ、色々と面白い事に\x01",
            "なっているみたいですわね。\x02\x03",

            "#2902Fわたくしの事はお気になさらずに。\x02\x03",

            "せいぜい、あなた方の代わりに\x01",
            "オークションでの出品物を\x01",
            "見届けておきますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        "#5102F#11P……感謝します。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_5358")

    #C0150
    ChrTalk(
        0x102,
        "#5302F#11Pありがとう、ベル。\x02",
    )

    CloseMessageWindow()
    Jump("loc_53AF")

    label("loc_5358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_538C")

    #C0151
    ChrTalk(
        0x103,
        "#5402F#11Pよろしくお願いします。\x02",
    )

    CloseMessageWindow()
    Jump("loc_53AF")

    label("loc_538C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_53AF")

    #C0152
    ChrTalk(
        0x104,
        "#5609F#11Pあざーす！\x02",
    )

    CloseMessageWindow()

    label("loc_53AF")

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

    # Function_42_4421 end

    def Function_43_543C(): pass

    label("Function_43_543C")


    def lambda_5441():
        OP_95(0xFE, 0, 0, 7450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5441)
    WaitChrThread(0xFE, 1)

    def lambda_545F():
        OP_95(0xFE, 5450, 0, 7450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_545F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_43_543C end

    def Function_44_5479(): pass

    label("Function_44_5479")

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
            "#3005F#5Pみ、皆さん、ご静粛に！\x02\x03",

            "#3000F少々ハプニングはありましたが\x01",
            "予定通りオークションを開催して──\x02",
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
            "#5Pそれより、先ほどの銃声は\x01",
            "いったい何だったのかね！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0155
    ChrTalk(
        0x18,
        "#5Pわ、我々を誰だと思っている！\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0156
    ChrTalk(
        0x1B,
        (
            "#11Pこ、事と次第によっては\x01",
            "自治州政府に抗議しますわよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x25, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0157
    ChrTalk(
        0x25,
        "#3005F#5Pどうか、どうか落ち着いて……！\x02",
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
            "#2703F#5Pフン、使えん連中だ……\x02\x03",

            "#2701F……よりにもよって\x01",
            "私の顔に泥を塗るとは……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x26, 0x10E, 0x190)

    def lambda_5B3D():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_5B3D)
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
            "#3005F#12Pハ、ハルトマン議長！？\x02\x03",

            "#3007F一体どちらへ……\x01",
            "ど、どうか待ってくだされ！\x02",
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
        "マリアベル",
        (
            "#2904F#11Pフフ……\x01",
            "競売会もお流れですわね。\x02\x03",

            "#2902F少々アテは外れてしまったけど……\x01",
            "面白いものが見られたから\x01",
            "良しとしましょうか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("t101B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_5479 end

    def Function_45_5D2D(): pass

    label("Function_45_5D2D")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_5D41():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5D41)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_5D61():
        OP_9B(0x0, 0xFE, 0x0, 0x526C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5D61)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_45_5D2D end

    def Function_46_5D76(): pass

    label("Function_46_5D76")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_5D8A():
        OP_9B(0x0, 0xFE, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5D8A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_5DAA():
        OP_9B(0x0, 0xFE, 0x0, 0x526C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5DAA)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_46_5D76 end

    def Function_47_5DBF(): pass

    label("Function_47_5DBF")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_5DD3():
        OP_9B(0x0, 0xFE, 0x0, 0x15AE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5DD3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_5DF3():
        OP_9B(0x0, 0xFE, 0x0, 0x3520, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5DF3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_47_5DBF end

    def Function_48_5E08(): pass

    label("Function_48_5E08")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_5E1C():
        OP_9B(0x0, 0xFE, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5E1C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_5E3C():
        OP_9B(0x0, 0xFE, 0x0, 0x3520, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5E3C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_48_5E08 end

    def Function_49_5E51(): pass

    label("Function_49_5E51")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_5E65():
        OP_9B(0x0, 0xFE, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5E65)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_5E85():
        OP_9B(0x0, 0xFE, 0x0, 0x48A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5E85)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_49_5E51 end

    def Function_50_5E9A(): pass

    label("Function_50_5E9A")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_5EAE():
        OP_9B(0x0, 0xFE, 0x0, 0x15AE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5EAE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_5ECE():
        OP_9B(0x0, 0xFE, 0x0, 0x48A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5ECE)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_50_5E9A end

    def Function_51_5EE3(): pass

    label("Function_51_5EE3")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_5EF7():
        OP_9B(0x0, 0xFE, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5EF7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_5F17():
        OP_9B(0x0, 0xFE, 0x0, 0x48A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5F17)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_51_5EE3 end

    def Function_52_5F2C(): pass

    label("Function_52_5F2C")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_5F40():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5F40)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_5F60():
        OP_9B(0x0, 0xFE, 0x0, 0x48A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5F60)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_52_5F2C end

    def Function_53_5F75(): pass

    label("Function_53_5F75")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_5F89():
        OP_9B(0x0, 0xFE, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5F89)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_5FA9():
        OP_9B(0x0, 0xFE, 0x0, 0x2198, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5FA9)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_53_5F75 end

    def Function_54_5FBE(): pass

    label("Function_54_5FBE")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_5FD2():
        OP_9B(0x0, 0xFE, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5FD2)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_5FF2():
        OP_9B(0x0, 0xFE, 0x0, 0x3520, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5FF2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_54_5FBE end

    def Function_55_6007(): pass

    label("Function_55_6007")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_601B():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_601B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_603B():
        OP_9B(0x0, 0xFE, 0x0, 0x2B5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_603B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_55_6007 end

    def Function_56_6050(): pass

    label("Function_56_6050")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_6064():
        OP_9B(0x0, 0xFE, 0x0, 0x15AE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6064)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_6084():
        OP_9B(0x0, 0xFE, 0x0, 0x2B5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6084)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_56_6050 end

    def Function_57_6099(): pass

    label("Function_57_6099")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_60AD():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_60AD)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_60CD():
        OP_9B(0x0, 0xFE, 0x0, 0x3EE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_60CD)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_57_6099 end

    def Function_58_60E2(): pass

    label("Function_58_60E2")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_60F6():
        OP_9B(0x0, 0xFE, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_60F6)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_6116():
        OP_9B(0x0, 0xFE, 0x0, 0x3EE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6116)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_58_60E2 end

    def Function_59_612B(): pass

    label("Function_59_612B")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_613F():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_613F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_615F():
        OP_9B(0x0, 0xFE, 0x0, 0x2B5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_615F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_59_612B end

    def Function_60_6174(): pass

    label("Function_60_6174")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_6188():
        OP_9B(0x0, 0xFE, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6188)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_61A8():
        OP_9B(0x0, 0xFE, 0x0, 0x3EE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61A8)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_60_6174 end

    def Function_61_61BD(): pass

    label("Function_61_61BD")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_61D1():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61D1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_61F1():
        OP_9B(0x0, 0xFE, 0x0, 0x3EE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61F1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_61_61BD end

    def Function_62_6206(): pass

    label("Function_62_6206")

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

    # Function_62_6206 end

    SaveToFile()

Try(main)
