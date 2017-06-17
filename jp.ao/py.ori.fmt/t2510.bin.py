from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2510.bin",                # FileName
        "t2510",                    # MapName
        "t2510",                    # Location
        0x005A,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1B,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 90, 0, 3, 0, 4],
    )

    BuildStringList((
        "t2510",                  # 0
        "オリバー隊員",           # 1
        "ジャック隊員",           # 2
        "ティマス",               # 3
        "アレクセイ隊員",         # 4
        "ラグ",                   # 5
        "観光客",                 # 6
        "観光客",                 # 7
        "観光客",                 # 8
        "観光客",                 # 9
        "観光客",                 # 10
        "男の子",                 # 11
        "遊撃士スコット",         # 12
        "遊撃士ヴェンツェル",     # 13
        "チルル",                 # 14
        "特務支援車",             # 15
        "運搬車",                 # 16
        "イベント用",             # 17
    ))

    AddCharChip((
        "chr/ch31300.itc",                   # 00
        "chr/ch31200.itc",                   # 01
        "chr/ch25000.itc",                   # 02
        "chr/ch31302.itc",                   # 03
        "chr/ch23400.itc",                   # 04
        "chr/ch20800.itc",                   # 05
        "chr/ch20802.itc",                   # 06
        "chr/ch32200.itc",                   # 07
        "chr/ch32202.itc",                   # 08
        "chr/ch21100.itc",                   # 09
        "chr/ch21102.itc",                   # 0A
        "chr/ch32300.itc",                   # 0B
        "chr/ch32302.itc",                   # 0C
        "chr/ch44200.itc",                   # 0D
        "chr/ch44202.itc",                   # 0E
        "chr/ch21402.itc",                   # 0F
        "chr/ch21400.itc",                   # 10
        "chr/ch41500.itc",                   # 11
        "chr/ch41400.itc",                   # 12
        "chr/ch41502.itc",                   # 13
        "chr/ch27202.itc",                   # 14
        "chr/ch27302.itc",                   # 15
        "chr/ch20500.itc",                   # 16
    ))

    DeclNpc(7780,    0,       6809,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-4280,   0,       5130,    180,  261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(106529,  0,       1980,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(95629,   150,     2380,    270,  261,  0x0, 0,   3,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(163020,  0,       -2410,   270,  261,  0x0, 0,   4,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(102949,  150,     2150,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(102900,  150,     4030,    270,  389,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(100569,  150,     2150,    90,   389,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(100569,  150,     3920,    90,   389,  0x0, 0,   11,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(102900,  150,     4030,    270,  389,  0x0, 0,   13,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(100569,  150,     2150,    90,   389,  0x0, 0,   15,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(101000,  150,     -2079,   270,  452,  0x0, 0,   20,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(98500,   150,     -2079,   90,   452,  0x0, 0,   21,  0,   255, 255, 0,   25,  255,  0)
    DeclNpc(159949,  0,       6000,    0,    389,  0x0, 0,   22,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-1750,   0,       -12300,  1000,    -1750,   1000,    -12300,  0x007C, 0,  31, 0x0000)
    DeclActor(105420,  0,       1980,    1000,    106530,  1500,    1980,    0x007E, 0,  11, 0x0000)
    DeclActor(161990,  0,       -2450,   1000,    163020,  1500,    -2410,   0x007E, 0,  14, 0x0000)
    DeclActor(7580,    0,       5630,    1000,    7780,    1500,    6810,    0x007E, 0,  6,  0x0000)
    DeclActor(108250,  0,       -5750,   1200,    108250,  1250,    -5750,   0x007C, 0,  5,  0x0000)

    ChipFrameInfo(1024, 0)                                       # 0

    ScpFunction((
        "Function_0_400",          # 00, 0
        "Function_1_4B0",          # 01, 1
        "Function_2_503",          # 02, 2
        "Function_3_52E",          # 03, 3
        "Function_4_872",          # 04, 4
        "Function_5_B67",          # 05, 5
        "Function_6_C0C",          # 06, 6
        "Function_7_C10",          # 07, 7
        "Function_8_1707",         # 08, 8
        "Function_9_1844",         # 09, 9
        "Function_10_1989",        # 0A, 10
        "Function_11_261F",        # 0B, 11
        "Function_12_2623",        # 0C, 12
        "Function_13_3072",        # 0D, 13
        "Function_14_394F",        # 0E, 14
        "Function_15_3953",        # 0F, 15
        "Function_16_43CA",        # 10, 16
        "Function_17_4598",        # 11, 17
        "Function_18_4902",        # 12, 18
        "Function_19_4AEA",        # 13, 19
        "Function_20_4CB7",        # 14, 20
        "Function_21_4E91",        # 15, 21
        "Function_22_4F66",        # 16, 22
        "Function_23_4FFD",        # 17, 23
        "Function_24_550C",        # 18, 24
        "Function_25_56A6",        # 19, 25
        "Function_26_5782",        # 1A, 26
        "Function_27_5867",        # 1B, 27
        "Function_28_61A2",        # 1C, 28
        "Function_29_636A",        # 1D, 29
        "Function_30_63C1",        # 1E, 30
        "Function_31_6A25",        # 1F, 31
    ))


    def Function_0_400(): pass

    label("Function_0_400")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_438"),
        (1, "loc_444"),
        (2, "loc_450"),
        (3, "loc_45C"),
        (4, "loc_468"),
        (5, "loc_474"),
        (6, "loc_480"),
        (SWITCH_DEFAULT, "loc_48C"),
    )


    label("loc_438")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_444")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_450")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_45C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_468")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_474")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_480")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_48C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_498")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_4AF")

    Return()

    # Function_0_400 end

    def Function_1_4B0(): pass

    label("Function_1_4B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_502")
    OP_95(0xFE, -21200, 0, -3250, 2000, 0x0)
    Sleep(2000)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, 10400, 0, -3250, 2000, 0x0)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    Jump("Function_1_4B0")

    label("loc_502")

    Return()

    # Function_1_4B0 end

    def Function_2_503(): pass

    label("Function_2_503")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52D")
    OP_94(0xFE, 0x24D56, 0xAC8, 0x25CA6, 0xFFFFFDA8, 0x3E8)
    Sleep(450)
    Jump("Function_2_503")

    label("loc_52D")

    Return()

    # Function_2_503 end

    def Function_3_52E(): pass

    label("Function_3_52E")

    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5BC")
    SetChrChipByIndex(0x8, 0x11)
    SetChrChipByIndex(0x9, 0x12)
    SetChrChipByIndex(0xB, 0x13)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -7600, 0, 2770, 270)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x10)
    SetChrPos(0x12, -8790, 0, 2770, 90)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 152840, 0, 1090, 270)
    BeginChrThread(0x11, 0, 0, 2)
    Jump("loc_848")

    label("loc_5BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_64D")
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_5D8")
    Jump("loc_648")

    label("loc_5D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_5E6")
    Jump("loc_648")

    label("loc_5E6")

    SetChrChipByIndex(0xB, 0x0)
    ClearChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, 10400, 0, -3250, 90)
    BeginChrThread(0xB, 0, 0, 1)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x6)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0xA)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 3040, 0, -2160, 0)

    label("loc_648")

    Jump("loc_848")

    label("loc_64D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_687")
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x8)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -21950, 0, 4400, 270)
    Jump("loc_848")

    label("loc_687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_714")
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x14)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0x15)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D9")
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x14, 0x10)

    label("loc_6D9")

    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 7660, 0, 4900, 0)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0xC)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    Jump("loc_848")

    label("loc_714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_764")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -8189, 0, -2160, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -21950, 0, 4400, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xE)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    Jump("loc_848")

    label("loc_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7C3")
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x6)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0xF)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 7660, 0, 4900, 0)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0x8, 0x10)
    Jump("loc_848")

    label("loc_7C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7FD")
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0xA)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 1540, 0, 2160, 180)
    Jump("loc_848")

    label("loc_7FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_848")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1540, 0, 2160, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x8)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -21950, 0, 4400, 270)

    label("loc_848")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_85F")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 7)
    Event(0, 28)
    Jump("loc_871")

    label("loc_85F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_871")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x1, 0)
    Event(0, 30)

    label("loc_871")

    Return()

    # Function_3_52E end

    def Function_4_872(): pass

    label("Function_4_872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8A0")

    label("loc_88E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_8A0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8A0")

    OP_70(0x4, 0x8C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8ED")
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    OP_78(0x6, 0x16)
    SetChrPos(0x16, -8690, 0, 220, 90)
    OP_D5(0x16, 0x0, 0x15F90, 0x0, 0x0)
    Jump("loc_A44")

    label("loc_8ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_944")
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    SetMapObjFrame(0x7, "chukin", 0x0, 0x1)
    OP_78(0x7, 0x16)
    SetChrPos(0x16, 2500, 0, 0, 90)
    OP_D5(0x16, 0x0, 0x15F90, 0x0, 0x0)
    Jump("loc_A44")

    label("loc_944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_952")
    Jump("loc_A44")

    label("loc_952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_981")
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    SetMapObjFrame(0x7, "chukin", 0x0, 0x1)
    Jump("loc_A44")

    label("loc_981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9CA")
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    OP_78(0x6, 0x16)
    SetChrPos(0x16, -8690, 100, 220, 90)
    OP_D5(0x16, 0x0, 0x15F90, 0x0, 0x0)
    Jump("loc_A44")

    label("loc_9CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9F9")
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    SetMapObjFrame(0x7, "chukin", 0x0, 0x1)
    Jump("loc_A44")

    label("loc_9F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A1A")
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    Jump("loc_A44")

    label("loc_A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A44")
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    SetMapObjFrame(0x7, "chukin", 0x0, 0x1)

    label("loc_A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A6A")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_A6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_B0B")
    SetChrPos(0x16, 8500, 0, 0, 90)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetMapObjFlags(0x9, 0x1000)
    OP_78(0x9, 0x17)
    SetChrPos(0x17, -3500, 0, 0, 90)
    OP_D5(0x17, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    SetMapObjFlags(0xA, 0x1000)
    OP_78(0xA, 0x18)
    SetChrPos(0x18, -3500, 0, 0, 90)
    OP_D5(0x18, 0x0, 0x15F90, 0x0, 0x0)
    Jump("loc_B66")

    label("loc_B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_B66")
    SetChrPos(0x16, 8500, 0, 0, 90)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetMapObjFlags(0x9, 0x1000)
    OP_78(0x9, 0x17)
    SetChrPos(0x17, -3500, 0, 0, 90)
    OP_D5(0x17, 0x0, 0x15F90, 0x0, 0x0)

    label("loc_B66")

    Return()

    # Function_4_872 end

    def Function_5_B67(): pass

    label("Function_5_B67")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "車雑誌『行軍・爆走野郎！』がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x371, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C08")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "ペイントパターン\x01\x07\x02",

            "『ガードカラー』\x07\x00",
            "を覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x371, 1)

    label("loc_C08")

    TalkEnd(0xFF)
    Return()

    # Function_5_B67 end

    def Function_6_C0C(): pass

    label("Function_6_C0C")

    Call(0, 7)
    Return()

    # Function_6_C0C end

    def Function_7_C10(): pass

    label("Function_7_C10")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_DD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D29")

    #N0003
    NpcTalk(
        0x8,
        "兵士オリバー",
        (
            "クロスベルから逃げ遅れていた\x01",
            "共和国人たちが訪れていてね。\x02",
        )
    )

    CloseMessageWindow()

    #N0004
    NpcTalk(
        0x8,
        "兵士オリバー",
        (
            "だが、共和国への警戒が解けない\x01",
            "今の状況じゃあ、さすがに\x01",
            "足止めせざるを得ないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #N0005
    NpcTalk(
        0x8,
        "兵士オリバー",
        (
            "帰りたい気持ちは分かるから、\x01",
            "少し心苦しいんだけどね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DD0")

    label("loc_D29")


    #N0006
    NpcTalk(
        0x8,
        "兵士オリバー",
        (
            "共和国への警戒が解けない\x01",
            "今の状況じゃあ、さすがに\x01",
            "足止めせざるを得ない。\x02",
        )
    )

    CloseMessageWindow()

    #N0007
    NpcTalk(
        0x8,
        "兵士オリバー",
        (
            "納得いかないかもしれないけど、\x01",
            "分かってもらうしかないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD0")

    Jump("loc_1703")

    label("loc_DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_110B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9F")

    #C0008
    ChrTalk(
        0x8,
        (
            "さっき、無理やりゲートを通った\x01",
            "黒い運搬車は、指名手配中の\x01",
            "詐欺師のものだったみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "この緊張状態の時に驚いたけど……\x01",
            "何にせよ、捕まってよかったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F1D")

    label("loc_E9F")


    #C0010
    ChrTalk(
        0x8,
        "とにかく、君たちもお疲れ様だったな。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "ダグラス副司令には\x01",
            "すでに報告しておいたから、\x01",
            "そっちは気にしなくていいからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1D")

    Jump("loc_1106")

    label("loc_F22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_FD8")

    #C0012
    ChrTalk(
        0x8,
        (
            "さっき、ゲートを無理やり通っていった\x01",
            "黒い運搬車は、指名手配中の\x01",
            "詐欺師のものだったみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "この緊張状態の時に……\x01",
            "まったく、馬鹿げたことをしてくれるよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1106")

    label("loc_FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B4")

    #C0014
    ChrTalk(
        0x8,
        (
            "国境の緊張は、\x01",
            "まさに極限に近い状態だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "共和国方面はタングラム丘陵という\x01",
            "緩衝地帯があるにはあるけど、\x01",
            "それでもやはり安心はできない。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "ここが踏ん張りどころだ。\x01",
            "しっかり警戒を続けないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1106")

    label("loc_10B4")


    #C0017
    ChrTalk(
        0x8,
        (
            "クロスベルにとっても、\x01",
            "ここが踏ん張りどころだ。\x01",
            "しっかり警戒を続けないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1106")

    Jump("loc_1703")

    label("loc_110B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_12AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1209")

    #C0018
    ChrTalk(
        0x8,
        (
            "昨日は、タングラム門も\x01",
            "脱線事故の対応に追われていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "共和国の旅客バスにも\x01",
            "応援を要請したりして、\x01",
            "なかなか大変だったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "この緊張状態が続いてるときに\x01",
            "事故だなんて……やれやれ、\x01",
            "間が悪いときに起きたものだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12A9")

    label("loc_1209")


    #C0021
    ChrTalk(
        0x8,
        (
            "この緊張状態が続いてるときに\x01",
            "事故だなんて……やれやれ、\x01",
            "間が悪いときに起きたものだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "せめて住民投票までは\x01",
            "これ以上の不測の事態は\x01",
            "ご遠慮願いたいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A9")

    Jump("loc_1703")

    label("loc_12AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_12BF")
    Call(0, 8)
    Jump("loc_1703")

    label("loc_12BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1485")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D2")

    #C0023
    ChrTalk(
        0x8,
        (
            "最近は共和国でも、\x01",
            "クロスベル独立の是非が\x01",
            "議論されてるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "しかも、クロスベルの中とは違って\x01",
            "その殆どは反対だそうだ。\x01",
            "まあ、仕方ないとは思うが……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "近く住民投票が行われるが、\x01",
            "こんな状況で独立が実現する\x01",
            "なんてことがあるんだろうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1480")

    label("loc_13D2")


    #C0026
    ChrTalk(
        0x8,
        (
            "近く住民投票が行われるが、\x01",
            "こんな状況で独立が実現する\x01",
            "なんてことがあるんだろうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "警備隊としては、ぜひとも\x01",
            "実現してほしいものだが……\x01",
            "やはり難しいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1480")

    Jump("loc_1703")

    label("loc_1485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1496")
    Call(0, 9)
    Jump("loc_1703")

    label("loc_1496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_151C")

    #C0028
    ChrTalk(
        0x8,
        (
            "交通規制でタングラム丘陵を\x01",
            "通れなかった車が、一気に来てね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "ふう、ある程度予想していたけど\x01",
            "こいつは忙しいな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1703")

    label("loc_151C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1703")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15A6")

    #C0030
    ChrTalk(
        0x8,
        (
            "ダグラス副司令の演習は\x01",
            "いつもあんな感じでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "厳しいことも多いけど……\x01",
            "頑張ってついていかなくちゃな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1703")

    label("loc_15A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1682")

    #C0032
    ChrTalk(
        0x8,
        (
            "ここを抜けると、自治州と\x01",
            "共和国の緩衝地帯である\x01",
            "『タングラム丘陵』だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "この丘陵は、旅客バスや導力車で\x01",
            "行き来される事が多いかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "導力車が普及している共和国らしい\x01",
            "傾向だといえるだろうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1703")

    label("loc_1682")


    #C0035
    ChrTalk(
        0x8,
        (
            "タングラム丘陵は、\x01",
            "旅客バスや導力車で\x01",
            "行き来される事が多い。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "導力車が普及している共和国らしい\x01",
            "傾向だといえるだろうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1703")

    TalkEnd(0x8)
    Return()

    # Function_7_C10 end

    def Function_8_1707(): pass

    label("Function_8_1707")

    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D7")

    #C0037
    ChrTalk(
        0x8,
        "朝早くにお疲れ様です。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "最近は、自治州内で\x01",
            "得体の知れない魔獣が\x01",
            "目撃されています。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "街道の運転、\x01",
            "どうかお気をつけて。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xD,
        (
            "うむ、ご苦労。\x01",
            "気をつけさせてもらうとしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_183B")

    label("loc_17D7")


    #C0041
    ChrTalk(
        0x8,
        (
            "……それでは、入国証明書に\x01",
            "サインをお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xD,
        (
            "おお、そうじゃったな。\x01",
            "サラサラサラ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_183B")

    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_8_1707 end

    def Function_9_1844(): pass

    label("Function_9_1844")

    OP_4B(0x8, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1919")

    #C0043
    ChrTalk(
        0x8,
        (
            "街についたら、市民会館のほうへ\x01",
            "駐車場所を届け出てください。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "これを忘れると、駐禁ステッカーを\x01",
            "貼られてしまうのでお気をつけて。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xE,
        (
            "おっと、そうなのか。\x01",
            "意外と面倒なんだなあ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_1980")

    label("loc_1919")


    #C0046
    ChrTalk(
        0x8,
        (
            "街についたら、市民会館のほうへ\x01",
            "車の駐車登録を届け出てくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xE,
        "へいへい、了解ですよっと。\x02",
    )

    CloseMessageWindow()

    label("loc_1980")

    OP_4C(0x8, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_9_1844 end

    def Function_10_1989(): pass

    label("Function_10_1989")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1ACA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A22")

    #N0048
    NpcTalk(
        0x9,
        "兵士ジャック",
        "湿地帯方面に異常、アリ！！\x02",
    )

    CloseMessageWindow()

    #N0049
    NpcTalk(
        0x9,
        "兵士ジャック",
        (
            "あの不可思議な大樹は一体……\x01",
            "不安が隠しきれないであります。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AC5")

    label("loc_1A22")


    #N0050
    NpcTalk(
        0x9,
        "兵士ジャック",
        (
            "あの不可思議な大樹は一体……\x01",
            "不安が隠しきれないであります。\x02",
        )
    )

    CloseMessageWindow()

    #N0051
    NpcTalk(
        0x9,
        "兵士ジャック",
        (
            "と、とにかく……\x01",
            "どんな時でも冷静に！\x01",
            "落ち着くのが大事であります！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC5")

    Jump("loc_261B")

    label("loc_1ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1D4D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1B63")

    #C0052
    ChrTalk(
        0x9,
        (
            "先ほどは、本当に\x01",
            "ビックリしたであります。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        (
            "捕まったからよかったものの……\x01",
            "……ルールは守ってほしいもので\x01",
            "ありますな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D48")

    label("loc_1B63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_1BD4")

    #C0054
    ChrTalk(
        0x9,
        (
            "先ほどは、本当に\x01",
            "ビックリしたであります。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "……ルールは守ってほしいもので\x01",
            "ありますな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D48")

    label("loc_1BD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC1")

    #C0056
    ChrTalk(
        0x9,
        (
            "国境のアルタイル市で、\x01",
            "共和国軍に動きが\x01",
            "見られるのであります。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "大きな演習でも始めて\x01",
            "クロスベルに圧力をかける……\x01",
            "そんな目的があるのでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x9,
        (
            "……由々しき事態でありますな。\x01",
            "我々警備隊が尽力しなければ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D48")

    label("loc_1CC1")


    #C0059
    ChrTalk(
        0x9,
        (
            "国境のアルタイル市で、\x01",
            "共和国軍に動きが\x01",
            "見られるのであります。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "……由々しき事態でありますな。\x01",
            "我々警備隊が尽力しなければ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D48")

    Jump("loc_261B")

    label("loc_1D4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1FB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EF7")

    #C0061
    ChrTalk(
        0x9,
        (
            "異常・ナシ！　この程度の雨、\x01",
            "警備#4Rけいび#への影響は軽微#4Rけいび#であります！！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)

    #C0062
    ChrTalk(
        0x103,
        "#00206F……０点です。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "ハッ……\x01",
            "べ、別にダジャレでは\x01",
            "ないでありますよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        (
            "自分はこの程度の雨など\x01",
            "大した影響はないと\x01",
            "言いたかっただけで……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x109,
        (
            "#10100Fあはは、分かってますよ。\x01",
            "（……でも、おかげで和めたかも。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FB2")

    label("loc_1EF7")


    #C0066
    ChrTalk(
        0x9,
        (
            "じ、自分はこの程度の雨など\x01",
            "大した影響はないと\x01",
            "言いたかったわけで……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "この緊張状態の下、\x01",
            "そんな、ふざけるわけが\x01",
            "ないでありますからしてっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#00006Fそ、そんな慌てなくても……\x02",
    )

    CloseMessageWindow()

    label("loc_1FB2")

    Jump("loc_261B")

    label("loc_1FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_213B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20AE")

    #C0069
    ChrTalk(
        0x9,
        (
            "《幻獣》は、タングラム丘陵には\x01",
            "出ていないようであります。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "あそこは共和国との緩衝地帯。\x01",
            "出現されると退治にいくにも\x01",
            "色々と厄介であります。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "これから出ないとも限りませんが……\x01",
            "とにかく警戒を厳に、であります！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2136")

    label("loc_20AE")


    #C0072
    ChrTalk(
        0x9,
        (
            "《幻獣》は、タングラム丘陵には\x01",
            "出ていないようであります。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "これから出ないとも限りませんが……\x01",
            "とにかく警戒を厳に、であります！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2136")

    Jump("loc_261B")

    label("loc_213B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_238D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2314")

    #C0074
    ChrTalk(
        0x9,
        (
            "通商会議の時に破壊された\x01",
            "レーダー施設の復旧が、\x01",
            "この間、完了したであります。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "しかしテロリストたちめ、\x01",
            "我々の目を盗んで施設を\x01",
            "破壊してしまうとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "よく考えると\x01",
            "改めて不可解ではありますな。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        (
            "#00001F（……地下で現れた装甲車といい、\x01",
            "  確かにテロリストたちだけでは\x01",
            "  準備が整いすぎていた。）\x02\x03",

            "#00003F（やっぱり、『結社』の協力が\x01",
            "  あったのかもしれないな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x105,
        (
            "#10300F（まあ、証拠はないけどね。\x01",
            "  可能性は高いんじゃないかな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2388")

    label("loc_2314")


    #C0079
    ChrTalk(
        0x9,
        (
            "ふむ、あのテロリストに関しては\x01",
            "まだ疑問は残るでありますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "とにかく、今は警備を\x01",
            "厳重にするであります！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2388")

    Jump("loc_261B")

    label("loc_238D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2483")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2414")

    #C0081
    ChrTalk(
        0x9,
        "今のところは異常・ナシ！\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "テロリストめ……\x01",
            "情報が入ったからには、\x01",
            "全力をもって迎え撃つであります。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_247E")

    label("loc_2414")


    #C0083
    ChrTalk(
        0x9,
        (
            "我々警備隊が絶対に首脳たちを\x01",
            "守ってみせるであります！\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "……とりあえず、\x01",
            "今のところは異常・ナシ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_247E")

    Jump("loc_261B")

    label("loc_2483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_254E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2512")

    #C0085
    ChrTalk(
        0x9,
        (
            "ロックスミス大統領の警備は、\x01",
            "異常・ナシでありました！！\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "引き続き、通商会議の警備を\x01",
            "続けていくであります！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2549")

    label("loc_2512")


    #C0087
    ChrTalk(
        0x9,
        (
            "引き続き、通商会議の警備を\x01",
            "続けていくであります！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2549")

    Jump("loc_261B")

    label("loc_254E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_261B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_25D6")

    #C0088
    ChrTalk(
        0x9,
        (
            "先ほどの演習は、\x01",
            "大変いい経験になりました！\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "今後の警備に、是非とも\x01",
            "生かしていきたい所存であります！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_261B")

    label("loc_25D6")


    #C0090
    ChrTalk(
        0x9,
        "異常・ナシ！\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "通商会議にむけて、\x01",
            "警備体制は万全であります！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_261B")

    TalkEnd(0xFE)
    Return()

    # Function_10_1989 end

    def Function_11_261F(): pass

    label("Function_11_261F")

    Call(0, 12)
    Return()

    # Function_11_261F end

    def Function_12_2623(): pass

    label("Function_12_2623")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_264C")
    Call(0, 27)
    Return()

    label("loc_264C")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2659")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_306E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26B7")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_26B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26D7")
    OP_AF(0x6E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3069")

    label("loc_26D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26EB")
    Jump("loc_3069")

    label("loc_26EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2703")
    TalkEnd(0xA)
    Return()

    label("loc_2703")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3069")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_27A8")

    #C0092
    ChrTalk(
        0xA,
        (
            "鍋は簡単で美味しいから、\x01",
            "タングラム門でもよくやるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "みんなでワイワイ鍋を囲むのは、\x01",
            "やっぱり賑やかで楽しいよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3069")

    label("loc_27A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_28E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2868")

    #C0094
    ChrTalk(
        0xA,
        (
            "こんな時だけど……\x01",
            "何か食べていくかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        (
            "不安になったりイライラするのは、\x01",
            "きっと腹が減っているせいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xA,
        (
            "うんと食べてから、\x01",
            "一度心を落ち着けるといいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_28E0")

    label("loc_2868")


    #C0097
    ChrTalk(
        0xA,
        (
            "不安になったりイライラするのは、\x01",
            "きっと腹が減っているせいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xA,
        (
            "うんと食べてから、\x01",
            "一度心を落ち着けるといいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28E0")

    Jump("loc_3069")

    label("loc_28E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29BE")

    #C0099
    ChrTalk(
        0xA,
        (
            "警備隊の被害……\x01",
            "隊員じゃない僕やラグさんも\x01",
            "かなり堪える出来事だった。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xA,
        (
            "志半ばで倒れてしまって、\x01",
            "彼らも悔しかったろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "せめて、残された隊員たちは\x01",
            "元気を取り戻して欲しいな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A49")

    label("loc_29BE")


    #C0102
    ChrTalk(
        0xA,
        (
            "犠牲となった隊員たち……\x01",
            "志半ばで倒れてしまって、\x01",
            "彼らも悔しかったろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "せめて、残された隊員たちは\x01",
            "元気を取り戻して欲しいな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A49")

    Jump("loc_3069")

    label("loc_2A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2ADA")

    #C0104
    ChrTalk(
        0xA,
        (
            "昨日は、列車の振り替え輸送バスで\x01",
            "沢山の客が送られてきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        (
            "大多数はもう帰っていったけど、\x01",
            "さすがに大変だったな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3069")

    label("loc_2ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B90")

    #C0106
    ChrTalk(
        0xA,
        (
            "緊張状態の続くこの状況、\x01",
            "僕みたいなしがない料理人が\x01",
            "できることは少ないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "隊のみんなが\x01",
            "１００％の力を発揮できるよう、\x01",
            "せめてウマい料理を作らなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3069")

    label("loc_2B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2CE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C5E")

    #C0108
    ChrTalk(
        0xA,
        (
            "独立提唱か……クロスベルも\x01",
            "なんだか大変なことになってきたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xA,
        (
            "帝国や共和国がすんなりと\x01",
            "許してくれるとは思えないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        (
            "個人的にも、市長たちには\x01",
            "頑張ってほしいかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2CE1")

    label("loc_2C5E")


    #C0111
    ChrTalk(
        0xA,
        (
            "帝国や共和国が、\x01",
            "独立なんてものをすんなりと\x01",
            "許してくれるとは思えないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xA,
        (
            "個人的にも、市長たちには\x01",
            "頑張ってほしいかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CE1")

    Jump("loc_3069")

    label("loc_2CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2D7D")

    #C0113
    ChrTalk(
        0xA,
        (
            "テロへの対策で、\x01",
            "警備隊のみんなもかなり\x01",
            "気合が入ってるみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "ここはガッツリと食べてもらって、\x01",
            "一日頑張ってもらわないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3069")

    label("loc_2D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2F0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E6F")

    #C0115
    ChrTalk(
        0xA,
        (
            "カルバードといえば、\x01",
            "昔から多くの異文化を\x01",
            "受け入れてきた国だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        (
            "東方文化もその一つで、\x01",
            "料理の世界にも多大な影響を\x01",
            "与えたとされている。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xA,
        (
            "実際、東方料理は絶品だからね。\x01",
            "コックとしても学ぶところが多いよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F0A")

    label("loc_2E6F")


    #C0118
    ChrTalk(
        0xA,
        (
            "共和国が受け入れた東方文化は、\x01",
            "料理の世界にも多大な影響を\x01",
            "与えたとされている。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xA,
        (
            "実際、東方料理は絶品だからね。\x01",
            "コックとしても学ぶところが多いよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F0A")

    Jump("loc_3069")

    label("loc_2F0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3069")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF2")

    #C0120
    ChrTalk(
        0xA,
        (
            "新しく来た副司令サンは、\x01",
            "なかなか面白い兄さんでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "クールなソーニャ司令とは\x01",
            "また違うタイプで、グイグイと\x01",
            "皆を引っ張っていく頼もしい人だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xA,
        (
            "警備隊にも、まだまだ\x01",
            "優秀な人がいたんだなあ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3069")

    label("loc_2FF2")


    #C0123
    ChrTalk(
        0xA,
        (
            "新しい副司令サンは、\x01",
            "グイグイ皆を引っ張っていく\x01",
            "頼もしい人だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        (
            "警備隊にも、まだまだ\x01",
            "優秀な人がいたんだなあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3069")

    Jump("loc_2659")

    label("loc_306E")

    TalkEnd(0xA)
    Return()

    # Function_12_2623 end

    def Function_13_3072(): pass

    label("Function_13_3072")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3221")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_317A")

    #N0125
    NpcTalk(
        0xB,
        "兵士アレクセイ",
        "ふう……なんだか食欲がない。\x02",
    )

    CloseMessageWindow()

    #N0126
    NpcTalk(
        0xB,
        "兵士アレクセイ",
        (
            "……いや、こんなときこそ\x01",
            "無理してでも食べておかないとな。\x02",
        )
    )

    CloseMessageWindow()

    #N0127
    NpcTalk(
        0xB,
        "兵士アレクセイ",
        (
            "帝国や共和国の侵攻に備えて、\x01",
            "このクロスベルを守る……\x01",
            "……その使命を全うするためにも。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_321C")

    label("loc_317A")


    #N0128
    NpcTalk(
        0xB,
        "兵士アレクセイ",
        (
            "色々な事が起こりすぎたからな……\x01",
            "どうも頭が混乱しているみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #N0129
    NpcTalk(
        0xB,
        "兵士アレクセイ",
        (
            "このクロスベルを守る。\x01",
            "……その使命を全うしなくちゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_321C")

    Jump("loc_394B")

    label("loc_3221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_32BF")

    #C0130
    ChrTalk(
        0xB,
        (
            "市の襲撃犯たちは、\x01",
            "今はどこに潜伏しているのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xB,
        "……フン、上等だ。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xB,
        (
            "仲間たちの敵を討つためにも……\x01",
            "いつか必ずあぶりだしてやる。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_394B")

    label("loc_32BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3352")

    #C0133
    ChrTalk(
        0xB,
        (
            "ふう……労働の後の食事は\x01",
            "まさに至高のウマさだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xB,
        (
            "今後も何が起こるか分からん……\x01",
            "腹ごしらえだけは\x01",
            "常にしておかなければな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_394B")

    label("loc_3352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_34DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_343F")

    #C0135
    ChrTalk(
        0xB,
        (
            "クロスベルが独立して、\x01",
            "警備隊が軍としての活動を\x01",
            "認められるようなことになったら……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xB,
        (
            "是非とも武装だけじゃなく、\x01",
            "レーションを改善してほしいものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xB,
        (
            "あれは本当に不味いとしか\x01",
            "言いようがないからな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_34D6")

    label("loc_343F")


    #C0138
    ChrTalk(
        0xB,
        (
            "……帝国軍で出される食事も、\x01",
            "かなり不味いと聞く。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xB,
        (
            "独立して脱・帝国を成せば、\x01",
            "きっとレーションも改善されるはずだ。\x01",
            "……完全に俺の想像だがな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34D6")

    Jump("loc_394B")

    label("loc_34DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_357E")

    #C0140
    ChrTalk(
        0xB,
        (
            "幻獣……報告を聞いた限りでは\x01",
            "かなり手強そうな相手だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xB,
        (
            "俺たち警備隊は国境の警戒に\x01",
            "集中する必要がある……\x01",
            "あとはあんたたちに任せたぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_394B")

    label("loc_357E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_363D")

    #C0142
    ChrTalk(
        0xB,
        (
            "テロリストが現れるかもって話だが……\x01",
            "実際、どういう方法で侵入を\x01",
            "しようとしてるかが重要だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xB,
        (
            "既に協力者が入り込んでる可能性もある。\x01",
            "今日は一瞬たりとも気が抜けないな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_394B")

    label("loc_363D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_37B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3729")

    #C0144
    ChrTalk(
        0xB,
        (
            "ああ、俺もミシュラムのほうの\x01",
            "警備に行きたかったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        (
            "一度だけ行ったことがあるが、\x01",
            "あそこのレストランのメシは\x01",
            "なかなか……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xB,
        (
            "……ミシュラムが休止中なのに\x01",
            "さすがにレストランなんか\x01",
            "やっちゃいないか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_37B3")

    label("loc_3729")


    #C0147
    ChrTalk(
        0xB,
        (
            "……ミシュラムが休止中なのに\x01",
            "さすがにレストランなんか\x01",
            "やっちゃいないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xB,
        (
            "……もぐもぐ。\x01",
            "とりあえず早くメシを\x01",
            "食っちまおうっと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B3")

    Jump("loc_394B")

    label("loc_37B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_394B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_38E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3870")

    #C0149
    ChrTalk(
        0xB,
        "ぱくぱく、もぐもぐ……\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xB,
        (
            "やはり演習のあとの\x01",
            "メシは格別だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xB,
        (
            "演習前にもさんざ\x01",
            "腹ごしらえをしたんだが、\x01",
            "コレばかりはやめられないね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38DE")

    label("loc_3870")


    #C0152
    ChrTalk(
        0xB,
        (
            "クソ不味いレーションですら、\x01",
            "演習後は美味く感じるもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xB,
        (
            "やはり演習のあとの\x01",
            "メシは格別だと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38DE")

    Jump("loc_394B")

    label("loc_38E3")


    #C0154
    ChrTalk(
        0xB,
        (
            "もぐもぐ……\x01",
            "うまいうまい……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xB,
        (
            "今日は演習をやるって話だし、\x01",
            "しっかり腹ごしらえしとかないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_394B")

    TalkEnd(0xFE)
    Return()

    # Function_13_3072 end

    def Function_14_394F(): pass

    label("Function_14_394F")

    Call(0, 15)
    Return()

    # Function_14_394F end

    def Function_15_3953(): pass

    label("Function_15_3953")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3960")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43C6")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",        # 0
            "休憩をする\x01",      # 1
            "やめる\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39BC")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_39BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39DC")
    OP_AF(0x6F)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43C1")

    label("loc_39DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39F0")
    Jump("loc_43C1")

    label("loc_39F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A08")
    TalkEnd(0xC)
    Return()

    label("loc_3A08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43C1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3B70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AEC")

    #C0156
    ChrTalk(
        0xC,
        (
            "風の噂で、イリアの意識が\x01",
            "戻ったと聞いてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xC,
        (
            "これから、クロスベルは\x01",
            "段々と大変な事態に\x01",
            "見舞われるだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xC,
        (
            "イリアという光がある限り、\x01",
            "きっと俺たちは大丈夫だ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3B6B")

    label("loc_3AEC")


    #C0159
    ChrTalk(
        0xC,
        (
            "これから、クロスベルは\x01",
            "段々と大変な事態に\x01",
            "見舞われるだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xC,
        (
            "イリアという光がある限り、\x01",
            "きっと俺たちは大丈夫だ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B6B")

    Jump("loc_43C1")

    label("loc_3B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3CED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C56")

    #C0161
    ChrTalk(
        0xC,
        (
            "イリア・プラティエは\x01",
            "クロスベルに住む多くの人々にとって\x01",
            "太陽のような存在なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xC,
        "そんな彼女が重傷を負っただなんて……\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xC,
        (
            "……ダメだ、仕事に身が入らない。\x01",
            "彼女は舞台に復帰できるんだろうか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3CE8")

    label("loc_3C56")


    #C0164
    ChrTalk(
        0xC,
        (
            "噂では、イリア・プラティエは\x01",
            "いまだに意識が戻ってないらしいが……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xC,
        (
            "……ダメだ、仕事に身が入らない。\x01",
            "彼女は舞台に復帰できるんだろうか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CE8")

    Jump("loc_43C1")

    label("loc_3CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3E62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DDE")

    #C0166
    ChrTalk(
        0xC,
        (
            "明日はいよいよアルカンシェルの\x01",
            "リニューアル公演……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xC,
        (
            "やはり注目は《星の姫》を演じる\x01",
            "期待の新人・シュリか……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xC,
        (
            "結局チケットはとれなかったが、\x01",
            "クロスベルタイムズが特集するだろう。\x01",
            "楽しみにしておくか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3E5D")

    label("loc_3DDE")


    #C0169
    ChrTalk(
        0xC,
        (
            "明日はいよいよアルカンシェルの\x01",
            "リニューアル公演……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xC,
        (
            "どんな出来なのか……\x01",
            "クロスベルタイムズの\x01",
            "次の特集が楽しみだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E5D")

    Jump("loc_43C1")

    label("loc_3E62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3EE4")

    #C0171
    ChrTalk(
        0xC,
        "近頃、何かとヒマでな。\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xC,
        (
            "明日も雨だという話しだし、\x01",
            "アルカンシェルのファンブックでも\x01",
            "読んでいるとするか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C1")

    label("loc_3EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4061")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FD7")

    #C0173
    ChrTalk(
        0xC,
        (
            "警備隊員たちは２大国の緊張状態で、\x01",
            "随分と忙しそうにしているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xC,
        (
            "そんな中、警備隊の仕事を\x01",
            "支援課とギルドが\x01",
            "引き受けてくれたらしいが……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xC,
        (
            "これからも、なんとか多方面と\x01",
            "補い合っていければいいんだがな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_405C")

    label("loc_3FD7")


    #C0176
    ChrTalk(
        0xC,
        (
            "警備隊の仕事を\x01",
            "支援課とギルドが\x01",
            "引き受けてくれたらしいが……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xC,
        (
            "これからも、なんとか多方面と\x01",
            "補い合っていければいいんだがな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_405C")

    Jump("loc_43C1")

    label("loc_4061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4219")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4175")

    #C0178
    ChrTalk(
        0xC,
        (
            "テロリズムの危険性は、\x01",
            "自分たちが“正義”だと\x01",
            "信じ込んでいるところにある。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xC,
        (
            "目的の為には犠牲は厭わない……\x01",
            "それを悪だと感じていないんだ、\x01",
            "はっきり言ってクソくらえだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xC,
        (
            "そんなことをさせないためにも、\x01",
            "隊の連中には頑張ってほしいもんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4214")

    label("loc_4175")


    #C0181
    ChrTalk(
        0xC,
        (
            "目的の為には犠牲は厭わない……\x01",
            "そんなクソくらえな思想が、\x01",
            "テロリズムの根本にある。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xC,
        (
            "そんなことをさせないためにも、\x01",
            "隊の連中には頑張ってほしいもんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4214")

    Jump("loc_43C1")

    label("loc_4219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_42B8")

    #C0183
    ChrTalk(
        0xC,
        (
            "クロスベル入りした首脳たちは\x01",
            "今夜、アルカンシェルの舞台を\x01",
            "観劇するらしいな……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xC,
        (
            "これが国賓の特権というやつか。\x01",
            "素直にうらやましいな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C1")

    label("loc_42B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_43C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4353")

    #C0185
    ChrTalk(
        0xC,
        (
            "アルカンシェルの公演が\x01",
            "近づいている……\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xC,
        (
            "チケットの売れ行きも\x01",
            "すさまじいスピードらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xC,
        "また諦めるしかないか……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_43C1")

    label("loc_4353")


    #C0188
    ChrTalk(
        0xC,
        (
            "俺はイリア・プラティエの\x01",
            "大ファンなんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xC,
        (
            "今度こそ公演を観に行きたいが、\x01",
            "また諦めるしかないか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43C1")

    Jump("loc_3960")

    label("loc_43C6")

    TalkEnd(0xC)
    Return()

    # Function_15_3953 end

    def Function_16_43CA(): pass

    label("Function_16_43CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4469")

    #C0190
    ChrTalk(
        0xD,
        (
            "まさか、旅行に来ていた先で\x01",
            "襲撃事件なんぞが起こるとはな……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xD,
        (
            "フン、街ひとつ守れんで何が警備隊じゃ。\x01",
            "こんな危ない国には居られんわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4594")

    label("loc_4469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4477")
    Jump("loc_4594")

    label("loc_4477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4488")
    Call(0, 8)
    Jump("loc_4594")

    label("loc_4488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4496")
    Jump("loc_4594")

    label("loc_4496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4521")

    #C0192
    ChrTalk(
        0xD,
        (
            "今日の本会議は\x01",
            "一体どんな様相を呈すのやら……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xD,
        (
            "共和国に帰ったら、\x01",
            "次号のクロスベルタイムズを\x01",
            "取り寄せてみるかのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4594")

    label("loc_4521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_452F")
    Jump("loc_4594")

    label("loc_452F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4594")

    #C0194
    ChrTalk(
        0xD,
        (
            "タングラム丘陵の運転で\x01",
            "疲れてしもうたわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xD,
        (
            "どれ、食堂でなにか\x01",
            "食べていくかのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4594")

    TalkEnd(0xFE)
    Return()

    # Function_16_43CA end

    def Function_17_4598(): pass

    label("Function_17_4598")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_461E")

    #C0196
    ChrTalk(
        0xE,
        (
            "うう、せっかく\x01",
            "結界が解除されたのに\x01",
            "共和国に帰れないなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xE,
        (
            "せめてこの子だけでも\x01",
            "守っていかなければ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48FE")

    label("loc_461E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_46EE")

    #C0198
    ChrTalk(
        0xE,
        (
            "クロスベルの人たちには同情するが……\x01",
            "ちゃんとした軍がいれば\x01",
            "被害は最小限に抑えられたはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xE,
        (
            "やはり、通商会議で出たという\x01",
            "大統領や《鉄血宰相》の案を\x01",
            "受け入れるべきだったんじゃないか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48FE")

    label("loc_46EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4794")

    #C0200
    ChrTalk(
        0xE,
        (
            "共和国方面に出張に行ってた同僚が、\x01",
            "列車事故に巻き込まれたらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xE,
        (
            "今から入院してる病院に向かうんだが……\x01",
            "ひとまず命が助かってよかったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48FE")

    label("loc_4794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_47A2")
    Jump("loc_48FE")

    label("loc_47A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_483F")

    #C0202
    ChrTalk(
        0xE,
        (
            "クロスベルの住民が\x01",
            "独立を考えるのは、ある意味\x01",
            "必然ともいえる気がするな。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xE,
        (
            "私の商売に悪影響が出ない限りは、\x01",
            "この流れを傍観してみるか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48FE")

    label("loc_483F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4850")
    Call(0, 9)
    Jump("loc_48FE")

    label("loc_4850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_485E")
    Jump("loc_48FE")

    label("loc_485E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_48FE")

    #C0204
    ChrTalk(
        0xE,
        (
            "私は個人の雑貨商でね。\x01",
            "クロスベルには仕入れに来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xE,
        (
            "大陸の交差点であるクロスベルでは\x01",
            "実に色々な商品が見つかる。\x01",
            "ふふ、今から楽しみだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48FE")

    TalkEnd(0xFE)
    Return()

    # Function_17_4598 end

    def Function_18_4902(): pass

    label("Function_18_4902")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_497B")

    #C0206
    ChrTalk(
        0xF,
        (
            "もう、お父さんったら\x01",
            "興奮しちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xF,
        (
            "オホホ、ごめんなさいね。\x01",
            "気を悪くしないでちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AE6")

    label("loc_497B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4989")
    Jump("loc_4AE6")

    label("loc_4989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4997")
    Jump("loc_4AE6")

    label("loc_4997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4A35")

    #C0208
    ChrTalk(
        0xF,
        (
            "なんでも、最近クロスベルで\x01",
            "得体の知れない大型の魔獣が\x01",
            "現れるんですってね？\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xF,
        (
            "やだ、怖いわあ……\x01",
            "旅行に来る時期を\x01",
            "間違えちゃったかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AE6")

    label("loc_4A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4A43")
    Jump("loc_4AE6")

    label("loc_4A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4ADD")

    #C0210
    ChrTalk(
        0xF,
        (
            "オルキスタワーとやらが気になって\x01",
            "ついつい見物に来ちゃったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xF,
        (
            "除幕式でのお披露目はもう見ちゃったし、\x01",
            "そろそろ帰るとしましょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AE6")

    label("loc_4ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4AE6")

    label("loc_4AE6")

    TalkEnd(0xFE)
    Return()

    # Function_18_4902 end

    def Function_19_4AEA(): pass

    label("Function_19_4AEA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4AFB")
    Jump("loc_4CB3")

    label("loc_4AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4B2D")

    #C0212
    ChrTalk(
        0x10,
        "は～、早くバスが来ねえかな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4CB3")

    label("loc_4B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4C03")

    #C0213
    ChrTalk(
        0x10,
        (
            "そういえば昨日、\x01",
            "偽ブランド商をやってたバーさんが\x01",
            "アルタイル市で逮捕されたんだと。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x10,
        (
            "いやー、折角シャキシャキしてるのに\x01",
            "悪徳商法なんかに手を染めちまうなんて、\x01",
            "ある意味可哀想なバーさんだよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB3")

    label("loc_4C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4C11")
    Jump("loc_4CB3")

    label("loc_4C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4C1F")
    Jump("loc_4CB3")

    label("loc_4C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4CAA")

    #C0215
    ChrTalk(
        0x10,
        (
            "今朝は交通規制で、\x01",
            "タングラム丘陵もまったく\x01",
            "通行できなかったんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x10,
        (
            "まあ、大統領の訪問だから\x01",
            "仕方ないんだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB3")

    label("loc_4CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4CB3")

    label("loc_4CB3")

    TalkEnd(0xFE)
    Return()

    # Function_19_4AEA end

    def Function_20_4CB7(): pass

    label("Function_20_4CB7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4D2A")

    #C0217
    ChrTalk(
        0x11,
        (
            "ああ、もうっ！\x01",
            "どうしてこんなことに\x01",
            "なってしまったのかしら！\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x11,
        "一体誰のせいなの、ねえ！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E8D")

    label("loc_4D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4D38")
    Jump("loc_4E8D")

    label("loc_4D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4D46")
    Jump("loc_4E8D")

    label("loc_4D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4D54")
    Jump("loc_4E8D")

    label("loc_4D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4E05")

    #C0219
    ChrTalk(
        0x11,
        (
            "門の隊員さんたち、\x01",
            "なんだかコワいっていうかぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x11,
        (
            "緊張状態だか何だか知らないけどぉ……\x01",
            "もうちょっとアイソよくしたって\x01",
            "バチはあたらないんじゃないのォ～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E8D")

    label("loc_4E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4E13")
    Jump("loc_4E8D")

    label("loc_4E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4E21")
    Jump("loc_4E8D")

    label("loc_4E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4E8D")

    #C0221
    ChrTalk(
        0x11,
        (
            "えっと、クロスベル市へのバスは\x01",
            "どこから出てるんだっけ……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x11,
        "乗り継ぎって面倒よね、やっぱ。\x02",
    )

    CloseMessageWindow()

    label("loc_4E8D")

    TalkEnd(0xFE)
    Return()

    # Function_20_4CB7 end

    def Function_21_4E91(): pass

    label("Function_21_4E91")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4ECB")

    #C0223
    ChrTalk(
        0x12,
        (
            "パパ～……\x01",
            "おうちに帰りたいよう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F62")

    label("loc_4ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4ED9")
    Jump("loc_4F62")

    label("loc_4ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4EE7")
    Jump("loc_4F62")

    label("loc_4EE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4EF5")
    Jump("loc_4F62")

    label("loc_4EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4F03")
    Jump("loc_4F62")

    label("loc_4F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F4B")

    #C0224
    ChrTalk(
        0x12,
        (
            "おじいちゃん、\x01",
            "ムズカシー話はいいから\x01",
            "食べようよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F62")

    label("loc_4F4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4F59")
    Jump("loc_4F62")

    label("loc_4F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4F62")

    label("loc_4F62")

    TalkEnd(0xFE)
    Return()

    # Function_21_4E91 end

    def Function_22_4F66(): pass

    label("Function_22_4F66")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F7B")
    Call(0, 23)
    Jump("loc_4FF9")

    label("loc_4F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F8D")
    Call(0, 24)
    Jump("loc_4FF9")

    label("loc_4F8D")


    #C0225
    ChrTalk(
        0xFE,
        (
            "とりあえず……\x01",
            "今は仕事に集中しないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "君たちも仕事があるだろうし、\x01",
            "こっちの調査は任せてくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FF9")

    TalkEnd(0xFE)
    Return()

    # Function_22_4F66 end

    def Function_23_4FFD(): pass

    label("Function_23_4FFD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x13, 0x10)
    TurnDirection(0x13, 0x0, 0)
    OP_52(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_508E")
    Jump("loc_50D8")

    label("loc_508E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_50AE")
    OP_52(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50D8")

    label("loc_50AE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_50CE")
    OP_52(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50D8")

    label("loc_50CE")

    OP_52(0x13, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50D8")

    OP_52(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x13, 0x10)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x0, 0)
    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_518E")
    Jump("loc_51D8")

    label("loc_518E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_51AE")
    OP_52(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_51D8")

    label("loc_51AE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_51CE")
    OP_52(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_51D8")

    label("loc_51CE")

    OP_52(0x14, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_51D8")

    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x14, 0x10)

    #C0227
    ChrTalk(
        0x13,
        "やあ、君たちか。\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x101,
        (
            "#00000Fスコットさんたち……\x01",
            "国境まで来ていたんですね。\x02\x03",

            "もしかして、共和国方面……\x01",
            "あるいはタングラム丘陵に幻獣が？\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x14,
        "いや、そういうわけじゃない。\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x14,
        (
            "タングラム丘陵付近に\x01",
            "出現したとしても\x01",
            "警備隊の管轄だろうしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x109,
        (
            "#10100Fそれは確かにそうですね。\x01",
            "……えっと、それじゃあ？\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x13,
        (
            "俺たちは、君たちが昨日幻獣を退治した\x01",
            "東クロスベル街道の近辺を調査してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x13,
        (
            "報告にあった『プレロマ草』とやらが\x01",
            "本当に幻獣と関係あるとしたら、\x01",
            "他に咲いてないか確認はしておかないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x103,
        (
            "#00200Fなるほど……\x01",
            "確かに確認は必要そうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x104,
        (
            "#00300F遊撃士の兄さんたちなら\x01",
            "俺たちが入れないような\x01",
            "奥地の方も探索出来るだろうしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x13,
        "まあ、そういうことだ。\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x13,
        (
            "とりあえずこっちは任せてくれ。\x01",
            "君たちにも君たちにしか\x01",
            "できない事があるだろうしな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrSubChip(0x13, 0x0)
    SetChrSubChip(0x14, 0x0)
    SetScenarioFlags(0x17C, 7)
    Return()

    # Function_23_4FFD end

    def Function_24_550C(): pass

    label("Function_24_550C")

    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrSubChip(0x13, 0x0)
    SetChrSubChip(0x14, 0x0)

    #C0238
    ChrTalk(
        0x13,
        (
            "それにしても……\x01",
            "通商会議に続いてなかなか\x01",
            "忙しさが抜けないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x13,
        (
            "婚約者のパールにも\x01",
            "なかなか会ってやれないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x14,
        "百貨店で働いている娘か……\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x14,
        (
            "まあ……今は致し方あるまい。\x01",
            "人手も足りない状況だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x14,
        (
            "一通りの案件が片付いたら、\x01",
            "ミシェルに休暇を申請するといい。\x01",
            "日程の調整には俺も協力する。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x13,
        (
            "はは、ありがとうヴェンツェル。\x01",
            "お前には助けられてばかりだな。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x10)
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 3)
    Return()

    # Function_24_550C end

    def Function_25_56A6(): pass

    label("Function_25_56A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56BB")
    Call(0, 23)
    Jump("loc_577E")

    label("loc_56BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56CD")
    Call(0, 24)
    Jump("loc_577E")

    label("loc_56CD")


    #C0244
    ChrTalk(
        0xFE,
        (
            "お前たちの報告を受けて確認したが、\x01",
            "他の幻獣出現地点にもひっそりと\x01",
            "『プレロマ草』が咲いていた。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "……何とも得体のしれない植物だ。\x01",
            "重々注意していたほうがよさそうだな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_577E")

    TalkEnd(0xFE)
    Return()

    # Function_25_56A6 end

    def Function_26_5782(): pass

    label("Function_26_5782")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5820")

    #C0246
    ChrTalk(
        0xFE,
        (
            "街の襲撃事件のときは、\x01",
            "アルモリカ村にいたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "一応連絡をとったら、\x01",
            "リュウもお父さんも\x01",
            "無事だって……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        "……本当に安心した。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_5863")

    label("loc_5820")


    #C0249
    ChrTalk(
        0xFE,
        (
            "もう少ししたら家に帰ろうかな。\x01",
            "リュウとお父さんが心配だし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5863")

    TalkEnd(0xFE)
    Return()

    # Function_26_5782 end

    def Function_27_5867(): pass

    label("Function_27_5867")

    EventBegin(0x0)
    Fade(500)
    OP_68(106160, 1050, 2060, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26130, 0)
    SetChrPos(0x101, 104310, 0, 2009, 90)
    SetChrPos(0x109, 104340, 0, 3150, 135)
    SetChrPos(0x102, 104290, 0, 980, 90)
    SetChrPos(0x104, 104150, 0, -190, 45)
    SetChrPos(0x103, 103100, 0, 930, 90)
    SetChrPos(0x105, 102910, 0, -220, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0x109, 0)
    OP_0D()

    #C0250
    ChrTalk(
        0xA,
        (
            "やあ、ノエル曹長。\x01",
            "特務支援課の皆さんといっしょかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x109,
        "#10100Fお疲れ様です、ティマスさん。\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        (
            "#00000Fえっと、今日は仕事で\x01",
            "来たんですが……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)
    SetChrName("")

    #A0253
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『一押しグルメ』の取材で\x01",
            "来たことを説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0254
    ChrTalk(
        0xA,
        (
            "ああ、確かに通信社に\x01",
            "そんなことを頼まれてたかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xA,
        (
            "ちょうど、タングラム門名物の\x01",
            "『芳醇潮鍋』が出来たところだ。\x01",
            "みんなで食べていくといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x104,
        (
            "#00305Fああ、こっちの食堂じゃ\x01",
            "魚鍋がメインだったんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x102,
        "#00100Fふふ、よろしくお願いします。\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xA,
        (
            "それじゃ、待っててくれ。\x01",
            "いま取り分けるからね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    #A0259
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちは芳醇潮鍋を食べた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0260
    ChrTalk(
        0x103,
        (
            "#00200Fもぐもぐ……\x01",
            "なかなか風味がいいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x101,
        (
            "#00000Fああ、魚本来の味が\x01",
            "よく出ているみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xA,
        "はは、だろう？\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xA,
        (
            "鍋は簡単で美味しいから、\x01",
            "タングラム門でもよくやるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xA,
        (
            "みんなでワイワイ鍋を囲むのは、\x01",
            "やっぱり賑やかで楽しいよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x105,
        (
            "#10304F……そういえば、テスタメンツの皆と\x01",
            "こんな風に鍋をつついたりしたことは\x01",
            "あんまりなかったかな。\x02\x03",

            "#10302Fフフ、機会があったら皆で\x01",
            "遊びに来てもいいかもしれないね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5D1D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5D1D)
    Sleep(50)

    def lambda_5D2D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5D2D)
    Sleep(50)

    def lambda_5D3D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D3D)
    Sleep(50)

    def lambda_5D4D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5D4D)
    Sleep(50)

    def lambda_5D5D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5D5D)
    Sleep(300)

    #C0266
    ChrTalk(
        0x104,
        (
            "#00305Fへえ……\x01",
            "何だか珍しい事を言うな。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x102,
        (
            "#00102Fふふ、この料理を\x01",
            "結構気に入ったんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x103,
        (
            "#00200Fだったら、ここの紹介は\x01",
            "ワジさんに任せたほうが\x01",
            "いいかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x1F4)

    #C0269
    ChrTalk(
        0x105,
        (
            "#10304Fやれやれ、面倒だけど\x01",
            "引き受けてあげるとしようかな。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x173, 3)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_5EAE")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_5ECB")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_5EDE")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5EDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_5EF1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5EF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_5F0E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_5F21")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_5F3E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_5F51")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_5F6E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_5F81")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_5F9E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F9E")

    OP_29(0x80, 0x1, 0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60A1")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0270
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "飲食店６ヶ所の取材を終えた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6098")

    #A0271
    AnonymousTalk(
        0x101,
        (
            "#00003Fすぐにでもグレイスさんに\x01",
            "報告に行く事はできそうだけど……\x02\x03",

            "#00000Fまだ６人全員のお気に入りが\x01",
            "見つかったわけじゃない。\x01",
            "もう少し頑張ってみるかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6098")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_60A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6172")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0272
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "特務支援課メンバー全員の\x01",
            "お気に入りを見つけた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0273
    AnonymousTalk(
        0x101,
        (
            "#00000Fこれで６人全員の\x01",
            "お気に入りが見つかった。\x02\x03",

            "取材はこれで十分だな。\x01",
            "さっそく通信社に報告へ行こう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_6172")

    OP_4C(0xA, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 104640, 0, 1980, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_5867 end

    def Function_28_61A2(): pass

    label("Function_28_61A2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(7990, 1000, 40, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(24500, 0)
    SetChrFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 10950, 0, 4070, 180)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x5, 0x0, 0x8C, 0x1, 0x8)
    Sleep(300)
    Sound(143, 0, 100, 0)
    Sleep(200)
    Sound(145, 0, 100, 0)
    Sleep(1500)
    Sound(486, 0, 80, 0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x79, 0xB4, 0x1, 0x20)
    BeginChrThread(0x17, 1, 0, 29)
    Sleep(1500)
    Sound(487, 0, 50, 0)
    Sound(494, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x8, 0x87, 0x0)
    OP_93(0x9, 0x87, 0x0)
    Sleep(1000)
    Sound(486, 0, 80, 0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x79, 0xB4, 0x1, 0x20)
    BeginChrThread(0x18, 1, 0, 29)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1500)
    Sound(487, 0, 50, 0)
    Sound(494, 0, 100, 0)
    Sleep(1500)
    OP_64(0x8)
    OP_64(0x9)

    #C0274
    ChrTalk(
        0x8,
        "な……なんだあ……？\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x9,
        (
            "ほっ、報告！\x01",
            "ダグラス副司令に報告であります！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("e4101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_61A2 end

    def Function_29_636A(): pass

    label("Function_29_636A")

    SetChrPos(0xFE, -3500, 0, 0, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -2000, 0, 0)
    OP_9F(0x1, 3500, 0, -4000)
    OP_9F(0x1, 10500, 0, -4000)
    OP_9F(0x1, 25000, 0, -4000)
    OP_9F(0x2, 0xFE, 7000, 0x6)
    Return()

    # Function_29_636A end

    def Function_30_63C1(): pass

    label("Function_30_63C1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-20630, 1000, -340, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(20760, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x101, -28060, 0, 0, 270)
    SetChrPos(0x102, -28260, 0, -1200, 270)
    SetChrPos(0x104, -28260, 0, 1200, 270)
    SetChrPos(0x109, -29460, 0, 0, 270)
    SetChrPos(0x103, -29260, 0, -1200, 270)
    SetChrPos(0x105, -29260, 0, 1200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_647F():
        OP_95(0x101, -21060, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_647F)
    Sleep(30)

    def lambda_649C():
        OP_95(0x102, -21260, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_649C)
    Sleep(40)

    def lambda_64B9():
        OP_95(0x104, -21260, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_64B9)
    Sleep(800)

    def lambda_64D6():
        OP_95(0x109, -23560, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_64D6)
    Sleep(30)

    def lambda_64F3():
        OP_95(0x103, -23360, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_64F3)
    Sleep(10)

    def lambda_6510():
        OP_95(0x105, -23360, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6510)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0276
    ChrTalk(
        0x101,
        "#00000Fあ、あれは……！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(7990, 1000, 40, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(24500, 0)
    SetChrFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 10950, 0, 4070, 180)
    OP_4B(0x9, 0xFF)
    OP_0D()
    OP_71(0x5, 0x0, 0x8C, 0x1, 0x8)
    Sleep(300)
    Sound(143, 0, 100, 0)
    Sleep(200)
    Sound(145, 0, 100, 0)
    Sleep(1500)
    Sound(486, 0, 80, 0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x79, 0xB4, 0x1, 0x20)
    BeginChrThread(0x17, 1, 0, 29)
    Sleep(1500)
    Sound(487, 0, 50, 0)
    Sound(494, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x8, 0x87, 0x0)
    OP_93(0x9, 0x87, 0x0)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0277
    ChrTalk(
        0x8,
        "な……なんだあ……？\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x9,
        (
            "ほっ、報告！\x01",
            "ダグラス副司令に報告であります！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x8)
    OP_64(0x9)
    Fade(500)
    OP_68(-20630, 1000, -340, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(20760, 0)
    OP_0D()

    #C0279
    ChrTalk(
        0x102,
        "#00107Fああっ……\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x104,
        "#00306F逃がしちまったか……\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x101,
        (
            "#00003Fくそっ、あの運搬車には\x01",
            "騙し取られた医療物資が……\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x103,
        (
            "#00200Fでも……\x01",
            "もう追いかけようがありません。\x02\x03",

            "#00206F一歩遅かったみたいですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x109,
        (
            "#10108Fこちらも導力車を使って\x01",
            "追いかけてくるべきでしたね……\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x105,
        (
            "#10306Fやれやれ、依頼は失敗ってことか。\x01",
            "……どうするんだい、ロイド？\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        (
            "#00008F……ひとまず、\x01",
            "ビリーさんたちに連絡しよう。\x02\x03",

            "#00003F悔しいけど……\x01",
            "捕まえられなかったことを\x01",
            "きちんと報告しないとな。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0286
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちは事の顛末を\x01",
            "クロスベル空港で待つ\x01",
            "ビリーとリカルドに伝え……\x02",
        )
    )

    CloseMessageWindow()

    #A0287
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ビリーと共に\x01",
            "ウルスラ病院へ事情を\x01",
            "伝えに行くのだった。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 2)
    NewScene("t1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_63C1 end

    def Function_31_6A25(): pass

    label("Function_31_6A25")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0288
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "この先、警備隊専用貨物線路\x01",
            "  関係者以外立ち入り禁止\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_31_6A25 end

    SaveToFile()

Try(main)
