from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t4010.bin",                # FileName
        "t4010",                    # MapName
        "t4010",                    # Location
        0x0000,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1F,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 7, 0, 8],
    )

    BuildStringList((
        "t4010",                  # 0
        "シスター・マーブル",     # 1
        "エラルダ大司教",         # 2
        "シスター・リース",       # 3
        "ジーナス司祭",           # 4
        "レントン司祭",           # 5
        "シスター・ハティナ",     # 6
        "貿易商モルジオ",         # 7
        "シスター・ジュジュ",     # 8
        "レイテ",                 # 9
        "キーア",                 # 10
        "リュウ",                 # 11
        "アンリ",                 # 12
        "モモ",                   # 13
        "パンセ",                 # 14
        "タミル",                 # 15
        "ハミル",                 # 16
        "クータ",                 # 17
        "ユゴット",               # 18
        "男の子",                 # 19
        "男の子",                 # 20
        "女の子",                 # 21
        "女の子",                 # 22
        "プルーナ",               # 23
        "リナリー",               # 24
        "ブリック",               # 25
        "青年",                   # 26
        "娘",                     # 27
        "人形",                   # 28
    ))

    AddCharChip((
        "chr/ch25500.itc",                   # 00
        "chr/ch26500.itc",                   # 01
        "chr/ch14000.itc",                   # 02
        "chr/ch23802.itc",                   # 03
        "chr/ch25400.itc",                   # 04
        "chr/ch25300.itc",                   # 05
        "chr/ch21802.itc",                   # 06
        "chr/ch22202.itc",                   # 07
        "chr/ch20602.itc",                   # 08
        "chr/ch20702.itc",                   # 09
        "chr/ch22302.itc",                   # 0A
        "chr/ch21402.itc",                   # 0B
        "chr/ch34202.itc",                   # 0C
        "chr/ch20602.itc",                   # 0D
        "chr/ch23802.itc",                   # 0E
        "chr/ch21502.itc",                   # 0F
        "chr/ch23902.itc",                   # 10
        "chr/ch20502.itc",                   # 11
        "chr/ch22102.itc",                   # 12
        "chr/ch20402.itc",                   # 13
        "chr/ch22802.itc",                   # 14
        "chr/ch21302.itc",                   # 15
        "chr/ch08202.itc",                   # 16
        "chr/ch20500.itc",                   # 17
        "chr/ch22100.itc",                   # 18
        "chr/ch26502.itc",                   # 19
        "chr/ch21800.itc",                   # 1A
        "chr/ch10300.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(150800,  200,     17500,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-209,    379,     23229,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-2960,   250,     20010,   180,  257,  0x0, 0,   4,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(99300,   0,       5679,    225,  257,  0x0, 0,   5,   0,   0,   1,   0,   17,  255,  0)
    DeclNpc(2950,    189,     19709,   165,  257,  0x0, 0,   0,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-3849,   150,     6519,    0,    325,  0x0, 0,   26,  0,   255, 255, 0,   18,  255,  0)
    DeclNpc(0,       0,       0,       180,  385,  0x0, 0,   0,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(1059,    0,       11659,   0,    389,  0x0, 0,   27,  0,   0,   0,   0,   47,  255,  0)
    DeclNpc(153619,  150,     9130,    0,    453,  0x0, 0,   22,  0,   255, 255, 0,   28,  255,  0)
    DeclNpc(153619,  150,     12229,   0,    453,  0x0, 0,   8,   0,   255, 255, 0,   29,  255,  0)
    DeclNpc(154929,  150,     12229,   0,    453,  0x0, 0,   7,   0,   255, 255, 0,   30,  255,  0)
    DeclNpc(154929,  150,     9130,    0,    453,  0x0, 0,   9,   0,   255, 255, 0,   31,  255,  0)
    DeclNpc(148490,  150,     9130,    0,    453,  0x0, 0,   10,  0,   255, 255, 0,   32,  255,  0)
    DeclNpc(148490,  150,     12229,   45,   453,  0x0, 0,   3,   0,   255, 255, 0,   33,  255,  0)
    DeclNpc(147139,  150,     12229,   0,    453,  0x0, 0,   3,   0,   255, 255, 0,   34,  255,  0)
    DeclNpc(148490,  150,     12229,   0,    453,  0x0, 0,   11,  0,   255, 255, 0,   35,  255,  0)
    DeclNpc(147139,  150,     9130,    0,    453,  0x0, 0,   12,  0,   255, 255, 0,   36,  255,  0)
    DeclNpc(154929,  150,     12229,   0,    453,  0x0, 0,   13,  0,   255, 255, 0,   37,  255,  0)
    DeclNpc(153619,  150,     6150,    0,    453,  0x0, 0,   14,  0,   255, 255, 0,   38,  255,  0)
    DeclNpc(153619,  150,     9130,    0,    453,  0x0, 0,   15,  0,   255, 255, 0,   39,  255,  0)
    DeclNpc(148490,  150,     6150,    0,    453,  0x0, 0,   16,  0,   255, 255, 0,   40,  255,  0)
    DeclNpc(147139,  150,     12229,   0,    453,  0x0, 0,   23,  0,   255, 255, 0,   41,  255,  0)
    DeclNpc(148490,  150,     12229,   0,    453,  0x0, 0,   24,  0,   255, 255, 0,   43,  255,  0)
    DeclNpc(154929,  150,     12229,   0,    453,  0x0, 0,   19,  0,   255, 255, 0,   44,  255,  0)
    DeclNpc(148490,  150,     9130,    0,    453,  0x0, 0,   20,  0,   255, 255, 0,   45,  255,  0)
    DeclNpc(153619,  150,     9130,    0,    453,  0x0, 0,   21,  0,   255, 255, 0,   46,  255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(150910,  200,     16530,   1200,    150800,  1700,    17500,   0x007E, 0,  22, 0x0000)
    DeclActor(40,      500,     21930,   1200,    -210,    2100,    23230,   0x007E, 0,  9,  0x0000)
    DeclActor(50280,   0,       12800,   1200,    50160,   1000,    13560,   0x007C, 0,  48, 0x0000)

    ChipFrameInfo(1392, 0)                                       # 0

    ScpFunction((
        "Function_0_570",          # 00, 0
        "Function_1_620",          # 01, 1
        "Function_2_64B",          # 02, 2
        "Function_3_676",          # 03, 3
        "Function_4_6A1",          # 04, 4
        "Function_5_6CC",          # 05, 5
        "Function_6_6F7",          # 06, 6
        "Function_7_848",          # 07, 7
        "Function_8_F0D",          # 08, 8
        "Function_9_1118",         # 09, 9
        "Function_10_111C",        # 0A, 10
        "Function_11_2BCE",        # 0B, 11
        "Function_12_2CD2",        # 0C, 12
        "Function_13_307B",        # 0D, 13
        "Function_14_3195",        # 0E, 14
        "Function_15_3323",        # 0F, 15
        "Function_16_4617",        # 10, 16
        "Function_17_5A3D",        # 11, 17
        "Function_18_6A22",        # 12, 18
        "Function_19_801B",        # 13, 19
        "Function_20_8ABF",        # 14, 20
        "Function_21_8ED1",        # 15, 21
        "Function_22_90D6",        # 16, 22
        "Function_23_9105",        # 17, 23
        "Function_24_AE71",        # 18, 24
        "Function_25_B49E",        # 19, 25
        "Function_26_B608",        # 1A, 26
        "Function_27_BC37",        # 1B, 27
        "Function_28_BD3F",        # 1C, 28
        "Function_29_BDCC",        # 1D, 29
        "Function_30_BEEF",        # 1E, 30
        "Function_31_C000",        # 1F, 31
        "Function_32_C124",        # 20, 32
        "Function_33_C427",        # 21, 33
        "Function_34_C5FB",        # 22, 34
        "Function_35_C7A6",        # 23, 35
        "Function_36_C877",        # 24, 36
        "Function_37_C8EA",        # 25, 37
        "Function_38_C927",        # 26, 38
        "Function_39_C99A",        # 27, 39
        "Function_40_CAB0",        # 28, 40
        "Function_41_CB1A",        # 29, 41
        "Function_42_CBD4",        # 2A, 42
        "Function_43_CD03",        # 2B, 43
        "Function_44_CD73",        # 2C, 44
        "Function_45_CE58",        # 2D, 45
        "Function_46_CEAE",        # 2E, 46
        "Function_47_CFF7",        # 2F, 47
        "Function_48_D366",        # 30, 48
        "Function_49_D415",        # 31, 49
        "Function_50_D912",        # 32, 50
        "Function_51_DBE9",        # 33, 51
        "Function_52_EF84",        # 34, 52
        "Function_53_F804",        # 35, 53
        "Function_54_10D89",       # 36, 54
        "Function_55_10F9D",       # 37, 55
        "Function_56_112A4",       # 38, 56
        "Function_57_11E20",       # 39, 57
    ))


    def Function_0_570(): pass

    label("Function_0_570")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_5A8"),
        (1, "loc_5B4"),
        (2, "loc_5C0"),
        (3, "loc_5CC"),
        (4, "loc_5D8"),
        (5, "loc_5E4"),
        (6, "loc_5F0"),
        (SWITCH_DEFAULT, "loc_5FC"),
    )


    label("loc_5A8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5B4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5C0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5CC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5D8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5E4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5FC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_608")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_61F")

    Return()

    # Function_0_570 end

    def Function_1_620(): pass

    label("Function_1_620")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64A")
    OP_94(0xFE, 0x17A8E, 0x125C, 0x186A0, 0x1D4C, 0x3E8)
    Sleep(450)
    Jump("Function_1_620")

    label("loc_64A")

    Return()

    # Function_1_620 end

    def Function_2_64B(): pass

    label("Function_2_64B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_675")
    OP_94(0xFE, 0xFFFFF7F4, 0x1ACC, 0x8B6, 0x3D68, 0x3E8)
    Sleep(450)
    Jump("Function_2_64B")

    label("loc_675")

    Return()

    # Function_2_64B end

    def Function_3_676(): pass

    label("Function_3_676")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A0")
    OP_94(0xFE, 0xBA5E, 0x319C, 0xCD46, 0xC44, 0x3E8)
    Sleep(450)
    Jump("Function_3_676")

    label("loc_6A0")

    Return()

    # Function_3_676 end

    def Function_4_6A1(): pass

    label("Function_4_6A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6CB")
    OP_94(0xFE, 0xFFFFF7F4, 0x1ACC, 0x8B6, 0x3D68, 0x3E8)
    Sleep(450)
    Jump("Function_4_6A1")

    label("loc_6CB")

    Return()

    # Function_4_6A1 end

    def Function_5_6CC(): pass

    label("Function_5_6CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F6")
    OP_94(0xFE, 0x24A7C, 0x17DE, 0x25170, 0x34F8, 0x3E8)
    Sleep(450)
    Jump("Function_5_6CC")

    label("loc_6F6")

    Return()

    # Function_5_6CC end

    def Function_6_6F7(): pass

    label("Function_6_6F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_847")
    OP_95(0xFE, 48280, 0, 9200, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 5070, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 3530, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 1560, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 3530, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 5070, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 9200, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 10730, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    Jump("Function_6_6F7")

    label("loc_847")

    Return()

    # Function_6_6F7 end

    def Function_7_848(): pass

    label("Function_7_848")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_868")
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)

    label("loc_868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_876")
    Jump("loc_F0C")

    label("loc_876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8A0")
    ClearChrFlags(0xE, 0x40)
    SetChrPos(0xE, 160, 0, 10850, 0)
    BeginChrThread(0xE, 0, 0, 4)
    Jump("loc_F0C")

    label("loc_8A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8B3")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_F0C")

    label("loc_8B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_948")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DF")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -6960, 0, 20030, 135)

    label("loc_8DF")

    SetChrPos(0x8, 8480, 0, 19550, 225)
    SetChrPos(0x16, 5350, 150, 11500, 0)
    SetChrPos(0x17, 6400, 150, 11500, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x16, 0x3)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    SetChrChipByIndex(0x17, 0x3)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x10)
    Jump("loc_F0C")

    label("loc_948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_956")
    Jump("loc_F0C")

    label("loc_956")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9A1")
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 48280, 0, 10730, 180)
    BeginChrThread(0xF, 0, 0, 6)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 151520, 0, 9530, 0)
    BeginChrThread(0xA, 0, 0, 5)
    Jump("loc_F0C")

    label("loc_9A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9CB")
    SetChrFlags(0xD, 0x80)
    SetChrPos(0xC, 95850, 0, 8119, 270)
    BeginChrThread(0xC, 0, 0, 0)
    Jump("loc_F0C")

    label("loc_9CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9EC")
    SetChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9E7")
    SetChrFlags(0xE, 0x10)

    label("loc_9E7")

    Jump("loc_F0C")

    label("loc_9EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_AD0")
    SetChrPos(0x9, 100000, 150, 10600, 180)
    SetChrChipByIndex(0x9, 0x19)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0xC, 160, 0, 10850, 0)
    BeginChrThread(0xC, 0, 0, 4)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x8, 150800, 200, 17500, 90)
    SetChrPos(0xF, 153000, 200, 17650, 270)
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A69")
    SetChrFlags(0xF, 0x10)

    label("loc_A69")

    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrChipByIndex(0x20, 0x13)
    SetChrSubChip(0x20, 0x0)
    EndChrThread(0x20, 0x0)
    SetChrBattleFlags(0x20, 0x4)
    SetChrPos(0x1E, 155440, 0, 3630, 270)
    SetChrPos(0x1F, 153430, 0, 3820, 90)
    BeginChrThread(0x1E, 0, 0, 0)
    BeginChrThread(0x1F, 0, 0, 0)
    SetChrFlags(0x1E, 0x10)
    SetChrFlags(0x1F, 0x10)
    ClearChrFlags(0x1E, 0x40)
    ClearChrFlags(0x1F, 0x40)
    Jump("loc_F0C")

    label("loc_AD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_BAB")
    SetChrPos(0x9, 97640, 0, 12650, 0)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xC, 160, 0, 10850, 0)
    BeginChrThread(0xC, 0, 0, 4)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 153790, 200, 17470, 180)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrChipByIndex(0x1E, 0x11)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    SetChrChipByIndex(0x1F, 0x12)
    SetChrSubChip(0x1F, 0x0)
    EndChrThread(0x1F, 0x0)
    SetChrBattleFlags(0x1F, 0x4)
    SetChrChipByIndex(0x20, 0x13)
    SetChrSubChip(0x20, 0x0)
    EndChrThread(0x20, 0x0)
    SetChrBattleFlags(0x20, 0x4)
    SetChrChipByIndex(0x21, 0x14)
    SetChrSubChip(0x21, 0x0)
    EndChrThread(0x21, 0x0)
    SetChrBattleFlags(0x21, 0x4)
    SetChrChipByIndex(0x22, 0x15)
    SetChrSubChip(0x22, 0x0)
    EndChrThread(0x22, 0x0)
    SetChrBattleFlags(0x22, 0x4)
    SetChrFlags(0x1E, 0x10)
    SetChrFlags(0x1F, 0x10)
    SetChrFlags(0x20, 0x10)
    SetChrSubChip(0x1E, 0x2)
    SetChrSubChip(0x1F, 0x1)
    Jump("loc_F0C")

    label("loc_BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CA0")
    SetChrPos(0xC, 49920, 0, 9850, 359)
    BeginChrThread(0xC, 0, 0, 3)
    SetChrPos(0x9, 97640, 0, 12650, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEB")
    SetChrFlags(0x9, 0x10)

    label("loc_BEB")

    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 150800, 200, 17500, 180)
    SetChrPos(0x8, 153790, 200, 17470, 180)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x18, 0xB)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    SetChrChipByIndex(0x19, 0xC)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrChipByIndex(0x1A, 0xD)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    SetChrChipByIndex(0x1B, 0xE)
    SetChrSubChip(0x1B, 0x0)
    EndChrThread(0x1B, 0x0)
    SetChrBattleFlags(0x1B, 0x4)
    SetChrChipByIndex(0x1C, 0xF)
    SetChrSubChip(0x1C, 0x0)
    EndChrThread(0x1C, 0x0)
    SetChrBattleFlags(0x1C, 0x4)
    SetChrChipByIndex(0x1D, 0x10)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    Jump("loc_F0C")

    label("loc_CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_CEB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CE6")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0x8, 150800, 200, 17500, 90)
    SetChrPos(0xA, 153000, 200, 17650, 270)

    label("loc_CE6")

    Jump("loc_F0C")

    label("loc_CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D25")
    SetChrPos(0xD, 2330, 500, 22880, 270)
    OP_93(0x9, 0x5A, 0x0)
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D20")
    SetChrFlags(0xD, 0x10)

    label("loc_D20")

    Jump("loc_F0C")

    label("loc_D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D33")
    Jump("loc_F0C")

    label("loc_D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_DDB")
    SetChrPos(0xD, 2330, 500, 22880, 270)
    OP_93(0x9, 0x5A, 0x0)
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D68")
    SetChrFlags(0xD, 0x10)

    label("loc_D68")

    SetChrPos(0xB, 160, 0, 10850, 0)
    BeginChrThread(0xB, 0, 0, 4)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -1000, 0, 7830, 270)
    BeginChrThread(0xF, 0, 0, 4)
    SetChrPos(0x8, 150800, 200, 17500, 90)
    SetChrPos(0xA, 153000, 200, 17650, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD1")
    SetChrFlags(0x8, 0x10)

    label("loc_DD1")

    SetChrFlags(0xA, 0x10)
    Jump("loc_F0C")

    label("loc_DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_DF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF3")
    SetChrFlags(0x9, 0x10)

    label("loc_DF3")

    Jump("loc_F0C")

    label("loc_DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_E55")
    SetChrPos(0x9, 100000, 150, 10610, 180)
    SetChrChipByIndex(0x9, 0x19)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 100000, 0, 7200, 0)
    SetChrPos(0xC, 50430, 0, 4030, 0)
    BeginChrThread(0xC, 0, 0, 3)
    Jump("loc_F0C")

    label("loc_E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_F0C")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x11, 0x16)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    SetChrChipByIndex(0x12, 0x8)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrChipByIndex(0x13, 0x7)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    SetChrChipByIndex(0x14, 0x9)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrChipByIndex(0x15, 0xA)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrChipByIndex(0x16, 0x3)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    SetChrChipByIndex(0x17, 0x3)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F07")
    SetChrFlags(0x13, 0x10)

    label("loc_F07")

    SetChrFlags(0x14, 0x10)

    label("loc_F0C")

    Return()

    # Function_7_848 end

    def Function_8_F0D(): pass

    label("Function_8_F0D")

    OP_65(0x2, 0x1)
    SetMapObjFlags(0x2, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F2F")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F3D")
    Jump("loc_1036")

    label("loc_F3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_F4B")
    Jump("loc_1036")

    label("loc_F4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_F59")
    Jump("loc_1036")

    label("loc_F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F67")
    Jump("loc_1036")

    label("loc_F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F75")
    Jump("loc_1036")

    label("loc_F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F83")
    Jump("loc_1036")

    label("loc_F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F91")
    Jump("loc_1036")

    label("loc_F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F9F")
    Jump("loc_1036")

    label("loc_F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_FB1")
    OP_65(0x1, 0x1)
    Jump("loc_1036")

    label("loc_FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_FC3")
    OP_65(0x1, 0x1)
    Jump("loc_1036")

    label("loc_FC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_FD5")
    OP_65(0x1, 0x1)
    Jump("loc_1036")

    label("loc_FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_FE3")
    Jump("loc_1036")

    label("loc_FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_FF1")
    Jump("loc_1036")

    label("loc_FF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_FFF")
    Jump("loc_1036")

    label("loc_FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_100D")
    Jump("loc_1036")

    label("loc_100D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_101B")
    Jump("loc_1036")

    label("loc_101B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_102D")
    OP_65(0x1, 0x1)
    Jump("loc_1036")

    label("loc_102D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1036")

    label("loc_1036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1048")
    OP_65(0x0, 0x1)

    label("loc_1048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1064")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_107B")

    label("loc_1064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_107B")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_107B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10CD")
    SetMapObjFrame(0xFF, "hikari00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "obj_18", 0x0, 0x1)
    SetMapObjFrame(0xFF, "obj_27", 0x0, 0x1)
    Sound(128, 1, 50, 0)
    Jump("loc_10DE")

    label("loc_10CD")

    SetMapObjFrame(0xFF, "cloudwind", 0x0, 0x1)

    label("loc_10DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F1")
    OP_1B(0x2, 0x0, 0x33)

    label("loc_10F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1104")
    OP_1B(0x2, 0x0, 0x34)

    label("loc_1104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1117")
    OP_1B(0x4, 0x0, 0x35)

    label("loc_1117")

    Return()

    # Function_8_F0D end

    def Function_9_1118(): pass

    label("Function_9_1118")

    Call(0, 10)
    Return()

    # Function_9_1118 end

    def Function_10_111C(): pass

    label("Function_10_111C")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_13EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1152")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_114A")
    Call(0, 12)
    Jump("loc_114D")

    label("loc_114A")

    Call(0, 11)

    label("loc_114D")

    Jump("loc_13EA")

    label("loc_1152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_133F")

    #C0001
    ChrTalk(
        0x9,
        (
            "湿地帯に現れた《大樹》……\x01",
            "あのようなものは七耀教会の\x01",
            "どの聖典にも伝わっておらん。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x9,
        (
            "もはや世俗の者の手でどうにかなる\x01",
            "類のものではないのかもしれぬ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1306")

    #C0003
    ChrTalk(
        0x105,
        (
            "#10400Fまあ、ひとまず僕たちに\x01",
            "任せてもらおうかな。\x02\x03",

            "#10404F事態が解決した暁には、\x01",
            "是非とも今後の協力を\x01",
            "お願いしたいところだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            "……前向きに考えさせてもらおう。\x01",
            "それがクロスベルのためならばな。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x9,
        "おぬしらに、女神の加護があらんことを。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1337")

    label("loc_1306")


    #C0006
    ChrTalk(
        0x9,
        (
            "……おぬしらに、\x01",
            "女神の加護があらんことを。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1337")

    SetScenarioFlags(0x0, 0)
    Jump("loc_13EA")

    label("loc_133F")


    #C0007
    ChrTalk(
        0x9,
        (
            "あの《大樹》は、七耀教会の\x01",
            "どの聖典にも伝わっておらん。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "もはや世俗の者の手でどうにかなる\x01",
            "類のものではないのかもしれぬが……\x01",
            "女神の加護を祈らせてもらうとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13EA")

    Jump("loc_2BCA")

    label("loc_13EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_15B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1422")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_141A")
    Call(0, 12)
    Jump("loc_141D")

    label("loc_141A")

    Call(0, 11)

    label("loc_141D")

    Jump("loc_15B4")

    label("loc_1422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_151E")

    #C0009
    ChrTalk(
        0x9,
        (
            "今回のクロスベルの事態……\x01",
            "《封聖省》の介入を拒み続けた\x01",
            "この私にも一因があろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x9,
        (
            "もし彼らを受け入れてさえいれば、\x01",
            "ここまでの事態には\x01",
            "ならなかったのかもしれん。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x9,
        (
            "私も、頭を冷やして\x01",
            "自分を見つめなおす時間が\x01",
            "必要なようだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15B4")

    label("loc_151E")


    #C0012
    ChrTalk(
        0x9,
        (
            "もし《封聖省》を受け入れていれば、\x01",
            "ここまでの事態には\x01",
            "ならなかったのかもしれん。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        (
            "私も、頭を冷やして\x01",
            "自分を見つめなおす時間が\x01",
            "必要なようだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15B4")

    Jump("loc_2BCA")

    label("loc_15B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_17A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16F6")

    #C0014
    ChrTalk(
        0x9,
        (
            "シスター・リースが\x01",
            "アルテリア総本山に戻ったか……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x9,
        (
            "……クロスベルへの介入に、\x01",
            "封聖省も本格的に動き出したようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "このクロスベルが動乱の時代へと\x01",
            "突入しようとしている……\x01",
            "その予兆なのかもしれぬ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        (
            "私もクロスベル教区の長として、\x01",
            "今後の身の振り方を\x01",
            "考えねばならんようだな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_179E")

    label("loc_16F6")


    #C0018
    ChrTalk(
        0x9,
        (
            "封聖省も本格的に動き出し、\x01",
            "このクロスベルが動乱の時代へと\x01",
            "突入しようとしている。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        (
            "私もクロスベル教区の長として、\x01",
            "今後の身の振り方を\x01",
            "考えねばならんようだな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179E")

    Jump("loc_2BCA")

    label("loc_17A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1981")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18CC")

    #C0020
    ChrTalk(
        0x9,
        (
            "……少し前に、典礼省からの\x01",
            "情報が届いてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        (
            "封聖省のクロスベル介入を\x01",
            "法王御自らがお認めになりそうだという。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x9,
        (
            "襲撃事件などが起こっている\x01",
            "今の状況では仕方ないのかもしれん……\x02",
        )
    )


    #C0023
    ChrTalk(
        0x9,
        (
            "だが、それでも……\x01",
            "非合法的活動を行う彼らを、\x01",
            "私は認めることはできないのだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_197C")

    label("loc_18CC")


    #C0024
    ChrTalk(
        0x9,
        (
            "封聖省のクロスベル介入を\x01",
            "法王御自らがお認めになりそうだという\x01",
            "情報が入ってはいるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        (
            "だが、それでも……\x01",
            "非合法的活動を行う彼らを、\x01",
            "私は認めることはできないのだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_197C")

    Jump("loc_2BCA")

    label("loc_1981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1A9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A3C")

    #C0026
    ChrTalk(
        0x9,
        (
            "今もなお、マインツ山道では\x01",
            "多くの警備隊員が危険に晒されている。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        (
            "大いなる空の女神よ、\x01",
            "どうか彼らにご加護を……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x9,
        "そして邪悪なるものを退けたまえ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A97")

    label("loc_1A3C")


    #C0029
    ChrTalk(
        0x9,
        (
            "大いなる空の女神よ、\x01",
            "どうか彼らにご加護を……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x9,
        "そして邪悪なるものを退けたまえ……\x02",
    )

    CloseMessageWindow()

    label("loc_1A97")

    Jump("loc_2BCA")

    label("loc_1A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1BC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B4D")

    #C0031
    ChrTalk(
        0x9,
        (
            "先ほど遊撃士が聞き込みに来たが、\x01",
            "エオリア君たちが行方不明だそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x9,
        (
            "残念ながら大聖堂には来ていないのだ。\x01",
            "ふむ、無事でいるといいのだが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BBF")

    label("loc_1B4D")


    #C0033
    ChrTalk(
        0x9,
        (
            "エオリア君たちには、\x01",
            "薬の材料調達や司祭の護衛など、\x01",
            "色々と世話になっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x9,
        "無事でいるといいのだが……\x02",
    )

    CloseMessageWindow()

    label("loc_1BBF")

    Jump("loc_2BCA")

    label("loc_1BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1C65")

    #C0035
    ChrTalk(
        0x9,
        (
            "さて……\x01",
            "次のミサの日程を詰めなければな。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x9,
        (
            "先の教団事件から事件続きだ……\x01",
            "市民たちにはミサに参加してもらい、\x01",
            "心を安らかにしてもらわねば。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BCA")

    label("loc_1C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1DA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D21")

    #C0037
    ChrTalk(
        0x9,
        (
            "……昨日の花の件、\x01",
            "まだ嗅ぎまわっているのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x9,
        (
            "この広い大陸には、\x01",
            "触れない方がいい世界が\x01",
            "往々にして存在するのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x9,
        "……あまり深入りせぬことだな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D9C")

    label("loc_1D21")


    #C0040
    ChrTalk(
        0x9,
        (
            "この広い大陸には、\x01",
            "触れない方がいい世界が\x01",
            "往々にして存在するのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x9,
        (
            "あまり深入りせぬよう、\x01",
            "肝に銘じておくのだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D9C")

    Jump("loc_2BCA")

    label("loc_1DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_202E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F54")

    #C0042
    ChrTalk(
        0x9,
        (
            "この花について私から\x01",
            "話せることはなにもない。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            "教会にいる他の人間……\x01",
            "例えばシスター・マーブルでも\x01",
            "その存在は知らないはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "さあ、お引取り願おう。\x01",
            "私も何かと忙しい身なのでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#00003F（やっぱり、大司教は\x01",
            "  教えてくれそうにないな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        (
            "#00100F（リースさんが話があるって\x01",
            "  言っていたし……\x01",
            "  一旦そっちに行ってみましょう。）\x02\x03",

            "（彼女は礼拝堂を出てすぐの\x01",
            "  寄宿舎で待っているはずよ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2029")

    label("loc_1F54")


    #C0047
    ChrTalk(
        0x9,
        (
            "この花について私から\x01",
            "話せることはなにもない。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x9,
        (
            "さあ、お引取り願おう。\x01",
            "私も何かと忙しい身なのでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#00000F（リースさんが礼拝堂を出てすぐの\x01",
            "  寄宿舎で待っているはずだ……\x01",
            "  とにかく、行ってみよう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2029")

    Jump("loc_2BCA")

    label("loc_202E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_2122")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20EE")

    #C0050
    ChrTalk(
        0x9,
        (
            "リース・アルジェント……\x01",
            "やはり、彼女の妹で間違いないだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "ふん……あの連中め。\x01",
            "一体何を企んでいる……？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#00003F（何か考え事をしてるみたいだ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_211D")

    label("loc_20EE")


    #C0053
    ChrTalk(
        0x9,
        (
            "……あの連中め。\x01",
            "一体何を企んでいる……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_211D")

    Jump("loc_2BCA")

    label("loc_2122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2289")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2223")

    #C0054
    ChrTalk(
        0x9,
        (
            "通商会議の本会議当日……\x01",
            "シスター・リースのマインツへの出張が\x01",
            "やけに時間がかかっていた。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "そして、マインツ方面には\x01",
            "例の遺跡があったはず……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "……なるほどな。\x01",
            "何をしていたか知らんが……\x01",
            "やはり、間違いなさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_2284")

    label("loc_2223")


    #C0057
    ChrTalk(
        0x9,
        "……おや、何の用だね。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x9,
        (
            "今は調べものをしているのだ。\x01",
            "軽々しく部屋に入らないでもらおう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2284")

    Jump("loc_2BCA")

    label("loc_2289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2579")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2438")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22C5")
    Call(0, 57)
    Return()

    label("loc_22C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C1")

    #C0059
    ChrTalk(
        0x9,
        (
            "怪盗Ｂ……まさか神聖なる\x01",
            "クロスベル大聖堂に盗品を隠すとは。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "話くらいは聞いていたが\x01",
            "相当な不届き者のようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "大いなる女神の僕#2Rしもべ#として、\x01",
            "かようなものを許してはおけん。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "諸君、何としても\x01",
            "捕まえてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2434")

    label("loc_23C1")


    #C0063
    ChrTalk(
        0x9,
        (
            "怪盗Ｂ……\x01",
            "大いなる女神の僕として、\x01",
            "かようなものを許してはおけん。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        (
            "諸君、何としても\x01",
            "捕まえてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2434")

    TalkEnd(0x9)
    Return()

    label("loc_2438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24F3")

    #C0065
    ChrTalk(
        0x9,
        (
            "クローディア王太女が先ほど\x01",
            "挨拶にいらっしゃったのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "若くしてなかなか洗練された\x01",
            "考えをお持ちのようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "リベール王国の未来は\x01",
            "明るいと言えるだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2574")

    label("loc_24F3")


    #C0068
    ChrTalk(
        0x9,
        (
            "クローディア王太女は、\x01",
            "若くしてなかなか洗練された\x01",
            "考えをお持ちのようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "リベール王国の未来は\x01",
            "明るいと言えるだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2574")

    Jump("loc_2BCA")

    label("loc_2579")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2623")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2594")
    Call(0, 14)
    Jump("loc_261E")

    label("loc_2594")

    OP_4B(0xD, 0xFF)

    #C0070
    ChrTalk(
        0x9,
        (
            "マインツ方面への出張か……\x01",
            "多少気になるが、いいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "彼女に関しては\x01",
            "また何かあったら報告したまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xD,
        "は、はい……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)

    label("loc_261E")

    Jump("loc_2BCA")

    label("loc_2623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_27B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2716")

    #C0073
    ChrTalk(
        0x9,
        (
            "ウルスラ病院のラゴー教授から\x01",
            "手紙が届いたのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "以前渡した、ルピナス草という\x01",
            "薬草を用いた研究に成果が出た……\x01",
            "などと書かれていたようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "……私の知る所ではないのだが、\x01",
            "よくやったとだけ言っておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_27AB")

    label("loc_2716")


    #C0076
    ChrTalk(
        0x9,
        (
            "ウルスラ病院のラゴー教授から、\x01",
            "以前協力した研究についての\x01",
            "報告が届いたのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "……私の知る所ではないのだが、\x01",
            "よくやったとだけ言っておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27AB")

    Jump("loc_2BCA")

    label("loc_27B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_286D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27CB")
    Call(0, 13)
    Jump("loc_2868")

    label("loc_27CB")

    OP_4B(0xD, 0xFF)

    #C0078
    ChrTalk(
        0x9,
        (
            "リース・アルジェントか……\x01",
            "まあよかろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "シスター・ハティナ。\x01",
            "彼女にしっかりと仕事を\x01",
            "教えてやってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xD,
        "ええ、お任せください。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)

    label("loc_2868")

    Jump("loc_2BCA")

    label("loc_286D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_2A60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29AE")

    #C0081
    ChrTalk(
        0x9,
        (
            "……リース・アルジェント……\x01",
            "あの娘は……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    #C0082
    ChrTalk(
        0x153,
        "#01111Fだいしきょーさん、どうしたのー？\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x105,
        (
            "#10300Fリースっていうのは\x01",
            "さっきのシスターさんだよね。\x02\x03",

            "#10304Fフフ、何か気になる事でもあるのかな？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 500)

    #C0084
    ChrTalk(
        0x9,
        (
            "……君たちには関係のない話だ。\x01",
            "気にしないでくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_2A5B")

    label("loc_29AE")


    #C0085
    ChrTalk(
        0x9,
        (
            "……リース・アルジェント……\x01",
            "あの娘は……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x153,
        (
            "#01100Fおなかイタいのなら言ってね。\x01",
            "キーア、救急箱とってくるからー！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x153, 500)

    #C0087
    ChrTalk(
        0x9,
        (
            "う、うむ。\x01",
            "……気にしないでくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A5B")

    Jump("loc_2BCA")

    label("loc_2A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_2A6E")
    Jump("loc_2BCA")

    label("loc_2A6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2BCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B43")

    #C0088
    ChrTalk(
        0x9,
        (
            "このクロスベル大聖堂に\x01",
            "よくぞいらっしゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "敬虔な心を以って救いを求めし者に、\x01",
            "空の女神#8Rエ　イ　ド　ス#は必ず手を差し伸べるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        "君たちに女神の導きがあらん事を……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2BCA")

    label("loc_2B43")


    #C0091
    ChrTalk(
        0x9,
        (
            "敬虔な心を以って救いを求めし者に、\x01",
            "空の女神#8Rエ　イ　ド　ス#は必ず手を差し伸べるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x9,
        "君たちに女神の導きがあらん事を……\x02",
    )

    CloseMessageWindow()

    label("loc_2BCA")

    TalkEnd(0x9)
    Return()

    # Function_10_111C end

    def Function_11_2BCE(): pass

    label("Function_11_2BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C76")

    #C0093
    ChrTalk(
        0x9,
        (
            "……まさかここまでの事態を\x01",
            "引き起こしてしまうとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "これも“彼ら”の介入を拒んだ\x01",
            "私の責任なのかも知れぬ……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        "………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2CD1")

    label("loc_2C76")


    #C0096
    ChrTalk(
        0x9,
        (
            "これも“彼ら”の介入を拒んだ\x01",
            "私の責任なのかも知れぬ……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        "………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_2CD1")

    Return()

    # Function_11_2BCE end

    def Function_12_2CD2(): pass

    label("Function_12_2CD2")

    TurnDirection(0x9, 0x105, 0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0098
    ChrTalk(
        0x9,
        "おぬしは……\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x105,
        (
            "#10400Fやあ、エラルダ大司教。\x01",
            "お久しぶりだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "……そういうことか。\x01",
            "ワジ・ヘミスフィア、\x01",
            "おぬしはやはり……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "シスター・リースを隠れ蓑に、\x01",
            "この私の目をまんまと\x01",
            "誤魔化したというわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        "……《封聖省》の考えそうなことだ。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x105,
        (
            "#10404Fフフ、その件に関しては\x01",
            "改めて謝罪させていただくよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "……今回の件に関しては、\x01",
            "頑なにおぬしらの介入を拒み続けた\x01",
            "この私にも一因があろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "糾弾こそすれ、謝罪などを\x01",
            "される義理はないはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x102,
        "#00108F大司教さま……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x104,
        "#00306F相変わらず厳しいお人だなあ。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x105,
        (
            "#10404Fまあ、あなたの立場を考えると\x01",
            "詮無いことだとは思うけどね。\x02\x03",

            "#10400Fフフ、今後は僕たちの活動に\x01",
            "少しだけ目を瞑ってくれるように\x01",
            "してくれると嬉しいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        "#00011Fお、おいおいワジ……\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        "#00211F要求が露骨すぎです。\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "……二つ返事で答えることはできぬ。\x01",
            "だが、改めて検討はさせてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        (
            "この私も、頭を冷やして\x01",
            "自分を見つめなおす時間が\x01",
            "必要なようだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 1)
    Return()

    # Function_12_2CD2 end

    def Function_13_307B(): pass

    label("Function_13_307B")

    OP_4B(0x9, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0113
    ChrTalk(
        0x9,
        (
            "……彼女はシスター・マーブルの\x01",
            "手伝いをしているようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xD,
        "シスター・リースですか？\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xD,
        (
            "ええ、彼女はとても\x01",
            "仕事を覚えるのが早くて……\x01",
            "私たちも随分助けられています。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        "ふむ、そうか……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        "（……まあ、よかろう。）\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0x9, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_13_307B end

    def Function_14_3195(): pass

    label("Function_14_3195")

    OP_4B(0x9, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0118
    ChrTalk(
        0x9,
        (
            "ふむ……\x01",
            "シスター・リースに\x01",
            "明日の出張を任せたと？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xD,
        (
            "ええ、日曜学校の授業も\x01",
            "初めてではないそうですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xD,
        (
            "……あの、大司教様。\x01",
            "シスター・リースが何か……？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xD,
        (
            "この間からとても気にして\x01",
            "いらっしゃるようですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x9,
        (
            "……いや、大したことではない。\x01",
            "少しばかり、仕事ぶりが\x01",
            "気になっていてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "彼女に関しては\x01",
            "また何かあったら報告したまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xD,
        "は、はい……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    OP_4C(0x9, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_14_3195 end

    def Function_15_3323(): pass

    label("Function_15_3323")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_345D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33E6")

    #C0125
    ChrTalk(
        0xFE,
        (
            "大統領が拘束されたとはいえ、\x01",
            "クロスベルを取り巻く状況は\x01",
            "決して楽観視できないでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "この地が再び戦火に巻き込まれる日は\x01",
            "そう遠くないのかもしれません……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3458")

    label("loc_33E6")


    #C0127
    ChrTalk(
        0xFE,
        (
            "このクロスベルが\x01",
            "再び戦火に巻き込まれる日は、\x01",
            "そう遠くないのかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        "祈りましょう、女神様に……\x02",
    )

    CloseMessageWindow()

    label("loc_3458")

    Jump("loc_4613")

    label("loc_345D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_35C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_353C")

    #C0129
    ChrTalk(
        0xFE,
        (
            "大司教はこの事態に\x01",
            "少なからず責任を\x01",
            "感じているご様子です。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "ご自分に対しても\x01",
            "厳格な方ですから、\x01",
            "無理もありませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "なればこそ、私たちを\x01",
            "今までどおり導いて\x01",
            "いただきたく思います。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_35BE")

    label("loc_353C")


    #C0132
    ChrTalk(
        0xFE,
        (
            "大司教はこの事態に\x01",
            "少なからず責任を感じている\x01",
            "ご様子ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "それでも私たちは、\x01",
            "エラルダ大司教に\x01",
            "ついていく所存です。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35BE")

    Jump("loc_4613")

    label("loc_35C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3753")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36BC")

    #C0134
    ChrTalk(
        0xFE,
        (
            "クロスベルの国家独立は、\x01",
            "周辺諸国にも大きな波紋を\x01",
            "広げるはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "特に、２大国からは\x01",
            "これからさらに強い圧力が\x01",
            "かかってくるはず……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "私たちクロスベルの住民は、\x01",
            "それを乗り切っていくことが\x01",
            "できるのでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_374E")

    label("loc_36BC")


    #C0137
    ChrTalk(
        0xFE,
        (
            "これから、２大国から\x01",
            "さらに強い圧力が\x01",
            "かかってくるはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "私たちクロスベルの住民は、\x01",
            "それを乗り切っていくことが\x01",
            "できるのでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_374E")

    Jump("loc_4613")

    label("loc_3753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_38C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3836")

    #C0139
    ChrTalk(
        0xFE,
        (
            "先の襲撃事件では、\x01",
            "警備隊や一般市民に\x01",
            "多くの被害が出ました。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "再び同じような事件を\x01",
            "起こさせない為に、\x01",
            "どうすればいいか……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "クロスベルの住民が\x01",
            "皆で考えていかなければ\x01",
            "ならないでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38BC")

    label("loc_3836")


    #C0142
    ChrTalk(
        0xFE,
        (
            "再び同じような事件を\x01",
            "起こさせない為に、\x01",
            "どうすればいいか……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "クロスベルの住民が\x01",
            "皆で考えていかなければ\x01",
            "ならないでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38BC")

    Jump("loc_4613")

    label("loc_38C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_394A")

    #C0144
    ChrTalk(
        0xFE,
        (
            "マインツの住民が\x01",
            "一体何をしたというのでしょう……\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "このような所業……\x01",
            "女神は絶対にお許しに\x01",
            "なるはずがありません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4613")

    label("loc_394A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_39CE")

    #C0146
    ChrTalk(
        0xFE,
        (
            "昨日起きた西クロスベル街道での\x01",
            "脱線事故は、酷い有様だったとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "死者が出なかったのは\x01",
            "不幸中の幸いでしたね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4613")

    label("loc_39CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A99")

    #C0148
    ChrTalk(
        0xFE,
        (
            "どんなときでも正しくあろうとする……\x01",
            "それは並大抵のことではありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "他人にだけでなく、自らを厳しく\x01",
            "律することができるエラルダ大司教は、\x01",
            "私にとってもっとも尊敬すべき人物です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4613")

    label("loc_3A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3B3C")

    #C0150
    ChrTalk(
        0xFE,
        (
            "大司教は七耀教会の戒律に\x01",
            "とても厳格であらせられます。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "頑固者と仰る方もおられますが、\x01",
            "私はむしろ大司教のそんなところを\x01",
            "尊敬しているのです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4613")

    label("loc_3B3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_3BBF")

    #C0152
    ChrTalk(
        0xFE,
        (
            "おや、大司教とはもう\x01",
            "話されたのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "ふむ……\x01",
            "随分早く切り上げたようですが、\x01",
            "なにかあったのでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4613")

    label("loc_3BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_3C57")

    #C0154
    ChrTalk(
        0xFE,
        (
            "近頃、クロスベル各地に\x01",
            "謎の化物が目撃されているのだとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "警備隊からも通達がありましたし、\x01",
            "注意を呼びかけていきたいところです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4613")

    label("loc_3C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D1E")

    #C0156
    ChrTalk(
        0xFE,
        (
            "大司教なら、現在は執務室に\x01",
            "こもっておられます。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "なんでも、リースさんの\x01",
            "ここ最近の行動を\x01",
            "調べている様子で……\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "大司教とリースさん……\x01",
            "何かあったのでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D55")

    label("loc_3D1E")


    #C0159
    ChrTalk(
        0xFE,
        (
            "大司教なら、現在は執務室に\x01",
            "こもっておられますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D55")

    Jump("loc_4613")

    label("loc_3D5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3EBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E38")

    #C0160
    ChrTalk(
        0xFE,
        (
            "なんでもクローディア殿下は、\x01",
            "剣のたしなみがあるそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "ユリア准佐に直伝されたそうで、\x01",
            "なかなかの腕をお持ちなのだとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "こう言ってはなんですが、\x01",
            "人は見かけによらないものですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3EB6")

    label("loc_3E38")


    #C0163
    ChrTalk(
        0xFE,
        (
            "なんでもクローディア殿下は、\x01",
            "剣のたしなみがあるそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "こう言ってはなんですが、\x01",
            "人は見かけによらないものですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EB6")

    Jump("loc_4613")

    label("loc_3EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4033")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FA5")

    #C0165
    ChrTalk(
        0xFE,
        (
            "通商会議の行方は\x01",
            "私も気になるところです。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "各国の首脳たちは、\x01",
            "それぞれが名高い識者で\x01",
            "いらっしゃいますし……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "どのような取り決めがされるのか、\x01",
            "クロスベルの住民として\x01",
            "見逃すわけにはいきませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_402E")

    label("loc_3FA5")


    #C0168
    ChrTalk(
        0xFE,
        (
            "通商会議の行方は\x01",
            "私も気になるところです。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "どのような取り決めがされるのか、\x01",
            "クロスベルの住民として\x01",
            "見逃すわけにはいきませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_402E")

    Jump("loc_4613")

    label("loc_4033")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_418C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_411F")

    #C0170
    ChrTalk(
        0xFE,
        (
            "大司教とラゴー教授には\x01",
            "強い確執があったのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "最近はそれも少し和らいで、\x01",
            "教授の手紙くらいは\x01",
            "読んで頂けるようになりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "読まずに捨てていた頃よりは\x01",
            "かなり関係も改善された\x01",
            "みたいですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4187")

    label("loc_411F")


    #C0173
    ChrTalk(
        0xFE,
        (
            "もとはラゴー教授も\x01",
            "大司教の下で学んだ司祭……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "その内、お２人の確執が\x01",
            "無くなるといいのですが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4187")

    Jump("loc_4613")

    label("loc_418C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4229")

    #C0175
    ChrTalk(
        0xFE,
        (
            "今日は手の空いている者で\x01",
            "大聖堂の掃除をしているのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "なにぶん古い建物ですから……\x01",
            "定期的に掃除をしないと\x01",
            "痛んでしまいますからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4613")

    label("loc_4229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_43CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_431E")

    #C0177
    ChrTalk(
        0xFE,
        (
            "年長クラスの授業は、\x01",
            "年少クラスよりも格段に\x01",
            "難しくなってくるはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "キーアちゃんの理解力は\x01",
            "素晴らしいものがありますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x153,
        (
            "#01109Fえへへ……\x01",
            "褒められちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        "#00000Fはは、なんだか俺も鼻が高いよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43C6")

    label("loc_431E")


    #C0181
    ChrTalk(
        0xFE,
        (
            "キーアちゃんは、ともすれば\x01",
            "大人でも考えてしまうような問題も\x01",
            "サラリと解いてしまうとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "授業を見ていなくても、\x01",
            "その話を聞くだけで\x01",
            "すごさが伝わってきますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43C6")

    Jump("loc_4613")

    label("loc_43CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_4521")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44A7")

    #C0183
    ChrTalk(
        0xFE,
        (
            "エラルダ大司教は、\x01",
            "新しく来たシスター・リースと\x01",
            "面会しているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "彼女の名前を聞いたときに、\x01",
            "大司教が少し驚いていた\x01",
            "ようなのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "ふむ、もしや有名な方\x01",
            "なのでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_451C")

    label("loc_44A7")


    #C0186
    ChrTalk(
        0xFE,
        (
            "シスター・リースの名前に、\x01",
            "大司教が少し驚いていた\x01",
            "ようなのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "ふむ、もしや有名な方\x01",
            "なのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_451C")

    Jump("loc_4613")

    label("loc_4521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4613")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45BF")

    #C0188
    ChrTalk(
        0xFE,
        (
            "大聖堂では定期的に\x01",
            "ミサが催されています。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "ミサは空の女神を奉る\x01",
            "神聖な行事……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "開催の折には、\x01",
            "ふるって参加ください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4613")

    label("loc_45BF")


    #C0191
    ChrTalk(
        0xFE,
        (
            "ミサは空の女神を奉る\x01",
            "神聖な行事……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "開催の折には、\x01",
            "ふるって参加ください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4613")

    TalkEnd(0xFE)
    Return()

    # Function_15_3323 end

    def Function_16_4617(): pass

    label("Function_16_4617")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4768")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46CA")

    #C0193
    ChrTalk(
        0xFE,
        (
            "市外の子供たちとも、\x01",
            "ようやく連絡をとることができました。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "しばらくは日曜学校の出張も\x01",
            "様子を見ることにはなりそうですが、\x01",
            "ひとまず安心です。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4763")

    label("loc_46CA")


    #C0195
    ChrTalk(
        0xFE,
        (
            "市外の子供たちと連絡がとれて、\x01",
            "ひとまず安心です。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "さて、日曜学校が再開した時のために\x01",
            "シスター・マーブルと授業内容を\x01",
            "相談しておきましょうかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4763")

    Jump("loc_5A39")

    label("loc_4768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4844")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_480C")

    #C0197
    ChrTalk(
        0xFE,
        (
            "市外の子供たちに\x01",
            "連絡が取りにくい状態が続く中、\x01",
            "こんな事が起こってしまうなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "ああ、女神よ……\x01",
            "どうか人々をお護り下さい……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_483F")

    label("loc_480C")


    #C0199
    ChrTalk(
        0xFE,
        (
            "ああ、女神よ……\x01",
            "どうか人々をお護り下さい……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_483F")

    Jump("loc_5A39")

    label("loc_4844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4A09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_498E")

    #C0200
    ChrTalk(
        0xFE,
        (
            "先日、シスター・リースが\x01",
            "クロスベルを離れました。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "何でもアルテリア法国からの\x01",
            "召還指示があったそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        "#00005F（エリィ、これはもしかして……）\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x102,
        (
            "#00101F（ええ、たぶん《星杯騎士》としての\x01",
            "  指示が下ったんじゃないかしら。）\x02\x03",

            "#00103F（それが何かまでは\x01",
            "  さすがに分からないけど……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4A04")

    label("loc_498E")


    #C0204
    ChrTalk(
        0xFE,
        (
            "先日、シスター・リースが\x01",
            "クロスベルを離れました。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "何でもアルテリア法国からの\x01",
            "召還指示があったそうですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A04")

    Jump("loc_5A39")

    label("loc_4A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4AC2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A3B")
    Call(0, 54)
    Return()

    label("loc_4A3B")


    #C0206
    ChrTalk(
        0xFE,
        (
            "今回のミサには、普段よりも\x01",
            "かなり多くの人が訪れています。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "やはり襲撃事件で人々が負った傷は、\x01",
            "とても大きいようですね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A39")

    label("loc_4AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4C2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BA5")

    #C0208
    ChrTalk(
        0xFE,
        (
            "キミィちゃんやアレクくん……\x01",
            "おととい会ったばかりなのに\x01",
            "こんな事件に巻き込まれてしまうなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "さぞ怖い思いをしているでしょう……\x01",
            "ああ女神様、どうかあの子達を、\x01",
            "マインツをお救いください……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4C2A")

    label("loc_4BA5")


    #C0210
    ChrTalk(
        0xFE,
        (
            "マインツへは、一昨日に\x01",
            "日曜学校の出張に行った\x01",
            "ばかりなのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "ああ女神様、どうかあの子達を、\x01",
            "マインツをお救いください……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C2A")

    Jump("loc_5A39")

    label("loc_4C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4C3D")
    Jump("loc_5A39")

    label("loc_4C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4C4B")
    Jump("loc_5A39")

    label("loc_4C4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4C59")
    Jump("loc_5A39")

    label("loc_4C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_4D27")

    #C0212
    ChrTalk(
        0xFE,
        (
            "年長クラスの授業も\x01",
            "そろそろ終わったようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "私も明日、明後日は\x01",
            "マインツ、アルモリカに\x01",
            "日曜学校の出張に行くんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "あとでシスター・マーブルに\x01",
            "授業内容を相談しておかないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A39")

    label("loc_4D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_4E9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E01")

    #C0215
    ChrTalk(
        0xFE,
        "シスター・マーブルに御用ですか？\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "彼女はただいま、\x01",
            "年長クラスの授業の最中です。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "今日はシスター・ジュジュに\x01",
            "授業のやり方を教えているようですし、\x01",
            "手が離せないかもしれませんが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4E96")

    label("loc_4E01")


    #C0218
    ChrTalk(
        0xFE,
        (
            "シスター・マーブルはたった今、\x01",
            "年長クラスの授業の最中です。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "今日はシスター・ジュジュの\x01",
            "教育も兼ねているので、\x01",
            "手が離せないかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E96")

    Jump("loc_5A39")

    label("loc_4E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_503F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FC8")

    #C0220
    ChrTalk(
        0xFE,
        (
            "今日は、シスター・ジュジュが\x01",
            "シスター・マーブルに授業のやり方を\x01",
            "学んでいるようなのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "この間、マインツへの出張を\x01",
            "シスター・リースに任せたことが\x01",
            "いい刺激になったみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "彼女は技術こそ拙いですが、\x01",
            "子供に好かれる才能があるので\x01",
            "きっと上手になりますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_503A")

    label("loc_4FC8")


    #C0223
    ChrTalk(
        0xFE,
        (
            "シスター・ジュジュは\x01",
            "子供に好かれる才能があるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "日曜学校の授業にしても、\x01",
            "きっと上手になりますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_503A")

    Jump("loc_5A39")

    label("loc_503F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_532F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5198")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5114")

    #C0225
    ChrTalk(
        0xFE,
        (
            "シスター・リースが\x01",
            "先ほど日曜学校の出張から\x01",
            "戻ってきたようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "少し遅かったので\x01",
            "心配していましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "もしかして、どこかで\x01",
            "ご飯でも食べてきてたのかしら？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5193")

    label("loc_5114")


    #C0228
    ChrTalk(
        0xFE,
        (
            "シスター・リースが\x01",
            "先ほど日曜学校の出張から\x01",
            "戻ってきたようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "今はシスター・マーブルの所へ\x01",
            "報告に行っていますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5193")

    Jump("loc_532A")

    label("loc_5198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52A7")

    #C0230
    ChrTalk(
        0xFE,
        (
            "シスター・リースは今日、\x01",
            "マインツ方面に日曜学校の\x01",
            "出張に行ってるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "彼女、物静かな方ですけど\x01",
            "教えるのが上手なんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "そういえば、そろそろ帰ってきても\x01",
            "いい時間なんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "もしかして、バスを乗り過ごして\x01",
            "しまったのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_532A")

    label("loc_52A7")


    #C0234
    ChrTalk(
        0xFE,
        (
            "シスター・リース、\x01",
            "そろそろ出張から帰ってきても\x01",
            "いい時間なんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "もしかして、バスを乗り過ごして\x01",
            "しまったのかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_532A")

    Jump("loc_5A39")

    label("loc_532F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_53DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_534A")
    Call(0, 14)
    Jump("loc_53D9")

    label("loc_534A")


    #C0236
    ChrTalk(
        0xFE,
        (
            "エラルダ大司教……\x01",
            "以前からシスター・リースのことを\x01",
            "やけに気にかけているご様子です。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "私たちの知らない事情でも\x01",
            "あるんでしょうか……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53D9")

    Jump("loc_5A39")

    label("loc_53DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_55E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5547")

    #C0238
    ChrTalk(
        0xFE,
        (
            "マインツやアルモリカの子などは、\x01",
            "大聖堂が遠いので、日曜学校にも\x01",
            "なかなか通えません。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "また、旧市街の子たちなどは\x01",
            "授業の日でも教会には\x01",
            "なかなか来てくれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "そういった子たちに向けて、\x01",
            "私たちシスターは町村に出向いて\x01",
            "授業を行っているのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "ちなみに今日は、\x01",
            "シスター・リースに旧市街へ\x01",
            "出張してもらってるんですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_55DE")

    label("loc_5547")


    #C0242
    ChrTalk(
        0xFE,
        (
            "ちなみに今日は、\x01",
            "シスター・リースに旧市街へ\x01",
            "出張してもらってるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "あそこは一癖ある子達ばかりですし、\x01",
            "しっかりやれているでしょうか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55DE")

    Jump("loc_5A39")

    label("loc_55E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_56A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55FE")
    Call(0, 13)
    Jump("loc_56A0")

    label("loc_55FE")


    #C0244
    ChrTalk(
        0xFE,
        (
            "シスター・リースはとても\x01",
            "仕事を覚えるのが早くて……\x01",
            "私たちも随分助けられています。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "エラルダ大司教……\x01",
            "彼女について何か気になる事でも\x01",
            "あるんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56A0")

    Jump("loc_5A39")

    label("loc_56A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_572C")

    #C0246
    ChrTalk(
        0xFE,
        (
            "リースさんは\x01",
            "大司教への挨拶を終えて、\x01",
            "墓地の方に行ったようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "明日からは私たちで\x01",
            "色々と仕事を教えませんと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A39")

    label("loc_572C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_59A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5917")

    #C0248
    ChrTalk(
        0xFE,
        (
            "シスター・リースは\x01",
            "なんというか落ち着いていて、\x01",
            "とても雰囲気のある方ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "それにしても、彼女から\x01",
            "とても美味しそうな匂いが\x01",
            "してきたのですが、あれは一体……\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        (
            "#00005Fそういえば……\x01",
            "ほのかにリースさんから\x01",
            "パンの匂いがしたような。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x102,
        (
            "#00100F多分、来る前にパン屋に寄って\x01",
            "買い物をしたんじゃないかしら。\x02\x03",

            "#00109Fリースさんはあの細身で\x01",
            "なかなか大食家なのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x109,
        "#10105Fへ、へえ……そうなんですね。\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、一度食事を\x01",
            "ご一緒したいものだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_59A4")

    label("loc_5917")


    #C0254
    ChrTalk(
        0xFE,
        (
            "シスター・リースは\x01",
            "なんというか落ち着いていて、\x01",
            "とても雰囲気のある方ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "シスター・ジュジュにとっても\x01",
            "いい刺激になりそうです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59A4")

    Jump("loc_5A39")

    label("loc_59A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5A39")

    #C0256
    ChrTalk(
        0xFE,
        (
            "実は今日、新しいシスターが\x01",
            "アルテリア法国から\x01",
            "派遣されてくる予定なのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "一体どのような方が来るのか……\x01",
            "少々楽しみですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A39")

    TalkEnd(0xFE)
    Return()

    # Function_16_4617 end

    def Function_17_5A3D(): pass

    label("Function_17_5A3D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5AC0")

    #C0258
    ChrTalk(
        0xC,
        (
            "教会にも救いを求める人が\x01",
            "続々と押し寄せてくるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xC,
        (
            "僕たちもしっかり準備して\x01",
            "迎え入れてあげないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_5AC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5B2B")

    #C0260
    ChrTalk(
        0xC,
        (
            "クロスベル市では大変な事に\x01",
            "なっているみたいだね……\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xC,
        "市民たちが無事だといいんだが。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_5B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5CB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C1C")

    #C0262
    ChrTalk(
        0xC,
        (
            "クロスベルの国家独立か……\x01",
            "とんでもないことになったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xC,
        (
            "しかも、銀行の資金凍結なんて……\x01",
            "七耀教会の人間としては、\x01",
            "さすがに擁護できることじゃないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xC,
        (
            "僕たちもしばらく様子を見ることに\x01",
            "なりそうだな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5CAD")

    label("loc_5C1C")


    #C0265
    ChrTalk(
        0xC,
        (
            "銀行の資金凍結なんて……\x01",
            "七耀教会の人間としては、\x01",
            "さすがに擁護できることじゃないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xC,
        (
            "僕たちもしばらく様子を見ることに\x01",
            "なりそうだな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CAD")

    Jump("loc_6A1E")

    label("loc_5CB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5D62")

    #C0267
    ChrTalk(
        0xC,
        (
            "旧市街の復旧は、\x01",
            "テスタメンツの子達が\x01",
            "率先してやっているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xC,
        (
            "最初は何を考えているか\x01",
            "分からないと思っていたけど……\x01",
            "根はいい子たちだったみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_5D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5DD6")

    #C0269
    ChrTalk(
        0xC,
        (
            "こんな事件が起きるなんて\x01",
            "信じられない思いだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xC,
        (
            "マインツの人たちが\x01",
            "無事だといいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_5DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5E63")

    #C0271
    ChrTalk(
        0xC,
        (
            "さっき、ジュジュくんが\x01",
            "盛大にしりもちをついていたのを\x01",
            "目撃しちゃってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xC,
        (
            "やれやれ、彼女もなかなか\x01",
            "ドジが抜けないね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_5E63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5ED7")

    #C0273
    ChrTalk(
        0xC,
        (
            "この台座は、調薬などに\x01",
            "よく使われているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xC,
        (
            "他のところよりも\x01",
            "入念に掃除しておかないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_5ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6028")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F9C")

    #C0275
    ChrTalk(
        0xC,
        (
            "リースくんは、いつも聖典を\x01",
            "持ち歩いているようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xC,
        (
            "暇さえあれば本を開いて\x01",
            "読みふけっているのを\x01",
            "よく見かけるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xC,
        (
            "いやあ、勤勉だなあ。\x01",
            "大変結構なことだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6023")

    label("loc_5F9C")


    #C0278
    ChrTalk(
        0xC,
        (
            "リースくんは、いつも聖典を\x01",
            "持ち歩いているようでね。\x01",
            "暇さえあれば読んでるみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xC,
        (
            "いやあ、勤勉だなあ。\x01",
            "大変結構なことだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6023")

    Jump("loc_6A1E")

    label("loc_6028")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_60A0")

    #C0280
    ChrTalk(
        0xC,
        (
            "リースくん、街から\x01",
            "戻ってきたみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xC,
        (
            "今日はどこで食べてきたんだろう。\x01",
            "後で聞いてみるかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_60A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_6111")

    #C0282
    ChrTalk(
        0xC,
        "うむ、掃除はこんなところかな。\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xC,
        (
            "みんなが使う場所なんだ。\x01",
            "しっかり綺麗にしておかないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_6111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6232")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61C5")

    #C0284
    ChrTalk(
        0xC,
        (
            "執務室の掃除をしていたら、\x01",
            "大司教が入ってきてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xC,
        (
            "調べたいことがあるから\x01",
            "１人にしてくれと言われたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xC,
        (
            "ふむ……\x01",
            "一体何を調べてるのかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_622D")

    label("loc_61C5")


    #C0287
    ChrTalk(
        0xC,
        (
            "リースくんもさっき、\x01",
            "昼食をとりに街へ行って\x01",
            "しまったみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xC,
        "僕も休憩をとるとするかな。\x02",
    )

    CloseMessageWindow()

    label("loc_622D")

    Jump("loc_6A1E")

    label("loc_6232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_639F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6315")

    #C0289
    ChrTalk(
        0xC,
        (
            "クローディア殿下も、\x01",
            "今日の本会議に向けて緊張を\x01",
            "なさってるかとおもったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xC,
        (
            "いやとんでもない、\x01",
            "とても落ち着いておられたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xC,
        (
            "さすがはリベールの次期女王……\x01",
            "肝が据わってらっしゃるな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_639A")

    label("loc_6315")


    #C0292
    ChrTalk(
        0xC,
        (
            "本会議を前にして、\x01",
            "クローディア殿下は\x01",
            "実に落ち着いておられたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xC,
        (
            "さすがはリベールの次期女王……\x01",
            "肝が据わってらっしゃるな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_639A")

    Jump("loc_6A1E")

    label("loc_639F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_652C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6486")

    #C0294
    ChrTalk(
        0xC,
        "除幕式には僕も度肝を抜かれたよ。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xC,
        (
            "正直に言ってしまうと、\x01",
            "地上４０階なんてのがとても\x01",
            "信じられなくてねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xC,
        (
            "ハハ、ディーター市長には、\x01",
            "今度礼拝にいらっしゃったときにでも\x01",
            "謝らないといけないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6527")

    label("loc_6486")


    #C0297
    ChrTalk(
        0xC,
        (
            "除幕式には僕も度肝を抜かれたよ。\x01",
            "まさか本当に４０階もあるとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xC,
        (
            "ハハ、ディーター市長には、\x01",
            "今度礼拝にいらっしゃったときにでも\x01",
            "謝らないといけないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6527")

    Jump("loc_6A1E")

    label("loc_652C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_66DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6643")

    #C0299
    ChrTalk(
        0xC,
        (
            "エラルダ大司教は\x01",
            "とても厳格なお方だから、\x01",
            "教会内でも対立が多いんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xC,
        (
            "中でも、活動内容がはっきりしない\x01",
            "《封聖省》の人間に関しては、\x01",
            "特に厳しい態度をとっていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xC,
        (
            "おかげで封聖省の関係者が\x01",
            "クロスベル教区に\x01",
            "滅多にやって来ないくらいなんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_66D6")

    label("loc_6643")


    #C0302
    ChrTalk(
        0xC,
        (
            "封聖省といえば\x01",
            "女神の秘蹟を管理すると言われる\x01",
            "教会内の機関だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xC,
        (
            "その活動内容は、我々一般の聖職者にも\x01",
            "詳しくは知らされていないんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66D6")

    Jump("loc_6A1E")

    label("loc_66DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6850")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67C5")

    #C0304
    ChrTalk(
        0xC,
        (
            "リースさん、大人しそうだから\x01",
            "みんなに馴染めるか心配だったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xC,
        (
            "昨日の夕食当番のジュジュくんとは\x01",
            "真っ先に打ち解けてたみたいでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xC,
        (
            "昨夜は市内の美味しい店の話で\x01",
            "大いに盛り上がってたようだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_684B")

    label("loc_67C5")


    #C0307
    ChrTalk(
        0xC,
        (
            "リースさん、食べ物のことになると\x01",
            "積極的に話に食い入ってくるんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xC,
        (
            "はは、食に対しての情熱は\x01",
            "すごいものがあるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_684B")

    Jump("loc_6A1E")

    label("loc_6850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_68E9")

    #C0309
    ChrTalk(
        0xC,
        (
            "大司教、挨拶が終わったのに\x01",
            "なにか考え事をしてるふうだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xC,
        (
            "リースさんに何か\x01",
            "問題でもあったんだろうか。\x01",
            "そうは見えないけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_68E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_698E")

    #C0311
    ChrTalk(
        0xC,
        (
            "新しく入ってくる\x01",
            "司祭やシスターに関しては、\x01",
            "大司教が一人一人面会を行うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xC,
        (
            "聖職者として不適格な人間を\x01",
            "大聖堂に置くわけにはいかないからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_698E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6A1E")

    #C0313
    ChrTalk(
        0xC,
        (
            "ここはエラルダ大司教の\x01",
            "執務室になっているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xC,
        (
            "珍しい薬草や貴重な書物が\x01",
            "保管されているから、\x01",
            "あまり色々と触らないようにね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A1E")

    TalkEnd(0xFE)
    Return()

    # Function_17_5A3D end

    def Function_18_6A22(): pass

    label("Function_18_6A22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6BA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B0F")

    #C0315
    ChrTalk(
        0xFE,
        (
            "突然あんなものが現れて、\x01",
            "商売仲間も皆驚いておるようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        (
            "だが、心配はいらん。\x01",
            "女神に祈ってさえいれば\x01",
            "絶対に大丈夫だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "さあ、君たちも祈ろうじゃないか。\x01",
            "それで何もかもが\x01",
            "上手くいくはずだからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6B9F")

    label("loc_6B0F")


    #C0318
    ChrTalk(
        0xFE,
        (
            "何が起ころうとも、\x01",
            "女神に祈ってさえいれば\x01",
            "絶対に大丈夫だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        (
            "さあ、君たちも祈ろうじゃないか。\x01",
            "それで何もかもが\x01",
            "上手くいくはずだからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B9F")

    Jump("loc_8017")

    label("loc_6BA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6CA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C58")

    #C0320
    ChrTalk(
        0xFE,
        (
            "か、戒厳令が出ている中\x01",
            "こっそりとお祈りに来たら、\x01",
            "あんな事が起こってしまった……\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "これでは街に戻ることができん。\x01",
            "一体どうすればいいんだ……！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6CA0")

    label("loc_6C58")


    #C0322
    ChrTalk(
        0xFE,
        (
            "と、とにかく、\x01",
            "早く事態が収まるように\x01",
            "女神にお祈りをしなければ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CA0")

    Jump("loc_8017")

    label("loc_6CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6E15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D9D")

    #C0323
    ChrTalk(
        0xFE,
        (
            "鉄道の運行が止まるとなると、\x01",
            "これからは貿易の仕事は\x01",
            "厳しくなりそうだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        (
            "しかし、私は世の中の流れに\x01",
            "逆らうつもりはない。\x01",
            "きっとこれも女神の意思なのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "なあに、何とかなる。\x01",
            "信じる心を忘れさえしなければな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6E10")

    label("loc_6D9D")


    #C0326
    ChrTalk(
        0xFE,
        (
            "女神に祈ってさえいれば\x01",
            "きっと、何もかも\x01",
            "上手くいくはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "君たちも祈るといい。\x01",
            "大事なのは信じる心だぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E10")

    Jump("loc_8017")

    label("loc_6E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6F6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EF8")

    #C0328
    ChrTalk(
        0xFE,
        (
            "最近、女神への祈りもあって\x01",
            "商売は上手くいっていたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        (
            "ここまで深刻な事件が起きたら\x01",
            "正直、手放しでは喜べないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "きっと、儲けそのものに\x01",
            "意味はないのだろう。\x01",
            "平穏をこそ祈らなければな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6F69")

    label("loc_6EF8")


    #C0331
    ChrTalk(
        0xFE,
        (
            "どんなに儲けても、\x01",
            "クロスベルがこんな状況では\x01",
            "手放しでは喜べない。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        (
            "平穏をこそ、\x01",
            "女神に祈らなければな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F69")

    Jump("loc_8017")

    label("loc_6F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7089")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_701C")

    #C0333
    ChrTalk(
        0xFE,
        (
            "実は今日、マインツで七耀石を\x01",
            "仕入れる予定だったのだが……\x01",
            "まさかこんな事件が起きるとは。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "そ、そうだ、事件の解決を\x01",
            "女神に祈らなければ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7084")

    label("loc_701C")


    #C0335
    ChrTalk(
        0xFE,
        (
            "商売を抜きにしても、\x01",
            "マインツの状況が心配だ……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        (
            "女神よ、どうかこの事件を\x01",
            "解決に導きたまえ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7084")

    Jump("loc_8017")

    label("loc_7089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_71D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_714E")

    #C0337
    ChrTalk(
        0xFE,
        (
            "実は昨日、一日中\x01",
            "不吉な予感を感じていてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        (
            "後で聞いて見れば、\x01",
            "脱線事故が起こっていた\x01",
            "そうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "私の商談には影響がなかったが……\x01",
            "正直ゾッとしたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_71D3")

    label("loc_714E")


    #C0340
    ChrTalk(
        0xFE,
        (
            "実は昨日、一日中\x01",
            "不吉な予感を感じていてな。\x01",
            "脱線事故の話には驚いたぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xFE,
        (
            "私の商談には影響がなかったが……\x01",
            "正直ゾッとしたよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71D3")

    Jump("loc_8017")

    label("loc_71D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_72F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_727B")

    #C0342
    ChrTalk(
        0xFE,
        (
            "女神に熱心に祈っていたのだが……\x01",
            "こんどは靴紐が切れてしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xFE,
        (
            "今日は商談があるというのに……\x01",
            "どうしてこうも不吉なのだっ！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_72F3")

    label("loc_727B")


    #C0344
    ChrTalk(
        0xFE,
        (
            "クロネコが前を横切ったり、\x01",
            "靴紐が切れてしまったり……\x01",
            "今朝からどうにも不吉だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        "何事も起こらねばよいのだが……\x02",
    )

    CloseMessageWindow()

    label("loc_72F3")

    Jump("loc_8017")

    label("loc_72F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7437")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73C4")

    #C0346
    ChrTalk(
        0xFE,
        (
            "……実は今朝、\x01",
            "私の前を黒猫が横切ってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "ああ、くそう……\x01",
            "今日は商談があるというのに\x01",
            "不吉極まりないじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "これはいつもより\x01",
            "念入りに祈らねばな……\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    SetScenarioFlags(0x0, 2)
    Jump("loc_7432")

    label("loc_73C4")


    #C0349
    ChrTalk(
        0xFE,
        (
            "今日は商談だというのに、\x01",
            "目の前を黒猫が横切ったのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        (
            "女神よ、どうかこの\x01",
            "不吉な気配を祓いたまえ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7432")

    Jump("loc_8017")

    label("loc_7437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_74C5")

    #C0351
    ChrTalk(
        0xFE,
        (
            "……うむ、よくお祈りをしたし\x01",
            "そろそろ帰るとするかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "……やっぱり、まだ祈り足りないな。\x01",
            "もう少しここにいるとしよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8017")

    label("loc_74C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_7641")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75A6")

    #C0353
    ChrTalk(
        0xFE,
        (
            "先ほど来ていたのは\x01",
            "確か、イアン・グリムウッド先生だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xFE,
        (
            "少々疲れていたようだが……\x01",
            "礼拝堂に満ちる聖なる空気に、\x01",
            "さぞ癒されたに違いない。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "お祈りもしていたし……\x01",
            "きっと大丈夫だろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_763C")

    label("loc_75A6")


    #C0356
    ChrTalk(
        0xFE,
        (
            "私も商売をする中で\x01",
            "グリムウッド先生には\x01",
            "よく相談に乗ってもらった。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "少々疲れていたようだが、\x01",
            "お祈りもしていたし……\x01",
            "さぞ癒されたことだろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_763C")

    Jump("loc_8017")

    label("loc_7641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_77CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_772C")

    #C0358
    ChrTalk(
        0xFE,
        (
            "この間の独立提唱については、\x01",
            "諸外国でも関心が高いようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        (
            "外国の商売仲間たちも、\x01",
            "クロスベル独立の是非を\x01",
            "日々議論しているそうでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        (
            "ここにきて、クロスベルの注目度は\x01",
            "より一層増しているようだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_77C6")

    label("loc_772C")


    #C0361
    ChrTalk(
        0xFE,
        (
            "独立の是非を問う住民投票も近い。\x01",
            "そして、その結果は\x01",
            "女神のみぞ知るだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "おお、女神よ。\x01",
            "どうかクロスベルにとって\x01",
            "最良の選択がされますよう……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77C6")

    Jump("loc_8017")

    label("loc_77CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_786E")

    #C0363
    ChrTalk(
        0xFE,
        (
            "今日の本会議は、一般市民が\x01",
            "傍聴することは出来ないそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "残念だが……仕方あるまい。\x01",
            "私はここで会議の成功を\x01",
            "女神に祈り続けることにしよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8017")

    label("loc_786E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_79BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7940")

    #C0365
    ChrTalk(
        0xFE,
        (
            "私もオルキスタワーを\x01",
            "見にいったのだが……\x01",
            "とてつもない高さだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "あの屋上からなら、\x01",
            "空の女神への祈りも\x01",
            "より届きやすいはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "うむ、是非とも\x01",
            "登ってみたいものだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_79B9")

    label("loc_7940")


    #C0368
    ChrTalk(
        0xFE,
        (
            "オルキスタワーの屋上からなら、\x01",
            "空の女神への祈りも\x01",
            "より届きやすいはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        (
            "うむ、私も是非\x01",
            "登ってみたいものだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79B9")

    Jump("loc_8017")

    label("loc_79BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7ADA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A75")

    #C0370
    ChrTalk(
        0xFE,
        (
            "明日からの通商会議では、\x01",
            "経済関係の取り決めについて\x01",
            "話し合われるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        (
            "クロスベルを拠点に\x01",
            "商売をしている私にとって、\x01",
            "非常に関心の高い行事だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7AD5")

    label("loc_7A75")


    #C0372
    ChrTalk(
        0xFE,
        (
            "通商会議は、商人として\x01",
            "とても関心がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "どれ、会議の成功を\x01",
            "女神に祈っておかねばな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AD5")

    Jump("loc_8017")

    label("loc_7ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7C02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B8D")

    #C0374
    ChrTalk(
        0xFE,
        (
            "雨だろうと、台風だろうと、\x01",
            "朝早くに商談があろうと、\x01",
            "毎日の祈りを欠かしたことはない。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        (
            "そのおかげで、\x01",
            "商売の調子は右肩上がりだ。\x01",
            "はっはっは……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7BFD")

    label("loc_7B8D")


    #C0376
    ChrTalk(
        0xFE,
        (
            "私はどんな事があろうと、\x01",
            "毎日の祈りを欠かしたことはない。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "継続は力なり、というからな。\x01",
            "はっはっは……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BFD")

    Jump("loc_8017")

    label("loc_7C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_7DE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D5D")

    #C0378
    ChrTalk(
        0x153,
        (
            "#01105Fあ、いつもお祈りにきてる\x01",
            "オジサンだー。\x02\x03",

            "#01109F朝から来てたみたいだけど、\x01",
            "まだ居たんだー？\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "うむ、私は休みの日は、\x01",
            "一日中祈りを捧げることに\x01",
            "しているのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xFE,
        (
            "お嬢ちゃんも祈りたまえ。\x01",
            "そうすればきっと、\x01",
            "何もかも上手くいくだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x153,
        "#01105F……ロイド、そうなの？\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        "#00006F（……俺に聞かれても。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7DE3")

    label("loc_7D5D")


    #C0383
    ChrTalk(
        0xFE,
        (
            "私は休みの日は、\x01",
            "一日中祈りを捧げることに\x01",
            "しているのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xFE,
        (
            "君たちも祈りたまえ。\x01",
            "そうすればきっと、\x01",
            "何もかも上手くいくだろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DE3")

    Jump("loc_8017")

    label("loc_7DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_7EDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E6C")

    #C0385
    ChrTalk(
        0xFE,
        (
            "今の私があるのは、\x01",
            "女神の加護のおかげ……\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "感謝の気持ちを充分に込めて、\x01",
            "祈らねばならぬな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 2)
    Jump("loc_7ED6")

    label("loc_7E6C")


    #C0387
    ChrTalk(
        0xFE,
        (
            "ああ、空の女神よ、\x01",
            "いつもありがとうございます……\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xFE,
        (
            "是非次の商売も、\x01",
            "ご加護をお願いしますぞ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7ED6")

    Jump("loc_8017")

    label("loc_7EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8017")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F83")

    #C0389
    ChrTalk(
        0xFE,
        (
            "私は貿易商をしていてな。\x01",
            "こちらには商売のお祈りのため、\x01",
            "よく来るようにしているのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        (
            "是非、君たちも祈っていく事を\x01",
            "オススメするぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8017")

    label("loc_7F83")


    #C0391
    ChrTalk(
        0xFE,
        (
            "以前にも、商売の成功を祈ったら、\x01",
            "本当に上手くいったことがあってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        (
            "何をするにも、まずは女神に祈ることだ。\x01",
            "そうすれば間違いないだろうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8017")

    TalkEnd(0xFE)
    Return()

    # Function_18_6A22 end

    def Function_19_801B(): pass

    label("Function_19_801B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_802C")
    Jump("loc_8ABB")

    label("loc_802C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8537")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_805E")
    Call(0, 56)
    Return()

    label("loc_805E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83BF")

    #C0393
    ChrTalk(
        0x101,
        (
            "#00000Fリースさん、\x01",
            "ミサの手伝いをしてる\x01",
            "みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xA,
        (
            "#04400Fええ、そんなところです。\x02\x03",

            "#04408F……今回のミサには、\x01",
            "特に多くの参拝客が\x01",
            "訪れているようですね。\x02\x03",

            "自分の大切な場所が襲われ、\x01",
            "傷つけられる恐ろしさ……\x02\x03",

            "#04403F……私にも分かる気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x102,
        "#00105Fリースさん……\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x105,
        (
            "#10303F（……彼女にも昔、似たような事が\x01",
            "  あったのかもしれないね。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    #C0397
    ChrTalk(
        0xA,
        (
            "#04400F（ここだけの話……\x01",
            "  今回の事件の影響で《封聖省》も\x01",
            "  この先の動きを決めかねています。）\x02\x03",

            "#04403F（……私はクロスベルに居られるうちに#13R㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　　　　　　　　　　　　　#、\x01",
            "  出来る限り情報を集めておくつもりです。）\x02\x03",

            "#04400F（ロイドさんたちも、動向には\x01",
            "  注意しておくようにしてください。）\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x103,
        "#00200F（居られるうちに……ですか。）\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x101,
        (
            "#00003F（……分かりました。\x01",
            "  リースさんもお気をつけて。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 5)
    Jump("loc_84B5")

    label("loc_83BF")


    #C0400
    ChrTalk(
        0xA,
        (
            "#04400F（今回の事件の影響で《封聖省》も\x01",
            "  この先の動きを決めかねています。）\x02\x03",

            "#04403F（……私はクロスベルに居られるうちに、\x01",
            "  出来る限り情報を集めておくつもりです。）\x02\x03",

            "#04400F（ロイドさんたちも、動向には\x01",
            "  注意しておくようにしてください。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84B5")

    Jump("loc_8532")

    label("loc_84BA")


    #C0401
    ChrTalk(
        0xA,
        (
            "#04400F私はもうしばらく\x01",
            "ミサの手伝いがありますので。\x02\x03",

            "#04404Fプログラムが開始するときに\x01",
            "こちらに連絡してください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8532")

    Jump("loc_8ABB")

    label("loc_8537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8545")
    Jump("loc_8ABB")

    label("loc_8545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8951")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8886")

    #C0402
    ChrTalk(
        0xA,
        (
            "#04400F昨日の脱線事故……\x01",
            "現場付近で巨大な化物が\x01",
            "目撃されたそうですね。\x02\x03",

            "みなさん、\x01",
            "何か心当たりは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x101,
        "#00001Fええ、実は……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0404
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "昨日の事件について\x01",
            "かいつまんで説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0405
    ChrTalk(
        0xA,
        (
            "#04405F……ノックスの樹海にも\x01",
            "プレロマ草が……\x02\x03",

            "#04408Fそして、この地に再び現れた\x01",
            "《グノーシス》ですか……\x02\x03",

            "#04403F問題は『誰がグノーシスを』……\x01",
            "というところでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x105,
        (
            "#10301F……そっちでは\x01",
            "なにか掴んでいないのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xA,
        (
            "#04400F生憎ですが……\x01",
            "グノーシスを含む教団関係の情報は\x01",
            "依然調査が進んでいない状況です。\x02\x03",

            "#04403Fプレロマ草については\x01",
            "私が調査をすすめていますが、\x01",
            "咲く原因などもいまだ不明……\x02\x03",

            "#04400Fこの地に潜入できているのが\x01",
            "私だけなので、こればかりは\x01",
            "時間を要しそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x101,
        (
            "#00003Fそうですか……\x02\x03",

            "#00000Fでは、また何か分かったら\x01",
            "よろしくおねがいします。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xA,
        "#04400Fええ……了解しました。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16D, 1)
    Jump("loc_894C")

    label("loc_8886")


    #C0410
    ChrTalk(
        0xA,
        (
            "#04403Fノックスの樹海のプレロマ草……\x01",
            "そして、この地に再び現れた\x01",
            "《グノーシス》……\x02\x03",

            "#04400F表立った動きができないこともあって、\x01",
            "調査状況は芳しくありませんが……\x01",
            "何か分かり次第、ご報告します。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_894C")

    Jump("loc_8ABB")

    label("loc_8951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_895F")
    Jump("loc_8ABB")

    label("loc_895F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_896D")
    Jump("loc_8ABB")

    label("loc_896D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_897B")
    Jump("loc_8ABB")

    label("loc_897B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_8989")
    Jump("loc_8ABB")

    label("loc_8989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8997")
    Jump("loc_8ABB")

    label("loc_8997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8A37")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89BE")
    Call(0, 21)
    Jump("loc_8A32")

    label("loc_89BE")


    #C0411
    ChrTalk(
        0xA,
        (
            "#04400F……みなさん、今日はどうも\x01",
            "ありがとうございました。\x02\x03",

            "#04403Fまた何かありましたら\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A32")

    Jump("loc_8ABB")

    label("loc_8A37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8A45")
    Jump("loc_8ABB")

    label("loc_8A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8A53")
    Jump("loc_8ABB")

    label("loc_8A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8A96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A6E")
    Call(0, 20)
    Jump("loc_8A91")

    label("loc_8A6E")


    #C0412
    ChrTalk(
        0xA,
        "#04403F（ルフィナ姉さん……）\x02",
    )

    CloseMessageWindow()

    label("loc_8A91")

    Jump("loc_8ABB")

    label("loc_8A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_8AA4")
    Jump("loc_8ABB")

    label("loc_8AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_8AB2")
    Jump("loc_8ABB")

    label("loc_8AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8ABB")

    label("loc_8ABB")

    TalkEnd(0xFE)
    Return()

    # Function_19_801B end

    def Function_20_8ABF(): pass

    label("Function_20_8ABF")

    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0413
    ChrTalk(
        0xA,
        (
            "#04400F……なるほど、こちらの教育は\x01",
            "なかなか進んでいるようですね。\x02\x03",

            "#04404Fさすがは最先端の\x01",
            "近代都市というところでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x8,
        (
            "ふふ、確かに\x01",
            "少しは進んでいるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x8,
        (
            "どこに行っても\x01",
            "子供たちは変わらないものよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xA,
        "#04402F確かに……そうかもしれません。\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x8,
        (
            "……ところで、リースさん。\x01",
            "一つ気になっていることが\x01",
            "あるのだけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x8,
        (
            "あなたはもしかして、\x01",
            "ルフィナさんの妹さん……\x01",
            "ではないかしら。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0419
    ChrTalk(
        0xA,
        "#04405F……姉を知っていたのですか？\x02",
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x8,
        (
            "ふふ、やっぱり。\x01",
            "苗字が同じだからピンときたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x8,
        (
            "彼女には昔、色々と\x01",
            "お世話になったことがあったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xA,
        (
            "#04403Fそうでしたか……\x02\x03",

            "#04400Fあの、シスター・マーブル。\x01",
            "お願いがあるのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x8,
        (
            "ふふ、言わなくていいわ。\x01",
            "多分あなたも、そう#4R㈲  ㈲ #なんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x8,
        (
            "ルフィナさんにはお世話になっていたし、\x01",
            "大司教に告げることはしないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x8,
        "……でも、一つだけいいかしら？\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0426
    ChrTalk(
        0x8,
        (
            "決して、無理はしないようにね。\x01",
            "あなたのお姉さんのためにも……\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xA,
        (
            "#04403F……分かりました。\x01",
            "お心遣いありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x135, 3)
    Return()

    # Function_20_8ABF end

    def Function_21_8ED1(): pass

    label("Function_21_8ED1")

    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0428
    ChrTalk(
        0x8,
        (
            "リースさん、\x01",
            "少し遅かったようですけど\x01",
            "なにかあったのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x8,
        (
            "それに、修道服がところどころ\x01",
            "すすけてしまっていますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xA,
        (
            "#04403F遅れて申し訳ありません。\x02\x03",

            "#04400F実は、帰る途中につまづいて\x01",
            "転んでしまいまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x8,
        (
            "あらあら、リースさんったら\x01",
            "意外とドジなのねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x8,
        (
            "……若いからと言って、\x01",
            "無理ばかりしてはだめですよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xA,
        (
            "#04400F……お気遣いありがとうございます。\x01",
            "今、着替えてきますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x101,
        (
            "#00000F（マーブル先生……\x01",
            "  何があったのかある程度\x01",
            "  気づいているみたいだな。）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x2, 0)
    Return()

    # Function_21_8ED1 end

    def Function_22_90D6(): pass

    label("Function_22_90D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9101")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_90F9")
    Call(0, 23)
    Jump("loc_90FC")

    label("loc_90F9")

    Call(0, 25)

    label("loc_90FC")

    Jump("loc_9104")

    label("loc_9101")

    Call(0, 23)

    label("loc_9104")

    Return()

    # Function_22_90D6 end

    def Function_23_9105(): pass

    label("Function_23_9105")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9458")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92F9")

    #C0435
    ChrTalk(
        0x8,
        (
            "ロイド、エリィ……\x01",
            "あなたたちに聞きたい事があります。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x8,
        (
            "あの大樹には……\x01",
            "キーアちゃんがいるのですね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0437
    ChrTalk(
        0x101,
        "#00005F先生……分かるんですか？\x02",
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x8,
        (
            "……あなたたちの\x01",
            "心配そうな顔を見て、\x01",
            "何となく察しがつきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x8,
        (
            "……詳しく事情は知りませんが、\x01",
            "私に言えることは唯一つです。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x8,
        (
            "キーアちゃんの保護者として、\x01",
            "必ずあなたたちの手に取り戻すこと。\x01",
            "……いいですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x102,
        "#00101Fはい……必ず！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 3)
    Jump("loc_9453")

    label("loc_92F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93D8")

    #C0442
    ChrTalk(
        0x8,
        (
            "どんな事情があっても、\x01",
            "キーアちゃんには\x01",
            "まだあなたたちが必要です。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x8,
        (
            "キーアちゃんにとっても、\x01",
            "それは同じのはず……\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x8,
        (
            "ロイド、エリィ、それに皆さん。\x01",
            "必ず彼女をあなたたちの手に\x01",
            "取り戻すのですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9453")

    label("loc_93D8")


    #C0445
    ChrTalk(
        0x8,
        (
            "どんな事情があっても、\x01",
            "キーアちゃんには\x01",
            "まだあなたたちが必要です。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x8,
        (
            "必ず彼女をあなたたちの手に\x01",
            "取り戻すのですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9453")

    Jump("loc_AE6D")

    label("loc_9458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_97B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_966A")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0447
    ChrTalk(
        0x8,
        (
            "まあ、ロイドにエリィ、\x01",
            "それに皆さん……！\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x101,
        (
            "#00000Fマーブル先生……\x01",
            "ご無事でなによりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x102,
        (
            "#00100Fご心配をおかけして\x01",
            "申しわけありませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x8,
        (
            "いえ、いいのです。\x01",
            "あなたたちが無事ならば\x01",
            "それが何よりですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x8,
        (
            "ところで……キーアちゃんは、\x01",
            "あなたたちと一緒なのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x103,
        "#00203F……いえ。\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x104,
        "#00306F居場所は分かってるんだが……\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x8,
        "そうですか……心配ですね。\x02",
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x8,
        (
            "……とにかく、今は\x01",
            "抜き差しならない状況です。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x8,
        (
            "あなたたちも十分に\x01",
            "気をつけるのですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 2)
    Jump("loc_97AE")

    label("loc_966A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_974E")

    #C0457
    ChrTalk(
        0x8,
        "キーアちゃん……心配ですね。\x02",
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x8,
        (
            "あの独立宣言の日から\x01",
            "一度も姿を見ないので、\x01",
            "私も気にはかけていたのですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x8,
        (
            "……とにかく、今は\x01",
            "抜き差しならない状況です。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x8,
        (
            "あなたたちも十分に\x01",
            "気をつけるのですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_97AE")

    label("loc_974E")


    #C0461
    ChrTalk(
        0x8,
        (
            "……とにかく、今は\x01",
            "抜き差しならない状況です。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x8,
        (
            "あなたたちも十分に\x01",
            "気をつけるのですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97AE")

    Jump("loc_AE6D")

    label("loc_97B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9A4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99BB")

    #C0463
    ChrTalk(
        0x8,
        (
            "ロイド……\x01",
            "キーアちゃんは大丈夫ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x8,
        (
            "最近は日曜学校もなかったですから、\x01",
            "少し心配になってしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x101,
        (
            "#00008F……そう言われると、\x01",
            "ここ数日は様子が変だった\x01",
            "ような気がします。\x02\x03",

            "#00003Fどこか思いつめているというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x102,
        (
            "#00108Fそうね……\x01",
            "私たちが出かけるときも、\x01",
            "とても心配していたみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x8,
        "そうですか……\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x8,
        (
            "おそらく、この状況が\x01",
            "不安で仕方ないのでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x8,
        (
            "ロイド、保護者として\x01",
            "しっかりとキーアちゃんを\x01",
            "見守ってあげるのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x101,
        "#00000Fええ、もちろんです。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 4)
    Jump("loc_9A46")

    label("loc_99BB")


    #C0471
    ChrTalk(
        0x8,
        (
            "クロスベルのこの状況……\x01",
            "今後、何が起こるかわかりません。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x8,
        (
            "ロイド、保護者として\x01",
            "しっかりとキーアちゃんを\x01",
            "見守ってあげるのですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A46")

    Jump("loc_AE6D")

    label("loc_9A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9BD8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A7D")
    Call(0, 55)
    Return()

    label("loc_9A7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B48")

    #C0473
    ChrTalk(
        0x8,
        (
            "日曜学校に出席していた子達は、\x01",
            "ひとまず無事を確認できました。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x8,
        (
            "こんな状況ですから、\x01",
            "授業はお休みになっていますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x8,
        (
            "再開されたら、また元気な笑顔を\x01",
            "見せてほしいものです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9BD3")

    label("loc_9B48")


    #C0476
    ChrTalk(
        0x8,
        (
            "こんな状況ですから、\x01",
            "日曜学校の授業もしばらくは\x01",
            "お休みになっているのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x8,
        (
            "再開されたら、また元気な笑顔を\x01",
            "見せてほしいものです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BD3")

    Jump("loc_AE6D")

    label("loc_9BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9C48")

    #C0478
    ChrTalk(
        0x8,
        (
            "とんでもない事態になって\x01",
            "しまいましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x8,
        (
            "マインツの人々が\x01",
            "無事であればいいのですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE6D")

    label("loc_9C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9DBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D21")

    #C0480
    ChrTalk(
        0x8,
        (
            "今日はシスター・ハティナに、\x01",
            "アルモリカ村へ日曜学校の\x01",
            "出張に行ってもらっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x8,
        (
            "今日はクロスベル全土で\x01",
            "雨が降っているそうですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x8,
        (
            "ずぶ濡れになって\x01",
            "なければいいのですが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9DB9")

    label("loc_9D21")


    #C0483
    ChrTalk(
        0x8,
        (
            "今日はシスター・ハティナに、\x01",
            "アルモリカ村へ日曜学校の\x01",
            "出張に行ってもらっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x8,
        (
            "雨も降ってますし、\x01",
            "ずぶ濡れになって\x01",
            "なければいいのですが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DB9")

    Jump("loc_AE6D")

    label("loc_9DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9FC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F28")

    #C0485
    ChrTalk(
        0x8,
        (
            "リースさんには\x01",
            "ルフィナというお姉さんがいて、\x01",
            "私とも知己だったのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x8,
        (
            "彼女は教会の《封聖省》に所属し、\x01",
            "卓越した交渉術で様々な事件の\x01",
            "解決にあたっていました。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x8,
        (
            "いつしか《千の腕》などと呼ばれ、\x01",
            "教会でも有名な存在だったのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x8,
        (
            "……残念ながら数年前に、\x01",
            "不幸な事故で殉教されたそうですが……\x01",
            "惜しい人を亡くしたものです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9FC0")

    label("loc_9F28")


    #C0489
    ChrTalk(
        0x8,
        (
            "ルフィナさんには\x01",
            "私も昔、お世話になったことが\x01",
            "あったのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x8,
        (
            "彼女にはもう一度\x01",
            "お礼を言いたかったものですが……\x01",
            "惜しい人を亡くしたものです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FC0")

    Jump("loc_AE6D")

    label("loc_9FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A1EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A166")

    #C0491
    ChrTalk(
        0x8,
        (
            "そういえばロイドたち……\x01",
            "昨日は私を訪ねてくれた\x01",
            "そうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x8,
        (
            "何か、聞きたいことでも\x01",
            "あったのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x101,
        (
            "#00000Fいえ、それに関しては\x01",
            "とりあえずもう大丈夫です。\x02\x03",

            "#00003F（《プレロマ草》に関わることは\x01",
            "  教会でも禁忌#4Rタブー#みたいだし……\x01",
            "  先生には言わない方がいいだろう。）\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x8,
        (
            "そうですか……\x01",
            "それならいいのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x8,
        (
            "ふふ、いつでも力になりますから\x01",
            "遠慮なく頼ってくださいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A1E6")

    label("loc_A166")


    #C0496
    ChrTalk(
        0x8,
        (
            "私も、できるだけロイドたちの\x01",
            "助けになりたいと思っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x8,
        (
            "ふふ、いつでも力になりますから\x01",
            "遠慮なく頼ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1E6")

    Jump("loc_AE6D")

    label("loc_A1EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_A2F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A206")
    Call(0, 27)
    Jump("loc_A2EC")

    label("loc_A206")


    #C0498
    ChrTalk(
        0x8,
        (
            "千里の道も一歩からというし……\x01",
            "ひとつずつ、覚えていけばいいのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x101,
        (
            "#00008F（大司教の話だと、\x01",
            "  あの蒼い花の事は\x01",
            "  先生も知らないそうだし……）\x02\x03",

            "#00003F（やはりリースさんを訪ねてみよう。\x01",
            "  礼拝堂前の寄宿舎にいるはずだ。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2EC")

    Jump("loc_AE6D")

    label("loc_A2F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_A460")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3BC")

    #C0500
    ChrTalk(
        0x8,
        (
            "クロスベル自治州には、\x01",
            "帝国と共和国に税収の１０％を\x01",
            "収める決まりがあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x8,
        (
            "これは、宗主国である２大国に\x01",
            "定められた、自治州成立当初からある\x01",
            "自治州法の一つであり……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A45B")

    label("loc_A3BC")


    #C0502
    ChrTalk(
        0x8,
        (
            "つまり、もし独立が成立すれば\x01",
            "クロスベルはこれらの不利な決まりから\x01",
            "解放されることになるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x8,
        (
            "もちろん、決して口で言うほど\x01",
            "簡単ではありませんが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A45B")

    Jump("loc_AE6D")

    label("loc_A460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A60A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A551")

    #C0504
    ChrTalk(
        0x8,
        (
            "一所懸命さというものは\x01",
            "子供たちに正面から伝わります。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x8,
        (
            "そうすれば、難しい授業でも\x01",
            "熱心に聞いてくれるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x8,
        (
            "シスター・ジュジュの授業は\x01",
            "まだ、たどたどしいですが、\x01",
            "一所懸命さに関しては合格点ですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A605")

    label("loc_A551")


    #C0507
    ChrTalk(
        0x8,
        (
            "シスター・ジュジュの授業は\x01",
            "まだ、たどたどしいですが\x01",
            "一所懸命さに関しては合格点です。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x8,
        (
            "あとは基本的な教え方さえ\x01",
            "身につければ、きっといい授業が\x01",
            "できるようになるでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A605")

    Jump("loc_AE6D")

    label("loc_A60A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A87D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A6B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A631")
    Call(0, 21)
    Jump("loc_A6AF")

    label("loc_A631")


    #C0509
    ChrTalk(
        0x8,
        (
            "リースさんの仕事柄、\x01",
            "仕方ないことだとは思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x8,
        (
            "……ロイドたちも、若いからと言って\x01",
            "無理ばかりしてはだめですよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6AF")

    Jump("loc_A878")

    label("loc_A6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7F7")

    #C0511
    ChrTalk(
        0x8,
        (
            "クローディア殿下は、\x01",
            "少し前にあったリベールの異変の\x01",
            "解決に貢献したそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x8,
        (
            "そんな大変な事件の最中、\x01",
            "彼女は王太女の儀を済ませ\x01",
            "リベールの次期女王となりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x8,
        (
            "そこに至るまでに\x01",
            "どれほどの葛藤があったのか、\x01",
            "窺い知ることはできませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x8,
        (
            "お若いのに、大変芯の強い\x01",
            "お方なのでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A878")

    label("loc_A7F7")


    #C0515
    ChrTalk(
        0x8,
        (
            "クローディア殿下は\x01",
            "リベールの異変の最中\x01",
            "王太女の儀を済ませたと言います。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x8,
        (
            "お若いのに、大変芯の強い\x01",
            "お方なのでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A878")

    Jump("loc_AE6D")

    label("loc_A87D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A9FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A95D")

    #C0517
    ChrTalk(
        0x8,
        (
            "そういえば今日は、\x01",
            "除幕式の日でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x8,
        (
            "地上４０階の建造物ともなれば、\x01",
            "子供たちが見上げれば\x01",
            "天まで届くような迫力でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x8,
        (
            "ふふ、子供たちは今頃\x01",
            "はしゃいでいるところじゃ\x01",
            "ないかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A9F5")

    label("loc_A95D")


    #C0520
    ChrTalk(
        0x8,
        (
            "地上４０階の建造物ともなれば、\x01",
            "子供たちが見上げれば\x01",
            "天まで届くような迫力でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x8,
        (
            "ふふ、子供たちは今頃\x01",
            "はしゃいでいるところじゃ\x01",
            "ないかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9F5")

    Jump("loc_AE6D")

    label("loc_A9FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_AB3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AACE")

    #C0522
    ChrTalk(
        0x8,
        (
            "いよいよ通商会議が\x01",
            "明日に迫りましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x8,
        (
            "色々大変でしょうが……\x01",
            "あなたたちもがんばるのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x101,
        "#00000Fはい、頑張ります！\x02",
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x102,
        (
            "#00100Fありがとうございます、\x01",
            "マーブル先生。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_AB3A")

    label("loc_AACE")


    #C0526
    ChrTalk(
        0x8,
        (
            "色々大変でしょうが……\x01",
            "あなたたちもがんばるのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x8,
        (
            "私も陰ながら応援させて\x01",
            "いただきますからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB3A")

    Jump("loc_AE6D")

    label("loc_AB3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_ABC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB5A")
    Call(0, 20)
    Jump("loc_ABC2")

    label("loc_AB5A")


    #C0528
    ChrTalk(
        0x8,
        (
            "おや、ロイドたち……\x01",
            "こんな雨の日にお出かけかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x8,
        (
            "風邪を引かないように\x01",
            "気をつけるのですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABC2")

    Jump("loc_AE6D")

    label("loc_ABC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_ADD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD4C")
    TurnDirection(0x8, 0x153, 0)

    #C0530
    ChrTalk(
        0x8,
        (
            "ふふ、キーアちゃん。\x01",
            "次の年長クラスを\x01",
            "楽しみにしていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x8,
        (
            "今度はもう少し難しい問題を\x01",
            "用意していますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x153,
        (
            "#01109Fうん、わかったー。\x01",
            "キーア、がんばって予習するね！\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x109,
        (
            "#10104Fう～ん、本当に凄いなあ……\x01",
            "感心しちゃいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、そのうち僕らも\x01",
            "追い越されちゃうかもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x101,
        (
            "#00006Fうーん、そうなったら\x01",
            "さすがに立つ瀬がないな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_ADD3")

    label("loc_AD4C")


    #C0536
    ChrTalk(
        0x8,
        (
            "キーアちゃんが来てから、\x01",
            "年長クラスの授業にも\x01",
            "より活気が出てきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x8,
        (
            "ふふ、他の子たちにも\x01",
            "いい刺激になっているようですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADD3")

    Jump("loc_AE6D")

    label("loc_ADD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_ADE6")
    Jump("loc_AE6D")

    label("loc_ADE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_AE6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE01")
    Call(0, 24)
    Jump("loc_AE6D")

    label("loc_AE01")


    #C0538
    ChrTalk(
        0x8,
        (
            "ふふ、それじゃああなたたち。\x01",
            "私は授業の続きがあるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x8,
        (
            "また別の機会にでも\x01",
            "遊びに来てちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE6D")

    TalkEnd(0x8)
    Return()

    # Function_23_9105 end

    def Function_24_AE71(): pass

    label("Function_24_AE71")

    EventBegin(0x0)
    Fade(500)
    OP_68(152600, 1700, 16650, 0)
    MoveCamera(322, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27870, 0)
    OP_93(0x8, 0xB4, 0x0)
    SetChrPos(0x101, 153000, 200, 16800, 270)
    SetChrPos(0x102, 153300, 200, 17700, 270)
    SetChrPos(0x109, 154200, 200, 17580, 270)
    SetChrPos(0x105, 153900, 200, 16580, 270)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    #C0540
    ChrTalk(
        0x8,
        (
            "まあ、ロイドにエリィ……\x01",
            "よく来てくれたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x101,
        "#00000Fお久しぶりです、マーブル先生。\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x102,
        (
            "#00105Fご無沙汰してます……\x01",
            "って、あまり驚かれてないですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x8,
        (
            "ふふ、さっきキーアちゃんが\x01",
            "『帰ってきた～！』って\x01",
            "嬉しそうに話してましたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x109,
        (
            "#10100F確か、ロイドさんとエリィさんの、\x01",
            "日曜学校時代の先生……でしたっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x8,
        (
            "ええ、そうよ。\x01",
            "そういうあなたたちは\x01",
            "支援課の新しいメンバーみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x8,
        (
            "私は七耀教会のシスター、\x01",
            "マーブルと申します。\x01",
            "よろしくおねがいしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x101,
        (
            "#00005Fあれ、そういえば……\x01",
            "ノエルはマーブル先生には\x01",
            "習っていなかったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x109,
        (
            "#10100Fええ、当時私とフランが通っていた\x01",
            "東通りのクラスは、\x01",
            "神父様が受け持ってたんですよ。\x02\x03",

            "#10103F今はクロスベルには\x01",
            "いらっしゃらないみたいですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x105,
        (
            "#10304Fまあ、教会の司祭が\x01",
            "異動するなんてことは\x01",
            "ままあることだろうしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x8,
        (
            "ふふ、そういう意味では\x01",
            "ロイドとエリィとの再会も\x01",
            "なかなかの幸運でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x12,
        (
            "マーブル先生～、\x01",
            "兄ちゃんたちとばっかり\x01",
            "話してないで授業しようぜ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x13,
        (
            "もう、リュウってば。\x01",
            "せっかくの再会みたいだし\x01",
            "水を差さないであげようよ～。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0553
    ChrTalk(
        0x8,
        (
            "あらあら、ごめんなさい。\x01",
            "つい嬉しくて話し込んじゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x8,
        (
            "ふふ、それじゃああなたたち、\x01",
            "私は授業の続きがあるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x8,
        (
            "また別の機会にでも\x01",
            "遊びに来てちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x101,
        (
            "#00005Fす、すみません、\x01",
            "授業の邪魔をしてしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x102,
        (
            "#00100Fえっと、それじゃあ\x01",
            "失礼しますね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 153260, 200, 16760, 270)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x135, 2)
    EventEnd(0x5)
    Return()

    # Function_24_AE71 end

    def Function_25_B49E(): pass

    label("Function_25_B49E")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B58E")

    #C0558
    ChrTalk(
        0xF,
        (
            "えっとですね。\x01",
            "要するに、先日行われた\x01",
            "通商会議というのは……\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0xF,
        (
            "いわゆる\x01",
            "経済関係の取り決めを……\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x18,
        (
            "先生、ちょっとよく\x01",
            "分かりません。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xF)

    #C0561
    ChrTalk(
        0xF,
        (
            "え、えっと、それじゃあ、\x01",
            "もう一度最初から……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_B604")

    label("loc_B58E")


    #C0562
    ChrTalk(
        0xF,
        (
            "（うう、ちょっと扱う課題が\x01",
            "  難しすぎたかしら……）\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xF,
        (
            "（で、でも大事な事だから\x01",
            "  しっかり教えないとっ……！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B604")

    TalkEnd(0xF)
    Return()

    # Function_25_B49E end

    def Function_26_B608(): pass

    label("Function_26_B608")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B619")
    Jump("loc_BC33")

    label("loc_B619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B627")
    Jump("loc_BC33")

    label("loc_B627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B635")
    Jump("loc_BC33")

    label("loc_B635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B73C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6BD")

    #C0564
    ChrTalk(
        0xFE,
        (
            "雨の日は\x01",
            "床が滑りやすいですから\x01",
            "注意してくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0xFE,
        (
            "……さっき、私も滑って\x01",
            "転んじゃいましたから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_B737")

    label("loc_B6BD")


    #C0566
    ChrTalk(
        0xFE,
        (
            "はあ、今日は日曜学校が休みで\x01",
            "本当に良かったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0xFE,
        (
            "あんな場面子供たちに見られてたら\x01",
            "もっとなめられちゃいます……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B737")

    Jump("loc_BC33")

    label("loc_B73C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_B74A")
    Jump("loc_BC33")

    label("loc_B74A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B758")
    Jump("loc_BC33")

    label("loc_B758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_B7E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B773")
    Call(0, 27)
    Jump("loc_B7E3")

    label("loc_B773")


    #C0568
    ChrTalk(
        0xFE,
        (
            "シスター・マーブルの教えは\x01",
            "本当に勉強になります。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0xFE,
        (
            "いつか、彼女のような\x01",
            "立派なシスターになりたいです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7E3")

    Jump("loc_BC33")

    label("loc_B7E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_B905")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B892")

    #C0570
    ChrTalk(
        0xFE,
        (
            "やっぱりシスター・マーブルの授業は\x01",
            "タメになりますねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xFE,
        (
            "はっ、いけないいけない。\x01",
            "普通に授業を聞くんじゃなくて、\x01",
            "参考にしないと……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_B900")

    label("loc_B892")


    #C0572
    ChrTalk(
        0xFE,
        (
            "シスター・マーブルの授業を見て\x01",
            "教え方を勉強してるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xFE,
        (
            "でも、ついつい\x01",
            "聞き入っちゃうんですよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B900")

    Jump("loc_BC33")

    label("loc_B905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BA76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9FB")

    #C0574
    ChrTalk(
        0xFE,
        (
            "えっとですね。\x01",
            "要するに、先日行われた\x01",
            "通商会議というのは……\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0xFE,
        (
            "いわゆる\x01",
            "経済関係の取り決めを……\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x18,
        (
            "先生、ちょっとよく\x01",
            "分かりません。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0577
    ChrTalk(
        0xFE,
        (
            "え、えっと、それじゃあ、\x01",
            "もう一度最初から……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_BA71")

    label("loc_B9FB")


    #C0578
    ChrTalk(
        0xFE,
        (
            "（うう、ちょっと扱う課題が\x01",
            "  難しすぎたかしら……）\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0xFE,
        (
            "（で、でも大事な事だから\x01",
            "  しっかり教えないとっ……！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA71")

    Jump("loc_BC33")

    label("loc_BA76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_BA84")
    Jump("loc_BC33")

    label("loc_BA84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_BA92")
    Jump("loc_BC33")

    label("loc_BA92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BAA0")
    Jump("loc_BC33")

    label("loc_BAA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_BC0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB87")

    #C0580
    ChrTalk(
        0xFE,
        (
            "シスター・リースって、\x01",
            "アルテリアで何年か\x01",
            "シスターをやってたみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0xFE,
        (
            "歳は同じくらいだけど、\x01",
            "私よりもよっぽど落ち着いてるし……\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xFE,
        (
            "はあ、えらそうに先輩ぶろうとした\x01",
            "自分が恥ずかしいです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_BC09")

    label("loc_BB87")


    #C0583
    ChrTalk(
        0xFE,
        (
            "はあ、まさかシスター・リースが\x01",
            "何年も先輩だったなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0xFE,
        (
            "後輩ができたと思って喜んでた自分が、\x01",
            "なんだか恥ずかしいです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC09")

    Jump("loc_BC33")

    label("loc_BC0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_BC1C")
    Jump("loc_BC33")

    label("loc_BC1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_BC2A")
    Jump("loc_BC33")

    label("loc_BC2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_BC33")

    label("loc_BC33")

    TalkEnd(0xFE)
    Return()

    # Function_26_B608 end

    def Function_27_BC37(): pass

    label("Function_27_BC37")

    OP_4B(0xF, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0585
    ChrTalk(
        0xF,
        (
            "シスター・マーブル。\x01",
            "今日はとても勉強になりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0xF,
        (
            "その、年少クラスの授業では\x01",
            "情けないところを見せて\x01",
            "しまいましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x8,
        "ふふ、気にしなくていいわ。\x02",
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x8,
        (
            "千里の道も一歩からというし……\x01",
            "ひとつずつ、覚えていけばいいのよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_27_BC37 end

    def Function_28_BD3F(): pass

    label("Function_28_BD3F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD54")
    Call(0, 50)
    Jump("loc_BDC8")

    label("loc_BD54")


    #C0589
    ChrTalk(
        0x11,
        (
            "#01100Fキーア、日曜学校大好きだよ。\x02\x03",

            "#01109F毎日色々勉強できるし、\x01",
            "リュウやアンリたちと\x01",
            "会うのも楽しいんだー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDC8")

    TalkEnd(0xFE)
    Return()

    # Function_28_BD3F end

    def Function_29_BDCC(): pass

    label("Function_29_BDCC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEC0")

    #C0590
    ChrTalk(
        0xFE,
        (
            "うー、やっぱ勉強って\x01",
            "めんどくせーよなー……\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0xFE,
        (
            "兄ちゃん、ちょっと\x01",
            "俺の代わりに勉強してくれない？\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x101,
        (
            "#00006Fあのな……自分のためだろ？\x01",
            "しっかりやったほうがいいぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0xFE,
        (
            "ちぇっ、父ちゃんみたいなこと\x01",
            "言ってやがんの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_BEEB")

    label("loc_BEC0")


    #C0594
    ChrTalk(
        0xFE,
        (
            "うー、やっぱ勉強って\x01",
            "めんどくせー……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BEEB")

    TalkEnd(0xFE)
    Return()

    # Function_29_BDCC end

    def Function_30_BEEF(): pass

    label("Function_30_BEEF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF94")
    SetChrSubChip(0x13, 0x1)
    Sleep(500)
    SetChrSubChip(0x12, 0x2)
    Sleep(500)

    #C0595
    ChrTalk(
        0xFE,
        "リュウ、ちゃんとしなよ。\x02",
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xFE,
        (
            "このままじゃキーアちゃんに\x01",
            "置いてかれるばっかりだよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x12,
        "わ、分かってるってば。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x13, 0x0)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x13, 0x10)
    SetScenarioFlags(0x1, 2)
    Jump("loc_BFFC")

    label("loc_BF94")


    #C0598
    ChrTalk(
        0xFE,
        (
            "僕も、リュウのことばかり\x01",
            "言ってられませんよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0xFE,
        (
            "キーアちゃんに\x01",
            "負けないようにがんばらないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFFC")

    TalkEnd(0xFE)
    Return()

    # Function_30_BEEF end

    def Function_31_C000(): pass

    label("Function_31_C000")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C0ED")
    OP_63(0x14, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x14)

    #C0600
    ChrTalk(
        0xFE,
        "うんと、えっと……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x14, 0x1)
    Sleep(500)
    SetChrSubChip(0x11, 0x2)
    Sleep(500)

    #C0601
    ChrTalk(
        0xFE,
        (
            "ねえキーアちゃん……\x01",
            "ここってどうすればいいんだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x11,
        "#01100Fえっと、ここの計算はねー……\x02",
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x101,
        (
            "#00002F（はは……\x01",
            "  仲良くやってるみたいだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_C120")

    label("loc_C0ED")


    #C0604
    ChrTalk(
        0xFE,
        (
            "そ、そっか……\x01",
            "こういうふうにやればいいんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C120")

    TalkEnd(0xFE)
    Return()

    # Function_31_C000 end

    def Function_32_C124(): pass

    label("Function_32_C124")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3B4")

    #C0605
    ChrTalk(
        0x101,
        (
            "#00000Fやあ、パンセじゃないか。\x01",
            "元気にしてたかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0xFE,
        (
            "あ、お兄さんって\x01",
            "ウェンディお姉ちゃんの\x01",
            "お友達だっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0xFE,
        (
            "どーもお久しぶり、\x01",
            "お世話になってマス。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 6)), scpexpr(EXPR_END)), "loc_C26E")

    #C0608
    ChrTalk(
        0x105,
        "#10305Fウェンディっていうと、確か……\x02",
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x102,
        (
            "#00100Fええ、さっき会った\x01",
            "オーバルストアの技師さんよ。\x02\x03",

            "#00109Fふふ、ロイドの幼馴染なのよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2EE")

    label("loc_C26E")


    #C0610
    ChrTalk(
        0x105,
        "#10305Fウェンディっていうと……\x02",
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x102,
        (
            "#00100Fオーバルストアにいる\x01",
            "技師さんのことよ。\x02\x03",

            "#00109Fふふ、ロイドの幼馴染なのよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2EE")


    #C0612
    ChrTalk(
        0xFE,
        (
            "そー、そのメカオタクが\x01",
            "あたしのお姉ちゃんなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x109,
        "#10112Fず、随分な言い様だね。\x02",
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0xFE,
        (
            "でも、本当のことだもん。\x01",
            "お兄さんもそう思うでしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x101,
        "#00006F（……確かに、否定はしないな。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x135, 1)
    Jump("loc_C423")

    label("loc_C3B4")


    #C0616
    ChrTalk(
        0xFE,
        (
            "お姉ちゃんが\x01",
            "メカオタクになったのは、\x01",
            "おとーさんの影響なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0xFE,
        (
            "私はぜったい、\x01",
            "そーはならないんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C423")

    TalkEnd(0xFE)
    Return()

    # Function_32_C124 end

    def Function_33_C427(): pass

    label("Function_33_C427")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C438")
    Jump("loc_C5F7")

    label("loc_C438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C4AF")

    #C0618
    ChrTalk(
        0xFE,
        "今日はミサなんだってさ。\x02",
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0xFE,
        (
            "俺たちも普段は遊んでばっかだけど、\x01",
            "こういうときはビシッとしないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5F7")

    label("loc_C4AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C4BD")
    Jump("loc_C5F7")

    label("loc_C4BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C4CB")
    Jump("loc_C5F7")

    label("loc_C4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C4D9")
    Jump("loc_C5F7")

    label("loc_C4D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C4E7")
    Jump("loc_C5F7")

    label("loc_C4E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_C4F5")
    Jump("loc_C5F7")

    label("loc_C4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_C503")
    Jump("loc_C5F7")

    label("loc_C503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C511")
    Jump("loc_C5F7")

    label("loc_C511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C51F")
    Jump("loc_C5F7")

    label("loc_C51F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C52D")
    Jump("loc_C5F7")

    label("loc_C52D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C53B")
    Jump("loc_C5F7")

    label("loc_C53B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C549")
    Jump("loc_C5F7")

    label("loc_C549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_C557")
    Jump("loc_C5F7")

    label("loc_C557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_C565")
    Jump("loc_C5F7")

    label("loc_C565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C5F7")

    #C0620
    ChrTalk(
        0xFE,
        (
            "ちぇっ、ハミルのやつ\x01",
            "キーアにいいトコ見せたいからって\x01",
            "最近ハリキってんだよなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0xFE,
        (
            "俺は勉強なんかより\x01",
            "外で遊んでる方が好きだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5F7")

    TalkEnd(0xFE)
    Return()

    # Function_33_C427 end

    def Function_34_C5FB(): pass

    label("Function_34_C5FB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C60C")
    Jump("loc_C7A2")

    label("loc_C60C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C65A")

    #C0622
    ChrTalk(
        0xFE,
        (
            "女神様……\x01",
            "どうか街のみんなを\x01",
            "元気にしてあげてください……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7A2")

    label("loc_C65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C668")
    Jump("loc_C7A2")

    label("loc_C668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C676")
    Jump("loc_C7A2")

    label("loc_C676")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C684")
    Jump("loc_C7A2")

    label("loc_C684")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C692")
    Jump("loc_C7A2")

    label("loc_C692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_C6A0")
    Jump("loc_C7A2")

    label("loc_C6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_C6AE")
    Jump("loc_C7A2")

    label("loc_C6AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C6BC")
    Jump("loc_C7A2")

    label("loc_C6BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C6CA")
    Jump("loc_C7A2")

    label("loc_C6CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C6D8")
    Jump("loc_C7A2")

    label("loc_C6D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C6E6")
    Jump("loc_C7A2")

    label("loc_C6E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C6F4")
    Jump("loc_C7A2")

    label("loc_C6F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_C702")
    Jump("loc_C7A2")

    label("loc_C702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_C710")
    Jump("loc_C7A2")

    label("loc_C710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C7A2")

    #C0623
    ChrTalk(
        0xFE,
        (
            "はあ～……\x01",
            "キーアちゃん、かわいいなあ。\x01",
            "一緒に勉強できて嬉しいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0xFE,
        (
            "今日もいっぱい手をあげて、\x01",
            "ばんばん問題に答えてかないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7A2")

    TalkEnd(0xFE)
    Return()

    # Function_34_C5FB end

    def Function_35_C7A6(): pass

    label("Function_35_C7A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C83E")

    #C0625
    ChrTalk(
        0xFE,
        (
            "僕はお買い物が好きだし、\x01",
            "経済のことには\x01",
            "興味があるんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0xFE,
        (
            "この間の通商会議のことは\x01",
            "まだまだ僕らには難しいですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_C873")

    label("loc_C83E")


    #C0627
    ChrTalk(
        0xFE,
        (
            "通商会議のことは\x01",
            "まだまだ僕らには難しいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C873")

    TalkEnd(0xFE)
    Return()

    # Function_35_C7A6 end

    def Function_36_C877(): pass

    label("Function_36_C877")

    TalkBegin(0xFE)

    #C0628
    ChrTalk(
        0xFE,
        (
            "この話って、アゼル兄ちゃんなら\x01",
            "分かるのかなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0xFE,
        (
            "今度お兄ちゃんが帰ってきたら\x01",
            "聞いてみようかな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_C877 end

    def Function_37_C8EA(): pass

    label("Function_37_C8EA")

    TalkBegin(0xFE)

    #C0630
    ChrTalk(
        0xFE,
        "ふんふん……\x02",
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0xFE,
        "……やっぱりよく分かんないや。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_C8EA end

    def Function_38_C927(): pass

    label("Function_38_C927")

    TalkBegin(0xFE)

    #C0632
    ChrTalk(
        0xFE,
        (
            "ふあ～……\x01",
            "勉強すると眠くなるなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0xFE,
        (
            "でも、シスターもがんばってるし\x01",
            "ちゃんと聞いてあげなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_C927 end

    def Function_39_C99A(): pass

    label("Function_39_C99A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA3E")

    #C0634
    ChrTalk(
        0xFE,
        (
            "ふ、ふーん……\x01",
            "ツーショーカイギね……\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0xFE,
        (
            "この程度、常識よね。\x01",
            "簡単すぎて笑っちゃうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0xFE,
        (
            "……ほ、ほんとよ？\x01",
            "ほんとに分かるんだから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_CAAC")

    label("loc_CA3E")


    #C0637
    ChrTalk(
        0xFE,
        (
            "ツーショーカイギなんて常識よね。\x01",
            "簡単、簡単……\x02",
        )
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0xFE,
        (
            "……もう、あっちにいって！\x01",
            "私は勉強してるんだから！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CAAC")

    TalkEnd(0xFE)
    Return()

    # Function_39_C99A end

    def Function_40_CAB0(): pass

    label("Function_40_CAB0")

    TalkBegin(0xFE)

    #C0639
    ChrTalk(
        0xFE,
        (
            "将来のためにも、難しいことでも\x01",
            "きちんと勉強しないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0xFE,
        "……お兄ちゃんたちは勉強してる？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_CAB0 end

    def Function_41_CB1A(): pass

    label("Function_41_CB1A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_CB67")

    #C0641
    ChrTalk(
        0xFE,
        "ねー、この後どこ行く？\x02",
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0xFE,
        "やっぱ百貨店のほうかなあ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_CBD0")

    label("loc_CB67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_CBD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB82")
    Call(0, 42)
    Jump("loc_CBD0")

    label("loc_CB82")


    #C0643
    ChrTalk(
        0xFE,
        (
            "（リナリー……\x01",
            "  あんたのせいであたしまで\x01",
            "  怒られちゃったじゃ～ん……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CBD0")

    TalkEnd(0xFE)
    Return()

    # Function_41_CB1A end

    def Function_42_CBD4(): pass

    label("Function_42_CBD4")


    #C0644
    ChrTalk(
        0x1F,
        (
            "シスターって、\x01",
            "簡単なダイエットとか\x01",
            "知らないかなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x1E,
        (
            "あんた、授業中に\x01",
            "バカなこと聞こうとするのは\x01",
            "やめときなさいって。\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x1E,
        "また怒られるよー？\x02",
    )

    CloseMessageWindow()
    OP_4B(0x8, 0xFF)

    #C0647
    ChrTalk(
        0x8,
        (
            "ふふ、そこのお二人さん。\x01",
            "授業中はお静かにね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    Sleep(1000)

    #C0648
    ChrTalk(
        0x1F,
        "はーい……\x02",
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x1E,
        (
            "は、はーい……\x01",
            "（あたしまで怒られちゃった……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x2)
    SetChrSubChip(0x1F, 0x1)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x1, 7)
    Return()

    # Function_42_CBD4 end

    def Function_43_CD03(): pass

    label("Function_43_CD03")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_CD3A")

    #C0650
    ChrTalk(
        0xFE,
        "あたしらもホント飽きないよねー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CD6F")

    label("loc_CD3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_CD6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD55")
    Call(0, 42)
    Jump("loc_CD6F")

    label("loc_CD55")


    #C0651
    ChrTalk(
        0xFE,
        "（ご、ごめ～ん……）\x02",
    )

    CloseMessageWindow()

    label("loc_CD6F")

    TalkEnd(0xFE)
    Return()

    # Function_43_CD03 end

    def Function_44_CD73(): pass

    label("Function_44_CD73")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_CDFA")

    #C0652
    ChrTalk(
        0xFE,
        (
            "いや、今日は独立について\x01",
            "学べてよかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0xFE,
        (
            "クロスベルタイムズを読むだけじゃ\x01",
            "見えてこないものもあるもんな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE54")

    label("loc_CDFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_CE54")

    #C0654
    ChrTalk(
        0xFE,
        "なるほどなるほど……\x02",
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0xFE,
        (
            "マーブル先生の授業は、\x01",
            "やっぱり分かりやすいなあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE54")

    TalkEnd(0xFE)
    Return()

    # Function_44_CD73 end

    def Function_45_CE58(): pass

    label("Function_45_CE58")

    TalkBegin(0xFE)

    #C0656
    ChrTalk(
        0xFE,
        (
            "年長クラスの授業は\x01",
            "やっぱり難しいな……\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0xFE,
        "きっちり予習するんだったよ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_CE58 end

    def Function_46_CEAE(): pass

    label("Function_46_CEAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF7C")

    #C0658
    ChrTalk(
        0xFE,
        (
            "あれ、今日は\x01",
            "あのキーアちゃんって子、\x01",
            "来てないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0xFE,
        (
            "……ああ、そういえば\x01",
            "あの子が参加するのは\x01",
            "自然科学だけだったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0xFE,
        (
            "チェッ、今日も可愛い後姿を\x01",
            "眺めたかったんだけどな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_CFF3")

    label("loc_CF7C")


    #C0661
    ChrTalk(
        0xFE,
        (
            "いつもはキーアちゃん、\x01",
            "私の前に座ってるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0xFE,
        (
            "可愛い後頭部を\x01",
            "眺めながら授業を受けるのは\x01",
            "なかなか楽しいもんよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFF3")

    TalkEnd(0xFE)
    Return()

    # Function_46_CEAE end

    def Function_47_CFF7(): pass

    label("Function_47_CFF7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D26D")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0663
    ChrTalk(
        0xFE,
        "あら、みんな……\x02",
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x101,
        (
            "#00005Fおばさん……\x01",
            "ここにいたんだね。\x02\x03",

            "#00000Fついさっき、セシル姉が\x01",
            "支援課に来たところなんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0xFE,
        (
            "あら、そうだったの。\x01",
            "後で会いにいかないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0xFE,
        (
            "はあ……\x01",
            "クロスベルはこれから\x01",
            "どうなってしまうのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x101,
        (
            "#00003F……俺たちも、\x01",
            "正直戸惑ってるけど……\x02\x03",

            "#00000Fどんな形になっても、\x01",
            "クロスベルを守っていくって\x01",
            "気持ちは変わらないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x102,
        "#00104F……ええ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x103,
        "#00200F勿論です。\x02",
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x104,
        "#00300Fま、そういうこったな。\x02",
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0xFE,
        (
            "……ふふ、あなたたちは\x01",
            "本当に頼もしくなったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0xFE,
        (
            "うん、おかげで\x01",
            "少しだけ不安が晴れたわ。\x01",
            "声をかけてくれてありがとうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 5)
    Jump("loc_D362")

    label("loc_D26D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D326")

    #C0673
    ChrTalk(
        0xFE,
        (
            "私はここで、もうしばらく\x01",
            "お祈りをしていくことにするわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0xFE,
        (
            "これからどうなってしまうのか\x01",
            "分からないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0xFE,
        (
            "女神様なら、きっと私たちを\x01",
            "導いてくださるわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_D362")

    label("loc_D326")

    OP_93(0xFE, 0x0, 0x0)

    #C0676
    ChrTalk(
        0xFE,
        (
            "空の女神よ……\x01",
            "どうか私たちをお守りください……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D362")

    TalkEnd(0xFE)
    Return()

    # Function_47_CFF7 end

    def Function_48_D366(): pass

    label("Function_48_D366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D378")
    Call(0, 49)
    Jump("loc_D414")

    label("loc_D378")

    TalkBegin(0xFF)
    SetChrName("")

    #A0677
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "部屋の中でシスター・リースが\x01",
            "大司教に挨拶をしているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0678
    ChrTalk(
        0x101,
        (
            "#00000F……ひとまずキーアを迎えに行こう。\x01",
            "日曜学校の教室にいるはずだ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_D414")

    Return()

    # Function_48_D366 end

    def Function_49_D415(): pass

    label("Function_49_D415")

    EventBegin(0x0)
    Fade(500)
    OP_68(50010, 1500, 11920, 0)
    MoveCamera(320, 24, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28290, 0)
    SetChrPos(0x101, 49000, 0, 12340, 0)
    SetChrPos(0x102, 51000, 0, 12340, 0)
    SetChrPos(0x109, 49500, 0, 11330, 0)
    SetChrPos(0x105, 50500, 0, 11330, 0)
    SetChrFlags(0xC, 0x80)
    OP_0D()

    #C0679
    ChrTalk(
        0x102,
        (
            "#12P#00100Fここは確か、\x01",
            "エラルダ大司教のお部屋よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x101,
        (
            "#6P#00005Fん……？\x01",
            "中から声が聞こえるな。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0xA, 0xFF)
    LoadChrToIndex("chr/ch11500.itc", 0x1E)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    OP_68(100890, 1500, 8200, 0)
    MoveCamera(314, 21, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28290, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0681
    ChrTalk(
        0xA,
        (
            "#6P#13800F……それでは、本日より\x01",
            "お世話にならせていただきます。\x02\x03",

            "#13803F若輩者ではありますが、\x01",
            "どうかよろしくご鞭撻のほどを……\x02",
        )
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0x9,
        (
            "#11P……待ちたまえ。\x01",
            "君の『アルジェント』という名は……\x02",
        )
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0x9,
        (
            "#11P確かにアルテリア法国より、\x01",
            "新人の赴任が連絡されてはいたが、\x01",
            "まさか……\x02",
        )
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0xA,
        (
            "#6P#13803F……何か、問題でも\x01",
            "ありましたでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x9,
        "#11P…………いや、なんでもない。\x02",
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x9,
        (
            "#11P歓迎させていただこう、\x01",
            "シスター・リース。\x01",
            "これから頑張ってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0xA,
        (
            "#6P#13802Fありがとうございます。\x02\x03",

            "#13804F女神の名の下に、\x01",
            "謹んで勤めさせていただきます。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    OP_4C(0xA, 0xFF)
    OP_D7(0x1E)
    OP_68(50010, 1500, 11920, 0)
    MoveCamera(320, 24, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28290, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0688
    ChrTalk(
        0x109,
        (
            "#6P#10105Fこれって……\x01",
            "さっきのリースさんの声ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x105,
        (
            "#12P#10304Fどうやら、大司教殿に\x01",
            "赴任の挨拶をしているみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0690
    ChrTalk(
        0x102,
        (
            "#12P#00103F……みんな。\x01",
            "立ち聞きはよくないわ。\x02\x03",

            "#00100F今はキーアちゃんを\x01",
            "迎えにいきましょう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0691
    ChrTalk(
        0x101,
        "#5P#00000Fああ、それもそうだな。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 50430, 0, 4030, 360)
    BeginChrThread(0xC, 0, 0, 3)
    SetScenarioFlags(0x134, 7)
    SetChrPos(0x0, 50280, 0, 12000, 180)
    EventEnd(0x5)
    Return()

    # Function_49_D415 end

    def Function_50_D912(): pass

    label("Function_50_D912")

    EventBegin(0x0)
    Fade(500)
    OP_68(152600, 1000, 8640, 0)
    MoveCamera(15, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(24640, 0)
    SetChrPos(0x101, 151610, 0, 8490, 90)
    SetChrPos(0x102, 151620, 0, 9490, 90)
    SetChrPos(0x109, 150550, 0, 7660, 90)
    SetChrPos(0x105, 150560, 0, 8880, 90)
    SetChrPos(0x11, 153620, 150, 9130, 270)
    SetChrSubChip(0x11, 0x1)
    OP_0D()

    #C0692
    ChrTalk(
        0x11,
        (
            "#11P#01105Fあ、ロイドたちだー。\x02\x03",

            "#01100F今日って授業参観だっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x101,
        (
            "#6P#00000Fああいや、\x01",
            "そういうわけじゃないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x109,
        (
            "#6P#10100Fキーアちゃん、\x01",
            "お勉強がんばってる？\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x11,
        (
            "#11P#01110Fうん！\x02\x03",

            "#01109F毎日色々勉強できるし、\x01",
            "リュウやアンリたちと\x01",
            "会うのも楽しいよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x102,
        "#5P#00102Fふふ、そっか。\x02",
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0x105,
        (
            "#6P#10300Fふうん、結構\x01",
            "馴染んでるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x101,
        (
            "#6P#00004Fああ、最初は心配してたけど……\x01",
            "正直杞憂だったと思うよ。\x02\x03",

            "#00000Fキーア、しっかりがんばるんだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x11,
        (
            "#11P#01109Fうんー！\x01",
            "ロイドたちもお仕事、\x01",
            "がんばってねー！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x135, 0)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 151150, 0, 8870, 90)
    SetChrPos(0x11, 153620, 150, 9130, 0)
    SetChrSubChip(0x11, 0x0)
    EventEnd(0x5)
    Return()

    # Function_50_D912 end

    def Function_51_DBE9(): pass

    label("Function_51_DBE9")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch20400.itc", 0x1E)
    SoundLoad(3598)
    OP_68(9000, 1000, 2500, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x101, 9500, 0, 2500, 90)
    SetChrPos(0x102, 8750, 0, 2000, 90)
    SetChrPos(0x109, 8150, 0, 3200, 90)
    SetChrPos(0x105, 7350, 0, 2750, 90)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrChipByIndex(0x1E, 0x11)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    SetChrChipByIndex(0x1F, 0x12)
    SetChrSubChip(0x1F, 0x0)
    EndChrThread(0x1F, 0x0)
    SetChrBattleFlags(0x1F, 0x4)
    SetChrChipByIndex(0x20, 0x13)
    SetChrSubChip(0x20, 0x0)
    EndChrThread(0x20, 0x0)
    SetChrBattleFlags(0x20, 0x4)
    SetChrChipByIndex(0x21, 0x14)
    SetChrSubChip(0x21, 0x0)
    EndChrThread(0x21, 0x0)
    SetChrBattleFlags(0x21, 0x4)
    SetChrChipByIndex(0x22, 0x15)
    SetChrSubChip(0x22, 0x0)
    EndChrThread(0x22, 0x0)
    SetChrBattleFlags(0x22, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0700
    ChrTalk(
        0x101,
        "#00005F#5Pあれっ……？\x02",
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x102,
        "#00105F#5Pどうしたの？\x02",
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x101,
        (
            "#00008F#5Pいや、まだ授業を\x01",
            "やってるみたいだけど──\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    AddParty(0x52, 0xFF, 0xFF)
    SetChrPos(0x153, 151000, 200, 18000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 148500, 200, 18000, 90)
    OP_4B(0x8, 0xFF)
    OP_68(151000, 1600, 10500, 0)
    MoveCamera(324, 18, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29710, 0)
    OP_68(151000, 1600, 15500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0703
    ChrTalk(
        0x153,
        (
            "#01105F#5Pえっと、ここの式が\x01",
            "こうなって、こうなるから……\x02\x03",

            "#01101F…………………（カリカリカリ）\x02\x03",

            "#01109Fはいっ、答えは\x01",
            "５１２平方セルジュでーす！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(837, 0, 100, 0)
    SetChrName("年長の生徒たち")
    SetMessageWindowPos(50, 150, -1, -1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #A0704
    AnonymousTalk(
        0xFF,
        "#4Sおお～っ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0705
    ChrTalk(
        0x8,
        "#5Pはい、正解です。\x02",
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x8,
        (
            "#5P式の展開がユニークでしたけど\x01",
            "今、自分で考えたのですか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x8, 500)

    #C0707
    ChrTalk(
        0x153,
        (
            "#01104F#11Pえへへ、こっちのやり方のほうが\x01",
            "何となく気持ちよかったからー。\x02\x03",

            "#01110Fキーア、まちがってた？\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x8,
        (
            "#5Pいえいえ。\x01",
            "とても素晴らしい解法でした。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(300)

    #C0709
    ChrTalk(
        0x8,
        (
            "#11P──皆さん、公式というのは\x01",
            "あくまで正解を導き出すための\x01",
            "指針の一つでしかありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0x8,
        (
            "#11P時には工夫して、楽しみながら\x01",
            "問題に挑戦してみてください。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrName("年長の生徒たち")
    SetMessageWindowPos(50, 150, -1, -1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #A0711
    AnonymousTalk(
        0xFF,
        "#4Sはいっ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(9000, 1000, 2500, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x101, 9300, 0, 2200, 45)
    SetChrPos(0x102, 9100, 0, 2950, 90)
    SetChrPos(0x109, 9000, 0, 1400, 45)
    SetChrPos(0x105, 8400, 0, 2400, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0712
    ChrTalk(
        0x101,
        "#00001F#5Pあ、あれって……\x02",
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x102,
        (
            "#00108F#5P日曜学校の\x01",
            "年長クラスの授業よね……\x02",
        )
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x109,
        (
            "#10105F#6Pキーアちゃん、凄い……\x02\x03",

            "#10106Fあの問題、あたしだったら\x01",
            "結構手こずりそうですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x105,
        (
            "#10304F#5Pいわゆる中等数学だね。\x02\x03",

            "#10302Fふーん、なかなか\x01",
            "見事な解法じゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x101,
        (
            "#00004F#5Pああ、さすがは\x01",
            "うちのキーアだよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0x102,
        (
            "#00109F#5Pそうね、キーアちゃんなら\x01",
            "あのくらいできても……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0718
    ChrTalk(
        0x101,
        "#6P#00011F#4S#1K──じゃなくて！\x02",
    )


    #C0719
    ChrTalk(
        0x102,
        "#5P#00105F#4S#1K──じゃなくて！\x02",
    )

    OP_57(0x1)
    OP_5A()

    #C0720
    ChrTalk(
        0x105,
        (
            "#10306F#5Pやれやれ。\x01",
            "少しは落ち着きなよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x109,
        (
            "#10112F#6Pと、とりあえず授業が\x01",
            "終わるのを待ちましょう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(151000, 1000, 13400, 0)
    MoveCamera(312, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(33000, 0)
    SetCameraDistance(30000, 6000)
    SetChrPos(0x101, 147750, 0, 3750, 45)
    SetChrPos(0x102, 146400, 0, 4000, 45)
    SetChrPos(0x109, 146750, 0, 2850, 45)
    SetChrPos(0x105, 145500, 0, 3150, 45)
    SetChrPos(0x153, 151400, 0, 13400, 270)
    SetChrPos(0x8, 150600, 0, 13400, 90)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x1E, 0x4)
    ClearChrBattleFlags(0x1F, 0x4)
    ClearChrBattleFlags(0x20, 0x4)
    SetChrChipByIndex(0x1E, 0x17)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x1F, 0x18)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x1E, 150000, 0, 12000, 270)
    SetChrPos(0x1F, 150550, 0, 11100, 315)
    SetChrPos(0x20, 152000, 0, 11550, 180)
    Sleep(1000)
    FadeToBright(1000, 0)

    def lambda_E50D():
        OP_9B(0x0, 0x20, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_E50D)
    Sleep(1000)
    TurnDirection(0x1E, 0x1F, 500)
    Sleep(300)

    def lambda_E52F():
        OP_93(0x1F, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_E52F)
    Sleep(50)

    def lambda_E53F():
        OP_93(0x1E, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_E53F)
    WaitChrThread(0x1F, 2)

    def lambda_E550():
        OP_9B(0x0, 0x1F, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_E550)
    Sleep(50)
    WaitChrThread(0x1E, 2)

    def lambda_E56C():
        OP_9B(0x0, 0x1E, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_E56C)
    WaitChrThread(0x1E, 1)
    WaitChrThread(0x1F, 1)
    WaitChrThread(0x20, 1)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    OP_0D()
    OP_6F(0x79)

    #C0722
    ChrTalk(
        0x101,
        "えっと、キーア？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_E5DC():
        OP_93(0x153, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_E5DC)
    Sleep(50)

    def lambda_E5EC():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_E5EC)
    OP_68(149000, 1000, 7700, 2000)
    MoveCamera(317, 22, 0, 2000)
    OP_6E(300, 2000)
    SetCameraDistance(35000, 2000)
    OP_6F(0x79)

    #C0723
    ChrTalk(
        0x8,
        "あら、あなたたち……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0724
    ChrTalk(
        0x153,
        (
            "#01105F#3598V#11P#30Wあれれ……\x01",
            "みんなどーしたの？\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE0E)
    OP_C9(0x1, 0x80000000)
    OP_68(151000, 1000, 12400, 5000)
    MoveCamera(312, 25, 0, 5000)
    SetCameraDistance(30000, 5000)

    def lambda_E6B2():
        OP_95(0xFE, 151400, 0, 4000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E6B2)
    Sleep(100)

    def lambda_E6CF():
        OP_95(0xFE, 150600, 0, 4000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E6CF)
    Sleep(500)

    def lambda_E6EC():
        OP_95(0xFE, 151400, 0, 3800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E6EC)
    Sleep(100)

    def lambda_E709():
        OP_95(0xFE, 150600, 0, 3800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E709)
    WaitChrThread(0x101, 1)

    def lambda_E727():
        OP_95(0xFE, 151400, 0, 11500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E727)
    WaitChrThread(0x102, 1)

    def lambda_E745():
        OP_95(0xFE, 150600, 0, 11300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E745)
    WaitChrThread(0x109, 1)

    def lambda_E763():
        OP_95(0xFE, 151400, 0, 10000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E763)
    WaitChrThread(0x105, 1)

    def lambda_E781():
        OP_95(0xFE, 150600, 0, 9800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E781)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    OP_6F(0x79)

    #C0725
    ChrTalk(
        0x101,
        (
            "#00006F#6Pいや、キーアが遅いから\x01",
            "迎えに来たんだけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x153, 500)
    Sleep(300)

    #C0726
    ChrTalk(
        0x102,
        (
            "#00102F#5Pそ、それよりキーアちゃん。\x01",
            "どうして年長クラスの授業を？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0727
    ChrTalk(
        0x153,
        (
            "#01112F#11Pあ……\x02\x03",

            "#01108Fえっと、そのぅ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x153, 350)

    #C0728
    ChrTalk(
        0x8,
        (
            "#5Pひょっとしてロイドたちに\x01",
            "事情を話していないのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0x153,
        "#01106F#11P……………………（コクン）\x02",
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x105,
        (
            "#10303F#6P察するに、彼女の学力は\x01",
            "かなり高いみたいだね？\x02\x03",

            "#10300F年長クラスの授業に\x01",
            "付いていけるくらいに。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 350)

    #C0731
    ChrTalk(
        0x8,
        (
            "#11Pええ、本人の希望もあって\x01",
            "少し前から年長クラスにも\x01",
            "参加してもらっているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0x8,
        (
            "#11Pと言っても、数学などの\x01",
            "自然科学に限ってですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x101,
        "#00008F#6Pそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0x102,
        (
            "#00103F#5Pまさかキーアちゃんが\x01",
            "ここまで頭がよかったなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x153,
        (
            "#01112F#11Pえっと……\x01",
            "だまっててゴメンね……？\x02\x03",

            "#01106Fキーア、まだコドモなのに\x01",
            "数学なんか勉強しちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x101,
        (
            "#00012F#6Pはは、謝ることないだろ？\x02\x03",

            "#00002Fキーアが興味あるんだったら\x01",
            "俺は反対しないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x102,
        (
            "#00104F#5Pそうね……知的好奇心は\x01",
            "そのまま延ばしてあげたいし。\x02\x03",

            "#00102Fうん、私も賛成かな。\x02",
        )
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0x153,
        "#01110F#11Pホントー！？\x02",
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0x101,
        (
            "#00004F#6Pただし、リュウたちと一緒の\x01",
            "授業もちゃんと受けるんだぞ？\x02\x03",

            "#00000F日曜学校で得られるのは\x01",
            "何も勉強だけじゃないんだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x153,
        (
            "#01109F#11Pうんっ、分かってる！\x02\x03",

            "リュウとモモに、わからない所を\x01",
            "教えてあげるのもたのしーし！\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x101,
        "#00012F#6Pそ、そっか。\x02",
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0x109,
        (
            "#10102F#6Pキーアちゃん……\x01",
            "本当に頭がいいんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x8,
        (
            "#11Pふふ、おかげで私も\x01",
            "助けられているくらいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0x8,
        (
            "#11P年長クラスへの参加は\x01",
            "週に一度くらいですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x8,
        (
            "#11P私も見ていますから\x01",
            "どうか安心してください。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 500)

    #C0746
    ChrTalk(
        0x101,
        "#00002F#6Pええ、もちろん。\x02",
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0x102,
        "#00104F#6Pよろしくお願いします。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    #C0748
    ChrTalk(
        0x105,
        (
            "#10304F#6Pフフ……\x01",
            "話がまとまったようで何より。\x02\x03",

            "#10302Fそれじゃ、日が暮れる前に\x01",
            "とっとと支援課に戻ろうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x101,
        (
            "#00004F#6Pああ、そうしよう。\x02\x03",

            "#00000Fマーブル先生。\x01",
            "それでは失礼します。\x02",
        )
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0x102,
        "#00102F#6Pどうもお疲れさまでした。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x8, 500)
    Sleep(150)

    #C0751
    ChrTalk(
        0x153,
        "#01110F#12Pセンセー、さよーなら！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x153, 350)

    #C0752
    ChrTalk(
        0x8,
        (
            "#5Pふふっ、さようなら。\x01",
            "気をつけて帰るのですよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    SetChrPos(0x8, 150800, 200, 17500, 180)
    ClearChrFlags(0x8, 0x8000)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 151000, 0, 11500, 0)
    SetScenarioFlags(0x128, 0)
    OP_29(0xA1, 0x1, 0xB)
    OP_1B(0x2, 0xFF, 0xFFFF)
    SetMapObjFlags(0x2, 0x10)
    OP_66(0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_51_DBE9 end

    def Function_52_EF84(): pass

    label("Function_52_EF84")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(150000, 1500, 10500, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(33000, 0)
    OP_68(150000, 1500, 13500, 3000)
    SetChrPos(0x101, 9300, 0, 2200, 90)
    SetChrPos(0x102, 9000, 0, 1300, 45)
    SetChrPos(0x103, 9150, 0, 3250, 135)
    SetChrPos(0x104, 8100, 0, 2700, 90)
    SetChrPos(0x109, 7250, 0, 2150, 90)
    SetChrPos(0x105, 7800, 0, 4250, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, -2500, 0, 2500, 90)
    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(8750, 1000, 2500, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30500, 0)
    SetCameraDistance(30000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0753
    ChrTalk(
        0x101,
        (
            "#00005F#5Pこの時間は年長クラスの\x01",
            "授業があるのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0x103,
        (
            "#00200F#5P今日はキーアは\x01",
            "参加してないようですが……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)

    #N0755
    NpcTalk(
        0x9,
        "威厳のある声",
        "#4P──君たち、何か用かね？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_F1ED():

        label("loc_F1ED")

        TurnDirection(0x101, 0x9, 500)
        Yield()
        Jump("loc_F1ED")

    QueueWorkItem2(0x101, 2, lambda_F1ED)

    def lambda_F1FF():

        label("loc_F1FF")

        TurnDirection(0x102, 0x9, 500)
        Yield()
        Jump("loc_F1FF")

    QueueWorkItem2(0x102, 2, lambda_F1FF)

    def lambda_F211():

        label("loc_F211")

        TurnDirection(0x103, 0x9, 500)
        Yield()
        Jump("loc_F211")

    QueueWorkItem2(0x103, 2, lambda_F211)

    def lambda_F223():

        label("loc_F223")

        TurnDirection(0x104, 0x9, 500)
        Yield()
        Jump("loc_F223")

    QueueWorkItem2(0x104, 2, lambda_F223)

    def lambda_F235():

        label("loc_F235")

        TurnDirection(0x109, 0x9, 500)
        Yield()
        Jump("loc_F235")

    QueueWorkItem2(0x109, 2, lambda_F235)

    def lambda_F247():

        label("loc_F247")

        TurnDirection(0x105, 0x9, 500)
        Yield()
        Jump("loc_F247")

    QueueWorkItem2(0x105, 2, lambda_F247)
    Sleep(500)
    OP_68(7420, 1000, 2480, 4000)

    def lambda_F26D():
        OP_9B(0x0, 0x9, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_F26D)

    #C0756
    ChrTalk(
        0x101,
        "#00011F#12Pあ……\x02",
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0x102,
        "#00105F#12Pエラルダ大司教……\x02",
    )

    CloseMessageWindow()

    #C0758
    ChrTalk(
        0x109,
        "#10112F#6Pお、お疲れさまです！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 3)
    OP_6F(0x79)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)

    #C0759
    ChrTalk(
        0x9,
        (
            "#5P君たちは確か……\x01",
            "クロスベル警察の者だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0x9,
        "#5Pシスター・マーブルに用かね？\x02",
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x101,
        (
            "#00003F#12Pは、はい。\x02\x03",

            "#00000Fその、とある植物について\x01",
            "相談したい事がありまして。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0762
    ChrTalk(
        0x9,
        "#5Pふむ、植物か。\x02",
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0x9,
        "#5Pそれは薬草か何かかね？\x02",
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x102,
        (
            "#00103F#12Pいえ、そういう訳では\x01",
            "ないんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0x104,
        (
            "#00300F#12P何でも聖典に載ってるかも\x01",
            "しれないって話ッスけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0x9,
        "#5Pほう……？\x02",
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x9,
        (
            "#5Pふむ、ならば私が\x01",
            "代わりに話を聞いてもいいが。\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0x9,
        (
            "#5Pこれでも薬草や植物全般には\x01",
            "それなりに知識があるのでね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F5C2")

    #C0769
    ChrTalk(
        0x101,
        (
            "#00002F#12Pあ、そういえば……\x01",
            "ルピナス草の件では\x01",
            "お世話になりました。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5EB")

    label("loc_F5C2")


    #C0770
    ChrTalk(
        0x101,
        "#00005F#12Pそ、そうだったんですか。\x02",
    )

    CloseMessageWindow()

    label("loc_F5EB")


    #C0771
    ChrTalk(
        0x9,
        "#5Pまあ、君たちが良ければだ。\x02",
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0x9,
        (
            "#5P私は執務室に下がっている。\x01",
            "よければ訪ねてくるがいい。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x10E, 0x1F4)
    OP_68(-9000, 1000, 2500, 6500)
    OP_9B(0x0, 0x9, 0x0, 0x3778, 0x8FC, 0x0)
    Sleep(250)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)

    def lambda_F696():
        OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_F696)
    OP_9B(0x0, 0x9, 0x0, 0x7D0, 0x7D0, 0x0)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    Sleep(250)
    WaitChrThread(0x9, 3)
    SetChrFlags(0x9, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(8750, 1000, 2500, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(31000, 0)
    OP_0D()

    #C0773
    ChrTalk(
        0x101,
        "#00001F#12Pう、うーん……\x02",
    )

    CloseMessageWindow()

    #C0774
    ChrTalk(
        0x109,
        (
            "#10106F#6P相変わらず\x01",
            "厳格そうな方ですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0x102,
        (
            "#00100F#12Pでも、せっかくだし\x01",
            "相談してみましょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0776
    ChrTalk(
        0x105,
        "#10308F#11P…………………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 9000, 0, 2500, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x161, 6)
    OP_29(0xA6, 0x1, 0x7)
    OP_1B(0x2, 0xFF, 0xFFFF)
    EventEnd(0x5)
    Return()

    # Function_52_EF84 end

    def Function_53_F804(): pass

    label("Function_53_F804")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis253.itp")
    OP_68(100000, 1000, 10600, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28000, 0)
    SetCameraDistance(27000, 1500)
    SetChrPos(0x101, 100000, 0, 2500, 0)
    SetChrPos(0x102, 101200, 0, 2250, 0)
    SetChrPos(0x103, 99000, 0, 2250, 0)
    SetChrPos(0x104, 100000, 0, 500, 0)
    SetChrPos(0x109, 101000, 0, 1000, 0)
    SetChrPos(0x105, 98750, 0, 900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 100000, 100, 10600, 180)
    SetChrChipByIndex(0x9, 0x19)
    SetChrSubChip(0x9, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(808, 0, 100, 0)
    Sleep(500)

    #C0777
    ChrTalk(
        0x101,
        (
            "#00000F#2P──失礼します。\x01",
            "特務支援課の者です。\x02",
        )
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0x9,
        "#11Pああ、入りたまえ。\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(500)
    OP_68(100000, 1000, 8500, 3000)
    MoveCamera(315, 22, 0, 3000)
    SetCameraDistance(30000, 3000)

    def lambda_F9A3():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F9A3)
    Sleep(100)

    def lambda_F9BB():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F9BB)
    Sleep(100)

    def lambda_F9D3():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F9D3)
    Sleep(100)

    def lambda_F9EB():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F9EB)
    Sleep(100)

    def lambda_FA03():
        OP_9B(0x0, 0x109, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_FA03)
    Sleep(100)

    def lambda_FA1B():
        OP_9B(0x0, 0x105, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_FA1B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    #C0779
    ChrTalk(
        0x9,
        "#11Pふむ、話を聞こうか。\x02",
    )

    CloseMessageWindow()

    #C0780
    ChrTalk(
        0x9,
        (
            "#11P聖典に載っているという\x01",
            "植物とのことだとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0x101,
        (
            "#00003F#6Pいえ、まだそうだと\x01",
            "決まったわけではありませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0782
    ChrTalk(
        0x102,
        (
            "#00101F#6Pまずは、これまでの\x01",
            "経緯を一通りお話します。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_7D(0xFF, 0xE6, 0xDC, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(600)
    OP_64(0x9)

    #C0783
    ChrTalk(
        0x9,
        (
            "#11P……時、空、識の気配に\x01",
            "不可思議なる魔獣……\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0x109,
        (
            "#10106F#6Pその、以前報告させて頂いた\x01",
            "塔や僧院の魔獣とも違っていて……\x02",
        )
    )

    CloseMessageWindow()

    #C0785
    ChrTalk(
        0x101,
        "#00005F#5P（あ、そういえば……）\x02",
    )

    CloseMessageWindow()

    #C0786
    ChrTalk(
        0x103,
        (
            "#00200F#5P（前に教会に相談してみるって\x01",
            "  言ってましたよね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0x9,
        "#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0788
    ChrTalk(
        0x9,
        (
            "#11P……その花というのは\x01",
            "今、持っているのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x101,
        (
            "#00000F#6Pあ、はい。\x01",
            "光は失われていますが……\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x101, 0x0, 0x3E8, 0x3E8, 0x0)
    Fade(250)
    Sound(812, 0, 100, 0)
    ClearMapObjFlags(0x6, 0x4)
    OP_0D()
    OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #A0790
    AnonymousTalk(
        0x9,
        (
            "#11P#4S！！！\x02\x03",

            "……これは………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0791
    AnonymousTalk(
        0x101,
        "#00001F#6Pひょっとして……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0792
    AnonymousTalk(
        0x109,
        "#10107Fやはり何か心当たりが！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)
    Sleep(300)

    #C0793
    ChrTalk(
        0x9,
        (
            "#11P────いや。\x02\x03",

            "残念ながら、心当たりは無いな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0794
    ChrTalk(
        0x101,
        "#00011F#6Pええっ！？\x02",
    )

    CloseMessageWindow()

    #C0795
    ChrTalk(
        0x104,
        (
            "#00301F#6Pおいおい！\x01",
            "そりゃねえッスよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x103,
        (
            "#00211F#6Pどう考えても心当たりが\x01",
            "ありそうな反応でしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x9,
        "#11P無いものは無いだけだ。\x02",
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0x9,
        (
            "#11P……こちらから誘って何だが\x01",
            "お引取り願おうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x9,
        "#11Pこれでも忙しい身なのでな。\x02",
    )

    CloseMessageWindow()

    #C0800
    ChrTalk(
        0x101,
        "#00006F#6Pそ、そんな……\x02",
    )

    CloseMessageWindow()

    #C0801
    ChrTalk(
        0x9,
        (
            "#11Pああ、シスター・マーブルに\x01",
            "聞いたところで無駄だぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0802
    ChrTalk(
        0x9,
        (
            "#11P博識な彼女であっても\x01",
            "その花のことは知らぬ筈だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0803
    ChrTalk(
        0x9,
        (
            "#11P逆に、もし知っていれば\x01",
            "いささか問題になるのだがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0804
    ChrTalk(
        0x109,
        "#10108F#6Pそ、それって……\x02",
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x105,
        (
            "#10302F#6P……どう考えても\x01",
            "知ってる前提の発言だよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0806
    ChrTalk(
        0x9,
        (
            "#11Pどう言われようとも\x01",
            "私の答えは変わらない。\x02",
        )
    )

    CloseMessageWindow()

    #C0807
    ChrTalk(
        0x9,
        (
            "#11Pたとえ警備隊のソーニャ司令が\x01",
            "直接、訪ねて来ようともな。\x02",
        )
    )

    CloseMessageWindow()

    #C0808
    ChrTalk(
        0x101,
        "#00013F#6Pくっ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(250)

    #C0809
    ChrTalk(
        0x102,
        (
            "#00106F#12P……ロイド、失礼しましょう。\x02\x03",

            "#00108Fこれ以上お聞きしても無駄だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0x101,
        "#00006F#5P……分かった。\x02",
    )

    CloseMessageWindow()

    def lambda_101FF():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_101FF)
    Sleep(50)

    def lambda_1020F():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1020F)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    Sleep(200)

    #C0811
    ChrTalk(
        0x101,
        "#00003F#6P失礼します、大司教。\x02",
    )

    CloseMessageWindow()

    #C0812
    ChrTalk(
        0x9,
        "#11Pうむ、悪く思わないでくれ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x6, 0x4)
    OP_68(50000, 1000, 13000, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x101, 50000, 0, 14000, 180)
    SetChrPos(0x102, 50000, 0, 14000, 180)
    SetChrPos(0x103, 50000, 0, 14000, 180)
    SetChrPos(0x104, 50000, 0, 14000, 180)
    SetChrPos(0x109, 50000, 0, 14000, 180)
    SetChrPos(0x105, 50000, 0, 14000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, 60000, 0, 3000, 270)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    FadeToBright(1000, 0)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x2)

    def lambda_10398():
        OP_95(0x101, 50000, 0, 2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10398)

    def lambda_103B2():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_103B2)
    OP_68(49820, 1000, 3570, 7000)
    MoveCamera(315, 20, 0, 7000)
    OP_6E(300, 7000)
    SetCameraDistance(30000, 7000)
    Sleep(500)

    def lambda_103F4():
        OP_95(0x102, 48800, 0, 3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_103F4)

    def lambda_1040E():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1040E)
    Sleep(500)

    def lambda_10422():
        OP_95(0x103, 51000, 0, 2650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10422)

    def lambda_1043C():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_1043C)
    Sleep(500)

    def lambda_10450():
        OP_95(0x104, 50000, 0, 4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10450)

    def lambda_1046A():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_1046A)
    Sleep(500)

    def lambda_1047E():
        OP_95(0x109, 48750, 0, 4400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1047E)

    def lambda_10498():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_10498)
    Sleep(500)

    def lambda_104AC():
        OP_95(0x105, 50000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_104AC)

    def lambda_104C6():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_104C6)
    WaitChrThread(0x105, 1)
    OP_93(0x105, 0x0, 0x1F4)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)

    def lambda_104FD():
        OP_95(0x105, 50750, 0, 4500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_104FD)
    WaitChrThread(0x101, 1)

    def lambda_1051B():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1051B)
    WaitChrThread(0x102, 1)

    def lambda_1052C():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1052C)
    WaitChrThread(0x103, 1)

    def lambda_1053D():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1053D)
    WaitChrThread(0x104, 1)

    def lambda_1054E():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1054E)
    WaitChrThread(0x109, 1)

    def lambda_1055F():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1055F)
    WaitChrThread(0x105, 1)
    TurnDirection(0x105, 0x101, 500)
    OP_0D()
    OP_6F(0x79)

    #C0813
    ChrTalk(
        0x104,
        (
            "#00303F#11Pオイオイオイ……\x02\x03",

            "#00301Fちょいとばかり\x01",
            "意地悪すぎやしねぇか？\x02",
        )
    )

    CloseMessageWindow()

    #C0814
    ChrTalk(
        0x109,
        "#10108F#5Pせ、先輩……\x02",
    )

    CloseMessageWindow()

    #C0815
    ChrTalk(
        0x103,
        (
            "#00206F#12Pでも、後ろめたい雰囲気も\x01",
            "特にありませんでしたね。\x02\x03",

            "#00208Fまるでわたし達に隠すのが\x01",
            "正しい事だと思っているような……\x02",
        )
    )

    CloseMessageWindow()

    #C0816
    ChrTalk(
        0x101,
        (
            "#00006F#6P……恐らく何らかの\x01",
            "禁忌#4Rタブー#があるんだろうな。\x02\x03",

            "#00008Fそれもマーブル先生が\x01",
            "知らないほどの禁忌が……\x02",
        )
    )

    CloseMessageWindow()

    #C0817
    ChrTalk(
        0x105,
        (
            "#10304F#11Pやれやれ、そんな風に言われると\x01",
            "余計に知りたくなるだけだけどね。\x02\x03",

            "#10302Fこうなったら全部の聖典を\x01",
            "一から読み漁ってみるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0818
    ChrTalk(
        0x102,
        (
            "#00106F#5Pでも、聖典全部となると\x01",
            "膨大な数になるし……\x02\x03",

            "#00108F……私が昔読んだのって\x01",
            "どのあたりの下りだったかしら……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    Sound(103, 0, 60, 0)

    #N0819
    NpcTalk(
        0xA,
        "娘の声",
        (
            "#1P#2S……多分、普通の聖典には\x01",
            "詳しくは載っていない筈です。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1083C():
        OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1083C)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0820
    ChrTalk(
        0x101,
        "#00005F#5Pえ……\x02",
    )

    CloseMessageWindow()
    OP_68(52730, 1000, 3870, 2000)
    MoveCamera(326, 21, 0, 2000)
    OP_6E(300, 2000)
    SetCameraDistance(30000, 2000)

    def lambda_1092A():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1092A)
    Sleep(0)

    def lambda_1093A():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1093A)
    Sleep(0)

    def lambda_1094A():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1094A)
    Sleep(0)

    def lambda_1095A():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1095A)
    Sleep(0)

    def lambda_1096A():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1096A)
    Sleep(0)

    def lambda_1097A():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1097A)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    def lambda_1099F():
        OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1099F)
    OP_95(0xA, 56800, 0, 3000, 2000, 0x0)
    OP_6F(0x79)

    #C0821
    ChrTalk(
        0x101,
        "#00005F#5P貴女は……\x02",
    )

    CloseMessageWindow()

    #C0822
    ChrTalk(
        0x102,
        "#00105F#5Pリ、リースさん……？\x02",
    )

    CloseMessageWindow()

    #C0823
    ChrTalk(
        0xA,
        (
            "#04403F#12P（シッ、お静かに……）\x02\x03",

            "#04400F（……このまま礼拝堂から出て\x01",
            "  寄宿舎まで来てください。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x5A, 0x1F4)
    OP_9B(0x0, 0xA, 0x0, 0x4B0, 0x7D0, 0x0)

    def lambda_10A83():
        OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_10A83)
    OP_9B(0x0, 0xA, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xA, 3)
    SetChrFlags(0xA, 0x80)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(49820, 1000, 3570, 2000)
    MoveCamera(315, 20, 0, 2000)
    OP_6E(300, 2000)
    SetCameraDistance(30000, 2000)
    OP_6F(0x79)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    Sleep(300)

    def lambda_10B5D():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10B5D)

    def lambda_10B6A():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10B6A)
    Sleep(50)

    def lambda_10B7A():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10B7A)
    Sleep(50)

    def lambda_10B8A():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10B8A)
    Sleep(50)

    def lambda_10B9A():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10B9A)
    Sleep(50)

    def lambda_10BAA():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10BAA)
    Sleep(50)

    def lambda_10BBA():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10BBA)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x101, 2)

    #C0824
    ChrTalk(
        0x109,
        "#10101F#5P（ど、どうします……？）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10CA9")

    #C0825
    ChrTalk(
        0x101,
        (
            "#00003F#6P（彼女は確か『星杯騎士団』の\x01",
            "  関係者という話だな……）\x02\x03",

            "#00001F（とにかく行ってみよう。）\x02",
        )
    )

    CloseMessageWindow()

    #C0826
    ChrTalk(
        0x102,
        "#00101F#5P（ええ、それがいいわ。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_10D44")

    label("loc_10CA9")


    #C0827
    ChrTalk(
        0x102,
        (
            "#00103F#5P（……彼女は信用できるわ。）\x02\x03",

            "#00101F（何か話があるみたいだし\x01",
            "  とにかく行ってみましょう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)

    #C0828
    ChrTalk(
        0x101,
        "#00001F#6P（……ああ、分かった。）\x02",
    )

    CloseMessageWindow()

    label("loc_10D44")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 50000, 0, 2500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x161, 7)
    OP_29(0xA6, 0x1, 0x8)
    OP_1B(0x4, 0xFF, 0xFFFF)
    EventEnd(0x5)
    Return()

    # Function_53_F804 end

    def Function_54_10D89(): pass

    label("Function_54_10D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F1E")

    #C0829
    ChrTalk(
        0xD,
        (
            "おや……\x01",
            "なにかお困りのご様子ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0x101,
        (
            "#00003F（『シスター』枠でミスコンに\x01",
            "  出てくれるかな……？）\x02\x03",

            "#00000Fあの、すみません。\x01",
            "ちょっと相談なのですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0831
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "チャリティイベントの\x01",
            "ミスコンへの参加を頼んでみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0832
    ChrTalk(
        0xD,
        (
            "……え、えっと……\x01",
            "まさか私に誘いがかかるとは。\x02",
        )
    )

    CloseMessageWindow()

    #C0833
    ChrTalk(
        0xD,
        (
            "ですが、すみません。\x01",
            "ちょっと他に仕事がありまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0834
    ChrTalk(
        0x101,
        (
            "#00006Fそうですか……\x01",
            "なら仕方ないですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x199, 2)
    Jump("loc_10F99")

    label("loc_10F1E")


    #C0835
    ChrTalk(
        0xD,
        (
            "すみません、ちょっと他に\x01",
            "仕事がありまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0836
    ChrTalk(
        0xD,
        (
            "ミスコンという雰囲気も\x01",
            "ちょっと苦手ですし……\x01",
            "今回はお断りしますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10F99")

    TalkEnd(0xD)
    Return()

    # Function_54_10D89 end

    def Function_55_10F9D(): pass

    label("Function_55_10F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11217")

    #C0837
    ChrTalk(
        0x8,
        (
            "おや……\x01",
            "皆さん、どうしたのです？\x02",
        )
    )

    CloseMessageWindow()

    #C0838
    ChrTalk(
        0x101,
        (
            "#00000F（マーブル先生も\x01",
            "  シスターだけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0839
    ChrTalk(
        0x102,
        (
            "#00106F（さ、さすがに\x01",
            "  ミスコンになんて\x01",
            "  誘えないわよね……）\x02",
        )
    )

    CloseMessageWindow()

    #C0840
    ChrTalk(
        0x8,
        "……ふふ、もしかして……\x02",
    )

    CloseMessageWindow()

    #C0841
    ChrTalk(
        0x8,
        (
            "私をミスコンに誘って\x01",
            "くれるつもりなのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0842
    ChrTalk(
        0x8,
        (
            "そういうものが\x01",
            "企画されているという\x01",
            "噂がありましたが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)

    #C0843
    ChrTalk(
        0x101,
        (
            "#00012Fえ、ええっと……\x01",
            "ご存知でしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0844
    ChrTalk(
        0x8,
        (
            "うふふ、冗談です。\x01",
            "さすがに私も歳ですしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0845
    ChrTalk(
        0x8,
        (
            "他のシスターに頼んでごらんなさい。\x01",
            "きっと誰か手伝ってくれるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0846
    ChrTalk(
        0x102,
        (
            "#00106Fふう……\x01",
            "マーブル先生には\x01",
            "かないませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x199, 3)
    Jump("loc_112A0")

    label("loc_11217")


    #C0847
    ChrTalk(
        0x8,
        (
            "ミスコンについては\x01",
            "他のシスターに頼んでごらん。\x01",
            "きっと誰か手伝ってくれるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0848
    ChrTalk(
        0x8,
        (
            "ふふ、私ももう少し若ければ\x01",
            "立候補したのですけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112A0")

    TalkEnd(0x8)
    Return()

    # Function_55_10F9D end

    def Function_56_112A4(): pass

    label("Function_56_112A4")

    EventBegin(0x0)
    Fade(500)
    OP_68(-5600, 2000, 18210, 0)
    MoveCamera(339, 30, 0, 0)
    OP_6E(280, 0)
    SetCameraDistance(31500, 0)
    SetChrPos(0x101, -5140, 0, 19480, 315)
    SetChrPos(0x102, -5930, 0, 18250, 315)
    SetChrPos(0x103, -5840, 0, 17320, 315)
    SetChrPos(0x104, -5040, 0, 18120, 315)
    SetChrPos(0x109, -4230, 0, 18930, 315)
    SetChrPos(0x105, -4420, 0, 17290, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0xA, 0x87, 0x0)
    OP_4B(0xA, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 5)), scpexpr(EXPR_END)), "loc_11449")

    #C0849
    ChrTalk(
        0xA,
        (
            "#04405Fおや、みなさん。\x01",
            "私に何か御用ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0850
    ChrTalk(
        0x105,
        (
            "#10300F（ミスコンの『シスター』枠……\x01",
            "  彼女だったらいいんじゃない？）\x02",
        )
    )

    CloseMessageWindow()

    #C0851
    ChrTalk(
        0x101,
        (
            "#00003F（そうだな……頼んでみようか。）\x02\x03",

            "#00000Fあの、リースさんに相談があるんですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_118D9")

    label("loc_11449")


    #C0852
    ChrTalk(
        0x101,
        (
            "#00000Fリースさん、\x01",
            "ミサの手伝いをしてる\x01",
            "みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0853
    ChrTalk(
        0xA,
        (
            "#04400Fええ、そんなところです。\x02\x03",

            "#04400F……今回のミサには、\x01",
            "特に多くの参拝客が\x01",
            "訪れているようですね。\x02\x03",

            "自分の大切な場所が襲われ、\x01",
            "傷つけられる恐ろしさ……\x02\x03",

            "#04403F……私にも分かる気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0854
    ChrTalk(
        0x102,
        "#00105Fリースさん……\x02",
    )

    CloseMessageWindow()

    #C0855
    ChrTalk(
        0x105,
        (
            "#10303F（……彼女にも昔、似たような事が\x01",
            "  あったのかもしれないね。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    #C0856
    ChrTalk(
        0xA,
        (
            "#04400F（ここだけの話……\x01",
            "  今回の事件の影響で《封聖省》も\x01",
            "  この先の動きを決めかねています。）\x02\x03",

            "#04403F（……私はクロスベルに居られるうちに#13R㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　　　　　　　　　　　　　#、\x01",
            "  出来る限り情報を集めておくつもりです。）\x02\x03",

            "#04400F（ロイドさんたちも、動向には\x01",
            "  注意しておくようにしてください。）\x02",
        )
    )

    CloseMessageWindow()

    #C0857
    ChrTalk(
        0x103,
        "#00200F（居られるうちに……ですか。）\x02",
    )

    CloseMessageWindow()

    #C0858
    ChrTalk(
        0x101,
        (
            "#00003F（……分かりました。\x01",
            "  リースさんもお気をつけて。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0859
    ChrTalk(
        0xA,
        (
            "#04405Fそういえば……\x01",
            "もしかして私に何か御用ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0860
    ChrTalk(
        0x101,
        "#00012Fえ、えっと、まあ……\x02",
    )

    CloseMessageWindow()

    #C0861
    ChrTalk(
        0x105,
        (
            "#10300F（フフ、忘れる所だったけど、\x01",
            "  ミスコンの『シスター』枠……\x01",
            "  彼女だったらいいんじゃない？）\x02",
        )
    )

    CloseMessageWindow()

    #C0862
    ChrTalk(
        0x101,
        (
            "#00003F（そうだな……\x01",
            "  来たついでだし頼んでみようか。）\x02\x03",

            "#00000Fあの、リースさんに相談があるんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 5)

    label("loc_118D9")

    SetChrName("")

    #A0863
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "チャリティイベントの\x01",
            "ミスコンへの参加を頼んでみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0864
    ChrTalk(
        0xA,
        (
            "#04405Fミスコン……ですか。\x02\x03",

            "#04402Fチャリティイベントというのは\x01",
            "とてもよいことだと思いますが……\x01",
            "今日は色々と忙しいのです。\x02\x03",

            "#04406Fそれに、聖職者がそのようなものに\x01",
            "出るというのはちょっと……\x02",
        )
    )

    CloseMessageWindow()

    #C0865
    ChrTalk(
        0x102,
        "#00106Fま、まあそれはそうですよね……\x02",
    )

    CloseMessageWindow()

    #C0866
    ChrTalk(
        0x104,
        (
            "#00306Fちぇっ、ステージに立つ\x01",
            "リースちゃんを見たかったんだがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0867
    ChrTalk(
        0xA,
        (
            "#04402Fふふ……\x01",
            "でも、イベント自体は\x01",
            "とてもよいことだと思います。\x02\x03",

            "ミスコン以外にはどういったことを\x01",
            "なさっているんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0868
    ChrTalk(
        0x109,
        "#10105Fええと、ミスコンの他は確か……\x02",
    )

    CloseMessageWindow()

    #C0869
    ChrTalk(
        0x103,
        (
            "#00200Fピアノのコンサートと、\x01",
            "立食パーティですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0870
    ChrTalk(
        0xA,
        (
            "#04403F…………………………\x01",
            "みなさん、やはりミスコンとやらに\x01",
            "参加させてもらってもいいですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0871
    ChrTalk(
        0x101,
        (
            "#00012Fえ、えっと……かまいませんよ。\x02\x03",

            "#00004F（立食パーティにつられたのかな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0872
    ChrTalk(
        0x105,
        "#10309F（アハハ、みたいだね。）\x02",
    )

    CloseMessageWindow()

    #C0873
    ChrTalk(
        0xA,
        (
            "#04402Fでは、私はもうしばらく\x01",
            "ミサの手伝いがありますので。\x02\x03",

            "#04404Fプログラムが開始するときに\x01",
            "こちらに連絡してください。\x02",
        )
    )

    CloseMessageWindow()

    #C0874
    ChrTalk(
        0x101,
        "#00000Fええ、分かりました。\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11DED")

    #C0875
    ChrTalk(
        0x101,
        (
            "#00003F──さて、これでようやく\x01",
            "参加者枠が埋まったな。\x02\x03",

            "#00000F市民会館に行って\x01",
            "ロイさんたちに報告しよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x5)

    label("loc_11DED")

    SetScenarioFlags(0x199, 7)
    OP_4C(0xA, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -5530, 0, 18650, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_56_112A4 end

    def Function_57_11E20(): pass

    label("Function_57_11E20")

    EventBegin(0x0)
    Fade(500)
    OP_68(860, 2190, 20270, 0)
    MoveCamera(319, 24, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30010, 0)
    SetChrPos(0x101, -160, 500, 20710, 0)
    SetChrPos(0x102, -1330, 500, 20570, 0)
    SetChrPos(0x103, 1040, 500, 20540, 0)
    SetChrPos(0x104, -1100, 250, 19370, 0)
    SetChrPos(0x109, 60, 250, 19350, 0)
    SetChrPos(0x105, 1230, 250, 19340, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x9, 0xB4, 0x0)
    OP_0D()

    #C0876
    ChrTalk(
        0x9,
        "おや……私に何か用かね？\x02",
    )

    CloseMessageWindow()

    #C0877
    ChrTalk(
        0x9,
        (
            "説教を希望するのならば\x01",
            "時間を割かせてもらうが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0878
    ChrTalk(
        0x101,
        (
            "#6P#00005Fい、いえ。\x01",
            "そういうわけではないんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0879
    ChrTalk(
        0x102,
        (
            "#6P#00103F（怪盗Ｂのカードに書いていた\x01",
            "  『最も大いなる女神の光』……）\x02",
        )
    )

    CloseMessageWindow()
    OP_68(570, 3200, 26250, 3000)
    MoveCamera(325, 24, 0, 3000)
    OP_6E(300, 3000)
    SetCameraDistance(31590, 3000)
    OP_6F(0x79)

    #C0880
    ChrTalk(
        0x102,
        (
            "#6P#N#00100F（多分、この大きな\x01",
            "  ステンドグラスからの\x01",
            "  光を指してるんだと思うけど。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0881
    ChrTalk(
        0x103,
        (
            "#6P#N#00203F（だとしたら、その光を\x01",
            "  『その背に浴びし者』は……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(860, 2190, 20270, 2000)
    MoveCamera(319, 24, 0, 2000)
    OP_6E(300, 2000)
    SetCameraDistance(30010, 2000)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_6F(0x79)
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0882
    ChrTalk(
        0x9,
        "何やらよく分からんが……\x02",
    )

    CloseMessageWindow()

    #C0883
    ChrTalk(
        0x9,
        (
            "言いたい事があるなら\x01",
            "はっきり言ってはどうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0884
    ChrTalk(
        0x101,
        (
            "#6P#00012Fえ、えっとそれじゃあ……\x02\x03",

            "#00000Fエラルダ大司教。\x01",
            "その教壇の下を調べさせて\x01",
            "もらえませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0885
    ChrTalk(
        0x9,
        "……何？\x02",
    )

    CloseMessageWindow()

    #C0886
    ChrTalk(
        0x105,
        (
            "#6P#10300Fフフ、怪しいことを\x01",
            "するわけじゃないから安心してよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0887
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちはエラルダ大司教に\x01",
            "事情を説明し、教壇を調べた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(1025, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0888
    AnonymousTalk(
        0x101,
        "#00000Fあった……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(470, 2000, 10610, 0)
    MoveCamera(311, 34, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28510, 0)
    SetChrPos(0x101, -1250, 0, 11150, 0)
    SetChrPos(0x102, 150, 0, 11210, 315)
    SetChrPos(0x103, -2060, 0, 10100, 0)
    SetChrPos(0x104, -670, 0, 10170, 0)
    SetChrPos(0x109, 1000, 0, 10460, 315)
    SetChrPos(0x105, -1350, 0, 9170, 0)
    SetChrPos(0x9, 120, 0, 14230, 225)
    ClearMapObjFlags(0x5, 0x4)
    LoadChrToIndex("apl/ch51099.itc", 0x1E)
    SetChrChipByIndex(0x23, 0x1E)
    SetChrSubChip(0x23, 0x1)
    SetChrPos(0x23, -1320, 150, 12580, 0)
    OP_52(0x23, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x2)
    SetChrFlags(0x23, 0x10)
    SetChrFlags(0x23, 0x20)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis348.itp")
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(1024, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x1, 0x14, 0x1, 0x8)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_79(0x5)
    Sleep(1000)
    SetChrName("")

    #A0889
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "トランクの裏側には\x01",
            "カードが貼り付けてあった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    #A0890
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第四の檻は市外に。\x01",
            "『西方の防人たちの\x01",
            "　足元を通る鉄の道』を探せ。\x07\x00\x02",
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

    #C0891
    ChrTalk(
        0x102,
        (
            "#6P#00100Fこれは、ベルが可愛がっている\x01",
            "『ミステル』って人形だったはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0892
    ChrTalk(
        0x105,
        (
            "#6P#10302Fふむ、間違いないみたいだね。\x01",
            "……ようやくこれで３体目か。\x02",
        )
    )

    CloseMessageWindow()

    #C0893
    ChrTalk(
        0x9,
        (
            "このようなものがいつの間に\x01",
            "あんなところに……！\x02",
        )
    )

    CloseMessageWindow()

    #C0894
    ChrTalk(
        0x9,
        (
            "時々所用で席を外す事はあったが\x01",
            "そこまでの時間があったとは思えん。\x02",
        )
    )

    CloseMessageWindow()

    #C0895
    ChrTalk(
        0x104,
        (
            "#6P#00306F正直言って神業としか\x01",
            "言いようがないッスよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0896
    ChrTalk(
        0x101,
        (
            "#6P#00001Fそれと、カードの方は\x01",
            "相変わらず難解みたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0897
    ChrTalk(
        0x102,
        (
            "#12P#00100F『防人#4Rさきもり#』は字の通り、\x01",
            "“守る者”という意味があるはずよ。\x02\x03",

            "#00103F『西方の』ということは、\x01",
            "『クロスベルの西側にいる守る者』\x01",
            "っていうことなんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0898
    ChrTalk(
        0x109,
        (
            "#12P#10105Fそしてその、“守る者”の\x01",
            "足元を通る“鉄の道”……ですか。\x02\x03",

            "#10106Fううん、まだよく分かりませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0899
    ChrTalk(
        0x103,
        "#6P#00200Fまた、何かの例えなんでしょうか。\x02",
    )

    CloseMessageWindow()

    #C0900
    ChrTalk(
        0x101,
        (
            "#6P#00003Fああ、多分そうだと思う。\x02\x03",

            "#00000Fとにかく、このトランクを回収して\x01",
            "次を探しに行ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)

    #C0901
    ChrTalk(
        0x9,
        (
            "#11P怪盗Ｂか……\x01",
            "話くらいは聞いていたが\x01",
            "相当な不届き者のようだな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1291C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1291C)
    Sleep(50)

    def lambda_1292C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1292C)

    #C0902
    ChrTalk(
        0x9,
        (
            "#11P大いなる女神の僕として、\x01",
            "かようなものを許してはおけん。\x02",
        )
    )

    CloseMessageWindow()

    #C0903
    ChrTalk(
        0x9,
        (
            "#11P諸君、何としても\x01",
            "捕まえてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0904
    ChrTalk(
        0x101,
        "#6P#00012Fが、頑張らせていただきます。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0905
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#16Iローゼンベルク人形・Ｍ\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x337, 1)
    SetMapObjFlags(0x5, 0x4)
    SetChrFlags(0x23, 0x80)
    OP_D7(0x1E)
    SetChrPos(0x0, 180, 0, 10810, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x9, -210, 380, 23230, 180)
    OP_29(0x7A, 0x1, 0x4)
    SetScenarioFlags(0x157, 3)
    TalkEnd(0x9)
    EventEnd(0x5)
    Return()

    # Function_57_11E20 end

    SaveToFile()

Try(main)
