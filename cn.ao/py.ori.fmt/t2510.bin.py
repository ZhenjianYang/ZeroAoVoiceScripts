from ScenarioHelper import *

def main():
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
        "奥利弗队员",             # 1
        "杰克队员",               # 2
        "提马斯",                 # 3
        "阿雷库瑟队员",           # 4
        "拉古",                   # 5
        "游客",                   # 6
        "游客",                   # 7
        "游客",                   # 8
        "游客",                   # 9
        "游客",                   # 10
        "男孩",                   # 11
        "游击士斯克特",           # 12
        "游击士温蔡尔",           # 13
        "琪露露",                 # 14
        "特别任务支援科车辆",     # 15
        "运输车",                 # 16
        "剧情用",                 # 17
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
        "Function_8_1553",         # 08, 8
        "Function_9_165C",         # 09, 9
        "Function_10_174F",        # 0A, 10
        "Function_11_214F",        # 0B, 11
        "Function_12_2153",        # 0C, 12
        "Function_13_29D6",        # 0D, 13
        "Function_14_3127",        # 0E, 14
        "Function_15_312B",        # 0F, 15
        "Function_16_3A12",        # 10, 16
        "Function_17_3BBA",        # 11, 17
        "Function_18_3E96",        # 12, 18
        "Function_19_4010",        # 13, 19
        "Function_20_418F",        # 14, 20
        "Function_21_42FF",        # 15, 21
        "Function_22_43BE",        # 16, 22
        "Function_23_4445",        # 17, 23
        "Function_24_48D6",        # 18, 24
        "Function_25_4A32",        # 19, 25
        "Function_26_4AEC",        # 1A, 26
        "Function_27_4BB5",        # 1B, 27
        "Function_28_53BC",        # 1C, 28
        "Function_29_557A",        # 1D, 29
        "Function_30_55D1",        # 1E, 30
        "Function_31_5BD3",        # 1F, 31
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
            "摆放着车辆杂志《突进·急行少年！》。\x07\x00\x02",
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
            "导力车喷漆式样\x01\x07\x02",

            "『警备色彩』\x07\x00",
            "已经记下来了。\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CFF")

    #N0003
    NpcTalk(
        0x8,
        "士兵奥利弗",
        (
            "有一些没有及时逃离克洛斯贝尔的\x01",
            "共和国人到这里来了。\x02",
        )
    )

    CloseMessageWindow()

    #N0004
    NpcTalk(
        0x8,
        "士兵奥利弗",
        (
            "但现在还没有解除\x01",
            "对共和国的警戒，\x01",
            "我们不得不拦住他们。\x02",
        )
    )

    CloseMessageWindow()

    #N0005
    NpcTalk(
        0x8,
        "士兵奥利弗",
        (
            "其实我很理解他们那归心似箭的心情，\x01",
            "所以有些不好受……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D84")

    label("loc_CFF")


    #N0006
    NpcTalk(
        0x8,
        "士兵奥利弗",
        (
            "现在还没有解除\x01",
            "对共和国的警戒，\x01",
            "我们不得不拦住他们。\x02",
        )
    )

    CloseMessageWindow()

    #N0007
    NpcTalk(
        0x8,
        "士兵奥利弗",
        (
            "虽然他们可能难以接受，\x01",
            "但也只能希望他们理解了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D84")

    Jump("loc_154F")

    label("loc_D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1033")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E45")

    #C0008
    ChrTalk(
        0x8,
        (
            "刚才强行通过大门的\x01",
            "那辆黑色运输车，\x01",
            "似乎是一名通缉诈骗犯的。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "在这种紧张时期发生这种情况，真是吓了一跳……\x01",
            "不管怎么说，能抓住他真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E99")

    label("loc_E45")


    #C0010
    ChrTalk(
        0x8,
        "总之，你们辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "我们已经向\x01",
            "道格拉斯副司令报告过了，\x01",
            "你们不必担心那边。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E99")

    Jump("loc_102E")

    label("loc_E9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_F24")

    #C0012
    ChrTalk(
        0x8,
        (
            "刚才强行通过大门的\x01",
            "那辆黑色运输车，\x01",
            "似乎是一名通缉诈骗犯的。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "偏偏在这种紧张时期做出这样的蠢事……\x01",
            "真是的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102E")

    label("loc_F24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE2")

    #C0014
    ChrTalk(
        0x8,
        (
            "边境线一带的紧张程度\x01",
            "已经逼近极限了。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "虽然共和国方向有唐古拉姆丘陵\x01",
            "这个缓冲地带，\x01",
            "但还是不能掉以轻心。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "现在正是需要拿出干劲的时候，\x01",
            "必须要坚持做好警戒工作。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_102E")

    label("loc_FE2")


    #C0017
    ChrTalk(
        0x8,
        (
            "为了克洛斯贝尔，\x01",
            "现在正是需要拿出干劲的时候，\x01",
            "必须要坚持做好警戒工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_102E")

    Jump("loc_154F")

    label("loc_1033")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1184")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1105")

    #C0018
    ChrTalk(
        0x8,
        (
            "昨天，唐古拉姆门的队员们\x01",
            "也都在忙于应对脱轨事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "另外还要处理协助共和国的\x01",
            "旅客巴士等工作，\x01",
            "真是忙得不可开交。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "偏偏在这种紧张时期\x01",
            "发生事故……\x01",
            "哎呀呀，真是祸不单行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_117F")

    label("loc_1105")


    #C0021
    ChrTalk(
        0x8,
        (
            "偏偏在这种紧张时期\x01",
            "发生事故……\x01",
            "哎呀呀，真是祸不单行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "至少在居民投票活动之前，\x01",
            "千万别再发生\x01",
            "新的意外事故了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_117F")

    Jump("loc_154F")

    label("loc_1184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1195")
    Call(0, 8)
    Jump("loc_154F")

    label("loc_1195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_130D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1280")

    #C0023
    ChrTalk(
        0x8,
        (
            "最近似乎连共和国的人\x01",
            "都在讨论克洛斯贝尔的\x01",
            "独立问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "和克洛斯贝尔的民众不同，\x01",
            "他们大多数人都持反对意见。\x01",
            "呼，这也是没办法的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "马上就要举行居民投票了，\x01",
            "但是在这种情况下，\x01",
            "真的能实现独立吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1308")

    label("loc_1280")


    #C0026
    ChrTalk(
        0x8,
        (
            "马上就要举行居民投票了，\x01",
            "但是在这种情况下，\x01",
            "真的能实现独立吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "身为警备队的一员，\x01",
            "我自然希望顺利独立……\x01",
            "但终究还是很困难吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1308")

    Jump("loc_154F")

    label("loc_130D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_131E")
    Call(0, 9)
    Jump("loc_154F")

    label("loc_131E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_13A8")

    #C0028
    ChrTalk(
        0x8,
        (
            "之前因为交通管制而无法通行于\x01",
            "唐古拉姆丘陵的车辆，现在一口气都涌来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "呼，虽然已经有所预料，\x01",
            "但这下真是有的忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_154F")

    label("loc_13A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_154F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_141E")

    #C0030
    ChrTalk(
        0x8,
        (
            "道格拉斯副司令的演习\x01",
            "一直都是那种感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "虽然要求很严厉……\x01",
            "但还是要努力跟上啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_154F")

    label("loc_141E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14E0")

    #C0032
    ChrTalk(
        0x8,
        (
            "穿过这里，就是自治州\x01",
            "和共和国之间的缓冲地带\x01",
            "『唐古拉姆丘陵』了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "来往于这片丘陵的大多是\x01",
            "旅客巴士和导力车。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "这大概也是因为在共和国\x01",
            "导力车已经广泛普及了的缘故吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_154F")

    label("loc_14E0")


    #C0035
    ChrTalk(
        0x8,
        (
            "来往于唐古拉姆\x01",
            "丘陵的大多是\x01",
            "旅客巴士和导力车。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "这大概也是因为在共和国\x01",
            "导力车已经广泛普及了的缘故吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_154F")

    TalkEnd(0x8)
    Return()

    # Function_7_C10 end

    def Function_8_1553(): pass

    label("Function_8_1553")

    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160D")

    #C0037
    ChrTalk(
        0x8,
        "这么早就开车远行，真是辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "最近有人在\x01",
            "自治州境内目击到了\x01",
            "来历不明的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "在郊外开车的时候，\x01",
            "请务必多加小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xD,
        (
            "嗯，辛苦了，\x01",
            "我会小心的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1653")

    label("loc_160D")


    #C0041
    ChrTalk(
        0x8,
        (
            "……那么，请您在\x01",
            "入境证明书上签字。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xD,
        (
            "哦，好的。\x01",
            "（签字）……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1653")

    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_8_1553 end

    def Function_9_165C(): pass

    label("Function_9_165C")

    OP_4B(0x8, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1701")

    #C0043
    ChrTalk(
        0x8,
        (
            "到达市内后，请您去\x01",
            "市民会馆申请停车位。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "如果忘记了，就会被贴上\x01",
            "违章停车的标签，还请注意。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xE,
        (
            "哦，是这样啊，\x01",
            "没想到这么麻烦……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_1746")

    label("loc_1701")


    #C0046
    ChrTalk(
        0x8,
        (
            "到达市内后，请您去\x01",
            "市民会馆申请停车位。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xE,
        "好的好的，知道啦。\x02",
    )

    CloseMessageWindow()

    label("loc_1746")

    OP_4C(0x8, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_9_165C end

    def Function_10_174F(): pass

    label("Function_10_174F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1848")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C4")

    #N0048
    NpcTalk(
        0x9,
        "士兵杰克",
        "湿地方向无异常！\x02",
    )

    CloseMessageWindow()

    #N0049
    NpcTalk(
        0x9,
        "士兵杰克",
        (
            "那棵不可思议的大树到底是……\x01",
            "真让人不安。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1843")

    label("loc_17C4")


    #N0050
    NpcTalk(
        0x9,
        "士兵杰克",
        (
            "那棵不可思议的大树到底是……\x01",
            "真让人不安。\x02",
        )
    )

    CloseMessageWindow()

    #N0051
    NpcTalk(
        0x9,
        "士兵杰克",
        (
            "总、总之……\x01",
            "无论什么时候都要保持冷静！\x01",
            "冷静是最重要的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1843")

    Jump("loc_214B")

    label("loc_1848")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A2D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_18B9")

    #C0052
    ChrTalk(
        0x9,
        (
            "刚才真是\x01",
            "吓了我一跳。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        (
            "虽然抓住了犯人值得高兴……\x01",
            "……但还是应该\x01",
            "遵守规定啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A28")

    label("loc_18B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_1908")

    #C0054
    ChrTalk(
        0x9,
        (
            "刚才真是\x01",
            "吓了我一跳。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "……希望你们今后\x01",
            "遵守规定哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A28")

    label("loc_1908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C3")

    #C0056
    ChrTalk(
        0x9,
        (
            "共和国军已经在\x01",
            "边境附近的阿尔泰尔市\x01",
            "展开行动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "通过大型军事演习\x01",
            "对克洛斯贝尔施加压力……\x01",
            "这就是他们的目的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x9,
        (
            "情况不容乐观啊……\x01",
            "我们警备队必须要努力。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A28")

    label("loc_19C3")


    #C0059
    ChrTalk(
        0x9,
        (
            "共和国军已经在\x01",
            "边境附近的阿尔泰尔市\x01",
            "展开行动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "情况不容乐观啊……\x01",
            "我们警备队必须要努力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A28")

    Jump("loc_214B")

    label("loc_1A2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B97")

    #C0061
    ChrTalk(
        0x9,
        (
            "没有异常！对我们来说，\x01",
            "这点小雨只是毛毛雨而已！\x02",
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
        "#00206F……一点都不好笑。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "啊……\x01",
            "这、这不是\x01",
            "冷笑话啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        (
            "我只是想说，\x01",
            "这点小雨对工作\x01",
            "不会有什么影响……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x109,
        (
            "#10100F啊哈哈，我们明白的。\x01",
            "（……话说回来，气氛好像因此缓和了不少呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C1C")

    label("loc_1B97")


    #C0066
    ChrTalk(
        0x9,
        (
            "我、我只是想说，\x01",
            "这点小雨对工作\x01",
            "不会有什么影响……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "在这种紧张时期，\x01",
            "谁还有心情\x01",
            "开玩笑啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#00006F不、不用那么激动……\x02",
    )

    CloseMessageWindow()

    label("loc_1C1C")

    Jump("loc_214B")

    label("loc_1C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1D75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D02")

    #C0069
    ChrTalk(
        0x9,
        (
            "听说『幻兽』并没有出现在\x01",
            "唐古拉姆丘陵。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "那里是自治州与共和国之间的缓冲地带，\x01",
            "如果『幻兽』出现在那里，\x01",
            "想去消灭就很麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "现在也无法保证今后就不会出现……\x01",
            "总之，要严格执行警备工作！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D70")

    label("loc_1D02")


    #C0072
    ChrTalk(
        0x9,
        (
            "听说『幻兽』并没有出现在\x01",
            "唐古拉姆丘陵。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "现在也无法保证今后就不会出现……\x01",
            "总之，要严格执行警备工作！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D70")

    Jump("loc_214B")

    label("loc_1D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1F57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EFA")

    #C0074
    ChrTalk(
        0x9,
        (
            "在通商会议时遭到破坏的\x01",
            "雷达设施，不久之前已经\x01",
            "修复完毕。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "那些可恶的恐怖分子，\x01",
            "居然能在我们毫无察觉的\x01",
            "情况下破坏雷达设施……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "仔细想想，\x01",
            "真是不可思议呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        (
            "#00001F（……出现在地下的装甲车也是一样，\x01",
            "  光凭那些恐怖分子，\x01",
            "  很难准备得如此周全。）\x02\x03",

            "#00003F（说不定『结社』\x01",
            "  在暗中协助了他们吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x105,
        (
            "#10300F（呼，虽然没有证据，\x01",
            "  但可能性很高。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F52")

    label("loc_1EFA")


    #C0079
    ChrTalk(
        0x9,
        (
            "唔，关于那些恐怖分子，\x01",
            "目前仍然留有疑问……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "总之，现在必须\x01",
            "认真执行警备任务！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F52")

    Jump("loc_214B")

    label("loc_1F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_200F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC8")

    #C0081
    ChrTalk(
        0x9,
        "暂无异常！\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "可恶的恐怖分子……\x01",
            "既然收到了消息，\x01",
            "我们就会做好全力迎击的准备。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_200A")

    label("loc_1FC8")


    #C0083
    ChrTalk(
        0x9,
        (
            "我们警备队一定会\x01",
            "保护好各位首脑的！\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "……目前\x01",
            "没有异常！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_200A")

    Jump("loc_214B")

    label("loc_200F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_20B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2080")

    #C0085
    ChrTalk(
        0x9,
        (
            "洛克史密斯总统的安保工作\x01",
            "没有异常！！\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "接下来，继续开展\x01",
            "通商会议的警备工作！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20AB")

    label("loc_2080")


    #C0087
    ChrTalk(
        0x9,
        (
            "接下来，继续开展\x01",
            "通商会议的警备工作！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20AB")

    Jump("loc_214B")

    label("loc_20B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_214B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2116")

    #C0088
    ChrTalk(
        0x9,
        (
            "刚才的演习\x01",
            "真是一次很好的体验！\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "我一定会活用在今后的\x01",
            "警备工作中！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_214B")

    label("loc_2116")


    #C0090
    ChrTalk(
        0x9,
        "无异常！\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "面向通商会议的\x01",
            "警备体制万无一失！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_214B")

    TalkEnd(0xFE)
    Return()

    # Function_10_174F end

    def Function_11_214F(): pass

    label("Function_11_214F")

    Call(0, 12)
    Return()

    # Function_11_214F end

    def Function_12_2153(): pass

    label("Function_12_2153")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_217C")
    Call(0, 27)
    Return()

    label("loc_217C")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2189")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29D2")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21D9")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_21D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F9")
    OP_AF(0x6E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29CD")

    label("loc_21F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_220D")
    Jump("loc_29CD")

    label("loc_220D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2225")
    TalkEnd(0xA)
    Return()

    label("loc_2225")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29CD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_22BC")

    #C0092
    ChrTalk(
        0xA,
        (
            "火锅制作简单，而且很美味，\x01",
            "所以唐古拉姆门的人经常吃呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "大家围坐在一起，边聊边吃火锅，\x01",
            "又热闹又开心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29CD")

    label("loc_22BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_23B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_235E")

    #C0094
    ChrTalk(
        0xA,
        (
            "虽然现在的局势很紧张……\x01",
            "但还是吃点东西吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        (
            "会感觉烦躁不安，\x01",
            "一定是因为肚子饿了。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xA,
        (
            "只要大吃一顿，\x01",
            "心情就会平静下来了哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_23B4")

    label("loc_235E")


    #C0097
    ChrTalk(
        0xA,
        (
            "会感觉烦躁不安，\x01",
            "一定是因为肚子饿了。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xA,
        (
            "只要大吃一顿，\x01",
            "心情就会平静下来了哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B4")

    Jump("loc_29CD")

    label("loc_23B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_24E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247A")

    #C0099
    ChrTalk(
        0xA,
        (
            "警备队伤亡惨重……\x01",
            "我和拉古先生虽然不是队员，\x01",
            "但同样悲痛难耐。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xA,
        (
            "壮志未酬身先死……\x01",
            "那些牺牲的队员想必很不甘吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "至少希望剩下的队员们能\x01",
            "尽快振作起来……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_24DD")

    label("loc_247A")


    #C0102
    ChrTalk(
        0xA,
        (
            "壮志未酬身先死……\x01",
            "那些牺牲的队员\x01",
            "想必很不甘吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "至少希望剩下的队员们能\x01",
            "尽快振作起来……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24DD")

    Jump("loc_29CD")

    label("loc_24E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2558")

    #C0104
    ChrTalk(
        0xA,
        (
            "代替事故列车的巴士\x01",
            "昨天送来了很多客人。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        (
            "大多数人现在都已经回去了，\x01",
            "但当时还真是忙得不可开交。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29CD")

    label("loc_2558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_25F0")

    #C0106
    ChrTalk(
        0xA,
        (
            "在这种紧张局势下，\x01",
            "我这个小小的厨师\x01",
            "也帮不上什么忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "不过，我至少可以做出美味的料理，\x01",
            "让警备队的队员们\x01",
            "发挥出百分之百的力量。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29CD")

    label("loc_25F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_26F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2690")

    #C0108
    ChrTalk(
        0xA,
        (
            "独立提案啊……克洛斯贝尔\x01",
            "真是发生了大事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xA,
        (
            "虽然帝国和共和国\x01",
            "肯定不会轻易允许……\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        (
            "但我个人还是希望\x01",
            "市长他们坚持到底。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_26F3")

    label("loc_2690")


    #C0111
    ChrTalk(
        0xA,
        (
            "虽然帝国和共和国\x01",
            "肯定不会轻易允许\x01",
            "克洛斯贝尔独立……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xA,
        (
            "但我个人还是希望\x01",
            "市长他们坚持到底。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26F3")

    Jump("loc_29CD")

    label("loc_26F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_277B")

    #C0113
    ChrTalk(
        0xA,
        (
            "为了应对恐怖袭击，\x01",
            "警备队的所有成员\x01",
            "都干劲十足。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "在这种时候，一定要让他们大吃一顿，\x01",
            "一整天都保持充沛精力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29CD")

    label("loc_277B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_28C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_284D")

    #C0115
    ChrTalk(
        0xA,
        (
            "卡尔瓦德这个国家，\x01",
            "从很久以前开始就\x01",
            "不断吸收多种外来文化。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        (
            "东方文化作为其中之一，\x01",
            "在料理方面产生了\x01",
            "很大的影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xA,
        (
            "东方料理确实是极品，\x01",
            "身为厨师，有很多东西值得从中学习。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_28C4")

    label("loc_284D")


    #C0118
    ChrTalk(
        0xA,
        (
            "共和国所吸收的东方文化\x01",
            "在料理方面产生了\x01",
            "很大的影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xA,
        (
            "东方料理确实是极品，\x01",
            "身为厨师，有很多东西值得从中学习。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28C4")

    Jump("loc_29CD")

    label("loc_28C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_29CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_297E")

    #C0120
    ChrTalk(
        0xA,
        (
            "新来的副司令\x01",
            "是位很有意思的老兄呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "相比冷静的索妮亚司令，\x01",
            "完全是另一种类型，\x01",
            "但同样非常可靠，能很好的领导大家。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xA,
        (
            "警备队中真是\x01",
            "人才济济啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_29CD")

    label("loc_297E")


    #C0123
    ChrTalk(
        0xA,
        (
            "新来的副司令\x01",
            "非常可靠，\x01",
            "能很好的领导大家。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        (
            "警备队中真是\x01",
            "人才济济啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29CD")

    Jump("loc_2189")

    label("loc_29D2")

    TalkEnd(0xA)
    Return()

    # Function_12_2153 end

    def Function_13_29D6(): pass

    label("Function_13_29D6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2B47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AC0")

    #N0125
    NpcTalk(
        0xB,
        "士兵阿雷库瑟",
        "呼……没什么食欲呢。\x02",
    )

    CloseMessageWindow()

    #N0126
    NpcTalk(
        0xB,
        "士兵阿雷库瑟",
        (
            "……不行，在这种时期，\x01",
            "就算不想吃也得硬吃啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0127
    NpcTalk(
        0xB,
        "士兵阿雷库瑟",
        (
            "……这也是为了履行自己的使命──\x01",
            "抵御帝国和共和国的侵略，\x01",
            "保卫克洛斯贝尔这片土地。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2B42")

    label("loc_2AC0")


    #N0128
    NpcTalk(
        0xB,
        "士兵阿雷库瑟",
        (
            "发生了太多事情……\x01",
            "我的脑中一片混乱。\x02",
        )
    )

    CloseMessageWindow()

    #N0129
    NpcTalk(
        0xB,
        "士兵阿雷库瑟",
        (
            "……但我必须要履行自己的使命，\x01",
            "保卫克洛斯贝尔这片土地。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B42")

    Jump("loc_3123")

    label("loc_2B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2BC9")

    #C0130
    ChrTalk(
        0xB,
        (
            "袭击城市的罪犯\x01",
            "如今潜伏在哪里呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xB,
        "……哼，可恶的家伙。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xB,
        (
            "为了给同伴们报仇……\x01",
            "我早晚会把他们揪出来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3123")

    label("loc_2BC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2C46")

    #C0133
    ChrTalk(
        0xB,
        (
            "呼……劳动之后的饭菜\x01",
            "真是无上美味啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xB,
        (
            "不知今后还会发生什么事……\x01",
            "但不管在什么时候，\x01",
            "都要先填饱肚子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3123")

    label("loc_2C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2D8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D01")

    #C0135
    ChrTalk(
        0xB,
        (
            "等到克洛斯贝尔独立，\x01",
            "警备队重组为受国际认可的\x01",
            "正式军队时……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xB,
        (
            "最好不要只改善武装，\x01",
            "也适当改善一下伙食。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xB,
        (
            "现在那种食物真的只能\x01",
            "用难以下咽来形容……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2D86")

    label("loc_2D01")


    #C0138
    ChrTalk(
        0xB,
        (
            "……听说帝国军的伙食\x01",
            "也相当难吃。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xB,
        (
            "如果能顺利独立，脱离帝国的控制，\x01",
            "伙食应该也会有所改善吧。\x01",
            "……当然，这只是我的想象而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D86")

    Jump("loc_3123")

    label("loc_2D8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2E22")

    #C0140
    ChrTalk(
        0xB,
        (
            "幻兽……从报告来看，\x01",
            "似乎是相当难对付的怪物啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xB,
        (
            "我们警备队必须要集中精神，\x01",
            "加强边境地区的警备工作……\x01",
            "幻兽的事情就交给你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3123")

    label("loc_2E22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2EB3")

    #C0142
    ChrTalk(
        0xB,
        (
            "听说可能会出现恐怖分子……\x01",
            "最重要的问题就是，\x01",
            "他们究竟会用什么方式入侵。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xB,
        (
            "可能已经有内应混进来了，\x01",
            "今天一刻都不能放松啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3123")

    label("loc_2EB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2FDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F73")

    #C0144
    ChrTalk(
        0xB,
        (
            "唉，我也想去米修拉姆\x01",
            "那边执行警备任务啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        (
            "我以前只去过一次，\x01",
            "那边餐馆里的饭菜\x01",
            "可真是美味无比……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xB,
        (
            "……但米修拉姆\x01",
            "已经停止营业了，\x01",
            "餐馆肯定也关门了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2FD7")

    label("loc_2F73")


    #C0147
    ChrTalk(
        0xB,
        (
            "……米修拉姆\x01",
            "已经停止营业了，\x01",
            "餐馆肯定也关门了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xB,
        (
            "……（嚼嚼）。\x01",
            "总之，\x01",
            "赶快把饭吃完吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FD7")

    Jump("loc_3123")

    label("loc_2FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3123")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_30D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3074")

    #C0149
    ChrTalk(
        0xB,
        "（嚼嚼嚼）……\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xB,
        (
            "演习之后的饭菜\x01",
            "果然格外好吃啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xB,
        (
            "虽然在演习之前\x01",
            "已经大吃了一顿，\x01",
            "但还是欲罢不能呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_30D2")

    label("loc_3074")


    #C0152
    ChrTalk(
        0xB,
        (
            "平时觉得难吃无比的伙食，\x01",
            "在演习之后也会觉得很美味。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xB,
        (
            "演习之后的饭菜\x01",
            "果然格外好吃啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30D2")

    Jump("loc_3123")

    label("loc_30D7")


    #C0154
    ChrTalk(
        0xB,
        (
            "（嚼嚼嚼）……\x01",
            "好吃好吃……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xB,
        (
            "据说今天要演习，\x01",
            "必须先把肚子填饱啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3123")

    TalkEnd(0xFE)
    Return()

    # Function_13_29D6 end

    def Function_14_3127(): pass

    label("Function_14_3127")

    Call(0, 15)
    Return()

    # Function_14_3127 end

    def Function_15_312B(): pass

    label("Function_15_312B")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3138")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A0E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3188")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3188")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31A8")
    OP_AF(0x6F)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A09")

    label("loc_31A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31BC")
    Jump("loc_3A09")

    label("loc_31BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31D4")
    TalkEnd(0xC)
    Return()

    label("loc_31D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A09")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3318")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_329E")

    #C0156
    ChrTalk(
        0xC,
        (
            "据说伊莉娅\x01",
            "已经恢复意识了。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xC,
        (
            "克洛斯贝尔今后\x01",
            "肯定还要面临各种\x01",
            "更加严峻的事态吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xC,
        (
            "但只要还有伊莉娅这道光芒存在，\x01",
            "我们就一定能战胜困难。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3313")

    label("loc_329E")


    #C0159
    ChrTalk(
        0xC,
        (
            "克洛斯贝尔今后\x01",
            "肯定还要面临各种\x01",
            "更加严峻的事态吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xC,
        (
            "但只要还有伊莉娅这道光芒存在，\x01",
            "我们就一定能战胜困难。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3313")

    Jump("loc_3A09")

    label("loc_3318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_344D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33DC")

    #C0161
    ChrTalk(
        0xC,
        (
            "对于克洛斯贝尔的广大居民而言，\x01",
            "伊莉娅·普拉提耶就是\x01",
            "如同太阳一般的人物。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xC,
        "她居然受了重伤……\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xC,
        (
            "……不行，没心思工作啊。\x01",
            "伊莉娅小姐到底还能不能重返舞台呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3448")

    label("loc_33DC")


    #C0164
    ChrTalk(
        0xC,
        (
            "听说伊莉娅·普拉提耶\x01",
            "至今都没有恢复意识……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xC,
        (
            "……不行，没心思工作啊。\x01",
            "她到底还能不能重返舞台呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3448")

    Jump("loc_3A09")

    label("loc_344D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_35AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_352C")

    #C0166
    ChrTalk(
        0xC,
        (
            "彩虹剧团的新版舞剧\x01",
            "终于要在明天公演了……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xC,
        (
            "最引人注目的角色自然是\x01",
            "扮演『星之舞姬』的超级新人修利……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xC,
        (
            "我最后还是没拿到票，\x01",
            "不过，克洛斯贝尔时代周刊应该会出特刊吧。\x01",
            "就期待一下好了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_35A5")

    label("loc_352C")


    #C0169
    ChrTalk(
        0xC,
        (
            "彩虹剧团的新版舞剧\x01",
            "终于要在明天公演了……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xC,
        (
            "究竟会是场怎样的演出呢……\x01",
            "真期待克洛斯贝尔时代周刊的\x01",
            "下一期特刊啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35A5")

    Jump("loc_3A09")

    label("loc_35AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_360E")

    #C0171
    ChrTalk(
        0xC,
        "最近很闲呢。\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xC,
        (
            "听说明天又要下雨，\x01",
            "到时就看看彩虹剧团的\x01",
            "资料集来打发时间吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A09")

    label("loc_360E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_373D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36D7")

    #C0173
    ChrTalk(
        0xC,
        (
            "由于与两大国的关系进入紧张状态，\x01",
            "警备队员们似乎相当忙碌。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xC,
        (
            "在这种情况下，\x01",
            "支援科和游击士协会\x01",
            "好像接手了警备队的一些工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xC,
        (
            "希望他们今后也能\x01",
            "在各方面互助协作。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3738")

    label("loc_36D7")


    #C0176
    ChrTalk(
        0xC,
        (
            "支援科和游击士协会\x01",
            "好像接手了警备队的\x01",
            "一些工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xC,
        (
            "希望他们今后也能\x01",
            "在各方面互助协作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3738")

    Jump("loc_3A09")

    label("loc_373D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_38AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3827")

    #C0178
    ChrTalk(
        0xC,
        (
            "恐怖分子的危险性就在于，\x01",
            "他们深信自己是\x01",
            "『正义』的一方。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xC,
        (
            "为了达成目的，不惜做出任何牺牲……\x01",
            "他们丝毫不觉得这有任何错误，\x01",
            "完全就是见鬼的思维模式。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xC,
        (
            "希望警备队的人加把劲，\x01",
            "别让恐怖分子为所欲为。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_38A6")

    label("loc_3827")


    #C0181
    ChrTalk(
        0xC,
        (
            "为了达成目的，不惜做出任何牺牲……\x01",
            "这种见鬼的思维\x01",
            "就是恐怖主义的根源。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xC,
        (
            "希望警备队的人加把劲，\x01",
            "别让恐怖分子为所欲为。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38A6")

    Jump("loc_3A09")

    label("loc_38AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_392E")

    #C0183
    ChrTalk(
        0xC,
        (
            "听说来访克洛斯贝尔的\x01",
            "各国首脑今晚会去观看\x01",
            "彩虹剧团的表演……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xC,
        (
            "这就是国宾的特权吗？\x01",
            "说实话，真是很羡慕啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A09")

    label("loc_392E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3A09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39A9")

    #C0185
    ChrTalk(
        0xC,
        (
            "彩虹剧团的公演\x01",
            "日渐临近……\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xC,
        (
            "听说票的售出速度\x01",
            "十分惊人。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xC,
        "这次又要被迫放弃了吗……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3A09")

    label("loc_39A9")


    #C0188
    ChrTalk(
        0xC,
        (
            "我是伊莉娅·普拉提耶的\x01",
            "忠实支持者……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xC,
        (
            "本想这次一定要去看公演的，\x01",
            "又要被迫放弃了吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A09")

    Jump("loc_3138")

    label("loc_3A0E")

    TalkEnd(0xC)
    Return()

    # Function_15_312B end

    def Function_16_3A12(): pass

    label("Function_16_3A12")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3AA5")

    #C0190
    ChrTalk(
        0xD,
        (
            "没想到竟然在旅行的目的地\x01",
            "赶上了恐怖袭击事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xD,
        (
            "哼，连座城市都保护不了，这种警备队有什么用。\x01",
            "这么危险的地方可不能久留。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BB6")

    label("loc_3AA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3AB3")
    Jump("loc_3BB6")

    label("loc_3AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3AC4")
    Call(0, 8)
    Jump("loc_3BB6")

    label("loc_3AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3AD2")
    Jump("loc_3BB6")

    label("loc_3AD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3B51")

    #C0192
    ChrTalk(
        0xD,
        (
            "今天的正式会议\x01",
            "到底会呈现出怎样的局面呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xD,
        (
            "回到共和国之后，\x01",
            "邮购一本下期的\x01",
            "克洛斯贝尔时代周刊看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BB6")

    label("loc_3B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3B5F")
    Jump("loc_3BB6")

    label("loc_3B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3BB6")

    #C0194
    ChrTalk(
        0xD,
        (
            "一路开车穿过唐古拉姆丘陵，\x01",
            "还真是觉得累了。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xD,
        (
            "好，在食堂\x01",
            "吃点东西吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BB6")

    TalkEnd(0xFE)
    Return()

    # Function_16_3A12 end

    def Function_17_3BBA(): pass

    label("Function_17_3BBA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C30")

    #C0196
    ChrTalk(
        0xE,
        (
            "呜呜，结界\x01",
            "总算消除了，\x01",
            "但没想到还是不能回共和国……\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xE,
        (
            "不管怎么说，我至少要\x01",
            "保护好这孩子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E92")

    label("loc_3C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3CDA")

    #C0198
    ChrTalk(
        0xE,
        (
            "虽然我很同情克洛斯贝尔的人……\x01",
            "但如果有比较正规的军队，\x01",
            "应该可以把损失控制到最低。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xE,
        (
            "看来还是应该接受\x01",
            "总统和『铁血宰相』\x01",
            "在通商会议上提出的提案啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E92")

    label("loc_3CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D54")

    #C0200
    ChrTalk(
        0xE,
        (
            "我的同事去共和国出差，\x01",
            "结果被卷进了列车事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xE,
        (
            "我正要去他住的医院……\x01",
            "不管怎么说，保住了性命就好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E92")

    label("loc_3D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3D62")
    Jump("loc_3E92")

    label("loc_3D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3DE7")

    #C0202
    ChrTalk(
        0xE,
        (
            "我觉得，克洛斯贝尔的居民\x01",
            "会考虑到独立，从某种意义上来说\x01",
            "也是必然的。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xE,
        (
            "只要不影响我的生意，\x01",
            "我就保持旁观态度。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E92")

    label("loc_3DE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3DF8")
    Call(0, 9)
    Jump("loc_3E92")

    label("loc_3DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E06")
    Jump("loc_3E92")

    label("loc_3E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3E92")

    #C0204
    ChrTalk(
        0xE,
        (
            "我是个体杂货商，\x01",
            "这次是来克洛斯贝尔进货的。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xE,
        (
            "克洛斯贝尔是大陆的枢纽，\x01",
            "在这里可以找到各色各样的商品。\x01",
            "呵呵，真让人期待啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E92")

    TalkEnd(0xFE)
    Return()

    # Function_17_3BBA end

    def Function_18_3E96(): pass

    label("Function_18_3E96")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3EF1")

    #C0206
    ChrTalk(
        0xF,
        (
            "爸爸真是的，\x01",
            "情绪也太激动了……\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xF,
        (
            "呵呵呵，不好意思，\x01",
            "不要见怪哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_400C")

    label("loc_3EF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3EFF")
    Jump("loc_400C")

    label("loc_3EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3F0D")
    Jump("loc_400C")

    label("loc_3F0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F83")

    #C0208
    ChrTalk(
        0xF,
        (
            "听说克洛斯贝尔最近\x01",
            "出现了来历不明的\x01",
            "大型魔兽？\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xF,
        (
            "讨厌，真可怕啊……\x01",
            "是不是选错\x01",
            "来旅行的时间了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_400C")

    label("loc_3F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3F91")
    Jump("loc_400C")

    label("loc_3F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4003")

    #C0210
    ChrTalk(
        0xF,
        (
            "我很想见识一下兰花塔，\x01",
            "所以忍不住前来参观。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xF,
        (
            "在揭幕式上已经观赏到了，\x01",
            "差不多也可以回去啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_400C")

    label("loc_4003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_400C")

    label("loc_400C")

    TalkEnd(0xFE)
    Return()

    # Function_18_3E96 end

    def Function_19_4010(): pass

    label("Function_19_4010")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4021")
    Jump("loc_418B")

    label("loc_4021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4049")

    #C0212
    ChrTalk(
        0x10,
        "呼～巴士快点来吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_418B")

    label("loc_4049")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_40E5")

    #C0213
    ChrTalk(
        0x10,
        (
            "说起来，听说昨天\x01",
            "有个假货商老婆婆\x01",
            "在阿尔泰尔市被捕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x10,
        (
            "哎呀，精力那么旺盛，\x01",
            "却从事无良买卖，\x01",
            "从某种意义上说，那个老婆婆也挺可怜呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_418B")

    label("loc_40E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_40F3")
    Jump("loc_418B")

    label("loc_40F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4101")
    Jump("loc_418B")

    label("loc_4101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4182")

    #C0215
    ChrTalk(
        0x10,
        (
            "今天早上，由于实行交通管制，\x01",
            "唐古拉姆丘陵也完全\x01",
            "禁止通行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x10,
        (
            "唉，因为总统要来访问，\x01",
            "这也是没办法的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_418B")

    label("loc_4182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_418B")

    label("loc_418B")

    TalkEnd(0xFE)
    Return()

    # Function_19_4010 end

    def Function_20_418F(): pass

    label("Function_20_418F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_41EA")

    #C0217
    ChrTalk(
        0x11,
        (
            "啊，真是的！\x01",
            "为什么事情\x01",
            "会变成这样啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x11,
        "到底应该怪谁！？你说啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_42FB")

    label("loc_41EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_41F8")
    Jump("loc_42FB")

    label("loc_41F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4206")
    Jump("loc_42FB")

    label("loc_4206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4214")
    Jump("loc_42FB")

    label("loc_4214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_428B")

    #C0219
    ChrTalk(
        0x11,
        (
            "看守大门的队员们\x01",
            "显得有些可怕呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x11,
        (
            "紧张局势什么的和我无关……\x01",
            "难道态度就不能\x01",
            "稍微亲切一点吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42FB")

    label("loc_428B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4299")
    Jump("loc_42FB")

    label("loc_4299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_42A7")
    Jump("loc_42FB")

    label("loc_42A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_42FB")

    #C0221
    ChrTalk(
        0x11,
        (
            "唔，去往克洛斯贝尔市的巴士\x01",
            "要在哪里搭乘呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x11,
        "换乘果然很麻烦啊。\x02",
    )

    CloseMessageWindow()

    label("loc_42FB")

    TalkEnd(0xFE)
    Return()

    # Function_20_418F end

    def Function_21_42FF(): pass

    label("Function_21_42FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_432B")

    #C0223
    ChrTalk(
        0x12,
        (
            "爸爸……\x01",
            "我想回家……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43BA")

    label("loc_432B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4339")
    Jump("loc_43BA")

    label("loc_4339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4347")
    Jump("loc_43BA")

    label("loc_4347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4355")
    Jump("loc_43BA")

    label("loc_4355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4363")
    Jump("loc_43BA")

    label("loc_4363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_43A3")

    #C0224
    ChrTalk(
        0x12,
        (
            "爷爷，\x01",
            "别再说那些听不懂的话啦，\x01",
            "我们吃饭吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43BA")

    label("loc_43A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_43B1")
    Jump("loc_43BA")

    label("loc_43B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_43BA")

    label("loc_43BA")

    TalkEnd(0xFE)
    Return()

    # Function_21_42FF end

    def Function_22_43BE(): pass

    label("Function_22_43BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43D3")
    Call(0, 23)
    Jump("loc_4441")

    label("loc_43D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43E5")
    Call(0, 24)
    Jump("loc_4441")

    label("loc_43E5")


    #C0225
    ChrTalk(
        0xFE,
        (
            "总之……\x01",
            "现在必须集中精力工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "你们应该也有自己的工作，\x01",
            "这边的调查就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4441")

    TalkEnd(0xFE)
    Return()

    # Function_22_43BE end

    def Function_23_4445(): pass

    label("Function_23_4445")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x13, 0x10)
    TurnDirection(0x13, 0x0, 0)
    OP_52(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_44D6")
    Jump("loc_4520")

    label("loc_44D6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_44F6")
    OP_52(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4520")

    label("loc_44F6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4516")
    OP_52(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4520")

    label("loc_4516")

    OP_52(0x13, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4520")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_45D6")
    Jump("loc_4620")

    label("loc_45D6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_45F6")
    OP_52(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4620")

    label("loc_45F6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4616")
    OP_52(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4620")

    label("loc_4616")

    OP_52(0x14, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4620")

    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x14, 0x10)

    #C0227
    ChrTalk(
        0x13,
        "哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x101,
        (
            "#00000F斯克特先生……\x01",
            "你们两位来边境大门了啊。\x02\x03",

            "莫非共和国那边……\x01",
            "或是唐古拉姆丘陵出现了幻兽？\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x14,
        "不，那倒没有。\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x14,
        (
            "就算幻兽出现在\x01",
            "唐古拉姆丘陵一带，\x01",
            "也是属于警备队的管辖范围。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x109,
        (
            "#10100F这倒也是。\x01",
            "……那又是什么原因呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x13,
        (
            "我们正在调查你们昨天消灭了幻兽的地点——\x01",
            "东克洛斯贝尔街道一带。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x13,
        (
            "如果报告中提到的『灵智之草』\x01",
            "真的与幻兽有关，那就必须要\x01",
            "确认一下那种花是否还盛开在其它地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x103,
        (
            "#00200F原来如此……\x01",
            "确实有这个必要。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x104,
        (
            "#00300F凭两位游击士大哥的本领，\x01",
            "应该可以去我们难以进入的\x01",
            "腹地一带探察呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x13,
        "嗯，如你所说。\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x13,
        (
            "总之，这件事就交给我们好了。\x01",
            "你们应该也有别人\x01",
            "无法代劳的工作在身吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrSubChip(0x13, 0x0)
    SetChrSubChip(0x14, 0x0)
    SetScenarioFlags(0x17C, 7)
    Return()

    # Function_23_4445 end

    def Function_24_48D6(): pass

    label("Function_24_48D6")

    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrSubChip(0x13, 0x0)
    SetChrSubChip(0x14, 0x0)

    #C0238
    ChrTalk(
        0x13,
        (
            "话说回来……\x01",
            "自从通商会议之后，\x01",
            "一直闲不下来。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x13,
        (
            "都没什么时间和\x01",
            "未婚妻帕尔见面呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x14,
        "是在百货商店工作的那个女孩吗……\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x14,
        (
            "哎……但这也没办法，\x01",
            "毕竟现在人手不足啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x14,
        (
            "等工作大致告一段落之后，\x01",
            "你就去向米歇尔申请休假吧。\x01",
            "如果需要调整日程，我也会配合你的。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x13,
        (
            "哈哈，谢啦，温蔡尔，\x01",
            "总是承蒙你照顾呢。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x10)
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 3)
    Return()

    # Function_24_48D6 end

    def Function_25_4A32(): pass

    label("Function_25_4A32")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A47")
    Call(0, 23)
    Jump("loc_4AE8")

    label("loc_4A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A59")
    Call(0, 24)
    Jump("loc_4AE8")

    label("loc_4A59")


    #C0244
    ChrTalk(
        0xFE,
        (
            "收到你们的报告之后，我们已经确认过了，\x01",
            "其它的幻兽出现地点\x01",
            "也生长着『灵智之草』。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "……这种植物真是来历不明，\x01",
            "看来还是多加注意为好……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AE8")

    TalkEnd(0xFE)
    Return()

    # Function_25_4A32 end

    def Function_26_4AEC(): pass

    label("Function_26_4AEC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B7A")

    #C0246
    ChrTalk(
        0xFE,
        (
            "市内发生袭击事件的时候，\x01",
            "我还在阿尔摩利卡村。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "联系上家里之后，\x01",
            "得知隆和爸爸\x01",
            "都没事……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        "……总算是放心了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_4BB1")

    label("loc_4B7A")


    #C0249
    ChrTalk(
        0xFE,
        (
            "再稍微过段时间就回家吧。\x01",
            "还是有点担心隆和爸爸……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BB1")

    TalkEnd(0xFE)
    Return()

    # Function_26_4AEC end

    def Function_27_4BB5(): pass

    label("Function_27_4BB5")

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
            "啊，诺艾尔上士，\x01",
            "你和特别任务支援科的各位在一起啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x109,
        "#10100F辛苦了，提马斯先生。\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        (
            "#00000F打扰了，我们今天是\x01",
            "为了工作而来的……\x02",
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
            "将『美食向导』取材一事的\x01",
            "情况做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0254
    ChrTalk(
        0xA,
        (
            "哦，通讯社和我\x01",
            "打过招呼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xA,
        (
            "正好，唐古拉姆门的拿手料理\x01",
            "『芳醇潮锅』刚刚做好。\x01",
            "大家一起吃吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x104,
        (
            "#00305F哦，是这个食堂的\x01",
            "拿手菜鱼火锅啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x102,
        "#00100F呵呵，那就麻烦您了。\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xA,
        (
            "嗯，稍等一下，\x01",
            "我这就给你们盛。\x02",
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
            "罗伊德等人品尝了芳醇潮锅。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0260
    ChrTalk(
        0x103,
        (
            "#00200F（嚼嚼）……\x01",
            "味道很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x101,
        (
            "#00000F是啊，很好地保留了\x01",
            "鱼的原味。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xA,
        "哈哈，是吧？\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xA,
        (
            "火锅制作简单，而且很美味，\x01",
            "唐古拉姆门的人经常吃呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xA,
        (
            "大家围坐在一起，边聊边吃火锅，\x01",
            "又热闹又开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x105,
        (
            "#10304F……说起来，\x01",
            "我和圣书会的成员们都没怎么\x01",
            "像这样围在一起吃过火锅呢。\x02\x03",

            "#10302F呵呵，以后要是有机会，\x01",
            "可以带他们一起过来玩玩。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4FB1():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4FB1)
    Sleep(50)

    def lambda_4FC1():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4FC1)
    Sleep(50)

    def lambda_4FD1():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4FD1)
    Sleep(50)

    def lambda_4FE1():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4FE1)
    Sleep(50)

    def lambda_4FF1():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4FF1)
    Sleep(300)

    #C0266
    ChrTalk(
        0x104,
        (
            "#00305F嘿……\x01",
            "你很少说这种话啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x102,
        (
            "#00102F呵呵，瓦吉好像\x01",
            "很喜欢这道料理呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x103,
        (
            "#00200F既然如此，介绍它的\x01",
            "任务就交给\x01",
            "瓦吉先生好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x1F4)

    #C0269
    ChrTalk(
        0x105,
        (
            "#10304F哎呀呀，虽然很麻烦，\x01",
            "但我就接受了吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x173, 3)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_5104")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_5121")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5121")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_5134")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_5147")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_5164")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_5177")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5177")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_5194")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_51A7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_51A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_51C4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_51C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_51D7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_51D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_51F4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_51F4")

    OP_29(0x80, 0x1, 0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52C9")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0270
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在六家饮食店完成了取材！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52C0")

    #A0271
    AnonymousTalk(
        0x101,
        (
            "#00003F现在就可以去向\x01",
            "格蕾丝小姐报告了……\x02\x03",

            "#00000F不过，还没有把六个人\x01",
            "喜欢的美食全部找到。\x01",
            "不如再努努力吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_52C0")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_52C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_538C")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0272
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "找到了特别任务支援科\x01",
            "全体成员各自喜欢的美食。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0273
    AnonymousTalk(
        0x101,
        (
            "#00000F这样一来，已经找到\x01",
            "所有人喜欢的美食了啊。\x02\x03",

            "取材工作已经足够了，\x01",
            "马上去通讯社报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_538C")

    OP_4C(0xA, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 104640, 0, 1980, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_4BB5 end

    def Function_28_53BC(): pass

    label("Function_28_53BC")

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
        "怎……怎么回事……？\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x9,
        (
            "报、报告！\x01",
            "快报告给道格拉斯副司令！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("e4101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_53BC end

    def Function_29_557A(): pass

    label("Function_29_557A")

    SetChrPos(0xFE, -3500, 0, 0, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -2000, 0, 0)
    OP_9F(0x1, 3500, 0, -4000)
    OP_9F(0x1, 10500, 0, -4000)
    OP_9F(0x1, 25000, 0, -4000)
    OP_9F(0x2, 0xFE, 7000, 0x6)
    Return()

    # Function_29_557A end

    def Function_30_55D1(): pass

    label("Function_30_55D1")

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

    def lambda_568F():
        OP_95(0x101, -21060, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_568F)
    Sleep(30)

    def lambda_56AC():
        OP_95(0x102, -21260, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_56AC)
    Sleep(40)

    def lambda_56C9():
        OP_95(0x104, -21260, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_56C9)
    Sleep(800)

    def lambda_56E6():
        OP_95(0x109, -23560, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_56E6)
    Sleep(30)

    def lambda_5703():
        OP_95(0x103, -23360, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5703)
    Sleep(10)

    def lambda_5720():
        OP_95(0x105, -23360, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5720)
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
        "#00000F那、那是……！\x02",
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
        "怎……怎么回事……？\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x9,
        (
            "报、报告！\x01",
            "快报告给道格拉斯副司令！\x02",
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
        "#00107F啊……\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x104,
        "#00306F让他跑了吗……\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x101,
        (
            "#00003F可恶，那辆运输车上\x01",
            "还装着他骗取的医疗物资……\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x103,
        (
            "#00200F可是……\x01",
            "已经追不上了。\x02\x03",

            "#00206F看来我们迟了一步呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x109,
        (
            "#10108F早知如此，我们真应该\x01",
            "驾驶导力车追过来……\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x105,
        (
            "#10306F哎呀呀，任务失败了呢。\x01",
            "……罗伊德，怎么办？\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        (
            "#00008F……总之，\x01",
            "先联络比利先生他们吧。\x02\x03",

            "#00003F虽然很不甘心……\x01",
            "但还是要把没能抓到犯人的情况\x01",
            "如实报告给他们。\x02",
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
            "罗伊德等人将事情经过\x01",
            "告知给等待在克洛斯贝尔\x01",
            "空港的比利和利卡尔德……\x02",
        )
    )

    CloseMessageWindow()

    #A0287
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，众人与比利一起\x01",
            "前往乌尔斯拉医院，\x01",
            "将情况做了报告。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 2)
    NewScene("t1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_55D1 end

    def Function_31_5BD3(): pass

    label("Function_31_5BD3")

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
            "前方为警备队专用货运路线\x01",
            "    无关人员禁止入内\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_31_5BD3 end

    SaveToFile()

Try(main)
